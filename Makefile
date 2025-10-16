people:
	uv run python scripts/airtable.py people

books:
	uv run python scripts/airtable.py books

podcast:
	uv run python scripts/airtable.py podcast

events:
	uv run python scripts/airtable.py events

all: people books podcast events

doc:
	uv run python scripts/pandoc_google_doc.py -i

run:
	bundle exec jekyll serve

runinc:
	bundle exec jekyll serve --incremental