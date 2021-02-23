import os
import subprocess

import yaml

from jinja2 import Template
from slugify import slugify


with open('_data/events.yaml', 'r') as f_in:
    data = yaml.full_load(f_in)

podcasts = [e for e in data if e['type'] == 'podcast' and 'anchor' in e]


def create_podcast_page(p):
    if 'short' in p:
        short = p['short']
    else:
        short = p['title']

    if 'slug' in p:
        slug = slugify(p['slug'])
    else:
        slug = slugify(short)

    podcast_id = 's%02de%02d-%s' % (p['season'], p['episode'], slug)
    
    filename = '_podcast/%s.md' % podcast_id

    if os.path.exists(filename):
        print('%s is already processed' % podcast_id)
        return
    
    with open('_podcast/_template.md') as f_in:
        template_raw = f_in.read()

    template = Template(template_raw)

    youtube_url = p['youtube']
    youtube_id = youtube_url.split('?v=')[1]
    anchor_url = p['anchor']
    anchor_id = anchor_url[len('https://anchor.fm/datatalksclub/episodes/'):]
    image_path = 'images/podcast/%s.jpg' % podcast_id

    params = {
        'title': p['title'],
        'short': short,
        'image': image_path,
        'guest': p['speakers'][0],
        'season': p['season'],
        'episode': p['episode'],
        'youtube': youtube_url,
        'youtube_id': youtube_id, 
        'anchor': anchor_url,
        'anchor_id': anchor_id
    }

    template = Template(template_raw)
    result = template.render(**params)

    print(filename)
    print(result)
    
    with open(filename, 'w') as f_out:
        f_out.write(result)
    
    subprocess.call(['bash', 'scripts/generate-podcast-preview.sh', podcast_id])


for p in podcasts:
    print(p['title'])
    create_podcast_page(p)
    print()


