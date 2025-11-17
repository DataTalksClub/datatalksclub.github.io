---
title: 'CRISP-DM Methodology for Data Science Projects: Business Understanding, Data Preparation, Modeling, Evaluation & Deployment'
short: Processes in a Data Science Project
season: 1
episode: 2
guests:
- alexeygrigorev
image: images/podcast/s01e02-processes.jpg
ids:
  youtube: SesVTDklFYQ
  anchor: Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg
links:
  youtube: https://www.youtube.com/watch?v=SesVTDklFYQ
  anchor: https://anchor.fm/datatalksclub/episodes/Processes-in-a-Data-Science-Project---Alexey-Grigorev-encdlg
  spotify: TODO
  apple: TODO

description: Learn the CRISP-DM methodology for managing data science projects. Step-by-step guide covering business understanding, data preparation, modeling, evaluation, and deployment
topics:
- data science
- machine learning
- project management
dateadded: 2021-02-23



keywords: CRISP-DM, data science process, machine learning methodology, data science project management, ML project lifecycle, data science workflow, A/B testing, model deployment, data science best practices, ML model evaluation, cross-functional data teams
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

