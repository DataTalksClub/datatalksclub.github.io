---
authors:
- valeriiakuka
description: Learn MLOps principles and take your projects from the notebook to production
  in 9 weeks
image: images/posts/2024-03-07-mlops-zoomcamp/image9.png
layout: post
subtitle: Learn MLOps principles and take your projects from the notebook to production
  in 9 weeks
tags:
- courses
- mlops
title: MLOps Zoomcamp
---

In this article, we take a closer look at the MLOps Zoomcamp, a free nine-week course that covers practical aspects of productionizing ML services — from training and experimenting to model deployment and monitoring. It is perfect for people who plan to work with ML services at any stage.

We will describe different aspects of this course so you can learn more about it:

-   Key course features
-   Who is the course for?
-   Course curriculum
-   Course project for your portfolio
-   Course assignments
-   Learning in public
-   DataTalks.Club community



> The next cohort of the course starts on 13 May (Monday), 2024. If you’re ready to join, sign up [here](https://airtable.com/appYdhA23GVZd1iN2/shrCb8y6eTbPKwSTL){:target="_blank"}.

### Why is it important?

MLOps (machine learning operations) is becoming a must-know skill for many data professionals. With all the noise around that topic, it might be difficult to find one source covering the basics of each stage of the MLOps cycle and giving you the practical knowledge you could apply to your work.

That's why DataTalks.Club created the free MLOps course. It is practical and focused, designed to help you take your projects from the notebook to production.

### Key features of MLOps Zoomcamp

-   Comprehensive Curriculum: The course explores each part of the entire MLOps cycle
-   Hands-On Project: A final project to apply the skills learned from the course and enhance your portfolio
-   Diverse materials: Video lectures, code samples, and community notes. Weekly homework for practice.
-   Supportive community: Course channel in Slack to ask questions and interact with peers and instructors.
-   Expert Instructors: Cristian Martinez, Alexey Grigorev, Emeli Dral, and others.



### Who is the course for?

This course is for:

-   Data scientists
-   ML engineers
-   Software developers who are interested in understanding MLOps, the process of putting machine learning code in production.



MLOps involves transitioning the raw code from a development environment into a deployed model within a live service, including stages for performance monitoring and problem-solving.

Before we get into the details, it’s important to know what skills you should have to follow the course comfortably.

Here are the main prerequisites for the course:

-   Prior programming experience (at least 1+ year)
-   Prior exposure to machine learning (at work or from other courses, e.g. from [ML Zoomcamp](https://datatalks.club/blog/machine-learning-zoomcamp.html){:target="_blank"})

-   Being comfortable with the command line
-   Python
-   Docker (you can check [ML Zoomcamp](https://datatalks.club/blog/machine-learning-zoomcamp.html){:target="_blank"} for that)

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image5.png"  />
<figcaption><a href="https://github.com/DataTalksClub/machine-learning-zoomcamp">GitHub repository</a> of the course</figcaption>
</figure>

## Course Curriculum

The course curriculum is structured to guide you step-by-step through each stage of the MLOps cycle starting from experimentation and model selection to model deployment to monitoring. You’ll spend the first six weeks learning and practicing each part of the MLOps cycle. In the concluding two weeks, you will apply your acquired knowledge and skills to develop an [end-to-end machine learning project](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/07-project){:target="_blank"}.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image2.png"  />
<figcaption>Course Curriculum</figcaption>
</figure>

-   Week 1: Introduction & Prerequisites
-   Week 2: Experiment tracking and model management
-   Week 3: Orchestration and ML Pipelines
-   Week 4: Model Deployment
-   Week 5: Model Monitoring
-   Week 6: Best Practices
-   Weeks 7, 8, 9: Project



Let's quickly go over each week, focusing on the main points and the tech you'll use.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image4.png"  />
<figcaption>Course <a href="https://www.youtube.com/live/hwtdTrBp6TA?si=5P7u2BbQh2deIyI3">opening presentation</a> from the previous cohort</figcaption>
</figure>

### Week 1: Introduction & Prerequisites

**Tech**: Docker, AWS

**Focus**: Week 1 is dedicated to setting up the key tools and technologies you'll be using throughout the course and introducing you to the concept of MLOps and why we need to use that concept.

### Week 2: Experiment tracking and model management

**Tech**: MLFlow

**Focus**: Week 2 covers experiment tracking to store and organize relevant information about your experiments. For example, the input data, source code, model architecture parameters, and corresponding outputs of the model.

### Week 3: Orchestration and ML Pipelines

**Tech**: Mage

Focus: Week 3 focuses on creating a production-ready pipeline for training machine learning models. It means that the pipeline is easily reproduced, and re-run, in a fully automated way.

### Week 4: Model Deployment

**Tech**: Flask, Docker, MLflow, Mage, AWS Lambda & AWS Kinesis

**Focus**: Week 4 introduces you to the three ways of model deployment and gives you a demonstration of how to work with each of them.

### Week 5: Model Monitoring

Tech: Prometheus, Evidently AI, and Grafana

**Focus**: Week 5 is about monitoring machine learning models including service health, model performance, data quality and integrity, and data Drift & concept drift.

### Week 6: Best Practices

**Tech**: Python, Docker, Localstack, Github Actions

**Focus**: Week 6 summarizes the best practices like unit tests, integration tests, checking code quality, and automating deployments with CI/CD and GitHub Actions.

### Weeks 7, 8, 9: Project

**Duration**: 2 weeks for development, 1 week for peer review

**Objective**: The project focuses on applying your acquired skills to build a data engineering pipeline from scratch. Completing this hands-on project not only validates your skills but also enhances your portfolio, offering a competitive edge in job searches.

**Peer Review**: To complete the project, you are required to evaluate projects from at least three of your peers. Failure to do so will result in your project being marked as incomplete. For detailed peer review criteria, check this [link](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/07-project){:target="_blank"}.

**Project Requirements**:

-   Choose a dataset of interest
-   Train a model on the selected dataset and track your experiments
-   Develop a pipeline for model training
-   Deploy the model in a batch, as a web service, or in a streaming format
-   Monitor your model's performance
-   Adhere to best practices



<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image6.png"  />
<figcaption>Star history of the <a href="https://github.com/DataTalksClub/mlops-zoomcamp/tree/main">MLOps Zoomcamp GitHub repository</a></figcaption>
</figure>

> To support us, star the repository of the MLOps Zoomcamp. You can do it [here](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main){:target="_blank"}.

The [course description](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main){:target="_blank"} on GitHub provides a detailed overview of the topics covered each week. You can see the video lectures, slides, code, and community notes for each week of the course to dive into the content. By the end of the course, you will have acquired the fundamental skills necessary for a career as a data engineer.

> If you’re ready to join the next cohort of the course, submit this [form](https://airtable.com/appYdhA23GVZd1iN2/shrCb8y6eTbPKwSTL){:target="_blank"} to register and stay updated.

## Course assignments and scoring

### Homework and getting feedback

To reinforce your learning, you can submit a homework assignment at the end of each week. Your scores are added to an anonymous leaderboard, creating friendly competition among course members and motivating you to do your best.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image1.png"  />
<figcaption>The leaderboard with scored homework</figcaption>
</figure>

For support, we have an [FAQ](https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit){:target="_blank"} section with quick answers to common questions. If you need more help, [our Slack community](https://datatalks.club/slack.html){:target="_blank"} is always available for technical questions, clarifications, or guidance. Additionally, we host live Q&A sessions called "office hours" where you can interact with instructors and get immediate answers to your questions.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image8.png"  />
<figcaption>A screenshot of a <a href="https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit">FAQ document</a></figcaption>
</figure>

### Learning in public approach

A unique feature is our "learning in public" approach, inspired by [Shawn @swyx Wang](https://www.youtube.com/watch?v=tkBCPqWKCL8&list=PL7NIGf5_PlM-Dk3lgPsZFT94Ng7PpRQEh&index=5&t=195s){:target="_blank"}'s [article](https://www.swyx.io/learn-in-public){:target="_blank"}. We believe that everyone has something valuable to contribute, regardless of their expertise level.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image10.png"  />
<figcaption>An extract from Shawn @swyx Wang's article about learning in public</figcaption>
</figure>

Throughout the course, we actively encourage and incentivize learning in public. By sharing your progress, insights, and projects online, you earn additional points for your homework and projects.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image3.png"  />
<figcaption>Anonymous leaderboard from the previous cohort of the course. On the right, you can see the bonus points for learning in public</figcaption>
</figure>

This not only demonstrates your knowledge but also builds a portfolio of valuable content. Sharing your work online also helps you get noticed by social media algorithms, reaching a broader audience and creating opportunities to connect with individuals and organizations you may not have encountered otherwise.

## DataTalks.Club community

DataTalks.Club has a supportive community of like-minded individuals in [our Slack](https://datatalks.club/slack.html){:target="_blank"}. It is the perfect place to enhance your skills, deepen your knowledge, and connect with peers who share your passion. These connections can lead to lasting friendships, potential collaborations in future projects, and exciting career prospects.

<figure>
<img src="/images/posts/2024-03-07-mlops-zoomcamp/image7.png"  />
<figcaption>Course channel in <a href="https://datatalks.club/slack.html">our Slack community</a></figcaption>
</figure>

## Conclusion

The MLOps Zoomcamp offers a comprehensive and hands-on approach to mastering the essentials of machine learning operations. It provides a solid foundation for anyone looking to integrate ML services into real-world applications. Whether you’re looking to enhance your portfolio, boost your career prospects, or simply deepen your understanding of MLOps, this course can help you achieve your goals.

Again, the next cohort starts on 13 May (Monday), 2024. You can [register](https://airtable.com/appYdhA23GVZd1iN2/shrCb8y6eTbPKwSTL){:target="_blank"} for the MLOps Zoomcamp now.