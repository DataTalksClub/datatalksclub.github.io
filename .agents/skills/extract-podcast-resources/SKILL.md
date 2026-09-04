---
name: extract-podcast-resources
description: Extract the resources (tools, books, papers, people, companies, etc.) mentioned in a DataTalksClub podcast episode transcript and add them to the episode page. Use when a new podcast episode needs its "Resources Mentioned" section, or when asked to extract/backfill podcast resources.
argument-hint: [episode-slug-or-path]
---

# Extract Podcast Resources

You extract the resources **yourself, in-context** — read the transcript, identify
the resources, write the result. Do **not** dispatch subagents and do **not** call
any LLM API; this is your job as the agent.

Repo: this repository (website root). The mechanical steps (YouTube fetching,
front-matter merging) are done by `scripts/extract_podcast_resources.py`; the
extraction judgment is yours.

## Workflow

1. **Find the episode**: `_podcast/<slug>.md` in the website repo.
2. **Get the transcript**:
   - Normally it is in the episode front matter under `transcript:` (list of
     `header` / `who`+`line` entries). Read the file and use that.
   - If it is missing or near-empty: make sure the front matter has
     `ids.youtube`, then run
     `uv run python scripts/extract_podcast_resources.py --fetch-transcripts --file <slug>`
     from the repo root. It caches raw captions to
     `scripts/data/youtube_transcripts/<video-id>.txt` (Oxylabs proxy from
     `~/.config/youtube/.env` is used automatically). Read the cached file.
   - Long episodes: read the transcript in chunks with the Read tool
     (`offset`/`limit`) and collect resources as you go.
3. **Extract the resources yourself** following the rules below.
4. **Write** `scripts/data/podcast_resources/<slug>.json`:

   ```json
   {
     "slug": "<slug>",
     "resources": [
       {"name": "Feast", "type": "tool", "url": "https://feast.dev",
        "context": "open-source feature store discussed in depth"},
       {"name": "Designing Machine Learning Systems", "type": "book",
        "context": "recommended by the guest"}
     ]
   }
   ```

5. **Merge into the episode page**:
   `uv run python scripts/extract_podcast_resources.py --merge --file <slug>`
   (idempotent; normalizes and dedupes what you wrote).
6. Build (`~/git/datatalksclub.github.io/.bin/rustkyll build`) and check the
   Resources tab on the episode page. Commit.

## What counts as a resource

Concrete, identifiable entities **actually mentioned in the transcript**:

| Type | Examples |
|------|----------|
| `tool` | software tools, libraries, frameworks, platforms, languages (dbt, Feast, Kubernetes, Python) |
| `book` | books with a specific title |
| `paper` | research papers, publications |
| `course` | courses, tutorials, MOOCs |
| `person` | public figures (authors, researchers, bloggers), **not** the host or guests |
| `company` | companies/organizations discussed as entities (Databricks, Netflix) |
| `community` | communities, conferences, meetups (PyData, MLOps Community) |
| `dataset` | named datasets |
| `service` | hosted services / SaaS (Snowflake, OpenAI API) |
| `other` | blogs, newsletters, podcasts, websites, reports |

## Rules

- Only what is **actually said** in the transcript — never add related resources
  from your own knowledge.
- Normalize names to official casing/spelling ("scikit-learn", "GitHub",
  "PyTorch", "dbt"); merge spelling variants into one entry. Fix obvious
  speech-to-text garbles when the referent is unambiguous ("Psychic Learn" →
  scikit-learn); skip garbles you cannot identify rather than guessing.
- `url` only if you are confident about the official domain (homepage for
  tools, arXiv/DOI for papers, official page for books). Omit the field
  entirely rather than guessing.
- `context`: one short phrase (≤ ~12 words) on how it came up in this episode.
- Skip the podcast itself, the host, the guests, and trivia. Typically 10–30
  entries, most important first, hard max 40. One entry per unique resource.
- Small lists are fine — a resource-light episode gets a short list; never pad.
