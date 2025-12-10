---
title: 'Feature Stores for MLOps: Real-Time Feature Engineering, Feast & Tecton Guide'
short: Feature Stores in MLOps Explained
season: 2
episode: 5
guests:
- willempienaar
image: images/podcast/mlops-feature-stores-feature-stores-feast-tecton.jpg
ids:
  youtube: FQYTb4uWljQ
  anchor: Feature-Stores-Cutting-through-the-Hype---Willem-Pienaar-ept6m8/a-a4hlg3r
links:
  youtube: https://www.youtube.com/watch?v=FQYTb4uWljQ
  anchor: https://anchor.fm/datatalksclub/episodes/Feature-Stores-Cutting-through-the-Hype---Willem-Pienaar-ept6m8/a-a4hlg3r
  spotify: https://open.spotify.com/episode/05YnfTWbplXwOwicR2doy3
  apple: https://podcasts.apple.com/us/podcast/feature-stores-cutting-through-the-hype-willem-pienaar/id1541710331?i=1000508782957
description: Discover feature store use cases, real-time features with Feast & Tecton,
  build scalable MLOps to speed production, cut duplication and detect drift
intro: How do you reliably build and serve real-time features for production ML without
  rework, duplication, or training/serving skew? In this episode, Willem Pienaar —
  engineering lead at Tecton and creator of Feast — walks through what feature stores
  solve in MLOps and how they enable real-time feature engineering. We define feature
  stores, compare feature creation vs retrieval (SQL, Python, APIs, on-demand transforms),
  and illustrate a production real-time fraud detection lookup. Willem separates hype
  from value, explains organizational challenges like team silos and speed to production,
  and outlines the platform role across materialization, serving, and validation.
  <br><br> You’ll get practical coverage of Feast (open-source) and Tecton (enterprise),
  architecture components (transform engine, storage, serving, registry, monitoring),
  and when online tabular use cases require a feature store versus when it’s overkill.
  The episode also covers integrations (dbt, Kubeflow, Airflow), streaming vs batch
  (Flink, Spark), validation and monitoring (drift detection, Great Expectations,
  TFDV), backfilling strategies, ownership and governance, and getting started resources
  (feast.dev, Docker). Listen to learn when to adopt a feature store and concrete
  next steps for productionizing features in your MLOps stack
topics:
- machine learning
- MLOps
- feature stores
- tools
dateadded: 2021-02-23
quotableClips:
- name: 'Episode Introduction: Feature Stores in MLOps'
  startOffset: 0
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=0
  endOffset: 120
- name: 'Background: From Mechatronic Engineering to ML Platform Builder'
  startOffset: 120
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=120
  endOffset: 390
- name: Feature Store Definition and Core ML Problems Addressed
  startOffset: 390
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=390
  endOffset: 660
- name: 'Transformations: From Raw Streams/Warehouses to Features'
  startOffset: 660
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=660
  endOffset: 870
- name: 'Feature Creation vs Retrieval: SQL, Python, APIs, and On-Demand Transforms'
  startOffset: 870
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=870
  endOffset: 990
- name: 'Production Example: Real-Time Fraud Detection Feature Lookup'
  startOffset: 990
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=990
  endOffset: 1110
- name: 'Hype vs Value: Why Feature Stores Matter in MLOps'
  startOffset: 1110
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=1110
  endOffset: 1260
- name: 'Organizational Challenges: Team Silos, Duplication, and Speed to Production'
  startOffset: 1260
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=1260
  endOffset: 1500
- name: 'Platform Role: Feature Stores within the ML Lifecycle'
  startOffset: 1500
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=1500
  endOffset: 1680
- name: 'Ideal Production Setup: Materialization, Serving, and Validation'
  startOffset: 1680
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=1680
  endOffset: 1890
- name: 'Feast Overview: Open-Source Feature Store Design and Use Cases'
  startOffset: 1890
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=1890
  endOffset: 2040
- name: 'Tecton Overview: Enterprise Feature Platform and Full Lifecycle Support'
  startOffset: 2040
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2040
  endOffset: 2190
- name: 'Architecture Breakdown: Transform Engine, Storage, Serving, Registry, Monitoring'
  startOffset: 2190
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2190
  endOffset: 2400
- name: 'When to Adopt Feature Stores: Online Tabular Use Cases vs Overkill Scenarios'
  startOffset: 2400
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2400
  endOffset: 2550
- name: 'Integrations: dbt, Kubeflow, Airflow, Warehouses, and ML Pipelines'
  startOffset: 2550
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2550
  endOffset: 2700
- name: 'Streaming vs Batch: Flink, Spark, and Real-Time Feature Engineering'
  startOffset: 2700
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2700
  endOffset: 2850
- name: 'Validation and Monitoring: Drift Detection, Great Expectations, TFDV'
  startOffset: 2850
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=2850
  endOffset: 3000
- name: Backfilling and Materialization Strategies for Historical Features
  startOffset: 3000
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=3000
  endOffset: 3120
- name: Feature Ownership, Governance, and Migration Strategies
  startOffset: 3120
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=3120
  endOffset: 3240
- name: 'Practical Getting Started: feast.dev, Docker Examples, and Learning Resources'
  startOffset: 3240
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=3240
  endOffset: 3360
- name: 'Key Takeaways: Where Feature Stores Deliver Business Impact'
  startOffset: 3360
  url: https://www.youtube.com/watch?v=FQYTb4uWljQ&t=3360
  endOffset: 3450
transcript:
- line: Hello everyone. This event is brought to you by DataTalks.Club, a community
    of people who love data. We host two types of events. On Tuesdays, we usually
    have technical events with presentations, like workshops.
  sec: 0
  time: 0:00
  who: Alexey
- line: Today is Tuesday, but this event is different, and I'll explain why in a moment.
    I can briefly share our plans for the future. Next month, in February, we will
    have a conference on Fridays, which I will discuss shortly.
  sec: 16
  time: 0:16
  who: Alexey
- line: In March, during the first week, we will have a workshop about building scalable
    end-to-end data pipelines, specifically deep learning pipelines in the cloud.
    The following week, we will talk about active learning and self-supervised learning.
    Usually on Fridays, we host live podcast sessions where we discuss various topics.
    Today, even though it’s not a Friday, we have a similar event.
  sec: 35
  time: 0:35
  who: Alexey
