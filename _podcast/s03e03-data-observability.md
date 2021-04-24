---
title: "Data Observability: The Next Frontier of Data Engineering"
short: "Data Observability: The Next Frontier of Data Engineering"
guests: [barrmoses]

image: images/podcast/s03e03-data-observability.jpg

season: 3
episode: 3

ids:
  youtube: TrMG1SOqZkQ
  anchor: Data-Observability---Barr-Moses-evghmh

links:
  youtube: https://www.youtube.com/watch?v=TrMG1SOqZkQ
  anchor: https://anchor.fm/datatalksclub/episodes/Data-Observability---Barr-Moses-evghmh
  spotify: https://open.spotify.com/episode/48QcLAw2I1apC1jeo8e1sd
  apple: https://podcasts.apple.com/us/podcast/data-observability-barr-moses/id1541710331?i=1000518351217

transcript:
- line: This week we will talk about data observability and we have a special guest
    today, Barr. Barr is a CEO and co-founder of Monte Carlo which is a data reliability
    company. She has experience with building data and analytics teams, working as
    a management consultant, doing research as a research assistant and even working
    in Israeli air force. Welcome.
  sec: 108
  time: '1:48'
  who: Alexey
- line: Hi! Thanks for having me. It is great to be here.
  sec: 138
  time: '2:18'
  who: Barr
- header: "Barr\u2019s background"
- line: Thanks for coming. Before we go into our main topic of data observability,
    maybe we can talk a bit about your background. Can you tell us about your career
    journey so far?
  sec: 140
  time: '2:20'
  who: Alexey
- line: As you mentioned I was actually born and raised in Israel. I started my career
    in the Israeli air force, I was commander over a data analyst unit. I moved to
    the bay area about a decade ago, so I am located in San Francisco in California.
    I studied math and statistics, that is my background in data as well. And working
    as a management consultant, I worked a lot with data science teams, working with
    fortune 500 companies under strategy and operations.
  sec: 153
  time: '2:33'
  who: Barr
- line: "Then most recently I joined a company called GainSight \u2014 a customer\
    \ data platform, which created the customer success category. At GainSight I actually\
    \ built and led the team that was responsible for our customer data. So GainSight\
    \ on game sites, we called it \u201CGONG\u201D for short \u2014 that was our nickname\
    \ for it. We helped our customers use data to grow their businesses with their\
    \ customers. Throughout that experience, leading the team that are responsible\
    \ for customer data and analytics, I realized how big of an issue is\u2026 some\
    \ of the very fundamentals around data. As companies try to become data driven\
    \ and rely on data, they actually run into what I call \u201Cdata downtime\u201D\
    . We will talk a little bit about that later, but that is when I first encountered\
    \ it."
  who: Barr
- line: "That got me thinking how is it that we are so advanced in data and yet there\
    \ are some things that we have not figured out. So I started Monte Carlo with\
    \ the goal of helping organizations use data, adopt data, become data-driven by\
    \ minimizing what I think is the biggest problem \u2014 the biggest hurdle which\
    \ is data downtime. It is a big pleasure for us to work with some amazing companies\
    \ on helping them solve this problem and helping achieve data reliability."
  who: Barr
- header: Market gaps in data reliability
- line: "You were leading analytics teams and you were working closely with data and\
    \ you noticed, \u201Cokay we have some ideas how to process this data but when\
    \ something breaks then things go wrong\u201D. That led you to realizing, okay\
    \ there is a gap in the market that you could fill. This is why you created the\
    \ company. Right?"
  sec: 275
  time: '4:35'
  who: Alexey
- line: "Let me describe to you a scenario that I am sure is familiar to anyone data\
    \ and potentially in engineering as well. It is always like on a Friday evening,\
    \ at 6:00 p.m., five minutes before you are just about to log out, something hits\
    \ you. Like a customer reaches out and says \u201Chey the data here looks really\
    \ wrong, what is going on\u201D. You are literally just leaving the office, just\
    \ about to sign off, and then suddenly something blows up. Or five minutes before\
    \ a really important board meeting, the CEO pings you and says \u201Chey the graph\
    \ here, something with the numbers that I am showing just looks off, what is going\
    \ on\u201D. Then it starts to scramble of what went wrong and where the report\
    \ is refreshed. Did all the data arrive? Did someone make a schema change somewhere,\
    \ that messed everything downstream?"
  sec: 300
  time: '5:00'
  who: Barr
- line: "It started this guessing game of what is going on. So there are a few problems.\
    \ One \u2014  data teams are often the last to know about these issues. They often\
    \ find out about these problems from consumers of data: executives or business\
    \ units or consumers or actually users of your product. Second, it often takes\
    \ ages to understand what the problem is and identify the root cause. Our systems\
    \ are so complex today that the ability to pinpoint the root causes is extremely\
    \ complicated, especially when done in a manual way."
  who: Barr
- line: "Seeing this problem come up again and again both for myself but also for\
    \ data teams with other organizations. I was like, \u201CAre we crazy? Am I crazy?\
    \ How is it that this problem exists? How can it be that?\u201D We do not have\
    \ a better way to do this and that. Inspired by the realization that there is\
    \ a better way to do it \u2014 and the better way to do it is actually based on\
    \ best practices from engineering."
  who: Barr
- header: Observability in engineering
- line: "Speaking about best practices. I did a bit of googling before our talk today.\
    \ Data observability is based on \u201Cobservability\u201D, which is a concept\
    \ from the devops world, right? So, before we go into data observability, can\
    \ you tell us what it means in the devops world? What are the best practices you\
    \ are talking about?"
  sec: 416
  time: '6:56'
  who: Alexey
- line: "In general the data space has been evolving very quickly. We are still quite\
    \ behind in terms of methodologies and frameworks compared to engineering. It\
    \ is actually worthwhile spending time understanding what are these concepts like\
    \ devops and others in software engineering that can help us navigate the space\
    \ of data. Navigate what we want to accomplish in a better way. The idea of devops\
    \ has emerged in the last couple of decades. The underlying tech stack became\
    \ way more complicated, similarly to how they are in data. For example, for an\
    \ organization that is moving from a monolith to a microservice architecture \u2014\
    \ something that almost every organization is doing. As a result of that, there\
    \ has been the rise of devops \u2014 teams that help, have a constant pulse on\
    \ the health of their systems and make sure that all the applications and infrastructure\
    \ are up and running."
  sec: 440
  time: '7:20'
  who: Barr
