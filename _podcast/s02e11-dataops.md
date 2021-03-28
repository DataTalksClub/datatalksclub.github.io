---
title: "DataOps 101"
short: "DataOps 101"
guests: [larsalbertsson]

image: images/podcast/s02e11-dataops.jpg

season: 2
episode: 11

ids:
  youtube: vyF3yGsF6UY
  anchor: DataOps-101---Lars-Albertsson-ethsp1

links:
  youtube: https://www.youtube.com/watch?v=vyF3yGsF6UY
  anchor: https://anchor.fm/datatalksclub/episodes/DataOps-101---Lars-Albertsson-ethsp1
  spotify: https://open.spotify.com/episode/5c2m4FVq4KPCfSXndCAzNd
  apple: https://podcasts.apple.com/us/podcast/dataops-101-lars-albertsson/id1541710331?i=1000514542438

transcript:
- line: "This week, we'll talk about data Ops \u2014 what is this and how is it different\
    \ from any *ops that we have out there. We have a special guest today \u2014 Lars.\
    \ Lars is the founder Scling, which is a data engineering startup based in Stockholm.\
    \ Lars frequently speaks on data related topics and we tried to get him on this\
    \ podcast to talk about data ops. Luckily, he agreed. Welcome, Lars. Thanks for\
    \ joining us today."
  sec: 159
  time: '2:39'
  who: Alexey
- line: Thank you. It's a pleasure to be here.
  sec: 206
  time: '3:26'
  who: Lars
- header: "Lars\u2019 career"
- line: Before we go into our main topic of DataOps, let's start with your background.
    Can you briefly tell us about your career journey so far?
  sec: 208
  time: '3:28'
  who: Alexey
- line: "Yes, I'll try to not dwell for too long. I graduated from the Royal Institute\
    \ of Technology in 97. I was an academic for a long time in theory of distributed\
    \ systems. When distributed systems became popular in industry, I got a call from\
    \ a Google recruiter. I joined Google in 2007 and as one of the first engineers\
    \ in Stockholm, and we built Google's first generation of video conferencing systems.\
    \ That was a milestone in my career because it gave a glimpse into the future.\
    \ Google was the only company in 2007 to do what we today called \u201CBig Data\u201D\
    . It immediately became apparent to me how much value you could extract from your\
    \ data if you have the skills and the infrastructure and the competence. Ever\
    \ since my career gravitated towards data. At Google, I was working on engineering\
    \ productivity. We did some productivity improvements that are still beyond what\
    \ is state of practice and in most companies. These two things have essentially\
    \ covered my career, a focus on efficiency and obsession on efficiency and then\
    \ on data."
  sec: 218
  time: '3:38'
  who: Lars
- line: Fast forward a couple of years, I managed to join Spotify here in Stockholm.
    I realized they were doing interesting things and had a Hadoop cluster. I was
    part of the core data infrastructure team. We did it back in 2013, a transformation
    to what today has the name of DataOps, but we didn't yet have a name at the time.
  who: Lars
- line: "Fast forward again, a couple of years, I've been freelancing for a number\
    \ of years, trying to spread the superpowers of data and machine learning and\
    \ AI to other companies outside the little tech elite that currently are running\
    \ ahead of everybody else. I did that as a self-employed consultant for a while\
    \ and embedded into companies \u2014 everything from big banks, to startups, to\
    \ retail, to news. But I was ultimately limited in how there's only so much that\
    \ you can do to change these companies. Usually I go in there and try to build\
    \ technology, but technology is not the limiting factor. I\u2019ve been very limited\
    \ in what I could achieve as a lone consultant."
  who: Lars
- line: "A couple of years ago, we flip this around and say, \u201COkay, the key is\
    \ the ways of working and the workflows and how you work with data, not the technology.\u201D\
    \ We're now trying out a different collaboration paradigm where we say \u201C\
    You have data to our customers, you have data that has potential, that has value.\
    \ How about we together with you figure out what the value is in this data? And\
    \ try to extract value from it through simple things reporting analytics, or all\
    \ the way to machine learning, but we do it. We, together with you, because you\
    \ are the domain experts, but we handle how we work, the technology stack and\
    \ the operations and so forth.\u201D Thereby, we circumvent the need to change\
    \ how our customers work. Instead, extract the value from the data and then returning\
    \ valuable data or data assets to customers.\u201D"
  who: Lars
- line: So, you've been self-employed for five, six years?
  sec: 462
  time: '7:42'
  who: Alexey
- line: For something that.
  sec: 468
  time: '7:48'
  who: Lars
- header: Doing DataOps before it existed
- line: "You said, you started with DataOps, even before it became a thing \u2014\
    \ in 2013. How was it called there? How did you come up with this?"
  sec: 472
  time: '7:52'
  who: Alexey
- line: "We didn't give it a name. The name was coined the year after by someone from\
    \ IBM. It became a thing in 2018, or 2017. But roll back to 2013. There were just\
    \ a few teams that were intensively working with data at Spotify at the time.\
    \ I was in the core team, and we were doing the infrastructure on the platform,\
    \ but also handling some of the main pipelines \u2014 what songs have been played,\
    \ and what uses that we have, and so forth. Then there were a couple of power\
    \ user teams like recommendations. We were getting swamped with requests from\
    \ analytics and from various other sources. \u201CHey, can you implement this\
    \ X, Y, and Z for us?\u201D We were, in a way, in an internal consultant team\
    \ as well. This was no longer feasible. Everybody was dissatisfied with us for\
    \ having so little bandwidth."
  sec: 493
  time: '8:13'
  who: Lars
- line: "So, in a Spotify manner, we said, the team should be autonomous, There's\
    \ a very autonomous culture at Spotify. We should enable them instead of being\
    \ dependent on us. We flipped that situation around and said, \u201COkay, let's\
    \ build the tooling and the workflows to support everybody to go in and build\
    \ their own data flows on the data platform,\u201D \u2014 the Hadoop based data\
    \ platform that we had. The goal was to enable everyone to be able to deploy a\
    \ pipeline in production in less than a day. Then fix pipelines, if there was\
    \ a problem, in less than an hour. It took us a few months to get everything in\
    \ place. One of the factors of success, I believe, is that we embedded with the\
    \ teams that were the early adopters. We worked very tightly with them to figure\
    \ out where we were missing things. Shortly thereafter, the use of data pipeline\
    \ spread throughout the company and the Hadoop cluster exploded in size. Nowadays,\
    \ they are producing hundreds of 1000s of new data sets per day and building data\
    \ pipelines using data is an obvious thing for every developer team in the company."
  who: Lars
