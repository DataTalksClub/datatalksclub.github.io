---
authors:
- luisoliveira
description: With Docker and Docker Compose
image: images/posts/2022-09-17-how-to-setup-lightweight-local-version-for-airflow/cover.jpg
layout: post
subtitle: With Docker and Docker Compose
tags:
- airflow
- docker
- data-engineering
title: How to Setup a Lightweight Local Version for Airflow
datepublished: '2022-09-17'
date: '2022-09-17'
---

<figure>
<img src="/images/posts/2022-09-17-how-to-setup-lightweight-local-version-for-airflow/image2.png"  />
<figcaption><p>Forget about the “Low Memory” issues when running Airflow (logos are taken from <a href="https://airflow.apache.org/"><u>Apache Airflow</u></a> and <a href="https://www.docker.com/"><u>Docker</u></a>)</p></figcaption>
</figure>

This article was created under the scope of the first edition of the [Data Engineer Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp){:target="_blank"} by [DataTalksClub](https://datatalks.club/){:target="_blank"}. I will present a technical variation I made to the initially proposed development to run **Apache Airflow** locally (see [*What means “to run one software locally”*](https://medium.com/@lgsoliveira/what-means-to-run-one-software-locally-a8b556d6f34c){:target="_blank"}) with **Docker** and **Docker Compose**. This adaptation was later incorporated into the DE Zoomcamp as seen in this [video](https://www.youtube.com/watch?v=A1p5LQ0zzaQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=23){:target="_blank"}.

What we’ll cover in this article:

-   What are Apache Airflow and Docker
-   How to setup the lightweight Docker version to run Airflow
-   Reasons why this setup is lighter

This is not a tutorial about Airflow or Docker but an explanation on how to set up a less demanding version of Docker environment to run Airflow locally.

The “full” proposed version to run Airflow inside a Docker container is highly resource-intensive, and hence pushes a lot of one computer/laptop (the cooling fan of my laptop was always ON). For more information about the full version, I advise you to see the Data Engineering Zoomcamp mentioned above and this [article](https://www.linkedin.com/pulse/airflow-o-que-%C3%A9-o-faz-hands-on-leandro-bueno/){:target="_blank"} (in Portuguese) by Leandro Bueno.

## 1. Introduction to Airflow and Docker

### 1.1 Apache Airflow

**Apache Airflow** is one of the most known tools in the data engineering world therefore I will not take long to explain it.

This software is an open-source data orchestrator tool allowing to build full end-to-end pipelines by connecting several processes in **Directed Acyclic Graphs** (**DAG**s). It connects and organizes tasks that manage data, and is not a data streaming tool as mentioned on the official [Airflow website](https://airflow.apache.org/docs/apache-airflow/stable/#){:target="_blank"}: “*Airflow is not a data streaming solution. Tasks do not move data from one to the other (though tasks can exchange metadata!)”.*

<figure>
<img src="/images/posts/2022-09-17-how-to-setup-lightweight-local-version-for-airflow/image1.png"  />
<figcaption><p>The official logo for Apache Airflow</p></figcaption>
</figure>

[Airbnb](http://airbnb.com){:target="_blank"} developed Airflow in 2014, it was made available as a free tool in 2015, and it was donated to the [Apache Foundation](https://www.apache.org/){:target="_blank"} in the following year.

In addition to being open-source, Airflow has the following main advantages:

-   It is more maintainable, versionable, testable, and collaborative because it was all developed in code, according to the official Airflow website;
-   Python, a well-known programming language, is used throughout;
-   It has several built-in operators, but you can write your own custom operator if they don’t fulfill your requirements;
-   Even being all develop with code it has a fantastic web interface allowing the correct understatement of the flow;
-   It is highly scalable.

### 1.2. Docker and Docker Compose

One year ago I started working on **Docker**, a fantastic set of Platform As A Software (PAAS) products, and I'm now a huge fan.

This tool uses OS-level virtualization that allows fantastic customization of software in containers that can be easily shared with your colleagues or between development environments, “*and be sure that everyone you share with gets the same container that works in the same way”* (by the [Official Docker website](https://docs.docker.com/get-started/overview/#:~:text=Docker%20provides%20the%20ability%20to,simultaneously%20on%20a%20given%20host.){:target="_blank"}).

The way Docker works is very simple because it uses a client-server architecture. “*The Docker client talks to the **Docker daemon**, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another Docker client is Docker Compose, which lets you work with applications consisting of a set of containers.”* (text extracted from the Official Docker Website).

<figure>
<img src="/images/posts/2022-09-17-how-to-setup-lightweight-local-version-for-airflow/image3.png"  />
<figcaption><p>Docker architecture (from the <a href="https://docs.docker.com/get-started/overview/#:~:text=Docker%20provides%20the%20ability%20to,simultaneously%20on%20a%20given%20host."><u>Official Docker website</u></a>)</p></figcaption>
</figure>

The most common way of using Docker is by setting several instructions in a text file called **Dockerfile**. This file first “calls” an image from the public Docker repository (e.g., Python Image, Airflow Image, etc) setting the Base Image, and then it will run several user-defined commands to customize your new image. Then after running the “docker build” command a new image is created and the entire context (recursively) is sent to the daemon.

***“Docker Compose** is a tool for defining and running multi-container Docker applications. It uses YAML files to configure the application's services and performs the creation and start-up process of all the containers with a single command (...) The **docker-compose.yml** file is used to define an application's services and includes various configuration options.”* (text extracted from [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software){:target="_blank"})*).*

## 2. Setup and run Airflow locally with a less demanding Docker-compose version (with bonus information)

The setup I am presenting in this section was built and set to run successfully under the scope of my final Capstone of the Zoomcamp mentioned above. You can see my full capstone [here](https://github.com/guoliveira/data-engineer-zoomcamp-project){:target="_blank"}.

I divided this part of the article into two:

1.  The main design to enable Airflow to run in Docker containers and
2.  The adaptation I created to allow a less demanding configuration.

### 2.1. Structure to allow Airflow to run in Docker

In order to run Airflow locally (in a Docker container), I used an extended image, containing some additional dependencies.

Therefore I firstly created a Dockerfile pointing to the Airflow version I needed, such as apache/airflow:2.2.3, as the base image.

```docker
FROM apache/airflow:2.2.3
```

Then I customized this Dockerfile by adding some custom packages to be installed. The one I was going to need the most was *gcloud* to connect with the GCS bucket/Data Lake and integrate “requirements.txt” to install libraries via pip install.

And here is the bonus I promised: I decided to run Spark (using Pyspark) in my DAG so I had to configure Spark in the Dockerfile. This was possible by adding bash commands to set Java env and inserting commands to download all the necessary files to run Spark. Besides, it was necessary to insert Pyspark as a requirement.

```docker
ENV JAVA_HOME=/home/jdk-11.0.2

ENV PATH="${JAVA_HOME}/bin/:${PATH}"

RUN DOWNLOAD_URL="https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz" \
    && TMP_DIR="$(mktemp -d)" \
    && curl -fL "${DOWNLOAD_URL}" --output "${TMP_DIR}/openjdk-11.0.2_linux-x64_bin.tar.gz" \
    && mkdir -p "${JAVA_HOME}" \
    && tar xzf "${TMP_DIR}/openjdk-11.0.2_linux-x64_bin.tar.gz" -C "${JAVA_HOME}" --strip-components=1 \
    && rm -rf "${TMP_DIR}" \
    && java --version
```

Then I ran curl to import the official docker-compose setup file (docker-compose.yml) from the latest Airflow version into my laptop.

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
```

Then I adapted the Yaml file for running docker-compose:

-   In x-airflow-common, a) I removed the image tag, to replace by my Dockerfile, b) mounted my google_credentials in volumes section as read-only and c) set environment variables `GOOGLE_APPLICATION_CREDENTIALS` and `AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT`;

-   And I changed `AIRFLOW__CORE__LOAD_EXAMPLES` to `false`;

With all the steps mentioned before I was ready to run the full version to run Airflow locally with Docker.

### 2.2. Modification to allow a lightweight version

To achieve my objective of having a lightweight version I had to remove several parts of the docker-compose.yml file. All these processes were removed for a solid reason as I will explain in the next section.

1.  I firstly removed the *redis* part:

```yaml
redis:
  image: redis:latest
  expose:
    - 6379
  healthcheck:
    test: ["CMD", "redis-cli", "ping"]
    interval: 5s
    timeout: 30s
    retries: 50
  restart: always
```

2.  It was to remove the *airflow-worke*r service. A controversial approach since we are talking about workers but in the next section you will understand this:

```yaml
airflow-worker:
  <<: *airflow-common
  command: celery worker
  healthcheck:
    test:
      - "CMD-SHELL"
      - 'celery --app airflow.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}"'
    interval: 10s
    timeout: 10s
    retries: 5
  environment:
    <<: *airflow-common-env
    # Required to handle warm shutdown of the celery workers properly
    # See https://airflow.apache.org/docs/docker-stack/entrypoint.html#signal-propagation
    DUMB_INIT_SETSID: "0"
  restart: always
  depends_on:
    <<: *airflow-common-depends-on
    airflow-init:
      condition: service_completed_successfully
```

3.  Then I removed the section for *airflow-triggerer*:

```yaml
airflow-triggerer:
  <<: *airflow-common
  command: triggerer
  healthcheck:
    test: ["CMD-SHELL", 'airflow jobs check --job-type TriggererJob --hostname "$${HOSTNAME}"']
    interval: 10s
    timeout: 10s
    retries: 5
  restart: always
  depends_on:
    <<: *airflow-common-depends-on
    airflow-init:
      condition: service_completed_successfully
```

4.  And finally, the *flower* section was removed:

```yaml
flower:
  <<: *airflow-common
  command: celery flower
  ports:
    - 5555:5555
  healthcheck:
    test: ["CMD", "curl", "--fail", "http://localhost:5555/"]
    interval: 10s
    timeout: 10s
    retries: 5
  restart: always
  depends_on:
    <<: *airflow-common-depends-on
    airflow-init:
      condition: service_completed_successfully
```

With those parts removed some dependencies need to be corrected:

```yaml
user: "${AIRFLOW_UID:-50000}:0"
  depends_on:
    &airflow-common-depends-on
    redis:
      condition: service_healthy
    postgres:
      condition: service_healthy
```

And ultimately I set the Executor from CoreExecutor to LocalExecutor. In the next section, I’ll explain why we changed the Executor and why this is the **most important part**.

`AIRFLOW__CORE__EXECUTOR`: CeleryExecutor LocalExecutor

The original and official version of the docker-compose.yml is [this](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml){:target="_blank"} and my final version is presented [here](https://github.com/guoliveira/data-engineer-zoomcamp-project/blob/main/Airflow/docker-compose.yaml){:target="_blank"}.

## 3. Why this setup is lighter

The main reason this setup is lighter than the full version is due to the choice of setting the core executor as **LocalExecutor** (single-node). Then, in a relationship of correlation, some features that were dependent on **CeleryExecutor** (multi-node) could be removed.

In Airflow a DAG will be executed and completed due to three main components, a) the **Metadata** **Database**, b) the **Scheduler** and c) the **Executor**(from the [Astronomer.io](https://www.astronomer.io/guides/airflow-executors-explained/){:target="_blank"} website)

The function of the Executor is to work together with the Scheduler to understand what resources will actually complete those tasks as they’re queued.

A CeleryExecutor (related to the [Celery](https://docs.celeryq.dev/en/stable/){:target="_blank"} distributed system) is specially made for horizontal scaling because CeleryExecutor works with a “pool” of independent workers (in a reliable distributed system) across which it can delegate tasks, via messages (according to the [Astronomer.io](https://www.astronomer.io/guides/airflow-executors-explained/){:target="_blank"} website). However, this Executor is highly resource-intensive. The LocalExecutor exemplifies single-node architecture (hence its resource light) but it still allows parallelism.

Therefore it is recommended to use LocalExecutor for local tests (run locally) and CeleryExecutor for production.

Since I set the Executor to LocalExecutor I could remove the parts *airflow-worke*r and *flower* because they only work for Celery architecture.

*Redis* is a simple caching server (see [Redis.io](https://redis.io/){:target="_blank"}) and it is necessary to setup as a Celery backend (see [CeleryExecutor](https://airflow.apache.org/docs/apache-airflow/1.10.13/executor/celery.html#:~:text=For%20this%20to%20work%2C%20you%20need%20to%20setup%20a%20Celery%20backend%20(RabbitMQ%2C%20Redis%2C%20%E2%80%A6){:target="_blank"})) for the CeleryExecutor. Since we will not use this Executor it is safe to remove this service-

I decided to remove the *airflow-trigger* because it is a new airflow service specially made for asyncio event loop, that I was not going to use.

## Conclusion

Now I can run Airflow locally without damaging my laptop too much or worrying about the integrity of my cooling face (it doesn't feel like I'm operating an airplane 😉) because we are running it with a single-node executor (but still having parallelism) and having fewer processes running.

I would like to have your feedback on the information in this article.

Do you think I was clear or unclear on the technical point of view?

Did I write anything technically wrong?

Did you like this article? Follow me for more articles on [Medium](https://medium.com/@lgsoliveira){:target="_blank"}.