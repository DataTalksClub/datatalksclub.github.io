---
title: "Build Your Own Data Pipeline"
short: "Build Your Own Data Pipeline"
guests: [andreaskretz]

image: images/podcast/s04e02-build-your-own-data-pipeline.jpg

season: 4
episode: 2

ids:
  youtube: IrZPAG6OBqo
  anchor: Build-Your-Own-Data-Pipeline---Andreas-Kretz-e139se1

links:
  youtube: https://www.youtube.com/watch?v=IrZPAG6OBqo
  anchor: https://anchor.fm/datatalksclub/episodes/Build-Your-Own-Data-Pipeline---Andreas-Kretz-e139se1
  spotify: https://open.spotify.com/episode/0fFRCAYFCReMxEiq2RDVak
  apple: https://podcasts.apple.com/us/podcast/build-your-own-data-pipeline-andreas-kretz/id1541710331?i=1000527643914

transcript:
- line: "Today we'll talk about learning how to build data pipelines for data scientists.\
    \ One of the most frequent questions I get is, \u201CI'm a data scientist and\
    \ I want to build data pipelines. How do I do this?\u201D Finally, today, I'll\
    \ know how to answer this question. The guests we have today, Andreas, knows this\
    \ better than anyone. Andreas is data engineer and calls himself \u201Cthe plumber\
    \ of data science\u201D. He writes and talks about platform architecture, as well\
    \ as the tools and techniques that are used to build modern data science platforms.\
    \ Welcome, Andreas."
  sec: 116
  time: '1:56'
  who: Alexey
- line: Thanks for having me.
  sec: 153
  time: '2:33'
  who: Andreas
- line: "So why \u201Cthe plumber of data science\u201D? Do you have a story behind\
    \ this?"
  sec: 157
  time: '2:37'
  who: Alexey
- line: "Well, I call data engineering \u201Cthe plumbing of data science\u201D because\
    \ when you look at data science, you usually see what the data scientists do,\
    \ like the algorithms and so on, but in the background there is a platform that\
    \ you have to run on \u2013 pipelines that you have to build. Basically an infrastructure\
    \ that needs to support what the data scientists do. Usually it's invisible, but\
    \ it's a huge mess when done wrong, a bit like plumbing. Also this analogy fits\
    \ very well with \u201Cpipelines\u201D."
  sec: 162
  time: '2:42'
  who: Andreas
- header: "Andreas\u2019s background"
- line: Indeed. Before we go into our main topic of plumbing and building pipelines,
    let's start with your background. Can you tell us about your career journey so
    far?
  sec: 199
  time: '3:19'
  who: Alexey
- line: "Sure. My name is Andreas Kretz. I come from Germany and I've been involved\
    \ with computer science my entire life. I\u2019ve always loved computers. I started,\
    \ like many people, by playing computer games. Then I got into actual computer\
    \ science and studied it. After that, I made a quick detour towards SAP consulting,\
    \ but that wasn't my thing. I came back into the computer science realm where\
    \ I started as a software engineer in an industrial IoT project. We were working\
    \ on getting and analyzing machine data, and that's where I got into the topic\
    \ of big data."
  sec: 209
  time: '3:29'
  who: Andreas
- line: "Big data was a popular thing back then \u2013 everybody was talking about\
    \ it and we were doing it. But I actually had the problem with so much data coming\
    \ in, because the standard tools didn't work anymore. I needed to find different\
    \ solutions to actually work this out. Back then I started with Hadoop. Hadoop\
    \ was really a big thing back then as well, so that turned out really good. That's\
    \ how I got into the field \u2013 through big data."
  who: Andreas
- line: "Now I\u2019m in data engineering and data science. I switched to a data engineer\
    \ role \u2013 specifically, I became a team lead for data engineering. This year\
    \ I started leading a data lab. But since this month, I went full time with teaching\
    \ data engineering with my Academy at LearnDataEngineering.com."
  who: Andreas
- header: Why data engineering is becoming more popular
- line: "We will talk a bit about your course as well. It seems like there is a lot\
    \ of interest in data engineering these days. Since you said that you worked with\
    \ Hadoop, I think you\u2019ve been in this area for quite a while. I think nowadays,\
    \ there is a lot more interest in data engineering then even a couple of years\
    \ ago. Now, I talk to some data scientists and they say that they want to get\
    \ into data engineering and start building data pipelines. Not just learn to build\
    \ the pipelines, but switch to data engineering entirely. Do you have an idea\
    \ of while this is happening?"
  sec: 343
  time: '5:43'
  who: Alexey
- line: "When you look back a few years, the thing that generally happened was \u2013\
    \ and I've saw this everywhere \u2013 people were starting with data science and\
    \ hired data scientists. They had some data lying around and the data scientists\
    \ analyzed this data. They had a few business ideas, \u201CWe could do this. We\
    \ could do that.\u201D And then they get to the data science track and they solved\
    \ these problems. But at some point, one that we\u2019re rapidly approaching these\
    \ days, the people realized, \u201COkay, I have these analytics methods. I solved\
    \ the problem. But now I need to automate it. Now I need to build something around\
    \ it. How do I actually bring this into production?\u201D That's why we see a\
    \ lot more engineering today. People leave the stage of \u2018proof of concept\u2019\
    \ and they get more into the stage of \u201COkay, now we need to build something.\
    \ We want to make money. We want to build a platform.\u201D That's what I currently\
    \ see."
  sec: 387
  time: '6:27'
  who: Andreas
- line: "So data science becomes more mature and companies realize \u201COkay. This\
    \ is not just a one-time thing, where we do something in Jupyter Notebook and\
    \ throw it away. We need to automate it. We need to build data pipelines.\u201D\
    \ That's why people realized that, \u201COkay, this is what data engineers do.\u201D"
  sec: 453
  time: '7:33'
  who: Alexey
- line: "From a data scientist\u2019s perspective, usually you would think \u201C\
    Okay, why should the scientist actually do that? The scientist should work on\
    \ designs, right? He shouldn't work on the engineering.\u201D But it also depends\
    \ on the structure of the project. Or it can depend on the structure of the company.\
    \ If you're in a small startup \u2013 most likely, they start small. They have\
    \ a data scientist and that data scientist needs set something up. There is no\
    \ engineer. So once it works, then they bring it to the engineers and they make\
    \ everything nice and beautiful. But that's why also the data scientists are getting\
    \ more into this."
  sec: 476
  time: '7:56'
  who: Andreas
