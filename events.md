---

title: Events
description: "Join our data science events including webinars, live podcasts, workshops, and conferences. Connect with experts and learn about the latest trends in data, ML, and AI."
image: images/cover.jpg
layout: page

---

# Events

We host multiple types of events to help you learn and connect with the data science community:

<section class="event-types" aria-labelledby="event-types-heading">
  <h2 id="event-types-heading" class="sr-only">Types of Events</h2>
  <ul class="emoji-list">
    <li class="webinar">Webinars &ndash; events on Tuesday, with slides, mostly technical</li>
    <li class="podcast">Live podcasts &ndash; events on Friday, a discussion without slides, the recording is published as a podcast</li>
    <li class="workshop">Workshop &ndash; hands-on tutorials about technical topics</li>
    <li class="conference">Conference &ndash; bigger events with multiple talks, both webinar-type talks and podcast-type talks</li>
  </ul>
</section>

> 📅 <b>Pro tip</b>: you can also subscribe to [our Google calendar](https://calendar.google.com/calendar/?cid=ZjhxaWRqbnEwamhzY3A4ODA5azFlZ2hzNjBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ){:target="_blank"}
to get notified about all our events (subscribing works from desktop only).

{% assign upcoming = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time > site.time"
  | sort: 'time' %}

{% if upcoming %}
## Upcoming events

<section class="upcoming-events" aria-labelledby="upcoming-events-heading">
  <h2 id="upcoming-events-heading" class="sr-only">Upcoming Events</h2>
  <ul class="emoji-list">
    {% for event in upcoming %}
      <li class="{{ event.type }}">
        {% include event.html event=event speakers=true %}
      </li>
    {% endfor %}
  </ul>
</section>
{% endif %}


{% assign past = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time <= site.time"
  | sort: 'time'
  | reverse %}

{% if past %}
## Past events

<section class="past-events" aria-labelledby="past-events-heading">
  <h2 id="past-events-heading" class="sr-only">Past Events</h2>
  <ul class="emoji-list">
    {% for event in past %}
      <li class="{{ event.type }}">{% include event.html event=event speakers=true %}</li>
    {% endfor %}
  </ul>
</section>
{% endif %}
