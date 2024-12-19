---
authors:
- toddunderwood
- krantik-parisa
- cathychen
- niallmurphy
cover: images/books/20221121-reliable-machine-learning/cover.jpg
description: Book of the Week. Reliable Machine Learning by Todd Underwood, Kranti
  K. Parisa, Cathy Chen and Niall Murphy
end: 2022-12-09 23:59:59
image: images/books/20221121-reliable-machine-learning/preview.jpg
links:
- link: https://www.oreilly.com/library/view/reliable-machine-learning/9781098106218/
  text: Book's page
- link: https://www.amazon.com/Reliable-Machine-Learning-Principles-Production/dp/1098106229
  text: Buy on Amazon
start: 2022-12-05 00:00:00
title: Reliable Machine Learning

archive:
- name: Cyril de Catheu
  text: "Hey, thanks for sharing.\nHow does the book relate to the [google SRE](https://sre.google/books/)\
    \ books? Should I read it if I\u2019ve read (and applied) those?"
  replies:
  - name: Niall Murphy
    text: "HI Cyril - to be clear, there\u2019s no \u201Cshould\u201D here. No requirement\
      \ to read one or the other before anything. The books speak to each other in\
      \ the sense that they come from a similar mindset, but they\u2019re actually\
      \ about pretty different things. (They\u2019re not in the same grouping at the\
      \ publisher, for example.)\nHaving said the above, the Google SRE books are\
      \ a good intro to questions about systems thinking in general, and obviously\
      \ share some authors in common (though of the two, one has not been in Google\
      \ for five years)."
  - name: Cyril de Catheu
    text: Thanks Niall Murphy!
- name: Cyril de Catheu
  text: 'I find it difficult with ML issues to understand whether an issue is related
    to infra, modeling, or data.

    Is this something discussed in the book?

    In a few words do you have strategies to approach this problem?'
  replies:
  - name: Niall Murphy
    text: Yeah, good point, that is definitely one of the challenges. We deal with
      this in the monitoring chapter, though not quite as directly as you put it there.
  - name: Cyril de Catheu
    text: Thanks Niall Murphy.
- name: Eunice
  text: Hi, Thank you very much to answer our questions. Do you see any big difference
    for MLRE process between Deep Learning and Machine Learning Projects ?
  replies:
  - name: Niall Murphy
    text: "Nope. I would say it\u2019s broadly unchanged under both methods, except\
      \ to the extent you can ignore training data for RL processes - if you don\u2019\
      t have training data to manage, a bunch of complexity goes away."
- name: Eunice
  text: A second question, how did you get the excellent idea of writing this book?
  replies:
  - name: Niall Murphy
    text: "You\u2019re very kind! We talk about this a bit in [https://www.youtube.com/watch?v=ypt62rP3zhg](https://www.youtube.com/watch?v=ypt62rP3zhg)\
      \ but the basic story is - there\u2019s a lot in the MLOps world that\u2019\
      s a total wild-west situation right now, Todd in particular has some great experience\
      \ that other people could benefit from, and Todd and I were going to write a\
      \ book together anyway \U0001F609 But then we realised the _actual_ book to\
      \ write was one that talked about everything in ML that _wasn\u2019t_ building\
      \ a model, which includes data, privacy, monitoring, organizational design,\
      \ etc etc. Those things don\u2019t get talked about in the one book."
- name: Alexey Grigorev
  text: 'Hi everyone! Thanks for being here!

    Do you think ML reliability engineer is already an established role? Or most of
    the time it''s "usual" SREs working in ML teams?'
  replies:
  - name: Cathy Chen (she/her)
    text: "From my exposure, it is normally SRE type who have special interest in\
      \ ML but usually their expertise is in SRE topics, not ML topics. \ntodd underwood\
      \ did a few talks at SREcon about this:\n[https://www.usenix.org/conference/srecon22emea/presentation/underwood](https://www.usenix.org/conference/srecon22emea/presentation/underwood)\n\
      [https://www.usenix.org/conference/srecon21/presentation/underwood-sre-ml](https://www.usenix.org/conference/srecon21/presentation/underwood-sre-ml)"
  - name: Niall Murphy
    text: "Speaking personally - I would disconnect from the job title and think about\
      \ the _behaviours_. Are there people in your org who are concerned about the\
      \ reliability of the ML stack? If so, maybe without realising it, they are MLREs.\n\
      My intuition today is that there are loads of people who care about the reliability\
      \ of what they\u2019re doing, but very few of them have the job title MLRE.\
      \ I suspect those that do, are in places with lots of existing SREs.\nI have\
      \ no opinion about whether or not MLRE will establish itself as a job title,\
      \ but I think the behaviour of caring about the reliability of your production\
      \ stack is going to continue indefinitely."
