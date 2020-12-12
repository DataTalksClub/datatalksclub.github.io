---

title: Book of the Week
description: "Book of the week at DataTalks.Club. Let's talk about books!"
image: images/cover.jpg
layout: page

---

## Book of the Week 

Each week we have a book author coming to DataTalks.Club to answer your questions about their book
and, in general, about the topic of their book.

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