- line: 'This is not a workshop; it’s a conversation about feature stores. In March,
    we will also cover public speaking in the first week and then discuss Datums.
    Speaking of conferences, this week we have the first day of the conference on
    Friday. We will cover machine learning use cases with four examples: reinforcement
    learning, food industry applications, healthcare, and manufacturing.'
  sec: 67
  time: '1:07'
  who: Alexey
- line: Next week, we will discuss products and processes, followed by career opportunities
    in data. Finally, during the last week of February, we will focus on machinery
    and production. You can read more about this event on our website, datatalks.club.
  sec: 110
  time: '1:50'
  who: Alexey
- line: We also have support from our friends at O'Reilly and the Machine Learning
    Ops community. During our chat with Willem, we will use Slido for questions. I’ll
    share a link in the chat now.
  sec: 122
  time: '2:02'
  who: Alexey
- line: Whenever you have a question, feel free to use Slido to submit it.
  sec: 156
  time: '2:36'
  who: Alexey
- line: Last week, we talked about MLOps, including machine learning platforms. One
    component of these platforms is a feature store. This week, we will discuss this
    topic in more detail with Willem. Willem is the creator of Feast, an open-source
    feature store. Previously, he worked at Gojek, where he led the data science platform
    team. He currently works at Tecton, a company that develops a feature store.
  sec: 169
  time: '2:49'
  who: Alexey
- line: Welcome, Willem.
  sec: 208
  time: '3:28'
  who: Alexey
- line: Thanks, Alexey. I’m happy to be here.
  sec: 211
  time: '3:31'
  who: Willem
- line: Before we dive into feature stores, can you tell us a bit more about your
    background and your journey so far?
  sec: 213
  time: '3:33'
  who: Alexey
- line: Sure. I’ll give a one to two-minute summary. I’m South African and grew up
    there. I studied mechatronic engineering. During university, I built a networking
    company, which I eventually sold. Then I moved into control systems and automation,
    bridging traditional engineering and software.
  sec: 220
  time: '3:40'
  who: Willem
- line: I worked in that industry for about three years, then moved to Asia, where
    I worked across the stack from low-level electronics to cloud solutions. We built
    vertically integrated solutions for large MNCs and eventually focused on large
    data solutions and analytical warehousing for about two years.
  sec: 256
  time: '4:16'
  who: Willem
- line: After that, I moved to Singapore and became the first engineering hire for
    a machine learning, or at the time, data science team at Gojek. At that stage,
    Gojek was a unicorn valued at about a billion dollars. They had a lot of interesting
    products and data but were not using it effectively.
  sec: 288
  time: '4:48'
  who: Willem
- line: They hired many data scientists but couldn’t get them into production. They
    embedded us as engineers and asked me to lead the team to help productionize the
    data scientists’ work. Traditional product engineers were busy with other responsibilities,
    so they couldn’t handle this. I led that team for about four years.
  sec: 312
  time: '5:12'
  who: Willem
- line: After building the ML platform at Gojek and leading that team, I moved to
    Tecton. A large part of my focus at Gojek was building feature stores, which is
    also my primary focus at Tecton.
  sec: 348
  time: '5:48'
  who: Willem
- line: That’s an interesting journey. As a mechanical engineer, did you learn to
    code at university?
  sec: 361
  time: '6:01'
  who: Alexey
- line: Technically, it was mechatronics, but most of the focus was on mechanical
    aspects. About 70% of it didn’t interest me much. The software aspect was always
    the most interesting and relevant to what I do today.
  sec: 369
  time: '6:09'
  who: Willem
- line: That’s impressive from low-level work to cloud. So, what exactly are feature
    stores, why do we need them, and what problems do they solve?
  sec: 389
  time: '6:29'
  who: Alexey
- line: Feature stores solve multiple problems. Essentially, a feature store is an
    operational data system designed specifically for machine learning. It addresses
    operational problems like moving offline features into an online production environment.
  sec: 403
  time: '6:43'
  who: Willem
- line: It ensures consistency between online and offline environments, which models
    require. It allows data scientists to ship features into production without relying
    on engineers. It provides version control and enables the creation, sharing, and
    reuse of transformation code.
  sec: 434
  time: '7:14'
  who: Willem
- line: Companies typically start considering feature stores when features are being
    duplicated across projects. That duplication signals a problem. Feature stores
    help monitor features, ensure valid data is served to models, and detect drift
    or distribution shifts over time.
  sec: 470
  time: '7:50'
  who: Willem
- line: So, feature stores act as a data storage layer that ensures consistency, is
    user-friendly for data scientists, supports version control, and simplifies feature
    reuse.
  sec: 506
  time: '8:26'
  who: Alexey
- line: Exactly. Not all feature stores solve the same problems. For example, Feast
    doesn’t handle transformations, while Tecton’s feature store does. The scope of
    what a feature store should handle varies, but these are the core problems.
  sec: 530
  time: '8:50'
  who: Willem
- line: By transformation, do you mean taking raw data from a data lake, applying
    some function, and then sending it to the feature store?
  sec: 554
  time: '9:14'
  who: Alexey
- line: Yes. Typically, a feature store sits between raw data and your production
    ML environment. It can access streams, data warehouses, and data lakes. Transformations
    can be applied to any of these sources, then served to production, decoupling
    ML from data infrastructure.
  sec: 567
  time: '9:27'
  who: Willem
- line: As a data scientist, I’m used to querying data with SQL. Do feature stores
    provide a SQL-like interface, or is it different?
  sec: 603
  time: '10:03'
  who: Alexey
- line: 'There are two aspects: production creation and retrieval. Most features are
    pre-computed. Feature stores like Tecton allow transformations via Python, PySpark,
    or SQL. Once published, features are materialized and persisted in a storage engine
    like DynamoDB or Redis.'
  sec: 621
  time: '10:21'
  who: Willem
- line: For retrieval, you normally use an API rather than SQL. A SQL interface for
    retrieval would defeat the purpose.
  sec: 662
  time: '11:02'
  who: Willem
- line: If you provided a SQL interface for retrieval, you wouldn't have the same
    guarantees in terms of performance and production. Most online models only require
    key-value enrichment of entity data; they don’t need arbitrary queries executed.
  sec: 667
  time: '11:07'
  who: Willem
- line: Some feature stores, like Tecton, do provide on-demand or real-time transformations.
    For example, in a fraud detection system, incoming requests may include live data
    attached to an order or booking. Those features are transformed at request time.
    For the most part, though, features are pre-computed, and that’s where most arbitrary
    logic is applied.
  sec: 690
  time: '11:30'
  who: Willem