- name: Alexey Grigorev
  text: '&gt;  How ML, product, and production teams can communicate effectively

    Can you give a short summary?

    Also, what does each of these teams do? Why do we need 3 teams? And in which case
    it should be just one team with all these 3 functions inside the team?'
  replies:
  - name: Cathy Chen (she/her)
    text: This would really be a great one for Kranti Parisa! I'll check in with him
      if he's doing any better.
  - name: Cathy Chen (she/her)
    text: "ML engineering team could be that team who creates and trains the models.\
      \ Thinking your data scientists, with a bit of training and serving expertise.\
      \ (In case you haven't read the book: we have an imaginary online shoppe [yarnit.ai](http://yarnit.ai)\
      \  \nFor yarnit, this may be the team who is making ml models for suggesting\
      \ additional purchases on the \"view my cart\" page. \nProduct could be the\
      \ team who owns the overall product or the rest of the product. For yarnit,\
      \ the shopping cart might be part of the product team."
  - name: Cathy Chen (she/her)
    text: ML production is the team who ensues that all the training and serving infrastructure
      is up and working
  - name: Niall Murphy
    text: "large company bias, of course, but yes, those functions can all totally\
      \ co-exist in the same team. in which case the problem isn\u2019t necessarily\
      \ communication, it\u2019s communication of value of the different types of\
      \ work, and deciding how to allocate resources towards those types of work."
- name: LOIC EMO SIANI
  text: Hello. After reading the book, can we apply for a MLRE role in a company?
  replies:
  - name: Niall Murphy
    text: _me grins_
  - name: Niall Murphy
    text: "I think there\u2019s nothing to stop you applying even before you read\
      \ the book"
- name: LOIC EMO SIANI
  text: Hello. How many pages has this book?
  replies:
  - name: Niall Murphy
    text: "I strongly suspect you\u2019d be as capable of establishing that as I am:\
      \ [https://www.amazon.co.uk/dp/1098106229?linkCode=gs2&amp;tag=oreilly20-21](https://www.amazon.co.uk/dp/1098106229?linkCode=gs2&amp;tag=oreilly20-21)"
- name: LOIC EMO SIANI
  text: Hello Cathy Chen (she/her) A1IndiaDS Kranti Parisa todd underwood. I have
    a question. What are the tools used in the book to set up a system to proactively
    monitor ML models ?
  replies:
  - name: Niall Murphy
    text: "We are deliberately \u201Ctool agnostic\u201D. We don\u2019t recommend\
      \ any specific tools (we do mention a few). We focus on general principles instead.\n\
      (This might mean we\u2019re not a good book for you, but we think many of the\
      \ principles and recommendations can be easily translated into whatever tools\
      \ you happen to be using.)"
- name: LOIC EMO SIANI
  text: What are the relevant skills required to be a MLRE ?
  replies:
  - name: Niall Murphy
    text: "It\u2019s more of a mindset than a skill, as such, but if I had to pick\
      \ one, I would say \u201Csystems thinking\u201D. This is IMHO the largest distinction\
      \ between product developers focused on features and \u2026 well, more or less\
      \ anything else, really.\nSystems thinkers focus on the whole thing, and think\
      \ deeply about the interaction between subcomponents of the system. We believe\
      \ this aligns very well with ML, which almost by its nature is very cross-cutting/horizontal.\n\
      In order to develop this skill, I would probably start off by looking at these\
      \ books: [https://www.mostrecommendedbooks.com/lists/best-systems-thinking-books](https://www.mostrecommendedbooks.com/lists/best-systems-thinking-books)\
      \ but if you\u2019re looking for something more concrete I can follow up."
