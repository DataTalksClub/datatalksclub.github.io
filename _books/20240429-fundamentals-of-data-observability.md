---
authors:
- andypetrella
cover: images/books/20240429-fundamentals-of-data-observability/cover.jpg
description: Book of the Week. Fundamentals of Data Observability by Andy Petrella
end: 2024-05-03 23:59:59
image: images/books/20240429-fundamentals-of-data-observability/preview.jpg
links:
- link: https://www.oreilly.com/library/view/fundamentals-of-data/9781098133283/
  text: Book's page
- link: https://www.amazon.com/Fundamentals-Data-Observability-End-End/dp/1098133293/ref=sr_1_1?dib=eyJ2IjoiMSJ9.s8TnsjYOLmjtj08oEt-oGIOVCvhkCzJs0qxcXnONGxF0vbIMrUi4CT5RrX37Ejzhj_fFqjMUTOKW2sCbc1sQlYyzI8-WlK58J3igEUyZRzgVz6bDrDwIBcGyL9phOAaMFvLXlSjywTD_2hpXnNvE3g.---K5vJ2BW7Ehs6U-9eDtaQYNW1LATBZuf1bGGbIZUM&dib_tag=se&hvadid=695062583497&hvdev=c&hvlocphy=9033313&hvnetw=g&hvqmt=e&hvrand=937541805025489773&hvtargid=kwd-1845109640600&hydadcr=3440_13743889&keywords=fundamentals+of+data+observability&qid=1712920726&sr=8-1
  text: Buy on Amazon
start: 2024-04-29 00:00:00
title: Fundamentals of Data Observability

archive:
- name: Romuald Tcheutchoua
  text: Thanks for the book!
  replies: []
- name: Romuald Tcheutchoua
  text: Does the book cover ALL the KEY observability needs for the ENTIRE machine
    learning lifecycle? if yes, please can you share a glimpse of how the book can
    help at the specific stages of ML lifecycle?
  replies:
  - name: Andy Petrella
    text: "Hello Romuald Tcheutchoua, good one.\nSo data observability has a big role\
      \ to play in analytics observability (see chapter 1 and 2). They are working\
      \ hand in hand to produce the needed \u201Cfeatures\u201D to represent the system\
      \ in place (a ML product or so).\nA ML lifecycle is likely including a data\
      \ lifecyle, this is where you want DO to back you up.\nNote that the concept\
      \ introduced in the book are mainly translating concepts from application and\
      \ infrastructure observability\u2026 which therefore can easily translated in\
      \ analytics/ml one\n(I did the exercise but must be continued further\u2026\
      \ perhaps a future book \u2014 but happy if someone writes it for me ahaha)"
- name: Romuald Tcheutchoua
  text: Also, there are  couple of ML observability platforms (such as Arize, etc.)
    available out there. what are the innovative aspects of the book that makes it
    better compared to other available observability resources?
  replies:
  - name: Andy Petrella
    text: "A question I would love to answer your own POV on.\nAn observability platform\
      \ is complete when you have added all observability components taking care of\
      \ their relative facet of the system. This is also explained in chapter 1 and\
      \ 2.\nThere is not yet 1 observability platform (OSS or not) that does everything\u2026\
      \ it\u2019ll happen one day probably though \U0001F642"
