---
episode: 3
guests:
- adrianbrudaru
ids:
  anchor: atalksclub/episodes/Trends-in-Data-Engineering--Adrian-Brudaru-e2ui9ae
  youtube: AlCFKbFIEM8
image: images/podcast/s20e03-trends-in-data-engineering.jpg
links:
  anchor: https://creators.spotify.com/pod/show/datatalksclub/episodes/Trends-in-Data-Engineering--Adrian-Brudaru-e2ui9ae
  apple: https://podcasts.apple.com/us/podcast/trends-in-data-engineering-adrian-brudaru/id1541710331?i=1000698294801
  spotify: https://open.spotify.com/episode/35QbCW6Evqk1EPMKUDGGdv
  youtube: https://www.youtube.com/watch?v=AlCFKbFIEM8
season: 20
short: Trends in Data Engineering
title: 'Future-Proof Data Engineering: Adopt Apache Iceberg, DuckDB & AI-Powered Pipelines'
transcript:
- header: Episode opening & guest introduction
- line: This week, we’ll talk about trends in data engineering. Our special guest
    today is Adrian, a returning guest. This is his third time on the podcast, but
    he’s also been part of workshops and open-source demos. Many of you probably know
    him already.
  sec: 1
  time: 0:01
  who: Alexey
- line: Adrian is the co-founder of DLT Hub, the company behind DLT, which we’ll discuss
    today. We’ll also talk about trends in data engineering. When we launched our
    Data Engineering Zoom Camp recently, one of the questions from participants was,
    “How do you see data engineering evolving, and what are the trends?” I realized
    I couldn’t answer that, so I thought of Adrian.
  sec: 1
  time: 0:01
  who: Alexey
- line: Welcome to the podcast, Adrian. It’s a pleasure to have you here again.
  sec: 1
  time: 0:01
  who: Alexey
- header: Perspective on evolving data engineering challenges
- line: The pleasure is mine. I don’t have all the answers, but I can share my perspective
    and observations.
  sec: 143
  time: '2:23'
  who: Adrian
- line: That’s what makes it interesting. Everyone has opinions, and you’re much closer
    to data engineering than I am.
  sec: 155
  time: '2:35'
  who: Alexey
- line: As always, the questions for today’s interview were prepared by Johanna Bayer.
    Thank you, Johanna, for your help.
  sec: 155
  time: '2:35'
  who: Alexey
- line: Before we dive into trends, let’s start with your background. Can you briefly
    share your career journey?
  sec: 155
  time: '2:35'
  who: Alexey
- header: 'Career journey: startups, freelancing, founding DLT'
- line: Sure. I started in data in 2012. I spent five years working at startups in
    Berlin, building data warehouses. Then I joined an enterprise but didn’t enjoy
    it, so I became a freelancer for five years.
  sec: 190
  time: '3:10'
  who: Adrian
- line: After freelancing, I wanted to do more than just consulting. I didn’t enjoy
    managing an agency, so I decided to build DLT, a tool I wish I had as a data engineer.
    That’s the short version.
  sec: 190
  time: '3:10'
  who: Adrian
- line: You mentioned DLT is a tool you wish you had as a data engineer. Do you use
    it often?
  sec: 236
  time: '3:56'
  who: Alexey
- header: DLT as a Python-based ingestion standard and market impact
- line: I use it all the time. As a data engineer, much of your work involves data
    ingestion—taking data from semi-structured formats like JSON and transforming
    it into a structured format. DLT automates this process, so there’s no reason
    to use anything else.
  sec: 243
  time: '4:03'
  who: Adrian
- line: Do you remember when we last spoke on the podcast?
  sec: 266
  time: '4:26'
  who: Alexey
- line: Just over a year ago, I think.
  sec: 271
  time: '4:31'
  who: Adrian
- line: Yes, over a year ago. You were already at DLT, and we talked about your journey
    from freelancing to founding a company.
  sec: 273
  time: '4:33'
  who: Alexey
