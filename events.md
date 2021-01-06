---

title: Events
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## Events


We host two types of events:

* Presentations &ndash; events on Tuesday, with slides, mostly technical
* Live podcasts &ndash; events on Friday, a discussion without slides, the recording is published as a podcast


For the full list of our events, check our page on <a href="https://www.eventbrite.com/o/datatalksclub-31603209675" target="_blank">Eventbrite</a>

{% assign upcoming = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time > site.time"
  | sort: 'time' %}

{% if upcoming %}
## Upcoming events

<ul>
  {% for event in upcoming %}
    <li>
      <a href="{{ event.link }}" target="_blank">{{ event.title }}</a> on {{ event.time | date_to_string }} by
        {% include authors.html authors=event.speakers %}
    </li>
  {% endfor %}
</ul>
{% endif %}


{% assign past = site.data.events
  | where_exp: "event", "event.draft != true"
  | where_exp: "event", "event.time < site.time"
  | sort: 'time'
  | reverse %}

{% if past %}
## Past events

<ul>
  {% for event in past %}
    <li>
      {{ event.title }} by {% include authors.html authors=event.speakers %}
        (<a href="{{ event.youtube }}" target="_blank">watch on youtube</a>{% if event.anchor %}, <a href="{{ event.anchor }}" target="_blank">listen on anchor.fm</a>{% endif %})
    </li>
  {% endfor %}
</ul>
{% endif %}
