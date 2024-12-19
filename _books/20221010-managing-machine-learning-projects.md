---
authors:
- simonthompson
cover: images/books/20221010-managing-machine-learning-projects/cover.jpg
description: Book of the Week. Managing Machine Learning Projects by Simon Thompson
end: 2022-10-14 23:59:59
image: images/books/20221010-managing-machine-learning-projects/preview.jpg
links:
- link: http://mng.bz/Dg6R
  text: Book's page
start: 2022-10-10 00:00:00
title: Managing Machine Learning Projects
archive:
- name: Simon Thompson
  text: "Another great question!\nYou need to do some hard yards :\n- Undertake organizational\
    \ analysis\n- Understand the data as best you can \n- Understand the system architecture\
    \ \n- Understand the application \n- Understand the ethics and security/privacy\
    \ implications \n- Understand the path to production\nBy getting this knowledge\
    \ you get yourself into a position where you can make sensible judgements about\
    \ what the \"real\" requirement of the project are. Of course this is very hard\
    \ to do, so commonly people run lighthouse/pathfinder projects and also do a \"\
    sprint 0\" to try to get a better insight into what the actual blockers and path\
    \ to value is.\nHaving said that an ML project is a journey of discovery - my\
    \ view is that the whole process is about finding and eliminating risk - right\
    \ up until the last pull request is signed off and the code is all pushed into\
    \ prod.\nActually - quite a long time after that!!!!"
  replies: []
- name: Muhammad Awon
  text: 'Hi Simon Thompson,

    Thank you for sharing the book presentation and allowing us to learn from your
    invaluable knowledge and experience. Your presentation gives a holistic perspective
    on how to think about machine learning projects.

    My question is, what would you advise a sole engineer who has minimal experience
    with real-world projects, but he is asked by the stakeholder to evaluate the initial
    cost of the project, from developing the model to put into production (at least
    for the first iteration)? What are the determining factors one should consider
    to evaluate the initial cost?

    Thanks for giving us this opportunity!!'
  replies:
  - name: Simon Thompson
    text: "Hello Muhammad,\nThat's a really tough ask, but the questions I would ask\
      \ are:\n- is it small enough that you can do it yourself in a few weeks? In\
      \ this case I would recommend doubling the amount of time that you think it\
      \ will take you and offering that as an estimate because for sure you will discover\
      \ things are more complex than you think.\n- If it's something that will take\
      \ you more than 20 days of work, I would suggest that this is an indicator that\
      \ it's a lot bigger than that!\n- Some factors to consider:\n    \u25E6 is the\
      \ data simple or complex - if it's complex and hard to understand then double\
      \ your estimate \n    \u25E6 is the data small or big - if it's big then...\
      \ double your estimate\n    \u25E6 is the processing/compute platform required\
      \ complex/distributed... if it's complex then (you guessed it) double your estimate\n\
      \    \u25E6 is the data clean? \n    \u25E6 are there ethical / security/ privacy\
      \ issues\n    \u25E6 how many models will need to be developed \n    \u25E6\
      \ unstructured data? \n    \u25E6 is evaluation complicated? \n    \u25E6 what\
      \ sort of model documentation is required..."
  - name: Simon Thompson
    text: hope that helps?
  - name: Muhammad Awon
    text: That's a big help. Thank you!
  - name: Simon Thompson
    text: Another thought - if you are able to split the project into tasks then than
      helps the estimation alot, and it can give stakeholders insight as to how you
      came up with your estimate. I understand that that's very difficult if you are
      inexperienced
  - name: Muhammad Awon
    text: Indeed, it is going to challenging but getting answers from you is a big
      step forward to lay down the initial plan.
  - name: Muhammad Awon
    text: One last thing, how can I maintain good relationship with the stakeholder
      so to speak? Just in general.
  - name: Simon Thompson
    text: 'First try to understand the other person - what do they want, why do they
      want it? What sort of standards or behaviours can you expect from them - ask
      some other people who work with them about what their hot buttons are and what
      they learned about working with them.

      Second, respect their time. Prepare for your first meetings, treat their time
      as precious to you - use it well.

      Third  be positive and clear - don''t be negative, don''t be evasive. If you
      don''t understand something say so, try to get misunderstandings out of the
      way, try to clarify things at the beginning.

      Win their trust - you can''t be bringing failure at the beginning, but be honest
      and open. Concealed problems are your problem. Shared issues at the beginning
      are everyone''s problem.

      The cliche is underpromise, over deliver. It''s a good mantra. Don''t promise
      things you can''t give - if you bend to the pressure things will get worse and
      worse until something snaps. Honesty and clarity are your friend. Show your
      workings, show early results, get feedback early.

      Good luck!'
  - name: Muhammad Awon
    text: Thank you for your time. I really appreciate!!