- line: Was it around the time when Luigi appeared?
  sec: 648
  time: '10:48'
  who: Alexey
- line: Luigi dates back to 2010, 2011. That was our workhorse, at the time. It still
    is at Spotify. We can go back and come back to Luigi later.
  sec: 652
  time: '10:52'
  who: Lars
- line: "What I heard was \u2014 you were working on a data platform, but were swamped\
    \ with requests, everybody wanted you to implement something. What you did, instead,\
    \ you created a self-service platform. Other teams could implement whatever they\
    \ needed, whatever data transformation things they want to do. You enabled them\
    \ to implement that, and you focused on building the self-service thing. So, others\
    \ could move faster without you implementing things."
  sec: 668
  time: '11:08'
  who: Alexey
- line: Exactly.
  sec: 708
  time: '11:48'
  who: Lars
- header: "What is DataOps? (it\u2019s about people!)"
- line: Is this why you said this is the core of DataOps? Or, what is DataOps?
  sec: 710
  time: '11:50'
  who: Alexey
- line: "Well, what is data ops? That's a good question. You can look at it from a\
    \ few angles. One is the enablement, which was the angle that you brought up now.\
    \ Enable everybody to be self-sufficient. There's a parallel here today to DevOps\
    \ \u2014 instead of having developers throw things over the wall to operations,\
    \ you integrate the activities so that people are enabled to run their own things.\
    \ There is also the workflows and the tooling with continuous deployment. I believe\
    \ that was one of the first continuous deployments at scale in Europe. At least\
    \ on a data platform."
  sec: 717
  time: '11:57'
  who: Lars
- line: "But I would highlight another aspect \u2014 the people aspect. If I can go\
    \ out in the tangent here, I do more philosophical and historical view on this.\
    \ If you look back 50 years from now. The waterfall paper came out by Winston\
    \ Royce and he said he looked at software engineering and he said, this is what\
    \ seems to be happening. He just observed and said that there seems to be phases\
    \ of requirements, then design, then coding, then testing and deployment or operations.\
    \ These are done by different people and they're done in that order. This made\
    \ sense from a civil engineering point of view. But he said it doesn't seem to\
    \ make sense from a software engineering point of view. But people disregarded\
    \ his comments and said \u201CYes, that's how we do it. We now have a methodology\
    \ and let's call that \u2018waterfall\u2019\u201D."
  who: Lars
- line: "That was dominant for a long time, and eventually extreme programming popped\
    \ up and said \u2014 It doesn't seem to be efficient. How about we mix the activities\
    \ of development and quality assurance and do that in an integrated way. Mix these\
    \ two different skills and different people working together towards the same\
    \ goal. Instead of having different goals where the developers throw something\
    \ over the wall, and the quality assurance, trying to prevent the developers from\
    \ doing bad things, with contradictory goals and alignment. Instead, we sit these\
    \ people together, have the same alignment. Nowadays, that's obvious \u2014 that's\
    \ much more efficient and those types of tests formations have appeared ever since."
  who: Lars
- line: Agile is not a type of such transformation, where you take the design and
    the requirements and you muddle that up with development, so that it becomes iterative.
    You same people do it and try to figure out what the requirements are along the
    path.
  who: Lars
- line: "DataOps is yet another of that evolution of mixing up different types of\
    \ people and different types of competencies. Not only development, equality,\
    \ assurance and operations, but also data modelling and data skills and analytics\
    \ into the same melting pot. All are aligned towards the same goal. That is the\
    \ key. This alignment has become obvious for QA, they used to be a blocking thing.\
    \ And operations used to be a blocking thing that said \u201CNo\u201D."
  who: Lars
- line: "If we look at the disciplines that still have this blocking thing \u2014\
    \ security, for example \u2014 where you have lots of people that say \u201Cno\u201D\
    , and see this as their goal in life or in the company, there's still so much\
    \ friction. So, DataOps is a way to remove that friction and get people aligned\
    \ towards the same goal. I think that's the important part. It's the people part."
  who: Lars
- line: "So, the first one is enablement. \u041Dow enable others to do self-service\
    \ and build data pipelines. Then the actual data pipelines, so you have this workflow\
    \ component, you can design and build the workflow, when one thing depends on\
    \ the other, you can help that. Then the final one \u2014 the most important one\
    \ \u2014 is the people component where everyone works together on the same goal.\
    \ It's not a waterfall, where you throw something over the wall and hope they\
    \ will take care of everything. Instead, you work together in one team \u2014\
    \ developers, analysts, data engineers, everyone work together on achieving the\
    \ same goal."
  sec: 954
  time: '15:54'
  who: Alexey
- header: Data platform
- line: Exactly. There is a key technical or process component here that needs to
    be in place in order to do the enablement. That is to switch from the traditional
    database oriented, mutable data storages. If you look back in time, we used to
    have databases. All the data that we had was in databases. In databases, you have
    mutable records, where you can go in and change your address, for example. We
    have mutable collections of records. So, every day the user list is different
    and that only scales to a certain degree. We all know the limitations of the monolith
    and because too many people cannot go in there at the same time. So, you have
    few teams that are able to work there.
  sec: 1002
  time: '16:42'
  who: Lars
- line: "We have the microservices split, where everybody has their own database,\
    \ but that spreads out all the data. So, we cannot use data easily from one end\
    \ of the company to another. The solution here has been \u2014 and now we're getting\
    \ into that what you mentioned before a data platform \u2014 to gather all of\
    \ the data that you have within the company into a data platform. That's the key\
    \ technology or workflow component that you need to get in place."
  who: Lars
