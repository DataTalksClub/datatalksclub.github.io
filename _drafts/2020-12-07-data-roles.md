---
layout: post
title: "Roles in a Data Team"
subtitle: ""
description: "In this article, we'll talk about different roles in a data team and discuss their responsibilities."
image: "images/2020-11-29-segmentation/cover.jpg"
authors: [alexeygrigorev]
tags: [team, process, podcast]
---

In this article, we'll talk about different roles in a data team and discuss their responsibilities.

In particular, we will cover:

* The types of roles in a data team;
* The responsibilities of each role;
* The skills and knowledge each role needs to have.

> Want to listen to it as a podcast? Go to [anchor.fm](https://anchor.fm/datatalksclub/episodes/Roles-in-a-data-team---Alexey-Grigorev-emqcft) or your favorite podcasting platfrom.


This is not a comprehensive list and the majority of what you will read in this article is my opinion, which comes out of my experience from working as a data scientist.

You can interpret the following information as “the description of data roles from the perspective of a data scientist”. For example, my views on the role of a data engineer may be a bit simplified because I don't see all the complexities of their work firsthand. I do hope you will find this information useful nonetheless.


## Roles in a Team

A typical data team consists of the following roles:

* Product managers,
* Data analysts,
* Data scientists,
* Data engineers,
* Machine learning engineers, and
* Site reliability engineers / MLOps engineers.



## The data team

All these people work to create a data product.

To explain the core responsibilities of each role, we will use a case scenario:


Suppose we work at an online classifieds company. It’s a platform where users can go to sell things they don't need (like OLX, where I work). If a user has an iPhone they want to sell — they go to this website, create a listing and sell their phone.


On this platform, sellers sometimes have problems with identifying the correct category for the items they are selling. To help them, we want to build a service that suggests the best category. To sell their iPhone, the user creates a listing and the site needs to automatically understand that this iPhone has to go in the “mobile phones” category.


<img src="/images/2020-12-07-data-roles/category-suggestion.png" />
Use case: we want to build a service that automatically identifies the correct category for a listing.


Let’s start with the first role: product manager.

## Product Manager

A product manager is someone responsible for developing products. Their goal is to make sure that the team is building the right thing. They are typically less technical than the rest of the team: they don’t focus on the implementation aspects of a problem, but rather the problem itself.



<img src="/images/2020-12-07-data-roles/pm.png" />

A product manager makes sure the team builds a product that users will use.


Product managers need to ensure that the product is actually used by the end-users. This is a common problem: in many companies, engineers create something that doesn’t solve real problems. Therefore, the product manager is somebody who speaks to the team on behalf of the users.


The primary skills a PM needs to have are communication skills. For data scientists, communication is a soft skill, but for a product manager — it’s a hard skill. They have to have it to perform their work.


Product managers also do a lot of planning: they need to understand the problem, come up with a solution, and make sure the solution is implemented in a timely manner. To accomplish this, PMs need to know what's important and plan the work accordingly.


When somebody has a problem, they approach the PM with it. Then the task of the PM is to figure out if users actually need this feature, how important this feature is, and if the team has the capacity to implement it.


Let’s come back to our example. Suppose somebody comes to the PM and says:


“We want to build a feature to automatically suggest the category for a listing. Somebody's selling an iPhone, and we want to create a service that predicts that the item goes in the mobile phones category.”


Product managers need to answer these questions:

* “Is this feature that important to the user?”
* “Is it an important problem to solve in the product at all?”

To answer these questions, PMs ask data analysts to help them figure out what to do next.

## Data Analyst

Data analysts know how to analyze the data available in the company. They discover insights in the data and then explain their findings to others.


<img src="/images/2020-12-07-data-roles/analyst.png" />


So, analysts need to know:

* What kind of data the company has;
* How to get the data;
* How to interpret the results;
* How to explain their findings to colleagues and management.
 

Data analysts are also often responsible for defining key metrics and building different dashboards. This includes things like showing the company’s profits, displaying the number of listings, or how many contacts buyers made with sellers.  Thus, data analysts should know how to calculate all the important business metrics, and how to present them in a way that is understandable to others.


When it comes to skills, data analysts should know:

* SQL — this is the main tool that they work with;
* Programming languages such as Python or R;
* Tableau or similar tools for building dashboards;
* Basics of statistics;
* How to run experiments;
* A bit of machine learning, such as regression analysis, and time series modeling.

For our example, product managers turn to data analysts to help them quantify the extent of the problem. Together with the PM, the data analyst tries to answer questions like:

* “How many users are affected by this problem?”
* “How many users don’t finish creating their listing because of this problem?”
* “How many listings are there on the platform that don't have the right category selected?”


<img src="/images/2020-12-07-data-roles/pm-da-example.png" />


After the analyst gets the data, analyzes it and answers these questions, they may conclude: “Yes, this is actually a problem”. Then the PM and the team discuss the repost and agree: “Indeed, this problem is actually worth solving”.


Now the data team will go ahead and start solving this problem.

After the model for the service is created, it’s necessary to understand if the service is effective: whether this model helps people and solves the problem. For that, data analysts usually run experiments — usually, A/B tests.


When running an experiment, we can see if more users successfully finish posting an item for sale or if there are fewer ads that end up in the wrong category.

## Data Scientist

The roles of a data scientist and data analyst are pretty similar. In some companies, it's the same person who does both jobs. However, data scientists typically focus more on predicting rather than explaining.


A data analyst fetches the data, looks at it, explains what’s going on to the team, and gives some recommendations on what to do about it. A data scientist, on the other hand, focuses more on creating machine learning services. For example, one of the questions that a data scientist would want to answer is “How can we use this data to build a machine learning model for predicting something?”


<img src="/images/2020-12-07-data-roles/ds.png" />



In other words, data scientists incorporate the data into the product. Their focus is more on engineering than analysis. Data scientists work more closely with engineers on integrating data solutions into the product.


The skills of data scientists include:

* Machine learning — the main tool for building predictive services;
* Python — the primary programming language;
* SQL — necessary to fetch the data for training their models;
* Flask, Docker, and similar — to create simple web services for serving the models.

For our example, the data scientists are the people who develop the model used for predicting the category. Once they have a model, they can develop a simple web service for hosting this model.

## Data Engineers

Data engineers do all the heavy lifting when it comes to data. A lot of work needs to happen before data analysts can go to a database, fetch the data, perform their analysis, and come up with a report. This is precisely the focus of data engineers — they make sure this is possible. Their responsibility is to prepare all the necessary data in a form that is consumable for their colleagues.



<img src="/images/2020-12-07-data-roles/de.png" />


To accomplish this, data engineers create "a data lake". All the data that users generate needs to be captured properly and saved in a separate database. This way, analysts can run their analysis, and data scientists can use this data for training models.


Another thing data engineers often need to do, especially at larger companies, is to ensure that the people who look at the data have the necessary clearance to do so. Some user data is sensitive and people can’t just go looking around at personal information (such as emails or phone numbers) unless they have a really good reason to do so. Therefore, data engineers need to set up a system that doesn't let people just access all the data at once.


The skills needed for data engineers usually include:

* AWS or Google Cloud — popular cloud providers;
* Kubernetes and Terraform — infrastructure tools;
* Kafka or RabbitMQ — tools for capturing and processing the data;
* Databases — to save the data in such a way that it's accessible for data analysts;
* Airflow or Luigi — data orchestration tools for building complex data pipelines.

In our example, a data engineer prepares all the required data. First, they make sure the analyst has the data to perform the analysis. Then they also work with the data scientist to prepare the information that we’ll need for training the model. That includes the title of the listing, its description, the category, and so on.


A data engineer isn’t the only type of engineer that a data team has. There are also machine learning engineers.

## Machine Learning Engineer

Machine learning engineers take whatever data scientists build and help them scale it up. They also ensure that the service is maintainable and that the team follows the best engineering practices. Their focus is more on engineering than on modeling.


<img src="/images/2020-12-07-data-roles/ds-mle.png" />


The skills ML engineers have are similar to that of data engineers:

* AWS or Google Cloud;
* Infrastructure tools like Kubernetes and Terraform;
* Python and other programming languages;
* Flask, Docker, and other tools for creating web services.

Additionally, ML engineers work closely with more “traditional” engineers, like backend engineers, frontend engineers, or mobile engineers, to ensure that the services from the data team are included in the final product.


For our example, ML engineers work together with data scientists on productionizing the category suggestion services. They make sure it's stable once it's rolled out to all the users. They must also ensure that it's maintainable and it's possible to make changes to the service in the future.


There's another kind of engineer that can be pretty important in a data team — site reliability engineers.

## DevOps / Site Reliability Engineer

The role of SREs is similar to the ML engineer, but the focus is more on the availability and reliability of the services.


SREs aren’t strictly limited to working with data. Their role is more general: they tend to focus less on business logic and more on infrastructure, which includes things like networking and provisioning infrastructure.

<img src="/images/2020-12-07-data-roles/mle-sre.png" />


Therefore, SREs look after the servers where the services are running and take care of collecting all the operational metrics like CPU usage, how many requests per second there are, the services’ processes, and so on.


As the name suggests, site reliability engineers have to make sure that everything runs reliably. They set up alerts and are constantly on call to make sure that the services are up and running without any interruptions. If something breaks, SREs quickly diagnose the problem and fix it, or involve an engineer to help find the solution.


The skills needed for site reliability engineers:

* Cloud infrastructure tools;
* Programming languages like Python,
* Unix/Linux;
* Networking;
* Best DevOps practices like automation, CI/CD, and the like.

Of course, ML engineers and data engineers should also know these best practices, but the focus of DevOps engineers/SREs is to establish them and make sure that they are followed.


There is a special type of DevOps engineer, called “MLOps engineer”.

## MLOps Engineer

An MLOps engineer is a DevOps engineer who also knows the basics of machine learning. Similar to an SRE, the responsibility of an MLOps Engineer is to make sure that the services, developed by data scientists, ML engineers, and data engineers, are up and running all the time.


MLOps engineers know the lifecycle of a machine learning model: the training phase, serving phase, and so on.


Despite having this knowledge, MLOps Engineers are still focused more on operational support than on anything else. This means that they need to know and follow all the DevOps practices and make sure that the rest of the team is following them as well. They accomplish this by setting up things like continuous retraining, and CI/CD pipelines.



Even though everyone in the team has a different focus, they all work together on achieving the same goal: solve the problems of the users.  

## Summary

To summarize, the roles in the data team and their responsibilities are:

* Product managers — make sure that the team is building the right thing, act as a gateway to all the requests and speak on behalf of the users.
* Data analysts — analyze data, define key metrics, and create dashboards.
* Data scientists — build models and incorporate them into the product.
* Data engineers — prepare the data for analysts and data scientists.
* ML engineers — productionize machine learning services and establish the best engineering practices.
* Site reliability engineers — focus on availability, reliability, enforce the best DevOps practices.

This list is not comprehensive, but it should be a good starting point if you are just getting into the industry, or if you just want to know how the lines between different roles are defined in the industry.

<div class="article-divider"></div>

This article is based on the podcast "Roles in a data team". You can watch it on YouTube: 

{% include youtube.html video_id="2ZOnA19sDpM" %}

Or listen to audio: 

<iframe src="https://anchor.fm/datatalksclub/embed/episodes/Roles-in-a-data-team---Alexey-Grigorev-emqcft/a-a3to8hl" height="102px" width="400px" frameborder="0" scrolling="no"></iframe>