- line: You mentioned fraud detection. I imagine a scenario where a user goes to an
    e-commerce store like Amazon and makes a purchase. We have information about the
    user, and when a transaction happens, we want to predict if it is fraudulent.
    At that moment, we query our model with the user ID and transaction details. We
    then ask the feature store, "What are the features for this user ID?"
  sec: 719
  time: '11:59'
  who: Alexey
- line: Yes, that’s correct.
  sec: 766
  time: '12:46'
  who: Willem
- line: Feature stores are very popular these days. I’m part of the MLOps community,
    and people discuss them almost every day. Why do you think they are so popular?
    Why is there so much hype?
  sec: 773
  time: '12:53'
  who: Alexey
- line: The hype is interesting. It’s not just feature stores; ML in general has had
    a lot of hype. Part of it is competition in the space—employment, marketability,
    and skills. It’s similar to the Node.js hype in the past.
  sec: 797
  time: '13:17'
  who: Willem
- line: A large part is people rebranding their skill sets and becoming niche experts.
    But feature stores and MLOps also provide real value to companies. Many organizations
    are digitizing, and those that don’t implement these systems properly may fall
    behind. Some companies have succeeded because they solved these problems, like
    Uber’s Michelangelo platform.
  sec: 828
  time: '13:48'
  who: Willem
- line: MLOps is critical if you want to use ML at scale. Machine learning platforms
    have become standard—whether it’s Kubeflow, MLflow, or Seldon, most companies
    have a stack running models. But data accounts for almost 90% of the equation.
    The value comes from producing new features, shipping them to production, and
    iterating constantly.
  sec: 880
  time: '14:40'
  who: Willem
- line: A feature store sits between your data scientists and your production environment.
    It acknowledges the value of a system that enables feature reuse and reduces waste.
    Whether feature stores solve all problems is another matter, but they have massive
    potential business impact.
  sec: 906
  time: '15:06'
  who: Willem
- line: So there is hype around MLOps and feature stores, but this hype is warranted?
  sec: 950
  time: '15:50'
  who: Alexey
- line: Yes. Data science and machine learning engineering have been around for five
    to ten years. The industry is maturing, and these new tools address hard problems,
    which is why there is hype.
  sec: 956
  time: '15:56'
  who: Willem
- line: Most of the remaining hype comes from feature store vendors promoting their
    software.
  sec: 988
  time: '16:28'
  who: Alexey
- line: Let’s take a step back and discuss the problems data science teams usually
    face. Are these problems more organizational or technical?
  sec: 996
  time: '16:36'
  who: Alexey
- line: Both. Individual contributors often focus on technical problems, thinking
    organizational issues are unique to their company. But many organizational problems
    are common patterns across organizations.
  sec: 1009
  time: '16:49'
  who: Willem
- line: Some core technical problems include getting features into production, ensuring
    online and offline consistency, allowing data scientists to ship data without
    engineers, enabling transformations, sharing and reuse, and monitoring features
    for quality.
  sec: 1038
  time: '17:18'
  who: Willem
- line: These are technical problems, but organizational problems overlap.
  sec: 1078
  time: '17:58'
  who: Willem
- line: For example, shipping features into production without an engineer is an organizational
    challenge. Engineers may prioritize their product OKRs over helping data science
    projects. Data scientists can be treated as second-class citizens, even if they
    are highly skilled. Their use cases and goals may not be prioritized, yet they
    are expected to deliver results.
  sec: 1084
  time: '18:04'
  who: Willem
- line: Sometimes, organizations don’t fully understand the value data scientists
    can bring. Failures in data science projects are normal, but organizations may
    undervalue their contribution. Over time, this is changing.
  sec: 1133
  time: '18:53'
  who: Willem
- line: Shipping features into production involves organizational friction, because
    data scientists need to see the results in production to iterate. Sharing and
    reuse is also an organizational problem. Siloed teams often lack communication
    channels, infrastructure, or ways to broadcast how features were created, their
    intent, semantics, and dependencies.
  sec: 1168
  time: '19:28'
  who: Willem
- line: There’s a social and trust aspect to sharing and reuse, and that’s largely
    the challenge.
  sec: 1204
  time: '20:04'
  who: Willem
- line: An organizational problem, okay. That makes sense. We have multiple teams,
    and each team is solving its own problems. They are building their own services
    and machine learning solutions.
  sec: 1216
  time: '20:16'
  who: Alexey
- line: At the end, it turns out there is some overlap between the work two teams
    are doing. They might be solving different problems, but some features, like user-based
    features or other common features, are the same. They have to implement them from
    scratch, and this is an organizational problem.
  sec: 1234
  time: '20:34'
  who: Alexey
- line: I would say a lot of organizations take a flat approach to these teams. They
    embed them in product teams and verticals. Often, a fraud team and a team doing
    analytics on user data use the same entity data. The features are common and reusable
    across teams.
  sec: 1252
  time: '20:52'
  who: Willem
- line: However, the fraud data science team may have an air of secrecy. They feel
    that what they are working on should not be exposed to other teams. Those are
    organizational inefficiencies. From a CDO or CIO perspective, it does not make
    sense for work and data to be duplicated. This inefficiency could be solved through
    technology or other means.
  sec: 1284
  time: '21:24'
  who: Willem
- line: The solution would be to have some sort of central theme or central piece
    of technology. Perhaps a platform that is common for all teams, and the feature
    store would be part of this ML platform.
  sec: 1310
  time: '21:50'
  who: Alexey
- line: Yes, that is correct. At Gojek, you can architect these systems in different
    ways, but in an ML life cycle, at each stage, you have tools that allow you to
    progress further. This includes data transformations, storage, model training,
    model deployment, serving, and experimentation. Feature stores primarily operate
    in the data transformation and data serving stages.
  sec: 1327
  time: '22:07'
  who: Willem
- line: The idea is to have a platform with all these capabilities. Data scientists
    do not need to rely on engineers who are busy with their own work. They can use
    pre-computed features that are already in the feature store, pull them, and train
    models.
  sec: 1363
  time: '22:43'
  who: Willem
- line: You can think of a utopian end state where you do not write any boilerplate.
    You only write your transformations, iterate easily, deploy, and the results are
    materialized into offline and online stores. An API allows your model to access
    features in production or development. You can enrich entities like user IDs with
    features without needing an engineer.
  sec: 1409
  time: '23:29'
  who: Willem
