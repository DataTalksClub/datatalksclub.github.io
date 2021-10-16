---
title: "Similarities and Differences between ML and Analytics"
short: "Similarities and Differences between ML and Analytics"
guests: [rishabhbhargava]

image: images/podcast/s05e07-ml-vs-analytics.jpg

season: 5
episode: 7

ids:
  youtube: rMRUa8WxDz4
  anchor: Similarities-and-Differences-between-ML-and-Analytics---Rishabh-Bhargava-e18rcam

links:
  youtube: https://www.youtube.com/watch?v=rMRUa8WxDz4
  anchor: https://anchor.fm/datatalksclub/episodes/Similarities-and-Differences-between-ML-and-Analytics---Rishabh-Bhargava-e18rcam
  spotify: https://open.spotify.com/episode/19fWdSuxTLwIdzVT45qF9x
  apple: https://podcasts.apple.com/us/podcast/similarities-and-differences-between-ml-and/id1541710331?i=1000538713607

transcript:
- line: "This week, we'll talk about the similarities and differences between machine\
    \ learning and analytics. We have a special guest today, Rishabh. Rishabh has\
    \ worked with analytics and machine learning teams for more than seven years.\
    \ Most recently, he led a sales engineering team at a data infrastructure company\
    \ called DataCoral, which was acquired by Cloudera. He was helping analytics teams\
    \ with their data pipelines there. Before that, he was an employee at Premer.ai,\
    \ where he built and deployed machine learning models for multiple natural language\
    \ applications. He also writes a newsletter called MLOpsRoundUp, which discusses\
    \ challenges with machine learning production. Subscribe to that \u2013 it's mlopsroundup.substack.com.\
    \ This is a cool newsletter. I am subscribed, and you should do that as well.\
    \ Welcome, Rishabh."
  sec: 65
  time: '1:05'
  who: Alexey
- line: Thank you for having me, Alexey.
  sec: 126
  time: '2:06'
  who: Rishabh
- header: "Rishabh\u2019s background"
- line: Before we go into our main topic, let's start with your background. Can you
    tell us about your career journey so far?
  sec: 128
  time: '2:08'
  who: Alexey
- line: "Absolutely. You covered a little bit of that, but I'll give you a quick introduction\
    \ myself. Until recently, I was at this data infrastructure company called Datacorel,\
    \ which has just been acquired by Cloudera. In my time there, I had worked on\
    \ engineering, some product work, and then some sales engineering work. Really,\
    \ the goal for the team was, \u201CHow do you help data scientists move data from\
    \ point A to point B as efficiently as possible so that they're not blocked on\
    \ data engineering resources?\u201D We had a nice little product that would allow\
    \ them to do that."
  sec: 135
  time: '2:15'
  who: Rishabh
- line: "Before that, I was doing machine learning work myself at a company called\
    \ Primer. There, we were basically helping customers make sense of a large amount\
    \ of unstructured text. A lot of fun NLP problems including summarization, entity\
    \ extraction, sentiment, classification \u2013 all of those fun things. So that\
    \ was kind of my journey with Primer."
  who: Rishabh
- line: Before that, I was at Stanford doing a Master's in computer science. Lots
    of machine learning classes there. I was also a TA for a few classes, including
    the Andrew Yang machine learning class. As you mentioned at the end I write this
    newsletter called the ML Ops Roundup. It's been a pretty fun journey this past
    year to research, think about what is interesting to the community, and just write
    my learnings there.
  who: Rishabh
- header: "Rishabh\u2019s experience as a sales engineer"
- line: What did you do as a sales engineer? I know it's a bit off topic, but I'm
    really curious, what did you actually do there?
  sec: 224
  time: '3:44'
  who: Alexey
- line: "Absolutely. It's still a very technical role. It's about helping folks who\
    \ are evaluating the product \u2013 \u201CHow to best understand what the capabilities\
    \ are? What are the sorts of problems that it can solve for them?\u201D Basically,\
    \ \u201CWhat are the things that it can do? What are the things that it can't\
    \ do?\u201D A lot of my work was actually just working with prospective customers,\
    \ either doing demos or sometimes running trials with them. Sometimes it was just\
    \ getting in the weeds with their data infrastructure and saying \u201COkay, maybe\
    \ you might want to change this little X here, because not only will the integration\
    \ with us become easier, but it will also make your life easier down the line.\u201D\
    \ So it was a lot of getting into the weeds with data infrastructure stuff for\
    \ our customers, and then taking the product that we had and saying, \u201CHere's\
    \ how it would help. Here's what it could do for you.\u201D"
  sec: 235
  time: '3:55'
  who: Rishabh
- line: Which I guess also involved doing some proof of concepts?
  sec: 287
  time: '4:47'
  who: Alexey
- line: Absolutely. Yeah.
  sec: 283
  time: '4:43'
  who: Rishabh
- line: Then the customer would evaluate if this POC works for them or not.
  sec: 295
  time: '4:55'
  who: Alexey
- line: Exactly. I was responsible for the trials that we used to do with companies
    and the POCs. Yeah.
  sec: 297
  time: '4:57'
  who: Rishabh
- line: "You mentioned that you did a Master\u2019s at Stanford and that you were\
    \ a TA at Andrew Yang\u2019s course. That's cool. I took that at Coursera. Of\
    \ course, I think it's pretty different from the real one."
  sec: 304
  time: '5:04'
  who: Alexey
- line: "It's funny because I think some of the problem sets and such might be similar,\
    \ or the programming assignments at least, but I haven't seen the exact courses.\
    \ But, I\u2019m sure it's still pretty good."
  sec: 320
  time: '5:20'
  who: Rishabh
- line: "I was also doing my Master\u2019s, though I wasn't really studying computer\
    \ science. I think I ended up getting a Master's in computer science, but the\
    \ main direction there was BI \u2013 business intelligence. I was studying BI\
    \ and we were taking courses like data mining, data warehousing, business intelligence\
    \ \u2013 all these kinds of things. In our courses, we studied two types of analytics."
  sec: 335
  time: '5:35'
  who: Alexey
- line: "One kind of analytics was \u2018prescriptive analytics\u2019 and the other\
    \ kind was \u2018predictive analytics\u2019. Sometimes for predictive analytics,\
    \ we would call it \u2018data mining\u2019. So it's not like you're just digging\
    \ something up in your data but you also do some predictions there. I guess these\
    \ \u2018predictive analytics\u2019 are what today we call \u2018machine learning\u2019\
    \ to some extent \u2013 we analyze some data that we have, and we do analytics\
    \ in order to do predictions. But still, is there a reason why this thing is called\
    \ \u2018predictive analytics\u2019?"
  who: Alexey
- header: Prescriptive vs predictive analytics
- line: "Do you know what the main difference between these two types is \u2013 \u2018\
    prescriptive analytics\u2019 and \u2018predictive analytics\u2019?"
  sec: 406
  time: '6:46'
  who: Alexey
- line: "This is super interesting, because many different fields have been working\
    \ with data in different capacities for decades at this point. Today, we're having\
    \ a conversation about analytics and machine learning and it's very much in the\
    \ modern context \u2013 in \u2018today's\u2019 context. You referenced the word\
    \ \u2018data mining\u2019. \u2018Data mining\u2019 is an old school kind of term,\
    \ but it's really about just extracting patterns from data. You can do some extracting\
    \ patterns by machine learning techniques \u2013 sometimes you can do it by clustering\
    \ and those unsupervised kinds of techniques."
  sec: 413
  time: '6:53'
  who: Rishabh
