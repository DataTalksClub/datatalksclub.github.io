## DataTalks.Club Website

### Building the site

You have two options for building the site:

#### Option 1: Rust Static Site Generator (Recommended for Development - Much Faster!)

The Rust SSG is **100x+ faster** than Jekyll, building 761 pages in ~1.8 seconds.

**Best for:**
- Quick local development and testing
- Previewing content changes
- Fast iteration cycles

**Limitations:**
- Index page and listing pages won't show dynamic content (events, latest posts)
- Direct page URLs work correctly

```bash
# Build the site
cargo build --release
./target/release/ssg

# Or use the Makefile
make build-rust

# Build and serve locally at http://localhost:4000
make serve-rust
```

See [SSG_README.md](SSG_README.md) for more details.

#### Option 2: Jekyll (Traditional - For Production)

Use Jekyll for production builds with full feature support including dynamic listings.

**Best for:**
- Production deployments
- Full dynamic content support
- Complex template features

Use ruby 2.7.0:

```
rvm use ruby-2.7.0

gem install bundler
```

Running it for the first time:

```
bundle install
```

Running Jekyll:

```
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000)


## Scripts 

Installing the requirements:

```bash
uv sync

cd previews
npm install
cd ..
```

Running:

```bash
uv run python scripts/create.py
``` 

### Generating post from docx

```bash
uv run python scripts/pandoc_full.py \
    --input ~/Downloads/template.docx \
    --author angelicaloduca \
    --tags "mlops,devops,process"
```