---
authors:
- ruimachado
- helderrussa
cover: images/books/20231106-analytics-engineering-with-sql-and-dbt/cover.jpg
description: Book of the Week. Analytics Engineering with SQL and DBT by Rui Machado
  and Hélder Russa
end: 2023-11-10 23:59:59
image: images/books/20231106-analytics-engineering-with-sql-and-dbt/preview.jpg
links:
- link: https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/
  text: Book's page
- link: https://www.amazon.com/Analytics-Engineering-SQL-dbt-Meaningful/dp/1098142381
  text: Buy on Amazon
start: 2023-11-06 00:00:00
title: Analytics Engineering with SQL and DBT

archive:
- name: Shalltear
  text: '1. Is there any tool comparable to dbt?

    2. Have you tested dbt vault? If yes, how does it support?

    3. Some database are supported by dbt labs, some by other companies and some by
    the community. Can you recommend dbt to all databases or would you say, that on
    some one should prevent using dbt?

    4. Can you say anything regarding dbt certificates, in particular how complex
    they are?

    5. Since version 1.3, dbt supports python next to sql. Do you have some examples
    where this is really useful?'
  replies:
  - name: "H\xE9lder Russa"
    text: "Hello Shalltear, thank you very much for all theses questions. So starting\
      \ from the begging:\n1. Yes there are tools comparable with dbt, one that I\
      \ mentioned earlier is [https://www.matillion.com](https://www.matillion.com).\
      \ For sure each tool have their own specificities, but others like Mode Analytics,\
      \ or even Ibis (also discussed earlier) could in a sense be use as an alternative\
      \ of dbt - at least in some features;\n2. Never tested AutomateDV (formerly\
      \ dbt vault), but definitely it is supported by dbt. In high level, if you think\
      \ about data vault with links, satellites and hubs, your models would be built\
      \ under this paradigm. Doc good to read: [Data Vault 2.0 with dbt Cloud](https://docs.getdbt.com/blog/data-vault-with-dbt-cloud);\n\
      3. Good point. I\u2019ve used dbt with BigQuery (for the book), but also redshift\
      \ and databricks. Those I\u2019m comfortable. Also heard good things using dbt\
      \ with Postgres or SQL Server, but indeed each database has is particularities,\
      \ so the suitability of dbt for a specific database depends on the use case\
      \ and requirements. It's essential to evaluate compatibility and performance\
      \ before deciding to use dbt with a specific database;\n4. Dbt certification\
      \ is a new thing. It didn\u2019t exist when we started to write this book. For\
      \ what I heard it is not that is complex, but it is to broader since it can\
      \ cover all the features within dbt. Unfortunately I can\u2019t give you more\
      \ details than that up to now, but I know that with the comprehensive trainings\
      \ provided by dbt (and our book \U0001F605) you\u2019ll be one step ahead;\n\
      5. On the book we\u2019ve focused only in SQL but yes dbt support Python alongside\
      \ SQL, allowing more advanced data transformations and manipulations. For example,\
      \ you can use Python functions and libraries within dbt to perform complex calculations,\
      \ data cleansing, or custom aggregations, providing greater flexibility in your\
      \ data transformations.\nHope I could help with your questions!"
  - name: Shalltear
    text: Thank you
  - name: iobruno
    text: "Shalltear  I'd like to add a few points here:\n> *Is there any tool comparable\
      \ to dbt?*\n- Matilion is more of fully-fledged ETL / ELT tool, comparable to\
      \ [Airbyte](https://airbyte.com/) / [Fivetran](https://www.fivetran.com/) /\
      \ [Meltano](https://meltano.com/) - [with integrations for ](https://www.matillion.com/blog/introducing-matillion-integration-for-dbt)*[dbt](https://www.matillion.com/blog/introducing-matillion-integration-for-dbt)*\
      \ for handling the 'Transformation' part of the pipeline\n- An alternative to\
      \ dbt, for *Transformations only*  is [Dataform](https://dataform.co/). \n \
      \   \u25E6 It used to support the three major Data Warehouses (Snowflake, RedShift,\
      \ BigQuery), But, back in 2020, [Dataform was acquired by Google](https://dataform.co/blog/dataform-is-joining-google-cloud).\
      \ If you're working with GCP, you can use it in a pretty similar way of that\
      \ in `dbt Cloud`, it has its own UI, schedulers, etc \n    \u25E6 Otherwise,\
      \ you can use [dataform core](https://github.com/dataform-co/dataform) to connect\
      \ to RedShift or Snowflake, but it's like working with `dbt-core` , you'll have\
      \ to deal with CLI and schedule your runs on your own (e.g.: Airflow/Mage)\n\
      \    \u25E6 Also, instead of Python, you'll have JavaScript support. \n    \u25E6\
      \ But, honestly? Stick with dbt, your CV/resume will thank you\n> *Have you\
      \ tested dbt vault?*\n- Nope\n> *Some database are supported by dbt labs, some\
      \ by other companies and some by the community*\n- The adapters for BigQuery,\
      \ Snowflake, Databricks and RedShift are production-grade. I haven't worked\
      \ with the others in production. \n- I'd advise against using an OLTP DB such\
      \ as Postgres for OLAP purposes. Just because you \"can\", doesn't mean you\
      \ should. Transactions queries are meant to be extremely fast and handle high\
      \ concurrency, Analytical queries, OTOH, are the exact opposite\n- If you're\
      \ on AWS and don't wanna spend sh*t ton of money on setting up a RedShift cluster\
      \ that will be idle most of the time, go with RedShift Serverless; if you're\
      \ On-Premises (for God-knows-what-reason), try [Clickhouse](https://clickhouse.com/)\
      \ but avoid the sacrilegious use of Postgres for OLAP on scale\n> *Can you say\
      \ anything regarding dbt certificates, in particular how complex they are?*\n\
      I think you'll find [this article useful](https://docs.getdbt.com/blog/tips-for-the-dbt-certification-exam):\
      \ it tells how the girl failed and then passed on the exam, and what she did\
      \ to accomplish it\n> *Since version 1.3, dbt supports python next to sql. Do\
      \ you have some examples where this is really useful?*\n- When you're dealing\
      \ with dynamic unions queries, you would have to make long and ugly store procedures\
      \ to handle it, OR you could use a python function to make it cleaner and tidy\n\
      - When your datalake is more like a data swamp, with schemas mixed up all over\
      \ the place (for example, saving schemaless JSONs as strings `just because back\
      \ then we thought it'd be easier` \U0001F926\U0001F3FB) , the SQL statements\
      \ become so complex to the point it's illegible and hard to maintain, so, using\
      \ Python would make it much cleaner\n- TL;DR: when the SQL is becoming too complex\
      \ to read and to maintain"
  - name: Shalltear
    text: Hi iobruno, thank you very much. Good points, as always. Appreciate it.
  - name: iobruno
    text: u're very welcome Shalltear
  - name: Stelios
    text: 'Another, similar to dbt, tool is sqlmesh: [https://sqlmesh.com](https://sqlmesh.com)'
