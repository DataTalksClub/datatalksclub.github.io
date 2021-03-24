---
title: "Machine Learning Design Patterns"
description: "Book of the Week. Machine Learning Design Patterns by Valliappa Lakshmanan, Sara Robinson, Michael Munn"
cover: "images/books/20210208-ml-design-patterns/cover.jpg"
image: "images/books/20210208-ml-design-patterns/preview.jpg"
start: 2021-02-08 00:00:00
end: 2021-02-12 22:59:58
authors: [Valliappa Lakshmanan, Sara Robinson, michaelmunn]
links: 
  - text: Book's page on O'Reilly
    link: https://www.oreilly.com/library/view/machine-learning-design/9781098115777/
  - text: Book's Github Page
    link: https://github.com/GoogleCloudPlatform/ml-design-patterns

archive:
- name: Denis Lepchev
  text: 'Hi Mike Munn - thank you and your colleagues for such a great book!

    I have a question regarding the "continued model evaluation" design pattern. As
    you mention in the book, usually we act on the model''s predictions - as an example
    trying to prevent customer''s churn.

    How companies like Google deal with the feedback loops, when acting on the model''s
    prediction changes the outcome, making it impossible to observe the ground truth?
    Many books and articles mention this problem, but the solution is not discussed.

    One of the solutions I am aware of is to have a small (untouched) hold-out group
    as a basis for model evaluation and for re-training, but it comes with its own
    set of problems. Is there an alternative method(s)?'
  replies:
  - name: Mike Munn
    text: "Hi Denis Lepchev thanks!\nYou bring up a really good point about \u2018\
      feedback loops\u2019 when dealing with continued model evaluation. There is\
      \ a lot written about this. I remember reading an article about a company called\
      \ Stripe that discussed this problem for them in some detail for a credit fraud\
      \ model they had developed.\nWe discuss this briefly in the subsection called\
      \ \u201CCapturing ground truth\u201D as well as other considerations. You mention\
      \ a good approach. Another technique to consider is to use causal impact models.\
      \ Causal impact uses Bayesian techniques to understand how a certain \u201C\
      treatment\u201D might have affected a population. It\u2019s commonly used in\
      \ scenarios where it\u2019s not possible (or not ethical) to have a hold out\
      \ or control group. This is commonly used at Google and that team has open sourced\
      \ a CausalImpact package you might want to check out."
  - name: Denis Lepchev
    text: Thank you for the answer, Mike.
- name: Alper Demirel
  text: "Hello Mike Munn, thank you for writing this beautiful book and coming to\
    \ this channel \U0001F44F\n- What is the most important difference from similar\
    \ books on the market?\n- Why did you need to write such a book with your friends?"
  replies:
  - name: Mike Munn
    text: "Thanks so much Alper Demirel. I\u2019m glad you enjoy it. \U0001F642\n\
      - In my mind, this book would come after an intro book or reference on ML. We\
      \ certainly talk about how you would do things (and there is a github repo with\
      \ code implementing the ideas in code) but this book is focused more on common\
      \ problems and their solutions that we\u2019ve learned in working with customers\
      \ along the years. Likely a lot of patterns will be familiar to you, if you\u2019\
      re a practicing ML/AI engineer. So this book is a kind of formal collection\
      \ of \u201Cnotes from the field\u201D and solutions to common real world problems\
      \ of building and productionizing ML models. \n- Following on a bit from my\
      \ point above, another reason we wanted to write this book (in addition to having\
      \ a collection of common problems/solutions) was to create a shared language\
      \ for these ML patterns. Like any pattern, you find yourself using the same\
      \ tricks over and over. And in talking with other colleagues we wanted to create\
      \ a single term or phrase that describes that problem/solution. So, for example,\
      \ the \u201CBridged Schema\u201D pattern gives a name to the common problem\
      \ that arises when dealing with changing data fields. This way, we can try to\
      \ have a shared language of common patterns for everyone to use."
  - name: Alper Demirel
    text: "Thank you so much for the answers, now I'm more excited to read the book\
      \ \U0001F929\U0001F51D"
