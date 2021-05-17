---

title: DataTalks.Club Conference &ndash; 2021 Summer Marathon 
description:
  DataTalks.Club 2021 Summer Marathon &ndash; two weeks of awesomness.
image: images/cover.jpg
layout: page

tracks:
  - name: Career in Data
    eventbrite: 153177531119
    youtube: NA
    talks:
      - speaker: svpino
        name: "From Software Engineering to Machine Learning"
        date: 2021-06-14 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: dalianaliu
        name: "The Next Level of Your Data Science Career"
        date: 2021-06-15 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: andreaskretz
        name: "Build Your Own Data Pipeline"
        date: 2021-06-16 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: roksolanadiachuk
        name: "Big Data Engineer vs Data Scientist"
        date: 2021-06-17 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: elenasamuylova
        name: "I Want to Build a Machine Learning Startup!"
        date: 2021-06-18 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
  - name: Machine Learning in Production
    eventbrite: 153178006541
    youtube: NA
    talks:
      - speaker: janzawadzki
        name: "Setting Up AI Projects for Success"
        date: 2021-06-21 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: benwilson
        name: "Running from Complexity"
        date: 2021-06-22 17:00:00
        eventbrite: TBA
        abstract:
          TBA.
      - speaker: linaweichbrodt
        name: "Humans in the Loop"
        date: 2021-06-23 17:00:00
        eventbrite: TBA
        abstract:
          How to navigate users, stakeholders and your own biases in MLOps
      - speaker: dougturnbull
        name: "Why Your Search Relevance Project Will Fail"
        date: 2021-06-24 17:00:00
        eventbrite: TBA
        abstract:
          "We should just feed our user’s clicks into an ML model, teaching it to rank what’s clicked more...
          Right? Well not so fast! Transforming search clickstream data into usable training data can be
          a daunting task. Without careful, systematic study, we can easily create a negative feedback loop
          where clicks strengthen the existing poor search experience.<br><br>

          I’ve led and participated in dozens of search relevance projects. Poor training data is the #1
          reason relevance and machine learning projects fail.<br><br>

          In this talk, I’ll cover the core biases in search clickstream data and what to do about it.
          You’ll see how to systematically overcome biases due to low traffic and how you display results.
          With a good foundation in place, then the sky is the limit for how much you can grow, tune,
          or machine-learn relevance: having an impact beyond the test/training split!"
      - speaker: fabianaclemente
        name: "The Importance of Data Quality"
        date: 2021-06-25 17:00:00
        eventbrite: TBA
        abstract:
          TBA.


partners:
  - name: O'Reilly Media
    link: https://www.oreilly.com/
    image: "/images/partners/oreilly.jpg"
  - name: MLOps.community
    link: https://mlops.community/
    image: "/images/partners/mlops-community.jpg"

---


### DataTalks.Club 2021 Summer Marathon

* Two weeks of awesomness
* It's online and entirely free!
* Can't attend? Register anyways, we will send you the recordings.


<h2>Tracks</h2>

<ul>
{% for track in page.tracks %}
  <li>
    <a href="#{{ track.name | slugify }}">{{ track.name}}</a>
  </li>
{% endfor %}
</ul>

{% for track in page.tracks %}
<h2 id="{{ track.name | slugify }}">{{ track.name}}</h2>

<div class="conference-talks">
{% for talk in track.talks %}
  {% assign speaker = site.people | where: "short", talk.speaker | first %}
  <div class="talk-wrap d-flex">
    <div class="talk-speaker-img-container">
      <img class="talk-speaker-img" src="/{{speaker.picture}}" />
    </div>
    <div class="talk-details">
      <span class="datetime">{{ talk.date | date: "%A, %d %B at %H:%M" }} CET</span>
      <h2>{{talk.name}}</h2>
      <h3 class="speaker-name">— <a href="/people/{{talk.speaker}}.html" target="_blank">{{ speaker.title }}</a></h3>
      <span class="toggle-abscract"><a href="javascript:void();" onclick="toggle('{{ talk.name | slugify }}')">Show abstract</a></span>
      <div class="talk-absctract" id="{{ talk.name | slugify }}" style="display: none;">{{ talk.abstract }}</div>
    </div>
  </div>
{% endfor %}
</div>

<center class="my-3">
<button class="btn btn-secondary btn-lg" id="eventbrite-widget-modal-trigger-{{ track.eventbrite }}" type="button">
  <i class="fas fa-check"></i> Register
</button>
</center>

{% endfor %}



<script src="https://www.eventbrite.com/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
  var exampleCallback = function() {
      console.log('Order complete!');
  };

  {% for track in page.tracks %}
  window.EBWidgets.createWidget({
      widgetType: 'checkout',
      eventId: '{{ track.eventbrite }}',
      modal: true,
      modalTriggerElementId: 'eventbrite-widget-modal-trigger-{{ track.eventbrite }}',
      onOrderComplete: exampleCallback
  });
  {% endfor %}

  function toggle(name) {
    var x = document.getElementById(name);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
</script>
