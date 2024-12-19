---
authors:
- nakulbajaj
- jonaschristensen
- manmohangosada
cover: images/books/20240408-data-centric-machine-learning-with-python/cover.jpg
description: Book of the Week. Data-Centric Machine Learning with Python by Nakul
  Bajaj, Jonas Christensen and Manmohan Gosada
end: 2024-04-12 23:59:59
image: images/books/20240408-data-centric-machine-learning-with-python/preview.jpg
links:
- link: https://www.packtpub.com/en-ro/product/data-centric-machine-learning-with-python-9781804618127?type=print
  text: Book's page
- link: https://www.amazon.com.au/Data-Centric-Machine-Learning-Python-high-quality/dp/1804618128/ref=sr_1_1?dib=eyJ2IjoiMSJ9.ES1-C5exEWqe-UJlg6Ui_W3xcj4uPQTlaBnuGCsOG1pWWfU5ZoCyTPvwMjv1SWMpaLbTz9iDp0_1VCewLejDAThUcRNRJHb-XUhXXeGQpCRmMzxQ1OUhbBn0qCyEf0VpBrj2ZKlCwgb-590dFgnHT5fmzz2sX3UqGibX1O59t5x_GX18bWRgmhiiT77_G7JwW7rei0iKypzukVxgo5vkQU0kziza8b__rxO93vUzHsc.MnRR6PaBcNCFg1nxwFOXkccDDAynY-ScGNIrBdpp5ag&dib_tag=se&keywords=data+centric+machine+learning&qid=1709336201&s=books&sr=1-1
  text: Buy on Amazon
- link: https://github.com/PacktPublishing/Data-Centric-Machine-Learning-with-Python
  text: GitHub repository
start: 2024-04-08 00:00:00
title: Data-Centric Machine Learning with Python

