---
authors:
- joereis
- matthewhousley
cover: images/books/20220815-fundamentals-of-data-engineering/cover.jpg
description: Book of the Week. Fundamentals of Data Engineering by Joe Reis and Matthew
  Housley
end: 2022-08-19 23:59:59
image: images/books/20220815-fundamentals-of-data-engineering/preview.jpg
links:
- link: https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
  text: Book's page
- link: https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302
  text: Buy on Amazon
start: 2022-08-15 00:00:00
title: Fundamentals of Data Engineering

archive:
- name: Jasmin Classen
  text: "Hi Joseph Reis and @matthew housley, thanks so much for answering questions\
    \ here. I'd be curious about the following things:\n1. How would you describe\
    \ the target audience of this book? (e.g. Software Engineers as well as Data Scientists,\
    \ beginner experience with Data Engineering vs. more advanced) \n2. I'm very interested\
    \ in the \u201Ecut through the marketing hype\u201C part of the book. How would\
    \ you sum up this section exactly, how do you yourselves decide which technologies\
    \ would be worth trying in an enterprise context? \n3. Does this book touch upon\
    \ Data Engineering in context of providing data for Data Science projects? \n\
    Thank you again and have a nice day!"
  replies:
  - name: Joseph Reis
    text: "Hey Jasmin,\n1. Another way to answer this question are learning outcomes\
      \ - the reader will come away with a good understanding of the foundations of\
      \ data engineering, which they can apply in their respective disciplines (SWE,\
      \ DS/DA, data engineering, etc)\n2. To determine the best technologies worth\
      \ trying in an enterprise context, please read Chapter 4 \U0001F642\n3. Yep,\
      \ it provides a holistic context for providing data for DS projects. This is\
      \ covered throughout the book, via the Data Engineering Lifecycle"
  - name: Matthew Housley
    text: "Jasmin Classen One thing I\u2019d add to Joe\u2019s response to 2 above:\
      \ study classes of technologies rather than single technologies. For example,\
      \ instead of just looking at Apache Kafka, try to understand streaming event\
      \ platforms as a class (Kafka, Pulsar, Kinesis, Pub/Sub.)"
- name: Daniel
  text: "Hi Joseph Reis and Matthew Housley,\nthanks for doing this. I'd be interested\
    \ in ...\n- How do you stay up-to-date with the breadth and depth of techniques\
    \ that are available/upcoming in data science?\n- From your experience: What are\
    \ frequent mistakes when developing robust data systems? \n- Any cloud provider\
    \ you prefer/ would recommend (if you had to choose a single one)?\nMany thanks\
    \ in advance! \nCheers\nDaniel"
  replies:
  - name: Joseph Reis
    text: Your first question - Staying up to date is tricky, as there's so much going
      on. I personally read a ton of newsletters, articles, and whitepapers on a weekly
      basis. For example, on most weekends, I've got 50+ articles/papers queued on
      my ipad to read. In general, I try to focus 80% of my time on areas in my peripheral
      area of expertise, with another 20% on outliers or stuff that might impact the
      field I work in.
  - name: Matthew Housley
    text: "My follow on to what Joe said about staying up to date is related to my\
      \ response to Jasmin Classen\u2019s question about technologies. Try to connect\
      \ that dots between different technology developments. Try to understand common\
      \ engineering threads between current technology announcements and other technologies\
      \ that you are familiar with."
  - name: Matthew Housley
    text: "Regarding frequent mistakes when developing robust data systems:\nWe frequently\
      \ see companies \u201Crolling their own\u201D stacks, when they could rely more\
      \ on off the shelf solutions. (Note that off the shelf includes open source.)\
      \ This leads to excessive complexity, maintenance overhead, massive tech debt\
      \ and slow ongoing delivery."
  - name: Matthew Housley
    text: "Small startups will often point to Google or Facebook as examples of why\
      \ you should build your own technology from the ground up, but this ignores\
      \ the fact that many off the shelf technologies didn\u2019t exist when these\
      \ companies were trying to solve problems."
  - name: Joseph Reis
    text: "re: cloud providers - they're all great \U0001F609"
  - name: Matthew Housley
    text: Build a custom solution when you discover a problem that is not solved by
      something already in the ecosystem.
  - name: Joseph Reis
    text: "&gt; Small startups will often point to Google or Facebook as examples\
      \ of why you should build your own technology from the ground up, but this ignores\
      \ the fact that many off the shelf technologies didn\u2019t exist when these\
      \ companies were trying to solve problems."
  - name: Joseph Reis
    text: We sometimes call this "cargo-cult data engineering"
  - name: Cesar Garcia
    text: Is that the reason for the proliferation of endless orchestrators in the
      ecosystem?
  - name: Matthew Housley
    text: "Haha, that\u2019s part of it."
  - name: Matthew Housley
    text: "We\u2019ve seen several startups create their own orchestrators. (I\u2019\
      m even aware of an orchestrator written in Clojure\u2026)"
  - name: Matthew Housley
    text: "Although I think that orchestration is so central to data engineering that\
      \ there are legitimately many different visions. Unfortunately, there\u2019\
      s only so much mindshare available, so the small players end up on the sidelines."
- name: Roman Zabolotin
  text: 'Hey Joseph Reis and @Matt Housley,

    Thank you for sharing your ideas with us in your book.

    Can you give a piece of advice to ones, who stand in data engineering path.

    What practice project would be best to advance in this path? Can you give us some
    sketch examples?'
  replies:
  - name: Joseph Reis
    text: 'There''s no single right answer to this question, but the approach I''ve
      seen fail over and over is doing projects that you think will land you a job.
      It might, but what did you learn from the project?

      The best practice project is the one you''ll be interested in working on after
      the "homework" is over. Meaning, pick something that truly interests you.'
  - name: Matthew Housley
    text: "Also, decide what kind of job you\u2019re looking for. Are you trying to\
      \ work for a Silicon Valley giant? A rapidly growing startup? A large enterprise?"
  - name: Matthew Housley
    text: For the latter two, focus on cloud skills, both data specific ones and general
      cloud infrastructure skills. Consider working on cloud certifications to stand
      out.
