"""
search_index.py
---------------
Builds and queries a minsearch index from podcast segments.

minsearch is a lightweight in-memory search library — no vector DB, 
no embeddings, no setup. It uses TF-IDF style scoring under the hood.

FIELDS WE INDEX:
  text_fields   → full-text search (minsearch tokenizes + scores these)
  keyword_fields → exact-match filters (for filtering by episode/season)

HOW TO USE:
    from search_index import build_index, search
    index = build_index(segments)
    results = search(index, "how does personalization work?")
    results = search(index, "A/B testing", video_id="IDzhmmKeNG4")  # one episode only
"""

import minsearch


def build_index(segments: list[dict]) -> minsearch.Index:
    """
    Builds a minsearch index over all transcript segments.
    
    TEXT FIELDS (searched with TF-IDF scoring):
      - text          : the actual transcript content ← most important
      - section       : section header name (e.g. "Personalization Strategy")
      - episode_title : full episode title
      - short_title   : short episode title
      - speakers      : speaker names (so "what did Stefan say about X" works)
    
    KEYWORD FIELDS (exact-match filters only, not scored):
      - video_id      : filter to one specific episode
      - season        : filter to a season
      - chunk_type    : filter to "header" or "window" chunks
    """
    print("🔍 Building minsearch index …")
    
    index = minsearch.Index(
        text_fields=[
            "text",           # transcript content
            "section",        # section header
            "episode_title",  # full title
            "short_title",    # short title
            "speakers",       # who was speaking
        ],
        keyword_fields=[
            "video_id",       # exact episode filter
            "season",         # season filter
            "chunk_type",     # "header" or "window"
        ],
    )
    
    index.fit(segments)
    print(f"✅ Index ready — {len(segments)} segments indexed")
    return index


def search(
    index,
    query:        str,
    video_id:     str | None = None,   # filter to one episode
    season:       str | None = None,   # filter to one season
    chunk_type:   str | None = None,   # "header" or "window" or None for both
    top_k:        int = 5,
) -> list[dict]:
    """
    Searches the index for segments matching the query.
    
    BOOST WEIGHTS explain what gets scored higher:
      - text ×5     : direct transcript match is most important
      - section ×3  : section header match is very useful
      - episode_title ×1, short_title ×1 : minor boost
      - speakers ×1 : helps with "what did Stefan say about X"
    
    Args:
        query:      Natural language question from the user
        video_id:   If set, only search within this YouTube video ID
        season:     If set, only search within this season number
        chunk_type: "header" = topic-level only, "window" = detail only, None = both
        top_k:      Number of results to return
    
    Returns:
        List of matching segment dicts, best match first
    """
    filter_dict = {}
    if video_id:
        filter_dict["video_id"] = video_id
    if season:
        filter_dict["season"] = str(season)
    if chunk_type:
        filter_dict["chunk_type"] = chunk_type

    results = index.search(
        query       = query,
        filter_dict = filter_dict,
        boost_dict  = {
            "text":          5,
            "section":       3,
            "episode_title": 1,
            "short_title":   1,
            "speakers":      1,
        },
        num_results = top_k,
    )
    
    return results


def deduplicate_results(results: list[dict], min_gap_seconds: int = 30) -> list[dict]:
    """
    Removes near-duplicate results that point to almost the same timestamp.
    
    WHY NEEDED?
    Because we index both header chunks AND window chunks, the same moment 
    in the podcast might appear in multiple results that are only seconds apart.
    This keeps only the "best" (first = highest scored) result per time region.
    
    Args:
        results:         Ranked results from search()
        min_gap_seconds: Results within this many seconds of each other 
                         (in the same episode) are considered duplicates
    
    Returns:
        Deduplicated list, preserving original ranking order
    """
    seen   = []   # list of (video_id, start_seconds) we've kept
    unique = []
    
    for r in results:
        vid   = r.get("video_id", "")
        start = r.get("start_seconds", 0)
        
        # Check if this result is too close to one we already kept
        is_duplicate = any(
            kept_vid == vid and abs(kept_start - start) < min_gap_seconds
            for kept_vid, kept_start in seen
        )
        
        if not is_duplicate:
            unique.append(r)
            seen.append((vid, start))
    
    return unique


# ─────────────────────────────────────────────────────────────
# Quick test
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Fake segments to test without real data
    fake = [
        {
            "chunk_type": "header", "section": "Personalization Strategy",
            "text": "Stefan: We build a recommender system with an agenda to nudge patients towards better habits.",
            "speakers": "Stefan, Alexey", "episode_title": "AI in Healthcare",
            "short_title": "ML Healthcare", "video_id": "IDzhmmKeNG4",
            "season": "8", "episode_num": "4",
            "start_seconds": 2139, "timestamp": "35:39",
            "deep_link": "https://www.youtube.com/watch?v=IDzhmmKeNG4&t=2139",
        },
        {
            "chunk_type": "header", "section": "A/B Testing Foundation",
            "text": "Stefan: A/B testing is the foundation before building collaborative filtering.",
            "speakers": "Stefan, Alexey", "episode_title": "AI in Healthcare",
            "short_title": "ML Healthcare", "video_id": "IDzhmmKeNG4",
            "season": "8", "episode_num": "4",
            "start_seconds": 2397, "timestamp": "39:57",
            "deep_link": "https://www.youtube.com/watch?v=IDzhmmKeNG4&t=2397",
        },
    ]
    
    idx = build_index(fake)
    
    print("\n🔎 Query: 'how does the recommender system work?'")
    for r in search(idx, "how does the recommender system work?"):
        print(f"  [{r['timestamp']}] {r['section']} → {r['text'][:80]}")
        print(f"  🔗 {r['deep_link']}\n")