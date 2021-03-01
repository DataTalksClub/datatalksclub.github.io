import os

import subprocess

from datetime import date
from math import ceil, floor
from io import BytesIO
from urllib import request
from glob import glob
from datetime import datetime, timedelta

import questionary

from PIL import Image
from jinja2 import Template


def center_crop(img):
    h = img.height
    w = img.width
    d = min(w, h)

    if h == w:
        return img

    if h > w:
        left = 0
        right = w
        top = floor((h - d) / 2)
        bottom = h - top - 1
    else:
        left = floor((w - d) / 2)
        right = w - left - 1
        top = 0
        bottom = h

    return img.crop((left, top, right, bottom))


def resize(img, d=128):
    h = img.height
    w = img.width

    if h > w:
        new_h = d
        new_w = floor(h * d / w)
    else:
        new_h = floor(w * d / h)
        new_w = d

    return img.resize((new_h, new_w), resample=Image.BICUBIC)


def center_crop_resize(img):
    return center_crop(resize(img, d=128))


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def load_local_image(path):
    with Image.open(path) as img:
        return img.copy()


def load_image(path):
    if path.startswith('http'):
        return download_image(path)
    return load_local_image(path)


def save_resized_profile_picture(path, id):
    img = load_image(path)
    cropped = center_crop_resize(img)

    path = './images/authors/%s.jpg' % id
    cropped.save(path)
    print("The image is saved to %s" % path)


def create_person():
    raw = questionary.text("Person name:").ask()

    tokens = raw.split()
    full = ' '.join(tokens)
    small = ''.join(tokens).lower()

    print('Full name: %s, id: %s' % (full, small))
    print('Checking if person exist...')

    path = './_people/%s.md' % small
    if os.path.exists(path):
        print('Person already exists')
        return dict(full=full, small=small)

    print("Creating the person...")

    github = questionary.text('Github:').ask().strip()
    twitter = questionary.text('Twitter:').ask().strip()
    linkedin = questionary.text('LinkedIn:').ask().strip()
    website = questionary.text('Website:').ask().strip()
    bio = questionary.text('Bio:').ask().strip()

    image_location = questionary.text('Image location:').ask().strip()
    save_resized_profile_picture(image_location, small)

    params = {
        'id': small,
        'full': full,
        'github': github,
        'twitter': twitter,
        'linkedin': linkedin,
        'website': website,
        'bio': bio
    }

    with open('./_people/_template.md') as f_in:
        template_string = f_in.read() 

    template = Template(template_string)
    result = template.render(**params)

    print(result)

    with open(path, 'w') as f_out:
        f_out.write(result)

    return dict(full=full, small=small)


def file_starts_with_underscore(path):
    filename = path.split('/')[-1]
    return filename.startswith('_')


def find_last_book_date():
    books = glob('./_books/*.md')
    books = [b for b in books if not file_starts_with_underscore(b)]
    books = sorted(books)[::-1]
    dates = [b[9:17] for b in books]

    print("Last books:")
    for b in books[:3]:
        print(" - %s" % b)

    s = dates[0]
    prev_year = int(s[:4])
    prev_month = int(s[4:6])
    prev_day = int(s[6:])

    next_week = datetime(year=prev_year, month=prev_month, day=prev_day) + timedelta(days=7)

    year = '%04d' % next_week.year
    month = '%02d' % next_week.month
    day = '%02d' % next_week.day

    print("Next date: %s %s %s" % (year, month, day))

    return year, month, day


def create_book():
    print("Okay, let's create a book!")

    default_year, default_month, default_day = find_last_book_date()

    year = questionary.text("Year:", default_year).ask()
    month = questionary.text("Month:", default_month).ask()
    day = questionary.text("Day:", default_day).ask()    

    title_raw = questionary.text("Title:").ask()
    title_tokens = title_raw.split()
    title_hypthened = '-'.join([t.lower() for t in title_tokens])
    book_id = '%s%s%s-%s' % (year, month, day, title_hypthened)
    print('Book ID: %s' % book_id)

    title = ' '.join(title_tokens)

    start_date_str = '%s-%s-%s' % (year, month, day)
    end_date = datetime(year=int(year), month=int(month), day=int(day)) + timedelta(days=4)
    end_date_str = '%04d-%02d-%02d' % (end_date.year, end_date.month, end_date.day)

    author = create_person()

    params = {
        'title': title,
        'author_full': author['full'],
        'author_id': author['small'],
        'book_id': book_id,
        'start': start_date_str,
        'end': end_date_str
    }

    with open('./_books/_template.md') as f_in:
        template_string = f_in.read() 

    template = Template(template_string)
    result = template.render(**params)

    print(result)

    path = './_books/%s.md' % book_id
    with open(path, 'w') as f_out:
        f_out.write(result) 

    images_path = './images/books/%s' % book_id
    os.makedirs(images_path, exist_ok=True)

    image_location = questionary.text('Image location:').ask().strip()
    img = load_image(image_location)

    image_location_result = '%s/cover.jpg' % images_path
    img.save(image_location_result)

    print('Creating a preview...')
    subprocess.call(['bash', 'scripts/generate-book-preview.sh', book_id])


def create_event():
    print("Okay, let's create an event!")

    speaker_result = create_person()
    speaker = speaker_result['small']

    today = date.today()
    default_year = '%04d' % today.year
    default_month = '%02d' % today.month
    default_day = '%02d' % today.day

    year = questionary.text("Year:", default_year).ask()
    month = questionary.text("Month:", default_month).ask()
    day = questionary.text("Day:", default_day).ask()

    typ = questionary.select("Type:", choices=['webinar', 'podcast']).ask()    
    title = questionary.text("Title:").ask()

    event_id = questionary.text("Event ID:").ask()

    template_string = """
- time: {{ year }}-{{ month }}-{{ day }} 17:00:00
  title: "{{ title }}"
  speakers: [{{ speaker }}]
  type: {{ type  }}
  link: https://eventbrite.com/e/{{ event_id }}
"""

    template = Template(template_string)
    params = {
        'year': year,
        'month': month,
        'day': day,
        'title': title,
        'speaker': speaker,
        'type': typ,
        'event_id': event_id
    }

    rendered = template.render(**params)
    print(rendered)

    events_path = './_data/events.yaml'
    with open(events_path) as f_in:
        content = f_in.read()

    with open(events_path, 'w') as f_out:
        f_out.write(rendered)
        f_out.write('\n\n')
        f_out.write(content) 



def create_article():
    print("Okay, let's create an article!")


def main():
    actions = {
        'Book': create_book,
        'Event': create_event, 
        'Article': create_article,
        'Person': create_person
    }

    what = questionary.select(
        "What do you want to create?",
        choices=actions.keys(),
    ).ask()

    action = actions[what]
    action()


if __name__ == "__main__":
    main()

    