- line: "But then there's also classic data mining techniques. I'd be curious about\
    \ the predictive versus prescriptive, because predictive definitely sounds, from\
    \ my very minimal understanding, very similar to machine learning work. But prescriptive,\
    \ from what I gather at least, goes above and beyond. It\u2019s also about \u201C\
    How do you explain this decision that was made? What are the implications of a\
    \ particular decision that was made from a prediction?\u201D So it encompasses\
    \ a little bit more than the former. Is that generally how you remember prescriptive\
    \ analytics?"
  who: Rishabh
- line: "Exactly. If I translate what I studied to the work I'm doing now \u2013 to\
    \ the work we're doing at OLX Group \u2013 I would say that \u2018prescriptive\
    \ analytics\u2019 is what data analysts do and \u2018predictive analytics\u2019\
    \ is more what data scientists do, in addition to building services. At university,\
    \ we were focusing more on algorithms, but not on actually putting these things\
    \ in production. From what I remember, this was the main difference. So prescriptive\
    \ is going through the data, understanding what\u2019s there, and then coming\
    \ out with a report. This is what I see my analyst colleagues doing \u2013 coming\
    \ up with reports or dashboards. While predictive analytics is coming up with\
    \ a model and then again, BI. This model would continue doing some predictions\
    \ for time series. Then you would put this on a dashboard."
  sec: 490
  time: '8:10'
  who: Alexey
- line: That makes a lot of sense. It's funny, right? I can totally imagine that five
    years from now, if we have this conversation again, I bet the names would change
    a little bit. And we'd be talking about a slightly different concept, but it feels
    similar to what we've seen before. I think that's just how it goes.
  sec: 555
  time: '9:15'
  who: Rishabh
- header: "The problem with the term \u2018data science\u2019"
- line: "Actually, in the question that I initially put, I wrote \u2018data science\u2019\
    . Then you left a comment saying: \u201CHey, let's not use \u2018science\u2019\
    \ here because it's too ambiguous. It can mean too many things.\u201D"
  sec: 572
  time: '9:32'
  who: Alexey
- line: "It's too overloaded, at least to me. At different companies \u2018data science\u2019\
    \ can end up being just vastly different jobs. If somebody was being interviewed\
    \ for a data science role, I think it's pretty important to just ask the team\
    \ exactly what they mean and exactly the kinds of projects that they can imagine\
    \ that the person will be doing. Because it can mean everything from writing some\
    \ SQL and writing some code, all the way to building machine learning models \u2013\
    \ everything in that space."
  sec: 585
  time: '9:45'
  who: Rishabh
- line: "You mentioned that it's interesting how this would be different in five years.\
    \ It\u2019s curious to me how data science will be different in 5 years."
  sec: 618
  time: '10:18'
  who: Alexey
- line: I mean, we're seeing some of those changes already. I think I saw that you
    interviewed somebody that was in analytics engineering. Is that right? That's
    a very recent thing. It's only maybe gained steam in the last six months to a
    year. So we're already seeing a new thing emerge that is probably here to stay.
  sec: 630
  time: '10:30'
  who: Rishabh
- header: Should machine learning be part of analytics?
- line: "Yeah, definitely. Who knows what will happen with \u2018data scientist\u2019\
    \ in the future? So, we talked about \u2018predictive analytics\u2019 and \u2018\
    prescriptive analytics\u2019 \u2013 can we say that machine learning is actually\
    \ a part of analytics? Or are they two different things?"
  sec: 648
  time: '10:48'
  who: Alexey
- line: "Hmm. Let\u2019s put the \u2018predictive vs prescriptive\u2019 thing aside,\
    \ because there might be some connotations of it being a subset there. To me,\
    \ analytics and machine learning feel distinct. The goals there are slightly different.\
    \ Maybe this is a good time to go into them in a little bit more detail. To me,\
    \ analytics is about looking at data in the past. It's about looking at history\
    \ and trying to understand what happened so that you can answer certain questions.\
    \ The data is there, so there's a true answer that you're looking for, assuming\
    \ that you've collected enough data. It's about \u201CHere\u2019s what happened.\u201D"
  sec: 669
  time: '11:09'
  who: Rishabh
- line: "Whereas machine learning work is often about looking at data in the past,\
    \ but \u201CCan you predict stuff in the future?\u201D It\u2019s always forward-looking.\
    \ It's about making predictions and making forecasts. There are no guarantees\
    \ that you're going to get it right, so it's about coming up with the best guess.\
    \ At least when viewed from that lens, they end up being different things. Although,\
    \ they might have shared data infrastructure or they might have the same people\
    \ working on them. But often the mentality and the outcome of these two end up\
    \ being a little bit different. Coming back to your original question, maybe some\
    \ people would classify machine learning as a part of analytics. And maybe that's\
    \ because often machine learning work begins in classic analyst teams \u2013 where\
    \ they're sort of in a place where they can train a machine learning model. Maybe\
    \ that's how it emerges for a few companies. But to me, they feel very different."
  who: Rishabh
- line: "Yeah, I saw something on this in a couple of talks about data engineering.\
    \ Data engineers, at least in those talks, refer to machine learning things as\
    \ \u2018analytical workloads\u2019. Things like training the model or scoring\
    \ customers \u2013 they would refer to this as \u2018analytical workloads\u2019\
    . I guess from a data engineering point of view, it's kind of similar. You're\
    \ going through the data. You're doing something with the data. Then you\u2019\
    re producing more data. Right? From this point of view, maybe it's not that different."
  sec: 774
  time: '12:54'
  who: Alexey
- line: "Yeah, that's possible. Look, I'll caveat this with \u2013 because I've been\
    \ in the field, maybe similar things feel different to me. Whereas maybe somebody's\
    \ looking at it somewhat from the outside and it may seem like kind of the same\
    \ thing. But yeah, I totally hear that."
  sec: 811
  time: '13:31'
  who: Rishabh
- header: Day-to-day of people that work with ML
- line: "So basically, analytics is looking at the history and then describing what\
    \ happened there. While machine learning is more forward-looking \u2013 describing\
    \ what will happen. Okay. So, for analytics, usually, it's the data analysts that\
    \ are working on this. While for machine learning, we can argue whether it's data\
    \ scientists or somebody else doing it. But let's say that it's data scientists.\
    \ For the people who work with machine learning, what does their day-to-day work\
    \ look like?"
  sec: 828
  time: '13:48'
  who: Alexey
- line: "The starting point for that is \u201CWhat is the outcome? What is the thing\
    \ that the data science/machine learning team is producing?\u201D Typically, it's\
    \ going to be either a live-running system, which basically, you submit questions\
    \ to it and it returns with the prediction \u2013 something that is a machine\
    \ learning model behind an API. That's the live system that they're producing.\
    \ Or they might be producing predictions that are computed on a daily basis and\
    \ then stored in a database so that they can be consumed by the product later\
    \ on. So, if you think about it, it\u2019s a live system that they're producing\
    \ and there are predictions to be made."
  sec: 865
  time: '14:25'
  who: Rishabh