- name: Michal
  text: Hello, what are the main differences between your book and Chip Huyen's Designing
    Machine Learning Systems?
  replies:
  - name: Cathy Chen (she/her)
    text: "todd underwood read Chip's book \U0001F4DA so hopefully can answer this\
      \ best (Niall Murphy as well?)"
  - name: Niall Murphy
    text: "Yep. In my opinion the differences are:\n- Chip focuses on model creation.\
      \ We don\u2019t really touch that at all. (And you might ask - an ML book NOT\
      \ about model creation?? How does that make sense?? To which the answer is\u2026\
      )\n- We focus on \u201Cthe whole system\u201D, including the organizational,\
      \ ethical, and technical components of what it means to have ML in your company.\n\
      There\u2019s plenty to learn from both and we both blurbed each other\u2019\
      s books, IIRC, but you might start reading Chip\u2019s book first if you\u2019\
      re an IC (ML) engineer and you care most about making models and the wider context\
      \ doesn\u2019t matter to you. You might start reading our book first if you\u2019\
      re an IC engineer in DevOps, SRE, a PM/TL, manager or VP, and you care about\
      \ the wider context for some reason."
- name: Michal
  text: How many code examples does your book include? Is it primarily focused on
    Google Cloud / TensorFlow, or is it framework agnostic?
  replies:
  - name: Cathy Chen (she/her)
    text: We don't have code examples as we tried to stay agnostic of frameworks.
      We did have some reviewers from Google Cloud since three of the authors are
      Google employees, but that was mainly to ensure we didn't do anything counter
      to their product direction.
