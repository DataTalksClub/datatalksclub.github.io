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
              <a href="/people/{{a}}.html">{{ author.name }}</a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
        </li>
      {% endfor %}
    </ul>

  </div>
</div>