- name: Aleix
  text: 'Hi there, Mike Munn! Pleasure talking to you :)

    What has been the most recurring problem to an ML engineer like you when working
    at Google?'
  replies:
  - name: Mike Munn
    text: "Thanks Aleix glad to have the opportunity to talk to you as well. \U0001F642\
      \nThat\u2019s a good question. It\u2019s hard to say what the most common problem\
      \ would be. I work a lot with Google Cloud customers. We typically work on engagements\
      \ that span the entire ML work lifecycle. The project specific problems or patterns\
      \ that arise are so use case dependent. So I guess the most recurring problems\
      \ then would be the problems that relate to initial or final stages of the lifecycle\
      \ (since they are broad and similar across multiple use cases). Those would\
      \ be the patterns addressing data issues or dealing with Responsible AI and\
      \ working with business stakeholders. Typically the most common problem is in\
      \ framing the problem and understanding issues with the data. That seems to\
      \ be consistent across all projects I\u2019ve worked on."
- name: Matthew Emerick
  text: Hey, Mike Munn!  Appreciate a moment of your time.  Your book is on my (rather
    large) Amazon wishlist.  I do have a question for you.  Are the patterns organized
    by difficulty level?
  replies:
  - name: Mike Munn
    text: "hi Matthew Emerick! Happy to be able to stop by \U0001F642 I know too well\
      \ about large book to-read lists lol.\nThe patterns aren\u2019t arranged by\
      \ difficulty. Instead we arranged them loosely with the different stages of\
      \ a typical ML workflow or ML lifecycle. So we start with patterns related to\
      \ Data Representation, then move to Problem Representation, then talk about\
      \ patterns related to Resiliency and then Reproducibility and end with Responsible\
      \ AI and stakeholder management."
  - name: Matthew Emerick
    text: I like that.  Is there anything about the complexity (ie bubble sort is
      easy to do, but slow) for each pattern?
  - name: Mike Munn
    text: "kind of! Each pattern is broken down into four main sections: Problem,\
      \ Solution, Why It Works and Tradeoffs &amp; Alternatives. The Tradeoffs &amp;\
      \ Alternatives section discusses exactly that. We touch on any \u2018gotchas\u2019\
      \ or complexity issues, or common pitfalls or just other related approaches\
      \ you might want to consider."
  - name: Matthew Emerick
    text: Okay, so the expected style for a pattern book.  Makes it easier anyone
      who has used a pattern book in the past.  Good plan.  Organization is something
      I touch on in my book reviews, both macro and micro.  A well written book with
      great and important content can hit a wall if it's not organized well.  Great
      job!
- name: George Melvin
  text: "Hey Mike Munn, thanks for sharing your time with this community! I\u2019\
    m excited to dive deeper into the book. My question is around company size: are\
    \ certain patterns more conducive to smaller/larger teams/organisations? In particular,\
    \ I\u2019d be interested to hear about your experience (re)learning patterns when\
    \ moving between teams/organisations that are comprised of larger/smaller teams.\
    \ Thanks!"
  replies:
  - name: Mike Munn
    text: "hi George Melvin thanks for having me\nGood question. The patterns are\
      \ more focused on implementation. So I can see how they would apply to both\
      \ smaller/larger orgs. That being said, for some smaller orgs or smaller teams\
      \ there is less focus on some MLOps aspects. For example, we have a section\
      \ on Feature Stores. This is a super useful pattern and important to know about;\
      \ however, I can image for a smaller org the need for a feature store may be\
      \ less imperative than for a large organization where you have dedicated teams\
      \ to engineer features for the models that another dedicated team is building.\n\
      But, I\u2019d say the patterns in general are relevant for small or large teams\
      \ and orgs. Just some may resonate more than others."
  - name: George Melvin
    text: "Great, thanks for your answer! I \u2019m looking forward to learning more\
      \ \U0001F913"
- name: Neal Fultz
  text: 'Thanks Mike Munn for answering questions. Mine is: what are the most dangerous
    anti-patterns that you have encountered?'
  replies:
  - name: Mike Munn
    text: "Hi Neal Fultz and thanks!\nOhhh that\u2019s a good one. A lot of things\
      \ come to mind. I think the most dangerous (and I may be biased in the type\
      \ of work I usually do and some bad past experiences) would be anti-patterns\
      \ related to reproducibility and resiliency. So much of ML development is experimentation\
      \ (with data, with pipelines with models, etc) and reproducibility is crucial\
      \ to running thorough experiments. Also, as I work with more companies interested\
      \ in productionizing their models, anti-patterns related to resiliency really\
      \ end up being more and more detrimental"
