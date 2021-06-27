---
title: "Building Machine Learning Pipelines"
description: "Book of the Week. Building Machine Learning Pipelines by Hannes Hapke"
cover: "images/books/20210607-building-machine-learning-pipelines/cover.jpg"
image: "images/books/20210607-building-machine-learning-pipelines/preview.jpg"
start: 2021-06-07 00:00:00
end: 2021-06-11 22:59:58
authors: [hanneshapke, Catherine Nelson]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/building-machine-learning/9781492053187/
  - text: Book's website
    link: https://www.buildingmlpipelines.com/
archive:
- name: Sricharan
  text: 'Thanks for doing this Hannes Hapke.

    Are CPUs predominant for powering inference services today?'
  replies:
  - name: Hannes Hapke
    text: Hi Sricharan, I think the answer depends on the model architecture. But
      I think it is true in most cases. At [digits.com](http://digits.com) we have
      deployed a number of transformer models, and we have optimized them to such
      an extended that the latency is decent on a CPU instance.
- name: Sricharan
  text: What are your thoughts on inference chips like Google Coral or Jetson Nano?
  replies:
  - name: Hannes Hapke
    text: I haven't really seen consumer facing applications since the users always
      need the device. That changes in an instance as soon as a phone contains a coral
      chip.
- name: Sricharan
  text: What are your thoughts on building and deploying continuous training models
    at scale?
  replies:
  - name: Hannes Hapke
    text: "A must for scalable ML projects. \U0001F642"
- name: Sricharan
  text: "What inspired you to write this book? Do you see a future where ML deployment/training\
    \ a part of  \u201Cfull-stack\u201D software engineer portfolio?"
  replies:
  - name: Hannes Hapke
    text: "When I wrote the initial proposal, I was missing an overarching toolchain\
      \ for MLOps. Luckily that developed during the course of the book writing with\
      \ the most promising contender TFX.\nML part of \u201Cfull-stack\u201D software\
      \ engineer? I don't think so. The term \u201Cfull-stack\u201D software engineer\
      \ is already overloaded, I doubt we can squeeze in another definition. However,\
      \ I would like to see that more domain experts (regardless of the field) apply\
      \ more ML. The standardization of ML will help with the adoption."
- name: Alper Demirel
  text: 'Thank you so much for being here Hannes Hapke.

    What do you think are the biggest challenges a junior machine learning engineer
    or intern will face when building a machine learning pipeline? What should they
    pay attention to?'
  replies:
  - name: Hannes Hapke
    text: 'biggest challenge: Seeing an ML project end-to-end.'
  - name: Hannes Hapke
    text: From the data investigation, model architecture selection, validation, deployment,
      feedback loop (last one often missed).
  - name: Alper Demirel
    text: thank you for your answers, sir
  - name: Hannes Hapke
    text: My pleasure!
- name: Lalit Pagaria
  text: 'Thank you Hannes Hapke for being here.

    I see very tight coupling between training and serving pipeline. Most of ML pipeline
    concentrate more towards training side in comparison to serving side. But real
    user of Model are served by serving pipeline. What is your opinion about completely
    delinking these two pipelines? and what do suggest towards building scalable serving
    pipeline?'
  replies:
  - name: Hannes Hapke
    text: Hi Lalit Pagaria I think the processes are already delinked. At last at
      Digits where I work. We produce model version candidates which come out of our
      pipelines. After a human review, those model get deployed via a 2nd automated
      process.
  - name: Hannes Hapke
    text: To keep your pipelines scalable, I think the combination between Apache
      Beam and Kubernetes is key.
  - name: Hannes Hapke
    text: Beam lets you scale all data heavy tasks. You can start off with a direct
      runner (runs within a k8s container) and you can later export the data heavy
      tasks to its own cluster (with Beam using Apache Flink or GCP Dataflow)
  - name: Lalit Pagaria
    text: 'Thank you Hannes Hapke

      I will explore this idea of using Beam''s Pipeline IO for my project [Obsei](https://github.com/lalitpagaria/obsei).'
  - name: Hannes Hapke
    text: Cool Project! Thank you for sharing.
- name: Shankar Somayajula
  text: 'Hi Hannes Hapke Thanks a lot for taking questions.

    Most DS work seems to occur in python but what role can SQL play in the execution/orchestration
    of ML Pipelines especially within Tensorflow ecosystem?

    Also cant we use SQL in Model Analysis ... A lot of the Fairness/Checks can be
    performed using sql.  Analyzing the performance of a model is akin to performing
    BI tool actions to compare actual and prediction data sets. Its similar to comparing
    Sales or Marketing Campaign performance for 2 applicable products.'
  replies:
  - name: Hannes Hapke
    text: 'Hi Shankar Somayajula

      SQL is very useful for building the data ingestion in ML pipelines.

      SQL for model validation? I think this only works if the model is deployed in
      some way. The results would be stored in the db and then analyzed with SQL.
      But the model validation should happen before a model deployment, therefore
      SQL isn''t a great tool here. If we do it in Python, we don''t have to store
      the validation results in a db and can keep it memory.'
  - name: Shankar Somayajula
    text: 'Hannes Hapke Some follow up questions. Hope you dont mind :)

      Sorry, I meant sql for purpose of Model Monitoring post deployment to catch
      things like data drift, concept drift, model internal patterns becoming stale
      etc, not Model Validation (during model build). Yes, i agree this would require
      that all scoring details have to be stored in the database.

      Regd sql usage in ML Pipelines, i guess you mean that sql part of pipeline exists
      prior to Tensorflow coming into the pic. Do you know of any cases of Tensorflow
      doing its magic (so to say :D) and sql doing some analytics post TF? Is that
      a rarity, python usually does the post processing, if any.

      Background/Explainer: We use In-Database ML in our company, so sql is the go
      to tool even for ML tasks.'
  - name: Hannes Hapke
    text: In-Database ML seems to be great if the models are smallish. I haven't seen
      such a setup for larger language models (might be a minority anyway).
  - name: Hannes Hapke
    text: We use BigQuery very heavily at Digits and therefore use SQL for analytics
      of the deployed models
  - name: Shankar Somayajula
    text: Thanks for the info. Personally I dont know much about NLP... Our In-Database
      usecases are more traditional ML usecases like classification, regression, anomaly
      detection etc. I work for Oracle so the technology is based on Oracle Db and
      Oracle Cloud Tech.
- name: Rona Ainslie
  text: Hi, what do you see as the main differences between deep learning and machine
    learning? I've never used tensorFlow, but I have used a little sklearn to create
    neural networks (eg MLPClassifier) is that still machine learning or does it cross
    into deep learning?
  replies:
  - name: Hannes Hapke
    text: 'Hi Rona Ainslie
      Deep learning is subset of ML where model are "deeper" meaning they contain
      more layers to capture more complex relationships. I think the boudary between
      traditional ML and deep learning are fuzzy. If you are interested in MLOps with
      Scikit learn, take a look at this example below on how to use TensorFlow Extended
      for Scikit Learn models: [penguin_pipeline_sklearn_local.py](https://github.com/tensorflow/tfx/blob/master/tfx/examples/penguin/experimental/penguin_pipeline_sklearn_local.py)'
  - name: Rona Ainslie
    text: Brilliant, that looks very interesting. Thanks
- name: Bayram Kapti
  text: "Hi Hannes Hapke,\nWhat are the roles in a team that supports building ML\
    \ pipeline? \nHow do MLEs, DEs &amp; DSs work together to build a ML pipeline?\
    \ \nWho manages this process? DS Lead, ML Engineer Lead, DE Lead?"
  replies:
  - name: Hannes Hapke
    text: The roles are often defined differently from company to company. In the
      context at [Digits.com](http://Digits.com), ML Engineers work hand in hand with
      Data engineers. For example, data engineers are the experts to provide BigQuery
      queries for data ingestion component. ML Engineers then take it from there and
      build the down stream components.
  - name: Hannes Hapke
    text: 'Q: Who manages this process? DS Lead, ML Engineer Lead, DE Lead?

      Honestly, I haven''t seen a place where all three roles come together.'
- name: Bayram Kapti
  text: And as a follow up, do you discuss these in your book? Thanks!
  replies:
  - name: Hannes Hapke
    text: We discuss the aspects of the different roles in Ch 1
- name: Dr Abdulrahman Baqais
  text: 'Hi Hannes Hapke. Thanks for your effort in putting your experience in this
    book. Very interesting book and very valuable for team leads. Couple of questions:

    1) Do you think having an automated process is a necessary step or a luxurious
    one for data teams?


    2) Shall an automated pipeline be only enforced in mature teams at big organizations
    or even startup should consider it?


    3) Automated pipeline usually is discussed at modeling and deployment....should
    not that be extended to project scoping , business analysis and data gathering
    and customer satisfaction. So then we havean overall operating model for the whole
    process?


    4) Can we have the same pipeline for all types of analytics: Insights, ML, DL,
    RL?  Or DL &amp; RL might demand different requirements?


    5) Can automated ML tools from Datarobot, Google and Amazon helps in setting up
    the right pipeline for new teams? Or an expert ML must be there to design and
    operate?.'
  replies:
  - name: Hannes Hapke
    text: "1. For long term projects a necessity\n2. Startups with a solid product\
      \ market fit will tremendously benefit from the standardization around the ML\
      \ practices. Our data team at Digits doesn't have the size of Amazon's \U0001F642"
  - name: Hannes Hapke
    text: 3) MLOps is focusing on the continuous "production" of ML model versions
      for a given model. I think the tasks you mentioned are important, but I think
      they are part of the job of a ML product manager or data scientist. The project
      scoping wouldn't change with every new model version. It can be (and should
      be) set before the project starts.
  - name: Hannes Hapke
    text: '4) I don''t think that insights require ML pipelines, but a proper data
      engineering work flow,. Here, we aren''t training a model which needs to be
      validated and deployed.

      ML Pipelines generally focus on ML and DL models.

      I haven''t seen a pipeline for RL models. But that doesn''t mean that a pipeline
      couldn''t be used. I just haven''t seen a proper production RL model so far
      (except for hand crafted, very specific solutions).'
  - name: Hannes Hapke
    text: 5) I think products like Datarobot provide the same thinking behind their
      products. Last time I checked Datarobot was only focused on ML models. Whoever
      operates Datarobot, Google, etc. on your team needs to understand the implications
      of the ML model and investigate it before deploying it.
  - name: Dr Abdulrahman Baqais
    text: Thank you much for this elaborated answers. Indeed ML pipeline is necessary
      for data teams.
