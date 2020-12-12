---

title: People of DataTalks.Club
description:
  "DataTalks.Club &ndash; the place to talk about data"
image: images/cover.jpg
layout: page

---

## People
<ul>
  {% for author in site.people %}
    <li><a href="{{ author.id }}.html">{{ author.title }}</a></li>
  {% endfor %}
</ul>