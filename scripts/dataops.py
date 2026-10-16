"""
Website page generator backed by DataOps (replaces the Airtable import).

This script reads published website content data from the DataOps portal API
and generates the same website files the retired Airtable import produced:

    python scripts/dataops.py person --id <person-id>
    python scripts/dataops.py book --id <book-id>
    python scripts/dataops.py event (--card <card-id> | --episode <episode-id>) --url URL --time "YYYY-MM-DD HH:MM:SS" [--type webinar]
    python scripts/dataops.py podcast <episode-id | SxxEyy | website-slug>

Environment variables required:
    DATAOPS_TOKEN - portal API token (work-read is enough to generate)
    DATAOPS_URL   - portal base URL (default: https://ops.dtcdev.click)

Behavior:
    - Files are generated locally only. Nothing is committed or pushed.
      Review with git diff, build with make build, then commit/push.
    - An existing page file is never overwritten; the command refuses instead.
    - --dry-run prints what would be written without writing anything.
    - Speaker/author slugs must already exist in _people/ (create the profile
      first with the person command); names are resolved through /api/people.
"""

import argparse
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlparse

import frontmatter
import requests

import utils
import image_utils


DATAOPS_URL = os.getenv('DATAOPS_URL', 'https://ops.dtcdev.click').rstrip('/')
DATAOPS_TOKEN = os.getenv('DATAOPS_TOKEN')

WEBSITE_EVENT_TYPES = {'podcast', 'webinar', 'workshop', 'conference'}


def api_get(route, params=None):
    if not DATAOPS_TOKEN:
        raise Exception('DATAOPS_TOKEN is not set')

    response = requests.get(
        f'{DATAOPS_URL}{route}',
        params=params or {},
        headers={'Authorization': f'Bearer {DATAOPS_TOKEN}'},
    )
    if response.status_code == 404:
        raise Exception(f'{route} not found')
    if response.status_code != 200:
        raise Exception(f'GET {route} failed ({response.status_code}): {response.text[:300]}')
    return response.json()


def load_people_index():
    """Map normalized person name -> _people slug, from the website checkout."""
    index = {}
    people_dir = './_people'
    for filename in os.listdir(people_dir):
        if not filename.endswith('.md') or filename.startswith('_'):
            continue
        slug = filename[:-3]
        try:
            page = frontmatter.load(os.path.join(people_dir, filename))
            title = str(page.metadata.get('title', '') or '').strip()
        except Exception:
            title = ''
        if title:
            index[normalize_name(title)] = slug
    return index


def normalize_name(name):
    return re.sub(r'\s+', ' ', name.strip()).lower()


def fetch_register_people():
    """Map normalized name -> slug from the DataOps people register."""
    payload = api_get('/api/people')
    return {
        normalize_name(person['name']): person['slug']
        for person in payload.get('items', [])
        if person.get('name') and person.get('slug')
    }


def resolve_speakers(names, register_people):
    """Resolve display names to _people slugs. Never invent a slug."""
    website_people = load_people_index()
    slugs = []
    missing = []
    for name in names:
        key = normalize_name(name)
        slug = register_people.get(key) or website_people.get(key)
        if slug is None:
            missing.append(name)
        else:
            slugs.append(slug)
    if missing:
        raise Exception(
            'unknown speaker(s): %s. Create the profile(s) first '
            'with: python scripts/dataops.py person --id <person-id>' % ', '.join(missing)
        )
    return slugs


def check_profile_files(slugs):
    missing = [s for s in slugs if not os.path.exists(f'./_people/{s}.md')]
    if missing:
        raise Exception(
            '_people profile(s) missing: %s. Create them first '
            'with: python scripts/dataops.py person --id <person-id>' % ', '.join(missing)
        )


def youtube_id_of(url):
    if not url or '?v=' not in url:
        return None
    return url.split('?v=')[1].split('&')[0].strip()


def anchor_id_of(url):
    if not url:
        return None
    path = urlparse(url).path.rstrip('/')
    return unquote(path.split('/')[-1]) or None