- line: "Inside the data platform, you have a couple of principles in order for it\
    \ to make it work at scale. When I say \u201Cscale\u201D, I don't necessarily\
    \ mean data scaling from terabytes to petabytes, but a human scale from one team,\
    \ to 10 teams, to 100 teams. Also to scale in terms of business logic, complexity,\
    \ they can do more and more complex things and achieve more things. The key principles\
    \ for achieving this scale is essentially what can be described as \u201Cfunctional\
    \ architecture\u201D principles."
  who: Lars
- line: You take the principles for functional programming and apply them on an architectural
    level. All the data you have should be immutable. You strive to make it immutable,
    as much as you can. Because immutable things you can freely share. If I dump a
    data set in a file and say, here's the data set, it will never change, then I
    don't need to coordinate with other teams that might use it.
  who: Lars
- line: But In order to do something intelligent with it, I need to process it. If
    I can't mutate it, I need to transform it into a new data set. So instead of mutating
    things in databases with SQL queries, we ended up with these pipelines of steps
    of transformations on immutable data sets and purely functional transformations
    without any external input and so forth. These functional principles are critical
    to data processing and extracting value from data, and scale to large volumes
    of value.
  who: Lars
- line: "This data platform is the key technology enabler for an organization to implement\
    \ DataOps. We need to scale in terms of people \u2014 to process all the data\
    \ we have. Immutability helps with that. I just had a chat today, about ETL processes,\
    \  when you have some data, and you transform this data with a sequence of steps.\
    \ Then the problem is that when you run this data on different times, you have\
    \ different results. Let's say you can run it at six o'clock or 12 o'clock and\
    \ the problem is when you run it, and the results are different. This is because\
    \ your data is not immutable. You can change your rows, you can change your database\
    \ and when you run this ETL process at different times, result is different. Data\
    \ platform tries to solve with this immutability."
  sec: 1212
  time: '20:12'
  who: Alexey
- header: Data warehouse and data lake
- line: "Exactly. The situation you described, that was the case in the data warehouse\
    \ days when you would do these things for reporting purposes. In data warehouses,\
    \ each of the data sets was represented as mutable data tables. As new data was\
    \ arriving, they would change it a bit. So, you could not reproduce the steps.\
    \ In a purely built data platform with these data pipelines and data factories,\
    \ then you will have \u2014 in theory \u2014 reproducibility."
  sec: 1289
  time: '21:29'
  who: Lars
- line: "But then we have other ways to handle late incoming data, for example. The\
    \ world is still in training on this one. Because it's very easy to fall back\
    \ into the old mutable practices. And we actively see some of the main actors\
    \ in the scene falling back there. For example, we've seen Databricks has pushed\
    \ something called the \u201Clake house\u201D, where you can mutate datasets.\
    \ You can look at this from different angles. I sometimes say that this is an\
    \ anti-pattern. This is something that you really should avoid. On the other hand,\
    \ you can see it as a gateway drug to those that have the existing ETL flows in\
    \ their data warehouse. They can now easily move without changing their workflows\
    \ to a data lake and not have to redo the logic and the workflow logic to handle\
    \ the immutability."
  who: Lars
- line: "Maybe we can take a step back \u2014 what is the data lake?"
  sec: 1396
  time: '23:16'
  who: Alexey
- line: "When I described what data lake is to one of my clients, my clients said\
    \ \u2014 so this buzzword that everybody keeps talking about is just the big disk?\
    \ I said yes, sorry to disappoint you, but it is a big disk. It's just a bunch\
    \ of files. They became popular. When Hadoop came out, it was suddenly economically\
    \ feasible to store all raw data from your web applications forever. But you could\
    \ do it with older NFS server technology. So, it's just a big file system that\
    \ is shared between the nodes that do the data processing."
  sec: 1409
  time: '23:29'
  who: Lars
- line: HDFS or these days cloud-based storages like S3 or Google Storage?
  sec: 1451
  time: '24:11'
  who: Alexey
- line: Exactly. Now Hadoop is obsolete and we use object stores in the cloud.
  sec: 1461
  time: '24:21'
  who: Lars
- line: "So ever data you have \u2014 you dump into S3 \u2014 and just call it the\
    \ data lake?"
  sec: 1472
  time: '24:32'
  who: Alexey
- line: "Yes. From a glass \u2014 yes. But this will degenerate in \u201Cdata swamp\u201D\
    \ and if you do it without any control or governance. In order to get value from\
    \ it, you need to have structure in there. In order to be compliant, you need\
    \ to have some kind of governance. A part of this \u2014 this big data and data\
    \ platform philosophy \u2014 is that you store raw data. You store the data that\
    \ has been generated in source systems by events and mobile apps or clicks on\
    \ your web page or dumps of your current database, and so forth. You store those\
    \ in raw format without processing them whatsoever in your data lake. In what\
    \ I usually call \u201Cthe cold pond\u201D \u2014 upon this the lingo \u2014 for\
    \ parts of the data lake. If it's not personal data, you store that forever. If\
    \ it is personal data, you have to separate the personal data from the non-personal\
    \ data so that you can discover the personal data in order to be compliant with\
    \ GDPR."
  sec: 1478
  time: '24:38'
  who: Lars
- line: "We have this data lake. Then a data platform is a tool that enables us to\
    \ process the data \u2014 the raw data. But for an analyst, the raw data is not\
    \ super useful. They need to be able to transform it, aggregate and whatnot and\
    \ this is where a data platform comes into place. This is like an enabler. Right?"
  sec: 1559
  time: '25:59'
  who: Alexey
- line: Exactly. The data platform is a wider thing that consists of a lake and also
    has processing capabilities. From a value perspective, the primary processing
    capabilities is batch processing. It enables you to build a series of batch processes
    that take one data set at a time or several and combine them and so forth and
    do refinements. Usually there's a series of steps where the first ones are cleaning,
    you remove the invalid records, you fix whatever you know is broken and then you
    decorate the record.
  sec: 1586
  time: '26:26'
  who: Lars
- line: 'At Spotify, we had songs that have been played and then we joined with the
    user so we know what product they were or what country they''re in. Then these
    pipelines fan out, these popular data sets are used for many purposes: for reporting
    purposes, for recommendation purposes, and so forth.'
  who: Lars
