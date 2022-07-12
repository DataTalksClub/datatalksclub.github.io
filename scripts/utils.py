import os
from hashlib import sha1
from datetime import datetime
from datetime import timedelta

import unidecode
import frontmatter

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


stopwords = {'am', 'is', 'are', 'the', 'a', 'an'}

def slugify_title(title):
    title_tokens = title.split()
    title_tokens = [t.lower() for t in title_tokens]
    title_tokens = [t for t in title_tokens if t not in stopwords]
    res = '-'.join(title_tokens)
    res = res.replace('.', '-')
    res = res.replace(',', '')
    res = res.replace("'", '')
    res = res.replace(':', '')
    res = res.replace('?', '')
    res = res.replace('<', '')
    res = res.replace('>', '')
    res = res.replace('\\', '')
    res = res.replace('/', '')

    res = unidecode.unidecode(res)
    return res


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


def lookup_author_id(email):
    ids = lookup_author_ids([email])
    slug, = ids.values()
    return slug 


def lookup_author_ids(emails):
    emails = [email.lower().strip() for email in emails]
    email_hashes = {compute_hash(e): e for e in emails}

    result = {}

    with open('./scripts/data/hashes.csv', 'r') as f_in:
        for line in f_in:
            line = line.strip()
            if len(line) == 0:
                continue

            email_hash, slug = line.split(',')
            if email_hash in email_hashes:
                result[email_hash] = slug

    diff = email_hashes - result.keys()
    if len(diff) > 0:
        print('not found authors for these emails')
        print(email_hashes)

    return result
            

def join_comma_and(authors):
    if len(authors) == 1:
        return authors[0]

    return ', '.join(authors[:-1]) + ' and ' + authors[-1]


def load_author_info(author_id):
    fm = frontmatter.load(f'./_people/{author_id}.md')
    author = dict(fm.metadata)
    author['bio'] = fm.content
    return author


def load_authors_info(emails):
    author_ids = lookup_author_ids(emails)
    authors = [load_author_info(a) for a in author_ids.values()]
    return authors


def render_template_from_file(template_file, params, output_file):
    with open(template_file) as f_in:
        template_string = f_in.read() 

    render_template(template_string, params, output_file)


def render_template_str(template_string, params):
    template = Template(template_string)
    result = template.render(**params)
    return result


def render_template(template_string, params, output_file):
    template = Template(template_string)
    result = template.render(**params)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(result)

    print(f'writing to {output_file}...')
    print(result)



def parse_date(date_raw):
    return datetime.strptime(date_raw, '%Y-%m-%d')


def book_start_end(date_start_raw):
    date_start = parse_date(date_start_raw)
    date_end = date_start + timedelta(days=4)
    return date_start, date_end


def prepend_to_file(content, filename, sep='\n\n'):
    print(f'appending to {filename}:')
    print(content)

    with open(filename) as f_in:
        old_content = f_in.read()

    with open(filename, 'w') as f_out:
        f_out.write(content)
        f_out.write(sep)
        f_out.write(old_content) 