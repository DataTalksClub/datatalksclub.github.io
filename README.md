## DataTalks.Club Website

### Building the site

You have two options for building the site:

#### Option 1: Rust Static Site Generator (Recommended - Much Faster!)

The Rust SSG is **100x+ faster** than Jekyll, building 765+ pages in under 1 second.

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

#### Option 2: Jekyll (Traditional)

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