- line: "Then, step by step, for each use case, you have a series of refinements steps\
    \ where you do more and more. First, the domain and application specific things,\
    \ and then use case specific transformation steps. At the end of such a pipeline,\
    \ you arrive with some kind of refined data set \u2014 a recommendation index,\
    \ for example \u2014 of high value. They are built from the raw things of low\
    \ value, and then you take this high value dataset and you export it \u2014  or\
    \ egress it \u2014 to some kind of storage, where that is more suitable for serving\
    \ SQL or NoSQL database. Then it goes out to the data platform and\u2026"
  who: Lars
- header: Egress and ingress
- line: "Ingress \u2014 what does it exactly mean?"
  sec: 1702
  time: '28:22'
  who: Alexey
- line: So, Ingress is the processing of taking things into the platform, and egress
    is the process of taking things out of the platform. The platform itself is completely
    offline. It doesn't have any direct connections to the online world and that's
    important. Because when you are offline, you can accept high risk. You can move
    with higher speed, and with very little operational overhead. You don't need any
    staging environments, or development environments. You can do your tests in production.
    That speed translates to innovation capability.
  sec: 1707
  time: '28:27'
  who: Lars
- line: This is what enables other teams to do the self-service. An analyst who is
    not necessarily a Hadoop expert can just go there, write SQL queries. Then they
    get translated to, maybe presto, or hive or whatever. They just focus on SQL and
    then the platform takes care of executing this and having the data in the form
    they need. They don't need to care about all these things staging and all these
    things you mentioned.
  sec: 1749
  time: '29:09'
  who: Alexey
- line: Something like that. Yes, the data platforms are usually fairly technical.
    You need it for a team to work directly with a platform. You need a software engineering
    expertise and then depending on the maturity on the size of the company, you might
    have self-serve analytics capabilities for analysts to develop things right away.
    Or you could combine the analysts with engineering expertise. Then there's also
    usually some kind of data warehouse or data mars in a warehouse at a corner of
    the platform, which serves the purpose of exploratory analytics.
  sec: 1783
  time: '29:43'
  who: Lars
- header: Main components of the data platform and tools to implement it
- line: 'You touched a bit on maturity level, this is something which we should cover
    later. But first we can summarize what this data platform is. The main part of
    it is the data lake that stores the data. Everything is immutable. The only way
    we can produce something is by creating transformation steps. This is what we
    create with a processing component. We have these two: the data lake and the workflow
    engine. Is there something else that we have on the platform?'
  sec: 1834
  time: '30:34'
  who: Alexey
- line: There is very little technology that you actually need to have. You need storage
    for the lake. But that's just fine. It's that simple. When you egress, you need
    some kind of database storage, that has indexes as well. For most use cases, relational
    databases are fine.
  sec: 1878
  time: '31:18'
  who: Lars
- line: "Then you need compute. You need some way to perform these transformations.\
    \ There are scalable things like Spark and Flink. For most companies, horizontal\
    \ scalability is actually not necessary. You can get 12 terabyte memory machines\
    \ in the cloud these days and most data sets fit in one machine nowadays. These\
    \ tools tend to have languages or DSL \u2014 domain specific languages that are\
    \ highly suited for data processing. It's easier to take something like Spark\
    \ or Flink and express your data processing in that language, as opposed to chopping\
    \ up your own Java solution and do for loops."
  who: Lars
- line: "The only component that's really unique here is the workflow engine \u2014\
    \ or rather, the workflow orchestrator. That is a simple piece of technology.\
    \ But it's crucial, because it keeps you sane. It makes you weld a robust system\
    \ from fragile components. You define your dependencies between all of your transformations\
    \ in this workflow orchestrator. You say that for this particular recommendation,\
    \ we need the raw events on the web shop and we need the information about the\
    \ uses dumped on this particular day and so forth. You don't do processing inside\
    \ the orchestration engine, you rather do that in your Spark jobs or whatever\
    \ \u2014 on the outside. Then you schedule this to run every once in a while,\
    \ when new data arrives, or every hour or so. When it fails, it will need to try\
    \ again. Which means that if the data is late, or if you have a transient problem,\
    \ or if you have a bug, the workflow engine will try and repair it."
  who: Lars
- line: "It's like a build system for data. And that's one of the keys of data success\
    \ at Spotify. We nailed this with Luigi. We used to have Oozie that is shipped\
    \ with Hadoop and that's a terrible thing. Then we made something else that was\
    \ called a \u201Cbuilder\u201D and then we made a \u201Cbuilder 2\u201D and then\
    \ we made \u201CRambo\u201D. And finally, we made Luigi based on the learnings\
    \ that we have made and got this right. That's what kept us sane. I kept us able\
    \ to do these things at a very large scale. But Luigi is a very, very simple tool.\
    \ It has very little complexity and it's easy to adapt. But you need to get this\
    \ welding in place."
  who: Lars
- line: This only applies to batch processing, which I tend to focus on. Nowadays,
    stream processing is very popular as well. Many data platforms have a stream processing
    capability usually built around Kafka or some similar. There are pros and cons
    with batch and stream. Streaming is very fashionable these days, but it comes
    at a significantly higher cost of operations. Because it doesn't have a workflow
    orchestration that automatically repairs and heals the system. You need to keep
    things up and if things go down, you need to do much, much more operation. I tend
    to gravitate towards batch, because the time that I don't have to spend on operations
    I can spend on innovation.
  who: Lars
- line: You mentioned that for data platform, we have three components. We have the
    storage, we have compute, and we have a workflow engine. Are there data platforms
    that just work out of the box, you just buy them and you have it?
  sec: 2157
  time: '35:57'
  who: Alexey
- line: Yes and no. Usually people go to the cloud for these things and then they
    just pick the pieces. But all of these components are technically so simple, that
    it's easy to put them together. And you can get some help. If you go to the cloud,
    different vendors have different prepackaged things. Several of them are not particularly
    good to be honest, but there are a few that are useful.
  sec: 2189
  time: '36:29'
  who: Lars
- line: If you instead of Luigi use Airflow as your workflow orchestrator, it comes
    with more things, it has a wider scope. And it's more opinionated, which, if you're
    a power user like me, that becomes annoying. Because there are some things that
    it can't do. For beginners, that's usually a good thing, because it pushes you
    towards some reasonable patterns. But no, there are no fully prepackaged data
    platforms that I would recommend. On the other hand, once you obtain the skills,
    it's technically easy to put together.
  who: Lars
