---
title: "Machine Learning Engineering in Action"
description: "Book of the Week. Machine Learning Engineering in Action by Ben Wilson"
cover: "images/books/20210301-ml-engineering/cover.jpg"
image: "images/books/20210301-ml-engineering/preview.jpg"
start: 2021-03-01 00:00:00
end: 2021-03-05 22:59:59
authors: [benwilson]
links: 
  - text: Book's page on Manning
    link: https://www.manning.com/books/machine-learning-engineering-in-action
  - text: Book's GitHub repository
    link: https://github.com/BenWilson2/ML-Engineering

archive:
- name: Akshaya Natarajan
  text: Ben Wilson Hi Ben! Can you share some common examples that you have come across
    where one might assume an ML solution to the problem but alternate approaches
    are way cheaper and efficient?
  replies:
  - name: Ben Wilson
    text: 'Hi Akshaya Natarajan, great question!

      I''d have to say that, in broadly general terms, this is ''the hammer'' problem.

      "When all you have is a hammer, everything looks like a nail".

      I think it''s a default behavior for most modern ML practitioners that, when
      faced with a seemingly complex problem, they frequently default to supervised
      or unsupervised learning.

      To answer your actual question, for examples... I might as well talk about dumb
      things that I''ve done and later fixed with a much more simplistic (and cheaper,
      easier to maintain, etc.) solution.

      - Spending 2 months building a custom customer segmentation and similarity ensemble
      using KMeans, MinhashLSH, and a determinism-enforcing cluster labeling approach.
      It was about 3000 lines of modular and abstracted code. The final implementation
      was quantile bucketing on 3 variables to identify cohorts. With SQL. In about
      25 lines of script.

      - Transfer learning on ResNet50 to build a classifier that identified the primary
      color present in clothing on a person in an image. Training that on 118M images,
      adding some layers, and struggling with improperly labeled data took about 4
      months of work. It got it right about 97% of the time at a cost of ~100k.  Over
      a weekend, just for fun, I tried to use old-skool computer vision and some color
      space inversions (RGB-&gt; HSV, filter skin tones -&gt; RGB) and basic bucketing
      aggregations on the pixel data. It was basically 100% accurate and could run
      on my laptop. I had the MVP done in a weekend.

      - Building an XGBoost + shap implementation for a business problem that identified
      as ''key important features'' elements that were just general knowledge that
      the business operations team already knew and were part of their current daily
      job. (In this case, just walking over to the other side of the office building
      and having a quick 5 minute conversation could have saved me 3 weeks of work).

      I have countless other stories like these that I''ve seen customers do (recent
      trends seem to favor a LOT of DL approaches to otherwise ''already solved''
      methodologies). It''s one of the reasons that I chose the example implementation
      in the book (Chapters 6 - 8 ) for time series modeling. Could an LSTM, properly
      tuned, beat the prediction accuracy? Sure, probably. Could you build it and
      have it ready for production in the same amount of time? Heck no.'
  - name: Akshaya Natarajan
    text: Wow amazing examples!! Thank you for sharing them. This is something to
      really think about! I completely get your computer vision example as I did something
      similar during one of my coursework. A simple MAP approach worked much better
      the 'state-of-art-models'.
  - name: Doink
    text: Ben Wilson so for time series which approach would you take?
  - name: Ben Wilson
    text: "Whichever approach is best for the problem being solved \U0001F61C.\nChapters\
      \ 5,6, and 7 actually go through my exact process of prototyping (including\
      \ all of the comical failures) for a seasonality dominated, non stationary forecasting\
      \ use case. \nI don't get into a bakeoff with DL, but I have used RNN's and\
      \ LSTM's in the past to solve forecasting problems, but I only go to DL implementations\
      \ if the arguably simpler ARIMA-based methods don't work well.\nI always choose\
      \ fast and cheap over complex and expensive if I can."
