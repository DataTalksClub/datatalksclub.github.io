---
authors:
- chiphuyen
cover: images/books/20220627-designing-machine-learning-systems/cover.jpg
description: Book of the Week. Designing Machine Learning Systems by Chip Huyen
end: 2022-07-01 23:59:59
image: images/books/20220627-designing-machine-learning-systems/preview.jpg
links:
- link: https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/
  text: Book's page
- link: https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969
  text: Buy on Amazon
- link: https://github.com/chiphuyen/machine-learning-systems-design
  text: GitHub repository
start: 2022-06-27 00:00:00
title: Designing Machine Learning Systems

archive:
- name: Michal
  text: 'Hello, what do you think about end to end ML solutions? Tools that will help
    you do more than just one thing (for instance: training, monitoring, and serving).
    Are we going this way or specialized libraries (that do one thing exceptionally)
    for each task are the future?'
  replies: []
- name: Michal
  text: 'Also, one more thing. Do you cover testing ML models before putting it in
    production in your book?

    Thanks for coming here and answering some questions!'
  replies:
  - name: Chip Huyen
    text: yes!! half of chapter 6 and half of chapter 9!
- name: Dr Abdulrahman Baqais
  text: Hi, Is this book targeting data scientists or machine learning engineers more
    closely?
  replies:
  - name: Chip Huyen
    text: 'depends on how you define data scientist / ML engineer. they''re defined
      differently at different orgs

      this book discusses ml systems as whole, so i believe it has a lot of relevant
      points for both DS and MLEs'
- name: Dr Abdulrahman Baqais
  text: Can the design be applied to deep learning , NLP, recommendation systems?
  replies:
  - name: Chip Huyen
    text: 'yes'
- name: Dr Abdulrahman Baqais
  text: Does the book explore preML-modeling stages such as Data Engineering? Modern
    data stack?
  replies:
  - name: Chip Huyen
    text: yes, chapter 3 discuss data engineering
- name: Dr Abdulrahman Baqais
  text: Does it explore ML systems in the cloud? For embedded deviced? or at the edge?
  replies:
  - name: Chip Huyen
    text: yes, that's what chapter 7 is about
- name: Shaksham Kapoor
  text: "First of all, I would like to thank you Chip Huyen for all that you have\
    \ done (and still do) for the ML community \U0001F642 \U0001F64F I learn something\
    \ new almost every time I read your blog.\nMy question to you is - *what do you\
    \ think are the bare essentials that a data scientist need to know?* \n&gt; *Context*:\
    \ \n&gt; I have seen poorly defined JDs where the expectations from a data scientist\
    \ is to literally know anything and everything between ML and DevOps. The issue\
    \ that I see with such roles is that these are separate fields, and getting a\
    \ mastery over either of them is challenging (let alone both) given the rapid\
    \ pace in which the fields evolve. I am a core data science person and I am good\
    \ at it; however, I know that there are still a lot of things in data science\
    \ (alone) that I need to learn to become a complete data scientist. \n&gt; \n\
    &gt; Having said that, I also want to gain experience in other components of ML\
    \ lifecycle, but where do you draw the line when you say \"this much\" of DevOps\
    \ is sufficient for a data scientist to know."
  replies:
  - name: Chip Huyen
    text: thanks Shaksham Kapoor for your kind words!
  - name: Chip Huyen
    text: 'agree that JDs can be ambiguous. at the same time, different orgs have
      different challenges. 2 data scientists at 2 different companies, even same
      company on different teams, can do very different things.

      i''d work at it backwards. figure out what teams you want to join, read their
      tech blogs / look at their JDs / talk to people on their team and figure out
      what problems they care about'
  - name: Shaksham Kapoor
    text: 'I agree. I have observed the following in my experience:-

      - Startups (any stage) - they require an all-rounder, who knows anything and
      everything.

      - Mid-size firms (&gt;1000 to &lt;=10000) - there is a split. Some require an
      all-rounder, while others don''t.

      - Large-size firms (&gt;=10000) - they don''t need an all-rounder but an expert.
      I believe the main reason for this is the presence of separate teams (sometimes
      departments) that takes care of different components of ML, so one can get a
      chance to really focus on core ML stuff.'
