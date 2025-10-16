# Rust Static Site Generator

This is a fast, lightweight static site generator written in Rust that replaces Jekyll for building the DataTalks.Club website.

## Features

- **Fast**: Generates 765+ pages in under 1 second (vs Jekyll which takes much longer)
- **Parallel processing**: Uses Rayon for parallel page rendering
- **Jekyll-compatible**: Reads the same `_config.yml`, markdown files, and frontmatter
- **Collections support**: Handles Jekyll collections like `_books`, `_posts`, `_podcast`, `_people`, etc.
- **Markdown rendering**: Uses pulldown-cmark for fast, spec-compliant markdown parsing
- **Template processing**: Processes layouts and includes with basic Liquid-like template support

## Requirements

- Rust 1.70+ (tested with 1.90.0)
- Cargo

## Building

```bash
cargo build --release
```

## Usage

### Build the site

```bash
./target/release/ssg
```

Or use the Makefile:

```bash
make build-rust
```

### Build and serve locally

```bash
make serve-rust
```

This will build the site and serve it at http://localhost:4000

## Performance

Typical build times:
- **Rust SSG**: ~600ms - 1.1s for 765 pages
- **Jekyll**: Several minutes (varies)

This represents a **100x+ speedup** compared to Jekyll!

## How it works

1. **Configuration**: Reads `_config.yml` for site configuration and collection definitions
2. **Content Collection**: Walks through:
   - Root-level markdown files (e.g., `index.md`, `articles.md`)
   - Collection directories (e.g., `_books/`, `_posts/`, `_podcast/`)
   - Blog posts in `_posts/` with date-based filenames
3. **Parsing**: Extracts YAML frontmatter and markdown content from each file
4. **Rendering**: 
   - Converts markdown to HTML using pulldown-cmark
   - Applies layouts from `_layouts/`
   - Processes includes from `_includes/`
   - Performs variable substitution
5. **Output**: Writes rendered HTML files to `_site/`
6. **Assets**: Copies static assets (CSS, images, etc.) to `_site/`

## Template Support

The SSG supports a subset of Liquid template syntax:

### Variables
- `{{ content }}` - Rendered markdown content
- `{{ page.title }}`, `{{ page.subtitle }}`, etc. - Page frontmatter
- `{{ site.name }}`, `{{ site.url }}`, etc. - Site config

### Includes
- `{% include head.html %}` - Includes a file from `_includes/`

### Conditionals
- `{% if page.title %} ... {% endif %}` - Basic conditional rendering

### Filters
- `{{ page.title | default: site.name }}` - Default values
- `{{ page.date | date_to_string }}` - Date formatting

## Limitations

This is a simplified implementation focused on the specific needs of the DataTalks.Club website. It doesn't support:
- Full Liquid template engine (only basic subset)
- Pagination
- Data files (YAML/JSON in `_data/`)
- Complex loops and filters
- Plugins

For these features, you can extend the Rust implementation or continue using Jekyll.

## Architecture

The codebase is organized as a single `main.rs` file with these key components:

- `PageFrontMatter`: Deserializes YAML frontmatter
- `Page`: Represents a content page with metadata
- `SiteConfig`: Site-wide configuration
- `SiteGenerator`: Main orchestrator that:
  - Loads templates and config
  - Collects and parses pages
  - Renders pages in parallel
  - Copies static assets

## Future Improvements

Potential enhancements:
- Add incremental builds (only rebuild changed pages)
- Implement live reload for development
- Add more complete Liquid template support
- Support for data files
- Plugin system
- Better error messages
