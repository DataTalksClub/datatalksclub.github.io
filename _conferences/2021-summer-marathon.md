---

title: DataTalks.Club Conference &ndash; 2021 Summer Marathon 
description:
  DataTalks.Club 2021 Summer Marathon &ndash; two weeks of awesomness.
image: images/other/conference-2021-summer-marathon-cover.jpg
layout: page

tracks:
  - name: Career in Data
    eventbrite: 153177531119
    youtube: NA
    talks:
      - speaker: svpino
        name: "From Software Engineering to Machine Learning"
        date: 2021-06-14 17:00:00
        eventbrite: 156360377097
        abstract:
          "You’re more qualified than you think!<br/><br/>
          <ul>
            <li>Why software engineers are already qualified to do machine learning</li>
            <li>Core tools and frameworks</li>
            <li>Learning plan for the transition</li>
          </ul>"
      - speaker: dalianaliu
        name: "The Next Level of Your Data Science Career"
        date: 2021-06-15 17:00:00
        eventbrite: 156383548403
        abstract:
          TBA
      - speaker: andreaskretz
        name: "Build Your Own Data Pipeline"
        date: 2021-06-16 17:00:00
        eventbrite: 156383644691
        abstract:
          "Become a better data scientist by learning data engineering<br/><br/>
          <ul>
            <li>Learning to build data pipelines for data scientist </li>
            <li>Which tools and technologies I need to learn</li>
            <li>Stream vs batch</li>
          </ul>"
      - speaker: roksolanadiachuk
        name: "Big Data Engineer vs Data Scientist"
        date: 2021-06-17 17:00:00
        eventbrite: 156383773075
        abstract:
          "<ul>
            <li>Skills big data engineers and data scientists have</li>
            <li>Tools that they use</li>
            <li>How big data engineers and data scientists can work together</li>
            <li>Walkthrough of an project from idea to production</li>
          </ul>"
      - speaker: elenasamuylova
        name: "I Want to Build a Machine Learning Startup!"
        date: 2021-06-18 17:00:00
        eventbrite: 156461405275
        abstract:
          "<ul>
            <li>Things to consider when building a startup</li>
            <li>Getting ideas</li>
            <li>Open source vs closed source</li>
          </ul>"
  - name: Machine Learning in Production
    eventbrite: 153178006541
    youtube: NA
    talks:
      - speaker: janzawadzki
        name: "Setting Up AI Projects for Success"
        date: 2021-06-21 17:00:00
        eventbrite: 157373360959
        abstract:
          TBA
      - speaker: benwilson
        name: "Running from Complexity"
        date: 2021-06-22 17:00:00
        eventbrite: 157377603649
        abstract:
          "Simplicity is the key to keeping your models running in production<br/><br/>
          <ul>
            <li>Why our projects don’t make to production</li>
            <li>Dangers of siloed projects</li>
            <li>Implementing novel algorithms for solving our problems - pros and cons </li>
            <li>Is it a good idea to be an early technology adopter?</li>
          </ul>"
      - speaker: linaweichbrodt
        name: "Humans in the Loop"
        date: 2021-06-23 17:00:00
        eventbrite: 157377701943
        abstract:
          Navigating users, stakeholders and your own biases in MLOps
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
          TBA

partners:
  - name: AICamp
    link: https://www.aicamp.ai/
    image: "/images/partners/aicamp.png"
  - name: The New Stack
    link: https://thenewstack.io/
    image: "/images/partners/thenewstack.png"
  - name: MLOps.community
    link: https://mlops.community/
    image: "/images/partners/mlops-community.jpg"
  - name: "PyData London"
    link: https://www.meetup.com/PyData-London-Meetup/
    image: "/images/partners/pydata-london.png"

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
      <div class="talk-absctract" id="{{ talk.name | slugify }}" style="display: none;">
        {{ talk.abstract }}
        {% if talk.eventbrite != 'TBA' %}<br/>
        <a href="https://eventbrite.com/e/{{ talk.eventbrite }}" target="_blank">Register just for this talk</a>
        {% endif %}
        </div>
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


## Event community partners

<div class="text-center row">
{% for partner in page.partners %}
  <div class="my-3 col-md-6">
    <a href="{{ partner.link }}" target="_blank">
      <img src="{{ partner.image }}" class="partner"/>
    </a>
  </div>
{% endfor %}
</div>


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
