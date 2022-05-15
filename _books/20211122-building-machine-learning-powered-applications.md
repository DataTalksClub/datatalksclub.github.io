---
title: "Building Machine Learning Powered Applications"
description: "Book of the Week. Building Machine Learning Powered Applications by Emmanuel Ameisen"
cover: "images/books/20211122-building-machine-learning-powered-applications/cover.jpg"
image: "images/books/20211122-building-machine-learning-powered-applications/preview.jpg"
start: 2021-11-22 00:00:00
end: 2021-11-26 22:59:58
authors: [emmanuelameisen]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/building-machine-learning/9781492045106/
  - text: Amazon
    link: https://www.amazon.com/Building-Machine-Learning-Powered-Applications/dp/149204511X/
  - text: Book's GitHub repository
    link: https://github.com/hundredblocks/ml-powered-applications

archive:
- name: "\xC1lvaro Budr\xEDa"
  text: Hi Emmanuel Ameisen, I'm a DS intern just one week into my internship. For
    novices like me, what are the crucial basic good practices, skills and ways of
    approaching the role that will make someone like me stand out?
  replies:
  - name: Emmanuel Ameisen
    text: "That really depends on your team, company and the goal of the internship!\
      \ More generally when onboarding to a new company, here are a few things I would\
      \ always recommend doing:\n- Ask a lot of questions, especially at the start.\
      \ Ask not only about subjects of interest, but meta-questions like \u201Chow\
      \ can I find documentation by myself?\u201D for example\n- Setup introductory\
      \ chats with many folks on the team (I would aim for at least one chat a day\
      \ for the first few weeks) to get to know them. In that process, ask about their\
      \ priorities and goals. This will let you know what matters to different parts\
      \ of the org, and angle your work to match.\n- Ask your manager and leaders\
      \ what they think are the success and failure criteria ahead of time. Than,\
      \ regularly check in to see whether you and them are in agreement on how everything\
      \ is going \nLast but not least: in an internship, you are also evaluating the\
      \ company as a potential place to work. Don't forget to take the time to explore\
      \ and decide whether this would be the right full-time role for you."
  - name: "\xC1lvaro Budr\xEDa"
    text: You give an angle to this question that I didn't think much about. I'll
      be applying all these tips. thanks!
- name: Nikhil Shrestha
  text: "Hello Emmanuel Ameisen  \nThank you for writing this book. \nAs we usually\
    \ talk a lot about statistics and learn too many concepts, also on the other hand\
    \ we come across senior lecturers n experts etc who also claim that you in real\
    \ world you don't use the theory but you use some tricks or things in practical\
    \ way.\nTo give small example: when we learn precision recall we find different\
    \ tricks like *P*recision = *P*ositive. The proportion of *TP* from all *Positive\
    \ labels*\nBut when solving in competition or real time we go vertical for Precision\
    \ and Horizontal for recall \n- My question is how does things actually work in\
    \ real life ? \n- How and when is statistics or other theoretical topics actually\
    \ used in real time ? \nLike I learnt from many instructors and webinars that\
    \ they usually use practical statistics. \n- But what does practical stats actually\
    \ mean ?"
  replies:
  - name: Emmanuel Ameisen
    text: 'Right, the body of theoretical knowledge that is taught at school is often
      much larger than what you will need in an applied role. This doesn''t mean it
      isn''t useful to learn all these concepts, but it is good to be aware of the
      practical realities of the job.

      For statistics specifically, I''d say it depends on your role. Some companies
      hire statisticians which may use every tool in their arsenal. For Data Scientists
      and ML Engineers, you''ll most commonly use stats to:

      - Understand model performance metrics, such as FPR/TPR, ROC curves, Brier scores,
      NDCG, etc

      - Design and interpret results of applied experiments such as A/B test. That
      includes understanding confidence intervals, statistical significance, MDEs,
      etc.

      - Understand model loss functions such as cross entropy loss and their impact
      on model training'
  - name: Nikhil Shrestha
    text: "Thank you for the swift reply and yes I totally agree that theory is as\
      \ important as knowing practicality. \U0001F642"
