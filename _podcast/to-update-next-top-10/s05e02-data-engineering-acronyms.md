---
title: "Making Sense of Data Engineering Acronyms and Buzzwords"
short: "Making Sense of Data Engineering Acronyms and Buzzwords"
guests: [nataliekwong]

image: images/podcast/s05e02-data-engineering-acronyms.jpg

season: 5
episode: 2

ids:
  youtube: t9Z1S3OYnJU
  anchor: Making-Sense-of-Data-Engineering-Acronyms-and-Buzzwords---Natalie-Kwong-e177303

links:
  youtube: https://www.youtube.com/watch?v=t9Z1S3OYnJU
  anchor: https://anchor.fm/datatalksclub/episodes/Making-Sense-of-Data-Engineering-Acronyms-and-Buzzwords---Natalie-Kwong-e177303
  spotify: https://open.spotify.com/episode/1AvtwdcAXGGjdJ7fl0Hsuw
  apple: https://podcasts.apple.com/us/podcast/making-sense-of-data-engineering-acronyms-and/id1541710331?i=1000534990760

transcript:
- line: This week we'll try to make sense of common engineering acronyms and buzzwords
    with the help of our special guest today, Natalie. Natalie works at Airbyte, focusing
    on building user experience and overseeing analytics. Your expertise includes
    scaling analytics teams and systems from the ground up. Welcome, Natalie.
  sec: 94
  time: '1:34'
  who: Alexey
- line: Thank you. Happy to be here.
  sec: 116
  time: '1:56'
  who: Natalie
- header: "Natalie\u2019s background"
- line: Before we go into our main topic of understanding these acronyms and buzzwords,
    let's start with your background. Can you tell us about your career journey so
    far?
  sec: 118
  time: '1:58'
  who: Alexey
- line: "Yeah, sure. I've been in startup tech for my entire career. I actually started\
    \ out in the Bay Area at Vox, doing marketing operations. Then I moved into marketing\
    \ analytics at a company called Admiral. I really went deeper into analytics there,\
    \ doing R, SQL, a little bit of Python, and really ended up becoming an acquisition\
    \ analyst. This involves looking at both marketing and sales and how they interact\
    \ \u2013 so that would be building out multi-touch attribution models and things\
    \ like that."
  sec: 128
  time: '2:08'
  who: Natalie
- line: "After that, I moved a little bit more into operations at AppDynamics, which\
    \ has been acquired by Cisco, and then moved to actually manage my own team at\
    \ a company called Keep Truckin\u2019, which is focused on more on the IoT space,\
    \ filling out dashcams and ELDs for the trucking industry. There, I built out\
    \ a team of about 11 analysts, already from marketing and sales to customer success\
    \ and product. Then I moved on to Harness doing a customer sales ops role. So\
    \ I really kind of straddled that analytics and operation space. Now I'm in Airbyte,\
    \ doing growth and analytics."
  who: Natalie
- header: Airbyte
- line: What does Airbyte do?
  sec: 199
  time: '3:19'
  who: Alexey
- line: "Airbyte is an extract/load or \u201CELT\u201D platform \u2013 with Transform\
    \ being the T \u2013 that essentially allows you to ingest a lot of different\
    \ data from different sources, maybe APIs like AdWords or Facebook ads, weave\
    \ it in data warehouses like Snowflake, and bring them into your data warehouse."
  sec: 202
  time: '3:22'
  who: Natalie
- header: What is ETL?
- line: "You mentioned a few things \u2013 transform, ingest, and ELT. We wanted to\
    \ talk about this today. Actually, this is a question I get sometimes. Not super\
    \ often, but it pops up: \u201CWhat's the difference between ELT/ETL, all these\
    \ acronyms \u2013 what do they actually mean?\u201D That's why we\u2019re having\
    \ a conversation today \u2013 to finally figure that out and help everyone else\
    \ with that. Let's start with ETL, which is probably the oldest concept from data\
    \ engineering. I think it was used even before the term \u2018data engineering\u2019\
    \ even existed. I think it's pretty old, coming from business intelligence times\
    \ or even older. I don't know. So what is ETL?"
  sec: 226
  time: '3:46'
  who: Alexey
- line: "ETL stands for \u2013 E is the extract, T is the transform, and L is the\
    \ load. When we think about ETL, we're really thinking about extracting the source-specific\
    \ routines where you pull selected data out of an external system. The transform\
    \ layer is kind of your specific business logic. Your organization is going to\
    \ have some sort of logic that really defines how you pull the data or certain\
    \ use cases that you have that are operational. Then the loading piece is where\
    \ you have destination-specific routines to push data into the place where it's\
    \ going to be consumed. So that's kind of the traditional way to think about it."
  sec: 270
  time: '4:30'
  who: Natalie
- line: "Can you think of an example? Let's say there are some sources, right? We\
    \ extract data from these sources, transform the data somehow, and then put it\
    \ in a data warehouse. Can you think of an example for this \u2013 you mentioned\
    \ something like Facebook ads or something like this?"
  sec: 313
  time: '5:13'
  who: Alexey
- line: "Generally, you might see \u2013 if you're working in the marketing space,\
    \ for example \u2013 your data is stored in Google AdWords, because you're running\
    \ data or you're running ads on Google. Or maybe the same thing but with Facebook.\
    \ If you're working in sales, your data might be stored in Salesforce, your CRM.\
    \ If you're working in finance, it might be stored in NetSuite, maybe. So all\
    \ of these different kinds of API sources all house some data that your business\
    \ needs to build some picture of how the business is doing. Those sources would\
    \ be the places that we would extract from."
  sec: 332
  time: '5:32'
  who: Natalie
- line: The example is that your background is more in marketing, as I understood.
    You would want to extract some things from Google AdWords and from Facebook, right?
    There is something interesting in this data that you want, and then you do some
    transformation on it. You go to Google AdWords, it returns you some data, and
    then you want to transform this data. Is that right?
  sec: 369
  time: '6:09'
  who: Alexey
- line: "Yeah, exactly. One really good use case that we could speak to here \u2013\
    \ just to be a little bit more concrete \u2013\u201CWhat is your cost to acquire\
    \ a customer?\u201D You need an accurate CAC, in other words. In order to get\
    \ that, you need to know how many customers that you've specifically acquired\
    \ from, let's say, Google AdWords. You also need to know how much is being spent\
    \ to acquire those customers. The only way to really concretely bridge those things\
    \ is to pull out data from your CRM, which stores all of your revenue information\
    \ and where the customers came from. Then you also pull up the spend data from\
    \ a more upper-funnel source. Then you merge those together using the transform\
    \ capability."
  sec: 397
  time: '6:37'
  who: Natalie