- name: Rui Machado
  text: "Thank you everyone for the great sets of questions, the winners will be announced\
    \ soon \U0001F64C\U0001F3FB !! Was a pleasure for us to join this book of week\
    \ and hope you find the book interesting!! Any other questions or feedback ping\
    \ me or H\xE9lder Russa directly, we are staying in this amazing DataTalks slack!"
  replies: []
- name: "H\xE9lder Russa"
  text: Thank you everyone! It was a pleasure. And yes, we will be around, definitely.
  replies: []
- name: Aviv Zikel
  text: Thank you very much!
  replies: []
- name: Luis Oliveira
  text: "Congrats!!! \U0001F642"
  replies: []
- name: Valery Rabinin
  text: "Rui Machado and H\xE9lder Russa thanks for the effort you put into the book!\n\
    One of the main architecture patterns realized by dbt is moving away from stored\
    \ procedures towards tables/views - this is great for design readability and lineage\
    \ exploration. However, in some cases business logic is so complex that wiring\
    \ it into a set of views can become a nightmare. So, a couple of quesrions\n-\
    \ What is you personal take on \u201Cmodular\u201D approach of dbt?\n- Does your\
    \ book provide any tips &amp; tricks which would help with migrating from stored\
    \ procedures or handling complex transformation logic?"
  replies:
  - name: "H\xE9lder Russa"
    text: "Hello Valery. Indeed good discussion topic. \nThe modular approach of dbt\
      \ has its advantages in terms of design readability and lineage exploration.\
      \ However, it's true that in some cases, when we need to write complex business\
      \ logic into a set of views/tables can be challenging. I would say on these\
      \ cases a balanced approach, considering the complexity of the business logic\
      \ and the benefits of modularity, is essential to make effective use of dbt\
      \ capabilities."
  - name: "H\xE9lder Russa"
    text: "We don\u2019t cover direct migration from procedures to views, yet we introduce\
      \ and explain the benefits of modularity, and how to manage in particular scenarios."
  - name: Rui Machado
    text: "Valery!! Great to have a question from you!! \U0001F64C\U0001F3FB \U0001F64C\
      \U0001F3FB \U0001F64C\U0001F3FB"
  - name: Valery Rabinin
    text: "Thanks for the answers, Helder. \nRui Machado happy to be part of this\
      \ conversation! \U0001F64C"
