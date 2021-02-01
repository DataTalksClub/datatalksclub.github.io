## DataTalks.Club Website

### Running Jekyll locally
Use ruby 2.7.0:

```
rvm use ruby-2.7.0

gem install bundler
```

Running it for the first fime:

```
bundle install
```

Running Jekyll:

```
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000)


### Generating a cover image

Build the docker image for the cover generator:

```bash
cd previews
docker build -t datatalks-cover-generator .
cd ..
```

Now let's generate the image:

* the article: `_posts/2020-12-07-practical-guide-better-code.md`
* the output file: `images/posts/2020-12-07-practical-guide-better-code/cover.jpg`

```bash
./scripts/generate-post-preview.sh 2021-02-01-landing-product-analyst-job
```

Book cover:

```bash
./scripts/generate-book-preview.sh 20210301-ml-engineering
```