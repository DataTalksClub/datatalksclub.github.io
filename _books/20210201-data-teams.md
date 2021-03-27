---
title: "Data Teams"
description: "Book of the Week. Data Teams by Jesse Anderson"
cover: "images/books/20210201-data-teams/cover.jpg"
image: "images/books/20210201-data-teams/preview.jpg"
start: 2021-02-01 00:00:00
end: 2021-02-05 22:59:58
authors: [jesseanderson]
links: 
  - text: Book's page on Apress
    link: https://www.springer.com/us/book/9781484262276
  - text: Book's Page
    link: https://www.datateams.io/

archive:
- name: Wendy Mak
  text: 'Hi Jesse Anderson, I have a few questions:

    for data teams, when would you choose a more ''centralised'' mode (central data
    science team where all the business teams go to ) vs a ''distributed'' mode (each
    relevant business team having one or two DS people working with them)'
  replies:
  - name: Jesse Anderson
    text: I'm looking at this once we're clear on best practices and doing them is
      second nature. Also, I'm verifying that we aren't trying to move out of a centralized
      team because the data teams aren't giving enough time to the relevant business
      team. Those issues don't magically go away.
- name: Wendy Mak
  text: 'How would you encourage business people to do more data analysis for themselves,
    e.g. if there''s an in house metrics dashboards/analysis tool, how would you
    encourage biz people to use that and not just ask the data team to get the data
    for them?'
  replies:
  - name: Jesse Anderson
    text: Through good data democratization and training. Make sure that you've given
      a place to query data while having the skills to do it.
- name: Wendy Mak
  text: 'How would you timebox/plan a proof of concept type project where it''s
    harder to gauge how long things would take'
  replies:
  - name: Jesse Anderson
    text: If a project is that difficult and the team isn't experienced enough, I'm
      looking for outside help. This outside help wouldn't be writing the code but
      helping to gauge the difficulty relative to the team's skills. That would give
      you a better understanding.
- name: Wendy Mak
  text: 'If you are in a more senior role in a DS team, how do you balance time
    between working on your own working and helping other team members and generally
    making sure all the projects are on track?'
  replies:
  - name: Jesse Anderson
    text: Look at the StitchFix interview. I think they had an interesting way of
      dealing with this by having working managers. I'd be making sure that your help
      is actually improving others. E.g. do they consistently make the same mistake?
      If so, this may be a skill or knowledge gap that needs training rather than
      help.
- name: Filipa Castro
  text: Hi Jesse Anderson! Which method would you recommend for managing the work
    from a data team? I've seen people using sprints, Kaban, CRISP, but I'm not yet
    convinced...
  replies:
  - name: Jesse Anderson
    text: There hasn't been much written on this subject. It was part of why I included
      each interviewee's project management framework. I prefer scrum or Kanban when
      I'm working with a team.
- name: Wendy Mak
  text: do you have any recommendations for best practices around collaboration (git
    and so on?)
  replies:
  - name: Jesse Anderson
    text: Git, wikis, good documentation in both code and architecture, and fomenting
      a culture of sharing and communication.
- name: Alessandro Lavelli
  text: Hi Jesse Anderson , in data focused team data versioning is crucial and it
    is recommended to keep the same version ID both for code (feature extractor and
    models) and data sets. How manage this when multiple people work on the same source
    or when there are many data sources? Thanks a lot!
  replies:
  - name: Jesse Anderson
    text: There are software projects that address this issue. I think Datatron does
      this and some others too. IMHO, this is a mix of technical and business process
      that's breaking down.
  - name: Alessandro Lavelli
    text: Thanks!
