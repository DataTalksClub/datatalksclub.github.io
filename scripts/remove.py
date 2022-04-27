import subprocess
from glob import glob

import questionary


def extract_filenames(path):
    path = path.replace('\\', '/')
    filename = path.split('/')[-1]
    return filename


def remove_book():
    books = glob('./_books/*.md')
    books = [extract_filenames(b) for b in books]
    books = [b for b in books if not b.startswith('_')]
    books = sorted(books)[::-1]
    
    last_10 = books[:10]

    choices = [book[:-3] for book in last_10]

    book = questionary.select(
        "Which book would you like to remove?",
        choices=choices,
    ).ask()

    if book is None:
        return

    print(f'removing {book}...')

    subprocess.call(['git', 'rm', f'_books/{book}.md'])
    subprocess.call(['git', 'rm', '-rf', f'images/books/{book}/'])

    commit_push = questionary.select(
        "Do you want to commit and push?",
        choices=['Yes', 'No'],
    ).ask()

    if commit_push == 'Yes':
        subprocess.call(['git', 'commit', '-m', f'remove {book}'])
        subprocess.call(['git', 'push'])



def main():
    actions = {
        'Book': remove_book,
        # 'Event': create_event, 
        # 'Article': create_article,
        # 'Person': create_person
    }

    what = questionary.select(
        "What do you want to remove?",
        choices=actions.keys(),
    ).ask()

    action = actions[what]
    action()

if __name__ == '__main__':
    main()