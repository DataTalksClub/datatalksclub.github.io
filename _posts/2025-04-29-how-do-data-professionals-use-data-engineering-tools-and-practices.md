---
authors:
- valeriiakuka
description: Results of our DataTalks.Club Survey
image: images/posts/2025-04-29-how-do-data-professionals-use-data-engineering-tools-and-practices/cover.jpg
layout: post
subtitle: Results of our DataTalks.Club Survey
tags:
- survey
- data-engineering
- '2024'
- test
title: How Do Data Professionals Use Data Engineering Tools and Practices?
datepublished: '2025-04-29'
date: '2025-04-29'
---

We [surveyed](https://docs.google.com/forms/d/e/1FAIpQLScdx1FAIp2GDGgiMf7xu-I1PfhsQBJDvFstGmWmWbpP4S69Zg/viewform){:target="_blank"} over 200 data professionals involved in data engineering tasks to understand which tools, platforms, and methodologies they rely on.

<figure>
<img src="/images/posts/2025-04-29-how-do-data-professionals-use-data-engineering-tools-and-practices/image1.png"  />
<figcaption>Our survey form</figcaption>
</figure>

In this article, we share key findings and major trends in storage, orchestration, integration, and more.

## Data Storage Solutions

Organizations rely on a mix of established and emerging storage options. Traditional relational databases are still dominant, while newer architectures, such as data lakehouses, are rapidly gaining ground.

- **Relational Databases:** Employed by 70.9% of respondents, they remain the go-to solution for structured, transactional workloads.
- **Data Warehouses & Lakehouses:** Both are used by 53.6% of respondents, indicating a trend toward combining structured storage with modern, flexible architectures.
- **Data Lakes:** Reported by 49.8%, continuing to serve as a repository for raw data ingestion.
- **Lower Usage:** NoSQL (27.8%), vector databases (18.6%), and niche options like MinIO (0.8%) are less common, reflecting their more specialized or emerging status.



\[DATA\]

<span class="mark">Which data storage solutions do you use? (Select all that apply)</span>

- **Relational Databases** – 168 (70.9%)
- **Data Warehouses** – 127 (53.6%)
- **Data Lakehouses** – 127 (53.6%)
- **Data Lakes** – 118 (49.8%)
- **NoSQL Databases** – 66 (27.8%)
- **Vector Databases** – 44 (18.6%)
- **MinIO** – 2 (0.8%)
- Others (Salesforce, HDFS, “Not Sure”) – each \<1%



\[DATA\]

Relational databases are a cornerstone for many organizations, given their maturity and robustness for transactional workloads. The near parity in adoption between data warehouses and data lakehouses indicates a trend toward converging traditional structured storage with more flexible, modern architectures.

While data lakes remain popular for raw, unprocessed data, the rise of lakehouses points to an industry move toward unifying the benefits of both warehouses and lakes. The relatively lower usage of niche solutions like vector databases suggests that while they receive buzz in certain AI/ML circles, they have yet to achieve widespread adoption in day-to-day operations.

## Data Warehouses

Data warehouses are key for business intelligence and analytics. Major cloud vendors dominate the landscape, providing fast query performance and advanced integration.

- **Google BigQuery:** Leads with 38.6%, benefiting from its seamless integration in the Google Cloud ecosystem.
- **Snowflake:** Used by 32.1%, showing strong competition in the cloud analytics space.
- **Amazon Redshift (25%) and Azure Synapse Analytics (20.1%):** Also significant, reinforcing the presence of diversified cloud vendor solutions.
- **Others:** Smaller players (e.g., ClickHouse at 8.2%) indicate that while there’s room for specialized solutions, the market is largely consolidated around the major vendors.



\[DATA\]

Which data warehouse solutions do you use?

- **Google BigQuery** – 71 (38.6%)
- **Snowflake** – 59 (32.1%)
- **Amazon Redshift** – 46 (25%)
- **Azure Synapse Analytics** – 37 (20.1%)
- **ClickHouse** – 15 (8.2%)
- Others (Vertica, Motherduck, Databricks, Greenplum) – each \<4%



\[DATA\]

The survey data shows Google BigQuery as the leading choice, which may be attributed to its integration within the broader Google Cloud ecosystem that is well-regarded for data science and machine learning workloads. Snowflake and Amazon Redshift also enjoy strong adoption, reflecting a competitive market where multiple cloud vendors address analytical needs. The presence of Azure Synapse Analytics and other smaller platforms further demonstrates that organizations weigh considerations such as integration with existing cloud services and pricing structures when choosing.

## Data Lakes and Lakehouses

### Data Lakes

Cloud-based storage services are the primary choice for handling raw and unprocessed data, reflecting a shift towards managed, scalable solutions.

- **Amazon S3:** Dominates with 52.8%, followed by
- **Google Cloud Storage:** 34.2%, and
- **Azure Data Lake Storage:** 30.6%.
- Legacy systems like Apache Hadoop (HDFS) are present but on a smaller scale (19.2%), emphasizing an industry-wide shift to cloud-native options.



\[DATA\]

<span class="mark">Which data lake solutions do you use? (Select all that apply)</span>

- **Amazon S3** – 102 (52.8%)
- **Google Cloud Storage** – 66 (34.2%)
- **Azure Data Lake Storage** – 59 (30.6%)
- **Apache Hadoop (HDFS)** – 37 (19.2%)
- **MinIO** – 3 (1.6%)
- Other/None – minimal



\[DATA\]

Cloud object storage services dominate as data lakes of choice, emphasizing their scalability, durability, and ease of integration with various processing engines. The significant adoption of services like Amazon S3 and Google Cloud Storage underscores the importance of cloud infrastructure for modern data operations. The relatively lower usage of on-premise or legacy systems (like HDFS) hints at a broader industry transition toward fully managed, cloud-native environments.

### Lakehouse Architectures

While still emerging, lakehouse architectures are being trialed by a subset of respondents, with Databricks at the forefront.

- **Databricks:** Used by 31.3% of survey participants, making it the leading lakehouse solution.
- **Other Technologies:** Apache Iceberg (13%), Delta Lake (12.5%), and Apache Hudi (2.6%) have more modest adoption.
- **Adoption Status:** Over half (58.3%) report not using any lakehouse solutions, suggesting that many organizations are either in a pilot phase or see limited current need for this hybrid model.



\[DATA\]

<span class="mark">Do you use any lakehouse architecture solutions? (Select all that apply)</span>

- **Databricks** – 60 (31.3%)
- **Apache Iceberg** – 25 (13%)
- **Delta Lake** – 24 (12.5%)
- **Apache Hudi** – 5 (2.6%)
- **Not using any Lakehouse** – 112 (58.3%)



\[DATA\]

Although lakehouse concepts are gaining traction, over half of the survey respondents still do not utilize this architecture, which may suggest a cautious approach toward new methodologies or a limited requirement in some organizations. Databricks leads among lakehouse adopters, benefiting from its well-integrated ecosystem and community support. The relatively modest adoption rates for Apache Iceberg, Delta Lake, and Apache Hudi reflect an experimental phase where many organizations still evaluate the benefits versus the complexity of a lakehouse approach.

## Workflow Orchestration

Workflow orchestration is crucial for managing data pipelines, but its adoption varies based on team complexity and project scale.

- **Apache Airflow:** The dominant player with 48.3%, favored for its mature ecosystem and community support.
- **Other Tools:** AWS Step Functions (12%), Mage (7.2%), Prefect (6.7%), and Dagster (4.8%) serve niche or emerging needs.
- **No Orchestration:** Notably, 35.9% of respondents do not utilize any orchestration tool, which might reflect simpler workflows or resource constraints in smaller teams.



\[DATA\]

<span class="mark">Which workflow orchestration tools do you use to manage data pipelines? (Select all that apply)</span>

- **Apache Airflow** – 101 (48.3%)
- **AWS Step Functions** – 25 (12%)
- **Prefect** – 14 (6.7%)
- **Mage** – 15 (7.2%)
- **Dagster** – 10 (4.8%)
- **No orchestration used** – 75 (35.9%)
- Others (Beam, GitHub Actions, Jenkins) – each \<2%



Apache Airflow is the dominant player, likely because of its mature ecosystem and widespread community support. However, the notable fraction of respondents not using any orchestration tools suggests that smaller teams or straightforward workflows may not yet require the overhead of dedicated scheduling systems. The varied adoption of alternatives like Prefect and Dagster indicates ongoing experimentation with newer and sometimes more streamlined orchestration solutions.

## Data Integration (ETL/ELT)

In data integration, modular and SQL-driven approaches are gaining favor, although many organizations still rely on custom or manual solutions.

- **dbt:** Leads at 33.5%, indicating strong momentum behind this modern transformation tool.
- **Other Tools:** Airbyte (8.4%), Fivetran (7.9%), and dlt (6.9%) are present in a smaller share, while Talend registers 5.4%.
- **Manual/Custom Approaches:** Almost half (46.3%) do not use formal ETL tools, highlighting both the persistence of legacy practices and opportunities for greater automation.



\[DATA\]

<span class="mark">Which data integration or ETL/ELT tools do you use? (Select all that apply)</span>

- **dbt** – 68 (33.5%)
- **Airbyte** – 17 (8.4%)
- **dlt** – 14 (6.9%)
- **Fivetran** – 16 (7.9%)
- **Talend** – 11 (5.4%)
- **No ETL tools used** – 94 (46.3%)
- Others (custom Python scripts, self-built) – many mentioned



\[DATA\]

The adoption of dbt reflects its growing popularity and ease of use in transforming data at scale, reinforcing the trend towards modular, SQL-driven approaches to data engineering. Yet, almost half of the respondents still depend on custom or manual solutions, which implies a clear maturity gap in tooling. This reliance on bespoke methods may also signal opportunities for improved automation and integration frameworks, especially in organizations lacking dedicated data teams.

## Data Processing Frameworks

Data processing frameworks vary widely in scale. Many professionals favor robust, well-known libraries for their flexibility and ease of use.

- **Pandas:** The leading tool for data manipulation at 69.5%, reflecting its simplicity for handling small- to medium-sized tasks.
- **Apache Spark:** Adopted by 46.6%, especially where scalable, distributed processing is required.
- **Other Options:** Apache Flink (7.6%), Dask (4.5%), and Apache Beam (4.9%) have smaller footprints. Notably, 14.8% report not using any formal processing framework, which may indicate reliance on ad hoc methods or simpler workflows.



\[DATA\]

<span class="mark">Which frameworks do you use for data processing? (Select all that apply)</span>

- **Pandas** – 155 (69.5%)
- **Apache Spark** – 104 (46.6%)
- **Apache Flink** – 17 (7.6%)
- **Dask** – 10 (4.5%)
- **Apache Beam** – 11 (4.9%)
- **Polars/DuckDB** – mentioned but minimal
- **No processing frameworks used** – 33 (14.8%)



\[DATA\]

Pandas remains the go-to tool for many professionals, primarily due to its intuitive interface and versatility for smaller to medium-sized data tasks. Meanwhile, Apache Spark's adoption for scalability in handling big data workloads confirms its integral role in more demanding environments. The smaller footprints of newer or niche frameworks (like Flink, Dask, or Beam) suggest they are still establishing themselves as reliable alternatives in a competitive ecosystem.

## Observability and Monitoring

Ensuring data quality and pipeline reliability is critical, yet formal observability solutions are still underutilized. A majority (76.6%) of respondents do not use dedicated observability tools.

Among those that do, Great Expectations (10.3%) and Monte Carlo (6%) are the most noted, with only minor representation from Soda.io and Databand (each 2.7%).

\[DATA\]

<span class="mark">Do you use any data observability or monitoring tools for your pipelines? (Select all that apply)</span>

- **Great Expectations** – 19 (10.3%)
- **Monte Carlo** – 11 (6%)
- **Soda.io** – 5 (2.7%)
- **Databand** – 5 (2.7%)
- **No observability tools** – 141 (76.6%)
- Others (custom scripts, Grafana) – \<3% each



\[DATA\]

The lack of observability tool adoption suggests that many organizations are either early in maturing their data infrastructure or rely on ad hoc methods. This gap represents a significant area for improvement, as enhanced observability could lead to more proactive issue resolution and optimized system performance.

## Cloud Platforms

Cloud adoption remains robust in data engineering, with the choice of platform often reflecting broader enterprise strategies and legacy considerations.

- **AWS:** Leads with 46.7%, underscoring its comprehensive service offerings and established market presence.
- **Azure and Google Cloud (GCP):** Hold significant shares at 35.2% and 33.8% respectively, illustrating competitive alternatives within the cloud sphere.
- **On-Premise:** Still in use by 21.9% of respondents, indicating that despite the cloud’s advantages, traditional infrastructures continue to serve essential roles in some organizations.



\[DATA\]

<span class="mark">Which cloud platforms do you use for data engineering workloads? (Select all that apply)</span>

- **AWS** – 98 (46.7%)
- **Azure** – 74 (35.2%)
- **Google Cloud (GCP)** – 71 (33.8%)
- **On-Premise** – 46 (21.9%)
- Others (Yandex, Huawei) – very limited



\[DATA\]

AWS leads in adoption, reflecting its long-standing prominence and breadth of services in the cloud ecosystem. Azure and GCP also maintain substantial market shares, driven by their unique strengths and integration with enterprise products. A notable segment still uses on-premise solutions, indicating that while cloud adoption is high, there remains a dependency on traditional infrastructures in certain contexts or regulatory environments.

## Data Governance

Data governance remains a weak link for many teams. Automated tooling is lagging, with many organizations relying on manual methods.

- **Manual Cataloging:** Used by 20.1% of respondents.
- **Formal Tools:** Apache Atlas (6.3%), Collibra (5.3%), and Alation (4.2%) see limited use.
- **No Governance Tooling:** A substantial majority (64.6%) are not using any specialized governance tools, pointing to an area ripe for improvement as data ecosystems become more complex.



\[DATA\]

<span class="mark">Which data governance tools or practices do you use? (Select all that apply)</span>

- **Manual Cataloging** – 38 (20.1%)
- **Apache Atlas** – 12 (6.3%)
- **Collibra** – 10 (5.3%)
- **Alation** – 8 (4.2%)
- **Not using any governance tooling** – 122 (64.6%)
- Others (Atlan, OpenMetadata, DataHub) – very limited



\[DATA\]

The survey reveals a significant reliance on manual cataloging or a complete lack of governance tooling, highlighting an area where many organizations are lagging behind. Without automated governance frameworks, data quality, security, and compliance may be compromised, particularly as data ecosystems become complex. These gaps call for more robust and accessible solutions that can integrate seamlessly with existing workflows.

## Real-Time Data Processing

There is a split in the approach to real-time processing, some teams invest in dedicated frameworks, while many continue with batch processing.

- **Dedicated Frameworks:** 26.7% actively use specialized tools for real-time data processing.
- **Minimal Real-Time Use:** An additional 28.1% engage in real-time processing on a limited basis.
- **No Real-Time Processing:** 47% of respondents have not adopted any real-time strategies, suggesting that for many, batch processing remains adequate.



\[DATA\]

<span class="mark">Do you work with real-time data processing?</span>

- **Yes, using dedicated frameworks** – 58 (26.7%)
- **Yes, minimally** – 61 (28.1%)
- **No** – 102 (47%)



\[DATA\]

Approximately half of the respondents do not engage in real-time processing, suggesting that for many organizations, batch processing remains sufficient for their current needs. However, the considerable share using dedicated or minimal real-time frameworks indicates that a segment of the industry is investing in faster, near-real-time analytics, potentially a precursor to more widespread adoption as data velocity increases.

## Data Quality

Data quality practices are mixed. Organizations are shifting toward automation, yet manual oversight still predominates.

- **Manual Checks:** Rely on human oversight (48.8%).
- **Automated Tests:** Used by 39.2%, showing a trend toward reducing manual intervention.
- **Validation Tools:** Such as Great Expectations, employed by 22.6%.
- **No Quality Practices:** Alarmingly, 26.7% do not implement any data quality measures, highlighting potential vulnerabilities.



\[DATA\]

<span class="mark">How do you ensure data quality in your workflows? (Select all that apply)</span>

- **Manual Checks** – 106 (48.8%)
- **Automated Tests** – 85 (39.2%)
- **Validation Tools (e.g., Great Expectations)** – 49 (22.6%)
- **No practices** – 58 (26.7%)



\[DATA\]

The prevalence of manual checks suggests that many teams rely on human oversight for data quality, a practice that is both time-consuming and prone to error. Adopting automated tests and validation tools shows a positive shift toward streamlining these processes. However, the notable share of organizations with no data quality practices underscores a critical vulnerability that could lead to operational inefficiencies or misinformed decisions.

## Key Challenges

The survey identifies common hurdles that data engineering teams confront daily. The most significant challenge echoes through many facets of the data lifecycle.

- **Data Quality:** The top challenge at 68.8%, consistently affecting multiple stages of operations.
- **Data Integration:** Cited by 59.6%, reflecting difficulties in consolidating diverse data sources.
- **Scaling Pipelines:** A concern for 53.8% of respondents, emphasizing issues around growing data volumes.
- **Security and Compliance:** Reported by 40.4%, underscoring the increasing importance of regulatory and security measures.



\[DATA\]

<span class="mark">What are the primary challenges you face in data engineering? (Select all that apply)</span>

- **Data Quality** – 143 (68.8%)
- **Integration of Data Sources** – 124 (59.6%)
- **Scaling Pipelines** – 112 (53.8%)
- **Security and Compliance** – 84 (40.4%)



\[DATA\]

The most cited challenge, data quality, resonates throughout nearly every stage of the data lifecycle. Integration issues and scaling challenges further illustrate that while many organizations have embraced digital transformation, they still contend with legacy systems and infrastructural constraints. Security and compliance, while secondary in this survey, remain critical given the increasing regulatory scrutiny and the high stakes of data breaches. These challenges underscore the need for more robust, integrated solutions to address technical and organizational hurdles.

## Team Sizes

The survey reveals that many data operations are driven by small teams or solo practitioners.

- **Small Teams (1–5 members):** The largest group, with 117 teams.
- **Solo Practitioners:** 55 professionals operate independently.
- **Larger Teams:** There are fewer teams with 6+ members, which may explain the conservative approach toward adopting more complex, automated systems.



\[DATA\]

<span class="mark">How many people are in your data engineering team(s)?</span>

- **1–5 members** – 117
- **6–10** – 21
- **11–20** – 19
- **21–50** – 8
- **51+** – 12
- **Solo (0)** – 55



\[DATA\]

The data indicates that most teams are small, with many professionals operating in solo or very small groups. This size limitation likely contributes to a cautious approach toward adopting more complex infrastructures—such as automated observability stacks, advanced orchestration systems, or comprehensive lakehouse architectures. The lean nature of most teams stresses the importance of tools that are not only powerful but also easy to implement and maintain.

## Conclusion

The survey offers a clear perspective on where the industry stands today and highlights critical areas for potential improvement as organizations scale their data operations.

### Takeaway 1: Adoption of Mature vs. Emerging Technologies

Established tools like relational databases, Apache Airflow, and Pandas are widely used and form the backbone of many operations.

Emerging trends include the movement toward lakehouses and automated data quality and governance practices, areas where adoption is still in progress.

### Takeaway 2: Resource Constraints Drive Tool Choices

The prevalence of small teams and solo practitioners explains the reliance on tools that are both effective and straightforward to implement.

In contrast, the limited use of observability and automated governance indicates potential growth areas as organizations scale.

### Takeaway 3: Fragmentation and Opportunity

While cloud-based solutions are almost universal, the fragmentation in tooling for orchestration, governance, and real-time processing suggests ample opportunities for more unified and automated frameworks.