---

title: Welcome to DataTalks.Club
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: img/image.jpg
layout: home

---

<div class="row my-5">
  <div class="col-md-8 offset-md-3">
    <h4>Latest articles</h4>
    <ul>
      {% for post in site.posts %}
        <li>
          <a href="{{ post.url }}">{{ post.title }}</a> by {{ post.author }}
        </li>
      {% endfor %}
    </ul>

  </div>
</div>


<div class="row">
  <div class="col">
    {% include subscribe.html subscribe="true" %}
  </div>
</div>