---
title: "Data Governance: The Definitive Guide"
description: "Book of the Week. Data Governance: The Definitive Guide by Jessi Ashdown"
cover: "images/books/20210524-data-governance-the-definitive-guide/cover.jpg"
image: "images/books/20210524-data-governance-the-definitive-guide/preview.jpg"
start: 2021-05-24 00:00:00
end: 2021-05-28 22:59:58
authors: [Evren Eryurek, urigilad, Valliappa Lakshmanan, Anita Kibunguchy-Grant, jessiashdown]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/data-governance-the/9781492063483/
  - text: Amazon
    link: https://www.amazon.com/_/dp/1492063495

archive:
- name: Phil Winder
  text: "Hi there. Given that I haven\u2019t read the book yet - I will - and I totally\
    \ understand that this is out of scope, but I\u2019m really interested in how\
    \ governance can be applied to layers further up the stack. I think there\u2019\
    s a lot of lessons that could be applied to other areas of the stack, which is\
    \ common in certain industries like finance, but non existent everywhere else.\n\
    Q: Given what you\u2019ve learnt writing and experiencing this, where can these\
    \ ideas best be applied next? Which part of the ML stack could benefit most?"
  replies:
  - name: Uri Gilad
    text: 'I am not quite certain I am clear on what "layers up the stack" mean, but the
      topic of ML models is interesting. An ML model is both an executable (meaning
      it needs access to machine resources - CPU/RAM) and operates on data. The combination
      of Data Governance and Resource Governance becomes complex and interesting,
      but generally speaking, we tried to stick to broad concepts in this book. Great
      topic for a follow-up though!'
  - name: Phil Winder
    text: 'Sorry Uri Gilad  I should have clarified but yes I think you get my drift.
      You''ve done data governance.

      What about governance for:

      - Features

      - Training

      - ETL

      - Models

      - Serving/inference

      - Monitoring

      - Etc.

      This is what I mean by stack. MLOps terminology. Sorry.

      So the question remains, from your experience writing this book, what do you
      think about governance all-the-things?'
- name: Matthew Emerick
  text: Thanks for doing this! Is there really a major difference between top-down
    and bottom-up data governance? Which tends to be more effective?
  replies:
  - name: Uri Gilad
    text: "I am taking \"Top down governance\" to mean pushing down policies from\
      \ above. While there are benefits to centralized management care should be taken\
      \ not to overwhelm individual analysts with rules, because they will find ways\
      \ to \"do their job faster\". I would prefer a \"carrot\" (no stick) approach\
      \ in which you get access to MORE data under centrally managed policies \n-\
      \ AI Governance includes several topics discussed in the book such as lineage\
      \ of where the data came from and how it is used in a model. There is a highly\
      \ related topic concerning bias in AI which we did not approach in the book\
      \ which focuses on how to make sure data used in AI does not introduce certain\
      \ biases (many examples )\n- Where do we see data governance going in the next\
      \ five, ten years? - I believe it will become tablestakes for an organization\
      \ to care not only about access to data but also about how it is used, and for\
      \ what purpose. The book really talks about basic processes you can set, but\
      \ its up to \"corporate culture\" to adopt the approaches\n- \"How effective\
      \ is data governance? Does it really protect us individuals against maleficent\
      \ usage of our data by corporations and governments?\"\n - data governance is\
      \ not a \"solve all\" - it is a set of principles (and processes) you can put\
      \ in place to make sure the data an analysts accesses is appropriate for their\
      \ permissions and their task at hand. At the end of the day, you are trusting\
      \ people and there are very few ways to prevent individuals from willful misuse\
      \ (for example, you can always put a video camera in front of your monitor and\
      \ scroll tables in front of it)"