- line: "You can imagine that some of the work that they're doing is figuring out\
    \ \u201CHow do we make the prediction quality better?\u201D That involves a whole\
    \ set of machine learning activities \u2013 gathering data, labeling data, training\
    \ models, hyper-parameter tuning. Then you get into some of the more \u2018system\u2019\
    \ aspects, which is, \u201CHow do you actually deploy it? What are the SLAs that\
    \ the live system needs to produce?\u201D Many companies have fraud teams that\
    \ are trying to detect fraud. So initially, they start out as rules-based activities,\
    \ but eventually, they transition into doing some machine learning."
  who: Rishabh
- line: "With fraud, you have to catch that reasonably early. For example, if you're\
    \ onboarding somebody and you wait a few days \u2013 that might already be too\
    \ late. So they often have to think a lot about these SLAs for the system. So,\
    \ again, coming back to the original question, I think machine learning folks\
    \ \u2013 machine learning engineers, at least \u2013 often spend a bunch of the\
    \ time on \u201CHow do we improve the quality of the predictions when we're training\
    \ the model, but also on an ongoing basis?\u201D And then also \u201CHow do we\
    \ improve the system such that it actually is performant from a software perspective?\u201D\
    \ Has that been your experience, as well?"
  who: Rishabh
- line: "Yeah. It\u2019s interesting that you mentioned that machine learning often\
    \ started in companies in these fraud teams. They first started with rule-based\
    \ systems, and then added machine learning. To my knowledge, this is also what\
    \ happened at OLX group. It was before I joined, but as far as I know, this is\
    \ the first big use case of machine learning at OLX group. This was like five\
    \ years ago, maybe seven years ago \u2013 it was way back before I joined. So\
    \ it\u2019s very interesting that you mentioned it."
  sec: 992
  time: '16:32'
  who: Alexey
- line: "As for the experience, from what I saw, it's very similar that there is this\
    \ system aspect, or maybe I would call it an engineering aspect. It's not enough\
    \ just to create a model \u2013 logistic, regression, SciKit Learn \u2013 you\
    \ also need to take care of other things. Because what data scientists do \u2013\
    \ or you can call them machine learning engineers \u2013 but this is what needs\
    \ to happen to be able to use the model."
  who: Alexey
- header: From rule-based systems to machine learning
- line: "Yeah. I know we're getting a little off-script here. The rules-based system\
    \ in machine learning is always fascinating. I think a lot of sophisticated machine\
    \ learning fraud detection teams also still continue to use a lot of rules. The\
    \ simple reason is \u2013 rules are really fast, right? Somebody can just see\
    \ some data, write a rule, and have that deployed in one hour, compared to training\
    \ a machine learning model with that as a feature or maybe as a separate model,\
    \ which can take an order of weeks. So it's about the speed that you get. I was\
    \ recently talking to a team that does fraud detection. They'll have a team that\
    \ is coming up with these rules and getting them deployed. Then eventually, if\
    \ a rule is important enough, it'll become a feature in a model, or it will even\
    \ become its own model at some point, whereas some rules will die away because\
    \ those patterns don't work anymore. So it's this constant battle that is going\
    \ on."
  sec: 1058
  time: '17:38'
  who: Rishabh
- header: Role of analysts
- line: "Exactly. And these rules \u2013 at least what we have at OLX \u2013 we have\
    \ a UI where fraud specialists just go there, click a button, and then they have\
    \ a rule. Then they can see how effective this rule is. But with machine learning,\
    \ things will take a few more iterations to actually do. Speaking of that \u2013\
    \ we just talked about the rule and then seeing how effective it is. All these\
    \ charts and things. I guess this is something that maybe analysts would do? Doing\
    \ some sort of analytics \u2013 let's say we have a rule and then we go in there\
    \ and try to understand how effective this rule is, like what the false positive\
    \ rate is and things like this. Is this something that analysts would do?"
  sec: 1119
  time: '18:39'
  who: Alexey
- line: "Absolutely. For example, you might have this person \u2013 sometimes it can\
    \ be an analyst, sometimes it might be a fraud specialist, or an operations person\
    \ \u2013 who might define the rule because it was relevant in that given moment.\
    \ But then it might actually be an analytics team or an analyst who actually looks\
    \ at the performance of that rule on an ongoing basis, like \u201CWhich rules\
    \ actually continue to work? Which rules actually flagged important stuff?\u201D\
    \ Then as they gather the \u2018true\u2019 labels, whether a particular transaction\
    \ or particular users were fraudulent or not, then there'll be comparing of this\
    \ and saying, \u201CThese last 20 rules are not working anymore. Maybe we should\
    \ get rid of them.\u201D Once they have that \u2018true\u2019 data \u2013 which\
    \ were fraudulent or not \u2013 they might actually have a good sense of, \u201C\
    Here are the examples of things that were still not caught.\u201D They might be\
    \ providing those recommendations. But yeah, this would absolutely be some of\
    \ the work that an analytics team might do."
  sec: 1171
  time: '19:31'
  who: Rishabh
- line: "This term, \u2018prescriptive analytics\u2019 \u2013 here, an analyst or\
    \ a team of analysts would do the analysis. They would analyze all the rules,\
    \ and then say, \u201COkay, these 20 rules are not working anymore.\u201D Then\
    \ they kind of prescribe this, \u201COkay, throw these rules away. They're useless.\u201D\
    \ So this would be the prescription. They have some sort of report and some sort\
    \ of recommendations on this decision, \u201CWe analyzed the data. This is what\
    \ you should do based on our analysis.\u201D Would you say that this is the main\
    \ outcome of analytical work?"
  sec: 1234
  time: '20:34'
  who: Alexey
- line: "It's definitely one of them. If I were to look at a few different things\
    \ that an analyst would be expected to do \u2013 there are some things, like ad\
    \ hoc queries, that they will be asked to do because their boss or their boss's\
    \ boss will say, \u201CHey, I need the answer to this question. I need this because\
    \ I'm presenting to person X (or team X) and this needs to be in my slides.\u201D\
    \ So the analyst will probably go to their favorite SQL client, write some queries\
    \ and get that answer. Depending on the team, that can often be close to 100%\
    \ of their work. Although it probably shouldn't be 100%. So, that's one aspect\
    \ of their work."
  sec: 1271
  time: '21:11'
  who: Rishabh
- line: "Speaking of the fraud example, this request could be like, \u201CHey, what\
    \ are the success ratios for these rules for the last month? We have a board meeting\
    \ and we want to show how effective our team is. Please prepare this. I need this\
    \ soon.\u201D"
  sec: 1319
  time: '21:59'
  who: Alexey
- line: "Absolutely. They could be answering all sorts of questions like \u201CHow\
    \ many fraudulent cases were found? How many were caught in time? What was the\
    \ overall damage (or whatever the right word is) that was caused by the fraudulent\
    \ activities?\u201D Yeah, there are so many interesting questions there. Part\
    \ of their work is this. Another part, as you referenced, is coming up with these\
    \ reports and recommendations, which is absolutely a super important piece of\
    \ work. For example, if a data science or data analyst person is embedded in a\
    \ product team, often they're working closely with a product manager to say, \u201C\
    If we build this feature, it's probably going to impact this kind of user. This\
    \ is maybe how we can model the improvements (or maybe a particular hit on some\
    \ business metric) if this gets released to 100% of traffic vs if it was only\
    \ released to 2%.\u201D There are all these kinds of questions there that they\
    \ might be helping product teams with."
  sec: 1340
  time: '22:20'
  who: Rishabh