- line: And then everything eventually goes to the data warehouse, which you use for
    building reports. Then you see how much money was spent? Is that right?
  sec: 438
  time: '7:18'
  who: Alexey
- line: "Exactly. Yep. The way that you finish out the process is \u2013 once it's\
    \ loaded in the data warehouse, in this traditional ETL model, you'd essentially\
    \ have a data mart that specifically says, \u201CHey, this is the data mart that\
    \ answers that question.\u201D Then you would have a visualization tool like Looker\
    \ or Superset in order to show that from a visualization perspective \u2013 bring\
    \ it out to the business so that they can actually consume the insights."
  sec: 447
  time: '7:27'
  who: Natalie
- header: Why ELT instead of ETL?
- line: What is ELT, then? Why do we want to switch to this tool?
  sec: 477
  time: '7:57'
  who: Alexey
- line: "I think the traditional way to think about this is \u2013 ETL is just a little\
    \ bit more inflexible. The business logic changes a lot of the time and you're\
    \ going to receive friction whenever you need to change part of this pipeline.\
    \ So because you're transforming it before you load it into a data warehouse,\
    \ it's difficult to actually bring in new data. Let's say, there's a new table\
    \ or a new field that gets added to Salesforce, the new data that you're collecting\
    \ or the new data source, it's fairly inflexible to just go ahead and add those\
    \ things. It often will force data to be completely re-extracted, which takes\
    \ much more computation and much more time than is really necessary for small\
    \ changes like this."
  sec: 483
  time: '8:03'
  who: Natalie
- line: "You also have this lack of autonomy. What we've generally seen is that these\
    \ ELT tools are actually managed by engineering teams. When analysts \u2013 who\
    \ are working more with the business end \u2013 have these needs, they actually\
    \ have a dependency on an external team to go and compute those. This, of course,\
    \ creates more cycles and takes more time to make these changes. Really the crux\
    \ of it is \u2013 it requires engineering to be actually involved."
  who: Natalie
- line: So ELT is really generalizing to the ETL. Instead of having the transform
    be in the middle, in ELT, the T is at the end. Thus, instead of having a tool
    to actually manage the transformation for you, you're actually bifurcating the
    E-L and the T. Everything is loaded into your data warehouse and then the transformation
    happens after the data is loaded. The transformation actually happens within the
    data warehouse itself, the destination.
  who: Natalie
- header: Transformations
- line: "Yeah, thanks. We already have a comment about transformations. The question\
    \ is, \u201CWhen you say transform, can you elaborate so that we can understand\
    \ what\u2019s happening here?\u201D Like, \u201CWhat kind of transformations do\
    \ we run?\u201D"
  sec: 600
  time: '10:00'
  who: Alexey
- line: "Yeah, we definitely can be more specific about that. It can go from the very\
    \ basic \u2013 the simplest transformation I can think of is something like changing\
    \ a column type from a numeric to a character one. That's a very basic transformation.\
    \ It's almost like it's a casting of a column to a different data type. The more\
    \ complex transformations generally will join across different data sources. So\
    \ you'll say \u201CI want to grab AdWords data and Salesforce data, join them\
    \ using some kind of unique identifier, and then figure out how to show these\
    \ data sources alongside each other in some sort of finalized data model.\u201D\
    \ Generally, we think of these as a kind of transformations that you're running\
    \ in SQL. These can be very simple SQL statements or pretty complex ones. But\
    \ those are the two ways that I see transformation being done."
  sec: 622
  time: '10:22'
  who: Natalie
- line: "When you swap the T and L, so that the T comes at the end, you said the reason\
    \ for this is \u2013 when T is in the middle (ETL) it's not flexible because the\
    \ business logic can change. Then you also depend on engineering teams. I also\
    \ imagine that, let's say the data we extract from the source, we don't need the\
    \ entire response from the ads \u2013 if we\u2019re talking about marketing. So\
    \ this service gives us some response. Let's say we keep only one part of this\
    \ response, if we're interested in how much money we spent, for example."
  sec: 679
  time: '11:19'
  who: Alexey
- line: "So we keep only this data, we transform it, and we load it to our data warehouse,\
    \ only the specific part. Later somebody comes and says, \u201CHey, what about\
    \ some other thing from Google AdWords?\u201D and you reply \u201COkay, sorry,\
    \ because our T was only keeping this part and we don't have the rest of the data.\u201D\
    \ Thus, by keeping the entire thing and then doing the transformation later, if\
    \ somebody comes to us and asks for something extra, then the data is there. We\
    \ just write another transformation on top of the data that we already extracted.\
    \ Is that right?"
  who: Alexey
- line: Exactly. Yep.
  sec: 757
  time: '12:37'
  who: Natalie
- header: How does ELT help analysts be more independent?
- line: "Yeah, and this part about depending on engineering teams \u2013 I'm curious.\
    \ How does it help analysts to be more independent now? Why do they not depend\
    \ on engineers now?"
  sec: 759
  time: '12:39'
  who: Alexey
- line: "Generally, analytics teams operate within the data warehouse itself. I know\
    \ you recently had an interview with Victoria, an analytics engineer. There's\
    \ sort of a rise of this analytics engineer role, which is a role that is generally\
    \ found on the analytics team. Essentially, it\u2019s managing the process from\
    \ the pipelines to the data warehouse and building out that transformation later.\
    \ Instead of business analysts or product analysts going to the engineering team,\
    \ which are generally more focused on the data platform or data infrastructure,\
    \ we can actually see this rise of the analytics engineer role. This role allows\
    \ there to be autonomy within the analytics team itself. That allows them to not\
    \ only understand the business, its needs, and impact, but also to be able to\
    \ make their changes very quickly."
  sec: 772
  time: '12:52'
  who: Natalie
- line: Basically, analysts were not necessarily strong engineers, so we have an analytic
    engineer role that can help them if something is more complex than just writing
    the usual SQL query, right?
  sec: 825
  time: '13:45'
  who: Alexey
- line: "Yeah. I think a lot of these transformations can honestly be done using SQL.\
    \ That's just very ubiquitous \u2013 it's a very well understood, very common\
    \ language. The level of access or the level of ability to access it and build\
    \ your own transformations \u2013 that barrier is much lower. Even if the team\
    \ is so small that you don't have an analytics engineer, you're essentially empowering\
    \ your analysts to be much more full-stack and say, \u201CI know that the data\
    \ is in the data warehouse, all I have to do is write SQL using something like\
    \ DBT. Then I can service any requests or generate any insights autonomously.\
    \ That reduces my time to be able to make positive relationships with my stakeholders.\u201D"
  sec: 840
  time: '14:00'
  who: Natalie
- line: Also, if the data is already extracted, I guess you have fewer steps to run.
  sec: 894
  time: '14:54'
  who: Alexey
