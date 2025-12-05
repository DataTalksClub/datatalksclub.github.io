---
title: "CRISP-DM Methodology for Data Science Projects: Business Understanding, Data Preparation, Modeling, Evaluation & Deployment"
short: "Processes in a Data Science Project"
season: 1
episode: 2
guests:
- alexeygrigorev
image: images/podcast/crisp-dm.jpg
ids:
  youtube: SesVTDklFYQ
  anchor: Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg
links:
  youtube: https://www.youtube.com/watch?v=SesVTDklFYQ
  anchor: https://anchor.fm/datatalksclub/episodes/Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg
  spotify: TODO
  apple: TODO

description: "Learn the CRISP-DM methodology for managing data science projects. Step-by-step guide covering business understanding, data preparation, modeling, evaluation, and deployment"
topics:
- data science
- machine learning
- project management
dateadded: 2021-02-23



keywords: CRISP-DM, data science process, machine learning methodology, data science project management, ML project lifecycle, data science workflow, A/B testing, model deployment, data science best practices, ML model evaluation, cross-functional data teams

transcript:
- line: I will start with an introduction. Thank you very much for coming to this
    event. This event is brought to you by DataTalks Club, one of our weekly events.
    We have multiple events per week of different kinds. On Tuesday we have more technical
    events such as workshops or webinars with presentations.
  sec: 0
  time: 0:00
  who: Alexey
- line: Next week we will have a talk about serverless machine learning with AWS.
    The week after that we will have a talk about a new service from AWS called AWS
    Glue DataBrew. We also have less technical events like the one today. Usually
    we host them on Friday. Last week I had to cancel and move it to today.
  sec: 21
  time: 0:21
  who: Alexey
- line: Today it is more of a discussion. It does not have slides, so it is structured
    as a conversation. We then publish this as a podcast. Today we will talk about
    processes for machine learning projects. Tomorrow we will talk about building
    a data science team.
  sec: 54
  time: 0:54
  who: Alexey
- line: Next week we have another talk about recruiting processes and how to stand
    out as a data scientist. For today we will use Slido for questions. First I will
    talk about the processes, and then you can ask questions during the conversation.
    After that I will spend some time answering them. I will send the link to the
    chat now.
  sec: 73
  time: '1:13'
  who: Alexey
- line: Please feel free to use Slido for asking your questions. Let us start. Let
    me open my notes.
  sec: 119
  time: '1:59'
  who: Alexey
- line: Thanks again for joining. Today we will talk about processes in a machine
    learning project. By processes I mean how everyone can work together in one team
    on the same project to deliver value. Last week we talked about roles in the team,
    and this topic is related.
  sec: 154
  time: '2:34'
  who: Alexey
- line: Previously we talked about the product manager. The main responsibility of
    a product manager is making sure the team is doing the right thing. Then the team
    has a data analyst whose main responsibility is understanding and explaining the
    data. We also have a data scientist whose focus is more on predicting than explaining
    and on more engineering work than a data analyst does.
  sec: 179
  time: '2:59'
  who: Alexey
- line: We also have data engineers. Data engineers make sure that analysts, data
    scientists, and everyone else have access to the data they need for analysis and
    model training. They also provide the tools to access the data. Then we have machine
    learning engineers who work together with data scientists. They take the models
    data scientists build and make sure these models are scalable and built as web
    services.
  sec: 211
  time: '3:31'
  who: Alexey
- line: Finally we have site reliability engineers, now often called MLOps engineers.
    They focus on the reliability of the solution and handle monitoring. Everyone
    in the team needs to work together. If we have a problem to solve, having a process
    is a good idea.
  sec: 239
  time: '3:59'
  who: Alexey
- line: If we do not follow a process, the project may fail. What is worse, we might
    spend a lot of time on a project that ends up failing and realize that the time
    invested was wasted because the project was not useful. A process helps us iterate
    faster. It helps us check our assumptions and ideas.
  sec: 269
  time: '4:29'
  who: Alexey
