import sys
import subprocess
from pathlib import Path
import pandoc_process

input = Path(sys.argv[1])

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