- line: Yeah. Honestly, a big part of it is also speed. Because it's already there
    and because these data warehouses have really scaled out how much time it takes
    to compute. The cost of storage is also way down and has produced a ton over time.
    The amount of speed it takes to actually even do these computing calculations
    is much lower.
  sec: 903
  time: '15:03'
  who: Natalie
- header: Data marts and Data warehouses
- line: "You also mentioned one thing when talking about ETL \u2013 this thing called\
    \ data mart. We also talked about the data warehouse. What are those? What is\
    \ a data mart? What is a data warehouse? What is the difference between them?"
  sec: 930
  time: '15:30'
  who: Alexey
- line: "=Data marts are very specific. Maybe we can use marketing again as a use\
    \ case. In this case, you could say \u201CI'm going to build a data mart to serve\
    \ a dashboard that I'm going to build in Superset or Looker.\u201D That data mart\
    \ specifically contains the average spend \u2013 the Facebook spending \u2013\
    \ aggregates. You put them together, build out how many leads came in from those\
    \ sources, how many customers actually converted from those sources, and actually\
    \ serve a marketing use case. On the same level, you can produce data marts for\
    \ sales, finance, or product. But they each serve a certain use case for the business."
  sec: 945
  time: '15:45'
  who: "I think of data warehouses sort of as places to store data marts. When I think\
    \ about data warehouses, there's an ingestion layer. Some users of ours, they'll\
    \ call it an ingestion DB. Maybe within your data warehouse, you have multiple\
    \ databases. That first layer is almost like the rawest form that comes from Airbyte.\
    \ You hook your data warehouse up to, let's say, Snowflake, and you have a database\
    \ called \u201Cingestion DB\u201D. That's essentially it \u2013 you don't touch\
    \ it \u2013 but that is where your next layer comes from. This could be maybe\
    \ a common layer, which is something that maybe several teams can draw from in\
    \ order to build out the data marts."
- line: So a data mart is basically a bunch of tables within a database, right? If
    I understood that correctly.
  sec: 1039
  time: '17:19'
  who: Alexey
- line: "Yeah, it\u2019s post-transformation. I think you can have a lot of different\
    \ types of data tables. But the ones that I would consider a data mart is like\
    \ a finalized table \u2013 it's almost production-ready. A business user can take\
    \ this and there are enough guardrails in place so that when they do pull metrics\
    \ out of it, they're sanitized. They're ready to use and the business user can\
    \ trust the data that comes out of there."
  sec: 1045
  time: '17:25'
  who: Natalie
- header: Ingestion DB
- line: "So ingestion databases are everything that comes before data marts, right?\
    \ This is where the data that is maybe dirty or not cleaned or that is not aggregated\
    \ \u2013 this is not something that business users can use. Right?"
  sec: 1075
  time: '17:55'
  who: Alexey
- line: "Exactly. It's the rawest form. We generally wouldn't want business users\
    \ to be pulling off the raw forms of data, because they'll probably have to do\
    \ some transformation. That transformation might not be consistent across different\
    \ users in the business. So in order to reduce the potential mistakes or different\
    \ interpretations of the data down the line, that's why that transformation layer\
    \ exists \u2013 to separate and bifurcate the ingestion from the actual business\
    \ users and the data marts that they use."
  sec: 1091
  time: '18:11'
  who: Natalie
- header: ETL vs ELT
- line: "So previously, in ETL, we would extract some data, we would immediately do\
    \ the transformation, apply it perhaps without saving it, and then put it into\
    \ a data warehouse or data mart. Now the data that we extract, we first put it\
    \ to the ingestion database, where we keep it, and then we run transformation\
    \ on top of this. Then we pull it again to create some tables that we call data\
    \ marts. This is where the data that is used by the final users \u2013 the business\
    \ users \u2013 is where we keep it. Is that right?"
  sec: 1127
  time: '18:47'
  who: Alexey
- line: "Yeah, exactly. Going back to ELT vs ETL \u2013 previously, these transformations\
    \ might have been done outside the data warehouse, and now we're bringing it into\
    \ the data warehouse. That's the biggest difference here. That transform layer\
    \ is essentially operating within the destination and then does the transformation,\
    \ creating new tables within the exact same destination."
  sec: 1166
  time: '19:26'
  who: Natalie
- header: Data lakes
- line: And what is a data lake?
  sec: 1190
  time: '19:50'
  who: Alexey
- line: "Yeah, it's interesting because a data lake has some similarities to data\
    \ warehouses. But a data lake is much more unstructured. When we think about data\
    \ warehouses, they're all relational tables \u2013 they all have set schemas.\
    \ You can very easily pull from them using SQL. When we think about data lakes,\
    \ they're a little bit more unstructured. I'd say the place that I've seen it\
    \ become very useful is when I was at Keep Truckin\u2019. We were in the IoT business,\
    \ so we had a bigger warehouse and we had Snowflake. But the data that we had\
    \ on all our customers weren\u2019t always in the table format. We would sometimes\
    \ be collecting videos using our hardware, and those are files. Those files are\
    \ not things that data warehouses can store and read. That's something that really\
    \ belongs in a data lake, which is a lot more unstructured and can support these\
    \ different file types."
  sec: 1192
  time: '19:52'
  who: Natalie
- line: Basically, we just dump everything into a lake and then later figure out how
    to actually make it cleaner, more organized, and more structured. Is that right?
  sec: 1259
  time: '20:59'
  who: Alexey
- line: "Yes, it's definitely interesting at a very raw level. I know there are certain\
    \ other terms like \u2018data swamp\u2019 or things that were, you know\u2026"
  sec: 1271
  time: '21:11'
  who: Natalie
- header: Data swamps
- line: "We actually have a question about this, \u201CWhat is a data swamp? How can\
    \ a lake become a swamp?\u201D"
  sec: 1282
  time: '21:22'
  who: Alexey
- line: "Yeah, I think when I've heard that term it's generally because there's maybe\
    \ low quality or maybe very unrefined data. I've also heard this term refer to\
    \ places or data lakes that have essentially become large places of just unused\
    \ data. You put so much in there, and there's so little organization that it\u2019\
    s very difficult to actually be able to utilize what\u2019s in there. Maybe over\
    \ time, especially as new people come in or people leave the team, it becomes\
    \ harder and harder to manage what is there and what is usable. Yeah, I heard\
    \ that term being used as a generic term to refer to data lakes that essentially\
    \ have low quality data \u2013 data that people can't trust."
  sec: 1289
  time: '21:29'
  who: Natalie
- header: Data governance
- line: "Yeah, there is another buzzword, \u201Cdata governance\u201D \u2013 I guess\
    \ this refers to making sure that your data lake doesn't become a swamp. When\
    \ you make sure that the data is clean, what kind of data is there, everything\
    \ is accounted for. So you just keep it more organized, I guess."
  sec: 1341
  time: '22:21'
  who: Alexey