- name: Dan Gurin
  text: What do you perceive as the biggest challenges / opportunities on the horizon
    for the future of machine learning?
  replies:
  - name: Chip Huyen
    text: real-time ML!
- name: Jeanine Harb
  text: 'Hello Chip Huyen! Thank you for this book, can''t wait to read it!

    From what I''ve seen in the field, a lot of ML projects have a hard time getting
    into production. In your opinion, what are the biggest hurdles and how can companies/organizations
    overcome them?'
  replies:
  - name: Chip Huyen
    text: 'nice to meet you Jeanine! i think the biggest hurdle is that companies
      don''t invest enough into infra to enable data scientists to do their jobs.
      ml production is largely an infra problem.

      hiring infra engineers doesn''t solve it though. infra engineers will need to
      work closely with data scientists to understand their workflows. not all companies
      have their communication channels set up to enable cross-functional team communication.'
- name: Sergio Rozada
  text: "Hi Chip Huyen! It\u2019ll be a pleasure to read your book, seems really insightful!!\
    \ I would love to hear your opinion about batch vs online inference. Thank you\
    \ very much!"
  replies:
  - name: Chip Huyen
    text: "i have 10 pages in my book discussing batch vs. online prediction alone\
      \ so not sure how to respond to this in a message \U0001F605"
- name: Contato Rupp
  text: Hi Chip Huyen! In your opinion, which aspect of ML system designs is particularly
    hard to iterate on? and when should teams think about a complete redesign of their
    systems?
  replies:
  - name: Chip Huyen
    text: "devops track metrics such as:\n- change failure rate: how often does new\
      \ update fail?\n- time to detection: how long does it take to detect a problem\n\
      - time to response: after a problem is detected, how long does it take to address\
      \ it\nwe should track similar metrics in mlops. how often does new models fail?\
      \ how long does it take to discover new model failure? how long does it take\
      \ to update models / debug the systems?\nteams should think about redesign whenever\
      \ those metrics fail short of their expectations.\nand if they can't track those\
      \ metrics, they should definitely consider redesign \U0001F642"
- name: Shaksham Kapoor
  text: Another question for you Chip Huyen - how do you keep yourself updated with
    the breath and depth of techniques that are available/upcoming in data science?
  replies:
  - name: Chip Huyen
    text: by working with people smarter than me!
