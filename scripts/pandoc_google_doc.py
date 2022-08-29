import sys
import argparse
from pathlib import Path
from typing import List

import requests

import pandoc_full
import pandoc_util


def download_docx(file_id, location: Path=None):
    if location is None:
        location = pandoc_util.get_tmp_file('docx')

    f_out = open(location, 'wb')

    url = f'https://docs.google.com/document/d/{file_id}/export?format=docx'

    with f_out:
        response = requests.get(url)
        response.raise_for_status()
        f_out.write(response.content)

        print(f'wrote docx from {file_id} to {location}')

    return location


def main(file_id: str, author: str, tags: List[str]):
    location = download_docx(file_id)

    pandoc_full.main(input=location, author=author, tags=tags,
            remove_source=True, remove_temporary=True)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-i':
        import questionary
        
        fileid = questionary.text("File ID:").ask()
        author: str = questionary.text("Author:").ask()
        author = author.replace(' ', '').strip().lower()

        tags_raw = questionary.text("Tags:").ask()
        tags = tags_raw.replace(' ', '').strip().lower().split(',')
    else:
        parser = argparse.ArgumentParser()

        parser.add_argument('--fileid')
        parser.add_argument('--author')
        parser.add_argument('--tags')

        args = parser.parse_args()

        fileid = args.fileid
        author = args.author
        tags = args.tags.split(',')
        tags = [t.lower().strip() for t in tags]

    main(fileid, author, tags)