- line: "As part of that Devops \u2014 the idea of observability. Observability is\
    \ this holistic view that includes monitoring, tracking, triaging of incidents\
    \ to prevent downtime of those systems. So, at its core, observability in engineering\
    \ is broken into three major pillars, metrics, logs and traces. All of these together\
    \ help us understand what is the health of the system based on its outputs. When\
    \ things are wrong, why? So, answering basic questions like, is a system healthy.\
    \ If not, what happened? When did it happen? Are there other events that are correlated\
    \ that could help us understand what is happening here? So you have systems and\
    \ software to help address the need for observability and monitoring. Every engineering\
    \ team today that respects itself has something to manage that."
  who: Barr
- line: "A solution like NewRelic or DataDog or AppDynamics or PagerDuty \u2014 all\
    \ very familiar solutions that help us answer these questions when it comes to\
    \ applications and infrastructure. So it is a very important concept in software\
    \ engineering and one that has been relied on for many years now."
  who: Barr
- header: Data downtime
- line: "You said teams were moving from monoliths to micro services. Usually micro\
    \ services are some sort of web services. Tools like DataDog, NewRelic or even\
    \ open source tools like Prometheus and grafana \u2014 they are tailored to these\
    \ kinds of applications, to web services, something that is always running. While\
    \ in the data world, we often have something different, we more often have batch\
    \ processes rather than something that is up and running all the time. That is\
    \ why we need a bit of a different approach, right?"
  sec: 589
  time: '9:49'
  who: Alexey
- line: "Exactly. It is a different approach but it is very important to do. Let us\
    \ talk about why it is very important. If you think about \u2014 I will draw the\
    \ analogy of what we call \u201Cdata downtime\u201D, explain what data downtime\
    \ and what application downtime is. If we take a specific example. If a company\
    \ \u2014 say an e-commerce company \u2014 has a particular website. A couple of\
    \ decades ago if your website was down, no one noticed because you probably had\
    \ a real shop where people actually purchased things."
  sec: 628
  time: '10:28'
  who: Barr
- line: So the website was something minor that nobody cared about. But today if your
    website is down, it is your product. You have to manage that very carefully. You
    have a commitment to like 99.99 percent uptime. Today you have all these solutions
    and many others like you mentioned to actually make sure that your website is
    always up and running.
  who: Barr
- line: "If you think about the corollary of that to data, as you mentioned. Maybe\
    \ a couple of years ago, maybe like 10 years or five years ago \u2014 who is using\
    \ your data? There is only a small handful of people. They were using data very\
    \ infrequently, maybe only once a quarter to report numbers to the street. But\
    \ in today's world, there is way more data engineers, data analysts, data scientists.\
    \ There is way more people in the organization who are using data to make decisions\
    \ to power your product and so. If the data is down, that is a big deal. Maybe\
    \ 10 years ago it was not a big deal because no one uses it. But today it is a\
    \ big deal. (Stream here goes down =))"
  who: Barr
- line: "To be honest I do not remember what you were talking about. You were saying\
    \ that data downtime is a big deal. While previously nobody cared about this,\
    \ today there are data analysts, data scientists and everyone else who is using\
    \ data. We rely on this data. And if the data is not there \u2014 I know, I work\
    \ as a data analyst [correction: data scientist], we build machine learning things\
    \ on top of data. When the data is not there, when our model stopped working,\
    \ then we started \u201Cokay what happened?\u201D. Then we see the data is not\
    \ there. Or it should be 1 million records but today we only have 10000. Where\
    \ is the rest?"
  sec: 731
  time: '12:11'
  who: Alexey
- line: These failures, they are often silent failures. If the data did not appear
    in all volume, like maybe just a fraction of it appeared and if we do not have
    monitoring to our machine learning pipeline, it looks okay. There is some data,
    let us apply the model to this data and I am done. But it is silent, we did not
    notice that something is wrong. I think you were talking about something like
    that?
  who: Alexey
- line: That is exactly right. The job is completed; it is all green, everything passed.
    But you know? You only got a small fraction of the rows that you are hoping to
    get. Or you know what job completed, you got all the data but now all the values
    are NULL suddenly. Or you got all the data but it is credit card data and suddenly
    you have values that you do not expect, like letters or something that you should
    not have there. But you never knew because the job was completed and everything
    was fine. You might just not know about it. If you are lucky, you might find out
    about it the same day. But oftentimes it can take weeks or even months until you
    realize that. Yeah, my model was operating on completely wrong data, or I was
    using data to make decisions that were just totally incomplete or actually wrong.
  sec: 820
  time: '13:40'
  who: Barr
- header: Data quality problems and the five pillars of data observability
- line: 'If we talk about the problems we have with data, about data quality problems.
    First there could be some things that are not supposed to be there, like letters
    in the numeric fields. Another problem is data is simply incomplete: we do not
    have all the rows that were supposed to be there, like instead of one million,
    we have only 100000 for example or even less than that. What are the other problems
    that we can have?'
  sec: 878
  time: '14:38'
  who: Alexey
- line: "When we first started to determine what data observability is and what it\
    \ should mean, one of the common things that we heard was, \u201Cevery data team\
    \ is different\u201D. Every data team is unique. My data can break for millions\
    \ of different reasons. There might not be even a pattern for all this. I actually\
    \ disagree with that. Before we started the company, we spoke with hundreds of\
    \ data teams to come up with a database of all the times and all the reasons when\
    \ your data goes wrong \u2014 and why? What is the root cause? What is the symptom?\
    \ And how did you identify it?"
  sec: 909
  time: '15:09'
  who: Barr
- line: What we have seen is actually there are patterns. There is a coherence set
    that you could work off, that you could instrument and monitor for. That will
    help you gain observability. Similarly to how you do that in observability for
    devops, even though your applications and your infrastructure can break for a
    million different reasons, there is still those three core pillars that we talked
    about that help engineers identify when their systems are down and so for data
    teams what are those, what is that framework, what are those metrics, and so we
    do, we define five different pillars for this and we believe that.
  who: Barr
- line: It is the three pillars you mentioned? Metrics, logs and traces. And for data
    you said there are five, right?
  sec: 989
  time: '16:29'
  who: Alexey