- line: Since then, a lot has changed. I’ve enjoyed visiting your office and seeing
    your team grow. You’ve moved to a bigger space, and it’s been amazing to witness
    your progress.
  sec: 273
  time: '4:33'
  who: Alexey
- line: From an outsider’s perspective, it’s been exciting. Can you share what’s been
    happening internally over the past year?
  sec: 273
  time: '4:33'
  who: Alexey
- line: We started by squatting in other people’s offices, but now we’ve grown significantly.
    Last year, I talked about creating a standard for data ingestion with DLT, and
    I think we’ve succeeded.
  sec: 353
  time: '5:53'
  who: Adrian
- line: DLT has become a standard for Python-based data ingestion. We’ve commoditized
    this market, making it accessible to everyone. This has challenged the industry
    to offer more value beyond just connectors.
  sec: 353
  time: '5:53'
  who: Adrian
- line: Are you still actively working as a data engineer, or what does your role
    look like now?
  sec: 453
  time: '7:33'
  who: Alexey
- header: DLT Plus vision and partnership outreach for freelancers
- line: Right now, I’m focused on DLT Plus, figuring out how to make it a meaningful
    product. We’re building a data platform around DLT, incorporating best practices
    and innovation.
  sec: 465
  time: '7:45'
  who: Adrian
- line: So your work involves figuring out how DLT Plus will function?
  sec: 527
  time: '8:47'
  who: Alexey
- line: Yes, as a founder, my role involves exploring initiatives, listening to feedback,
    and testing ideas. I’m also working on building a partnership network to maximize
    value for customers.
  sec: 535
  time: '8:55'
  who: Adrian
- line: For freelancers listening, how can they reach out to learn more about this
    partnership network?
  sec: 590
  time: '9:50'
  who: Alexey
- line: They can reach out on LinkedIn or find partnership links on our website. This
    is mainly for people already using DLT.
  sec: 607
  time: '10:07'
  who: Adrian
- line: You’ve been in the data engineering industry for over a decade. How has the
    industry changed over the past five years?
  sec: 621
  time: '10:21'
  who: Alexey
- header: 'Industry shift toward specialization: governance, data quality, streaming'
- line: Five years ago, there was a shortage of data engineers, and anyone who could
    do basic integration was called a data engineer. Now, the field is becoming more
    specialized.
  sec: 663
  time: '11:03'
  who: Adrian
- line: We’re seeing data engineers focus on areas like data governance, data quality,
    and streaming. These specializations often have little overlap, driven by industry
    requirements like handling sensitive data or new use cases like energy management.
  sec: 663
  time: '11:03'
  who: Adrian
- line: For junior data engineers, is it harder to enter the field now?
  sec: 737
  time: '12:17'
  who: Alexey
- header: 'Early-career opportunities: AI projects and startup hiring'
- line: It depends. There’s still opportunity, especially in AI. Many companies are
    exploring AI and need data engineers to support those efforts. Startups also need
    help building modern data stacks, which has become easier with tools like DLT.
  sec: 757
  time: '12:37'
  who: Adrian
- line: You mentioned the modern data stack. How modern is it, and what does it entail?
  sec: 848
  time: '14:08'
  who: Alexey
- header: Modern data stack critique and open-source "postmodern" alternatives
- line: The modern data stack is largely marketing. It’s a package of software from
    various vendors that you can combine to build a data platform.
  sec: 872
  time: '14:32'
  who: Adrian
- line: For example, Fivetran with Snowflake and Looker. Vendors needed a way to sell
    together, and the modern data stack concept was born. It’s effective marketing,
    but not necessarily modern.
  sec: 872
  time: '14:32'
  who: Adrian
- line: Now, people are talking about the postmodern data stack, which uses open-source
    technologies to achieve better efficiency and lower costs.
  sec: 872
  time: '14:32'
  who: Adrian
- line: Fivetran, Snowflake, and Looker aren’t open source, right?
  sec: 956
  time: '15:56'
  who: Alexey
- line: Correct, but you can build similar stacks with open-source tools.
  sec: 964
  time: '16:04'
  who: Adrian
