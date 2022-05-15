---
authors:
- manojkukreja
cover: images/books/20220314-data-engineering-with-apache-spark-delta-lake-and-lakehouse/cover.jpg
description: Book of the Week. Data Engineering with Apache Spark, Delta Lake, and
  Lakehouse by Manoj Kukreja
end: 2022-03-18 23:59:59
image: images/books/20220314-data-engineering-with-apache-spark-delta-lake-and-lakehouse/preview.jpg
links:
- link: https://www.packtpub.com/product/data-engineering-with-apache-spark-delta-lake-and-lakehouse/9781801077743
  text: Book's page
- link: https://www.amazon.com/Engineering-Apache-Spark-Delta-Lakehouse/dp/1801077746/ref=sr_1_1?dchild=1&keywords=Data+Engineering+with+Apache+Spark%2C+Delta+Lake%2C+and+Lakehouse&qid=1634832283&sr=8-1
  text: Buy on Amazon
- link: https://github.com/PacktPublishing/Data-Engineering-with-Apache-Spark-Delta-Lake-and-Lakehouse
  text: GitHub repository
start: 2022-03-14 00:00:00
title: Data Engineering with Apache Spark, Delta Lake, and Lakehouse

archive:
- name: Isaac Toluwani
  text: 'Hi Manoj Kukreja . Congratulations on your book

    Does this book also cover in detail how Data Lakes differ from Data warehouses
    and use cases for either one or both of them'
  replies:
  - name: Manoj Kukreja
    text: Hi Isaac Toluwani Over several years, data warehouses have been the de-facto
      standard for OLAP use cases, until the challenges around the volume, variety
      and velocity of data took over. Last few years, we have been in an era where
      analytics has moved over to data lakes. But this has created a unique challenge
      which I refer to as the "The power struggle" in my book. Moving from data warehouses
      to data lakes has forced us to sacrifice a few good things such as ACID compliance,
      indexing and caching. And that's precisely why the modern Lakehouse architecture
      is taking over. My book not only promotes the new architecture but also explains
      how it is different from other architectures like lambda and kappa.
  - name: Isaac Toluwani
    text: Nice.. Thanks
- name: Tony Gunawan
  text: Hi Manoj Kukreja.. From the book description it says that the book explains
    more detail about Microsoft Azure Cloud for data engineering purpose. How about
    people that do not using the cloud service, instead using other ones like GCP
    or AWS? Could your examples and codes in this book be implemented also in other
    cloud service provider? Thank you and congrats for your book.
  replies:
  - name: Manoj Kukreja
    text: Hi Tony Gunawan Moreover, all cloud vendors perform data processing using
      open-source frameworks like Spark, Hadoop, and Kafka but are packaged into services
      under different names. My book tries to teach the readers about big data concepts
      rather than enforce a particular technology or cloud service. Most of the examples
      particularly Databricks Spark can be run on the cloud platform of your choice.
  - name: Tony Gunawan
    text: Cool. Thanks for answering, Manoj Kukreja
- name: Anand
  text: '&gt; Hi Manoj Kukreja - Congratulation on your book. From the description
    of your book, it would provide steps to deploy the data pipelines in a repeatable
    and continuous way. May I infer that it would cover data-ops as well?Would it
    provide the steps to implement the data-ops using Azure ?Would it also cover similar
    steps using cloud agnostic way?'
  replies:
  - name: Manoj Kukreja
    text: "Hi Anand Towards the end of my book, Chapter 11 \u201CInfrastructure Provisioning\u201D\
      \ and chapter 12 \u201CContinuous Integration and Deployment (CI/CD) of Data\
      \ Pipelines\u201D  are covered in great detail. Since this book is centered\
      \ around Azure, I have used services like ARM templates and Azure DevOps. Having\
      \ said that these services use the same deployments principles as any other\
      \ cloud agnostic tool such as Terraform or Ansible."
