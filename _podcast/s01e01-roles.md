---
title: "Data Team Roles Explained"
short: "Roles in a Data Team"
guests: [alexeygrigorev]

image: images/podcast/s01e01-roles.jpg

keywords: "data team roles, data scientist, data engineer, machine learning engineer, data analyst, MLOps engineer, product manager, data team structure, data science roles, ML engineer vs data engineer, data team responsibilities, data science career"

season: 1
episode: 1

ids:
  youtube: UukjwSIAnpw
  anchor: Roles-in-a-data-team---Alexey-Grigorev-emqcft

links:
  youtube: https://www.youtube.com/watch?v=UukjwSIAnpw
  anchor: https://anchor.fm/datatalksclub/episodes/Roles-in-a-data-team---Alexey-Grigorev-emqcft
  spotify: TODO
  apple: TODO
---

The topic today is the roles in data teams. We want to understand what kind of people work in the data team, what responsibilities they have, what they do, and what they need to know.

**Q: Before we dive into the different roles in data teams, could you tell us about your professional background and what perspective you bring to this topic?**

I work as a **lead data scientist** and this means that my views might be a bit biased towards the views of a data scientist. This is how a data scientist sees other people, so I might not necessarily be right in all aspects. If you think I'm wrong somewhere, please tell me, because the views of how I see data engineers are simplified - I don't see all the complexities of the work they're doing.

**Q: What are the main roles that typically exist within a data team, and how do they differ from each other?**

In a data team there are many different roles. First we have a **product manager** - somebody who is responsible for the entire product and for making sure that the team is building the right thing. Then we have data specialists. The product manager is a little less technical than the rest, but we have people such as **data analysts**, **data scientists**, **data engineers**, **machine learning engineers**, and **MLOps engineers**.

It's often difficult to understand who is who and who needs to do what, and this is why we have this conversation today - to answer these questions. There are also more traditional roles such as **backend engineers**, **mobile engineers**, and **software engineers**. All these people often work together with data scientists and other people to create data science products.

**Q: Let's dive deeper into the specific responsibilities of each role. Could you walk us through a concrete example to illustrate how these roles work together?**

I'll use an example from my work. I work at OLX Group - OLX is a platform for online classifieds where you can sell things you don't need. If you have an iPhone you want to sell, you go to this website, create a listing, and sell your iPhone. If you want to buy something, you go to OLX, browse different advertisements, find what you want, and buy it.

Imagine we want to automatically detect the category of an item. If I'm selling an iPhone and creating a listing, the system should understand that iPhone belongs in the mobile phones category. This is the problem we'll use for illustration.

**Q: Let's start with the product manager role. What are the main responsibilities of a product manager in a data team, and how do they contribute to the project?**

The main responsibility of a product manager is to **make sure that the team is building the right thing** - that whatever we build will be used by the user. Often a team is solving some problem, but in the end these services are not used. This is a problem in many companies, and that's why the role of a product manager exists - to make sure that the team is as close to the user as possible. The product manager **speaks on behalf of the user**.

The main skills here are **communication skills**. For a data scientist, communication is a soft skill, but for a product manager it's a hard skill - something they must have to do their work. They also need to do **prioritization and planning** to tell others what is more important, what is less important, what the team should focus on and what they shouldn't focus on.

In our example, somebody comes with a request: "We want to build this feature to automatically categorize a listing." First, this person would go to a product manager. Product managers receive these kinds of requests - they act as a gateway to receive all these requests. Then the task of a product manager is to figure out: do users really need that? Is this feature really important? Is it an important problem to solve or not? They often work together with data analysts to understand if this problem is worth solving.

**Q: What about data analysts? What are their specific responsibilities and how do they contribute to the data team's success?**

The role of a data analyst is to **understand the data we have and explain this data to others**. Analysts know all the data that we have in our company. They know how to get this data and how to interpret results. They are in charge of **building different dashboards** and **defining KPIs** - showing profit, number of listings, how many contacts buyers made to sellers. Data analysts know how to capture these metrics and how to present them in a way that others will understand. They are also in charge of **building reports**, often to the executive team, with actionable recommendations.