- name: Dr Abdulrahman Baqais
  text: "Hi Simon Thompson. Thank you for being here.\nDo you believe that deep learning\
    \ projects should be handled differently than traditional ML projects? \nProbably\
    \ In NLP or computer vision due to labeling, annotation reviwer and required infrastructure.\n\
    Also do you recommend assigning managing the project to a manager rather than\
    \ a technical. Probably for his soft skills in leadership, conflicts handling,\
    \ non-perfectiones mentality."
  replies: []
- name: Simon Thompson
  text: 'Hello Abdulrahman,

    there are different types of deep learning projects. Some are not that different
    because they are dealing with relatively manageable data resources, and managable
    training resources. To be honest training a model using an isolation forest using
    data that''s squeezed out of a spark query that takes 5hrs to run isn''t that
    different from running a model on an A100... However, once we get into big scale
    training with a bunch of GPUs and training runs lasting days then things are very
    different and a very different management problem is on the table.

    Deep learning projects do have a big issue about artefact management and tracking
    in comparison to statistical ML projects as well. Managing transfer models, training
    regimes, hyper parameters and evaluation results can become non-trivial. It''s
    easy to get into a place where you have a model but can''t rebuild it or reproduce
    it. This is a bad place.

    You are right about handling training data resources and acquiring training data
    as well. Work on vision and text projects now includes creating data augmentations
    as well as the labelling and annotation steps - all of this has to be accounted
    for and executed.'
  replies: []
- name: Simon Thompson
  text: '&gt; Also do you recommend assigning managing the project to a manager rather
    than a technical. Probably for his soft skills in leadership, conflicts handling,
    non-perfectiones mentality.

    Ideally you need a technical person to lead the project; project led by people
    who don''t understand them can come apart really suddenly. However, project managers
    and people manager are really, really valuable and wise leaders will lean on their
    skills to organise and support the team.

    Send your technical leaders on a people management course and a project management
    course - "T" shaped people are really valuable!'
  replies: []
- name: Simon Thompson
  text: Thanks to everyone for the questions. Please feel free to email me at <mailto:simon.2.thompson@gmail.com|simon.2.thompson@gmail.com>
    if you want to talk further. Or follow @AiSimonThompson on Twitter
  replies: []
- name: Rohit
  text: HI Simon Thompson, one of the challenges we face is how we can deploy and
    monitor our model after the model is deployed into on-prem of our customer or
    their own cloud platform which is different from ours. How can we tackle this?
  replies:
  - name: Simon Thompson
    text: I think that you need to make sure that appropriate provisions and arrangements
      are in the contract (and if they aren't then you aren't doing it!) and that
      they are paid for as part of the bill of work... If you are liable for looking
      after it you need to be able to look after it!
- name: Alexey Grigorev
  text: Is there a better methodology for managing ML projects then CRISP-DM?
  replies:
  - name: Simon Thompson
    text: At the top level the CRISP-DM process covers everything - apart from in
      life management probably! But I think things have moved on a lot since CRISP-DM
      came along. I think in particular the tooling that teams need to manage the
      development of large complex models consisting of many artefacts and developed
      with very large complex data sets using many transforms needs to be emphasised.
      I also think that we now live in a world where our models get evaluated online
      and not just with a few statistical measures. Finally - ethics... you've got
      to think about the ethics all the way along, and that carrys with it the need
      to support reproducability and accountability. So - it's not that there is anything
      wrong with CRISP-DM, it's just that there are concerns in each part of the process
      that need to be addressed in a very different way from the way we used to work
      in the 1990's!