- name: Preetdeep Kumar
  text: 'Hi Jesse Anderson - As a manager of a data team, how do you define role of
    product owner (PO).  I prefer a PO who is also aware of SQL and familiar with
    tools like AWS Athena or Presto.

    Second how we define a boundary for Data teams or their exist overlaps and ambiguity
    which can''t be done with.'
  replies:
  - name: Jesse Anderson
    text: Brian O'Neill and I did a podcast about this [https://designingforanalytics.com/resources/episodes/053-creating-and-debugging-successful-data-product-teams-with-jesse-anderson/](https://designingforanalytics.com/resources/episodes/053-creating-and-debugging-successful-data-product-teams-with-jesse-anderson/).
      I ideally want a PO who is very close to the business problem and is technical
      enough to validate the data product meets the needs of the business.
  - name: Jesse Anderson
    text: For the boundary, I think that's a team maturity issue. I'd be focusing
      on the symbiotic relationships between the individual data teams. This will
      help them solve an ambiguity quickly or improve the times when the teams need
      to work together to solve a problem.
- name: Jesse Anderson
  text: Be sure to check out the extras I created for the book. I created a series
    of videos to complement the book. I did one more case study with Criteo that was
    really interesting. Get them at [https://www.datateams.io](https://www.datateams.io).
  replies: []
- name: Ricky McMaster
  text: Hi Jesse Anderson - Considering that data teams generally receive ad hoc,
    unplanned requests on a regular basis, do you think this can be accommodated structurally
    within Scrum?  Or is it more realistic to opt for Kanban?
  replies:
  - name: Jesse Anderson
    text: For analytics, lots of ad hoc tasks are unavoidable. If all tasks are ad
      hoc, that's a sign of another problem. This especially applies to data engineering.
      For ad hoc that's correct, I usually recommend Kanban.
  - name: Ricky McMaster
    text: 'Great, thanks a lot.  The proportion of ad hoc stuff is usually ~15-20%,
      so the challenge is to balance this with the strategic, planned tasks in a way
      that works for the team and doesn''t create too much admin overhead for them.

      So far, the best idea we''ve come up with is 2 boards - one for Scrum, one for
      Kanban.  The Scrum board could contain ''placeholder'' tickets for the expected
      Kanban commitment (effectively timeboxing), so that this anticipated effort
      is budgeted in advance alongside the strategic issues.'
  - name: Jesse Anderson
    text: Another way would be to divide the team. One doing ad hoc and the other
      long-term. Have the team members rotate through this so they're not getting
      bored.
  - name: Ricky McMaster
    text: Yep, we do that to an extent - I'm thinking of making each ad hoc 'shift'
      shorter though, max 2 days, for that very reason (boredom).  Anyway thanks a
      lot for your responses!  Super helpful for me.
- name: Sara Lane
  text: There are many ways to manage data teams. How did you go about doing research
    for this book?
  replies:
  - name: Jesse Anderson
    text: I've been consulting and working with data teams for the past 9 years. There's
      a great deal of my experience and comparing notes with others. The majority
      of the book is my observations of best practices and how I consult with my own
      clients. I didn't want the book to be just my own views. I had others contribute
      viewpoints and conducted interviews. The interviewees were chosen based on me
      asking my network who would they hold out as examples of well-functioning teams.
- name: Rosona
  text: Hey Jesse Anderson! Excited about this topic. Thoughts on how to take a group
    of siloed independent researchers (university backgrounds, now in industry in
    the same team) who each use a different programming language and with a different
    focus area and make them a "team"?
  replies:
  - name: Jesse Anderson
    text: 'This will be a really difficult task. There are three things in your question
      that make me worried: "researchers", "different languages", and an apparent
      lack of data engineering. You want to be careful of this.

      To your question, there are likely some skill gaps. You''d want to standardize
      on 1, maybe 2 languages. The others will need to learn that language. You''ll
      want to explain why there is a need for teams. IME researchers aren''t as used
      to being in a team. Show them how being in a team will improve the situation.
      e.g. if something breaks while they''re on vacation, it can be fixed rather
      than trying to call them.'
  - name: Rosona
    text: Yeah, I was thinking what is really needed is projects where people are
      forced to work together. Not sure how to encourage that, but I'm also not the
      manager or pseudo group lead. Thank you for your thoughts.
  - name: Jesse Anderson
    text: that will be even more difficult for you to enact change without more power.
      try to get your management to read the book.
- name: Rosona
  text: "And another question for Jesse Anderson: if there is no active leadership\
    \ in your team (no dailies/weeklies, no one tracking progress concretely, plans\
    \ only on the level of \"we should try to do x in this quarter\") -- what can\
    \ a team member do to encourage cohesion? Is it necessary to effectively take\
    \ the reins? Are there lessons from scrum-style \"servant leadership\" that can\
    \ be brought to bear? \nI see this as a data teams theme since the group mentioned\
    \ is sort of research flavored, people are developing models at whatever pace\
    \ and creating proof of concepts to try to sell the notion of using data science\
    \ and its value. I can't imagine this is an uncommon kind of side problem, that\
    \ too much leeway is then given."
  replies:
  - name: Jesse Anderson
    text: Pairing your two questions together, this team's dynamics are a big worry.
      I winced while reading your question because this won't improve without concerted
      effort and buy-in from the management. In your situation, I'd be trying to convince
      management of the need to improve. This could manifest as a real train wreck
      if it isn't already (sorry). Servant leadership will only get you so far on
      this one. This situation isn't uncommon because I've already seen it. They become
      total free-for-alls that don't get anything out the door. Take an honest look
      if this is going to improve or not.
- name: Ash Smith
  text: "Hey Jesse Anderson,\nGreat book! Great timing for me in the stage of career\
    \ too.\nI'm a PO in a data team and feel I protect the team too much from the\
    \ business and stakeholders and want them to get out into the business more (dogfooding\
    \ more \U0001F604 )\nAny thoughts on this? Some engineers just want to write code\
    \ but never want to understand how the analysis actually wants to use the data.\n\
    Thanks!"
  replies:
  - name: Jesse Anderson
    text: The engineers have to do this. If you use Agile, the engineers were always
      supposed to work with the business too but could get by without talking to them.
      Now as data engineers, it isn't an option anymore. You should figure why the
      data engineers don't want to. Is it laziness, too much work, personality conflicts?
      Once you've figured that out, you can start working with the individuals on
      those flaws.
- name: Vic
  text: "Hi Jesse Anderson \nHow would you approach the distribution of seniority\
    \ in a data team in a start up? Having too many senior people could mean they\
    \ end up doing boring job and having too many juniors could end up generating\
    \ low quality work or using up too much of the senior people's time."
  replies:
  - name: Jesse Anderson
    text: Data teams tend to skew senior. If I see a team mostly junior people, that's
      a problem. The boring jobs come with the territory. The senior people should
      be able to finish them much quicker by using the right tool for the job.
- name: Sara Lane
  text: What are the key components to creating a successful data team?
  replies:
  - name: Jesse Anderson
    text: Having all three teams present and with the right skills/people on the teams.
      You should be working with the business to deliver value from the data.
- name: Ashutosh Sanzgiri
  text: Jesse Anderson - what metrics do you think are appropriate for measuring the
    success of a data team? are there ways you can use data science techniques e.g.
    monitoring team communications, code checkins etc. to provide feedback and improve
    the efficiency of data teams?
  replies:
  - name: Jesse Anderson
    text: I talk about these metrics in the book. The overall metric is are you creating
      usable data products that the business can use and those data products generate
      business value.
- name: Sara Lane
  text: Do you see an advantage to teams working together on-site or do you think
    they can work equally well remotely?
  replies:
  - name: Jesse Anderson
    text: 'There is a certain comfort and experience with on-site teams. It''s simply
      what we''ve been used to. With the right changes and communication, they can
      be equally effective. Done right, I think remote teams can be more effective
      and have an easier time with hiring.

      I talk more about this in my interview with [Criteo](https://www.datateams.io/extras/).
      Also, see the [survey results](https://www.jesse-anderson.com/2020/12/data-teams-survey-results/)
      about data teams and COVID.'
  - name: Sara Lane
    text: Thanks!
- name: Rishabh Bhargava
  text: 'Hi Jesse Anderson, thanks for writing the book and answering the questions
    here.

    My question is around specialization. How do you think data teams should think
    about specializing in tools/skills? For example, should everyone know how Airflow
    works, or should there be a go-to guy or gal for implementing pipelines? Alternatively,
    should everyone be reasonably proficient in the core skills/tools that are important
    to the data team? Or should this be thought through on a project-to-project basis?

    I ask because there are so many tools (and everyday there''s a new one) that folks
    work with, and each and every one of them has its own unique quirks.'
  replies:
  - name: Jesse Anderson
    text: For the base or foundational technologies, everyone should know them. For
      others, there should be at least three people. This way, you can have vacations
      without worrying about coverage. The issue of so many tools is the nature of
      the data engineering beast. It isn't going to change any time soon.
- name: Vic
  text: "Hi again Jesse Anderson , and thanks for your replies so far. \nHow should\
    \ we address ownership in a data team? it's very easy and natural by silos. But,\
    \ some models affect more than one siklo, for example, finance and commercial.\
    \ How to define ownership in such cases?"
  replies:
  - name: Jesse Anderson
    text: Having two of something results in all kinds of problems. I think there
      is a team that's responsible for the data product that is actively working with
      other teams to add or improve it.
- name: Jeanine Harb
  text: 'Hi Jesse Anderson!

    Thanks for writing the book. Came here because I was looking for a book about
    Managing Data Engineering Projects, and your book was suggested to me!

    I am working on a project where I was tasked to convert some un-versioned enormous
    SQL query, into a full-fledged data pipeline. We are 2.25 engineers on the project,
    and not having managed projects before, I am finding it hard to work in a scrum-like
    way, where we define tasks and organize our work into stories. A lot of the code
    is being built from scratch, with a clear end goal though.

    Do you have any advice on how to tackle organization challenges in a data environment?
    What should be the main focus and guiding point for every iteration?

    Thanks a lot!'
  replies:
  - name: Jesse Anderson
    text: Firstly, I'd be checking if those 2.25 engineers meet the skills qualifications
      to fix this. From the sounds of it, this sort of project should lend itself
      well to scrum. You'd have to give me more context to give a suggestion.
- name: Alexey Grigorev
  text: If somebody wanted to follow your path and get into consulting - especially
    consulting companies about establishing data teams. What would you recommend them
    to do?
  replies:
  - name: Jesse Anderson
    text: Join me and together we will rule the galaxy as father and son
  - name: Rosona
    text: Alexey Grigorev you should follow up on this. :)
  - name: Alexey Grigorev
    text: "Let's say that somebody wants to rule the galaxy alone \U0001F605\nAre\
      \ there any recommendations for wannabe-solo-consultants?"
  - name: Jesse Anderson
    text: Start cross-training heavily in marketing, sales, and business. Get really
      comfortable talking about money and contracts. Create a strong brand and good
      recognition. Build up your LinkedIn connections.
  - name: Alexey Grigorev
    text: Thanks! What kind of training would you recommend for business? Something
      like an online mini MBA?
  - name: Jesse Anderson
    text: A big realization in my entrepreneur journey is that MBAs teach you to run
      other people's business rather than start your own. Focus on ones that teach
      you entrepreneurship. My favorites is the Million Dollar Consulting series.
  - name: Alexey Grigorev
    text: thanks!
- name: Alexey Grigorev
  text: Also, what do you think about MLOps? You covered DataOps in the book a bit,
    but I'm curious to know your opinion about MLOps and how is it related to DataOps
  replies:
  - name: Jesse Anderson
    text: MLOps is an important part of the equation. I'm going to be doing more content
      and research on this area this year.
  - name: Jesse Anderson
    text: It could become part of DataOps or stay separate. IMHO it will be a specialization
      of operations teams.
  - name: Alexey Grigorev
    text: 'You can start your research with our two last podcast episodes about MLOps
      and feture stores (haha sorry for the plug)

      I do agree it looks like a specialization of ops

      Thanks!'
- name: Alexey Grigorev
  text: "Quote from the book:\n&gt; Data engineering and\u2014especially\u2014operations\
    \ won't get the credit they deserve unless management makes a concerted effort\
    \ to educate others. Failing to garner praise will make other teams think that\
    \ a person or an entire team isn't necessary to the success of the project. The\
    \ reality is that key people often take their own competence for granted and don't\
    \ know how to call attention to their accomplishments.\n&gt; \nIt's often a big\
    \ problem and a demotivating factor for data engineers and ops people. I've experienced\
    \ that as well.\nWhat are the best ways to address it? Shouting out to the engineering\
    \ teams every time data scientists make a demo? Ask them to take part in demos?\
    \ Something else?"
  replies:
  - name: Jesse Anderson
    text: 'I think it starts with management taking an active role in calling out
      data engineering and operations to other managers. During a demo or conference
      talk, I think data scientists should acknowledge and call out the contributions
      of other teams. Even better is to get data engineers and operations up on stage
      or in the demo too.

      The reason for this is that listeners just assume the data scientists did it
      all. When the listeners go to implement this feature, etc they don''t know why
      they fail.'
  - name: Surya G
    text: 'This is the main reason I am planning to move away from DE to more customer
      focused team. No one ever gets a promotion for writing

      " Successfully replicated 10TB/day data into datalake/snowflake"

      in their self review.

      No matter how much we stress the importance of DE/Ops, ppl holding the purse
      string will always consider it to be a cost center that they would rather not
      have.  They have no way to know how hard or easy is it to replicate data or
      if even thats sort of an accomplishment.'
  - name: Jesse Anderson
    text: If you put "Successfully replicated 10TB/day data into datalake/snowflake"
      some of the shame is on you too. You're forcing someone to figure out the value
      you created instead of telling them the value you created. What you do is say
      "Improved data lake replicated to reduce latency by 10 minutes" or "Added new
      data product to the data lake that allow business to reduce costs by 30%". Engineers
      are good at engineering but terrible at marketing. TBH you may find yourself
      in the same boat in a customer-focused team if you don't start marketing/positioning
      your value better.
  - name: Surya G
    text: thats a very good point Jesse Anderson
  - name: Surya G
    text: '`Added new data product to the data lake that allow business to reduce
      costs by 30%".`  problem is that I alone didn''t add a new data product to datalake.
      I just did a part of that task.'
  - name: Surya G
    text: there were 10 other ppl working on that project. Would be a little weird
      to say my contribution reduced the business costs by 30%
  - name: Jesse Anderson
    text: you're saying the data product does that
  - name: Jesse Anderson
    text: you helped create that data product. you may have been part of a team but
      you'll want to take some concrete credit for the value created individually
      or as a team
  - name: Surya G
    text: 'for example there was an existing product driving off of bunch of streams/nosql/postgres
      databases.  new project,

      1. ETL-ed data from databases,streams into snowflake.

      2. Created datamodels from raw tables in snowflake

      3. migrated existing codebase to use snowflake instead of bunch of random datasources.

      I  did part of 1 as a support person for the product team doing 3. I have no
      insight into budgets/spends ect for existing projects, i really have no idea
      how much money my contribution saved the company.'
  - name: Jesse Anderson
    text: if you're a support person, your value comes from uptime and reliability.
      for example, did the reliability increase now? how much? what is that increased
      reliability worth? you'll have some leg work to figure this out but it's worth
      it. also, this is what your resume bullet points should look like. in the longer
      term, this is what will get to a next-level position.
  - name: Surya G
    text: "yea agreed Jesse Anderson. I've always looked at my contributions form\
      \ engineering pov like you mentioned.\n I will def strive to think in terms\
      \ of overall value created going forward.  Point noted."
  - name: Surya G
    text: thank you
- name: Matt Welke
  text: lol I get this a lot at my company, except people somehow subconsciously understand
    the data engineering team is important. They say things like "someday I'll understand
    what the &lt;team&gt; team does", but at the same time we get a lot of questions
    sent our way.
  replies:
  - name: Jesse Anderson
    text: Send them the book! This is a big reason I wrote the book. I cut out the
      technical jargon and tried to make it management-friendly.
  - name: Matt Welke
    text: I think your book really relates to my company right now. We've had data
      science and ML in one silo and data engineering and all other engineering in
      another silo. Literally two offices. In two countries.
  - name: Matt Welke
    text: We desperately need to get everyone working together.
  - name: Jesse Anderson
    text: That is something we do to help companies
- name: Matt Welke
  text: Data engineering seems to be a cross cutting concern.
  replies:
  - name: Jesse Anderson
    text: It's a different animal and it sound like your company understands it at
      some level
- name: Noa Tamir
  text: "I try to often call the data engineering teams \u201Cunsung heroes\u201D\
    . I heard another manager say it once and it clicked for me. So whenever I feel\
    \ like giving stakeholders or other teams some perspectives I plug it into the\
    \ conversation and people often agree."
  replies:
  - name: Alexey Grigorev
    text: "But maybe engineers actually want to hear songs about their accomplishments?\
      \ \U0001F642"
  - name: Jesse Anderson
    text: +1 on singing their songs. "Throw a coin to your data engineer"
- name: Noa Tamir
  text: "Jesse Anderson thanks for answering the questions so far - I really enjoy\
    \ going back and reading your answers. I haven\u2019t gotten through them all,\
    \ so please forgive me if I\u2019m repeating someone else.\nWhat is your experience\
    \ and/or take on having embedded DS in a DE team and vice versa? I found it very\
    \ useful in a setup where we had distinct teams for each function, but also wanted\
    \ to give each team enough in-team context and skill to handle small issues on\
    \ the go."
  replies:
  - name: Jesse Anderson
    text: I cover that in the DataOps section. It's an advanced setup where you can
      accelerate data products.
  - name: Alexey Grigorev
    text: 'In my (quite limited) experience, cross-functional teams are a lot more
      effective in terms of delivering useful things - with respect to product impact

      But from reading the book I get an impression that the setup you suggest is
      separate teams.

      In your opinion, what''s the best way to select the setup that will work better
      for a company? When to choose which approach? What kind of things we should
      take into account when deciding?'
  - name: Jesse Anderson
    text: I suggest separate teams initially. IMHO DataOps configurations are a more
      difficult organizational type. You look at DataOps once your biggest problem
      is organizational or team friction and not technical or beginners issues.
  - name: Alexey Grigorev
    text: Okay so basically start with the three teams and switch to a more complex
      setup as the org grows?
  - name: Jesse Anderson
    text: not grows, matures
  - name: Alexey Grigorev
    text: Got it, thanks!
- name: Timothy Wolodzko
  text: Jesse Anderson do you think it is a good idea to have mixed teams of data
    scientists who build the models &amp; ML engineers &amp; developers who move them
    to production, or those should be split? There seem to be pros &amp; cons of both
    approaches.
  replies:
  - name: Jesse Anderson
    text: 'I''ve seen this happen. Those teams need to be working with data scientists
      to level up their programming skills.

      IMHO a data scientist who can''t put something into production isn''t a data
      scientist. They''re still a mathematician or statistician. The data scientist
      does need to know how to program.

      It is common for MLE and data engineers to help harden data scientist''s code.'


---

Are you starting a data team and don’t know where to start? Are your data teams working but not
producing, and you don’t know why? I’ve written this book to share my extensive experience helping
companies create value with data.

Data Teams goes in-depth on the unified model for creating successful data teams. Being successful
includes ensuring you have the three fundamental teams: data science, data engineering, and operations.
Without all three teams, the data teams won’t achieve their highest and best output. For some
organizations, the team model is there but isn’t working. Data Teams helps you diagnose the problems
so you get the right teams in the right places.
