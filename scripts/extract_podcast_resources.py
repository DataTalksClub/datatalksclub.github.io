#!/usr/bin/env python3
"""
Extract resources mentioned in podcast episodes and add them to episode pages.

For every episode in _podcast/ this script:

1. Collects the transcript text - either from the `transcript` front matter key,
   or from a raw YouTube transcript cached in scripts/data/youtube_transcripts/.
   Missing transcripts can be fetched from YouTube with --fetch-transcripts
   (requires the youtube-transcript-api package; Oxylabs proxy credentials from
   ~/.config/youtube/.env are used automatically when YouTube blocks the IP).
2. Asks an LLM to extract the mentioned resources (tools, books, papers, courses,
   people, companies, communities, datasets, services). The LLM is any
   OpenAI-compatible endpoint configured via OPENAI_API_KEY and optionally
   OPENAI_BASE_URL / RESOURCES_LLM_MODEL (default: gpt-5-mini, like the other
   scripts in this folder).
3. Saves the extraction result to scripts/data/podcast_resources/<slug>.json
   so results can be reviewed and re-merged without re-running the LLM.
4. With --merge, writes the saved results into the `resources` front matter key
   of each episode page, rendered by the "Resources" tab in _layouts/podcast.html.

Usage:
    # fetch missing transcripts from YouTube into the cache directory
    python scripts/extract_podcast_resources.py --fetch-transcripts

    # run the LLM extraction for episodes that have no saved result yet
    python scripts/extract_podcast_resources.py --extract
    python scripts/extract_podcast_resources.py --extract --limit 5 --force

    # write saved results into the episode front matter
    python scripts/extract_podcast_resources.py --merge
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import yaml
import frontmatter

ROOT = Path(__file__).resolve().parent.parent
PODCAST_DIR = ROOT / '_podcast'
# Raw YouTube transcripts live in a separate place, away from the content collections.
YOUTUBE_CACHE_DIR = ROOT / 'scripts' / 'data' / 'youtube_transcripts'
# Per-episode LLM extraction results (JSON), also kept outside the content collections.
RESOURCES_DATA_DIR = ROOT / 'scripts' / 'data' / 'podcast_resources'

MAX_CHUNK_CHARS = 45000
MAX_RESOURCES = 40

RESOURCE_TYPES = [
    'tool', 'book', 'paper', 'course', 'person',
    'company', 'community', 'dataset', 'service', 'other',
]

PROMPT = """You are an editor for the DataTalks.Club podcast. Below is the transcript of an episode. Extract every external resource mentioned in it.

A resource is a concrete, identifiable entity of one of these types:
- tool: software tools, libraries, frameworks, platforms, languages (e.g. dbt, Feast, Kubernetes, Python)
- book: books with a specific title
- paper: research papers or publications
- course: courses, tutorials, MOOCs
- person: public figures (authors, researchers, bloggers) relevant to the field, other than the host and the guest
- company: companies or organizations discussed as entities (e.g. Databricks, Netflix)
- community: communities, conferences, meetups (e.g. PyData, MLOps Community)
- dataset: named datasets
- service: hosted services or SaaS products (e.g. Snowflake, OpenAI API)
- other: other noteworthy references (blogs, newsletters, podcasts, websites, reports)

Rules:
- Include only resources actually mentioned in the transcript, not related ones you think of yourself.
- Normalize names to their official casing and spelling (e.g. "scikit-learn", "GitHub", "PyTorch", "dbt"). Merge spelling variants into one entry.
- For "url" give the official domain ONLY if you are confident about it (homepage for tools, publisher/Goodreads-free official page for books, arXiv/DOI for papers). Otherwise omit the url field entirely - never guess.
- "context" is one short phrase (max 12 words) about how it came up in this episode.
- Skip the podcast itself, its host, its guests, and generic phrases.
- Prefer substance: keep everything meaningfully referenced, but do not inflate the list with trivia. At most {max_resources} entries, most important first.

Return STRICT JSON only, no markdown:
{{"resources": [{{"name": "...", "type": "tool", "url": "https://...", "context": "..."}}]}}

Episode transcript:

