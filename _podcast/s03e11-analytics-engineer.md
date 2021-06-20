---
title: "Analytics Engineer: New Role in a Data Team"
short: "Analytics Engineer: New Role in a Data Team"
guests: [victoriaperezmola]

image: images/podcast/s03e11-analytics-engineer.jpg

season: 3
episode: 11

ids:
  youtube: C5UcxBwdCEg
  anchor: Analytics-Engineer-New-Role-in-a-Data-Team---Victoria-Perez-Mola-e131e3n

links:
  youtube: https://www.youtube.com/watch?v=C5UcxBwdCEg
  anchor: https://anchor.fm/datatalksclub/episodes/Analytics-Engineer-New-Role-in-a-Data-Team---Victoria-Perez-Mola-e131e3n
  spotify: https://open.spotify.com/episode/4rLQ5ulsYR9LqXxbFe2MlN
  apple: https://podcasts.apple.com/us/podcast/analytics-engineer-new-role-in-data-team-victoria-perez/id1541710331?i=1000526036141

transcript:
- line: "This week, we'll talk about a new role in the data team. This role is the\
    \ analytics engineer. We have a special guest today, Victoria. Victoria works\
    \ as an analytics engineer. She has a background in system engineering and she\
    \ works as an analytics engineer at Tier in Berlin. Overall, she has over five\
    \ years of experience working with ERP systems \u2013 reporting and databases.\
    \ She's very passionate about using technology and she wants to help people to\
    \ make their daily tasks easier. But in her free time, she likes to encourage\
    \ people to enter the IT world by volunteering, teaching and mentoring. Also,\
    \ Victoria is one of the first people who joined DataTalks.club \u2013 one of\
    \ the first 10 or 20. Welcome, Victoria!"
  sec: 108
  time: '1:48'
  who: Alexey
- line: Thank you for having me.
  sec: 162
  time: '2:42'
  who: Victoria
- header: "Victoria\u2019s background"
- line: "Before we go into our main topic of what analytics engineering is, let\u2019\
    s start with your background. Can you tell us about your career journey so far?"
  sec: 165
  time: '2:45'
  who: Alexey
- line: "As you said, I started as a systems engineer back in Argentina. That\u2019\
    s computer science. I knew a lot about accounting because my parents are accountants\
    \ and I worked with them for several years. I like accounting as well, it felt\
    \ super natural to me to start working with ERP systems. I was helping accountants\
    \ use ERP \u2013 to use technology to calculate payroll and taxes. Then from there,\
    \ I came to Berlin in 2018. I also continued working in a similar role \u2013\
    \ helping in the finance team, defining and making reports, connecting the European\
    \ systems with other systems and automating processes. Eventually, I wanted to\
    \ move from the European world and that's how I ended up in the analytics engineer\
    \ role. I've been here now for seven months as an analytics engineer and I\u2019\
    m enjoying it a lot."
  sec: 175
  time: '2:55'
  who: Victoria
- header: A typical day as an Analytics Engineer
- line: What do you do as an analytics engineer? What kind of responsibilities do
    you have? What does your typical day look like?
  sec: 245
  time: '4:05'
  who: Alexey
- line: I do a lot of data modeling. I also work a lot around the data quality and
    data availability. Things that I could be doing on a day-to-day basis are building
    new pipelines, making that data available, building models. Also I clean that
    data so it's available for data analysts and the data scientists by exposing that
    data to Looker. I also work on it if something goes wrong. If something fails,
    then I have to chime in and check why the data is not available or why the data
    is not clean.
  sec: 254
  time: '4:14'
  who: Victoria
- line: "You said modeling \u2013 you probably mean data modeling, right?"
  sec: 300
  time: '5:00'
  who: Alexey
- line: Yeah, data modeling.
  sec: 303
  time: '5:03'
  who: Victoria
- line: That would mean creating diagrams, how the data looks like, what are the entities
    in the data, right?
  sec: 305
  time: '5:05'
  who: Alexey
- line: "Yeah, but it\u2019s more about writing that. More writing the SQL I mean.\
    \ Building the models around the data, creating the tables, or views, and writing\
    \ the queries behind it to model the data so that the data can be used for analysis."
  sec: 315
  time: '5:15'
  who: Victoria
- line: You mentioned a tool called Looker, which is a tool for building dashboards,
    right? Or what is it?
  sec: 340
  time: '5:40'
  who: Alexey
- line: "Yeah. Looker is a BI tool, similar to Tableau. There, you can write queries\
    \ as well. Then you can create dashboards and build reports as well. That would\
    \ be the tool that gets exposed to the end user. The business users are going\
    \ to be consuming the data from Looker. Then the data team uses DBT for doing\
    \ the whole modeling. DBT is a transformation tool. We take the data that comes\
    \ from the data pipelines, from either our backend events, or maybe our external\
    \ data. Then with DBT, we transform that data and we make the models. We do everything\
    \ we need to either clean the data, change it, or maybe calculate something \u2013\
    \ things like that. We try to do everything in DBT."
  sec: 347
  time: '5:47'
  who: Victoria
- header: What is DBT?
- line: "This \u201CDBT\u201D is a transformation tool you said. What does it do exactly?\
    \ You just write a bunch of SQL queries and put them somewhere?"
  sec: 409
  time: '6:49'
  who: Alexey
