# 🎙️ Podcast Chatbot — RAG with minsearch + Groq

Ask natural-language questions about your podcast library and get concise,
timestamped answers with YouTube deep links that jump to the exact moment.

---

## 🚀 Setup (4 steps)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a FREE Groq API key
Go to https://console.groq.com → sign up → API Keys → Create Key

### 3. Add your key to `.env`
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

### 4. The .md files containing transcripts are loaded from the `_podcast/` folder

### 5. Run!
```bash
streamlit run streamlit_chatbot.py 
```

---

## 💬 Example

```
You: How does the personalization recommender system work?

🤖 Stefan described it as a "recommender system with an agenda" — like Spotify 
   nudging a heavy metal listener toward country music, gradually moving patients 
   toward healthier behaviors [35:39] → https://youtube.com/watch?v=IDzhmmKeNG4&t=2139
   
   He noted this builds on collaborative filtering but adds a directional goal 
   rather than just "more of the same" [39:57] → https://youtube.com/watch?v=IDzhmmKeNG4&t=2397
```

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `md_parser.py` | Parses your .md files → searchable segments |
| `search_index.py` | Builds minsearch index, runs queries |
| `rag_pipeline.py` | Connects search → Groq LLM → answer |
| `chatbot.py` | Interactive terminal chatbot |
| `.env` | Your Groq API key |

---

## 🗂️ How Your .md Files Are Chunked

Your MD files have two chunking strategies applied simultaneously:

### Strategy A — Header Chunks
Each section header in your transcript becomes one chunk:
```
quotableClips entry:
  name: "Personalization Strategy: Agenda-Driven Recommender Systems"
  startOffset: 2139  ← exact YouTube timestamp
  url: https://youtube.com/watch?v=...&t=2139  ← deep link

→ Chunk contains ALL transcript lines under that header
→ Deep link comes directly from quotableClips (no guessing!)
```
**Best for:** "What did they say about personalization?"

### Strategy B — Sliding Window Chunks
60-second windows with 30-second overlap over all transcript lines:
```
Window 1: lines from 0s → 60s   → link &t=0
Window 2: lines from 30s → 90s  → link &t=30
Window 3: lines from 60s → 120s → link &t=60
```
**Best for:** "What exact step count did they mention?"

Both strategies are searched simultaneously and results are merged + deduplicated.

---

## ⌨️ Chatbot Commands

| Command | Action |
|---------|--------|
| (any text) | Ask a question |
| `/quit` | Exit |

---

## 🔧 Tuning

**Change window size** in `md_parser.py`:
```python
chunk_by_time_window(..., window_seconds=90, step_seconds=45)
```

**Change number of results** in `chatbot.py`:
```python
rag = PodcastRAG(index=index, segments=segments, top_k=7)
```

**Switch Groq model** for better quality:
```python
rag = PodcastRAG(..., model="llama3-70b-8192")   # slower but smarter
```

**Custom episodes directory:**
```bash
python chatbot.py --episodes /path/to/your/md/files
```