- line: It also helps us stop projects that are not promising earlier so we do not
    waste too much time on them. There are many methodologies for organizing machine
    learning projects, and they are relatively similar. Today I will talk about one
    of them called CRISP DM, which stands for Cross Industry Standard Process in Data
    Mining. It is an old methodology created by IBM in the 1990s.
  sec: 299
  time: '4:59'
  who: Alexey
- line: Back then data science was called data mining and things were different, but
    the framework still applies today with some corrections. The general process is
    still valid. A process in CRISP DM consists of six steps. The first step is business
    understanding.
  sec: 334
  time: '5:34'
  who: Alexey
- line: We want to understand the business problem, set objectives, and make sure
    the problem is worth solving. Once we have that, we move to data understanding.
    At this step we analyze the available data and decide if it is good enough. We
    then decide if we need additional data.
  sec: 360
  time: '6:00'
  who: Alexey
- line: Next we have data preparation. Once we analyze the data and see that we have
    what we need, we transform it so it can be used for a machine learning model.
    When the data is prepared in a usable form, we move to modeling. This is the step
    where we actually train the model using our favorite libraries such as scikit
    learn.
  sec: 386
  time: '6:26'
  who: Alexey
- line: After training the model we evaluate it. We check the results and see if the
    model performs according to our expectations and the objectives we defined during
    the business understanding step. Finally we have the deployment step. If the model
    meets expectations, we roll out the solution to all users.
  sec: 422
  time: '7:02'
  who: Alexey
- line: Now we will take a closer look at all the steps and see what happens in each
    one. To illustrate the process better, we will use the same example we discussed
    previously. The example is classifying the category of a listing.
  sec: 447
  time: '7:27'
  who: Alexey
- line: Imagine we have an online classified website where people sell items they
    no longer need and buy items they want. Websites like Craigslist, eBay, or Avito
    work this way. Imagine you have an iPhone and want to sell it. You go to the website,
    create a listing, and people contact you if they are interested.
  sec: 475
  time: '7:55'
  who: Alexey
- line: We want to help sellers create listings faster. To do this we want to develop
    a model that automatically suggests the right category. When you create a listing
    for an iPhone, the model should suggest the mobile phones category. We work in
    a cross functional team responsible for the posting flow.
  sec: 506
  time: '8:26'
  who: Alexey
- line: This team includes a product manager, back end and front end engineers, a
    data analyst, a data scientist, a data engineer, a machine learning engineer,
    and a site reliability engineer. All these people work together on the services
    related to the posting flow. Let us see how we can solve this problem using CRISP
    DM.
  sec: 528
  time: '8:48'
  who: Alexey
- line: The first step is business understanding. At this step we want to understand
    the problem and decide whether it is worth investing time. Usually someone comes
    to our team, often to the product manager, and asks if the team can solve a problem.
    The product manager does not immediately agree.
  sec: 562
  time: '9:22'
  who: Alexey
- line: They first need to analyze the problem. They usually say that it sounds like
    a good problem to solve and suggest thinking about it. Then together with the
    data analyst they try to quantify the size of the problem. They want to understand
    how many users are affected.
  sec: 594
  time: '9:54'
  who: Alexey
- line: They want to know how many sellers cannot finish posting an item because they
    cannot figure out the correct category. Some users simply leave the site. They
    also want to know how many items end up in the wrong category. They need a number
    that explains how big the problem is before starting to solve it.
  sec: 623
  time: '10:23'
  who: Alexey
- line: Measuring how many users cannot finish posting can be tricky. It is not always
    easy to understand why a user drops out. Was it because they could not select
    the right category or because something else happened. This requires talking to
    users and understanding the difficult steps in posting.
  sec: 658
  time: '10:58'
  who: Alexey