- name: Nirupama Valluru
  text: "Have you advocated for the need for SLAs in the book? If yes, how effective\
    \ would they be in agile systems. \nIf no, what is the alternative and how can\
    \ data reliability be ensured across teams?"
  replies:
  - name: Andy Petrella
    text: "Hello Nirupama Valluru, nice one!\nAdvocating is a strong statement but\
      \ I am covering it yuup.\nIt is coming after having cover many aspects leading\
      \ naturally to this concept, but also SLOs and SLIs.\nThe best I can recommend\
      \ is to read up to that point rather than me trying to summarize it too shortly\
      \ here TBH.\nIt is already in chapter 2, just before talking about garbage in/out.\
      \ So there is not much to wait before getting to it.\nHowever, I am not covering\
      \ the \u201Cagile\u201D part, IMHO SLA and agile practices are not BFFs \U0001F605\
      . Agile is meant to allow quick deliveries and fail fast and safe, which are\
      \ concepts covered also in the book  (page 151, chapter 6).\nDon\u2019t get\
      \ me wrong, I don\u2019t mean SLA doesn\u2019t fit an agile team, I mean that\
      \ relying \u201Conly\u201D on SLA is not possible in an agile system (defining\
      \ an SLA is a long process postponing delivery).\nI am advocating more SLO and\
      \ SLI in fact, which are closer to data observability than SLA is to data quality."
  - name: Nirupama Valluru
    text: "Okay \nThank you for the detailed response"
- name: Edwin Chuy (edchuy)
  text: How does data observability fit within a data governance framework?
  replies:
  - name: Andy Petrella
    text: "Hello Edwin Chuy (edchuy), neat question \U0001F642.\nSome other members\
      \ asked me corollary questions, and I can complement my previous answers with\
      \ an additional info that might be close to your specific question.\nAcutally,\
      \ data observability is working hand in hand with data governance - while one\
      \ describes policies and laws to be known and embraced, the other helps automating\
      \ associated controls and ensuring they are implemented.\nIn a way, DG is the\
      \ governement, DO are the sensors (eg cameras, \u2026) to monitor, judge and\
      \ cops are engineers, stewards, etc \U0001F642\nHere is attached a screenshot\
      \ showing where DO fits in the DAMA Wheel"
  - name: Edwin Chuy (edchuy)
    text: Andy Petrella Thanks for the answer. I somehow knew that the answer would
      fit within the DAMA framework.
- name: Manoj
  text: How different is data observability for different systems (like analytics,
    databases, ml models, llms etc) are there any common things/framework we can apply
    to all?
  replies:
  - name: Andy Petrella
    text: "Hello Manoj thanks for the question, I would recommend you to check my\
      \ answer to Romuald Tcheutchoua\u2019s questions as it is very similar.\nHowever,\
      \ that gives me another to emphasize again that there are several observability\
      \ areas: data and analytics (ML) are two of them, others are application and\
      \ infrastructure.\nAll areas have some common concepts, roles, and concepts,\
      \ but each is also coming with its own set of capabilities which are distinguishing\
      \ one another.\nA system is, in fact, observable if it has all areas of observability\
      \ enabled (see chapter 1 and 2).\nYou don\u2019t need either one (ml obs) or\
      \ another (data obs), but all of them due to the heterogeneity of data systems\
      \ (which cannot be avoided as this is intrinsic and vital)"
  - name: Manoj
    text: Thanks Andy Petrella
- name: Arjun
  text: 'Hii all Good day, Can Anyone help me to how to get an copy of the book  Fundamentals
    of Data Observability!

    Thanks'
  replies:
  - name: Andy Petrella
    text: "Hey Arjun you can get a free e-copy on the Kensu website: [https://www.kensu.io/oreilly-all-chapters](https://www.kensu.io/oreilly-all-chapters)\n\
      Otherwise, it is available ofc on O\u2019Reilly platform and Amazon"
- name: Andy Petrella
  text: "Hey @everyone! I\u2019m happy to start the week with interacting with this\
    \ great community about my book - big up to Alexey Grigorev for having me.\nFYI,\
    \ you can download freely FODO on this page [https://www.kensu.io/oreilly-all-chapters](https://www.kensu.io/oreilly-all-chapters).\n\
    If this can make you save some bucks \U0001F605 .\nLooking forward to your questions\
    \ and chatting with you.\nHave a great week ahead!"
  replies: []
