---
title: "DataOps for Dummies"
description: "Book of the Week. DataOps for Dummies by Guy Adams"
cover: "images/books/20210913-dataops-for-dummies/cover.jpg"
image: "images/books/20210913-dataops-for-dummies/preview.jpg"
start: 2021-09-13 00:00:00
end: 2021-09-17 22:59:58
authors: [Justin Mullen, guyadams]
links: 
  - text: Book's website
    link: https://www.dataops.live/dataops-for-dummies-download

archive:
- name: Guy Adams
  text: Thank you Alexey Grigorev! I'm around all week to answer any questions about
    DataOps, bringing Agile principles, automation and CI/CD to Data Warehousing -
    fire away!
  replies: []
- name: Matthew Emerick
  text: "Hey, Guy Adams! Thanks for doing this. \nHow important is it to establish\
    \ DataOps from the beginning of a new product?"
  replies:
  - name: Guy Adams
    text: Matthew Emerick - great question! Most of the people I work with already
      have something in place and want to retrofit DataOps to their current ways of
      working. However, much like DevOps and CI/CD for software, it's always easier
      to "start as you mean to go on" and build DataOps in from day 0.
- name: Matthew Emerick
  text: What do you think is the greatest obstacle in establishing DataOps in an older,
    larger company?
  replies:
  - name: Guy Adams
    text: If you'd have asked me maybe 2 years ago I would have said the biggest obstacle
      would be the die hard data veterans - people with 30 years of experience saying
      "well that's not how we do things". The reality has been quite the opposite
      - those people are saying "thank goodness, I've been waiting for this to come
      along for years".  In a larger company, maybe the biggest obstacle is how the
      teams are organized and work is done. Inevitably teams are organized around
      the way that they work (or are forced to work). When a new, better way appears,
      it can be hard for larger organizations to adopt this quickly. That said, we
      are working with some of the largest organizations in the world, and they are
      100% committed to this sort of transition, because of the benefits they get
      as a result.
- name: Toxicafunk
  text: Hi Guy Adams, thx for being here. I hear SPC as an important component for
    DataOps, in particular as introduced by Demming. I wonder if you (or other authors)
    have studied other Quality COntrol Gurus (Juran, Ishikawa, Crosby) and tried to
    introduce their ideas to DataOps?
  replies:
  - name: Guy Adams
    text: Toxicafunk - thanks for the great question. Actual in the world of DataOps,
      much like Software DevOps, the Statistical Process Control, while very important
      is actually very simplistic in it's requirements. In simple terms if very rarely
      more complex that "only execute D if and when A, B and C have completed successfully".
      Therefore the deeper science of Quality Control is rarely needed. What is important
      and unique in DataOps is how we determine that "A has completed successfully".
      In traditional DevOps or CI/CD this is simply based on a return code from a
      function/module i.e. the piece of code itself tells you whether it was successful
      or not e.g. the software compiled without errors or it didn't. In the Data world
      things can be a little bit different e.g. a software ingestion job MAY return
      a successful return code that indicates it had no failures, but does this mean
      that it has done what we EXPECT. If we are ingesting sales data every day and
      we know even on the worst day we get over 1000 sales records and the sales ingestion
      job just ran and loaded 2 rows, while the process may call this a success, we
      have additional information we can apply to post ingestion testing above this
      to determine that we didn't get the minimum we expect and therefore to stop
      the pipeline. I'm interested to hear what you think about the work of such people
      applies to data as I'm always interest to hear other perspectives!
  - name: Toxicafunk
    text: "I'm a complete noob on dataops which is why your book interests me, but\
      \ I've heard it described as the intersection of DevOps, lean Mgmt, agile methodologies\
      \ and data analytics. So I thought maybe Ishikawa's quality circles would play\
      \ well with the agile component and following your example of a successful job\
      \ but with less rows than expected... That sounds like maybe a fish diagram\
      \ could play some role. Hence my question \U0001F638"
