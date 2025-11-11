---
episode: 7
guests:
- nikolamaksimovic
ids:
  anchor: From-Digital-Marketing-to-Analytics-Engineering---Nikola-Maksimovic-e1qr75s
  youtube: GawJ7mG5ElQ
image: images/podcast/s11e07-from-digital-marketing-to-analytics-engineering.jpg
links:
  anchor: https://anchor.fm/datatalksclub/episodes/From-Digital-Marketing-to-Analytics-Engineering---Nikola-Maksimovic-e1qr75s
  apple: https://podcasts.apple.com/us/podcast/from-digital-marketing-to-analytics-engineering-nikola/id1541710331?i=1000586740912
  spotify: https://open.spotify.com/episode/5VwS6ijaToirTzR7Xd5Phw?si=OsOVLOzBSt2sIgvbRS3krg
  youtube: https://www.youtube.com/watch?v=GawJ7mG5ElQ
season: 11
short: From Digital Marketing to Analytics Engineering
title: 'Marketing to Analytics Engineering: DBT, SQL, Data Modeling & Career Playbook'
transcript:
- line: This week, we'll talk about switching careers from marketing to analytics
    engineering. We have a special guest today, Nikola. Nikki started her career as
    a performance marketing specialist and quickly realized that she needs to rely
    on data to make good decisions. That's how her data journey started and she eventually
    became an analytics engineer. In this interview, we will find out how that happened.
    Welcome to our event.
  sec: 0
  time: 0:00
  who: Alexey
- line: Thank you very much for having me.
  sec: 30
  time: 0:30
  who: Nikola
- header: Nikola’s background
- line: I want to mention – this is something new – questions for this interview were
    prepared by Leat Shemesh, and Victoria Perez Mola, so thanks a lot for your help
    in preparing the questions. If anyone here who is listening and wants to help
    us prepare for more interviews in the future, please reach out to me. Okay, let's
    start. Before we go into our main topic of switching to analytics engineering,
    let's start with your background. Can you tell us about your career journey so
    far?
  sec: 32
  time: 0:32
  who: Alexey
- line: Yeah, of course. I actually studied in the UK, in London, and I moved over
    to Berlin soon after graduating from my Bachelor's quite spontaneously. I found
    myself just in the data startup scene, like many English-speaking people do, [chuckles]
    because it was pretty much the only available route. So I started out working
    for Movinga, which was a big removals startup, backed by Rocket Internet. I was
    working in the operations team there. I kind of had my first taste of working
    at a startup there.
  sec: 64
  time: '1:04'
  who: Nikola
- line: Of course, as you can imagine, that was very intense – fast growth, lots of
    change. It was kind of a baptism of fire for six months. After that, I found a
    job at Ecosia. I was really following Ecosia really closely because I really was
    inspired by the business model and the mission. For those who don't know, Ecosia
    is the search engine that uses its profits to plant trees. It's essentially a
    purpose company, which means that profits are basically entirely used towards
    financing the tree planting project. Then I suddenly saw a job for a generalist
    marketing role, which I applied for. My first role at Ecosia was actually sort
    of more generic marketing.
  sec: 64
  time: '1:04'
  who: Nikola
- line: Was it something that you also did at Movinga? Was it something different?
  sec: 166
  time: '2:46'
  who: Alexey
- line: It was completely different. But it was a generalist kind of junior role,
    where you're helping write press releases, think up campaigns, reach out to potential
    partners – this kind of work. I've done quite a lot of that through university
    when I've been volunteering for an organization that helps students get into volunteering.
    Through that kind of work, and through more not professional work, but rather
    just more organizing, political work, event planning and stuff I've done at university,
    that's kind of where I had built up those organizational and marketing skills
    from. That's essentially what I ended up really speaking about largely at the
    interview.
  sec: 173
  time: '2:53'
  who: Nikola
- line: We were a really small company with 15 people when I joined. So it was really
    one of those early-stage startups. We were doing whatever job needed to be done.
    Sometimes it was replying to user feedback, other times it was helping test a
    new app design – all sorts of things. At some point, I felt like I really wanted
    to go deeper into an area and I basically started running the paid campaigns that
    we started doing after I joined the company. First it was on Facebook, but later
    on we expanded onto YouTube and Instagram. And I really enjoyed that. I found
    it very helpful to really focus in on a specific area.
  sec: 173
  time: '2:53'
  who: Nikola
- line: Something I found very gratifying about performance marketing was that you
    get results very quickly, so you can kind of really see what's working and what's
    not working. As opposed to other areas of marketing where something like a press
    campaign or brand activation, where it's not necessarily clear what impact that
    might have had right away. Sometimes it's really difficult or almost impossible
    to measure, which I found very frustrating. [chuckles] But with performance marketing,
    you're given the data immediately and you can analyze that and make a decision
    in minutes on how to move forward. I got really, really into that.
  sec: 173
  time: '2:53'
  who: Nikola
- line: Of course, there are so many online resources for performance marketing, and
    in general. It's a relatively new discipline as well, in the grand scheme of the
    history of marketing. So I was really able to dive into that by myself, largely.
    I was given a lot of responsibility at the company as well, so I learned that
    way. I did that for two years. At some point, I also started to kind of think,
    “Okay. Well, I feel like I've kind of understood this. It maybe has its limits
    in terms of what's interesting or not.” The part that I really enjoyed was looking
    at the data coming in, analyzing what the click-through rates are saying, what
    the conversion rates are and what that means. “How can we optimize this campaign
    based on the data that we're getting? How does it compare with historical trends?”
    All of this sort of work I really enjoyed.
  sec: 173
  time: '2:53'
  who: Nikola