archive:
- name: Vivek Kumar
  text: 'Hi, thanks for the book. I have some questions:

    1. While labeling the data what steps can we take for addressing challenges related
    to human error and ambiguity in annotation tasks?

    2. How can we make sure that the new incoming data does not drifts from the original
    training set?'
  replies:
  - name: Nakul Bajaj
    text: 'Thanks for asking the questions Vivek.

      In the book we cover ambiguity in data labelling, and issues associated with
      manual labelling.

      We provide some techniques on handling these issues.

      Some methods used can be programmatic labelling which include:

      1. Pattern Matching

      2. DB lookup

      These are methods associate with using rules and lookup tables to label the
      data.

      We also cover advanced techniques which use machine learning:

      1. Weak supervision

      2. Semi weak supervision

      3. Active learning

      4. Transfer learning

      We also cover combining these and using slicing functions.

      For point number 2:

      I am not sure what do you mean. I usually believe new data is likely to drift
      over a period of time. For instance if your products started to appeal to newer
      demographics or an event like covid happened, which led to model degradation
      across so many organisations.

      Or you are trying to ask a different question?'
  - name: Nakul Bajaj
    text: Manmohan Gosada, your thoughts?
  - name: Jonas Christensen
    text: Adding to Nakul's response, we cover a number of techniques for dealing
      with ambiguity in human annotation tasks. Two examples of innovative techniques
      for this purpose are Gated Instruction and Jury Learning.
  - name: Vivek Kumar
    text: "Thanks Nakul Bajaj &amp; Jonas Christensen\nFor the 2nd question , I see\
      \ what you're getting at. It's not about preventing data drift entirely \u2013\
      \ you're right, that's practically impossible given the dynamic nature of data.\
      \ Instead, what we should focus on is building mechanisms to detect when data\
      \ drift occurs and adapt our models accordingly.\nHow do you envision implementing\
      \ such monitoring and adaptation mechanisms in your specific context?"
  - name: Nakul Bajaj
    text: 'Hi Vivek,

      There are some open source tools such as EvidentlyAI that can help with model
      and data drift. Another one is [https://github.com/SeldonIO/alibi-detect](https://github.com/SeldonIO/alibi-detect)

      Alternatively, there are statistical methods too which measure distribution
      differences between numerical features. or chi-square test for categorical variables.'
- name: Ilya Lukibanov
  text: "Hi, thank you for the book! I've got a few questions:\n- What is your recommendation\
    \ for cases in which we detect a very significant data drift and cannot use all\
    \ of our historical data for modelling the new data generating process? \n   \
    \ \u25E6 For example, you are a data science team in a sports team and you predict\
    \ your team event demand to adjust prices. The only data you have is your team\
    \ performance and your team ticket sales. The team historically had a bad performance\
    \ and mediocre game attendances. However, in current season, the team recruited\
    \ a young player who plays very well and the team has a great season, so, the\
    \ attendance is very high. What the data-centric approach would suggest the data\
    \ science team do in this situation?\n- How do you detect a data/model drift in\
    \ a distributed environment? \n- What would your recommend to do in production\
    \ if you have a single model that serves the whole workflow and you detect a data\
    \ drift for a relatively small subset of customers (~3-5%)?\n- What are your thoughts\
    \ on using LLMs for feature extractions and data cleaning?"
  replies:
  - name: Nakul Bajaj
    text: "Point 1:\nIf I understood correctly that old data might have become irrelevant.\n\
      I can think of few data centric approaches\n1. If the new events are low in\
      \ volume, but their impact is high, we could create synthetic data and oversample\
      \ the new events\n2. We could do some feature engineering, and in historical\
      \ data add a feature associated with \u201Cyoung_player_present\u201D, where\
      \ in old data values will be 0 and in new data values will be 1\nJonas Christensen\
      \ anything else you can suggest?\nPoint 2:\nCan you explain what do you mean\
      \ by distributed environments?\nOne can use statistical methods such as chi-square\
      \ tests, or distance specific tests, distribution tests, etc. to detect data\
      \ drift and features drift. [https://docs.evidentlyai.com/presets/data-drift](https://docs.evidentlyai.com/presets/data-drift)\n\
      Point 3. I think this really depends on business appetite. First one needs to\
      \ build these metrics and monitor them to detect in different segments. I would\
      \ also suggest measuring bias and comparing between training and inference data\
      \ points. If bias has increased, then again we may need to retrain the model\
      \ by reducing bias. This could be done by feature engineering, under sampling\
      \ and oversampling data, or removing/adding examples based on Shapley values\n\
      Point 4: Personally not knowledgeable enough about LLM\u2019s"
  - name: Ilya Lukibanov
    text: 'Nakul Bajaj Thank you for your answers!

      1. Yes, the old data is completely irrelevant in this scenario. It is a real
      world problem that Blackhawks said that they faced. But there can be a different
      scenario where a second league sports team wins it and join a premier league.
      In this case, the past attendance data is not very relevant as well. Think of
      the English Premier League where there are 19 home games in the season or NHL
      where there are 41 home games. You will have a very limited amount of new data.
      Moreover, the attendance can vary a lot between the games, so you cannot simply
      oversample it because there is nothing to sample from and it can be very biased
      for the following games (depending on the schedule - if you play first against
      strong opponents and then weak -&gt; attendance might be higher in the beginning
      of the season and you don''t have any observations against weak opponents).
      In these cases, the data is accurate, but the world has changed and you need
      to create new models that would be more statistical than machine learning (machine
      cannot really learn in this setting, you have to spoon-feed it).

      2. By distributed, I mean you get new data each day that is not able to be fit
      on a single machine. Let''s say you are Uber and you get data on million of
      trips each day that come from different markets (different city sizes, different
      countries), do you still you a single metric for each feature from a list that
      you provided above to monitor the data quality? For example, you can compare
      the distribution of all trip lengths, but will it be informative to you? What
      would the book suggest to do in this scenario?

      3. Let''s say you have tens of millions observations, do you still use the same
      methods that you suggested above?'
  - name: Nakul Bajaj
    text: 'The way to know when data has drifted, is we compare the data or statistical
      features of the data on which the model was trained vs the data on which inference
      is performed.

      As the new data coming in inference is being performed on this data. All these
      predictions are stored on systems or databases that are quite performant and
      can work with big distributed data. Monitoring can run on these systems. If
      there is an API and each data point is predicted with one request, then drift
      is not calculated at that time. However if batch inference is done, then engineers
      can build a system for each batch , if the batch of data has drifted from original
      data.

      This is more an engineering lense on how to do this, but was not covered in
      the book.'
- name: Ramazan Abylkassov
  text: 'Hey everyone!

    Any tips on how to maintain idempotency of the ETL task?'
  replies:
  - name: Nakul Bajaj
    text: 'We didnt cover data warehousing concepts in the book, as you can tell from
      the title data centric machine learning.

      However, I have some suggestions for ETL.

      1. UPSERT (Assuming you have the unique key)

      2. DELETE and then INSERT UNIQUE records

      If you are using a modern stack or ELT

      1. You insert the data and stage the data. You then clean the data in the warehouse
      and move it to the next layer.

      2. You can use DBT with modern data warehouses, that do T part of ELT. using
      the unique key defined, it can check which data is already there and which one
      needs to be added. One can leverage incremental and snapshot strategies'
- name: Carlos Orjuela
  text: 'Hi, thanks for taking the time to answer our questions. I recently came across
    a chat between Ben Lorica and Sebastian Raschka on The data exchange podcast where
    Ben gave an opinion on the lines of the newly data-centric ML concept (it was
    back in 2022) being a bit redundant. I believe I saw some discussion around the
    same on X, probably from author Andriy Burkov although can''t recall it for sure.

    I''d love if you can chime in on the discussion. Thanks!'
  replies:
  - name: Jonas Christensen
    text: "Hi Carlos, I don't know what arguments were used to say that DCML is redundant,\
      \ but we obviously disagree since we've gone to the effort of writing a book\
      \ about it!\nThe traditional focus on model-centric approaches, where the primary\
      \ emphasis is on improving algorithms and tuning hyperparameters, has indeed\
      \ led to significant advancements in ML. However, this model-centric view has\
      \ its limitations, particularly when deployed in real-world applications across\
      \ various domains. In reality, most of us don't work for a FAANG where data\
      \ and resourcing are typically abundant and created in a controlled environment.\n\
      Instead, we work in the long tail of ML problems where datasets are smaller\
      \ (and often more complex), and use cases are higher risk. In the long tail\
      \ it can be hard to find a ML project worth $50m, but it's often possible to\
      \ find 50 projects worth $1m. These use cases might not be \"big data\" so we\
      \ need another way to unlock them - through increasing signal and reducing noise\
      \ in our \"small\" dataset.\nAs I see it, the 3 main evolutions of DCML are:\n\
      *1. Addressing data quality*: The shift towards data-centric ML emphasises the\
      \ importance of data quality, not just quantity. In many real-world applications,\
      \ the adage \"garbage in, garbage out\" holds true \u2013 no matter how sophisticated\
      \ an algorithm is, its output is only as good as the input data. Data-centric\
      \ approaches prioritise cleaning, labelling and curating high-quality datasets,\
      \ which are foundational for robust and reliable AI systems.\nEven ChatGPT is\
      \ built on lots of data-centric activity, see these examples:\n[https://me.mashable.com/tech/27956/the-human-cost-of-chatgpts-success-openais-unfair-treatment-of-data-labelers](https://me.mashable.com/tech/27956/the-human-cost-of-chatgpts-success-openais-unfair-treatment-of-data-labelers)\n\
      [https://www.nextbigfuture.com/2023/02/chatgpt-has-a-human-team-train-it-to-be-a-lot-better.html](https://www.nextbigfuture.com/2023/02/chatgpt-has-a-human-team-train-it-to-be-a-lot-better.html)\n\
      *2. Reducing bias and enhancing fairness*: By focusing on the data used to train\
      \ ML models, we can more effectively identify and mitigate biases that may be\
      \ present. This is critical for developing fair and ethical AI systems, especially\
      \ as these technologies are increasingly applied to sensitive areas such as\
      \ healthcare, finance, and law enforcement.\n*3. Broadening accessibility*:\
      \ Data-centric ML democratises ML development. Not every organisation or individual\
      \ has the resources to develop cutting-edge algorithms, but with a focus on\
      \ improving data quality, smaller teams and organisations can make meaningful\
      \ contributions to ML advancements. This broadens the accessibility of ML development\
      \ and encourages innovation from a diverse range of contributors."
  - name: Carlos Orjuela
    text: Thanks heaps Jonas Christensen. Much appreciated!
- name: Farid T.
  text: "I posted this question in a thread in another (inactive) channel. At the\
    \ risk of looking very ignorant, I\u2019m going to pose it here as well:\nMay\
    \ I ask: when you \u201Cread\u201D a book on a technical topic, how do you do\
    \ the actual reading? Do you read every paragraph of every chapter in order? How\
    \ about the hands-on parts? Do you stop and implement the code yourself? And how\
    \ long does a typical O\u2019Reilly book take to finish on average?\nI love reading\
    \ but I never thought it possible to actually read a technical book with everything\
    \ else I have my fingers in. I\u2019m wondering how people do it.\nWould appreciate\
    \ responses and insights from anyone and everyone. \U0001F64F"
  replies:
  - name: Alexey Grigorev
    text: I read with a pen and a notebook, and add notes. this way not only I read
      slower, but also more thoroughly. If I read fast, my brain doesn't retain anything
- name: Francisco Delca
  text: 'Hey,

    Thank you for the book, its a really important topic to cover, my questions are:


    1. How can human judgment be efficiently included in data labeling processes?

    2. What key strategies do you recommend for effectively using ''small data''?

    3. What is the value of synthetic data in data-centric ML projects?

    4. What are the first steps for adopting data-centric ML practices?'
  replies:
  - name: Nakul Bajaj
    text: '1. One of the key principles of data-centric approach is human in the loop
      approach. Using domain expertise and creating rule based programmatic labelling
      can be one approach. Or ensuring spending huge effort on accurately labelling
      a small sample of data, then applying active learning and providing probability
      scores back to humans, where low probability scores can be updated by humans.
      Any further thoughts Manmohan Gosada?

      2. Data centric approach recommends that ensuring high data quality in small
      samples can lead to great results. We can measure the quality of the data across
      6 dimensions. Is the data consistent? Is data accurate? Is data up to date?
      Is data unique? Is data complete ? Is the data valid? As data practioners we
      should iterate over this data and make it top-notch quality. We should also
      speak to data producers and ensure they understand how data consumers are using
      the data, so there could be data contracts in place. This is one of the longest
      chapter in the book.

      3. Synthetic data can help with creating rare events, help with reducing bias,
      help with generalisation, help with improving the signal of the data points,
      where model was making mistakes previously? Any other thoughts Jonas Christensen?

      4. Usually, data-centric approaches are thought about where model-centric approaches
      fall short, and when data-scientist , ml engineer has spent days/weeks on tuning
      the algorithms. We want to change that paradigm. We think as data-scientists
      and data-engineers , we start ensuring data coming in the organisation is good
      quality and start measuring data quality. Once we have that, then model-centric
      approaches should be thought about. Data-centric approaches can make data-scientists
      more confident in their results. Any thing you would like to add Jonas Christensen
      and Manmohan Gosada?'
  - name: Jonas Christensen
    text: 'Great questions Francisco Delca! Nakul Bajaj has done a good job providing
      answers, but I will add a couple of points:

      1. We describe a range of techniques for this purpose in the book and also share
      our own experience of combining ML with subject matter expert opinions. There
      is a lot that can be done to include human judgement, but at the end of the
      day, it comes down to a combination of very clear instructions, iterative loops
      and also aligning incentives of labellers with your goals. The last point is
      often missed. Here''s a simple example: if a call centre agent is incentivised
      to wrap up calls quickly they may not collect as much data (or the *right data*)
      as the data science team would like. If you can align incentives then the right
      information is more likely to get captured. Sometimes it''s enough to just explain
      the bigger picture of how the collected/labelled data is used, for labellers
      to change their behaviours.

      2. When it comes to "small data", it often depends on the specific use case.
      However, I find it helpful to ask myself "if I only had 1000 rows in my dataset,
      what would it need to contain to be used for my model?" That question can help
      you think about the depth and breadth of observations/features needed, but also
      that you need to define which are the most important kinds of observations for
      the model to understand and distinguish between objects, classes or whatever
      you''re modelling.'
  - name: Francisco Delca
    text: "Thank you Nakul Bajaj for the clarifications. I recently took a course\
      \ for AI Product Manager and my key takeaways are a lot related with a data\
      \ centric approach. They were:\n- \U0001D413\U0001D421\U0001D41E \U0001D429\U0001D428\
      \U0001D430\U0001D41E\U0001D42B \U0001D428\U0001D41F \U0001D403\U0001D41A\U0001D42D\
      \U0001D41A: Effective AI begins with a solid data strategy. The key is initiating\
      \ a data flywheel process that focuses on collecting quality data, optimizing\
      \ for speed in data preparation, and continuously refining models with new insights.\
      \ It's all about harnessing the power of iterative improvement for maximum impact.\n\
      - \U0001D404\U0001D426\U0001D41B\U0001D42B\U0001D41A\U0001D41C\U0001D422\U0001D427\
      \U0001D420 \U0001D42D\U0001D421\U0001D41E \U0001D414\U0001D427\U0001D41C\U0001D428\
      \U0001D426\U0001D426\U0001D428\U0001D427: Incorporating long-tail data is essential\
      \ for AI's ability to handle both common and rare scenarios, enriching the data\
      \ flywheel with diversity and depth."

---

In the rapidly advancing data-driven world where data quality is pivotal to the success of machine learning and artificial intelligence projects, this critically timed guide provides a rare, end-to-end overview of data-centric machine learning (DCML), along with hands-on applications of technical and non-technical approaches to generating deeper and more accurate datasets. This book will help you understand what data-centric ML/AI is and how it can help you to realize the potential of ‘small data’. Delving into the building blocks of data-centric ML/AI, you’ll explore the human aspects of data labeling, tackle ambiguity in labeling, and understand the role of synthetic data. From strategies to improve data collection to techniques for refining and augmenting datasets, you’ll learn everything you need to elevate your data-centric practices. Through applied examples and insights for overcoming challenges, you’ll get a roadmap for implementing data-centric ML/AI in diverse applications in Python. By the end of this book, you’ll have developed a profound understanding of data-centric ML/AI and the proficiency to seamlessly integrate common data-centric approaches in the model development lifecycle to unlock the full potential of your machine learning projects by prioritizing data quality and reliability.