- name: Alexey Grigorev
  text: "What's dataops? \U0001F914"
  replies:
  - name: Rosona
    text: 'Related: how do you distinguish it from data engineering?'
  - name: Guy Adams
    text: I think I can answer both questions at the same time. DataOps is to Data
      Engineering as DevOps is to Software Engineering. Software Engineering is the
      process of actually writing software - lines of code. DevOps is the processes
      and technologies around how the complete piece of software is built, tested
      and deployed. DevOps supports Software Engineering and makes Software Engineers
      far more agile and efficient - they can make some changes and have an entire
      version of the software (including their changes) built and tested, including
      automatically building the correct environments etc. DataOps is exactly the
      same for Data. Data Engineering is still required, but DataOps takes all the
      manual heavy lifting around building environments, getting test data, doing
      all the automated testing etc and, assuming everything works as expected, deal
      with the review, promotion and ultimate deployment into production.
- name: Tony Gunawan
  text: Hi, Guy Adams. Thanks for being here. Is it an overkill when I want to design
    the data warehouse to maintain the enormous data that will happen in the future
    in the company when the current data is not as big as imagined? For example if
    the company has only 10k-20k of data as of now and use the Hadoop-like design
    system with big data in mind to handle those current data?
  replies:
  - name: Guy Adams
    text: Firstly I wouldn't be advocating a Hadoop-like design for data volumes of
      any size - it's a fairly dated and very expensive and VERY complex approach
      compared to something like Snowflake. In terms of DataOps overkill - if done
      right, a DataOps project can be very simple and cost effective/show a good ROI
      for a project of any scale. In many ways if you are starting small but knowing
      you are doing to grow - that's the perfect time to implement DataOps as you
      have some time to learn and get everything the way you want it before the data
      volumes explode. Ask a professional Software Engineer the very first thing they
      do before they write a single line of functional code in a new project - they
      setup their DevOps and CI/CD system - no matter how bit of small the project
      is. Starting this way is always a great investment for the future.
  - name: Tony Gunawan
    text: "Great. Yes, I learned a lot about CI/CD implementation from software engineer\
      \ like using micro services to handle things so it can be scalable, and interesting\
      \ point when you said that the perfect time to implement DataOps is when you\
      \ start from small (aka scratch) environment so you can be more \u201Ccreative\u201D\
      \  to design and implement it, Thanks, Guy Adams. Cheers!"
- name: WingCode
  text: Is it easier for a DevOps professional transition to DataOps or a Data Scientist
    professional to transition into DataOps?
  replies:
  - name: Guy Adams
    text: Great question. In the early days of DevOps, DevOps professionals didn't
      exist - they 'converted' from a variety of disciplines - Software Engineers,
      Sys Admins even Project Managers. DataOps is in the same place - the pioneers
      becoming DataOps champions are coming from a variety of places, but of course
      some will have a slightly easier time in the transition. The most typical path
      into a DataOps Engineer is from someone historically a Data Engineer, but with
      some coding/automation background. However a DevOps professional (who typically
      has some passable database knowledge) is going to have a pretty easy time of
      it. The Data Scientist is harder to predict since I have worked with a lot of
      Data Scientists who have very different skill sets - however I would say it's
      a less obvious transition that the others.
  - name: WingCode
    text: Thank you Guy Adams for the great answer!
- name: Yash Khandelwal
  text: '*Why we need the DataOps ?*'
  replies:
  - name: Guy Adams
    text: If you are working in the Data/Analytics space and you enjoy building everything
      manually, having no automated testing, having no integration between systems,
      being very slow to respond to business requests and having very little governance
      - then you don't. However is you want to have the same Agility, Speed, Automation
      etc as Software Development has enjoyed for 20+ years then you absolutely want
      DataOps.
- name: Tim Becker
  text: Hi Guy Adams, thank you for answering our questions!
  replies: []
- name: Tim Becker
  text: '- I saw in your book that you mention good collaboration as crucial. Could
    you provide some advice on how to best collaborate in data centric teams. I mean
    how to design a framework that helps with better collaboration.'
  replies:
  - name: Guy Adams
    text: Tim - collaboration requires three main things - overall philosophy, the
      right technology and the right team structure. One of this biggest thing people
      seem to struggle with is that no amount of technology can mitigate the need
      for people to actually talk and work together. The goal of technology in this
      situation is to support people working collaboratively rather than to magically
      create collaboration. In my experience actually, if you take the technical barriers
      away, in general people are pretty good, and work quite naturally in a collaboratively
      way. There is clearly a lot about how you plan your work, structure your team
      etc - if you are running your teams in an Agile way - this naturally creates
      collaboration. Technically, by far the best approach, and the one we follow
      within the DataOps.live is system, is to follow how the software world solved
      this - using git. Git is a phenomenal tool to allow potentially massive teams
      (thousands of people) to all go off, do their own thing, work in little teams,
      but still be able to bring work together in a very controlled way. With this
      in place, and good Agile methodologies, it's actually pretty easy.