{transcript}"""


def episode_files():
    for path in sorted(PODCAST_DIR.glob('*.md')):
        if path.name.startswith('_'):
            continue
        yield path


def transcript_text_from_front_matter(fm):
    """Flatten the structured transcript into readable text."""
    parts = []
    for entry in fm.get('transcript') or []:
        if entry.get('header'):
            parts.append('## ' + entry['header'])
        elif entry.get('line'):
            who = entry.get('who') or 'Speaker'
            parts.append(f'{who}: {entry["line"]}')
    return '\n'.join(parts)


def youtube_id_of(fm):
    ids = fm.get('ids') or {}
    yt = ids.get('youtube')
    if not yt or yt == 'TODO':
        return None
    return yt


def load_cached_youtube_transcript(video_id):
    path = YOUTUBE_CACHE_DIR / f'{video_id}.txt'
    if not path.exists():
        return None
    lines = []
    for line in path.read_text(encoding='utf-8').splitlines():
        # raw captions look like "1:23 some words" or "1:02:03 some words"
        line = re.sub(r'^\d+:\d\d(:\d\d)?\s+', '', line.strip())
        if line:
            lines.append(line)
    return '\n'.join(lines)


def fetch_youtube_transcript(video_id):
    """Fetch a transcript from YouTube, saving it to the cache directory."""
    from youtube_transcript_api import YouTubeTranscriptApi

    proxies = None
    env_file = Path(os.path.expanduser('~/.config/youtube/.env'))
    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
        except ImportError:
            pass
    user = os.getenv('OXYLABS_USER')
    password = os.getenv('OXYLABS_PASSWORD')
    endpoint = os.getenv('OXYLABS_ENDPOINT')
    if user and password and endpoint:
        proxies = {
            'http': f'http://{user}-sessid-1:{password}@{endpoint}',
            'https': f'http://{user}-sessid-1:{password}@{endpoint}',
        }

    api = YouTubeTranscriptApi(proxy_config=proxies) if proxies else YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=['en', 'en-US', 'en-GB'])
    lines = [f'{s.start:.0f}s {s.text}' for s in fetched]

    YOUTUBE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = YOUTUBE_CACHE_DIR / f'{video_id}.txt'
    cache_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'  cached youtube transcript to {cache_path}')
    return load_cached_youtube_transcript(video_id)


def episode_transcript(fm, fetch=False):
    """Return the transcript text for an episode, or None if unavailable."""
    text = transcript_text_from_front_matter(fm)
    if len(text) >= 500:
        return text

    video_id = youtube_id_of(fm)
    if not video_id:
        return None

    text = load_cached_youtube_transcript(video_id)
    if text and len(text) >= 500:
        return text

    if fetch:
        try:
            return fetch_youtube_transcript(video_id)
        except Exception as e:
            print(f'  failed to fetch youtube transcript {video_id}: {e}')
    return None


def chunk_text(text, max_chars=MAX_CHUNK_CHARS):
    chunks = []
    while len(text) > max_chars:
        cut = text.rfind('\n', max_chars // 2, max_chars)
        if cut == -1:
            cut = max_chars
        chunks.append(text[:cut])
        text = text[cut:]
    chunks.append(text)
    return chunks


def call_llm(transcript, api_key):
    from openai import OpenAI

    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv('OPENAI_BASE_URL') or None,
    )
    model = os.getenv('RESOURCES_LLM_MODEL', 'gpt-5-mini')
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role': 'system',
                'content': (
                    'You extract structured metadata from podcast transcripts. '
                    'You answer with strict JSON only.'
                ),
            },
            {'role': 'user', 'content': transcript},
        ],
    )
    return response.choices[0].message.content


def parse_llm_json(raw):
    raw = raw.strip()
    if raw.startswith('```'):
        raw = re.sub(r'^```(json)?\s*', '', raw)
        raw = re.sub(r'\s*```$', '', raw)
    data = json.loads(raw)
    return data.get('resources', [])


def normalize_resources(items):
    """Validate, clean and deduplicate an extraction result."""
    seen = {}
    for item in items:
        name = (item.get('name') or '').strip()
        if not name or len(name) > 120:
            continue
        rtype = (item.get('type') or 'other').strip().lower()
        if rtype not in RESOURCE_TYPES:
            rtype = 'other'
        url = (item.get('url') or '').strip()
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        if url and '.' not in url:
            url = ''
        context = (item.get('context') or '').strip().rstrip('.')
        if len(context) > 140:
            context = context[:137] + '...'

        key = re.sub(r'[^a-z0-9]', '', name.lower())
        if key in seen:
            if url and not seen[key].get('url'):
                seen[key]['url'] = url
            continue
        entry = {'name': name, 'type': rtype, 'context': context}
        if url:
            entry['url'] = url
        seen[key] = entry
    return list(seen.values())[:MAX_RESOURCES]


def extract_for_episode(path, fetch=False, force=False, api_key=None):
    slug = path.stem
    out_path = RESOURCES_DATA_DIR / f'{slug}.json'
    if out_path.exists() and not force:
        return 'skipped'

    post = frontmatter.load(path)
    transcript = episode_transcript(post.metadata, fetch=fetch)
    if transcript is None:
        return 'no-transcript'

    resources = []
    for chunk in chunk_text(transcript):
        prompt = PROMPT.format(transcript=chunk, max_resources=MAX_RESOURCES)
        raw = call_llm(prompt, api_key)
        resources.extend(parse_llm_json(raw))
        time.sleep(1)

    result = {
        'slug': slug,
        'title': post.metadata.get('title'),
        'youtube': youtube_id_of(post.metadata),
        'resources': normalize_resources(resources),
    }
    RESOURCES_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'  extracted {len(result["resources"])} resources -> {out_path.name}')
    return 'ok'


def resources_yaml_block(resources):
    data = []
    for r in resources:
        entry = {'name': r['name'], 'type': r['type']}
        if r.get('url'):
            entry['url'] = r['url']
        if r.get('context'):
            entry['context'] = r['context']
        data.append(entry)
    serialized = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True,
        default_flow_style=False, width=100,
    )
    lines = serialized.splitlines()
    # keep the list items at top level under "resources:"
    body = '\n'.join(lines)
    return 'resources:\n' + body


def merge_episode(path, force=False):
    slug = path.stem
    out_path = RESOURCES_DATA_DIR / f'{slug}.json'
    if not out_path.exists():
        return 'no-result'

    result = json.loads(out_path.read_text(encoding='utf-8'))
    resources = normalize_resources(result.get('resources') or [])
    if not resources:
        return 'empty-result'

    block = resources_yaml_block(resources)
    text = path.read_text(encoding='utf-8')

    # front matter is between the first two "---" delimiter lines
    lines = text.split('\n')
    assert lines[0].strip() == '---', f'{path}: missing front matter'
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break
    assert end is not None, f'{path}: unterminated front matter'

    fm_lines = lines[1:end]
    # drop an existing resources block (key line + following list items)
    cleaned = []
    in_resources = False
    for line in fm_lines:
        if re.match(r'^resources:\s*($|#)', line):
            in_resources = True
            continue
        if in_resources:
            if line.startswith((' ', '-', '\t')) or line.strip() == '':
                continue
            in_resources = False
        cleaned.append(line)

    new_fm = '\n'.join(cleaned).rstrip('\n')
    if new_fm.strip():
        new_fm += '\n'
    new_fm += block.rstrip('\n') + '\n'

    new_text = '---\n' + new_fm + '---\n' + '\n'.join(lines[end + 1:])
    path.write_text(new_text, encoding='utf-8')
    return 'merged'


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    parser.add_argument('--fetch-transcripts', action='store_true',
                        help='fetch missing transcripts from YouTube into the cache dir')
    parser.add_argument('--extract', action='store_true',
                        help='run LLM extraction for episodes without saved results')
    parser.add_argument('--merge', action='store_true',
                        help='merge saved extraction results into episode front matter')
    parser.add_argument('--force', action='store_true',
                        help='re-run extraction even if a saved result exists')
    parser.add_argument('--limit', type=int, default=None,
                        help='process at most N episodes')
    parser.add_argument('--file', action='append', default=None,
                        help='process only this episode file (repeatable, slug or path)')
    args = parser.parse_args()

    if not any([args.fetch_transcripts, args.extract, args.merge]):
        parser.print_help()
        sys.exit(1)

    paths = list(episode_files())
    if args.file:
        wanted = {Path(f).stem for f in args.file}
        paths = [p for p in paths if p.stem in wanted]

    if args.fetch_transcripts:
        for i, path in enumerate(paths):
            post = frontmatter.load(path)
            text = transcript_text_from_front_matter(post.metadata)
            if len(text) >= 500:
                continue
            video_id = youtube_id_of(post.metadata)
            if not video_id:
                print(f'{path.name}: no transcript, no youtube id')
                continue
            cached = load_cached_youtube_transcript(video_id)
            if cached and len(cached) >= 500:
                print(f'{path.name}: already cached ({video_id})')
                continue
            print(f'{path.name}: fetching {video_id}...')
            try:
                fetch_youtube_transcript(video_id)
            except Exception as e:
                print(f'  FAILED: {e}')

    if args.extract:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print('OPENAI_API_KEY is not set; cannot run extraction')
            sys.exit(1)
        done = 0
        for path in paths:
            status = extract_for_episode(
                path, fetch=True, force=args.force, api_key=api_key
            )
            print(f'{path.name}: {status}')
            if status == 'ok':
                done += 1
            if args.limit and done >= args.limit:
                break

    if args.merge:
        for path in paths:
            status = merge_episode(path)
            if status != 'no-result':
                print(f'{path.name}: {status}')


if __name__ == '__main__':
    main()