- name: Sejal Vaidya
  text: 'Hi Ben, nice to have you here.

    Your book looks really interesting from an e2e ML project aspect.

    My question is: Do you have a framework or a set of ways to understanding/approaching
    a problem and defining the business requirements and scope of an ML project?'
  replies:
  - name: Ben Wilson
    text: 'A framework? Eh, not really.

      I like to listen. I ask the business in a casual discussion about what they
      want to solve. Then I listen.

      If the conversation seems like magical thinking (they''re talking about something
      that is so far beyond the scope of current capabilities of humanity that it''s
      doomed from an implementation perspective), then I gently steer the conversation
      to something that is more practical.

      I never have just a single discussion at the outset either. After an initial
      ''brainstorming'' session, I try to have some one-on-one discussions with the
      subject matter experts. If I''m building something that is intended to augment
      their job functions, then I want to watch them work. I''ll sit with them and
      quietly observe what it is that they''re struggling with, how they do that task,
      and try to gain as much insight into what they find frustrating or annoying
      about doing it manually.

      If it''s something that is wholly new to the company (and myself!), then I like
      to have space between initial planning meetings and followup sessions where
      I can share options based on research and testing.

      The TL&amp;DR answer, though, is: ask a lot of questions, listen to the answers,
      and interview people 1:1. Then go and do some research and thinking about how
      to solve it, and discuss what the options are with the business in non-technical
      terms.

      Just stick with that quote from Einstein and it won''t fail you:

      "If I had an hour to solve a problem, I''d spend 55 minutes thinking about the
      problem and 5 minutes thinking about solutions."

      You''ll get into trouble if, immediately upon hearing the problem, start thinking
      about feature data to collect, which algorithms to use, and instantly running
      out to find a blog that someone did on the subject to follow along with.'
  - name: Sejal Vaidya
    text: "Thank you for answering! Of course, I agree that there can't be a standardized\
      \ way of doing this. I was actually thinking more around the lines of what you've\
      \ stated in chapter 3 (planning &amp; scoping) of your book: [https://livebook.manning.com/book/machine-learning-engineering/chapter-3/v-5/](https://livebook.manning.com/book/machine-learning-engineering/chapter-3/v-5/)\n\
      to get an idea on your approach of understanding the problem and gathering requirements\
      \ based on that. \nYour answer was certainly helpful. I'm presently looking\
      \ at taking new responsibilities in Management along with my current Engineering\
      \ tasks at work, and will try this out.\nThank you again. :)"
  - name: Ben Wilson
    text: 'So you''re going to be the gatekeeper and the rosetta stone for the ML
      team?

      I wish you good luck and hope you enjoy the new role. It''s arguably the most
      critical position in a DS team.

      My best advice on this? Make friends. Get to know people in the different business
      units (not just management folks, but more the ''boots on the ground'' people
      who actually are doing the work in their departments or divisions). With a healthy
      working relationship, they can help to explain what a project needs to accomplish
      in the terms of how it applies to that group.

      Ask a LOT of questions as well. Probe in as many ways as you can to figure out
      the hidden ''gotchas'' of things that you may need to consider when building
      a solution (these elements are usually obvious elements to the business unit
      team, but are completely not-obvious to an outsider).

      "Why do you not ever do ''x'' to group ''y''?"

      "Oh, because they''re completely different in how they behave. We have different
      rules for how to interact with them." &lt;- these insights can help to define
      what they actually want out of the project. They''re also ways for you to identify
      if an ML solution can even handle those ''special case'' elements.

      As for scope, that''s all about collecting the total wishlist (with accompanying
      details that you garner from those interview-style interactions that you have
      with SMEs) and making a solid estimate based on your previous history solving
      similar tasks.

      Then you lay out the timeline with options. Let the business sponsor determine
      what''s palpable. Associate each feature with a dollar and time value, which
      can really put the elements of features into terms that they can grok.'
  - name: Sejal Vaidya
    text: "Wow, that's very insightful! Thank you so much for sharing this. \U0001F603\
      \ A lot of this is still quite new to me. I'm certainly not a gatekeeper, but\
      \ I'm only gradually taking some of these responsibilities. So yes, nervousness\
      \ with excitement but good support from my managers. Let's see how it goes.\
      \ \U0001F605"