- name: Toxicafunk
  text: How does dataform compares to DBT? Do you think yet choice of JS instead of
    Python makes adoption easier due to its prominence in web and fullstack devs or
    does the panda crowd is more likely to use these tools?
  replies:
  - name: Paul Priest
    text: 'I find JS to be a weird choice, given how widely python is viewed as the
      main language in the data space.

      We had a tough time on our team where one developer wrote some javascript transforms
      then left the team. We ended up having to re-write them because the rest of
      the team didn''t want to spend the team learning enough javascript to debug
      it.'
  - name: "H\xE9lder Russa"
    text: Hello again Toxicafunk. I would say there are some similarities in terms
      of features between dbt and Dataform.
  - name: "H\xE9lder Russa"
    text: Respective with JS and Python. I would say that JS has indeed a broader
      adoption between software engineers, yet not that much from data practitioners.
      In the other hand Python has a broader adoption from the whole variants of data
      practitioners and even from some software engineers, example Django framework.
- name: Shalltear
  text: 'My first question: dbt is a nice tool. But I have also seen some disadvantages,
    like debugging is sometimes not easy or using snapshots for a scd table when you
    have to make a back-fill and the dataset now contains the unique identifier more
    than once. From your perspective could you provide a list of the greatest advantages
    and more even important a list of the greatest disadvantages of using dbt? I think
    this would help many people to decide whether they should introduce dbt or not.'
  replies:
  - name: Rui Machado
    text: 'Hey Shalltear! Thank you for your question! Definitely a great way to start.
      I can give you a set of dbt''s pros and cons that we actually cover in our book.
      (This answer assumes you know what dbt is)

      *Some Pros:*

      - This is my favorite: It''s SQL-friendly. If you''re comfortable with SQL,
      dbt will be very natural to you.

      - dbt encourages modular and reusable code, which can make your life easier
      when building complex data models.

      - It integrates with Git, so you can keep track of changes and roll back if
      something goes wrong.

      - dbt automatically generates documentation, which is a huge time-saver and
      helps with data governance.

      - It has built-in testing functions to ensure your transformations are accurate,
      which helps maintain data integrity.

      *Challenges (Not going to say cons as there are ways to overcome) of dbt:*

      1. dbt doesn''t handle the extract and load in ELT; you''ll need other tools
      for that, such as Airflow which means more moving parts to manage.

      2. When things don''t go as planned, debugging in dbt can be a bit of a headache,
      especially if you''re used to more visual debugging tools.

      3. For those not familiar with Jinja or advanced SQL, there might be a learning
      curve - Not very hard though, you will pick it up quite fast

      4. If you''re coming from a GUI-based tool, dbt''s code-centric approach might
      feel less intuitive.'
  - name: Shalltear
    text: thank you
