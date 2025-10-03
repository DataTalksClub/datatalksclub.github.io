---
title: "Processes in a Data Science Project"
short: "Processes in a Data Science Project"
guests: [alexeygrigorev]

image: images/podcast/s01e02-processes.jpg

season: 1
episode: 2

ids:
  youtube: SesVTDklFYQ
  anchor: Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg

links:
  youtube: https://www.youtube.com/watch?v=SesVTDklFYQ
  anchor: https://anchor.fm/datatalksclub/episodes/Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg
  spotify: TODO
  apple: TODO
---

## Introduction

Today we'll talk about processes for machine learning projects.

## Team Roles Recap

**What do you mean by "processes" in a machine learning project?**

By processes I mean how everyone can work together in one team on the same project to deliver value. Last week we talked about roles in the team, and this talk is related. Let me quickly recap.

**Can you remind us about the different roles in a data science team?**

**Product managers** make sure the team is doing the right thing.

**Data analysts** understand and explain the data.

**Data scientists** focus more on predicting than explaining, and are more engineering-focused than data analysts.

**Data engineers** ensure that analysts, data scientists, and everyone else have access to the data and tools they need for analysis and model training.

**Machine learning engineers** work with data scientists to take their models and make them scalable and production-ready as web services.

**Site reliability engineers** (now often called MLOps engineers) focus on reliability, monitoring, and operational aspects of the solution.

## Why Processes Matter

**Why is having a process important for machine learning projects?**

Everyone in a team needs to work together. Without a process, projects may fail—or worse, you can spend months building something only to discover it wasn't useful.

With a process, you can iterate faster, ensure you're solving the right problem, validate your assumptions, and kill unpromising projects early without wasting time.

## CRISP-DM Methodology

**What methodology will you discuss today?**

There are many methodologies for organizing machine learning projects. Today I'll talk about CRISP-DM, which stands for Cross-Industry Standard Process in Data Mining. Created by IBM in the 90s when data science was called data mining, this framework surprisingly still applies to modern data science projects.

**What are the main steps in CRISP-DM?**

CRISP-DM consists of six steps:

1. **Business Understanding** - Understand the business problem, set objectives, and ensure the problem is worth solving.

2. **Data Understanding** - Analyze available data and decide if it's good enough or if you need new data.

3. **Data Preparation** - Transform the data into a format usable for machine learning models.

4. **Modeling** - Train the model using libraries like scikit-learn.

5. **Evaluation** - Check if the model performs according to your objectives from the business understanding step.

6. **Deployment** - If the model meets expectations, roll out the solution to all users.

## Example Use Case

**Can you give us a concrete example to illustrate these steps?**

We'll use an example of classifying listing categories. Imagine an online classified website like Craigslist, eBay, or Avito where people sell and buy items. When you want to sell an iPhone, you create a listing, and interested buyers contact you.

**What problem are we trying to solve?**

We want to help sellers create listings faster by developing a model that automatically suggests the right category. When you create an iPhone listing, it suggests "mobile phones" as the category.

**What does the team look like for this project?**

We have a cross-functional team responsible for the posting flow. The team includes a product manager, back-end and front-end engineers, a data analyst, a data scientist, a data engineer, a machine learning engineer, and a site reliability engineer.

## Step 1: Business Understanding

**How does business understanding work in practice?**

When someone brings a problem to the team, the product manager doesn't immediately commit. First, they analyze whether it's worth solving. Together with data analysts, they quantify the size of the problem.

**What questions need to be answered?**

- How many users complain about this problem?
- How many sellers cannot finish posting because they can't figure out the correct category?
- How many items end up in the wrong category?

We need numbers to explain how big the problem is before jumping into solving it.

**How do you measure something like that?**

Measuring user drop-off is tricky because it's hard to understand why users stop—was it the category selection or something else? User interviews help, but they don't easily translate into metrics.

**How did you quantify the problem?**

We talked to the moderation team—people who manually inspect listings and correct them. They told us that 10% of listings end up in the wrong category, and they spend 10 hours per week (25% of their time) manually fixing categories. This is a significant problem worth solving.

**Once you have the numbers, what's next?**

We need to set an objective. In this case: reduce the time moderators spend manually reassigning categories by 50%. This means moderators will save 5 hours per week and can focus on more important work.

We now have:
- A way to measure the problem size
- A way to measure success
- Clear direction on whether we're moving in the right direction

**Do you validate that machine learning is the right approach?**

Yes. The PM and data analysts consult with data scientists to confirm that machine learning can solve this problem. For this case, machine learning can indeed suggest the right category for a listing.

**Why is business understanding such an important step?**

This step ensures the problem is worth solving before investing time in development, training, and productionization. Many teams waste time on unimportant problems. Investing more time upfront in understanding and quantifying the problem prevents this.

## Step 2: Data Understanding

**What happens in the data understanding step?**

Data scientists and data analysts work together to understand what data is available and what's needed to solve the problem.

**What data do we need for the listing categorization example?**

We need:
- Listing title (e.g., "iPhone")
- Description
- Images (potentially)
- Correct category (from moderator decisions)

**What if some data is missing or hard to access?**

