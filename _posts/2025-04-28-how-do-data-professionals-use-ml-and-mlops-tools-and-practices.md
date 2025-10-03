---
authors:
- valeriiakuka
description: Discover how 200+ data professionals deploy, monitor, and manage ML models in production. Survey insights on MLOps tools, deployment practices, model versioning, CI/CD workflows, and team structures in 2024.
image: images/posts/2025-04-28-how-do-data-professionals-use-ml-and-mlops-tools-and-practices/cover.jpg
layout: post
subtitle: Results of our DataTalks.Club Survey
tags:
- survey
- ai
- '2024'
title: How Do Data Professionals Use MLOps Tools and Frameworks?
charts: true
---

We [surveyed](https://docs.google.com/forms/d/e/1FAIpQLScdx1FAIp2GDGgiMf7xu-I1PfhsQBJDvFstGmWmWbpP4S69Zg/viewform){:target="_blank"} over 200 data professionals to understand the tools they use for deploying, monitoring, versioning, and managing machine learning workflows.

In this article, we highlight key trends, from model deployment and monitoring to CI/CD practices and team structures, revealing how organizations are operationalizing their ML models in production.

Let's explore the data.

## Model Deployment Tools

Deployment practices vary widely.

A substantial portion (nearly 40%) does not deploy models. Among those who do, Kubernetes, SageMaker, and Azure ML are the top tools.

* **Kubernetes** is used by 27.1% of respondents.  
* **AWS SageMaker** and **Google AI Platform** appear frequently (27.1% and 21.6%, respectively), while **Azure Machine Learning** is used by 18.3%.  
* **TensorFlow Serving** is deployed by 9.6% of teams.  
* Notably, 38.5% of respondents indicated that they do not deploy models at all.

Some respondents mentioned alternatives (e.g., TorchServe, OpenVino, MLFlow Serving, and homegrown solutions), suggesting a diverse ecosystem with no single solution dominating all use cases.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Model Deployment Tools Usage"
          data-labels='["We don’t deploy models", "Kubernetes", "AWS SageMaker", "Azure Machine Learning", "Google AI Platform", "TensorFlow Serving", "TorchServe", "Others"]'
          data-values='[38.8, 26.9, 21.5, 18.3, 11.9, 9.6, 1.8, 0.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of model deployment tools usage among data professionals.</figcaption>
</figure>

## Monitoring ML Models in Production

Monitoring practices are still in the early stages. A majority (57.9%) reported that they do not monitor models in production. Open-source and general-purpose monitoring tools (Grafana, ELK) are more common than specialized ML tools.

Among specific tools:

* **Prometheus and Grafana** are the most common monitoring tools (20.8%).  
* Other solutions include the **ELK Stack** (9.1%), **Evidently AI** (5.6%), and custom monitoring scripts (11.2%).

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="ML Model Monitoring Tools Usage"
          data-labels='["We don’t monitor models", "Prometheus & Grafana", "Custom scripts", "ELK Stack", "Evidently AI", "Arize AI", "WhyLabs", "Others"]'
          data-values='[58.1, 20.7, 11.1, 9.1, 5.6, 2.5, 2.0, 0.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of ML model monitoring tools usage.</figcaption>
</figure>

## CI/CD for ML Workflows

CI/CD adoption for ML shows mixed usage. Almost half of respondents don't use CI/CD for ML. Among those who do, GitLab CI/CD and MLflow are leading choices. Traditional DevOps tools dominate over ML-native pipelines.

**GitLab CI/CD** leads with 26.6%, followed by **Jenkins** (14.5%).

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="CI/CD Tools Usage for ML Workflows"
          data-labels='["We don’t use CI/CD tools", "GitLab CI/CD", "Jenkins", "CircleCI", "Argo Workflows", "Others"]'
          data-values='[44.2, 27.0, 20.5, 14.4, 6.5, 2.8, 1.3]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of CI/CD tools usage for ML workflows.</figcaption>
</figure>

## Model Versioning

A significant 58.1% of respondents do not use any model versioning tools.

Among those who do:

* **MLflow** is the most popular tool for versioning models (32.3%).  
* **DVC (Data Version Control)** and **Weights & Biases (W&B)** are used by 10.6% and 11.1% of respondents, respectively.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Model Versioning Tools Usage"
          data-labels='["We don’t use versioning tools", "MLflow", "Weights & Biases", "DVC", "Others"]'
          data-values='[58.3, 32.2, 11.1, 10.6, 0.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of model versioning tools usage.</figcaption>
</figure>

## Data Versioning Tools

Notably, 75.8% of respondents don't use data versioning tools. DVC leads among those that do. There's a notable tooling gap in reproducible data pipelines.

Among those who do:

* **DVC** is used by 16.5% of participants.  
* Other tools such as **Quilt**, **LakeFS**, and **Pachyderm** see minimal adoption.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Data Versioning Tools Usage"
          data-labels='["We don’t use data versioning tools", "DVC", "LakeFS", "Quilt", "Pachyderm", "Others"]'
          data-values='[75.9, 16.4, 3.6, 2.6, 2.1, 1.4]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of data versioning tools usage.</figcaption>
</figure>

## Feature Store Adoption

Feature stores are not widely adopted. A dominant 74.9% reported not using any feature store, indicating that many teams rely on custom or ad hoc solutions for feature management.

Only a minority use dedicated feature stores like **AWS SageMaker Feature Store** (12.3%), **Databricks Feature Store** (10.8%), or **Vertex AI Feature Store** (7.7%).

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Feature Store Usage"
          data-labels='["We don’t use feature stores", "AWS SageMaker Feature Store", "Databricks Feature Store", "Vertex AI Feature Store", "Hopsworks", "Feast", "Custom solutions"]'
          data-values='[75.0, 12.2, 10.7, 7.7, 3.1, 2.0, 2.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of feature store usage among data professionals.</figcaption>
</figure>

## Model Training and Experimentation Tools

More than half (55.2%) of respondents do not use dedicated experimentation tools, suggesting that many teams might leverage native frameworks or simple scripts.

Among those who do:

* **MLflow** leads again with 34.3% adoption.  
* **Weights & Biases (W&B)** is used by 13.4%, while **TensorBoard** and **Neptune.ai** have lower adoption (10% and 3.5%, respectively).

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Model Training and Experimentation Tools Usage"
          data-labels='["We don’t use dedicated tools", "MLflow", "Weights & Biases", "TensorBoard", "Neptune.ai", "Others"]'
          data-values='[55.4, 34.2, 13.4, 9.9, 3.5, 3.6]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of model training and experimentation tools usage.</figcaption>
</figure>

## Workflow Orchestration for ML Pipelines

Orchestrating ML pipelines is not yet widespread. Over half (53.6%) of respondents do not employ any workflow orchestration tools, which may impact scalability and automation.

Among those who do:

* **Apache Airflow** is the most used orchestration tool (34%).  
* Other tools such as **Prefect** (6.2%), **Kubeflow** (7.2%), and **AWS Step Functions** (7.7%) are also noted. 

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Workflow Orchestration Tools Usage"
          data-labels='["We don’t use orchestration tools", "Apache Airflow", "AWS Step Functions", "Kubeflow", "Prefect", "Others"]'
          data-values='[53.8, 33.8, 7.7, 7.2, 6.2, 7.3]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of workflow orchestration tools usage.</figcaption>
</figure>

## Model Retraining Frequency

Retraining remains reactive or infrequent for most teams.

* A substantial 43.9% do not retrain their models once deployed.  
* Among those that do, 28.6% retrain models as needed based on performance degradation, and 23% retrain periodically.  
* Only a very small percentage (around 3.1%) use continuous online learning.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Model Retraining Frequency"
          data-labels='["We don’t retrain models", "As needed", "Periodically", "Continuously (online learning)"]'
          data-values='[43.7, 28.9, 22.8, 3.0]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Distribution of model retraining frequency among data professionals.</figcaption>
</figure>

## Infrastructure for ML Workloads

Regarding where ML workloads run, the results show a mix of diverse deployment environments, with many organizations leveraging cloud scalability.

* **Cloud platforms** dominate with AWS (39.9%), Azure (28.7%), and GCP (20.8%).  
* **On-premise infrastructures** are used by 21.3% of respondents, while 11.2% report a hybrid approach.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="ML Infrastructure Usage"
          data-labels='["Cloud (AWS)", "Cloud (Azure)", "On-premise", "Cloud (GCP)", "Hybrid", "Others"]'
          data-values='[39.7, 28.5, 21.8, 20.7, 11.2, 2.1]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Distribution of ML infrastructure usage among organizations.</figcaption>
</figure>

## Team Structure and Centralization

Most teams are small or solo. This aligns with the widespread absence of orchestration, monitoring, and versioning practices.

Only 18.8% reported having a centralized MLOps team, while the vast majority (81.2%) do not, indicating that ML operations are often managed in a more distributed manner.

* The largest segment (45.6%) have small ML teams of 1–5 members.  
* About 34.8% report teams of 6–10 members.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="ML Team Size Distribution"
          data-labels='["1-5 members", "Solo (0)", "6-10 members", "11-20 members", "21-50 members", "51+ members"]'
          data-values='[45.4, 35.1, 9.3, 6.3, 1.5, 2.4]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Distribution of ML team sizes across organizations.</figcaption>
</figure>

## Production ML Models

While the survey captured data on the number of models in production, many respondents reported having few or no models deployed. This suggests that many organizations are still in early stages of scaling ML operations.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Number of ML Models in Production"
          data-labels='["0 models", "1 model", "2-5 models", "5+ models"]'
          data-values='[45.5, 20.6, 21.5, 12.4]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Distribution of the number of ML models in production across organizations.</figcaption>
</figure>

## Conclusion

The survey reveals a diverse and evolving ML and MLOps landscape.

Key takeaways include:

* **Deployment:** Many tools are in use, from Kubernetes to cloud-native platforms, but many teams have not yet deployed models.  
* **Monitoring:** Over half of respondents do not monitor their models, underscoring an opportunity for improved observability.  
* **Versioning & Experimentation:** Although tools like MLflow and DVC are gaining traction, many teams are not using dedicated versioning solutions.  
* **Infrastructure & Retraining:** Cloud platforms are widely used, and most models are not retrained frequently.  
* **Challenges:** Data quality, deployment, monitoring, and integration remain critical pain points.

Overall, while many teams are adopting modern tools for ML workflows, there remains ample opportunity for standardizing practices and addressing operational challenges as organizations mature their ML initiatives.