- name: Luis Oliveira
  text: 'My questions are three:

    1- What are in your opinion the best tools and packages to use with dbt?

    2- Does dbt have any concurrency?

    3- What is going to be the next trends/changes in the analytics engineering?'
  replies:
  - name: Paul Priest
    text: "My opinions:\nPackages\n- dbt-utils (must have for tests/quality checks/freshness/etc)\n\
      - dbt-expectations (more advanced statistical testing)\n- dbt-checkpoint (formerly\
      \ pre-commit, excellent for coverage reports, automating linting rules etc)\n\
      [https://github.com/dbt-checkpoint/dbt-checkpoint](https://github.com/dbt-checkpoint/dbt-checkpoint)\n\
      Concurrency\n dbt generates a dependency graph and will run models concurrently\
      \ that do not depend on one another.\nIf we had parent model and two children\n\
      `A -&gt; [B, C]`  \nA would be run first and then B and C could be run concurrently.\
      \ There's flexibility with how much concurrency you use and it does depend a\
      \ bit on the backend warehouse/db you're using.\nTrends\nI think a number of\
      \ people are saying LLMs will be the future of modelling. I'm skeptical of this\
      \ claim because of the difficulty of mapping business processes to code but\
      \ that's just my 2 cents."
  - name: "H\xE9lder Russa"
    text: 'Hello Luis!

      Paul pretty much answered the questions. From one side, dbt-utils and dbt-expectations
      (which relies on great expectations data quality tool) are potentially the most
      used and useful packages of dbt'
  - name: "H\xE9lder Russa"
    text: In the other side, yes, dbt allows concurrency at model execution level.
      For that you need to define the execution threads, saying how many models can
      be parallelized. Yet, important to know, and as Paul mentioned, this also needs
      to consider the dependency graph. If you have three models (A, B and C), but
      if B and C dependes from the A, even if you increase the number of threads.
      It will always execute the A first and then B and C in parallel.
  - name: "H\xE9lder Russa"
    text: I think one of the main challenges the analytics engineer field might face
      is related to the boundaries of their work, where might be some gray area between
      what a data engineer does and what a data analyst of even scientist do. It is
      a new field, and I believe that in the future we might see some more enlightening
      on this.
- name: Shalltear
  text: 'Next question: Comparing dbt core with dbt cloud. Is it worth to use dbt
    cloud?'
  replies:
  - name: Rui Machado
    text: Choosing between dbt Core and dbt Cloud depends on your team's technical
      skills, resource availability, and project requirements. dbt Core suits teams
      that prefer managing infrastructure and workflows via command-line, offering
      a robust, open-source option without added costs. On the other hand, dbt Cloud
      provides a managed, user-friendly platform with collaborative features, scheduling,
      and built-in CI/CD, streamlining operations at a monthly cost. For teams prioritizing
      ease and reduced maintenance, dbt Cloud is ideal, while budget-conscious or
      technically proficient teams may lean towards dbt Core.
  - name: Shalltear
    text: thank you
- name: Shalltear
  text: 'Next question: Can you or does your book provide a list of `dos and don''ts`  and
    something like "10 best tips and tricks"?'
  replies:
  - name: Paul Priest
    text: "Not the author but speaking from my own experience.\nSome mistakes we made.\n\
      Incorrectly configure incremental models so all of your tables are doing full\
      \ refreshes for a full year.\nSet the test config block to limit test failures\
      \ to 100 and only throw an error with &gt; 100 test failures. Partly due to\
      \ how the failures get saved to a table and you specify the max row count but\
      \ definitely our mistake! \U0001F923\nSo many warnings that were ignored which\
      \ should have been failing!\nAs for dos:\nUse the great functionality dbt has\
      \ for data quality, checking freshness and generating/persisting docs."
  - name: Rui Machado
    text: "In the book we do cover a few tips and recommendations although we don't\
      \ really have a chapter on \"top 10\" across the book you will find many best\
      \ practices \U0001F642 Not just on dbt but also on data modelling, sql, jinja\
      \ among others"
  - name: Shalltear
    text: thanks
- name: Low Kim Hoe
  text: Hi, want to ask how do you setup the dbt core for production env workflow?
  replies:
  - name: Paul Priest
    text: 'Not the author but I''ve used airflow for orchestration by packaging each
      project separately into a docker container to be triggered via airflow.

      It works nicely and allows for versioning different projects, dbt versions,
      dbt dependencies, etc.'
  - name: Rui Machado
    text: Hey Low! Thank you for your question. The answer is not that easy as it
      depends on the availability, security, scalability and other factor you might
      want to take in consideration. However I will build on top of Paul and say that
      in fact, when setting up dbt Core for production, incorporating Airflow and
      Kubernetes elevates data operations. Airflow orchestrates dbt tasks, managing
      dependencies and precise scheduling, providing a control tower for data workflows.
      Kubernetes ensures containerisation of each project, functioning as a self-adjusting
      engine for efficient performance.
  - name: Low Kim Hoe
    text: "thank you so much for both of your responses on my questions \U0001F604"
