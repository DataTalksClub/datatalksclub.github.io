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

    pandoc_full.main(location, author, tags)

    print('removing the tmp docx file...')
    location.unlink()


if __name__ == '__main__':
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