- line: At the same time around this time, the company had switched to Looker from
    Tableau. At the time, we only had one data person at Ecosia. I helped her with
    the migration to Looker just as a side project. Since I was kind of the person
    who was most comfortable with data and reporting and numbers and measuring KPIs
    and whatnot in the marketing team, I took on building out the marketing team reporting.
    And I really enjoyed that.
  sec: 173
  time: '2:53'
  who: Nikola
- header: Making the first steps towards a transition to BI and Analytics Engineering
- line: It was your initiative, right? Nobody told you, “Hey, you should do this.”
    You were just like “Okay, this sounds interesting. I really like this topic. And
    I kind of learned everything that was there about performance marketing, so let
    me try to also run this new tool.”
  sec: 424
  time: '7:04'
  who: Alexey
- line: Yeah, exactly. I think at this point, it wasn't really clear to me that I
    wanted to necessarily move into the data team. I just wanted to maybe have more
    focus on numbers and data in general, but probably still within the marketing
    team. Eventually, I think the big shift that happened was – the pandemic hit.
    Like a lot of people, it just forced me to consider what I was doing and whether
    I was happy in my role, and I found that I really wasn't. At this point, I decided
    to yet make the shift into the BI team. I think, at this point, I had already
    done a SQL course some months before with a view to going down the marketing/analytics
    route. But with the pandemic, I really realized that I wanted to move away from
    the purely marketing focus and go towards BI.
  sec: 438
  time: '7:18'
  who: Nikola
- line: These SQL courses – did you have a plan that you wanted to work in the BI
    team eventually? Or it was like, “Okay, let me see what I should do in order to
    do my job better.”?
  sec: 509
  time: '8:29'
  who: Alexey
- line: I think I remember speaking to my colleague in the BI team, who was in the
    context of being a marketing analyst person. Initially, the idea was kind of that
    I'd sit between marketing and BI. But I think it's because I really didn't think
    it was possible for me to move departments. That hadn't really happened in the
    company before. There wasn't really an example of that to me. So I think I was
    rather thinking, “Well, what's possible? What could I do?” And it was this marketing
    analyst role. But yeah, I definitely took the SQL course in order to move closer
    towards the data side.
  sec: 525
  time: '8:45'
  who: Nikola
- line: So then you realized, “Okay, maybe I'm not really super happy with the job
    I'm doing in the marketing department and there is this BI team.” So did you just
    approach them and ask, “Can I just join you and start working with you?” Or how
    did this happen?
  sec: 576
  time: '9:36'
  who: Alexey
- line: Eventually – yes. I think eventually the conversation was already there, as
    I mentioned before, around how to become more into this marketing analyst role.
    Already, my colleague was giving me lots of advice. It was probably through that
    process and those conversations that the possibility of me moving into the BI
    team came up, to be honest. I don't remember exactly who brought it up. But what
    I remember is my colleague in BI saying, “Well, these are the things that we really
    need you to have. Once you have those things, there's no reason why you shouldn't
    be able to join the team as a junior analyst.”
  sec: 593
  time: '9:53'
  who: Nikola
- header: Learning the skills necessary to transition to Analytics Engineering
- line: Do you remember what these things were? SQL, I suppose, is one.
  sec: 642
  time: '10:42'
  who: Alexey
- line: Yes, SQL was the main thing. Then learning and understanding the data pipeline
    that we had was another.
  sec: 645
  time: '10:45'
  who: Nikola
- line: So it wasn't a list of courses that you have to take, but rather, “Okay, these
    are the things we’re working on. Try to figure out what's happening there.”
  sec: 655
  time: '10:55'
  who: Alexey
- line: Yeah, exactly. One of the things was like, “Python would be great.” I ended
    up doing a Python course, but barely actually using it. It's been useful to have.
    Of all the things, the most useful practically was jumping into… once you know
    SQL and you can write and read SQL, you'll still need to get good at reading and
    writing SQL. You start coming across much more complicated SQL queries and you're
    like, “[expletive], there's like a nested loop here. Where is this coming from?”
  sec: 662
  time: '11:02'
  who: Nikola
- line: Then improving SQL to be able to read and understand much more complex data
    models – that was a big part of the journey. It was really about understanding
    what our models were, how everything fit together in the wider scheme of the pipeline,
    and how it came to be. Because I had no idea even how a tracker really worked
    – I just sort of knew that there was this thing called the Snowplow Tracker that
    collected the data. But it was all sorts of not very detailed knowledge. So really
    going in and understanding how things really work to get the data from one point
    to the other and transform it.
  sec: 662
  time: '11:02'
  who: Nikola
- header: The in-between period – from Marketing to Analytics Engineering
- line: Did you need to keep doing your old job of marketing specialist, or could
    you completely just immerse yourself in BI? Or was there some in-between period
    where you had to do both?
  sec: 749
  time: '12:29'
  who: Alexey