- line: "Then there's a whole set of activities that a data analyst might be doing\
    \ when it comes to integrating different data sets. They might already be working\
    \ with certain data sets in their database, but then, let's say they find an API\
    \ for a completely different new data set, which has some symbol for them. They\
    \ might probably spend some time exploring the data, seeing what that can bring\
    \ when joined with their existing data. So, there's a bunch of activities there\
    \ as well. Of course, one of the maybe \u2018unsaid\u2019 parts of a lot of this\
    \ data work is, often a lot of education needs to go into it. Whether it's data\
    \ analysts, data scientists, or data leaders \u2013 often they spend a lot of\
    \ time telling people, \u201CThis is what you actually can achieve and this is\
    \ what you can\u2019t achieve with the kinds of things that we're doing. Here's\
    \ maybe the question that you should be asking before you make important decisions.\u201D\
    \ There's a lot of important work that goes on there in that sense."
  who: Rishabh
- line: Do data analysts know data better than data scientists?
  who: Rishabh
- line: "In my experience, I often see this \u2013 let's say, there is a new potential\
    \ project where we think that machine learning will help. So analysts will often\
    \ help with understanding the size of the problem. Then we can see \u201CActually,\
    \ just 10 users complained about this. Maybe it's not actually worth solving it.\u201D\
    \ Or like, \u201CLet's give it a lower priority because there\u2019s this thing\
    \ where 10,000 users complained versus this one that seems to have affected fewer\
    \ users.\u201D"
  sec: 1463
  time: '24:23'
  who: Alexey
- line: "The other thing I noticed \u2013 I'm a data scientist myself and I noticed\
    \ that data analysts know data a lot better than me. They know where things are.\
    \ So, if I need to find something, I usually use this hack where I would just\
    \ go to an analyst and say, \u201CHey, I need to find this data. Can you help\
    \ me?\u201D And then they would say, \u201CHere you go. This is the SQL query.\
    \ You can just go with this.\u201D Yeah, it saves a lot of time. So I think data\
    \ analysts know data a lot better \u2013 than me, for sure \u2013 but maybe better\
    \ than the average data scientist as well. I imagine they spend their entire day\
    \ crunching this data, doing all these queries, and then doing reports. Is that\
    \ right?"
  who: Alexey
- line: "Yeah, that's exactly right. That's where they spend the bulk of their time.\
    \ They are the experts, right? I often think a lot of data analytics work is tying\
    \ what data we have to important business metrics. The senior folks who've spent\
    \ a lot of time with the data have a very keen sense of what to look for, and\
    \ figuring things out like, \u201CWhat are the common \u2018gotchas\u2019? What\
    \ are the things that commonly go wrong?\u201D They might be classic things where,\
    \ \u201COh! To make this query work and get you the right data, you have to add\
    \ this \u2018where\u2019 clause. If you don't write this \u2018where\u2019 clause,\
    \ you'll get a bunch of garbage data.\u201D Often, that kind of knowledge is with\
    \ specific people."
  sec: 1551
  time: '25:51'
  who: Rishabh
- line: Like tribal knowledge, right?
  sec: 1591
  time: '26:31'
  who: Alexey
- line: Yeah.
  sec: 1591
  time: '26:31'
  who: Rishabh
- header: Documenting analytics
- line: "Exactly. Even if it's documented \u2013 maybe it's in a wiki somewhere where\
    \ nobody looks at it \u2013 but these people know it and they will just say, \u201C\
    Hey, your query is wrong. Here's the good one.\u201D"
  sec: 1593
  time: '26:33'
  who: Alexey
- line: "There are folks building good tools for documentation, but honestly, I've\
    \ yet to see documentation systems for this that really work. I hope we get there.\
    \ Because, otherwise, it's kind of hard to scale. I had a quick question around\
    \ something you mentioned. You said at OLX, sometimes analysts would help answer\
    \ questions of \u201CIt only affects 10 people.\u201D Do you find that analysts\
    \ are often brought in at the right time to be able to answer those questions?\
    \ How often are their recommendations headed?"
  sec: 1606
  time: '26:46'
  who: Rishabh
- line: "The setup we use is embedding data scientists and data analysts in teams.\
    \ So yes \u2013 usually it happens at the right time. Sometimes it didn't happen,\
    \ and then we ended up spending time on something we shouldn\u2019t have. But\
    \ I guess that happens to everyone, right?"
  sec: 1642
  time: '27:22'
  who: Alexey
- line: "Yeah. That's awesome, honestly. I think there are plenty of stories of product\
    \ managers saying, \u201CHey, this is the coolest feature that needs to be built.\u201D\
    \ Often you can write a simple query to say that, \u201CThis will only affect\
    \ a small number of people. Maybe it\u2019s not worth it.\u201D But this doesn't\
    \ always happen in time. But that's awesome to hear that that happens with you."
  sec: 1665
  time: '27:45'
  who: Rishabh
- line: "Yeah, we actually don\u2019t call our data analysts \u2018data analysts\u2019\
    , but \u2018product analysts\u2019. They work very closely with product managers.\
    \ They're quite deep in the product work, so they are very product-oriented, I\
    \ would say. It definitely helps that they are close to the product and they know\
    \ what is important for users and what is not important for users. They know it\
    \ a lot better than data scientists, I think. I think data scientists need to\
    \ learn a lot from product analytics in order to understand what is important\
    \ for the product."
  sec: 1683
  time: '28:03'
  who: Alexey
- header: Is ML more experimental than analytics?
- line: "But it's good that we work together so we can always learn from each other.\
    \ When I think about this, I think that data science work, or machine learning\
    \ work, is more experimental than analytics. In data science, you have a hypothesis\
    \ that you want to test. So you build some model or something simple and then\
    \ you test this hypothesis. While in analytics \u2013 I might be wrong, because\
    \ I never worked as an analyst myself \u2013 but I think it's less experimental.\
    \ It\u2019s clearer what they need to do. There is some specific ad hoc query\
    \ or some report they need to do. Do you think this is a correct observation?"
  sec: 1722
  time: '28:42'
  who: Alexey
- line: "Yeah, I think that's definitely fair. One of the things is \u2013 both types\
    \ of work are fairly iterative. You have to try something, see if it works \u2013\
    \ try something slightly different, see if it works. So in the world of analysts,\
    \ they're often iterating on different versions of SQL. I know analysts who have\
    \ thousands of lines-long SQL queries and they're making small changes as they\
    \ understand something new about the business. They want to add something slightly\
    \ different to the queries. So there\u2019s often this iterative work, but it's\
    \ still in the service of finding something that is kind of true \u2013 an answer\
    \ that is true based on the history of the business and the data that's been collected."
  sec: 1770
  time: '29:30'
  who: Rishabh