- name: Tim Becker
  text: '- How much test coverage do you recommend?'
  replies:
  - name: Guy Adams
    text: Enough!!! This is very much "how long is a piece of string question" - there
      is no simple answer. The software world has been measuring test coverage for
      20+ years and still can't agree on this. The way I encourage customers to think
      about this as an ongoing process rather than a one off activity. When you start
      out, spend some time about thinking about the most like, or the most business
      impactful failure modes and add tests for these. I recommend, as a rule of thumb,
      if you have 5 tests for a table, you are probably in the right ball park. However,
      much more important than the number of tests is the usefulness of the tests.
      It's trivial to add a set of simple tests to every column in a table unique,
      not null etc - and doing this you can easily create 10s or 100s of tests - but
      are these really telling you much. 1 really smart test can be worth 100 tests
      created "for the sake of it". However you get there, you will eventually go
      live with a set of tests and they will be imperfect, and issues can slip through.
      It's a fact, just accept it. By catching the majority of issues that would have
      got into production you are already well ahead of most people. Business users
      are actually relatively forgiving of things like this. What they are NOT forgiving
      of is repeition. If they report an issue and you fix it - no problem. If that
      problem reoccurs and they have to report it again - now you have lost trust
      and credibility. This brings me to the second part - every time you fix a data
      issue that you didn't catch, you MUST add the tests to prevent this issue from
      getting to users again and you REALLY SHOULD spent 10 minutes thinking a) could
      this same issue occur again in other places - if so lets catch that now and
      b) could this issue occur in a slightly different form, if so, lets catch that
      now. This becomes an ongoing process if improving your tests over time and I
      believe is the best and most pragmatic approach.
