import os
import requests

import utils
import image_utils


AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
AIRTABLE_DATABASE = os.getenv('AIRTABLE_DATABASE')

GET_RECORDS_URL_TEMPLATE = "https://api.airtable.com/v0/" + \
    "{database_name}/{table_name}?maxRecords=10&view={view_name}"
PATCH_RECORDS_URL_TEMPLATE = "https://api.airtable.com/v0/" + \
    "{database_name}/{table_name}"

PEOPLE_TABLE = 'People'

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

    print(f'processed {len(records)} records')