- header: "Who to hire first \u2013 a data engineer or a data scientist?"
- line: Do you think a company should first hire a data scientist, and then a data
    engineer? Or the other way around?
  sec: 520
  time: '8:40'
  who: Alexey
- line: "I personally think companies should hire both. But they don\u2019t need a\
    \ huge engineering team to start. If you want to start really small \u2013 hire\
    \ one scientist and one engineer. The scientist can focus on the actual science\
    \ and the engineer can think of \u201COkay, how can we turn this into a product\
    \ later down the road?\u201D That's usually a big hurdle. \u201COnce the proof\
    \ of concept is finished, how can we make this into a product?\u201D \u201CHow\
    \ can we build a platform around it?\u201D If you can get a data engineer early,\
    \ then you are already ahead of the game. But generally, I would say the science\
    \ part starts with the scientist. That's the main thing. They have some one-off\
    \ data, which usually lies around somewhere. Somewhere, somebody has the right\
    \ CSV, the right database - hopefully. Most likely."
  sec: 526
  time: '8:46'
  who: Andreas
- header: How can I, as a data scientist, learn to build pipelines?
- line: "So a company hires a data scientist and this data scientist works on a proof\
    \ of concept. Then they need to productionize it. If the company doesn\u2019t\
    \ realize that they need a data engineer, this data scientist implements the whole\
    \ thing himself. What we usually end up with is a lot of code that is difficult\
    \ to maintain, because data scientists are usually not the best engineers. I think\
    \ this is where the question actually comes from."
  sec: 587
  time: '9:47'
  who: Alexey
- line: "The question that I mentioned in the beginning, \u201CHow can I, as a data\
    \ scientist, improve my data engineering skills?\u201D Sometimes it happens that\
    \ data scientists need to do this. So I\u2019ll come back to this question \u2013\
    \ \u201CI am a data scientist. I want to learn how to build data pipelines. How\
    \ can I do this?\u201D"
  who: Alexey
- line: "I think the problem isn't actually the coding. The coding is usually fairly\
    \ simple. Nowadays, in engineering, you can do most stuff with Python if you're\
    \ a good developer, which you should be as a data scientist. This shouldn't be\
    \ a problem. The actual problem that data scientists tend to have or what they\
    \ should look into is thinking ahead to \u201CHow can I deploy this? How can I\
    \ bring this into a uniformed platform?\u201D What a lot of data scientists tend\
    \ to do is choose too many tools for their platform. They choose the packages\
    \ that they use in Python \u2013 \u201CI\u2019ll take this. Take that and try\
    \ this out here.\u201D But actually, in engineering, that doesn't work. You can't\
    \ introduce 20 different tools. You need to figure out which few things you need\
    \ to select and then build everything around them. The actual conceptual part\
    \ is actually the problematic part, which is what the scientist needs to understand."
  sec: 644
  time: '10:44'
  who: Andreas
- header: "Don\u2019t use too many tools"
- line: "Why can't we take 20 different tools and make a platform from them? You said\
    \ it doesn't work like this \u2013 data scientists tend to take many different\
    \ packages and just put them into one thing and do the data science. Why can\u2019\
    t we do this with the platform? Why can't we take 20 different tools?"
  sec: 723
  time: '12:03'
  who: Alexey
- line: The problem is the operations part. Somebody needs to take care of it all
    at some point, even if it's the data scientists themselves. Say you have one data
    scientist and he needs to set something up. He uses 20 different tools. Then the
    data scientist needs to take care of it himself if there are no more people available.
    This will be problematic because there are so many things to keep afloat. Very
    often, some pipeline gets stuck somewhere, something quits, and you need to look
    up what the problem is. If you're using an open source tool here or there, you
    need to optimize the configuration. Therefore, it gets more and more complicated
    to actually have everything up and running as opposed to focusing on a few areas
    and using a few tools. That's very important.
  sec: 742
  time: '12:22'
  who: Andreas
- header: What is a data pipeline and why do we need it?
- line: You mentioned data pipelines and our talk is about data pipelines. Maybe we
    can talk a bit about this. What is a data pipeline? Why do we need a data pipeline?
    Why is my Jupyter Notebook, with all the coordinates, not enough?
  sec: 805
  time: '13:25'
  who: Alexey
- line: "Well, from an analytic standpoint, it's enough. You don't need to set up\
    \ huge pipelines for the actual analytics stuff in most cases. In other cases,\
    \ if it gets more complicated, you need to split up your notebook and create Docker\
    \ containers out of it or whatever and deploy it. But let's forget about the analytics.\
    \ When you think about the pipelines or the platforms, somehow, somewhere \u2013\
    \ you have ingestion. The data needs to come from somewhere. At the other end,\
    \ you have the analytics and the visualization behind it, or storage. So you need\
    \ to actually build something for that. For instance, I always put it into a few\
    \ parts. One part is ingestion. Another part is our buffers, like message queues.\
    \ The next part is processing frameworks, storage, and visualization. These are\
    \ the different areas that you need to look at. If you think about ingestion \u2013\
    \ how could you ingest the data later? For instance, you set up an API or you\
    \ set up an ETL job that pulls the data in. You can have different types of processing\
    \ frameworks."
  sec: 819
  time: '13:39'
  who: Andreas
- header: What is ingestion?
- line: "To clarify on what ingestion is \u2013 let's say we have a website and the\
    \ user can do a bunch of things on it. These events that we track need to end\
    \ up in our database. The process of getting these events and putting them someplace\
    \ \u2013 this is called ingestion. Is that right?"
  sec: 911
  time: '15:11'
  who: Alexey
- line: "You could say it another way. Say you have your website where the user is\
    \ clicking something and you want to track the clicks. The website would actually\
    \ shoot the event and the event would go into a message queue, like Apache Kafka,\
    \ or Kinesis on AWS. Then it lies around there somewhere. Then you need to process\
    \ it further, so you would introduce a processing framework that actually takes\
    \ this message, processes it, and stores it somewhere. The next step would be\
    \ the visualization. In between there somewhere, you use the analytics to actually\
    \ access the data, do the analytics, and put the data back. That\u2019s just an\
    \ example."
  sec: 929
  time: '15:29'
  who: Andreas
- line: To recap, the process is as follows. First, the user makes an event. This
    goes to some message queue. From the message queue it gets into some storage.
    I think this is what is usually called a Data Lake these days, right?
  sec: 971
  time: '16:11'
  who: Alexey
