---

title: Welcome to DataTalks.Club
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: home

---

<hr />

<div class="row mt-5 my-3">
  <div class="col-md-6 offset-md-4">
    Are you looking for a place where you can

    <ul>
      <li>Learn more about applied machine learning</li>
      <li>Talk about data engineering and machine learning engineering</li>
      <li>Discuss career options</li>
      <li>Attend weekly events</li>
      <li>Ask any question</li>
    </ul>

    Then DataTalks.Club is the place for you! Join our Slack group!
  </div>
</div>

<div class="row">
  <div class="col">
    {% include subscribe.html subscribe="true" %}
  </div>
</div>

<hr />

<div class="row my-5">
  <div class="col-md-8 offset-md-3">
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

    <p>Check <a href="/events.html">events</a> for all past events.</p>

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