- line: "Yeah, you write a lot of SQL queries with it. But it has very good things.\
    \ If you think about the software development process that you normally study\
    \ in university and you think about data \u2013 they normally don't get along\
    \ very well. DBT brings that to the data team and the data work. You have all\
    \ these SQL files, but you also have YML files, where you would have documentation\
    \ about the models that you're writing about. Everything is in a GitHub repository,\
    \ so you have version control as well. It is sometimes very hard, at least in\
    \ my experience, to introduce something like version control in data. But it's\
    \ also something that is extremely useful to have. You can also write tests in\
    \ DBT about your data. You can write your own or you can also use normal, unique,\
    \ non-null kinds of tests. The nice thing about it is that you don't really have\
    \ to write the DDL. So you wouldn't have to write CREATE TABLE, CREATE VIEW, DROP\
    \ TABLE \u2013 you just write a SELECT and it does the whole thing for you. It\
    \ compiles the code afterwards."
  sec: 419
  time: '6:59'
  who: Victoria
- line: "DBT is a tool, as you said, for transforming data \u2013 you write a bunch\
    \ of SQL queries and then it takes care of actually creating this table. Is that\
    \ right? You said you don't need to worry about the DDL. Then, you can also do\
    \ tests with this tool, right? Check that the data quality is good. And I guess\
    \ you can also schedule the queries? To run them on a particular day, for example?"
  sec: 505
  time: '8:25'
  who: Alexey
- line: "Yes. It manages the dependencies. It even builds the DAG, and you can see\
    \ how the models connect to each other. Let's say we have a source module and\
    \ then on top of that, you build a dim table. Then you could run from the dim\
    \ table everything that comes before, from the source, and everything that comes\
    \ afterwards. This is very nice. You can easily check dependencies downstream\
    \ and upstream as well. DBT is open source, but they also have a paid part \u2013\
    \ enterprise I think it\u2019s called \u2013 which is DBT cloud. There, you can\
    \ schedule everything. You can set the schedule and run your models depending\
    \ on tags that you could use. For example, if there are tables or views or things\
    \ like that. We have some of them. For example, some of the data is refreshing\
    \ every hour. Some of the data only refreshes during the night."
  sec: 539
  time: '8:59'
  who: Victoria
- header: Tools for Analytics Engineers
- line: You mentioned Looker, which is a tool for end users. You mentioned DBT. Are
    there other tools that you also typically use in your work?
  sec: 604
  time: '10:04'
  who: Alexey
- line: "Yes. I also use a tool a lot called Adlib \u2013 for doing the ETL. We mostly\
    \ do ELE because the transformation is done in DBT. We also use Adlib. It's an\
    \ ETL tool to load the data from the S3. We have the data coming into S3 buckets\
    \ and then we use this tool to load this data into Snowflake. So \u2013 also Snowflake.\
    \ We used to have Redshift before. Normally, you'd have to use one of these cloud\
    \ computing warehouses. I've also seen other companies that use Python, or at\
    \ least the folks in the analytics engineer role. At least they request for that."
  sec: 615
  time: '10:15'
  who: Victoria
- line: Do you also use them? Or is it just something that others require?
  sec: 665
  time: '11:05'
  who: Alexey
- line: I saw that others do it. I don't. I use a lot of SQL. That's my main language,
    and then Adlib, Snowflake and Looker.
  sec: 669
  time: '11:09'
  who: Victoria
- line: Okay, so Snowflake is there. You have this DBT tool, where you write SQL queries.
    But these queries need to be executed somewhere. And this somewhere is Snowflake,
    right? This is where the queries are running.
  sec: 683
  time: '11:23'
  who: Alexey
- line: Yeah. The queries are running in Snowflake.
  sec: 697
  time: '11:37'
  who: Victoria
- header: How Victoria became an Analytics Engineer
- line: How did you become an analytics engineer? I think you mentioned that you were
    interested in accounting and you were doing all this ERP analysis and working
    with financial data. But then at some point, you decided to become an analytics
    engineer. How did this happen? And what did you need to actually do to transition
    into this role?
  sec: 708
  time: '11:48'
  who: Alexey
- line: "Yeah, it was by chance. I wasn\u2019t actively looking for an analytics engineer\
    \ role, and I didn't really know what it was before. But I applied for a normal\
    \ BI position. I don't even remember which position I applied for. Then I did\
    \ all the interviews and I think the last interview was on a Friday. Then on the\
    \ coming Monday, I was told that they were going through a hiring freeze because\
    \ of the Coronavirus. After a few months, the hiring manager reached out to me\
    \ again and said, \u201CHey, we're opening. We're hiring again. Are you willing\
    \ to have a chat?\u201D Then he told me about this position and it sounded really\
    \ cool. It sounded like something that I wanted to be doing. Some parts are very\
    \ similar to what I was doing before. Before I was also working with data warehousing\
    \ and all of that. I was working more with the ERP data. That's how I ended up\
    \ here. I even remember that at the end of that call, he says, \u201COkay, so\
    \ then I'll send you the email with the details of the offer. And by the way,\
    \ the role is called \u2018analytics engineer\u2019."
  sec: 734
  time: '12:14'
  who: Victoria
- line: Okay. So you had no idea that this is the role you interviewed for?
  sec: 824
  time: '13:44'
  who: Alexey
- line: Yeah, basically.
  sec: 706
  time: '11:46'
  who: Victoria
- line: Okay. That's interesting. Do you know how or why the company actually decided
    to have this kind of role?
  sec: 707
  time: '11:47'
  who: Alexey
