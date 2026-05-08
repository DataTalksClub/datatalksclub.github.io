RUSTKYLL_VERSION ?= v0.4.6
RUSTKYLL_ASSET ?= rustkyll-linux-amd64
RUSTKYLL_INSTALL_DIR ?= .bin
RUSTKYLL ?= $(RUSTKYLL_INSTALL_DIR)/rustkyll
RUSTKYLL_BUILD_FLAGS ?=
RUSTKYLL_SERVE_FLAGS ?=

.PHONY: help install serve build clean run runinc people books podcast events all doc

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install dependencies
	mkdir -p $(RUSTKYLL_INSTALL_DIR)
	curl -fsSL -o $(RUSTKYLL) https://github.com/alexeygrigorev/rustkyll/releases/download/$(RUSTKYLL_VERSION)/$(RUSTKYLL_ASSET)
	chmod +x $(RUSTKYLL)

serve: ## Start the development server (http://localhost:4000)
	$(RUSTKYLL) serve --no-watch $(RUSTKYLL_SERVE_FLAGS)

build: ## Build the site for production
	$(RUSTKYLL) build $(RUSTKYLL_BUILD_FLAGS)

clean: ## Remove generated site and caches
	rm -rf _site .rustkyll-manifest.json

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

run: serve

runinc: serve