- line: Yes precisely. There are five that we define. We believe that if you monitor
    all of them, instrument and track those, you will get the same level of confidence
    in your data. Let us talk about which five of those are.
  sec: 998
  time: '16:38'
  who: Barr
- line: "The first one is freshness. Let us say we have a table that gets updated\
    \ three times an hour regularly. And then it has not been updated for a full hour.\
    \ That might be a freshness problem. There are many different ways to think about\
    \ freshness. Basically it answers the question of \u201Chow up-to-date is my data\u201D\
    ."
  who: Barr
- line: "The second pillar is volume. The volume you shared the example \u2014 \u201C\
    I expect one million rows and I am getting only 10000 rows\u201D. This tells us\
    \ the completeness of our data tables."
  who: Barr
- line: "The third pillar is distribution. Distribution looks at the range of data.\
    \ Let\u2019s say I expect a certain field to be between 5 and 15. And then suddenly\
    \ I am getting values that are in the hundreds or 200s for example. Or I expect\
    \ credit card fields suddenly get letters instead of numbers. All of these examples\
    \ would be under the distribution pillar."
  who: Barr
- line: The fourth pillar is schema. It looks at who makes changes to our data and
    when. That is both at the table and at the field level. If a table is added, removed,
    deprecated, if a field is changed in type.
  who: Barr
- line: "The fifth pillar is lineage. Lineage is basically a map \u2014 an auto discovered\
    \ or auto reconstructed map of all the dependencies, both upstream and downstream,\
    \ of your data assets. Lineage helps us answer the question of \u201Cif I have\
    \ a freshness problem in a given table, what downstream assets are impacted by\
    \ that?\u201D Maybe no one is using that table. So, I do not need to care about\
    \ that freshness problem. But maybe this actually feeds an important model that\
    \ someone is using? Or maybe this goes into a report that gets sent to a customer\
    \ regularly? What are the dependencies? And then similarly what are the upstream\
    \ root causes for these problems? What may have contributed?"
  who: Barr
- header: 'Example: job failing because of a schema change'
- line: "I recalled an example \u2014 something we had recently at work. Data changed,\
    \ schema changed. It was announced of course, in a slack channel. But of course,\
    \ I have so many slack channels open, and not all of them I read. So, I simply\
    \ missed that. Then, two weeks later, it stopped working. Then \u201Cokay what\
    \ happened?\u201D Why is the data now in the wrong format? But it was announced!\
    \ If there was something like this, like a map with downstream dependencies, then\
    \ it would have been possible to know, \u201Cokay this data source is used by\
    \ this team\u201D, and I would be one of these users of this data. Then maybe\
    \ for me, I would get a personalized alert that is saying \u201Cthe data is about\
    \ to change, you have to take action now, else in two weeks your jobs will fail\u201D\
    . This is, I guess, a good illustration of the lineage pillar, right?"
  sec: 1150
  time: '19:10'
  who: Alexey
- line: "Yeah, that is a perfect illustration of a few. It is both the schema pillar\
    \ --because there was a change in schema. And it sounds like someone manually\
    \ notified you on slack \u2014 which is very thoughtful \u2014 but maybe that\
    \ should be automated as well. Then yes, lineage \u2014 you are spot on with that.\
    \ It is a great example of how that could have helped. Then you mentioned that\
    \ it caused the data to just stop arriving."
  sec: 1225
  time: '20:25'
  who: Barr
- line: It was still arriving, just not in the format my jobs were expecting.
  sec: 1252
  time: '20:52'
  who: Alexey
- line: "Got it. In that case that might be an example of a distribution type problem,\
    \ when it is arriving in a different format. The interesting thing with data downtime\
    \ is that oftentime it includes problems from multiple pillars. Each pillar can\
    \ have multiple different problems. So when you are thinking about observability\
    \ and monitoring \u2014  all that good stuff \u2014  what you need is a system\
    \ that can detect all of these and can help you automatically draw insight from\
    \ this. Your example is spot on. I hope that was resolved quickly."
  sec: 1256
  time: '20:56'
  who: Barr
- line: "Yeah it was. I had to stop working on other things and fix that. At least\
    \ my code complained that \u201Chey something is wrong, this field is not there\u201D\
    ..."
  sec: 1230
  time: '20:30'
  who: Alexey
- line: That is how you found out about it?
  sec: 1300
  time: '21:40'
  who: Barr
- line: "Yeah. It broke \u2014 it did not work. But it could have been worse if the\
    \ script, the job kept running. Then I do not know when I would have noticed that.\
    \ Maybe one month after that."
  sec: 1302
  time: '21:42'
  who: Alexey
- line: Three pillars of observability (good pipelines and bad data)
  who: Alexey
- line: You also mentioned other things from the DevOps Observability world, like
    metrics, logs and traces. Do we still care about these things in data observability?
  sec: 1317
  time: '21:57'
  who: Alexey
- line: "Yeah, it is a great question. I would say we definitely still need to think\
    \ about them, it is just two different parts of the system. You probably cannot\
    \ run a very healthy system with only one or without the other. Oftentimes we\
    \ call it \u201Cthe good pipelines bad data\u201D problem. You might have really\
    \ reliable, great pipelines or great systems. You are still tracking the observability\
    \ from an engineering perspective. But the data itself that is running in your\
    \ pipeline is inaccurate. That is why you need data observability."
  sec: 1339
  time: '22:19'
  who: Barr
- line: "Okay. The idea here is \u2014 we still care about DevOps. We have both observability\
    \ and data observability. It does not mean that we stop caring about all the other\
    \ things and care about these five pillars. We still need to be on top of good\
    \ engineering and DevOps practices. And on top of that, so we need to take the\
    \ three DevOp Observability pillars to make sure that our systems have the observability\
    \ from the engineering point of view. But we also need to add the five pillars\
    \ of Data Observability so we have good pipelines and good data health?"
  sec: 1377
  time: '22:57'
  who: Alexey
- line: Yes, that was spot-on! We often find that data engineering teams are really
    busy. They have a lot of things to do. And we see a significant reduction in time,
    when data observability is used in practice. Things like 120 hours per week on
    average for a five person team and a reduction of almost 90 percent of data incidents.
    When you think about when teams practice data observability, you are spot on.
    We cannot use only one, we have to use both for different parts of our tech stack.
  sec: 1422
  time: '23:42'
  who: Barr