- line: How did they come up with the idea of hiring analytics engineers? I know that
    during Corona, they were thinking about how to reshape the team. How were they
    going to grow, make the team grow, and all of that. They were using DBT before
    and the ones that are pushing for the analytics engineers, I would say. So that
    would also make sense that it came from there, but I owe you the answer to that
    one.
  sec: 841
  time: '14:01'
  who: Victoria
- header: Difference between an analytics engineer, a data analyst, and data engineer
- line: "When I read the job descriptions, the position really looks like a data engineer.\
    \ But on the other hand, there\u2019s this analytics component. So what is the\
    \ main difference between an analytics engineer, a data analyst, and data engineer?"
  sec: 874
  time: '14:34'
  who: Alexey
- line: The analytics engineer is supposed to be in the middle between the data engineer
    and the data analyst. The lines are a little bit blurry even in my team and not
    just in different companies. Some of us are regarded to be more in the data engineer
    side and others more in the data analyst side. I think that will vary. But overall,
    the data analysts sometimes have to do a lot of data cleaning/data availability.
    In reality, they have to have a lot of business knowledge as well. They should
    take care of analyzing the data and not cleaning the data, right? Maybe their
    SQL can work and it has a lot of business logic, but it's not the most efficient
    queries. Because they normally come from another type of background, not a computer
    science background. They know good software deployment practices.
  sec: 891
  time: '14:51'
  who: Victoria
- line: In the case of the data engineers, they are way more technical, and maybe
    they lacki more of the business vision to the thing. They do have the software
    engineering practices, but they maybe don't have the domain knowledge. The analytics
    engineer is in between that. They are supposed to help the analyst apply their
    business models, but also work with the data engineers to bring in this business
    knowledge as well.
  who: Victoria
- line: They know both, right? The analytics engineer knows how to be a good analyst,
    and he or she also knows how to be a good data engineer. Right?
  sec: 984
  time: '16:24'
  who: Alexey
- line: "They\u2019re in between, yeah. I mean, I wouldn't say that I would be a great\
    \ data analyst, because everyone's different here. I have to know that part, but\
    \ I wouldn't replace any of my data analyst coworkers."
  sec: 998
  time: '16:38'
  who: Victoria
- header: What gap does the Analytics Engineer role fill?
- line: "Six months ago, we had a chat and you told me that you found this new job\
    \ called analytics engineer. I asked you \u201CWhat is that?\u201D Before that,\
    \ I had no idea that this role existed. But after talking to you, all of a sudden,\
    \ I started noticing it everywhere. I would go to LinkedIn and I would see open\
    \ positions. I would go to some Slack communities and I would see job postings\
    \ there. Also on the internet, I started to see this thing. It looked like it\
    \ became popular recently \u2013 at least that\u2019s my impression. Do you know\
    \ why it happened? Why did it become popular? And what is the gap that this role\
    \ is trying to close?"
  sec: 1014
  time: '16:54'
  who: Alexey
- line: "Yeah, there\u2019s definitely an analytics engineer movement starting. I\
    \ left a few links about when people started to talk about this role, what they\
    \ need, and things like that. There's one about Spotify. They talk about this\
    \ very clearly. They were having issues where the analysts were spending too much\
    \ time cleaning the data. Whenever they needed new data, they needed to set up\
    \ this stream of new data. They needed to check the quality and they needed to\
    \ model the data in a way that they could use. Only after that were they able\
    \ to sit and do the actual analysis. Then on the other side, data engineers didn't\
    \ really want it to get more into that part \u2013 taking that work out of the\
    \ data analyst. That\u2019s when Spotify said that they will open this position.\
    \ They said, \u201COkay, let's just hire a new person. We need someone else \u2013\
    \ someone in between.\u201D"
  sec: 1063
  time: '17:43'
  who: Victoria
- line: Are you saying that data analysts spent too much time cleaning data and solving
    quality issues and that data engineers didn't want to take care of it for some
    reason?
  sec: 1132
  time: '18:52'
  who: Alexey
- line: "Yeah, they didn't want to get more involved with modeling this type of data,\
    \ because then they have to understand what the data is for. They just wanted\
    \ to build the infrastructure. Also what Spotify was seeing was that data analysts\
    \ weren\u2019t very good at writing and doing these kinds of things. They weren't\
    \ writing the best code. They started to see that they were hiring more people\
    \ to do this. And then they said, \u201CWe need a person to do this as a full\
    \ time job.\u201D Then they opened this position and they invented a title, which\
    \ wasn\u2019t analytics engineer originally. It was something else along the lines\
    \ of \u2018data specialist\u2019. That's how they hired their first analytics\
    \ engineer. The guy that was hired as the first Spotify analytics engineer said\
    \ at the beginning, \u201CHey, this title that you gave me is crap.\u201D Then\
    \ they maybe found a blog or something else and changed it to \u2018analytics\
    \ engineer\u2019."
  sec: 1145
  time: '19:05'
  who: Victoria
- line: Okay, so it started at Spotify, right? And then other companies noticed it
    and also decided to follow?
  sec: 1211
  time: '20:11'
  who: Alexey
- line: "I don't know. They (Spotify) did it in early 2018, and every blog seems to\
    \ say that the role started over there. I wouldn\u2019t pinpoint that \u201CYes,\
    \ it was Spotify.\u201D But people started noticing this missing role \u2018in\
    \ between\u2019. One that allows analysts to actually analyze data, and for data\
    \ engineers to actually just care about the infrastructure and the pipelines.\
    \ That\u2019s how someone came up with the analytics engineer role."
  sec: 1219
  time: '20:19'
  who: Victoria