- name: adanai
  text: 'Hi Chip, thank you for the work you do and the QnA! I hope to earn an in-person
    interaction opportunity with you someday!

    Q: What are some strategies for data collection to approach problems. What is
    the role of data ethics in the process?'
  replies:
  - name: Chip Huyen
    text: great question. data ethics is a nuanced topic that i don't think i can
      discuss in one message. chapter 4 covers data collection [https://github.com/chiphuyen/dmls-book/blob/main/ToC.pdf](https://github.com/chiphuyen/dmls-book/blob/main/ToC.pdf)
- name: adanai
  text: 'Q: What are few critical points to keep in mind for scalability of the system?
    Should scalability be planned for in the initial design of the ML  system or can
    it be planned in future iterations when the need arises?'
  replies:
  - name: Chip Huyen
    text: 'depends on when you anticipate the scaling issues to arise: a week from
      now or a year from now?

      i''m a big fan of scalability, but i''m not a fan of premature optimization
      [https://wiki.c2.com/?PrematureOptimization](https://wiki.c2.com/?PrematureOptimization)'
  - name: adanai
    text: Thank you for the insight! I agree; it is more important to get things running
      than implement the system to perfection.
- name: adanai
  text: 'Q: For someone trying to dive deeper into ML, how should they pick a specific
    branch to attain mastery. I am interested in a number of branches in ML (NLP  |
    CV | Time series | ...), but unable to choose one specifically. Do you suggest
    a framework for the same?'
  replies:
  - name: Chip Huyen
    text: 'you know the venn diagram that says to choose the intersection of:

      1. what you''re interested in

      2. what the world needs

      3. what you''re good at

      it sounds like all branches of ML are pretty needed right now (though time series
      and tabular data might be a little bit underrated compared to CV &amp; NLP)

      i''d choose based on what problems interest me and what i''m good at'
  - name: adanai
    text: I think it's called `Ikigai` . Will keep this framework in mind going further
      on
  - name: Chip Huyen
    text: good luck!
- name: Ashish Lalchandani
  text: 'Hello Chip Huyen! Thanks for being here! My question is :

    1. As someone who is looking to switch from data engineering to MLOps, what are
    the skills required for it and what is the best way to prepare for interviews?
    By focusing more on projects?

    2. How to determine the right amount of MLOps for a project?'
  replies:
  - name: Chip Huyen
    text: '1. yes, real-world projects. but it can be difficult if you don''t already
      work at any company already.

      2. the right amount is whatever is needed to achieve the project''s goals!

      i also wrote a free book on interviews -- hope that helps! [https://github.com/chiphuyen/ml-interviews-book](https://github.com/chiphuyen/ml-interviews-book)'
  - name: Ashish Lalchandani
    text: Oohh great, you have written on interviews too, awesome! Thanks for contributing
      so much to the community,  much appreciated!
- name: Sergio Rozada
  text: Hello Chip Huyen, another question here, can you share any insight into how
    to make scalable systems with large models (e.g. transformers)? Thank you very
    much!!
  replies:
  - name: Chip Huyen
    text: 'hi Sergio, thanks for your question! i''d need more context on:

      - how your system fails at scale (e.g. higher latency, higher cost)

      - where does your system fail when scaling (e.g. if it''s high latency at inference,
      is it due to network latency or model latency), etc....'
  - name: Sergio Rozada
    text: "Hi Chip, thanks your answer, for the sake of clarity:\n- You just hit the\
      \ point! In our case, we struggle a lot to improve in terms of latency keeping\
      \ the costs controlled. We\u2019re running on a Kubernetes cluster in GCP (managed\
      \ by us).\n- Our main latencies are model latencies."
- name: "Utku Sava\u015F"
  text: Hi Chip Huyen, how should we perform monitoring on computer vision related
    projects? Thank you.
  replies:
  - name: Chip Huyen
    text: "this would be a looooong answer \U0001F62D  maybe we can start with: what\
      \ problems do you have with monitoring CV projects rn?"
  - name: "Utku Sava\u015F"
    text: Hi, I can check model results on UI but I want to monitor whether data drifting(or
      similar problems) occurs or not on our projects. Which programs or approachs
      should I use to notice data drifting before it happens on image data?
- name: Tim Becker
  text: 'Hello Chip Huyen, thanks for being here. I would like to know:

    - What are frequent mistakes when designing ML systems and how to avoid them?

    - What kind of considerations should I take in mind when setting up automated
    re-training? How often should it be done? Only if the quality of the model decreases?

    - How do you document your ML projects?'
  replies:
  - name: Chip Huyen
    text: "hi Tim, thanks for your questions!\ni wish there were shorter answers to\
      \ those questions, but they are complicated \U0001F62D  i have a pretty long\
      \ section in my book on the myths of ml deployment and half of a chapter on\
      \ question 2 (which includes a section discussing how often to update models).\
      \ here's the summary\nEugene Yan has a lot more thoughts on documenting ML projects\
      \ \U0001F440"
- name: Warrie Warrie
  text: 'Hello Chip Huyen. Thanks for investing time here.

    1. As an academic researcher and application engineer, what areas in ML system
    design have you observed to be more disparity between the 2 industries?

    2. How critical is software engineering skill in designing an ML system?'
  replies:
  - name: Chip Huyen
    text: 'hii Warrie, i gave a talk on 1 here [https://www.youtube.com/watch?v=c_AUuTuPA5k&amp;ab_channel=StanfordMLSysSeminars](https://www.youtube.com/watch?v=c_AUuTuPA5k&amp;ab_channel=StanfordMLSysSeminars)

      engineering is critical for designing ml systems'
  - name: Javier
    text: "\U0001F92F"
- name: Max Payne
  text: 'Hi,

    How different is the design process for traditional ML vs DL?'
  replies:
  - name: Chip Huyen
    text: i think the difference is less between ML vs. DL but between different projects,
      goals, and constraints
- name: adanai
  text: '&gt; *Q:* lets say you are building a model with X technique which is in
    production but now you see that Y technique which is state of the art outperforms
    better than X during development do you remove model X and replace with model
    Y?

    Hello Chip, this question was earlier asked by a fellow member in another channel
    of the DTC workspace. I am interested to learn of your opinion

    Source (with suggestions from other members): [https://datatalks-club.slack.com/archives/C01BQDWEAHW/p1654315552971539](https://datatalks-club.slack.com/archives/C01BQDWEAHW/p1654315552971539)

    cc: Doink'
  replies:
  - name: Chip Huyen
    text: "i'd agree with the first answer there: run experiments (both online and\
      \ offline) to compare the 2 models on the metrics you care about (not just overall\
      \ performance metrics but can also be other metrics like latency, inference\
      \ cost, interpretability, how easy it is to update each model, how likely each\
      \ model's performance will improve over time with more data)\nchapter 6 as a\
      \ pretty long section on the framework for comparing 2 different models. here\
      \ are 6 key points:\n1. *Avoid the state-of-the-art trap*\n2. *Start with the\
      \ simplest models*\n3. *Avoid human biases in selecting models*\n4. *Evaluate\
      \ good performance now versus good performance later*\n5. *Evaluate trade-offs*\n\
      6. *Understand your model\u2019s assumptions*"
- name: Ramsi Kalia
  text: 'Chip Huyen Hi Chip, thanks for answering questions here!,

    I am wondering how re-usable ML systems are in your opinion? With every new problem
    statement, the dataset, features, splits, training etc. changes right? I am trying
    to understand how much value can be generated from building entire systems around
    ML projects?

    I understand that for large industries like Uber etc. if the models are being
    used daily and retrained very often it would make a lot of sense.

    But for smaller businesses, where models are retrained infrequently and there
    is a larger focus on trying out different techniques and newer models, how should
    we justify the extra time and effort spent on building systems? And what would
    the benefit be?

    Appreciate any insight you can offer!

    Thanks again for your time!'
  replies:
  - name: Chip Huyen
    text: 'i think you answered your own question!

      100% agree with you that how much to invest into a reusable ML platform depends
      on how much you need it (not just today but also in 6 months).

      it sounds like you''ve spent a lot of thinking about it. curious what your approach
      for this i?'
  - name: Ramsi Kalia
    text: 'Hi Chip Huyen, I don''t really have a plan of action atm,

      I''m working at a startup in the automotive space (we just won the NASSCOM Gamechangers
      Award in the transport &amp; logistics category , company is Carscan) but we
      don''t really have full fledged systems for retraining.

      There is active learning in place for the primary damage detection model, but
      even for that we''ve been trying out different methods to improve performance
      (e.g. SAHI, Autoassign, PAANET etc.)

      For edge deployment models, up till now we just trained a bunch of classifiers
      (cos they''re faster than object detection) and moved them to s3 and work from
      there.

      We''ve had numerous discussions on how to streamline the edge deployment of
      models for the webapp and we just seem to be going in circles lol.

      The last sprint was focussed in edge deployment and we tried out Hydranet, multihead
      models, mobilenet ssd, multilabel classification to name a few.

      With regards to code reusability and experiment/model tracking, I am giving
      a training session to my team on DVC this coming Monday, (still figuring it
      out for myself),

      however, for designing systems, I think we''re still lost.

      An argument could be made in favor if the benefits of taking such a thing on
      were greater than what I seem to be understanding atm.,

      Have you worked with startups before?

      Do you have any case studies you''d be open to sharing?'
- name: Sandhya G
  text: Chip Huyen,this is an exciting book. How do we determine which problems are
    worth exploring if ML is a viable solution? Sometimes, ML might add more cost/
    complexity than using an expert to solve the problem. For example, experts scan
    ground scan data to determine where to drill for oil. Using ML here maybe difficult
    as 1. we do not have a lot of training data 2. Experts maybe using their intuition
    which may be hard to codify. What is a framework for answering if ML is a viable
    route with decent chance of success given the cost to develop it. Also, any framework
    to have ML assisted workflows? Thanks!
  replies:
  - name: Chip Huyen
    text: whoa that does sound like an interesting challenge. how are you doing about
      approaching this?
  - name: Sandhya G
    text: "In my workplace, this is mostly based on instinct (experience). Do a pilot,\
      \ about 6 months, see where we get. We also go for a lot of non ML components\
      \ for the solution (data management and access, for example) so that customers\
      \ get guaranteed value. \nHowever I've seen this in my learning too. I'd start\
      \ off with something in mind, but fail to produce a good model. Since this is\
      \ for learning, I do not know if it is because I am not doing it right or if\
      \ the problem is not amenable."
- name: Dustin Coates
  text: 'Chip Huyen thank you for doing this. I''m coming at this from a PM perspective,
    and one question we have is: how do you show incremental added value in early
    days of ML projects?'
  replies:
  - name: Chip Huyen
    text: oooh this would be a fun discussion. happy to set up a call to discuss more!
- name: Bharat
  text: 'Chip Huyen thanks for doing this! My initial 2 questions:

    - What''s the latest industry trend with respect to ML system design? I have heard
    (and read blogs) that there is increasing online learning &amp; retraining, is
    this true?

    - What would you recommend as the first set of skill(s) to pick up for a Software
    Engineer transitioning to an ML Engineer apart from just the ML Theory basics?'
  replies:
  - name: Chip Huyen
    text: 'hi Bharat thanks for stopping by!

      1. i''m very big on online prediction and continual learning, so perhaps i''m
      biased, but i''ve talked to a LOT of companies interested in online learning
      &amp; retraining!

      2. hmm this is a hard question as the answer depends on who''s asking. for me,
      i love databases and devops!'
- name: Gur Hevroni
  text: "Hi Chip Huyen! Great to have you here \U0001F642 Your book sounds super interesting!\n\
    Do you cover in the book the things you should consider before you start to building/designing\
    \ anything? E.g. how to approach a problem, how to validate your understanding\
    \ of the situation and use cases, etc.\nLooking forward to learn more about your\
    \ book \U0001F4D6"
  replies:
  - name: Chip Huyen
    text: 'Hi Gur, nice to meet you and thanks for your kind word!!

      Yep that''s what the first 2 chapters are about!'

- name: James Gough
  text: "Hi Chip Huyen I have what I think is an easy or at least mundane question\
    \ for you (or anyone else if they know). \U0001F642\nI want to buy your book but\
    \ do you know how compatible your book is with Kindle? I know O'Reilly's subscription\
    \ service doesn't provide Kindle-compatible ebooks so wondered if there's been\
    \ much QA for the Kindle version. I've bought some programming books on Kindle\
    \ before and the formatting isn't always the best. Thank you."
  replies:
  - name: Chip Huyen
    text: ooh i'd love to know that too. if anyone does know please lmk. i've only
      looked at the book sample on kindle and it seems fine!!!?
- name: Ashish Lalchandani
  text: Hi Chip Huyen, another question - What are the best practices for ML in production,
    and as someone who is looking to switch from data engineering to MLOps, what are
    the bad practices to avoid?
  replies:
  - name: Chip Huyen
    text: "Hi Ashish, nice to meet you!\nSooo best / bad practices are going to be\
      \ a loong conversation -- I think it might take a book \U0001F61B\nShort answer:\
      \ i wish we have better engineering best practices in MLOps!"
  - name: Ashish Lalchandani
    text: "Thanks Chip Huyen..waiting for you future books then\U0001F92A hehe"
  - name: Chip Huyen
    text: "haha it's part of this book \U0001F61B"
  - name: Ashish Lalchandani
    text: "Oh same book, nice! Will have to wait till i get my copy then\U0001F605\
      \ \U0001F64C"
- name: Daniel
  text: "Hi Chip Huyen, thanks for taking the time and providing the offer to answer\
    \ questions. I'd like to know\n- What's the approach of the book: rather theoretical\
    \ explanations to get an overview over the topic or a practical one with hands-on\
    \ code/ best practice-examples to go through by yourself?\n- Which chapter was\
    \ the most difficult to write and why?\n- Just out of curiosity: team PyTorch\
    \ or Keras/Tensorflow? \nThanks!"
  replies:
  - name: Chip Huyen
    text: 'Hi Daniel!

      - I think it''s practical with examples but very little code.

      - They''re all difficult in different ways, but Chapter 3 (data systems), 8
      (distribution shift / monitoring), 10 (ml platform) took the longest time!

      - PyTorch &amp; JAX!'
- name: JC
  text: "Hi Chip Huyen, thank you for taking the time to share your opinions. I\u2019\
    d like to ask about the best practices on improving the ML/DL reference time.\
    \ And what can we do/consider ahead of time in order to improve the inference\
    \ time when designing the ML/DL system? Thank you a lot!!"
  replies:
  - name: Chip Huyen
    text: Hi JC, quantization seems to be the most common method today!
  - name: Gagan M
    text: Can we also add Knowledge Distillation if we are dealing with DL?
  - name: Chip Huyen
    text: yes! in the Model Compression section in the book i discussed the pros and
      cons of distillation vs. other compression methods like quantization
- name: "Philip Die\xDFner"
  text: 'Hello Chip Huyen, as is evident by the multitude of questions (Thanks for
    answering all of them!) your book is definitely hitting a nerve with the community.

    Can you talk a bit about how your writing process worked?

    What was your motivation in finding the breadth and width of the content?

    And as all is now done, would you do it again (e.g. writing another book)?'
  replies:
  - name: Chip Huyen
    text: 'hi Philip, nice to meet you!

      the writing process was an iterative one over 4 years with a ton of feedback
      and restructuring!

      i''d love to write another book one day, but not sure the topic yet. would love
      to hear if you have any topics you''d be interested in learning more about!'
  - name: Doink
    text: Decentralized Machine Learning?
- name: Allan
  text: 'Hi Chip Huyen!  Thanks so much for taking the time to answer questions here.

    This book sounds super interesting and relevant!  I know some of your blog postings
    have been about real-time ML.  To what degree is this covered in the book?  (Seems
    like Ch9 deals with it, at least in part).'
  replies:
  - name: Chip Huyen
    text: "Hi Allan, you're right that i'm very excited about real-time ML \U0001F604\
      \ in the book, real-time ML appears in multiple parts:\n- data engineering (batch\
      \ vs. streaming)\n- deployment / prediction service (batch vs. online prediction)\n\
      - real-time observability\n- continual learning"
  - name: Allan
    text: "Thanks Chip, yes it seems like real-time ML is really something wanted/needed\
      \ in industry today. Looking forward to learning more about it!  \U0001F600"
---

Machine learning systems are both complex and unique. Complex because they consist of many different components and involve many different stakeholders. Unique because they're data dependent, with data varying wildly from one use case to the next. In this book, you'll learn a holistic approach to designing ML systems that are reliable, scalable, maintainable, and adaptive to changing environments and business requirements.

Author Chip Huyen, co-founder of Claypot AI, considers each design decision--such as how to process and create training data, which features to use, how often to retrain models, and what to monitor--in the context of how it can help your system as a whole achieve its objectives. The iterative framework in this book uses actual case studies backed by ample references.

This book will help you tackle scenarios such as:

- Engineering data and choosing the right metrics to solve a business problem
- Automating the process for continually developing, evaluating, deploying, and updating models
- Developing a monitoring system to quickly detect and address issues your models might encounter in production
- Architecting an ML platform that serves across use cases
- Developing responsible ML systems