- name: Alexey Grigorev
  text: Hi Ben! You have a chapter "moving from prototype to MVP". What's the main
    difference between a prototype and an MVP in your opinion? I see these terms are
    used interchangeably
  replies:
  - name: Ben Wilson
    text: 'I''ve always seen prototypes as the equivalent of ''script complete'';
      basically, the model functions well enough (perhaps not fine-tuned, but it meets
      the requirements for the most part).

      MVP phase is where everything else is done. The script has been transformed
      into maintainable abstracted code, unit tests are written, integration tests
      are finalized, monitoring / logging / registration capabilities are in place,
      and, perhaps most importantly, user acceptance testing (QA) is done. When all
      of those components are finished up with some form of hyperparameter tuning
      in place to automate away the infinitely frustrating task of guessing at good
      values, then you''re ready to do a production release with the MVP.

      Basically when the MVP is delivered, it''s not the DS team that marks the project
      as a success. Rather, it''s the business that gives the thumbs-up, confident
      in the solution''s effectiveness to solve their problem.

      The reason that I use the term ''MVP'' is that all ML projects are, by virtue
      of how mutable they end up being over time (if they''re useful), constantly
      evolving to new versions. Features added or removed, more sophisticated approaches
      (or less!) are developed to solve the problem, or just minute drift-driven tweaks
      being done to the code base for ongoing maintenance.'
  - name: Alexey Grigorev
    text: Thanks! So there's a vast difference between a prototype and an MVP!
- name: Alexey Grigorev
  text: 'Another one: the purpose of a prototype is to validate things as quickly
    as possible. How do we maintain code quality while still cutting corners and moving
    fast? Do you have any suggestions about that?'
  replies:
  - name: Ben Wilson
    text: 'I never use my prototype code for building an MVP. It''s usually embarrassingly
      sloppy and difficult to read script. I''m trying out perhaps dozens of approaches,
      multiple different packages, have some unintelligible to anyone but me shorthand
      notes, and sometimes some less-than-professional variable naming conventions
      (depending on how frustrated I am in the build process of testing things).

      Once I have something that seems like it works well enough, I use my terrible
      scripted nonsense to build out functions, abstracting away complexity and defining
      reusable fragments of code.

      It''s from this point that I will do a presentation of the prototype to the
      team (and SME''s). If everyone agrees that it''s worthwhile to build out properly,
      I''ll start using those functions to design a maintainable code architecture,
      building classes, objects, et al. to create a ''proper code base''. Every piece
      of work from that point on is done through branch commits, PR''s, and proper
      merges.

      I''m also a fan of creating abstract utility modules to help me in my day to
      day work of prototyping and MVP development. I''m a super lazy developer and
      it pains me to have to re-implement the same logical block in different projects,
      so I''ll just put that functionality into its own repository with other similar
      ''tooling''. Over time, as that common code base grows, the amount of ''terrible
      code'' that needs to be written during the fast prototyping phase reduces significantly.'
  - name: Alexey Grigorev
    text: Great, thanks!
  - name: Alexey Grigorev
    text: Just curious, how many of your prototypes don't survive and don't become
      an MVP?
  - name: Ben Wilson
    text: "My prototypes work 100% of the time, 5% of the time.\nMy general rule of\
      \ thumb is that for any production-grade, truly useful ML solution that I've\
      \ built, I typically throw away 80-90% of all code written during the journey\
      \ to production. \nThere are always crazy ideas that I thought would be clever\
      \ (and usually aren't), inefficient code, computationally or space complexity\
      \ issues that need refactoring, or just a load of trials of ideas that don't\
      \ pan out.  I think that having a mindset when approaching ML work that you\
      \ are expecting to throw away a lot of things (which is good - it means you\
      \ approached the problem like a scientist, testing hypotheses) and also time-boxing\
      \ idea trials is one of the most successful ways of going about it."
  - name: Alexey Grigorev
    text: That's a good idea to have that mindset - thanks for sharing it !
