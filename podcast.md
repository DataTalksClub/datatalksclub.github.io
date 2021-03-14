---

title: DataTalks.Club Podcast
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## Podcast

<div class="pod-badges">
  <div class="pod-badge-container">
    <a href="https://podcasts.apple.com/us/podcast/id1541710331" target="_blank">
      <img class="pod-badge" src="/images/podcast/badges/apple-podcasts.svg" />
    </a>
  </div>
  <div class="pod-badge-container">
    <a href="https://open.spotify.com/show/0pck8zuiXdI0OrCg86DAPy" target="_blank">
      <img class="pod-badge" src="/images/podcast/badges/spotify.svg" />
    </a>
  </div>
  <div class="pod-badge-container">
    <a href="https://www.youtube.com/c/DataTalksClub" target="_blank">
      <img class="pod-badge" src="/images/podcast/badges/youtube.svg" />
    </a>
  </div>
  <div class="pod-badge-container">
    <a href="https://anchor.fm/datatalksclub" target="_blank">
      <img class="pod-badge" src="/images/podcast/badges/anchor.svg" />
    </a>
  </div>
</div>

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