- line: User interviews are useful, but they are not always easy to use as a metric.
    We can also talk to the moderation team. Moderators manually inspect listings,
    accept them, or correct them. From them we can learn that about 10 percent of
    listings end up in the wrong category.
  sec: 690
  time: '11:30'
  who: Alexey
- line: This gives us a number. We also learn that moderators spend a lot of time
    moving items to the correct categories. They manually change the category so listings
    end up in the right place. We can measure the size of the problem by looking at
    the moderators' workload.
  sec: 720
  time: '12:00'
  who: Alexey
- line: For example, if moderators spend an average of 10 hours per week on this task,
    it means a quarter of their time is spent solving this manually. This is a large
    number, so we can see the problem is worth solving. We then define an objective.
  sec: 751
  time: '12:31'
  who: Alexey
- line: If we develop a model that suggests the correct category automatically, we
    want to reduce the number of hours moderators spend on manual reassignment by
    50 percent. This gives us a clear objective. Moderators would then spend four
    hours less per week on this task. They could focus on more important work.
  sec: 772
  time: '12:52'
  who: Alexey
- line: The problem is important, we can measure its size, and we have a way to measure
    success. We also want to understand if machine learning is the right tool. The
    product manager and data analyst talk to the data scientist and ask for an assessment.
  sec: 805
  time: '13:25'
  who: Alexey
- line: For this particular problem, the data scientist would confirm that machine
    learning can be used to suggest the right category. At this step the team decides
    that machine learning is appropriate. They quantify the size of the problem and
    set the objective of reducing moderator time by 50 percent.
  sec: 842
  time: '14:02'
  who: Alexey
- line: Business understanding is an important step. We want to make sure the problem
    is worth solving so that the time spent developing, training, and productionizing
    the model is justified. Often we spend time on things that are not important.
    Investing time in understanding and quantifying the problem is better.
  sec: 889
  time: '14:49'
  who: Alexey
- line: Once we have that, we move to the next step, which is data understanding.
    We want to understand what data we have available. Usually data scientists and
    data analysts work together at this stage. They look at the data, examine what
    is there, and determine what kind of data is needed for solving the problem.
  sec: 903
  time: '15:03'
  who: Alexey
- line: "For our problem we need the title of the listing, for example \u201CiPhone.\u201D\
    \ We also need the description, and ideally we would have images. We need the\
    \ correct category as well, meaning the category moderators assign when they review\
    \ the listing. They might say the listing already belongs to the correct category\
    \ or that it should be moved, and for an iPhone the correct category is mobile\
    \ phones."
  sec: 932
  time: '15:32'
  who: Alexey
- line: We look at the data and see that we have the title and the description, but
    access to images is difficult. Now we must decide if investing time into image
    access is necessary or if the available information is enough. We can talk to
    the data scientist to check whether title and description are sufficient or if
    something else is needed. Since images might not be crucial, it can be a good
    idea to continue without them and use only title and description.
  sec: 938
  time: '15:38'
  who: Alexey
- line: "If all the needed data is already in the data lake then data engineers do\
    \ not need to take further action. If some data is not accessible, for example\
    \ the moderators\u2019 decisions, then data engineers need to work with the moderation\
    \ team to make it available. They ensure this data is stored in the data lake\
    \ so we can use it for the model. Once we confirm the required data exists, we\
    \ move to the next step."
  sec: 946
  time: '15:46'
  who: Alexey
- line: The next step is data preparation, where we prepare the data for modeling.
    Data engineers ensure the data is present by building pipelines and moving data
    from the moderation team to our team. In early project stages it makes sense to
    move fast and iterate, meaning the first version of the pipeline does not need
    to be perfect. What matters is having a reliable way to get the data and use it.
    The goal here is to have all needed data easily accessible.
  sec: 960
  time: '16:00'
  who: Alexey
- line: Ideally the data is in one table with all features and the target. In our
    case the features are title and description, and the target is the correct category.
    Once we have that ready, we move to modeling.
  sec: 983
  time: '16:23'
  who: Alexey