- line: What trends do you think we’ll see more of in 2025 and beyond?
  sec: 975
  time: '16:15'
  who: Alexey
- header: '2025 trends: AI integration in data engineering and Apache Iceberg adoption'
- line: AI will continue to grow, with more complex use cases and fewer hallucinations.
    AI is entering the data engineering space, with data engineers building AI agents.
  sec: 1000
  time: '16:40'
  who: Adrian
- line: Another trend is Apache Iceberg. It’s moving from hype to production deployments,
    especially with Pythonic implementations.
  sec: 1000
  time: '16:40'
  who: Adrian
- line: Can you explain what Apache Iceberg is?
  sec: 1088
  time: '18:08'
  who: Alexey
- header: 'Apache Iceberg explained: table format, Parquet storage, vendor lock-in
    reduction'
- line: Iceberg is a table format that simulates the storage layer of a SQL database.
    It’s a way of storing data independently of databases, allowing updates without
    rewriting entire files.
  sec: 1097
  time: '18:17'
  who: Adrian
- line: So it’s a bunch of Parquet files on S3 with metadata?
  sec: 1143
  time: '19:03'
  who: Alexey
- line: Yes, it’s similar to Delta and Hudi. The industry is excited because it breaks
    vendor lock-in, but vendors are still trying to capture value through catalogs.
  sec: 1151
  time: '19:11'
  who: Adrian
- line: 'You mentioned databases have four layers: storage, compute, access, and metadata.
    Can you clarify what a catalog is?'
  sec: 1270
  time: '21:10'
  who: Alexey
- header: 'Database layers and catalog role: storage, compute, access, metadata &
    lineage'
- line: A catalog maps data to compute and manages access control. Some catalogs also
    handle metadata, like lineage, which helps track data usage.
  sec: 1287
  time: '21:27'
  who: Adrian
- line: What tools are used for catalogs?
  sec: 1416
  time: '23:36'
  who: Alexey
- header: Metadata and catalog tooling overview (AWS Glue and peers)
- line: I don’t recall all the names, but tools like AWS Glue Catalog are examples.
  sec: 1421
  time: '23:41'
  who: Adrian
- line: What about DuckDB? Will we see more “on-laptop” data warehouses?
  sec: 1427
  time: '23:47'
  who: Alexey
- header: 'DuckDB impact: embeddable local OLAP and portable query engine'
- line: DuckDB is amazing and a key technology for us. It’s embeddable, meaning you
    can use it as a building block in your own product.
  sec: 1558
  time: '25:58'
  who: Adrian
- line: We use DuckDB in DLT to query data through a universal interface, whether
    it’s a file system, data lake, or SQL database.
  sec: 1558
  time: '25:58'
  who: Adrian
- line: Is DuckDB changing how we do data engineering?
  sec: 1652
  time: '27:32'
  who: Alexey
- header: 'Cost-efficient pipelines: DuckDB with GitHub Actions and headless table
    formats'
- line: Absolutely. People are challenging the high costs of vendor solutions. I’ve
    seen setups using DuckDB and GitHub Actions to run entire data stacks for cents
    per month.
  sec: 1660
  time: '27:40'
  who: Adrian
- line: So DuckDB allows us to process data locally and save results back to storage?
  sec: 1703
  time: '28:23'
  who: Alexey
- line: Yes, and because it’s portable, you can take advantage of cheaper compute
    options like GitHub Actions.
  sec: 1724
  time: '28:44'
  who: Adrian
- line: Is DuckDB related to headless table formats?
  sec: 1766
  time: '29:26'
  who: Alexey
- line: Yes, DuckDB provides a local access layer, which is useful for data pipelines.
  sec: 1773
  time: '29:33'
  who: Adrian
- line: You mentioned headless table formats with DLT. Is that where you’re heading?
  sec: 1818
  time: '30:18'
  who: Alexey
