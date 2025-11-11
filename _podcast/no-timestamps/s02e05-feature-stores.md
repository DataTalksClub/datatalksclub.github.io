---
title: 'Feature Stores for MLOps: Real-Time Feature Engineering, Feast & Tecton Guide'
short: Feature Stores in MLOps Explained
description: Discover feature store use cases, real-time features with Feast & Tecton,
  build scalable MLOps to speed production, cut duplication and detect drift.
tags:
- feature-stores
- feast
- tecton
- mlops
- machine-learning
- data-science
- ml-platform
- ml-architecture
- willem-pienaar
- gojek
guests:
- willempienaar
image: images/podcast/s02e05-feature-stores.jpg
season: 2
episode: 5
ids:
  youtube: FQYTb4uWljQ
  anchor: Feature-Stores-Cutting-through-the-Hype---Willem-Pienaar-ept6m8/a-a4hlg3r
links:
  youtube: https://www.youtube.com/watch?v=FQYTb4uWljQ
  anchor: https://anchor.fm/datatalksclub/episodes/Feature-Stores-Cutting-through-the-Hype---Willem-Pienaar-ept6m8/a-a4hlg3r
  spotify: https://open.spotify.com/episode/05YnfTWbplXwOwicR2doy3
  apple: https://podcasts.apple.com/us/podcast/feature-stores-cutting-through-the-hype-willem-pienaar/id1541710331?i=1000508782957
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