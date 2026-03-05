"""
streamlit_app.py
----------------
Streamlit UI for the Podcast RAG Chatbot.

HOW TO RUN:
    streamlit run streamlit_app.py
    streamlit run streamlit_app.py -- --episodes ../path/to/episodes
"""

import os
import re
import streamlit as st
from dotenv import load_dotenv
from rapidfuzz import process, fuzz

load_dotenv()

from md_parser import load_all_episodes
from search_index import build_index
from rag_pipeline import PodcastRAG

# ─────────────────────────────────────────────
# Page config (must be first Streamlit call)
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="🎙️ Podcast Chatbot",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Syne', sans-serif;
    }

    /* Dark background */
    .stApp {
        background-color: #0d0d0d;
        color: #f0ece4;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #2a2a2a;
    }
    [data-testid="stSidebar"] * {
        color: #c9c3bb !important;
    }

    /* Header */
    .chatbot-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .chatbot-header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #f0ece4 0%, #ff6b35 60%, #f0ece4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .chatbot-header p {
        color: #666;
        font-size: 0.95rem;
        margin-top: 0.3rem;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Chat messages */
    .user-bubble {
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 16px 16px 4px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        margin-left: 15%;
        color: #f0ece4;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .bot-bubble {
        background: #141414;
        border: 1px solid #ff6b35;
        border-left: 3px solid #ff6b35;
        border-radius: 4px 16px 16px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        margin-right: 15%;
        color: #f0ece4;
        font-size: 0.95rem;
        line-height: 1.7;
    }
    .bot-bubble a {
        color: #ff6b35;
        text-decoration: none;
        border-bottom: 1px solid #ff6b3550;
    }
    .bot-bubble a:hover {
        border-bottom-color: #ff6b35;
    }
    .label-user {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        color: #555;
        text-align: right;
        margin-bottom: 0.2rem;
        margin-right: 0.3rem;
    }
    .label-bot {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        color: #ff6b35;
        margin-bottom: 0.2rem;
        margin-left: 0.3rem;
    }

    /* Input area */
    .stTextInput input {
        background-color: #1a1a1a !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 12px !important;
        color: #f0ece4 !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 0.8rem 1rem !important;
    }
    .stTextInput input:focus {
        border-color: #ff6b35 !important;
        box-shadow: 0 0 0 2px #ff6b3520 !important;
    }

    /* Buttons */
    .stButton > button {
        background: #ff6b35 !important;
        color: #0d0d0d !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 1.2rem !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        background: #e55a27 !important;
        transform: translateY(-1px);
    }

    /* Episode card in sidebar */
    .episode-card {
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        margin: 0.3rem 0;
        font-size: 0.82rem;
        cursor: pointer;
        transition: border-color 0.2s;
    }
    .episode-card:hover {
        border-color: #ff6b35;
    }
    .episode-card.active {
        border-color: #ff6b35;
        background: #1f1510;
    }
    .episode-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        color: #ff6b35;
        margin-bottom: 0.2rem;
    }

    /* Status badges */
    .badge {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        color: #888;
    }
    .badge-active {
        border-color: #ff6b35;
        color: #ff6b35;
        background: #1f1510;
    }

    /* Thinking indicator */
    .thinking {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #ff6b35;
        padding: 0.5rem 0;
    }

    /* Divider */
    hr {
        border-color: #2a2a2a !important;
        margin: 1rem 0 !important;
    }

    /* Hide Streamlit branding */
    #MainMenu, footer, header { visibility: hidden; }

    /* Scrollable chat area */
    .chat-container {
        max-height: 60vh;
        overflow-y: auto;
        padding-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def build_vocabulary(all_chunks: list[dict]) -> set[str]:
    vocab = set()
    for chunk in all_chunks:
        words = re.findall(r'\b\w+\b', chunk["text"].lower())
        vocab.update(words)
    return vocab


def normalize_query(query: str, vocab: set[str]) -> str:
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
                merged.append(combined)
                i += 2
                continue
            result = process.extractOne(combined, vocab, scorer=fuzz.ratio)
            if result and result[1] >= 85:
                merged.append(result[0])
                i += 2
                continue
        merged.append(tokens[i])
        i += 1
    return " ".join(merged)


def get_unique_episodes(segments: list[dict]) -> list[dict]:
    seen, episodes = set(), []
    for s in segments:
        vid = s.get("video_id", "")
        if vid and vid not in seen:
            seen.add(vid)
            episodes.append({
                "video_id":    vid,
                "title":       s.get("episode_title", "Unknown"),
                "season":      s.get("season", ""),
                "episode_num": s.get("episode_num", ""),
            })
    episodes.sort(key=lambda e: (e["season"], e["episode_num"]))
    return episodes


# ─────────────────────────────────────────────
# Cached startup (runs once)
# ─────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_resources(episodes_dir: str):
    segments = load_all_episodes(episodes_dir)
    index    = build_index(segments)
    rag      = PodcastRAG(index=index, segments=segments)
    vocab    = build_vocabulary(segments)
    return rag, segments, vocab


# ─────────────────────────────────────────────
# Session state defaults
# ─────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []          # [{role, content}]
if "video_id_filter" not in st.session_state:
    st.session_state.video_id_filter = None # None = all episodes
if "debug_mode" not in st.session_state:
    st.session_state.debug_mode = False


# ─────────────────────────────────────────────
# Load resources
# ─────────────────────────────────────────────

EPISODES_DIR = os.environ.get("EPISODES_DIR", "../_podcast/")

with st.spinner("🎙️ Loading episodes…"):
    try:
        rag, segments, vocab = load_resources(EPISODES_DIR)
        episodes = get_unique_episodes(segments)
        load_error = None
    except Exception as e:
        load_error = str(e)
        rag = segments = vocab = episodes = None

if load_error:
    st.error(f"❌ Failed to load episodes: {load_error}")
    st.stop()


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("### 🎙️ Podcast Chatbot")
    st.markdown(f"<span class='badge'>RAG · minsearch · Groq</span>", unsafe_allow_html=True)
    st.markdown("---")

    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown(f"<span style='font-size:0.75rem;color:#444;font-family:monospace'>{len(segments):,} chunks indexed</span>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Main area
# ─────────────────────────────────────────────

st.markdown("""
<div class='chatbot-header'>
    <h1>🎙️ Podcast Chatbot</h1>
    <p>Ask anything · get answers with timestamps + YouTube links</p>
</div>
""", unsafe_allow_html=True)

# Render chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='label-user'>you</div><div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='label-bot'>🤖 podcast bot</div><div class='bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# Input
st.markdown("---")
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        label="Ask a question",
        placeholder="e.g. How do I become a freelancer in data?",
        label_visibility="collapsed",
        key="chat_input",
    )
with col2:
    send = st.button("Send →", use_container_width=True)

# Handle send
if send and user_input.strip():
    raw_query   = user_input.strip()
    clean_query = normalize_query(raw_query, vocab)

    # Determine scope label
    if st.session_state.video_id_filter:
        active_ep  = next((e for e in episodes if e["video_id"] == st.session_state.video_id_filter), None)
        scope_label = active_ep["title"] if active_ep else st.session_state.video_id_filter
    else:
        scope_label = "all episodes"

    # Save user message
    st.session_state.messages.append({"role": "user", "content": raw_query})
    st.markdown(f"<div class='label-user'>you</div><div class='user-bubble'>{raw_query}</div>", unsafe_allow_html=True)

    # Generate answer
    with st.spinner(f"🔍 Searching [{scope_label}]…"):
        answer = rag.ask(
            question        = clean_query,
            video_id        = st.session_state.video_id_filter,
            show_debug_info = st.session_state.debug_mode,
        )

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.markdown(f"<div class='label-bot'>🤖 podcast bot</div><div class='bot-bubble'>{answer}</div>", unsafe_allow_html=True)

    # Show normalized query if different
    if clean_query != raw_query.lower() and st.session_state.debug_mode:
        st.caption(f"🔧 Query normalized: `{raw_query}` → `{clean_query}`")

# Empty state
if not st.session_state.messages:
    st.markdown("""
    <div style='text-align:center;padding:3rem;color:#333;'>
        <div style='font-size:3rem;margin-bottom:1rem'>🎙️</div>
        <div style='font-family:monospace;font-size:0.85rem'>
            Ask about topics, guests, career advice, tools, or anything discussed in the podcasts.
        </div>
    </div>
    """, unsafe_allow_html=True)