- name: Wendy Mak
  text: Hi Ben, what do you think are some of the biggest mistakes people/companies
    make when trying to move ML from experimental prototypes to fully functional products?
  replies:
  - name: Ben Wilson
    text: "Hi Wendy, that's a great question. It's actually pretty much the synopsis\
      \ for the entire book.\nIf I were to rank mistakes for the top 5 things that\
      \ I see 'blow up a project'....\n1. Not having business buy-in on the solution\
      \ / not knowing what the actual 'thing' is that you're working to build. (No\
      \ matter how fancy the algorithm utilized, how cool the code is, how production-ready\
      \ it is... if you're not solving the problem for the business, the project is\
      \ D.O.A.)\n2. Not having attribution monitoring set up (the \"how well is this\
      \ solution solving our problem\" question). If you can't measure your solutions,\
      \ the business is just guessing at its effectiveness. You don't want the project\
      \ to get blamed for being either successful or detrimental with the nigh infinite\
      \ realm of  exogenous latent factors that drive a business. With data, statistical\
      \ tests, and (perhaps) causality modeling to go along with the the hypothesis\
      \ testing and attribution modeling, you're armed with the munitions needed to\
      \ defend the solution.\n3. Terrible code standards. Unreadable code, fragile\
      \ code, and dangerous code. The number of times that I've seen blind exception\
      \ eating cause production down-time that erodes the business' faith in the DS\
      \ team is too many to count. \n4. Decision paralysis. No one can decide on what\
      \ direction to go in from the prototype phase because everyone has spent so\
      \ much time on their solution. Having no process about time-blocking experimentation,\
      \ research, and testing of theories can cause an emotional attachment to prototype\
      \ solutions (I think there's something in there about behavioral sciences and\
      \ psychology... I'm not an expert about that, I'm just reporting what I've seen\
      \ and experienced).\n5. The business expects magic and no one on the DS team\
      \ has told the business that they are not, in actuality, wizards, sorcerers,\
      \ conjurors, or mythical beasts capable of snapping their fingers and just 'making\
      \ it happen'. The 'it like magic' perception at some companies and the hubris\
      \ of very junior DS practitioners can be a recipe for disaster. \nThere's about\
      \ 600 other pages that'll be in the final book that touch on many of the other\
      \ things that I see (and have lived through) cause projects to blow up in people's\
      \ faces. \U0001F642"
- name: Denis Lepchev
  text: 'Hi Ben!

    How do you think a notebook based environment will evolve to make it more suitable
    for production-ready development? Do you envision a convergence between notebooks
    and full-fledged IDEs? Do you think the industry got it right at the moment?'
  replies:
  - name: Ben Wilson
    text: "Hi Denis!\nOooooh... is this a question for Ben the author of this book,\
      \ or Ben the Practice Lead at Databricks? \U0001F609\nThere is a great deal\
      \ of active development in this area - basically to bridge the gap between the\
      \ benefits of an IDE (depending on language utilized, this can be substantial\
      \ - Java or Scala ML development outside of an IDE is a nightmare) and that\
      \ of a notebook (embedded visualizations, widgets, live data-focused results\
      \ in a friendly environment). A lot of work to support the bridging of these\
      \ different development practices is in abstraction of code in notebooks, utilizing\
      \ caller and callee notebooks that can be wrapped up in a project structure\
      \ that can be properly version controlled (branching, merging, et al.).\nPart\
      \ 2: Do I think people have this figured out?\nNo. Emphatically, no. There is\
      \ a massive gap between how DS's work (primarily in notebooks), focused on a\
      \ lot of feature work (ELT + cleverness) and algorithm utilization and how production\
      \ code is written.\nI don't think an easy solution exists to make the transition\
      \ between prototype script in notebooks (even if you're using functions) to\
      \ production-grade abstracted FP/OO based testable code. Every time I do a production-grade\
      \ ML project, I'm doing my prototyping and hacking away in notebooks, only to\
      \ have to port over functionality into OO modules in a package. It's time consuming,\
      \ frustrating to test during development and annoying to debug in an IDE.\n\
      I think a big part of why a lot of this hasn't reached a critical mass until\
      \ recently is that large-scale production-hardened ML code hasn't been adopted\
      \ by enough companies yet. Many are running notebooks in production, struggling\
      \ with issues that crop up, wasting countless hours updating scripts to keep\
      \ the lights on, and generally hating life when they ship something to 'production'.\
      \ There are, of course, plenty of teams out there that are packaging their ML\
      \ solutions into .jar's, .egg's, .whl files, etc. They just sort of 'deal with\
      \ it' like I do. That's not to say that anyone enjoys the process, though."
  - name: Denis Lepchev
    text: "&gt;  is this a question for Ben the author of this book, or Ben the Practice\
      \ Lead at Databricks?\nIt was a question for both (I am a Databricks user) \U0001F642\
      \nSometimes I feel it is like a big elephant in the room that nobody notices\
      \ - but good to hear about the progress. You are right - probably critical mass\
      \ hasn't been reached yet."
  - name: Ben Wilson
    text: "You'll really like what's coming late summer / early fall this year \U0001F609"
