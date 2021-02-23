---

title: DataTalks.Club Podcast
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## Podcast

* [Apple podcast](https://podcasts.apple.com/us/podcast/id1541710331){:target="_blank"}
* [Spotify](https://open.spotify.com/show/0pck8zuiXdI0OrCg86DAPy){:target="_blank"}
* [Anchor.fm](https://anchor.fm/datatalksclub){:target="_blank"}
* [RSS](https://anchor.fm/s/41286f68/podcast/rss){:target="_blank"}

{% assign seasons = site.podcast | reverse | group_by: 'season'  %}

Register for upcoming podcast events in <a href="/events.html" target="_blank">events</a>.

{% for season in seasons %}

<h3>Season: {{ season.name }}</h3>

<ul>
  {% for episode in season.items %}
    <li><a href="{{ episode.id }}.html">{{ episode.title }}</a> by
      {% include authors.html authors=episode.guests %}</li>
  {% endfor %}
</ul>

{% endfor %}