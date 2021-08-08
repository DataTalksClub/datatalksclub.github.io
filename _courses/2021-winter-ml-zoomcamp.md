---

title: Machine Learning Zoomcamp (2021) 
description: Learn machine learning engineering in 4 months in a free online course
image: images/cover.jpg
layout: page

schedule:
  - title: "Lesson 1: Introduction to Machine Learning"  
    start: 2021-09-06 17:00:00
    content:
      - Course overview and logistics 
      - Understanding machine learning and the problems it can solve    
      - "CRISP-DM: Organizing a successful machine learning project"
    homework:
      content:
        - point 1
        - point 2
      due: 2021-09-12 12:00:00
  - title: "Lesson 1: Introduction to Machine Learning"  
    start: 2021-09-06 17:00:00
    content:
      - Course overview and logistics 
      - Understanding machine learning and the problems it can solve    
      - "CRISP-DM: Organizing a successful machine learning project"
    homework:
      content:
        - point 1
        - point 2
      due: 2021-09-12 12:00:00

---


* Each week, there’s a lecture and a homework assignment. 
* We have two projects: in the middle of the class and a capstone project at the end. Those who complete these two projects get a certificate. 
* For homework, projects and other activities, you’ll get scores. At the end, we’ll publish the list of top 100 participants on our website.


[Register here](https://airtable.com/shr6Gz46UZCgJ9l6w){:target="_blank"}


(the form and this document will be published to DataTalks.Club website)

Join [#course-ml-zoomcamp](https://app.slack.com/client/T01ATQK62F8/C0288NJ5XSA){:target="_blank"} channel in Slack (register in Slack [here](/slack.html){:target="_blank"})



<h2>Plan</h2>

<ul>
{% for item in page.schedule %}
  <li>
    <a href="#{{ track.name | slugify }}">{{ item.title }}</a>
  </li>
{% endfor %}
</ul>