- name: Alexey Grigorev
  text: 'Hi Ben!

    What are the key skills that a machine learning engineer should have? And what
    are their core responsibilities? How is this role different from data engineering,
    in your opinion?'
  replies:
  - name: Ben Wilson
    text: "I know what I look for in people who I interview \U0001F609 .\nDE skill\
      \ set...\n- SQL knowledge = pro\n- Python and/or Java or Scala = intermediate\
      \ data-focused skills of those languages\n- Deep understanding of space complexity\n\
      - Deep knowledge of real-time streaming architectures\n- Relational data modeling\
      \ theory\n- Capable of implementing architectures in RDBMS, NoSQL, GraphDB's,\
      \ and how to interface with Queues (streaming).\n- OO knowledge = intermediate\
      \ (should know how to use abstract classes, how to implement factory patterns,\
      \ and how to design with proper encapsulation, how not to make a mess with polymorphism,\
      \ how to write data generators for unit tests...)\n- FP knowledge is a plus\
      \ (I guess? some people really like it. I think it's pretty cool.)\n- How to\
      \ speak to Analysts properly.\n- How to be an agreeable and pleasant human.\n\
      ML Engineer: I really think this is just the natural progression of a DS. It's\
      \ a continuing education broadening of skills that I'm a firm believer that\
      \ any ML practitioner should be working towards.\n- Deep specialization in some\
      \ 'flavor' of ML (NLP, Timeseries, Computer Vision, traditional supervised learning,\
      \ unsupervised learning, bayesian... whatever you work with the most, you should\
      \ be VERY knowledgeable about not just how to use some API, but know how the\
      \ algorithms work and be able to read their source code implementation and explain\
      \ how it was coded to work the way it does).\n- General knowledge of 1 or 2\
      \ other fields of DS work from above.\n- Be able to construct standard DL architectures\
      \ from scratch.\n- Deep understanding of statistics, probability, and linear\
      \ algebra.\n- Highly proficient at OO.\n- Skilled at creating visualizations.\n\
      - Capable of talking to other humans in a way that doesn't give them a headache\
      \ (translate the geekspeak to layperson's terms)\n- Highly proficient at distilling\
      \ vague (or overly complex) requirements and designs into simple, explainable,\
      \ and story-level work tasks\n- Capable of public speaking\n- Proficient in\
      \ at least 2 software languages (non-declarative; OO / FP-based languages)\n\
      Maybe that was a bit too much. But, in essence, Data Engineers specialize in\
      \ different things than ML Engineers do. The one thing that is common between\
      \ them is that they're both working with data, manipulating it to make it useful\
      \ for purposes, and they're both writing professional code (and can do so in\
      \ several languages). To be successful at either requires a great deal of time,\
      \ effort, and the ability to be humble and pleasant to work with."
  - name: Alexey Grigorev
    text: Wow, that's very detailed, thank you!
  - name: Alexey Grigorev
    text: Just curious, why public speaking is in the list? is it a must-have or nice-to-have?
  - name: Ben Wilson
    text: 'If a DS can''t communicate to a crowd, they''re going to be hampered when
      having to explain how their solution works to the business and will be at a
      disadvantage in discussions with internal customers.

      I''ve sent DS employees that I managed in previous companies (I''m an IC now,
      no direct reports) to public speaking classes to help them be more successful
      in this critical aspect of their careers. When they can ''find their voice''
      and learn to communicate in a complexity-free manner with  non-technical coworkers...
      that''s when they really shine.'
  - name: Alexey Grigorev
    text: That's nice of you to send them to classes! Makes sense, thank you
