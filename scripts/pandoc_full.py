import os
import sys
import subprocess
from pathlib import Path
import pandoc_process


REMOVE_DOC = os.getenv('REMOVE_DOC', 'False') == 'True'

def main(input):
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

    post_id = pandoc_process.load_and_process(output)

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
    input = Path(sys.argv[1])
    main(input)