- name: Tim Becker
  text: '- How to automate documentation in practice?'
  replies:
  - name: Guy Adams
    text: 'We have this built into out DataOps.live platform - since we have all of
      the logic about how we build, transform, test etc in the repository, and we
      have access to the target database itself, we have all the information needed
      to build a really good set of automated documentation.  I''ve added a few screenshots
      for this. My team host a weekly office hours session: [https://www.dataops.live/office-hours](https://www.dataops.live/office-hours)  if
      you''d like to learn more!'
  - name: Tim Becker
    text: "Guy Adams Thank you for answering my questions \U0001F642 automated documentation\
      \ seems pretty nice"
- name: JGatz
  text: Hi Guy Adams, thanks for doing this!  Regarding overcoming organisational
    hurdles - have you ever experienced issues between pre-existing DevOps teams and
    the new DataOps team that an organisation was trying to introduce?  For example
    ownership, best practices etc.
  replies:
  - name: Guy Adams
    text: What I have experienced most is that existing DevOps teams have already
      regarded/been told "sorry the Data team is special - you have no business here"!
      Once they actually see an organization start to move towards DataOps and embrace
      DevOps principles, they are usually very happy. One big warning - if you are
      starting looking at DataOps, ALWAYS involve your existing DevOps teams - if
      you don't, they will see this as a Shadow DevOps initiative and the team that
      should be your biggest supporters may turn into a barrier. They may well have
      some corporate requirements you need to adhere to, but these are usually straightforward
      to adopt. Ownership is usually within the DataOps team, because DataOps is a
      unique thing, but adopting standard company best practices and standards would
      come from the DevOps team
  - name: JGatz
    text: 'Cool, that sounds good advice.  As ever, a lot depends on clear and proactive
      communication.

      &gt; ALWAYS involve your existing DevOps teams - if you don''t, they will see
      this as a Shadow DevOps initiative and the team that should be your biggest
      supporters may turn into a barrier

      ...well said.'
- name: Timur Kamaliev
  text: 'Hi Guy Adams, thanks for your detailed answers!

    I noticed that for the past 2-3 years, there has been an explosion of different
    terms related to the world of IT operations (DataOps, MLOps and more). Do you
    think this trend will stay in the future? And will the business be  interested
    in this and in specialists from such areas?'
  replies:
  - name: Guy Adams
    text: Great question. I believe when there is new concepts, there becomes an explosion
      of concepts, terms (and with a lot over overlap, duplication, contradiction)
      etc and then overtime some of these coalesce and become a better defined and
      more standard thing. For example I consider MLOps as a subset of functionality
      within DataOps. As the tools become easier to use and the areas become better
      defined, most organizations won't need separate specialists for say DataOps,
      MLOps etc - one team will be able to handle all of these. I don't think the
      wider business will care about any of this - they just want the Data team to
      be able to deliver quickly, reliably and with good governance!
- name: Jeanine Harb
  text: 'Hi Guy Adams, thanks for taking our questions!

    In my few years of experience as a data engineer, I''ve found that the most complicated
    aspect about testing data pipelines (and overall dataops) is the fact that data
    models constantly shift (schema changes, different needs...). It is quite time-consuming
    to adapt automated tests. What would you recommend to simplify this process?'
  replies:
  - name: Guy Adams
    text: 'You are very welcome. You are absolutely right - when everything is shifting
      rapidly, keeping tests lined up can be hard. I have a few recommendations here:

      1. Ensure that your tests are stored in the same git repo as your actual configuration
      and code so that as you make changes and deploy them - the functional changes
      and tests are deployed together

      2. Ensure that your tests are defined in the same place, right along side your
      functional logic. If you have the data modelling defined in one place and the
      tests in a different place it''s virtually impossible to keep them in sync.
      BTW the same here applies to Grants are permissions - if you define them right
      along side the functional code is MUCH easier to manage and MUCH harder to make
      mistakes.

      3. Deploy your actual functional changes using an automated declarative approach
      like the Snowflake Object Lifecycle Engine in the DataOps platform - not writing
      endless ALTER TABLE statements!'
  - name: Jeanine Harb
    text: Thanks a lot, this is great advice!
- name: Sri
  text: 'Thanks Guy Adams for this book and taking our questions!

    Site Reliability Engineering (SRE) is being used by many big organizations for
    operating large software systems. Similar to `class SRE implements DevOps`  (as
    mentioned in [this blog](https://cloud.google.com/blog/products/gcp/sre-vs-devops-competing-standards-or-close-friends)),
    what is your thought on `class DRE implements DataOps`  DRE-&gt; Data Reliability
    Engineering with metrics like SLIs/SLOs and SLAs for all data/pipelines related
    tasks?'
  replies:
  - name: Guy Adams
    text: Very forward thinking question! I've never really come across the term DRE
      in the real world *yet* - but I like it a lot. I think some of this is a maturity
      thing. DevOps took a while to mature before SRE really became a thing - I think
      full DRE is a little bit down the line for most organizations. However here
      is one question I always encourage my customers to think about "What is the
      % availability of your data" - most of them answer very quickly "the uptime
      of my data platform is 99.99x" - but I challenge them on this. I didn't ask
      what the uptime was, I asked what the availability of your data was - by which
      I mean, what percentage of the time is the the *correct* data available to the
      *right* business users, *up to date* and *provably*  correct. Virtually no-one
      is able to measure this today, but I think this sort of metric would be at the
      core of DRE.
  - name: Guy Adams
    text: An add on though - if you search for DRE - you get many more matches for
      "Database Reliability Engineering" than "Data Reliability Engineering" - I think
      this is totally missing the point - to me Database Reliability Engineering is
      focusing on that uptime element. Data Reliability Engineering must have a much
      broader focus - to get good, valid, provable data in the hands of the users
      that need it requires many things working on concert - the Database is a critical
      component, but it is only one part of the puzzle so for me "Data Reliability
      Engineering" &gt;&gt; "Database Reliability Engineering"
  - name: Sri
    text: Thanks Guy, for your thoughts.. Yes, I too agree that database reliability
      engineering is completely missing the broader focus on the dataops.. I like
      the way you put it.. DB is subset of broader "Data". Thanks again!
- name: Guy Adams
  text: Thanks all for having me on book of the week - there have been some great
    and thoughtful questions and I've really enjoyed it. Feel free to contact me here
    or at guy.adams@dataops.live if you have any further questions about DataOps  and
    I'd be happy to help!
  replies: []
---

DataOps describes a novel way of development teams working together collaboratively
around data to achieve rapid results and improve customer satisfaction. This book is
intended for everyone looking to adopt the DataOps philosophy to improve the governance
and agility of their data products. The principles in this book should create a shared
understanding of the goals and methods of DataOps and `#TrueDataOps` and create
a starting point for collaboration.