- name: Ricky McMaster
  text: 'Hi Joseph Reis and Matthew Housley thanks so much for doing this!

    In your recent appearance on the Data Engineering Podcast you spoke of the need
    for a new conversation on data modelling.  A reevaluation of dimensional modelling
    was recently offered (in brief) by Holistics'' [Analytics Setup Guidebook](https://www.holistics.io/books/setup-analytics/);
    given how much has changed technologically since the ubiquity of cloud data warehouses
    (which even the more recent additions to the canon such as Agile Data Warehouse
    Design do not consider), could you imagine a new (or modified) set of modelling
    principles usefully stretching to book-length?

    Also, can you cite any interesting discussions of the topic?  For example, Maxime
    Beauchemin''s contention that slowly changing dimensions could be considered obsolete
    given the cheap columnar storage provided by cloud DWH''s, which allows options
    like daily partitioned dimensions that were previously considered anti-patterns?'
  replies:
  - name: Joseph Reis
    text: 'These are all good ideas. Modeling needs to incorporate much more than
      batch-paradigms. I''m personally excited on data modeling for streaming and
      event data, among other innovations.

      Data Vault is pretty dope too.'
  - name: Joseph Reis
    text: Graph is another area I'm excited about, and I think there's quite a bit
      to borrow from graph models with respect to traditional relational data modeling.
  - name: Matthew Housley
    text: "I think there are a lot of ideas out there on the present and future of\
      \ data modeling. However, so far I haven\u2019t seen someone commit to a new\
      \ global vision of data modeling principles that can be adapted to current database\
      \ and data lake technologies. That could potentially be a great book (or multiple\
      \ books), but would require a huge amount of work."
  - name: Ricky McMaster
    text: "Thanks for the responses guys.  So far I haven't needed to do much with\
      \ streaming data but modelling for that sounds interesting, along with graph\
      \ - will check that out.  I guess the neo4j O'Reilly book would be a good place\
      \ to start?\nAdmittedly I've only really used the Kimball approach so I don't\
      \ really know what Data Vault could offer in addition.\nOk so a new book would\
      \ be difficult but definitely useful then - here's hoping that happens \U0001F91E"
  - name: Ricky McMaster
    text: 'Sorry Joseph Reis and Matthew Housley, a follow-up on this one: I''ve been
      using the Kimball approach exclusively as it seemed best suited to what was
      necessary (and I liked the iterative approach in comparison to Inmon).  However,
      it seems Inmon is personally quite persuaded by Lakehouse...

      In any case, you mention Data Vault above: would you say any of the three main
      dimensional modelling approaches lend themselves best to the cloud DWH landscape?'
  - name: Joseph Reis
    text: 'There might be some confusion with how these various modeling techniques
      are described. Inmon originated the concept of the data warehouse (and later
      extending this to the data lakehouse). The data warehouse as defined by Inmon
      uses data marts to present data for various business use cases. These data marts
      might be modeled using Kimball''s dimensional modeling techniques.

      Inmon defines a data warehouse as "a subject-orientated, integrated, time variant,
      non-volatile collection of data in support of management''s decision-making
      process.

      Kimball took the notion of dimensional modeling, and applied it to a data mart
      only. He called this a data warehouse, which caused decades of confusion and
      infighting about the meaning of a data warehouse (I define it as Bill Inmon
      originally did).

      Data Vault is considered the son of the data warehouse (according to Inmon).
      It''s a way of organizing your data from various sources in a very coherent
      way. You can add Kimball star schema on top of the Data Vault.

      There''s not a one-size fits all answer to the cloud DWH, sadly, since can also
      go for wide, quasi-denormalized tables too, incorporating nested data structures.

      As I mentioned before...confusing, isn''t it?'
  - name: Ricky McMaster
    text: "Hmmmm yeah maybe my perception of Inmon is not in fact the reality \U0001F609\
      \ ... I need to research him and Data Vault for sure."
  - name: Joseph Reis
    text: "welcome to a giant can of worms \U0001F642"
  - name: Ricky McMaster
    text: "Hahahahaha thanks \U0001F642"
  - name: Ricky McMaster
    text: '&gt; Data Vault is considered the son of the data warehouse (according
      to Inmon). It''s a way of organizing your data from various sources in a very
      coherent way. You can add Kimball star schema on top of the Data Vault.

      Very good to know, thanks a lot.  This is exactly the sort of thing I wanted
      to find out.'
  - name: Joseph Reis
    text: sadly, this stuff is often buried underneath hundreds of pages of text in
      various books
  - name: Ricky McMaster
    text: Your hours (weeks?) of pain on our behalf is much appreciated
  - name: Joseph Reis
    text: months and years and decades :)
  - name: Ricky McMaster
    text: Yes I can imagine... based on that, I guess even some stuff that's very
      dated in technical terms, e.g. The DWH ETL Toolkit, might still have useful
      ideas/techniques?
  - name: Joseph Reis
    text: The underlying techniques are still very valid
  - name: Ricky McMaster
    text: Very good to know
  - name: Matthew Housley
    text: "One problem with traditional data modeling techniques is that the emphasize\
      \ normalization, but absolute adherence to normalization doesn\u2019t really\
      \ make sense for today\u2019s data and databases."
  - name: Matthew Housley
    text: "For example, third normal form (3NF) prohibits arrays and other forms of\
      \ nesting. With the rise of NoSQL, trying to remove all JSON nesting in analytics\
      \ data really doesn\u2019t make sense. In addition, modern columnar database\
      \ offer extraordinary performance on nested data and arrays; data engineers\
      \ are foolish not to take advantage of these capabilities."
  - name: Matthew Housley
    text: "On the opposite end of the spectrum, I\u2019ve frequently seen people advocate\
      \ for denormalizing everything. Does this mean that you should try to put all\
      \ of your data into one huge table? It\u2019s a non-sensical prescription."
  - name: Matthew Housley
    text: My suggestion is that data engineers learn traditional approaches to modeling,
      then make adjustments based on the data their handling, the use case, and the
      technology involved.
  - name: Matthew Housley
    text: Normalization should be viewed not as a strict set of rules, but as a knob
      we can turn to suit the problem at hand.
  - name: Matthew Housley
    text: "For example, data that is naturally nested should potentially remain that\
      \ way in tables for analytics, ML, etc. On the other hand, data that\u2019s\
      \ reused in many places should potentially live in its own table and get joined\
      \ into other tables as required."