- line: "The data governance term also definitely applies to data warehouses. I have\
    \ one company I worked at, we had this schema called \u201Cad hoc.\u201D Of course,\
    \ people are going to throw things into \u201Cad hoc\u201D whenever they want\
    \ \u2013 there are no rules around it. So part of the data governance that we\
    \ did was, \u201CHow do we ensure that in certain databases or schemas, it's always\
    \ clear what they're used for. It\u2019s always clear how long things will stay\
    \ there.\u201D Because I've kind of married into the definition of \u201CHow is\
    \ this useful?\u201D Of course, there's always this continual inspection of what\
    \ is there, in order to ensure that it is still relevant or still will be used.\
    \ Rather than having almost a trash bin that never gets empty. You want to make\
    \ sure that your data warehouse or your data lake has that level of quality and\
    \ relevance."
  sec: 1368
  time: '22:48'
  who: Natalie
- line: "Maybe not a trash bin, I'm thinking about my basement, which has all the\
    \ things that I don't need right now. I don't know what to do with them. I don't\
    \ want to throw them away yet. So what to do with them? I'll just put them in\
    \ my basement and figure out what to do with them later. You can do the same with\
    \ data, right? \u201CDo I need to track this data? Maybe I do. Let's track it.\
    \ Let's keep this data.\u201D Then one year later, you have this huge data source\
    \ that nobody uses. So it becomes a swamp."
  sec: 1427
  time: '23:47'
  who: Alexey
- line: Yeah, exactly.
  sec: 1463
  time: '24:23'
  who: Natalie
- header: Ingestion layer vs Data lake
- line: "We also talked about the ingestion layer and the ingestion database. We talked\
    \ about the data lake. I\u2019m wondering \u2013 to me, they look similar. First\
    \ of all, are they similar? Are they the same? Or are those different things?"
  sec: 1464
  time: '24:24'
  who: Alexey
- line: "Yeah, I think Evo actually came up with a good article on this too. Maybe\
    \ we can put it in the links. She wrote about the difference and how they might\
    \ be converging in some ways. I'd say there's still relevance for both. Data lakes\
    \ are obviously going to be more flexible \u2013 they're going to be able to support\
    \ a lot more different file types and structures. That's the thing that data warehouses\
    \ don't do. So there's a purpose for both. From what I've noticed, data warehouses\
    \ are generally very helpful for smaller or intermediate-sized teams. As your\
    \ needs grow and become more complex \u2013 maybe your organization gets larger\
    \ \u2013 you may need to move to the data lake structure, which offers flexibility.\
    \ As your team organization grows, it might be something that you have to weigh\
    \ the pros and cons of, whether to even add a data lake as an addition, or potentially\
    \ migrating fully to it. But a lot of the functionalities of the industry are\
    \ allowing for the flexibility to choose between a data lake and a data warehouse."
  sec: 1485
  time: '24:45'
  who: Natalie
- line: "Basically, the ingestion database is a part of a data warehouse, right? Maybe\
    \ this is one of the tables in the data warehouse. Let's say we\u2019re talking\
    \ about Snowflake \u2013 this can be one of the tables that are already in Snowflake.\
    \ It's just that the end users, the business users or analysts, don't use this\
    \ particular table, but it's still part of the warehouse. Is that right?"
  sec: 1556
  time: '25:56'
  who: Alexey
- line: "We were talking about the ingestion database. This is where we keep intermediate\
    \ results. To me, a data lake also seems like a place where we keep intermediate\
    \ results. So I was wondering \u2013 are the ingestion layers part of the data\
    \ warehouse or not?"
  who: Alexey
- line: "I think in the analytics team framework, it generally is ingesting into a\
    \ data warehouse, not a data lake. Because they're generally dealing with different\
    \ APIs, different sources, and then doing that transformation there and, of course,\
    \ doing the visualization on top. From an analytics team perspective, I think\
    \ the data warehouse is the most relevant. Where it may not be as relevant is\
    \ maybe for engineering teams, who need data lakes to power parts of their application,\
    \ or maybe data science teams who need to parse through lots of data that isn't\
    \ necessarily in a structured format in order to do their analysis. I think it\
    \ depends on your business use case, what kind of team you're on, and what is\
    \ helpful for you. You have to make that call \u2013 what are the capabilities\
    \ that you really need to get your work done? Essentially, you choose the solution\
    \ from there."
  sec: 1607
  time: '26:47'
  who: Natalie
- header: Do you need both a Data warehouse and a Data lake?
- line: "We have a question \u2013 \u201CDo we need to have both a data lake and a\
    \ data warehouse?\u201D I think, from what I understood, the answer was \u201C\
    Yes.\u201D Right? We have the raw data in the lake. We have prepared data in a\
    \ data mart in a data warehouse. Then if somebody such as data scientists, like\
    \ you said in your example \u2013 if they need to parse through raw data, they\
    \ can just go ahead and do it."
  sec: 1659
  time: '27:39'
  who: Alexey
- line: "I don\u2019t think you need to have both. We don't necessarily need it in\
    \ our business to have both. It really depends on the complexity of your business.\
    \ From an analytics perspective, generally, if I'm in the analytics team, I probably\
    \ will never touch a data lake. I\u2019ll probably operate within the data warehouse.\
    \ But I know that there are teams within the organization that might rely on more\
    \ of a data lake structure instead. I think it really depends on the complexity\
    \ of the business and what different teams need."
  sec: 1687
  time: '28:07'
  who: Natalie
- line: Yeah. I prepared a question, but I think you already answered it. Let me ask
    the question and maybe I can answer it and then you tell me if I'm right.
  sec: 1718
  time: '28:38'
  who: Alexey
- line: Sure.
  sec: 1729
  time: '28:49'
  who: Natalie
- line: "Let's say we have an ecommerce online shop. We want to track some events\
    \ there \u2013 so clicks. Every time a user comes to our online shop and selects\
    \ a product, clicks on this product, we track this event. These events \u2013\
    \ these clicks \u2013 they end up in the data lake where we keep the clicks. I\
    \ have a bunch of SQL queries to transform these clicks into something else \u2013\
    \ so aggregate, calculate some statistics. I'm a data scientist, so what I do\
    \ is run some machine learning on top of these clicks. For example, I have a model\
    \ that wants to predict how many clicks there will be for each product. So I need\
    \ to use this information about the clicks. I write some SQL queries, extract\
    \ these clicks, and I build the model for that. Maybe instead of building a model,\
    \ I just put the clicks into a dashboard. Then the top management sees \u201C\
    Okay, in this category, we have that many clicks. In that category, we have that\
    \ many clicks.\u201D Then to orchestrate everything, in our company at least,\
    \ we typically use Airflow for all these things."
  sec: 1730
  time: '28:50'
  who: Alexey