- line: To be honest, as part of the performance marketing role, I was really acting
    like a kind of marketing analyst, in a way – building the reporting for the teams
    and for the people who are doing other jobs, I was helping them build reports
    and managing that. So I was already kind of doing a lot of that kind of work.
    There was a transition period where the first projects that I worked on were more
    marketing-focused. I think one of the main projects was helping establish how
    to measure brand campaigns, looking into that and building dashboards based on
    that, and a wider topic around that.
  sec: 770
  time: '12:50'
  who: Nikola
- line: I think it was kind of a transition period, but at some point, I just handed
    over the main performance marketing tasks, which are managing the campaigns. It
    was quite a good moment because the pandemic meant that we were already hitting
    a slight stagnation point with some of our campaigns. Then the pandemic hit and
    it was really difficult to record new ads, as well, in quarantine. There was a
    kind of natural slowing down of that side of the work anyway, so it was a good
    moment to pivot.
  sec: 770
  time: '12:50'
  who: Nikola
- header: Nikola’s current responsibilities
- line: And what do you do now? What do your responsibilities include?
  sec: 854
  time: '14:14'
  who: Alexey
- line: As I've mentioned, I'm working as an analytics engineer, but also as a data
    analyst. We are still a relatively small team. We are four people in total. For
    reference, the company size is just over 100. None of us have a particularly specialized
    role. We kind of do a little bit of everything at the moment. Our team lead is
    on extended leave, so I'm acting as interim team lead. A lot of work is really
    working with the new CPO who's just come in, reassessing the KPI that we have
    at the company and how we measure them. Of course, I think it’s quite common when
    a new C-level comes in to rehash the dashboards and rework the core reporting
    to suit the new requirements, so a lot of work has been recently done on that.
  sec: 860
  time: '14:20'
  who: Nikola
- line: There are two of us that are in these analyst roles and we work very closely
    with product managers. We're focusing very closely on supporting the various product
    teams with experimentation, building out new features, A/B testing, evaluating
    those, and when necessary, building out our data model to reflect those new changes.
    I think the day to day is really a mixture of supporting the teams – sometimes
    ad hoc analysis is needed. For example, there is a new feature being developed
    and there's some hypothesis around the kinds of users they want to reach and how
    big those cohorts might be, jumping into the data and taking a look at that. Other
    work is maybe more on an initiative of our own. For example, recently, we ran
    a big RFM analysis (recency, frequency, monetary) user behavior analysis, which
    was a bigger project. There's many ways to do it and we took some time to experiment
    with different options. That's been a larger project over some months with several
    presentations of insights.
  sec: 860
  time: '14:20'
  who: Nikola
- line: There are those bits of work where we're not necessarily working directly
    for an individual product manager, but working on wider pieces of analysis and
    insight that's beneficial for the company as a whole. I just wanted to add that
    we've also recently started doing a few small data science projects in the team,
    just on the side, which I myself am not directly involved with. But one of my
    colleagues is. We're trying to basically run some NLP models on trying to improve
    how we understand queries that our users make, and try and essentially build better
    query categorization so we can ultimately serve better results. It's been really
    nice that we've been able to pick up some more data-sciencey topics in the team
    and not work exclusively on reporting and internal.
  sec: 860
  time: '14:20'
  who: Nikola
- line: 'This query understanding – it''s about understanding intent, right? Why a
    user is searching for some information: Do they want to come in and navigate to
    a certain website? Do they want to get some information? Do they want to buy something?'
  sec: 1079
  time: '17:59'
  who: Alexey
- line: Yeah, exactly. Specifically, it's around being able to segment various queries
    into the correct categories. So “does this query or query group fall into the
    category of ‘travel’ or ‘shopping’ or ‘transport’ or etc.?”
  sec: 1094
  time: '18:14'
  who: Nikola
- header: Understanding what a Data Model is
- line: So a different kind of characterization. When you were describing what kind
    of duties you have and what kind of things you work on, you mentioned that you're
    working on KPIs, dashboards, supporting product teams with experiments, ad hoc
    analytics.
  sec: 1114
  time: '18:34'
  who: Alexey
- line: You also mentioned a data model. Up to the data model, I think I understood,
    more or less, what you are doing. But what is a “data model”? Why do you need
    to build a data model? Why do you need to update it?
  sec: 1114
  time: '18:34'
  who: Alexey
- line: We built a data model in DBT based on something called the domain model. Basically,
    we began two or so years ago, maybe even longer now. We migrated to DBT. In that
    moment, we basically rewrote all our queries basically to build all our tables
    – the whole database was rebuilt from scratch. It had evolved over time. We have
    something like six installed tables or something ridiculous.
  sec: 1147
  time: '19:07'
  who: Nikola
- line: Six what tables?
  sec: 1190
  time: '19:50'
  who: Alexey
- line: Install.
  sec: 1191
  time: '19:51'
  who: Nikola
- line: The data model is about describing what kind of data you have – all this schema
    and definitions, right?
  sec: 1195
  time: '19:55'
  who: Alexey
- line: Yeah, sorry. For the data model, what I mean is – what we have in DBT, essentially,
    is all about different transformation logic for the entire business, from the
    most basic staging layer down through to the presentation tables that we then
    use for analysis.
  sec: 1200
  time: '20:00'
  who: Nikola
- header: Tools needed to work as an Analytics Engineer
- line: I’m just trying to understand what kind of tools you use. You mentioned three
    tools already. You mentioned Snowplow, which is a tool for tracking – to understand
    what kind of actions users perform and save intersections. Then you also mentioned
    DBT, which is a tool for transformation. You have some data sitting somewhere
    and you need to change it slightly, rework, aggregate it, and then put it in such
    a form that you can use it for reports. You also have Looker, which is a tool
    for dashboards. What else do you use? You probably use some sort of database (a
    data warehouse) right? Maybe some other tools too?
  sec: 1234
  time: '20:34'
  who: Alexey