- name: Dustin Coates
  text: Emmanuel Ameisen no question here, but a thank you. As a PM ("former" dev),
    your book was immensely valuable. Almost instantly, our team put into place the
    "do it manually first" rule in a way that we hadn't before, and if that was the
    only thing we got out of it, it would have been useful enough, but I got much
    more. I've recommended your book to many others at my company.
  replies:
  - name: Emmanuel Ameisen
    text: I'm glad the book was useful and applicable to you and your team. It's been
      amazing to hear which parts resonated with folks at different companies and
      roles. Thanks for the kind words and for recommending it to others! If you haven't
      yet feel free to leave a review on Amazon if you have the time to let other
      PMs know to check it out, it really helps.
  - name: Maja
    text: "I agree \U0001F4AF Thank you for writing a great book on this topics and\
      \ being here with us. One of my colleague loves your book and highly recommended\
      \ it to all of us in the team. It was a huge help for him."
- name: WingCode
  text: 'Hi Emmanuel Ameisen,

    How do you validate an DS idea to full blown product? Is doing a quick PoC and
    then followed by agile methodology to build incrementally and deploy work or do
    you suggest anything else from your experience?'
  replies:
  - name: Emmanuel Ameisen
    text: "Love this question. One thing I try to focus a lot on in the book and in\
      \ real life is making iteration cycles as short as possible. When validating\
      \ an idea, you're often trying to do a couple things at once:\n- Determine whether\
      \ the product idea is useful before investing a lot of effort. For this, I recommend\
      \ finding either a rule/heuristic or using humans to build a first version.\
      \ Even if the performance isn't close to what you think you can reach with ML,\
      \ that will help you decide whether you need to work on this problem at all.\
      \ Oftentimes at this point you will find a fundamental flaw in your product\
      \ idea and rethink it \n- Figure out whether you need ML at all. ML is great,\
      \ but it has very high maintenance burden. Few models are ever \u201Cset it\
      \ and forget it\u201D (see googles paper about ML being the high interest credit\
      \ card of technical debt). This is a different problem, but the advice above\
      \ applies to it pretty directly\n- Figure out whether ML can solve it. It may\
      \ be the case that this is outside of the realm of what is doable today (\u201C\
      use ML to build a chatbot that can automate all of the work of a medical doctor\u201D\
      \ would be an example of something out of reach). For this, I recommend starting\
      \ by carefully defining the inputs and outputs of your ML system (where is it\
      \ going to live in your app? What information will it have access to? What kind\
      \ of prediction will it make? How long will it have to make this prediction?).\
      \ Once you have that, define what performance level will be your bar to ship\
      \ this model. Base this on business outcomes! If you are building a recommencer\
      \ system for a YouTube like service, you may for example decide that you'd only\
      \ use a model that recommends at least one useful video to a user 80% of the\
      \ time it displays recommendations. If the model will be used in a modal that\
      \ shows three recommended videos, that means your top3 recall should be 80%.\
      \ \nOnce you have those, you can start your iteration loop of model building\
      \ and evaluating. Of course you may learn more as you go along and fine tune\
      \ these goals, but doing the work ahead of time will save months of time wasted\
      \ in dead ends"
- name: WingCode
  text: 'How do you handle "pivots" in product development? For example: You start
    building your product around a particular framework later realise that there is
    a new superior framework out there. Do you have any steps which you follow to
    avoid these "pivots" in the future?'
  replies:
  - name: Emmanuel Ameisen
    text: That's a challenging one, and slightly outside the scope of my expertise.
      I'll say that my experience is that pivots and refactors are always more costly
      than expected, so I generally require a strong motivation to buy in to one.
      Again, a bias for simplicity can help here as it makes swapping out any piece
      of your pipeline easier. It's hard to say much more without a more specific
      situation
  - name: WingCode
    text: "Thank you Emmanuel for all of your elaborate answers \U0001F642"
- name: Nikhil Shrestha
  text: "Hello Emmanuel Ameisen again \nWe hear this a lot, if you want to get into\
    \ the industry you must make projects on real life situations solving real life\
    \ problem \nI want to know how we approach towards solving one. Are there some\
    \ pointers which you could tell in terms beginning a project, challenges and some\
    \ tips to tackle them."
  replies:
  - name: Emmanuel Ameisen
    text: Practical experience is very worthwhile, so working on a project is valuable.
      My only guideline for picking a project is to pick something applicable and
      useful, and get your hands dirty. In my experience the main value of a side
      project for recruiting folks that are early in their career is to show that
      they can be productive. Often times I hear students get hung up on how much
      ml or rl or computer vision their project contains. As long as you can show
      that you know the required theory, it actually doesn't need to be part of an
      applied project. I would consider them separate and chose a project by finding
      a use case you like, not shoe horning an ML application to it
  - name: Nikhil Shrestha
    text: "Thank you for the insights and I will use these in practical from now on.\U0001F64F\
      \U0001F642"