- line: "So the question is, \u201CIs this ETL, or ELT?\u201D I think \u2013 let me\
    \ answer this and you correct me \u2013 I think this is ELT. Because first, we\
    \ dump everything into a data lake \u2013 we don't change the raw events. We leave\
    \ them be in the data lake. Then there are other jobs \u2013 other transformation\
    \ jobs \u2013 that take the raw data, transform, and then eventually put this\
    \ in a model or in a dashboard. Right?"
  who: Alexey
- line: Exactly. Yeah. You're not using a tool to do that transformation. You yourself
    are taking all the data that has been loaded into your area, and then doing something
    with it. Exactly.
  sec: 1844
  time: '30:44'
  who: Natalie
- line: "Yeah. All this time I thought that Airflow was an ETL tool, but it\u2019\
    s actually an ELT tool, right?"
  sec: 1859
  time: '30:59'
  who: Alexey
- line: "Airflow? Yeah, I think it's very much like an orchestrator. It also helps\
    \ to just schedule. But ultimately, yeah. Everybody has a very good integration\
    \ with Airflow that essentially runs your Airbyte jobs, using Airflow. So yeah\
    \ \u2013 we also use Airflow here."
  sec: 1872
  time: '31:12'
  who: Natalie
- header: Airbyte and ELT
- line: "I think you mentioned at the beginning what Airbyte does \u2013 it's about\
    \ transformation, right? It's about ingesting and then putting it into a data\
    \ warehouse. Maybe now we can try to make sense from all these buzzwords. We know\
    \ what the transformation means. This is taking the data and changing it a little\
    \ bit. Then ingestion is about putting something into a data warehouse. Then a\
    \ data warehouse is basically the database that we use for all these analytical\
    \ purposes. So yeah, maybe you can tell us now what Airbyte does?"
  sec: 1891
  time: '31:31'
  who: Alexey
- line: "Yeah, so everybody tackles the E-L part. That's our main goal \u2013 to ensure\
    \ that the E-L is as seamless and reliable as any other product on the market\
    \ and that you have a great understanding and expectation of what the output in\
    \ your data warehouse is going to be. We also integrate really well with DBT,\
    \ right within the product. So we're not handling the transformation ourselves,\
    \ per se, but we're relying on DBT as a part of our product to ensure that analysts\
    \ can use DBT to do those SQL transformations once the data is there. We're not\
    \ like a transform product necessarily, but we just integrate really well with\
    \ that and have embedded that into our product."
  sec: 1931
  time: '32:11'
  who: Natalie
- line: "One thing I didn't actually mention earlier is that Airbyte is also open\
    \ source. We are really focused on building our community, enabling users \u2013\
    \ people out there who are excited to contribute back to our project \u2013 to\
    \ enable those people to actually build out potentially new connectors or maybe\
    \ even amend existing ones, and contribute back to our project."
  who: Natalie
- line: DBT is also open source, right?
  sec: 2011
  time: '33:31'
  who: Alexey
- line: Yes, exactly. DBT is also open source. It's part of that modern data stack,
    you could say, for the evolution towards more open source tools. They also have
    a cloud product.
  sec: 2013
  time: '33:33'
  who: Natalie
- header: Modern data stack
- line: "Yeah. So speaking of this modern stack, I've heard this term many times and\
    \ actually we have a talk about this quite soon. It's about this modern stack\
    \ for analytics. Actually the talk we have is \u201Cmodern data stack for analytics\
    \ engineering.\u201D I don't know if there are different stacks for analytics\
    \ and for analytics engineering \u2013 probably they\u2019re the same. So, what\
    \ is it? Can you tell us a bit about it? Which tools are a part of this stack?\
    \ Why do we even talk about it? Why is it a thing?"
  sec: 2025
  time: '33:45'
  who: Alexey
- line: "So why it's a thing \u2013 because essentially, you are now able to choose\
    \ each piece of the stack individually instead of having a platform approach where\
    \ \u201Cone fits all\u201D \u2013 where you have a lot of vendor lock-in. You\
    \ now get to choose the best of breed for each of the pieces of the data puzzle.\
    \ For extract and load obviously, there's Airbyte. There are also incomes like\
    \ Fivetran that have been around for quite a bit longer. From a data warehousing\
    \ perspective, you have Snowflake, you have Databricks, BigQuery, Amazon Redshift.\
    \ Then for transformation, you have DBT. Outside of DBT and all the features it\
    \ provides, you could just write SQL and that would also work as well. Then from\
    \ a visualization perspective, we see new tools like Superset being adopted fairly\
    \ well. Then obviously, incumbents like Looker, or even Tableau. The idea of the\
    \ modern data stack is that instead of having one solution that tries to do it\
    \ all, you're essentially picking and choosing the one that really fits with what\
    \ you need the best."
  sec: 2063
  time: '34:23'
  who: Natalie
- line: So basically, it's a bunch of tools that work really well together.
  sec: 2138
  time: '35:38'
  who: Alexey
- header: Reverse ETL
- line: Yeah, and of course, we can't forget Airflow, which does a lot of the orchestration.
    Then there's also this emerging space of reverse ETL, where you'll have tools
    like Hightouch or Census, and even Airbyte is thinking about going into this space
    as well.
  sec: 2142
  time: '35:42'
  who: Natalie
- line: "Yeah, so can you tell us a bit more about this \u201Creverse ETL\u201D? Or\
    \ should it be reverse ETL or reverse ELT? Or what is that anyways? Why is it\
    \ reverse? Why would you want to reverse it?"
  sec: 2162
  time: '36:02'
  who: Alexey
- line: "=In the past, what I've seen data teams use is maybe a Python wrapper to\
    \ push data back into Salesforce. These \u201Creverse ETL\u201D tools are enabling\
    \ really low-code solutions for salespeople or marketers to actually come and\
    \ just kind of \u201Cpoint and click\u201D and say, \u201CI want to copy this\
    \ table and the output of this table in this data warehouse and bring it back\
    \ into my source system to be able to action on it.\u201D You don't have to be\
    \ technical \u2013 it's pretty low-code or no code. That's really something that's\
    \ very powerful, because it essentially allows analytics to be a function within\
    \ the organization itself. It allows analysts to really be very aligned with what\
    \ the business needs."
  sec: 2174
  time: '36:14'
  who: "Reverse ETL is definitely something that a lot of data teams are trying to\
    \ already solve today using custom scripts that bring a lot of that analysis that\
    \ analytics teams do. It also brings that back into the operational systems that\
    \ business users actually need that data in. One good example is \u2013 let's\
    \ say that an analytics team is working on a lead scoring model. Essentially,\
    \ it says, \u201CI have 100 leads. I rank them using behavioral data, demographic\
    \ data. I take this information and I rate these leads from 1 to 100 on what the\
    \ priority is \u2013 who you should reach out to.\u201D Traditionally, that data\
    \ would just live in a data warehouse and maybe in a visualization tool too. If\
    \ I'm a salesperson, I need that data in the system that I'm using to actually\
    \ action on it."
