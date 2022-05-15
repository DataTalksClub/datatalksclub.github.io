---
title: "Effective Data Science Infrastructure"
description: "Book of the Week. Effective Data Science Infrastructure by Ville Tuulos"
cover: "images/books/20210927-effective-data-science-infrastructure/cover.jpg"
image: "images/books/20210927-effective-data-science-infrastructure/preview.jpg"
start: 2021-09-27 00:00:00
end: 2021-10-01 22:59:58
authors: [villetuulos]
links: 
  - text: Book's page
    link: https://www.manning.com/books/effective-data-science-infrastructure
  - text: Book's GitHub repository
    link: https://github.com/outerbounds/dsbook

archive:
- name: Alper Demirel
  text: 'Hi Ville Tuulos, thank you for being with us.

    In order to be successful in a data science project, the infrastructure we need
    to set up must have the basic features?'
  replies:
  - name: Ville Tuulos
    text: "great question! Answering the question is exactly the topic of the book\
      \ \U0001F642\n\"Must\" is a strong word since every company (or even every project)\
      \ has different needs. The most common infrastructure layers are:\n- Integrations\
      \ to the surrounding *data infrastructure* - practically all projects need to\
      \ ingest data.\n- A *compute layer* that allows you to train models and process\
      \ data at scale.\n- A *workflow orchestrator* allowing you to run workflows\
      \ in production reliably.\n- A *versioning* system that allows you to version\
      \ not only code, but also models, experiments, and maybe keep track of data\
      \ lineage too.\nFor prototyping, I am a fan of cloud-based workstations but\
      \ technically a laptop/desktop will work too. You probably want to run notebooks\
      \ on the workstation too.\nDepending on the needs of your project, you may need\
      \ other components like a model hosting solution, specific support for feature\
      \ engineering, or a distributed training system for DNNs. I think it is a good\
      \ idea to start first with the foundational layers in any case."