- name: H.Sajid
  text: Hello everyone! Andy Petrella does the book address how to seamlessly integrate
    data observability into existing data workflows and processes?
  replies:
  - name: Andy Petrella
    text: 'Hello H.Sajid ! Yes definitely there is a chapter that integrates all concepts
      and methods, the chapter 7: integrating data observability in your data stack
      (50 pages).

      Chapter 8 provides other additional keys for other systems'
  - name: H.Sajid
    text: Thank you for your response and the book.
- name: Luis Oliveira
  text: "Hello everyone. \nThank you for this book Andy Petrella \U0001F642 \nMy question\
    \ is regarding data observability in the big world of data governance. \nHow far\
    \ can a team implement data observability processes if the company as no data\
    \ governance structure implemented?\nCan a data team start with data observability\
    \ processes on its own?"
  replies:
  - name: Andy Petrella
    text: "Hello Luis Oliveira good ones!\nData observability can be initiated without\
      \ data governance in place, at all.\nOf course, I am not recommending to not\
      \ have DG \U0001F604 (see my other report on the topic: [What Is Data Governance?\
      \ Understanding the Business Impact](https://www.oreilly.com/library/view/what-is-data/9781492090328/)).\n\
      Data observability is a practice dedicated to give the processes (applications,\
      \ pipelines, ml, \u2026) manipulating data to ability to expose information\
      \ about their behaviour (usage, purpose, patterns, \u2026).\nUsing this information\
      \ (data observations) doesn\u2019t necessarily rely on data governance because\
      \ they are used primarily by all data users to have visibility about what\u2019\
      s happening with data at any time.\nHowever, having DG in place, allows DO to\
      \ be leveraged in more standard ways and to use the data observations to \u201C\
      control\u201D data governance policies are followed, and, conversely, allow\
      \ DG policies to evolve (given data observations are facts from the fields and\
      \ DG can adapt over time to that).\nYou can make a parallel with other observability:\
      \ using prometheus for example doesn\u2019t require to have IT Governance in\
      \ place (think about startups). It doesn\u2019t prevent it to be useful for\
      \ the whole team/company (by transivity), but its value benefits with governance\
      \ practices \u2014 ultimately, support teams, SREs, \u2026\nAlternatively, we\
      \ can think like this:\nHow much do we need to be convinced or do we need to\
      \ be forced to produce logs about data schema, data metrics, and even some data\
      \ lineages?\nThen, how often do we think about it?\nThen, how much governance\
      \ policies will make us do it?\nThen, how much enforced policies will enable\
      \ them?"
- name: Tim Makhambetov
  text: 'Thanks for the book Andy Petrella! Couple of questions:

    1. What are the approaches to get a buy in from the management and stakeholders
    on implementing robust data observability in the organization?'
  replies:
  - name: Andy Petrella
    text: "Hey Tim Makhambetov cool, thanks for the qs!\nGetting a buy in for data\
      \ observability is similar to get a buy in for other type of observability (eg\
      \ prometheus, datadog, and other folks of the kind).\nIt used to be hard, because\
      \ the \u201Cvalue\u201D is hard to demonstrate (esp. for non tech savvy ppl)\
      \ - and also, the value is hard to track or measure (or there is no baseline\
      \ yet):\n- the number of errors anticipated, \n- the amount of processes trusted\
      \ by automation vs team work, \n- the satisfaction of users (and engineers\u2026\
      )\n- the management of unknown-unknowns\nAnd the list goes on.\nA mistake often\
      \ made is to use \u201Cthe quality\u201D as one of the goal to be reached with\
      \ observability.\nIn fact, observability (data in this case) is to avoid \u201C\
      quality\u201D issues to propagate and to become huge problems due to the amount\
      \ of time and efforts needed to understand each issue.\nAvoiding all quality\
      \ issues can be made with tests and pre-requesites and contract (prepping my\
      \ next answer \U0001F605) and stuff alike, those can take a lot of time and\
      \ perhaps infinite (if you want to avoid \u201Call\u201D issues). So best is\
      \ to find a limit (or just abandon it to go to prod aha) and then\u2026 what?\n\
      Then data observability. To support all other cases.\nBut also the cases that\
      \ were predefined above, because data observability will provide information\
      \ about their occurences.\nSo how to get buy-in from stakeholders?\nBy experience,\
      \ it is sold as an insurance, a backup, because the team cannot humanly support\
      \ efficiently (I mean people and time, hence \U0001F4B8) all data product/pipeline/\u2026\
      \ at maximum satisfaction. Because negociating quality in data is a matter of\
      \ push back and throwing the ball between producers and users.\nTeams know that\
      \ problems * will * happen, but users are not accepting them because they have\
      \ not been told problems * will * happen. So it is inacceptable when any little\
      \ thing happens.\nTeams don\u2019t tell anything about this fact to users, they\
      \ are scared to do it because they can\u2019t say \u201Cyes, there will be problems,\
      \ but we\u2019re ready, so don\u2019t worry\u201D.\nData observability is allowing\
      \ teams to tell their users they can trust them because they are prepared to\
      \ help them out in case of problems, and over time, avoid them.\nPS: remember\
      \ how hard it was to sell/convince about application/infrastructure observability\
      \ back in 2010s :face_with_spiral_eyes:"