- name: Cesar Garcia
  text: "Hey Joseph Reis and Matt Housing! Thanks for creating this book on Data Engineering.\
    \ These are my questions for you: \n- What are the areas less developed in the\
    \ Data Engineering ecosystem? \n- Do you envision that Data Engineering practices\
    \ could pervade other areas besides big corps, like Open Government Data? \n-\
    \ What would be the biggest knowledge gaps for someone with sysadmin background\
    \ to work as Data Engineer? \nThanks for your time!\nC\xE9sar"
  replies:
  - name: Joseph Reis
    text: Less developed areas in the DE ecosystem - collaboration with upstream/downstream
      stakeholders is a big mess right now, the immaturity  of skills and competencies
      of data engineering teams is something that holds back the full potential of
      data engineering best practices. That's hopefully where a book like FoDE can
      help bridge the skills gap.
  - name: Matthew Housley
    text: I would love to see data engineering principles applied to open government
      data, but this is not something easily achieved given that government IT tends
      to be way behind corporate IT, and even further behind startups and tech companies.
      In the US, a huge initiative at the federal level would be required to make
      this happen.
  - name: Cesar Garcia
    text: "Thanks for your responses! I am getting ready some publications regarding\
      \ data engineering principles applications to improve open government data quality.\
      \ \nI totally agree about the inertia in public administration so I am proposing\
      \ a complementary approach: could citizens/civic initiatives collaboratively\
      \ construct a quality checking infrastructure as some sort of check and balances\
      \ system?\nTo offer a concrete example, I am envisioning some kind of shared\
      \ Meltano infrastructure, that automatically extracts data from Open Government\
      \ Data Portals and then triggers a quality check using Great Expectations. These\
      \ Great Expectations rules could be versioned and shared across different cities,\
      \ states, countries, etc. These checks could also trigger some metrics on response\
      \ times, data drift, etc. \nIf you'd like to know more about this topic, please\
      \ let me know so I can send you the links when published"
  - name: Joseph Reis
    text: seems reasonable
  - name: Ning Wang
    text: "It would be great if there is a unified governance system. Maybe finally\
      \ smart contract has a suitable use case that can benefit everyone in the world.\
      \ \U0001F642"
- name: Nakul Bajaj
  text: 'Hi Joseph Reis and [Matthew](https://datatalks.club/people/matthewhousley.html),

    Thanks for creating the book.

    I wanted to ask when building data ingestion pipelines and or data ingestion patterns,
    what design principles can be utilised when creating pipelines and design patterns?

    I also wanted to ask, if there are frameworks to help choose between open source
    pipeline orchestrators on the basis of their deployment, maintenance vs managed
    services.  Will the book cover those?

    Finally. What is the role of the data quality framework in data engineering? Also
    any tips on best practices for ELT and ETL? And which one is better for modern
    data warehouses such as snowflake or  Big query?'
  replies:
  - name: Joseph Reis
    text: '&gt; I wanted to ask when building data ingestion pipelines and or data
      ingestion patterns, what design principles can be utilised when creating pipelines
      and design patterns?'
  - name: Joseph Reis
    text: Think in terms of push/pull and sync/async. Ensure reliability of payloads
      in terms of schedule and structure.
  - name: Joseph Reis
    text: '&gt; I also wanted to ask, if there are frameworks to help choose between
      open source pipeline orchestrators on the basis of their deployment, maintenance
      vs managed services. Will the book cover those?'
  - name: Joseph Reis
    text: yes, we cover this extensively in Chapter 4 - choosing the right technologies.
  - name: Joseph Reis
    text: '&gt; Finally. What is the role of the data quality framework in data engineering?
      Also any tips on best practices for ELT and ETL? And which one is better for
      modern data warehouses such as snowflake or Big query?'
  - name: Joseph Reis
    text: 'Data quality is part of data management, one of the undercurrents of the
      Data Engineering Lifecycle. Definitely incorporate data quality into your workflows.

      As for ELT vs ETL for Snowflake or BQ, both can handle either one. We don''t
      pick a side with ELT vs ETL, and suggest using the best approach for the job.'
  - name: Matthew Housley
    text: "Regarding data ingestion: use off-the-shelf ingestion tools when they exist.\
      \ Writing custom ingestion code is often a waste of time if someone else has\
      \ already done this work. You\u2019ll find that you still spend a lot of time\
      \ on ingestion pipelines where there are no existing solutions."
  - name: Matthew Housley
    text: "In the long term, I would like to see data providers move toward a \u201C\
      data sharing\u201D paradigm where they land data in object storage or a cloud\
      \ columnar database. This would free up a lot of time for data engineers to\
      \ focus on higher value tasks. Google is a leader in this area, and we\u2019\
      ve recently seen companies like Stripe move in this direction."
  - name: Joseph Reis
    text: And Snowflake
  - name: Matthew Housley
    text: 'Regarding open source pipeline orchestrators: this area is changing extremely
      fast. I would suggest watching the current market leaders (Airflow, Dagster,
      Prefect) and talking to other practitioners. There will likely be interesting
      new entrants in 2022 and 2023, though I would be careful about being an early
      adopter.'
  - name: Joseph Reis
    text: "Cron \U0001F609"
  - name: Joseph Reis
    text: jk
  - name: Matthew Housley
    text: "\U0001F631"
  - name: Ricky McMaster
    text: Yeah this was something I was thinking about asking - what you both reckon
      about the data platforms like Snowflake and Databricks.  Now I know.
  - name: Nakul Bajaj
    text: 'Thanks so much for the reply Joseph Reis and Matthew Housley..

      Love airflow, used it as a managed service mostly.

      Started testing out Prefect..

      Any serverless orchestrators or serverless frameworks suggested? And your thoughts
      on these compared to deployments..'
- name: Matthew Housley
  text: Thank you!
  replies:
  - name: Joseph Reis
    text: Howdy Matt!
- name: Matthew Housley
  text: I just joined the channel.
  replies: []
- name: Rosona
  text: "Hey Joseph Reis  and Matthew Housley . From the \"look in the book\" preview,\
    \ this looks like a bird's eye view, readable like a book book instead of a \"\
    bam, here's a GitHub repo, get your hands dirty\" book. I'm here to ask if that\
    \ changes mid book or if I've understood the vibe and writing style correctly.\
    \ \nAlso, thanks for coming here to answer questions."
  replies:
  - name: Joseph Reis
    text: 'Part 1 sets the tone. Part 2 gets decently technical, but in an approachable
      way.

      There are no github repos or code exercises.'
  - name: Matthew Housley
    text: "We essentially wrote a book to compliment other technical resources. Data\
      \ engineering is so vast that we felt like we had to take bird\u2019s eye view.\
      \ But we would suggest reading this book in conjunction with general engineering\
      \ books (e.g. Designing Data Intensive Applications) and specific technology\
      \ books based on the stack you\u2019re working with. (E.g. Learning Spark or\
      \ Stream Processing with Apache Flink)."
  - name: Rosona
    text: Excellent! Thanks for the very thorough answers.
- name: Gur Hevroni
  text: 'Hi Joseph Reis and Matthew Housley, thanks for writing the book and for taking
    questions here!

    I have a couple of questions:

    1. Do you cover in the book what would a data engineer role entails in different
    organizational settings? (corporate, startup,  etc.). For example, I''m curious
    to know what would be the first order of business for the first data engineer
    hire in a 50-100 employees startup, compared to that joining one of the big-tech
    companies.

    2. What are the set of skills required to become a successful data engineer? Would
    it be more similar to the skill set of a software engineer? a data scientist?
    a combination of both/others?

    I''m looking forward to learn more about your book!'
  replies:
  - name: Joseph Reis
    text: '1. Yes, we discuss this quite thoroughly throughout the book. As the end
      of each chapter, there''s a "who you''ll work with" section. We also cover early
      vs mature companies, and how they should work with DE

      2. There''s not a single answer to the question. A successful DE is the one
      who can keep the business and stakeholders happy :)'