- header: Headless table formats and DLT support for Delta Lake and Iceberg
- line: Yes, we’re already serving headless Delta Lake and working on similar solutions
    for Iceberg.
  sec: 1831
  time: '30:31'
  who: Adrian
- line: Instead of processing everything in Snowflake and paying a fortune.
  sec: 1883
  time: '31:23'
  who: Alexey
- line: Exactly.
  sec: 1888
  time: '31:28'
  who: Adrian
- header: dbt's influence on engineering workflows and alternatives like SQLMesh
- line: How did dbt change data engineering?
  sec: 1889
  time: '31:29'
  who: Alexey
- line: dbt changed how people think about data engineering. It eliminated boilerplate
    code and improved project quality.
  sec: 1972
  time: '32:52'
  who: Adrian
- line: What about alternatives like SQLMesh?
  sec: 2048
  time: '34:08'
  who: Alexey
- line: Competition is healthy. dbt was first, but tools like SQLMesh are doubling
    down on what dbt core offered.
  sec: 2054
  time: '34:14'
  who: Adrian
- line: What about workflow orchestration? What should we use in 2025?
  sec: 2121
  time: '35:21'
  who: Alexey
- header: 'Workflow orchestration options in 2025: Airflow, Prefect, Dagster, GitHub
    Actions'
- line: It depends on your team. Airflow is a common choice, but tools like Prefect
    and Dagster are also popular. We often use GitHub Actions for its cost efficiency.
  sec: 2137
  time: '35:37'
  who: Adrian
- line: For simple workflows, GitHub Actions is sufficient?
  sec: 2220
  time: '37:00'
  who: Alexey
- line: Yes, it’s serverless and much cheaper than always-on orchestrators.
  sec: 2228
  time: '37:08'
  who: Adrian
- line: Let’s move to audience questions.
  sec: 2241
  time: '37:21'
  who: Alexey
- line: For someone pursuing multiple disciplines like data engineering, data science,
    and AI engineering, I recommend focusing on one area first.
  sec: 2258
  time: '37:38'
  who: Adrian
- header: 'AI engineering convergence: data engineers building AI agents'
- line: AI engineering often overlaps with data engineering, especially when building
    systems like chatbots.
  sec: 2282
  time: '38:02'
  who: Alexey
- line: AI requires data, algorithms, and semantics. Data engineers will play a key
    role in building AI agents.
  sec: 2318
  time: '38:38'
  who: Adrian
- line: With so many tools in data engineering, how should beginners choose what to
    learn?
  sec: 2413
  time: '40:13'
  who: Alexey
- header: 'Beginner roadmap: SQL, Python, capturing business requirements, building
    a portfolio'
- line: Focus on understanding the concepts and solving problems. Tools are secondary.
    Learn SQL, Python, and how to capture business requirements.
  sec: 2466
  time: '41:06'
  who: Adrian
- line: For building a portfolio, is it okay to pick any tool for each component?
  sec: 2583
  time: '43:03'
  who: Alexey
- line: Yes, but consider the end user. Tools like notebooks or dashboards should
    align with how your audience interacts with data.
  sec: 2608
  time: '43:28'
  who: Adrian
- line: So, try things and see what works.
  sec: 2678
  time: '44:38'
  who: Alexey
- header: Tool selection guidance and vendor caution for modern data stacks
- line: Exactly. The modern data stack is interchangeable, but be cautious of vendors
    with questionable practices.
  sec: 2682
  time: '44:42'
  who: Adrian
- line: How challenging is it for a senior backend engineer to transition into data
    engineering?
  sec: 2711
  time: '45:11'
  who: Alexey
- header: 'Transition paths: senior backend engineers moving into data engineering'
- line: It’s relatively easy. The main gap is understanding the business case and
    requirements.
  sec: 2756
  time: '45:56'
  who: Adrian
- line: So, a senior backend engineer can transition into a senior data engineering
    role.
  sec: 2824
  time: '47:04'
  who: Alexey
- line: Yes, unless they’re aiming for something highly specialized.
  sec: 2837
  time: '47:17'
  who: Adrian