- name: "Laura Uzc\xE1tegui"
  text: "Hi \U0001F44B, \nWill put my questions on this thread. \n1. Is metaflow restricted\
    \ to be used only with aws? Or does it have integration with other cloud providers?"
  replies:
  - name: "Laura Uzc\xE1tegui"
    text: 2. Until what point of having great performance and scalability is recommend
      it? Is there any trade-off or use case where you will say metaflow should not
      be used?
  - name: "Laura Uzc\xE1tegui"
    text: "3. I have worked previously in ML Platform team, it was fun. \nOur infra/platform\
      \ was based on collecting data across different services, serialised with avro\
      \ and encrypt payloads to be send to Kafka. \nUsing Apache Flink, we will consume\
      \ from Kafka, un-encrypt, do aggregations and send it to an encrypted blob store\
      \ , so that ML Engineers could take it and use it for building models. \n  \n\
      Questions: \n- I have always thought about , if the blob store would make sense\
      \ in case of big amounts of data, is this something could be done differently?\
      \ \n- How would you handle the trade off of having to do encryption of your\
      \ data and reading it fast because you need to handle SLAs with respect to time\
      \ to response and the overload of encryption itself?"
  - name: Ville Tuulos
    text: 1. Coming soon! Metaflow will start supporting Kubernetes in a few weeks,
      which allow you to deploy it to other clouds (we tested it with Azure). We are
      actively working on to support e.g. Azure Object Storage natively.
  - name: Ville Tuulos
    text: Could you rephrase your question about performance? I am not sure if I got
      it
  - name: Ville Tuulos
    text: '2. Re: when not Metaflow. Here are some good reasons for not using it:

      - You use primarily JVM-based languages. Metaflow works well with Python, R,
      and extensions written in C/C++. There''s probably too much friction if you
      want to use it with Java/Scala/Clojure.

      - Your use cases are all based on streaming data. Metaflow is quite batch-centric
      as of today. If you need *only* online learning and low-latency data, Metaflow
      isn''t the right tool. However, Metaflow can work with with e.g. real-time predictions
      and streaming data with batch training, which is a common use case e.g. at Netflix.

      - You have one specific use case that has very specific requirements, e.g. running
      ML on an embedded device. It is probably better to create a custom solution
      in that case.'
  - name: Ville Tuulos
    text: "The list is not exhaustive \U0001F642"
  - name: Ville Tuulos
    text: '3. Using a blob store could work well in a scenario you described. Netflix
      uses Kafka and Flink to populate data in S3 (a blob store) very actively. You
      may want to take a look at [Apache Iceberg](https://iceberg.apache.org/) as
      a convenient metadata format which works with Spark and Presto/Trino for such
      use cases.

      There are very high-throughput encrypting libraries available these days, so
      I doubt it would become a major bottleneck. The upcoming chapter 7 in the book
      will talk about high-performance data loading, so you can read it for inspiration.'
  - name: "Laura Uzc\xE1tegui"
    text: "Thanks Ville! \nReally good points there, previous team was using scala/java\
      \ for the streaming part and orchestration with golang, as you said , for this\
      \ use in particular it wouldn't work. \nLooking forward to read and learn from\
      \ you as author of the book \U0001F64C"
- name: Dr Abdulrahman Baqais
  text: "Hi  Ville. Thank you for writing this most needed book. Few questions as\
    \ I am going to set up a new DS team:\n1) for a new DS lead, What are the skills\
    \ needed in order for someone to design a good data science process or workflow\
    \ if they can not use metaflow?  \n2) Can technical people : senior data scientists\
    \ set up the process or it is better to be assigned to people with strategic mindset\
    \ and process-oriented?\n3)  is CRISP still relevant and useful for data science\
    \ projects?\n4) Is this workflow applicable to deep learning as well?\n5) Is there\
    \ a checklist or a guidelines to know when Netflix metaflow is suitable to my\
    \ team or not?\n\nThank you so much\U0001F64F \U0001F64F \U0001F64F :thank_you:"
  replies:
  - name: Ville Tuulos
    text: '`1)` The book advocates for a spiral approach like this, which is applicable
      to all projects whether to use Metaflow or not:

      1. Start with a business problem - what do you need to deliver to make a positive
      impact in the business.

      2. Do you have data that can be used to reach the desired outcome? Often the
      answer is "no" or "not quite", in which case it makes sense to see how to improve
      the data situation first.

      3. Assuming the data is there, how do you integrate the results to the surrounding
      business systems and processes, including human workflows, to achieve the desired
      impact? This is often a really deep question that requires lots of alignment
      and product management-type work.

      4. Finally when you have a good grasp of the 1-2-3, start thinking about the
      modeling approach and how to build a process that allows data scientists to
      continuously improve the model. You can start with something super simple -
      [the first version doesn''t even have to use ML](https://eugeneyan.com/writing/first-rule-of-ml/).

      Since you asked about skills, as a DS lead I''d prioritize my work and learning
      process in the order specified above, 1-2-3-4. Often the instinct is to focus
      on 4) - the modeling - but it is hard to even choose the best approach without
      knowing the problem domain well.'
  - name: Ville Tuulos
    text: '`2)` I think it would be great if data scientists can at least help to
      define the process, naturally in collaboration with business stakeholders etc.'
  - name: Ville Tuulos
    text: '`3)` I assume you mean this [CRISP](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining).
      It is really close to the spiral model above, but it seems a bit waterfall-like:
      Understand-&gt;Model-&gt;Deploy, which puts too much emphasis on a static deliverable.
      Coming up with a process that allows you to iterate on models quickly is more
      important than any single model.

      Providing the building blocks for such a process is the reason why you need
      Effective Data Science Infrastructure in the first place.'
  - name: Ville Tuulos
    text: '`4)` yeah, DNNs are just models like any other models. I don''t think they
      change anything about the process, besides maybe putting even more emphasis
      on scalable data and compute layers.'
  - name: Ville Tuulos
    text: '`5)` You can find [a non-technical checklist in the documentation](https://docs.metaflow.org/introduction/what-is-metaflow#should-i-use-metaflow).
      Whether it works well in your technical environment is a more nuanced question.
      I''m happy to follow up here if you want to know more technical details.'
  - name: Ville Tuulos
    text: "great questions, btw! \U0001F917"
- name: Timur Kamaliev
  text: 'Hi Ville Tuulos and thank you for being here.

    I think my questions may be closer to the development. I usually notice that the
    position of an ML engineer often requires C++ background. But there are almost
    no mentions of Golang. It''s ok, if we deal with CV (and CUDA is here) or with
    some embedded system. But what about classic ML area? From my point of view, it''s
    quite strange, especially for all the relative advantages and comparable performance
    of Go in comparision with C++. All the experienced SW engineers I know, who are
    dealing with highload in production, switched on to the Go for 3-4 years ago.
    Do you think that it concerned with some infrastructure restrictions? Or DS/ML
    area is a couple of steps behind?'
  replies:
  - name: Ville Tuulos
    text: "I think Go is a great language but it has weaknesses when it comes to ML/DS\
      \ use cases. It makes sense to implement low-level computational kernels in\
      \ C or C++, since you want to control memory carefully and optimizing the last\
      \ bit of performance matters. Due to its design, Go has exceptionally high overhead\
      \ when calling C/C++ libraries ([the infamous CGo overhead](https://www.cockroachlabs.com/blog/the-cost-and-complexity-of-cgo/)),\
      \ so it is actually harder to use Go with ML libraries than, say, Python. This\
      \ issue applies equally to classic ML (think XGBoost or LibSVM) as it does to\
      \ DNN.\nIn the future, there's likely going to be a relatively small number\
      \ of engineers building low-level libraries who will need to use C/C++ for performance\
      \ reasons. In contrast, the vast majority of ML engineers and data scientists\
      \ can use a high-level language like Python that delegates all heavy lifting\
      \ to a low-level library like Tensorflow.\nWhile Go is a superb language for\
      \ systems software, I am not sure where it lands in the DS landscape: It is\
      \ too slow for computational kernels and too low-level and hard-to-integrate-with\
      \ for high-level work \U0001F914"
- name: Timur Kamaliev
  text: 'My second question also about development. Let''s suppose that our ML service
    was developed on FastAPI/Flask and packed into a docker. And one day we faced
    with a performance problem in production due to an increased load. Assume that
    we have already done all the tricks with code optimization and so on, and now
    it''s time to make more serious steps. We have two ways:

    - to configure the required number of docker containers and additionally write
    a special load balancer that will interact with these containers;

    - or just take and rewrite the entire project in C++ (or another faster language).

    So, which option would be more preferable in terms of infrastructure and costs?
    :thank_you:'
  replies:
  - name: Ville Tuulos
    text: "Here's how I understand your problem as a hierarchy of three levels:\n\
      ```[ Microservice (Flask)\n    [ Query endpoint\n         [ ML Model ]\n   \
      \ ]\n]```\nWhat's causing the slowness?\n1. ML Model -&gt; Producing inferences\
      \ take too long, so it is a model architecture problem. If the model is e.g.\
      \ a DNN model, you can use a project like [Apache TVM/OctoML](https://octoml.ai/)\
      \ to try to optimize it.\n2. Query endpoint -&gt; Since you are using Flask,\
      \ I presume you are using Python. Maybe you are doing some non-trivial preprocessing\
      \ of data in Python that's slow. You might be able to refactor the code to be\
      \ much faster (see the upcoming Chapter 5 in the book!) but in some cases it\
      \ can get tricky, which might be a reason to consider another language.\n3.\
      \ Microservice -&gt; Scaling microservices to handle an arbitrary queries-per-second\
      \ is a common problem which is not specific to ML. Maybe you can use existing\
      \ techniques to make it more scalable.\nChapter 5 also talks about the difference\
      \ between scalability and performance. In this case, levels 1 and 2 might have\
      \ performance issues and level 3 a scalability issue. Often it is easier to\
      \ solve a scalability problem (just add more machines!) than it is to solve\
      \ a performance problem (reimplement everything in C++), so I tend to bias towards\
      \ solving the former, if possible."
  - name: Timur Kamaliev
    text: "Ville Tuulos Thanks for your detailed answers \U0001F44D"
- name: Prasad Paravatha
  text: 'Hi Ville Tuulos, my question is about different Distributed training options
    successfully implemented.

    To be more specific what are our options for Distributed training on Kubernetes
    vs Distributed training on non-Kubernetes?'
  replies:
  - name: Ville Tuulos
    text: "interesting question. It would be useful to understand what type of distributed\
      \ training you have in mind: Do you want to train a huge model that is too big\
      \ for any single machine to handle (model parallelism) or do you want to train\
      \ a medium-size model that fits on a single box using a huge amount of data\
      \ (data parallelism)? Or do you want to train many independent models e.g. with\
      \ different parametrizations? There are different solutions for each use case.\n\
      For the non-Kubernetes case, you could look into a solution like [Sagemaker's\
      \ Distributed Training service](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html).\
      \ For K8S, [Determined.ai](https://www.determined.ai/blog/determined-on-kubernetes)[\
      \ is one option](https://www.determined.ai/blog/determined-on-kubernetes)  (it\
      \ [works nicely with Metaflow](https://www.determined.ai/blog/metaflow-determined-integration)\
      \ too). Or you could roll-out your own solution using e.g. [Horovod](https://www.google.com/search?q=horovod+github&amp;rlz=1C5CHFA_enUS921US921&amp;oq=horovod&amp;aqs=chrome.3.69i57j0i20i263i512l2j0i512l7.2851j0j7&amp;sourceid=chrome&amp;ie=UTF-8).\n\
      We are actively working on distributed training and K8S use cases - it is definitely\
      \ a non-trivial problem, so happy to share more details if you are interested\
      \ \U0001F642"
- name: Prasad Paravatha
  text: 'Hi Ville Tuulos My 2nd question: Python and R are very popular in Data science
    and Machine Learning community

    In your experience, What are some other programming languages which have potential
    to be suitable for DS/ML?'
  replies:
  - name: Ville Tuulos
    text: 'When choosing a programming language for DS/ML, I''d consider

      1. Existing library ecosystem. Unless you are in academia, you probably don''t
      want to implement modeling libraries from scratch.

      2. Low-overhead interfacing with C/C++ libraries (more details in this thread
      [https://datatalks-club.slack.com/archives/C01H403LKG8/p1632733036461900](https://datatalks-club.slack.com/archives/C01H403LKG8/p1632733036461900))

      3. Expressive, supports rapid iterations, and can handle even complex, messy
      business logic.

      Obviously Python and R score really well on all the points, 1, 2, and 3. Julia
      is promising but its library ecosystem is still behind Python and R. JVM-based
      languages have a problem at least with 2, these days with 1 too. There are less
      mainstream languages that support 2 and 3 really well ([D](https://tech.nextroll.com/blog/data/2014/11/17/d-is-for-data-science.html),
      [Nim](https://benjamindlee.com/posts/2021/why-i-use-nim-instead-of-python-for-data-processing/)
      etc) but they are sorely lacking on 1.'
- name: Yasser
  text: 'Hello Ville Tuulos. Thank you for writing this great book. I have a question:
    What fundamentals and How much can I take for starting a data science infrastructure
    career ?'
  replies:
  - name: Ville Tuulos
    text: "thanks \U0001F647\nYou could approach a career in DS infra from different\
      \ angles, depending on your personal interests and background. This may count\
      \ as <#C01F53D373M|shameless-promotion> but I can answer your question in terms\
      \ of the four \"roles\" we have open at [my DS infra company](https://outerbounds.co/workwithus)\
      \ (feel free to apply \U0001F61B) :\n- *Systems engineer angle*: Learn about\
      \ Computer Science, operating systems, distributed systems etc. The CS fundamentals\
      \ are very useful when building infrastructure for ML/AI.\n- *Cloud angle*:\
      \ I believe that a vast majority of ML/AI workloads will be run in the cloud\
      \ (as they already are). Systems like AWS are huge and complex enough that you\
      \ could just focus on learning about VPCs, Placement Groups, Spot Instances,\
      \ Auto-Scaling Groups, CI/CD systems, and various higher-level services - not\
      \ to mention Kubernetes. Infra companies will be competing fiercely to hire\
      \ you with this skillset.\n- *Product design angle*: I also believe that the\
      \ more our field advances, the more people will matter over machines. Often,\
      \ optimizing the productivity of data scientists is more valuable than optimizing\
      \ the performance of a piece of code. There's a hugely important emerging field\
      \ of [ML User Experience](https://www.meetup.com/MLUXmeetup/) and [UX of ML\
      \ tools themselves](https://future.a16z.com/the-case-for-developer-experience/).\n\
      - *AI/ML angle*: Getting exposed to various ML/AI problems in the real-life\
      \ is the best way to understand pain points that infrastructure needs to solve.\
      \ Knowing libraries like PyTorch or even Pandas inside-out allows you to understand\
      \ how to improve them, or maybe build better libraries altogether. [Many people\
      \ in this field](https://www.youtube.com/watch?v=gFEE3w7F0ww) are here to scratch\
      \ their own itch."
  - name: Yasser
    text: "Thanks a lot for your helpful detailed answer \U0001F64F"
- name: Alexey Grigorev
  text: What do you think of data versioning? Is it always worth the troubles?
  replies:
  - name: Ville Tuulos
    text: 'while it is a good idea, as long as commonly used data warehouses don''t
      support versioning as the first-class citizen, it is hard to claim that it is
      _always_ a good idea. It takes effort to implement it today.

      While snapshotting bulk input data can be tedious, snapshotting and versioning
      smaller data like the internal state of workflows and especially metadata and
      metrics is _a really good idea_ and not too hard, which is why Metaflow does
      it out of the box.'
  - name: Ville Tuulos
    text: here's an exploration of what a full data versioning solution could look
      like [https://www.dolthub.com/blog/2021-04-12-metaflow-dolt-integration/](https://www.dolthub.com/blog/2021-04-12-metaflow-dolt-integration/)
- name: Alexey Grigorev
  text: Also curious, did you have cases when you wished you had it, but you didn't?
  replies:
  - name: Ville Tuulos
    text: "all the time \U0001F642 For instance, Netflix has [a custom-built Fact\
      \ Store](https://databricks.com/session/fact-store-scale-for-netflix-recommendations)\
      \ (aka a versioned datastore) for data points feeding into the recommendation\
      \ system. However, it only supports that one use case well.\nIt would be great\
      \ to have a similar solution for all use cases but building a universal fact\
      \ store is hard, so even Netflix doesn't have it. I am optimistic that it will\
      \ become a default feature in all [modern data warehouses](https://docs.snowflake.com/en/user-guide/data-time-travel.html)\
      \ eventually, since cloud storage is so cheap."
  - name: Ville Tuulos
    text: at small scale you can use tools like [dvc.org](http://dvc.org) and [pachyderm.com](http://pachyderm.com)
      but a challenge to any larger company is that your whole data infrastructure
      and governance policies should work well with versioned data, so it is hard
      to adopt point solutions
- name: WingCode
  text: 'Hi Ville Tuulos,

    For an organisation starting to build their ML infrastructure, do you suggest
    adopting cutting edge tools from the start (ex: Kubernetes for training, inference)  or
    adopt simpler tools (ex: Using airflow to schedule jobs in spark on YARN) then
    gradually move onto adopting cutting edge tools?'
  replies:
  - name: Ville Tuulos
    text: 'there are of course many things to consider - what are the needs of the
      business / environment overall - but in general I''d recommend starting with
      managed systems, so you can maximize the time spent on ML and minimize the time
      spent on infrastructure.

      This is the reason why Metaflow integrates with AWS Batch today, which is probably
      the easiest way to run compute in the cloud with minimal maintenance headache.
      For orchestration, AWS Step Functions plays a similar role. They provide a managed
      Airflow these days too.'
  - name: Ville Tuulos
    text: 'The main reason why things like Kubeflow exists, and why Metaflow is integrating
      with Kubernetes too, is that businesses have other, non-ML reasons to use Kubernetes
      and it is certainly convenient to use a single system that engineers know how
      to operate, instead of having a wholly separate underlying compute layer for
      ML.

      In general there''s a lot of value in making sure that the ML platform integrates
      well with the surrounding infrastructure. If your ML projects live inside a
      walled garden, it can make it hard to access data from the outside world effectively
      and deploy ML to benefit the rest of the business.

      Even if the business runs on Kubernetes, [I don''t think it should be necessary
      for data scientists to know Kubernetes (to quote Chip Huyen)](https://huyenchip.com/2021/09/13/data-science-infrastructure.html).
      It is more of an implementation detail.'
  - name: WingCode
    text: "Thank you Ville for the answer \U0001F642"
- name: Krzysztof Ograbek
  text: 'Hi Ville Tuulos. Thanks for being here!

    A couple of weeks ago I deployed an ML model for the first time ever. I used Heroku.
    Are there any other platforms for deploying that are free and available? When
    does it make sense to pay for such platforms?'
  replies:
  - name: Ville Tuulos
    text: "congrats for your first deployment! \U0001F389\nIf you are testing and\
      \ tinkering, you could take a look at [https://replit.com/site/hosting](https://replit.com/site/hosting)\
      \ which is possibly even a simpler approach than Heroku."
  - name: Ville Tuulos
    text: for more serious use cases you can consider [https://cloud.google.com/appengine](https://cloud.google.com/appengine)
  - name: Ville Tuulos
    text: 'unless you deploy complex deep neural networks that require e.g. GPUs for
      inference, you probably don''t need a dedicated ML hosting solution.

      If you are curious what an ML-specific solution could look like, you can see
      e.g. [https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html)'
  - name: Ville Tuulos
    text: non-ML specific hosting solutions tend to be quite cheap, so paying maybe
      $10/month just for the convenience of someone managing it for you seems like
      a good deal.
  - name: Ville Tuulos
    text: "I wouldn't pay a lot of money unless the model produces a lot of money\
      \ \U0001F642"
  - name: Krzysztof Ograbek
    text: Wow, thank you so much Ville Tuulos You wrote way more than I expected
- name: Wendy Mak
  text: Hi Ville Tuulos what are your opinions on using a platform independent tool
    such as Metaflow/MLFlow  vs what the cloud providers already has (e.g. Vertex
    pipelines), assuming costs is not the deal breaker?
  replies:
  - name: Ville Tuulos
    text: 'great question! I like the idea of being able to use ML tools provided
      by the cloud. However, for the past many years these cloud-tools have been quite
      hard to use and constraining, which has motivated the development of systems
      like Metaflow, MLFlow and many others.

      In other words, assuming that cost wasn''t an issue and the cloud tools provided
      an excellent user experience, using them seems like a good idea. Now, in reality,
      it seems that many companies find that either one or both of these assumptions
      not holding well.'
  - name: Ville Tuulos
    text: 'a nice thing is that it should be quite easy to evaluate them: Try implementing
      a real-world ML project (not just a tutorial) on the platform and see how it
      feels. If the platform works well for your needs and it integrates well with
      the surrounding business environment, that''s great!'
  - name: Ville Tuulos
    text: If the evaluation reveals any rough edges or missing features, then you
      can consider tools like Metaflow, MLFlow etc. which work well with the cloud,
      so you still get many of the same benefits, hopefully with a more pleasant user
      experience and more flexibility.
  - name: Wendy Mak
    text: if there are things that don't work so well, but some other aspects are
      nice, how do you decide at which point you'll accept the time spent is enough
      and try another tool?
  - name: Ville Tuulos
    text: 'that''s a tough one. I''d consider the migration cost too. If you have
      built N projects on a platform X but then find another platform Y better, Y
      needs to be much better to justify replatforming of the previous N projects.
      And, how many future projects M are going to be built on the new platform.

      Really hard to give a generally applicable answer.'
  - name: Ville Tuulos
    text: I'd also emphasize thinking how the ML platform can leverage other tooling,
      talent, and existing expertise at the company (cf. [https://datatalks-club.slack.com/archives/C01H403LKG8/p1632933598496200?thread_ts=1632893087.488600&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1632933598496200?thread_ts=1632893087.488600&amp;cid=C01H403LKG8))
- name: Tim Becker
  text: Hi Ville Tuulos, thanks for the great book! After reading the first chapter
    of your book, I would also like to ask you a few questions.
  replies: []
- name: Tim Becker
  text: '- How can I recognise incidental complexity and hot to avoid it?'
  replies:
  - name: Ville Tuulos
    text: 'I :heart: the question! I can start by answering the other side: how do
      you recognize inherent complexity?

      If something seems complex but the complexity is really not in your control,
      it is inherent complexity in your point of view. For instance, if you are analyzing
      a dataset that includes text written in Chinese, Arabic, Cyrillic, and Latin
      scripts, it seems complex but there''s nothing you can do about it - that''s
      the nature of the world.

      On the other hand, if you are asked to develop a system to parse a JSON file
      but you decided to make it more generic by supporting XML, HTML, and YAML too,
      the extra complexity seems quite incidental and maybe hardly justifiable - you
      just decided to do it.

      So how to avoid adding complexity deliberately? Keep things simple deliberately.
      This is the best talk I have seen about the topic [https://www.youtube.com/watch?v=LKtk3HCgTa8](https://www.youtube.com/watch?v=LKtk3HCgTa8)
      (Simple Made Easy by Rich Hickey)'
- name: Tim Becker
  text: '- You mentioned that relying on pre-build solutions from cloud providers
    is not always cost affective. Could you elaborate on this? Which parts of, for
    example, AWS do you consider more and less cost affective?'
  replies:
  - name: Ville Tuulos
    text: 'The AWS of today is a thick stack of services, building upon each other:

      - At the bottom of the stack you have foundational services like S3, EC2, networking,
      security (IAM).

      - On top of this, mid-tier, you have databases (RDS, DynamoDB, ElastiCache etc),
      container management systems (EKS, ECS), EMR, and bunch of other things like
      CloudWatch.

      - At the top of the current stack you have high-level services like Sagemaker,
      QuickSight, WorkSpaces, all kinds of things.

      Since most of AWS'' own high-level services are built on lower-level services,
      higher-level services can''t be less expensive than the low-level services they
      sit on top of. Often, they are more expensive, sometimes much more. For instance,
      Sagemaker and EMR charge you the cost of the underlying service (e.g. EC2) plus
      a margin. Some mid-tier services like ECS and AWS Batch don''t charge a margin
      on top of the underlying EC2 cost.

      Whether a higher-level service is cost-effective depends on your specific situation.
      You should estimate the Total Cost of Ownership carefully. In contrast, lower-level
      services like EC2 and S3 are pretty much no-brainer cost-effective for most
      use cases (the jury is out on GPU instances...)'
- name: Tim Becker
  text: '- Could you give an example of when to use metaflow?'
  replies:
  - name: Ville Tuulos
    text: "definitely yes:\n- You have many data scientists developing one or more\
      \ ML projects using Python.\n- You are using AWS already.\n- You are experiencing\
      \ any of the following symptoms:\n    \u25E6 difficulties with scaling\n   \
      \ \u25E6 difficulties with deploying or managing workflows\n    \u25E6 friction\
      \ in collaboration\n    \u25E6 want to get better at reproducibility, versioning,\
      \ and tracking experiments.\nmaybe:\n- You are using other clouds and/or Kubernetes\
      \ (I'd love you to test our new K8S integration or talk about use cases on Azure/GCP\
      \ \U0001F642 ).\n- You are pretty happy with the current setup - no big pain\
      \ points.\nno:\n[https://datatalks-club.slack.com/archives/C01H403LKG8/p1632727165458700?thread_ts=1632726041.457100&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1632727165458700?thread_ts=1632726041.457100&amp;cid=C01H403LKG8)"
- name: Tim Becker
  text: '- Do you know a way of measuring the quality of data science infrastructure
    and to determine bottlenecks that should be improved?'
  replies:
  - name: Ville Tuulos
    text: 'here are some questions you can ask:

      - how quickly does a new data scientist become productive with the platform
      and projects?

      - can you hire and onboard domain experts who are not devops or software engineers
      and let them focus on being domain experts?

      - how quickly can you iterate on new, experimental versions of end-to-end ML
      projects (not just the model)?

      - does the platform fail randomly? Do data scientists spend a lot of time waiting
      compute/data/deployment to happen?

      - can you test different modeling approaches easily and experiment with even
      bleeding-edge libraries and techniques?

      - how easy it is to deploy new versions of models to production? is it scary?
      can anyone in the team do it confidently?

      - can you A/B test models and workflows against the production version using
      live data before promoting them fully to production? Can you analyze the results
      of A/B tests confidently?

      - how easily can you onboard new data in your projects, e.g. to test new features?

      - do you know what''s happening? Do you know how models are performing?

      - if something fails unexpectedly, can you quickly figure out the root cause,
      test a fix, and deploy it?'
  - name: Ville Tuulos
    text: then prioritize the questions based on your specific needs and address the
      most glaring pain points
  - name: Tim Becker
    text: "Ville Tuulos thank you so much for answers, Super useful \U0001F4AF:thank_you:"
- name: luckylittle
  text: "Warm regards Ville Tuulos  - I have a simple question: Who is the target\
    \ audience for your book? I briefly looked at the TOC and not entirely sure...\
    \ When the book is finished, will there be any practical tips for DevOps engineers\
    \ managing/designing data science platforms? Many thanks and enjoy your stay \U0001F64F"
  replies:
  - name: Ville Tuulos
    text: if you are a DevOps engineer designing a data science platform, you are
      very much in the target audience. Metaflow is only used as an example in the
      book, so you should find it useful even if you use another framework(s).
- name: Tino
  text: "Hey Ville Tuulos \U0001F642 Thanks for taking the time. At what stage in\
    \ companies would you recommend to focus on \u201Ceffective\u201D infrastructure?\
    \ In many small startups they focus on delivery whereas in my opinion a solid\
    \ foundation should be given at all time. Any thoughts on that or is it to individual?"
  replies:
  - name: Ville Tuulos
    text: realistically it is probably not the first concern at a new startup. It
      becomes more relevant once you have a few people (data scientists / engineers)
      focusing on ML / data science
  - name: Ville Tuulos
    text: 'I wouldn''t wait for too long though, especially with open-source projects
      that don''t require a huge upfront commitment. In a small startup you have often
      resourceful people who know that they could do everything by themselves, so
      there might be a feeling that "we don''t need anything fancy, we can just set
      up X, Y, Z quickly".

      Especially at a smaller company it is important to focus on the company''s core
      business and minimize the time spent on generic infrastructure.'
- name: Krzysztof Ograbek
  text: 'Hi Ville Tuulos, thanks for answering my yesterday''s question. As mentioned,
    I just started deploying ML Models into production. For the next few weeks, my
    goal is to create small web apps based on flask and react with models making predictions
    in the backend. In the end, I want to deploy the apps. I''m comfortable with coding
    but everything else is new to me. So my here come my questions:

    - How can your book help me?'
  replies:
  - name: Ville Tuulos
    text: in your case, maybe the biggest help is to show how you can structure the
      training pipeline and get it running regularly, if you want to update your model
      automatically. It helps to set up the workflows in a way that makes debugging
      and further development easier if you keep working on your project.
- name: Krzysztof Ograbek
  text: '- When should I start using Docker? Is it the sooner the better? How can
    Docker be beneficial?'
  replies:
  - name: Ville Tuulos
    text: 'as we discussed in the thread above, these days you can deploy web apps
      without Docker, e.g. using [Repl.it](http://Repl.it) / Heroku / AppEngine and
      others. In this sense I don''t think you must use Docker.

      If you anticipate that the web app will grow more complex over time and you
      want to invest energy in it, probably learning Docker is a good idea. It is
      relatively easy to get started with Docker.'
  - name: Ville Tuulos
    text: 'Docker is beneficial for two main reasons:

      1. It allows you to package the whole execution environment, all libraries etc.,
      in a single image.

      2. The image can be executed in various environments.'
- name: Krzysztof Ograbek
  text: '- What are the topics I should learn first? Could you recommend any resources?'
  replies:
  - name: Ville Tuulos
    text: can you tell more about your project? Do you want to mainly focus on the
      modeling side or the webapp side?
  - name: Krzysztof Ograbek
    text: "Hi Ville Tuulos and sorry for the late reply. My main goal is to train\
      \ ML models and do something more than just evaluate them in a jupyter notebook\
      \ or similar. This is why Im thinking about web apps. For now I've got two ideas\
      \ how I'd like to bring more value:\n- Educational purposes - let users interactively\
      \ play with model and it's input to see how it affects output\n- Create some\
      \ fun by playing some silly games, eg uploading an image to see if it's a hot-dog.\n\
      So what is my main focus? I want to learn how to effectively deploy models.\
      \ In my latest project I'm dealing with memory challenges. They're completely\
      \ new to me and I'm really stuck. \nI hope any of this answers your question."
- name: "Laura Uzc\xE1tegui"
  text: "Hi Ville Tuulos, \nOne last question before the round closes :) \nIn terms\
    \ of constantly monitoring your models in terms of , for example, accuracy, precision,\
    \ recall, rmse among all the other metrics for evaluation , I have few questions:\n\
    - How often those metrics should be evaluated ? \n- What platform is used in terms\
    \ of observability for evaluation metrics of a model in production? \n- Would\
    \ you say is fair to say if a metric presents a degradation under certain threshold\
    \ to perform training or refresh of the model? \nWhat resources would you recommend\
    \ for learning more about evaluating metrics in production models?"
  replies:
  - name: Ville Tuulos
    text: 'great question! There are many different kinds of monitoring / metrics
      evaluation involved in production ML.

      Monitoring model metrics like precision, recall, RMSE etc. is a good baseline
      sanity check. Many tools like [Weights and Biases](https://wandb.ai/), Tensorboard,
      and of course standard visualization components from e.g. Scikit Learn can help.
      For more production-oriented monitoring, there are newer services like [arize.com](http://arize.com)
      and [monalabs.io](http://monalabs.io) (and many others) which can help.

      For models that drive actual business outcomes in production, it is a good idea
      to focus on monitoring the KPIs that matter for the business rather than just
      model metrics. For instance, if your model predicts who will click ads, you
      should measure the actual Click Through Rates (or even better: Cost Per Click)
      and not just RMSE. For monitoring KPIs, any business analytics tool (Tableau,
      Mode Analytics etc) will work.'
  - name: Ville Tuulos
    text: 're: refreshing models - in most cases it is a good idea to retrain the
      model frequently, independent of the metrics, backtest its performance with
      historical data to ensure that nothing is obviously wrong, and potentially A/B
      test in production if the use case is sensitive. If you retrain only when the
      performance degrades, you will suffer from data/concept drift and worsening
      performance until you hit the threshold. Instead of being reactive, you can
      be proactive and retrain continuously (e.g. once a day).

      Measuring and plotting the delta in model performance day-over-day (or week-over-week
      etc) is a powerful way to catch issues when you roll out new models (and even
      when you don''t).'
  - name: "Laura Uzc\xE1tegui"
    text: "Thank you so much for your answer and insights. \nReally useful and I enjoyed\
      \ learning from your experience. \nHope to see you around \U0001F60A \nDo you\
      \ have social media or a blog or a place where you share your knowledge ?? \n\
      All the best Ville Tuulos"
  - name: Ville Tuulos
    text: you can find me any time at our Slack [https://datatalks-club.slack.com/archives/C01H403LKG8/p1633128052035000](https://datatalks-club.slack.com/archives/C01H403LKG8/p1633128052035000)

---

Effective Data Science Infrastructure: How to make data scientists more productive is a hands-on guide to assembling infrastructure for data science and machine learning applications. It reveals the processes used at Netflix and other data-driven companies to manage their cutting edge data infrastructure. In it, you’ll master scalable techniques for data storage, computation, experiment tracking, and orchestration. You’ll also learn how to collaborate with data scientists to deliver exactly what they need to succeed.