- line: It could be a data lake. It could also be a noSQL database.
  sec: 983
  time: '16:23'
  who: Andreas
- line: "So, just some storage. Then these are raw events, and we need to process\
    \ them. So then there is a job that takes the events and processes them, does\
    \ some transformation, and it ends up in some visualization \u2013 some dashboard,\
    \ maybe, for analytics. Or maybe this is something I, as a data scientists, can\
    \ also take and use it for building my models. Is that right?"
  sec: 989
  time: '16:29'
  who: Alexey
- line: "Yeah. It depends a bit on what you're doing. Are you doing event processing?\
    \ Are you doing streaming \u2013 where you're immediately reacting to the data\
    \ that's coming in? Or are you taking the data in a batch processing way? Because\
    \ when you do streaming, you are going to take the data immediately from the message\
    \ queue, take it, process it, analyze it, make a forecast, and push the data further.\
    \ Or if you're doing a batch process, you would store it first, then take it out,\
    \ process it and put it back in."
  sec: 1011
  time: '16:51'
  who: Andreas
- line: In both cases, we refer to this sequence of things as a data pipeline, right?
  sec: 1046
  time: '17:26'
  who: Alexey
- line: "Yes, I would call this a data pipeline \u2013 a complete pipeline, where\
    \ you have a beginning and an end. You could argue, \u201CWhere's the end? Is\
    \ the end at the storage? Or is the end at the visualization?\u201D It depends.\
    \ But the important part is that there are just a few tools, or a few parts, that\
    \ interact with each other. It's not something that comes and gets stored and\
    \ then at some point you take it out or use a CSV file that you download from\
    \ somewhere. That's not a pipeline."
  sec: 1053
  time: '17:33'
  who: Andreas
- header: Can just one person build a data pipeline?
- line: "That seems like a lot of work. Something that a data scientist \u2013 just\
    \ one person \u2013 probably cannot really implement on his or her own, so it\
    \ needs multiple people and a data engineer, at the very least."
  sec: 1094
  time: '18:14'
  who: Alexey
- line: "It depends where you are. If you're in a private cloud or an on-premise setup,\
    \ where you have to install everything with open source tools and run everything\
    \ on them, that can be annoying. If you're on a cloud platform like AWS, Azure,\
    \ or GCP, it's fairly simple to actually set up a message queue or a no-SQL database.\
    \ As I said before, the problem is understanding \u201CWhich tools make sense\
    \ in the case that I currently have?\u201D Also, another thing that is always\
    \ a problem is the actual schema design. Not in terms of a relational database,\
    \ but the fact that you have to design how the data looks. How do you process\
    \ the data? It's important to understand, \u201COkay, in this step, I need to\
    \ do that. Then I need to do that. And the final result that comes in my documents\
    \ story looks like this. So where can the problems come up there?\u201D"
  sec: 1107
  time: '18:27'
  who: Andreas
- header: Approaches to building data pipelines for data scientists
- line: "Maybe we can simplify this a bit. Let's say I work at a company as a data\
    \ scientist and we have data engineers. The data engineers take care of the ingestion\
    \ part \u2013 they track the events, put them into these message queues, and then\
    \ eventually these events end up in our data lake or some other form of storage.\
    \ We need to then use these events to build our pipelines for our machine learning\
    \ models. The data engineers focus on this lake, so they're not really helping\
    \ us. Maybe they can help a bit, but basically, we're on our own here. We have\
    \ access to this data lake and we need to build a model."
  sec: 1187
  time: '19:47'
  who: Alexey
- line: "Usually data scientists know Python pretty well and some SQL. They know all\
    \ these GitBash things. And when it comes to Python, they also usually know a\
    \ so-called Py Data Stack \u2013 SciKit Learn or NumPy, Pandas. With this knowledge,\
    \ how do we approach this process of building a pipeline to get our events from\
    \ the data lake?"
  who: Alexey
- line: "You mentioned in the beginning, you're more alone in this as a scientist?\
    \ Hopefully not. Hopefully, the engineer speaks to you or you speak with the engineer\
    \ to turn it all in a way that the data gets stored somewhere in a form that you\
    \ can already work with. That's one of the main things that you need to look at.\
    \ As a scientist, I would start very simple. I would focus on Python. If you know\
    \ Python, don't go spread yourself thin with another language. Don't go for something\
    \ like Scala or Java. Use what you already know best. Let\u2019s say I like working\
    \ with Git, and Docker for writing Python code. In this case I would focus on\
    \ what tools there are available to me. What processing frameworks could I use\
    \ to apply my Python skills and build something up with that? You would then use\
    \ it for API building. You wouldn't use something with Java, you would most likely\
    \ look at something like Flask or fast API, which I like a lot for prototyping.\
    \ You would likely need to go in that direction."
  sec: 1265
  time: '21:05'
  who: Andreas
- header: Processing frameworks
- line: So what are these processing frameworks?
  sec: 1351
  time: '22:31'
  who: Alexey
- line: "Processing frameworks. When I coach in my Academy, I try to show my students\
    \ that \u201COkay, there is this section called processing frameworks, which is\
    \ everything that actually takes some data, does something with it, analyzes or\
    \ modifies it, and then gives the output.\u201D So you could think of the processing\
    \ framework as, \u201COkay, what does some processing? A Python script that runs\
    \ in a Docker container.\u201D I already count this as processing. Apache Spark,\
    \ Apache Flink, or if you're on the cloud, you could say, \u201COkay, AWS lambda\
    \ functions or Azure Functions.\u201D These things or perhaps I would use AWS\
    \ Glue for that. These are frameworks that are doing the processing for you, you\
    \ just need to code them right. That's one area that you need to decide on."
  sec: 1356
  time: '22:36'
  who: Andreas
- line: "Back to what we talked about before \u2013 it wouldn't make sense to do a\
    \ part in Spark, then a part in Flink, and then introduce some Lambda functions\
    \ here and there, and then run a Jupyter Notebook, where you do some processing.\
    \ [groans] It almost gets too complicated to actually run with a small team."
  who: Andreas
- line: "So, basically, this is a thing that gets some data in and produces data out,\
    \ right? It might convert something or\u2026?"
  sec: 1444
  time: '24:04'
  who: Alexey
- line: The processing framework, I would say is what you train your algorithms with.
    It's what you apply your algorithms with. It's where you, as a data scientist,
    do the pre-processing. These are the kinds of things where you filter out the
    data.
  sec: 1454
  time: '24:14'
  who: Andreas