- name: Laura
  text: "Hi Joseph Reis and Matthew Housley, nice to meet you here. I really enjoyed\
    \ listening to your Super Data Science podcast episode.  \U0001F44B\nI have a\
    \ questions as well:\nWhat's your advice for a Data Scientist trying to get more\
    \ professional experience with cloud technologies? Doing some hobby projects and\
    \ watching YouTube tutorials is a nice start, but I feel that I am still missing\
    \ a lot of knowledge on how to actually run things in production. Do you have\
    \ any advice?"
  replies:
  - name: Joseph Reis
    text: "Nothing like digging into cloud products, tinkering, and breaking things\
      \ \U0001F642"
  - name: Joseph Reis
    text: On another note, to get a comprehensive view of a cloud (AWS, GCP, Azure),
      you might want to consider getting one of their dedicated certs. While some
      people might bash cloud certs, we think they're useful for providing a baseline
      context and skills for that particular cloud. There's what you think you know
      about a cloud, and then there's the way the cloud wants you to use it. These
      aren't always clear, and a cert can help clarify these things.
  - name: Matthew Housley
    text: "I second that, and I\u2019ll add that most of the clouds have data engineering\
      \ and machine learning specific certs. For example: Google Cloud Platform Certified\
      \ Professional Data Engineer or the Google Machine Learning Engineer certifications."
- name: Joseph Reis
  text: We're answering questions now. Feel free to drop new questions. We'll answer
    until 5pm MT
  replies: []
- name: Cesar Garcia
  text: "This is side question but\u2026 why are there almost no scholar references\
    \ about data engineering? In the first chapter you talk about the story of data\
    \ engineering (coming from DBs to Big Data to current situation) and the term\
    \ is quite new. But, are academics still using BigData terms? Are there people\
    \ outside O\u2019Reilly / Packt writing about this topic? Is everything moving\
    \ so fast that people don't have time to publish about it?"
  replies:
  - name: Joseph Reis
    text: "Academics tend to be quite behind industry (we also teach at a university,\
      \ so we know of which we speak). Data engineering is still a relatively new\
      \ field, so it will take some time for the term and practices to solidify.\n\
      That said, read ch. 11 if you really want to be confused \U0001F642"
  - name: Cesar Garcia
    text: I will do it for sure! Thanks for the tip!
  - name: Matthew Housley
    text: The mandate of academia is much more focused on theoretical problems. So,
      for example, computer science researchers are interested in general questions
      about distributed systems, where tech company engineers want to build working
      distributed systems to solve concrete problems.
  - name: Matthew Housley
    text: A typical feedback loop between academia and silicon valley goes like this.
      Engineers build a distributed system and discover some kind of behavior. They
      write a paper about it. Academic researchers take the problem and develop a
      theoretical framework to explain it. Engineers then use this to improve their
      distributed systems.
  - name: Matthew Housley
    text: "There is definitely value in this feedback loop, but it\u2019s a slow process."
  - name: Matthew Housley
    text: This is not to say that _every_ academic research is strictly focused on
      theoretical problems, but this is the tendency. Professors who want to do concrete
      experimentation have to work very hard to stay up to date.
  - name: Matthew Housley
    text: From my perspective, Martin Kleppmann has done a good job of staying up
      to date, partially based on his experience in the trenches.
  - name: Matthew Housley
    text: "Regarding incentives to publish: many technology employers don\u2019t offer\
      \ incentives for employees to publish. Worse still, employees may not be allowed\
      \ to publish due to NDAs."
  - name: Matthew Housley
    text: "Google has done a good job of contributing back to the community through\
      \ publications, but I\u2019m sure they keep many things under wraps, and it\u2019\
      s possible that they\u2019re less open now as a huge, mature company."
- name: Joseph Reis
  text: 'Re: q&amp;a. We will try to answer all questions by 5pm MT every day of this
    book club. Ask away!'
  replies: []
- name: Ricky McMaster
  text: 'Second question: I totally agree with your point about the importance of
    data engineers understanding business requirements from the stakeholders'' perspective.
    However, do you have any advice for junior engineers who do not have previous
    experience in more stakeholder-oriented roles such as data analysis, and whose
    main academic and career focus hitherto has been overwhelmingly technical? Would
    you consider it useful for such roles to be embedded in business unit teams?'
  replies:
  - name: Joseph Reis
    text: Definitely. Embedding is a great way to build useful non-DE skills that
      actually make you a better DE. Learning the downstream user's requirements builds
      empathy.
  - name: Matthew Housley
    text: "It\u2019s a tricky problem to solve. To some extent, you\u2019re at the\
      \ mercy of the company that employs you, especially as a junior engineer. You\u2019\
      re stuck with their organizational dysfunction. Having said that, conversations\
      \ go a long ways. Learn to have conversations with stakeholders you work with.\
      \ Also, try to meet people in many roles across the company and talk to them\
      \ about how they use data."
  - name: Ricky McMaster
    text: 'Cool, good to know thanks.  For me personally I come from a BI background
      so I''m definitely sold on the need for these conversations; it''s good to have
      it confirmed though that it''s important to prioritise the topic for data engineers,
      whether formally (e.g. embedding) or not.

      I''ve often experienced quite a division between business and tech, but ultimately
      everyone loses if it persists.'
