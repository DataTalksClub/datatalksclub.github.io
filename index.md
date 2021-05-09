---

title: Welcome to DataTalks.Club
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: home

---

<hr />

<div class="row">
  <div class="col title">
    <h1>The place to talk about data</h1>
    <h2>A community of aspiring and experienced data enthusiasts</h2>
  </div>
</div>

{% include subscribe-main.html %}

<hr />

<div class="row my-3">
  <div class="col-md-8 offset-md-2">
    {% assign upcoming = site.data.events
      | where_exp: "event", "event.draft != true"
      | where_exp: "event", "event.time > site.time"
      | sort: 'time'  %}
    <h4>Upcoming events</h4>
    <ul class="emoji-list">
      {% for event in upcoming %}
        <li class="{{ event.type }}">
          <a href="{{ event.link }}" target="_blank">{{ event.title }}</a> on {{ event.time | date_to_string }} by
          {% include authors.html authors=event.speakers %}
        </li>
      {% endfor %}
    </ul>

    <p>Check <a href="/events.html">events</a> for all past events. You can also subscribe to <a href="https://calendar.google.com/calendar/?cid=ZjhxaWRqbnEwamhzY3A4ODA5azFlZ2hzNjBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ" target="_blank">our Google calendar</a> to get notified about all our events.</p>
    <p>&nbsp;</p>

    {% assign episodes = site.podcast
      | sort: 'episode'
      | sort: 'season'
      | reverse %}
    <h4>Latest podcast episodes</h4>
    <ul>
      {% for episode in episodes limit: 5%}
        <li><a href="{{ episode.id }}.html">{{ episode.title }}</a> with 
          {% include authors.html authors=episode.guests %}</li>
      {% endfor %}
    </ul>

    <p>Check the <a href="/podcast.html">podcast</a> page for all past podcast episodes.</p>

    <p>&nbsp;</p>

    <h4>Book of the week</h4>
    {% assign books = site.books 
        | where_exp: "book", "book.end > site.time"
        | sort: 'end' %}
    <ul>
      {% for book in books %}
        <li>
          <a href="{{ book.id }}.html">{{ book.title }}</a> by {% include authors.html authors=book.authors %}
            ({{ book.start | date_to_string }} &ndash; {{ book.end | date_to_string }})
        </li>
      {% endfor %}
    </ul>

    <p>Check the <a href="/books.html">book of the week</a> page for more books!</p>
    
    <p>&nbsp;</p>

    <h4>Latest articles</h4>
    <ul>
      {% for post in site.posts %}
        <li>
          <a href="{{ post.url }}">{{ post.title }}</a> by
            {% include authors.html authors=post.authors %}
        </li>
      {% endfor %}
    </ul>

  </div>
</div>
