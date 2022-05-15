---
authors:
- angelicaloduca
description: An overview of what DevOps and MLOps have in common and what are their
  differences (if any).
image: images/posts/2022-05-15-devops-and-mlops-same-thing/cover.jpg
layout: post
subtitle: An overview of what DevOps and MLOps have in common and what are their differences
  (if any).
tags:
- mlops
- devops
- process
title: Are DevOps and MLOps the Same Thing?
---

<figure>
<img src="/images/posts/2022-05-15-devops-and-mlops-same-thing/image2.jpg"  />
<figcaption>Image from <a href="https://pixabay.com/it/photos/devops-attivit%c3%a0-commerciale-3155972/" target="_blank">Pixabay</a></figcaption>
</figure>


About ten years ago, the community realized that there was a barrier between the delivery and operations teams. On the one hand, there was the **development team, which was responsible for writing and testing the code**. On the other hand, **the operations team should make the code run in production**. Production literally means that the software is ready to be publicly used.

Moving software from development to production was a manual process that required a lot of time. To reduce this gap and save time while deploying software, a new culture began to spread: the DevOps culture, which aims to make people collaborate together.

**DevOps (Development and Operations) is a set of best practices that try to establish a collaboration between the development and operations teams, with the purpose of automatizing the software deployment process as much as possible.**

In the last ten years, much progress has been made in the DevOps sector, reaching a fairly high level of maturity. Many tools and platforms were born. To mention the most famous platforms, you can remember Docker and Kubernetes.

Recently, a new concept is spreading. It is MLOps, which means Machine Learning Operations. MLOps is a set of best practices that helps people to **deliver** and **maintain** Machine Learning models in production. The interesting aspect is that in MLOps you should not be able to only deliver Machine Learning models, but also maintain them.

At first, one might think that MLOps is just a new term for DevOps, with a special focus on Machine Learning. But in reality, the matter is not as trivial as it seems.

In this article, we try to give an answer to all those who are wondering if DevOps and MLOps are the same things or not.

The article is organized as follows:

-   The DevOps and MLOps workflow

-   DevOps and MLOps monitoring

-   The DevOps and MLOps teams

-   Maturity in DevOps and MLOps.

## The DevOps and MLOps workflow

The typical DevOps workflow includes three main steps:

-   building the software

-   testing the software

-   delivering the software.

The idea is to connect the third phase with the first one, to make the process as much as possible automatic. The classical DevOps workflow is represented through the symbol of infinity, as shown in the following figure:

<figure>
<img src="/images/posts/2022-05-15-devops-and-mlops-same-thing/image3.png"  />
<figcaption>Image from <a href="https://pixabay.com/it/illustrations/devops-attivit%c3%a0-commerciale-3148393/" target="_blank">Pixabay</a> with Pixabay license.</figcaption>
</figure>

The infinity symbol indicates that all the steps should be run endlessly.

The main artifact in a DevOps workflow is the software, usually provided in a container. The software is **static**, in the sense that it does not degrade over time. However, you could discover some bugs in the code, thus you should update it, following the DevOps workflow.

In an MLOps workflow, you do not have only the software as an artifact. **You also have the model and data.** Unfortunately, your data does not last forever, as well as the model. Your model may be subjected to degradation, both in terms of data drift and concept drift:

-   **Data drift** means that data used to train your model are not suitable to represent reality because they are too old. In other words, actual data and data used to train the model have different distributions.

-   **Concept drift** means that the relationship between the output variable and the input variable of your model is not valid anymore, thus there is a conceptual error in your model.

Both data drift and concept drift should generate **model retraining**.

This means that the MLOps workflow should also consider this aspect. The building step of the DevOps workflow should be extended to also include model training/model retraining.

The challenge of the MLOps workflow is that the final artifact, which includes the software, the model, and the data, is not static, but it changes (degrades) over time. So you should define a strategy to monitor it, and trigger the retraining process whenever it is needed.

The MLOps workflow should consider **model maintenance**, which includes the previously described steps. Thus, organizations should move from data-driven solutions to model-driven solutions.

## DevOps and MLOps monitoring

Monitoring in the space of DevOps is very important. But in MLOps is even more important, because it should be able to trigger a retrain action.