- line: Ideally, there is also a validation layer that monitors metrics and ensures
    that good quality data reaches your model.
  sec: 1445
  time: '24:05'
  who: Willem
- line: This dream state sounds really impressive. Are there companies that are already
    there?
  sec: 1456
  time: '24:16'
  who: Alexey
- line: I cannot speak about that specifically. My employer already provides a product
    like that.
  sec: 1466
  time: '24:26'
  who: Willem
- line: Companies like Uber, with Tecton, already have this from a feature store perspective.
  sec: 1472
  time: '24:32'
  who: Willem
- line: If you have an ML platform and other components, and you plug that into Tecton,
    you get the complete flow?
  sec: 1486
  time: '24:46'
  who: Alexey
- line: Yes. If you deploy these with an ML platform, Tecton does not perform upstream
    transformations. You need a system upstream, like dbt, Airflow, or Spark ETL,
    to handle transformations.
  sec: 1492
  time: '24:52'
  who: Willem
- line: Kubeflow pipelines also fall into this category, right?
  sec: 1517
  time: '25:17'
  who: Alexey
- line: Yes. I would not use Kubeflow pipelines for transformations, but it is a good
    tool for model training. I consider these separate tools based on the stage of
    the ML life cycle they address.
  sec: 1522
  time: '25:22'
  who: Willem
- line: Feast is an open source library you created. What problem does it solve?
  sec: 1540
  time: '25:40'
  who: Alexey
- line: Feast is a feature store built at Gojek, productionized and operated as part
    of the ML platform stack. It solves many of the common problems. We aimed to solve
    online and offline consistency, provide a way to publish data into production
    without engineers, and support monitoring.
  sec: 1547
  time: '25:47'
  who: Willem
- line: We did not fully solve sharing and reuse. We did not focus on UI or discovery
    because many teams were content duplicating code and pipelines. This is often
    to protect production environments.
  sec: 1581
  time: '26:21'
  who: Willem
- line: Feast primarily decouples your production ML environment from data infrastructure.
    It ingests pre-computed features from streams and batch sources, provides an interface
    to build training data sets in a point-in-time correct way, and gives a unified
    interface for models to access features online and offline.
  sec: 1614
  time: '26:54'
  who: Willem
- line: For online serving, we use Redis. Feast was co-developed with Google Cloud
    and open sourced. I continued developing it at Tecton, where it is one of our
    focused offerings.
  sec: 1645
  time: '27:25'
  who: Willem
- line: Feast can be installed on Google Cloud and AWS?
  sec: 1676
  time: '27:56'
  who: Alexey
- line: Yes. We have generalized it so it can also be deployed on Azure. We recently
    launched a Terraform deployment for Azure, and of course, GCP is supported.
  sec: 1681
  time: '28:01'
  who: Willem
- line: Tecton provides an end-to-end package for enterprises. You can use it without
    setting up the cloud infrastructure yourself.
  sec: 1698
  time: '28:18'
  who: Willem
- line: Tecton is more full-featured. It covers transformations, user interface, on-demand
    streaming transformations, batch transformations, monitoring, security, auditability,
    and compliance. It is targeted at companies that want a complete solution.
  sec: 1715
  time: '28:35'
  who: Willem
- line: Feast is targeted at teams that are happy to slot a smaller tool into a larger
    stack. At the end of the day, feature stores are still overloaded and trying to
    solve many problems.
  sec: 1754
  time: '29:14'
  who: Willem
- line: Can we step back and discuss the basic components of a feature store? You
    mentioned offline and online storage. For online, you mentioned Redis or Dynamo.
    What about offline storage?
  sec: 1774
  time: '29:34'
  who: Alexey
- line: There is a great blog post I wrote with Mike for Tecton called What Is a Feature
    Store?. In that post, we describe all the components.
  sec: 1797
  time: '29:57'
  who: Willem
- line: We'd say there is a transformation or computation engine. You have your upstream
    data sources such as streams or batch. Then there is the transformation system,
    such as Spark or SQL in a warehouse, that transforms the data. Then there are
    storage layers.
  sec: 1809
  time: '30:09'
  who: Willem
- line: Normally there is offline and online storage. In Tecton, offline storage is
    an object store like Delta, but you can also use a warehouse like BigQuery or
    Snowflake. For online storage in Tecton, that is Dynamo or Redis. Normally it
    is a key-value, low-latency store for online use. Offline storage is typically
    a big data lake or warehouse, such as Hive, BigQuery, Redshift, or Snowflake.
  sec: 1822
  time: '30:22'
  who: Willem
- line: Those are the two storage components. Then there is a serving layer, which
    is normally an API that allows you to read from either the online or offline store.
    Sometimes an SDK is used as a query generator. Serving is the third component.
  sec: 1852
  time: '30:52'
  who: Willem
- line: A critical component in a feature store is the registry. Both Feast and Tecton
    have this. You define schemas that describe where your data is upstream and the
    transformations to apply. You register this in the registry, and the feature store
    executes those schemas as infrastructure. It either creates tables in the warehouse
    or runs computational jobs based on the registry definitions.
  sec: 1871
  time: '31:11'
  who: Willem
- line: The final component is the monitoring layer. It tracks data being ingested
    from streams or batch sources, row counts, distributions, and data being read
    out of the feature store. Teams, especially in fraud, often log features back
    into a warehouse to validate the data being served to models and ensure there
    is no drift.
  sec: 1902
  time: '31:42'
  who: Willem
- line: The five main components are the transformation engine, storage engine, serving
    layer, registry, and operational monitoring layer. Registries also usually include
    a user interface for feature discovery and entity discovery.
  sec: 1934
  time: '32:14'
  who: Willem
- line: Let's say we want to start using a feature store at our organization. It would
    likely come with a machine learning platform. How would we go about doing this?
  sec: 1964
  time: '32:44'
  who: Alexey
- line: It depends on the use case. Some use cases are not suitable for a feature
    store. At Gojek, with 16 or 17 products, we identified cases where a feature store
    was not necessary. If you only need batch processing, you may not need it. If
    your use case involves tabular data with online serving needs, like fraud detection,
    product recommendations, or user risk scores, then a feature store is very valuable.
  sec: 1976
  time: '32:56'
  who: Willem
