---

title: Open-Source Spotlight
description:
  "Let's talk about open-source"
image: images/cover.jpg
layout: page

---

{% for tool in site.tools %}
<h2>{{ tool.name }}</h2>
<p>
Github: <a href="{{ tool.github }}">Link</a>

Demo: <a href="{{ tool.demo }}">Link</a> by {% include authors.html authors=tool.who %}

<a href="{{ tool.id }}.html">Link</a>

</p>

<br/>
<br/>
{% endfor %}