- header: Observability vs monitoring
- line: "I noticed that you often say \u201Cobservability\u201D and \u201Cmonitoring\u201D\
    . Is there any difference between these two things or are they synonyms?"
  sec: 1471
  time: '24:31'
  who: Alexey
- line: "Monitoring is a subset of observability. Observability basically tells us,\
    \ \u201Cbased on the output of a system, what is the health of that system?\u201D\
    \ Observability helps us answer questions about the health of a system based on\
    \ the results that you get in monitoring. Monitoring will tell us \u201Cthis system\
    \ is operating as expected and it is healthy\u201D, or \u201Chey there is an outlier\
    \ or a problem with the system here\u201D \u2014 like an indication of a freshness\
    \ problem. On the other hand, observability will help us answer the question of\
    \ \u201Cwhy is this all happening\u201D. With monitoring, we will see there is\
    \ a problem, but with observability we can identify what that problem is, identify\
    \ the root cause of it. Then also how it can be solved by means of answering what\
    \ downstream tables rely on that data. It can also tell if you it\u2019s an important\
    \ table to fix or if it\u2019s not a priority. So you actually need both. I see\
    \ monitoring as a part of observability that helps us answer these questions."
  sec: 1485
  time: '24:45'
  who: Barr
- header: Finding the root cause
- line: "I am just trying to think of an example. Let us say, there is a job that\
    \ is producing data and it stopped working. We have monitoring in place that says\
    \ \u201CWe expect that in this table. The data appears three times per hour, but\
    \ it has been one hour since it appeared and nothing is still there\u201D. Would\
    \ we get an alert? You get called by PagerDuty \u201CHey something is wrong with\
    \ the data!\u201D It does not tell us what went wrong \u2014 it just tells us\
    \ that something is wrong. Then using other tools and other pillars like lineage,\
    \ how do we figure out what actually went wrong? How does it work?"
  sec: 1564
  time: '26:04'
  who: Alexey
- line: The other pillars can give us clues and help us understand why this happened
    and what we can do about it. Let us say we have a strong monitoring system and
    we get an alert about a freshness problem. Then we look at that table and we see
    that three other tables downstream also had a problem. We see that those are correlated,
    they happen sequentially. That can help us give clues around what is the impact
    of this. To your point, using lineage, we can see that there are a bunch of other
    tables further downstream that rely on this. They are going to be impacted later
    today. We need to stop the data from going to those tables or we need to fix this
    immediately. That gives us clues as to how we can actually solve this.
  sec: 1630
  time: '27:10'
  who: Barr
- line: "Another example of understanding why this is happening. Let\u2019s assume\
    \ we see that there is a freshness problem. We want to look at the query logs,\
    \ we want to understand who is making updates to this table. I can actually ping\
    \ the right person or the user of this table to better understand why they are\
    \ using this table, is it important or not, when are they using it. Actually using\
    \ metadata about this data, getting data-driven about our data, can help us answer\
    \ that. The way that I think about observability is \u2014 \u201Cgetting data-driven\
    \ about data\u201D. That includes knowing when things are wrong like monitoring\
    \ but also answering a bunch of other questions too."
  who: Barr
- header: Who is accountable for data quality? (the RACI framework)
- line: "This makes me think who should be responsible for it. I imagine this setup\
    \ \u2014 there is some sort of central data platform. There are teams who publish\
    \ to this platform, there are teams who consume from this platform. I am wondering\
    \ whose responsibility is to make sure that the data is there. The platform probably\
    \ can help us with freshness. But if the producers of the data start publishing\
    \ data with errors, there should be some process that lets them know, \u201CSomething\
    \ is probably wrong\u201D. Should it be the team who implements these checks?\
    \ Or the platform tells them, \u201Chey something is wrong\u201D. How is it implemented\
    \ usually?"
  sec: 1740
  time: '29:00'
  who: Alexey
- line: "That very much depends on the maturity and the size of the data organization.\
    \ When you are a very small company and you have maybe one data engineer \u2014\
    \ the lone data engineer \u2014 he or she is typically responsible for everything.\
    \ They are going to be setting up the system, receiving the alerts, troubleshooting\
    \ it, and letting everyone know about it."
  sec: 1799
  time: '29:59'
  who: Barr
- line: "In a large company, you might have 30,000 people consuming data. And you\
    \ have a data team that is several thousands of people. We see that people are\
    \ moving towards a decentralized model of ownership. You have sub teams of data\
    \ in the data organization. Those people have ownership of that data. In those\
    \ cases, organizations actually make data observability and data monitoring self-serve.\
    \ There is typically a centralized group that is responsible for saying this is\
    \ \u201Cthe platform that we should be using for Data Observability\u201D. For\
    \ each data team, for each sub team, that sub team actually defines how they engage\
    \ or interact with that platform. That sub team will receive personalized alerts\
    \ for their data assets only."
  who: Barr
- line: "Oftentimes, as companies move from being very small to being very large,\
    \ on that trajectory, we are seeing different models along that path. I think\
    \ one of the main questions that people ask us is \u201Cwho is actually responsible\
    \ for this?\u201D and \u201Chow do we set accountability?\u201D"
  who: Barr
- line: "One of the ways that we are seeing companies deal with this is with a framework\
    \ called \u201CRACI\u201D. It helps to determine accountability in organizations.\
    \ RACI stands for \u2014 \u201CR\u201D is \u201Cresponsible\u201D \u2014 the person\
    \ who is executing on the specific task at hand. \u201CA\u201D is for \u201Caccountable\u201D\
    \ \u2014 a person whose neck is on the line. It is their main job to make sure\
    \ that the people held accountable. \u201CC\u201D is \u201Cconsulted\u201D, meaning\
    \ their opinion might count, or you would want to seek their opinion about something.\
    \ Then \u201CI\u201D is for \u201Cinformed\u201D, meaning someone needs to know\
    \ about something."
  who: Barr