- line: "Whereas with machine learning work, you're right \u2013 it is fairly experimental\
    \ and the iterations themselves are the experiments. You might have experiments\
    \ that are running pre-deployment, where you're just testing out a bunch of different\
    \ models, different features, different hyperparameters, so there are a bunch\
    \ of experiments going on there. Then, depending on the scale of the company and\
    \ their infrastructure setup, you might be doing experiments on live traffic.\
    \ Before releasing the full model to production, you might be running them in\
    \ shadow mode, or you might be doing A/B tests with the model. So it definitely\
    \ feels very experimental. A lot of machine learning is just empirical results\
    \ on the data that you're seeing and observing. Who knows what the right, perfect\
    \ model is? It\u2019s just one that works \u2018best\u2019 \u2013 that's the guiding\
    \ principle. Yeah, I think that the data science/machine learning world and being\
    \ experimental makes sense."
  who: Rishabh
- header: Analyzing results of experiments
- line: "From what I see \u2013 again, not only at OLX but also at other companies\
    \ \u2013 we talked about experiments on live traffic, usually, it\u2019s A/B tests\
    \ or shadow testing. This analysis of A/B tests or live experiments is also often\
    \ done by analysts, or by analysts working together with data scientists. Let\u2019\
    s say the data scientists and/or machine learning engineers work together on setting\
    \ up experiments. They have two versions of the model \u2013 the baseline model\
    \ and the new model that they improved. Then, together with analysts, they analyze\
    \ the results and see, \u201COkay, we have an uplift here. Why did this uplift\
    \ happen? Is there any specific segment of users where this uplift happened? Or\
    \ is it an uplift across all their cohorts?\u201D"
  sec: 1879
  time: '31:19'
  who: Alexey
- line: "So this is something that analysts would do. They would dig into it. Especially\
    \ when experiments go wrong, like \u201CWhy did the new model, which was perfect\
    \ in offline experiments, did not result in uplift? Instead, the performance was\
    \ even worse than the baseline. Why did this happen?\u201D And then maybe there\
    \ is one specific category where it was bad, and in other categories it was good.\
    \ This is something that the analysts often do, or help a lot with doing this\
    \ kind of work."
  who: Alexey
- line: "Yeah, I can totally see that. We were talking about this earlier as well.\
    \ Often, you'll have analysts who are much closer to the business metrics and\
    \ have an understanding of what is actually improving the top line or improving\
    \ the bottom line in whatever respect. Having somebody who is helping the machine\
    \ learning team keep very close tabs on whether it\u2019s actually moving the\
    \ needle or not \u2013 that is pretty important. I think there are some machine\
    \ learning teams that have that mentality and expertise built-in. But if not,\
    \ the model that you're talking about is perfect. That's exactly it."
  sec: 1967
  time: '32:47'
  who: Rishabh
- header: Overlaps between machine learning and analytics
- line: Yes, maybe we can summarize a bit. In your opinion, what are the overlaps?
    What are the similarities between machine learning and analytics?
  sec: 2010
  time: '33:30'
  who: Alexey
- line: "=One of the other things is \u2013 often it feels like the same people are\
    \ working on both analytic stuff and machine learning stuff. I think that there\
    \ are teams \u2013 or at least within teams \u2013 where you'll have specialization.\
    \ Where the bulk of what somebody does is just working with SQL, while somebody\
    \ else does more of the machine learning and modeling stuff. But it still feels\
    \ that there can be a lot of interchange there. Of course, when compared to software,\
    \ they're both fairly less mature \u2013 as ecosystems and processes and how to\
    \ actually do stuff. There's a lot that will change. There's a lot of change that\
    \ is going on already, but there's a lot that will change about how this work\
    \ gets done. In my head, those are roughly the similarities."
  sec: 2021
  time: '33:41'
  who: "In terms of similarities, it's the data. That\u2019s the biggest one. These\
    \ are both professions that heavily rely on it. Without data, nothing works. And\
    \ without good data quality, nothing works. Whenever it comes to data, you're\
    \ dealing with problems of, \u201CHow do you store it efficiently? How do you\
    \ process it efficiently? How do you know where the status is coming from? How\
    \ do you make sure that the data quality errors are caught as early as possible?\u201D\
    \ You have all of these data similarities. I think we talked about them being\
    \ both iterative. Nothing is ever quite \u2018done\u2019, right? Not even a SQL\
    \ is ever quite perfect because there's probably something that is missing. Models\
    \ surely break all the time and you need to keep updating them."
- line: "To me, some of the differences come from, \u201CWhat are the use cases that\
    \ they address?\u201D Analytics is typically helping the business understand \u201C\
    What actually happened? What worked? What didn't work?\u201D The use cases are\
    \ often very internally facing \u2013 it's for the organization themselves. Whereas\
    \ for machine learning, there can be internal-facing stuff like \u201CWhat revenues\
    \ do we forecast?\u201D But a lot of it is actually making predictions for users\
    \ \u2013 things that will actually directly impact users. We were talking about\
    \ fraud, so in this case, it would be something like \u201CWhose transactions\
    \ to block? What users to stop (in some capacity)?\u201D There'll be a lot of\
    \ externally facing stuff there as well. We talked about the differences around\
    \ \u201CWhat are the outputs of these two data streams?\u201D With analytics,\
    \ you have things like dashboards and reports, whereas with machine learning stuff,\
    \ you have systems that are the output. It's a live system that you have to keep\
    \ running."
  who: "In terms of similarities, it's the data. That\u2019s the biggest one. These\
    \ are both professions that heavily rely on it. Without data, nothing works. And\
    \ without good data quality, nothing works. Whenever it comes to data, you're\
    \ dealing with problems of, \u201CHow do you store it efficiently? How do you\
    \ process it efficiently? How do you know where the status is coming from? How\
    \ do you make sure that the data quality errors are caught as early as possible?\u201D\
    \ You have all of these data similarities. I think we talked about them being\
    \ both iterative. Nothing is ever quite \u2018done\u2019, right? Not even a SQL\
    \ is ever quite perfect because there's probably something that is missing. Models\
    \ surely break all the time and you need to keep updating them."
- line: "With systems, you often see that they can be fairly real-time. You're talking\
    \ about SLAs \u2013 a return of prediction in 200 milliseconds. But if you think\
    \ about analytics stuff \u2013 their people are comparing week-on-week on how\
    \ the business metrics are changing, which is a completely different timescale\
    \ to be thinking about problems on. Of course, there are different technologies,\
    \ different tools, and in the ecosystems, there are slight differences. Anyway,\
    \ I can probably go on for longer, but those are some of the key similarities\
    \ and differences from my point of view."
  who: "In terms of similarities, it's the data. That\u2019s the biggest one. These\
    \ are both professions that heavily rely on it. Without data, nothing works. And\
    \ without good data quality, nothing works. Whenever it comes to data, you're\
    \ dealing with problems of, \u201CHow do you store it efficiently? How do you\
    \ process it efficiently? How do you know where the status is coming from? How\
    \ do you make sure that the data quality errors are caught as early as possible?\u201D\
    \ You have all of these data similarities. I think we talked about them being\
    \ both iterative. Nothing is ever quite \u2018done\u2019, right? Not even a SQL\
    \ is ever quite perfect because there's probably something that is missing. Models\
    \ surely break all the time and you need to keep updating them."
- line: "Yeah, I'm looking at my notes and I don't think you missed anything. Apart\
    \ from maybe the point, that data analysts know data a bit more, or a bit better,\
    \ than data scientists. They tend to spend a lot more time with that. You said\
    \ it\u2019s because, in the case of analysts, the output is dashboards and reports,\
    \ which involves a lot of SQL and data understanding, while data scientists spend\
    \ more time on systems rather than on analyzing data."
  sec: 2221
  time: '37:01'
  who: Alexey
