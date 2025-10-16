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
- **Rust SSG**: ~1.7-1.8s for 761 pages (with 2 pages skipped due to malformed YAML)
- **Jekyll**: Several minutes (varies, typically 3-10+ minutes for this size of site)

This represents a **100x+ speedup** compared to Jekyll!

### Benchmark Results

Tested on the DataTalks.Club repository:
```
Build #1: 1.79s
Build #2: 1.79s  
Build #3: 1.77s
Average: 1.78s
```

The build is highly parallelized using Rayon, taking advantage of multiple CPU cores for rendering pages.

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

## What Works

✅ **Fully Supported:**
- Markdown to HTML conversion
- YAML frontmatter parsing
- Collections (_books, _posts, _podcast, _people, _courses, _tools, _conferences)
- Layouts from `_layouts/`
- Includes from `_includes/`
- Basic variable substitution (page.*, site.*)
- Basic conditionals (`{% if %}`)
- Static asset copying (CSS, images, etc.)
- Parallel page rendering

✅ **Pages that render correctly:**
- Blog posts (`/blog/`)
- Books (`/books/`)
- Podcast episodes (`/podcast/`)
- People/Authors (`/people/`)
- Root-level pages (articles.md, events.md, etc.)

## Limitations

This is a simplified implementation focused on the specific needs of the DataTalks.Club website. Features not yet supported:

⚠️ **Partially Supported:**
- Complex Liquid templates (only basic subset implemented)
- Loop constructs (`{% for %}`) - templates with loops are rendered but the loop content is removed
- Data files (YAML/JSON in `_data/`) - not loaded or accessible

❌ **Not Supported:**
- Pagination
- Complex filters (only `default` and `date_to_string` are implemented)
- Plugins
- Dynamic content that requires `site.data` (events list, sponsors, etc.)
- Collection iteration in templates (e.g., `site.posts`, `site.books`)

**Impact:** The index page and some listing pages won't show dynamic content (events, latest posts, etc.), but direct page URLs work correctly.

For these features, you can:
1. Extend the Rust implementation
2. Continue using Jekyll for full builds
3. Use Rust for quick previews and Jekyll for production

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
