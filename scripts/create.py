import os

from datetime import date
from math import ceil, floor
from io import BytesIO
from urllib import request

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

    return img.resize((new_h, new_w),resample=Image.BICUBIC)


def center_crop_resize(img):
    return center_crop(resize(img, d=128))


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def save_resized_image(url, id):
    img = download_image(url)
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
        return small

    print("Creating the person...")

    with open('./_people/_template.md') as f_in:
        template_string = f_in.read() 

    github = questionary.text('Github:').ask().strip()
    twitter = questionary.text('Twitter:').ask().strip()
    linkedin = questionary.text('LinkedIn:').ask().strip()
    website = questionary.text('Website:').ask().strip()
    bio = questionary.text('Bio:').ask().strip()

    image_url = questionary.text('Image URL:').ask().strip()
    save_resized_image(image_url, small)

    params = {
        'id': small,
        'full': full,
        'github': github,
        'twitter': twitter,
        'linkedin': linkedin,
        'website': website,
        'bio': bio
    }

    template = Template(template_string)
    result = template.render(**params)

    print(result)

    with open(path, 'w') as f_out:
        f_out.write(result)

    return small



def create_book():
    print("Okay, let's create a book!")


def create_event():
    print("Okay, let's create an event!")
    
    speaker = create_person()

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
  title: {{ title }}
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

    

