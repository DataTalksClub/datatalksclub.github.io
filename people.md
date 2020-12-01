---

title: Welcome to DataTalks.Club
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: home

---

<div class="row my-5">
  <div class="col-md-8 offset-md-3">
    <h4>People</h4>
    <ul>
      {% for author in site.people %}
        <li><a href="{{ author.id }}.html">{{ author.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
</div>

<div class="row">
  <div class="col">
    {% include subscribe.html subscribe="true" %}
  </div>
</div>