- line: If we talk about clouds, then for storage, we have this object stores, like
    S3 or Google. Then for compute, all the major cloud providers have their own tools.
    I guess for Google Cloud, this is Big Query. Can it be one of these things?
  sec: 2270
  time: '37:50'
  who: Alexey
- line: "Big Query is essentially a data warehouse. But yes, you can run jobs in Big\
    \ Query as well. For compute, plain virtual machines work fine. Nowadays, everything\
    \ is containerized. One of the managed Kubernetes clusters is perfectly fine \u2014\
    \ or things Fargate or GK Autopilot where you just run a container. That's perfectly\
    \ fine as well, you just need to be able to run a batch or a cron job."
  sec: 2294
  time: '38:14'
  who: Lars
- line: If you can then express your job in terms of SQL, then you can use Big Query,
    or Athena. But then you lose some flexibility. Also, most of the clouds have a
    managed Spark that you can just use. For workflow orchestration we have Luigi,
    Airflow. And I know now that we have more and more such tools, they are not written
    in Python and use YAML. Do you use any of them?
  sec: 2326
  time: '38:46'
  who: Alexey
- line: I am aware of Daxter and Prefect. I think they're both in Python. Nowadays,
    fortunately, we've left the day when we need XML workflow orchestration. Since
    people tend to target data scientists as well, Python is the natural choice.
  sec: 2372
  time: '39:32'
  who: Lars
- header: DataOps books
- line: We already have a couple of questions. The first one is regarding functional
    programming principles applied to architecture. Is there any good literature that
    you can recommend on building these functional architectures?
  sec: 2397
  time: '39:57'
  who: Alexey
- line: "There are a couple of tangential books. I think the original good book that\
    \ described these functional transforms is Nathan Marz, who made Storm. Once upon\
    \ a time, he wrote a book called \u201CBig Data\u201D \u2014 back in 2012-2013\
    \ \u2014 that defines the lambda architecture. Lambda architecture actually has\
    \ two parts. Now just one is remembered, and that's the part where you have dual\
    \ streaming and batch pipelines, and combine them. But the other part is more\
    \ important. That's where \u2014 what I explained earlier \u2014 you save the\
    \ raw datasets, and then you do these transformations and that was formulated\
    \ in the book, and in a blog post at the same time. There's a fresher book, by\
    \ Harvinder Atwal, which is called \u201CPractical DataOps\u201D. That has a much\
    \ wider scope, and is not so focused on these functional transforms. Then the\
    \ third resource that I want to throw out is that we have a data engineering reading\
    \ lists on scling.com/reading-list, with lots of links to books, presentations,\
    \ YouTube videos, and so forth."
  sec: 2418
  time: '40:18'
  who: Lars
- header: Batch vs Streaming
- line: I remember going through this page to prepare for this podcast. Thanks a lot
    for putting this together, I will make sure to include the link in the description.
    We have another question. You already touched a bit on batch vs streaming. We
    have a question related to that. As far as batch vs streaming goes, what are your
    thoughts on data latency? How frequent is too frequent for batch jobs?
  sec: 2513
  time: '41:53'
  who: Alexey
- line: "There\u2019s a trade off. With streaming, you can process it more or less\
    \ right away. Actually, let's split it into three-time windows here. If we're\
    \ now talking about the latest \u2014 from new interesting data coming in, to\
    \ your process reacting on it and serving something back to the user. The shortest\
    \ latency is when you have direct interaction. When you have a user that expects\
    \ something within the order of 100 milliseconds, streaming is too slow for that.\
    \ Then it has to be in memory in your server in order to get the hang of this\
    \ completely interactive experience."
  sec: 2549
  time: '42:29'
  who: Lars
- line: "Then you have batch, where things can be really slow, like reporting, or\
    \ you're making analytics or business insights. You can wait for an hour and that's\
    \ fine. Then you have streaming. It takes care of the window in-between. Then\
    \ the question is \u2014 how big is that window. You can't get it down to 10s\
    \ or hundreds of milliseconds: streaming involves hops between multiple machines,\
    \ and also some internal batching in order to make it efficient. There are cases\
    \ where that might be interesting. For example, fraud detection is one typical\
    \ example where, in a few seconds, it will be great if you figured out that this\
    \ credit transaction was fraudulent. Batch cannot go down to a few seconds, but\
    \ it can easily go down to a couple of minutes. I've been running batch processes\
    \ with one-two minute latencies. I think that we can \u2014 with the current technology\
    \ \u2014 squeeze the batch latency down to 10 seconds. This means that the window\
    \ where you'd really need to do streaming is small and there are a few use cases\
    \ in that particular window. So, instead of developing a complex streaming technology,\
    \ we tried to push the latency of batches. Because then you have this workflow\
    \ orchestration and the very forgiving environment, where we can operate with\
    \ an accepted high risk, but be able to recover. Nevertheless, I don't know if\
    \ that answered the question."
  who: Lars
- line: I think it does. We have a related question. In your opinion, what is the
    boundary between micro-batching and streaming?
  sec: 2711
  time: '45:11'
  who: Alexey
- line: "The important boundary here is not what the technology does. For example,\
    \ if you go to Spark streaming, they have this micro batching thing. But from\
    \ a programmer perspective, it's a streaming experience. Whereas if you go to\
    \ batch and you have the workflow orchestration. As a programmer, you explicitly\
    \ say that this minute of events is one batch, or these 10 seconds of events is\
    \ another batch. Then you explicitly define the dependencies between these batches\
    \ and say, \u201CI'm now going to take six of these 10 second batches and I'm\
    \ going to make a minute batch out of them and then I'm going to do an average\
    \ over five of these\u201D and so forth. That explicit dependency management is\
    \ really the key difference between streaming and batch. Because once you have\
    \ that, then you can have these forgiving environments in the data factories that\
    \ automatically heal. But if you're in the streaming mode, then your dependencies\
    \ are implicit. Then you get different results depending on how two different\
    \ streams are synchronized in matching time. If you do click-through rate analysis,\
    \ but one stream is late, you will get the different results from both streams.\
    \ Whereas if you have the dependency management in place, the result is entirely\
    \ predictable. That's the key difference."
  sec: 2719
  time: '45:19'
  who: Lars