- name: A
  text: "Hello Manoj Kukreja \U0001F44B\U0001F3FB\nAsking questions that I am personally\
    \ struggling with at this point of time. Hope to get your viewpoints on the same.\n\
    1. Do you consider Infra first or Use case first as sort of a chicken and egg\
    \ problem? Should organizations hack together some models and define some business\
    \ use cases and then move on and create an DE backed infrastructure to support\
    \ them or should the first and foremost thing should be to create an Infrastructure\
    \ of consistent and reliant data and then working on Data Science use cases?\n\
    2. With more and more push towards data compliance, what role do you think DE\
    \ or Solution architects should play to ensure that Data availability should not\
    \ be a bottleneck for a Data Scientist?\nI might have some more questions which\
    \ I\u2019ll try to get your opinions on. Hope thats alright. Would love to hear\
    \ other peoples opinion as well."
  replies:
  - name: Manoj Kukreja
    text: "Hi A\nAnswer to Q1\nBack in 2011, I and my team were one of the early adopters\
      \ of big data. In my experience, starting a data science practice without a\
      \ proper data engineering back-end is a mistake that several organizations have\
      \ made in the past and unfortunately have paid dearly for it. Data scientists\
      \ are not the best data engineers but are forced to perform that work in their\
      \ absence, in many cases they don\u2019t get proper time to do the work they\
      \ are originally supposed to be doing. In my opinion, these days it is mandatory\
      \ to have a solid DE back-end that enforces proper governance, master-data-management,\
      \ and data sharing techniques like data mesh.\nAnswer to Q2\nData engineers\
      \ play a very huge role in ensuring data compliance. Newer regulations such\
      \ as GDPR and CCPA are very strict about enforcement. Once again having a DE\
      \ practice that takes care of data security, standardization, quality, and cataloging\
      \ is becoming a huge necessity for any organization that dreams of adopting\
      \ effective data science principles. Instead of being a bottleneck, it ends\
      \ up making the job of data scientist easier. It lets them focus on what they\
      \ do best."
- name: juan manuel franzante
  text: "Hello Manoj Kukreja. Thanks for the opportunity to get your amazing book\
    \ free. I read the topics and I understand that you propose the delta lake architecture.\n\
    1.  Which technic of modeling data is the more accurate for this kind of architecture?\
    \ For example: Data Vault 2.0 , Canonical tables, Kimball, OBT, a mix of technics\
    \ etc. \n2.  In which layer of the architecture would you apply this technique?\
    \ Do you consider it necessary to order and modeling data starting in the bronze\
    \ layer?\n Thanks for sharing the knowledge and experience. Regards"
  replies:
  - name: Manoj Kukreja
    text: "juan manuel franzante I don\u2019t think it is advisable to rank the modeling\
      \ techniques based on accuracy. Overall, I can say that the use of Kimball model\
      \ is generally preferred and widespread. The modeling techniques are usually\
      \ applied at the gold layer. However, in some cases particularly related to\
      \ denormalization, you may end up implementing them at the silver layer as well.\
      \ The bronze layer represents the state of data in the shape or form that it\
      \ was delivered or ingested from sources. There are many reasons why you should\
      \ not model data in the bronze layer of a lakehouse:\n- Having the exact state\
      \ of data is important for auditing\n- You may need to replay data in the future\
      \ in which case you may need the pre-existing state\n- Format of data in bronze\
      \ is usually a mixture, applying a particular modeling technique is technically\
      \ not even possible"
  - name: juan manuel franzante
    text: But Kimball is based on oldest paradigm when the storage and compute were
      expensive in my opinion. I think that its important have a technic of modeling
      that offer more advantages for the current Cloud paradigm like Data Vault. I'm
      totally agree with apply these in the silver layer or gold. Thanks for answer!
  - name: Manoj Kukreja
    text: I do agree that its the oldest paradigm, and that is precisely why good
      practices and differs from reality. Most times on projects you are forced to
      do things a certain way based on what the customer is comfortable supporting
      and/or has skills for.
- name: Tim Becker
  text: Hi Manoj Kukreja, thanks for this really interesting book and for the opportunity
    to ask questions.
  replies: []
- name: Tim Becker
  text: '- What is a delta lake?'
  replies: []
- name: Tim Becker
  text: '- In your book, do you cover an end-to-end project?'
  replies: []
- name: Tim Becker
  text: '- Do you cover streaming and batch processing of data?'
  replies: []
