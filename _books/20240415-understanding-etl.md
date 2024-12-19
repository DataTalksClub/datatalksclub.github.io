---
authors:
- mattpalmer
cover: images/books/20240415-understanding-etl/cover.jpg
description: Book of the Week. Understanding ETL by Matt Palmer
end: 2024-04-19 23:59:59
image: images/books/20240415-understanding-etl/preview.jpg
links:
- link: https://www.oreilly.com/library/view/understanding-etl/9781098159269/
  text: Book's page
start: 2024-04-15 00:00:00
title: Understanding ETL

archive:
- name: PHAM NGUYEN HUNG
  text: Matt Palmer Can you share examples how folks at Replit use Databricks products
    (for ETL or not)? I know you guys partnered with MosaicML to train your LLM ([https://www.youtube.com/watch?v=ju73sWVtvU0](https://www.youtube.com/watch?v=ju73sWVtvU0))
    but not sure about anything else.
  replies:
  - name: Matt Palmer
    text: "I can't comment on our tech stack outside of what you'll find online \U0001F642"
  - name: Matt Palmer
    text: 'Databricks is a great option for ETL, but Snowflake has good options too.

      Depending on your situation, an open-source stack could work well, also'
- name: William Jamir
  text: 'In the field of software engineering, we rely on established best practices,
    design patterns, and architectural principles to develop robust and maintainable
    systems.

    However, borrowing some of these design principles to design an ETL pipeline is
    not straightforward (at least in my opinion).

    I am interested in applying/implementing layered architectures, such as business
    layers, repository layers, and routing layers, to my ETL pipelines any other well
    know design patterns.

    My goal is to create a structure that resembles an "well know and approved" architecture,
    or something that more well designed to avoid coupling and allow better maintenance,
    just to run away of having one large function with all the code, or multiple small
    functions complementing each other without a clear design.

    In your opinion, can these patterns and practices from traditional software engineering
    be effectively translated to data pipelines in tools like Airflow or Prefect?

    If not, why not? What are the alternatives?

    Additionally, do you have any suggestions or recommendations for resources that
    touch on these topics? (software design of etl pipelines).

    Does your book discuss any of these questions/concerns?

    Matt Palmer'
  replies:
  - name: Matt Palmer
    text: 'I would research the "modern data stack" for best practices in data engineering.

      This guide will feature some of those principles, but it''s written more for
      folks who are just learning about ETL.

      There are newer tools that leverage best practices in software development to
      create robust, scalable solutions.

      IMO things like pure airflow or prefect do not accomplish that alone. Again,
      researching "modern data stack" as well as new tools in the ETL space, reading
      things like r/dataengineering and chatting in slack groups is a great place
      to start'
  - name: Matt Palmer
    text: If you live somewhere with industry events or if you can chat with practitioners,
      that's also an excellent source of knowledge
  - name: Matt Palmer
    text: 'I would be wary of "data influencers," many of them are paid or operating
      on some sort of agenda.

      Just be skeptical, which it sounds like you already are'
- name: Ricky McMaster
  text: 'Hi Matt Palmer, thanks a lot for doing this. Just curious as to whether the
    book covers how the nature of ETL (and ELT) has changed due to the rise of the
    cloud data platforms.

    For example, since cloud DWHs provide more volume and speed at the cost of less
    rigorous data integrity measures, the gap has been filled to a large extent by
    frameworks such as dbt. Therefore data integrity is being handled more and more
    by these tools, rather than the data platforms themselves.  And would you see
    this as a positive development?'
  replies:
  - name: Matt Palmer
    text: "Hi Ricky! The focus of the book is very much on the basics of ETL / ELT\u2014\
      \ you bring up an interesting point though.\nThe need for platforms like dbt\
      \ has largely grown from the volume / velocity of data, made possible by cloud\
      \ data platforms"
- name: Low Kim Hoe
  text: Hi, what is the data destination of data pipeline for this text book? Azure
    Synapse Analytic or Databricks Data Lake?
  replies:
  - name: PHAM NGUYEN HUNG
    text: I think the book does not have a GitHub repo for code. But most the technologies
      come from Databricks. So Databricks Delta Lake could be the answer for your
      question, at least when it comes to ETL or ELT.
  - name: Low Kim Hoe
    text: Thanks for the reply :D
- name: Ella
  text: 'Does the book cover the theory behind ELT/ETL, use-cases? Or, it showcases
    examples using specific tools/platforms?

    Book released Mar 2024? Oh, not sure my local library has it in yet...'
  replies: []
- name: Romuald Tcheutchoua
  text: what data engineering technologies does this book cover?
  replies:
  - name: Matt Palmer
    text: ''
  - name: PHAM NGUYEN HUNG
    text: "By technologies, I understand 2 things:\n1. Specific _tools, services,\
      \ etc._ like Databricks, dbt, GCP's Dataproc. If that's the question, then the\
      \ answer is things that Databricks offer like Delta Lake. (The cover kinda gives\
      \ it away \U0001F642).\n2. _Theoretical solution_ to the problem of data engineering.\
      \ Then it is Matt's answer.\nTalking about effective and innovative, for point\
      \ 1., it really depends on what you are trying to do to select the correct tool\
      \ or service providers (My company is a Databricks customer, though we are being\
      \ pitched by others too). For theoretical solution, there can be ETL, ELT, reverse-ETL,\
      \ shm-ETL, but in the end the stuff you have to do based on 1st principle will\
      \ always involve:\n1. *E*xtract the data into the system somehow.\n2. *T*ransform\
      \ it into something useful.\n3. *L*oad the useful stuff out to where it can\
      \ be useful.\nwhich Matt covered in the book."
- name: Romuald Tcheutchoua
  text: does it take into account the most effective and innovative Technologies ?
  replies: []
- name: Konrad
  text: 'Sorry if my question is not thoroughly thought through. In the book''s table
    of contents, terms such as _Data Transformation Patterns_, _Data Update Patterns_,
    and _Design Patterns_ are listed.

    Q: If we could provide bullet points naming those DT, DU, and Design patterns,
    what would they be?

    Thank you for the answer

    EDIT: Got the book thanks to the link shared : ) and now I can see the names of
    the patterns'
  replies: []
- name: Ricky McMaster
  text: Hi again Matt Palmer, just wondering what thoughts you had (or what you put
    in the book) about change data capture, and how that's evolved?  It's an old topic,
    but given the huge increase in variety and volume of data sources, I would imagine
    there are quite a few more approaches than those written about by (for example)
    Joe Caserta and Ralph Kimball ~20 years ago.
  replies:
  - name: Matt Palmer
    text: 'There are! and it seems like CDC is being supported out-of-the-box by more
      and more tools.

      Even tech like [Delta Lake](https://www.databricks.com/blog/2021/06/09/how-to-simplify-cdc-with-delta-lakes-change-data-feed.html)
      (and Iceberg, I''m sure) supports simple CDC'

---

Whether your title is data engineer, scientist, or analyst, you’ve likely heard the term ETL. There’s a good chance ETL is a part of your life, even if you don’t know it.

Short for extract, transform, load, ETL is used to describe the foundational workflows most data practitioners are tasked with—taking data from a source system, changing it to suit their needs, and loading it to a target.

- Want to help product leaders make data-driven decisions? ETL builds the critical tables for your reports. 
- Want to train the next iteration of your team’s machine learning model? ETL creates quality datasets. 
- Are you trying to bring more structure and rigor to your company’s storage policies to meet compliance requirements? ETL will bring process, lineage, and observability to your workflows.

If you want to do anything with data, you need a reliable process or pipeline. This holds true from classic business intelligence (BI) workloads to cutting-edge advancements, like large language models (LLMs) and AI.

In Understanding ETL, we walk through the components of ETL, step-by-step, discussing architecture, maintainability, and scalability. With a focus on brevity, we’ll give you the tools you need to understand the basics about the pattern that drives data processing at scale.