- name: Sumith Nangunuri
  text: 'I have few question and hope you can help me on it,

    - Can you please provide insights into the specific sections or chapters of the
    book that would be most beneficial for someone with a foundational understanding
    of DBT and SQL (Snowflake) and and how DBT assists in ensuring data quality and
    reliability??

    - In your opinion, what are the key takeaways or advanced techniques that readers
    with basic knowledge of DBT and SQL (Snowflake) can expect to gain from reading
    this book?

    - How does the book cater to readers like me who want to deepen their knowledge
    and proficiency in DBT and SQL (Snowflake) while focusing on practical implementation?'
  replies:
  - name: Rui Machado
    text: 'Hey Sumith, thank you for your questions!! the book overall is quite accessible
      but I would highlight our Data Modelling with SQL and dbt as the main one to
      take in consideration in your case.

      I would say reader will gain enough understanding of analytics engineering,
      the importance of data modelling and overall sql and dbt which in my opinion
      will help analysts and engineers booting their data skills.

      Although we go deep in some chapters, our intention was always to set the direction
      when it comes to understanding what is worth deep diving into. Take it as a
      comprehensive depth first book. Then for deep dives maybe there are other books
      that will complement.'
  - name: Sumith Nangunuri
    text: Thank you Rui Machado for sharing much useful information.
- name: Waqas Shah
  text: 'Question: I tried simple tutorial. But my ask is where exactly in my DE day
    to day job i can use DBT. Where experienced DE guys are using it and how?

    For analytics or general data quality or transformation i get it. But is there
    anything DE guy can leverage from it?'
  replies:
  - name: Rui Machado
    text: 'Hey Waqas, I would say that dbt is great for making data transformations
      more efficient, automated and reusable. Imagine that you can take all your ETL
      packages tranformations into a sql-friendly environment full of packages that
      understand your needs (Create surrogate keys, test data, document data, see
      lineage, among others ).

      It also helps you work better with analysts because you can set up the core
      transformations and they can build on top of them to gain insights. dbt also
      integrates well with version control and CI/CD workflows, which is a big win
      for reliability. Plus, dbt is a trusted ally when it comes to ensuring the accuracy
      of your data through testing and automatically keeping your documentation up
      to date.'
- name: Josh
  text: "Hi there. I have a few questions. \n- There are some who say analytics engineering\
    \ is a passing trend that will become phased out sooner or later as a sub-field\
    \ or field in data. I'd love to know your thoughts on that if possible, thank\
    \ you. \n- Secondly, what in your opinion are the emerging trends in analytics\
    \ engineering at the moment that are of importance to note for someone in this\
    \ field looking to boost their career?\n- Thirdly and finally, what general tips\
    \ would you give someone who's about to go into an analytics engineering interview?\
    \ \nThank you for your time."
  replies:
  - name: Rui Machado
    text: "Hey Josh! Great one.\nI believe analytics engineering is bigger that you\
      \ call it \U0001F642 For example, when I started working with data we have roles\
      \ such as data miner, business intelligence developer among other. My personal\
      \ view is that at the moment companies are facing the need to have people that\
      \ understand data in such a way that can create semantic models on top of it\
      \ to facilitate insights creation. Analytics Engineers are in fact data lovers\
      \ that live in between data engineers and scientists. With this in mind the\
      \ role might evolve and its name might change but the need for the kind of responsibilities\
      \ will be around for a long time."
  - name: Rui Machado
    text: "My piece of advice would be: Invest in owning the basics: Data modelling,\
      \ the main transformation patterns, and how to ensure data reliability and understanding.\
      \ dbt can help there but its only a tool \U0001F642"
  - name: Josh
    text: "Thank you so much for the response Rui Machado \U0001F64F\U0001F3FE"
- name: Aviv Zikel
  text: "Hi there, I got a question as somebody who has being working on his first\
    \ project with Dbt snowflake and airflow for the last year.\nDuring my way I\u2019\
    ve seen how things are done in the DBT way.\nSometimes, my team intuitively solved\
    \ with a way which is not Dbt native solution.\nDo you show any ways of thinking\
    \ the DBT way when facing various problems?"
  replies:
  - name: Rui Machado
    text: Great point Aviv!! Embracing the dbt way means thinking in modular SQL models,
      writing tests alongside transformations, and documenting your work for clarity
      and collaboration. It's about trusting the process, which means structuring
      your work so it's maintainable, understandable, and ready for automation.
  - name: Aviv Zikel
    text: Thanks! I was also talking about the usage of the different materialisation
      types to our models :)