- header: Analytics Engineer job requirements
- line: "Yeah, I actually thought that data engineers should take care of data quality.\
    \ But I never thought that they wouldn\u2019t need to have this domain knowledge\
    \ that maybe is difficult to acquire, while analysts have it. Yeah. Before this\
    \ interview, I wanted to check a couple of positions (job postings) for an analytics\
    \ engineer and see what kind of requirements there are. I didn't check Spotify,\
    \ but I found a job posting from Airbnb."
  sec: 1252
  time: '20:52'
  who: Alexey
- line: "They have these requirements: the first is \u201Cunderstand data needs by\
    \ interacting with data scientists and data engineers.\u201D Then the second one\
    \ \u201CArchitect and build data pipelines with data engineers.\u201D The third\
    \ one is \u201CBe a data expert and tone data quality.\u201D I think we talked\
    \ already about all these things like data pipelines and taking care of data quality.\
    \ Then the fourth one is \u201CBuild and improve data tools for auditing, error\
    \ logging, and so on.\u201D And the fifth one is \u201CDesign and build dashboards\
    \ to enable self service.\u201D"
  who: Alexey
- line: Do you think this is an accurate description of the requirements that analytics
    engineers have, in general?
  who: Alexey
- line: "Yeah, I would say so. It goes from the pipeline to the BI tool. But since\
    \ it's such a nice position, it's going to change from company to company. For\
    \ example, Spotify also talks about something quite similar. They talk more about\
    \ being the \u201Cdata owner\u201D and to check on data quality. But in other\
    \ companies \u2013 I've seen in Trade Republic \u2014 they don't even mention\
    \ data pipelines. The role seems to be more on the business side. So it\u2019\
    s going to lean a little bit more towards the data analysts."
  sec: 1345
  time: '22:25'
  who: Victoria
- header: In between Data Analysts and Data Engineer
- line: "So there is a wide spectrum. On one side you have the data analysts, on the\
    \ other side you have the data engineer, and there is a whole spectrum of how\
    \ you can mix the two to arrive at the analytics engineer. You can take 50/50\
    \ \u2013 I think in the case of Airbnb, my impression is that it leans more towards\
    \ the data engineer, because there is a lot of work with data pipelines and data\
    \ tools. But still they have this \u201Cdesign and build dashboards\u201D part,\
    \ which is more of what analysts would typically do. So they have maybe 70% data\
    \ engineering and 30% data analysts. Then you said Trade Republic, is more maybe\
    \ on the other side of the spectrum. So maybe 70% analysts and 30% engineers."
  sec: 1393
  time: '23:13'
  who: Alexey
- line: They do write a lot in the Netflix blog about this. I really like the Netflix
    blog in Medium. They actually have an article, which I also put in the links,
    where they talk about this. It looks like it also varies from team to team. Some
    teams are going to need people like analytics engineers, who are going to be more
    technical than others. There's also another link that I put about Nubank. They
    also use DBT. While, Airbnb doesn't seem like they use DBT. Even the tool changes
    from company to company. In Nubank, they even have a comparison of what they expect
    to have in the analytics engineer profile versus the data engineer and the data
    analyst. In the case of the analytics engineer, it goes more towards analytics
    and reporting, data pipelines, data modelling, and the whole data quality and
    data sharing part.
  sec: 1450
  time: '24:10'
  who: Victoria
- line: "The last comment in the live chat that I just noticed is the comment from\
    \ Lufassa is \u201CData engineers are mainly focused on infrastructure. They don't\
    \ leverage insight and curate data. Analytics engineers would take the data and\
    \ carefully curate it, so analysts can streamline and use the data easier.\u201D\
    \ Do you agree with that?"
  sec: 1518
  time: '25:18'
  who: Alexey
- line: Yeah, I would agree. I didn't hear the name properly. I was thinking it's
    my coworker.
  sec: 1541
  time: '25:41'
  who: Victoria
- line: "Lufassa. But maybe I\u2019m mispronouncing it. What's the right way of pronouncing?"
  sec: 1550
  time: '25:50'
  who: Alexey
- line: No, it's not. It looked a little bit like it.
  sec: 1557
  time: '25:57'
  who: Victoria
- line: "Yeah, but there\u2019s Alan who says, \u201CVictoria rocks,\u201D maybe he\u2019\
    s your colleague?"
  sec: 1560
  time: '26:00'
  who: Alexey
- line: No, I don't know any Alan. Maybe he just realized I rock.
  sec: 1564
  time: '26:04'
  who: Victoria
- header: Analytics Engineer Skills
- line: Yeah, I do agree with him. I'm continuing with the same position. We talked
    about requirements. After requirements, we usually have the skill section.
  sec: 1570
  time: '26:10'
  who: Alexey
- line: "In that position, the skills that Airbnb requires from analytics engineers\
    \ is SQL, not surprisingly. The second category of skills is \u201Cdistributed\
    \ systems for data processing\u201D which is Spark, Presto, Hadoop and Hive. Then\
    \ they have programming \u2013 Python, R, Schema design, dimensional data modeling.\
    \ The last thing, which I liked \u2013 \u201Can eye for design\u201D."
  who: Alexey
