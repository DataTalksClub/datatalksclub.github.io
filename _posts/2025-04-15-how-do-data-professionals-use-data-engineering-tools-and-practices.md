---
authors:
- valeriiakuka
description: Results of our DataTalks.Club Survey
image: tbd
layout: post
subtitle: Results of our DataTalks.Club Survey
tags:
- survey
- ai
- '2024'
title: How Do Professionals Use Data Engineering Tools and Practices?
charts: true
---

We [surveyed](https://docs.google.com/forms/d/e/1FAIpQLScdx1FAIp2GDGgiMf7xu-I1PfhsQBJDvFstGmWmWbpP4S69Zg/viewform){:target="_blank"} over 200 data professionals involved in data engineering tasks to understand which tools, platforms, and methodologies they rely on.

In this article, we share key findings and major trends in storage, orchestration, integration, and more.

Let's explore the data.

## Data Storage Solutions

Organizations rely on a mix of established and emerging storage options. Traditional relational databases remain dominant, while newer architectures, such as data lakehouses, are rapidly gaining ground.

* **Relational Databases:** Employed by 70.9% of respondents, they remain the go-to solution for structured, transactional workloads.  
* **Data Warehouses & Lakehouses:** Both are used by 53.6% of respondents, indicating a trend toward combining structured storage with modern, flexible architectures.  
* **Data Lakes:** Reported by 49.8%, continuing to serve as repositories for raw data ingestion.  
* **Lower Usage:** NoSQL (27.8%), vector databases (18.6%), and niche options like MinIO (0.8%) are less common, reflecting their more specialized or emerging status.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which data storage solutions do you use?"
          data-labels='["Relational Databases", "Data Warehouses", "Data Lakehouses", "Data Lakes", "NoSQL Databases", "Vector Databases", "MinIO"]'
          data-values='[70.9, 53.6, 53.6, 49.8, 27.8, 18.6, 0.8]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Relational databases lead in adoption, followed closely by data warehouses and lakehouses.</figcaption>
</figure>

Relational databases are a cornerstone for many organizations, given their maturity and robustness for transactional workloads. The near parity in adoption between data warehouses and data lakehouses indicates a trend toward converging traditional structured storage with more flexible, modern architectures.

While data lakes remain popular for raw, unprocessed data, the rise of lakehouses points to an industry move toward unifying the benefits of both warehouses and lakes. The relatively lower usage of niche solutions like vector databases suggests that while they receive attention in certain AI/ML circles, they have yet to achieve widespread adoption in day-to-day operations.

## Data Warehouses

Data warehouses are key for business intelligence and analytics. Major cloud vendors dominate the landscape, providing fast query performance and advanced integration.

* **Google BigQuery:** Leads with 38.6%, benefiting from its seamless integration in the Google Cloud ecosystem.  
* **Snowflake:** Used by 32.1%, showing strong competition in the cloud analytics space.  
* **Amazon Redshift (25%) and Azure Synapse Analytics (20.1%):** Also significant, reinforcing the presence of diversified cloud vendor solutions.  
* **Others:** Smaller players (e.g., ClickHouse at 8.2%) indicate that while there's room for specialized solutions, the market is largely consolidated around the major vendors.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which data warehouse solutions do you use?"
          data-labels='["Google BigQuery", "Snowflake", "Amazon Redshift", "Azure Synapse Analytics", "ClickHouse"]'
          data-values='[38.6, 32.1, 25, 20.1, 8.2]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Google BigQuery leads the data warehouse market, followed by Snowflake and Amazon Redshift.</figcaption>
</figure>

The survey data shows Google BigQuery as the leading choice, which may be attributed to its integration within the broader Google Cloud ecosystem that is well-regarded for data science and machine learning workloads. Snowflake and Amazon Redshift also enjoy strong adoption, reflecting a competitive market where multiple cloud vendors address analytical needs. The presence of Azure Synapse Analytics and other smaller platforms further demonstrates that organizations weigh considerations such as integration with existing cloud services and pricing structures when choosing.

## Data Lakes and Lakehouses

### Data Lakes

Cloud-based storage services are the primary choice for handling raw and unprocessed data, reflecting a shift toward managed, scalable solutions.

* **Amazon S3:** Dominates with 52.8%, followed by  
* **Google Cloud Storage:** 34.2%, and  
* **Azure Data Lake Storage:** 30.6%.  
* Legacy systems like Apache Hadoop (HDFS) are present but on a smaller scale (19.2%), emphasizing an industry-wide shift to cloud-native options.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which data lake solutions do you use?"
          data-labels='["Amazon S3", "Google Cloud Storage", "Azure Data Lake Storage", "Apache Hadoop (HDFS)", "MinIO"]'
          data-values='[52.8, 34.2, 30.6, 19.2, 1.6]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Amazon S3 dominates the data lake market, with Google Cloud Storage and Azure Data Lake Storage following.</figcaption>
</figure>

Cloud object storage services dominate as data lakes of choice, emphasizing their scalability, durability, and ease of integration with various processing engines. The significant adoption of services like Amazon S3 and Google Cloud Storage underscores the importance of cloud infrastructure for modern data operations. The relatively lower usage of on-premise or legacy systems (like HDFS) hints at a broader industry transition toward fully managed, cloud-native environments.

### Lakehouse Architectures

While still emerging, lakehouse architectures are being trialed by a subset of respondents, with Databricks at the forefront.

* **Databricks:** Used by 31.3% of survey participants, making it the leading lakehouse solution.  
* **Other Technologies:** Apache Iceberg (13%), Delta Lake (12.5%), and Apache Hudi (2.6%) have more modest adoption.  
* **Adoption Status:** Over half (58.3%) report not using any lakehouse solutions, suggesting that many organizations are either in a pilot phase or see limited current need for this hybrid model.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Do you use any lakehouse architecture solutions?"
          data-labels='["Not using any Lakehouse", "Databricks", "Apache Iceberg", "Delta Lake", "Apache Hudi"]'
          data-values='[58.3, 31.3, 13, 12.5, 2.6]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Most organizations are not using lakehouse architectures, with Databricks being the most popular choice among adopters.</figcaption>
</figure>

Although lakehouse concepts are gaining traction, over half of the survey respondents still do not utilize this architecture, which may suggest a cautious approach toward new methodologies or a limited requirement in some organizations. Databricks leads among lakehouse adopters, benefiting from its well-integrated ecosystem and community support. The relatively modest adoption rates for Apache Iceberg, Delta Lake, and Apache Hudi reflect an experimental phase where many organizations still evaluate the benefits versus the complexity of a lakehouse approach.

## Workflow Orchestration

Workflow orchestration is crucial for managing data pipelines, but its adoption varies based on team complexity and project scale.

* **Apache Airflow:** The dominant player with 48.3%, favored for its mature ecosystem and community support.  
* **Other Tools:** AWS Step Functions (12%), Mage (7.2%), Prefect (6.7%), and Dagster (4.8%) serve niche or emerging needs.  
* **No Orchestration:** Notably, 35.9% of respondents do not utilize any orchestration tool, which might reflect simpler workflows or resource constraints in smaller teams.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which workflow orchestration tools do you use?"
          data-labels='["Apache Airflow", "No orchestration used", "AWS Step Functions", "Mage", "Prefect", "Dagster"]'
          data-values='[48.3, 35.9, 12, 7.2, 6.7, 4.8]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Apache Airflow dominates workflow orchestration, though many teams still don't use any orchestration tools.</figcaption>
</figure>

Apache Airflow is the dominant player, likely because of its mature ecosystem and widespread community support. However, the notable fraction of respondents not using any orchestration tools suggests that smaller teams or straightforward workflows may not yet require the overhead of dedicated scheduling systems. The varied adoption of alternatives like Prefect and Dagster indicates ongoing experimentation with newer and sometimes more streamlined orchestration solutions.

## Data Integration (ETL/ELT)

In data integration, modular and SQL-driven approaches are gaining favor, although many organizations still rely on custom or manual solutions.

* **dbt:** Leads at 33.5%, indicating strong momentum behind this modern transformation tool.  
* **Other Tools:** Airbyte (8.4%), Fivetran (7.9%), and dlt (6.9%) are present in a smaller share, while Talend registers 5.4%.  
* **Manual/Custom Approaches:** Almost half (46.3%) do not use formal ETL tools, highlighting both the persistence of legacy practices and opportunities for greater automation.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which data integration or ETL/ELT tools do you use?"
          data-labels='["No ETL tools used", "dbt", "Airbyte", "Fivetran", "dlt", "Talend"]'
          data-values='[46.3, 33.5, 8.4, 7.9, 6.9, 5.4]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Nearly half of organizations don't use formal ETL tools, with dbt being the most popular choice among adopters.</figcaption>
</figure>

The adoption of dbt reflects its growing popularity and ease of use in transforming data at scale, reinforcing the trend toward modular, SQL-driven approaches to data engineering. Yet, almost half of the respondents still depend on custom or manual solutions, which implies a clear maturity gap in tooling. This reliance on bespoke methods may also signal opportunities for improved automation and integration frameworks, especially in organizations lacking dedicated data teams.

## Data Processing Frameworks

Data processing frameworks vary widely in scale. Many professionals favor robust, well-known libraries for their flexibility and ease of use.

* **Pandas:** The leading tool for data manipulation at 69.5%, reflecting its simplicity for handling small- to medium-sized tasks.  
* **Apache Spark:** Adopted by 46.6%, especially where scalable, distributed processing is required.  
* **Other Options:** Apache Flink (7.6%), Dask (4.5%), and Apache Beam (4.9%) have smaller footprints. Notably, 14.8% report not using any formal processing framework, which may indicate reliance on ad hoc methods or simpler workflows.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which frameworks do you use for data processing?"
          data-labels='["Pandas", "Apache Spark", "No processing frameworks", "Apache Flink", "Apache Beam", "Dask"]'
          data-values='[69.5, 46.6, 14.8, 7.6, 4.9, 4.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Pandas and Apache Spark are the most popular data processing frameworks.</figcaption>
</figure>

Pandas remains the go-to tool for many professionals, primarily due to its intuitive interface and versatility for smaller to medium-sized data tasks. Meanwhile, Apache Spark's adoption for scalability in handling big data workloads confirms its integral role in more demanding environments. The smaller footprints of newer or niche frameworks (like Flink, Dask, or Beam) suggest they are still establishing themselves as reliable alternatives in a competitive ecosystem.

## Observability and Monitoring

Ensuring data quality and pipeline reliability is critical, yet formal observability solutions are still underutilized. A majority (76.6%) of respondents do not use dedicated observability tools.

Among those that do, Great Expectations (10.3%) and Monte Carlo (6%) are the most noted, with only minor representation from Soda.io and Databand (each 2.7%).

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Do you use any data observability or monitoring tools?"
          data-labels='["No observability tools", "Great Expectations", "Monte Carlo", "Soda.io", "Databand"]'
          data-values='[76.6, 10.3, 6, 2.7, 2.7]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Most organizations don't use formal observability tools, with Great Expectations being the most popular choice.</figcaption>
</figure>

The lack of observability tool adoption suggests that many organizations are either early in maturing their data infrastructure or rely on ad hoc methods. This gap represents a significant area for improvement, as enhanced observability could lead to more proactive issue resolution and optimized system performance.

## Cloud Platforms

Cloud adoption remains robust in data engineering, with the choice of platform often reflecting broader enterprise strategies and legacy considerations.

* **AWS:** Leads with 46.7%, underscoring its comprehensive service offerings and established market presence.  
* **Azure and Google Cloud (GCP):** Hold significant shares at 35.2% and 33.8% respectively, illustrating competitive alternatives within the cloud sphere.  
* **On-Premise:** Still in use by 21.9% of respondents, indicating that despite the cloud's advantages, traditional infrastructures continue to serve essential roles in some organizations.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which cloud platforms do you use for data engineering workloads?"
          data-labels='["AWS", "Azure", "Google Cloud (GCP)", "On-Premise"]'
          data-values='[46.7, 35.2, 33.8, 21.9]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>AWS leads in cloud platform adoption, followed by Azure and Google Cloud.</figcaption>
</figure>

AWS leads in adoption, reflecting its long-standing prominence and breadth of services in the cloud ecosystem. Azure and GCP also maintain substantial market shares, driven by their unique strengths and integration with enterprise products. A notable segment still uses on-premise solutions, indicating that while cloud adoption is high, there remains a dependency on traditional infrastructures in certain contexts or regulatory environments.

## Data Governance

Data governance remains a weak link for many teams. Automated tooling is lagging, with many organizations relying on manual methods.

* **Manual Cataloging:** Used by 20.1% of respondents.  
* **Formal Tools:** Apache Atlas (6.3%), Collibra (5.3%), and Alation (4.2%) see limited use.  
* **No Governance Tooling:** A substantial majority (64.6%) are not using any specialized governance tools, pointing to an area ripe for improvement as data ecosystems become more complex.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Which data governance tools or practices do you use?"
          data-labels='["Not using any governance tooling", "Manual Cataloging", "Apache Atlas", "Collibra", "Alation"]'
          data-values='[64.6, 20.1, 6.3, 5.3, 4.2]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Most organizations don't use formal governance tools, with manual cataloging being the most common practice.</figcaption>
</figure>

The survey reveals a significant reliance on manual cataloging or a complete lack of governance tooling, highlighting an area where many organizations are lagging behind. Without automated governance frameworks, data quality, security, and compliance may be compromised, particularly as data ecosystems become complex. These gaps call for more robust and accessible solutions that can integrate seamlessly with existing workflows.

## Real-Time Data Processing

There is a split in the approach to real-time processing, with some teams investing in dedicated frameworks while many continue with batch processing.

* **Dedicated Frameworks:** 26.7% actively use specialized tools for real-time data processing.  
* **Minimal Real-Time Use:** An additional 28.1% engage in real-time processing on a limited basis.  
* **No Real-Time Processing:** 47% of respondents have not adopted any real-time strategies, suggesting that for many, batch processing remains adequate.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Do you work with real-time data processing?"
          data-labels='["No", "Yes, minimally", "Yes, using dedicated frameworks"]'
          data-values='[47, 28.1, 26.7]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Nearly half of organizations don't engage in real-time data processing.</figcaption>
</figure>

Approximately half of the respondents do not engage in real-time processing, suggesting that for many organizations, batch processing remains sufficient for their current needs. However, the considerable share using dedicated or minimal real-time frameworks indicates that a segment of the industry is investing in faster, near-real-time analytics, potentially a precursor to more widespread adoption as data velocity increases.

## Data Quality

Data quality practices are mixed. Organizations are shifting toward automation, yet manual oversight still predominates.

* **Manual Checks:** Rely on human oversight (48.8%).  
* **Automated Tests:** Used by 39.2%, showing a trend toward reducing manual intervention.  
* **Validation Tools:** Such as Great Expectations, employed by 22.6%.  
* **No Quality Practices:** Alarmingly, 26.7% do not implement any data quality measures, highlighting potential vulnerabilities.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="How do you ensure data quality in your workflows?"
          data-labels='["Manual Checks", "Automated Tests", "No practices", "Validation Tools"]'
          data-values='[48.8, 39.2, 26.7, 22.6]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Manual checks are the most common data quality practice, though automated approaches are gaining traction.</figcaption>
</figure>

The prevalence of manual checks suggests that many teams rely on human oversight for data quality, a practice that is both time-consuming and prone to error. Adopting automated tests and validation tools shows a positive shift toward streamlining these processes. However, the notable share of organizations with no data quality practices underscores a critical vulnerability that could lead to operational inefficiencies or misinformed decisions.

## Key Challenges

The survey identifies common hurdles that data engineering teams confront daily. The most significant challenge echoes through many facets of the data lifecycle.

* **Data Quality:** The top challenge at 68.8%, consistently affecting multiple stages of operations.  
* **Data Integration:** Cited by 59.6%, reflecting difficulties in consolidating diverse data sources.  
* **Scaling Pipelines:** A concern for 53.8% of respondents, emphasizing issues around growing data volumes.  
* **Security and Compliance:** Reported by 40.4%, underscoring the increasing importance of regulatory and security measures.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="What are the primary challenges you face in data engineering?"
          data-labels='["Data Quality", "Integration of Data Sources", "Scaling Pipelines", "Security and Compliance"]'
          data-values='[68.8, 59.6, 53.8, 40.4]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Data quality is the most cited challenge, followed by integration and scaling issues.</figcaption>
</figure>

The most cited challenge, data quality, resonates throughout nearly every stage of the data lifecycle. Integration issues and scaling challenges further illustrate that while many organizations have embraced digital transformation, they still contend with legacy systems and infrastructural constraints. Security and compliance, while secondary in this survey, remain critical given the increasing regulatory scrutiny and the high stakes of data breaches. These challenges underscore the need for more robust, integrated solutions to address technical and organizational hurdles.

## Team Sizes

The survey reveals that many data operations are driven by small teams or solo practitioners.

* **Small Teams (1–5 members):** The largest group, with 117 teams.  
* **Solo Practitioners:** 55 professionals operate independently.  
* **Larger Teams:** There are fewer teams with 6+ members, which may explain the conservative approach toward adopting more complex, automated systems.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="How many people are in your data engineering team(s)?"
          data-labels='["1-5 members", "Solo (0)", "6-10", "11-20", "21-50", "51+"]'
          data-values='[117, 55, 21, 19, 8, 12]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Most data engineering teams are small, with 1-5 members being the most common size.</figcaption>
</figure>

The data indicates that most teams are small, with many professionals operating in solo or very small groups. This size limitation likely contributes to a cautious approach toward adopting more complex infrastructures—such as automated observability stacks, advanced orchestration systems, or comprehensive lakehouse architectures. The lean nature of most teams stresses the importance of tools that are not only powerful but also easy to implement and maintain.

## Conclusion

The survey offers a clear perspective on where the industry stands today and highlights critical areas for potential improvement as organizations scale their data operations.

Key takeaways:

1. **Adoption of mature vs. emerging technologies:** Established tools like relational databases, Apache Airflow, and Pandas are widely used and form the backbone of many operations. Emerging trends include the movement toward lakehouses and automated data quality and governance practices, areas where adoption is still in progress.

2. **Resource constraints drive tool choices:** The prevalence of small teams and solo practitioners explains the reliance on tools that are both effective and straightforward to implement. In contrast, the limited use of observability and automated governance indicates potential growth areas as organizations scale.

3. **Fragmentation and opportunity:** While cloud-based solutions are almost universal, the fragmentation in tooling for orchestration, governance, and real-time processing suggests ample opportunities for more unified and automated frameworks.