- name: Saskia Kutz
  text: Hi Hannes Hapke. The description of your book sounds very interesting. How
    well do I need to know Tensorflow (and further prior knowledge) to understand
    your book?
  replies:
  - name: Hannes Hapke
    text: 'Hi Saskia Kutz,

      We have focused on the TF ecosystem because it provides the most holistic toolset
      for ML Engineering. Some chapters are framework agnostic (e.g. TensorFlow Data
      Validation can be used with Scikit learn or PyTorch models). Since we published
      the book, TFX improved further to be used with scikit, JAX, or PyTorch models.
      See please [penguin_utils_sklearn.py](https://github.com/tensorflow/tfx/blob/master/tfx/examples/penguin/experimental/penguin_utils_sklearn.py)
      for an example. Furthermore, the book introduces a variety of concepts (e.g.
      model feedback loops, ML Privacy) which transfer well to other frameworks.

      Viele Gruesse,

      Hannes'
- name: Ricky McMaster
  text: 'Thanks a lot for doing this Hannes Hapke

    Given the greater scope/need for scalability in contemporary ML pipelines, do
    you see there being increased chances for bias/prejudices in model development,
    as a result of the need for greater automation?

    Or does the fact that there is increased role specification (e.g. ML engineers
    were fairly rare a few years ago) help to mitigate this, so that this issue could
    be more formally addressed in the development lifecycle?

    Do you discuss this in your book?'
  replies:
  - name: Hannes Hapke
    text: 'Hi Ricky McMaster,

      Re: Bias due to automation - Yes and no. Let me explain. if the training is
      just automated and "forgotten", it will (most likely) lead to a bias in the
      models. But if the pipelines are well set up (e.g. TFMA is cont. tuned), the
      feedback loops continuously analyzed and the model reviewed by a data scientist
      before the final deployment, then I think it can contribute to less bias in
      a model. Why? All model versions are stepping through the exact same steps -
      basically being treated equally and a human can''t cut corners.'
  - name: Ricky McMaster
    text: "Thanks Hannes Hapke.  That\u2019s a really good point about TFMA, I\u2019\
      ll bear that in mind.  But in essence I guess you\u2019re saying it\u2019s the\
      \ same as it ever was - you need to have proper processes and standards in place\
      \ to counteract the risks."
  - name: Hannes Hapke
    text: Yes, it is important to look for the Unknown unknowns.
  - name: Hannes Hapke
    text: as much as possible
  - name: Ricky McMaster
    text: "\U0001F91D"
  - name: Ricky McMaster
    text: "I really wish it wasn\u2019t Donald Rumsfeld that coined this phrase\u2026\
      \ since it\u2019s a good one"
  - name: Hannes Hapke
    text: I totally hear you. Was he the first one using the terminology?
  - name: Ricky McMaster
    text: 'I thought so!  But it seems (thankfully) that he got it from NASA: [https://en.wikipedia.org/wiki/There_are_known_knowns](https://en.wikipedia.org/wiki/There_are_known_knowns)'
- name: Kyle Shannon
  text: "\u2753 Hey Hannes Hapke, thanks for contributing and sharing you knowledge\
    \ with the data community. What does a healthy evolution of an ML product look\
    \ like when trying to POC and iterate? What would be some key things learned to\
    \ make sure to take care of earlier or wait until later to do?"
  replies:
  - name: Hannes Hapke
    text: Hi Kyle Shannon ,
  - name: Hannes Hapke
    text: Great question! We are treating an ML project in two phases. First, solve
      a real business with a model proof of concept. This could be based on a limited
      dataset, in a Jupyter notebook, and with experimental code. Only when the project
      stakeholders see the value in the ML model and you can show that it is solving
      the business problem, then focus on the pipeline development. From that model
      on try to keep the model architecture constant, increase the datasets and automate
      as much as you can. It will be helpful in the long run (e.g. in 6 months when
      you want to update the model architecture or update the model validation). Pipeline
      code is generally cleaner than an experimental Jupyter notebook.
  - name: Kyle Shannon
    text: Thanks Hannes Hapke that makes a ton of sense. As a follow up, how do you
      typically monitor and maintain performance for these models as they evolve once
      pipelined into production?
  - name: Hannes Hapke
    text: We have built a ton of custom code at Digits since I haven't found a managed
      tool for that purpose which checked all boxes. It all ties back to model feedback
      loops to check if the model predictions performed as the users expected.
  - name: Kyle Shannon
    text: What kinds of challenges do you think prevent a tool like this from existing?
      or is it just a matter of time?
- name: Matthew Emerick
  text: A big thank you to Hannes Hapke for doing this!
  replies:
  - name: Hannes Hapke
    text: Thank you Matthew Emerick my pleasure
  - name: Matthew Emerick
    text: I really enjoy interacting with authors of AI related books. It's why I
      review so many of them and link to the authors.
- name: Matthew Emerick
  text: When do you think ML pipelines should be learned in relation to learning ML
    itself?
  replies:
  - name: Hannes Hapke
    text: Hi Matthew Emerick I think it depends where the person is coming from. For
      a DevOps person, it could be their entry point to the ML world, esp. if they
      have data engineering experience. Data scientists would probably first learn
      ML and then focus on the productization of their models.
- name: Matthew Emerick
  text: Do you any ideas for another book?
  replies:
  - name: Hannes Hapke
    text: 'A variety of good books was released recently:

      - Machine Learning Design Patterns (really love this book)

      - Kubeflow Operations Guide

      - Kubeflow for Machine Learning

      All publications provide a good ML Eng overview.'
  - name: Matthew Emerick
    text: "I meant that you would write.  \U0001F642"
  - name: Hannes Hapke
    text: Oh, haha. Yes, TBA :)