- line: Modeling is the step where we train the model. Ideally the data is prepared
    well enough that we can simply select it from the database and feed it into the
    model. Sometimes we need extra preprocessing, such as count vectorizer or tf-idf
    vectorizer for text. We define a model evaluation metric such as accuracy, precision,
    recall, f1 or AUC. These metrics are internal data science metrics, not business
    metrics.
  sec: 995
  time: '16:35'
  who: Alexey
- line: "Often it makes sense to create a simple baseline before training a real model.\
    \ A baseline can be a set of rules, such as \u201Cif the title contains iPhone,\
    \ the category is mobile phones.\u201D We then check the accuracy of this baseline.\
    \ If the baseline is bad we may need to invest time in a more complex model, but\
    \ sometimes the baseline may be enough. The important thing is to have a way to\
    \ measure performance."
  sec: 1014
  time: '16:54'
  who: Alexey
- line: If the baseline accuracy is sufficient we can move to the evaluation step.
    Evaluation checks whether the model meets the original objective. Our objective
    was to reduce the time moderators spend adjusting categories by 50 percent. We
    now need to check if the model helps achieve that.
  sec: 1025
  time: '17:05'
  who: Alexey
- line: To evaluate, we integrate the solution and apply it to a small portion of
    traffic. For example, we take five percent of new listings and apply the model
    to them. We observe how users react and assign a few moderators to handle this
    five percent while others handle the remaining traffic. We run this for a week
    or two and measure whether our business metric improves. We check if the time
    spent on category corrections decreases by 50 percent, by 25 percent, or does
    not improve at all.
  sec: 1037
  time: '17:17'
  who: Alexey
- line: Evaluation can lead to different outcomes. One outcome is that the solution
    meets expectations and we can deploy it. Another outcome is that it does not meet
    expectations because we did not understand the problem well or the baseline was
    too simple. In that case we improve the model, retrain it and evaluate again with
    the same five percent of traffic. A third outcome is that we see no improvement
    at all, in which case we might stop the project and move to something else.
  sec: 1049
  time: '17:29'
  who: Alexey
- line: If the solution meets expectations we go to deployment. Deployment means rolling
    out the solution to all users. At this stage the focus is on engineering. We ensure
    the service is reliable and scalable under full traffic. Machine learning engineers
    and site reliability engineers work together on infrastructure, monitoring and
    alerting.
  sec: 1063
  time: '17:43'
  who: Alexey
- line: At the end of this step the model is in production. It affects all users and
    works reliably. Even if it is not a model but a heuristic, it is packaged in a
    web service and deployed. After deployment we can return to business understanding
    and decide how much we want to improve the model.
  sec: 1079
  time: '17:59'
  who: Alexey
- line: We look at the numbers again, set new objectives and iterate. After building
    a simple model, such as logistic regression, we might consider adding images.
    We then evaluate what is needed to include images in the pipeline and whether
    training an image classification model brings enough improvement.
  sec: 1096
  time: '18:16'
  who: Alexey
- line: When making these decisions we always keep the business objective in mind.
    We check whether the extra complexity is justified. We need a clear way to calculate
    return on investment. If spending additional weeks or months does not bring enough
    improvement, we work on something else.
  sec: 1103
  time: '18:23'
  who: Alexey
- line: In my experience we should start with a simple heuristic. Then we validate
    it and complete one full iteration through the process up to evaluation. If the
    heuristic meets the objective we keep it. If there is room for improvement we
    introduce simple machine learning and then iterate further.
  sec: 1114
  time: '18:34'
  who: Alexey
- line: After a few iterations with simple models we can move to more complex ones.
    We might add more features or use the heuristics themselves as features. If improvement
    is still possible we can explore deep learning models for NLP or images. This
    is appropriate only after we have a reliable baseline working in production.
  sec: 1127
  time: '18:47'
  who: Alexey
