import os
from math import floor
from io import BytesIO

import requests
from PIL import Image


def center_crop(img):
    h = img.height
    w = img.width
    d = min(w, h)

    if h == w:
        return img

    if h > w:
        left = 0
        right = w
        top = floor((h - d) / 2)
        bottom = h - top - 1
    else:
        left = floor((w - d) / 2)
        right = w - left - 1
        top = 0
        bottom = h

    return img.crop((left, top, right, bottom))


def resize(img, d=128):
    h = img.height
    w = img.width

    if h <= d and w <= d:
        return img

    if h > w:
        new_h = d
        new_w = floor(h * d / w)
    else:
        new_h = floor(w * d / h)
        new_w = d

    return img.resize((new_h, new_w), resample=Image.BICUBIC)


def center_crop_resize(img, d=128):
    return center_crop(resize(img, d=d))


def download_image(url):
    resp = requests.get(url)
    buffer = resp.content
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def load_local_image(path):
    with Image.open(path) as img:
        return img.copy()


def load_image(path):
    if path.startswith('http'):
        return download_image(path)
    return load_local_image(path)


def save_resized_profile_picture(path, id, d=128):
    img = load_image(path)

    cropped = center_crop_resize(img, d=d)

    if cropped.mode == 'RGBA':
        cropped = cropped.convert('RGB')

    path = './images/authors/%s.jpg' % id
    cropped.save(path)

    print("The image is saved to %s" % path)
    return path


def save_image(image_location, output_file, d=400):
    img = load_image(image_location)

    folder = os.path.dirname(output_file)
    os.makedirs(folder, exist_ok=True)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    img = resize(img, d=d)

    if output_file.endswith('.jpg'):
        img.save(output_file, quality=95)
    else:
        img.save(output_file)
