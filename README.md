## DataTalks.Club Website

### Running Jekyll locally
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