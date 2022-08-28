import uuid

from pathlib import Path


def get_tmp_dir():
    tmp = Path('tmp')
    tmp.mkdir(parents=True, exist_ok=True)
    return tmp


def get_tmp_file(ext):
    filename = str(uuid.uuid4())
    fullname = f'{filename}.{ext}'
    tmp = get_tmp_dir()
    return tmp / fullname