- name: Tim Becker
  text: '- Why did you choose Spark and Azure?'
  replies:
  - name: Manoj Kukreja
    text: 'Tim Becker What is a delta lake?

      Delta lake is a new framework that works over Spark to provide some useful features
      to data lake such as ACID transactions, time travel, schema evolution, etc.

      In your book, do you cover an end-to-end project?

      My book covers an end-to-end project for an online electronics retailer that
      wants to streamline its inventory, shipping, finance, and marketing operations
      using analytics.

      Do you cover streaming and batch processing of data?

      The project covers both streaming and batch operations.

      Why did you choose Spark and Azure?

      Azure is one of the most prevalent cloud platforms for big data storage and
      computing operations. Similarly, Spark is the most widely used distributed compute
      platform. Serious big data operations using Spark can most effectively be supported
      using highly scalable platforms like Azure.

      How do you implement monitoring in practice?

      In the book, I have pretty much relied on Azure monitor. However, I would recommend
      using Datadog for enterprise monitoring.

      What kinds od tools do you use to automate it and what are best practices and
      common mistakes?

      Azure DevOps and ARM templates

      I am currently implementing monitoring for ML models and I believe there could
      be a lot of similarities. Do you have any advice?

      I have many times used Prometheus (Kubernetes service monitoring) to collect
      metrics from endpoints.'
  - name: Tim Becker
    text: "thanks a lot \U0001F642 I will look into it"
- name: Tim Becker
  text: '- How do you implement monitoring in practice? What kinds od tools do you
    use to automate it and what are best practices and common mistakes? I am currently
    implementing monitoring for ML models and I believe there could be a lot of similarities.
    Do you have any advice?'
  replies: []
- name: "Philip Die\xDFner"
  text: 'Hello Manoj Kukreja, Congrats on your book!

    Depending on the size of a company/project (and the types of data to be aggregated),
    a data or delta lake seems to possibly introduce a lot complexity than needed,
    especially when considering very small use cases. Do you give recommendations
    in the book on when to extend from e.g. a DWH to a data lake? Or would you always
    start with a data lake(house) architecture to take advantage of the scalability?'
  replies:
  - name: Manoj Kukreja
    text: "Thanks Philip Die\xDFner You have a valid point. The problem is not visible\
      \ and can be easily resolved if the data is small. Overall. it is not about\
      \ whether Delta Lake introduces complexity or not, it\u2019s about can we survive\
      \ without it. In a normal DWH/database environment, atomic updates to row data\
      \ are easily possible. Data lakes are file/object stores, there is no concept\
      \ of atomicity. This means every change (CDC) is delivered to you as a duplicate\
      \ row. In days before delta lake, whenever we got CDC we had to run compute-intensive\
      \ operations (sometimes lasting hours depending on the size of data)  to deduplicate\
      \ data. All of that has disappeared when delta lake was introduced. In many\
      \ respects, it has proven to be a life savior for data engineers."
  - name: Manoj Kukreja
    text: There are legit cases where the complexities of a data lake are unwanted.
      But hose cases are typically that have a limited volume, variety and almost
      non-existent velocity of data.
  - name: "Philip Die\xDFner"
    text: Thanks for your answer and sharing your experience.
- name: Manoj Kukreja
  text: Thanks everyone for the great questions, please don't hesitate to ask more
    in the future.
  replies: []

---

In the world of ever-changing data and schemas, it is important to build data pipelines that can auto-adjust to changes. This book will help you build scalable data platforms that managers, data scientists, and data analysts can rely on.

Starting with an introduction to data engineering, along with its key concepts and architectures, this book will show you how to use Microsoft Azure Cloud services effectively for data engineering. You'll cover data lake design patterns and the different stages through which the data needs to flow in a typical data lake. Once you've explored the main features of Delta Lake to build data lakes with fast performance and governance in mind, you'll advance to implementing the lambda architecture using Delta Lake. Packed with practical examples and code snippets, this book takes you through real-world examples based on production scenarios faced by the author in his 10 years of experience working with big data. Finally, you'll cover data lake deployment strategies that play an important role in provisioning the cloud resources and deploying the data pipelines in a repeatable and continuous way.

By the end of this data engineering book, you'll know how to effectively deal with ever-changing data and create scalable data pipelines to streamline data science, ML, and artificial intelligence (AI) tasks.