In DevOps monitoring, you should have logs, system metrics, and business-specific metrics. The most popular tools to monitor your DevOps workflow are [Prometheus](https://prometheus.io/docs/introduction/overview/){:_target="_blank"} and [Grafana](https://grafana.com/grafana/?plcmt=footer){:_target="_blank"}.

In MLOps you continue to monitor the classical metrics already defined for DevOps. But you should also monitor other metrics, including data and concept drift, model accuracy, adversarial attacks to your model, fairness detection, and so on. As a monitoring tool, you could continue to use Prometheus, but you should extend it with new components for the specific task.

As additional (or specific monitoring tools), you can use some experimentation platforms, which permit you to track, monitor, and compare your experiments, as well as choose the best model to send to production. Some of the most popular tools in this field include [Comet](https://comet.ml/){:_target="_blank"}, [MLflow](https://mlflow.org/){:_target="_blank"}, and [Neptune](https://neptune.ai/){:_target="_blank"}.

Monitoring DevOps and MLOps should help to identify abnormal situations that call to action. **In an ideal situation, all actions should be performed automatically.**

## The DevOps and MLOps teams

There are three different roles in DevOps:

-   the **production operator**, who makes the pipeline work

-   the **business manager**, who defines the requirements and the metrics, and

-   the **developer**, who implements the code.

They work together to solve the same problem, that is make the software work in production, by guaranteeing continuous integration and continuous delivery.

In MLOps, you have again three roles, but the developer is a more specific figure, named **Machine Learning Engineering**, who is responsible for building the model.

## Maturity in DevOps and MLOps

Maturity in both DevOps and MLOps measures the extent to which human intervention in software release and update processes has been replaced with total automation.

You can check at which level of DevOps and MLOps your organization is. DevOps does not define any specific levels of maturity. However, broadly, we can define the following levels of maturity in DevOps, as shown in the following figure:

<figure>
<img src="/images/posts/2022-05-15-devops-and-mlops-same-thing/image1.png"  />
<figcaption></figcaption>
</figure>

The levels are:

-   **Initial** — the Development and Operations teams are separated.

-   **Managed** — intent of collaboration between the two teams, but only in the Operations team, there is some kind of automation.

-   **Defined** — there is a collaboration between the two teams and some kind of automation.

-   **Measured** — there is a better understanding of the process and automation.

-   **Optimized** — the gap between the two teams disappears.

In MLOps, both Google and Microsoft have defined some levels of maturity:

-   3 levels of maturity from Google

-   5 levels from Microsoft

The two models are quite similar. In this article, we describe the Google’s ones, as shown in the following figure:

<figure>
<img src="/images/posts/2022-05-15-devops-and-mlops-same-thing/image4.png"  />
<figcaption></figcaption>
</figure>

The levels are:

-   **level 0** — you don’t have MLOps, you have a manual process, for deploying and monitoring a model. For instance, you write your code in Jupyter notebooks.

-   **level 1** — you start introducing some automation. You introduce a **pipeline**. You have components that are validating the data you are expecting. You have the evaluation module, that controls the criteria you have set. Teams work together. Machine Learning engineers maintain the training job. Jupyter notebooks are moved to scripts. You produce metrics, you have **buttons to trigger retraining**.

-   **level 2** —the retraining process is automatic. You do not monitor only system metrics, but also quality metrics. To detect if the model is degrading, you should have **triggers** that trigger the execution of the pipeline.

This triggering problem is still under discussion. There are two possible ways to trigger an event:

-   **on a periodic basis** — this is the case of a scheduler, which periodically checks if something changes, and if so, it triggers a specific event.

-   **when data changes** — there is not any scheduler. This aspect is still under investigation and remains an open challenge for the next years.

## Conclusion

DevOps and MLOps share many things in common, but they also have many differences.

**So to the question: DevOps and MLOps are the same, we can answer: No, they are not the same, although they share the same principles of collaboration between development and operations teams.**

Both in DevOps and in MLOps the mentality is the same and is based on the principle of automating all processes as much as possible, in order to move **from people to technology**.

This text was freely inspired by the interview with Theofilos Papapanagiotou and Alexey Grigorev, entitled The Rise of MLOps, and available in the [DataTalks.Club](https://datatalks.club/podcast/s02e04-mlops.html){:_target="_blank"} website as a podcast.

If you have read this far, maybe you’d be interested to know that DataTalks.Club is running a free course about MLOps. You can find out more about it [here](https://github.com/DataTalksClub/mlops-zoomcamp){:_target="_blank"}!