- line: Feast adds value in the online serving layer and unified access. You implement
    it after your transformation pipelines. You already have some system to do transformations,
    like BigQuery batch or streaming.
  sec: 2051
  time: '34:11'
  who: Willem
- line: Traditionally, some teams transform data and write it directly into production.
    We do not recommend that. We recommend pushing streams back to streams and batch
    data back to the lake or warehouse. The feature store is a layer on top that lets
    you pick which columns and tables to productionize for serving.
  sec: 2089
  time: '34:49'
  who: Willem
- line: Feast can read existing transformed data from streams and batch sources. You
    could also read raw event logs and transform them using Tecton. Typically, feature
    stores are deployed between your data infrastructure and production serving environments.
  sec: 2113
  time: '35:13'
  who: Willem
- line: To summarize, if we already have data infrastructure, such as dbt or Airflow,
    we can add Feast on top of existing pipelines, register schemas for specific tables,
    and productionize them.
  sec: 2144
  time: '35:44'
  who: Alexey
- line: Feast would take features from the offline store, like a data lake or Snowflake,
    and put them in online storage.
  sec: 2200
  time: '36:40'
  who: Alexey
- line: With Tecton, you can also perform transformations. It can read from logs or
    events, apply transformations, and produce features.
  sec: 2220
  time: '37:00'
  who: Willem
- line: With Feast, you point to tables that are already featurized or transformed.
    With Tecton, you point to raw data in your lake, apply transformations, and compute
    features.
  sec: 2238
  time: '37:18'
  who: Willem
- line: You mentioned some cases where a feature store is not a good solution. Can
    you explain?
  sec: 2263
  time: '37:43'
  who: Alexey
- line: Feast is not very useful if you only need batch scoring, such as for marketing
    campaigns. You can handle that with SQL, BigQuery ML, or similar tools. There
    is no online serving component needed. For Tecton, it can still be valuable because
    it provides a transformation system and bridges offline and online use cases.
  sec: 2281
  time: '38:01'
  who: Willem
- line: If we have batch pipelines, when we decide to go online and start serving
    models, we already have everything and can deploy a web service.
  sec: 2330
  time: '38:50'
  who: Alexey
- line: Feature stores are great for tabular data online models. For less structured
    data, such as images or text, they are not the best solution.
  sec: 2346
  time: '39:06'
  who: Alexey
- line: It depends on the value you get. You can serve binary blobs to production,
    but for a 2D image, treating it as a 2D array provides little semantic value.
    Features are normally identified and have intent. Binary blobs are harder to reuse
    or share between teams. You are serving data for a specific use case but not building
    efficiency for the team.
  sec: 2372
  time: '39:32'
  who: Willem
- line: A good use case might be applying a model, such as image classification, and
    saving the results.
  sec: 2439
  time: '40:39'
  who: Alexey
- line: Let's say we have a model that outputs the probability that an image is a
    car and we just save it. In real time, we ask the feature store for the probability
    for this image ID, and it gives back the prediction. This is a good use case,
    right?
  sec: 2450
  time: '40:50'
  who: Alexey
- line: If you are using those outputs as features for downstream systems, that is
    a great use case. You can have a column like is_car as a binary value and probability_car
    as a float, like 0.7, to feed a subsequent model. If the input to the model itself
    is the image, reading the image from the feature store is not a good use case.
    Normally, incoming requests have a request ID and a URL to S3 where you download
    the image and feed it to the model.
  sec: 2476
  time: '41:16'
  who: Willem
- line: The output of that model is something you do want to store in a feature store.
    At Gojek, we often sent model outputs back into a stream and then read them into
    the feature store, creating cycles that expand the data foundation. These output
    models can be reused as features because the model itself is just a transformation.
  sec: 2535
  time: '42:15'
  who: Willem
- line: If I want to learn more about feature stores as an individual contributor,
    how should I start?
  sec: 2578
  time: '42:58'
  who: Alexey
- line: Go to the ML Ops community. There are many resources, especially in the Data
    Ops and open-source channels. Read blog posts from Tecton. These explain our thinking
    about feature stores and the category itself.
  sec: 2596
  time: '43:16'
  who: Willem
- line: For hands-on learning, you can install Feast on your laptop. Go to feast.dev,
    run Docker Compose, and try the example notebook. This gives sufficient understanding.
    If your company has a similar use case, you can propose it.
  sec: 2651
  time: '44:11'
  who: Willem
- line: We have not fully articulated all use cases yet. We plan to produce more content
    that explains when to use feature stores within an organizational context. The
    documentation provides guidance even without installing Feast. Some companies,
    like Monzo, use feature stores differently, such as storing text data.
  sec: 2691
  time: '44:51'
  who: Willem
- line: What workflow do you recommend for engineering new features, testing offline
    performance, and ensuring offline and online data matches?
  sec: 2751
  time: '45:51'
  who: Alexey
- line: Transformations are treated separately. Streaming transformations are handled
    differently from batch. For batch, you can use dbt or a similar system. Validate
    during transformations using tools like Great Expectations or TFDV.
  sec: 2765
  time: '46:05'
  who: Willem
- line: 'Four main validation points are: streaming ingestion and transformation,
    batch validation before ingestion into the offline store, validation before training,
    and validation before serving. A feature store provides hooks for these validations.
    Without a feature store, you need to write boilerplate code to prevent bad data
    from reaching models.'
  sec: 2808
  time: '46:48'
  who: Willem
- line: Great Expectations is a tool that allows you to create expectations about
    your data, profile columns and distributions, and validate new datasets against
    these expectations. You can layer expectations, such as ranges, distributions,
    or categorical values. It is mostly focused on batch today, but tools for streaming
    use cases are emerging.
  sec: 2887
  time: '48:07'
  who: Alexey
- line: Do you have any opinion on Apache Flink versus Apache Spark for calculating
    real-time features?
  sec: 2948
  time: '49:08'
  who: Alexey
- line: We started with Apache Beam. Beam and Flink are similar. Flink has a great
    API and is highly regarded. We use Spark with Feast because of its ecosystem and
    connector support. Flink may be superior in raw technology, but Spark can execute
    in multiple environments, including Hadoop, GCP, Azure, and AWS, making it easier
    for companies to adopt. Flink is getting there; some cloud providers support it,
    such as AWS. There is also a Kinesis connector for Flink.
  sec: 2962
  time: '49:22'
  who: Willem
- line: I remember seeing something like that.
  sec: 3050
  time: '50:50'
  who: Alexey