- line: I think most of the time we can do plain SQL for most of these things, except
    model training. Like data transformation.
  sec: 1474
  time: '24:34'
  who: Alexey
- line: "It depends on what you're working with. If you're working with some kind\
    \ of a no-SQL database, running simple SQL queries might be a problem. If you're\
    \ doing a more relational-orient or relation database, then yeah \u2013 you most\
    \ likely would use SQL to get the data or just simple files from a data lake.\
    \ But within your framework, it could be that you use SQL to build data frames,\
    \ and then access these data frames via SQL. SQL is still a big part in engineering\
    \ and in science. Everybody knows it. All the tools support it. It's one of the\
    \ big things in data science."
  sec: 1484
  time: '24:44'
  who: Andreas
- header: "Common setup for data pipelines \u2014 car price prediction"
- line: "So what are the most common setups that you see? Or a setup that you would\
    \ recommend? Let's say we have these tasks \u2013 we have data in our S3 bucket,\
    \ for example, or some Google Storage bucket. Let's say these are parquet files\
    \ that the engineers prepared for us. For those who don't know \u2013 parquet\
    \ is a special format for files that is optimized for storing data. So we have\
    \ that \u2013 what would we use to actually process this data?"
  sec: 1536
  time: '25:36'
  who: Alexey
- line: "Giving general recommendations is always a bit problematic because you don't\
    \ know what people are working on. There are a lot of ways of actually processing\
    \ this data. As I said before, you could say, \u201COkay. This data is just lying\
    \ around. I'm just using Docker containers on-house called ECS to actually trigger\
    \ ECS jobs and read the data from the data lake, process it, and then put it somewhere\
    \ else.\u201D"
  sec: 1569
  time: '26:09'
  who: Andreas
- line: "You could even schedule this. AWS, for instance, has a as a scheduling service,\
    \ which is basically Airflow in the cloud. I just forgot how they call it \u2013\
    \ \u201CManage Data Flows\u201D or something like that. You could set up something\
    \ like this. You could also build something within SageMaker \u2013 using SageMaker\
    \ notebook. I use that as well. The possibilities are endless. I don't want to\
    \ cheap out of this question, but there are so many things you could do. It\u2019\
    s difficult to answer."
  who: Andreas
- line: "It may be a problem as well. Because when you have so many tools for doing\
    \ your job, you can get lost. Maybe we can make it a bit more concrete. Let's\
    \ say I want to build a model for predicting car prices. Suppose we have a website\
    \ with cars, their prices, and other different characteristics for cars. We want\
    \ to build the pipeline for training our model \u2013 for predicting prices \u2013\
    \ and a pipeline for applying this model. To make it more concrete, let\u2019\
    s say the data is stored in MySQL. The engineers copy all the data to an S3 bucket,\
    \ so we don't need to touch the production MySQL database. So we have a replica\
    \ of the data set and we need to build a model for that. I don't know if you have\
    \ any preferences for the cloud, so let's say we use S3, as I already mentioned\
    \ it."
  sec: 1642
  time: '27:22'
  who: Alexey
- line: I like AWS the most. I work with AWS the most, so I'm always thinking in AWS.
  sec: 1717
  time: '28:37'
  who: Andreas
- line: "Alright, we can take AWS as an example. I think they're the most popular\
    \ cloud provider right now \u2013 for seven years already or something close to\
    \ it."
  sec: 1729
  time: '28:49'
  who: Alexey
- line: Yeah. By far the most popular.
  sec: 1736
  time: '28:56'
  who: Andreas
- line: I imagine that for most of our listeners, the chances that they use AWS are
    pretty high.
  sec: 1738
  time: '28:58'
  who: Alexey
- line: That depends, by the way. It depends on the on the actual industry. It also
    depends on the actual location. I have students from northern European countries
    where they looked at job descriptions, and it turns out Azure is more prevalent
    for some industries. Then in others, like in the US, most of the things have AWS
    in them. So there are actually differences.
  sec: 1749
  time: '29:09'
  who: Andreas
- line: To your example. I'm not sure if I understood it correctly. Is there data
    coming in from two sides? From the website and from the from the SQL database?
  who: Andreas
- line: "Yeah. Let\u2019s say we have a product. We have a website with cars. We own\
    \ it as a company. What we want to do is help our users when they are not sure\
    \ what price to put. We want to build the model for them when they enter the car\
    \ make, model, etc., we help them by suggesting a price. This is a simple model.\
    \ For this website, it's backed by MySQL \u2013 there is a MySQL database with\
    \ all the data for all the listings. But as data scientists, we cannot really\
    \ go and access this MySQL database, because it's a production database. So what\
    \ engineers made for us is some sort of snapshot replica, just for us to access\
    \ the data. And now we need to build this model."
  sec: 1794
  time: '29:54'
  who: Alexey
- line: "Well, first you need to think about \u201COkay, how do I apply this from\
    \ the analytic standpoint?\u201D You most likely want to apply it so that when\
    \ the customer searches, he already gets the predictions, or the recommendations,\
    \ right? So would you do that live or would you put that into the categories?\
    \ The end result of your analytics - is it always getting generated live, or are\
    \ you doing some predictions and storing them somewhere?"
  sec: 1851
  time: '30:51'
  who: Andreas
- line: "I know it's going to complicate things, but let's say when a user creates\
    \ a new listing, fills everything in and once that\u2019s done, we suggest the\
    \ price. So they get a prediction when they create a new listing - it\u2019s a\
    \ live thing."
  sec: 1893
  time: '31:33'
  who: Alexey
- line: "Okay. There are a few methods you could apply. You could take the listing\
    \ that has just been created and send it into a message queue. That\u2019s how\
    \ you would stay in the streaming lane. At the other side of that is where the\
    \ algorithm is listening. Once something comes in, most likely it will come from\
    \ the website as a JSON, the algorithm takes the listing, does the recommendation\
    \ part, and then either stores it somewhere or offers it over an API. I'm not\
    \ sure how you would want to do that. If the listing already stored, then you\
    \ could say, \u201COkay, I'm putting that to the stored listing.\u201D I mean,\
    \ what you see is that people actually apply or supply the analytics as an API.\
    \ The website would actually call an API and it would run your script in the background.\
    \ The API would then return the recommendations."
  sec: 1910
  time: '31:50'
  who: Andreas