- name: Arun Nethi
  text: "Hi, \nThanks for taking time to answer.\nMy question:\nSchematically I believe\
    \ this is one question hence putting them together.\nCan any organization be able\
    \ to leverage DBT?Who is DBT for vs not for? Things to know before deciding to\
    \ use DBT? And common pitfalls for developers?"
  replies:
  - name: Rui Machado
    text: Great question Arun!! I believe dbt can be beneficial for any organization
      but a bit more to those with SQL-savvy teams that want to automate data transformations
      and adopt technical best practices. However, for organizations that rely heavily
      on ETL processes or don't have strong SQL skills, dbt might require a certain
      learning curve. Before getting involved with dbt, you should learn how to treat
      data like code, which can be a challenge by itself.
  - name: Arun Nethi
    text: "\u201CData like code\u201D! Interesting! Thank you. Will explore more on\
      \ this."
- name: Tim Makhambetov
  text: What functionality do you expect to be added/would like to be added to dbt
    in the future?
  replies:
  - name: "H\xE9lder Russa"
    text: Hello Tim, some two great features ahead (or that are having some refinements)
      is the dbt semantic layer and referencing models across projects - this last
      one will enable some new data architectures such as data mesh.
  - name: "H\xE9lder Russa"
    text: Nonetheless dbt Semantic Layer is here for a while, it now leverages MetricFlow
      where you can define and manage your companies metrics.
  - name: Tim Makhambetov
    text: ':thank_you: actually looking into implementing semantic layer in my org'
  - name: Tim Makhambetov
    text: all the best with the book release!
  - name: "H\xE9lder Russa"
    text: Thank you very much!
- name: Polite
  text: "Rui Machado and H\xE9lder Russa thank you so much .I have been following\
    \ Analyitcs engineering trends closely .Just few questions \n1.Iam a data analyst,\
    \ with experience in SQL ,do you think I need to learn data engineering first\
    \ before I learn DBT to be ready for the Analytics engineering career ? \n2. Besides\
    \ this book ,what other resources you can share for someone interested in Analytics\
    \ engineering career ?\n3.The future of Analytics engineering and AI ? How LLM\
    \ models assist the future Analytics engineer ?"
  replies:
  - name: Rui Machado
    text: 'Love this one Polite!! Great set of questions.

      Starting with 1) With your SQL experience, you''re already on the right path.
      Also, dbt can be a great entry point to learn data engineering concepts while
      focusing on analytics. It''s designed to bridge the gap between data analysis
      and engineering, making it a powerful tool for analysts. You can gradually dive
      deeper into data engineering as you go along.

      2) I would say the dbt community and blog itself but there are also great courses
      already available. Plus I always default to Kimball and Inmon for anyone to
      learn more about data modelling which is always helpful.

      3) When it comes to AI, always remember that garbage in garbage out, meaning
      that with increasing reliance on quality data for AI analytics engineers will
      play a pivotal role in designing efficient data pipelines and ensuring data
      quality - Of course often overlapping with data engineers and scientists responsibilities.'
- name: Sven
  text: What is your take on NoSQL? Especially for Analytics or Transformation. Is
    it best practices to always try SQL modeling first because most of time it makes
    more sense?
  replies:
  - name: Rui Machado
    text: Thank you Sven, as a data modelling fanatic I love your question. Personally
      I believe the choice between NoSQL and SQL for analytics and transformation
      depends on the specific project requirements. It's a best practice in my opinion
      to start with SQL modeling for its maturity and transactional integrity, but
      consider NoSQL for scalability and unstructured data when needed. Noways with
      certain file formats and databases you can benefit from both worlds (We briefly
      touch on that on the book)
  - name: Sven
    text: "Thanks! I also dig deeper into scalability for NoSQL but I also came to\
      \ the conclusion that most of time it won't be a problem. And as you mentioned\
      \ now you have DBs that combine the best of both worlds.\nI was just wondering\
      \ how to start but I think you have the same opinion, go with SQL until you\
      \ run in problems? \U0001F600"
- name: Toxicafunk
  text: "Hi,\nThanks for being here. \n1. What are the best practices for using DBT\
    \ in Analytics Engineering? \n2. Does your book cover lesser known DBT topics\
    \ such as seeding, snapshotting and debugging?\n3. What are the prerequisites\
    \ for reading this book?"
  replies:
  - name: Rui Machado
    text: "Hey Toxicafunk!\n1. Ehehe great question to find the answer in our book!!\
      \ There are a few in fact, I would highlight modularisation, data modelling\
      \ and testing properly\n2. Yes we do \U0001F642 We tried to go deep in coverage\
      \ of dbt features \n3. Not much, if you know a bit of SQL you should be fine\
      \ \U0001F642 We tried to make the book very accessible and easy to follow."