- name: Mike Munn
  text: "hello Everyone. Thanks for having me visit the channel and the opportunity\
    \ to talk about the book \U0001F642"
  replies: []
- name: Dr Abdulrahman
  text: "Thank you Mike Munn for the book and for your time answering questions.\n\
    I have three questions:\n 1. From your experience, how would you assess the awareness\
    \ of these patterns among senior practitioners. Would you say the majourity of\
    \ seniors are not aware."
  replies:
  - name: Mike Munn
    text: "hi Dr Abdulrahman very happy to join the channel this week.\n1. I\u2019\
      d imagine that for most senior ML practitioners would be aware of the majority\
      \ (if not all) of these patterns. Though they might not know it by the name\
      \ we used. We have code for each pattern and use a variety of tools, some of\
      \ them more recently developed than others. So even senior practitioners might\
      \ be able to learn something new from the book.\n2. That\u2019s a good question.\
      \ I\u2019m not sure. I imagine it would likely come from constraints either\
      \ in their infrastructure or project timing. For example, someone may understand\
      \ the importance and need for Continued Model Evaluation but it can be difficult\
      \ to implement carefully and require too much overhead for the business objective.\n\
      3. I wouldn\u2019t say a complement book is needed, but it could certainly help.\
      \ This book touches on patterns across the entire ML lifecycle so a book more\
      \ focused on one aspect (say data engineering or ML pipelines) could be helpful\
      \ for more  implementation details."
- name: Dr Abdulrahman
  text: 'Second question: What drives many seniors not to follow these patterns when
    developing their ML models?'
  replies: []
- name: Dr Abdulrahman
  text: 'Third one: Would we need a complement book about data engineering (pipeline)
    design patterns.'
  replies: []
- name: Simon Steinkamp
  text: "Thank you Mike Munn for taking the time answering questions here \U0001F642\
    \nThe idea of design patterns is actually very new to me and it was very interesting\
    \ to have a quick look at those. Having heard the term \"copy-paste\" data scientist\
    \ recently, I have the feeling that some patterns probably evolve naturally, especially\
    \ through worked examples for tensorflow, keras or scikit-learn.\nKnowing that\
    \ your book goes beyond the model fitting step, I was wondering what your opinion\
    \ on these patterns is?"
  replies:
  - name: Mike Munn
    text: "Hi Simon Steinkamp thanks for joining with questions \U0001F642 I\u2019\
      m not familiar with the term \u201Ccopy-paste\u201D data scientist, but I think\
      \ I can guess what it\u2019s referring to. In some sense, the ideas are similar.\
      \ However, these design patterns are more like ways of thinking when designing\
      \ solutions or building ML systems. This book would follow a course on how to\
      \ effectively build ML model, so we don\u2019t get into the weeds about those\
      \ details. There are already really great books out there that address that.\
      \ The idea of patterns is more focused on ways of thinking and recognizing common\
      \ solutions to common problems. The solutions can\u2019t typically be copy-pasted\
      \ directly (since each case is a bit different) but the idea is certainly repeated."
  - name: Simon Steinkamp
    text: "Great, thank you for your answer, I will have a closer look \U0001F642"
- name: Poornima
  text: "Hi Mike Munn first of all congratulations on your book release which will\
    \ help so many ML practitioners on their professional and/or learning journey.\
    \ \nLike to ask two questions:\n* What was your motivation behind coming up with\
    \ the idea of writing a book on design patterns in ML."
  replies:
  - name: Mike Munn
    text: "hi Poornima Thank you! I hope you enjoy it.\n1. The motivation came from\
      \ lots of customer engagements at Google Cloud in our roles. When designing\
      \ ML systems or thinking about common ML approaches, we saw that there were\
      \ some common patterns in the field. The book attempts to collect those pattens\
      \ into a single easy to reference source. \n2. There wasn\u2019t any monolithic\
      \ use case or project but we did try to use similar datasets throughout the\
      \ book when illustrating a concept. This way, the code solutions would be less\
      \ about the data or model and more about the pattern itself."
  - name: Poornima
    text: "Thank you much Mike Munn for answering. Looking forward to gain great knowledge\
      \ from the book. Hoping to see more such excellent works from you in future.\
      \ All the very best \U0001F642"