- header: Productionizing the model with the help of a data pipeline
- line: "What you described is the process when we already have a model and we want\
    \ to deploy it. So this how we would use it. But what I meant is \u2013 we don't\
    \ have model yet, we need to do build it, right? So what can I do as a data scientist?\
    \ I can pull this data in, save it on my laptop, open Jupyter Notebook. You know,\
    \ do stuff with Pandas, do stuff with NumPy, SciKit Learn. Train this model and\
    \ I have this pickle file."
  sec: 1997
  time: '33:17'
  who: Alexey
- line: "Then two months after that, things change \u2013 the prices are different\
    \ \u2013 and we need to retrain it. I don't want to do this every month. I don't\
    \ want to pull in new data and execute cells in a particular order in my Jupyter\
    \ Notebook, because maybe in half a year I will forget that I need to execute\
    \ this cell before this cell because I accidentally messed with the order. So\
    \ we need to somehow productionize it."
  who: Alexey
- line: "That's what I meant \u2013 with the Jupyter notebook, sometimes it's good.\
    \ For this, to create a proof of concept or the first version of your analytics,\
    \ you would set up in a Jupyter notebook so that you can see that it works. The\
    \ next part would be productionizing it. Most likely, if you're already in a Jupyter\
    \ Notebook and working with this stuff, you could just go and take your Python\
    \ code, put it in a Docker container, schedule this container to run on the data,\
    \ every day, every week. And then just retrain the models to see if you find something\
    \ better \u2013 to see if you find some different results for the current ones.\
    \ This way, you keep training your models and then you store the model somewhere\
    \ and apply them. Most likely you can store the model conflicts on S3. When you\
    \ apply the model in your pipeline, you will actually have your script, and that\
    \ script would pull the pull the information from S3 and then just apply it."
  sec: 2056
  time: '34:16'
  who: Andreas
- header: Scheduling
- line: So, we take our Jupyter notebook, we put it in a Python file, we put this
    Python file in some Docker container and we go to our cloud and find a way how
    we can schedule this script. And that's pretty much it. Right?
  sec: 2127
  time: '35:27'
  who: Alexey
- line: Depends on how you want to run it. For the training - yeah. The actual scheduling
    can be really easy. You could use something like Airflow. But if you have something
    real simple, you could use Cloudwatch and then schedule the bit with AWS. You
    need to schedule a lambda function, which then starts your container. You could
    very easily set this up without having the whole framework running like Airflow.
    That's what I meant before. Does the data scientists need to look into this to
    actually figure out? Is it worth it? Because it's one more thing to manage. Or
    can I can he live right now with something that is less complicated?
  sec: 2146
  time: '35:46'
  who: Andreas
- line: You said Cloudwatch. As far as I remember, in Amazon, there are multiple ways
    of deploying a Docker container. You have ECS, AWS Batch, and SageMaker, right?
    So you can just take any of these, put your Docker container there with your script,
    and then use Cloudwatch to schedule it to run every week, for example.
  sec: 2204
  time: '36:44'
  who: Alexey
- line: "I remember I think we talked about the fact that SageMaker can get quite\
    \ expensive. That's why I'm always hesitant to say \u201CUse SageMaker for everything.\u201D\
    \ [laughs]"
  sec: 2234
  time: '37:14'
  who: Andreas
- line: "Well, at least you can use AWS Batch. I think it\u2019s four times cheaper,\
    \ if I remember correctly."
  sec: 2247
  time: '37:27'
  who: Alexey
- line: That I don't know.
  sec: 2252
  time: '37:32'
  who: Andreas
- line: "So in SageMaker, they have the same instances \u2013 instance types \u2013\
    \ but they have ML in front of them. And just having ML in front of them makes\
    \ them more expensive. But in the end, it\u2019s the same types of instances."
  sec: 2256
  time: '37:36'
  who: Alexey
- line: Oh, well. That's logical.
  sec: 2269
  time: '37:49'
  who: Andreas
- line: "The cool thing I like about that is what I mentioned before. Deploying your\
    \ algorithm as a service \u2013 what you could do is deploy your algorithm as\
    \ an endpoint with SageMaker that you have running. You can send the data to the\
    \ endpoint and it will send you some predictions. That\u2019s something that is\
    \ really, really cool and now makes it a bit easier to do the management of the\
    \ pipelines."
  sec: 2273
  time: '37:53'
  who: Andreas
- line: Let's make our example a bit more complex. So let's say we have this [laughs]
  sec: 2304
  time: '38:24'
  who: Alexey
- line: "Usually I do this with boards \u2013 where we draw on the board, so I get\
    \ the picture. Yeah, let's make it more complicated."
  sec: 2309
  time: '38:29'
  who: Andreas
- header: Orchestration
- line: Let's say to get the data from this storage that we have, we need to write
    a couple of SQL queries. And we need to execute the SQL queries one after another.
    We have a lot of fraud data. So the first query would get us a smaller data set
    with only the data we need. Let's say this second query would do some extra aggregation
    or cleaning. So we have two queries that do something and then at the end, this
    is what we use for training in our model. We take the output of the second query
    and, again, do some simple stuff with Pandas, train our model, and we get this
    pickle file.
  sec: 2319
  time: '38:39'
  who: Alexey
- line: "Now we need to schedule this \u2013 to somehow run the whole thing in a sequence.\
    \ We need to run the first query, then the second query that gets the results\
    \ of the first query and produces some other results. Then the third job gets\
    \ the results from the second query and trains model and produces the pickle file.\
    \ So how do we orchestrate this whole thing?"
  who: Alexey
- line: "I feel like I say always \u2018it depends\u2019 but it depends on how complicated\
    \ you want to make it."
  sec: 2392
  time: '39:52'
  who: Andreas
- line: "Let\u2019s say the simplest possible."
  sec: 2400
  time: '40:00'
  who: Alexey
- line: "You could do something really simple where you build up a message queue.\
    \ Once the first script is ready, it fires up a message into the message queue.\
    \ Then on the other side, there\u2019s a listener that basically takes this message,\
    \ and in the message, you say, \u201COkay, what part of the job already ran? Where\
    \ is the data stored?\u201D Then the second part can take the data, process it,\
    \ and then writes back to the message queue. This way you can use your message\
    \ queue in a streaming manner, where one job takes the information out, \u201C\
    Okay, I need to do something. Where is the data lying around? Do it. I'm finished.\
    \ Write back.\u201D So it\u2019s often very easy to use queues for this kind of\
    \ job."
  sec: 2401
  time: '40:01'
  who: Andreas