- header: Maturity levels
- line: Makes sense. Thank you. I also wanted to talk about maturity levels, and you
    briefly touched on them. What are the maturity levels of an organization? When
    an organization is ready for DataOps? And what are the different levels of readiness?
  sec: 2812
  time: '46:52'
  who: Alexey
- line: "Everybody's ready for DataOps right now. Just like everybody\u2019s ready\
    \ for DevOps right now. There's absolutely no drawback in adopting these things.\
    \ We've mentioned it in context to enablement and scaling before \u2014 DataOps\
    \ is a necessity in order to scale efficiently. If you have just one little data\
    \ team doing all of the data things, you can have it. You can have a DataOps way\
    \ of working. Definitely."
  sec: 2833
  time: '47:13'
  who: Lars
- line: "Regarding the maturity levels, I don't have a super great definition of maturity\
    \ levels. There was an interesting development at Spotify. When I was at Google,\
    \ if we traced back to that time, we had a maturity ladder in terms of DevOps\
    \ \u2014 of quality assurance and software engineering. That ladder was called\
    \ \u201Ctest certified\u201D. That was the main vehicle for transformation at\
    \ Google from mostly manual testing to automated testing. That same idea was later\
    \ applied at Spotify. I can only take a tiny little credit because I dumped a\
    \ document on somebody's table and then I left the company. When I came back a\
    \ few years later, people had these T-shirts that said \u201Ctest certified\u201D\
    . It affected not only the processes, but also the fashion. That was very successful\
    \ at Spotify and precisely what they needed."
  who: Lars
- line: "They took that further to \u201Ctest certified for data\u201D, which essentially\
    \ became a DataOps maturity ladder. Instead of the original \u201Ctest certified\u201D\
    \ where you should have a continuous integration build, and you should have coverage\
    \ measurements, and you should add regression tests, and whatever you have in\
    \ production, they added similar things for data. So, you should have data quality\
    \ measurements, you should have a schema management automation so that you don't\
    \ push out invalid errors or incompatible schema changes and so forth. That is\
    \ the only DataOps maturity ladder that I've seen. Also, as a meta answer to that\
    \ question, I would like to point people to a great company called \u201CData\
    \ Kitchen\u201D based in Boston, where the CEO Christopher Berg is the premier\
    \ DataOps prophet. They have lots of good resources online and blogs and presentations\
    \ and white papers and so forth. You might be able to find further information\
    \ there."
  who: Lars
- header: Building self-service tools
- line: "I remember we were talking about self-service and enabling analysts to do\
    \ self-service. You mentioned that not all organizations are ready. For some,\
    \ pairing a data analyst with a data engineer will not solve this. But then at\
    \ some point, a tech company becomes mature enough when the pairing doesn't need\
    \ to happen. Analysts can just use these tools to do this themselves. How does\
    \ a company go from \u201Cthere is a central team who is taking care of all the\
    \ ad-hoc requests\u201D, to the state where analysts can themselves just go, and\
    \ build this ETL themselves?"
  sec: 3013
  time: '50:13'
  who: Alexey
- line: That's a long journey, I'm afraid. And if you have the centralized data team
    first, then the lower hanging fruit is to enable the developer teams in the organization.
    That's the step that we took back in 2013. The next step is to enable non-technical
    teams to also implement pipelines. But that's not necessarily a step that all
    organizations should take. It is much cheaper to embed analysts and software engineers
    or data engineers in the same team, working towards the same goal, rather than
    having this wall with a team that builds self service capabilities and then, on
    the other side of the wall, you have these analysts. That's the waterfall mentality
    still sticking around. In some organizations, you cannot break down these barriers
    and then it might make sense. But it's not necessarily a step that every organization
    should take, if you have the capability to mix up the competencies, you're better
    off that way, it's much more efficient.
  sec: 3071
  time: '51:11'
  who: Lars
- line: Would you say it's more an anti-pattern, then?
  sec: 3150
  time: '52:30'
  who: Alexey
- line: "In a sense. But some self-service you have to do. If you look at non-technical\
    \ teams in a very data mature organization like Spotify. Even the non-technical\
    \ teams have access to Big Query, and can do exploratory analytics there. I saw\
    \ some numbers \u2014 30% of the entire staff at Spotify use Big Query on a regular\
    \ basis, at least monthly. That is an extraordinary figure, it's as low friction\
    \ to get data for your decisions at such a company as it is for us to open a word\
    \ processor. It's the same. We don't think of it, we just do it and very few companies\
    \ are at that level of maturity."
  sec: 3155
  time: '52:35'
  who: Lars
- header: DevOps vs DataOps vs MLOps
- line: "This reminds me that at the beginning of our chat, we wanted to ask you about\
    \ different \u201Csomething-Ops\u201D. We already talked about the difference\
    \ between DevOps and DataOps. Correct me if I'm wrong, but in case of DataOps,\
    \ you have the same principles, but in addition, you have embedded data engineers\
    \ and data analysts in the team. This is a cross functional team. Then you have\
    \ this data platform with all these components that talked about. Is there something\
    \ else? Is it the key differentiator between DataOps and DevOps?"
  sec: 3211
  time: '53:31'
  who: Alexey
- line: I think you nailed it. It's the different mix of competencies. The philosophies
    are very similar. Some activities are different, but you nailed it. And yes, there
    are other Ops. I think that's what you were about to get to.
  sec: 3263
  time: '54:23'
  who: Lars
- line: Yes, exactly. There is MLOps. Do you have any ideas about it? And what is
    the difference between MLOps and DataOps?
  sec: 3279
  time: '54:39'
  who: Alexey
