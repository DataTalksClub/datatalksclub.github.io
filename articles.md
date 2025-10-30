---

title: Articles
description: "Explore the latest articles on data science, machine learning, and AI from the DataTalks.Club community. Insights, tutorials, and best practices from industry experts."
image: images/cover.jpg
layout: page

---

# Latest Articles

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.h1 | default: post.title  }}</a> by
    {% for a in post.authors %}
      {% assign author = site.people | where: "short", a | first %}
      <a href="/people/{{a}}.html">{{ author.title }}</a>{% unless forloop.last %}, {% endunless %}
    {% endfor %}
  </li>
{% endfor %}
</ul>