- name: Matthew Emerick
  text: What do you of the use of pipelines for AI in general?
  replies:
  - name: Hannes Hapke
    text: I am not sure what you mean. Do you mind rephrasing your question? Thank
      you.
  - name: Matthew Emerick
    text: Do you see a use for pipeline for other AI techniques such as genetic algorithms,
      decision trees, expert systems, cognitive architectures, multiagent systems,
      etc?
  - name: Hannes Hapke
    text: I think the concepts apply to all trained models.
- name: Shankar Somayajula
  text: 'Hannes Hapke What do you think of this potential advantage of implementing
    pipelines via sql? Needless to add, i''m a sql addict :D

    If we''re able to consolidate the entire pipeline processing into a (complicated,
    multi-stage) sql then it''s possible to inject some flexibility into the process
    by deferring config/ETL (or ELT) decisions to runtime and allowing the users freedom
    to experiment with what suits them. I understand that this wont scale well but
    many big data use cases start big but do devolve into small/normal data by the
    time it gets into the Data Scientists ambit once the scope of the analysis is
    defined and implemented.

    E.g: One may want to see the profile of Customers who buy or responded to a mail
    in campaign dealing with two products sold as part of a promotion in a region/country/state
    like Aus or NZ (say)... once we establish the necessary scoping filters of analysis
    this could eminently be in the realm of sql based analysis. Now if we are able
    to do this entire pipeline of analysis via sql (say, db views for data prep to
    cover the etl ot elt part) then via a BI tool we can give freedom to the analyst
    to decide the time period between which the two products could have been bought
    (perhaps same customer bought the two products on different days 8 days apart,
    i.e. not in same transaction ... this can be a hit or a miss depending on analyst/business
    user discretion/decision to consider 8 days separation between events as ok or
    not).

    An interactive UI can allow user to leverage parameterized sql by having a sliding
    bar from 1 (same day) to 10 days and see the effect of the setting on key Campaign
    Metrics. If we did this in the ETL or ELT cycle or in the pipeline then that decision
    is baked in at say 7 days and needs a new instance of the pipeline to modify the
    same from 7 to 10. Business users need to use Notebooks or similar tools to modify
    the setting. Does the what-if tool allow for such flexibility? I know it gives
    flexibility in the analysis part, the data processing part which is post load.
    Can it reach through to give some flxibility/benefit pertaining to the load/transform
    part of the pipeline too?'
  replies:
  - name: Hannes Hapke
    text: Hi Shankar Somayajula I am sorry for my late reply. The What if tool is
      designed for post training model analysis. It helps you perform a model sensitivity
      analysis. I think you can filter your data to test your model with, but only
      in a limit fashion. I don't think the WIT can use the feature engineering from
      TFTransform. Having said this, TFMA wasn't able to use it until recently too,
      so maybe the tool is already able to do so. But I think you are looking for
      a different tool, IMO.
  - name: Shankar Somayajula
    text: Thanks for the response. Hannes Hapke
