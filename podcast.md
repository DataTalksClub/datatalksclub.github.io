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
  <h2 id="platforms-heading" class="sr-only">Listen on Your Favorite Platform</h2>
  <div class="pod-badges">
    <div class="pod-badge-container">
      <a href="https://podcasts.apple.com/us/podcast/id1541710331" target="_blank" rel="noopener noreferrer" aria-label="Listen on Apple Podcasts">
        <img class="pod-badge" src="/images/podcast/badges/apple-podcasts.svg" alt="Apple Podcasts" />
      </a>
    </div>
    <div class="pod-badge-container">
      <a href="https://open.spotify.com/show/0pck8zuiXdI0OrCg86DAPy" target="_blank" rel="noopener noreferrer" aria-label="Listen on Spotify">
        <img class="pod-badge" src="/images/podcast/badges/spotify.svg" alt="Spotify" />
      </a>
    </div>
    <div class="pod-badge-container">
      <a href="https://www.youtube.com/c/DataTalksClub" target="_blank" rel="noopener noreferrer" aria-label="Watch on YouTube">
        <img class="pod-badge" src="/images/podcast/badges/youtube.svg" alt="YouTube" />
      </a>
    </div>
    <div class="pod-badge-container">
      <a href="https://anchor.fm/datatalksclub" target="_blank" rel="noopener noreferrer" aria-label="Listen on Anchor">
        <img class="pod-badge" src="/images/podcast/badges/anchor.svg" alt="Anchor" />
      </a>
    </div>
  </div>
</section>

{% assign seasons = site.podcast | reverse | group_by: 'season'  %}

<section class="podcast-info">
  <p>Register for upcoming podcast events in <a href="/events.html" target="_blank" rel="noopener noreferrer">events</a>.</p>
</section>

<section class="podcast-episodes" aria-labelledby="episodes-heading">
  <h2 id="episodes-heading" class="sr-only">All Podcast Episodes</h2>
  
  {% for season in seasons %}
    <section class="season" aria-labelledby="season-{{ season.name }}-heading">
      <h3 id="season-{{ season.name }}-heading">Season #{{ season.name }}</h3>
      <ul class="emoji-list">
        {% for episode in season.items %}
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