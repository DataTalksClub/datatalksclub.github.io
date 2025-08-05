---
authors:
- valeriiakuka, serenahaidar
description: 'Interview with ML Zoomcamp grad Serena Haidar: practical lessons, getting
  unstuck, and the impact of the final project'
image: images/posts/2025-08-05-key-lessons-from-ml-zoomcamp-serena-haidar/cover.jpg
layout: post
subtitle: 'Interview with ML Zoomcamp grad Serena Haidar: practical lessons, getting
  unstuck, and the impact of the final project'
tags:
- course
- ml-zoomcamp
title: 'Key Lessons from ML Zoomcamp: Serena Haidar'
---

DataTalks.Club’s [ML Zoomcamp](https://datatalks.club/blog/machine-learning-zoomcamp.html){:target="_blank"} is a free, four-month online course on machine-learning fundamentals and deploying models to production.

In our previous article, we covered graduate Serena Haidar’s end-to-end capstone. In this follow-up, she shares key lessons, study pace, how to get unstuck, and how the program shaped her approach to ML engineering.

## Key Lessons Learned

### Could you tell us a bit about your background and the moment you decided to join ML Zoomcamp?

**Serena**: Sure! I study computer and communications engineering (CCE) at college. While much of my coursework focuses on electronics, communications systems, and network protocols, I have always been moer drawn to math and programming. When I discovered the field of machine learning, I instantly knew it was the area I wanted to pursue.

When I discovered the course in September 2024, I didn’t have any hands-on experience with machine learning. The course only required basic knowledge of Python and a willingness to learn. I checked out the [course’s repository](https://github.com/DataTalksClub/machine-learning-zoomcamp#syllabus){:target="_blank"}, and I liked how organized and detailed everything was. The topics ranged from the basics of data pre-processing to building models and finally deploying them, so I decided to join right away.

### What are the key practical lessons for ML that you’ve learned from this course?

**Serena:** I’d say I have 3 main takeaways from this course:

**1. Leverage a cloud provider:** Training deep‑learning models demands significant compute and often parallel workflows. By using a cloud platform, I can spin up GPU or TPU instances on demand, run experiments in parallel, and scale resources up or down as needed.

2\. **Start from a pre‑trained backbone:** Rather than building and training a model from scratch, I used a pre‑trained network. This way, I only needed to fine‑tune the final layers for specific waste classes. It drastically cuts training time, reduces data requirements, and lets me focus on optimizing performance rather than reinventing basic feature extractors.

**3. Begin with reduced image dimensions:** To iterate quickly, first train on smaller input sizes (for example, 128×128 or 224×224 pixels). This speeds up each epoch, allowing me to identify promising architectures and hyperparameter settings. Once I’ve narrowed down the best candidates, I scale up to full resolution for final tuning and production‑ready performance.

## Advice For the Next Cohort

### What study pace do you recommend for the next cohort?

**Serena:** Aim to complete one module per week. This steady rhythm gives you enough time to absorb the material, apply each lesson in hands‑on exercises, submit the homework, and benefit from the practical tips shared at every stage.

### What learning outcomes can you expect by following that pace?

**Serena:** You’ll develop a solid understanding of every step in exploratory data analysis (EDA) and model training. More importantly, you’ll immediately put those concepts into practice through weekly homework and two to three real‑world projects.

### What should you do if you ever feel stuck?

**Serena:** First, check the [course’s public repository](https://github.com/DataTalksClub/machine-learning-zoomcamp){:target="_blank"} for comprehensive notes. If you need more clarification, rewatch the [YouTube lectures](https://youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&si=VHtM9Eia-PWQakVx){:target="_blank"}. Every topic is explained clearly in the ML Zoomcamp material. In my experience, external resources were rarely necessary because the curriculum covers everything you need.

<figure>
<img src="/images/posts/2025-08-05-key-lessons-from-ml-zoomcamp-serena-haidar/image2.png"  />
<figcaption>ML Zoomcamp public repository: <a href="https://github.com/DataTalksClub/machine-learning-zoomcamp">https://github.com/DataTalksClub/machine-learning-zoomcamp</a></figcaption>
</figure>

## Course Impact

### What foundational skills did this course give you for new machine learning projects?

**Serena:** The course provided me with the essential information I need to approach any new machine learning project. I can now build and deploy an end‑to‑end ML solution: from choosing the dataset all the way through Dockerization.

From the very first module, the course laid out the machine‑learning lifecycle you need to follow on every project. Each subsequent video offered valuable insights and concrete, actionable steps. So if you dedicate the time and keep your goal in mind, you’ll know exactly what to do next.

### What was your personal goal in taking this course? Have you achieved them?

**Serena:** My goal was to deepen my understanding of ML to land a job or a research position after I graduate from university. The course’s clear road map, from theory to deployment, helped me move confidently toward that objective. I learned a great deal and am continuing my learning journey with a solid foundation.

### What aspects of the Zoomcamp’s design stood out to you?

**Serena:** This zoomcamp is very well designed. It motivated me to join the [LLM Zoomcamp](https://datatalks.club/blog/llm-zoomcamp.html){:target="_blank"} in its next cohort. One of the best aspects is that the material is free and publicly accessible; you receive high-quality education in a structured format, with detailed short videos, and access to notebooks and code files. Additionally, you can easily [ask questions on Slack](https://datatalks.club/slack.html){:target="_blank"}, add your notes to the public repository, and benefit from others' notes, which makes the courses much more interactive.

<figure>
<img src="/images/posts/2025-08-05-key-lessons-from-ml-zoomcamp-serena-haidar/image1.png"  />
<figcaption>ML Zoomcamp course channel on Slack</figcaption>
</figure>

### How did peer interaction contribute to your learning?

**Serena:** Reviewing other people’s projects was one of the most interesting parts. Seeing different approaches taught me new techniques, and getting actionable feedback on my own work helped me improve quickly.

### Would you recommend this course to others?

**Serena:** Yes! If you’re willing to put in the effort, this bootcamp offers a structured, hands-on path through ML, with community support and real-world project reviews to keep you on track.

What makes this course stand out is its focus on practice over theory, the projects where you apply everything you've learned, and most importantly, the deployment phase, which is rarely covered in other courses but is crucial in real-world scenarios. This course teaches you to see the bigger picture and implement ML solutions that truly benefit users and businesses.

Thank you, Serena!