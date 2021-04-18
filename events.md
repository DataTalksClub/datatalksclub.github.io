---

title: Events
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## Events


We host multiple types of events:

<ul class="emoji-list">
<li class="webinar">Webinars &ndash; events on Tuesday, with slides, mostly technical</li>
<li class="podcast">Live podcasts &ndash; events on Friday, a discussion without slides, the recording is published as a podcast</li>
<li class="conference">Conference &ndash; bigger events with multipe talks, both webinar-type talks and podcast-type talks</li>
</ul>


{% assign upcoming = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time > site.time"
  | sort: 'time' %}

{% if upcoming %}
## Upcoming events

<ul class="emoji-list">
  {% for event in upcoming %}
    <li class="{{ event.type }}">
      <a href="{{ event.link }}" target="_blank">{{ event.title }}</a> on {{ event.time | date_to_string }} by
        {% include authors.html authors=event.speakers %}
    </li>
  {% endfor %}
</ul>
{% endif %}


📅 Pro tip: you can also subscribe to [our Google calendar](https://calendar.google.com/calendar/?cid=ZjhxaWRqbnEwamhzY3A4ODA5azFlZ2hzNjBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ){:target="_blank"}
to get notified about all our events (subscribing works from desktop only).


{% assign past = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time <= site.time"
  | sort: 'time'
  | reverse %}

{% if past %}
## Past events

<ul class="emoji-list">
  {% for event in past %}
    <li class="{{ event.type }}">
      {{ event.title }} by {% include authors.html authors=event.speakers %}
        (<a href="{{ event.youtube }}" target="_blank">watch on youtube</a>{% if event.anchor %}, <a href="{{ event.anchor }}" target="_blank">listen on anchor.fm</a>{% endif %})
    </li>
  {% endfor %}
</ul>
{% endif %}