When it comes to skills, data analysts should know **SQL** - this is the main tool. They should know a programming language such as **Python** or **R**. They should also be comfortable using **Tableau** or similar tools for building dashboards. They should know basics of **statistics** to be able to do different experiments, and a bit of **machine learning** - to do regression analysis or time series prediction. If we want to predict how many listings there will be next week or next month, this is something that data analysts can also do.

Data analysts in this example would help quantify the extent of a problem for the product manager. If somebody comes with a problem - "build a model for automatic categorization of listings" - data analysts would help quantify the problem. How many users are affected by this? How many users cannot finish creating the listing because they cannot select the right category? Or how many listings don't have the right category? Analysts fetch the data and say "this problem is indeed a problem," and then together with product managers they can say "this problem is worth solving," and the team will go ahead and start solving this problem.

Data analysts also do this: after we develop the feature and have a model that categorizes the listings, we want to understand if this service is actually effective, if this model really helps people and solves the problem. We typically **run an experiment such as an A/B test**. We check whether fewer users drop from the posting flow, so more users successfully finish posting an item for selling, or there are fewer ads that end up in the wrong category. We run an experiment and then the task of a data analyst is to **quantify and understand if this model indeed helps** compared to not using a model.

**Q: How do data scientists differ from data analysts? What are their unique responsibilities and skill sets?**

Data scientists and data analysts have pretty similar roles, and in some companies it's actually the same person doing both jobs. But typically, data scientists **focus more on predicting rather than explaining**. A data analyst fetches the data, looks at it, explains what is going on, and gives recommendations. But the task of a data scientist is focused more on predicting - how we can use this data to build a machine learning model for prediction. They're using the data, **incorporating the data in the product**. The focus is **more on engineering than analysis**. That's the main difference in my opinion between a data scientist and a data analyst. Data scientists are more like engineers, and they work closely with integrating data solutions in the product that users use.

The skills for data scientists are, of course, **machine learning** - this is the main tool they use for building these predictive services. Then **Python** as a programming language, and **SQL** to fetch the data and train the model. They also need **Flask** and **Docker** to create a web service for serving this model. In our example, when we want to predict the category of an item, data scientists are the people who **develop the model** for predicting this category. Once they have a model, they **develop a web service** for hosting it.

**Q: What about data engineers? What are their key responsibilities and how do they support the rest of the data team?**

Data engineers do all the **heavy lifting when it comes to data**. For data scientists and data analysts to be able to use this data, a lot of work needs to happen to make it possible for data analysts to go to a database, fetch the data, do the analysis, and come up with a report. This is the focus of data engineers - to make sure that this is possible. That all the data needed appears in a consumable form and doesn't affect the main product. This is usually called **creating a data lake** - all the data that users generate is captured properly and saved in a separate database so that analysts can run the analysis and data scientists can use this data for training models. They make it possible to **run analytical queries** on the data that users generate.

Also, especially at larger companies, they need to make sure that **only people who are supposed to look at the data can actually access it**. People who are just snooping around and trying to look at personal data cannot do this unless they have a business reason - for example, to look at emails or mobile phones. They need to build a system that doesn't let people access all the data without authorization.

Skills here for data engineers - usually, for most companies I saw in Germany and Europe, data engineers need to know a cloud provider such as **AWS** (the most popular), or **Google Cloud**. They also need to know infrastructure tools such as **Kubernetes** and **Terraform**. Then data services such as **Kafka** or **RabbitMQ** - these are for capturing the data, processing the data, and saving it somewhere. Of course **databases** - this is where the data is saved so it's accessible for data analysts. And data orchestration tools such as **Airflow** - they need to know how to use them to build complex data pipelines.

In the task that we have - creating a service for predicting the right category for a listing - data engineers make sure that all the data we need is there. First for doing the analysis, for quantifying the problem. And then the data about the listings themselves - everything we want to use for predicting the category. So this is their main responsibility.

**Q: Are there other types of engineers that work in data teams beyond data engineers? What roles do they play?**

Yes, we have **machine learning engineers**. A machine learning engineer is somebody who takes whatever data scientists built and their task is to **scale that**. Data scientists build a service and machine learning engineers pick up this service and make sure the service is **scalable**, **maintainable**, and follows the **best engineering practices**.

