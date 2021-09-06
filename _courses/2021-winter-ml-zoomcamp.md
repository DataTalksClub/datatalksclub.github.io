---

title: Machine Learning Zoomcamp (2021) 
description: Learn machine learning engineering in 4 months in a free online course
image: images/courses/zoomcamp.jpg
layout: page


schedule:
  - title: "Introduction to Machine Learning"
    subtitle: "Course overview and logistics"
    start: 2021-09-06 17:00:00
    content:
      - Understanding machine learning and the problems it can solve    
      - "CRISP-DM: Organizing a successful machine learning project"
      - Setting up the environment 
      - Quick introduction to Python, Numpy, Linear algebra and Pandas
    link: https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/01-intro
    homework:
      content:
        - point 1
      due: 2021-09-12 12:00:00
  - title: "Machine Learning for Regression"
    subtitle: "Predicting the price of a car"
    start: 2021-09-13 17:00:00
    content:
      - "Creating a car-price prediction project with a linear regression model"
      - "Doing an initial exploratory data analysis with Jupyter notebooks"
      - "Setting up a validation framework"
      - "Implementing the linear regression model from scratch"
      - "Evaluating the model: using RMSE"
      - "Performing simple feature engineering for the model"
      - "Keeping the model under control with regularization"
    homework:
      content:
        - House price prediction
      due: 2021-09-12 12:00:00
  - title: "Machine Learning for Classification"
    subtitle: "Predicting churning users"
    start: 2021-09-20 17:00:00
    content:
      - Predicting customers who will churn with logistic regression
      - Doing exploratory data analysis for identifying important features
      - Encoding categorical variables to use them in machine learning models
      - Using logistic regression for classification
    homework:
      content:
        - point 1
        - point 2
      due: 2021-09-29 12:00:00
  - title: "Evaluation Metrics for Classification"
    subtitle: "Evaluating the churn prediction model"
    start: 2021-09-27 17:00:00
    content:
      - Accuracy as a way of evaluating binary classification models and its limitations
      - Determining where our model makes mistakes using a confusion table
      - Deriving other metrics like precision and recall from the confusion table
      - Using ROC and AUC to further understand the performance of a binary classification model
      - Cross-validating a model to make sure it behaves optimally
      - Tuning the parameters of a model to achieve the best predictive performance
    homework:
      content:
        - point 1
        - point 2
      due: 2021-10-06 12:00:00
  - title: "Deploying Machine Learning Models"
    subtitle: "Deploying the churn prediction model"
    start: 2021-10-04 17:00:00
    content:
      - Saving models with Pickle
      - Serving models with Flask
      - Managing dependencies with Pipenv
      - Making the service self-contained with Docker
      - Deploying it to the cloud using AWS Elastic Beanstalk
    homework:
      content:
        - point 1
        - point 2
      due: 2021-10-13 12:00:00
  - title: "Decision Trees and Ensemble Learning"
    subtitle: "Credit risk scoring project"
    start: 2021-10-11 17:00:00
    content:
      - "Predicting the risk of default with tree-based models"
      - "Decision trees and the decision tree learning algorithm"
      - "Random forest: putting multiple trees together into one model"
      - "Gradient boosting as an alternative way of combining decision trees"
    homework:
      content:
        - point 1
        - point 2
      due: 2021-10-20 12:00:00
  - title: "Midterm Project"
    subtitle: "Implement a project end-to-end"
    start: 2021-10-18 17:00:00
    content:
      - Finding a problem and a dataset
      - EDA and data cleaning
      - Selecting the best model
      - Deploying this model as a web service
    homework:
      content:
        - point 1
        - point 2
      due: 2021-10-31 12:00:00
  - title: "Neural Networks and Deep Learning"
    subtitle: "Classifying the images of clothes"
    start: 2021-11-01 17:00:00
    content:
      - "Convolutional neural networks for image classification"
      - "TensorFlow and Keras: frameworks for building neural networks"
      - "Using pre-trained neural networks"
      - "Internals of a convolutional neural network"
      - "Training a model with transfer learning"
      - "Data augmentations: the process of generating more training data"
    homework:
      content:
        - TODO
      due: 2021-09-12 12:00:00
  - title: "Serverless Deep Learning"
    subtitle: "Serving the clothes classification model with AWS Lambda"
    start: 2021-11-08 17:00:00
    content:
      - "Serving models with TensorFlow-Lite"
      - "Deploying deep learning models with AWS Lambda"
      - "Exposing the Lambda function as a web service via API Gateway"
    homework:
      content:
        - TODO
        - TODO
      due: 2021-09-12 12:00:00
  - title: "Kubernetes and TensorFlow-Serving"
    subtitle: "Serving the clothes classification model with Kubernetes and TensorFlow-Serving"
    start: 2021-11-15 17:00:00
    content:
      - Understanding different methods of deploying and serving models in the cloud.
      - Serving Keras and TensorFlow models with TensorFlow-Serving
      - Deploying TensorFlow-Serving to Kubernetes
    homework:
      content:
        - TODO
        - TODO
      due: 2021-09-12 12:00:00
  - title: "Kubeflow and KFServing"
    subtitle: "Serving the clothes classification model with KFServing"
    start: 2021-11-22 17:00:00
    content:
      - Using Kubeflow and KFServing for simplifying the deployment process
    homework:
      content:
        - TODO
        - TODO
      due: 2021-09-12 12:00:00
  - title: "Capstone Project"
    subtitle: "Do a project end-to-end"
    start: 2021-11-22 17:00:00
    content:
      - Finding a problem and a dataset
      - EDA and data cleaning
      - Selecting the best model
      - Deploying this model as a web service
    homework:
      content:
        - TODO
        - TODO
      due: 2021-12-12 12:00:00
  - title: "Article"
    subtitle: "Teach us something"
    start: 2021-11-22 17:00:00
    content:
      - Do some research about a topic that wasn’t covered in the course and write an article about it (with code!)
    homework:
      content:
        - TODO
        - TODO
      due: 2021-12-26 12:00:00


