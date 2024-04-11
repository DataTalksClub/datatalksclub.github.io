#!/usr/bin/env python
# coding: utf-8

import re
import functools
from datetime import datetime
from pathlib import Path

import frontmatter
import markdown

import utils



re_span = re.compile('<span.+</span>')
re_md_links = re.compile(r'(\[.+?\]\(http.+?\))')
re_img = re.compile(r'<img .+?/>')
re_underline = re.compile('<u>(.+?)</u>')
re_style = re.compile('style=".+?"')
re_scr = re.compile('src="(.+?)"')


figure_template = """
<figure>
{img}
<figcaption>{caption}</figcaption>
</figure>
""".strip()


def clean_title(title):
    title = re_span.sub('', title)  
    title = title.replace('\<', '<')
    title = title.replace('\>', '>')
    return title


def create_post_id(title):
    title = utils.slugify_title(title)
    today = datetime.today().strftime('%Y-%m-%d')
    post_id = f'{today}-{title}'
    return post_id


def remove_specific_tags(html, tags):
    """Remove specified HTML tags from a string."""
    for tag in tags:
        html = re.sub(f'<{tag}[^>]*>', '', html)  # Remove opening tags
        html = re.sub(f'</{tag}>', '', html)  # Remove closing tags
    return html

def prepare_content(post_id, content):

    def replace_path(m):
        src = m.group(1)
        name = Path(src).parts[-1]
        path = f'/images/posts/{post_id}/{name}'
        return f'src="{path}"'

    def replace_image(m, caption=''):
        img = m.group(0)
        img = re_style.sub('', img)
        img = re_scr.sub(replace_path, img)
        return figure_template.format(img=img, caption=caption)

    result = []

    lines = content.split('\n')
    num_lines = len(lines)

    i = 0
    while i < num_lines:
        line = lines[i]
        line = line.replace('\u200a', ' ')

        if '<u>' in line:
            line = re_underline.sub(r'\1', line)
            result.append(line)
            i = i + 1
            continue

        if '<img' in line:
            # print(f'{line=}')
            # this line is an image, so the next line must be 
            # the caption for the image 
            next_line = ''

            j = i + 1
            while j < num_lines:
                next_line_candidate = lines[j].strip()
                if next_line_candidate.strip() != '':
                    next_line = next_line_candidate
                    break
                j = j + 1

            # print(f'{next_line=}')
            next_line_html = markdown.markdown(next_line)
            next_line_html = remove_specific_tags(next_line_html, ['u', 'p'])

            replace_image_caption = functools.partial(replace_image, caption=next_line_html)
            line = re_img.sub(replace_image_caption, line)
            result.append(line)
            i = j + 1
            continue

            # print(f'result={line}')
            # print()

        if line.startswith('-'):
            # print(f'{line=}')
            j = i + 1
            # this is enumeration, we don't want spaces there
            while j < num_lines:
                next_line = lines[j].strip()
                # print(f'{next_line=}')
                if next_line.strip() == '':
                    j = j + 1
                else:
                    break

            if not next_line.startswith('-'):
                # the next line is not another list item, so let's add a linebreak
                result.append(line)
                result.append('\n')
                i = j - 1
            else:
                result.append(line)
                i = j

            # print('')
            continue

        if line.startswith('#'):
            line = '#' + line
            result.append(line)
            i = i + 1
            continue

        result.append(line)
        i = i + 1

    result = '\n'.join(result)
    result, _ = re_md_links.subn(r'\1{:target="_blank"}', result)
    return result



def load_and_process(document_path, author, tags):
    post = frontmatter.load(document_path)

    post['title'] = clean_title(post['title'])
    post['subtitle'] = clean_title(post['subtitle'])

    post_id = create_post_id(post['title'])
    post.content = prepare_content(post_id, post.content)

    post['layout'] = 'post'
    post['description'] = post['subtitle']
    post['image'] = f'images/posts/{post_id}/cover.jpg'
    post['authors'] = [author]
    post['tags'] = tags

    post_path = Path(f'_posts/{post_id}.md')

    with post_path.open('wb') as f_out:
        frontmatter.dump(post, f_out)

    return post_id