- name: Grzegorz Sajko
  text: When it comes to breadth vs width  when acquiring tech skills - when do you
    recommend to go deeper? What are your thoughts on specialization? As the tech
    landscape is changing very fast, is it better to be jack-of-all-trades?
  replies:
  - name: Matthew Housley
    text: "I think you need to develop both general purpose and specific tech skills.\
      \ If I\u2019m looking to hire someone, I look for general purpose coding skills\
      \ and what I\u2019ll call \u201Cdata intuition.\u201D"
  - name: Matthew Housley
    text: "I frequently find that software engineers who have mostly worked on services\
      \ that handle single calls and events struggle when asked to handle bulk data.\
      \ There\u2019s a learning curve in transitioning from thinking of data as individual\
      \ elements to viewing data as a large set."
  - name: Matthew Housley
    text: "This often leads to monstrosities at startups such as \u201CETL pipelines\u201D\
      \ that are a bunch of single event microservices stitched together."
  - name: Matthew Housley
    text: "I\u2019ve seen many, many people make the transition from event level thinking\
      \ to bulk data thinking, but there\u2019s a learning, and ideally a potential\
      \ hire has already made that transition."
  - name: Matthew Housley
    text: "If someone has general data skills, it\u2019s relatively easy to retrain\
      \ them on new data tools. If someone is good at Spark, they can probably learn\
      \ other data frameworks with relative ease. If they know a realtime framework\
      \ such as Flink, they can probably make the transition Beam."
  - name: Matthew Housley
    text: "So, my concrete advice is that you should experiment with data frameworks\
      \ that you\u2019re interested in. It\u2019s critical that you move beyond frameworks\
      \ that are traditionally single machine oriented (Pandas, R) to bulk data processing\
      \ tools such as Spark and Beam. Also, get very good at SQL using database engines\
      \ such as BigQuery, Snowflake or Redshift to solve analytics and data transformation\
      \ problems. (SparkSQL is also great.) Even if you work primarily in Spark, SQL\
      \ is an extremely useful tool, and it shows a potential employer that you have\
      \ developed data intuition."
  - name: Matthew Housley
    text: "Also, as I mention in another reply, learn cloud infrastructure and orchestration\
      \ skills. You can\u2019t learn everything, but knowing one cloud and one orchestration\
      \ tool is a good start for developing proficiency with other such tools."
  - name: Grzegorz Sajko
    text: thanks! This is mine blind spot (single machine oriented / not cloud), because
      most personal projects don't need scale.