- line: "It's also the different mixes of people. If you have seen, if you've experienced\
    \ enterprise companies adopting data science and machine learning, and so forth.\
    \ But you usually see the water patterns showing up again. You see a bunch of\
    \ data scientists in a corner. First, they have nothing to do, and they are unhappy.\
    \ Then somebody figures out, they need a pile of data. They get one damp of data,\
    \ and then they build some models. Then those Python models are thrown over the\
    \ wall to a bunch of developers. They look at it and say \u201Cyuck\u201D, and\
    \ translate them to Java. That batch of things is thrown over the wall to the\
    \ operations people. Then the data scientists say, we now have a new model. And\
    \ the whole thing repeats. But they never get any feedback from how they work\
    \ in production. MLOps is essentially mixing these different competencies, data\
    \ science, data and software engineering, operations and quality assurance into\
    \ the same mix. All work together towards the same goal with the same type of\
    \ tools in the same environments, closing that feedback loop from model idea to\
    \ production, to measurements."
  sec: 3287
  time: '54:47'
  who: Lars
- line: "There's much overlap between DataOps because of the pipelines, work in the\
    \ data platform, and the data quality measurements \u2014 all of that is in common.\
    \ But there are a few other things that are specific to data science and machine\
    \ learning models. Like running multiple models in parallel and trying out the\
    \ new ones in mode; measuring internal characteristics of the models \u2014 precision\
    \ recall, in real life, and acting on that; having ensemble models where you combine\
    \ several. So there are a number of other ML specific things that come into play.\
    \ But the philosophies are the same."
  who: Lars
- line: I often see teams that have ML engineers, data engineers, and analysts and
    data scientists all work together. Is it MLOps? Or DataOps? Maybe it doesn't really
    matter, as long as teams are working on delivering value?
  sec: 3415
  time: '56:55'
  who: Alexey
- line: "Exactly. It's the alignment towards the same goal. I think if you fast forward\
    \ 5, 10 years, we will see DevSecOps becoming more mature, where security is aligned\
    \ towards the same goal; and the DataComplianceOps where the legal aspects also\
    \ are aligned, instead of having another department that says \u201Cno\u201D to\
    \ things."
  sec: 3436
  time: '57:16'
  who: Lars
- header: Data mesh
- line: "Recently I found out about this thing called \u201CData mesh\u201D, maybe\
    \ one month ago. I accidentally discovered it, and then I noticed that it's all\
    \ over the place. Everyone seems to be talking about this. So, what is data mesh?\
    \ How is it related to DataOps?"
  sec: 3466
  time: '57:46'
  who: Alexey
- line: "It is related. Everybody's talking about it, very few have seen one. I actually\
    \ have seen one. Spotify, again, moved to one, when we moved from Hadoop to the\
    \ cloud, as a side effect of the cloud move. First, it assumes DataOps is in place.\
    \ Otherwise, it's not meaningful to have a data mesh. It also assumes something\
    \ called \u201CData democratization\u201D, which we have touched on but not named.\
    \ It is the enablement of all teams to access the data and to implement data pipelines."
  sec: 3488
  time: '58:08'
  who: Lars
- line: "Data mesh is scaling technology that is relevant for large organizations.\
    \ Centralization of how you work with the data, the technology of the data platform,\
    \ and the storage of the data platform and so forth \u2014 where it becomes a\
    \ bottleneck. The data platform is homogeneous and is governed in a centralized\
    \ way. This used to be Hadoop, nowadays it's the cloud, where all of the data\
    \ files are of the same format. They're governed with the same workflow orchestration\
    \ and the same principles for privacy, access and so forth. Data mesh is about\
    \ decentralizing that governance. After Spotify has moved to data mesh, rather\
    \ than going to the central Hadoop cluster, you went to the people \u2014 the\
    \ teams that actually were producing a particular data set \u2014 the user team,\
    \ the web team or whatever. You talk to them to get access to the data, rather\
    \ than going to talk to some data infrastructure teams."
  who: Lars
- line: "There's also an aspect of responsibility on the source system owners \u2014\
    \ the user team, the web team, and so forth \u2014 to produce data artefacts into\
    \ the data platform. In early data platforms, it's often the case that I need\
    \ this data. \u201CCould you export it for me?\u201D And the other team says,\
    \ \u201CNo, we have more important things to do. But here you can get access to\
    \ the database. You do the dump yourselves. Please do it during the night when\
    \ the activity is low.\u201D With time, with maturity, that responsibility shifts\
    \ to the source system owners to do that export on their own \u2014 and having\
    \ that as part of their expectations."
  who: Lars
- line: "I am quite concerned regarding the buzz around data mesh. There's so many\
    \ companies that jump on the latest buzzword and say, \u201Cwe want that as well\u201D\
    . If you don't have a strong governance or strong culture of sharing in place,\
    \ if you rather go directly to data mesh instead of a centralized platform where\
    \ you share everything, then you will end up with the data spread around in silos.\
    \ This is what we used to have before there were data platforms. So, we're back\
    \ into \u201Ceverything is locked up in microservices\u201D and you won't have\
    \ the homogeneity that keeps the operations low, enables the data democratization\
    \ and so forth. If you say to teams, \u201Cyou are expected to export this data\
    \ set\u201D. But the data mesh philosophy says that we should also be responsible\
    \ for curating that and cleaning that data set. First of all, you have to wait\
    \ a quarter until we have more time. Second of all, we will export the cleaned\
    \ things. But in that cleaning, lots of information is lost \u2014 and whether\
    \ that information is important or not depends on the use case. For reporting\
    \ purposes, you want everything to be clean and smooth, and all the real users\
    \ are included. But for fraud detection purposes, or bot detection purposes, you\
    \ want all of the dirty information. In Data Lake, everything raw is dumped. All\
    \ the information is there. But with data silos, all of the raw interesting information\
    \ is hidden away. So, I'm quite concerned that all of the buzz around this will\
    \ make people never get out of the data silos."
  who: Lars
- line: 'Just to summarize: an organization evolves, there is a central data platform.
    But at some point, it just becomes too big. Then the idea behind data mesh is
    we start chopping this data platform into different sub platforms or even completely
    separate platforms. Is this, in essence, what data mesh is about?'
  sec: 3782
  time: '1:03:02'
  who: Alexey
- line: Something like that. The time at which it makes sense to split up the homogeneous
    or decentralized platform depends on your capabilities to coordinate. If you have
    strong autonomous culture, like at Spotify, then it makes sense. Spotify managed
    to become, I don't know, several thousand employees before you were at that scale.
    If you have a company with very strong capabilities of coordinating your work,
    like Google or Facebook have, then the centralized solutions work, to perhaps
    to infinite scape.
  sec: 3809
  time: '1:03:29'
  who: Lars