- name: Koffi
  text: "Hello\n1. Does the Book cover dimensional modeling with dbt ?\n2. Besides\
    \ running quality tests and documentation, what are the biggest use cases for\
    \ using dbt?\n3. At which size of team/company/tables using dbt become necessary?\
    \ \nThanks"
  replies:
  - name: Rui Machado
    text: "Hello Koffi!\n1. Yes it does, we show hoe you can implement start schemas\
      \ / snowflake and data vault with dbt. \n2. I can add what I wrote before:\n\
      \    a. *Some Pros:*\n        \u25AA\uFE0E This is my favorite: It's SQL-friendly.\
      \ If you're comfortable with SQL, dbt will be very natural to you.\n       \
      \ \u25AA\uFE0E dbt encourages modular and reusable code, which can make your\
      \ life easier when building complex data models.\n        \u25AA\uFE0E It integrates\
      \ with Git, so you can keep track of changes and roll back if something goes\
      \ wrong.\n        \u25AA\uFE0E dbt automatically generates documentation, which\
      \ is a huge time-saver and helps with data governance.\n        \u25AA\uFE0E\
      \ It has built-in testing functions to ensure your transformations are accurate,\
      \ which helps maintain data integrity.\n    b. *Challenges (Not going to say\
      \ cons as there are ways to overcome) of dbt:*\n        i. dbt doesn't handle\
      \ the extract and load in ELT; you'll need other tools for that, such as Airflow\
      \ which means more moving parts to manage.\n        ii. When things don't go\
      \ as planned, debugging in dbt can be a bit of a headache, especially if you're\
      \ used to more visual debugging tools.\n        iii. For those not familiar\
      \ with Jinja or advanced SQL, there might be a learning curve - Not very hard\
      \ though, you will pick it up quite fast\n        iv. If you're coming from\
      \ a GUI-based tool, dbt's code-centric approach might feel less intuitive.\n\
      3. Any size \U0001F642 As long as you handle transformations, dbt can be usefull"
  - name: Koffi
    text: Thanks
- name: Bilal khatri
  text: "Hello Rui Machado and H\xE9lder Russa thank you for your support.\nThere\
    \ are following thing i want to know.\n1. What are the prerequisite to explore\
    \ and read the book ? i am very excited.\n2. I know the data pipeline using airflow\
    \ and dbt, i have worked on data validation and testing, customized validation\
    \ etc. I want to learn to explore dbt outside of airflow data pipelines like analytics\
    \ engineering, data validation automation etc, will it be helpful to explore the\
    \ out of the box modeling. ?"
  replies:
  - name: Rui Machado
    text: "Hi Bilal, thank you for your questions.  Not much, if you know a bit of\
      \ SQL you should be fine \U0001F642 We tried to make the book very accessible\
      \ and easy to follow. Yes!! Modelling is always usefull, it will allow you to\
      \ create semantic layers that are fit for purpose (Multiple purposes actually)"
- name: Rui Machado
  text: "So far, great set of questions everyone \U0001F642"
  replies: []
- name: Konrad
  text: 'Cheers, everyone. The title "Analytics Engineering with SQL and DBT" made
    me come here : ) Congratulations on the release of the title!'
  replies: []
- name: William Jamir
  text: 'I know the book focuses on dbt as the primary tool for data transformation.

    However, do you know if are there other tools available as an alternative to dbt?

    Also, what are your thoughts on ibis and its potential as an alternative to dbt?
    Do you see ibis as something worth trying, or do you believe that these tools
    have different strengths that don''t complement each other? (my user case is an
    ETL pipeline in Python).'
  replies:
  - name: "H\xE9lder Russa"
    text: "Hello William, thank you for your questions. While writing the book I came\
      \ across with [Matillion](https://www.matillion.com) . Never tried tbh but might\
      \ be good to take a look as well.\nNow concerning with Ibis, just took a look\
      \ to get familiarize. I think it is interesting its native compatibility with\
      \ Spark, which is already a huge plus. Yet in its core can be just a matter\
      \ of choice between a more SQL-like syntax or pandas-like syntax. However if\
      \ you are looking into a bigger ecosystem and features, from testing, documentation\
      \ or even some flavor of governance (like data lineage), dbt might be more interesting.\n\
      Respective to your use case, if you are already in python, and considering time\
      \ to market just test Ibis, shouldn\u2019t be that hard as setup locally when\
      \ compared with dbt core, since you had also to re-do all your code."