- header: Start simple
- line: I think I implemented something like this a couple of companies ago. When
    I left, what they ended up doing this discovery and all that, and then moved into
    Airflow.
  sec: 2455
  time: '40:55'
  who: Alexey
- line: "Yeah. Airflow \u2013 these things are really strong, and really good, so\
    \ it makes sense to use them. But if this is a one-off thing and you need to build\
    \ something quick, you need to start somewhere. What is good enough? Most likely,\
    \ for this company, you build this, it ran for some time, and it was good enough\
    \ while you build it. At some point, it grew over. They needed to have more logging\
    \ behind it, more insight. Then you move to something like Airflow or something.\
    \ You don't need to go all out in the beginning."
  sec: 2466
  time: '41:06'
  who: Andreas
- line: So, for the first model, if it's just the first data science project in the
    company, you don't need to go with Airflow, Kubernetes, and all these big things.
  sec: 2514
  time: '41:54'
  who: Alexey
- line: "It depends a bit on your timeline. What the goal of the company? Where does\
    \ the company want to move? Is the company unsure where to move? Or is this going\
    \ to be a platform where a lot of projects are going to work? Then it's good to\
    \ have help \u2013 then I would set up everything already. Otherwise, start small.\
    \ Start Agile and you can always build something or add something to it after\
    \ afterwards. That's also what I usually tell my coaching students. \u201CBuild\
    \ something first. Build it simple. And then, at some point, add more stuff to\
    \ it. Start with a Lambda function and then use Spark streaming for that. And\
    \ then take the next step.\u201D In every area you can always escalate and make\
    \ it more complicated down the road."
  sec: 2527
  time: '42:07'
  who: Andreas
- header: Learning DevOps to implement data pipelines
- line: "We have a related question from Chetna. I think we already discussed how\
    \ we can do this from a Jupyter Notebook like our data scientists can start their\
    \ journey towards picking up data engineering skills. That part we discussed,\
    \ but the second part of the question is \u201CHow do you learn the DevOps and\
    \ software engineering skills that you need to actually to be able to implement\
    \ this?\u201D"
  sec: 2585
  time: '43:05'
  who: Alexey
- line: "DevOps skills \u2013 that's where the tool selection comes in. You need to\
    \ understand, \u201COkay, how can I actually bring this into production? How do\
    \ I manage my code? There are certain tools that I see around all the time, something\
    \ like GitLab. A lot of people use GitLab as their code repository, as well as\
    \ for building and deploying their code in production. That's something I see\
    \ a lot. Generally, there are many tools out there. It's the same most of the\
    \ time. If you use Jenkins for building and so on, most likely there's the same\
    \ stuff."
  sec: 2616
  time: '43:36'
  who: Andreas
- line: So your recommendation would be to just pick any tool and try to learn it?
  sec: 2676
  time: '44:36'
  who: Alexey
- line: I would pick something that fits to the rest of what I just built. That's
    what I meant in the beginning. You need to understand what tools you actually
    want to use so you don't go overboard and so that everything fits together. You
    need to know that you're actually using the right tool to manage and deploy your
    code so that it that fits into your actual production environment.
  sec: 2681
  time: '44:41'
  who: Andreas
- header: How to choose the right tool
- line: If I'm a data scientist and I don't have experience with these kinds of things,
    I would need to talk to a data engineer or somebody who's dealing with infrastructure
    to actually help me and guide me for that. Because how do I know if this is the
    right tool if I haven't used it previously?
  sec: 2713
  time: '45:13'
  who: Alexey
- line: "Yeah. There are a few options of what you can do. First of all, how I always\
    \ go about this \u2013 this may sound very lame, but I look at the documentation\
    \ of the tool. What can this tool actually do? Then I search for examples where\
    \ people already did that what I envision doing. If you can find some examples\
    \ out there \u2013 like on Google \u2013 examples where they did this, this, and\
    \ this, specifically. You can also find some quick to-do lists or tutorials. If\
    \ you can do all that, then you are most likely already on the right track. If\
    \ it's an open source tool, or whatever, just set it up in a dev environment and\
    \ test it out. If that works, that already looks good \u2013 you're most likely\
    \ on the right track."
  sec: 2731
  time: '45:31'
  who: Andreas
- line: "Coming back to our example of \u2018building a model for price prediction\u2019\
    . Let's say we decided to go with AWS Batch and Lambda and whatnot. What we can\
    \ do is go to our favorite search engine, put the queries there, like \u2018model\
    \ training pipeline\u2019, and the name of the tool \u2018AWS batch lambda\u2019\
    , and hit enter. Maybe adding \u2018tutorial\u2019 at the end might help as well.\
    \ We see what the results are. You may end up on \u2018towards data science\u2019\
    \ or some other similar website, where there is nearly a step-by-step tutorial\
    \ with all the steps that you need to do."
  sec: 2797
  time: '46:37'
  who: Alexey
- line: "Very often you can find something be entering, like in your case, \u2018\
    how to use AWS batch to analyze S3 data\u2019 or something along those lines.\
    \ Most likely, you\u2019ll find 10 blog posts that already do the exact thing\
    \ that you want to do. Then you just insert your code. Of course, you need to\
    \ write it, but the frame around it is there \u2013 how to get the data and where\
    \ to write the data. Most likely, you can already extract what you need from this."
  sec: 2842
  time: '47:22'
  who: Andreas
- line: "Yeah, so I guess the short answer to this question \u201CHow to learn DevOps?\u201D\
    \ is just \u201CDo stuff. If you don't know how, Google them.\u201D"
  sec: 2874
  time: '47:54'
  who: Alexey
- line: "Use the search to find out what different tools there are. What capabilities\
    \ do they have? How does that fit to the rest of the platform? And then just try\
    \ it out. I always go for the \u201COkay, let's try this\u201D approach. Because\
    \ usually, when you actually do it, you find the holes in the whole thing. \u201C\
    This doesn't work that way. This doesn't work that way.\u201D It's always the\
    \ same. Unfortunately."
  sec: 2882
  time: '48:02'
  who: Andreas
- header: Are Hadoop, Docker, Cloud necessary for a first job/internship?
- line: "Another question, \u201CDo you think data engineering skills like Hadoop,\
    \ Docker, Cloud, are necessary for students who are looking for internship? Do\
    \ they need to have these skills to get their first job?\u201D"
  sec: 2916
  time: '48:36'
  who: Alexey