- name: Tim Makhambetov
  text: 2. What is your view or recommendation on data contracts for the purpose of
    data observability?
  replies:
  - name: Andy Petrella
    text: "Data contracts are a great way to align on many things especially before\
      \ going production. Esp. if they can be enforced.\nLike any contract they can\
      \ go as deep as any human can think, and take as much time to do so, and thus\
      \ delay the value generated by the transaction being contractualized.\nA contract\
      \ has its limit, because compromise have limits, and also they are not covering\
      \ every single possible event that can happen (in fact they can, but how long\
      \ will it take to \u201Cdiscuss\u201D them -&gt; especially, the associated\
      \ responsibility and possible \u201Cfines\u201D?).\nData contracts are governing\
      \ the transactions.\nData observability is tracking the executions of transactions.\n\
      Sometimes (often!) things are not going the way it was expected, but we have\
      \ to deal with that, we need to be prepared, we need to find new compromise\
      \ to allow the relationship to keep going and the transactions to hold (with\
      \ trust).\nThat is make data contract evolving.\nHence, in data contracts, you\
      \ fix rules, with data observability you:\n- validate them\n- update them (yes\
      \ rules are not necessarily written in stone\u2026)\n- help creating new ones\n\
      So in a data contract, you specify that the processes in place must at least\
      \ produce some foundational information (as described in ch2 ^^). Contracts\
      \ can also specify which metrics are mandatory, but I don\u2019t recommend them\
      \ because it\u2019s not worth it.\nLike most contracts, there is a request for\
      \ both parties (esp. the service provider in such case) to have an insurance,\
      \ its terms are relatively vague (and often absurd at first - like a 1B dollar\
      \ coverage \U0001F605). That\u2019s data observability.\nNote: SLAs are not\
      \ observability per se, even though they are related."
