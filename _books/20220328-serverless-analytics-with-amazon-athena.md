---
authors:
- anthonyvirtuoso
cover: images/books/20220328-serverless-analytics-with-amazon-athena/cover.jpg
description: Book of the Week. Serverless Analytics with Amazon Athena by Anthony
  Virtuoso
end: 2022-04-01 23:59:59
image: images/books/20220328-serverless-analytics-with-amazon-athena/preview.jpg
links:
- link: https://www.packtpub.com/product/serverless-analytics-with-amazon-athena/9781800562349
  text: Book's page
- link: https://www.amazon.com/Serverless-Analytics-Amazon-Athena-semi-structured/dp/1800562349/ref=sr_1_1?dchild=1&keywords=Serverless+Analytics+with+Amazon+Athena&qid=1634629990&sr=8-1
  text: Buy on Amazon
- link: https://github.com/PacktPublishing/Serverless-Analytics-with-Amazon-Athena
  text: GitHub repository
start: 2022-03-28 00:00:00
title: Serverless Analytics with Amazon Athena

archive:
- name: adanai
  text: 'Hello Anthony, thank you for the QnA! I am relatively new to AWS and working
    to specialize in Analytics+ML in AWS.

    What level of experience in AWS is expected when starting with this book?'
  replies:
  - name: Anthony Virtuoso (Author)
    text: as long as you have an AWS account, basic SQL knowledge, and know how to
      modify IAM policies you can do everything in this book. We tried to really make
      it accessible to beginners and intermediate folks alike. Only one or two chapters
      at the end are a bit more advanced and do require comfort with developing java
      code.
- name: adanai
  text: What does an ETL pipeline look like? What are the components in it and why
    does Athena primitively not require one(or avoids it)?
  replies:
  - name: Anthony Virtuoso (Author)
    text: In this case we typically mean that you do not need to run jobs/queries
      that read literally ALL your data and then rearrange it or pre-join it with
      other data to make it either (a) small enough (b) in the right format or (c)
      denormalized across data sources. These techniques can still be helpful with
      Athena, but Athena does its best to still make data that is no well organized,
      optimized, or formated using best practices accessible without all the upfront
      work/maintenance of ETL
- name: adanai
  text: Would I, as a book reader, need to incur costs in executing the examples in
    this book?
  replies:
  - name: Anthony Virtuoso (Author)
    text: Yes, we typically mention it in the chapters but while authoring the book
      we spent &lt; $30 total on AWS fees and keep in mind we had to run through the
      exercises 5 or 6 times to refine them.
- name: adanai
  text: "I recently started learning about and working with Tableau (small data -\
    \ 100K records). All I did was click and drop elements and write a few queries\
    \ for calculated fields. The results seemed satisfactory.\n What are the ways\
    \ in which the Athena integration make working with Tableau better? Is it the\
    \ scale that makes the difference?"
  replies:
  - name: Anthony Virtuoso (Author)
    text: Aside from the visualizations that you get with Tableu I think youll find
      the experience with Athena is pretty similar with one key difference being that
      if you ever need to scale up from 100k records to 100Billion or somewhere in
      between Athena will handle that just as well and you might start to see other
      differentiation in terms of price and performance as you scale up. But id agree
      that at 100k records, probably even Excel can used for a bunch of quick analysis.
- name: Rui Ramos
  text: Hi, reinforcing adanai question. What would be the level of expertise required
    in AWS to start on this book ? Also does the book contains any use-cases for the
    usage of this service ? Are there practical examples to tryout ?
  replies:
  - name: Anthony Virtuoso (Author)
    text: "We tried to include practical examples in every chapter in the form of\
      \ exercises. There are also lots of stories about cases we\u2019ve seen people\
      \ use Athena for X or Y. As for AWS knowledge, the pre-requiste is pretty small,\
      \ just that you (a) have an AWS Account (b) know some basic SQL (c) are able\
      \ to modify IAM policies in your AWS account since each chapter requires different\
      \ levels of access (though you could just do the entire thing with admin access\
      \ if the account your using isn\u2019t a production account or is a \u2018burner\u2019\
      \ as we say)."