- line: "In my opinion, most of these things are technical, maybe apart from the last\
    \ one. I think most of these skills, apart from \u201Can eye for design,\u201D\
    \ is what I would see typically in data engineering positions. I think dimensional\
    \ data modeling, schema design, is also something that data engineers tend to\
    \ do when designing data warehouses maybe, or data lakes, or whatever. To me,\
    \ they look quite typical for data engineers. Is it a typical skill set for an\
    \ analytics engineer, or?"
  who: Alexey
- line: "If you want to apply for an analytics engineer role on Tier, and we do have\
    \ a lot of openings, by the way. I wouldn't say you need all of this toi apply.\
    \ You definitely need to know SQL. You need to know data modeling. So things like\
    \ what a dim table is, and what a fact table is. Basically, you need to have read\
    \ Kimball\u2019s data warehouse book. Then I would also expect something for Snowflake,\
    \ so definitely not Spark, Presto, Hadoop, Hive. That looks way more data engineer-focused\
    \ to me. As for programming, Python or R \u2013 analytics engineers don't use\
    \ that at the moment. It could be something that eventually we start using. We\
    \ do have some Python scripts, so it's not like I've never seen Python code ever\
    \ in the last seven months that I've been working at Tier. But I wouldn't say\
    \ I needed it. To me, Python seems like something that\u2019s easy to pick up\
    \ if you know coding already. Not so data engineering-focused. But again, Airbnb\
    \ the analytics engineer role definitely looks way more technical."
  sec: 1651
  time: '27:31'
  who: Victoria
- line: You also mentioned Spotify and Trade Republic? Do you remember what kind of
    skills they require for their positions?
  sec: 1745
  time: '29:05'
  who: Alexey
- line: "I know Trade Republic has a very similar tech stack to the one we have. They\
    \ also have Snowflake, or are about to have it. They use DBT as well. And some\
    \ ETL tool as well \u2013 something around that would probably be necessary. I\
    \ don't remember what it was in the case of Spotify. For example, Nubank is very\
    \ similar to what we have as well. They use DBT a lot. They've been featured in\
    \ the DBT blogs and everything. You would need something like SQL for sure. That\
    \ is going to be what you need to be familiar with, at least with everything like\
    \ data modeling."
  sec: 1755
  time: '29:15'
  who: Victoria
- header: Is DBT typical for Analytics Engineers?
- line: When I see DBT mentioned, I often see the analytics engineer role mentioned
    as well. I think this is a pretty typical tool that analytics engineers use, right?
  sec: 1806
  time: '30:06'
  who: Alexey
- line: Yeah.
  sec: 1818
  time: '30:18'
  who: Victoria
- line: I think even DBT has an article about the analytics engineer role. The company
    itself wrote an article about the role of the analytics engineer, right?
  sec: 1819
  time: '30:19'
  who: Alexey
- line: "Yeah. It's also in the links. DBT also has useful resources for learning\
    \ and more. They're one of the main companies that started the analytics engineer\
    \ movement, for sure. They did this by participating in blogs or talking about\
    \ the analytics engineer role, or by being in conferences talking about analytics\
    \ engineers. They've definitely started everything \u2013 it's heavily related\
    \ to DBT. When you think about an analytics engineer, or at least I do, I immediately\
    \ think of DBT. I think it goes the other way around \u2013 DBT and, obviously,\
    \ the analytics engineer role."
  sec: 1830
  time: '30:30'
  who: Victoria
- header: Varying descriptions of the Analytics Engineer role
- line: "I work as a data scientist. When it comes to data science, the description\
    \ of roles is a little bit different for every company. We have some data scientists\
    \ at our company, OLX, who are more actually data analysts \u2013 they do the\
    \ kind of work that analysts do. But in some cases, data scientists are doing\
    \ the engineering work. The other end of the spectrum is ML engineers, who are\
    \ sometimes also called \u2018data scientists\u2019. From what I see, when it\
    \ comes to the analytics engineer role, it's very similar. There is an analyst,\
    \ there is a data engineer, and then you have the whole spectrum of things in\
    \ between, while every company has its own interpretation of the role, right?"
  sec: 1869
  time: '31:09'
  who: Alexey
- line: Yeah. But I also think new data teams that include analytics engineers have
    a more defined data analyst or a data scientist role. As a data analyst, you usually
    only take care of analyzing the data, right? Because then, analytics engineers
    are going to take care of the rest. Same for data scientists. Data scientists
    complain all the time about cleaning the data. Well, they don't need to, because
    we are there for them.
  sec: 1928
  time: '32:08'
  who: Victoria
- line: Okay, so I should ask for analytics engineers at work to help me clean the
    data?
  sec: 1962
  time: '32:42'
  who: Alexey
- line: You should ask for an analytics engineer, definitely. You need one.
  sec: 1974
  time: '32:54'
  who: Victoria
- line: Okay, so this is who will help us clean the data?
  sec: 1978
  time: '32:58'
  who: Alexey
- line: Yeah.
  sec: 1981
  time: '33:01'
  who: Victoria
- header: How do Analytics Engineers work with other team members?
- line: You mentioned that analytics engineers help analysts and data scientists with
    cleaning data. They help data engineers to maybe understand the business domain
    better. In general, how do they work with others in the team? With product managers,
    for example? With backend engineers? With other people in the team?
  sec: 1982
  time: '33:02'
  who: Alexey