- name: Luis Oliveira
  text: "I have one more question to add \U0001F603  \nWhich are in your opinion the\
    \ best data observability tools and why? \nI use a lot of dbt so I use elementary\
    \ but IMO the package is full of bugs and has lots to grow. \nI also work with\
    \ databricks for data from raw to silver layer. \nDon\u2019t know which tool we\
    \ should implement but I am thinking on doing a POC for Great Expectations."
  replies:
  - name: Andy Petrella
    text: "Ahem, hehe, tricky one as I am also the founder of Kensu\u2026\nI won\u2019\
      t give a direct answer to this, as I don\u2019t want this to become a product\
      \ plug but provide everyone with some insights about \u201Ctooling\u201D for\
      \ data observability.\nFirst of all, there are two parts in data observability:\n\
      1. the data tools must be data observable\n2. the data observations must be\
      \ leveraged in a data observability platform\nFor 1., elementary is a good example\
      \ of what is called in the book an \u201Cagent\u201D, that is a component attached\
      \ to a tool that will turn it \u201Cdata observable\u201D. In this case, dbt-core\
      \ is already partially data observable as it produces manifest and run-results,\
      \ however they are not easily consumable. Plus, the tests are nice but the tracking\
      \ is tedious as devs must configure them all. Elementary solves the first part\
      \ by exposing the data observations (in the json files) in a table, and partially\
      \ the second, as it generates tests.\nHowever, elementary is not producing metrics\
      \ on data, but test-results which only addresses a minor part of what is needed\
      \ to be covered to leverage appropriately data observability.\nOn spark, same\
      \ thing, an agent (a jar + py module) can be attached to the applications to\
      \ generate the necessary information to add the data observability capability\
      \ to all jobs. There are component offering lineage exposure and some schema\
      \ as well, but there is only one I saw turning spark jobs into fully data observable\
      \ ones (guess who is publishing it \U0001F605).\n\nFor 2., a platform is needed\
      \ to aggregate and consolidate information coming from various agents (elementary,\
      \ spark agent, azure data factory, python script, stored proc, \u2026) to create\
      \ a holistic view of the processes and also offer capabilities leveraging the\
      \ \u201Chistory\u201D of the behavior (a database storing timeseries and a graph\
      \ at least!).\nThis is something that must be separated from the tools (eg,\
      \ dbt, spark, databricks, snowflake) and the agent (eg, elementary, spline,\
      \ \u2026) to allow interop and the holistic view mentioned above.\nSuch a platform\
      \ has the primary goals to detect anomalies and categorize which are issues\
      \ or not, provide notification systems, troubleshooting helpers/companions.\
      \ These must rely as much as possible on the information available in the platform\
      \ without necessarily constantly relying on people providing inputs (eg, quality\
      \ rules), hence statistical analysis (or AI if you want) is a table stake.\n\
      Another important feature is the circuit breaker that allows the platform to\
      \ act as a control tower for data processes -&gt; breaking pipelines involving\
      \ non reliable data, avoid GIGO etc.\nI HTH"
  - name: Luis Oliveira
    text: "Oh sorry. I didn\u2019t notice you were the founder of Kensu \U0001F601\
      \nI think I understood what you said\nIn a very simple way:\n- Both dbt and\
      \ databricks produce information that can be used to observe the data\n- The\
      \ DO tool should have a platform to organize and present all the results.\n\
      So *Elementary* is a good agent because it uses dbt core information to organizes\
      \ and present the results.\nRegarding *Great Expectation* I don't know exactly\
      \ how it works the organization and presenting the results.\nAs far as I noticed\
      \ *Kensu* is free for connecting to Databricks but if we want to present the\
      \ data from a report point view then it is paid. Am I correct?\nThere is also\
      \ the first one... *Monte Carlo* . I have no idea how it works and the pricing.\n\
      Thank you for the great information \U0001F642"
  - name: Andy Petrella
    text: "Yes, your summary is really close to what I had in mind \U0001F604.\nI\
      \ won\u2019t discuss any of the solutions (non free/oss) here, but happy to\
      \ take side chats privately as I don\u2019t want to puzzle folks here \U0001F61B"
- name: Kane Williams
  text: Andy Petrella is there any type of data you find particularly tricky to use
    some of the practices in your book well with? e.g. timeseries, ...
  replies:
  - name: Andy Petrella
    text: "Kane Williams not necessarily, because the nature of the data is not the\
      \ main driver. Of course, when logging metrics, the engineer may want to produce\
      \ specific metrics such as cardinality of a categorical variable or things like\
      \ this.\nThe practice in the book emphasises that to have control of a data\
      \ system and automate its operations, the information about the data must come\
      \ from elsewhere than the datastores themselves.\nHowever, the chapter 8 is\
      \ dedicated to systems that are less easy to integrate data observability into\
      \ - not necessarily legacy, but opaque (like a cloud/SaaS service for example).\n\
      So, graph, timeseries, non-structured, deep, flat, and so on data types are\
      \ totally OK with the practice introduced in the book \U0001F604"
