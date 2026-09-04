#!/usr/bin/env python3
"""
Mechanical plumbing for the podcast "Resources Mentioned" feature.

The resource extraction itself is done by the AI agent via the
extract-podcast-resources skill (the agent reads the transcript and writes
scripts/data/podcast_resources/<slug>.json itself - no LLM API involved).
This script only does the mechanical steps:

1. --fetch-transcripts  fetch missing transcripts from YouTube into the
                        scripts/data/youtube_transcripts/ cache directory
                        (requires youtube-transcript-api; Oxylabs proxy
                        credentials from ~/.config/youtube/.env are used
                        automatically when YouTube blocks the IP)
2. --merge              write the saved extraction results into the
                        `resources` front matter key of each episode page,
                        rendered by the "Resources" tab in
                        _layouts/podcast.html

Usage:
    python scripts/extract_podcast_resources.py --fetch-transcripts
    python scripts/extract_podcast_resources.py --merge
    python scripts/extract_podcast_resources.py --merge --file <slug>
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PODCAST_DIR = ROOT / '_podcast'
# Raw YouTube transcripts live in a separate place, away from the content collections.
YOUTUBE_CACHE_DIR = ROOT / 'scripts' / 'data' / 'youtube_transcripts'
# Per-episode extraction results (JSON), also kept outside the content collections.
RESOURCES_DATA_DIR = ROOT / 'scripts' / 'data' / 'podcast_resources'

RESOURCE_TYPES = [
    'tool', 'book', 'paper', 'course', 'person',
    'company', 'community', 'dataset', 'service', 'other',
]


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


def episode_transcript_source(fm):
    """Return how the episode's transcript is covered: 'front-matter',
    'youtube-cache' or None (needs fetching)."""
    if len(transcript_text_from_front_matter(fm)) >= 500:
        return 'front-matter'
    video_id = youtube_id_of(fm)
    if video_id:
        cached = load_cached_youtube_transcript(video_id)
        if cached and len(cached) >= 500:
            return 'youtube-cache'
    return None


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
    return list(seen.values())[:40]


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
    return 'resources:\n' + serialized


def merge_episode(path):
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
    parser.add_argument('--merge', action='store_true',
                        help='merge saved extraction results into episode front matter')
    parser.add_argument('--file', action='append', default=None,
                        help='process only this episode file (repeatable, slug or path)')
    args = parser.parse_args()

    if not any([args.fetch_transcripts, args.merge]):
        parser.print_help()
        sys.exit(1)

    paths = list(episode_files())
    if args.file:
        wanted = {Path(f).stem for f in args.file}
        paths = [p for p in paths if p.stem in wanted]

    if args.fetch_transcripts:
        for path in paths:
            import frontmatter
            post = frontmatter.load(path)
            if episode_transcript_source(post.metadata) is not None:
                continue
            video_id = youtube_id_of(post.metadata)
            if not video_id:
                print(f'{path.name}: no transcript, no youtube id')
                continue
            print(f'{path.name}: fetching {video_id}...')
            try:
                fetch_youtube_transcript(video_id)
            except Exception as e:
                print(f'  FAILED: {e}')

    if args.merge:
        for path in paths:
            status = merge_episode(path)
            if status != 'no-result':
                print(f'{path.name}: {status}')


if __name__ == '__main__':
    main()