We found that we have title and description, but images are difficult to access. We need to decide whether to invest time getting images or proceed without them. After consulting with data scientists, we determine that title and description are sufficient, so we proceed without images.

**What role do data engineers play?**

If all data is in our data lake, data engineers don't need to do anything. If some data isn't accessible (like moderator decisions), data engineers work with other teams to ensure the data is available in our data lake.

## Step 3: Data Preparation

**What happens in the data preparation step?**

Data engineers prepare the data by setting up pipelines to move data from other teams (like the moderation team) into our data lake.

**How polished does the data pipeline need to be at first?**

When starting a project, iterate quickly. The pipeline doesn't need to be perfect—just good enough to get data from other teams.

The goal is to have data easily accessible, ideally in a single table with all features and the target. In our case: features are title and description, target is the correct category.

## Step 4: Modeling

**What happens in the modeling step?**

Train a model. Ideally, the data is prepared so you can do a simple database select and feed it directly into `model.fit`. For text data, apply preprocessing like CountVectorizer or TF-IDF Vectorizer.

**What metrics do you use?**

Define model evaluation metrics like accuracy, precision, recall, F1, or AUC. These are internal data science metrics, not business metrics.

**Should you start with a complex model?**

Start with a simple baseline first—even just rules like "if 'iPhone' is in the title, then category is mobile phones." Check the accuracy. If it's good enough, proceed to evaluation. If not, train a slightly more complex model. The key is having a way to measure performance.

## Step 5: Evaluation

**What happens in the evaluation step?**

Check if the model meets the objective we set. In our example: does it reduce moderator time by 50%?

**How do you test the model in production?**

Test on a small portion of traffic (e.g., 5% of listings). Assign a couple of moderators to work only with this traffic, while the rest handle the remaining 95%. Run for one to two weeks and measure whether you hit your target—50%, 25%, or no reduction at all.

**What are the possible outcomes?**

Three possible outcomes:

1. **Meets expectations** - Deploy it.

2. **Doesn't meet expectations** - The heuristic or model needs improvement. Train a better model (e.g., using scikit-learn), redeploy, and evaluate again on 5% of traffic.

3. **Doesn't move the metric at all** - Stop the project and move on to something else.

## Step 6: Deployment

**What happens in the deployment step?**

If the solution meets expectations, roll it out to all users (100% of traffic).

**What do you need to focus on?**

Focus on engineering: ensure the service is reliable and scalable at 100% traffic. Machine learning engineers and site reliability engineers handle infrastructure, monitoring, and alerting.

**What does success look like?**

The model is in production, affecting all users reliably. Even if it's just a heuristic, it's packaged as a web service and deployed.

## Iteration and Continuous Improvement

**What happens after deployment?**

Go back to business understanding and decide how much to improve the model. Set a new objective and iterate. For example, once you have a simple logistic regression model, consider adding images and training an image classification model for better predictions.

**How do you decide whether to add complexity?**

Always keep the business objective in mind. Before adding complexity (like image classification), calculate the return on investment. Will spending weeks or months on this bring enough improvement? If not, work on something else—what you have may already be valuable enough.

## Best Practices

**What's your recommended approach?**

1. Start with a simple heuristic (rules, counters)
2. Validate it works and brings value through one full iteration
3. If the objective is met, great! If there's room for improvement, add complexity
4. Add proper machine learning, more features, or use heuristics as features
5. After iterating with simple models, try complex models (NLP, deep learning) only if needed
6. Calculate ROI before investing in complex models—usually the PM handles this

## Data Collection and Quality

**Why is data collection important?**

Julián Martínez noted that one of the hardest aspects in machine learning is labeling data correctly, and few people talk about this. It's an often overlooked but critical topic.

**Does CRISP-DM include data collection?**

Yes, it's part of the data understanding step. We analyze what data we have and what's missing. If something crucial is missing, invest time and money in collecting it—either by building better infrastructure or working with third-party providers for labeling.

**How do you ensure data quality?**

Data analysts typically check data quality to see if it's possible to build a sensible model. 

One useful trick: train a model and apply it to the training set. When the model makes mistakes, it's often because the training data is incorrect. Identify these cases and manually fix them.

## Q&A

**Question from Vladimir:** Isn't it better to check the relationship between business metric and data science metric before modeling rather than doing A/B testing in the end?

Yes, but if you don't have a model yet and want to start quickly, you need to roll out something simple to test if business metrics move. Once you have a running model and want to improve it, you can link data science metrics to business metrics.

For example, with a recommender system, if mean average precision is 60%, you can try to correlate that with a business metric like user engagement. This is possible once you have a running model.

**Question from Vladimir:** Is CRISP-DM used in smaller teams?

Team size doesn't matter. You don't have to follow CRISP-DM by the letter—adjust it to your needs. If you want a dedicated data collection step, add it. There are many similar methodologies you can find by Googling "machine learning processes."

Having a process is always a good idea, especially the business understanding step, because you don't want to spend time solving unimportant problems. The emphasis on business understanding is what makes these processes valuable.

**Question:** Do we conduct A/B tests?

Yes, A/B tests are the best way to evaluate models in production.