- name: Nikhil Shrestha
  text: "Also we study significance level and confidence level in theory class \n\
    As I learnt from some webinars and tutorials. Real world situation they are used\
    \ extensively, before every project SL and CL are decided and using them you decide\
    \ if model is generalized or not and also model evaluation.\nE.g. criteria could\
    \ be train-score &lt; test-score AND test-score &gt; CL \n- My question is how\
    \ far is this true. ? \n- If it is true then what happens to the results ? \n\
    As I tried this technique in NLP and other ML data (toy data). I had to reduce\
    \ my training accuracy to achieve this criteria. \n- So 90-99 % accuracies are\
    \ myths \U0001F646"
  replies:
  - name: Emmanuel Ameisen
    text: In my experience, confidence interval are more often used for superiority
      and non inferiority tests (is this model better than that one) both offline
      and online (A/B test).
  - name: Nikhil Shrestha
    text: "Thank you \nTotally understood and makes sense"
  - name: "\xC1lvaro Budr\xEDa"
    text: Nikhil Shrestha what do CL and SL mean?
  - name: Nikhil Shrestha
    text: SL is significance level and CL is confidence level.
- name: Tim Becker
  text: Hi Emmanuel Ameisen, thanks for this really interesting book!
  replies: []
- name: Tim Becker
  text: '- I was wondering which tech stack you are discussing in the book?'
  replies:
  - name: Emmanuel Ameisen
    text: The book mostly uses the Python data science stack
- name: Tim Becker
  text: '- Which deployment options do you cover in the book?'
  replies:
  - name: Emmanuel Ameisen
    text: The book doesn't focus too much on deployment infra. It discusses trade
      offs at a high level though, like synchronous and batch server side approaches
      vs edge deployments. If you want to learn about that specifically though, you'll
      probably want to check out more specialized books
- name: Tim Becker
  text: '- What is in your experience the most difficult part when building a ML powered
    application?'
  replies:
  - name: Emmanuel Ameisen
    text: Understanding the user need and trade offs well enough to chose the correct
      technical approach. Being able to tell when the current approach is a dead end
- name: Tim Becker
  text: '- What are the most common pitfalls during the process of building ML applications?
    And how can we avoid these?'
  replies:
  - name: Emmanuel Ameisen
    text: "Starting from the ML and deriving the application from it (\u201Cit would\
      \ be cool to ship a sentence model, we could use it to autocomplete searches\
      \ on our clothing website\u201D) vs the opposite (\u201Cusers often miss relevant\
      \ categories, so we should build a classifier based on search queries that suggests\
      \ relevant categories to browse\u201D)"
  - name: Tim Becker
    text: "thank you for answering my questions \U0001F642"
- name: adanai
  text: 'Hello Emmanuel, thank you for doing the QnA!

    How do we measure the outcome of the model in test after measuring the output
    during train/validation phase?

    What are the common indications to look for when the model does not do well in
    the production/test phase even when the outputs showed the model was doing well
    in validation phase?'
  replies:
  - name: Emmanuel Ameisen
    text: Regressions happen all the time between your validation set and production.
      They are commonly caused by mismatches in data generation, either on the filtering
      side (you trained on an unrepresentative distribution of samples) or the feature
      computation side (the way you compute some feature is different online/offline).
      The best way I've found to detect those mismatches is to rely on a shadow infrastructure.
      Shadow means that in production you send a copy of the request you send to the
      prod model to your candidate model, and log its output. Because you don't action
      the prediction in any way, it is a safe approach that gives you information
      about production performance.
  - name: adanai
    text: Shadow infra is something new to me and interesting, will read about it!
      Thank you
- name: Allan
  text: 'Hi Emmanuel, thanks for doing this and for the insightful answers you have
    provided this far. Sounds like a great book!

    What would you say is the minimal realistic practical size for a team to take
    a new project from prototype to production?'
  replies:
  - name: Emmanuel Ameisen
    text: Depends on the scale of the project and company! For internal tools, or
      at companies with strong infrastructure, a single IC can ship a model to prod.
      For companies that are smaller, or projects that are more complex, teams can
      get arbitrarily large. Think of the number of software, hardware, data and ML
      engineers are required to ship Tesla self driving, or OpenAI GPT-3

---

Learn the skills necessary to design, build, and deploy applications powered by machine learning (ML).
Through the course of this hands-on book, you’ll build an example ML-driven application from initial
idea to deployed product. Data scientists, software engineers, and product managers — including experienced
practitioners and novices alike — will learn the tools, best practices, and challenges involved in
building a real-world ML application step by step.
