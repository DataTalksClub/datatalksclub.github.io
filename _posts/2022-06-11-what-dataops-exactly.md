---
authors:
- angelicaloduca
description: An overview of DataOps and what makes it different from the other DevOps
  practices.
image: images/posts/2022-06-11-what-dataops-exactly/cover.jpg
layout: post
subtitle: An overview of DataOps and what makes it different from the other DevOps
  practices.
tags:
- dataops
- devops
- engineering
title: What is DataOps exactly?
---

<figure>
<img src="/images/posts/2022-06-11-what-dataops-exactly/image3.jpg"  />
<figcaption>
Photo by <a href="https://unsplash.com/@fabioha?utm_source=medium&amp;utm_medium=referral" target="_blank">fabio</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" target="_blank">Unsplash</a>
</figcaption>
</figure>

It’s hard to overstate the importance of data in modern enterprises. As a new practice, DataOps is aimed at helping organizations overcome obstacles in their data analytics processes. **But what exactly is this emerging practice, and how can it help businesses better leverage their data?** In this article, we’ll explore how important DataOps has become by looking at its various aspects and examining the ways it complements other DevOps and MLOps practices.

The article is organized as follows:

-   What is DataOps

-   The seven steps of DataOps

-   DataOps vs MLOps

-   DataOps tools

## 1 What is DataOps

DataOps is the result of applying DevOps principles to the data lifecycle.

The basic idea of DataOps is, **“if you build a system around that — that automates a lot of the monitoring, deployment, and collaboration—your productivity goes way up, your customers are much happier, and you end up doing better work.”**

DataOps focuses on three processes:

-   **Error Reduction**, which improves your customer's trust in your data. In practice, you should monitor all the software, aiming at checking the stuff that you’re doing.

-   **Cycle Time of Deployment,** which involves how fast you can get new models, new datasets, and new visualizations from your mind into production. This aspect involves both velocity and risk.

-   **Increasing Team Productivity**, with a reduction in the number of meetings and collaboration.

All the previously defined processes are measurable, and you should measure them. For example, you should measure metrics that answer the following questions:

-   How much work is your team doing?

-   How often are things broken?

-   How fast are you getting new things into production?

Those are really important metrics. It’s not so much about data science or data engineering. You always optimize the whole and not just the part. The idea is to show your work to people, get feedback from them, and then iterate on this feedback.

## 2 The seven steps of DataOps

DataOps involves the following seven steps:

<figure>
<img src="/images/posts/2022-06-11-what-dataops-exactly/image1.png"  />
<figcaption></figcaption>
</figure>

-   **Add data to logic tests,** to move from DevOps to DataOps.

-   **Take your code and put it in version control.** Don’t have it on your hard disk somewhere or file share. You could use frameworks such as Github or GitLab.

-   **Branch and Merge**. When you’re changing something in development, run automated tests against that to judge regression or impact analysis. If you change something on the back end, you’re able to tell if the front end is broken in a very simple way.

-   **Write automated tests that run in production**. You should test whether your code behaves as expected or not.

-   **Use multiple environments**. Many developers working on the same project at the production level may lead to conflicts. For this reason, it is important that every team member can work on a local copy of the project.

-   **Reuse and Containerize**. You should reuse your code and make it work independently on your local machine. For this reason, you should wrap your software in containers, such as Docker.

-   **Process Parameterization**, to make your software pipeline flexible to changes.

You can find more information about the seven steps of DataOps at [this link](https://em360tech.com/sites/default/files/2020-07/Data-Kitchen_WP_7Steps_710816A_LR.pdf){:target="_blank"}.

To run your tests, you could use tools such as Great Expectations to run your tests in ways that are simple. However, you can also write tests on your own, in a lot of ways that are pretty simple. For example, you can do row count checks, or you can write SQL queries to do the tests.

So the whole idea is that those tests:

-   should be done automatically,

-   are in version control

-   run during production,

-   are run during development.

In practice, about 10% of your work should be developing automated tests.

## 3 DataOps vs MLOps

What are the differences between DataOps and MLOps? Are they the same thing or different?

There are two answers to that. **From the point of view of an engineer, the answer is no.** It’s the same idea. It’s just DevOps applied to data, so you call it DataOps or MLOps.

**From a more general point of view, the answer is yes.** You can use the term DataOps to encompass the data, the model, the visualization, and the governance. The objective of DataOps is to optimize the whole of that, not just a single part.

More formally, DataOps is the concept of building an organization’s data infrastructure in a way that will allow you to not only perform better as an organization but also be more agile. It’s not just about having good data; it’s about having trustworthy and reliable data.

DataOps can lead to the following benefits:

-   Increased quality of data

-   Increased speed of data

-   Increased efficiency of data

-   Increased accuracy of data

-   Improved consistency (i.e., fewer errors) across teams or departments that are working with the same dataset(s).

The following figure shows the specific focus of Data, Machine Learning, Development, and Operations:

<figure>
<img src="/images/posts/2022-06-11-what-dataops-exactly/image2.png"  />
<figcaption></figcaption>
</figure>

## 4 DataOps tools

DataOps tools automate and simplify all parts of the data life cycle. They increase the agility of data management for organizations and accelerate data analytics for users.

There are four types of DataOps tools:

-   **All-in-One Tools**, which focus on data management, such as data ingestion, transformation, analysis, and visualization.

-   **DataOps Orchestration Tools**, which permit you to manage complex data pipelines in a centralized manner.

-   **Component Tools**, which focus only on a single component of the whole pipeline.

-   **Case-Specific Tools**, which focus on specific domains.

Some popular tools for DataOps include [Great Expectations](https://greatexpectations.io/){:target="_blank"}, [Dataform assertions](https://dataform.co/blog/data-assertions){:target="_blank"}, [Monte Carlo](https://www.montecarlodata.com/){:target="_blank"}, and [dbt tests](https://docs.getdbt.com/docs/building-a-dbt-project/tests){:target="_blank"}.

## Summary

Congratulations! You have just learned the basic concepts behind DataOps!

The DataOps approach can be a powerful tool for any company, and it’s worth taking the time to understand the framework and its benefits. The most important thing to remember is that this practice is about collaboration.

It’s about building a culture where everyone, from engineers to data scientists, works together with their stakeholders in order to produce data-driven results faster and more efficiently.

The content of this article has been inspired by the podcast episode [Storytime for DataOps](https://datatalks.club/podcast/s08e05-storytime-for-dataops.html#the-essence-of-dataops){:target="_blank"} with Christopher Bergh at DataTalks.Club.