- line: Before investing in complex models we calculate return on investment. We estimate
    how much time development will take and how much value improvement might bring.
    The product manager usually handles this evaluation.
  sec: 1139
  time: '18:59'
  who: Alexey
- line: I also want to talk about data collection. When I announced this event on
    LinkedIn, Julian Martinez commented that one of the hardest aspects of machine
    learning is labeling data correctly. He added that few people talk about this.
    I agree, so I want to spend a bit more time on it.
  sec: 1152
  time: '19:12'
  who: Alexey
- line: Crisp DM may not explicitly highlight data collection, but it is part of the
    data understanding step. At this step we analyze existing data and see whether
    anything is missing. If something important is missing, we must understand how
    crucial it is. If it is essential, we need to invest time and money into collecting
    it.
  sec: 1165
  time: '19:25'
  who: Alexey
- line: We might decide to acquire new data, build better infrastructure or work with
    a third party provider for labeling. Tracking data quality is also important at
    this stage. Data analysts check whether the data is good enough to train a meaningful
    model. They check whether the model will be accurate or if poor data quality will
    harm performance.
  sec: 1178
  time: '19:38'
  who: Alexey
- line: Often we inspect data manually and correct errors. One helpful trick to detect
    incorrect labels is to train a model and apply it to the same training set. If
    the model makes mistakes on the training set, these mistakes often point to wrong
    labels. We can review these errors and manually fix the training data.
  sec: 1192
  time: '19:52'
  who: Alexey
- line: This is everything I prepared for today. If you have questions, you can use
    the link to Slido in the chat. Let me share it again. I will now share my screen
    and open Slido.
  sec: 1205
  time: '20:05'
  who: Alexey
- line: Vladimir is asking whether it is better to check the relationship between
    business metrics and data science metrics before modeling instead of doing A/B
    testing at the end. It is possible to do that, but if you have no model yet you
    cannot check this relationship. In that case the only option is to roll out a
    simple solution and see how users react. After you already have a working model,
    it makes sense to check the connection between predictive metrics and business
    metrics.
  sec: 1886
  time: '31:26'
  who: Alexey
- line: For example, if you have a recommender system with a mean average precision
    of sixty percent, you can estimate how this usually affects engagement. This requires
    an existing model. I hope this answers the question.
  sec: 1892
  time: '31:32'
  who: Alexey
- line: If you want to ask a question, go to Slido.com or use the QR code and enter
    the event code. If you have questions later, you can ask them in Slack.
  sec: 1984
  time: '33:04'
  who: Alexey
- line: Vladimir asks whether Crisp DM is used in smaller teams. The size of the team
    does not matter, and you do not have to follow Crisp DM exactly. You can adjust
    it to your needs and include additional steps if needed, such as a separate data
    collection step. Many other methodologies exist and most are similar to Crisp
    DM.
  sec: 2037
  time: '33:57'
  who: Alexey
- line: Having a process is always a good idea, especially the business understanding
    step. You do not want to spend time solving a problem that is not important. Crisp
    DM emphasizes this step well.
  sec: 2051
  time: '34:11'
  who: Alexey
- line: Do we conduct user research? Yes, of course. That is often the best way to
    understand user problems.
  sec: 2109
  time: '35:09'
  who: Alexey
- line: "Thanks for coming. I will make this video available on YouTube and also upload\
    \ it as a podcast. Tomorrow we will have another episode about building a data\
    \ science team. It starts at twelve o\u2019clock European time."
  sec: 2128
  time: '35:28'
  who: Alexey
- line: See you, and thanks for attending. Goodbye.
  sec: 2163
  time: '36:03'
  who: Alexey
---

The topic today is the processes in a data science project. We want to understand how cross-functional teams work together to ship real value. We'll use a concrete example (auto-categorizing marketplace listings) and walk through CRISP-DM step by step.