- line: "Basically, before, engineers would need to write a bunch of scripts for doing\
    \ this. This is emphasized in the healthcare APIs that allow them to push the\
    \ data there. But I guess it's not easy to maintain these scripts and it's also\
    \ not the core business of the companies to do that. So there are some tools that\
    \ actually allow you to have this drag-and-drop experience, so you can say, \u201C\
    Okay, this data from this table in my BigQuery or Snowflake should go in my Salesforce\
    \ or something else.\u201D Right?"
  sec: 2281
  time: '38:01'
  who: Alexey
- line: "Exactly. Yeah. I would still consider this reverse-ETL, not reverse-ELT,\
    \ because that transformation is not happening in that source where you're pushing\
    \ it back to. The transformation is still happening before you move it out of\
    \ the database. Really, it's like a porting of the more finalized\u2026 maybe\
    \ you could even call it a data mart and bring it back into the source. No transformation\
    \ is actually happening in the source system itself."
  sec: 2316
  time: '38:36'
  who: Natalie
- header: Is drag-and-drop killing data engineering jobs?
- line: "To make sure I understood the whole picture: we have some of these tools\
    \ like Google AdWords \u2013 all these systems, like Google AdWords, or Facebook\
    \ Ads, or whatever. We first need to take the data from there and import \u2013\
    \ put it into our data warehouse or ingest. We import and then we do something\
    \ and then we export back, right? Or using the terminology we just learned, we\
    \ first extract, then do something, and then we do this reverse extract, and then\
    \ put that back."
  sec: 2346
  time: '39:06'
  who: Alexey
- line: "Speaking of this low-code/no-code, we have a question related to that. \u201C\
    Is the data engineering job dying with all these tools that give a drag-and-drop\
    \ experience? Since you can do these kinds of drag-and-drop data pipelines with\
    \ all these built integrations?"
  who: Alexey
- line: "I would not say dying, I think it is very much evolving. I think in data\
    \ engineering, these tools are essentially allowing for the more mundane parts\
    \ of data engineers\u2019 job to disappear and allow for them to focus on other\
    \ things. For example, in my team at Keep Truckin\u2019, our data engineer was\
    \ very much focused on a lot more data infrastructure pieces, instead of being\
    \ focused on managing pipelines and waking up in the morning, and feeling like,\
    \ \u201COh, these pipelines have broken, and I need to go fix that. This field\
    \ was deleted.\u201D It was more around tooling for the analytics team \u2013\
    \ ensuring that we have proper data governance pieces in place."
  sec: 2413
  time: '40:13'
  who: Natalie
- line: "There are a lot of things that really are beyond the technical scope of even\
    \ maybe any analytics engineer or an analyst \u2013 where a data engineer most\
    \ definitely can enable that data team to be operating very efficiently. Something\
    \ like common code standards, being able to bring the analytics team to a place\
    \ where they can be pushing out in a nearly-continuous delivery process. They\u2019\
    re ensuring that there's validation of the code and that pipelines aren't breaking\
    \ from the data team and what they're producing. There are a lot of pieces that\
    \ I think the data engineer can now actually go and tackle that the analytics\
    \ team might not necessarily be very focused on. But without these things, they\
    \ actually can't be successful."
  who: Natalie
- line: "We talked about these scripts that people would write before reverse ETL\
    \ tools existed. I imagined that maintaining the scripts was a nightmare because\
    \ they break in unpredictable ways. For example the API changes and then all your\
    \ scripts are not working. Then you have to deal with all these intricacies \u2013\
    \ I\u2019m guessing that this is not fun at all. A data engineer would probably\
    \ rather focus on other things. I'm not a data engineer, but I don't really want\
    \ to even think about maintaining scripts for talking to some third party tools\
    \ like Salesforce and trying to maintain them. Yeah, I'd rather focus on something\
    \ else. I guess this is why these tools are quite useful and why people love them.\
    \ Data engineers are still happy \u2013 nobody is going to fire them anytime soon."
  sec: 2520
  time: '42:00'
  who: Alexey
- line: Yeah.
  sec: 2581
  time: '43:01'
  who: Natalie
- header: Who is responsible for managing unused data?
- line: "Okay, thanks. We have some more questions. The question is \u201C70-90% of\
    \ beta in many organizations is collected but never used. Who is responsible for\
    \ taking care of that and for noticing that? Data engineers? How should we actually\
    \ go about noticing things like that?\u201D"
  sec: 2582
  time: '43:02'
  who: Alexey
- line: "If I can think back to my time when I took on more of that analytics manager\
    \ role, I would say it's very much a team effort. It's hard to know what is not\
    \ being used if you don't have the business analysts there trying to speak to,\
    \ \u201CWhat are the use cases that we're solving for in that business today?\u201D\
    \ And then tracing that back to the ingestion layer, \u201CWhat is a dependency\
    \ of those use cases? In order to figure out what isn't being used \u2013 I remember\
    \ how we would try to do this on a quarterly or monthly cleanup level \u2013 we\
    \ really try to take a critical look as a team. It wouldn't be on a single person\
    \ to really be responsible to know everything, because that's impossible. We would\
    \ really rely a lot on the business analyst and I guess the analytics engineers\
    \ to have them understand and be able to trace back to what is actually being\
    \ used and what are things that may not be used today, but might be used in the\
    \ future. So you always want to have that forward-looking piece too. Of course,\
    \ this whole idea of ELT is that you have all the data there, and it maybe might\
    \ not be used now, but potentially. If there's a use case for that in the future,\
    \ someone should speak to that.  I don't think it should ever be on one person.\
    \ I think that would be a pretty difficult role to have if it was, because that\
    \ person would be missing the context of the actual business."
  sec: 2617
  time: '43:37'
  who: Natalie
- line: "The person who doesn't miss this context \u2013 who has the context \u2013\
    \ would be an analytics engineer, perhaps or an analyst. Right?"
  sec: 2718
  time: '45:18'
  who: Alexey
- line: "I think it's both the business analyst and the analytics engineer. Because\
    \ the business analyst might be really focused and working with the business,\
    \ but they might not know as much about the pipelining. So they need to work together\
    \ to ensure that they both have a mutual understanding. Then whoever is in charge\
    \ of managing the data governance, the cleanliness of the database, then they\
    \ need to communicate with them that, \u201CHey, this is data that's not currently\
    \ being used,\u201D and then execute on cleaning it up from there."
  sec: 2728
  time: '45:28'
  who: Natalie