- line: Yeah, exactly. We use AWS services, so we use S3 and Redshift, and also Spectrum
    as well to query Athena. We play around a lot with so-called “hot and cold storage”
    so keeping data in Redshift versus keeping it in S3 in parquet files. That's due
    to cost optimization. That's what we use for our lake (warehouse). And then we
    use Airflow as well, as our orchestration tool and for our extracting and loading
    operations.
  sec: 1278
  time: '21:18'
  who: Nikola
- line: Was it a part of your job to set up all these tools?
  sec: 1323
  time: '22:03'
  who: Alexey
- line: It was part of my job to set up DBT. That was one of the first big projects.
    I'd been in the team for maybe six months or so and then we began the migration
    to DBT. We actually worked with a data consultancy, a small one, that helped us
    because we were essentially three people. I led that project – it was one of my
    first big projects, which was great. It was a really big learning curve.
  sec: 1328
  time: '22:08'
  who: Nikola
- line: I got to learn not only about DBT (the tool itself) but also data modeling
    theory and practices and different ways of doing things – what makes sense depending
    on the size of your data and your goals and needs. That was really great. So DBT
    is the main one. Looker as well, as I mentioned, I helped to migrate to and implement
    in the company.
  sec: 1328
  time: '22:08'
  who: Nikola
- line: This was before you actually joined the BI team, right? So you started this
    in marketing looking at this tool.
  sec: 1386
  time: '23:06'
  who: Alexey
- line: Actually I strangely learned LookML before I learned SQL, which is a slightly
    strange, I think, way of doing it. [chuckles] But there we go, that's how it happened.
    And Airflow was set up by my colleague who has more of a data engineering role
    within the team. That was also set up relatively recently – in the last two, three
    years or so. Those are the main tools. We recently started using Airbyte. Some
    people might be familiar with that. It was basically to be able to extract from
    some kind of common API's data sources. We haven't used it extensively.
  sec: 1392
  time: '23:12'
  who: Nikola
- line: So far, we often find that we've got a lot of options, but specifically what
    we need often doesn't necessarily have the connection yet. But I think it's a
    nice tool – relatively easy to use. We've also recently started using Redash,
    which is an open source visualization tool that we use for more ad hoc queries,
    to be able to have the visualization attached to them as well.
  sec: 1392
  time: '23:12'
  who: Nikola
- line: It seems like most of the tools are open source, apart from AWS. Is Looker
    open source?
  sec: 1466
  time: '24:26'
  who: Alexey
- line: No, I don't think so.
  sec: 1472
  time: '24:32'
  who: Nikola
- line: But the rest are, right? Snowplow is open source. DBT is open source. Airbyte
    is open source. Redash – I don’t know. Is it?
  sec: 1474
  time: '24:34'
  who: Alexey
- line: Redash is open source as well.
  sec: 1481
  time: '24:41'
  who: Nikola
- line: So you like open source. Don’t you?
  sec: 1484
  time: '24:44'
  who: Alexey
- line: Yes. [laughs] Exactly.
  sec: 1487
  time: '24:47'
  who: Nikola
- line: Do you host all these things yourself? For example, when it comes to DBT,
    do you use their cloud?
  sec: 1491
  time: '24:51'
  who: Alexey
- line: No, we host everything ourselves. That's just the general decision of the
    engineering department.
  sec: 1497
  time: '24:57'
  who: Nikola
- header: The Analytics Engineering role over time
- line: When you joined the BI team were you already called an analytics engineer,
    or you just realized over time that, “Okay, this is what I should call myself.”?
  sec: 1506
  time: '25:06'
  who: Alexey
- line: My official role is Analytics Engineer and Data Analyst, because I really
    do both. We’re not the size of a BI team that it's possible for someone to want
    too much to do. But I think initially, it was… I don't know what the title was
    initially, BI Analyst or something – Data Analyst. At that point, even the term
    Analytics Engineer really wasn't common. I think I really only learned about that
    in the process of implementing DBT, which was in 2020.
  sec: 1517
  time: '25:17'
  who: Nikola
- line: Really, some time has passed since DBT has obviously become huge in the data
    community. I think this role of an engineer is also becoming much more common.
    But I think at the time, when I joined the team, that wasn't even an option. I
    don't think anyone even thought of that. I don't think the people in the BI team
    were actually calling themselves that, even though that's essentially the job
    they were doing. Over time, as we all became familiar with that new term and realized
    that it basically described what we were doing – so that was taken on.
  sec: 1517
  time: '25:17'
  who: Nikola
- line: Do you think there's some hype in that role? I mean, there was no such thing
    before and now, all of a sudden, everyone’s talking about analytics engineering.
  sec: 1596
  time: '26:36'
  who: Alexey
- line: Yeah. To be honest, if you have a small BI team of six or less people – I
    guess it depends on your company, and your product and the business model – but
    I think it's a little bit overhyped. Ultimately, I still think that you need quite
    a large organization to be able to comfortably segment data analysts and analytics
    engineers – they have so much crossover anyway. I can see that in larger organizations,
    it's really helpful to have that separation. But I think in smaller ones, it's
    not that helpful, at least in my experience, which is simply this is one company.
    I can't speak for others, but I found that it's helpful in terms of your own personal
    progress, because you can align yourself with this role and say, “Okay, yes. This
    is what I do. This is somewhere where I could improve and an area that I could
    spend more time on, but I'm not necessarily sure.”
  sec: 1605
  time: '26:45'
  who: Nikola
