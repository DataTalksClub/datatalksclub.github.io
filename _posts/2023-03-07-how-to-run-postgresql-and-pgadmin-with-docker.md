---
authors:
- luisoliveira
description: And an alternative with Docker Compose
image: images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/cover.jpg
layout: post
subtitle: And an alternative with Docker Compose
tags:
- postgres
- docker
- data-engineering
title: How to run PostgreSQL and PgAdmin with Docker
---

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image6.png"  />
<figcaption>PgAdmin GUI welcome page (picture by author)</figcaption>
</figure>


As you saw in one of the previous articles I set [PostgreSQL to run in a Docker container](https://medium.com/dev-genius/learn-how-to-run-postgresql-locally-c388483712e9){:target="_blank"}. However, to manage and query databases in the [PostgreSQL](https://www.postgresql.org/){:target="_blank"} server I had to use other software like DBeaver or DataGrip.

What if I set a database management tool running in a Docker container too? Then we don’t need to install anything less but Docker 😁

This article is made under the [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp){:target="_blank"} by [Data Talks Club](https://datatalks.club/){:target="_blank"} and will show up some code related to these videos:

-   [Connecting Postgres and pgAdmin](https://www.youtube.com/watch?v=hCAIVe9N0ow&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb){:target="_blank"};
-   [Running Postgres and pgAdmin with Docker-Compose.](https://www.youtube.com/watch?v=hKI6PkPhpa0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb){:target="_blank"}

In this article I will present:

-   A brief introduction to Docker, PostgreSQL, and pgAdmin;
-   What do you have to do to run PostgreSQL and pgAdmin in two Docker containers;
-   What do you have to do to run PostgreSQL and pgAdmin with Docker compose.



## 1. A brief introduction to Docker, PostgreSQL, and pgAdmin

### 1.1 Docker

[Docker](https://www.docker.com/){:target="_blank"} uses OS-level virtualization to allow fantastic customization of software in containers that can be easily shared with your colleagues or between development environments, “and be sure that everyone you share with gets the same container that works in the same way” (from the Official Docker website).

Containers are isolated from one another and bundle their own software, libraries, and configuration files.

Because all of the containers share the services of a single operating system kernel, they use fewer resources than virtual machines.” (Source [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software){:target="_blank"}))

### 1.2 PostgreSQL

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image1.png"  />
<figcaption><p>Official PostgreSQL logo</p></figcaption>
</figure>

According to the [official website](https://www.postgresql.org/){:target="_blank"} “PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.”.

“It was originally named POSTGRES but in 1996, the project was renamed to PostgreSQL to reflect its support for SQL.

It features transactions with Atomicity, Consistency, Isolation, Durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures.

It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users.” (Source [Wikipedia](https://en.wikipedia.org/wiki/PostgreSQL){:target="_blank"})

### 1.3 PgAdmin

[PgAdmin](https://www.pgadmin.org/){:target="_blank"} is a free and open-source graphical user interface (GUI) tool for managing and developing databases. It is specifically designed for PostgreSQL, a powerful and popular open-source database management system.

PgAdmin provides users with an intuitive interface for creating and maintaining database objects, as well as a powerful SQL editor for writing and executing SQL queries and scripts. It is commonly used by database administrators and developers to manage and develop PostgreSQL databases.

Some features of pgAdmin for PostgreSQL include:

-   Graphical user interface for managing and interacting with databases;
-   Support for multiple PostgreSQL versions and operating systems;
-   Connection management, allowing users to connect to and switch between databases easily;
-   Query tool for executing SQL statements;
-   Object browser for managing database objects such as tables, views, and functions;
-   Table data editor for modifying table data directly;
-   Import/export capabilities for transferring data between databases;
-   Job scheduling and management for automating tasks;
-   Debugging tools for troubleshooting queries and functions.



## 2. Running PostgreSQL and pgAdmin in two Docker containers

In my previous article, I set the PostgreSQL server to run with two commands.

First, we needed to set a volume to persist the data of the server:

```bash
docker volume create --name postgres_volume_local -d local
```

Then we needed to run a Docker command:

```bash
docker run -it \\
  --rm --name postgresql \\
  -e POSTGRES_USER="root" \\
  -e POSTGRES_PASSWORD="root" \\
  -e POSTGRES_DB="ny_taxi" \\
  -v postgres_volume_local:/var/lib/postgresql/data \\
  -p 5432:5432 \\
  postgres:13
```

After running this command a PostgreSQL server starts to run with all the needed variables. For more details about each line of the full command please check the previous article.

However, now we are going to run two Docker containers and, therefore, we need to set a connection between both (remember that containers are isolated?). And the previous command to run PostgreSQL is incomplete.

To create a network in Docker you have to run the following command:

docker network create pg-network

Now we are going to adapt the previous command to run **PostgreSQL in a Docker container that can be connected to another container by adding the network and setting a name to the container**:

```bash
docker run -it --rm \\
  -e POSTGRES_USER="root" \\
  -e POSTGRES_PASSWORD="root" \\
  -e POSTGRES_DB="ny_taxi" \\
  -v postgres_volume_local:/var/lib/postgresql/data \\
  -p 5432:5432 \\
  --network=pg-network \\
  --name pg-database \\
  postgres:13
```

So now we have the server PostgreSQL in a Docker container with the name “pg-database” and a network that allows connection with other Docker containers.

Now we need to run pgAdmin in a Docker container by setting a full command calling the image “dpage/pgadmin4” with the following information:

-   Environment variables: User/Email and Password
-   Port: 8080
-   Network: the same network that you set for PostgreSQL
-   Name for the container

```bash
docker run -it --rm \\
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \\
  -e PGADMIN_DEFAULT_PASSWORD="root" \\
  -p 8080:80 \\
  --network=pg-network \\
  --name pgadmin \\
  dpage/pgadmin4
```

With the command above we started a docker container for running pgAdmin.

To see it running you have to go to your browser and call the localhost:8080 and you will be asked for the user and password similar to the picture below.

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image4.png"  />
<figcaption><p>After writing the user as “admin@admin.com” and the password “root” you will enter the main page of pgAdmin like presented at the beginning of the article.</p></figcaption>
</figure>

To connect to PostgreSQL you have to click on “Add a New Server” which will pop up a new window.

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image5.png"  />
<figcaption><p>In the “General” part you can call your server whatever you want. I called mine “postgresql”. 😂</p></figcaption>
</figure>

Then in “Connection” tab you have to fulfill the following information:

-   Host Name: **pg-database**
-   Port: **5432**
-   Maintenance database: **ny_taxi** (this is the name of the database you used to create the PostgreSQL server in a docker container)
-   Username: **root** (this is the user you used to create the PostgreSQL server in a docker container)
-   Password: **root** (this is the password you used to create the PostgreSQL server in a docker container)



AND… VOILÁ 🎉🎉

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image2.png"  />
<figcaption><p>Now you have a database administrator tool running in Docker connected to PostgreSQL server also running on a Docker container.</p></figcaption>
</figure>

## 3. How to run PostgreSQL and pgAdmin with docker-compose

However, we can run both containers already connected with docker-compose.

**“Docker Compose** is a tool for defining and running multi-container Docker applications. It uses YAML files to configure the application’s services and performs the creation and start-up process of all the containers with a single command (…) The **docker-compose.yml** file is used to define an application’s services and includes various configuration options.” (text extracted from [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software){:target="_blank"})*).*

Then we need to write in our docker-compose.yml file:

**The information for the PostgreSQL server:**

```yaml
services:
 pgdatabase:
   image: postgres:13
   environment:
     - POSTGRES_USER=root
     - POSTGRES_PASSWORD=root
     - POSTGRES_DB=ny_taxi
   volumes:
     - postgres_volume_local:/var/lib/postgresql/data:rw"
   ports:
     - "5432:5432"
```

**The information for the pgAdmin part:**

```yaml
 pgadmin:
   image: dpage/pgadmin4
   environment:
     - PGADMIN_DEFAULT_EMAIL=admin@admin.com
     - PGADMIN_DEFAULT_PASSWORD=root
   ports:
     - "8080:80"
```


**And a code informing that our volume is external:**

```yaml
  volumes:
  postgres_volume_local:
    external: true
```


**The full docker-compose Yaml file is as follows:**

```yaml
services:
 pgdatabase:
   image: postgres:13
   environment:
     - POSTGRES_USER=user_name
     - POSTGRES_PASSWORD=a_cool_but_difficult_password
     - POSTGRES_DB=my_database
   volumes:
     - postgres_volume_local:/var/lib/postgresql/data:rw"
   ports:
     - "5432:5432"
 pgadmin:
   image: dpage/pgadmin4
   environment:
     - PGADMIN_DEFAULT_EMAIL=admin@admin.com
     - PGADMIN_DEFAULT_PASSWORD=root
   ports:
     - "8080:80"
volumes:
 postgres_volume_local:
   external: true
```

Now we can call the command to start docker-compose

```bash
docker compose up
```

Now when starting a server in pgAdmin remember that our server is called “pgdatabase” like the image below.

<figure>
<img src="/images/posts/2023-03-07-how-to-run-postgresql-and-pgadmin-with-docker/image3.png"  />
<figcaption><h1>Summary</h1></figcaption>
</figure>

This article, it was presented a tutorial on how to run PostgreSQL and pgAdmin in docker containers.

Using PostgreSQL and pgAdmin inside docker containers can provide a simple and convenient way to set up and manage your database environment. By utilizing containerization technology, you can easily deploy your database environment on different machines with minimal configuration.

With this tutorial, you can practice your SQL skills without any extra installation.

Did you like this article? Follow me for more articles on [Medium](https://medium.com/@lgsoliveira){:target="_blank"}.