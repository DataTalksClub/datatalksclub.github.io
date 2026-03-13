"""
chatbot.py
----------
Interactive terminal chatbot for your podcast library.

HOW TO RUN:
    python chatbot.py                        # search all episodes
    python chatbot.py --episodes ./episodes  # custom episodes directory

COMMANDS WHILE CHATTING:
    Any question         → get answer with timestamps + YouTube links
    /episode             → pick a specific episode to search
    /all                 → go back to searching all episodes  
    /list                → show all available episodes
    /debug               → toggle showing retrieved chunks
    /quit                → exit
"""

import os
import sys
import argparse
from dotenv import load_dotenv

# Load .env so GROQ_API_KEY is available before any imports that need it
load_dotenv()

from md_parser import load_all_episodes
from search_index import build_index
from rag_pipeline import PodcastRAG
import re
from rapidfuzz import process, fuzz

def normalize_query(query: str, vocab: set[str]) -> str:
    """
    For each token in query, check if merging it with the next token
    produces a word that exists in the corpus vocabulary.
    Falls back to fuzzy match if exact merge isn't in vocab.
    """
    query = query.lower().strip()
    query = re.sub(r'[^\w\s]', ' ', query)
    query = re.sub(r'\s+', ' ', query)
    
    tokens = query.split()
    merged = []
    i = 0
    
    while i < len(tokens):
        if i + 1 < len(tokens):
            combined = tokens[i] + tokens[i + 1]
            
            if combined in vocab:
                # Exact match in corpus → definitely merge
                merged.append(combined)
                i += 2
                continue
            
            # Fuzzy check: is the combined form close to any vocab word?
            match, score, _ = process.extractOne(
                combined, vocab, scorer=fuzz.ratio
            )
            if score >= 85:  # high confidence it's a split word
                merged.append(match)  # use the actual vocab word
                i += 2
                continue
        
        merged.append(tokens[i])
        i += 1
    
    return " ".join(merged)

# ─────────────────────────────────────────────
# Startup
# ─────────────────────────────────────────────

def startup(episodes_dir: str) -> tuple[PodcastRAG, list[dict]]:
    """Loads episodes, builds index, initializes RAG."""
    print("=" * 60)
    print("  🎙️  Podcast Chatbot  ·  RAG + minsearch + Groq")
    print("=" * 60)
    
    # 1. Parse all .md files
    segments = load_all_episodes(episodes_dir)
    
    if not segments:
        print("\n❌ No segments loaded. Check your episodes directory.")
        raise SystemExit(1)

    # 2. Build minsearch index
    index = build_index(segments)
    
    # 3. Initialize RAG (checks for GROQ_API_KEY here)
    rag = PodcastRAG(index=index, segments=segments)
    
    return rag, segments


# ─────────────────────────────────────────────
# Episode listing & selection
# ─────────────────────────────────────────────

def get_unique_episodes(segments: list[dict]) -> list[dict]:
    """
    Extracts one entry per unique episode from the segments list.
    Returns list of {video_id, episode_title, season, episode_num}
    """
    seen  = set()
    episodes = []
    for s in segments:
        vid = s.get("video_id", "")
        if vid and vid not in seen:
            seen.add(vid)
            episodes.append({
                "video_id":     vid,
                "title":        s.get("episode_title", "Unknown"),
                "season":       s.get("season", ""),
                "episode_num":  s.get("episode_num", ""),
            })
    # Sort by season then episode
    episodes.sort(key=lambda e: (e["season"], e["episode_num"]))
    return episodes


def list_episodes(segments: list[dict]) -> None:
    episodes = get_unique_episodes(segments)
    print(f"\n📺 {len(episodes)} episode(s) in library:")
    print("-" * 55)
    for i, ep in enumerate(episodes, 1):
        label = f"S{ep['season']}E{ep['episode_num']}" if ep["season"] else ""
        print(f"  {i:2d}. [{label}] {ep['title']}")
        print(f"       ID: {ep['video_id']}")
    print()


def select_episode(segments: list[dict]) -> str | None:
    """
    Interactive episode picker.
    Returns a video_id string, or None meaning 'search all episodes'.
    """
    list_episodes(segments)
    choice = input("Enter episode number (or press Enter to search ALL): ").strip()
    
    if not choice:
        return None
    
    try:
        episodes = get_unique_episodes(segments)
        idx = int(choice) - 1
        if 0 <= idx < len(episodes):
            ep = episodes[idx]
            print(f"✅ Now searching: {ep['title']}\n")
            return ep["video_id"]
        else:
            print("⚠️  Invalid number — searching all episodes.\n")
            return None
    except ValueError:
        print("⚠️  Not a number — searching all episodes.\n")
        return None

def build_vocabulary(all_chunks: list[dict]) -> set[str]:
    """Extract all unique words from your indexed chunks."""
    vocab = set()
    for chunk in all_chunks:
        words = re.findall(r'\b\w+\b', chunk["text"].lower())
        vocab.update(words)
    return vocab
# ─────────────────────────────────────────────
# Chat loop
# ─────────────────────────────────────────────

def chat_loop(rag: PodcastRAG, segments: list[dict]) -> None:
    """Main interactive loop."""
    
    video_id_filter = None  # None = search all
    debug_mode      = False
    vocab = build_vocabulary(segments)
    
    print("\n💬 Ask anything about the podcast!")
    print("   Commands: /episode  /all  /list  /debug  /quit")
    print("-" * 55)
    
    # Show what's loaded
    episodes = get_unique_episodes(segments)
    if len(episodes) == 1:
        ep = episodes[0]
        print(f"   Loaded: {ep['title']}")
    else:
        print(f"   Loaded: {len(episodes)} episodes")
    print()
    
    while True:
        
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋  Goodbye!")
            break
        
        if not user_input:
            continue
        
        cmd = user_input.lower()
        user_input = normalize_query(user_input, vocab)
        
        # ── Commands ──────────────────────────────
        
        if cmd in ("/quit", "/exit", "quit", "exit", "q"):
            print("👋  Goodbye!")
            break
        
        elif cmd == "/list":
            list_episodes(segments)
            continue
        
        elif cmd == "/episode":
            video_id_filter = select_episode(segments)
            if not video_id_filter:
                print("🌐 Searching all episodes.\n")
            continue
        
        elif cmd == "/all":
            video_id_filter = None
            print("🌐 Now searching all episodes.\n")
            continue
        
        elif cmd == "/debug":
            debug_mode = not debug_mode
            state = "ON 🟢" if debug_mode else "OFF 🔴"
            print(f"🛠️  Debug mode: {state}\n")
            continue
        
        elif cmd.startswith("/"):
            print("❓ Unknown command. Try: /episode /all /list /debug /quit\n")
            continue
        
        # ── Answer the question ───────────────────
        
        # Show scope
        if video_id_filter:
            scope_ep = next(
                (e for e in get_unique_episodes(segments) if e["video_id"] == video_id_filter),
                None
            )
            scope = scope_ep["title"] if scope_ep else video_id_filter
        else:
            scope = "all episodes"
        
        print(f"\n🔍 Searching [{scope}] …")
        
        answer = rag.ask(
            question        = user_input,
            video_id        = video_id_filter,
            show_debug_info = debug_mode,
        )
        
        print(f"\n🤖  {answer}\n")
        print("-" * 55)


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Podcast RAG Chatbot")
    parser.add_argument(
        "--episodes",
        default="../_podcast/",
        help="Directory containing your .md episode files (default: ./episodes)",
    )
    args = parser.parse_args()
    
    rag, segments = startup(args.episodes)
    chat_loop(rag, segments)


if __name__ == "__main__":
    main()