- name: Poornima
  text: '* Is there any sort of monolithic usecase/project you are illustrating to
    showcase the optimal design patterns for each stage of ML lifecycle for that particular
    case.

    Thank you.'
  replies: []
- name: Poornima
  text: "Thank you much Mike Munn for answering. Looking forward to gain great knowledge\
    \ from the book. Hoping to see more such excellent works from you in future. All\
    \ the very best \U0001F642"
  replies: []
- name: Alexey Grigorev
  text: 'I remember when I was learning design patterns (the GOF ones), I tried to
    use them everywhere, and in most cases, it was doing more harm than good. With
    experience, I learned when the patterns should be used and when they shouldn''t.

    Do you think something like that can also happen with ML design patterns? If yes,
    what advice would you give to beginners to get started with ML design patterns?'
  replies:
  - name: Mike Munn
    text: "Alexey Grigorev yeah for sure! It\u2019s like the typical hammer/nail scenario.\
      \ For beginners, I think it would be helpful to first just read through the\
      \ patterns to be aware of what\u2019s out there. Then revisit certain patterns\
      \ based on the individual use case and really question of it will help solve\
      \ the problem *you* have. The final chapter of the book gives an overview of\
      \ all the patterns, breaking them down in a simple chart of problem/solution/description.\
      \ If you think a pattern might be a good solution, take a critical look at the\
      \ section that discusses that one in detail. And see if it fits or not."
  - name: Alexey Grigorev
    text: Makes sense, thanks!
- name: Justin Neumann
  text: "Dear Mike Munn,\nI read parts of your book with my O'Reilly learning account\
    \ and I really liked it so far! I particularly like the idea of the \"Reframing\"\
    \ concept. Do you think it is applicable to a single, global (gradient boosted\
    \ tree) regression model that captures multiple time series (which is the problem\
    \ I deal with on a daily basis)? I can't think of a way to apply the \"target\
    \ binning\" regression -&gt; classification approach to such a global model, unfortunately.\n\
    Thanks in advance for the answer!\nPS: I have the book on O'Reilly, so no need\
    \ to give me a book \U0001F609\n\nBest, Justin"
  replies:
  - name: Mike Munn
    text: "Thanks Justin Neumann great question. The Reframing pattern is an interesting\
      \ one. It\u2019s focus is less on the model itself and more on how the labels\
      \ are represented. So, for example, the regression -&gt; classification reframing\
      \ discusses how you can modify a typical regression problem and frame the problem\
      \ as learning a probability distribution via classification and binning. One\
      \ scenario where it is useful is when there may be training examples which have\
      \ the same features but different labels (I think in the book we used the dataset\
      \ of birthweights). This way you are learning a probability distribution for\
      \ a feature input and it can be less confusing for the model. So you\u2019re\
      \ really just changing your labels, and you would modify your gradient boosted\
      \ tree to be classification instead of regression. The pattern isn\u2019t model\
      \ dependent. Does that make sense?\nOne last point to mention is that this approach\
      \ of reframing may just not be beneficial to your data or use case. As with\
      \ most solutions, it\u2019s very use case dependent.\nLastly, I\u2019m glad\
      \ to hear you have the book. I really hope you enjoy it!"
  - name: Justin Neumann
    text: "Thanks for the reply. Your answer makes all sense to me and you're right,\
      \ this pattern may just be not applicable to my problem. I'll keep reading!\
      \ \U0001F609 Best, Justin"
