---

title: DataTalks.Club Podcast
description: "DataTalks.Club weekly podcast episodes with data science experts, ML engineers, and AI researchers. Listen on Apple Podcasts, Spotify, YouTube."
image: images/cover.jpg
layout: page

---

# Podcast

<div class="podcast-intro">
  <p>Listen to conversations with data science experts, machine learning practitioners, and AI researchers. Subscribe to stay updated with the latest episodes.</p>
</div>

<section class="podcast-platforms" aria-labelledby="platforms-heading">
  <h2 class="platforms-heading">Listen to or watch on your favorite platform</h2>
  <div class="platforms-chips-wrapper">
    <a href="https://podcasts.apple.com/us/podcast/id1541710331" target="_blank" rel="noopener noreferrer" class="chip-platform">
      <img src="https://cdn.prod.website-files.com/64416928859cbdd1716d79ce/6477a7c7ea921d6b17e8336c_icon-platform-apple-podcasts.webp" alt="Apple Podcasts icon" class="chip-platform-icon"/>
      <div>Apple Podcasts</div>
    </a>
    <a href="https://open.spotify.com/show/0pck8zuiXdI0OrCg86DAPy" target="_blank" rel="noopener noreferrer" class="chip-platform">
      <img src="https://cdn.prod.website-files.com/64416928859cbdd1716d79ce/6477a7c8fe3abf5dc324b071_icon-platform-spotify.webp" alt="Spotify icon" class="chip-platform-icon"/>
      <div>Spotify</div>
    </a>
    <a href="https://www.youtube.com/c/DataTalksClub" target="_blank" rel="noopener noreferrer" class="chip-platform">
      <img src="https://cdn.prod.website-files.com/64416928859cbdd1716d79ce/6477a7c7df55dac86621aa7f_icon-platform-youtube.webp" alt="YouTube icon" class="chip-platform-icon"/>
      <div>YouTube</div>
    </a>
    <a href="https://anchor.fm/datatalksclub" target="_blank" rel="noopener noreferrer" class="chip-platform">
      <img src="/images/podcast/badges/anchor-icon.jpg" alt="Anchor icon" class="chip-platform-icon"/>
      <div>Anchor</div>
    </a>
  </div>
</section>

{% assign all_seasons = site.podcast | map: 'season' | uniq | sort | reverse %}


<section class="podcast-info">
<br/>
  <p>Register for upcoming podcast events in <a href="/events.html" target="_blank" rel="noopener noreferrer">events</a>.</p>
</section>

<section class="podcast-episodes" aria-labelledby="episodes-heading">
  <h2 id="episodes-heading" class="sr-only">All Podcast Episodes</h2>
  
  {% for season_num in all_seasons %}
    {% assign season_episodes = site.podcast | where: 'season', season_num | sort: 'episode' | reverse %}
    <section class="season" aria-labelledby="season-{{ season_num }}-heading">
      <h3 id="season-{{ season_num }}-heading">Season #{{ season_num }}</h3>
      <ul class="emoji-list">
        {% for episode in season_episodes %}
          <li class="episode-item" itemscope itemtype="https://schema.org/PodcastEpisode">
            <a href="{{ episode.id }}.html" itemprop="url" title="Listen to: {{ episode.title }}">
              <span itemprop="name">{{ episode.title }}</span>
            </a> with
            <span itemprop="associatedMedia">
              {% include authors.html authors=episode.guests %}
            </span>
          </li>
        {% endfor %}
      </ul>
    </section>
  {% endfor %}
</section>