- line: I think for most small/medium-sized companies, I don't think it's necessary
    to get really bogged down into the differences between the two. Ultimately, you’re
    still going to need very overlapping skills. You need to be very analytical, very
    comfortable with your KPIs, what the business model is, the domain model – all
    of that work, which is not limited to an analytics engineer and a good data analyst
    needs all of those things. I think there's maybe a little bit of hype. But again,
    as I said, it depends on the organization size. If you have a huge company with
    a data Department of 20, 30, 40 people, then of course, it just makes structural
    sense to split out and focus.
  sec: 1605
  time: '26:45'
  who: Nikola
- header: The importance of DBT for Analytics Engineers
- line: Do you think it's synonymous to using DBT? Like “You use DBT, therefore, you’re
    an analytics engineer.” And “If you’re an analytics engineer, then you use DBT.”?
    Are they the same thing? Or  can you be an analytics engineer without using DBT?
  sec: 1720
  time: '28:40'
  who: Alexey
- line: It's a good question. I feel like DBT themselves have really promoted this
    concept, right?
  sec: 1740
  time: '29:00'
  who: Nikola
- line: I think, yeah. It’s coming from them.
  sec: 1747
  time: '29:07'
  who: Alexey
- line: Exactly. [chuckles] In a way, yeah – it kind of is synonymous. I, at least,
    haven't seen many job applications for an analytics engineer that haven't been
    like “Your job is to work with DBT.” [chuckles] I'd be interested in how that
    role could look with a different stack. I imagine there are people who are working
    under the title of data engineer or data analyst who do the work of an analytics
    engineer, but just don't call themselves that in other companies that maybe don’t
    use DBT.
  sec: 1749
  time: '29:09'
  who: Nikola
- line: In the company where I work, we don't have DBT. We have a homegrown DBT kind
    of replacement. But it was before DBT was popular. As many other companies, we
    kind of invented DBT, which is like an Airflow-based way to schedule SQL queries.
    I don't think any of our analysts who use this to call themselves analytics engineers.
    I'm wondering, are there any tools that do the same thing as DBT apart from these
    homegrown tools like we have? Is there any such thing on the market?
  sec: 1788
  time: '29:48'
  who: Alexey
- line: I don't know, to be honest. [laughs] I haven't had the time to really look
    into it. I think at the moment, DBT is on such a growth trajectory. I see so many
    job ads that are looking for people to help them set up DBT. I think it's really
    taking off, so I don't presently know. Like you said, we were previously using
    SQL Runner, which is like Snowplow. It’s kind of similar. That’s exactly what
    you described, basically. An orchestration tool for SQL queries, where you can
    specify the order and whatnot. Incrementalization strategies were not invented
    by DBT. There's many ways to set those up and there’s other kinds of setups.
  sec: 1828
  time: '30:28'
  who: Nikola
- line: In terms of analytics engineering, I think for me the focus is on the wider
    architecture of the data model, and with data analysts for example, perhaps there’s
    not so much focus on that. For me, that's where the analytics engineering role
    is, really important. Once you start collecting from various different data sources
    you have all of these issues around consistency and, of course, freshness. All
    of these various concerns are where an analytics engineer really needs to shine
    – to understand how everything fits together in this wider ecosystem. Perhaps
    an analyst doesn't necessarily need to understand all the transformations and
    how everything connects to each other, but an analytics engineer really does.
  sec: 1828
  time: '30:28'
  who: Nikola
- line: I think this focus on data modeling theory is much more important. In that
    way, it's slightly more like a theoretical role in many ways, which I think is
    often not really talked about. Often the focus is on the technical side, which
    it is, but I think it's really important to understand, as an analytics engineer,
    the different kinds of data modeling frameworks and what's possible. Whether having
    a wider table or a narrower table – in which case should you go for one versus
    the other? When should you choose a certain kind of incrementalization strategy
    and when not? So I think that's part of the role that is very specific. I guess
    it’s becoming more and more important, as there is so much more data that companies
    in general are collecting. By virtue of more companies, smaller companies, different
    kinds of companies, and the traditional big enterprises start using and collecting
    data and building up data departments, then, of course, this becomes more of a
    need.
  sec: 1828
  time: '30:28'
  who: Nikola
- header: Where can one learn about data modeling theory?
- line: About this data modeling theory that you mentioned, and selecting whether
    it should be a wide table or a narrow table – if I wanted to learn more about
    this, where would I go? What kind of resources do you have about this?
  sec: 2026
  time: '33:46'
  who: Alexey
- line: That is a good question. I really struggled a little bit with this, because
    there's really a lot of quite… I wouldn't even call it “advanced” stuff. But the
    textbooks that you can buy on data are very dry. [laughs] I'll just be honest.
  sec: 2041
  time: '34:01'
  who: Nikola
- line: Kimball and this kind of stuff, right?
  sec: 2057
  time: '34:17'
  who: Alexey
- line: Yeah, Kimball. There's loads of textbooks.
  sec: 2060
  time: '34:20'
  who: Nikola