- line: "For each part in the data lifecycle, you can define who is responsible, accountable,\
    \ consulted and informed. You can use that to determine what is right for your\
    \ organization. For example, for specific data observability or data quality problems,\
    \ we can say that the chief data officer or the CTO is the person who is accountable\
    \ (\u201CA\u201D). But the person who is actually solving that is the data engineering\
    \ team. The person or the organization that needs to be informed (meaning \u201C\
    I\u201D) is the data analyst team. They need to know about problems, they are\
    \ not responsible for the jobs in the pipeline specifically. You can use this\
    \ framework to help allocate who needs to do what and when, and clarify that.\
    \ So you are not in a position where there is one person doing all that."
  who: Barr
- line: "I am thinking about what I am doing. I am a data scientist and I build machine\
    \ learning models using data that other teams produce. There is a team that produces\
    \ this data source, there\u2019s a team that produces that other data source.\
    \ What I do is \u2014 I join these two data sources and build something on top\
    \ of that. In this case, I would be informed. If something goes wrong, somebody\
    \ from these teams will reach out and say \u201Csorry there is some problem with\
    \ the data\u201D. They are responsible. They are reaching out to me. The accountable\
    \ person is maybe a product manager in the team or a manager in the team. This\
    \ person would be doing communication saying \u201Chey sorry, I know you use this\
    \ data, I know you rely on this data but something happened, a server died, there\
    \ was a bug and the data is not there, sorry\u201D. The data engineers in the\
    \ meantime are trying to fix it. It also puts me in the consulted category. I\
    \ could be a stakeholder, I can say \u201Cokay what you promised this data with\
    \ a delay of one hour but this is not enough, can you make it a bit faster, with\
    \ smaller delay?\u201D If they care about my opinion, it means I am consulted,\
    \ right?"
  sec: 2022
  time: '33:42'
  who: Alexey
- line: That is right, you got it.
  sec: 2120
  time: '35:20'
  who: Barr
- header: Service level agreements
- line: "So what do we do with this? Responsible and accountable \u2014 this is the\
    \ team that actually puts the data. If I am a data scientist, I want to make a\
    \ model based on some data. I go to this team and ask what are your SLAs \u2014\
    \ \u201Cservice level agreements\u201D. Can you promise me that the data will\
    \ appear there five minutes after the user made an action? We make an agreement\
    \ between our team and the team of data engineers. Then you said, in small organizations\
    \ would be one data engineer who is doing everything. But once the company becomes\
    \ bigger we could have this centralized platform, where teams could define these\
    \ SLAs \u2014 \u201Cwe promised that the data will not be delayed more than by\
    \ five minutes\u201D, so the freshment requirement is five minutes. So there is\
    \ an agreement between us. Then they start pushing the data to the platform. And\
    \ when something goes wrong, the system alerts them and data engineers fix it."
  sec: 2124
  time: '35:24'
  who: Alexey
- line: That is exactly right.
  sec: 2209
  time: '36:49'
  who: Barr
- line: Do you want to add something there?
  sec: 2212
  time: '36:52'
  who: Alexey
- line: I think you did a great job of explaining that. I think that is perfect.
  sec: 2215
  time: '36:55'
  who: Barr
- line: Yeah. I think you are the podcast guest right now.
  sec: 2220
  time: '37:00'
  who: Alexey
- line: I know. I much prefer it when you do such a great job of explaining this.
    Yeah, that is spot on. In the same way that we have adopted observability as a
    concept, SLAs is something that is super common in engineering. We have not adopted
    it in data yet. But we can and it will be helpful for us to have that communication
    agreement. It is important because it will help your data engineering counterparts
    know what to focus and what to solve for.
  sec: 2224
  time: '37:04'
  who: Barr
- line: "Imagine that they have hundreds of tables that have freshness issues. But\
    \ there are only 10 of them where they have an SLA \u2014 a particular SLA for\
    \ freshness and timeliness that is like this five-minute window. Then they will\
    \ know to prioritize those and the rest can wait for later. It provides some agreement\
    \ between you two. And what actually matters to you and you can give the information\
    \ of these tables matter more. This data set does not matter at all. So it actually\
    \ allows us to have better communication \u2014 to also not waste our time on\
    \ things that do not matter."
  who: Barr
- header: Inferring the SLAs from the historical data
- line: "Here there are a few crucial components. The first \u2014 we need to have\
    \ this platform that allows us to define these requirements: we have these expectations\
    \ for freshness, we have these explanations for volume\u2026 Maybe for volume\
    \ we do not even need to define that? Maybe it should be like \u201Csomething\
    \ is wrong because yesterday it was that much but today it\u2019s less\u201D."
  sec: 2294
  time: '38:14'
  who: Alexey
- line: "Same for freshness, actually. Here is the cool thing \u2014 for each of the\
    \ pillars, there is a component that can be automated to begin with. I believe\
    \ we have under-invested in automation. Which is ironic. Teams are used to saying\
    \ \u201Cokay I need to define that the volume here needs to be this\u201D or \u201C\
    that the freshness needs to be\u201D to your point. But you have historical data\
    \ about that. You can infer what the volume that you expect is. You can also infer\
    \ \u201Cokay, this table is being updated three times an hour, so it should be\
    \ updated three times an hour\u201D. Obviously you can add customization on top\
    \ of that, so you can say \u201CNo, actually I want this data to arrive faster.\
    \ Can you make sure that happens?\u201D I definitely think that we need to start\
    \ with a layer of automation. Then add on top of that customization. But I would\
    \ start with what we already know about the data."
  sec: 2323
  time: '38:43'
  who: Barr
- line: "I imagine that we are not starting from scratch. There are already some processes\
    \ that push data somewhere, there are processes that read data from somewhere.\
    \ It is not like we have a blank page, right? There is already something. We can\
    \ just see \u201Cokay usually something appears here within five minutes\u201D\
    . Let\u2019s just use this as a SLA, so we can infer this from the past. But in\
    \ some cases, we should have a way to overwrite this and say \u201CLet us make\
    \ sure it appears earlier\u201D. In any way, we need to have this place where\
    \ it is possible to define this. Then we also need people who take responsibility,\
    \ they say \u201CWe are going to stick to these SLAs and if something is wrong\
    \ we are going to make sure that we recover as fast as possible\u201D."
  sec: 2388
  time: '39:48'
  who: Alexey
- line: Yeah, you can even have a monitor in your (virtual) office that shows, here
    is the SLAs and here is how well we are doing and we are crushing it.
  sec: 2443
  time: '40:43'
  who: Barr
