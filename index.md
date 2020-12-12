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
    <h4>Latest articles</h4>
    <ul>
      {% for post in site.posts %}
        <li>
          <a href="{{ post.url }}">{{ post.title }}</a> by
            {% for a in post.authors %}
              {% assign author = site.people | where: "short", a | first %}
              <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </li>
      {% endfor %}
    </ul>
      
    <p>&nbsp;</p>

    {% assign upcoming = site.data.events
      | where_exp: "event", "event.time > site.time"
      | sort: 'time'  %}
    <h4>Upcoming events</h4>
    <ul>
      {% for event in upcoming %}
        <li>
          <a href="{{ event.link }}" target="_blank">{{ event.title }}</a> on {{ event.time | date_to_string }} by
            {% for a in event.speakers %}
              {% assign author = site.people | where: "short", a | first  %}
              <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </li>
      {% endfor %}
    </ul>

    <p>Check <a href="/events.html">events</a> for the all past events.</p>

    <p>&nbsp;</p>

    <h4>Book of the week</h4>
    {% assign books = site.books 
        | where_exp: "book", "book.end > site.time"
        | sort: 'end' %}
    <ul>
      {% for book in books %}
        <li>
          <a href="{{ book.url }}">{{ book.title }}</a> by
            {% for a in book.authors %}
              {% assign author = site.people | where: "short", a | first  %}
              <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </li>
      {% endfor %}
    </ul>

    <p>Check the <a href="/books.html">book of the week</a> page for more books!</p>
  </div>
</div>