- line: It’s something I studied at university but never actually saw this book outside
    of university.
  sec: 2061
  time: '34:21'
  who: Alexey
- line: Exactly. To be honest, I've given them a good shot and I found that I just
    learned by doing. I learned through talking to the people who were my mentors
    or seniors – who are experts and I just asked as many questions as I could. I
    was never afraid to just ask stupid questions (and repeat questions if I needed
    to) until it made sense.
  sec: 2067
  time: '34:27'
  who: Nikola
- line: Sometimes if I had the basic knowledge and had something that I wanted to
    understand, I would go and just research online. There are increasingly a lot
    of really good blog posts and newsletters that are available. I think increasingly
    there are more and more resources that are a lot more accessible to people who
    haven't necessarily studied computer science or data science or statistics or
    these sorts of subjects at university.
  sec: 2067
  time: '34:27'
  who: Nikola
- header: Going from Ancient Greek and Latin to understanding Data (Just-In-Time Learning)
- line: You didn't study that, right? Did you?
  sec: 2127
  time: '35:27'
  who: Alexey
- line: No, I studied classics, which are Latin and ancient Greek. [laughs]
  sec: 2130
  time: '35:30'
  who: Nikola
- line: That was your education?
  sec: 2136
  time: '35:36'
  who: Alexey
- line: That was my Bachelor's, yeah.
  sec: 2138
  time: '35:38'
  who: Nikola
- line: Interesting. So you speak Ancient Greek and Latin?
  sec: 2142
  time: '35:42'
  who: Alexey
- line: No… I can read it.
  sec: 2144
  time: '35:44'
  who: Nikola
- line: Interesting. Okay. This just made our interview even more interesting. [both
    laugh] How do you go from studying Ancient Greek and Latin to being an analytics
    engineer? You learn basically everything you needed yourself, right?
  sec: 2148
  time: '35:48'
  who: Alexey
- line: Yeah, exactly. Um…
  sec: 2166
  time: '36:06'
  who: Nikola
- line: By “yourself” I mean not as a part of any official curriculum.
  sec: 2169
  time: '36:09'
  who: Alexey
- line: Yep. To be honest, I did this SQL course on Udemy that cost me 12 euros. And
    it was great. It was really, really good. It was quite long. I can't remember
    exactly, but I think it was just called The Complete Guide to SQL and it's run
    by this American dude called Colt Steele. It's just a very strange name. He's
    got loads of good Python courses as well that I did. I just did that in my spare
    time. And to be honest, it was really great that it cost me all of 12 euros and
    I haven't done a single other SQL course since.
  sec: 2174
  time: '36:14'
  who: Nikola
- line: Sometimes I do think, “Oh, should I go and pay for one of these fancy courses
    in data science or something because it's nice to have structure and whatnot.”
    But then I'm like, “Ah. If I just motivated myself, I could do it.” [laughs] There's
    so much stuff online. But it's just a case of me being quite lucky to find a good
    course right away. I think there are some not very good courses out there. It's
    a little bit of hit and miss. One thing that's really great about software engineering
    in general and computer science is that if you don't have a lot of resources,
    you can really teach yourself. There are a lot of resources online.
  sec: 2174
  time: '36:14'
  who: Nikola
- line: At the same time, as I said, practicing is really the thing that makes the
    difference and I was very lucky that I was already at a company where I knew the
    domain very well, the business model very well, the KPIs. I kind of had all of
    that already covered and could just focus on developing the SQL skills and data
    modeling, etc. I can imagine that someone who is maybe approaching this as a career
    change and maybe taking some time out to do it – it may be a little bit more difficult
    because you don't have that context of a specific business or a specific problem
    that you can hold in your mind as you think about these problems and have an example
    that you can apply the theory to.
  sec: 2174
  time: '36:14'
  who: Nikola
- line: Yeah, there is a thing called “just in time learning,” and I think you took
    this to the extreme. So without any formal education in computer science or analytics,
    you just focused on a specific problem, which in your case was marketing and then
    you were like “Okay, how do I set up Looker to do this thing?” By the way, are
    the tasks that you do now still more or less related to marketing? You mentioned
    RFM analysis. I think it's still somewhat related, right?
  sec: 2307
  time: '38:27'
  who: Alexey
- line: Not really, to be honest. No. At the moment, I'm really working very closely
    with the product team. We are focusing on growing, acquiring more users, retaining
    more users – which are all of course interlinked goals of the marketing team.
    It's not directly relevant, but my direct stakeholders are the product managers.
  sec: 2338
  time: '38:58'
  who: Nikola
- header: The importance of having domain knowledge to analytics engineering
- line: Okay. So I guess your background in marketing really helped you, right?
  sec: 2370
  time: '39:30'
  who: Alexey
- line: Yeah, it really did. I’ve noticed how just in everyday work, I definitely
    see an edge that I have because I'm very comfortable with things like a marketing
    funnel and a conversion funnel or web acquisition funnel. For example, a product
    manager might be focusing specifically on a part of the funnel or a whole funnel
    as part of the user journey and as a marketing person, you think about the user
    journey all the time. What are the touch points of the user? How do they feel
    at this moment? What are they thinking at this moment? What have they done? Where
    have they come from? You have this quite close empathy with the user, and specifically
    the journey.
  sec: 2376
  time: '39:36'
  who: Nikola