- line: "In my case, my stakeholders are my coworkers most of the time \u2014 the\
    \ data analysts and the data scientists. So it varies a lot. I don't have much\
    \ exposure to product managers, to the business\u2019 stakeholders. Some of my\
    \ coworkers have this exposure. The analytics engineers have more, but the idea\
    \ is also that the analyst is going to still be doing their work. They're talking\
    \ to these business stakeholders to understand what they need, and then also talk\
    \ to us. But this doesn't mean that the analytics engineers are not going to talk\
    \ with the business stakeholders, it could be that you also need to go directly\
    \ to the business stakeholder as well."
  sec: 2011
  time: '33:31'
  who: Victoria
- line: In the case of the backend engineers, say there's a new event that has to
    come in because of new data coming in. You're probably going to have to talk with
    the backend engineers as well to see how they set up that event, because at the
    end, you're going to have to consume that. Of course you have to get involved
    in this case.
  who: Victoria
- line: "Also, one thing about the analytics engineers in a team and how it works.\
    \ In my company, we have the analytics platform, it has the data platform. Then\
    \ we have more \u2013 operations, analytics, commercial analytics. And they have\
    \ a panel for the data scientists, and we\u2019re in the platform, and then the\
    \ data engineers. Now we\u2019re on the platform, we are old analytics engineers.\
    \ But then it went off these teams, they are also getting an analytics engineer.\
    \ So it's getting to be decentralized. These analytics engineers are going to\
    \ be more exposed to these business stakeholders, because they're going to be\
    \ inside the operations analytics team. This is also in the links. I left a link\
    \ on how Nubank is talking about how they're doing that. How they're scaling and\
    \ making it so that these teams don't depend on the analytics engineers for the\
    \ platform. They have their own analytics engineers in their teams. This is also\
    \ a way to collaborate."
  who: Victoria
- line: To summarize and to make sure I understood you correctly. There is a platform
    team, where there are a lot of analytics engineers, and then you have separate
    teams, and each team would have one analytics engineer who would work with the
    rest of the people in the team, right?
  sec: 2160
  time: '36:00'
  who: Alexey
- line: "Yeah, exactly. The commercial analytics engineer will only take care of the\
    \ commercial topics, for example. Whereas in the platform, I'm going to be working\
    \ more on the base data in general \u2013 more source client data or things like\
    \ that."
  sec: 2181
  time: '36:21'
  who: Victoria
- header: Dealing with bad data coming from different sources
- line: "Actually, speaking of sources \u2013 we have a question about that. \u201C\
    In your role, how do you deal with bad data coming from different sources, or\
    \ from changing schemas?\u201D"
  sec: 2204
  time: '36:44'
  who: Alexey
- line: "In the case of changing schemas, the tool that we have at the moment adapts\
    \ to that. We don't have much of an issue there. Of course, we have models that\
    \ rely a lot on that. But in that sense, I would say it's not such a big issue.\
    \ In terms of data quality, that's something that we're still working on a lot.\
    \ I don't think that's something that you ever finish. You never get to a point\
    \ \u201CMy data is 100% the best data.\u201D But there's also a lot going on in\
    \ the company note, and a little bit outside of us as well. A lot of this data\
    \ is coming from the backend engineers \u2013 the data has to come clean from\
    \ there as well, right? Or it has to be good quality when it comes from there."
  sec: 2217
  time: '36:57'
  who: Victoria
- line: "What we are doing right now is cleaning a lot of that in DBT and that gives\
    \ us a lot of control. We can see that code, what it\u2019s doing, what the records\
    \ are. Are they duplicated, or excluding, or transforming? We do a lot of things\
    \ like that. DBT also lets you create what they call macros, which is a UDF similar\
    \ to what I would create in any SQL, Servo, Snowflake or whatever. We can also\
    \ use that sometimes to try and form the name of the cities, for example. We have\
    \ the same names for all the cities in all of our day towers, things like that.\
    \ And there are also tests. We check that the cities are defined. That if a number\
    \ has to be between one to five \u2013 it doesn't go beyond that."
  who: Victoria
- header: Tests
- line: These tests apply to each incoming row? So for each row that DBT sees, there
    is a test. And if some record doesn't pass this test, you get an alert.
  sec: 2333
  time: '38:53'
  who: Alexey
- line: "So-so. The test is basically a query. Let's say you define your model. You\
    \ create your model and then you define the columns. Then you define that for\
    \ this column, the test that I'm going to apply is \u201Cnot null\u201D, for example.\
    \ Then, at the end, when you run the test, it's going to select from this table\
    \ where this field is now. Then if it returns nothing, the test is passed. If\
    \ it returns something, then it's going to give you either a warning or an error.\
    \ The nice thing about DBT is that we can do that before building the models.\
    \ What we do is check that the sources don't have errors. If they do have errors,\
    \ then the modules that use the sources are not going to be built. We do this\
    \ so that we don't build things on wrong data."
  sec: 2344
  time: '39:04'
  who: Victoria
- line: "That's how you control quality. Then I guess at some point, somebody comes\
    \ to you \u2013 probably an analyst \u2013 and says, \u201CHey, something's wrong\
    \ with this data.\u201D And you start looking and maybe realize that you missed\
    \ something in your test. Then you would add an extra test. Right?"
  sec: 2401
  time: '40:01'
  who: Alexey
- line: "Yeah. It\u2019s unfortunate that we never get to the point that someone says,\
    \ \u201CHey, these numbers don't match.\u201D I would like it if we had a test\
    \ for everything, so that we are always ahead. But I don't know if you can ever\
    \ get to that point."
  sec: 2419
  time: '40:19'
  who: Victoria
