---
authors:
- yuantang
cover: images/books/20240115-distributed-machine-learning-patterns/cover.jpg
description: Book of the Week. Distributed Machine Learning Sytems by Yuan Tang
end: 2024-01-19 23:59:59
image: images/books/20240115-distributed-machine-learning-patterns/preview.jpg
links:
- link: https://www.manning.com/books/distributed-machine-learning-patterns
  text: Book's page
- link: https://www.amazon.com/Distributed-Machine-Learning-Patterns-Yuan/dp/1617299022
  text: Buy on Amazon
- link: https://github.com/terrytangyuan/distributed-ml-patterns
  text: GitHub repository
start: 2024-01-15 00:00:00
title: Distributed Machine Learning Patterns

archive:
- name: luca pugliese
  text: Thank You very much to Yuan Tang for the interesting topic treated and for
    the answers received during this week! Thanks to DTC and in particular to Francis
    Terence Amit for the assistance.
  replies: []
- name: Prajwal Srinivas
  text: "Hello Yuan\U0001F44B\n1. What would be the prerequisite knowledge required\
    \ to learn from this book?\n2. At what point do we decide that a distributed ML\
    \ architecture is required?\n3. With the advent of LLMs and generative AI and\
    \ these APIs being available at a reasonable cost, how prevalent are fundamental\
    \ ML models now?\n4. Can the patterns be applied to Large Language Model based\
    \ applications too?\nThank you for organizing this Q and A\U0001F604"
  replies:
  - name: Yuan Tang
    text: '1. Check out ["about the reader" section here](https://github.com/terrytangyuan/distributed-ml-patterns/tree/main#about-the-reader):
      "for data analysts, data scientists, and software engineers familiar with the
      basics of machine learning algorithms and running machine learning in production.
      Readers should be familiar with the basics of Bash, Python, and Docker".

      2. When you have much larger dataset, larger models, and more complex ML workflows.

      3. Fundamental ML models still have their success in many domains and have been
      proven to work well in their current applications where leveraging LLMs may
      not be necessary or applicable. LLMs are growing fast but the side effects still
      need to be studied and their compliance and trust need to be gained over time.

      4. Yes! Large models still need to be trained and served efficiently in real-world
      applications. With the foundational patterns for distributed ML, the process
      would be more efficient, scalable, and reliable.'
- name: Wale Abiodun Ogundeji
  text: Hi Yuan Tang, how can get the book Distributed Machine Learning Systems?
  replies:
  - name: Yuan Tang
    text: "- Amazon: [https://www.amazon.com/dp/1617299022/](https://www.amazon.com/dp/1617299022/)\n\
      - Barnes &amp; Noble: [https://www.barnesandnoble.com/w/distributed-machine-learning-patterns-yuan-tang/1140209010](https://www.barnesandnoble.com/w/distributed-machine-learning-patterns-yuan-tang/1140209010)\n\
      - Powell\u2019s: [https://www.powells.com/book/distributed-machine-learning-patterns-9781617299025](https://www.powells.com/book/distributed-machine-learning-patterns-9781617299025)\n\
      - Bookshop: [https://bookshop.org/p/books/distributed-machine-learning-patterns-yuan-tang/17491200](https://bookshop.org/p/books/distributed-machine-learning-patterns-yuan-tang/17491200)\n\
      - Manning: [https://bit.ly/2RKv8Zo](https://bit.ly/2RKv8Zo)"
- name: Alex Litvinov
  text: "Hi! I have a question about TPUs. They seem to be amazing at least from the\
    \ first glance, I tried training CNNs on it on Kaggle and Google Colab and it\
    \ significantly sped up the training process. yes, one needs to change their code\
    \ in comparison to the training on GPU but it seems like a minor thing. Yet I\
    \ have the impression that TPUs are not getting a wide adoption, the majority\
    \ of the training that I see is happening on GPU. I might be very wrong, I haven't\
    \ done a deep analysis either. \nso, what's your take on it?"
  replies:
  - name: Yuan Tang
    text: This is beyond the scope of the book. The success of these hardware highly
      depend on the marketing, sales, and partnership from their vendors, as well
      as the community adoption.
  - name: Victor Arias Vanegas
    text: i used TFrecords and google storage (make sure that you are in the same
      region) for distributed training with TPUs, the speedup is amazing for the pro
      subscription price!
