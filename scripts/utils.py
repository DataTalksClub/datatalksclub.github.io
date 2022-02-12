import os
from hashlib import sha1

import unidecode
from jinja2 import Template


def clean_name(name):
    tokens = name.strip().split()
    return ' '.join(tokens)


def slugify_name(name):
    tokens = name.split()
    slug = ''.join(tokens).lower()
    slug = slug.replace("'", '').replace('-', '').replace('.', '-')
    slug = unidecode.unidecode(slug)
    return slug


def person_path_exists(slug):
    print('Checking if person exist...')

    path = './_people/%s.md' % slug

    if os.path.exists(path):
        print('Person already exists')
        return path, True
    
    return path, False


def compute_hash(email):
    email = email.strip().lower()
    return sha1(email.encode('utf-8')).hexdigest()


def append_email_hash(slug, email):
    email_hash = compute_hash(email)

    with open('./scripts/data/hashes.csv', 'a') as f_out:
        f_out.write(f'{email_hash},{slug}\n')


def lookup_slug(email):
    email_hash = compute_hash(email)
    pass


def render_template_from_file(template_file, params, output_file):
    with open(template_file) as f_in:
        template_string = f_in.read() 

    render_template(template_string, params, output_file)


def render_template(template_string, params, output_file):
    template = Template(template_string)
    result = template.render(**params)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(result)

    print(f'writing to {output_file}...')
    print(result)