def run_preview(script, page_id, dry_run):
    if dry_run:
        print(f'would run {script} {page_id}')
        return
    print(f'Creating a preview ({script} {page_id})...')
    try:
        subprocess.call(['bash', f'scripts/{script}', page_id])
    except Exception as e:
        print(f'WARNING: preview failed ({e}); the page file is still written')


# ---------------------------------------------------------------- person ---

def process_person(person_id, dry_run=False):
    person = api_get(f'/api/people/{person_id}')

    slug = person['slug'].strip()
    output_file = f'_people/{slug}.md'

    if os.path.exists(output_file):
        raise Exception(f'{output_file} already exists; refusing to overwrite')

    bio = (person.get('bio') or person.get('bioShort') or '').strip()
    if not bio:
        raise Exception(f'person {person_id} has no bio; add one with dataops speakers update')

    links = person.get('links') or {}
    params = {
        'id': slug,
        'full': person['name'].strip(),
        'bio': bio,
        'github': (links.get('github') or '').strip(),
        'twitter': (links.get('twitter') or '').strip(),
        'linkedin': (links.get('linkedin') or '').strip(),
        'website': (links.get('website') or '').strip(),
    }

    template_file = './_people/_template.md'

    print(f'person: {person["name"]} -> {output_file}')
    if dry_run:
        print('dry run: nothing written')
        return

    utils.render_template_from_file(
        template_file=template_file,
        params=params,
        output_file=output_file,
    )

    photo_url = (person.get('photoUrl') or '').strip()
    if not photo_url:
        raise Exception(f'{output_file} written, but person has no photoUrl; add the approved photo manually')
    image_utils.save_resized_profile_picture(photo_url, slug)


# ------------------------------------------------------------------ book ---

def process_book(book_id, dry_run=False):
    book = api_get(f'/api/books/{book_id}')
    register_people = fetch_register_people()

    title = book['title'].strip()
    author_slugs = resolve_speakers(
        [a['name'] for a in book.get('authors', [])],
        register_people,
    )
    check_profile_files(author_slugs)

    start = (book.get('startDate') or '').strip()
    if not start:
        raise Exception(f'book {book_id} has no startDate; set it with dataops books update')
    book_slug = (book.get('slug') or utils.slugify_title(title)).strip()
    book_id_str = f'{start.replace("-", "")}-{book_slug}'

    output_file = f'_books/{book_id_str}.md'
    if os.path.exists(output_file):
        raise Exception(f'{output_file} already exists; refusing to overwrite')

    description = (book.get('description') or '').strip()
    if not description:
        print('WARNING: book has no description; the page will need one before publishing')

    end = (book.get('endDate') or start).strip()
    end_full = f'{end} 22:59:59' if len(end) == 10 else end

    image_folder = f'images/books/{book_id_str}'
    cover_path = f'{image_folder}/cover.jpg'
    preview_path = f'{image_folder}/preview.jpg'

    links = [
        {'text': link['text'].strip(), 'link': link['url'].strip()}
        for link in (book.get('links') or [])
        if link.get('text') and link.get('url')
    ]

    post = frontmatter.Post(
        content=description,
        title=title,
        description=f'Book of the Week. {title} by {utils.join_comma_and([a["name"] for a in book.get("authors", [])])}',
        cover=cover_path,
        image=preview_path,
        start=f'{start} 00:00:00',
        end=end_full,
        authors=author_slugs,
        links=links,
    )

    print(f'book: {title} -> {output_file}')
    if dry_run:
        print('dry run: nothing written')
        return

    with open(output_file, 'wt', encoding='utf-8') as f_out:
        f_out.write(frontmatter.dumps(post))

    cover_url = (book.get('coverUrl') or '').strip()
    if not cover_url:
        raise Exception(f'{output_file} written, but book has no coverUrl; add the approved cover manually')
    image_utils.save_image(cover_url, cover_path, d=400)

    run_preview('generate-book-preview.sh', book_id_str, dry_run)


