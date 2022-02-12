import os
import subprocess

import requests
import frontmatter

import utils
import image_utils



AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
AIRTABLE_DATABASE = os.getenv('AIRTABLE_DATABASE')

GET_RECORDS_URL_TEMPLATE = "https://api.airtable.com/v0/" + \
    "{database_name}/{table_name}?maxRecords=10&view={view_name}"
PATCH_RECORDS_URL_TEMPLATE = "https://api.airtable.com/v0/" + \
    "{database_name}/{table_name}"

PEOPLE_TABLE = 'People'
BOOKS_TABLE = 'Book-of-the-week'

HEADERS = {
    'Authorization': f'Bearer {AIRTABLE_TOKEN}'
}


def get_records(table, view):
    url = GET_RECORDS_URL_TEMPLATE.format(
        database_name=AIRTABLE_DATABASE,
        table_name=table,
        view_name=view
    )

    result = requests.get(url, headers=HEADERS).json()
    return result


def pull_people():
    response = get_records(table=PEOPLE_TABLE, view='To-add')
    records = response['records']
    return records


def mark_record_processed(table, record_id):
    url = PATCH_RECORDS_URL_TEMPLATE.format(
        database_name=AIRTABLE_DATABASE,
        table_name=table,
    )

    data = {
        "records": [{
            "id": record_id,
            "fields": {"status": "Done"}
        }]
    }

    response = requests.patch(url, json=data, headers=HEADERS)
    print(f'response from PATCH {url}')
    print(response.json())


def process_person(record):
    fields = record['fields']

    email = fields['email']

    name = fields['name']
    name = utils.clean_name(name)
    slug = utils.slugify_name(name)

    output_file, person_exists = utils.person_path_exists(slug)

    if person_exists:
        return

    params = {
        'id': slug,
        'full': name,
        'bio': fields['bio']
    }

    for f in ['github', 'twitter', 'linkedin', 'website']:
        if f in fields:
            params[f] = fields[f].strip()

    if 'picture' in fields:
        picture_record = fields['picture'][0]
        image_location = picture_record['url']
    elif 'picture_url' in fields:
        image_location = fields['picture_url']
    else:
        raise Exception('no image')

    image_utils.save_resized_profile_picture(image_location, slug)
    utils.append_email_hash(slug, email)

    template_file = './_people/_template.md'
    utils.render_template_from_file(
        template_file=template_file,
        params=params,
        output_file=output_file
    )

    mark_record_processed(
        table=PEOPLE_TABLE,
        record_id=record['id'],
    )


def process_people():
    records = pull_people()

    for record in records:
        process_person(record)

    print(f'processed {len(records)} people')



def pull_books():
    response = get_records(table=BOOKS_TABLE, view='To-add')
    records = response['records']
    return records


def extract_emails_from_book(fields):
    emails = [fields['author_email'].strip().lower()]

    if 'emails' in fields:
        other_emails = fields['emails'].split(',')
        for e in other_emails:
            e = e.lower().strip()
            emails.append(e)

    return emails


def add_book_link(result, fields, key_name, link_name):
    if key_name not in fields:
        return
 
    link = {
        'text': link_name,
        'link': fields[key_name]
    }
    result.append(link)


def process_book(record):
    fields = record['fields']

    emails = extract_emails_from_book(fields)
    authors = utils.load_authors_info(emails)

    title = fields['title'].strip()
    title_slug = utils.slugify_title(title)

    book_description = fields['description']

    date_start_raw = fields['date']
    date_start, date_end = utils.book_start_end(date_start_raw)

    book_id = f'{date_start.year:04d}{date_start.month:02d}{date_start.day:02d}-{title_slug}'
    print(f'book_id = {book_id}')

    author_names = [a['title'] for a in authors]
    author_names_joined = utils.join_comma_and(author_names)
    author_ids = [a['short'] for a in authors]

    post_description = f'Book of the Week. {title} by {author_names_joined}'

    image_folder = f'images/books/{book_id}'
    cover_path = f'{image_folder}/cover.jpg'
    preview_path = f'{image_folder}/preview.jpg'

    links = []
    add_book_link(links, fields, 'book_page', "Book's website")
    add_book_link(links, fields, 'book_page_publisher', "Book's page")
    add_book_link(links, fields, 'book_page_amazon', "Buy on Amazon")
    add_book_link(links, fields, 'book_github', "GitHub repository")

    params = {
        'title': title,
        'description': post_description,
        'cover': cover_path,
        'image': preview_path,
        'start': date_start,
        'end': date_end.replace(hour=23, minute=59, second=59),
        'authors': author_ids,
        'links': links
    }
    
    post = frontmatter.Post(
        content=book_description,
        **params
    )

    with open(f'_books/{book_id}.md', 'wt', encoding='utf-8') as f_out:
        text = frontmatter.dumps(post)
        f_out.write(text)

    if 'book_cover' in fields:
        picture_record = fields['book_cover'][0]
        image_location = picture_record['url']
    elif 'book_cover_url' in fields:
        image_location = fields['book_cover_url']
    else:
        raise Exception('no image')

    image_utils.save_image(image_location, cover_path)
    
    print('Creating a preview...')
    subprocess.call(['gitbash', 'scripts/generate-book-preview.sh', book_id])

    #subprocess.call(['bash', 'scripts/generate-book-preview.sh', book_id])

    mark_record_processed(
        table=BOOKS_TABLE,
        record_id=record['id'],
    )


def process_books():
    records = pull_books()

    for record in records:
        process_book(record)

    print(f'processed {len(records)} books')