- name: Alexey Grigorev
  text: Why so many data scientists are suddenly interested in data engineering? Is
    data science no longer the sexiest job?
  replies:
  - name: Erald David
    text: 'Curious to hear your perspective on this, Alexey Alexey Grigorev

      Could this be because:

      1. Many data scientists realized that a lot of company who hired them don''t
      have the sufficient data, so decide to learn data engineering also (sort of
      become fullstack), or

      2. A lot of data scientist wanna be realized they fall in love with the engineering
      side of data science, so they flock to a more "engineering"-y position like
      data engineer or even analytics engineer (like [this great post](https://benn.substack.com/p/why-do-people-want-to-be-analytics)
      from Benn Stancil)?'
  - name: Roman Zabolotin
    text: "As for me, I think than I like work with data and I like programming too.\n\
      I think that working as a data scientist is more like research, math, science\
      \ and so on.\nBut if your interest is programming, that data engineering will\
      \ suit you more \U0001F60A"
  - name: serdar
    text: I am not even a data scientist but trying to make a change but in my last
      couple DS interviews I heard about interviewers complaning about the mediocre
      skills of the DS people. I guess those who really understand the needy greedy
      stuff find a new direction with DE. Just a thought..
  - name: GerryK
    text: Maybe DS needs sector expertise related to data. DE has more software /
      tools/ infrastructure.
  - name: Matthew Housley
    text: "See the thread above on becoming \u201Crecovering data scientists.\u201D\
      \ [https://datatalks-club.slack.com/archives/C01H403LKG8/p1660777107448379?thread_ts=1660703899.890469&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1660777107448379?thread_ts=1660703899.890469&amp;cid=C01H403LKG8)"
  - name: Matthew Housley
    text: "But I\u2019ll add that increasingly, data teams are expected to put models\
      \ into production."
  - name: Matthew Housley
    text: At the height of the data science craze a few years back, data scientists
      would create a simple model on their laptop, hand some magical insight to a
      business stakeholder, and move on to the next project.
  - name: Matthew Housley
    text: "At least, that was the dream. In practice, businesses discovered that the\
      \ value of their data initiatives was limited if they couldn\u2019t get models\
      \ into production."
  - name: Matthew Housley
    text: "Let\u2019s led to a much greater emphasis on data engineering and ML engineering.\
      \ As such, there seem to be more data engineering openings than data science\
      \ openings, and data engineer demand far outstrips supply. (We\u2019ll see if\
      \ this trend holds with ongoing economics shifts.)"
  - name: Matthew Housley
    text: This blog post provides a great visualization of the foundations required
      for successful data science.
  - name: Matthew Housley
    text: '[https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007)'
  - name: Matthew Housley
    text: At any rate, I would argue that the prestige of data science and ML have
      actually increased in the last several years, but this has led to companies
      emphasizing better support structures for these initiatives, hence the demand
      for data engineers.
  - name: Ning Wang
    text: My lab mates in college are mostly Data sciences, but I was an SWE before
      and a data engineer now (I am more interested in coding than building/tweaking
      data models). Personally I think with basic/standard tools, it could be very
      challenging to analyze most raw data. DEs build systems (standard or dedicated)
      to further process data so that DSs can get A LOT more values from the data
      and be A LOT more productive.
- name: Avinash M
  text: Joseph Reis would you suggest this book to a newbie in data engineering field
    like me?
  replies:
  - name: Joseph Reis
    text: yep!
  - name: Avinash M
    text: Thank you!
- name: Aayush
  text: "Thanks for this great book!\n- How, according to you, should one approach\
    \ Data Engineering at Reasonable scale, ie, at places that have data but not necessarily\
    \ at terabyte scale? Do you think there is a need of implementing any modern data\
    \ architecture at such organizations? \n- At what point does one realize that\
    \ they have reached a place where they now need specialised Data Engineers to\
    \ look after their data needs? \n- Currently, there is a heavy reliance on tool\
    \ based learning for Data Engineers - learn SQL, learn spark, kafka and you are\
    \ good to go. Do you think the heavy focus on tools rather than the Fundamentals\
    \ of DE is a concern?"
  replies:
  - name: Kevin Kho
    text: That third question is a very good question. Though SQL is universal so
      it's not the same level as Spark and Kafka. Wanna hear their thoughts.
  - name: Matthew Housley
    text: 'Regarding the first bullet point:'
  - name: Matthew Housley
    text: A really great thing about modern data engineering is that many of our tools
      now scale smoothly from gigabytes to petabytes.
  - name: Matthew Housley
    text: "Off the shelf tools such as Spark, BigQuery, Snowflake, etc. can quickly\
      \ process a few megabytes or run a 1 PB query. It\u2019s just a question of\
      \ allocating resources at the correct scale for the problem at hand."
  - name: Matthew Housley
    text: The relative simplicity of using these tools means that I generally advise
      organizations with small data problems to spin up one of these options rather
      than using self hosted Postgres (for example). The reason is that using a cloud
      based tool decreases operational overhead, and delivers better uptime and consistency,
      key considerations at any data scale.
  - name: Matthew Housley
    text: 'Regarding the second bullet point: because scaling data is now relatively
      easy, the main considerations for dedicated data engineering talent have shifted
      somewhat.'
  - name: Matthew Housley
    text: 'I would ask these questions to assess the need for dedicated data engineers:'
  - name: Matthew Housley
    text: '1. What are the quality expectations for the data? How difficult will it
      be to maintain quality? Are you ingesting data that is relatively dirty and
      complex, requiring complex pipelines for cleaning?

      2. What is the expected service level agreement for the data?

      3. How many different data sources are you handling? (Note that this is a separate
      question from the _size_ of the data.)

      4. How quickly will new data sources be onboarded in the future?

      5. How sensitive is the data? Are you handling data with proprietary company
      secrets or sensitive personal information?'
  - name: Matthew Housley
    text: Any such requirements can be a motivation for hiring dedicated data engineers
      even if the data is only gigabytes in size. One major problem with the modern
      data stack and the cloud is that it made data too easy, so that people with
      no security and engineering qualifications ended up causing data breeches or
      providing incorrect business data to business stakeholders.
  - name: Matthew Housley
    text: Regarding the last bullet point, see my response to Grzegorz Sajko above.
- name: Srik
  text: Joseph Reis and Matthew Housley - Do the contents of the book vary by each
    region they are released? Example - [Amazon.com](http://Amazon.com) indicates
    FoDE is 440 pages, [amazon.in](http://amazon.in) list it as 452 pages.
  replies:
  - name: Srik
    text: btw kindle edition has 740 pages
  - name: Matthew Housley
    text: "Not to my knowledge \u2014 I believe the editions are just formatted a\
      \ bit differently. The Kindle version paginates into smaller pages, and the\
      \ Indian version may have extra back or front matter pages. (I actually have\
      \ a copy of this edition. I\u2019ll have to check.)"
  - name: Srik
    text: Thank you
- name: Arianna Cooper
  text: "Hi Joseph Reis  and Matthew Housley! \U0001F604 Given the years of experience\
    \ and knowledge you both have in the industry, what have you both seen to be the\
    \ best practices when it comes to senior level data engineers growing their early\
    \ career level folks on their teams? What are the green or red flags that companies\
    \ have demonstrated that show you that they really value (or don\u2019t value)\
    \ growing their junior and mid level data engineers? (I ask since I just graduated!)"
  replies:
  - name: Joseph Reis
    text: 'Green flags - Showing you best practices and coaching you while you''re
      growing. Assigning you work and telling you what needs to be done, letting you
      figure out how. Stepping in to coach you when you''re astray or beyond stuck.

      Red flags - No support or direction.'
  - name: Arianna Cooper
    text: Gotcha. Thank you so much for your input, really appreciate it!!
- name: Ning Wang
  text: "Hi, Joseph Reis and Matthew Housley Thanks for writing the book! As a data\
    \ engineer myself, I think the job is relatively new comparing to many other computer\
    \ jobs, and many people may not have the right idea about what it is and what\
    \ it can/should do. A bird-eye view could be very helpful for data engineers and\
    \ other related people.\nMy question is: from some of your previous answers, it\
    \ seems to me that you are supports of \u201Cdata sharing\u201D. So what are the\
    \ main values of \u201Cdata sharing\u201D in your mind? In the high volume and\
    \ high efficiency scenarios, what are the main points in your mind to justify\
    \ \u201Cdata sharing\u201D vs efficiency? In the architecture in my company, we\
    \ cares a lot about performance and efficiency, it makes data sharing to be trickier\
    \ in my mind, so I am wondering what you think.\nFinally, good luck to your book!"
  replies:
  - name: Ning Wang
    text: "And btw, the \u201CCut through marketing hype\u201D part reminds me why\
      \ I left my previous company. LOL."
  - name: Matthew Housley
    text: Data sharing is generally used to share data in a database system that separates
      compute and storage. For example, BigQuery and Snowflake support flavors of
      data sharing, and Amazon S3 can be used for data sharing in a data lake environment.
  - name: Matthew Housley
    text: "The basic idea is that you grant another user, team or organization access\
      \ to specific data, such as a dataset in BigQuery, a \u201Cshare\u201D in Snowflake\
      \ or a specific set of objects in S3."
  - name: Matthew Housley
    text: "The users on the other end then spin up their own compute to consume the\
      \ data as they wish. This saves you the trouble of having to grant access to\
      \ account and clusters \u2014 they get read only access to the stored data itself."
  - name: Matthew Housley
    text: Data sharing is a great way to publish datasets publicly. For example, a
      good deal of government data is available through shared BigQuery public dataset.
  - name: Matthew Housley
    text: In addition, data sharing facilitates cross organizational collaboration.
      For example, you may be working with a partner ad tech company that needs access
      to certain data to create models. Data engineers build pipelines to appropriately
      scrub the data and load it into the shared datasets.
  - name: Matthew Housley
    text: "Finally, data sharing is interesting from the perspective of Zhamak Dehghani\u2019\
      s data mesh concept. Individual teams build pipelines to prepare data for external\
      \ consumption, then share the data product across the company without granting\
      \ any access to pipelines."
  - name: Ning Wang
    text: Thanks for the details! Totally makes sense.
- name: Alexey Grigorev
  text: For data scientists who want to go into data engineering, what should they
    do apart from reading your book?
  replies:
  - name: Doink
    text: "enroll in <#C01FABYF2RG|course-data-engineering> \U0001F609 ?"
  - name: Joseph Reis
    text: "What Doink said \U0001F609"
  - name: Joseph Reis
    text: Also, build your network of people who can get you in front of great job
      and project opportunities.
- name: Joseph Reis
  text: Thanks everyone!
  replies: []
- name: Ricky McMaster
  text: 'Another one: something I have experienced more often than not is years-old,
    accumulating technical debt as a result of poorly designed and maintained operational/application
    databases. Sometimes, this is compounded by a switch to a cloud data warehouse,
    but with even less data integrity given how flexible they are in this respect.

    I definitely acknowledge tools such as dbt filling the gap in data quality maintenance,
    but meanwhile do you detect a genuine rediscovery of solid relational database
    modelling principles, which are in large part decades old?'
  replies:
  - name: Joseph Reis
    text: Data modeling is making a comeback for sure. Learn it, love it.
  - name: Matthew Housley
    text: "Unfortunately, technical debt is just a part of the job. Even for forward\
      \ looking organizations that embrace new technologies, it takes time to retire\
      \ old systems, and you don\u2019t necessarily have the authority to accelerate\
      \ this process. Interfacing with old systems is often a data engineering responsibility."
  - name: Ricky McMaster
    text: '&gt; Unfortunately, technical debt is just a part of the job.

      Tell me about it... I actually don''t come from a technical academic background,
      and I would love to know if data modelling was given more of a priority in computer
      science degrees generally these days.'
  - name: Joseph Reis
    text: I've never seen CS degrees teach data modeling, at least as it pertains
      to analytics. A database class might teach relational algebra and the normal
      forms of relational data modeling.
  - name: Ricky McMaster
    text: '&gt; A database class might teach relational algebra and the normal forms
      of relational data modeling.

      Yup - I feel like the correct procedures for even 3NF modelling are often overlooked
      though (at least from my perspective in Germany).

      I don''t doubt that it''s part of my job to deal with the legacy issues, but
      I''d love to see modelling making a comeback for sure.'
  - name: Joseph Reis
    text: It's hard. The amount of laziness to put in the hard work is high
  - name: Ricky McMaster
    text: Haha well there is that
- name: Alexey Grigorev
  text: How important is it for data engineers to know how to build a dashboard? Usually
    it's more a job for an analyst
  replies:
  - name: Joseph Reis
    text: While building a dashboard isn't a direct requirement for a DE, if a DE
      knows how to build a dashboard, I think it helps the DE understand how to structure
      the data for delivery to the analyst. Zero downside for a DE to know dashboard
      basics
  - name: Matthew Housley
    text: I second that. And learn to communicate with the people building dashboards
      so you can be better at your job.
- name: GerryK
  text: "Hi Joseph Reis and Matthew Housley,\n1. Are you touching on data validation\
    \ during the ETL/ELT? \n2. Do you use coding examples?\n3. Are you touching on\
    \ unit test /integration / functional tests for data pipelines?"
  replies:
  - name: Joseph Reis
    text: '1. Yes, this is covered throughout the book

      2. No coding examples

      3. We touch on testing throughout the book'
  - name: GerryK
    text: Sounds good!
- name: Arnthor S
  text: "Hi Joseph Reis and Matthew Housley, thanks for doing this! I\u2019m currently\
    \ reading Designing Data-Intensive Applications, and wondering what the difference\
    \ between the books are and if I should read FoDE when I\u2019m finished with\
    \ DDIA? Any important/interesting chapters/areas in this book that are missing\
    \ in DDIA that you can highlight? I think I read somewhere here (can\u2019t find\
    \ it now) an answer from Joseph Reis where you recommended reading this book first\
    \ and then DDIA, so maybe I should pause DDIA and start this one now?"
  replies:
  - name: Joseph Reis
    text: 'DDIA shows you the ins and outs of building distributed systems. FoDE is
      oriented toward the big picture of data engineering. You can think of FoDE as
      the prequel to DDIA, and very much orthogonal to DDIA''s direction. If you''re
      a data engineer, I''d say read both, starting with FoDE.

      A common thing I hear about DDIA is it throws you off the deep end quite quickly.
      FoDE will make your experience with DDIA much nicer.

      Sidenote - DDIA authro Martin Kleppman was one of our tech reviewers'
  - name: Matthew Housley
    text: DDIA is important for two reasons in data engineering. First, if you work
      for a big tech company, you may be responsible for working on the guts of large
      scale distributed data systems. This book explains how the sausage is made.
      Second, if you work more with off the shelf technologies, you still need to
      understand how they work so you can debug problems.
  - name: Arnthor S
    text: Thanks!
- name: Sergio Rozada
  text: Hi Joseph Reis and Matthew Housley, quick question here, what do you think
    about ML Engineers with core capabilities of doing Data Engineering? Unicorns?
    Better to have competences split into different roles?
  replies:
  - name: Joseph Reis
    text: Split the competencies into different roles. All in one is definitely a
      unicorn.
  - name: Matthew Housley
    text: "There\u2019s also an ongoing debate about which responsibilities belong\
      \ under ML engineering versus data engineering. The exact boundaries will be\
      \ determined by the company you work for."
- name: Varun Nayyar
  text: "Hey Joseph Reis and Matt.\nThanks for visiting here and taking the time out\
    \ to answer our questions.\nI just have a few teeny ones.\n1. Would you recommend\
    \ this book to someone with a little to no knowledge about data engineering practices?\n\
    2. Which cloud provider would you recommend as there is a lot of diverse advice\
    \ in the market right now, keeping in mind future relevance?\n3. What is a good\
    \ starting point for data engg. Other than python and pandas? Or something entirely\
    \ different? \n4. How influential are data engineers in contributing to growth\
    \ of projects? Is their role undermined by someone say a data scientist?\nThanks\
    \ for your presence here.\nWish you great luck for your book."
  replies:
  - name: Joseph Reis
    text: '1. Definitely. This book is geared toward people new to the field. That
      said, very senior DE''s have said they''ve also learned a ton of new stuff from
      FoDE.

      2. I can''t suggest a particular cloud provider. Pick the one you''ll get most
      traction with (job prospects, joy, etc)'
  - name: Joseph Reis
    text: "3. A good starting point for a DE? Read our book and find out \U0001F609\
      \n4. The influence of DE's largely depends on the team they're operating in.\
      \ DS's shouldn't undermine the role of a DE, and vice versa."
  - name: Matthew Housley
    text: 'Regarding 2: GCP has great technology, but still somewhat limited mindshare.
      Azure appeals to companies that utilize Microsoft products; they are growing
      extremely fast and investing heavily in their data offerings. AWS still seems
      to be the mindshare leader for Silicon Valley engineers.'
  - name: Matthew Housley
    text: 'Regarding 4: many projects initially need data engineering more than they
      need data science. For example, customer facing analytics for a large number
      of customers can have a big impact on the growth of a SaaS platform, even if
      these analytics are relatively simple.'
  - name: Matthew Housley
    text: "In the days of peak data science a few years back, companies hired data\
      \ scientists like crazy, but they were stymied by a lack of data engineering.\
      \ Now, there\u2019s a recognition that data engineering acts as a catalyst for\
      \ the success of data science and machine learning."
  - name: Varun Nayyar
    text: 'Thanks for the responses.

      Looking forward to reading your book.'
- name: Joseph Reis
  text: Great questions so far. Keep 'em coming.
  replies: []
- name: Eric Sims
  text: Not directly related to your book, but how did you each find yourselves working
    in data engineering? I imagine it wasn't called DE then, and you probably didn't
    start out expecting to write a book about it someday. Where did you start? Where
    did you think you were going? And why did you end up here?
  replies:
  - name: Matthew Housley
    text: "I have a PhD in math, and my research was on the pure side of the discipline.\
      \ That is, theoretical research problems generally not related to statistics,\
      \ data, computer science, etc. When I started, \u201Cbig data engineer\u201D\
      \ was a hot title, with an emphasis on managing on-premises Hadoop clusters\
      \ and writing map reduce jobs. However, EMR (Amazon\u2019s managed Hadoop service)\
      \ and Redshift (Amazon\u2019s managed columnar database) were starting to take\
      \ off."
  - name: Matthew Housley
    text: Both Joseph Reis and I refer to ourselves as recovering data scientists
      because we started out in data science but organically became data engineers
      because we needed to build data pipelines in order to deliver projects we were
      working on.
  - name: Matthew Housley
    text: In my case, I worked on a number of cloud oriented data project and spotted
      that as a long term career growth opportunity.
  - name: Joseph Reis
    text: I've only really worked with data in some capacity or another. My path has
      been very circuitous in the details, but the general direction has always been
      there for over 20 years.
- name: "Philip Die\xDFner"
  text: "Hello Matthew Housley and Joseph Reis Thanks for being here!\nFollowing up\
    \ on a previous question, what are good ways to learn about data modeling, especially\
    \ when to use one or another modeling method? (Besides reading the section in\
    \ your book \U0001F609 )"
  replies:
  - name: Joseph Reis
    text: A lot of trial and error. I suggest learning the big ideas, such as dimensional
      and relational modeling, and applying those to real world datasets. For example,
      you can use BigQuery's numerous public datasets and experiment with various
      ways to model them.
- name: Alber Novo
  text: "- Joseph Reis in a previous thread, you shared how you stay up to date by\
    \ reading a lot. Could you share some of the sources you have found reliable?\
    \ \n-  Matthew Housley, you mentioned about getting a cloud certification in another\
    \ thread. In your opinion, which one would you recommend as a start point, AWS\
    \ or GCP (Just to clarify, I don't work in the area, but I'm considering work\
    \ in this area eventually). \n- And a question about the book, on chapter 11 you\
    \ mentioned about emerging tools boosting spreadsheets with OLAP systems, could\
    \ you mention some of the candidates for this new class of tools you've seen?\
    \ Thank you for writing this book and taking time to answer questions here :)"
  replies:
  - name: Matthew Housley
    text: "Hmm\u2026 this is a tough question to answer. Personally, I prefer GCP\u2019\
      s data tools, but AWS certs will potentially give you access to more jobs given\
      \ their massive mindshare."
  - name: Matthew Housley
    text: "Regarding our speculation on spreadsheets and new interactive data paradigms:\
      \ there are various SaaS scalable spreadsheets, such as [https://www.gigasheet.com/](https://www.gigasheet.com/).\
      \ We\u2019ll see how they do in the marketplace."
  - name: Matthew Housley
    text: "Beyond that, I suspect that we\u2019ll see a lot of interesting developments\
      \ in terms of interactive analytics paradigms in the next few years."
  - name: Alber Novo
    text: "Thanks Matthew Housley. If it's tough for you to give an opinion, you can\
      \ imagine how hard it's for me to decide \U0001F605. I appreciate your input;\
      \ I'm also inclined to start with GCP."
- name: Idil Ismiguzel
  text: "Hi Matthew Housley and Joseph Reis thanks for being here and writing this\
    \ wonderful book. You mention modern data engineering profession exists to serve\
    \ downstream data consumers such as data scientists and ML engineers, and boundaries\
    \ between these three roles are often blurry and depend on the organization\u2019\
    s data maturity. I was wondering your opinion on the main overlaps between ML\
    \ Engineering and Data Engineering. In which areas an ML Engineer should be as\
    \ expert as a Data Engineer even though the organization has the split between\
    \ these two roles?"
  replies:
  - name: Muhammad Awon
    text: 'I was trying to figure this out today but couldn''t find much help, glad
      you ask the question.

      Thanks.'
  - name: Joseph Reis
    text: 'Look at the similarities - both DEs and MLEs need to move data between
      systems and storage. Additionally, they need to store and serve it.

      The differences are the MLE needs to know ML pretty well, as that''s the use
      case the MLE is serving. The DE might also need to know ML, if that''s also
      the use case the DE is serving. And herein is where the lines get blurry...The
      big difference is the MLE focuses more on the ML lifecycle, which is quite distinct
      from the DE lifecycle'
  - name: Matthew Housley
    text: And MLEs build a lot of data pipelines. Each organization has to decide
      which pipelines are owned by MLEs and which by DEs.
  - name: Joseph Reis
    text: is MLDE a job title yet?
  - name: Grzegorz Sajko
    text: '[https://www.getsphere.com/ml-engineering/data-engineering-for-machine-learning?source=ITP](https://www.getsphere.com/ml-engineering/data-engineering-for-machine-learning?source=ITP)
      DE for ML'
  - name: Idil Ismiguzel
    text: Thank you for your answers!
  - name: Joseph Reis
    text: Thanks for your questions and interest!
- name: Jk Jensen
  text: "Thanks for putting in the effort to make a quality contribution to the space\
    \ Matthew Housley and Joseph Reis! I\u2019m curious what you see as the biggest\
    \ problems to be solved in the Data Engineering space with regard to privacy?\
    \ I am recently coming from the privacy infrastructure world and I would love\
    \ to see an increased focus in this community on protecting the data we use."
  replies:
  - name: Joseph Reis
    text: There are no shortage of problems, that's for sure. Privacy is becoming
      more top of mind, but it's still a relatively young consideration for DE's.
      If this is your specialty, you've got a bright future ahead of you!
  - name: Matthew Housley
    text: In some respects, the modern data stack has increased issues with privacy
      by making data too easy. Basically, anyone handling sensitive data needs appropriate
      training, experience and best practices to do so. Cutting corners can lead to
      disaster.
  - name: Matthew Housley
    text: "Beyond that, I\u2019m excited to see the continued emergence of automated\
      \ sensitive data detection tools. One example is GCP DLP (data loss prevention)."
  - name: Matthew Housley
    text: Always follow best practices and be on the lookout for sensitive data, but
      automated tools can help to prevent human error and oversights.

---

Data engineering has grown rapidly in the past decade, leaving many software engineers, data scientists, and analysts looking for a comprehensive view of this practice. With this practical book, you'll learn how to plan and build systems to serve the needs of your organization and customers by evaluating the best technologies available through the framework of the data engineering lifecycle.

Authors Joe Reis and Matt Housley walk you through the data engineering lifecycle and show you how to stitch together a variety of cloud technologies to serve the needs of downstream data consumers. You'll understand how to apply the concepts of data generation, ingestion, orchestration, transformation, storage, and governance that are critical in any data environment regardless of the underlying technology.

This book will help you:

- Get a concise overview of the entire data engineering landscape
- Assess data engineering problems using an end-to-end data framework of best practices
- Cut through marketing hype when choosing data technologies, architecture, and processes
- Use the data engineering lifecycle to design and build a robust architecture
- Incorporate data governance and security across the data engineering lifecycle