- name: William Jamir
  text: "In a scenario where a company already has a set of defined routines for data\
    \ transformation.\nI would like to know if your book covers these topics:\n- What\
    \ are the specific benefits of moving to dbt in this scenario? \n- How can companies\
    \ evaluate whether or not moving to dbt is a worthwhile investment? \n- What are\
    \ some potential challenges that companies may face when migrating to dbt?"
  replies:
  - name: "H\xE9lder Russa"
    text: "Hey again William, we don\u2019t have a dedicated chapter who covers the\
      \ benefits or challenges of dbt adoption within a company, it is sort of spread\
      \ through the book. This type of decision requires also to understand the company\
      \ reality. If there is already a transformation tool and want to move to dbt\
      \ I would say to evaluate if the current already supports features like:\n-\
      \ collaborative development and version control;\n- Scalability;\n- Data documentation\
      \ and testing parallel to documentation;\n- Facility of developing DRY code;\n\
      Along with that it will also be important to do a cost-benefit analysis and\
      \ time saving it will gain (or not) by adopt dbt. Not only from the potential\
      \ time gain in development but also from the native data observability capabilities\
      \ that dbt provides and that the whole company can benefit of.\nAnd by last,\
      \ the main challenges, for sure. dbt isn\u2019t a complex tool to learn but\
      \ requires always a learning curve. Plus, it is also important to understand\
      \ the current systems/databases inside the company, as well as ensure existing\
      \ data formats are compatible with dbt."
- name: Eduardo Vazquez
  text: "First question: Does the book focus on dbt core or dbt Cloud? I have experience\
    \ using both, but in the case of dbt core, Im having trouble setting up and configure\
    \ a scheduler, which becomes very important when you want the create a specific\
    \ materialization. It would be great if you could provide some guidance or point\
    \ us to some resources. \U0001F600\nSecond question: What is your opinion about\
    \ the Modern Data Stack?\nThank you!"
  replies:
  - name: "H\xE9lder Russa"
    text: Hello Eduardo! Interesting questions. The book uses dbt cloud to present
      dbt. We decided to go for a more pragmatic approach, since our goal was to show
      the full extent of dbt and its features and so with dbt cloud we were able (in
      a more simple way) to demonstrate that. Nevertheless a good number of what is
      done inside the dbt cloud, and it is presented in the book, uses the dbt CLI,
      which in the backend runs on top of dbt core.
  - name: "H\xE9lder Russa"
    text: Using only dbt core you can use airflow as a scheduler. It will certainly
      work.
  - name: "H\xE9lder Russa"
    text: "The second question, wow, it would be a whole new book \U0001F605. Overall\
      \ exciting times, yet more complex and dynamic. I remember back in 2013, my\
      \ \u201Cmodern data stack\u201D was using SSIS, SSAS and SSRS from Microsoft.\
      \ We had a more clear boundaries between tools and their purpose. Now the times\
      \ are different, we have way more requirements related with data security, governance,\
      \ processing, scalability, etc. Other tools more prepared, leveraging cloud,\
      \ has emerged. I love that but it turns the choice a bit more complex. As an\
      \ example, if you look into AWS data stack, you have some tools overlap. A good\
      \ example is Glue or EMR, which turns the choice a bit more challenged. But\
      \ from another point we have more offer and competition, which demands the data\
      \ tools developers to continue to level up their products and provide with more\
      \ cool features. dbt is a good example of that with the semantic layer (for\
      \ example)."
  - name: Eduardo Vazquez
    text: "Thank you so much H\xE9lder Russa"

---

With the shift from data warehouses to data lakes, data now lands in repositories before it's been transformed, enabling engineers to model raw data into clean, well-defined datasets. DBT (data build tool) helps you take data further. This practical book shows data analysts, data engineers, BI developers, and data scientists how to create a true self-service transformation platform through the use of dynamic SQL.

Authors Rui Machado from Monstarlab and Helder Russa from Jumia show you how to quickly deliver new data products by focusing more on value delivery and less on architectural and engineering aspects. If you know your business well and have the technical skills to model raw data into clean, well-defined datasets, you'll learn how to design and deliver data models without any technical influence.

With this book, you'll learn:

- What DBT is and how a DBT project is structured
- How DBT fits into the data engineering and analytics worlds
- How to collaborate on building data models
- The main tools and architectures for building useful, functional data models
- How to fit DBT into data warehousing and laking architecture
- How to build tests for data transformations