- line: "No. I think for an internship, if you can code Python and know your way around\
    \ SQL \u2013 that should be enough. You should have learned this during your studies.\
    \ If you have a bit of an idea of how computer networking works, like DNS, IP\
    \ networking, that\u2019s also good. If you have an idea about these things, you're\
    \ good to go for an internship. For becoming a junior data engineer, I think you\
    \ need some experience on some kind of a platform. Most likely it makes sense\
    \ to use AWS. I would start by using AWS. That's why in the academy I build the\
    \ AWS capstone project first, because I think that's the most important thing.\
    \ We use that most often in the coaching as well."
  sec: 2935
  time: '48:55'
  who: Andreas
- line: "The second important part, in my opinion, is the open source tools. Just\
    \ use a few open source tools like Kafka, Spark, MongoDB \u2013that\u2019s some\
    \ stuff that is around everywhere. It makes sense to know them. If you don't get\
    \ a junior role after that, I don't know\u2026 I would most likely hire someone\
    \ who has that on a resume. The important part is documenting it. That's what\
    \ I always say to my students \u2013 document your stuff. Never just do an AWS\
    \ certification, or whatever \u2013 never just do the certification. Always create\
    \ a GitHub, put up some information, put up interesting stuff that you have learned.\
    \ You need a track record. You need to have a track record. You need to have a\
    \ professional profile. Not just a LinkedIn page, but a professional profile that\
    \ has some experience."
  who: Andreas
- header: Is Hadoop still relevant or necessary?
- line: "In this question, there is a bunch of things mentioned under \u2018data engineering\
    \ skills\u2019, which are Hadoop, Docker, Cloud. So Docker and cloud \u2013 I\
    \ don't think you would argue that these are important things to learn. What about\
    \ Hadoop? Do people still need it or use it?"
  sec: 1256
  time: '20:56'
  who: Alexey
- line: "It depends. [laughs] I see the trend that Hadoop isn't what it used to be.\
    \ The cloud platforms got so strong and they innovated so fast, most companies\
    \ nowadays use the cloud platform. Yes, you still have stuff lying around that\u2019\
    s still working on Hadoop \u2013 very often in bigger companies where they\u2019\
    re running private clouds. And of course, they're running Hadoop. I think learning\
    \ it to get a role can make sense, but it's not one of the primary things. The\
    \ cool thing I\u2019ve noticed coming from Hadoop, I see that everything on the\
    \ cloud platform, is basically the same stuff that you do on Hadoop. You're running\
    \ on a Hadoop platform, it just has different name and works a bit differently.\
    \ It's very, very interesting how these tools fit together."
  sec: 3074
  time: '51:14'
  who: Andreas
- header: Data engineering academy
- line: "We have a question from Julian. The question is about your academy. You mentioned\
    \ it a couple of times. First of all, \u201CWhat is the link to the academy? How\
    \ can people find it?\u201D"
  sec: 3141
  time: '52:21'
  who: Alexey
- line: LearnDataEngineering.com
  sec: 3159
  time: '52:39'
  who: Andreas
- line: "It\u2019s one word, right?"
  sec: 3161
  time: '52:41'
  who: Alexey
- line: "One word. That's where I have the Academy and where I do the coaching. I\
    \ started with YouTube, I don't know how many years ago \u2013 four years, three\
    \ years? When did we talk Alexey? Do you know how many years ago?"
  sec: 3166
  time: '52:46'
  who: Andreas
- line: I think two years.
  sec: 3181
  time: '53:01'
  who: Alexey
- line: "Maybe two and a half years ago, I started with YouTube. On YouTube, you make\
    \ videos, but you can\u2019t put up a journey. You can say, \u201COkay, learn\
    \ this, this, this, and this and then it will work out.\u201D So last year, I\
    \ actually decided to \u201COkay, let's try to build a curriculum for actually\
    \ learning data engineering.\u201D It turns out that it's harder than I thought.\
    \ What we talked about before \u2013there are so many tools and you need to focus\
    \ on some stuff. But in the academy,"
  sec: 3183
  time: '53:03'
  who: Andreas
- line: "I created a step-by-step course that gives you the fundamentals of what data\
    \ engineering is and what you need to actually start. Then we go through basics\
    \ of platform pipeline design. Then the fundamental tools. Then capstone projects\
    \ \u2013 like the AWS project. We have one more coming next week about Azure \u2013\
    \ an Azure course. I'm currently working on another one, as I said before, with\
    \ open source tools, MongoDB, Kafka, Spark, and so on. If somebody is interested\
    \ in data engineering, check that out. Or check out one of my 300 videos on YouTube.\
    \ I don't know how many there are currently."
  who: Andreas
- line: "I think if you Google \u2018the plumbers of data science\u2019, the first\
    \ link should be your channel."
  sec: 3272
  time: '54:32'
  who: Alexey
- line: Could be. Yeah.
  sec: 3286
  time: '54:46'
  who: Andreas
- line: Or your name.
  sec: 3284
  time: '54:44'
  who: Alexey
- line: Yeah. My name is well. My name and data engineering most likely would bring
    something up.
  sec: 3286
  time: '54:46'
  who: Andreas
- header: How to pick up Cloud skills
- line: "What I understood by talking to you now is that one of the most important\
    \ skills data scientists need to have in order to pick up data engineering is\
    \ cloud skills. But \u2018cloud skills\u2019 is such a broad term, right? But\
    \ there are a couple of tools that are useful for data processing. I'm wondering\
    \ if it\u2019s possible to give a good recommendation on how to approach learning\
    \ this? I usually suggest learning things by doing projects. Maybe you can recommend\
    \ a project that people can build in order to pick up these cloud skills?"
  sec: 3292
  time: '54:52'
  who: Alexey
- line: "A project? Well, I don't want this to be a sales thing. One project you can\
    \ do is ecommerce data on AWS. I think the general approach is the more important\
    \ approach. On my website, you can find a link to the data engineering cookbook.\
    \ Also on my YouTube, I have videos about my data science platform blueprint.\
    \ This will help you a lot to actually see the areas that I talked about before\
    \ \u2013 connect, buffer, processing, framework, store, visualize. Then actually\
    \ choose some select tools for each of these and build a pipeline. Just start\
    \ by using this. Use a data set from Kaggle or wherever \u2013 you don't need\
    \ to go really big. Use a small data set, 40 megabytes, whatever. Just start applying\
    \ this in a building a platform and building some pipelines on it."
  sec: 3336
  time: '55:36'
  who: Andreas
