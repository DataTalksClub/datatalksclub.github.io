---

title: Book of the Week
description: "Discover the latest books in data science, machine learning, and AI. Join our weekly book discussions with authors at DataTalks.Club and win free copies of featured books."
image: images/cover.jpg
layout: page

---

# Book of the Week 

Each week we have a book author coming to DataTalks.Club to answer your questions about their book
and, in general, about the topic of their book.

## How it works

* [Register on DataTalks.Club](/slack.html){:target="_blank"}
* Join the `#book-of-the-week` channel in our Slack
* Ask as many questions as you'd like
* The book authors answer questions from Monday till Thursday
* On Friday, the authors decide who wins free copies of their book

## Upcoming books

{% assign upcoming = site.books 
  | where_exp: "book", "book.end > site.time"
  | sort: 'end' %}

<section class="upcoming-books" aria-labelledby="upcoming-heading">
  <h2 id="upcoming-heading" class="sr-only">Upcoming Book Discussions</h2>
  <div class="books">
    {% for book in upcoming %}
      {% include book.html book=book %}
    {% endfor %}
  </div>
</section>

## Archive

{% assign past = site.books 
  | where_exp: "book", "book.end < site.time"
  | sort: 'end'
  | reverse %}

<section class="book-archive" aria-labelledby="archive-heading">
  <h2 id="archive-heading" class="sr-only">Past Book Discussions</h2>
  <ul>
    {% for book in past %}
    <li>
      <a href="{{ book.id }}.html">{{ book.title }}</a> by
        {% include authors.html authors=book.authors %}
        (from {{ book.start | date_to_string }} to {{ book.end | date_to_string }})
    </li>
    {% endfor %}
  </ul>
</section>