- name: Nirupama Valluru
  text: "Thank you for the book Andy Petrella \nAre there any common signs or any\
    \ right time that would indicate it\u2019s the right time for a company to invest\
    \ in data observability?"
  replies:
  - name: Andy Petrella
    text: "Hello Nirupama Valluru, thanks for this! It is a good corollary question\
      \ to Luis Oliveira \u2019s.\nAnd, unusually \U0001F605, the answer is quite\
      \ short and straigthforward.\nYes, there are common signs, it is when your data\
      \ pipeline goes to production and created outcomes that will be used by others\
      \ (people or systems)"
  - name: Andy Petrella
    text: 'This is the time triggering doubts, stress, and anxiety for the people
      who take this action or responsibility. This is when you want to have a maximum
      of visbility.

      Especially at the beginning. Over time, the team could reduce the visibility
      as confidence has grown, etc.'
  - name: Andy Petrella
    text: "It\u2019s like when you go to prod the first time, you have logs level\
      \ DEBUG or INFO, then move to WARNING, ERROR later on"
  - name: Nirupama Valluru
    text: Thank you for answering!
  - name: Andy Petrella
    text: My pleasure Nirupama Valluru
- name: Mitch Edmunds
  text: Andy Petrella I'm interested to know, do authors get to select the bird/animal
    on the front of their O'Reilly books and if so, what is the bird you selected
    and why?
  replies:
  - name: Andy Petrella
    text: "Mitch Edmunds aha, well, you, as an author, have no power in this process.\n\
      There is a strict, secret (no kiddin), process followed internally to decide\
      \ this (it takes a lot of time).\nMy ornate hawk-eagle bird was selected because\
      \ it has a freakin\u2019 good eyesight (8x human\u2019s) :D"
  - name: Mitch Edmunds
    text: Oh right, ha! I guess they are a very important part of the brand and the
      illustrations are always beautiful. You seemed to have landed a particularly
      cool one, I'd never heard of this bird. And obviously very apt.
  - name: Andy Petrella
    text: "Ahahah, yeah. I loved it right away when they unveiled it to me \U0001F604"
- name: Andy Petrella
  text: "Thanks @everyone for your questions and big up to the ones running for the\
    \ book. I\u2019ll turn the ebook price into a hard book one, because you can get\
    \ a free copy on [https://www.kensu.io/oreilly-all-chapters](https://www.kensu.io/oreilly-all-chapters)\
    \ for a few months still.\nI am available for further questions obviously! Please\
    \ connect me on LinkedIn and let\u2019s rock it all \U0001F604\n[https://www.linkedin.com/in/andypetrella/](https://www.linkedin.com/in/andypetrella/)"
  replies:
  - name: Konrad
    text: Thank you kindly for the book

---

Quickly detect, troubleshoot, and prevent a wide range of data issues through data observability, a set of best practices that enables data teams to gain greater visibility of data and its usage. If you're a data engineer, data architect, or machine learning engineer who depends on the quality of your data, this book shows you how to focus on the practical aspects of introducing data observability in your everyday work.

Author Andy Petrella helps you build the right habits to identify and solve data issues, such as data drifts and poor quality, so you can stop their propagation in data applications, pipelines, and analytics. You'll learn ways to introduce data observability, including setting up a framework for generating and collecting all the information you need.

- Learn the core principles and benefits of data observability
- Use data observability to detect, troubleshoot, and prevent data issues
- Follow the book's recipes to implement observability in your data projects
Use data observability to create a trustworthy communication framework with data consumers
- Learn how to educate your peers about the benefits of data observability