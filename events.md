---

title: Events
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: home

---

{% assign upcoming = site.data.events | where: "finished", false %}
{% assign past = site.data.events | where: "finished", true %}

<div class="row my-5">
  <div class="col-md-8 offset-md-3">
    <p>For the full list of our events, check our page on <a href="https://www.eventbrite.com/o/datatalksclub-31603209675" target="_blank">Eventbrite</a>.</p>

    {% if upcoming %}
    <h4>Upcoming events</h4>
    <ul>
      {% for event in upcoming %}
        <li>
          <a href="{{ event.link }}" target="_blank">{{ event.title }}</a> on {{ event.date }} by
            {% for a in event.speakers %}
              {% assign author = site.people | where: "short", a | first  %}
              <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </li>
      {% endfor %}
    </ul>
    {% endif %}

    {% if past %}
    <h4>Past events</h4>
    <ul>
      {% for event in past %}
        <li>
          {{ event.title }} by
            {% for a in event.speakers %}
              {% assign author = site.people | where: "short", a | first %}
              <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
            (<a href="{{ event.youtube }}" target="_blank">watch on youtube</a>{% if event.anchor %}, <a href="{{ event.anchor }}" target="_blank">listen on anchor.fm</a>{% endif %})
        </li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
</div>


<div class="row">
  <div class="col">
    {% include subscribe.html subscribe="true" %}
  </div>
</div>