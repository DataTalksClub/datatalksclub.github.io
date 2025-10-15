---

title: People of DataTalks.Club
description: "Meet the data science experts, authors, and speakers of DataTalks.Club. Connect with professionals in machine learning, AI, and data engineering from our global community."
image: images/cover.jpg
layout: page

---

# People

<div class="people-summary">
  <p>Discover <strong>{{ site.people.size }}</strong> data science professionals, authors, and experts from our global community.</p>
</div>

<section class="people-list" aria-labelledby="people-heading">
  <h2 id="people-heading" class="sr-only">All Community Members</h2>
  <ul class="people-grid">
    {% for author in site.people %}
      <li class="person-item" itemscope itemtype="https://schema.org/Person">
        <a href="{{ author.id }}.html" itemprop="url" title="Learn more about {{ author.title }}">
          <span itemprop="name">{{ author.title }}</span>
        </a>
      </li>
    {% endfor %}
  </ul>
</section>