- line: If you want to position yourself as a Spark expert, it might take time, but
    solving data problems is more about engineering skills.
  sec: 2852
  time: '47:32'
  who: Alexey
- line: If you’re a junior claiming to be a Spark expert, I’d be skeptical.
  sec: 2865
  time: '47:45'
  who: Adrian
- header: 'Job market outlook: senior vs junior data engineering opportunities'
- line: What’s the job market like for data engineers?
  sec: 2884
  time: '48:04'
  who: Alexey
- line: For seniors, there’s no shortage of jobs. Juniors might need to explore related
    roles like BI or data science to get started.
  sec: 2884
  time: '48:04'
  who: Adrian
- line: What are Delta and Hudi?
  sec: 2940
  time: '49:00'
  who: Alexey
- header: 'Table format comparisons: Delta, Hudi, and Iceberg differences'
- line: They’re similar to Iceberg but differ in design and optimization. Delta is
    the most mature, while Hudi is more specialized.
  sec: 2982
  time: '49:42'
  who: Adrian
- line: Are these formats suitable for streaming
  sec: 3040
  time: '50:40'
  who: Alexey
- header: 'Streaming architectures and tools: micro-batching, Kafka, SQS, Flink'
- line: Yes, but streaming is often just micro-batching unless you have strict SLAs.
  sec: 3079
  time: '51:19'
  who: Adrian
- line: What tools are used for streaming?
  sec: 3151
  time: '52:31'
  who: Alexey
- line: Kafka and SQS are common buffers. Downstream, tools like Flink or DuckDB can
    process the data.
  sec: 3151
  time: '52:31'
  who: Adrian
- line: Will data engineering be automated by AI?
  sec: 3243
  time: '54:03'
  who: Alexey
- header: AI-driven commoditization and code generation in data engineering
- line: AI is speeding up commoditization, making it easier to generate code. Data
    engineers will specialize further and build AI agents.
  sec: 3375
  time: '56:15'
  who: Adrian
- line: What’s the future of DLT?
  sec: 3500
  time: '58:20'
  who: Alexey
- header: 'DLT roadmap: DLT Plus and a marketplace for reusable data products'
- line: In one year, we’re focusing on DLT Plus, a portable data platform. In five
    years, we aim to create a marketplace for data products, enabling reuse across
    organizations.
  sec: 3582
  time: '59:42'
  who: Adrian
- header: Episode wrap-up and key takeaways
- line: It’s been great talking to you, Adrian. Thanks for sharing your insights.
  sec: 3679
  time: '1:01:19'
  who: Alexey
- line: Thanks, Alexey. See you later.
  sec: 3735
  time: '1:02:15'
  who: Adrian
- line: Goodbye, everyone.
  sec: 3737
  time: '1:02:17'
  who: Alexey
description: Discover Apache Iceberg, DuckDB & AI-powered pipelines - learn cost-efficient
  table formats, orchestration tactics and a career roadmap for data engineers.
intro: How do you future‑proof data engineering against vendor lock‑in, rising AI
  demand, and exploding metadata complexity? In this episode, Adrian Brudaru — a former
  business analyst turned freelancer and co‑founder of DLT — walks through practical
  choices for building resilient, cost‑efficient pipelines. Adrian explains DLT as
  a Python‑based ingestion standard, the DLT Plus vision and marketplace for reusable
  data products, and why the industry is shifting toward specialization in governance,
  data quality, and streaming. <br><br> Key topics include adopting Apache Iceberg
  as a table format (Parquet storage and reduced vendor lock‑in), the role of data
  catalogs and metadata tooling (AWS Glue and peers), and how DuckDB enables embeddable
  local OLAP and portable query execution. We cover cost‑efficient patterns—DuckDB
  with GitHub Actions and headless table formats—dbt’s influence and alternatives
  like SQLMesh, orchestration choices (Airflow, Prefect, Dagster, GitHub Actions),
  and the 2025 trend of AI integration in pipelines and AI agents. Listeners will
  get actionable guidance on tool selection, beginner and transition roadmaps, and
  when Iceberg, DuckDB, or AI‑powered approaches make sense for their data engineering
  stack.