- header: How is Analytics Engineer related to BI Analyst or BI Developer
- line: "Thanks. We have another question. \u201CHow is this position related to BI\
    \ analyst and BI developer? And how is it different from these two?\u201D"
  sec: 2442
  time: '40:42'
  who: Alexey
- line: "I don't know exactly what a BI Analyst would be. I would imagine something\
    \ more like a data analyst. Then it would be the same as before, right? That means\
    \ you're a little bit before. You don't really do the analysis, per se, you just\
    \ make the data available so that the data analysts can do the analysis. And with\
    \ the BI\u2026"
  sec: 2453
  time: '40:53'
  who: Victoria
- line: BI developer. I suspect that maybe in these BI tools, instead of having a
    data engineer and data analysts, you would have a BI analyst who could do the
    analysis. Then you would have a data warehouse developer, who would actually build
    the data warehouse. Which is probably synonymous to the role of a data engineer
    these days.
  sec: 2477
  time: '41:17'
  who: Alexey
- line: Yes. I would say maybe the BI developer is similar. I think it would also
    depend on what the company calls a BI developer. It's quite close to maybe the
    analytics engineer. Because I would imagine that they write SQL as well and things
    like that.
  sec: 2503
  time: '41:43'
  who: Victoria
- header: Transition to Analytics Engineer
- line: Let's say I am an analyst and I want to become an analytics engineer. How
    can I do this? How can I make this transition? What kind of things do I need to
    do to become an analytics engineer?
  sec: 2525
  time: '42:05'
  who: Alexey
- line: First, learn about good software development practices. What does good code
    look like? What are good practices to implement? Definitely learn about data molding,
    or read books like Kimball and maybe Edmon. There's also two links that I left.
    One is DBT learning. This is free. Of course, it's around DBT, but they do talk
    about data tables, fact tables, what those are, and things like that. There's
    also another repository that someone very generously built and it has a lot of
    links to readings about pipelines, readings about good practices, readings about
    SQL. Definitely write good SQL. And learn other kinds of tools like DBT.
  sec: 2547
  time: '42:27'
  who: Victoria
- line: You mentioned this repository with information. Is it something you'll also
    put in the links?
  sec: 2610
  time: '43:30'
  who: Alexey
- line: "Yeah. It's in the learning resources. This one is very good. It\u2019s called\
    \ Analytics readings."
  sec: 2619
  time: '43:39'
  who: Victoria
- line: "Analytics readings. The links, there is a question \u2013 \u201CI'm not seeing\
    \ the links.\u201D They are not in the chat, they are in the description. If you\
    \ go to the description, the first link there, you click on this, and there's\
    \ a Notion document with all the links that Victoria prepared for today."
  sec: 2628
  time: '43:48'
  who: Alexey
- line: "These are the good resources. You said an analyst would need to pick up some\
    \ good software engineering practices, learn data modeling, and then learn DBT\
    \ skills \u2013 the most important tool. But I think for analysts, this is not\
    \ a problem, they already know SQL, right? More or less. I think for analysts,\
    \ this is the tool that they use 80% of the time, perhaps. They should be pretty\
    \ good at this already."
  sec: 2650
  time: '44:10'
  who: Alexey
- line: So probably not good enough to be the data analyst of Spotify. Apparently.
  sec: 2683
  time: '44:43'
  who: Victoria
- header: How to know if Analytics Engineer is the role for you
- line: "Let\u2019s say I really like what I hear. Suppose I'm an analyst or data\
    \ engineer, or somebody who works with ERP systems, and I think \u201CThis is\
    \ really cool. I want to try it.\u201D How do I make sure that this is something\
    \ for me? How do I make sure that I love this kind of work?"
  sec: 2692
  time: '44:52'
  who: Alexey
- line: "If you like data modeling, figuring out how to read models, tables, how to\
    \ model the data, and make it available, then the role is likely for you. Let's\
    \ say you're a data analyst, and you show more of that part \u2013 I think you're\
    \ getting close to the analytics engineer role. If you also care a lot about the\
    \ data quality, I would say, and about good practices, as I said before. For example,\
    \ with my team, we build a lot of guidelines and things like that for everyone.\
    \ For the data analysts and data scientists as well. We write about how to write\
    \ the code, what the good practices around this are, how to take care of the tests,\
    \ and things like Adlib tests, or how to do a proper peer review and all these\
    \ kinds of things. That\u2019s something that we also have in common with the\
    \ other analytics engineers \u2013 we care a lot about that. More than maybe the\
    \ data analyst. They care a little bit more about answering those questions. Which\
    \ is okay, because that's what they're meant to be doing."
  sec: 2716
  time: '45:16'
  who: Victoria
- header: The annoying parts of working as an Analytics Engineer
- line: "I'm also wondering if there are some annoying parts in your work. For me,\
    \ as a data scientist, I have to clean a lot of data. For many people, this is\
    \ \u201CSigh. Again, I have to clean the data.\u201D Now I know the solution \u2013\
    \ we just need to hire an analytics engineer. Are there such things for analytics\
    \ engineers? The things are annoying, but you have to do them anyway. For example,\
    \ if I don't clean the data, then my models will be bad, so I have to do it. It's\
    \ annoying, but it's inevitable. Are there things like that in the job of an analytics\
    \ engineer?"
  sec: 2788
  time: '46:28'
  who: Alexey