- name: ankush khanna
  text: 'Hi Hannes Hapke

    How is building ml pipeline different from building data pipelines? And what can
    a data engineer focused on building ETL pipeline move to building ML pipelines?'
  replies:
  - name: Hannes Hapke
    text: 'I think they share a variety of properties, for example scalability, task
      chaining, DAG, etc.

      At the same time, they are also very different. For example, in a data pipeline,
      your main concern is the final outcome (e.g. a transformed dataset). You probably
      don''t want to store snapshots of the artifacts from the individual steps. But
      this is critical for ML pipelines to repeat and reproduce ML models.'
  - name: Hannes Hapke
    text: "Hi ankush khanna \U0001F642"
  - name: ankush khanna
    text: 'Thanks for the answer. What can be some focus points for data engineers
      to learn more about ML pipeline?

      Any open source solutions, tools, languages, you suggest?'
  - name: Hannes Hapke
    text: I think TFX does a god job at introducing the necessary steps in ML pipelines.
      From there, you could take a look at the orchestration of such pipelines.
- name: Clara Matos
  text: "Hi Hannes Hapke \U0001F44B\nThank you for taking the time to answer questions!\n\
    During the data ingestion stage where can we draw the line between what is a data\
    \ pipeline and what is feature engineering? When using tabular data from different\
    \ sources (such as different tables in a data warehouse or relational database)\
    \ is combining the data part of the data pipeline? If so from your experience\
    \ is it commonly performed by data engineers? And then the machine learning engineers\
    \ perform feature engineering on top of the final dataset?\nWhen should the validation\
    \ take place? On top of the final dataset or on top of each table used to build\
    \ the final dataset?\nFrom your perspective what is the best tool/approach to\
    \ building a good (and scalable) data pipeline to feed a machine learning model?\
    \ How do you address training-serving skew? (When serving, the incoming data should\
    \ go through the same data pipeline as during training?)"
  replies:
  - name: Hannes Hapke
    text: Hi Clara Matos, I am sorry for my belated reply.
  - name: Hannes Hapke
    text: 'what is a data pipeline and what is feature engineering?

      I would transform any data in a data pipeline which can be reused by other models.
      Model specific transformations belong in the feature engineering in my opinion.'
  - name: Hannes Hapke
    text: 'Q: If so from your experience is it commonly performed by data engineers?
      And then the machine learning engineers perform feature engineering on top of
      the final dataset?

      A: I think so, however, my colleagues at Digits are going back and forth. Data
      engineerings transition to ML projects and vice versa.'
  - name: Hannes Hapke
    text: 'Q: When should the validation take place? On top of the final dataset or
      on top of each table used to build the final dataset?

      A: I would perform it on the final dataset. Why? Because you want to capture
      all stats/schema changes in respect to the model.

      Checking each table seems a bit more like a data quality task to me. What do
      you think?'
  - name: Hannes Hapke
    text: "Q: How do you address training-serving skew?\nA: TFTransform \U0001F642\
      \ I always try to build the feature engineering on top / inside of the actual\
      \ model"
  - name: Hannes Hapke
    text: TFTransform is really amazing and a great help for our team.
  - name: Hannes Hapke
    text: 'Q: From your perspective what is the best tool/approach to building a good
      (and scalable) data pipeline to feed a machine learning model?

      A: We are using Beam for our data and ML pipelines'
  - name: Clara Matos
    text: '_Checking each table seems a bit more like a data quality task to me. What
      do you think?_

      I see what you mean. Do you think tfx data validation is also suited for data
      quality checks in data pipelines?'
  - name: Clara Matos
    text: Also, have you ever integrated scikit-learn models within a tfx pipeline?
  - name: Clara Matos
    text: "and thank you for taking the time to answer the questions \U0001F603"
