people:
	pipenv run python scripts/airtable.py people

books:
	pipenv run python scripts/airtable.py books

podcast:
	pipenv run python scripts/airtable.py podcast

events:
	pipenv run python scripts/airtable.py events

all: people books podcast events

run:
	bundle exec jekyll serve

runinc:
	bundle exec jekyll serve --incremental