- name: Low Kim Hoe
  text: Hi Yuan Tang, for the distributed training, do you using Spark to perform
    the training or else tools?
  replies:
  - name: Yuan Tang
    text: 'These main technologies are used in this book: TensorFlow, Kubernetes,
      Kubeflow, and Argo Workflows.'
  - name: Low Kim Hoe
    text: "Alright thanks for the reply \U0001F604"
- name: Naeronatin Reditor
  text: Hi Yuan, why sometimes for some models using a single GPU is better than a
    cluster?
  replies:
  - name: Yuan Tang
    text: This highly depends on the model architecture and your distributed settings.
      With a cluster, there will be more things involved like network communications
      and data transfers among machines in the cluster.
- name: Peter Ernicke
  text: 'Hi Yuan,

    the second part of this book is about "PATTERNS OF DISTRIBUTED MACHINE LEARNING
    SYSTEMS". I like patterns as a guideline in complex processes and also to standardize
    things. I wonder that these patterns are also helpful just in normal ML system?'
  replies:
  - name: Yuan Tang
    text: By "normal ML system", do you mean non-distributed ML systems? If so, then
      yes there are certain chapters such as operational patterns and workflow patterns
      that can be useful for single-machine use cases as well.
  - name: Peter Ernicke
    text: "Oh yeah sry, of course I mean non-distributed ML systems \U0001F642"
- name: Peter Ernicke
  text: 'Maybe two more general questions: What are some of the most common challenges
    that developers face when building distributed machine learning systems? How do
    you address these challenges in your book?'
  replies:
  - name: Yuan Tang
    text: 'Each pattern chapter is divided into three sections: problem, solution,
      discussion. The problem section outlines the challenges whereas the solution
      section introduces the pattern that address those challenges.'
- name: Peter Ernicke
  text: What inspired you to write a book on distributed machine learning? Was there
    a particular experience or challenge that motivated you to share your knowledge
    with others? What do you think are the most promising applications of distributed
    machine learning in the near future?
  replies:
  - name: Yuan Tang
    text: There was no similar book in the market and I felt the need to have a collection
      of patterns that are commonly used in the industry so that people who are interested
      can get into the engineering and infrastructure perspectives of the ML world.
      I was working with both engineering and data science teams and it was difficult
      to communicate with each other due to lack of experience in this area. Data
      science practitioners were used to train models on their laptops and built small
      web applications that makes predictions based on the trained models. Now as
      the datasets and models get larger, the need for building distributed ML systems
      is stronger than ever.