- name: Tim Becker
  text: 'Hi Simon Thompson, thank you for being here and answering our questions.
    I have a couple of questions I would like to ask you:

    - What are the main considerations when resourcing a team for a ML project?

    - What are the main difference between a ML project and a software development
    project that does not include ML?

    - How to best estimate the time that is needed for monitoring and troubleshooting
    after the model has been put in production? How can this time be minimised?'
  replies:
  - name: Simon Thompson
    text: '&gt; What are the main considerations when resourcing a team for a ML project?

      For me I think you need to think about this :'
  - name: Simon Thompson
    text: ''
  - name: Simon Thompson
    text: So you need people who can do all of these tasks - but different project
      require different balances according to the challenges you see in front of you.
      If the data infrastructure is tricky you will need more data engineering. If
      the modelling is going to be demanding you need more data scientists - and so
      on.
  - name: Simon Thompson
    text: Also a blend of people is important - think about how people will work together.
      The team must become more than the sum of the individuals.
  - name: Simon Thompson
    text: '&gt; What are the main difference between a ML project and a software development
      project that does not include ML?

      I think that the main thing is managing and understanding the models and the
      modelling process. You have huge uncertainties in the fact that model building
      with ML is a discovery process. You have to have a scaffold for that, and then
      100''s of models come out of the process which you have to handle.'
  - name: Simon Thompson
    text: '&gt; How to best estimate the time that is needed for monitoring and troubleshooting
      after the model has been put in production? How can this time be minimised?

      This is a great question - I have had models that have worked for years and
      then exploded over night. I think that they important thing is to build a capability
      that allows them to be looked after for as long as they will be needed and to
      make sure that there are appropriate commercial arrangements in place to cover
      that. For instance in the telecoms industry it''s quite common for experts in
      a particular technology to be on on a long term retainer which is called on
      when something goes wrong. The expert does no work whatsoever normally - but
      if there is an incident then they are obliged to come and help immediately (and
      are handsomly compensated as well). I saw a guy get $10k for 20 minutes of work
      because of this once... but he saved us much much much much more!'
  - name: Tim Becker
    text: thank you!
- name: Simon Thompson
  text: Hi there
  replies: []
- name: Simon Thompson
  text: Thank you to everyone for writing questions so far - I hope the answers are
    interesting and I will check back tomorrow ! Apologies for not checking the discussion
    until now but WORK IS CRAZY at the moment!
  replies: []
- name: Simon Thompson
  text: "If anyone would like to listen to a presentation about the book there is\
    \ one online here : [https://www.brighttalk.com/webcast/9059/553113?utm_source=brighttalk-portal&amp;utm_medium[\u2026\
    ]m=search-result-1&amp;utm_campaign=webcasts-search-results-feed](https://www.brighttalk.com/webcast/9059/553113?utm_source=brighttalk-portal&amp;utm_medium=web&amp;utm_content=managing%20machine%20learning&amp;utm_term=search-result-1&amp;utm_campaign=webcasts-search-results-feed)"
  replies: []
- name: Alexey Grigorev
  text: "&gt; Understanding an ML project\u2019s requirements\nCan you summarize the\
    \ process of doing it? Let's say I want to start a new project - what are the\
    \ steps I need to finish to understand how to approach it?"
  replies: []
- name: Surnjani Djoko
  text: "Any suggestions how to link the ML performance measurements to the business\
    \ impact when the stakeholders can\u2019t provide KPI?"
  replies:
  - name: Simon Thompson
    text: "I think you have to understand the priorities of your business stakeholders\
      \ - if they are interested in revenue then your system needs to impact revenue.\n\
      Typical things to try to impact :\n- revenue\n- cost saving \n- cycle time (time\
      \ to get things done)\n- people intensity (free up people to do stuff)\n- customer\
      \ experience"
  - name: Simon Thompson
    text: If you find what the stakeholders want to improve and figure out the mechanism
      that your system will use to deliver that then performance measures can be found
      quite directly (often)
- name: Vladimir Finkelshtein
  text: ML projects are well-known for the iterations and feedback loops. While iterating
    over the training data or model is understandable, how to avoid iterating over
    the infrastructure setup?
  replies:
  - name: Simon Thompson
    text: I think that you should accept that when /if the team find that they need
      to improve their infrastructure that will need to be done. It's only justifiable
      if the improvement is going to enable the team to move faster and do more -
      but if it is going to do that then you will find that it's an investment that
      really pays.
- name: Vladimir Finkelshtein
  text: "Managing projects usually involves planning/estimating execution times. Is\
    \ there a reason that your book doesn\u2019t include a chapter on those?"
  replies:
  - name: Simon Thompson
    text: '...Simon looks in book TOC...'
  - name: Simon Thompson
    text: So - there isn't an entire chapter - but in chapter 3 there is a long section
      about estimation. I agree it's a very important and hard issue that's got to
      be worked through. Many teams and people see it as a bad thing to do now as
      it's linked to waterfalls and people want to work in an agile way - but I think
      a good estimate is a really important way to prevent waterfall thinking because
      it can give you the time and resources to enable an agile team to become really
      productive and effective and to start delivering. Once that happens your stakeholders
      become confident and start to give you the space and time to really do good
      work.