- name: Hannes Hapke
  text: 'Anyone interested in the internals of TFX, join the special interest discussions
    here: [https://github.com/tensorflow/tfx-addons](https://github.com/tensorflow/tfx-addons)'
  replies: []
- name: Hannes Hapke
  text: We have a mailing list and bi-weekly meetings to chat about TFX, and addon
    components. The discussion is open to anyone, beginners (very welcome) or experts
    of TFX
  replies: []
- name: Tim Becker
  text: "Hi Hannes Hapke I just finished chapter 2 of your book and it seems to be\
    \ very useful. As you discuss in the book, so far, I have been creating my own\
    \ custom solutions. Using TFX seems to be much easier than I initially thought.\
    \ I have been a little hesitant to look at libraries for pipelines. I thought,\
    \ it is difficult to practice it on my own, because I need datasets that are continuously\
    \ updated, and it might be much more work than the usual data science project.\
    \ But I was probably wrong, and I would like to ask you some related question:\n\
    \ \n- Do you have ideas for toy projects that have a reasonable size with data\
    \ that is regularly updated?\n- If you already have a model, which would be the\
    \ parts of the pipeline you would focus on first? In your experience, what is\
    \ the most crucial part of the pipeline. Where does a data science team benefits\
    \ the most?\n- If you build, for example, a model for stock trading, which metrics\
    \ would you use to monitor that your model is still performing? Do you monitor\
    \ your return? Or the error? Maybe, the drift of the error?\n \nThank you very\
    \ much!"
  replies:
  - name: Hannes Hapke
    text: 'Hi Tim Becker

      Apologies for the late reply.

      - Q: Do you have ideas for toy projects that have a reasonable size with data
      that is regularly updated?

      A: I would check for some time series data, e.g. stock prices. There are probably
      free sources which are updated daily. This would be a great way of showing the
      full benefit of Ml Pipelines'
  - name: Hannes Hapke
    text: '- Q: If you already have a model, which would be the parts of the pipeline
      you would focus on first? In your experience, what is the most crucial part
      of the pipeline. Where does a data science team benefits the most?

      A: I would start with the data validation (e.g. with TFDV or Great expectations).
      It is easy to use, and immediately provides great value. Data scientists will
      probably find interesting snippets about their data sets with such tools. Then
      I would on the model analysis part to compare model versions. Once the data
      scientists see the value in such models, focus on the automation of the entire
      end-to-end process. Here you could use TFX for.'
  - name: Hannes Hapke
    text: '- Q: If you build, for example, a model for stock trading, which metrics
      would you use to monitor that your model is still performing? Do you monitor
      your return? Or the error? Maybe, the drift of the error?

      A: The stock trading problem sounds like a time series forecasting issue to
      me. In such a case, I would pay attention to the mean and std, calculate it
      for a window of 30 days. check if your std is changing drastically. For classification
      problems, I would pay attention to the distribution of the your labels. At Digits,
      we do monitor the predictions and the feedback very closely. TFDV can help you
      to calculate the L-0 norm as an option to detect if your data moved more than
      X%'
  - name: Tim Becker
    text: "Hannes Hapke thank you very much! I will definitely give it a try \U0001F642"
  - name: Hannes Hapke
    text: Let me know how it goes.
---

Companies are spending billions on machine learning projects, but it’s money wasted if the models
can’t be deployed effectively. In this book, Hannes Hapke and Catherine Nelson walk you through
the steps of automating a machine learning pipeline using the TensorFlow ecosystem.
You’ll learn the techniques and tools that will cut deployment time from days to minutes,
so that you can focus on developing new models rather than maintaining legacy systems.