- name: Nisar Ahmed Shariff
  text: Yuan Tang My next question is regarding using trained model to respond to
    requests. During model serving one obvious way to increase response throughput
    is to have multiple instances of model running and have a load balancer before
    it. This is similar to having multiple pods running and ingress controller takes
    care of load balancing. And then we can use k8s pod auto scaling features to scale
    up and down based on traffic. I do not have in-depth knowledge of model serving
    processes. My actual question is - Is there any other way of getting throughput
    in model serving similar to how we get higher throughput by using non-blocking
    async processing for non-ML applications?
  replies:
  - name: Yuan Tang
    text: 'Great questions. We will cover some of these in the model serving patterns
      chapter, leveraging Kubernetes and [KServe](https://github.com/kserve/kserve).

      As to your question regarding increasing throughput, non-blocking async processing
      would certainly help but there are more optimizations you can do. I''d recommend
      looking into technologies like [vLLM](https://github.com/vllm-project/vllm)
      that provides a high-throughput and memory-efficient inference and serving engine
      for LLMs. It leverages techniques like PagedAttention, continuous batching of
      incoming requests, quantization, etc. They also [published a paper](https://arxiv.org/abs/2309.06180)
      if you''d like to dive into the details. This is beyond of this book but this
      book helps you build the right model serving infrastructure to support the use
      of different model serving runtimes.'
  - name: Nisar Ahmed Shariff
    text: Thanks for all inputs. I think now I have stuff for me to study and do some
      homework. Thanks again for the links.
- name: Dr Abdulrahman Baqais
  text: 'Hello Yuan Tang. Thank you for the book. few questions in mind:

    1)How many of these patterns are known by practitioners?

    2) At what stage do you believe  practioners should follow pattern-based practices
    ( Ingestion, dev , deployment).

    3) Are patterns adopted by ML engineers are enough to ensure successful delivery
    of ML models, Or we need to a full ML process across the team similar to Software
    engineering processes. And a follow up one, do you think researchers and practioners
    can find a process that ensure rapid development, incremwntal delivery and high
    ROI of ML models. Something that is better than CRISP.

    Thank you for your responce and insights.'
  replies: []
- name: luca pugliese
  text: Though, if I correctly understood, the use cases for the adoption of distributed
    design patterns origin from facing some large scale component (big dataset, high
    traffic on the server,...) could it be a sensible thing start locally by making
    a small scale prototype without the use of cloud resources. As an example, by
    making use of 2 or three machines (laptops/PCs) connected in a LAN , just to test
    the communication part of the final distributed system?
  replies: []