- name: Alexey Grigorev
  text: Also, what is the breakdown between ML and engineering for ML engineers -
    in terms of time spent working on these things?
  replies:
  - name: Ben Wilson
    text: 'In a typical project that I work on...

      30% research, reading, testing things, more reading, asking questions, talking
      to people about the problem.

      30% Getting the data into a state that is useable for the project, acquiring
      the data (writing scheduled ETL), fixing issues with the data.

      10% messing about with models, tuning them, having an algorithm tune them for
      me, figuring out how to improve the mess that I''ve created.

      20% Writing maintainable, extensible, abstracted, and testable code. CI/CD sometimes
      (usually if a large team is going to be messing with the code base frequently).
      Attribution, logging, and AB framework construction.

      10% Having meetings to win over the hearts and minds of the business. Listening
      to their feedback. Involving SME''s from the business to contribute their thoughts,
      perspectives, and deep knowledge to make the project better. Talking about it
      in presentations, convincing executives why it''s important. Apologizing to
      the Engineering Budget VP for why I blew through their yearly budget in the
      first 2 months.'
  - name: Alexey Grigorev
    text: That's quite a broad set of responsibilities! Like a full-stack data scientist
  - name: Ben Wilson
    text: "I'd say that's where I see most DS people end up going after 10 years experience.\
      \ If they're a solo person at a startup handling the full DS responsibilities\
      \ (with a lot of DE responsibilities baked in as well), it's basically a hard\
      \ requirement to have all of those skills (and more \U0001F609 ) to be successful."
  - name: Alexey Grigorev
    text: '&gt;  10% Having meetings to win over the hearts and minds of the business.

      I see why you want the engineers to be good at public speaking!'
- name: Matthew Emerick
  text: Hey, Ben Wilson! Thanks for doing this.  What ratio do you see for data engineers
    versus data scientists?  I know that more companies are suddenly hiring data engineers
    more than scientists, but where do you think it'll end up?
  replies:
  - name: Ben Wilson
    text: 'Oh, that''s a good question.

      I''d say it really depends on the industry, the age of the company, and the
      general skill of the workforce at the company.

      At startups, I often see "DaVinci''s" - women and men who have to assume the
      role of both DS and DE to get their projects working. At those small companies
      everyone sort of has to do everything. You learn a lot, but burn out quick.

      At non-tech-focused ''smallish'' companies (200-1000 employees, total tech workforce
      in engineering / analytics / ds might be 20 - 100? depending on industry)...

      If they were founded in the last 10 years, they''ve probably already got a modern-ish
      stack and have a lot of quality of life tooling to help them with DE tasks.
      So, typically not super DE-heavy. They also don''t have a lot of legacy systems
      loaded down with decades of techdebt to deal with. In these companies (if their
      data is cleanish), I see a big demand for DS''s who actually know what they''re
      doing (they''ve put 10+ projects into production at previous companies, have
      been around long enough to know how to generally do things right).

      If they''re an older company, the DE demand is MUCH higher. Loads of techdebt,
      weird decision made that make moving data around a completely excruciating process,
      and just need a lot more talented DE''s than they do DS''s. A DS in this environment
      won''t have too much to do until most of the techdebt is erased.

      Enterprise companies...

      hrmmmm...

      Which is more in demand?

      YES.

      Both. But skilled of both types. Typically you''re dealing with massive amounts
      of data (I''ve been working with a client recently who has a single data feed
      ingest through Kafka into Structured Streaming -&gt; Delta of ~ 160k records
      / sec, each payload is around 2MB uncompressed JSON). Some of the DE workloads
      for these customers are not for the faint of heart.

      ML for Enterprise companies is usually in pretty high demand and some execute
      better than others. The projects are typically very large-scale and complex
      so a large, well-managed team is critical to be successful there.'