We covered:
- [Why Processes Matter](#why-processes-matter)
- [CRISP-DM Methodology](#crisp-dm-methodology)
- [Example Use Case](#example-use-case)
- [Step 1: Business Understanding](#step-1-business-understanding)
- [Step 2: Data Understanding](#step-2-data-understanding)
- [Step 3: Data Preparation](#step-3-data-preparation)
- [Step 4: Modeling](#step-4-modeling)
- [Step 5: Evaluation](#step-5-evaluation)
- [Step 6: Deployment](#step-6-deployment)
- [Iteration and Continuous Improvement](#iteration-and-continuous-improvement)
- [Best Practices](#best-practices)
- [Data Collection and Quality](#data-collection-and-quality)
- [Q&A from the Audience](#qa-from-the-audience)

**Q: Can you remind us about the different roles that typically exist in a data science team and how they work together?**

**Product managers** make sure the team is doing the right thing.

**Data analysts** understand and explain the data.

**Data scientists** focus more on predicting than explaining, and are more engineering-focused than data analysts.

**Data engineers** ensure that analysts, data scientists, and everyone else have access to the data and tools they need for analysis and model training.

**Machine learning engineers** work with data scientists to take their models and make them scalable and production-ready as web services.

**Site reliability engineers** (now often called MLOps engineers) focus on reliability, monitoring, and operational aspects of the solution.

## Why Processes Matter

**Q: Why is having a structured process important for machine learning projects? What problems can it help avoid?**

Everyone in a team needs to work together. Without a process, projects may fail—or worse, you can spend months building something only to discover it wasn't useful.

With a process, you can iterate faster, ensure you're solving the right problem, validate your assumptions, and kill unpromising projects early without wasting time.

## CRISP-DM Methodology

**Q: What methodology will you be discussing today, and why did you choose this particular framework?**

There are many methodologies for organizing machine learning projects. Today I'll talk about CRISP-DM, which stands for Cross-Industry Standard Process in Data Mining. Created by IBM in the 90s when data science was called data mining, this framework surprisingly still applies to modern data science projects.

**Q: What are the main steps in the CRISP-DM methodology, and what does each step involve?**

CRISP-DM consists of six steps:

1. **Business Understanding** - Understand the business problem, set objectives, and ensure the problem is worth solving.

2. **Data Understanding** - Analyze available data and decide if it's good enough or if you need new data.

3. **Data Preparation** - Transform the data into a format usable for machine learning models.

4. **Modeling** - Train the model using libraries like scikit-learn.

5. **Evaluation** - Check if the model performs according to your objectives from the business understanding step.

6. **Deployment** - If the model meets expectations, roll out the solution to all users.

## Example Use Case

**Q: Can you give us a concrete example to illustrate how these CRISP-DM steps work in practice?**

We'll use an example of classifying listing categories. Imagine an online classified website like Craigslist, eBay, or Avito where people sell and buy items. When you want to sell an iPhone, you create a listing, and interested buyers contact you.

**Q: What specific problem are we trying to solve in this example?**

We want to help sellers create listings faster by developing a model that automatically suggests the right category. When you create an iPhone listing, it suggests "mobile phones" as the category.

**Q: What does the team composition look like for this particular project?**

We have a cross-functional team responsible for the posting flow. The team includes a product manager, back-end and front-end engineers, a data analyst, a data scientist, a data engineer, a machine learning engineer, and a site reliability engineer.

## Step 1: Business Understanding

**Q: How does the business understanding step work in practice? What does this process look like?**

When someone brings a problem to the team, the product manager doesn't immediately commit. First, they analyze whether it's worth solving. Together with data analysts, they quantify the size of the problem.

**Q: What specific questions need to be answered during the business understanding phase?**

- How many users complain about this problem?
- How many sellers cannot finish posting because they can't figure out the correct category?
- How many items end up in the wrong category?

We need numbers to explain how big the problem is before jumping into solving it.

**Q: How do you actually measure something like user drop-off or category misclassification? What are the practical challenges?**

Measuring user drop-off is tricky because it's hard to understand why users stop—was it the category selection or something else? User interviews help, but they don't easily translate into metrics.

**Q: How did you actually quantify this problem in your example? What data did you use?**

We talked to the moderation team—people who manually inspect listings and correct them. They told us that 10% of listings end up in the wrong category, and they spend 10 hours per week (25% of their time) manually fixing categories. This is a significant problem worth solving.

**Q: Once you have quantified the problem with numbers, what are the next steps in the business understanding phase?**

We need to set an objective. In this case: reduce the time moderators spend manually reassigning categories by 50%. This means moderators will save 5 hours per week and can focus on more important work.

We now have:
- A way to measure the problem size
- A way to measure success
- Clear direction on whether we're moving in the right direction

**Q: Do you validate whether machine learning is actually the right approach to solve this problem?**

Yes. The PM and data analysts consult with data scientists to confirm that machine learning can solve this problem. For this case, machine learning can indeed suggest the right category for a listing.

**Q: Why is the business understanding step so crucial? What happens if you skip it or rush through it?**

This step ensures the problem is worth solving before investing time in development, training, and productionization. Many teams waste time on unimportant problems. Investing more time upfront in understanding and quantifying the problem prevents this.

## Step 2: Data Understanding

**Q: What happens in the data understanding step? What activities does the team focus on?**

Data scientists and data analysts work together to understand what data is available and what's needed to solve the problem.

**Q: What specific data do we need for the listing categorization example? What sources should we consider?**

We need:
- Listing title (e.g., "iPhone")
- Description
- Images (potentially)
- Correct category (from moderator decisions)

**Q: What do you do if some required data is missing or difficult to access? How do you make decisions about data availability?**

We found that we have title and description, but images are difficult to access. We need to decide whether to invest time getting images or proceed without them. After consulting with data scientists, we determine that title and description are sufficient, so we proceed without images.

**Q: What role do data engineers play in the data understanding step?**

If all data is in our data lake, data engineers don't need to do anything. If some data isn't accessible (like moderator decisions), data engineers work with other teams to ensure the data is available in our data lake.

## Step 3: Data Preparation

**Q: What happens in the data preparation step? What activities are involved?**

Data engineers prepare the data by setting up pipelines to move data from other teams (like the moderation team) into our data lake.

**Q: How polished and complete does the data pipeline need to be when you first start? What is the initial approach?**

When starting a project, iterate quickly. The pipeline doesn't need to be perfect—just good enough to get data from other teams.

The goal is to have data easily accessible, ideally in a single table with all features and the target. In our case: features are title and description, target is the correct category.

## Step 4: Modeling

**Q: What happens in the modeling step? What is the typical workflow?**

Train a model. Ideally, the data is prepared so you can do a simple database select and feed it directly into `model.fit`. For text data, apply preprocessing like CountVectorizer or TF-IDF Vectorizer.

**Q: What metrics do you use to evaluate your models during the modeling step?**

Define model evaluation metrics like accuracy, precision, recall, F1, or AUC. These are internal data science metrics, not business metrics.

**Q: Should you start with a complex model, or is there a better approach for the initial modeling phase?**

Start with a simple baseline first—even just rules like "if 'iPhone' is in the title, then category is mobile phones." Check the accuracy. If it's good enough, proceed to evaluation. If not, train a slightly more complex model. The key is having a way to measure performance.

## Step 5: Evaluation

**Q: What happens in the evaluation step? How do you test whether the model meets your objectives?**

Check if the model meets the objective we set. In our example: does it reduce moderator time by 50%?

**Q: How do you test the model in a production environment? What is the testing strategy?**

Test on a small portion of traffic (e.g., 5% of listings). Assign a couple of moderators to work only with this traffic, while the rest handle the remaining 95%. Run for one to two weeks and measure whether you hit your target—50%, 25%, or no reduction at all.

**Q: What are the possible outcomes of the evaluation step, and how do you respond to each scenario?**

Three possible outcomes:

1. **Meets expectations** - Deploy it.

2. **Doesn't meet expectations** - The heuristic or model needs improvement. Train a better model (e.g., using scikit-learn), redeploy, and evaluate again on 5% of traffic.

3. **Doesn't move the metric at all** - Stop the project and move on to something else.

## Step 6: Deployment

**Q: What happens in the deployment step? What are the key activities and considerations?**

If the solution meets expectations, roll it out to all users (100% of traffic).

**Q: What do you need to focus on during the deployment phase? What are the priorities?**

Focus on engineering: ensure the service is reliable and scalable at 100% traffic. Machine learning engineers and site reliability engineers handle infrastructure, monitoring, and alerting.

**Q: What does success look like after deployment? How do you measure it?**

The model is in production, affecting all users reliably. Even if it's just a heuristic, it's packaged as a web service and deployed.

## Iteration and Continuous Improvement

**Q: What happens after deployment? Is this the end of the project, or is there more work to do?**

Go back to business understanding and decide how much to improve the model. Set a new objective and iterate. For example, once you have a simple logistic regression model, consider adding images and training an image classification model for better predictions.

**Q: How do you decide whether to add complexity to your model or keep iterating? What factors influence this decision?**

Always keep the business objective in mind. Before adding complexity (like image classification), calculate the return on investment. Will spending weeks or months on this bring enough improvement? If not, work on something else—what you have may already be valuable enough.

## Best Practices

**Q: What is your recommended approach for following the CRISP-DM methodology? What are the key principles?**

1. Start with a simple heuristic (rules, counters)
2. Validate it works and brings value through one full iteration
3. If the objective is met, great! If there's room for improvement, add complexity
4. Add proper machine learning, more features, or use heuristics as features
5. After iterating with simple models, try complex models (NLP, deep learning) only if needed
6. Calculate ROI before investing in complex models—usually the PM handles this

## Data Collection and Quality

**Q: Why is data collection such an important aspect of data science projects, and why is it often overlooked?**

Julián Martínez noted that one of the hardest aspects in machine learning is labeling data correctly, and few people talk about this. It's an often overlooked but critical topic.

**Q: Does the CRISP-DM methodology specifically address data collection, and where does it fit in the process?**

Yes, it's part of the data understanding step. We analyze what data we have and what's missing. If something crucial is missing, invest time and money in collecting it—either by building better infrastructure or working with third-party providers for labeling.

**Q: How do you ensure data quality throughout the project? What strategies and tools do you use?**

Data analysts typically check data quality to see if it's possible to build a sensible model. 

One useful trick: train a model and apply it to the training set. When the model makes mistakes, it's often because the training data is incorrect. Identify these cases and manually fix them.

## Q&A from the Audience

**Q: Isn't it better to establish the relationship between business metrics and data science metrics before modeling, rather than discovering this through A/B testing at the end?**

Yes, but if you don't have a model yet and want to start quickly, you need to roll out something simple to test if business metrics move. Once you have a running model and want to improve it, you can link data science metrics to business metrics.

For example, with a recommender system, if mean average precision is 60%, you can try to correlate that with a business metric like user engagement. This is possible once you have a running model.

**Q: Is the CRISP-DM methodology practical for smaller teams, or is it mainly for larger organizations?**

Team size doesn't matter. You don't have to follow CRISP-DM by the letter—adjust it to your needs. If you want a dedicated data collection step, add it. There are many similar methodologies you can find by Googling "machine learning processes."

Having a process is always a good idea, especially the business understanding step, because you don't want to spend time solving unimportant problems. The emphasis on business understanding is what makes these processes valuable.

**Q: Do you typically conduct A/B tests as part of the CRISP-DM process, and when are they most valuable?**

Yes, A/B tests are the best way to evaluate models in production.