- line: Okay, thank you. We still have three more questions, and they want to ask
    you if you have some time.
  sec: 3849
  time: '1:04:09'
  who: Alexey
- line: Absolutely. My time is yours.
  sec: 3856
  time: '1:04:16'
  who: Lars
- header: Keeping track of transformations
- line: How do you keep track of all the transformations that have been undertaken
    between each newly created data set within the data platform?
  sec: 3858
  time: '1:04:18'
  who: Alexey
- line: "That's a very good question and I skipped past that. The answer is simple.\
    \ It's all code. We don't keep track of data. We only keep track of code. A part\
    \ of that code is the workflow definitions, which says that these data sits over\
    \ here when they arrive, they are supposed to be transformed to this data set\
    \ over there. So, all of the definitions are thereby in code. The data sets can\
    \ get orphaned if you change the code without changing the data. You have to have\
    \ some \u2014 very lightweight \u2014 process for that, an automated retention\
    \ or something. But every single data set that is produced and active somewhere\
    \ is defined in code at some point. There's also tools \u2014 if you don't have\
    \ sufficient audit \u2014 to recover from that. There are cataloguing tools that\
    \ will go out and scout your Google Cloud Storage, or S3 storage, or databases,\
    \ and so forth. In a way, those are useful, but those are also to patch a symptom\
    \ when you've perhaps should address the root cause instead. I tend to not use\
    \ these tools heavily. But in some cases, they might be applicable. But the short\
    \ answer is you keep track of everything in code."
  sec: 3872
  time: '1:04:32'
  who: Lars
- header: Relational databases with immutable snapshots
- line: Can you name some relational databases that make immutable snapshots (for
    example, datasets) and then run version transformations, with the ability to differentiate
    between different versions?
  sec: 3961
  time: '1:06:01'
  who: Alexey
- line: "I cannot. But I know remarkably little about relational databases and I'm\
    \ terrible at SQL. What we do in data platforms, typically, is to dump the database\
    \ tables that we're interested in. We take a full dump each day or each hour or\
    \ something. That avoids this problem of slowly changing dimensions that you have\
    \ in data warehouses, because we have the full history way back in time. That\
    \ introduces some other problems, for example, with GDPR compliance, so you need\
    \ to prepare for that. But that's generally how we handle the different versions\
    \ of database tables. You lose some information in that dumping, because what\
    \ happened in-between, you don't catch. There are ways to mitigate that or to\
    \ get all of the information. One way is to have the application dump all of change\
    \ events, either on a stream or in a change table inside the database, or via\
    \ something called \u201CChange Data Capture\u201D, which is essentially a way\
    \ of translating the transaction log in the database to a Kafka stream, and that\
    \ you get all of the nitty-gritty details if you want."
  sec: 3977
  time: '1:06:17'
  who: Lars
- header: Lakehouse
- line: "The last question we have \u2014 how would you define lake house architecture?\
    \ And what's the core difference, compared to data warehouse?"
  sec: 4072
  time: '1:07:52'
  who: Alexey
- line: "Data warehouse predates the data lake. That is a construct for collecting\
    \ aggregate data from various systems, to a place where you can build reports\
    \ and do exploratory analytics, and so forth. Data warehouses usually don't have\
    \ the raw data, but they have the aggregate data. They tend to have mutable tables.\
    \ The data lake has all of the raw data and then you have these functional transforms.\
    \ A data lake house is a combination of these two, where they technically look\
    \ like a data lake. But you add the ability to interactively explore your data\
    \ within an array indexing and so forth. To be able to use it as a data warehouse,\
    \ and then also add mutability to the data sets, which means that you can reuse\
    \ your ETL scripts from the data warehouse without changing the transformations.\
    \ But you break these functional principles that make the data in the data platform\
    \ so efficient for operations and innovation. So, yes it can be useful as a gateway\
    \ drug, as I said, if you want to transition. But I think it's an anti-pattern,\
    \ so I strongly recommend people to get into immutability instead. Just like we\
    \ nowadays accept that a container image is immutable. It's something that we\
    \ build from the source code. If you say that we should revise that immutability\
    \ and start touching our containers in production, people will throw axes at you.\
    \ It\u2019s insane, because it increases this complexity so massively. So stick\
    \ to immutability and bear with the great fruits of functional transformations."
  sec: 4086
  time: '1:08:06'
  who: Lars
- line: Thank you. We have covered all the questions we have. I still have one more
    that we didn't manage to ask, but we can keep them for some other day. Thanks
    a lot for joining us today and sharing your experience, your knowledge and defining
    all these terms. Some of them were just buzzwords to me, like data mesh. Now I
    know. Thanks a lot. I think that's all. Do you have any last words?
  sec: 4233
  time: '1:10:33'
  who: Alexey
- line: "I do not. If you were interested in some of the topics that are brought up,\
    \ there's also a list of the conference presentations that I've done. If you go\
    \ to scling.com, next to \u201Creading list\u201D, you will find me diving into\
    \ things DataOps, and quality assurance for data pipelines, and how to solve GDPR\
    \ related problems and then solving some of the time related problems that we've\
    \ spoken of. For example, how do you deal with late incoming data and so forth.\
    \ If you want to dive further, that's a resource."
  sec: 4261
  time: '1:11:01'
  who: Lars
- line: Thanks a lot, and have a nice weekend.
  sec: 4302
  time: '1:11:42'
  who: Alexey
- line: It was a pleasure to be here.
  sec: 4326
  time: '1:12:06'
  who: Lars

---

We talked about:

- Lars’ career
- Doing DataOps before it existed
- What is DataOps
- Data platform
- Data warehouses and data lakes
- Main components of the data platform and tools to implement it
- Books about functional programming principles
- Batch vs streaming
- Maturity levels
- Building self-service tools
- MLOps vs DataOps
- Data Mesh
- Lake house


Links:

- [https://www.scling.com/reading-list](https://www.scling.com/reading-list){:target="_blank"}
- [https://www.scling.com/presentations](https://www.scling.com/presentations){:target="_blank"}