- name: Alexey Grigorev
  text: 'As I understood, the target reader of the book is a "data scientist familiar
    with supervised machine learning and the basics of object-oriented programming".

    Will software engineers or data engineers also find your book useful? In case
    they want to transition into ML Engineering'
  replies:
  - name: Ben Wilson
    text: "For the process around building projects, certainly. I intentionally don't\
      \ go into the nuts and bolts of algorithm work or feature engineering work (that's\
      \ what your book's for \U0001F609 ).\nHand in hand with some books on algorithms\
      \ and applied ML / applied analytics and statistics, I think it completes the\
      \ intro breadth of topics that people would need to be successful at the start\
      \ of moving into this profession.\nFWIW, I do hear a LOT from DE's who want\
      \ to 'make the transition'. I always tell them the same thing when they ask\
      \ how much they need to learn... \"Just read up on stats. You already know how\
      \ to code (ed.: most can code better than 90% of DS folks) and you already understand\
      \ how to handle data. Algos and stats is all you're missing.\""
  - name: Alexey Grigorev
    text: Makes sense, thank you!
- name: Alexey Grigorev
  text: And in general, what would you recommend doing for data engineers and software
    engineers if they want to get into ML engineering? What's the best way to make
    the transition, in your opinion?
  replies:
  - name: Ben Wilson
    text: '"Algorithms, stats, and get Alexey''s book on applied ML."'
  - name: Alexey Grigorev
    text: Nice sugguestion!
- name: Neal Fultz
  text: Hi Ben - Im working with a company that has stacked their model in to another
    company's (essentially a black box), and trying to control / monitor performance.
    How does ensembling / stacking / banditing affect the ways to monitor and troubleshoot
    models effectively?
  replies:
  - name: Ben Wilson
    text: "Depending on the model, that could be a black box inside another black\
      \ box (model inception? pimp my ride, ML-edition? \U0001F609 )\nJokes aside,\
      \ I feel your pain. Attribution modeling is rarely a super fun thing to build\
      \ when you don't have direct control of the model and can only kick off a retraining\
      \ and 'hope for the best'.\nIn the scope of ensembles in general, you're compounding\
      \ the issue of traceability to begin with. When you're looking at performance,\
      \ you're evaluating the correlation of features to a target (I assume we're\
      \ talking about supervised learning here) and scoring some loss or error function.\n\
      The 'easy way' that most people build ensembles (that's a joke. Ensembles are\
      \ ML on hard mode for production stability and maintainability considerations)\
      \ is to just score the final stage for stacking (and ignoring the interim stacked\
      \ states or not logging them anywhere). For pooled ensembles, where you're applying\
      \ a custom function to the results of many individual models... well, hopefully\
      \ each one is getting logged.\nI can't say that I see many ensembles in the\
      \ wild; if I had to guess the percentages that are being used (referring to\
      \ 'this runs in production, is useful, and has been running for &gt; 6 months')\
      \  as an overall percentage share of supervised modeling efforts, I'd say it's\
      \ less than 5%. My advice is to ensure that each model's tuning histories are\
      \ logged as children to a parent entry (the parent being the project as a whole\
      \ or the final model in a stacked implementation). MLflow works great for this\
      \ and gives you that provenance of all of the components.\nAs for attribution\
      \ (how does this crazy-complex implementation impact the problem that we're\
      \ trying to solve?), that'll be the same as any other model implementation;\
      \ just treat the ensemble as a single entity and score its merits through proper\
      \ hypothesis testing.\nStay tuned for Chapter 12 where I delve into this very\
      \ problem in (potentially overwhelming) detail - specifically attribution modeling,\
      \ AB testing, and drift detection.\nI mention drift detection here because you're\
      \ going to have a LOT of it with an ensemble. It's not going to be pleasant\
      \ to diagnose through analytics either.\nBest of luck!"