- line: "Maybe to even contradict myself a little bit on this \u2013 I do think that\
    \ some of the best scientists have a very keen understanding of the business.\
    \ Because without that, sometimes you'll just make bad decisions about what to\
    \ prioritize and what not to prioritize. The best data scientists, in my opinion,\
    \ very closely understand why they're working on something and how that will impact\
    \ the key metrics for the team and the company. But as a rough guiding stick,\
    \ I think you're right. I think analysts will spend a lot of time in SQL working\
    \ with business metrics directly, so they often have a much closer sense of it."
  sec: 2254
  time: '37:34'
  who: Rishabh
- line: "Maybe the same is true for analysts? Analysts who don\u2019t just spend time\
    \ in SQL, but also spend some time programming and doing a bit of the system aspects\
    \ \u2013 I don't know if analysts actually do this. But definitely doing a bit\
    \ of programming, like some Python and things like that. I think these can probably\
    \ be considered \u2018great analysts\u2019. Right? Similar to data scientists\
    \ and machine engineers who go outside of their typical day-to-day work and do\
    \ some business analytics. That is all good for business, such as maybe data analysts\
    \ who go and check out data science and how to do this whole machine learning\
    \ stuff? They're also very beneficial for the business."
  sec: 2295
  time: '38:15'
  who: Alexey
- header: Bridging the gap between ML and analytics
- line: "Absolutely. I think it comes down to using the right tool. So if the existing\
    \ tool \u2013 let\u2019s say SQL \u2013 doesn't get you the answers you need,\
    \ maybe you just need to run some analysis with Pandas or in a Jupyter Notebook\
    \ or something. It would be amazing if the analysts can just spin that up themselves\
    \ and write whatever code they need to. I do believe that until recently, it probably\
    \ wasn't the easiest to set up virtual environments and Jupyter Notebooks for\
    \ people who are less familiar with them. We're seeing a move into notebooks that\
    \ are much more inclusive \u2013 which allow you to write SQL and Python in sort\
    \ of the same environment and a lot of things are taken care of for you. I think\
    \ as more and more of that happens, it will become easier and easier for cases\
    \ like the one you mentioned about a data analyst who does mostly SQL and a little\
    \ bit of code."
  sec: 2344
  time: '39:04'
  who: Rishabh
- line: Now you're talking about something else a bit. Remember when this thing came
    out? Not Jupyter Notebooks, but the other sorts of notebooks? I think they were
    called Zeppelin Notebooks. I don't think it got much traction, but the idea there
    was that you could write a SQL query in one cell, and then you can write some
    Spark code in the second cell. Then you could also write some Pandas code and
    create these nice reports immediately in your dashboard. That was actually pretty
    nice.
  sec: 2401
  time: '40:01'
  who: Alexey
- line: "I personally never used Zeppelin. If you're working with the Hadoop ecosystem,\
    \ it's probably a better thing to use. I guess I know a few people who use it\
    \ \u2013 I probably won't name names. But, for example, there are a couple of\
    \ BI tools today that, in the same interface, will allow you to switch between\
    \ a notebook experience and a SQL client. There are a couple of smaller companies\
    \ that make running SQL and Python in similar cells possible. They're seeing some\
    \ amount of traction. Maybe the time wasn't quite right when Zeppelin came out\
    \ five-six years ago. Maybe the time is right now. But \u2013 who knows?"
  sec: 2432
  time: '40:32'
  who: Rishabh
- header: Overinvesting in ML and underinvesting in analytics
- line: "We already have some questions. The question is, \u201CDo you see that organizations\
    \ tend to overinvest in machine learning and underinvest in analytics?"
  sec: 2473
  time: '41:13'
  who: Alexey
- line: "Yeah, that's interesting. I don't know if I have a clear answer to that.\
    \ At the highest level, I would imagine that there is generally underinvestment\
    \ in data teams overall. The value that a couple of good data people, who have\
    \ the right infrastructure and set up, can bring is often very outsized, compared\
    \ to the resources that are spent on them. But between machine learning and data\
    \ analytics? It's possible. Sometimes, folks who are in executive positions \u2013\
    \ who are making these decisions \u2013 often rely on external factors. They might\
    \ read some piece from McKinsey or whatever, without going into details there,\
    \ and say \u201CLook, machine learning is the hot thing right now. We should have\
    \ a team. We should be doing this.\u201D I could totally see that happening. But\
    \ it's hard for me to say that without numbers. But generally, I think more investment\
    \ in this stuff is probably better, as long as we start from investing in both\
    \ analytics and machine learning. There's often a core investment in data infrastructure\
    \ that often also needs to be made along the side. I think that's often the most\
    \ underappreciated and underserved part of it."
  sec: 2491
  time: '41:31'
  who: Rishabh
- header: Forgetting to hire data analysts
- line: "The question continues. It's actually more like a comment that I see a lot.\
    \ \u201CAre organizations often hiring lots of data scientists, while forgetting\
    \ about data analysts?\u201D And \u201CDo they often forget to upskill others?\u201D\
    \ So perhaps, data science can appear sexier? We can talk about machine learning\
    \ robots and dashboards and stuff. It\u2019s cooler, right? \u201COkay, let's\
    \ add a bunch of data scientists. Put them in the room and let them do some magic.\u201D"
  sec: 2582
  time: '43:02'
  who: Alexey
- line: "Unfortunately, that sounds very true. That's why I typically want to stay\
    \ away from the term \u2018data science\u2019 as much as possible, just because\
    \ it becomes so broad. To a point whereby using that phrase, you can convince\
    \ someone how sexy a particular job can be. But maybe the person actually gets\
    \ into an organization and they realize that there is no amazing machine learning\
    \ model that they get to train. There's just these more important, pressing business\
    \ problems that can be answered with SQL and just getting your data into a better\
    \ shape. That's just what the business needs at that moment."
  sec: 2620
  time: '43:40'
  who: Rishabh
- line: "You may often have some amount of dissatisfaction for people that are hired\
    \ in. But yeah, it's kind of an unfortunate transitionary period in our lives.\
    \ Maybe five, seven years from now, things will be a little bit better defined\
    \ and these roles will be a little bit clearer. Hopefully, the importance and\
    \ the value that data analysts can bring to the table will become reasonably clear.\
    \ So it's not the mindset that data scientists are here and data analysts are\
    \ here \u2013 because that's just not true."
  who: Rishabh
- header: Finding senior data analysts
- line: Yeah, that's definitely not true. I talked to some people who are hiring both
    data scientists and data analysts. There was one comment that was a bit surprising
    for me, but then in retrospect, I thought it probably makes sense. They told me
    that it's a lot more difficult to find a senior analyst than a senior data scientist.
    Have you seen this? Do you have any ideas why this might be the case?
  sec: 2695
  time: '44:55'
  who: Alexey
- line: "Yeah, I\u2019m not 100% sure. If I had to make a guess for why that could\
    \ happen, it's likely because senior data analyst \u2013 people who spend a lot\
    \ of time doing that \u2013 if they find a differential in the amount of money\
    \ that they can make by just moving to a data science role, that seems like a\
    \ no-brainer, right? They should be doing that. It's also possible that some data\
    \ analysts actually make the transition from just writing SQL and understanding\
    \ the company's data, to becoming much more, almost infrastructure people. Because\
    \ they understand what it takes to have successful and high-performing analyst\
    \ teams."
  sec: 2730
  time: '45:30'
  who: Rishabh