The focus here is **more on engineering than on modeling**. When I say taking what data scientists built, I don't mean that data scientists finish their work, hand over the model, and say "take it and do something with this." Rather, they work **together with data scientists side by side**, making sure that the services that data scientists develop are scalable, maintainable, and follow best engineering practices.

Skills here are similar to data engineers. They also need to use the **cloud**, infrastructure tools such as **Kubernetes** and **Terraform**, **Python**, and other programming languages. They also work often closely with traditional engineers such as backend engineers, frontend engineers, or mobile engineers to make sure that these models are included in the final product that users use.

In our example of predicting the category, machine learning engineers ideally work together with data scientists on making sure that this model can be **productionized**. Once it's rolled out to the users, it's stable, it will sustain the load, and it's maintainable and possible to make changes in the future when needed.

**Q: What about DevOps engineers and Site Reliability Engineers? How do they fit into data teams and what are their responsibilities?**

Another kind of engineers are also important in a data team - **DevOps engineers** or sometimes **Site Reliability Engineers (SREs)**. They are also similar to machine learning engineers, but they focus more on **availability and reliability of the services**. They are not strictly working with data only - this is more of a general role. They focus more on **infrastructure than business logic** - things such as networking, provisioning, all the infrastructure, all the servers where our services are running.

They take care of **collecting all the operational metrics** such as CPU usage, how many requests per second our services process. They often **set up alerts**, they have **on-call** responsibilities. They really focus on making sure that the services are **up and running all the time without any breaks**.

If something breaks, SREs can quickly **diagnose the problem and fix it**, or involve an engineer to help them.

Skills here are again pretty similar to ML engineers. They need to know **cloud**, infrastructure tools, a programming language such as **Python**, but they also need to be **Unix/Linux experts** and they need to know **networking**. They should also know and follow all the **best DevOps practices** such as automation, **CI/CD**. Of course, ML engineers and data engineers should also know that, but DevOps engineers and Site Reliability Engineers focus on making sure that these practices are followed and they come up with tools to make sure that it's happening.

**Q: What about MLOps engineers? How do they differ from traditional DevOps engineers, and what makes their role unique in data teams?**

Maybe you heard about **MLOps engineers** - this is a pretty recent trend to have MLOps, not just DevOps. In my opinion, and many people disagree, but in my personal opinion, an MLOps engineer is a **DevOps engineer who knows the basics of machine learning**. They know some machine learning concepts - they know what a model is, they know that it's not deterministic, sometimes the output is a probability. They know the **life cycle of a machine learning model** - there is a training phase, there is a serving phase. But still, the background is more **operational support** than anything else.

They still know and follow all these DevOps practices, they make sure that everybody is following them, they set up all this **continuous integration**, **continuous delivery pipelines**. Their responsibility is to make sure that the services we develop - data scientists, machine learning engineers, data engineers - **are up and running all the time**.

**Q: Could you provide a summary of all these different roles and their key responsibilities in a data team?**

Let me summarize:

- **Product managers** make sure that the team is building the right thing. They act as a gateway to all the requests and are close to the user.
- **Data analysts** understand and analyze data. They interpret the results, build dashboards and reports.
- **Data scientists** build the models and incorporate these models in the product.
- **Data engineers** prepare all the data for analysts and data scientists to make their life easier.
- **Machine learning engineers** help data scientists scale the machine learning services and establish best engineering practices.
- **DevOps engineers and Site Reliability Engineers** focus on availability, reliability, and best DevOps practices - making sure that the service is up and running all the time, and if something breaks, they can quickly fix it, even if it's at night or over the weekend.

**Q: How can data engineers best support the other members of the data team? What does effective collaboration look like?**

I think I mostly answered that question during the description of the roles, but to be a bit more concrete - the best way that engineers can support others, support data analysts and data scientists and all the rest, is to **work together in one team, work on the same problem**.

Even though the focus is different, when you work on the same problem - if we work on building a service that predicts and identifies the category of a listing correctly - we want to work together as one team. Then data engineers will make sure that **all the needed data** - the data we need for analysis, the data we need for training the model - **is there**. If it's not, they usually take care of making sure that this data is available.