- name: Matias Rebolledo Dezerega
  text: 'Hi Anthony Virtuoso (Author)! :blob_wave: Now i''m starting work with AWS
    and my questions is about the pipelines, can you make a ETL in Athena or just
    work with a ELT like in google BigQuery?

    The books has examples of making a datalake loading data from different sources
    (like API, connectors, etc)? Thanks!!'
  replies:
  - name: Anthony Virtuoso (Author)
    text: "There is a chapter in the book with some basic examples on how to create\
      \ what many would call an ETL pipeline but if your needs include chains of jobs\
      \ (probably anything more than 3 or 4 jobs). I\u2019d recommend looking at Glue\
      \ ETL as it has the concept of scheduled jobs as well as a dependency modeler\
      \ that can run chains of jobs based on triggers like data arriving in S3, completion\
      \ of another job, or a schedule."
  - name: Matias Rebolledo Dezerega
    text: Thanks!
- name: Anthony Virtuoso (Author)
  text: Great questions! keep em coming, ill check back in later today.
  replies: []
- name: Tim Becker
  text: Hi Anthony Virtuoso (Author), really interesting topic! I was wondering who
    AWS charges for Athena and Lake Formation?
  replies:
  - name: Anthony Virtuoso (Author)
    text: what do you mean by who?
  - name: Tim Becker
    text: ah sorry, I meant how, sometimes my autocorrect behaves strangely
- name: Tim Becker
  text: Could you please explain the difference between Athena and redshift (for beginners)?
  replies:
  - name: Anthony Virtuoso (Author)
    text: Redshift targets datawharehouse usecases while Athena is more geared towards
      ad hoc analysis without ETL. Keep in mind this is an extremely reductive explaination
      and the two products can both do many of the same things just with different
      price/performance and strengths.
- name: Tim Becker
  text: Is it possible to use terraform or cloudformation to setup the data lake?
    If possible, would you recommend it?
  replies: []
- name: Denis L.
  text: Hi Anthony Virtuoso (Author), thanks for answering the questions. Once ACID
    transactions are out of public preview for Athena and Lake Formation, do you see
    it potentially replacing Redshift (+ Spectrum)? It seems there are 2 competitive
    solutions that are converging. What is your take on that?
  replies:
  - name: Anthony Virtuoso (Author)
    text: "it won\u2019t replace Redshift + Spectrum as those services do a lot more\
      \ than just ACID. They have a different performance profile, cost, and SQL feature\
      \ set."
  - name: Anthony Virtuoso (Author)
    text: I do think youll see more overlap as time goes on since AWS is striving
      to make it easy for customers to move between and/or use a combination of services
      as one seemless offering since each it fit for a specific purpose. For example,
      can you use a hammer to break concrete? Yes, but a sledge hammer would be btter.
      and You can use a sledgehammer to drive nails but a hammer would be better.

---

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using SQL, without needing to manage any infrastructure.

This book begins with an overview of the serverless analytics experience offered by Athena and teaches you how to build and tune an S3 Data Lake using Athena, including how to structure your tables using open-source file formats like Parquet. You’ll learn how to build, secure, and connect to a data lake with Athena and Lake Formation. Next, you’ll cover key tasks such as ad hoc data analysis, working with ETL pipelines, monitoring and alerting KPI breaches using CloudWatch Metrics, running customizable connectors with AWS Lambda, and more. Moving on, you’ll work through easy integrations, troubleshooting and tuning common Athena issues, and the most common reasons for query failure. You will also review tips to help diagnose and correct failing queries in your pursuit of operational excellence. Finally, you’ll explore advanced concepts such as Athena Query Federation and Athena ML to generate powerful insights without needing to touch a single server.

By the end of this book, you’ll be able to build and use a data lake with Amazon Athena to add data-driven features to your app and perform the kind of ad hoc data analysis that often precedes many of today’s ML modeling exercises.