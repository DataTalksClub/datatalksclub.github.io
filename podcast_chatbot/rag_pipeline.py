"""
rag_pipeline.py
---------------
Connects search results to Groq LLM to generate answers with timestamps.

FLOW:
    question
      → search_index.search()        # find relevant transcript chunks
      → deduplicate_results()        # remove near-duplicate timestamps  
      → build_prompt()               # structure chunks + question for LLM
      → Groq API call                # generate answer
      → formatted answer with links  # returned to user

HOW TO USE:
    from rag_pipeline import PodcastRAG
    rag = PodcastRAG(index, segments)
    print(rag.ask("How does the personalization recommender work?"))
"""

import os
from groq import Groq
from search_index import search, deduplicate_results


class PodcastRAG:
    
    def __init__(
        self,
        index,
        segments:   list[dict],
        model:      str = "llama-3.3-70b-versatile",  # free Groq model
        top_k:      int = 5,
    ):
        """
        Args:
            index:    minsearch index from build_index()
            segments: all transcript segments (kept for metadata reference)
            model:    Groq model name. Free options:
                        "llama3-8b-8192"      ← fast, good quality (recommended)
                        "llama3-70b-8192"     ← slower, better quality
                        "mixtral-8x7b-32768"  ← good for long contexts
            top_k:    how many chunks to retrieve and give to the LLM
        """
        self.index    = index
        self.segments = segments
        self.model    = model
        self.top_k    = top_k
        
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "❌ GROQ_API_KEY not found in environment!\n"
                "   1. Get a FREE key at https://console.groq.com\n"
                "   2. Add to your .env file: GROQ_API_KEY=gsk_xxx...\n"
                "   3. Make sure you called load_dotenv() before creating PodcastRAG"
            )
        self.client = Groq(api_key=api_key)
        print(f"✅ PodcastRAG ready | model={self.model} | top_k={self.top_k}")


    # ──────────────────────────────────────────────
    # A: Retrieve
    # ──────────────────────────────────────────────

    def retrieve(
        self,
        question:   str,
        video_id:   str | None = None,
        season:     str | None = None,
    ) -> list[dict]:
        """
        Searches the index and returns deduplicated top-k chunks.
        
        We run TWO searches and merge:
          1. Header chunks only  → good for topic-level answers
          2. Window chunks only  → good for specific detail answers
        
        Merging both gives the LLM richer context.
        """
        # Search header chunks (higher weight — these are cleaner)
        header_results = search(
            self.index, question,
            video_id=video_id, season=season,
            chunk_type="header",
            top_k=self.top_k,
        )
        
        # Search window chunks (catches details not in headers)
        window_results = search(
            self.index, question,
            video_id=video_id, season=season,
            chunk_type="window",
            top_k=self.top_k,
        )
        
        # Interleave: header[0], window[0], header[1], window[1], ...
        # This ensures we get a mix rather than all headers first
        merged = []
        for h, w in zip(header_results, window_results):
            merged.append(h)
            merged.append(w)
        # Add any leftovers
        merged.extend(header_results[len(window_results):])
        merged.extend(window_results[len(header_results):])
        
        # Remove results that point to almost the same timestamp
        unique = deduplicate_results(merged, min_gap_seconds=30)
        
        # Keep top_k after dedup
        return unique[:self.top_k]


    # ──────────────────────────────────────────────
    # B: Build Prompt
    # ──────────────────────────────────────────────

    def build_prompt(self, question: str, chunks: list[dict]) -> str:
        """
        Formats retrieved chunks into a prompt for the LLM.
        
        The prompt gives the LLM:
          - A clear role (podcast assistant)
          - The numbered context chunks with timestamps and links
          - Strict rules to cite timestamps and never make things up
          - The user's question
        """
        context_blocks = []
        
        for i, chunk in enumerate(chunks, 1):
            # Format each chunk as a labeled block
            block = (
                f"[Context {i}]\n"
                f"Episode  : {chunk.get('episode_title', 'Unknown')}\n"
                f"Section  : {chunk.get('section', '')}\n"
                f"Timestamp: {chunk.get('timestamp', '')}  "
                    f"(second {chunk.get('start_seconds', 0)})\n"
                f"Link     : {chunk.get('deep_link', '')}\n"
                f"Speakers : {chunk.get('speakers', '')}\n"
                f"Content  : {chunk.get('text', '')}\n"
            )
            context_blocks.append(block)
        
        context = "\n---\n".join(context_blocks)
        
        prompt = f"""You are a helpful podcast assistant. You answer questions about podcast episodes
using ONLY the transcript excerpts provided below. You never invent information.

ANSWER FORMAT RULES:
1. Give a concise answer in 2-4 sentences.
2. After each factual claim, cite the source like this:
     [MM:SS] → <YouTube link>
   Example: Stefan explained this using a Spotify analogy [35:39] → https://youtube.com/...&t=2139
3. If multiple excerpts support the answer, cite all of them.
4. Mention the speaker's name (Stefan, Alexey, etc.) when attributing a statement.
5. If the answer is NOT found in any excerpt below, respond exactly:
   "I couldn't find that in the available transcripts. Try rephrasing or asking about a different topic."
6. NEVER make up timestamps, links, or facts.

════════════════════════════════════════
TRANSCRIPT EXCERPTS:
{context}
════════════════════════════════════════

QUESTION: {question}

ANSWER:"""
        
        return prompt


    # ──────────────────────────────────────────────
    # C: Generate with Groq
    # ──────────────────────────────────────────────

    def generate(self, prompt: str) -> str:
        """
        Calls the Groq API with the assembled prompt.
        Plain API call — no frameworks, just HTTP.
        """
        response = self.client.chat.completions.create(
            model    = self.model,
            messages = [{"role": "user", "content": prompt}],
            temperature = 0.2,   # low temperature = factual, not creative
            max_tokens  = 600,
        )
        return response.choices[0].message.content.strip()


    # ──────────────────────────────────────────────
    # D: Full pipeline
    # ──────────────────────────────────────────────

    def ask(
        self,
        question:        str,
        video_id:        str | None = None,
        season:          str | None = None,
        show_debug_info: bool       = False,
    ) -> str:
        """
        Main method — runs the full RAG pipeline.
        
        Args:
            question:        User's natural-language question
            video_id:        Optional — restrict to one YouTube video ID
            season:          Optional — restrict to one season number
            show_debug_info: Print retrieved chunks (useful while building)
        
        Returns:
            Formatted answer string with timestamps and YouTube deep links
        """
        # Step 1: Retrieve
        chunks = self.retrieve(question, video_id=video_id, season=season)
        
        if not chunks:
            return (
                "❌ No relevant transcript segments found.\n"
                "   Try rephrasing your question or check that the episode "
                "transcripts are loaded correctly."
            )
        
        # Optional debug view
        if show_debug_info:
            print(f"\n📚 Retrieved {len(chunks)} chunks:")
            for c in chunks:
                print(
                    f"  [{c['timestamp']}] [{c['chunk_type']:6s}] "
                    f"{c['section'][:50]} | {c['text'][:60]}…"
                )
            print()
        
        # Step 2: Build prompt
        prompt = self.build_prompt(question, chunks)
        
        # Step 3: Generate
        answer = self.generate(prompt)
        
        return answer