import subprocess
from pathlib import Path
import pandoc_process

tmp = Path('tmp')
tmp.mkdir(parents=True, exist_ok=True)

# subprocess.call([
#     'wget',
#     ''
# ])

input = tmp / 'document.docx'
output = tmp / 'document.md'

subprocess.call([
    'pandoc',
        '-f', 'docx',
        '-s', input,
        '--to', 'gfm',
        '--markdown-headings=atx',
        '--wrap=none',
        '--columns=9999',
        '--extract-media=media',
        '--standalone',
        '-o', output
])

pandoc_process.load_and_process(output)