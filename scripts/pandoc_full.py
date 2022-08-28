import os
import subprocess
import argparse

from pathlib import Path
from typing import List

import pandoc_process


REMOVE_DOC = os.getenv('REMOVE_DOC', 'False') == 'True'


def main(input: Path, author: str, tags: List[str]):
    if not input.parts[-1].endswith('.docx'):
        print(f'{input} is not docx, exiting')
        return

    output = input.with_suffix('.md')

    media = input.with_suffix('')
    media = media.with_name(media.name + '_media')

    print(f'{input=}')
    print(f'{output=}')
    print(f'{media=}')

    pandoc_command = [
        'pandoc',
            '-f', 'docx',
            '-s', str(input),
            '--to', 'gfm',
            '--markdown-headings=atx',
            '--wrap=none',
            '--columns=9999',
            f'--extract-media={str(media)}',
            '--standalone',
            '-o', str(output)
    ]

    print('pandoc command:', ' '.join(pandoc_command))
    subprocess.call(pandoc_command)

    post_id = pandoc_process.load_and_process(output, author, tags)
    print(f'{post_id=}')

    mv_command = ['mv', str(media / 'media'), f'images/posts/{post_id}']
    print('mv command:', ' '.join(mv_command))
    subprocess.call(mv_command)

    generate_command = ['gitbash', 'scripts/generate-post-preview.sh', post_id]
    subprocess.call(generate_command)

    subprocess.call([
        'echo', f'::set-output name=post-id::{post_id}'
    ])

    print('removing all the termporaty files')
    subprocess.call(['rm', '-r', output, media])

    if REMOVE_DOC == True:
        subprocess.call(['git', 'rm', input])
        subprocess.call(['rm', '-f', input])


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