**Q: Are there different ways that machine learning models can be deployed in production? What are the main deployment patterns?**

I described a case when a model is running online - a data scientist develops a model, they put this inside a web service, and then machine learning engineers help them to make sure this is scalable. But sometimes we have models that we don't necessarily use in this way. Sometimes we just want to predict something once per hour or once per day. For these cases we don't need a web service.

One example could be: we have many users on our platform and we want to identify users who would be interested in particular listings. Basically, we want to advertise something to them. From all the users we have, we want to find users who are most likely to react positively to this kind of advertising.

Usually we don't need to do this in real time - it's fine if we do it once per day. Once per day we run our model, score all our users, and see that for this kind of ads these users are more likely to be interested. Then we just send emails to these users saying "hey, you might be interested in seeing this."

In this case we don't serve the models online, we do it offline. We call it **batch serving** because we do this periodically. The job of data engineers here would be to help data scientists make sure that it's possible to execute the model in such a way that it runs periodically, every day. The job of a data engineer would be to **help data scientists get the data into the model**, then the model does some prediction, and they will also **help get the predictions out of the model and save them** in such a way that this data can later be used by other services.

**Q: What's the key difference between machine learning engineers and data engineers when it comes to scaling data science models? How do their responsibilities overlap or differ?**

I think I partly answered that. In my personal opinion, this is at least the trends I see around me in the companies where I worked or in other companies - machine learning engineers mostly work on **online things**. The line is blurry, but the main difference in my opinion is that machine learning engineers focus more on online things. If we have a model and we want to serve it online so it can be used from a product, then this is what the machine learning engineer would do. If this is something we want to do offline, executed once per day, this is something that the data engineer would do.

But again, data engineers are also involved in things such as setting up Kafka, and Kafka is of course more real-time than offline. You can argue here that it's not really clear what is the difference, and yeah, in some cases there is no difference - actually both roles are doing the same job.

But one thing you can use to separate the two, in my opinion: a data engineer is **somebody who helps to prepare the data** - so it's **before the job of a data scientist**. And a machine learning engineer is somebody who is **picking up the model and doing the job after**.

But again, it's not like a wall and then a data scientist just throws a model over this wall. Of course they work together. Data engineers work together with data scientists to develop a model, and then data scientists work together with machine learning engineers to serve the model. This is just my opinion and I think opinions differ on this question. In some companies there is not really a difference.

**Q: Should data teams also include business analysts who sit between product managers and the technical data team? What value do they bring?**

Yeah, definitely, I think it's a really good idea. A business analyst - or what they called an analyst - of course, sometimes the roles are different. We have product analysts, we have data analysts, we have business analysts. Sometimes it's a different role, sometimes it's the same role, so it's difficult to draw a line here.

But I think they are pretty similar in this sense that they **help the product manager to quantify the size of a problem** and understand if this problem is actually worth solving. In some teams I know there is even no product manager - there is just a business analyst who **translates the requirements of a user to the team**. So it's also possible.

**Q: What communication and soft skills are most important for the different roles in a data team? How do these skills vary by position?**

I think the main soft skill is **communication skill** - basically being able to talk to each other and understand each other. When we work, everyone works in a team. Product managers are less technical, data engineers and machine learning engineers are more technical, and Site Reliability Engineers are even more technical, having more hardcore skills in Unix and networking.

Basically, **everyone in this team should be able to speak in the same language**. When a data scientist says something about machine learning, they need to make sure that everyone on the team understands what they are saying. Instead of going deep into saying "the gradient is exploding here" and no one understands what they talk about, they of course have to work with others and really explain what the problem is, how to address the problem, using metaphors or things like that.

For analysts, I think, probably for all the positions, **writing documentation is important**. Of course, documentation is different. For machine learning engineers or other engineers, when they write documentation, this is usually intended for other engineers. For analysts, they need to be probably better at writing in the sense that they really need to know **how to write in such a way that management understands** - the executive team understands what is the problem and what is the solution they are proposing when they are writing different reports about different things.

The more a person talks to the business side of things, to the user, the more they need to have a slightly different set of communication skills. But again, I think the most important thing is that **everyone in the team understands each other**.