- header: "CDC \u2013 Change Data Capture"
- line: "Thank you. Another question we have is, \u201CI have no idea what CDC is.\
    \ Do you know what CDC is?\u201D"
  sec: 2759
  time: '45:59'
  who: Alexey
- line: "Yeah. It's \u201Cchange data capture.\u201D That's a feature that is available\
    \ in our connectors. CDC is essentially a way to be able to capture only changed\
    \ records. That's where the recording product comes from. Essentially, what it\
    \ allows you to do is avoid having to fully replicate your database every time.\
    \ Instead, let's say, I sync my database today \u2013 tomorrow, only 10% of those\
    \ rows have changed. I only want to sync those 10%. And I only want to capture\
    \ those 10% that have changed and then only update those 10% in my destination.\
    \ Without Changed Data Capture, you might have to be doing a whole replication\
    \ every day. That isn't really the optimal way to manage cloud resources, because\
    \ you're consuming more resources to do that replication. By doing CDC, you actually\
    \ have the ability to reduce your own cloud costs if you're self-hosting. But\
    \ also, it's just much faster because you're moving less data."
  sec: 2771
  time: '46:11'
  who: Natalie
- line: "I'm trying to think of an example. I work at OLX, an online marketplace.\
    \ This is a place, let's say, if you want to sell your phone, you go create a\
    \ listing. Sometimes users \u2013 the sellers \u2013 can go and change the title,\
    \ or they can go and change the price. I guess this CDC (Change Data Capture)\
    \ will allow us to see\u2026 let\u2019s say if we have 30 million active listings\
    \ right now on the website \u2013 we don't want to look at the entire database\
    \ of listings. If something changes, if the prices change or titles change, we\
    \ just want to see that and keep the delta (difference between the old version\
    \ and the changes). Or we keep only the new thing instead of taking all the 30\
    \ million records and keeping them over and over again. Is that right?"
  sec: 2846
  time: '47:26'
  who: Alexey
- line: "Yeah, exactly. It\u2019s essentially a performance consideration. It also\
    \ allows you to capture deleted rows. So that's another benefit as well. I think\
    \ that we don't offer it on all of our data warehouse sources yet. But we are\
    \ actively working on building out CDC capabilities for all the sources that essentially\
    \ allow for that."
  sec: 2910
  time: '48:30'
  who: Natalie
- header: Slowly changing dimension
- line: "Do you know what a \u201Cslowly changing dimension\u201D is? I\u2019ve heard\
    \ this term a few times. I'm curious what this is."
  sec: 2938
  time: '48:58'
  who: Alexey
- line: Yeah, I can speak to what I think it means.
  sec: 2945
  time: '49:05'
  who: Natalie
- line: I'm also not 100% sure what it actually is, but I hear this term used many
    times.
  sec: 2950
  time: '49:10'
  who: Alexey
- line: "Yeah, I think in the business, you will probably start a pipeline process\
    \ with maybe 10 columns that you know you need. Maybe over time, if let's say\
    \ a salesperson says, \u201COh, I'm actually now going to collect information\
    \ on whether or not they'd be interested in this new product feature we just launched.\u201D\
    \ And they added maybe a checkbox or maybe a picklist in Salesforce. The slowly\
    \ changing dimension to me, when I hear that term, means your dimensions may change\
    \ over time as your business changes. Now that the sales team is collecting new\
    \ information, you also want to ingest that new information into your data warehouse.\
    \ That will mean that your dimensions change and that you will actually want to\
    \ adjust not just 10 fields, but now 11. Then maybe next week it's 12, because\
    \ now they're collecting something else, or there's another piece of data that's\
    \ relevant to what you need. That's what I think of when I hear that. I hope that\
    \ answers the question."
  sec: 2957
  time: '49:17'
  who: Natalie
- line: "Well, I think the example you gave about a new product feature that a user\
    \ is interested in \u2013 this user is currently interested in this feature, but\
    \ maybe in one year, the user is no longer interested. I guess this doesn't change\
    \ quickly \u2013 it changes slowly, right?"
  sec: 2418
  time: '40:18'
  who: Alexey
- line: "Well, when I think about dimensions, to me, it's like adding a new column\
    \ in a table structure \u2013 the value of that column, the field might change.\
    \ So that's kind of like capturing the history of the field. But ultimately, the\
    \ way to think about it is, you're actually capturing an additional dimension\
    \ of data that you weren't capturing before. I don't think that that ever happens\
    \ all at once in a business. A business is constantly evolving and changing, especially\
    \ if you're small and you're in that growth phase. You're constantly trying to\
    \ think of new things to track, maybe launching new products or new product features.\
    \ There's always going to be this ever-changing and growing set of dimensions\
    \ that you'll want to track and that's where the \u201Cslowly changing dimensions\u201D\
    \ aspect comes into place."
  sec: 2439
  time: '40:39'
  who: Natalie
- header: Are there cases where ETL is preferable over ELT?
- line: Do you know of any examples when we still would prefer ETL over ELT?
  sec: 2490
  time: '41:30'
  who: Alexey
- line: "I would say \u2013 if there's a large enterprise need for it. I personally\
    \ can't speak to being in a major enterprise company and having a need for this,\
    \ but it might be needed there. It might be something that much larger enterprises\
    \ might want to adopt. I think that is kind of the play where ETL has really been\
    \ successful \u2013 in these large enterprises. Where you're potentially combining\
    \ multiple data warehouses or data sources and bringing them together, and then\
    \ pushing them out to multiple data warehouses or lakes. So maybe there's a need\
    \ for this kind of intermediary place, maybe a staging area, where you need to\
    \ ingest from a lot and then you need to propagate out a lot."
  sec: 2500
  time: '41:40'
  who: Natalie
- line: Yeah, I think I worked at an enterprise and we had all these tools like Oracle,
    Informatica, and all these kinds of things. I'm pretty sure if I come back now
    and see what they use it's still Oracle and Informatica. It's been working for
    them pretty well at the bank where I worked. We were processing a lot of data
    there.
  sec: 2558
  time: '42:38'
  who: Alexey
- line: Yeah. If there's a certain use case for it. The place that I could see a use
    case for that kind of staging area and that really complex model, is that intermediary
    that essentially allows you to message things from many places to one and then
    from one to many again. I think smaller companies don't generally have that need
    as strongly but much more complex organizations might be using a different warehouse
    for every business unit, or a different data lake to service different teams.
    That might be where they need some sort of intermediary solution.
  sec: 2584
  time: '43:04'
  who: Natalie