- line: "Maybe this \u2018analytics engineer\u2019 role is a trend in that direction.\
    \ One where they're less about writing SQL queries and answering direct questions\
    \ from the business, but more about structuring and setting up the datasets in\
    \ a way where it makes it easier downstream. There are probably moves that analysts\
    \ would make, either in the direction of data science or a little bit more upstream\
    \ when it comes to infrastructure. But I think hiring is generally pretty hard\
    \ right now for a lot of folks. But I can imagine that analysts might be a little\
    \ bit harder than normal."
  who: Rishabh
- line: "I also noticed that some analysts mainly go to the data science path \u2013\
    \ many switch careers from data analytics to data science, but also many go to\
    \ the product aspect. They become product managers. Not many, necessarily, but\
    \ I saw multiple cases. Because data scientists get quite close to the product,\
    \ they realize that they like this product management work and they become product\
    \ managers."
  sec: 2817
  time: '46:57'
  who: Alexey
- line: That's super interesting. Yeah.
  sec: 2842
  time: '47:22'
  who: Rishabh
- line: So maybe by the time they're senior analysts and they see this data science
    or product management work, and then they just switch over. Not so many people
    get to the senior position, unfortunately.
  sec: 2845
  time: '47:25'
  who: Alexey
- line: I hope that changes. If that's true, I hope that it changes.
  sec: 2864
  time: '47:44'
  who: Rishabh
- header: Is data science sexier than data analytics?
- line: "As you said, maybe in industry, data science does look sexier. Right? There's\
    \ certainly more hype around this than analytics. Analytics has been around for\
    \ three, four decades, right? Whereas data science is something more fresh. At\
    \ least in the contemporary sense \u2013 we had this \u2018data mining\u2019 thing,\
    \ which is pretty old."
  sec: 2867
  time: '47:47'
  who: Alexey
- line: "It's kind of funny, I think. I don't remember where I was reading this, but\
    \ even the terms like \u2018data mining\u2019, were not very popular when they\
    \ started. There was something that made people feel a bit achy about the fact\
    \ of having to rely on empirical data to come up with the right decisions. At\
    \ the same time, you don't fully understand the problem deeply \u2013 like, from\
    \ your heart. The practice of digging into actual data to figure out what is correct\
    \ and what is right was kind of frowned upon when it began. But it's kind of funny\
    \ that today, everything seems to run on data and everybody's \u201Call about\
    \ data\u201D."
  sec: 2900
  time: '48:20'
  who: Rishabh
- header: Collaboration between ML and analytics teams
- line: "Thanks. We have another question. \u201CShould our team work independently\
    \ or together?\u201D Let's assume we have a machine learning team and analytics\
    \ team in our company. So should we put them in one room? Or should we put them\
    \ in separate rooms?"
  sec: 2941
  time: '49:01'
  who: Alexey
- line: "=In terms of the first direction, generally, it seems that data people like\
    \ to be managed by other data people, or at least people who understand what data\
    \ can and can't do, and some of the challenges that come with data. If you ask\
    \ somebody who's a business leader or maybe even someone like an engineering leader\
    \ \u2013 someone who doesn't really work with data \u2013 to manage people. That\
    \ can often be a little tricky. Because there are challenges there that are unique."
  sec: 2955
  time: '49:15'
  who: "That's a really interesting question. Maybe I'll caveat this with the fact\
    \ that my experience with this is limited. I rely on a lot of other smart people\
    \ who've written stuff about this. But there are two aspects to where they should\
    \ sit. One is from the perspective of, \u201CWhat is the management and reporting\
    \ structure? Who do they report into? How is their career and growth evaluated?\u201D\
    \ That's one direction. And the other direction is, \u201CWhat are the kinds of\
    \ projects that they do? How fast are they able to work on them and deliver business\
    \ value? That's the second direction."
- line: "But when it comes to the actual projects that they do, it can be super valuable\
    \ to have the data person embedded. I think, Alexey, you mentioned this for OLX.\
    \ Because then they have very close access to what the team needs \u2013 what\
    \ business metrics the team is tracking, what actually works, what doesn't work.\
    \ Their cycles are much faster, and they're able to make progress much faster.\
    \ Some of the challenges that they run into then is \u2013 if you're too independent,\
    \ then there are learnings across different data people percolating to everybody\
    \ else. That can often take a bit of a hit. But then again, if there is a common\
    \ reporting structure, like a manager who is directly managing these five or six\
    \ data analysts or data scientists, they should be able to take the common learnings\
    \ and help the broader team."
  who: "That's a really interesting question. Maybe I'll caveat this with the fact\
    \ that my experience with this is limited. I rely on a lot of other smart people\
    \ who've written stuff about this. But there are two aspects to where they should\
    \ sit. One is from the perspective of, \u201CWhat is the management and reporting\
    \ structure? Who do they report into? How is their career and growth evaluated?\u201D\
    \ That's one direction. And the other direction is, \u201CWhat are the kinds of\
    \ projects that they do? How fast are they able to work on them and deliver business\
    \ value? That's the second direction."
- line: But yeah, I would say it's reasonably team-dependent. But as long as there
    are ways for common learnings to be shared and adopted by the rest of the team
    and they can be embedded where they're learning from the business domain very
    fast, that's probably the best outcome. This probably stops being true once the
    team reaches a very large scale, because then there are probably too many data
    scientists to have centralized reporting. But at least until the organization
    reaches around 1000 or so people, they should work.
  who: "That's a really interesting question. Maybe I'll caveat this with the fact\
    \ that my experience with this is limited. I rely on a lot of other smart people\
    \ who've written stuff about this. But there are two aspects to where they should\
    \ sit. One is from the perspective of, \u201CWhat is the management and reporting\
    \ structure? Who do they report into? How is their career and growth evaluated?\u201D\
    \ That's one direction. And the other direction is, \u201CWhat are the kinds of\
    \ projects that they do? How fast are they able to work on them and deliver business\
    \ value? That's the second direction."
- line: "It's interesting that you mentioned that data people like to report to data\
    \ people. Because what I saw when data science just appeared, it wasn't clear\
    \ what part of the hierarchy, or what part of the structure, the data team belongs\
    \ to. Should they report to the product director? Or the VP of product? Should\
    \ they report to an engineering director? Should they be reporting to the engineering\
    \ part of the organization? And it's still not clear. Data science, for example,\
    \ maybe is closer to engineering. But then analytics is closer to the product.\
    \ Like, it's not clear where to put them. Right now at OLX, for example, we have\
    \ this chief data officer and the entire pillar \u2013 I don't know if that\u2019\
    s the right way to say that \u2013 basically, the entire hierarchy comes from\
    \ the chief data officer down to the data analysts and data scientists. I see\
    \ more and more companies are doing that and realizing that this is an important\
    \ thing to do."
  sec: 3113
  time: '51:53'
  who: Alexey