- line: "Yeah. I would say that the most \u2013 I wouldn't say it's extreme \u2013\
    \ but the most annoying part is: we do a lot of defining guidelines and that kind\
    \ of thing. We can\u2019t really make people follow them. That would be the most\
    \ annoying part. Also, another not annoying, but not-as-rewarding thing, if I\
    \ compare it with other jobs that I had in the past. Before, I would automate\
    \ something like a process and reports when I was working. When my stakeholders\
    \ were the accountants, and then the month would close, suddenly it was being\
    \ done in one day thanks to my work instead of one week. It was like a party,\
    \ right? I was a superhero. Now, since my stakeholders are technical people, they\
    \ know a bit more, so they don't get surprised. It\u2019s like a boost to your\
    \ ego maybe. But I also asked this question to my coworkers. One of them said\
    \ that the annoying thing is \u201Cworking with another analytics engineer,\u201D\
    \ but he was joking."
  sec: 2831
  time: '47:11'
  who: Victoria
- line: How many analytics engineers do you have in your company? More than two?
  sec: 2909
  time: '48:29'
  who: Alexey
- line: Nine.
  sec: 2916
  time: '48:36'
  who: Victoria
- line: Nine. Okay.
  sec: 2918
  time: '48:38'
  who: Alexey
- line: "Well, I can be very pushy, so I don't know. But my coworkers also talk a\
    \ lot about their stakeholders, management, the QI and QC. Everything around that\
    \ kind of thing. Sometimes you have to deal with things that you don't expect\
    \ from backend \u2013 backend events. Even with the stakeholders \u2013 suddenly\
    \ you have to jump in to stop something that could have been planned or something\
    \ like that. Also, we don't have much control over the raw data. We are very limited\
    \ to the tool that we have in that sense. It's not like we build custom pipelines\
    \ because we use this tool."
  sec: 2922
  time: '48:42'
  who: Victoria
- line: You have less control over the raw data than data engineers, right? Maybe
    data engineers can do more, and you're limited to the tools.
  sec: 2970
  time: '49:30'
  who: Alexey
- line: "Another thing that one coworker said \u2013 it was that data quality is not\
    \ our fault in most cases. Unless we made a mistake, of course. But we are affected\
    \ by that mistake the most. We're the ones that take care of that kind of thing\
    \ most of the time. When the quality of the data isn\u2019t good, we are the ones\
    \ that immediately have to jump in and take all this ad hoc work."
  sec: 2982
  time: '49:42'
  who: Victoria
- line: "I guess that happens for many people, not just analytics engineers. Analysts\
    \ also need to do ad hoc dashboards for something important. Data engineers will\
    \ also need to take care of some data quality issue that comes up \u2013 they\
    \ need to run and fix it."
  sec: 3011
  time: '50:11'
  who: Alexey
- line: Do you know what a data profile is? Because there is a question about data
    profiles. I don't know, maybe I can just read the question and you tell me if
    it makes sense for you.
  sec: 3030
  time: '50:30'
  who: Alexey
- line: "I don\u2019t know what a data profile is. But yeah, you can read it and let's\
    \ see if we can answer it."
  sec: 3043
  time: '50:43'
  who: Victoria
- header: Data profiles and Data documentation
- line: "This person is curious about data documentation. \u201CI've been planning\
    \ to use DBT, but I noticed that it doesn't have a great data profile. How do\
    \ you show the data profile?\u201D"
  sec: 3046
  time: '50:46'
  who: Alexey
- line: "Oh yeah, I know what a data profile is. You see how the values are \u2013\
    \ whether it\u2019s average, normal and things like that. Yeah, it's true, DBT\
    \ doesn't deal with that very well. There are other tools that are working now\
    \ until the upgrade of DBT that take care of that. For example, Datafold has something\
    \ like that about data profiling. There's another one, Monte Carlo \u2013 I think\
    \ they also have data profiling. There are other tools as well. Unfortunately\
    \ DBT doesn't have that. At least, I think it doesn't have that yet. But it's\
    \ also because it's not the role of DBT. DBT is going to support you in the workflow.\
    \ But on documentation, which is not the same as data profiling, which helps you\
    \ to understand the documentation, so it could be considered part of it, but I\
    \ wouldn't say it's the same thing. DBT actually has a lot regarding documentation.\
    \ It could have more, but it has a lot already. It has a schema YML associated\
    \ with every module and every source. There, you can write descriptions for your\
    \ model and you can also write descriptions for every field if you wanted to.\
    \ Then you can have tags on your models. You can even add your custom metadata\
    \ fields."
  sec: 3057
  time: '50:57'
  who: Victoria
- line: Let's say I want to have a metadata field for the area that the model is allowed
    to be in or something like that. Then all of this goes to these DBT docs, that
    you can host yourself, or it's part of the DBT cloud. There you can see everything
    and you can filter by the model names, the field names, etc. So it has everything
    like that. It has a very small profiling part, which is the amount of rows that
    the table has, table size, and maybe one more little thing, but it's not super
    detailed. It has the code and it has dependencies. It's very easy to go from there
    and see what else you are going to affect if you touch something.
  who: Victoria
---


Links: 

* <https://www.notion.so/Analytics-Engineer-New-Role-in-a-Data-Team-9decbf33825c4580967cf3173eb77177>{:target="_blank"}
* [Victoria's LinkedIn](https://www.linkedin.com/in/victoriaperezmola/){:target="_blank"}