- line: At the same time, your goals in marketing are to constantly optimize and grow
    and get more users or higher retention or more signups or whatever it might be.
    So you have this growth mindset that I think is very useful when you come to advising
    people from a data point of view because you can ask the question, “Yes, you've
    got some good feedback from the users on this feature. But, ultimately, the top
    line hasn't moved at all. We did this because we wanted to grow (whatever this
    KPI is).” It definitely does help, largely in the realm of understanding the user
    journey. It means that you can really hold this user perspective in your head,
    but also the data perspective together with it, and advise with those two things
    in your head.
  sec: 2376
  time: '39:36'
  who: Nikola
- header: Suggestion for those wishing to transition into analytics engineering
- line: If somebody wants to follow your journey – so somebody who's working in marketing
    (or not necessarily in marketing, but they really want to go into data and start
    doing analytics engineering) and they are experts in their domain – what would
    you suggest for them to do?
  sec: 2491
  time: '41:31'
  who: Alexey
- line: Firstly, I would say [chuckles] Excel is your best friend. Excel is great,
    ultimately. [laughs] I know everyone hates it, but it really doesn't get the credit
    it deserves. I still have people in the company who really should and don't know
    how to make a pivot table. They are quite annoying to make in Excel. The most
    difficult pivot table you will make will be in Excel. If you can do it there and
    be comfortable (understand what's happening with columns and rows) that’s the
    first place to go. So be really, really comfortable with Excel, play around with
    functions, pivot tables, and just explore. Look at different ways of trying to
    take a dataset that you feel comfortable with – it might just be something really
    simple like daily signups by country – and just, in Excel, start playing around
    with that and asking questions.
  sec: 2510
  time: '41:50'
  who: Nikola
- line: Then, of course, SQL is the most important thing. Learn SQL, try and find
    some datasets online that you can play around with and practice SQL. That's really,
    really useful. But ultimately, where I found a little bit of a gap in the self-learning
    was between the online SQL resources and finding advanced SQL queries that made
    sense – that weren't written by someone on the other side of the world about a
    company that had no connection to, didn't learn from the business models and was
    written in a way that, for example, wasn't the style that was going to be written
    in my team. It ended up just being a little bit confusing and extra work to try
    and understand. So if there's a way to access some of the SQL code that the BI
    team are using – maybe you can ask them to share a couple of SQL queries they
    use to make the main tables – that's definitely something to do.
  sec: 2510
  time: '41:50'
  who: Nikola
- line: If your company is using Looker, that's great. That's amazing – to get familiar
    with that. Really, just start building, building, building dashboards. Explore
    it. Become really comfortable with filtering, pivoting – those sorts of things.
    There are a lot of resources from Looker online as well. I think from Tableau
    as well, or whatever visualization tool you're using – it doesn't really matter.
    Just become comfortable with the basic features of those. Those would be the main
    things, I think. Then go from there. Find someone who can be your, if not mentor,
    then your champion – an ally, I guess, in the data team. Ask them, “What do I
    need to do? What skills are still missing? How do I do them? Do you think it's
    possible?” Ask them what they would recommend if you're in an existing company
    and you're looking to move to that role. I think that would be my suggestions.
  sec: 2510
  time: '41:50'
  who: Nikola
- header: The importance of having a mentor when transitioning
- line: How important do you think it is to have a mentor or champion in this journey?
    For you, from what I understood, it was quite important. It was crucial. That
    person was a marketing analyst, if I remember correctly, that actually helped
    you. She told you what you should do, what kind of things you should focus on,
    and then she also was helpful for you to actually transition to the team. Right?
  sec: 2709
  time: '45:09'
  who: Alexey
- line: Exactly. She was the BI analyst (the data analyst) – the only one that we
    had at the time. Actually, sorry we already had two people in the data team and
    she was one of them. For me, it was very useful and important. To be honest, though,
    it depends on the company, your position in the company, how comfortable you feel,
    what level of power (so to speak) you have in the company.
  sec: 2734
  time: '45:34'
  who: Nikola
- line: Also, for me, as a woman, I think transitioning from marketing into a more
    technical role (I was going to move to the engineering department, there was a
    meeting) I felt an element of imposter syndrome. I thought, “Oh, what am I doing?
    Can I really do this?” I think it really helped me to have another female, basically,
    mentor to champion me and encourage me and say, “Yeah, you can do this. Definitely,
    you can do this. You just need to do this, this and that. You can definitely do
    that. Once you've done that, we can find a way.” So it depends. I think if you
    have a lot of motivation and you're very clear on what you want, and you're confident,
    then I don't think it's necessarily needed.
  sec: 2734
  time: '45:34'
  who: Nikola
- line: But particularly for minorities, there's a lot of support groups outside of
    work like, PyLadies and lots of different various support groups for minorities
    in tech, which are great to be inspired by. But I think having that one person
    in your company who you can relate to can be really helpful just in terms of building
    up your own confidence. It's definitely something that helped me also to not just
    transition into the team but, once I was in the team, to accelerate quite quickly.
  sec: 2734
  time: '45:34'
  who: Nikola
- line: Yes, I was junior when I joined, but my career path up to being a mid-level
    analyst and now intern team lead was a lot quicker because I had to fight and
    be like, “Well, I have been doing analytics work for years before. I haven't actually
    picked all of this up from scratch.” So having the confidence to make that clear
    and argue it – it was really helpful having someone to champion me. I would recommend
    finding one person in your company who can be that for you.
  sec: 2734
  time: '45:34'
  who: Nikola
- line: Did you take part in any of these support groups that you mentioned like PyLadies?
    Or did you have mentors or people who you constantly talked to outside of the
    company? Or was it mostly that person and the rest of the team that you talked
    to in order to learn?
  sec: 2904
  time: '48:24'
  who: Alexey
- line: In my case, it was mainly my two teammates who were the BI team when I joined.
    They were incredible. So supportive. They really encouraged me a lot and helped
    me hugely. They were very excited for me to join the team and made me feel very
    welcome like I deserved to be there. This was very useful because at times, I
    was like, “Oh, what am I doing here? This is too hard.” But in terms of external
    support, not really, to be honest. I have two very close friends who worked in
    data, and it was nice to talk to them and have their advice as well – to have
    different perspectives from different companies.
  sec: 2925
  time: '48:45'
  who: Nikola
- line: Particularly as someone who's been at a company for a very long time, I definitely
    feel the need to speak to people in different places and see like, “Oh, is it
    also like this where you are? Is this a specific issue that only we're facing
    or is this a general thing?” Having that perspective has also been really useful
    in order to just benchmark certain issues that you come across. [chuckles] I think
    having a few more external mentors or support would be great. In the coming year,
    I'll probably look for a mentor just to help with kicking off the next phase of
    development.
  sec: 2925
  time: '48:45'
  who: Nikola
- header: Finding a mentor
- line: Do you have any ideas where you can look for these mentors? Would it be conferences,
    meetup groups or someplace online?
  sec: 3023
  time: '50:23'
  who: Alexey
- line: Probably a combination of LinkedIn, asking the networks of people that I know
    if they have anyone they recommend. Meetups as well. I think that's probably the
    best way to go.
  sec: 3032
  time: '50:32'
  who: Nikola
- line: Is there an analytics engineering meetup in Berlin?
  sec: 3050
  time: '50:50'
  who: Alexey
- line: I'm not sure. There's definitely a Snowplow meetup that I think has just started
    up again (or about to) In terms of the engineering, I'm not sure, to be honest.
    I know that there are some data meetups. I'm not sure if that's specifically analytics
    engineering. I have kept an eye open on the DBT Slack group, which is extensive
    and actually great. They have some city-specific groups and Berlin has yet to
    make its appearance. Perhaps in the future, there might be a DBT Berlin.
  sec: 3056
  time: '50:56'
  who: Nikola
- line: Yeah, I think there should be. One of the people who helped me with the questions
    is Victoria. Victoria was a guest on this podcast over a year ago and now she
    works at DBT. I think she is or will be organizing something soon. Maybe she will
    tell us about that. I see that it's almost time to finish. I wanted to ask you
    one last thing.
  sec: 3102
  time: '51:42'
  who: Alexey
- header: Helpful newsletters and blogs
- line: You mentioned that you are subscribed to some newsletters. There are good
    blog posts, good newsletters, and these newsletters are quite useful for you.
    What kind of newsletters are you subscribed to? If I want to keep an eye on what's
    happening in this area, what kind of newsletters should I subscribe to?
  sec: 3130
  time: '52:10'
  who: Alexey
- line: That's a good question. There's one I'm subscribed to (an analytics engineering
    one) that I think is called “The Roundup” or something. Analytics Engineering
    Roundup. It might be the DBT newsletter, actually. There's another one that I
    just subscribed to like a week or two ago. It’s called Lenny's Newsletter.
  sec: 3152
  time: '52:32'
  who: Nikola