team:
  - name: alexeygrigorev
    role: Instructor
  - name: dmitrymuzalevskiy
    role: Teaching Assistant
  - name: wendymak
    role: Teaching Assistant

faq:
  - Q: Is it going to be live? When?
    A: It is, on Mondays at 17:00 CET.
  - Q: Will it be recorded?
    A: Yes, everything will be recorded and you can watch the recording when it's convenient for you.
  - Q: What if I miss a session?
    A: The sessions are recorded, and you can ask questions in Slack.
  - Q: How much theory will you cover?
    A: The bare minimum. The focus is more on practice, and we'll cover the theory only on the intuitive level.
      E.g. we won't derive the gradient update rule for logistic regression (there are other great courses for that),
      but we'll cover how to use logistic regression and make sense of the results.
  - Q: I don't know math. Can I take the course?
    A: Yes! We'll cover some linear algebra in the course, but in general, there will be very few formulas, mostly code.
  - Q: How long will the sessions be?
    A: Not longer than one hour each.
  - Q: I filled the form, but haven't received a confirmation email. Is it normal?
    A: Yes. We process the sign-ups once per week. To make sure you don't miss anything,
       join the <a href="https://app.slack.com/client/T01ATQK62F8/C0288NJ5XSA" target="_blank"><code>#course-ml-zoomcamp</code></a>
       channel.


partners:
  # - name: DPhi
  #   link: https://dphi.tech/
  #   image: "/images/partners/dphi.png"
  - name: "Confetti"
    link: https://www.confetti.ai/
    image: "/images/partners/confetti.png"
  - name: MLOps.community
    link: https://mlops.community/
    image: "/images/partners/mlops-community.jpg"

---

# Machine Learning Zoomcamp

Learn machine learning engineering in 4 months (September 2021 &ndash; December 2021). Online and free!

<center>
<a href="https://airtable.com/shr6Gz46UZCgJ9l6w" target="_blank" class="btn btn-secondary btn-lg my-3">
<i class="fas fa-rocket"></i>
Register here</a>
</center>

Plan:

<ul>
{% for session in page.schedule %}
  <li><a href="#{{ session.title | slugify }}">{{ session.title }}</a> ({{ session.start | date: "%d %B %Y" }})</li>
{% endfor %}
</ul>

<center>
<a href="https://ctt.ac/XZ6b9" target="_blank" class="btn btn-secondary btn-lg my-3">
<i class="fab fa-twitter"></i>
Tweet about it!</a>
</center>


Logistics:

* Each week, there’s a lecture and a homework assignment.
* We have two projects: in the middle of the class and a capstone project at the end. Those who complete these two projects get a certificate.
* For homework, projects and other activities, you’ll get scores. At the end, we’ll publish the list of top 100 participants on our website.

The schedule and the plan are work in progress.


{% for session in page.schedule %}
  <h3 id="{{ session.title | slugify }}">{{ session.title }}</h3>
  {{ session.subtitle }} &ndash; <span class="datetime grey-text">{{ session.start | date: "%A, %d %B at %H:%M" }} CET</span>

  <ul>
  {% for item in session.content %}
    <li>{{ item }}</li>
  {% endfor %}  
  </ul>

  {% if session.link %}<a href="{{ session.link }}" target="_blank">Lession materials</a>{% endif %}
{% endfor %}

Don't forget to [register in Slack](/slack.html){:target="_blank"} and join [#course-ml-zoomcamp](https://app.slack.com/client/T01ATQK62F8/C0288NJ5XSA){:target="_blank"} channel.


&nbsp;

<center>
<a href="https://airtable.com/shr6Gz46UZCgJ9l6w" target="_blank" class="btn btn-secondary btn-lg my-3">Register here</a>
</center>

&nbsp;


## Team

<div class="row" style="justify-content: center;">
{% for teacher in page.team %}
  {% assign teacher_info = site.people | where: "short", teacher.name | first %}
  <div class="teacher-wrap col-md-3 text-center">
    <div class="talk-speaker-img-container">
      <img class="talk-speaker-img" src="/{{ teacher_info.picture }}" />
    </div>
    <div class="teacher-info">
      <p><a href="/people/{{ teacher.name }}.html" target="_blank">{{ teacher_info.title }}</a></p>
      <p><span class="grey-text">{{ teacher.role }}</span></p>
    </div>
  </div>
{% endfor %}
</div>


&nbsp;

<h2 id="faq">FAQ</h2>

{% for qa in page.faq %}
<p class="mb-3">
  <b>Question:</b> {{ qa.Q }}<br/>
  <b>Answer:</b> {{ qa.A }}
</p>
{% endfor %}

&nbsp;

<center>
<a href="https://airtable.com/shr6Gz46UZCgJ9l6w" target="_blank" class="btn btn-secondary btn-lg my-3">Register here</a>
</center>


&nbsp;

## Course community partners

<div class="text-center row justify-content-center">
{% for partner in page.partners %}
  <div class="my-3 col-md-6" style="display: flex">
    <a href="{{ partner.link }}" style="margin: auto" target="_blank">
      <img src="{{ partner.image }}" class="partner"/>
    </a>
  </div>
{% endfor %}
</div>

Thank you for your support!