dateadded: '2025-03-14'
duration: PT01H02M16S
quotableClips:
- name: Episode opening & guest introduction
  startOffset: 1
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1
  endOffset: 143
- name: Perspective on evolving data engineering challenges
  startOffset: 143
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=143
  endOffset: 190
- name: 'Career journey: startups, freelancing, founding DLT'
  startOffset: 190
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=190
  endOffset: 243
- name: DLT as a Python-based ingestion standard and market impact
  startOffset: 243
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=243
  endOffset: 465
- name: DLT Plus vision and partnership outreach for freelancers
  startOffset: 465
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=465
  endOffset: 663
- name: 'Industry shift toward specialization: governance, data quality, streaming'
  startOffset: 663
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=663
  endOffset: 757
- name: 'Early-career opportunities: AI projects and startup hiring'
  startOffset: 757
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=757
  endOffset: 872
- name: Modern data stack critique and open-source "postmodern" alternatives
  startOffset: 872
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=872
  endOffset: 1000
- name: '2025 trends: AI integration in data engineering and Apache Iceberg adoption'
  startOffset: 1000
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1000
  endOffset: 1097
- name: 'Apache Iceberg explained: table format, Parquet storage, vendor lock-in reduction'
  startOffset: 1097
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1097
  endOffset: 1287
- name: 'Database layers and catalog role: storage, compute, access, metadata & lineage'
  startOffset: 1287
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1287
  endOffset: 1421
- name: Metadata and catalog tooling overview (AWS Glue and peers)
  startOffset: 1421
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1421
  endOffset: 1558
- name: 'DuckDB impact: embeddable local OLAP and portable query engine'
  startOffset: 1558
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1558
  endOffset: 1660
- name: 'Cost-efficient pipelines: DuckDB with GitHub Actions and headless table formats'
  startOffset: 1660
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1660
  endOffset: 1831
- name: Headless table formats and DLT support for Delta Lake and Iceberg
  startOffset: 1831
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1831
  endOffset: 1889
- name: dbt's influence on engineering workflows and alternatives like SQLMesh
  startOffset: 1889
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=1889
  endOffset: 2137
- name: 'Workflow orchestration options in 2025: Airflow, Prefect, Dagster, GitHub
    Actions'
  startOffset: 2137
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2137
  endOffset: 2282
- name: 'AI engineering convergence: data engineers building AI agents'
  startOffset: 2282
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2282
  endOffset: 2466
- name: 'Beginner roadmap: SQL, Python, capturing business requirements, building
    a portfolio'
  startOffset: 2466
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2466
  endOffset: 2682
- name: Tool selection guidance and vendor caution for modern data stacks
  startOffset: 2682
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2682
  endOffset: 2756
- name: 'Transition paths: senior backend engineers moving into data engineering'
  startOffset: 2756
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2756
  endOffset: 2884
- name: 'Job market outlook: senior vs junior data engineering opportunities'
  startOffset: 2884
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2884
  endOffset: 2982
- name: 'Table format comparisons: Delta, Hudi, and Iceberg differences'
  startOffset: 2982
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=2982
  endOffset: 3079
- name: 'Streaming architectures and tools: micro-batching, Kafka, SQS, Flink'
  startOffset: 3079
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=3079
  endOffset: 3375
- name: AI-driven commoditization and code generation in data engineering
  startOffset: 3375
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=3375
  endOffset: 3582
- name: 'DLT roadmap: DLT Plus and a marketplace for reusable data products'
  startOffset: 3582
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=3582
  endOffset: 3679
- name: Episode wrap-up and key takeaways
  startOffset: 3679
  url: https://www.youtube.com/watch?v=AlCFKbFIEM8&t=3679
  endOffset: 3736
---

Links:

* [Linkedin](https://www.linkedin.com/in/data-team/){:target="_blank"}
* [Website](https://adrian.brudaru.com/){:target="_blank"}