# ----------------------------------------------------------------- event ---

EVENT_TEMPLATE = """
- time: {{ time }}
  title: "{{ title }}"
  speakers: [{{ speakers }}]
  type: {{ typ }}
  link: {{ url }}{{ extra }}
"""


def event_row_exists(time, title):
    with open('./_data/events.yaml', encoding='utf-8') as f_in:
        content = f_in.read()
    return f'- time: {time}\n  title: "{title}"' in content


def append_event_row(params, dry_run=False):
    row = utils.render_template_str(EVENT_TEMPLATE, params)
    print('event row:')
    print(row)
    if dry_run:
        print('dry run: events.yaml untouched')
        return
    utils.prepend_to_file(row, './_data/events.yaml')


def process_event(card_id=None, episode_id=None, url=None, time=None, typ=None, dry_run=False):
    if (card_id is None) == (episode_id is None):
        raise Exception('pass exactly one of --card or --episode')

    if not time or not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', time):
        raise Exception('--time "YYYY-MM-DD HH:MM:SS" is required (the site convention; never assume 17:00)')

    register_people = fetch_register_people()

    if episode_id is not None:
        episode = api_get(f'/api/podcast-episodes/{episode_id}')
        title = (episode.get('title') or '').strip()
        slugs = resolve_speakers(
            [g['name'] for g in episode.get('guests', [])],
            register_people,
        )
        check_profile_files(slugs)
        typ = 'podcast'
        links = episode.get('links') or {}
        extra = ''
        if episode.get('season') and episode.get('episode'):
            extra += f"\n  season: {episode['season']}\n  episode: {episode['episode']}"
        youtube_url = (links.get('youtube') or '').strip()
        if youtube_url:
            extra += f'\n  youtube: {youtube_url}'
        if episode.get('websiteSlug'):
            row_slug = episode['websiteSlug'].strip()
            if row_slug.startswith('s%02de%02d-' % (episode.get('season') or 0, episode.get('episode') or 0)):
                row_slug = row_slug[len('s00e00-'):]
            extra += f'\n  slug: "{row_slug}"'
        anchor_url = (links.get('anchor') or '').strip()
        if anchor_url:
            extra += f'\n  anchor: {anchor_url}'
        row_url = (url or '').strip()
        if not row_url:
            raise Exception('podcast event rows need --url (the registration link)')
    else:
        card = api_get(f'/api/cards/{card_id}')['card']
        title = (card.get('title') or '').strip()
        if not title:
            raise Exception(f'card {card_id} has no title')
        slugs = resolve_speakers(card.get('people') or [], register_people)
        check_profile_files(slugs)
        if typ is None:
            typ = infer_event_type(card)
        row_url = (url or pick_card_url(card)).strip()
        if not row_url:
            raise Exception('no --url given and the card has no single link to use; pass --url explicitly')
        extra = ''

    if typ not in WEBSITE_EVENT_TYPES:
        raise Exception(f'--type must be one of {sorted(WEBSITE_EVENT_TYPES)}')

    if event_row_exists(time, title):
        raise Exception(f'events.yaml already has "{title}" at {time}; refusing to duplicate')

    append_event_row({
        'time': time,
        'title': title,
        'speakers': ', '.join(slugs),
        'typ': typ,
        'url': row_url,
        'extra': extra,
    }, dry_run)


def infer_event_type(card):
    template_id = str(card.get('templateId') or '')
    if template_id:
        try:
            payload = api_get('/api/templates')
            templates = payload.get('templates') or payload.get('items') or []
            for template in templates:
                if template.get('id') == template_id:
                    typ = str(template.get('type') or '')
                    if typ in WEBSITE_EVENT_TYPES:
                        return typ
                    if typ == 'book-of-the-week':
                        raise Exception(
                            'this is a Book of the Week card; generate a book page with: '
                            'python scripts/dataops.py book --id <book-id>'
                        )
                    break
        except Exception as e:
            if 'Book of the Week' in str(e):
                raise
    raise Exception(
        f'cannot infer --type from card template "{template_id}"; '
        f'pass --type explicitly ({sorted(WEBSITE_EVENT_TYPES)})'
    )