- name: luckylittle
  text: 'Hi Simon Thompson, thanks for coming. *Q: How did you enjoy the process of
    writing this book with Manning Publications?*'
  replies:
  - name: Simon Thompson
    text: 'Manning were and are brilliant. I can''t recommend them highly enough.
      They provided lots of support and advice and I found the reviewing process that
      they offered incredibly good. I got 12 anonymous reviewers to read the book
      and make comments - and that really changed the book because... well they had
      some great points.

      I have to say though that "enjoy" is not the right way to describe what it''s
      like to write a book like this - more like cope!'
- name: luckylittle
  text: 'Second question I have Simon Thompson - I see a lot of good topics and I
    am particularly interested in `3.2.1 Time and Effort estimates` . *Q: How is estimating
    time &amp; effort different in ML project different from traditional software
    projects? I find any estimation to be quite difficult with so many unknowns.*'
  replies:
  - name: Simon Thompson
    text: I think you have 1/2 the picture - there are a lot of unknowns in typical
      ML projects. For example typically you won't have the full picture about the
      data you are working with at the beginning of the project. More importantly
      though the properties of the models that you *can* build using the data you
      get will only become clear when you build those models.... and that has some
      big implications for how you are going to structure your solution
- name: Hareesh
  text: '*Q: What should SME concentrate on (people - working in-house for the company
    OR technology - managed services via external contracts ?) to make most out of
    a ML project initiative ?*'
  replies:
  - name: Simon Thompson
    text: 'I am not sure what you mean... do you mean SME: Subject Matter Expert.
      or SME : Small Medium Enterprise?

      I think you mean small/medium enterprise. If so I think that a small company
      will typically not have the resources to sustain an in house ML team and so
      I think that long term investment for the company should go into the companies
      core operations and concerns, and then something like an ML project should be
      bought from an external supplier. I think that an external supplier should be
      able to offer a fixed price whereas developing the skills and capabilities internally
      might look cheaper on paper  - but in reality it might turn out to run out of
      control. Neither the in house or external team are going to be able to eliminate
      the project risk...'
  - name: Hareesh
    text: "Thank you for the response Simon Thompson.\n SME - Small Medium Enterprise.\
      \ Sorry for not mentioning that in my question."
  - name: Simon Thompson
    text: No problem Hareesh! Did my answer make sense to you?
  - name: Hareesh
    text: "Ohh.. yes!!\U0001F44D Your reply makes complete sense. \nML Projects that\
      \ SMEs envision  should add business value (irrespective if they avoid project\
      \ risk ). There is not point managing a ML project without the business aspect.\
      \ Having said that, i would argue that having 1-2 Data Specialist internally\
      \ will help SMEs better manage (both technical, financials and risk related\
      \ )  their ML projects handled by external providers."
  - name: Simon Thompson
    text: 'I think you are right - SME''s can use a Data Specialist to run their ops
      with or without an ML project going on. Someone who understand where the data
      is buried (!) and how it''s used in the business will be valuable all the time
      - but especially if an ML team is engaged to do a project. Being a smart buyer
      of services requires some insight into the services and what''s involved in
      delivering them.

      I just think ML expertise is too heavy a burden for a normal SME to carry.'

---

In Managing Machine Learning Projects you’ll learn essential machine learning project management techniques, including:

- Understanding an ML project’s requirements
- Setting up the infrastructure for the project and resourcing a team
- Working with clients and other stakeholders
- Dealing with data resources and bringing them into the project for use
- Handling the lifecycle of models in the project
- Managing the application of ML algorithms
- Evaluating the performance of algorithms and models
- Making decisions about which models to adopt for delivery
- Taking models through development and testing
- Integrating models with production systems to create effective applications
- Steps and behaviors for managing the ethical implications of ML technology

Managing Machine Learning Projects is an end-to-end guide for project managers who need to deliver machine learning applications on time and under budget. It gives you a unique set of tools, approaches, and processes designed to handle the unique requirements of machine learning project management—all proven in practice to deliver success in full-scale business environments. You’ll follow an in-depth case study of a Bike Shop developing their first machine learning application and see how to put each technique into practice. Throughout, the book gives strong consideration to the ethical issues of ML, including data privacy, and community impact. You’ll learn how to avoid and mitigate these issues and keep your machine learning project from being exposed to failure.