- header: Why is Airbyte open source?
- line: "Thank you. The last question they prepared for you was about\u2026 we talked\
    \ about open source, that Airbyte is open source, and we also talked about DBT\
    \ being open source. Do you know why Airbyte is open source? Why make it open\
    \ source? Aren't you afraid that somebody will come and just steal your code?"
  sec: 2625
  time: '43:45'
  who: Alexey
- line: "Your first question of \u201CWhy open source?\u201D I really think that this\
    \ is the way forward for this space. When you look at incumbents in the place\
    \ like Fivetran, they're never going to be able to support the long tail of connectors\
    \ that really exists out there. This explosion of tools that we're seeing in pretty\
    \ much every space means that every tool has an API, they are all housing your\
    \ business data, and all of that data is really relevant. But there's kind of\
    \ a long tail of connectors that may not be like NetSuite, or like AdWords, like\
    \ these really popular ones, but maybe less popular ones that people are still\
    \ using and experimenting with and trying out and growing with. Those need to\
    \ be supported too. Right now, what we're seeing in this space \u2013 and this\
    \ is how I like to think Airbyte actually came to be \u2013 our founders did a\
    \ bunch of interviews, what they heard was, \u201CYeah, we're using Fivetran or\
    \ Stitch. But we're still writing our own pipelines. We're still building things\
    \ on the side. We're still managing these numbers of scripts that tackle that\
    \ long tail, because the business still needs that data.\u201D"
  sec: 2652
  time: '44:12'
  who: Natalie
- line: That's not the future that we see. We want our community and us to enable
    that community to really be able to support the many connectors that should exist
    out there. We don't see something like a closed source project being able to support
    that. Being open source enables us to work like we have many hands, so to say.
    When people contribute, we accelerate at such a higher velocity that we can actually
    become the standard for data integration.
  who: Natalie
- line: "So basically, if I use some proprietary tool and I use something that this\
    \ proprietary tool doesn't support \u2013 some very unpopular system that, for\
    \ some reasons, we use at work. We need to be able to extract data from there.\
    \ If I use something like Fivetran, as you mentioned, or Stitch, they can say,\
    \ \u201CYeah, we will consider implementing this in five years\u2026 or never.\u201D\
    \ But if you use an open source tool a developer can actually just go ahead and\
    \ implement and then plug this thing into existing infrastructure and it just\
    \ works. Is that right? Is that the main idea?"
  sec: 2766
  time: '46:06'
  who: Alexey
- line: We do see a lot of people actually plugging in their custom connectors. We
    have a place in the UI where you just add a new source. We have a CDK (connector
    development kit) to enable people to build things themselves and it's very flexible.
    People can essentially fork our project and bring in custom connectors that they
    have. Maybe custom business logic or things that they want to ingrain into their
    connector, so they use Airbyte that way.
  sec: 2812
  time: '46:52'
  who: Natalie
- line: "To your second question, though, I think\u2026 We are open source and we\
    \ always want to enable our long-term connectors to be available to anyone to\
    \ use. We want to make it super easy for small or medium-sized teams to just get\
    \ that basic functionality of being able to be supported by connectors anytime.\
    \ We'll always have our connectors be open source. We are coming to the market\
    \ with a cloud offering which is more that enterprise set of features like SSO,\
    \ certain things around security like RBAC (role based access control), and other\
    \ features that generally larger enterprise teams will want. For a small team\
    \ or a single developer, they don't necessarily have a need for these, but they\
    \ just want to get up and running very quickly with connectors and moving data.\
    \ That's the part that will always be a part of our mission and goal."
  who: Natalie
- header: The case of Elasticsearch and AWS
- line: Have you heard about this story about Elasticsearch and AWS? I think everyone
    whose model has open sourcing in their code probably heard about this story. But
    for those who don't know, Elasticsearch had their own cloud offering. So if you
    don't want to maintain your own cluster of Elasticsearch servers, you just go
    to Elasticsearch and use a managed solution. Then one day, AWS decided that they
    also want to provide a managed solution of ElasticSearch. Now Elasticsearch has
    a problem, right? Because AWS just took their code and deployed it. Now, people
    will go to AWS, for example, instead of going to Elasticsearch for a managed solution.
    So, are you not afraid that something like this can happen? That somebody will
    basically do the same thing? And because you're open source, they can actually
    just do this.
  sec: 2906
  time: '48:26'
  who: Alexey
- line: "Yeah, it's definitely something that we think very carefully about. The things\
    \ that we talk about internally are \u201CAre we under the right license? We're\
    \ currently under MIT. Is this the right license for us moving forward, especially\
    \ as we launch cloud?\u201D These are definitely things that we consider very\
    \ carefully. I think probably there\u2019s more to come soon in the coming month\
    \ on that \u2013 on whether we have to make any changes or not. But that\u2019\
    s definitely something that we actively discuss internally."
  sec: 2972
  time: '49:32'
  who: Natalie
- line: "Yeah, I guess many open source companies are starting to think about this.\
    \ This story of AWS and Elasticsearch \u2013 new things keep appearing. Now, all\
    \ of a sudden, Elasticsearch are the bad people because they are starting to hide\
    \ things, they are starting to close source some things. I\u2019m curious to see\
    \ how it will end and I hope Elasticsearch figures it out."
  sec: 3605
  time: '1:00:05'
  who: Alexey
- line: Do you have any last words before we finish?
  sec: 3636
  time: '1:00:36'
  who: Alexey
- header: Conclusion
- line: "It was such a pleasure to be on this, talking about these acronyms. I hope\
    \ it helped some of your listeners get more clarity. Airbyte \u2013 check us out.\
    \ We are also hiring on a lot of different fronts. Not just on the engineering\
    \ front, but also within the go-to-market side as well. So check us out. Our entire\
    \ handle gets listed on our company docs page \u2013 very public. If you want\
    \ to contribute back or check us out, you can do that very easily. All the information\
    \ is on our website."
  sec: 3642
  time: '1:00:42'
  who: Natalie
- line: Thank you. How can people find you if they have a question?
  sec: 3677
  time: '1:01:17'
  who: Alexey
- line: For me, just on LinkedIn - Natalie Kwong. That is the best place to find me.
  sec: 3680
  time: '1:01:20'
  who: Natalie
- line: Ok. Thanks a lot. Thanks for joining us today. Thanks for telling us about
    acronyms. Now I can make sense of them and hopefully, everyone else can as well.
    Thanks, everyone, for joining us and for asking questions and for watching us.
  sec: 3689
  time: '1:01:29'
  who: Alexey

---


Links:

* [Natalie's LinkedIn](https://www.linkedin.com/in/nataliekwong/){:target="_blank"}
* [Why the Future of ETL Is Not ELT, But EL(T)](https://airbyte.io/blog/why-the-future-of-etl-is-not-elt-but-el){:target="_blank"}