- line: Lenny's Newsletter. Lenny's the name of the person.
  sec: 3184
  time: '53:04'
  who: Alexey
- line: I've only just subscribed to it recently. I think it was slightly more product
    analytics focused. Then there is a blog that I'm sure most of your readers will
    know about. I've just forgotten the name of it. It's called something like Profoundly
    Optimistic or something… Locally Optimistic, yeah! Yeah that one.
  sec: 3189
  time: '53:09'
  who: Nikola
- line: Yeah. They have a guest coming in as well.
  sec: 3218
  time: '53:38'
  who: Alexey
- line: From time to time, I'll check that one.
  sec: 3221
  time: '53:41'
  who: Nikola
- header: Finding Nikola online
- line: Profoundly Optimistic is also a good name. [both laugh] If somebody has questions
    for you, how can they find you? Is it LinkedIn or are there some other ways to
    contact you?
  sec: 3226
  time: '53:46'
  who: Alexey
- line: Yeah, LinkedIn would be best. They can just message me directly there.
  sec: 3244
  time: '54:04'
  who: Nikola
- line: Okay, Niki. Thank you very much. Thanks for joining us today. It's been a
    while since we started this conversation. So finally, we had this interview. Thanks
    a lot for joining us today, for telling us about your journey, for sharing all
    the experience and expertise you have. And thanks, everyone, also for joining
    us, for being active here. Have a great rest of the week.
  sec: 3248
  time: '54:08'
  who: Alexey
- line: Thank you for having me.
  sec: 3274
  time: '54:34'
  who: Nikola
description: 'Discover DBT, SQL & data modeling tactics for pivoting into analytics
  engineering: learn migration, tooling, A/B testing, and a career playbook to get
  hired.'
---

Links:

* [Nikola's LinkedIn account](https://www.linkedin.com/in/nikola-maksimovic-40188183/){:target="_blank"}