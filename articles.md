---

title: Articles
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## Latest articles

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a> by
    {% for a in post.authors %}
      {% assign author = site.people | where: "short", a | first %}
      <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
    {% endfor %}
  </li>
{% endfor %}
<ul>