- name: Yuan Tang
  text: 'Congrats to all the winners and thanks for all the questions!

    Here are my social links if you''d like to follow what I am working on: [LinkedIn](https://www.linkedin.com/in/terrytangyuan),
    [Twitter/X](https://twitter.com/TerryTangYuan), [Mastodon](https://fosstodon.org/@terrytangyuan),
    [GitHub](https://github.com/terrytangyuan)

    Thanks Alexey Grigorev for inviting me to this fun event and Francis Terence Amit
    for coordinating it!'
  replies:
  - name: Alexey Grigorev
    text: Thanks for doing it!
- name: Ali Manson
  text: "\U0001F44B Hi everyone! My name is Ali Manson and I'm from Germany.\nI am\
    \ finding peoples from US, UK, Canada, Philippines, Australia and India who can\
    \ work with me.\nIf you're interested in my suggestion, contact me."
  replies: []
- name: luca pugliese
  text: Is training of a generative AI model with several billions of paramaters a
    possible use case for distributed ML, especially if the model need periodical
    retraining? Do you mention something about this use case in the book?
  replies:
  - name: Yuan Tang
    text: 'Yes, the models are being saved as checkpoints regularly so you can easily
      continue training from existing checkpoints using your favorite ML framework
      without training the model from scratch. You can continue training in a distributed
      fashion as well leveraging the distributed training patterns introduced in the
      book or their variations.

      This specific use case isn''t explicitly mentioned in the book but the assumption
      is that once you build up the fundamental knowledge, you should be able to do
      some quick research to figure out how to customize for your specific needs.
      For example, in this case, you should be able to add a `ModelCheckpoint` callback
      that can be used in `model.fit()`.'
  - name: luca pugliese
    text: "Thank you! \U0001F44D"
- name: "Philip Die\xDFner"
  text: "Hello Yuan Tang, thanks for being here.\n Are the patterns and solutions\
    \ in your book also applicable and useful when working with a provided distributed\
    \ environment Databricks or is it for a pure build-it-yourself approach?"
  replies:
  - name: Yuan Tang
    text: It's for building distributed ML infrastructure from scratch without relying
      on any vendors. However, understanding the different patterns would be helpful
      if you want to build a career towards engineering or want to collaborate across
      different teams.
- name: "Philip Die\xDFner"
  text: How was your writing process for the book and long did it take?
  replies:
  - name: Yuan Tang
    text: I started planning and writing the book back in 2020 but fortunately Manning
      has a MEAP program so that each chapters can be made available to the public
      as soon as they finish without waiting for the entire book to finish. The first
      partially completed draft of the book was made public in 2021 (within a year).
- name: Yuan Tang
  text: 'Thanks everyone for all the great questions this week!

    Quick news to share: Distributed Machine Learning Patterns is now available in
    ePub and liveBook formats in case you''d like to add it to your digital collection!
    [https://bit.ly/2RKv8Zo](https://bit.ly/2RKv8Zo)'
  replies: []
- name: Nisar Ahmed Shariff
  text: Hi Yuan, As a person trying to understand ML process management improvements,
    I see this topic is of interest to me. I have been in solutioning Data intensive
    products delivering on k8s platfom. I am wondering how ML training, serving, and
    feedback loop back to improve model quality canbe made parallel. Can larger ML
    models be partially trained and combined similar to map-reduce patterns to increase
    parallelism? Does this book throw light into these aspects? What do you suggest
    me to get a good understanding of this?
  replies:
  - name: Yuan Tang
    text: 'Great question. The feedback loop is very important in real-world ML applications.
      Chapter 5 in the book talks about different patterns you can use to compose
      from simple to complex ML workflows where you can construct your feedback loop
      among the steps (e.g. model training and serving). It also mentions the use
      of ensemble models that are combinations of multiple models.

      Regarding whether larger ML models can be partially trained and combined similar
      to map-reduce patterns to increase parallelism, you can certainly do that if
      your choice of ML frameworks supports that functionality. There are primitives
      in ML frameworks like TensorFlow to allow you customize distributed training
      logic and control what part of the models need to be sharded or computed in
      different devices. This is beyond the scope of this book but the patterns introduced
      in this book would certainly help you build a solid foundation for further research.'
  - name: Brent Brewington
    text: 'Nisar Ahmed Shariff are you familiar with Kubeflow?  It''s the ML toolkit
      for Kubernetes [https://www.kubeflow.org/](https://www.kubeflow.org/)

      Google''s Vertex AI pipelines work with it: [https://cloud.google.com/vertex-ai/docs/pipelines/build-pipeline](https://cloud.google.com/vertex-ai/docs/pipelines/build-pipeline)'
  - name: Nisar Ahmed Shariff
    text: Thank YouYuan Tang. Brent Brewington Thank you for the link, I was going
      through Kubeflow - Certain a thing that I will try. Also ML-Ops ([https://ml-ops.org/](https://ml-ops.org/)).
      Trying to understand and compare in terms of how these frameworks take on dividing
      and distributing the work.

---

Distributed machine learning systems allow developers to handle extremely large datasets across multiple clusters, take advantage of automation tools, and benefit from hardware accelerations. This book reveals best practice techniques and insider tips for tackling the challenges of scaling machine learning systems.

In Distributed Machine Learning Patterns you will learn how to:

- Apply distributed systems patterns to build scalable and reliable machine learning projects
- Build ML pipelines with data ingestion, distributed training, model serving, and more
- Automate ML tasks with Kubernetes, TensorFlow, Kubeflow, and Argo Workflows
- Make trade-offs between different patterns and approaches
- Manage and monitor machine learning workloads at scale

Inside Distributed Machine Learning Patterns you’ll learn to apply established distributed systems patterns to machine learning projects—plus explore cutting-edge new patterns created specifically for machine learning. Firmly rooted in the real world, this book demonstrates how to apply patterns using examples based in TensorFlow, Kubernetes, Kubeflow, and Argo Workflows. Hands-on projects and clear, practical DevOps techniques let you easily launch, manage, and monitor cloud-native distributed machine learning pipelines.