- header: Implementing data observability
- line: 'We have these two things: the platform itself, the tool that lets us define
    all this. Then we have this framework, RACI, to identify who is responsible, so
    we have this people aspect. Do we need something else to make it work, to have
    data observability in place?'
  sec: 2463
  time: '41:03'
  who: Alexey
- line: "I would say that is a good start if you have both of those things. Maybe\
    \ the additional thing that folks do is they start defining playbooks and run\
    \ books for what happens in these instances \u2014 basically workflows. Let\u2019\
    s say, there was this table that you expected to get updated three times per an\
    \ hour and it stopped getting updated. Then there is a whole set of things that\
    \ happens. The first is \u2014 you get informed because your model relies on that\
    \ data. Then the data engineers need to take some actions in order to resolve\
    \ that. What are those actions? What exactly are they doing? What systems are\
    \ they using to look at to solve it? Who do they need to know? How do they resolve\
    \ it? All that stuff in one book."
  sec: 2487
  time: '41:27'
  who: Barr
- line: "Let\u2019s talk about how we can implement this. There is actually a question,\
    \ but I also wanted to ask this question. The question is: what are some of the\
    \ good tools in the marketplace that provide a good job in data observability?\
    \ And I think I know what you are going to say."
  sec: 2554
  time: '42:34'
  who: Alexey
- line: You have been doing a great job of that so you can go ahead and answer.
  sec: 2573
  time: '42:53'
  who: Barr
- line: Monte Carlo?
  sec: 2577
  time: '42:57'
  who: Alexey
- header: Data downtime maturity curve
- line: "I can provide an answer for what folks are doing if that is helpful. I talked\
    \ a little bit about the maturity curve \u2014 how people manage from a small\
    \ company where there is one person who is doing everything. Then there is a large\
    \ company where you might have a decentralized model, you have different ownership.\
    \ As I mentioned, we talked to hundreds of data teams, and there is a maturity\
    \ curve for how you deal with data downtime."
  sec: 2580
  time: '43:00'
  who: Barr
- line: "In the very early stage you might be in a \u201Creactive phase\u201D where\
    \ you do not have anything in place and you have disasters all the time. I remember\
    \ the CEO who told me that \u2014 back in the day when there were offices \u2014\
    \ they would walk around and put sticky notes on reports and saying \u201Cthis\
    \ is wrong\u201D, \u201Cthis is wrong\u201D, \u201Cthis is wrong\u201D. That is\
    \ a very reactive state, the first stage is."
  who: Barr
- line: "The second stage is when people start thinking about how to solve this in\
    \ a more proactive way. It\u2019s called a \u201Cproactive stage\u201D \u2014\
    \ when people put in place some basic checks. It can be just counts. I am going\
    \ to manually select a bunch of tables and make sure that they get a million rows\
    \ every day \u2014 because that is what I expect. Those teams spend a lot of time\
    \ in retros and post mortems and figuring out what is wrong."
  who: Barr
- line: "The third stage is \u201Cautomated\u201D. They recognize that a manual approach\
    \ is no longer scalable or effective. They start implementing some solutions \u2014\
    \ and we can talk about what those are."
  who: Barr
- line: "Then the fourth stage is \u201Cscalable\u201D. You have companies really\
    \ invested in both the scalable and automated solution, some of the best in class\
    \ out there. You can take a look at Netflix. They have written a lot about what\
    \ they have done for monitoring observability and detecting anomalies."
  who: Barr
- line: There are ranges from things that you can hack together or do on your own
    where you can basically use SQL or Python or Jupyter notebooks. And actually we
    put together some tutorials on this. I am happy to share the links after if that
    is helpful for creating your own monitors. The other thing that you could do is
    look at specific areas in your pipeline and define specific tests in those areas,
    like in airflow or something like that. What we are finding is that as data organizations
    start using their data and getting more serious about data downtime, they need
    a holistic approach. Whether it is an open source tool or something a bespoke
    solution that is easy to get up and running with. There needs to be something
    more holistic than a point solution.
  who: Barr
- line: "You mentioned that you at the beginning can get away with a bunch of counters\
    \ \u2014 just count how many rows appeared each hour. Then at the same time you\
    \ can check what is the timestamp of the last insert row \u2014 you can just look\
    \ at the max value of this column which will give you the freshness. I guess you\
    \ can get away with a bunch of things just using plain SQL and a bunch of Python\
    \ scripts like you said. That would put you to the proactive stage in this maturity\
    \ curve or already automated?"
  sec: 2765
  time: '46:05'
  who: Alexey
- line: I would say somewhere between the proactive stage. That is still pretty ad
    hoc.
  sec: 2814
  time: '46:54'
  who: Barr
- header: 'Monte carlo: data observability solution'
- line: "We need some sort of holistic picture. How do we get it? If all we have is\
    \ a bunch of ad-hoc stuff put together with a duct tape. It does some sort of\
    \ alerting already, maybe there is an email to some of the people, hopefully.\
    \ Or a slack message from a bot. That is already quite good. But how do we go\
    \ even further \u2014 how do we go to the automated phase?"
  sec: 2820
  time: '47:00'
  who: Alexey
- line: "In that case you will need an observability solution. Full disclosure \u2014\
    \ Monte Carlo \u2014 we have built a strong observability platform. That is the\
    \ core of what we do. Some of the characteristics that are important for a strong\
    \ observability solution. One it needs to give you end-to-end visibility. It needs\
    \ to connect to whatever your data stack is, including your data lake, your data\
    \ warehouse, your ETL and your BI or your machine learning models. If you are\
    \ just doing row counts and there are only a handful of tables in your data warehouse,\
    \ it is probably insufficient. You are relying on data arriving on time in other\
    \ areas and a lot of the data moving in different systems. If I were to choose\
    \ an observability solution, it would be one that can actually connect to my existing\
    \ stack end-to-end. It\u2019s important to choose a solution that automatically\
    \ learns your environment and your data."
  sec: 2853
  time: '47:33'
  who: Barr
- line: We talked earlier about whether you manually define the thresholds or you
    rely on automation. We are not starting from scratch. Solutions that can do the
    instrumentation for you and start the monitoring for you, using machine learning
    models based on historical data, I think that puts you at an advantage.
  who: Barr