def pick_card_url(card):
    urls = []
    for link in card.get('cardLinks') or []:
        url = (link.get('url') or '').strip()
        if url.startswith('https://'):
            urls.append(url)
    if len(urls) == 1:
        return urls[0]
    return ''


# --------------------------------------------------------------- podcast ---

def find_episode(ref):
    """Resolve an episode id, SxxEyy code, or website slug to the full record."""
    if re.match(r'^[Ss]\d+[Ee]\d+$', ref):
        m = re.match(r'^[Ss](\d+)[Ee](\d+)$', ref)
        season, number = int(m.group(1)), int(m.group(2))
        payload = api_get('/api/podcast-episodes', params={'season': season})
        for episode in payload.get('items', []):
            if episode.get('season') == season and episode.get('episode') == number:
                return api_get(f'/api/podcast-episodes/{episode["id"]}')
        raise Exception(f'no S{season}E{number} in the episode register')
    if re.match(r'^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$', ref) and '-' in ref or len(ref) <= 40:
        try:
            return api_get(f'/api/podcast-episodes/{ref}')
        except Exception:
            pass
    payload = api_get('/api/podcast-episodes')
    for episode in payload.get('items', []):
        if (episode.get('websiteSlug') or '') == ref:
            return api_get(f'/api/podcast-episodes/{episode["id"]}')
    raise Exception(f'no episode matches "{ref}"; pass an id, SxxEyy, or website slug')


def process_podcast(ref, dry_run=False, skip_preview=False):
    episode = find_episode(ref)
    register_people = fetch_register_people()

    season = episode.get('season')
    number = episode.get('episode')
    title = (episode.get('title') or '').strip()
    if not title:
        raise Exception(f'episode {episode["id"]} has no title')

    slugs = resolve_speakers(
        [g.get('name', '') for g in episode.get('guests', [])],
        register_people,
    )
    if not slugs:
        raise Exception(f'episode {episode["id"]} has no guests')
    check_profile_files(slugs)

    slug = (episode.get('websiteSlug') or utils.slugify_title(title)).strip()
    podcast_id = slug
    output_file = f'_podcast/{podcast_id}.md'
    if os.path.exists(output_file):
        raise Exception(f'{output_file} already exists; refusing to overwrite')

    links = episode.get('links') or {}
    youtube_url = (links.get('youtube') or '').strip()
    anchor_url = (links.get('anchor') or '').strip()
    spotify_url = (links.get('spotify') or '').strip()
    apple_url = (links.get('apple') or '').strip()

    youtube_id = youtube_id_of(youtube_url)
    anchor_id = anchor_id_of(anchor_url)

    ids = {}
    if youtube_id:
        ids['youtube'] = youtube_id
    if anchor_id:
        ids['anchor'] = anchor_id

    page_links = {}
    if youtube_url:
        page_links['youtube'] = youtube_url
    if anchor_url:
        page_links['anchor'] = anchor_url
    if spotify_url:
        page_links['spotify'] = spotify_url
    if apple_url:
        page_links['apple'] = apple_url

    if not youtube_url:
        print('WARNING: episode has no YouTube link yet; ids.youtube and clip URLs are omitted')
    if not spotify_url or not apple_url:
        print('WARNING: episode is missing Spotify/Apple links; add them in DataOps before publishing')

    description = (episode.get('description') or '').strip()
    if not description:
        print('WARNING: episode has no description; the page will need one before publishing')

    clips = []
    for clip in episode.get('clips') or []:
        entry = {
            'name': clip['name'],
            'startOffset': clip['startOffset'],
            'endOffset': clip['endOffset'],
        }
        url = clip.get('url')
        if not url and youtube_id:
            url = f'https://www.youtube.com/watch?v={youtube_id}&t={clip["startOffset"]}'
        if url:
            entry['url'] = url
        clips.append(entry)

    resources = []
    for resource in episode.get('resources') or []:
        entry = {'name': resource['name'], 'type': resource['type']}
        if resource.get('url'):
            entry['url'] = resource['url']
        if resource.get('context'):
            entry['context'] = resource['context']
        resources.append(entry)

    metadata = {
        'title': title,
        'guests': slugs,
        'image': f'images/podcast/{podcast_id}.jpg',
    }
    if episode.get('short'):
        metadata['short'] = episode['short'].strip()
    if season:
        metadata['season'] = season
    if number:
        metadata['episode'] = number
    if ids:
        metadata['ids'] = ids
    if page_links:
        metadata['links'] = page_links
    if description:
        metadata['description'] = description
    if episode.get('intro'):
        metadata['intro'] = episode['intro']
    if episode.get('topics'):
        metadata['topics'] = episode['topics']
    if episode.get('duration'):
        metadata['duration'] = episode['duration']
    if clips:
        metadata['quotableClips'] = clips
    if resources:
        metadata['resources'] = resources
    if episode.get('transcript'):
        metadata['transcript'] = episode['transcript']
    release = (episode.get('releaseDate') or '').strip()
    if release:
        metadata['dateadded'] = release

    post = frontmatter.Post(content='', **metadata)

    print(f'podcast: {title} -> {output_file}')
    if dry_run:
        print('dry run: nothing written')
        return

    with open(output_file, 'wt', encoding='utf-8') as f_out:
        f_out.write(frontmatter.dumps(post))

    image_url = (episode.get('imageUrl') or '').strip()
    if image_url:
        image_utils.save_image(image_url, f'images/podcast/{podcast_id}.jpg')

    if not skip_preview:
        run_preview('generate-podcast-preview.sh', podcast_id, dry_run)
    else:
        print('preview skipped (--skip-preview)')


