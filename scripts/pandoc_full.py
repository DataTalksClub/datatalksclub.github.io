import os
import sys
import subprocess
import argparse

from pathlib import Path

import pandoc_process



REMOVE_DOC = os.getenv('REMOVE_DOC', 'False') == 'True'

def main(input, author, tags):
    if not input.parts[-1].endswith('.docx'):
        print(f'{input} is not docx, exiting')
        return

    tmp = Path('tmp')
    tmp.mkdir(parents=True, exist_ok=True)

    output = tmp / 'document.md'
    media = tmp / 'media'

    subprocess.call([
        'pandoc',
            '-f', 'docx',
            '-s', input,
            '--to', 'gfm',
            '--markdown-headings=atx',
            '--wrap=none',
            '--columns=9999',
            f'--extract-media={media}',
            '--standalone',
            '-o', output
    ])

    post_id = pandoc_process.load_and_process(output, author, tags)

    subprocess.call([
        'mv',
            media / 'media',
            f'images/posts/{post_id}'
    ])

    subprocess.call([
        'gitbash',
        'scripts/generate-post-preview.sh',
        post_id
    ])

    subprocess.call([
        'echo', f'::set-output name=post-id::{post_id}'
    ])

    if REMOVE_DOC == True:
        subprocess.call([
            'git', 'rm', {input}
        ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--input')
    parser.add_argument('--author')
    parser.add_argument('--tags')

    args = parser.parse_args()

    input = Path(args.input)
    author = args.author
    tags = args.tags.split(',')
    tags = [t.lower().strip() for t in tags]

    main(input, author, tags)