- name: Michal
  text: What's the difference between MLOps engineer and ML SRE?
  replies:
  - name: Cathy Chen (she/her)
    text: 'This really depends but what we are finding is that AIOps usually refers
      to using AI to automate operations and ML Ops refers to the teams or people
      who operate the ML system/pipelines. Our definition of ML SRE is aligned with
      that definition of ML Ops.

      Also, todd underwood was in a panel at SRECon 2021 where a variety of folks
      discussed OpML [https://www.usenix.org/conference/srecon21/presentation/panel-opml](https://www.usenix.org/conference/srecon21/presentation/panel-opml)'
  - name: Niall Murphy
    text: "There isn\u2019t a huge distinction IMHO, and whatever distinction exists\
      \ right now, the linguistic meat grinder of the industry will mess up over time\
      \ \U0001F642"
  - name: Michal
    text: "Thank you for your answers x3 \U0001F642"
- name: Carlos Pumar
  text: "hi! While reading thru the table of contents of your book, I wondered:\n\
    1. *Organisational aspects*: \n    a. assuming a firm has interest in creating\
    \ internal capabilities for creating data-driven processes (e.g. creating a team\
    \ of specialists which collect data, select models, deploy and maintain them):\n\
    \        i. what could be criteria for deciding between investing in (re-)training\
    \ their existing staff vs. hiring specialists from \u201Coutside\u201D?\n    \
    \    ii. what measures could be undertaken to minimise the risk of people leaving\
    \ and potentially creating a \u201Chole\u201D (in terms of knowledge management)\n\
    \    b. assuming a firm has not yet decided between creating internal capacities,\
    \ vs. leveraging from services from third institutions (\u201CSaaS\u201D):\n \
    \       i. what could be criteria for deciding between these options?\n    c.\
    \ how could, in your view, one argument in favour of using open-source libraries\
    \ in a firm, towards which whose decision-makers might be skeptical to (mainly\
    \ for security issues)?\n2. *Model deployment and maintenance*:\n    a. even though\
    \ I lack of practical experience, it seems to me that \u201Cbatch training\u201D\
    \ is the default methodology for training models (as opposed to the alternative\
    \ of \u201Conline training\u201D)\n        i. if this is true: what are the main\
    \ reasons that \u201Conline training\u201D has not established itself as much\
    \ as batch, especially vis-\xE0-vis the risk of \u201Cdata drift\u201D (which\
    \ online training systems don\u2019t suffer of)\n        ii. what are good practices\
    \ for minimising the risk of data leakage (in the training phase) so that model\
    \ performance doesn\u2019t get affected in production?\n3. Does your book cover\
    \ aspects regarding *regulatory issues* as to how to manage data (e.g. often financial\
    \ institutions are strongly regulated by norms defined by regulatory bodies, which\
    \ limit financial institutions in their data-management decisions (e.g. model\
    \ deployment on the cloud))?\nMany thanks in advance!"
  replies:
  - name: Niall Murphy
    text: "Cathy Chen (she/her) would probably have some ideas for a lot of this,\
      \ but I\u2019ll do what I can.\n1ai: time, throughput, and feasibility, as always.\
      \ do you have a specific deadline for doing something which is infeasible with\
      \ current staff? there\u2019s a longer discussion that can be had here\n1aii:\
      \ the best \u2018conversion\u2019 project I know of (netops folks to SREs) promised\
      \ and _actually gave_ transition/education support, had a reasonable timeframe\
      \ (~18 months) and strong management support. in general many folks are up for\
      \ expanding their capabilities as long as they\u2019re treated well.\n1bi: the\
      \ classic build-vs-buy (see e.g. [https://rootly.com/buy-vs-build](https://rootly.com/buy-vs-build))\
      \ discussion generally ends up dividing things like this: \u2018if it is core\
      \ to your business or feasibly could become so in a reasonable time-frame, build\
      \ it. otherwise buy it.\u2019\n1c: OSS and security isn\u2019t really my thing\
      \ but see e.g. [https://www.zdnet.com/article/is-open-source-as-proprietary-software-these-tech-chiefs-think-it-is/](https://www.zdnet.com/article/is-open-source-as-proprietary-software-these-tech-chiefs-think-it-is/)\
      \ - if this is specifically within the context of ML i would probably argue\
      \ that right now the whole domain is so wild-west that there is no significant\
      \ quality difference between enterprise software and startup code and OSS.\n\
      2ai: (i call \u201Conline training\u201D \u201Ccontinuous training\u201D instead.)\
      \ they are both very popular in different contexts, but \u201Cthe large companies\u201D\
      \ have the resources to make continuous training a practical thing. to my mind\
      \ continuous training absolutely has risk of data drift just like batch. it\u2019\
      s just a question of the periods between the batches.\n(short answer: resources\
      \ IMHO)\n2aii: not sure what you mean by \u2018data leakage\u2019 - can you\
      \ expand?\n3: it mentions regulation in the ethics &amp; privacy chapter, mostly\
      \ in the context of motivating/illustrating various privacy techniques. many\
      \ of the things you do in order to preserve privacy, balance training data,\
      \ etc, also end up being the things you\u2019d do to align with e.g. financial\
      \ regulation. we don\u2019t discuss financial regulation in detail. off-hand\
      \ comment based on experience: many (not all) assertions about \u201Coh we can\u2019\
      t do X because the regulator forbids it\u201D actually is considerably more\
      \ nuanced than that if you actually got to talk to a regulator."
  - name: Carlos Pumar
    text: "thank you for your detailed response Niall Murphy!\nre \u201Cdata leakage\u201D\
      : I wonder if there are practices in order to avoid that models have access\
      \ to information during training phase, which they would not have when tested\
      \ on new, unseen data. As an example, you would want to combine cross-validation\
      \ with pipelines (sklearn package) in order to avoid this leakage\u2026\nI was\
      \ just wondering if there are any other standard measures in practice which\
      \ avoid the model from picking up information related to the labels at training\
      \ time - and if your book covers (parts) of these measures. thx again"
  - name: Niall Murphy
    text: "Partitioning training data is not an inherently difficult act, but it does\
      \ require discipline about what you make accessible to the training process\
      \ (and what you don\u2019t). In the situation where leakage is a threat, I\u2019\
      m wondering what is the information that\u2019s accessible that shouldn\u2019\
      t be? Are we talking about labels being accessible when they shouldn\u2019t\
      \ be, or labels being present at all?"
  - name: Carlos Pumar
    text: "sorry for being imprecise: I actually meant labels being accessible when\
      \ they shouldn\u2019t be, i.e. patterns of labels are accessible to model during\
      \ training - making the model to potentially underperform with new data.\nI\
      \ am particularly interested in understanding how to avoid this sort of leakage\
      \ so that performance is satisfactory in production\u2026and just curious to\
      \ know if there are any \u201Cbest practices\u201D during the workflow prior\
      \ to model deployment\u2026thx again!"
  - name: Cathy Chen (she/her)
    text: "For 1....\nGo ahead and skim chapters on org design (13-14) because we\
      \ try to give a framework that you can use to work this out. Based on structure\
      \ decisions, you need to then think about how to accomplish the best for end-to-end\
      \ product reliability by adapting process, metrics, people mindsets, and rewards...\n\
      1i. Depends on what you're looking to do. Often a combination of both is a useful\
      \ thing as long as you have the right mindset in mind. \n1ii. Always be training\
      \ your replacement? I like the book \"Influencer\" - there a chapter about a\
      \ restaurant in SF where every person is trained by the last person who started.\
      \ Everyone eventually does tasks, trains others, mentors others. Of course there's\
      \ also the need to specialize. We specialize on projects across regions but\
      \ generally have everyone at a baseline knowledge to be able to be oncall\n\
      1.b-c sorry don't know \n2. Sorry not my area of expertise \n3. Not that I know\
      \ of."
- name: Marc
  text: What would be a book to read before and after reading your book?
  replies:
  - name: Niall Murphy
    text: "if you don\u2019t have an SRE background, you might like to get started\
      \ with one of the big two beforehand.\nafterwards? maybe [https://www.oreilly.com/library/view/practical-fairness/9781492075721/?_gl=1*95hemv*_ga*MTA2ODM2NTQzNi4xNjU1NjQ3NTg4*_ga_092EL089CH*MTY3MDI2NTc4Ny4zLjEuMTY3MDI2NTg2NS41Ny4wLjA](https://www.oreilly.com/library/view/practical-fairness/9781492075721/?_gl=1*95hemv*_ga*MTA2ODM2NTQzNi4xNjU1NjQ3NTg4*_ga_092EL089CH*MTY3MDI2NTc4Ny4zLjEuMTY3MDI2NTg2NS41Ny4wLjA).\
      \ if you want to investigate fairness more.\notherwise, uh, i dunno. you\u2019\
      ll probably be quite tired. calvin &amp; hobbes maybe?"
  - name: Cathy Chen (she/her)
    text: '+1'
  - name: Niall Murphy
    text: "(the big two being \u201Cthe SRE book\u201D and \u201Cthe SRE workbook\u201D\
      )"
- name: David Braslow
  text: As a data scientist who is used to working in notebooks and is just starting
    to think about how to deploy models reliably at my company, what would be the
    top 1-3 things you would suggest focusing on?
  replies:
  - name: Niall Murphy
    text: "i think others would be better at answering this than me, particularly\
      \ Kranti Parisa, but i would probably start by thinking deeply about what the\
      \ non-notebook workflow is gonna look like. they\u2019re terrible for reproducibility\
      \ imho"
- name: Shiro Kulatilake
  text: When looking at the entire ML Loop what is the org structure that works best
    - having the ML model work being done by a separate team and then integrated into
    the apps or having a mix of people in various stages of the entire loop ?
  replies:
  - name: Niall Murphy
    text: "Hi Shiro: speaking for myself, _there is no answer to this question_. There\
      \ isn\u2019t a \u201Cbest\u201D. Everything, especially organizational decisions,\
      \ are contextual. I will say that centralised models are better in concentrating\
      \ expertise and improving domain performance, but can often end up being unresponsive\
      \ to business needs. Distributed models are better at responding to the needs\
      \ of the team, but can have staff expertise/retention/etc problems.\nDecide\
      \ what your org is weak in and what needs to be fixed, then take the appropriate\
      \ action\u2026"
  - name: Cathy Chen (she/her)
    text: I would say that the major thesis of the book is that we posit that it is
      better if people across the organization know enough about ML (and not having
      ML be completely silo'ed). And agree there is no best.  Every org design has
      issues and is not always practical or possible. Chapter 14 covers some practices
      to think about based on what the org structure looks like.
  - name: Shiro Kulatilake
    text: Thank you for your responses !
- name: Cathy Chen (she/her)
  text: Apologies that Kranti Parisa is out sick this week. He will try to join late
    in the week.
  replies:
  - name: Alexey Grigorev
    text: Oh no, I hope he gets better soon!
- name: Alexey Grigorev
  text: What are the most important SRE principles that ML projects should adopt?
  replies:
  - name: Niall Murphy
    text: "Gosh. There\u2019s a lot to choose from. I think\u2026 well, measuring\
      \ things is important, and is an SRE principle, but I think model development\
      \ understands that quite well.\n(Sometimes there are question marks around continuing\
      \ that approach to measurement in production as opposed to the development cycle,\
      \ but broadly speaking I think we\u2019re covered here.)\nMaybe eliminating\
      \ toil? [https://sre.google/sre-book/eliminating-toil/](https://sre.google/sre-book/eliminating-toil/)\
      \ I suspect there\u2019s still quite a bit of toil around a lot of what ML folks\
      \ do.\nDefense in depth is another good one. Our serving and training systems\
      \ can be quite brittle; putting some work into having algorithmic fallback can\
      \ be really useful."
- name: Ixchel Garcia
  text: hi everyone, I wanted to ask recommendations on books about Data Engineering,
    ML engineering and data infrastructure. I would deeply appreciate if you could
    give me a top 3 choices please. I want to specialize as a DS in the engineering
    behind data and ML.
  replies:
  - name: Niall Murphy
    text: "Hi Ixchel - I\u2019m not sure, but I _think_ this channel is for questions\
      \ related to the book of the week, rather than books in general?"
  - name: Ixchel Garcia
    text: 'Oh sorry I guesses this was the most appropriate channel of all hahaha
      :face_with_peeking_eye:'
  - name: Niall Murphy
    text: "I don\u2019t know for sure, but hopefully someone who knows the Slack best\
      \ will comment."
  - name: Alexey Grigorev
    text: "We have invited authors of books on these topics in the past, you can check\
      \ them in the archives \n[https://datatalks.club/books.html](https://datatalks.club/books.html)\n\
      And for most of the books we also have the answers from the authors there"
- name: LOIC EMO SIANI
  text: Hello. Is there any prerequisites we must have to read the book if we already
    have mlops background ?
  replies:
  - name: Niall Murphy
    text: "I can\u2019t think of any, no. (And it was written to be readable by a\
      \ very wide audience.)"
  - name: Cathy Chen (she/her)
    text: Definitely no prerequisites.
  - name: LOIC EMO SIANI
    text: ok thanks.
- name: Ataliba Miguel
  text: At what stage of the project should one plan/think to start implementing MLRE?
  replies:
  - name: Niall Murphy
    text: "Some signals to think about:\n- do you believe you\u2019re going to rapidly\
      \ scale, in which case \u201Cgetting out in front of it\u201D might be a good\
      \ idea\n- are you currently experiencing reliability problems\n- how much time\
      \ do model developers spend fighting with infra\nIn general, by the time the\
      \ argument is unassailably clear for doing reliability work, you would have\
      \ saved some time/money/effort starting about six months beforehand \U0001F609"

---

Whether you're part of a small startup or a multinational corporation, this practical book shows data scientists, software and site reliability engineers, product managers, and business owners how to run and establish ML reliably, effectively, and accountably within your organization. You'll gain insight into everything from how to do model monitoring in production to how to run a well-tuned model development team in a product organization.

By applying an SRE mindset to machine learning, authors and engineering professionals Cathy Chen, Kranti Parisa, Niall Richard Murphy, D. Sculley, Todd Underwood, and featured guest authors show you how to run an efficient and reliable ML system. Whether you want to increase revenue, optimize decision making, solve problems, or understand and influence customer behavior, you'll learn how to perform day-to-day ML tasks while keeping the bigger picture in mind.

You'll examine:

- What ML is: how it functions and what it relies on
- Conceptual frameworks for understanding how ML "loops" work
- How effective productionization can make your ML systems easily monitorable, deployable, and operable
- Why ML systems make production troubleshooting more difficult, and how to compensate accordingly
- How ML, product, and production teams can communicate effectively