- line: "Another key point is minimizing false positives. Data teams often have alert\
    \ fatigue. If you have a system that can take into account not only the data but\
    \ also metadata and think holistically about this \u2014 about the five pillars.\
    \ Each one is important. It has to include things like lineage. It can help minimize\
    \ false positives and give you rich context about each of the incidents. Then\
    \ you know whether you should take action on it.There are certain criteria that\
    \ you should look for when you are thinking about the data observability solution.\
    \ That is the way to improve health overall and move up in the maturity curve."
  who: Barr
- header: Open source tools
- line: Are there some open source tools for that?
  sec: 2992
  time: '49:52'
  who: Alexey
- line: "There is open source for different specific solutions \u2014 for each of\
    \ the pillars. But not one that does comprehensive for all of those five pillars."
  sec: 2996
  time: '49:56'
  who: Barr
- line: "I think the most difficult thing in my opinion is lineage \u2014 defining\
    \ all these dependencies. Is there a good tool for that?"
  sec: 3008
  time: '50:08'
  who: Alexey
- line: "They are different levels of lineage. For example airflow provides job level\
    \ lineage. But for table level and field level lineage, something that automatically\
    \ reconstructs that... I actually have not seen a very strong one. I am curious\
    \ to hear if there is anything that I haven\u2019t seen."
  sec: 3024
  time: '50:24'
  who: Barr
- header: Test-driven development for data
- line: We have a couple of questions from the audience. Maybe we can go through for
    them. RK is asking if any good approaches on test driven development in the data
    space. And does it [TDD] have anything to do with data observability?
  sec: 3052
  time: '50:52'
  who: Alexey
- line: "Can you say it again? I don\u2019t think I got the first part."
  sec: 3073
  time: '51:13'
  who: Barr
- line: There is this test driven development, a way to develop things in engineering.
    Are there some similar approaches in the data space? And how do we go about testing
    in data?
  sec: 3075
  time: '51:15'
  who: Alexey
- line: "I think the ultimate question here is what is the difference between testing\
    \ and monitoring, and or testing and observability and what does that mean for\
    \ us? Going back to software engineering and the importance of testing \u2014\
    \ in software engineering it\u2019s critical. You would be crazy to release something\
    \ to production without testing it thoroughly. Somehow in data we would actually\
    \ do that. Somehow we actually don\u2019t always have strong testing in place.\
    \ So putting in place strong measures for testing too is important. I think you\
    \ need both. You can get away with just testing. Some of the common pitfalls that\
    \ we see: teams that think that just testing is sufficient."
  sec: 3093
  time: '51:33'
  who: Barr
- line: "The problem with that \u2014 you do not know the unknown unknowns. In testing,\
    \ you need to specify things that might happen but there are always going to be\
    \ things that you did not pick up on. So monitoring helps make sure that when\
    \ something happens, you will know about that regardless. I am a strong advocate\
    \ of both. You can define tests like... For example, if you have a solution like\
    \ DBT, you can define data quality tests in DBT, to help make sure that you are\
    \ doing testing properly. I think that is important and another great area that\
    \ we can adopt from software engineering."
  who: Barr
- line: These data quality tests, we define some ranges? Or for this input, this is
    the sort of output we expect? Or how does this work?
  sec: 3196
  time: '53:16'
  who: Alexey
- line: "Yeah exactly! Like defining manually what you expect out of: making sure\
    \ that specific values are in specific range, or specific things that you know\
    \ are often breaking, or incorrect in this data that you wanted to test. Some\
    \ of the common pitfalls that we see is that, one as I mentioned \u2014 there\
    \ are some unknown unknowns. You do not always know what to test for. Then the\
    \ other thing is that \u2014 it is quite time consuming. There are folks who might\
    \ define thousands of tests, so for a data engineer to go through that, it is\
    \ actually quite laborious. So I would think of a strong strategy that would incorporate\
    \ both testing and monitoring as well to mitigate those."
  sec: 3206
  time: '53:26'
  who: Barr
- header: Is data observability cloud agnostic?
- line: "Thank you. Do you know if the big vendor\u2019s, big clouds, already move\
    \ into this space of data observability? Or they are still not really focused\
    \ on that?"
  sec: 3263
  time: '54:23'
  who: Alexey
- line: "At Monte Carlo, we have partnered with Looker which is acquired by Google\
    \ \u2014 so with GCP. We have partnered with PagerDuty, we have partnered with\
    \ SnowFlake. I think the large vendors or the large cloud providers have noticed\
    \ that something is important. We hear a lot from them \u2014 this is something\
    \ that comes up a lot for their customers, and something that they want to provide\
    \ a strong solution for. This is definitely something that is becoming more and\
    \ more important."
  sec: 3277
  time: '54:37'
  who: Barr
- line: But they should be agnostic of a cloud vendor. I imagine if a company is on
    AWS, it is quite a vendor lock. If you want to solve a problem for somebody who
    is on AWS, then you cannot be cloud agnostic. There are so many things that are
    specific in AWS, like S3, Athena, all these services. The question is, can it
    be cloud agnostic or it is difficult?
  sec: 3316
  time: '55:16'
  who: Alexey
- line: "For us... for our observability platform, we integrate with all cloud data\
    \ lakes and data warehouses and BI solutions, integrate with everyone that you\
    \ mentioned, GCP, AWS, and all others as well. I think that is important because\
    \ a good observability solution will actually connect to your existing stack.\
    \ You do not have to change to a different provider for that. So yes, it has to\
    \ be agnostic, in the same way that it is in engineering. For example like Prometheus,\
    \ Grafana, NewRelic, DataDog\u2026 They connect to whatever systems you have.\
    \ I think it has to be a requirement in the same way."
  sec: 3356
  time: '55:56'
  who: Barr
- line: And you can also use Kubernetes for your jobs and then it is also cloud agnostic.
  sec: 3409
  time: '56:49'
  who: Alexey
- line: That is right.
  sec: 3415
  time: '56:55'
  who: Barr
- header: Centralizing data observability
- line: Another question from RK. What are your thoughts on centralizing the observability
    in a distributed environment where we have multiple different data warehouses
    and data pipelines?
  sec: 3417
  time: '56:57'
  who: Alexey