- name: David Cox
  text: "Very excited to see this book come through! For individuals working in locations\
    \ where they\u2019re building this all from scratch, the totality of everything\
    \ that needs to get done can be daunting. How do you recommend assessing and prioritizing\
    \ tasks to build out mature data governance systems?"
  replies:
  - name: Uri Gilad
    text: 'My recommendation would be to prioritize. Start with the big rocks, and focus
      on where "most data is" and proceed from there. While you do that, keep scaling
      up in mind so that you will be able to encompass more and more areas. There
      are multiple tools at hand (discussed in the book ) Some of those are already
      included with your Bigdata infrstructure'
  - name: Jessi Ashdown
    text: I would also add to begin with a few things and then fan out from there.
  - name: Jessi Ashdown
    text: 'One thing we''ve seen work pretty well is to begin with selecting the most
      important data that you have to govern: remember it''s not only the "scary stuff"
      (like PII) but could also be data that is used to make business decisions'
  - name: Jessi Ashdown
    text: once you have identified a few of these "top categories" you can begin focusing
      on classifying/tagging/labeling and treating this data first
  - name: Jessi Ashdown
    text: This is especially useful when you don't have a lot of headcount to be mining
      through data, enriching it, curating it, etc.
  - name: David Cox
    text: These are all very helpful comments! Thanks Uri Gilad and Jessi Ashdown!
- name: Kyle Shannon
  text: "\u2753 In your experience what are some of the ways you were able to convince\
    \ executive level to understand the business value of governance and feel the\
    \ need to invest?"
  replies:
  - name: Uri Gilad
    text: 'The low hanging fruits data governance solves are

      "having analysts spend less time on finding data, and more time on extracting
      value from data" and in addition, "being able to tell who has access to what"

      If those two are not already a problem n your org, you are in a very good place
      already!'
  - name: Kyle Shannon
    text: "Thanks, as a follow up to the second low hanging \U0001F34E . If there\
      \ isn't concern or understanding about the value of who has access to what,\
      \ how would you get engagement in that conversation?"
  - name: Uri Gilad
    text: 'many organizations are liable to regulation such as GDPR which mandates
      (not explicitly) understanding of this sort.

      Smaller organizations which are not liable, or alternatively have a "everyone
      has access to anything" should still set the ground rules in a way which eventually,
      once they scale up - complying with such regulation becomes easier'
  - name: Kyle Shannon
    text: "Thanks Uri, I'm \U0001F4AF with you, I'm curious if you have any tips or\
      \ pointers on how to show the business value to setup now for the future or\
      \ does it typically come down to when they need the regulations it gets called\
      \ into action"
- name: Neal Lathia
  text: "\u2754 What are the first things that companies should think about when starting\
    \ out with data governance?"
  replies:
  - name: Jessi Ashdown
    text: 'One of the first places to start is to identify what data you should start
      to govern first and what kind of headcount you have that can work on this effort.
      You cannot govern what you don''t know, so you must begin with identifying (at
      least) two classes of data: sensitive stuff and then the "valuable stuff" (data
      that help the business make better decisions). Once you''ve identified these
      classes you can begin to categorize and enrich the data that falls into these
      classes. If you have the headcount to do more than this - great - but when you''re
      starting out you likely don''t. You likely have a few people who are having
      to do this work ON TOP of their other daily tasks.'
  - name: Jessi Ashdown
    text: The second thing is to identify who is doing what. This is often a piece
      that gets overlooked and when it does it becomes a free-for-all with tasks not
      being done well, or worse, not at all. Even if you only have a few people who
      are taking on governance tasks make it clear who is responsible for what part
      of the process.
  - name: Neal Lathia
    text: Thank you!
  - name: Jessi Ashdown
    text: you are so welcome!!
- name: Bayram Kapti
  text: "Hi Uri Gilad &amp; Jessi Ashdown! Thanks fortaking the time to answer our\
    \ questions.\nDo data lineage, data cataloguing (data dictionary), data security\
    \ &amp; user access management go under Data Governance? If you\u2019re just starting\
    \ to take these steps in an organization, what\u2019s the recommended order to\
    \ start things up? And do you cover these in your book?"
  replies:
  - name: Uri Gilad
    text: 'Hi Bayram!

      yes, we do cover these topics in the book. Generally speaking lineage/catalog/security/access
      managements are aspects of Data Governance.

      I would recommend actually starting from the Data view - what data does your
      org manage, what are the requirements for said data (e.g. protect PII) and later
      finding the tools to help with that.'