- name: Rosona
  text: Hi Mike Munn! Thanks for taking questions. Who do you see as the perfect reader
    (slash ideal audience) of this book? Do you see it as essential even for the raw
    beginners, or something to ingest after e.g. a year of experience or more?
  replies:
  - name: Mike Munn
    text: "Hi Rosona Thanks for joining in. Our target audience was someone that knows\
      \ the basics of ML and building models. We kind of pitched it as a follow up\
      \ to a beginning ML book, like Geron\u2019s book \u201CHands On ML with SciKit\
      \ and TF\u201D or Muller/Guido\u2019s book \u201CIntro to ML with python\u201D\
      \ or after a semester course in ML. With more experience, I image the reader\
      \ would be able to appreciate (or recognize) more of the patterns."
- name: Alexey Grigorev
  text: 'How would you rank patterns in terms of applicability and usefulness for
    applied machine learning in industrial settings?

    Which patterns come first to mind and we should use them in most of the projects?'
  replies:
  - name: Mike Munn
    text: "Alexey Grigorev yeah good question. When I think about applied machine\
      \ learning or ML projects we\u2019ve done with our cloud customers, I think\
      \ the most useful and common patterns are those that show up in our chapters\
      \ on Repeatability and Resiliency, patterns like ML Pipelines, Continued Model\
      \ Evaluation, Batch Serving, Keyed Predictions, Batch Predictions, Feature Store,\
      \ Transform, and Model Versioning. Also, the Responsible AI patterns are also\
      \ really important for applied machine learning projects."
  - name: Alexey Grigorev
    text: Thank you! And what is the least used one? You mentioned feature stores
      as something that smaller teams/companies usually don't need - maybe this one?
      or some other one?
  - name: Mike Munn
    text: "yeah some of the patterns are more use case driven, so I\u2019ve personally\
      \ see those less. And yes, patterns like Feature Store seem to be much more\
      \ important for industrial teams. In my experience, smaller, more agile teams\
      \ might not benefit or need to have a feature store set up. They can be incredibly\
      \ useful and necessary for some situations, but can also require a lot of technical\
      \ overhead."
  - name: Alexey Grigorev
    text: Got it, thank you!
- name: Rishabh Bhargava
  text: "Hi Mike Munn - thanks for writing this book! So invaluable as we figure out\
    \ good practices for shipping ML systems. My question is: what were some design\
    \ patterns (if any) that you would have liked to include, but that had to get\
    \ edited out? \U0001F642"
  replies:
  - name: Mike Munn
    text: "Hi Rishabh Bhargava thanks for joining with questions. It\u2019s funny,\
      \ that question has come up before, and honestly I think we were able to catch\
      \ all the patterns we had in mind. Our initial list didn\u2019t come out to\
      \ such a round number of 30, but as we were writing a couple topics we thought\
      \ would be covered as one pattern ended up getting their own section, or the\
      \ opposite (some individual patterns ended up getting grouped together naturally).\
      \ So in the end, we covered the ones we wanted\u2026.though, now that it\u2019\
      s been put in my mind I\u2019m already thinking of new patterns we could have\
      \ added \U0001F642"
  - name: Rishabh Bhargava
    text: "I have a 2 parter question as a follow up. \n1. Do you think these design\
      \ patterns will need significant updates in the near future, or these patterns\
      \ represent some general truths about how ML systems should be built? \n2. If\
      \ you think updates are likely, do you think the second edition will be needed\
      \ in 6 months, 1 year, 5 years or 10 years?"
  - name: Mike Munn
    text: "yeah good questions,\n1. i don\u2019t think these patterns themselves will\
      \ need much updates..though, for some, the code or implementations could change\
      \ over time and be updated or improved as tools continue to develop as solutions\
      \ to address these common problems\n2. I don\u2019t foresee the need for an\
      \ second edition soon, but if code updates do become necessary, they\u2019ll\
      \ make it into the book\u2019s github with the code examples much sooner."
---

The design patterns in this book capture best practices and solutions to recurring problems
in machine learning. The authors, three Google engineers, catalog proven methods to help data
scientists tackle common problems throughout the ML process. These design patterns codify the
experience of hundreds of experts into straightforward, approachable advice.

In this book, you will find detailed explanations of 30 patterns for data and problem
representation, operationalization, repeatability, reproducibility, flexibility, explainability,
and fairness. Each pattern includes a description of the problem, a variety of potential solutions,
and recommendations for choosing the best technique for your situation.