def main():
    parser = argparse.ArgumentParser(description='Generate website pages from DataOps data')
    sub = parser.add_subparsers(dest='command', required=True)

    p = sub.add_parser('person', help='generate a _people profile from a DataOps person')
    p.add_argument('--id', required=True, help='DataOps person id')
    p.add_argument('--dry-run', action='store_true', help='print what would be written')

    b = sub.add_parser('book', help='generate a _books page from a DataOps book')
    b.add_argument('--id', required=True, help='DataOps book id')
    b.add_argument('--dry-run', action='store_true', help='print what would be written')

    e = sub.add_parser('event', help='prepend an _data/events.yaml row from a DataOps card or episode')
    e.add_argument('--card', default=None, help='DataOps card id')
    e.add_argument('--episode', default=None, help='DataOps episode id')
    e.add_argument('--url', default=None, help='registration URL (required unless the card has exactly one link)')
    e.add_argument('--time', default=None, help='event time "YYYY-MM-DD HH:MM:SS" (required)')
    e.add_argument('--type', default=None, help='podcast|webinar|workshop|conference (podcast for --episode)')
    e.add_argument('--dry-run', action='store_true', help='print what would be written')

    c = sub.add_parser('podcast', help='generate a _podcast page from a DataOps episode')
    c.add_argument('ref', help='episode id, SxxEyy code, or website slug')
    c.add_argument('--skip-preview', action='store_true', help='skip the preview render')
    c.add_argument('--dry-run', action='store_true', help='print what would be written')

    args = parser.parse_args()

    if args.command == 'person':
        process_person(args.id, dry_run=args.dry_run)
    elif args.command == 'book':
        process_book(args.id, dry_run=args.dry_run)
    elif args.command == 'event':
        process_event(
            card_id=args.card,
            episode_id=args.episode,
            url=args.url,
            time=args.time,
            typ=args.type,
            dry_run=args.dry_run,
        )
    elif args.command == 'podcast':
        process_podcast(args.ref, dry_run=args.dry_run, skip_preview=args.skip_preview)


if __name__ == '__main__':
    main()