**Q: How do the roles in a data team change based on team size? For example, would you typically see a machine learning engineer in a small startup team, or do they usually come in later as the company grows?**

Yeah, it really depends on the company. I think there was a trend a while ago - I'm not sure it still exists - but many people thought that they can just hire a data scientist and this data scientist would solve all the problems that the company has. Of course, that wasn't true because then they realized: okay, we probably need a data engineer, we probably need a machine learning engineer, we probably need a data analyst.

Of course, if it's just starting and it's a small company, a small team, having a **data engineer who knows a bit of machine learning is probably enough**. Or it can be a **machine learning engineer who knows how to set up the data pipelines** and things like that. Ideally, it should be **somebody who knows how to do things end-to-end**. A machine learning engineer could be that person - if that person knows how to set up a data pipeline, how to train a model, and how to serve it, then this person is an ideal candidate for a small team.

Then, of course, when the project becomes bigger, the team grows, and there are people who **specialize more in certain areas**. Of course, then it makes sense to add more people. But I don't think there is a right or wrong answer - it just depends on what the company wants to achieve and what kind of person this machine learning engineer is.

Just thinking out loud - maybe in some cases it actually makes sense to **hire a machine learning engineer as the first person in a team**. Because they are engineers, they know how to build things. It wouldn't be a problem for them to figure out how to build a data pipeline, it wouldn't be a problem for them to figure out how to serve a model. And since they are machine learning engineers, they know a bit of machine learning to train a simple model such as logistic regression or a decision tree and already start solving a business problem and **start bringing value to the company**. Then once this person can show the value in this product, in this service, then the team can start growing and add more people such as data engineers and data scientists.

**Q: Do data engineers primarily work with big data, or do they also handle smaller datasets? What determines when you need dedicated data engineering resources?**

Yeah, I think if the data is small - again, there is probably a question like how large data should be to call it **big data** - but let's say a few million events per day, or maybe even 100 million events per day, that would qualify as big data. Then, of course, you need to have a **dedicated person who is dedicated to just processing this data** because there is a lot of volume. It will not be possible for a data scientist to take care of everything, and then in this case we need a data engineer who will work on making sure that the data can be processed, the data is stored in the right format, and others can access this data.

But if it's a small company and there's not so much load - it's not a company that works with advertisement and they don't generate a lot of events per day - then potentially even a **data scientist who does not necessarily have a very strong engineering background can already develop a first prototype**.

**Q: Is there a clear distinction between full-stack machine learning developers and full-stack web developers? How do these roles differ in practice?**

Just to make sure I understood the question - the question is asking if we have different kinds of full-stack engineers. We have machine learning full-stack engineers, or full-stack data scientists who can do things end-to-end. And then we have web engineers, full-stack engineers who can do things there end-to-end.

I think we actually need the separation here because, in my opinion, when we are talking about a **full-stack engineer**, this is somebody who mostly focuses on **web**. We quickly want to create an application that users can use, such as a web application, and this is what they would do. The nature of work here is a bit different from data science, so the process is a bit different.

I think fundamentally the processes are similar, but there are some differences as well. In the case of **full-stack data scientists**, they need to focus more on **data science and backend**. In my opinion, **full-stack web developers** focus more on **frontend and a bit of backend**. I think there is not a lot of connection between these two.

But I might be wrong, and I can imagine that some companies, especially early-stage startups, where **one person can do everything** - starting from setting up a company's website to collecting the data to training the model, and then maybe even configuring Wi-Fi routers in the office. I can imagine that this can also happen. But as the company grows, there is **more and more separation**, and of course, at the end, when the company is big, we have all these different roles which we talked about today.

**Q: In smaller teams that don't have dedicated MLOps or DevOps engineers, who would typically handle these operational tasks? What's the fallback approach?**

In my opinion, it would be just an engineer. Let's say if a company already has a **backend engineer** - it could be that backend engineer. It should be possible to train that person, to explain the basics of machine learning, and they will be able to perform this job. Or, of course, at some point the company will need to hire that person or grow somebody internally into this role.

I guess we are wrapping up for today. Thank you very much for attending the session today, and looking forward to seeing you next week.

Talk to you soon. Goodbye!