- line: "I think there are a couple of competitions on Kaggle, where it's not just\
    \ one CSV file, but they have multiple CSV files. Then you would need to actually\
    \ join four or five different files. Then to actually build this final table you\
    \ need to do multiple joins. I think this kind of dataset would be most interesting,\
    \ because this is what we usually do at work. So it's not just data that\u2019\
    s already prepared, but we need to do a couple of joins and couple of things on\
    \ top of that. I think one of the competitions was, I think, Outbrain Click Prediction.\
    \ There are a couple of them. These click prediction competitions are quite interesting,\
    \ because they have a lot of data there. But 40 megabytes, I think is also a good\
    \ start."
  sec: 3403
  time: '56:43'
  who: Alexey
- header: Avoid huge datasets when learning
- line: "The thing is, for learning it, you don't need the huge data sets. When you\
    \ use huge data sets, first of all, the loading times are going to be terrible.\
    \ Everything runs long. You cannot easily look into the data. Because it's big,\
    \ the cloud platforms are going to cost more because you need bigger systems and\
    \ everything. Don't need that. Very often in the academy or in the coaching, we\
    \ use a simple ecommerce datasets from Kaggle. Even there you can understand some\
    \ things like, \u201CWould you go the no-SQL route and not the standard route\
    \ of building a relational database?\u201D and so on. It doesn't need to be complicated\
    \ to actually start. If you're listening to this, you only need to remember one\
    \ thing \u2013 start simple and use a simple data set. Don't go all out. You will\
    \ only get frustrated. Most likely, use the cloud for beginning."
  sec: 3453
  time: '57:33'
  who: Andreas
- line: "So don\u2019t start with Kubernetes, Airflow and one terabyte of data, right?"
  sec: 3528
  time: '58:48'
  who: Alexey
- line: No. [laughs]
  sec: 3535
  time: '58:55'
  who: Andreas
- header: Convincing your employer to do data science
- line: "Good advice. So it's almost time for us to finish. But there is one interesting\
    \ question. Maybe we can take a couple of minutes to answer it. Maybe it's a tough\
    \ one. Let's try. \u201CI'm trying to convince my company to start a data science\
    \ department. What is the best tool set to show results with my current $0 budget?\u201D"
  sec: 3536
  time: '58:56'
  who: Alexey
- line: "Well\u2026 I don't want to discourage people, so I\u2019m being careful with\
    \ what I say. If you need to convince somebody to actually use data science, it's\
    \ already a bit of a problem. I would go the route of just doing it. If you don't\
    \ have money and you can spend some time. Just build something locally. Don't\
    \ build a platform. Don't build pipelines. Do a proof of concept. As we said,\
    \ use a notebook, get some data, and show what analytics can actually do \u2013\
    \ what analytics can deliver. Put a number on it. \u201CHow much money will this\
    \ bring?\u201D People don't care about data, like \u201CHow much data we processed\
    \ for that.\u201D or \u201CHow long it took.\u201D"
  sec: 3563
  time: '59:23'
  who: Andreas
- line: "\u201CHow much money will this bring in?\u201D is even better than \u201C\
    How much money will be saved through that.\u201D Most likely, revenue counts.\
    \ So if you can show a good result, if you can show a rough timeline, and how\
    \ much revenue this can generate in the future, then most likely, something will\
    \ move if you talk to the right people. Otherwise, forget it."
  who: Andreas
- line: So you need to turn this $0 budget into something greater than zero.
  sec: 3658
  time: '1:00:58'
  who: Alexey
- line: "Yeah. The cool thing nowadays is, if you have if you have a MacBook or whatever,\
    \ you can already start doing data science. It's not like you need that a big\
    \ machine \u2013 a $10,000 analytics PC. You can start small."
  sec: 3663
  time: '1:01:03'
  who: Andreas
- line: "In AWS, there is this thing called \u2018free tier\u2019. Right? Which allows\
    \ you to do some lambda stuff for free. You can get EC2 for free."
  sec: 3679
  time: '1:01:19'
  who: Alexey
- line: Yeah, but how much does that help you? Most likely, you are going to run tests
    for a few days or train models for a few days, and the feature is over. You have
    a computer at work, use that. Start a training at the end of the day, let it run
    throughout the night or over the weekend. And hope that something comes up on
    Monday.
  sec: 3690
  time: '1:01:30'
  who: Andreas
- header: How to find Andreas
- line: "That's interesting. Last question \u2013 how can people find you?"
  sec: 3725
  time: '1:02:05'
  who: Alexey
- line: "You can find me by just Googling my name \u2013 Andreas Kretz \u2013 or \u201C\
    plumbers of data science\u2019 or \u2018learn data engineering\u2019. On LinkedIn,\
    \ on YouTube, on Instagram."
  sec: 3730
  time: '1:02:10'
  who: Andreas
- line: Instagram?
  sec: 3743
  time: '1:02:23'
  who: Alexey
- line: "Instagram as well.  Andreas Kretz. I have 1400 followers. Wow. Trying so\
    \ hard on Instagram. Instagram is terrible. You can contact me there as well.\
    \ We have a Telegram chat group. If you go to LearnDataEngineering.com, on the\
    \ bottom is a telegram chat group \u2013 \u201CTeam Data Science\u201D I call\
    \ it."
  sec: 3744
  time: '1:02:24'
  who: Andreas
- line: "I\u2019ll put a link in the description. Do you have any last words?"
  sec: 3771
  time: '1:02:51'
  who: Alexey
- line: Thanks for inviting me. It was really fun talking to you, Alexey. I hope I
    a few people will  get into engineering now. It's really a cool profession. And
    I love it.
  sec: 3778
  time: '1:02:58'
  who: Andreas
- line: "I'll put all these links, maybe not right now, in a couple of hours. So check\
    \ the description. We have a couple of more talks tomorrow and on Friday. Check\
    \ them out. Thanks for joining us today. Thanks a lot, Andreas, for sharing your\
    \ experience with us. Now, the next time when somebody asks, \u201CHow can I build\
    \ a data pipeline?\u201D I will share this video with them and hopefully they\
    \ will not start with Kubernetes and other stuff but something simple."
  sec: 3791
  time: '1:03:11'
  who: Alexey
---


Links:

- LinkedIn: <https://www.linkedin.com/in/andreas-kretz>{:target="_blank"}
- Data engieering cookbook: <https://cookbook.learndataengineering.com/>{:target="_blank"}
- Course: <https://learndataengineering.com/>{:target="_blank"}
