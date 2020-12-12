---

title: Book of the Week
description: "Book of the week at DataTalks.Club. Let's talk about books!"
image: images/cover.jpg
layout: page

---

## Book of the Week 

Each week we have a book author coming to DataTalks.Club to answer your questions about their book
and, in general, about the topic of their book.

* Register at DataTalks.Club
* Join the `#book-of-the-week` channel in our Slack
* Ask as many questions as you'd like
* The book authors answer questions from Monday till Thursday
* On Friday, the authors decide who wins free copies of their book

## Upcoming books

{% assign upcoming = site.books 
  | where_exp: "book", "book.end > site.time"
  | sort: 'end' %}

<div class="books">
{% for book in upcoming %}
  {% include book.html book=book %}
{% endfor %}
</div>


## Archive

Nothing here yet