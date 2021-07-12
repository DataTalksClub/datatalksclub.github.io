---
title: "Big Data Engineer vs Data Scientist"
short: "Big Data Engineer vs Data Scientist"
guests: [roksolanadiachuk]

image: images/podcast/s04e03-big-data-engineer-vs-data-scientist.jpg

season: 4
episode: 3

ids:
  youtube: yg3d1lFd7Uo
  anchor: Big-Data-Engineer-vs-Data-Scientist---Roksolana-Diachuk-e139sl8

links:
  youtube: https://www.youtube.com/watch?v=yg3d1lFd7Uo
  anchor: https://anchor.fm/datatalksclub/episodes/Big-Data-Engineer-vs-Data-Scientist---Roksolana-Diachuk-e139sl8
  spotify: https://open.spotify.com/episode/08Mb5JOOo6sWOFgsXILVsj
  apple: https://podcasts.apple.com/us/podcast/big-data-engineer-vs-data-scientist-roksolana-diachuk/id1541710331?i=1000528386609

transcript:
- line: Today we will talk about the difference between big data engineers and data
    scientists. We have a special guest today, Roksolana. Roksolana works as a big
    data engineer at Captify. Today, she will talk about the roles of data engineer
    and data scientist. Welcome.
  sec: 112
  time: '1:52'
  who: Alexey
- line: Thank you.
  sec: 136
  time: '2:16'
  who: Roksolana
- header: "Roksolana\u2019s background"
- line: Before we start with our main topic, let's talk a bit about your background.
    Can you tell us a bit about your career journey so far?
  sec: 139
  time: '2:19'
  who: Alexey
- line: "Yeah, sure. I have a software engineering degree from one of Kiev\u2019s\
    \ universities. I have both Bachelor\u2019s and Master's degrees. After that,\
    \ I worked for some time as a backend engineer using mostly Java. At some point,\
    \ I learned about data science and big data engineering. I had some time to make\
    \ a decision about what exactly I wanted to do. Backend engineering just got a\
    \ bit boring for me at some point, so I switched into big data engineering and\
    \ learned the programming language Scala, which is currently my main programming\
    \ language. For a few years, I worked at a company called Ciklum. It's quite famous\
    \ in Ukraine, because it's quite a big company \u2013 one of the top five. It's\
    \ an outsourcing company, which works with clients and does some research. I was\
    \ working at the R&D department there. We had some internal research stuff and\
    \ we also worked on some client projects."
  sec: 148
  time: '2:28'
  who: Roksolana
- line: "About two years ago, I joined Captify, which is a product company. They build\
    \ products for the advertising industry. Actually the company is British \u2013\
    \ it's based in the UK. But a part of the engineering team is located in Kiev,\
    \ where I'm based. I mostly work on the product parts, specifically in the big\
    \ data engineering team."
  who: Roksolana
- line: "I\u2019ve heard that in advertising there is so much data that big data engineering\
    \ becomes really important. These companies get terabytes of data every day and\
    \ they need to effectively process this data. Is that an accurate assessment?"
  sec: 234
  time: '3:54'
  who: Alexey
- line: "Yes. What makes Captify\u2019s solutions unique is the data insights, which\
    \ are obviously delivered through the help of the big data engineering team, which\
    \ has different sources of data and different ways to transform this data and\
    \ deliver it to the client."
  sec: 250
  time: '4:10'
  who: Roksolana
- header: "A Big Data Engineer\u2019s typical day at work"
- line: What do you do at work? What do you usually do as a big data engineer?
  sec: 266
  time: '4:26'
  who: Alexey
- line: "My main responsibility is building data pipelines. Usually, it's in ETL format\
    \ \u2013 extract, transform, load \u2013 this entails reading the data from some\
    \ source, building transformations, doing some aggregations, and uploading the\
    \ result somewhere so that it will be available for other users. This can be a\
    \ relational database, or it's often just data storage, like HDFS or S3. Users\
    \ can query the data using query engines like Impala. Usually we service the data\
    \ in such a way that the analyst team could run queries and build reports with\
    \ it. That's my main responsibility."
  sec: 272
  time: '4:32'
  who: Roksolana
- line: "Aside from that, we have some internal libraries development and research.\
    \ For example, right now I'm working a bit on the Delta Lake introduction from\
    \ Databricks. We also work on some features or do some small fixes because there\u2019\
    s quite a bit of legacy code already. However, the product is quite stable."
  who: Roksolana
- line: Our department also does some new pipeline creation or just upgrades the existing
    infrastructure. Sometimes we just rewrite some parts to increase their performance.
    Optimizing performance of existing pipelines is also a big part of the job, especially
    during some production incidents, or in cases where something is not performing
    as good as it's supposed to.
  who: Roksolana
- line: "So basically, your main job is to take some raw data that is coming from\
    \ your product \u2013 data that users of your product generate. Your job is to\
    \ take this data, convert it, build data pipelines using ETLs so that analysts\
    \ or other users who need to analyze the data, can use tools like Impala to access\
    \ this data on SQL queries and get some insights. Is that right?"
  sec: 363
  time: '6:03'
  who: Alexey
- line: Yeah.
  sec: 391
  time: '6:31'
  who: Roksolana
- line: You also maintain this Impala to make it possible for them to do queries?
  sec: 393
  time: '6:33'
  who: Alexey
- line: "That\u2019s partially the work of the infrastructure team. We mostly work\
    \ on optimizing queries and jobs in such a way that other users will be able to\
    \ run their queries. Otherwise our jobs will take up way too much resources \u2013\
    \ it will be impossible to work with them. But we set up our own Spark jobs and\
    \ optimize them in terms of resources, in order to answer questions like \u201C\
    How many nodes in the cluster do we need? How do we want to scale that?\u201D\
    \ We decide whether we want to receive less or more resources for our own jobs\
    \ so that their performance is optimal, or whether we want to optimize it using\
    \ Spark capabilities, which would be just improving the code base."
  sec: 398
  time: '6:38'
  who: Roksolana
- header: "Big Data Engineer\u2019s tools"
- line: So what kind of tools do you use? You mentioned Spark, Impala, and you also
    mentioned HDFS and S3. What else do you use for creating these pipelines?
  sec: 438
  time: '7:18'
  who: Alexey
- line: Some other main ones, aside from some AWS services like S3, some services
    for Spark setup. Spark is built using Lazarus for now. We have a bit of Kubernetes,
    which we mostly use for metrics. We also use alerting systems like Prometheus
    and Grafana as well. We have some backend libraries for the data processing part,
    like Play in Scala or library split tests, which also are Scala libraries like
    Scala Test.
  sec: 450
  time: '7:30'
  who: Roksolana
- header: Alice discovers Kubernetes
- line: I remember you had an interesting talk with a funny name. Something about
    Alice discovering Kubernetes. What's the name of this talk?
  sec: 484
  time: '8:04'
  who: Alexey
