# Podcast "Resources Mentioned" — how it works and how to run it

Every podcast episode page has a **Resources** tab listing tools, books, papers,
people, companies, and other resources mentioned in the episode. The list is
generated from the episode transcript with AI and stored in the episode's front
matter under the `resources` key.

This document describes the full pipeline so new episodes can be processed the
same way.

## Pipeline overview

```
_podcast/<episode>.md            episode page; `transcript` lives in front matter
        │  (transcript missing?)
        ▼
scripts/data/youtube_transcripts/<video-id>.txt
                                 raw transcripts fetched from YouTube,
                                 cached separately (never committed into _podcast)
        │
        ▼  LLM extraction (one call per ~45k chars of transcript)
scripts/data/podcast_resources/<slug>.json
                                 per-episode extraction results, kept for review
        │  --merge
        ▼
_podcast/<episode>.md            gains a `resources:` block in its front matter
        │
        ▼  site build
Resources tab on /podcast/<episode>.html (+ schema.org "mentions" in JSON-LD)
```

Everything AI-generated that is *not* episode content lives in
`scripts/data/` — raw YouTube transcript caches in
`youtube_transcripts/`, extraction results in `podcast_resources/`.

## The tool

`scripts/extract_podcast_resources.py` does all three steps:

```bash
# 1. Fetch missing transcripts from YouTube (needs youtube-transcript-api;
#    uses Oxylabs proxy from ~/.config/youtube/.env automatically if set)
uv run python scripts/extract_podcast_resources.py --fetch-transcripts

# 2. Extract resources with an LLM for episodes that have no result yet
uv run python scripts/extract_podcast_resources.py --extract
#    options: --limit N, --force (redo existing), --file <slug> (one episode)

# 3. Write the saved results into the episode front matter
uv run python scripts/extract_podcast_resources.py --merge
```

Each step is idempotent and safe to re-run. `--fetch-transcripts` and
`--extract` skip anything already cached/extracted; `--merge` replaces the
`resources:` block in front matter with what the JSON says (and normalizes it).

### LLM configuration (step 2)

Any OpenAI-compatible endpoint works. Environment variables:

| Variable            | Meaning                                             | Default     |
|---------------------|-----------------------------------------------------|-------------|
| `OPENAI_API_KEY`    | API key (required for `--extract`)                  | —           |
| `OPENAI_BASE_URL`   | Point at a non-OpenAI OpenAI-compatible API         | OpenAI      |
| `RESOURCES_LLM_MODEL` | Model name                                        | `gpt-5-mini` |

Long transcripts are split into ~45k-char chunks at line boundaries, extracted
separately, then deduplicated by normalized name.

### YouTube fetching

Transcripts are fetched with [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
using the video id from the episode's `ids.youtube` front matter key. Raw
captions ("0:12 some words" lines) are cached to
`scripts/data/youtube_transcripts/<video-id>.txt`.

YouTube blocks datacenter IPs ("LOGIN_REQUIRED"). The script automatically
retries through an Oxylabs proxy when `~/.config/youtube/.env` contains:

```
OXYLABS_USER=...
OXYLABS_ENDPOINT=...
OXYLABS_PASSWORD=...
```

## What counts as a resource

The extraction prompt (see `PROMPT` in the script) asks for **concrete,
identifiable entities actually mentioned in the transcript**:

| Type        | Examples |
|-------------|----------|
| `tool`      | dbt, Feast, Kubernetes, Python |
| `book`      | "Designing Machine Learning Systems" |
| `paper`     | research papers, publications |
| `course`    | courses, tutorials, MOOCs |
| `person`    | public figures other than the host and guests |
| `company`   | Databricks, Netflix |
| `community` | PyData, MLOps Community |
| `dataset`   | named datasets |
| `service`   | Snowflake, OpenAI API |
| `other`     | blogs, newsletters, podcasts, websites, reports |

Rules applied to every entry:

- names normalized to official casing/spelling ("scikit-learn", "dbt");
  spelling variants merged into one entry
- `url` only when the official domain is certain — otherwise omitted, never guessed
- `context` is one short phrase (≤ ~12 words) about how it came up
- host, guests, and the podcast itself are excluded
- typically 10–30 entries per episode, hard max 40, most important first

Result JSON format (`scripts/data/podcast_resources/<slug>.json`):

```json
{
  "slug": "mlops-feature-stores-feature-stores-feast-tecton",
  "resources": [
    {"name": "Feast", "type": "tool", "url": "https://feast.dev",
     "context": "open-source feature store discussed in depth"},
    {"name": "Trustworthy Online Controlled Experiments", "type": "book",
     "context": "recommended by the guest"}
  ]
}
```

## Front matter format

`--merge` appends/updates a `resources:` block in the episode's YAML front
matter (the block sits after `transcript:`):

```yaml
resources:
- name: Feast
  type: tool
  url: https://feast.dev
  context: open-source feature store discussed in depth
```

## Rendering

`_layouts/podcast.html` adds a **Resources** tab (between Show Notes and
Timestamps) when `page.resources` exists. Each entry renders as a type badge +
name (linked when a url is present) + context, plus a disclaimer that the list
is AI-generated. Styles are in `assets/styles.css` (`.resources-list`,
`.resource-type--*`, with `.dark` variants). The JSON-LD on the page also gets
a `mentions` array built from the same data.

## Processing new episodes (runbook)

For each new episode file in `_podcast/`:

1. Make sure the episode has `ids.youtube` in front matter if the transcript
   key is missing or empty.
2. `uv run python scripts/extract_podcast_resources.py --fetch-transcripts`
3. `OPENAI_API_KEY=... uv run python scripts/extract_podcast_resources.py --extract --file <slug>`
4. Review `scripts/data/podcast_resources/<slug>.json` (spot-check names/URLs).
5. `uv run python scripts/extract_podcast_resources.py --merge --file <slug>`
6. Build the site and check the Resources tab on the episode page.

## How the initial backfill was done (for reference)

When the feature was first built there was no usable LLM API key, so the
extraction step for the backfill was done by AI coding agents instead of the
API: transcripts were flattened to `/tmp/podcast_tx/<slug>.txt`
(`header`/`who`/`line` entries only), split into batches of ~5 episodes, and
each batch was given to an agent with the same rules as the `PROMPT` in the
script, writing the result JSONs to `scripts/data/podcast_resources/`. The
`--merge` step and everything after is identical. Running `--extract` with an
API key reproduces the same output shape, so new episodes don't need agents.
