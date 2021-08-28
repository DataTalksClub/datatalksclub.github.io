---
title: "Data Science on AWS"
description: "Book of the Week. Data Science on AWS by Antje Barth"
cover: "images/books/20210628-data-science-on-aws/cover.jpg"
image: "images/books/20210628-data-science-on-aws/preview.jpg"
start: 2021-06-28 00:00:00
end: 2021-07-02 22:59:58
authors: [chrisfregly, antjebarth]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/data-science-on/9781492079385/
  - text: Book's page on Amazon
    link: https://www.amazon.com/dp/1492079391/
  - text: Book's website
    link: https://www.datascienceonaws.com/
  - text: Book's GitHub repository
    link: https://github.com/data-science-on-aws/workshop

archive:
- name: Antje Barth
  text: Hi everyone! Chris Fregly and myself are here to answer
    your questions!
  replies: []
- name: Antje Barth
  text: "We\u2019re also running a live, 4hrs hands-on workshop tonight, starting\
    \ at 6pm CET. The workshop is based on our book and code repo: Build an End-To-End\
    \ Pipeline With BERT, TensorFlow, and Amazon SageMaker. You can RSVP [here](https://pages.awscloud.com/NAMER-field-OE-Machine-Learning-Dev-Day-2021-reg-event.html)."
  replies:
  - name: Lalit Pagaria
    text: Thanks for sharing link. Is it possible to share link with other community?
  - name: Antje Barth
    text: Sure, please do!
  - name: Kshitiz
    text: Hi Antje Barth , Would this session be recorded? It
      will get pretty late in IST.
  - name: Ken Lee
    text: Hi same question here Antje Barth, it would be pretty
      late in SGT too
  - name: Antje Barth
    text: 'We do have previous workshop recordings shared here:

      [https://youtube.datascienceonaws.com/](https://youtube.datascienceonaws.com/)

      For example, [the May workshop](https://www.youtube.com/watch?v=sL8wpFo7LaQ)'
  - name: Chris Fregly
    text: 'yesterday''s workshop here:  [https://youtu.be/R0dyrBQMAnQ](https://youtu.be/R0dyrBQMAnQ)'
  - name: Ken Lee
    text: That's great stuff! Thanks
- name: Agrita Ga
  text: "Hi Antje Barth and Chris Fregly.\
    \ \U0001F44F\nIs there currently any standard (or trend) for MLOps _best practices_\
    \ in context of AWS tech stack?"
  replies:
  - name: Antje Barth
    text: "I think it\u2019s going to be a phased approach\n1/ Moving away from manually\
      \ building models to\n2/ Orchestrating the individual model building workflow\
      \ steps (ie. data preprocessing, training, evaluating) in a pipeline, and automating\
      \ tasks within each step\n3/ Automatically re-running training and/or deployment\
      \ pipelines on triggers such as model decay, or code changes\nThe tools and\
      \ technologies will likely vary based on each use case and team experience.\
      \ AWS recently launched SageMaker Projects, which automatically sets up a CI/CD\
      \ automation for your ML pipelines. So whenever you commit new code into a code\
      \ repo, it would re-run the model building and deployment pipeline.\nOn manual\
      \ approval, you could deploy into a staging environment, on a second approval,\
      \ after running integration tests, you could deploy into a production environment.\
      \ This is just a sample setup.\nWe also describe this approach in our book!"
- name: Bayram Kapti
  text: "Hi Antje Barth &amp; Chris Fregly!\
    \ Thanks for sharing your thoughts here with us! \nWhile every problem\
    \ requires different approach and solution, it\u2019s said that most of the times,\
    \ fundamental algorithms in DS are the most effective solutions to actually getting\
    \ results. \n1-) Do you agree? How has it been working for you so far?\n2-) How\
    \ does it work at #aws? Are there systems, procedures built at Amazon to make\
    \ sure best solution is used when approaching a problem?"
  replies:
  - name: Antje Barth
    text: "You should always go for the solution that solves your problem the fastest\
      \ and in the most efficient way. For example, if you need a simple image recognition\
      \ model, why build the model from scratch yourself, if there\u2019s plenty of\
      \ algorithms and models in the industry that have already solved this problem?\
      \ Re-use and customize it to your needs. You should focus your time on solving\
      \ the actual business problem, not figuring out how to train a model or managing\
      \ infrastructure.\nComing back to AWS, I would always recommend looking at the\
      \ pre-built AI services first, ie. Amazon Rekognition for object/video detection,\
      \ Amazon Comprehend for NLP, Amazon Textract for document text extraction, Amazon\
      \ Personalize for personalized recommendations etc. If they already solve your\
      \ problem, great.\nIf you need to build and train your own model, go to the\
      \ next level, Amazon SageMaker. This service gives you the freedom to either\
      \ use built-in algorithms, write your own code, or even bring your own Docker\
      \ images with your custom libraries. This layer still takes care of all of the\
      \ infrastructure management for you.\nAWS always works back from the customer\
      \ in solving customers\u2019 challenges."
- name: Bayram Kapti
  text: 3-) Also, how does your day look like working at aws?
  replies:
  - name: Antje Barth
    text: "Getting up, a lot of coffee \u2615\U0001F605, checking emails and Slack,\
      \ a few calls with team members, working on demo code, presenting at a conference,\
      \ running a workshop, dropping in here and answer #book-of-the-week\
      \ questions! \U0001F642"
- name: Alex
  text: "Hi there Antje Barth &amp; Chris Fregly!\
    \ Pleasure talking to you \U0001F642\nWhat are the three most important\
    \ things that someone using AWS (instead of any of the other main cloud providers)\
    \ for ML/AI purposes can brag about?\nIt\u2019s known that top-tier cloud providers\
    \ offer very similar services, so how would you convince someone who doesn\u2019\
    t know which one to start using to get into AWS? And more specifically, to AWS\
    \ _for data science_?"
  replies:
  - name: Antje Barth
    text: "AWS always approaches everything they do by focusing on their customers.\
      \ This customer obsession drives 90 percent of the product roadmap, leading\
      \ to the invention of a bevy of machine learning services at all three layers\
      \ of the stack that I mentioned earlier:\n \nFor example, at the bottom layer\
      \ of the stack AWS builds their own custom silicon designed to accelerate deep\
      \ learning workloads with AWS Inferentia.\nIn 2017, AWS launched Amazon SageMaker\
      \ \u2013 a fully managed service that enables developers to quickly build, train,\
      \ and deploy machine learning models at scale.\nAnd at the top layer of the\
      \ stack, AWS offers the broadest set of artificial intelligence services \u2013\
      \ with little to no ML experience required.\nThis includes entirely new categories\
      \ of services enabled through machine learning including Amazon Kendra to reinvent\
      \ enterprise search, Contact Lens for Amazon Connect to embed intelligence into\
      \ contact center operations, Amazon HealthLake to help healthcare organizations\
      \ make sense of their data, and machine learning services purpose built for\
      \ industrial and manufacturing companies just to name a few.\nAlso, AWS is the\
      \ only cloud provider to offer a choice of Intel, AMD, and Arm processors. And\
      \ for running machine learning at scale and in production, AWS introduced the\
      \ Inf1 instances for EC2, which are powered by AWS Inferentia chips.\nSo I\u2019\
      d say it\u2019s the combination of the depth and breadth of services, together\
      \ with the fast pace in innovation, always working backwards from customer challenges,\
      \ and the experience and maturity after 15 years in business paired with millions\
      \ of active customers and tens of thousands of partners globally."
- name: David Cox
  text: Very excited to see this book here! Riffing off Alex's post, my question is
    why AWS? Why contain everything within the AWS ecosystem?
  replies:
  - name: Chris Fregly
    text: "I use the AWS ecosystem everyday - works very well for me!  \U0001F642"
  - name: Chris Fregly
    text: We work with a lot of customers that use open source container (ie. Kubernetes),
      analytics (ie. Apache Spark), and machine learning (ie. TensorFlow/PyTorch/Scikit-Learn)
      technologies with AWS.  AWS handles the "undifferentiated heavy lifting" of
      managing your own infrastructure.  Would you like to spend your time debugging
      lower-level infrastructure issues?  Or would you like to spend your time solving
      higher-level business problems?  I personally like to solve business problems,
      so I use AWS for my analytics and ML infrastructure needs.
- name: Heeren Sharma
  text: "Hi Antje Barth Thanks for the heads up regarding workshop.\
    \ I have not played around with Sagemaker but have experience with Azure ML. One\
    \ challenge that I see time and again is integration among services e.g. for a\
    \ full blown data pipelines which leverages ML realtime scoring ( and maybe training),\
    \ something like a feedback loop related, how well AWS Sagemaker integrate well\
    \ with overall AWS services (e.g. with a Glue job, etc.)? Another quick follow\
    \ up question, how well code integration work e.g. can one connect with jupyter\
    \ servers with their local IDE, are there extension? Many thanks.\n_Disclaimer:\
    \ I am primarily coming from AWS world, but since past 1 year working over Azure\
    \ ML for a client project. So I am curious how AWS solves these problems_ \U0001F642"
  replies:
  - name: Chris Fregly
    text: Amazon SageMaker integrates with many of the AWS services - and we are always
      adding new integrations based on customer feedback.  More specifically, SageMaker
      Pipelines integrate with [EventBridge](https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbridge.html)
      to trigger a Start Pipeline event or respond to state changes within your pipeline
      execution.  Also, SM Pipelines supports a flexible [CallbackStep](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-callback)
      that lets you call any service directly using Python, Java, etc.
  - name: Heeren Sharma
    text: Many thanks! Sounds awesome.
- name: Fernando Lichtschein
  text: Hello! Is there a workshop that can be done by an IT student using an AWS
    Educate classroom account that can demonstrate a real pipeline? Ideally it should
    not involve too much knowledge of AWS services,
  replies:
  - name: Antje Barth
    text: "I\u2019m not super familiar with the Educate account, but we recently launched\
      \ a Coursera specialization in collaboration with [DeepLearning.AI](http://DeepLearning.AI),\
      \ called Practical Data Science.\nIt comes with 3 courses 10 weeks of lecture\
      \ videos, quizzes and on-demand, self-paced hands-on labs! (no personal AWS\
      \ account required, you get access to a demo account): [practical data science](https://www.coursera.org/specializations/practical-data-science)\n\
      This might be a good path to start!"
  - name: Ken Lee
    text: Looks great! Thanks Antje Barth will start on this
  - name: Fernando Lichtschein
    text: Great, thank you!
- name: Asmita
  text: Hi Antje Barth and Chris Fregly,
    will the book be helpful for beginners who are currently learning AWS and do not
    have much hands on experience? What advise would you give on how to start working
    on AWS?
  replies:
  - name: Antje Barth
    text: 'If you are completely new to AWS, you might want to start with a general,
      intro-level AWS course such as the [AWS Cloud Practitioner](https://www.coursera.org/learn/aws-cloud-practitioner-essentials),
      or [AWS Fundamentals](https://www.coursera.org/specializations/aws-fundamentals)
      course.

      As for our book, we always start with an introduction and discussion of the
      relevant concepts first before we go into the AWS specifics to help readers
      follow along. So as long as you bring some basic cloud and ML knowledge, readers
      should be able to follow along easily.'
- name: "Philip Die\xDFner"
  text: 'Hello Antje Barth and Chris Fregly.

    Thanks for being here! Where do you see your book on the way to becoming  AWS
    ML Certified? Is it + some more practice and experience a good basis? Or are there
    areas where other learning resources should be used?'
  replies:
  - name: Antje Barth
    text: "The book definitely covers a good amount of ground towards the ML certification.\
      \ In addition, I\u2019d spend some time hands-on, familiarizing yourself with\
      \ the services and concepts. And as a final check, scanning through the specific\
      \ ML cert preparation materials!"
- name: Livsha Klingman
  text: 'Hi  Antje Barth &amp; Chris Fregly! Thank you for being open for Q&amp;As!

    Being a trained data scientist but my employment pushing me more into the data
    engineering spectrum, due to the complexity &amp; velocity that data is now flooding
    the ''market'' with, and the greater need for pipelining data to apply ML/AI applications.
    After successfully building a few pipelines, both in Azure and AWS, I find myself
    quite bewildered by the array of AWS platform tools and almost unsurmountable
    amount of syntax surrounding each. Does your book provide a method of selecting
    the correct tools or combinations of for each given data scenario, to optimize
    the pipeline, as well as maximize the data prep needed for ML in a way that speaks
    not just to professionally trained data engineers? The documentation ''out in
    the market'' I find quite overwhelming coming from a data science stance and designed
    for professional data engineers at large. My role is purely ML/AI goal oriented
    data pipelining.'
  replies:
  - name: Chris Fregly
    text: the book is focused on ML/AI-oriented data pipelines, yes.  the first couple
      chapters show the breadth of services available for different use cases.  the
      remaining chapters dive deep into building an end-to-end pipeline for a single
      ML/AI use case.  we preferred this approach because it provides a specific slice
      through the broad set of AWS options across the analytics, machine learning,
      streaming, and security services on AWS.
  - name: Livsha Klingman
    text: Thank you!
- name: Ganeshkumar
  text: 'Hi Antje Barth and Chris Fregly
    , thank you so much for Q&amp;As.

    1. Currently AWS does not offer drag and drop feature in UI, which may simplify
    things while model creation. When can we expect such feature in Sagemaker?

    2. In your view how much of data architecture skill is required for data scientist
    to excel in building an effective model for consumption

    ?'
  replies:
  - name: Chris Fregly
    text: AWS offers drag-and-drop for the data/feature engineering step of the pipeline.  This
      service is called SageMaker Data Wrangler and it's integrated with SageMaker
      Studio.  we cover this in the book.  I can't comment on the roadmap for SageMaker,
      but we prioritize features based on customer feedback - and i will pass this
      request on to the SageMaker team!
  - name: Chris Fregly
    text: having a good data foundation is very important to building effective models.   everything
      starts with your data.
  - name: Ganeshkumar
    text: Thanks very much !
- name: Livsha Klingman
  text: 'Hi againAntje Barth &amp; Chris Fregly!

    Taking full advantage of this opportunity... Due to my novice data engineering
    stance and my ''on-the-job'' training. I basically devised a ''split personality''
    method of focusing on the engineering -Part 1, the most optimal ETL/ELT pipeline
    to a final data structure, and then and only then focusing on the specific data
    requirements to implement the Part 2- Data scientific or analytical ML algorithms
    or visualizations applications.

    My question is...Is this really in the long run (the final goal in mind) inhibiting
    my optimized process. I see the benefits of a final comprehensive data structure
    at the end of the ETL/ELT process, but maybe the final data manipulation output
    (ML or AI) specifications should really be incorporated into the initial pipeline?
    Does it make a difference whether processing BIG data or not? Within the AWS platform
    or not?'
  replies:
  - name: Chris Fregly
    text: definitely depends on the dataset (where is the data located?), model type
      (how difficult/time-consuming to re-generate the features for this model type?),
      organization structure (are you sharing this data with other teams outside of
      yours?), security needs (do you need to lock down certain features to certain
      teams?), etc.  data pipelines can get complex, for sure.  if you the data transformations
      are being re-used by many teams, you might want to use SageMaker Feature Store
      to store and manage your transformed features - [feature-store](https://aws.amazon.com/sagemaker/feature-store/)
  - name: Chris Fregly
    text: SageMaker Feature Store is supported by SageMaker Pipelines, btw.
  - name: Livsha Klingman
    text: I am going to look into this - thank you for the direction and your time!
- name: Livsha Klingman
  text: 'Another... Antje Barth &amp; Chris Fregly!

    Do you have any ideas how I can boost my knowledge and professionalism within
    my constraints of my full time job?

    When considering the whole picture, the pipeline AND the final output. What should
    the list of focus points and considerations in order of importance? What are the
    typical pitfalls to be aware of when integrating into the AWS platform?'
  replies:
  - name: Chris Fregly
    text: data is the most important.  useful data transformations that produce useful
      features.
  - name: Livsha Klingman
    text: 'Does this mean that the pipeline should be adapted for the features involved
      and not adapt (slice) the data after the data loading?

      The ideal, for producing a data science goal, would be to pipe the necessary
      features and not the whole data structure, like I am currently doing, only filtering
      out data (features) after all of the important data has been cleaned and stored
      in the correct structure?'
- name: Livsha Klingman
  text: 'Thanks so much your time and availability...Antje Barth &amp; Chris Fregly

    How do you see the tools in AWS providing an optimal medium for building &amp;
    training  a model? Is using the AWS infrastructure and their given tools really
    more effective for modeling, than experimenting with the vast assortment of other
    algorithms, NLP, CNNs and general deep and unsupervised learning  tools?'
  replies:
  - name: Chris Fregly
    text: Amazon SageMaker - and the broad AWS set of analytics tools such as Amazon
      Athena and Redshift - support all available algorithms for NLP, CNN's, deep
      learning, supervised learning, unsupervised learning, reinforcement learning
      - everything!  AWS provides the managed infrastructure that allows you focus
      more on the business problem and less on the infrastructure.  You can also scale
      out your data processing and model training/tuning/deploying with a simple API
      call or click of a button.  In other words, AWS does not limit your options
      in any way.  You can easily convert the Python code running on your laptop to
      a scalable SageMaker Job.  If it runs locally, it can run on the SageMaker infrastructure.
  - name: Livsha Klingman
    text: Amazing - almost too good to be true... so what's the snag? Why am I not
      crossing paths with others using AWS in this way?
  - name: Sara Lane
    text: The AI field is constantly evolving, and Amazon keeps adding new features
      to its AI suite. I think that many people are actually taking advantage of these
      features, and I think that usage will grow as time goes on.
- name: Tim Becker
  text: Hello Antje Barth and Chris Fregly,
    I would like to ask you a few questions concerning the book. Of course,
    the book focuses on AWS, but is the covered knowledge transferable to other platforms?
    For example, if my company is using google.
  replies:
  - name: Chris Fregly
    text: Sure, the book discusses the concepts/problems at a high level, then dives
      deep into how to implement the solution on AWS.  throughout the book, we provide
      best practices.  Some of the cost-savings and performance-related tips are AWS
      specific, but the concepts are transferrable across all environments.
- name: Tim Becker
  text: Do you have some recommendations on how to practice cloud services for free?
  replies:
  - name: Chris Fregly
    text: SageMaker supports free tier.  Just make sure to clean up the resources
      when you're done to avoid extra cost beyond the free tier.  ie. shutdown the
      notebooks, etc.
- name: Tim Becker
  text: What kind of performance can we expect from models developed with SageMaker
    Autopilot?
  replies:
  - name: Chris Fregly
    text: SageMaker Autopilot builds a set of model pipeline candidates using various
      algorithms and feature-engineering steps using Automated ML (AutoML).  Performance
      varies depending on your dataset and type of problem (classification, regression,
      NLP, multi-layer perceptron, etc).  The cool part is you can just point Autopilot
      to your dataset and try it out.  Your mileage may vary, etc.
  - name: Tim Becker
    text: thank you for your answers, is testing of autopilot included in the free
      trial?
- name: Ken Lee
  text: Hello Antje Barth and Chris Fregly. What are the advice on a proper machine
    learning project that accumulates as little of technical debt as possible?
    A lot of the tutorials found online taught us on the HOWS to build a model,
    but did not cover most of the stuffs other than that. Or can we find answer in the book?
  replies:
  - name: Chris Fregly
    text: In an ideal world, you would have clean data, perfect feature transformations,
      the best algorithm, and the optimal set of hyper-parameters.  This way, you
      would just train your models and push them to production.  This is rarely the
      case.  Anything beyond the ideal scenario will incur some technical debt.  The
      ideal state would be a perfectly-tuned experimentation pipeline that lets you
      easily try, track, and compare different combinations of data, feature transformations,
      algorithms, and hyper-parameters.  This is what SageMaker Pipelines (integrated
      with SageMaker Experiments) offers as a managed service to let you focus on
      the business problem.
  - name: Chris Fregly
    text: 'short answer:  the less infrastructure code you need to write, the less
      technical debt you will incur as you are focusing only on the business problem.'
  - name: Chris Fregly
    text: and yes, the book covers a clean, end-to-end implementation of the common
      machine learning task of text classification using natural language processing
      (NLP) and BERT.
  - name: Ken Lee
    text: Great! Thanks for the tips! Appreciate jt
- name: Ken Lee
  text: also particularly curious on the Model Monitoring aspects of the deployed
    model, aware that ML models invariably suffer from performance degradation.  Which
    AWS services cover the monitoring part? Also regarding the containerization of
    application on AWS, do you have a good resource to point us to or it is already
    covered in the book?
  replies:
  - name: Chris Fregly
    text: SageMaker Model Monitor is the AWS service that monitors models for drift
      and degradation in production.  Model Monitor uses an open source library called
      `deequ` (a library on top of Apache Spark) to continuously monitor the live
      model-prediction inputs for statistical drift against the baseline training
      dataset - as well as model prediction drift.  For other types of statistical
      analysis, check out SageMaker Clarify and the accompanying open source library
      `smclarify` .
  - name: Chris Fregly
    text: Containerization of applications should be very well-documented as containerization
      is so common these days.  If you hae trouble finding examples, ping me and i
      can point you to some references.  If you mean containerization of the trained
      models, we cover this in Chapter 10 when we talk about deploying models.
  - name: Chris Fregly
    text: "Oh, and it's worth highlighting that SageMaker Model Monitor is integrated\
      \ with Amazon CloudWatch to automatically notify you if your model starts to\
      \ drift or degrade outside of a given threshold.  This is a very powerful mechanism\
      \ to help wake up the data scientist at 2am!  \U0001F642"
  - name: Ken Lee
    text: "Great stuff! Thanks Chris Fregly \U0001F44D\U0001F44D\
      \U0001F44D"
- name: Ricky McMaster
  text: "Hi Antje Barth &amp; Chris Fregly,\
    \ many thanks for doing this!\nMy first question is on tool choices - I\
    \ see from the preface that you cover both Kinesis and Kafka, but generally speaking\
    \ you understandably stick to AWS products.  Do you discuss (or can you imagine)\
    \ use cases where it\u2019s best to opt for a more customised solution?  For example,\
    \ more than one company has had scaling issues with Athena - how do you address\
    \ this topic?"
  replies:
  - name: Chris Fregly
    text: AWS offers Managed Streaming for Apache Kafka (MSK) which uses open source
      Apache Kafka as an alternative to Amazon Kinesis.  However, I also see customers
      that prefer to manage their own Apache Kafka clusters on EC2 directly.  These
      are all valid options - and the choice depends on many factors including the
      skillset of the team, etc.
  - name: Chris Fregly
    text: I'm not familiar with the specific scaling issues that you mention.  In
      those cases, the customer should work with AWS Support to diagnose the issue
      and find the right solution forward.  Amazon Athena is based on - and compatible
      with - Apache Presto, so the customer could choose to manage their own Presto
      cluster on EC2 with minimal changes to their data pipelines.
  - name: Ricky McMaster
    text: "Ok thanks for your take on this Chris Fregly, appreciated.\
      \ The Presto approach you cite is something I\u2019m a little familiar with."
- name: Ricky McMaster
  text: Secondly, do you see any scope at AWS for developing its own framework(s)
    to rival either TensorFlow or PyTorch?
  replies:
  - name: Chris Fregly
    text: Amazon has contributed Apache MXNet to the Apache Foundation which is similar
      to TensorFlow and PyTorch.  Just like any large enterprise, we use many different
      machine learning, deep learning, and reinforcement learning frameworks for our
      business needs.
  - name: Ken Lee
    text: Correct me if I'm wrong but I recall that Amazon is a major contributor
      of Pytorch, alongside with Facebook?
- name: Alper Demirel
  text: Hi, first of all thanks for being here. What should be considered when migrating
    an ML project from local or another cloud platform to AWS? What are your suggestions
    about this?
  replies:
  - name: Antje Barth
    text: 'Depends on the complexity of the workloads you want to migrate.

      It could be as simple as using your local IDE and configuring a connection to
      AWS, importing Python SDKs and start launching jobs with Amazon SageMaker.

      For fully operational ML workload migrations, the plan would be more like:

      1/ Plan the migration

      - Validate source code and datasets

      - Identify target build, train, and deployment instance types and sizes

      - Create capability list and capacity requirements

      - Identify network requirements

      - Identify the network or host security requirements for the source and target
      applications

      - Determine a backup strategy

      - Determine availability requirements

      - Identify the application migration or switchover strategy

      2/ Configure the infrastructure

      - Network, security, storage

      3/ Upload the data and code

      - Migrate datasets to provisioned S3 buckets

      - Package ML training/hosting code as Python packages and push to provisioned
      code repos

      4/ Migrate the application, and cut over'
  - name: Alper Demirel
    text: "Thank you very much, what you said means a lot to me. It will work great\
      \ for me \U0001F64F"

---

With this practical book, AI and machine learning practitioners will learn how to successfully
build and deploy data science projects on Amazon Web Services. The Amazon AI and machine learning
stack unifies data science, data engineering, and application development to help level upyour skills.
This guide shows you how to build and run pipelines in the cloud, then integrate the results into
applications in minutes instead of days. Throughout the book, authors Chris Fregly and Antje Barth
demonstrate how to reduce cost and improve performance.