- line: All those folks running on-premise or large Hadoop stacks, HDFS, and Hive
    will eventually need to get onto BigQuery or Snowflake and modernize. For some
    companies, that will be a 10-year effort.
  sec: 3055
  time: '50:55'
  who: Willem
- line: What APIs are provided for feature transformations? Is it similar to building
    Spark or Beam transformations?
  sec: 3082
  time: '51:22'
  who: Alexey
- line: In Tecton, it's like PySpark or Spark SQL. If using an existing warehouse,
    it’s SnowSQL or BigQuery SQL. Online transformations, meaning just-in-time or
    request-time transformations, are Python. You can write Pandas transformations
    or other Python transformations. Some teams run Scala transformations in production,
    but that’s not supported today in Tecton.
  sec: 3087
  time: '51:27'
  who: Willem
- line: For Feast, it doesn’t matter. On-demand transformations are requested by many
    teams, but unifying on-demand, online, and offline aspects is challenging. You
    need to ensure the same transformations are applied to training datasets.
  sec: 3124
  time: '52:04'
  who: Willem
- line: At what size of a group does it make sense to build a feature store?
  sec: 3161
  time: '52:41'
  who: Alexey
- line: Traditionally, when you have multiple use cases, like two or three data scientists
    with multiple projects, or multiple teams with one project that need sharing and
    collaboration. We are exploring whether Feast can add value for a single data
    scientist or single team on a single use case. The current status quo is a platform
    team addressing multiple solution-oriented teams.
  sec: 3168
  time: '52:48'
  who: Willem
- line: If we’re a small startup hiring our first data engineer or data scientist,
    should we start using a feature store?
  sec: 3217
  time: '53:37'
  who: Alexey
- line: Not initially. If you have only a few features and one model, it’s manageable.
    A feature store becomes valuable when you want to iterate on models, have multiple
    use cases, and teams start working independently. Starting with two or three data
    scientists and engineers doesn’t require it.
  sec: 3229
  time: '53:49'
  who: Willem
- line: The biggest friction is transformations. If you already have transformations
    in one place and add a feature store that allows transformations, now you have
    two places. Feast doesn’t do transformations, so it slots in easily. With Tecton,
    you need to decide where transformations live. Greenfield projects may adopt Tecton,
    and brownfield projects may not migrate.
  sec: 3292
  time: '54:52'
  who: Willem
- line: Brownfield means an existing project, the opposite of greenfield.
  sec: 3360
  time: '56:00'
  who: Alexey
- line: What is your take on dbt and feature stores?
  sec: 3372
  time: '56:12'
  who: Alexey
- line: Data warehouses are dominating the space. Feature stores slot well onto them.
    If you already have dbt for batch transformations, it solves most of your transformation
    needs. Analysts can contribute features through SQL. Feature stores can leverage
    that to drive business value.
  sec: 3378
  time: '56:18'
  who: Willem
- line: How do you set up features back in time, for historical data?
  sec: 3456
  time: '57:36'
  who: Alexey
- line: In Feast, the upstream system handles backfill. You run a new ETL pipeline
    and call the feature store to re-ingest features into the online environment.
    In Tecton, you change the transformation, and it automatically backfills from
    a start date for production.
  sec: 3462
  time: '57:42'
  who: Willem
- line: Who should maintain features in a feature store?
  sec: 3542
  time: '59:02'
  who: Alexey
- line: The most effective approach is not to gatekeep. Initially, data scientists
    maintain features. Over time, a central team can step in when features are duplicated
    or highly reused, creating a golden dataset and coordinating deduplication. Central
    maintenance is usually driven by feature importance and production impact.
  sec: 3554
  time: '59:14'
  who: Willem
- line: What’s the difference between a feature store and a traditional data platform
    with ETL, preparation, and a good catalog?
  sec: 3696
  time: '1:01:36'
  who: Alexey
- line: A feature store is an opinionated data system for operational data for machine
    learning. Traditional data platforms are not focused on low-latency serving. Feature
    stores unify online and offline interfaces for ML, ensuring identical results
    for queries. In theory, a data platform could provide this, but the feature store
    bridges offline and online ML worlds.
  sec: 3703
  time: '1:01:43'
  who: Willem
- line: We still have seven more questions, but we shouldn’t keep you too long.
  sec: 3789
  time: '1:03:09'
  who: Alexey
- line: You can share the questions in Slack. I or the community can answer them later.
  sec: 3795
  time: '1:03:15'
  who: Willem
- line: Thanks a lot for coming. I learned a lot about feature stores, when to use
    them, and when not to. Thanks, everyone, for listening and asking questions.
  sec: 3809
  time: '1:03:29'
  who: Alexey
- line: Thanks. Have a nice day.
  sec: 3824
  time: '1:03:44'
  who: Willem
---

In this episode, we dive deeper into feature stores with Willem, creator of Feast (an open-source feature store). Previously, Willem led the Data Science Platform team at Gojek and now works at Tecton, which develops feature store technology.

Here's what we covered:

- [Willem's journey from mechatronic engineering to building Feast at Gojek](#guest-introduction-from-engineering-to-feature-store-creator)
- [What feature stores actually do and why ML teams need them](#what-is-a-feature-store-core-problems-and-solutions)
- [Understanding the hype: real value vs marketing noise](#why-feature-stores-are-popular-separating-hype-from-value)
- [How feature stores solve organizational problems like team silos and duplication](#team-silos-duplication-and-organizational-friction)
- [What an ideal feature store setup looks like in production](#ideal-setups-real-world-examples-and-when-to-use-feature-stores)
- [How feature stores integrate with Kubeflow, dbt, and other ML tools](#how-feature-stores-fit-with-kubeflow-dbt-and-other-ml-tools)
- [Comparing Feast and Tecton: open source vs enterprise solutions](#feast-vs-tecton-open-source-vs-enterprise-feature-store-solutions)
- [Breaking down the architecture: storage, transformations, and APIs](#feature-store-architecture-storage-transformations-and-apis)
- [Getting started: resources and hands-on learning paths](#resources-and-hands-on-learning-where-to-start-with-feature-stores)
- [Production workflows including validation, streaming, and tech choices](#production-workflows-validation-streaming-and-technology-choices)
- [Feature ownership and governance strategies](#who-should-own-features-governance-and-migration-strategies)

## Guest Introduction: From Engineering to Feature Store Creator

**Q: Before we dive into feature stores, could you tell us about your professional background and how you became involved in this space?**

**Willem:** Sure. I'm South African and studied mechatronic engineering, though I was always most interested in the software side. During university, I started and sold a networking company, then worked in control systems and automation—basically the intersection of traditional engineering and software—for about three years.

I moved to Asia and worked across the stack, from low-level devices up to the cloud, building vertically integrated solutions for large enterprises. That led me into large data solutions and analytical warehousing. Later, I moved to Singapore as the first engineering hire for a new data science team at Gojek. They had lots of products and data but struggled to productionize models, so I led a team focused on that for about four years. We built an ML platform and, in particular, feature stores. Since that became my main focus, I joined Tecton to continue building in that space.

## What is a Feature Store? Core Problems and Solutions

**Q: Let's start with the fundamentals. What is a feature store, and what specific problems does it solve for machine learning teams?**

**Willem:** A feature store is an operational data system built specifically for machine learning. It’s opinionated about ML problems such as:

* Getting offline features into an online production environment
* Ensuring online–offline consistency so features models are trained on match what's served in production
* Letting data scientists ship features to production without relying on product engineers
* Versioning and managing transformation code
* Enabling sharing and reuse of features to avoid duplication across teams
* Monitoring data quality and drift, both online and for training datasets

Not all feature stores cover everything. For example, Feast doesn't handle transformations, while others like Tecton do. There's ongoing discussion about what should fall within a feature store's scope.

**Q: When you mention "transformations," are you referring to the process of converting raw data from warehouses, data lakes, or streams into features before they're stored in the feature store?**

**Willem:** Exactly. A feature store sits between raw data sources (streams, warehouses, lakes) and your production ML environment. If it supports transformations, it should be able to act on any of those sources and provide a serving layer that decouples ML from the underlying data infrastructure.

**Q: What does the user interface look like for data scientists? Do they interact with feature stores using familiar tools like SQL?**

**Willem:** There are two parts: creation and retrieval. For creation, stores that support transformations typically offer Python/PySpark or SQL to define features, then materialize them into storage like DynamoDB or Redis. For retrieval in production, you usually call an API rather than using SQL, because online inference is mostly key-value enrichment of tabular data and needs predictable performance. Some systems also support real-time "on-demand" transformations at request time—for example, fraud detection—when you need to combine live request metadata with precomputed features.

**Q: Could you give us a concrete example of how this works in practice? For instance, in an e-commerce fraud detection scenario where a transaction comes in, does the system retrieve the user's features from the feature store using their ID?**

**Willem:** That’s right.

## Why Feature Stores Are Popular: Separating Hype from Value

**Q: Feature stores have become a very popular topic in the ML community. What's driving all this interest and excitement?**

**Willem:** Partly general MLOps hype and market dynamics—people specialize to stand out. But there's real value: many companies tried ML at scale and learned that data—especially feature creation and iteration—is most of the work. A feature store sits between data scientists and production decisioning, so it can unlock significant business impact through reuse, speed, and consistency. Of course, vendor marketing contributes to the noise, but the underlying problems are real and important.

## Team Silos, Duplication, and Organizational Friction

**Q: Would you say the challenges that feature stores address are primarily technical problems or more organizational and process-related issues?**

**Willem:** Both. The list I gave has technical aspects, but the pain often starts organizationally:

* **Shipping features without engineers:** Product teams have their own OKRs, so data scientists become dependent and blocked. A feature store reduces that dependency
* **Sharing and reuse:** Teams are siloed, with limited communication and no standard way to publish semantics, dependencies, and intent of features. A feature store provides a central, trusted layer
* **Quality and monitoring:** Ensuring only valid, monitored data reaches models is both a process and a platform concern

In short, feature stores address technical consistency and performance while easing organizational friction around ownership, reuse, and speed to production.

**Q: Many teams build their own ML services to solve local problems, but in practice there's a lot of overlap—especially around user-based features. Teams often re-implement the same things from scratch. This seems like an organizational issue, right?**

**Willem:** Exactly. A lot of organizations embed ML folks into vertical product teams. Take a fraud team and an analytics team: they model the same entities—users, orders—so many features are reusable. But the fraud team may keep work private, so duplication happens. From a CDO/CIO perspective, duplicated data and effort is pure inefficiency. You can fix it with organizational changes, technology, or both.

**Q: So the solution would be to add a shared layer across teams—some kind of central platform. Is that where an ML platform and feature store come into play?**

**Willem:** Yes. Think of the ML lifecycle: transformations and storage, training, deployment, serving, experimentation. A feature store spans the transformation and serving parts. With a common platform, data scientists don’t need to wait on product engineers with other OKRs—especially if features are precomputed and regularly loaded into the store. They can discover features, train models, and ship faster.

## Ideal Setups, Real-World Examples, and When to Use Feature Stores

**Q: What would an ideal feature store setup look like from a practical standpoint?**

**Willem:** You write only transformations—no boilerplate. The system materializes and backfills features to offline and online stores. Models hit an API to enrich entities like user IDs at low latency. You deploy a simple model wrapper to production without a dedicated engineer. And a validation/monitoring layer ensures only good data reaches models.

**Q: Are there companies that actually have this kind of end-to-end setup in production today?**

**Willem:** Some do. Commercial platforms like Tecton provide a full flow—transformations, serving, monitoring. Feast, on the other hand, doesn’t handle transformations; you plug it in after upstream systems like dbt or Airflow/Spark.

## How Feature Stores Fit with Kubeflow, dbt, and Other ML Tools

**Q: How do tools like Kubeflow Pipelines fit into this ecosystem, and where do they overlap or complement feature stores?**

**Willem:** Great for model training—not for data transformations. Different tools cover different lifecycle stages.

## Feast vs Tecton: Open Source vs Enterprise Feature Store Solutions

**Q: Could you give us a quick overview of Feast and how it differs from other feature store solutions?**

**Willem:** Feast is an open-source feature store we built at Gojek (co-developed with Google Cloud). It ingests precomputed features from batch or streams, builds point-in-time-correct training sets, and serves online features at low latency through a unified API. We didn't focus heavily on a discovery UI because many organizations preferred duplicating pipelines to protect production. Feast decouples ML from data infrastructure and keeps training/serving access consistent.

**Q: How does Tecton compare to Feast, and what are the key differences in their approach?**

**Willem:** Tecton is a fuller enterprise platform: batch/stream/on-demand transformations, UI, monitoring, security, audit, compliance—the works. It’s for teams that want a turnkey solution now. Feast suits teams that prefer a “small tool in a larger stack.”

## Feature Store Architecture: Storage, Transformations, and APIs

**Q: Let's break down the architecture. What are the core components that make up a typical feature store system?**

**Willem:** Five pieces:

1. **Transformation engine** (Spark, SQL/warehouse) over streams and batch
2. **Storage**: offline (lake/warehouse like Delta/BigQuery/Snowflake) and online (low-latency KV like Redis/DynamoDB)
3. **Serving layer** (API/SDK)
4. **Registry** (definitions of sources, entities, transforms that the system materializes as jobs/infrastructure)
5. **Monitoring/ops** (ingestion metrics, distributions, drift; logging served features for validation and training reuse). Advanced platforms add a discovery UI tied to the registry

**Q: When should a team consider adopting a feature store, and when might it be overkill or not the right solution?**

**Willem:** It shines for online/tabular scenarios—fraud detection, recommendations, risk scores, pricing/ranking—where you enrich entities with features and need train/serve consistency. If you only do batch scoring or campaigns, you can often get by with SQL, BigQuery ML, and dbt/Great Expectations (though Tecton still helps with transforms/monitoring). For unstructured-heavy workloads like images/text, the value is mostly in serving/consistency; reuse benefits are smaller.

**Q: What does the adoption process look like for teams that want to implement a feature store? How do they get started?**

**Willem:** 

* **Feast:** Keep transforms upstream (dbt/Airflow/Spark). Register transformed tables/schemas, ingest from batch/streams, materialize to online, use the unified API for training and serving
* **Tecton:** Point it at raw logs/events and define transforms inside the platform. It sits between data infrastructure and production serving, covering more of the lifecycle

**Q: With features, each column should have a clear identity and intent. If it's just a binary blob, other teams won't discover or reuse it. Is that a fair assessment?**

**Willem:** Exactly. You can serve blobs online, but they'll be single-use. That doesn't build team-wide efficiency.

**Q: What about a scenario where an image model outputs "probability this is a car"? We store that score as a feature and fetch it online by image ID. Would this be a good use case for a feature store?**

**Willem:** Perfect. Store outputs like `is_car` (0/1) and `p_car` (e.g., 0.7). Those are great downstream features. What you *don't* usually do is store the raw image in the feature store. The request will carry a pointer like an S3 URL; you fetch the image elsewhere, run the model, then write the **output** back—often into a stream that flows into the feature store. Models are just transformations; their outputs become new features.

## Resources and Hands-on Learning: Where to Start with Feature Stores

**Q: For an individual contributor who wants to learn about feature stores, where would you recommend they start their learning journey?**

**Willem:** The MLOps community (DataOps, Open-source, General channels) has tons of material. The Tecton blog has deeper thinking on the category. Hands-on: go to **feast.dev**, run Docker Compose, and try the example notebook. Feast docs also cover when to use—or not use—a feature store. Look at real organization write-ups too, like Monzo's lightweight approach.

## Production Workflows: Validation, Streaming, and Technology Choices

**Q: What does a typical workflow look like for creating features, testing them offline, and ensuring consistency between offline training and online serving?**

**Willem:** Treat **streaming** and **batch** separately. Build validations at four points:

1. Streaming ingestion/transform
2. Batch transform (pre-ingestion to offline store)
3. Training set build (pre-train)
4. Serving time (pre-serve/model side)

Use tools like **Great Expectations** or **TFDV**. With no feature store, you’ll write more boilerplate checks in serving code.

**Q: When it comes to building real-time features, how do you choose between technologies like Flink versus Spark?**

**Willem:** I like **Flink**—great API and technology. We use **Spark** with Feast for its ecosystem and connector support and because it runs easily across clouds and on-premises. Cloud support for Flink is improving, so parity is getting closer.

**Q: What APIs and programming interfaces do you typically use for defining transformations in feature stores?**

**Willem:** In **Tecton**: PySpark, Spark SQL, or warehouse SQL (Snowflake/BigQuery) for batch; Python for on-demand/request-time transforms. **Feast** doesn’t handle transforms today (we’re considering on-demand, but unifying offline/online parity is tricky).

**Q: At what organization size does it make sense to invest in a feature store? When is it worth the complexity?**

**Willem:** Historically, when you have multiple use cases or teams. We'd love to make it valuable for a single data scientist on a single project, but today it's most effective when a platform team serves several solution teams. For a tiny startup (one data engineer + one data scientist), it's often overkill—until ML becomes core, use cases multiply, and teams decouple.

**Q: If a company starts without a feature store and grows into needing one, is it difficult to adopt later, or can they migrate relatively smoothly?**

**Willem:** The main friction is where **transformations** live. If you already use dbt/Airflow/Spark, adding Feast is simple (it consumes transformed data). With Tecton, decide whether to keep transforms upstream or move them into Tecton. Greenfield projects may choose Tecton; brownfield projects might keep existing pipelines.

**Q: How well do dbt and feature stores work together? Is this a common and effective combination?**

**Willem:** Yes. Warehouses (BigQuery/Snowflake) are dominant; dbt covers 80–90% of batch transforms for many organizations. Analysts can contribute SQL-based features that drive the bottom line—dbt plus a feature store enables that.

**Q: How do you handle backfilling new features with historical data? What's the typical process?**

**Willem:** **Feast:** Upstream jobs backfill; then you call Feast to (re)ingest to online.
**Tecton:** Change the transform; Tecton detects what's missing and backfills from the chosen start date automatically.

## Who Should Own Features? Governance and Migration Strategies

**Q: From an organizational perspective, who should own features? Should it be the source teams, the consuming teams, or a central platform group?**

**Willem:** Don’t gatekeep early. Let use-case teams create features and iterate. As reuse patterns emerge, a central team can assume ownership of critical or duplicated features—curate “golden” sets and coordinate deduplication. Ownership should follow importance and production impact.

**Q: How do feature stores differ from traditional ETL processes combined with a data catalog? What makes them distinct?**

**Willem:** A feature store is an **opinionated, ML-operational** data system. It unifies **offline** and **low-latency online** serving with **identical semantics** for train/serve. Classic data platforms/catalogs don’t focus on that online path or parity. A feature store bridges data and ML platforms.

Thank you for joining us today, Willem. This conversation really clarified where feature stores help and where they might not be the right solution.