- name: Alexey Grigorev
  text: What the process should look like from identifying a user problem to solving
    it with ML in production? What are the steps in the process and which tools should
    we use at each step?
  replies:
  - name: Ben Wilson
    text: "The process that I typically use is probably a little controversial ;)\n\
      1. Make friends. Get to know the SME's that you're working with. Figure out\
      \ how they best learn / understand / communicate. Once you can REALLY talk with\
      \ them, they will tell you all the 'gotchas' about the domain's problem space.\
      \ If there is mutual respect and friendliness between the business unit experts\
      \ and the DS team, you will help each other out and work as a single unit.\n\
      2. Always look for a way to solve the problem WITHOUT USING ML. If you can solve\
      \ a problem with analytics or ETL, do that. We, as a profession, work to solve\
      \ problems, not use algorithms. The simplest approach is always the best approach.\n\
      3. Do your homework. This doesn't mean read 2 or 3 blog posts, see that everyone\
      \ is talking about XGBoost or Tensorflow and assume that those libraries are\
      \ the panacea to all of your woes. Read some books, read some white papers,\
      \ take your time to understand the problem space and then...\n4. Test a lot\
      \ of alternatives. But do it like you're competing in a Hackathon. Give each\
      \ attempt a fixed period of time. Remember that if it's super hard to get a\
      \ proof of concept working, it's going to be a nightmare to maintain in production.\
      \ \n5. Pick the most promising result from rapid prototyping. Don't pick the\
      \ 'new hotness'. Some of the best models I've built that have lasted the longest\
      \ in production have been generalized linear regression and Bayesian models.\
      \ The 'old stuff' might not be talked about much these days, but IT WORKS and\
      \ it works very well.\n6. Validate your data. Seriously, just please do formal\
      \ EDA. Correlation, collinearity analysis, distribution fits, etc..\n7. Use\
      \ the right tool for the job. Don't use Spark for a 20MB training set and don't\
      \ use scikit for a 200GB training set. \n8. Learn more than one language. We\
      \ do a lot of ETL as DS's. Scala is a great language.\n9. Don't be afraid to\
      \ let the business know early that it's an unsolvable problem. Pivot to something\
      \ easier.\n10. Watch your costs. Electrons are not free."
  - name: Alexey Grigorev
    text: 'That''s a nice one! Love #1. Thank you!'
  - name: Andy Petrella
    text: "the last 20 years I have been working on that subject told me that it very\
      \ vast. There are some important paper on it also like the one I love from D.\
      \ Sculley on hidden tech debt in ML.\nMy take on this is that it requires a\
      \ certain level of maturity of the team and even organization, because as Ben\
      \ Wilson says, in a way, the responsibility is spread as pipelines have dependencies.\
      \ Therefore the data culture is important\nThe maturity can be achieved IMHO\
      \ by introducing a specific management twist, which I called \u201Cdata intelligence\
      \ management\u201D (I recently wrote an article on that matter) - the focus\
      \ is on the data applications, not on the data.\nAlso, I have a forthcoming\
      \ O\u2019Reilly training on how to monitor ML in production with Python (the\
      \ first session is the 28th of April) that I\u2019ll invite you and the community\
      \ to join \u2014 when the page and announcement will be online ahaha."

---

Machine Learning Engineering in Action is a roadmap to delivering successful machine learning projects.
It teaches you to adopt an efficient, sustainable, and goal-driven approach that author
Ben Wilson has developed over a decade of data science experience. Every method in this book
has been used to solve a breakdown in a real-world project, and is illustrated with production-ready
source code and easily reproducible examples.

You’ll learn how to plan and scope your project, manage cross-team logistics that avoid fatal
communication failures, and design your code’s architecture for improved resilience. You’ll
even discover when not to use machine learning—and the alternative approaches that might be
cheaper and more effective. When you’re done working through this toolbox guide, you’ll be
able to reliably deliver cost-effective solutions for organizations big and small alike.