- line: I have a series of those. The first one was when Alice learns the difference
    between functional programming and Kubernetes. (I'm getting red. [laughs])
  sec: 496
  time: '8:16'
  who: Roksolana
- line: How did you come up with this idea about Alice?
  sec: 508
  time: '8:28'
  who: Alexey
- line: "It\u2019s hard for me to say. It's kind of a cumulative experience because\
    \ before I started to speak at conferences, I visited tons of local and European\
    \ conferences. I noticed that it's much more interesting to get invested into\
    \ the story aside from the technical side. That's how I tried this idea with the\
    \ first talk. After some time, I decided that I probably need to build more of\
    \ those. That sparked popularity because people enjoyed the story side quite a\
    \ lot as well."
  sec: 511
  time: '8:31'
  who: Roksolana
- line: It became like a brand.
  sec: 543
  time: '9:03'
  who: Alexey
- line: Sort of.
  sec: 545
  time: '9:05'
  who: Roksolana
- header: The difference between big data engineers and usual data engineers
- line: "Sometimes I get a bit confused. We have data engineers, we have big data\
    \ engineers \u2013 is there any difference between these two? Or are they mostly\
    \ synonyms \u2013 big data engineers and usual data engineers?"
  sec: 552
  time: '9:12'
  who: Alexey
- line: "If you\u2019re going \u2018by the book\u2019 or the way it's supposed to\
    \ be \u2013 there\u2019s a difference in terms of how you process the data. Big\
    \ data engineering requires tools that are a bit different, like heavy load optimizations,\
    \ data engineering, and a bit of software engineering on the backend. But in reality,\
    \ I would say that a lot of companies conflate big data engineers with data engineers.\
    \ It's possibly a bit confusing because of that."
  sec: 567
  time: '9:27'
  who: Roksolana
- line: "So many companies just drop the \u2018big\u2019 part and just go with \u2018\
    data engineer\u2019. Is there any difference in the tools they use? For example,\
    \ you mentioned Spark, Impala, and things like that. From what I see, data engineers\
    \ use tools that are maybe a bit different. Most of them use Spark as well, but\
    \ I see more cloud-based things like Streams, Lambda functions and things like\
    \ that. Or does it just depend on the company and there actually isn\u2019t a\
    \ big difference?"
  sec: 592
  time: '9:52'
  who: Alexey
- line: I would say that it depends on the company. Some companies choose multiple
    cloud services and some companies build custom solutions. Because of that, data
    engineers might be more on the side of parsing data, which is considered to be
    more of a backend thing, or maybe they write/read from the database. While a more
    big data thing would be working with so called Big Data-specific data formats
    like Avro, Parquet and ProtoBuf. Whereas backend engineers usually work with JSON
    or maybe a little bit with CSVs.
  sec: 629
  time: '10:29'
  who: Roksolana
- line: "Okay, so in the end, there usually isn\u2019t much of a difference. Would\
    \ you agree?"
  sec: 662
  time: '11:02'
  who: Alexey
- line: Yeah.
  sec: 665
  time: '11:05'
  who: Roksolana
- header: "Data Engineers\u2019 skills"
- line: "OK. We talked a bit about tools \u2013 we talked about Spark, Cloud, Scala.\
    \ I think Python is quite popular in data engineering as well. If we're not talking\
    \ about specific tools, but more fundamental skills, what kind of skills do people\
    \ need to be able to do their job?"
  sec: 667
  time: '11:07'
  who: Alexey
- line: "I would say the most important one is coding skills. Often senior level engineers\
    \ get into data engineering, which is quite logical, because they already have\
    \ some experience on the backend side. Then they learn the Big Data stack and\
    \ just understand how it works behind the scenes. So I would say it\u2019s definitely\
    \ important to have a great level of coding skills."
  sec: 692
  time: '11:32'
  who: Roksolana
- line: Another one is working with databases, like writing queries and being able
    to optimize them. Usually, it's SQL databases, but sometimes No-SQL as well. So
    they need to be able to switch from one to the other. In my experience, when you
    join different companies, you sometimes have a totally different stack, or even
    different projects, so you just have to switch really quickly. But the skills
    I mentioned would be the main ones.
  who: Roksolana
- line: Something I also consider important, but is sometimes missing, is the infrastructure-side
    skills. This would be understanding the networking side. For example, being able
    to know what the racks are supposed to look like, how it works on the hardware
    side, why it's important to optimize some of our applications in certain ways.
    So they have to not be afraid of getting into the infrastructure side and setting
    something up because we do need to do that sometimes.
  who: Roksolana
- line: "What about distributed computing and things like this? Or is this included\
    \ in \u2018databases\u2019?"
  sec: 771
  time: '12:51'
  who: Alexey
- line: "I would say that currently, frameworks are on such a high level that sometimes\
    \ people don't need to understand that. But I would say that it\u2019s quite a\
    \ basic thing \u2013 university stuff."
  sec: 781
  time: '13:01'
  who: Roksolana
- line: "I remember at university, we studied MapReduce. I don\u2019t think I really\
    \ used Hadoop outside of university. But it's still important to know these concepts,\
    \ right?"
  sec: 793
  time: '13:13'
  who: Alexey
- line: "In the current environment, I would say it's important to understand them.\
    \ But in terms of Hadoop, it's getting really outdated lately. When I was starting\
    \ out, it was important to understand how it works \u2013 HDFS specifically. But\
    \ right now a lot of people and a lot of companies just switch to something else\
    \ instead of that. It's easier to maintain some cloud services, for example."
  sec: 811
  time: '13:31'
  who: Roksolana
- header: Data scientist role from the perspective of a data engineer
- line: "We talked about big data engineers \u2013 they take care of data preparation.\
    \ Some data is generated by the users of our product and the data engineers take\
    \ care of processing it and making it possible for analysts and other people to\
    \ run their queries on it. What do data scientists do?"
  sec: 836
  time: '13:56'
  who: Alexey
- line: "The main part would be actually building machine learning models, but it's\
    \ only one part of the machine learning model cycle, as it's called. They do need\
    \ to clean the data, prepare it to build features, create the models, and deploy\
    \ them. Sometimes it's in their role, sometimes it\u2019s in someone else's, but\
    \ they still need to have a good understanding of how it's supposed to be deployed\
    \ so they are able to evaluate it further. It's called a cycle because it can\
    \ repeat. If we need to fix some features, tune hyper-parameters, or just do something\
    \ general like switch to another solution if a particular one doesn\u2019t suit\
    \ our needs."
  sec: 860
  time: '14:20'
  who: Roksolana
- line: So cleaning the data is something that data scientists do? You cannot expect
    big data engineers to clean data for data scientists, right?
  sec: 901
  time: '15:01'
  who: Alexey
- line: I would say that it's a bit controversial because sometimes data engineers
    do take care of that. Sometimes data scientists need to still take care of this
    pre-processing step. It depends on the company as well, or just the way the pipeline
    is built.
  sec: 909
  time: '15:09'
  who: Roksolana
- line: In the end, you could say they both do cleaning, just different kinds of cleaning.
    Is that an accurate assessment?
  sec: 923
  time: '15:23'
  who: Alexey
- line: Yeah.
  sec: 930
  time: '15:30'
  who: Roksolana
- header: "Big data engineers\u2019 tools vs data scientists\u2019 tools"
- line: I think I have an understanding in terms of tools. I think data scientists
    use quite a different set of tools compared to big data engineers, right?
  sec: 932
  time: '15:32'
  who: Alexey
- line: Yeah, sometimes the tools they use can coincide in Spark, because Spark is
    getting more and more popular for machine learning as well. Python is also heavily
    used by some big data engineers, so they coincide here as well. Mostly machine
    learning engineers or data scientists would use multiple specific libraries for
    specific model cases, whether it's a recommendation system, deployment, or computer
    vision. They may not get involved that much with infrastructure, however. The
    databases would be practically the same, especially for data engineers, who just
    pull the data there and the data scientists just take it from there.
  sec: 946
  time: '15:46'
  who: Roksolana
- header: Communication between big data engineers and data scientists
- line: What about in terms of the programming language? You use Scala. Do the data
    scientists you work with also use Scala, or do they use Python?
  sec: 986
  time: '16:26'
  who: Alexey
- line: They use Python. We communicate through files or data that we write to the
    database. Therefore, they don't need to go into our source code. But they also
    have a software engineer / machine learning engineers who work with both Scala
    and Python, depending on the task.
  sec: 998
  time: '16:38'
  who: Roksolana
- line: "Okay, so you produce a file \u2013 a parquet file, for example \u2013 and\
    \ then the data scientists know how to read this file using Python, for example,\
    \ and this is how you collaborate. Correct?"
  sec: 1015
  time: '16:55'
  who: Alexey
- line: Yes.
  sec: 1024
  time: '17:04'
  who: Roksolana
- line: "Actually, my next question was, \u201CHow do you work together?\u201D I think\
    \ we've partly answered that. The interface for your communication is the files\
    \ that you create, right? You create some files and the data scientists consume\
    \ these files. But how do you work together in general? Do you work in the same\
    \ team? Do you work in different teams? What does the process look like?"
  sec: 1027
  time: '17:07'
  who: Alexey
- line: "In my company, we work in different teams. We don't even have that much of\
    \ a connection, because we don't really know what data scientists do with the\
    \ data later. We just deliver it the way that they need it. For example, they\
    \ can just ask to add some field or to build some transformation, because it's\
    \ easier to build it on our side, which would reduce the heaviness of the load.\
    \ In other projects that I saw, or that my colleagues work on in different companies,\
    \ sometimes they have a specific team where they have a dedicated data engineer,\
    \ or multiple data engineers, and they work closely on each step of the pipeline.\
    \ So it\u2019s different from the way that my company works. Sometimes the workflow\
    \ is the same as in my company. Throughout my career, I didn't really work closely\
    \ with data scientists and I learned about data science outside of work. I was\
    \ just interested in understanding how it works. While my colleagues from a previous\
    \ workplace, for example, they changed their jobs and constantly and closely work\
    \ with data scientists. So there can be different workflows in different companies."
  sec: 1048
  time: '17:28'
  who: Roksolana
- line: "So if a data scientist needs a new field, would they just go and create a\
    \ JIRA ticket for you that says \u201CHey, I need this field.\u201D"
  sec: 1108
  time: '18:28'
  who: Alexey
- line: Yeah.
  sec: 1116
  time: '18:36'
  who: Roksolana
- line: "Something like that, okay. So this is how you interact with data scientists.\
    \ You sit maybe in different rooms, or, I mean\u2026 Now we don't have rooms \u2013\
    \ but you\u2019re in different teams, right? And you communicate occasionally\
    \ through JIRA, or maybe some common meetings that you have very frequently."
  sec: 1116
  time: '18:36'
  who: Alexey
- line: Yeah.
  sec: 1133
  time: '18:53'
  who: Roksolana
- header: Example project walkthrough
- line: Okay. Maybe we can do a sort of walkthrough of a project. Let's say you want
    to start a new project and it involves machine learning. But you still need to
    process some data before the data scientists can work with it. Do you have some
    ideas for a project that we can discuss?
  sec: 1134
  time: '18:54'
  who: Alexey
- line: "We can take a recommendation system case. For example, if we have a Netflix-type\
    \ website where there are different types of data \u2013 users\u2019 information,\
    \ history of their ratings of movies, or just their search history. We need to\
    \ recommend some movies to these users. The part of data engineering would be\
    \ to extract this data. They could probably build two pipelines \u2013 one streaming\
    \ and one static/batch processing. With streaming, some new data is constantly\
    \ coming in to update the model later. The batch pipeline would be used to store\
    \ the history and it can be in different formats. Then we would build some kind\
    \ of transformations to write it to either files like parquet or CSV for better\
    \ processing for data scientists. Or we would write some part of the information.\
    \ For example, we could store the data about movies or users in the database and\
    \ have the streaming information of all their ratings."
  sec: 1158
  time: '19:18'
  who: Roksolana
- line: "Then we could combine this together and the data scientists would be able\
    \ to go through this data, which would be cleaned from duplicates or some zero\
    \ values, which can get a bit confusing later. They can define which features\
    \ will play the biggest role and build the machine learning model. The deployment\
    \ part depends who is responsible for it. Sometimes, it\u2019s machine learning\
    \ engineers who do it, sometimes it\u2019s data scientists themselves, or it can\
    \ even be the data engineers. So someone would deploy the model to production\
    \ and then the data scientists could evaluate whether the solution works or not\
    \ and deliver some results. Actually, if it's deployed, there is a library that\
    \ is able to be connected to Tableau or write the results to the database if it's\
    \ recommendations. Then we can display it in Tableau in such a way that other\
    \ users, like data analysts, or business users can just visualize the data based\
    \ on graph charts. This allows the data scientists to present the solution with\
    \ these results in a more graphic way."
  who: Roksolana
- line: "Okay, so we have a Netflix-like website where users can watch movies. Every\
    \ time a user watches a movie, or leaves a rating about the movie, this data ends\
    \ up in your data pipeline immediately? You said you have a stream of data \u2013\
    \ this would be the kind of data you mean \u2013 right? You also have some processing\
    \ jobs that take this information, or this event, process this, and then put it\
    \ into some sort of storage, like parquet or CSV. Then the data scientists take\
    \ the data that you prepared from these events, and they can train a model with\
    \ that. I assume if this thing runs for maybe a month, they can then take this\
    \ one month of data and train their model. You said the data scientists also take\
    \ care of deploying the model and there are some analysts who can look at the\
    \ results."
  sec: 1293
  time: '21:33'
  who: Alexey
- line: So what kind of tools would you use here? For the steaming part, for example.
    Where do you use something like Kafka or Kinesis? Or what kind of tools would
    you use here?
  who: Alexey
- line: "I would probably use Flink. It's good for streaming. Spark is not that good,\
    \ but it's easier to connect Spark and Flink. For example, you'd have a Spark\
    \ pipeline for batch data processing if you already have some history about the\
    \ users. Let\u2019s say that the website was created some time ago so we already\
    \ have some historical data and stream it using Flink. Then you can write the\
    \ Flink files on some parquet to S3 storage and the Spark pipeline to be stored\
    \ within a database, which would include the historical data about users and movies.\
    \ Then we can combine the two in a library or the data scientists could read from\
    \ both and rely on historical data to build better predictions."
  sec: 1371
  time: '22:51'
  who: Roksolana
- header: Deployment
- line: Then they use their data science tools. At the end, you have a model which
    they deploy themselves? Or you can also help them deploy it? I imagine that if
    you have this stream of data, this is probably where you can put this model. Or
    not really?
  sec: 1420
  time: '23:40'
  who: Alexey
- line: "Yeah, actually data engineers can help with deployment. For example, there\
    \ are tools like ML flow, Kubeflow, which I know other teams in my company are\
    \ using. Therefore, they have a dedicated person for that \u2013 a data engineer\
    \ or machine learning engineer \u2013 it depends on what the company calls this\
    \ person. But they work on this more infrastructural side of things, like where\
    \ you build an API, or you have to work with Kubernetes or cloud services to build\
    \ the provision for this model service \u2013 probably build some container for\
    \ it. It's more backend work than data science work."
  sec: 1437
  time: '23:57'
  who: Roksolana
- line: And this person is in the data science team? They help the data scientists
    with this engineering work, right?
  sec: 1478
  time: '24:38'
  who: Alexey
- line: Yeah, that's kind of the way it works in my company.
  sec: 1486
  time: '24:46'
  who: Roksolana
- header: How much should data scientists know about data engineering?
- line: "Okay. We have a question and it's quite interesting. It\u2019s related to\
    \ what we're talking about now. \u201CHow much should data scientists know about\
    \ data engineering and what kind of skills do they need to have?\u201D You mentioned\
    \ that you have a dedicated engineer in the team. Does this engineer take care\
    \ of all the engineering stuff or do data scientists still need to have basic\
    \ knowledge of data engineering?"
  sec: 1489
  time: '24:49'
  who: Alexey
- line: "In my company, they\u2019re called machine learning engineers because they\
    \ deploy their own models sometimes, and they operate with data. Sometimes in\
    \ other teams, or in other companies, the data scientists only work with machine\
    \ learning models. But I would say that that would be an ideal case because startups\
    \ or new projects usually have this so-called \u2018full stack data scientist\u2019\
    \ \u2013 where they make one person do everything, or at least both the model\
    \ and deployment parts. I would say that it's important for data scientists just\
    \ to have an understanding of why some pipelines are built a particular way. It\
    \ would be helpful with assessment of time, or having an understanding how long\
    \ it might take for them to get the data or how some issues on the data engineering\
    \ side can influence them. But in general, I would say that it's only necessary\
    \ to have these skills if the person has to do the whole pipeline, which also\
    \ happens sometimes."
  sec: 1520
  time: '25:20'
  who: Roksolana
- line: Okay, so your data scientists are engineers, basically. If they need to, they
    can go and figure out how your pipelines work. Is that right?
  sec: 1581
  time: '26:21'
  who: Alexey
- line: Yeah.
  sec: 1591
  time: '26:31'
  who: Roksolana
- header: How can data scientists acquire knowledge about data pipelines?
- line: "But, in general, you said that it's a good idea for data scientists to know\
    \ how the pipelines are built. Do you know how they can acquire this knowledge?\
    \ How can they learn about how data pipelines are built if you're working in different\
    \ teams? The data scientists work in one team and you work in another team \u2013\
    \ how can data scientists gain this knowledge?"
  sec: 1592
  time: '26:32'
  who: Alexey
- line: I would say that there could be some knowledge-sharing sessions inside the
    company. We have, for example, internal engineering meetups, where each team can
    just talk about the technology that we use and how we build some solutions. Aside
    from that, if they are interested in the topic, they can also learn through resources
    like books, courses, or lectures. I think that there are quite a lot of resources
    lately on big data engineering. It's becoming more popular.
  sec: 1617
  time: '26:57'
  who: Roksolana
- header: Should data engineers become more like data scientists?
- line: "You mentioned that in your free time, you work a bit with data science, just\
    \ to learn a bit of machine learning. We have a question from Prem. The question\
    \ is \u201CShould data engineers gradually try to transition to become more like\
    \ data scientists?\u201D What are your thoughts on this? Should data engineers\
    \ get to know more data science to be better data engineers?"
  sec: 1650
  time: '27:30'
  who: Alexey
- line: "I would say that it's good to know more about how the machine learning cycle\
    \ works. For example, I don't really work with the internals of machine learning\
    \ models. I don't get into that, but I have knowledge of each step. Recently,\
    \ I started to learn how to deploy that \u2013 how to build the whole pipeline.\
    \ So that data scientist would only need to build the machine learning model.\
    \ I would say that it's important to understand each step and all the inputs and\
    \ outputs of those steps. It\u2019s not very important for data engineers to understand\
    \ how the model actually works. We're more on the software engineering side here,\
    \ like \u201CWhat is the input? What is the output?\u201D and \u201CWhat happens\
    \ next?\u201D That kind of thing."
  sec: 1682
  time: '28:02'
  who: Roksolana
- line: "So you don't need to go into the details of the exact mathematics or even\
    \ what kind of model they use inside. But you do need to know, \u201COkay, this\
    \ is a model. This is the kind of input it receives. This is the kind of output\
    \ it produces.\u201D And you need to know what to actually do with this. \u201C\
    How do you package this thing? How do you deploy this thing?\u201D And things\
    \ like this, right?"
  sec: 1728
  time: '28:48'
  who: Alexey
- line: "Yeah, I don't get much into algorithms. But it\u2019s important to understand\
    \ what the model actually does, because it influences the pipeline \u2013 this\
    \ knowledge help actually predict what can happen inside the pipeline or in different\
    \ cases where the unexpected happens."
  sec: 1753
  time: '29:13'
  who: Roksolana
- line: Do you think it would be beneficial for data engineers to actually learn these
    internals? Maybe not in great detail, but at least how random forest works, for
    example, or how logistic regression works. Or for data engineers, it's not really
    that important?
  sec: 1769
  time: '29:29'
  who: Alexey
- line: "I would say that it's not really important. It\u2019s more part of the person\u2019\
    s interests. I know some data engineers that are interested in machine learning\
    \ and they try it out. I think it's helpful if they work closely with data scientists.\
    \ It's also kind of nice to have a different perspective. While a lot of data\
    \ scientists have more mathematical backgrounds and analytical skills, data engineers\
    \ come from more software engineering backgrounds, and have the corresponding\
    \ point of view, which can be also helpful if people collaborate on building such\
    \ solutions."
  sec: 1788
  time: '29:48'
  who: Roksolana
- line: "I guess, if we reverse it, the same is true for data scientists. It would\
    \ also be beneficial for them to know the data engineering part of things. Maybe\
    \ not just \u201COkay, this is how I use this function in PySpark.\u201D But maybe\
    \ a bit more detail, right? It's not required for them to do this, but it would\
    \ be beneficial for them to get some idea of how it works underneath, right?"
  sec: 1821
  time: '30:21'
  who: Alexey
- line: Yeah. I agree with you here.
  sec: 1851
  time: '30:51'
  who: Roksolana
- header: Advice for analysts and scientists for transitioning into engineering
- line: "Now, we have a related question from Steve, \u201CWhat advice would you give\
    \ to analysts or data scientists who would like to transition into data engineering?"
  sec: 1853
  time: '30:53'
  who: Alexey
- line: "I would say that the most important thing is to work on having a great level\
    \ of coding skills. When I was mentoring a data analyst, I noticed that she doesn't\
    \ have the same background in software engineering, and therefore, she sometimes\
    \ couldn't understand how the actual algorithms work, which seemed to me as quite\
    \ basic. From my perspective, I didn't really understand that. But she had more\
    \ of a mathematical background. Therefore, I think it's very important to have\
    \ more experience here and learn on that side. Aside from that, I think \u2013\
    \ databases. Maybe a bit of the infrastructure side as well, if this person would\
    \ like to get involved in deployment and the set-up of the jobs."
  sec: 1865
  time: '31:05'
  who: Roksolana
- line: "\u201CAlgorithms\u201D is quite broad. What kind of algorithms do you think\
    \ will be most beneficial to know? Just basic data structures and algorithms,\
    \ or?"
  sec: 1913
  time: '31:53'
  who: Alexey
- line: Yeah, exactly. Some basic data structures, sometimes even the code reviews.
    It can turn out that someone could write something in a more performant way, just
    by reusing this knowledge from the algorithms and data structures.
  sec: 1924
  time: '32:04'
  who: Roksolana
- line: "It\u2019s like you said, at least know how hashmap works, and things like\
    \ this. Are there any other things that would be beneficial to know from these\
    \ algorithms and data structures? Would they need to go into graphs, for example?\
    \ Or trees? Or not at the beginning?"
  sec: 1937
  time: '32:17'
  who: Alexey
- line: "Depends on what they\u2019re working with. For example, I got into graphs\
    \ because I was working with graph databases \u2013 no-SQL databases. Before that,\
    \ you wouldn\u2019t need to know much of that. Also, it's not that often used.\
    \ I didn't notice that in other companies they would graph databases. Mostly it's\
    \ about the complexity of algorithms. It's not just knowing them by heart, but\
    \ rather understanding why it's better to use this data structure or this algorithm.\
    \ Also, it's a lot in the context of how the programming language works. In some\
    \ programming languages, it's different \u2013 some data structures are named\
    \ differently, some are implemented differently. It's important to know which\
    \ one is better to use."
  sec: 1963
  time: '32:43'
  who: Roksolana
- line: "From the top of your head, do you have a list of data structures that you\
    \ \u201Cmust know\u201D to get started? In addition to lists, sets, and hashmaps\
    \ that we mentioned."
  sec: 2010
  time: '33:30'
  who: Alexey
- line: "Get it from Scala. We have sequences at least, arrays. But in functional\
    \ programming, we don\u2019t use arrays much, so it's also different depending\
    \ on the programming language you use. I would say it\u2019s specific to the language.\
    \ In Python they have different names for the data structures."
  sec: 2031
  time: '33:51'
  who: Roksolana
- line: I guess the sequence you mentioned, I think is more like a link list, right?
  sec: 2051
  time: '34:11'
  who: Alexey
- line: Yeah.
  sec: 2056
  time: '34:16'
  who: Roksolana
- line: Okay. Then you have a different type of list, which is an array. Right? When
    it comes to sets, there are different ways of implementing a set. You can have
    a tree base set, or you can have a hash base set. Do you think that this is also
    good knowledge to have? Or not really? You just need to know that set is faster
    than list?
  sec: 2058
  time: '34:18'
  who: Alexey
- line: I would say that just knowing that a set is faster than a list is enough.
    In some cases, instead of sourcing, you could just use a set. Sometimes people
    do that.
  sec: 2083
  time: '34:43'
  who: Roksolana
- header: Database recommendations
- line: "When it comes to databases \u2013 what kind of databases would you recommend\
    \ to learn? Just pick any, or?"
  sec: 2093
  time: '34:53'
  who: Alexey
- line: "I think that PostgreSQL is probably the easiest one to start. Or MySQL. There\u2019\
    s not that much difference between the two. I would say that it's also nice to\
    \ have at least one no-SQL database, just to understand how it's different from\
    \ SQL databases. It becomes easier to switch to something else."
  sec: 2103
  time: '35:03'
  who: Roksolana
- line: Which one would you recommend? Mongo or?
  sec: 2121
  time: '35:21'
  who: Alexey
- line: I guess Mongo is easier to start. I had a lot of fun with Neo4j, but it's
    very specific. Not that many people use it.
  sec: 2126
  time: '35:26'
  who: Roksolana
- line: "Neo4j is a graph database, right? Then you also have some Mongo \u2013 I\
    \ think it's called Document Database. There are so many no-SQL databases \u2013\
    \ there\u2019s this Document Database, databases like Mongo, CouchDB. You also\
    \ have Key Value Databases. Maybe it's a good idea to try to play with at least\
    \ one, or?"
  sec: 2132
  time: '35:32'
  who: Alexey
- line: Yeah. Just to understand why it's called no-SQL. Because when you just hear
    about them, it's hard to understand and map it to reality.
  sec: 2155
  time: '35:55'
  who: Roksolana
- header: Data engineering and infrastructure
- line: "Now from the infrastructure side of things. I think you mentioned that data\
    \ engineers need to know networking and things like that. But when it comes to\
    \ data scientists who want to transition, they maybe don't need to get into the\
    \ nitty-gritty of networking and know the famous \u201COCI stack\u201D? Maybe\
    \ they don't need to know all the seven layers by heart."
  sec: 2167
  time: '36:07'
  who: Alexey
- line: But what kind of things do they need to know from the infrastructure point
    of view? Things that they can learn to know a bit of data engineering and to be
    successful in that.
  who: Alexey
- line: I think Docker is a must. Because data scientists also use Docker, as far
    as I know, for at least testing or deploying. Also some tools like cloud services,
    which would help understand this abstraction on top of the hardware. Cloud services
    like AWS, Lambda or something like that. I would also recommend Kubernetes, but
    it has a relatively high learning curve, so it's not for everyone in terms of
    starting out. But it's necessary to use Kubernetes. It's becoming more and more
    popular. I would recommend trying now to learn that.
  sec: 2205
  time: '36:45'
  who: Roksolana
- line: What's the easiest way to try out Kubernetes?
  sec: 2245
  time: '37:25'
  who: Alexey
- line: "I think just installing it and trying it out. Even having a small cluster\
    \ with one node and setting up something and seeing how it works. For me, it\u2019\
    s most interesting if it\u2019s more connected to my work. When I was just setting\
    \ up databases, it was kind of interesting, but it's not really practical if you\
    \ don't have to use that in your work. But in data science or data engineering,\
    \ sometimes you have to deploy some pipelines using Kubernetes. Trying that out\
    \ can help to actually learn that as a framework and the pipeline. It helps to\
    \ get a better understanding of how it works behind the scenes. For example, Spark\
    \ in Kubernetes is quite useful for future understanding of how Spark would work\
    \ with other providers of the data."
  sec: 2250
  time: '37:30'
  who: Roksolana
- line: "If a data scientist or analyst wants to transition to data engineering \u2013\
    \ first, they need to know the basic data structures: lists, sets, maps, etc.\
    \ Then they need to pick up one relational database, PostgreSQL or MySQL. Then\
    \ they need to pick one no-SQL database, for example, Mongo \u2013 and play around\
    \ with it. Also, they need to try to understand what kind of categories there\
    \ are in no-SQL databases. We mentioned document, key value, etc. Then from the\
    \ infrastructure side, they need Docker, Cloud, and maybe to play around with\
    \ Kubernetes. Even though there is a high learning curve, it's still useful to\
    \ try it. As you said, you can just install it locally and play with it. Right?"
  sec: 2298
  time: '38:18'
  who: Alexey
- line: Yeah.
  sec: 2348
  time: '39:08'
  who: Roksolana
- header: Monitoring and alerts
- line: "Another question we have is, \u201CHow do you deal with data quality checks?\
    \ What kind of monitoring do you recommend setting up?\u201D"
  sec: 2349
  time: '39:09'
  who: Alexey
- line: "I would say you would need to set up monitoring of how the data flows in\
    \ the pipelines. For example, monitoring that \u201CToday, there is no data in\
    \ this pipeline.\u201D or \u201CThere is too much data \u2013 more than you expected.\u201D\
    \ In other words, monitoring spikes in the data. This is also important because\
    \ it helps to optimize pipelines in the future. It would also be good to monitor\
    \ the schema changes, at least because monitoring data changes is way too complicated.\
    \ But monitoring schema changes is quite helpful."
  sec: 2368
  time: '39:28'
  who: Roksolana
- line: "Schema changes? What\u2019s that?"
  sec: 2402
  time: '40:02'
  who: Alexey
- line: "For example, in some data formats \u2013 like Avril, Parquet, or ProtoBuf\
    \ \u2013 they have either separate files with schema, or they are defined in such\
    \ a way that you can get it separately aside from the data, and track whether\
    \ it changed or it didn't change."
  sec: 2404
  time: '40:04'
  who: Roksolana
- line: Like if someone renamed a field, for example, or removed it?
  sec: 2422
  time: '40:22'
  who: Alexey
- line: Yeah. Or if someone renamed something, which also happens. We had a case like
    that and it simply was very not cool.
  sec: 2425
  time: '40:25'
  who: Roksolana
- line: "If that happens \u2013 if the schema changes \u2013 if somebody renamed something,\
    \ what do you do? Do you just send an alert and abort your job?"
  sec: 2433
  time: '40:33'
  who: Alexey
- line: "In that case, we didn't have a setup for CSV files, because they just have\
    \ this header and we just noticed that the pipeline doesn't return the same results\
    \ as it used to \u2013 it wasn\u2019t the same amount of data and it gave some\
    \ empty values. Therefore, the bug was because some naming changed."
  sec: 2441
  time: '40:41'
  who: Roksolana
- header: Do data scientists need to set up monitoring?
- line: I guess this kind of monitoring is more on the data engineers. Do data scientists
    also need to do a bit of monitoring for their jobs?
  sec: 2460
  time: '41:00'
  who: Alexey
- line: I think they can just do monitoring in terms of whether the model returns
    results and whether it produces expected results. I would say that another part
    would be monitoring in terms of resources. Something like that would be more on
    the data engineers or machine learning engineers. At least that's the way it works
    in another team, where the data scientists are in my company,
  sec: 2471
  time: '41:11'
  who: Roksolana
- line: "Do you think the tools you would use are the same? That data scientists and\
    \ data engineers would use the same tools? Or are they different \u2013 the tools\
    \ for monitoring quality?"
  sec: 2494
  time: '41:34'
  who: Alexey
- line: I think that it could be the same. For example, some alerts or metrics-gathering
    for something either regional, like dashboards with Grafana, or other tools, or
    Tableau. I think it's quite universal in this case.
  sec: 2505
  time: '41:45'
  who: Roksolana
- header: Do data engineers depend on data scientists for something?
- line: "We have an interesting question. As you said \u201CData scientists depend\
    \ on data engineers.\u201D Let's say a data scientist needs a new field, they\
    \ would open a Jira ticket for data engineers to this. Is there anything for which\
    \ data engineers depend on data scientists?"
  sec: 2524
  time: '42:04'
  who: Alexey
- line: "I think it depends on the workload. For example, if you would need to get\
    \ the results of the models in some way, we will definitely depend on data scientists.\
    \ Right now we depend on either the source of data, which is third-party clients,\
    \ or the database where another team pushes the data through. We kind of already\
    \ depend on another team. But on the data scientists side? Definitely, if you\
    \ need to get the data from them. For example, the case that we described with\
    \ recommendations \u2013 if you want to build some reports from it. Before that,\
    \ we need to do some transformations for other people, such as analysts, and therefore\
    \ it would depend on the result of the model."
  sec: 2546
  time: '42:26'
  who: Roksolana
- line: But I guess what happens more often is that data scientists depend on data
    engineers. Because to train a model, you need to have some data and if you don't
    have data engineers, you don't have data. Otherwise data scientists have to somehow
    get this data. Because of this dependence on data, it happens more often that
    the data scientists depend on data engineers. Would you agree?
  sec: 2588
  time: '43:08'
  who: Alexey
- line: Yeah, exactly.
  sec: 2614
  time: '43:34'
  who: Roksolana
- header: Data documentation
- line: "We have a question about data documentation, \u201CHow do you maintain data\
    \ documentation? Do you think it's important to have it and what would be your\
    \ recommendation there?\u201D"
  sec: 2617
  time: '43:37'
  who: Alexey
- line: "I would say it's important just in general to have it. But a lot of people\
    \ don't like to create documentation. Therefore, I noticed that it's important\
    \ in many companies, especially outsourcing companies. If you have a fixed-time\
    \ project or just don't have time for documentation, which can also happen. In\
    \ general, I would say that it's important to have some schemas documented at\
    \ least. We do that in terms of the fields, like \u201CWhat is this field? What\
    \ does this table have? What kind of data is stored here?\u201D There are examples\
    \ of values for each field, which is also helpful if you see some anomalies there\
    \ or it\u2019s just helpful for testing and having expectations in terms of these\
    \ values. Yeah, I would say that it\u2019s important to document schema or just\
    \ documentation in terms of what happens inside of the pipeline."
  sec: 2630
  time: '43:50'
  who: Roksolana
- header: Documentation tools
- line: What tools do you use for that? Would you just create an Excel spreadsheet
    with that or maybe use a specialized tool for this?
  sec: 2681
  time: '44:41'
  who: Alexey
- line: "For schema documentation, we use hype SQL files description. So this would\
    \ be things like the description of each field, the name, and the type. As for\
    \ the pipelines documentation, it's in Confluence\u2013 just documents with some\
    \ graphs or schemas, if it's necessary."
  sec: 2694
  time: '44:54'
  who: Roksolana
- line: "These hype SQL files, I think this documentation is optional. But you say\
    \ that, \u201COK, it's our standard that we put documentation there.\u201D Is\
    \ that right? And then you generate documentation on these files."
  sec: 2713
  time: '45:13'
  who: Alexey
- line: "Yeah, in such situations, it\u2019s our decision to build this data governance\
    \ solution so that we have a better understanding of what kind of data we process\
    \ and what kind of data we have. Instead of just multiple people having multiple\
    \ tables and no one knows what's in there."
  sec: 2728
  time: '45:28'
  who: Roksolana
- line: I assume the data scientists also produce a lot of data, or rather their models
    produce data. They also need to document this data, right? Do they use the same
    tools for that?
  sec: 2746
  time: '45:46'
  who: Alexey
- line: Yeah. They just use the same type description or documentation in Confluence.
  sec: 2759
  time: '45:59'
  who: Roksolana
- line: So you have a central place for documentation for your data and the data that
    data scientists produce?
  sec: 2765
  time: '46:05'
  who: Alexey
- line: Yeah.
  sec: 2773
  time: '46:13'
  who: Roksolana
- header: How much data engineering should a data scientist know?
- line: "We have a question from Akshot. \u201CHow much data engineering should one\
    \ ideally know?\u201D I think we've covered that a bit. Yeah, we talked about\
    \ how much data engineering skills data scientists need to know, ideally. We were\
    \ talking more about something like, \u201Cif a data scientist wants to transition\
    \ into data engineering.\u201D But to be able to successfully do work as data\
    \ scientists, what kind of data engineering skills should they have?"
  sec: 2774
  time: '46:14'
  who: Alexey
- line: I would say that good coding skills are also important. I know that some data
    scientists are somewhere in the mathematical side, and they are more interested
    in building algorithms rather than writing code. It actually influences the quality
    of the creation. Because they can either build everything in one notebook, and
    it would be hard to deploy it in some meaningful way. Or they would build the
    whole solution with libraries and classes in Python, maybe object-oriented programming.
    This would be more of a software-engineering way to do things. I think that data
    scientists need to know databases as well, because they need to read the data
    or write some results there.
  sec: 2818
  time: '46:58'
  who: Roksolana
- line: "Okay, so basically, \u201Cimprove your software engineering skills.\u201D"
  sec: 2859
  time: '47:39'
  who: Alexey
- line: Yeah.
  sec: 2863
  time: '47:43'
  who: Roksolana
- line: I think the trend that I see now in most companies is that data scientists
    are required to be good developers as well. Maybe they don't need to be as good
    as software engineers, but they need to be decent with coding.
  sec: 2866
  time: '47:46'
  who: Alexey
- line: There's a comment about getting started with Kubernetes. There is a good resource
    for that called Katacoda. I think I saw it before. Have you seen it? Katacoda?
  who: Alexey
- line: Yeah, I tried it once. In the beginning, it's quite useful. You can just try
    out different commands and see what happens.
  sec: 2898
  time: '48:18'
  who: Roksolana
- header: Trying out Kubernetes
- line: "I think I saw one with Kubernetes and I think one with Kubeflow. It's pretty\
    \ cool. They just set up a local Kubernetes for you in a browser. And then in\
    \ this browser, you get a terminal \u2013 like a Linux terminal. You have KubeCTL\
    \ there with these Kubernetes and they basically tell you what you should do,\
    \ like \u201CExecute this command. Execute that command.\u201D And then you get\
    \ this feeling of satisfaction from it."
  sec: 2906
  time: '48:26'
  who: Alexey
- line: "Also, Google Cloud sometimes has some Code Labs. They have documentation,\
    \ for example, of Kubeflow, where you can try out on each step. Some of them are\
    \ free, so it's possible for anyone to use them. Databricks has trainings as well,\
    \ but they are usually paid. Sometimes they allow people to use some of them for\
    \ free if it\u2019s for some conference attendance. Lately, Spark on it is free,\
    \ and people who attend the summit can use some of these trainings for free."
  sec: 2937
  time: '48:57'
  who: Roksolana
- header: "Choosing a path for graduates \u2013 engineering or science?"
- line: "There is a question that I wanted to ask you \u2013 I just remembered it.\
    \ Let's say I am graduating from a university. So I'm studying computer science.\
    \ I graduated from university, I studied computer science. Now I need to make\
    \ a choice. What kind of position do I want to take? Do I want to do data science\
    \ or I want to do data engineering? Which path would you recommend and why? Maybe\
    \ you can also suggest how people can find out what they're more interested in?"
  sec: 2969
  time: '49:29'
  who: Alexey
- line: "Yeah. Exactly. I would suggest first finding out what's more interesting\
    \ to the person. I personally chose big data engineering because for me, data\
    \ science was a bit \u2018not determined\u2019. I think that software engineers\
    \ would understand me. It's hard sometimes to explain why a machine learning model\
    \ does what it does and why these results are this way. Big data engineering is\
    \ more like software engineering \u2013 it's more determined. For me, I was just\
    \ interested in software engineering in general. I wanted to work with some different\
    \ tools and different tasks. Therefore, big data engineering is a great way for\
    \ people who are getting bored of backend engineering or they can just go right\
    \ from the university and learn more of big data and go into big data engineering.\
    \ If the person is more interested in building algorithms, like mathematics, or\
    \ machine learning, or just building \u201Cfashionable\u201D things, like computer\
    \ vision or deep learning, then it would be a good idea to start with data science."
  sec: 3013
  time: '50:13'
  who: Roksolana
- header: Project recommendations  to see if you like data engineering
- line: "Is there any project you would recommend that people try in order to understand\
    \ if they like data engineering or not? It sounds cool, right? If you look, people\
    \ say, \u201CHey, data engineers are so important. Data scientists really depend\
    \ on them.\u201D And many people think, \u201COkay, it's cool. I want to become\
    \ a data engineer.\u201D But maybe they don't really understand what this work\
    \ requires. Do you have any ideas about maybe a small project that they can do\
    \ to try to find out if they like doing this kind of stuff or not?"
  sec: 3076
  time: '51:16'
  who: Alexey
- line: "I would say even building a simple word count and getting some transformations\
    \ on that would be a good start. You could build it in a more complicated way\
    \ and trying to improve it with each step and build the pipeline around it. There\
    \ are so many ways you can do that. Either using HDFS, like MapReduce Standard,\
    \ or Spark and then try to optimize some algorithms. There\u2019s a project that\
    \ I enjoyed working on \u2013 I was at university and was just working with streaming\
    \ data. For example, Twitter has an open API. You could just read the data and\
    \ build some analytics on top of that. For example, \u201CHow many users tweet\
    \ about this?\u201D \u201CHow many users tweet from this location or another one?\u201D\
    \ It's quite fun in terms of seeing the results and getting to know how some frameworks\
    \ work. You can just deploy it or write the results somewhere, which is a great\
    \ practical way to see how it works."
  sec: 3109
  time: '51:49'
  who: Roksolana
- line: "About this Twitter project \u2013 you have a stream of data from Twitter,\
    \ you build a streaming pipeline to processes this data, and then display it in\
    \ real time on some sort of a dashboard?"
  sec: 3163
  time: '52:43'
  who: Alexey
- line: Yeah, I used Elasticsearch, which was quite easy to connect to Spark. You
    just dump the data into Elasticsearch and have it displayed in Kibana. This is
    easy to try and also to visualize results of work quickly.
  sec: 3176
  time: '52:56'
  who: Roksolana
- line: "That\u2019s a cool project. For the word count, you just take a text document\
    \ and you count how many times each word appears, right? Do you know any documents\
    \ that people can take to do this?"
  sec: 3191
  time: '53:11'
  who: Alexey
- header: Dataset sources
- line: "I think there are plenty of data banks with some texts. A typical example\
    \ is some Shakespeare works, but maybe it's more interesting to take some big\
    \ article, so that you have more data to process. Or you could even take some\
    \ scientific article as well \u2013 get some words from there and analyze that."
  sec: 3208
  time: '53:28'
  who: Roksolana
- line: "Well, Shakespeare I think is the opposite of the big data, right? How many\
    \ kilobytes are there? Even though he might have been a productive writer, but\
    \ it\u2019s not really big data scales. One thing I know people could do is to\
    \ process Wikipedia. It's also a bit challenging because Wikipedia gives you just\
    \ one big XML file that you need to figure out how to process. But I guess this\
    \ is the kind of thing that a big data engineer would need to enjoy doing. If\
    \ you enjoy figuring out \u201COkay, I have this big XML file. How do I actually\
    \ read it?\u201D then you\u2019re probably into data engineering."
  sec: 3232
  time: '53:52'
  who: Alexey
- line: "Then there is a data set \u2013 maybe you\u2019ve heard of it \u2013 it\u2019\
    s called CommonCrawl. I think they just get a copy of the internet. There is a\
    \ crawler and then they go on the internet and save all the pages they see. You\
    \ can just download these pages and every month they generate terabytes, or maybe\
    \ even petabytes, of data."
  who: Alexey
- line: Also, there are sometimes some scientific open API's. I found a NASA API about
    their discoveries or some results from their researches. Some data from Mars can
    be found, in terms of a topic.
  sec: 3305
  time: '55:05'
  who: Roksolana
- line: Data from Mars? So they publish all the data from Mars.
  sec: 3323
  time: '55:23'
  who: Alexey
- line: I think partially. Not all of the data, but they publish some data from various
    researches.
  sec: 3327
  time: '55:27'
  who: Roksolana
- line: Wow, that's cool. Do you know if they publish it in real time? No?
  sec: 3334
  time: '55:34'
  who: Alexey
- line: Yeah, I think some of them are in streaming because I was looking at the time
    into streaming API's.
  sec: 3339
  time: '55:39'
  who: Roksolana
- line: "How cool would it be to build a streaming pipeline to actually get data from\
    \ Mars and process it? Maybe it's not super high volume, but it\u2019s quite cool."
  sec: 3345
  time: '55:45'
  who: Alexey
- line: Also, it's possible to just parse some social media sites. Instagram, for
    example, has an API. So you could parse some information about the posts or from
    Facebook.
  sec: 3357
  time: '55:57'
  who: Roksolana
- header: Pre-built tools vs hiring a data engineer
- line: Right. So in social media, there is so much data to take advantage of. We
    still have some time and we have quite a few questions.
  sec: 3368
  time: '56:08'
  who: Alexey
- line: "One question is, \u201CWhat are your thoughts on companies that use tools\
    \ for ETL instead of hiring data engineers? And what are the advantages of outsourcing\
    \ this to these companies and these pre-built tools, or hiring data engineers\
    \ and building your own data pipelines?\u201D"
  who: Alexey
- line: "I can say that I have some attitude towards that. I think that is just one\
    \ way to solve an issue. I would say that I noticed this approach for startups\
    \ or projects that have a fixed amount of time and need to deliver something real\
    \ quick and get the results real quick as well. In such cases the pre-built approach\
    \ works really well, because you can just build an AWS or Google pipeline that\
    \ has all their services, like constructor details. That's it. I would say that\
    \ it doesn't really scale well, however. After some time, there\u2019s always\
    \ something that should be customizable in each product. Sometimes you have new\
    \ features of a product, new parts of a product, and therefore you can\u2019t\
    \ just rely on the cloud services. So this approach usually works on smaller scales.\
    \ That\u2019s my opinion."
  sec: 3402
  time: '56:42'
  who: Roksolana
- line: "I remember there's a tool from Microsoft that has this drag-and-drop feature.\
    \ You just drag-and-drop these boxes, which are components, and you connect them\
    \ with arrows. To add a deduplication step, for example, you just drag and drop\
    \ \u2018deduplication\u2019. Then you also can do this with fuzzy lookup. You\
    \ can build pipelines that are quite complex there. I guess at some point they\
    \ become less flexible, right?"
  sec: 3453
  time: '57:33'
  who: Alexey
- line: Yeah.
  sec: 3483
  time: '58:03'
  who: Roksolana
- header: Challenges in the work of a data engineer
- line: "A question from Less, \u201CWhat are the most challenging tasks for data\
    \ engineers in their daily work?\u201D"
  sec: 3485
  time: '58:05'
  who: Alexey
- line: "One of those is deduplication of data. Sometimes it can be quite a complex\
    \ condition in terms of how we want to track this deduplication. Another one,\
    \ which I often have to do, is historical data processing. It's usually for batch\
    \ jobs. For example, there was some mistake one month ago in the data, or something\
    \ changed, and you need to go back in time and remove these data and reprocess\
    \ it back. It's complicated because it's always very customizable in comparison\
    \ to just running a job. You have to set up some data limits, the ways you want\
    \ it to go back, the ways the solution changes. Then you also have to see that\
    \ it actually works well and that you don't need to do that again. It's very resource-consuming\
    \ because it usually consumes big periods of time \u2013 at least a week, or sometimes\
    \ months, or more than that."
  sec: 3496
  time: '58:16'
  who: Roksolana
- line: "Yeah. This historical data reprocessing \u2013 do you have a way of dealing\
    \ with this? Like a standard approach? Or you do something different every time?"
  sec: 3555
  time: '59:15'
  who: Alexey
- line: Yeah, there is a standard approach, but I would say that it currently has
    a lot of manual steps. We are on the path of trying to eliminate that. Some of
    those steps require some work from the infrastructure side because in some systems
    where you need to delete the data. Your infrastructure team hates when this happens
    because it's quite risky to delete some data in production systems and rewrite
    it.
  sec: 3569
  time: '59:29'
  who: Roksolana
- line: Yeah we had a talk recently in DataTalks.Club about that. I think it was called
    Data Historization, which allows us to actually do this. For those who are interested
    you can check. But it's indeed a complex topic. I remember there was one slide
    with the organism that describes the process and it's quite complicated.
  sec: 3597
  time: '59:57'
  who: Alexey
- line: "Delta Lake helps now with Spark for tracking versions of data, which we're\
    \ also trying to use to automate and see how the data changes. You can kind of\
    \ travel back in time to different versions of data there. So it\u2019s really\
    \ useful."
  sec: 3625
  time: '1:00:25'
  who: Roksolana
- header: Recommended courses and books for data scientists
- line: "Maybe one last question for you \u2013 \u201CDo you know any course about\
    \ data engineering that could be useful for data scientists?\u201D"
  sec: 3640
  time: '1:00:40'
  who: Alexey
- line: "I would say that there is one specialization I would recommend \u2013 Big\
    \ Data on Coursera \u2013 it\u2019s just called Big Data Specialization. That's\
    \ the one I started from. It was really great because the first course in the\
    \ specialization is purely theoretical. So if the person doesn't want to go into\
    \ specific practical tasks, they can just go through the first course where all\
    \ the tools are explained and the kind of tasks that data engineers do \u2013\
    \ they explain everything.  It gives a great understanding and perspective of\
    \ how everything works. The next courses are more practical and have specific\
    \ tools and solid specific tasks."
  sec: 3652
  time: '1:00:52'
  who: Roksolana
- line: Thank you. Do you have any last words?
  sec: 3691
  time: '1:01:31'
  who: Alexey
- line: Just in general, I also would suggest reading books as well. I find that it
    gives a deeper understanding sometimes than courses or lectures. There are a lot
    of books on Spark or Big Data in general, which cover quite a lot.
  sec: 3696
  time: '1:01:36'
  who: Roksolana
- line: Any specific book that you would recommend?
  sec: 3714
  time: '1:01:54'
  who: Alexey
- line: "Specifically, I enjoyed Spark books, like High Performance Spark or Learning\
    \ Spark. On big data there\u2019s this book by\u2026 I don\u2019t remember the\
    \ name \u2013 it's called Data Intensive Workloads, something like that."
  sec: 3716
  time: '1:01:56'
  who: Roksolana
- line: Building Data Intensive Applications, right?
  sec: 3734
  time: '1:02:14'
  who: Alexey
- line: Yeah. Something like that. Yeah.
  sec: 3735
  time: '1:02:15'
  who: Roksolana
- line: It has a pig on the cover.
  sec: 3736
  time: '1:02:16'
  who: Alexey
- line: Yeah. There are a lot of great books on that.
  sec: 3739
  time: '1:02:19'
  who: Roksolana
- line: The author is Martin Kleppmann. Designing Data-Intensive Applications. That's
    a good book.
  sec: 3742
  time: '1:02:22'
  who: Alexey
- line: How can people find you?
  who: Alexey
- line: "I am on Twitter, LinkedIn. Also, you can find my talks on YouTube, because\
    \ most of them are recorded. They\u2019re about big data or about Kubernetes as\
    \ well."
  sec: 3754
  time: '1:02:34'
  who: Roksolana
- line: And Alice.
  sec: 3764
  time: '1:02:44'
  who: Alexey
- line: Yeah. [laughs]
  sec: 3765
  time: '1:02:45'
  who: Roksolana
- line: Alice and Kubernetes.
  sec: 3767
  time: '1:02:47'
  who: Alexey
- line: Yeah. Thanks a lot for joining us today and for sharing your knowledge with
    us. And thanks everyone for joining us and asking questions. I just want to remind
    you that tomorrow, we have the last day of this conference. We will talk about
    building a machine learning startup. So don't forget to check it out. I guess
    that's all thanks.
  sec: 3768
  time: '1:02:48'
  who: Alexey
- line: Thank you. I enjoyed it.
  sec: 3737
  time: '1:02:17'
  who: Roksolana
- line: Yes, me too. Have a great evening.
  sec: 3799
  time: '1:03:19'
  who: Alexey

---

Links:

* [Roksonala's Twitter](https://twitter.com/dead_flowers22){:target="_blank"}
* [Roksonala's LinkedIn](https://www.linkedin.com/in/roksolanadiachuk/){:target="_blank"}