- line: "Thank you for the question RK. I\u2019d love to dig in deeper and better\
    \ understand your environment and see how it can help. It probably requires a\
    \ deeper dive of your system and your infrastructure to better understand. But,\
    \ even in an environment where you have distributed ownership, it is important\
    \ to find a centralized way to define SLAs as an organization. Does data overlap?\
    \ Is data reliability important to us? Do we care about having trust in the data?\
    \ That needs to be in some centralized fashion. Also each team can decide that\
    \ \u201Cit is important to us\u201D to make sure that we are delivering reliable\
    \ data. Each team can define the SLAs for their own organization."
  sec: 3433
  time: '57:13'
  who: Barr
- line: "So observability matters regardless of whether you are undistributed or centralized.\
    \ Providing trust and data is important for everyone, regardless of what your\
    \ structure is and what kind of data you are dealing with. If you do not have\
    \ trust in your data \u2014 that is the worst thing that can happen to you. If\
    \ you are producing data that people cannot use and cannot trust, it is the biggest\
    \ threat to us as an industry. So regardless of the structure, there are different\
    \ ways to adopt it and to implement it. Regardless of that, data observability\
    \ should be core to your strategy."
  who: Barr
- header: Detecting downstream and upstream data usage
- line: How Monte Carlo detects upstream and downstream usage of data?
  sec: 3531
  time: '58:51'
  who: Alexey
- line: "Again happy to go into more detail if folks want to reach out to me. Feel\
    \ free to email me, my email is barr@montecarlodata.com or go to our website montecarlodata.com.\
    \ I am happy to show the link after and get into more details and talk about this.\
    \ But at a super high level, what Monte Carlo does is \u2014 we actually have\
    \ a data observability platform. It is based around these five pillars. As part\
    \ of our lineage pillar, we reconstruct both the upstream and downstream dependencies,\
    \ and reconstruct the lineage for a particular system whether it is your data\
    \ lake, your data warehouse, your BI. We do that across your systems as well,\
    \ and we do that automatically. There is no manual input. Happy to go into more\
    \ detail if you want to reach out directly to me."
  sec: 3544
  time: '59:04'
  who: Barr
- line: "I noticed that you also joined our slack. That\u2019s another way of contacting\
    \ you."
  sec: 3605
  time: '1:00:05'
  who: Alexey
- line: Absolutely! That is a great point. I am a big fan of the community that you
    are building and I am available on Slack. Happy to take any questions, feel free
    to send over.
  sec: 3615
  time: '1:00:15'
  who: Barr
- header: Bad data vs unusual data
- line: Maybe the last one for today. How do you differentiate between getting bad
    data and getting uncommon data, which might be interesting but not wrong?
  sec: 3627
  time: '1:00:27'
  who: Alexey
- line: "If I will rephrase that a little bit, I think the question is \u2014 I might\
    \ get notified about something but it is intentional, it is not bad. It\u2019\
    s just different. It\u2019s unexpected but maybe it's a good thing. And you are\
    \ right, I don\u2019t think we can actually discern that. Also, I am not sure\
    \ that actually matters. I think people want to know about changes in their data,\
    \ even if they are simply uncommon. Let\u2019s say you had a crazy spike or you\
    \ got instead of a one million rows, you got 10000 rows. Maybe that was intentional\
    \ because someone made a schema change upstream. Maybe that is still good data,\
    \ it is not bad. But you still want to know about that because that has implications\
    \ on your machine learning model."
  sec: 3639
  time: '1:00:39'
  who: Barr
- line: I think a good observability solution will let you know about both instances.
    It will provide enough context about each event so that you can make the decision
    or someone can make the decision whether this is uncommon or bad. But we need
    to know about both. And the more context you have about that event, the easier
    it is to make that discernment and know what are the action items to take based
    on that.
  who: Barr
- line: "Should we actually get alerts every time there is a suspicious row? Let\u2019\
    s say we have a volume of one million rows. Do we want to get an alert for every\
    \ unusual one?"
  sec: 3712
  time: '1:01:52'
  who: Alexey
- line: Probably not. You probably will get alert fatigue. You want a system that
    is a little bit more sophisticated than that. At Monte Carlo we have invested
    a lot in making sure that we send alerts for events that matter. If this is a
    table that is highly used or highly queried or has many dependencies downstream
    for machine learning models. There could be other instances or other ways to identify
    whether something is really important. But I would definitely say, you want to
    be very thoughtful and make sure that you are being alerted and taking action
    on the things that truly matter to your system.
  sec: 3726
  time: '1:02:06'
  who: Barr
- line: I think we should be wrapping up. Do you have any last words before we do
    that?
  sec: 3770
  time: '1:02:50'
  who: Alexey
- line: I would just say thank you for the time. I really appreciate it. This is a
    topic that is near and dear to my heart. If anyone wants to continue the conversation
    I will be on slack.
  sec: 3776
  time: '1:02:56'
  who: Barr
- line: Thank you. I will put some contact details, Twitter and LinkedIn in the description.
    Thanks a lot for joining us today, for sharing your knowledge and experience with
    us. Thanks everyone on the stream for listening, for tuning in. I wish everyone
    a great weekend.
  sec: 3787
  time: '1:03:07'
  who: Alexey
- line: Have a great weekend.
  sec: 3811
  time: '1:03:31'
  who: Barr
- line: Nice talking to you.
  sec: 3813
  time: '1:03:33'
  who: Alexey
- line: Likewise.
  sec: 3816
  time: '1:03:36'
  who: Barr
- line: Goodbye.
  sec: 3817
  time: '1:03:37'
  who: Alexey
- line: Bye.
  sec: 3818
  time: '1:03:38'
  who: Barr
---

Links:

- Learn more about [Monte Carlo](https://www.montecarlodata.com)
- [The Data Engineer's Guide to Root Cause Analysis](https://www.montecarlodata.com/the-data-engineers-guide-to-root-cause-analysis/)
- [Why You Need to Set SLAs for Your Data Pipelines](https://www.montecarlodata.com/how-to-make-your-data-pipelines-more-reliable-with-slas/)
- [Data Observability: The Next Frontier of Data Engineering](https://www.montecarlodata.com/data-observability-the-next-frontier-of-data-engineering/)
- To get in touch with Barr, ping her in the DataTalks.Club group or use barr@montecarlodata.com