- name: Xavier Gumara Rigol
  text: "Hi! Looking forward to reading the book in the next few weeks! \U0001F4D6\
    \nI am curious to see your view on Data Governance initiatives implemented in\
    \ small companies versus big organisations. Do you think it is more of a challenge\
    \ in big corporations and _easier_ small companies?"
  replies:
  - name: Jessi Ashdown
    text: "Great question! I hate to say it but it depends \U0001F642 I'll unpack\
      \ that a little though - there are different factors that make it easier/more\
      \ difficult and company size is only one of the them."
  - name: Jessi Ashdown
    text: The kind of data and amount of it that's sensitive effects the difficulty
      of governance regardless of if an organization is large vs. small. A small company
      may PRIMARILY deal with sensitive data which can make governance a lot more
      challenging vs a large company that only has a small percentage of sensitive
      data.
  - name: Jessi Ashdown
    text: Also, on the one had smaller companies often have less employees so there
      is less complication with granting access controls, however, smaller headcount
      can also mean that less governance tasks overall are completed. Chapter 3 of
      the book goes into greater detail on these specific factors!
  - name: Xavier Gumara Rigol
    text: "Thanks! Good point on smaller headcount can also mean less governance tasks\
      \ are completed \U0001F92F"
- name: Xavier Gumara Rigol
  text: 'When implementing a data governance initiative, we know it is usually hard
    to convince management to fund it properly.

    In my experience, it is also hard to "convince" Data Engineers/Analysts/Scientists
    to invest in data governance initiatives (good documentation, working agreements
    between teams,...). How would you suggest to tackle investment in data governance
    initiatives in Individual Contributors that are not motivated so spend time on
    this topics?'
  replies:
  - name: Jessi Ashdown
    text: Excellent point and insight (chapter 9 of the book goes into this as well!)
      One of the things we mention in the book is creating a data culture. There are
      many aspects of a successful culture of protection but you're exactly right
      - motivation is key. One way we've seen this work well is in being really intentional
      about how you divide governance tasks. Often Data Engineers/Scientists/Analysts
      are not motivated because too many tasks fall onto them. When you define a process
      and identify who is responsible for what it makes the governance strategy less
      ambiguous. Another thing we've also seen work is to have ongoing "training"
      that is *relevant* to folks. So, perhaps there is a Governance Week that includes
      daily 1hr trainings that apply to these roles - such as how gov tools you currently
      have can help them do their job better, or a training around something that
      is very relevant to governance that's been in the news. These sorts of things
      tap into the psychology of folks connecting these tasks to themselves - and
      when they can see the benefit and aren't overwhelmed they're far more likely
      to follow through.
- name: Xavier Gumara Rigol
  text: What are the most important things to formalise first when starting a Data
    Governance initiative?
  replies:
  - name: Jessi Ashdown
    text: 'First and foremost it''s really important to identify where your company
      is in its governance journey to begin with: do you know what all your data is?
      Do you know *where* all of it is? Do you know who has access to what? This is
      the first thing to assess. Most organizations will answer "no" or "sort of"
      to the above and in that case they must first begin with what data they need
      to govern *now*. In general this will be the "scary stuff" (PII, etc.), and
      the "business critical stuff" (the key data that helps the company to make data
      driven biz decisions). This is where to start as trying to govern everything
      all at once is incredibly overwhelming! The next step is to then think about
      the process: you''ve identified what needs to be governed, now you need to identify
      *how* you''re going to do that. Will you use tools? Tagging? Labeling? Just
      moving data into different storage areas? You need to define the process and
      then the *tasks* that involved in this process (note: if you have minimal budget
      and/or headcount try to identify the bare minimum here). Then (and this is super
      important) you need to define *who* is going to do those tasks. And to your
      point above, it can help to divide these tasks up. But the key here is to make
      it VERY clear who is responsible for what tasks - and have a way to check on
      this; make sure they get done.'
  - name: Xavier Gumara Rigol
    text: Thanks a lot for your answers! Looking forward to reading the book!
  - name: Jessi Ashdown
    text: "You're so welcome! \U0001F642"
- name: Alexey Grigorev
  text: Maybe it's a silly question, but what is actually data governance? why should
    we care about it?
  replies:
  - name: Jessi Ashdown
    text: Actually a great question! The way we've defined gov in the book is really
      looking at the policies and procedures that maximize the utilization of data
      while also ensuring data quality, security, and regulatory compliance. So -
      it's more than just security or how to conduct access control - which is often
      how governance is defined. So in this way we should care about it because it's
      the process by which you can make your data *useful -* in terms of being able
      to derive insights from it while also protecting it.
  - name: Alexey Grigorev
    text: Do you have an example of such policy from the top of your mind?
  - name: Alexey Grigorev
    text: Something like "All data must go to this database and must be documented
      in this spreadsheet"?
  - name: Jessi Ashdown
    text: 'Yes, that''s def an example of one such policy. Another could be: all data
      from 3rd party vendors go into XX storage. Or credit card numbers are only retained
      for 30 days... or even, sales, income, and roi all are labeled "revenue"'
  - name: Alexey Grigorev
    text: That's clear now! Thank you!