- line: "Then coming to this question of \u201CShould they sit independently or together?\u201D\
    \ I also noticed that sometimes, a bit of both works. Because analysts can constantly\
    \ get distracted by ad hoc queries. Which often happens in companies, right? Let's\
    \ say, they're sitting on the team and they're working on some product things\
    \ like understanding the impact of something. Then somebody comes and says, \u201C\
    Hey, I need this report for a board meeting tomorrow.\u201D So \u201CWhat do I\
    \ do here?\u201D So what I see sometimes is that there is a team that takes care\
    \ of these ad hoc requests. Perhaps large organizations can afford an independent\
    \ team for these kinds of things. At OLX, we had actually a BI department that\
    \ was taking care of these ad hoc requests, and also building some sort of infrastructure\
    \ to enable self-service for this."
  who: Alexey
- line: "Yeah, that sounds reasonable as well \u2013 if there is common infrastructure\
    \ work that is being done by a separate team. I'm guessing the analyst must be\
    \ happy that some of the ad hoc requests can be sent over to somebody else."
  sec: 3242
  time: '54:02'
  who: Rishabh
- line: Only some, unfortunately. Not all. But also, the embedded mode, I think works
    really well, because analysts sometimes get too many ad hoc requests.
  sec: 3257
  time: '54:17'
  who: Alexey
- line: "When I say \u2018data people\u2019, data shouldn\u2019t have to do with the\
    \ title. It's about, \u201CDoes the person understand some of the natural challenges\
    \ with data?\u201D I'll give you a fictional example. Sometimes, data has all\
    \ sorts of weird problems, right? A good analyst or scientist would basically\
    \ look at that and say, \u201CThere's something really fishy here. I better investigate\
    \ it.\u201D The ideal thing to happen would be \u2013 if they're being very paranoid\
    \ and diligent about the quality of data, which they should be. They should be\
    \ able to spend hours, or maybe a few days, just investigating \u201CWhere is\
    \ this record coming from?\u201D And now if you go to somebody who hasn't faced\
    \ these things before, they'll be like, \u201CWell just ignore it. It doesn't\
    \ matter.\u201D But that can have all sorts of negative consequences down the\
    \ line. It\u2019s almost like what you need is some kind of support, right? It's\
    \ like, \u201CYeah. This is probably important.\u201D Then the data person can\
    \ go into detail and explain, \u201COkay, here are all of the problems that can\
    \ happen downstream.\u201D That's not ideal. So at least that's my thought process\
    \ on reporting."
  sec: 3266
  time: '54:26'
  who: Rishabh
- header: Building data teams
- line: "Last week, we had a guest, and we were talking about building data teams.\
    \ Tammy Liang was here talking about her experience. She suggested that if she\
    \ could start building a data team again, she would start with hiring a data engineer,\
    \ and hiring a business analyst and data analyst \u2013 preferably a senior data\
    \ analyst \u2013 and only then hire data scientists after these two-three people.\
    \ Would you say that you would do it the same way? Would you hire an engineer\
    \ and then analyst and then a data scientist? Or would you change something in\
    \ this approach?"
  sec: 3341
  time: '55:41'
  who: Alexey
- line: "That seems pretty reasonable. I'm sure Tammy has a lot of good experience\
    \ to back it up. I think data engineers, or somebody who can just get stuff into\
    \ a good place \u2013 that is pretty critical. Not much work can happen without\
    \ that. I think for most companies, this strategy seems reasonable. There are\
    \ probably some companies that are very machine learning focused \u2013 their\
    \ entire product might just be a machine learning thing. This could be everything\
    \ from self-driving, in the very extreme case, to even smaller models that are\
    \ in FinTech or Healthcare. So when the core business is machine learning, then\
    \ the team structure ends up developing very differently. It might be a set of\
    \ PhD students \u2013 or maybe not students, but folks with PhDs who are getting\
    \ started \u2013 and then you add engineers once you have to make prototypes and\
    \ productionize them. But for most teams, I think that that advice from Tammy\
    \ seems pretty reasonable."
  sec: 3381
  time: '56:21'
  who: Rishabh
- line: "We talked about the idea that companies tend to overinvest into data science\
    \ and data analytics, but maybe when they hire a person who knows in which order\
    \ people should be hired, maybe they don't need to change things. If we still\
    \ see this overinvestment in data science, maybe we can say that these organizations\
    \ are not mature yet. Maybe they need to hire somebody like a chief data officer\
    \ or a data person who would structure the hiring \u2013 someone who can say \u201C\
    This is the order in which we should hire people. First we need to have data engineers,\
    \ who have infrastructure. Then data analysts, to make use of the data, and only\
    \ then the data scientists.\u201D Right?"
  sec: 3443
  time: '57:23'
  who: Alexey
- line: That sounds pretty nice. Hopefully more and more organizations will move in
    that direction.
  sec: 3494
  time: '58:14'
  who: Rishabh
- header: "Rishabh\u2019s newsletter \u2013 MLOpsRoundup"
- line: Before we finish, I wanted to ask you about your newsletter. Maybe you can
    tell us a few words about this? So, what are you writing about?
  sec: 3499
  time: '58:19'
  who: Alexey
- line: "Absolutely \u2013 yeah. So, a friend of mine and I, for maybe years, have\
    \ been trading notes and information about things that we're seeing in the world\
    \ of machine learning. Not so much research, but more, \u201CHow do you take machine\
    \ learning and make it work in production?\u201D Then sometime last year, we just\
    \ decided that maybe we should just take some of the stuff that we're discussing,\
    \ put it into a newsletter, and at least share it with some of our friends. So\
    \ that's kind of how we got started. Even today, we just think about \u201CWhat\
    \ are the common challenges that teams are facing in production with machine learning?\u201D\
    \ All sorts of stuff around \u2013 some system stuff, some machine learning stuff,\
    \ and \u201CHow do you make these systems work?\u201D So, that's something that\
    \ we've been focused on \u2013 the overall ecosystem. Many folks call it ML Ops,\
    \ so our newsletter is called the ML Ops Roundup. It's on Substack. Please check\
    \ it out and let us know if you have any thoughts or feedback."
  sec: 3508
  time: '58:28'
  who: Rishabh
- line: "Yeah, I just realized that I mispronounced it at the beginning. I kept reading\
    \ it as \u2018ML Ops Rounds\u2019 and you didn't correct me. [laughs]"
  sec: 3575
  time: '59:35'
  who: Alexey
- line: It's all good. I think I didn't write out the name explicitly. I should have.
  sec: 3582
  time: '59:42'
  who: Rishabh
- line: Yeah, but the link is correct, because I copy/pasted it. So the link is fine.
    I'll put the link in the description, of course. Thanks. How can people find you?
  sec: 3588
  time: '59:48'
  who: Alexey
- header: Finding Rishabh online
- line: "You can find me on Twitter. My Twitter handle is @rish_bhargave. I\u2019\
    m also in the DataTalks.Club Slack channel, so feel free to find me and send me\
    \ a message. I\u2019m always happy to chat."
  sec: 3599
  time: '59:59'
  who: Rishabh
- line: Okay. Thanks a lot. Thanks for this fruitful discussion. It was a pleasure
    to talk to you. Thanks everyone for joining us today and for asking questions.
  sec: 3620
  time: '1:00:20'
  who: Alexey

---

Links:

- [MLOpsRoundup newsletter](https://mlopsroundup.substack.com/){:target="_blank"}
- [Rishabh's Twitter](https://twitter.com/rish_bhargava){:target="_blank"}