- name: Alexey Grigorev
  text: 'If I work as a data scientist, what are the main advantages of implementing
    it for me?

    What about analysts and data engineers? Why should they care about it?'
  replies:
  - name: Jessi Ashdown
    text: 'We have a chapter that goes into depth both about the people/process as
      well as the culture, but in short, governance needs to be a well thought out
      program with strategic process. That doesn''t mean that it has to be super complicated
      and require an inordinate amount of headcount, but it DOES need to be intentional.
      And part of being intentional is to define *who* does *what.* Not only does
      this help to ensure tasks are done, but it also gives shared responsibility
      and ownership. When someone has ownership of a task they are far more likely
      to see how they personally benefit from it. And it should probably go without
      saying, but as stated above: a gov program is not just about securing data -
      it''s also about making it useful - and any user of data (analyst, scientist,
      engineer..) wants to have data that is useful!'
- name: Alexey Grigorev
  text: And another one - who should actually be driving it? Analysts, data engineers,
    or data product managers?
  replies:
  - name: Jessi Ashdown
    text: "oof! Loaded question \U0001F609 we go into more depth in the book but I\
      \ will say that it shouldn't be one group - it should be bottom up, top down,\
      \ and part of a company culture."
  - name: Alexey Grigorev
    text: "I have an even more loaded follow up - how to make it a part of company\
      \ culture? \U0001F642"
  - name: Jessi Ashdown
    text: More loaded indeed! Well, one of the things we've seen work well is an actual
      intention to *make* it part of company culture. So things like setting up an
      intentional strategy, defining tasks, designating roles...all that is really
      important. But the special sauce is really embedding it from the top down and
      engaging from the bottom up. So what I mean by top down is for there to be intention
      and focus around doing _ongoing_ training. Now - most will define a gov strategy,
      do a training, and call it a day. But there needs to be continuous training.
      And this doesn't have to be super intense or time consuming - could even be
      a 1hr training around "new gov tools" or a guest speaker, or even "YIKES! this
      happened in the news - how do we make sure it doesn't happen to us". The point,
      really, is that it's even thought of at all and given at least a little bit
      of focus. And from bottom up I mean that this is where employees need to be
      engaged; do a training on a topic related to gov they care about or that actually
      helps them do their jobs better. Don't just send out the annual click thru and
      check  the box. When you engage the employees they help to facilitate the culture
      and it becomes symbiotic .
- name: Alexey Grigorev
  text: Maybe the last one. Let's say we implemented it in our organization. How can
    we measure the effectiveness of it?
  replies:
  - name: Jessi Ashdown
    text: 'Chapter 8 goes into monitoring, specifically, but I think of the key points
      is that you cannot measure what you haven''t pre-defined. So, a successful gov
      program needs to be intentional, with specific processes and tasks, and people
      who will do them (note: this doesn''t mean complicated) - when you have mapped
      out your strategy you can then track it over time. So, you defined these tasks
      - are they getting done? Let''s say part of your strategy was to only keep PII
      data in one particular storage location - is it? In short, the way that you
      define your strategy will help to inform what you''ll need to measure in order
      to know how it''s going.'
- name: Ricky McMaster
  text: "Not sure if you\u2019re still taking questions, but if so: do you think data\
    \ governance has generally deteriorated in recent years? Or perhaps is taken less\
    \ seriously?"
  replies: 
  - name: Jessi Ashdown
    text: I certainly don't get that sense. For the past 3yrs I have talked to many,
      many different organizations about their data management and data governance strategies/programs/needs
      and it seems that it's only becoming MORE top of mind as not only there are increasingly
      stricter regulations to comply with but also the amount of data companies now
      collect is higher. And the reason to collect that data is to derive insights from
      it which organizations know cannot be done (or at least done well) without some
      sort of governance process in place.

---

As you move data to the cloud, you need to consider a comprehensive approach to data governance,
along with well-defined and agreed-upon policies to ensure your organization meets compliance
requirements. Data governance incorporates the ways people, processes, and technology work together
to ensure data is trustworthy and can be used effectively. This practical guide shows you how to
effectively implement and scale data governance throughout your organization.