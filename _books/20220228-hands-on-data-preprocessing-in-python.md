---
authors:
- royjafari
cover: images/books/20220228-hands-on-data-preprocessing-in-python/cover.jpg
description: Book of the Week. Hands-On Data Preprocessing in Python by Roy Jafari
end: 2022-03-04 23:59:59
image: images/books/20220228-hands-on-data-preprocessing-in-python/preview.jpg
links:
- link: https://packtpub.com/product/hands-on-data-preprocessing-in-python/9781801072137
  text: Book's page
- link: https://www.amazon.com/Hands-Data-Preprocessing-Python-effectively-ebook/dp/B09F6R8V2L/ref=sr_1_1?dchild=1&keywords=Hands-On+Data+Preprocessing+in+Python&qid=1634537236&sr=8-1
  text: Buy on Amazon
- link: https://github.com/PacktPublishing/Hands-On-Data-Preprocessing-in-Python
  text: GitHub repository
start: 2022-02-28 00:00:00
title: Hands-On Data Preprocessing in Python

archive:
- name: GerryK
  text: Hi Roy Jafari, are the tools /techniques referred in the book applied for
    big data?
  replies:
  - name: Roy Jafari
    text: 'Hi GerryK! Great question. Thank you for asking it.

      The answer is yes and no.

      Yes, from the perspective that only python programming with the use of NumPy
      and pandas are covered in this book. As you know, being able to prepare, and
      analyze data using programing is the very first step in being able to deal with
      big data.

      No, from the perspective that the book does not cover computational optimization,
      parallel processing, or big data module such as Spark.'
- name: Carlos Orjuela
  text: Hi Roy Jafari, I saw part 2 is dedicated to prediction, classification models
    and clustering. How broad is the book's coverage on these topics and to what extent
    can it be used in place of others? Thank you!
  replies:
  - name: Roy Jafari
    text: 'Hi Carlos Orjuela! That''s an excellent question. I am glad you''ve provided
      a chance for me to address that.

      The second part of the book consisting of four chapters data visualization,
      prediction, classification, clustering analysis is not presented as a comprehensive
      introduction of these techniques. For instance, for classification and prediction,
      hyperparameter tuning which is a very important part of learning classification
      is not covered.

      Then what are the goals of this chapter? This content is provided to support
      the third part of the book: the preprocessing. One needs to know how the data
      will be used at the analytic stage for them to be able to effectively preprocess
      it. The simplest example is that if one needs to use clustering algorithms on
      their data, and if one understands that the clustering algorithm works by calculating
      the distances between the data objects, the requirement of normalizing the data
      before applying clustering algorithms will naturally come to them.'
  - name: Carlos Orjuela
    text: Great explanation. Thanks Roy Jafari!
- name: Roy Jafari
  text: 'Thank you Francis Terence Amit and Alexey Grigorev for the introduction and
    the opportunity. Also, I would like to thank GerryK and Carlos Orjuela for starting
    us off with great questions. Thank you!

    I am very excited to be here and for this opportunity to answer questions. Please
    don''t hold back any questions. Fire away!

    Looking forward to answering your questions.'
  replies: []
- name: Clifton Baldwin
  text: Hi Roy Jafari. One of my biggest problems with new projects is often just
    getting the data read in. Data is often collected by researchers using multiple
    Excel files, Word files, or various text files, often with no naming convention
    for the columns. A majority of my time is just getting the data so I can analyze
    it. I realize every situation is unique, but does the book raise awareness to
    these problems?
  replies:
  - name: Roy Jafari
    text: "Hi Clifton Baldwin! Thank you for your excellent question.\nThe book covers\
      \ similar situations such as this both as a level 1 data cleaning and also as\
      \ Data Integration.\nThe book's approach to data integration is to introduce\
      \ the readers to the most common challenges of data integration. Using examples,\
      \ 6 challenges are introduced and techniques on how to deal with them are presented.\
      \ One of the challenges is called \"Unwise Data Collection\" and is exactly\
      \ referring to the situations such as the ones you are describing here.\nHere\
      \ is an excerpt from the book that raises awareness about these issues.\n*Chapter\
      \ 9, Data Cleaning Level 1, Example 1 \u2013 unwise data collection*:\n\"From\
      \ time to time, you might come across sources of data that are not collected\
      \ and recorded in the best possible way. These situations happen when the data\
      \ collection has been done by someone or a group of people who have not had\
      \ enough skillset in database management. Regardless of why these situations\
      \ might have happened, you are given access to a source of data that requires\
      \ significant pre-processing before it is in one standard data structure.\n\
      For instance, imagine you have been hired by an election campaign to use the\
      \ power of data to help move the needle. Omid was hired just before you, and\
      \ he knows a lot about the political aspects of the election but not much about\
      \ data and data analytics. You are assigned to join Omid and help process what\
      \ he is tasked with. In your first meeting, you realize the task is to analyze\
      \ the speeches made by the 45th President of the United States, Donald Trump.\
      \ To bring you up to speed, he smiles and tells you that he has completed the\
      \ data collection and all that needs to be done is the analysis now; he shows\
      \ you the folder on his computer that has a text file (.txt) for every of Donal\
      \ Trump\u2019s speeches made in 2019 and 2020. \u2026.\nAfter seeing the folder\
      \ you instantly realize that a big task of data preprocessing remains to be\
      \ done before considering any analytics. In the interest of building a good\
      \ working relationship with Omid, you don\u2019t directly go to the point that\
      \ a huge data preprocessing needs to be done and instead comment on the aspect\
      \ of his data collection that has been great and can be used as a cornerstone\
      \ for data preprocessing. You mention that it is great that the naming of these\
      \ files follows a predictable order. The order is that city names come first\
      \ then comes the name of the month in three letters and then comes the day in\
      \ one or two digits and the year in four digits.\nAs you are well-versed with\
      \ Pandas DataFrame you suggest that the data be processed into one DataFrame\
      \ and Omid, eager to learn, accepts enthusiastically.\nThe following presents\
      \ the three steps that you can do to process the data into a DataFrame.\""
- name: Senthilkumar Gopal
  text: 'Hi Roy Jafari love the idea behind a book focused on pre-processing and data
    preparation. Some of the questions that we can benefit from your thoughts.

    1. What do you reckon are the key roadblocks that data scientists face in their
    EDA

    2. What are your thoughts on imputes and what role does that play in preprocessing

    3. Common standards and pipeline for data processing for ML

    4. Growth opportunities in data preparation space - For ex: companies provide
    cleaned data for financial and stock analysis'
  replies:
  - name: Roy Jafari
    text: Hi Senthilkumar Gopal! These are great quesitons. I will answer them one
      by one.
  - name: Roy Jafari
    text: "*Q1 - What do you reckon are the key roadblocks that data scientists face\
      \ in their EDA?* That\u2019s an important and a big question. I will list three\
      \ roadblocks that I believe have the most impact on the effectiveness of data\
      \ scientists.\nFirst, I think data scientists could hugely benefit from optimizing\
      \ their database and programming skills. There is a huge difference between\
      \ a code that works just now, and a code that is optimized, and will work again\
      \ and again and again in the future. Just like, there is a huge difference between\
      \ a solution that gets static data and output model insights just for that static\
      \ data, and a solution that automatically gets data from the source, preprocess\
      \ it and then outputs the insight; the first one must be run manually, the second\
      \ one can be deployed into a live dashboard or be used as an ML solution for\
      \ automatic decision making. If one needs to improve their programming skills\
      \ regarding data preprocessing and analytics.  this book is a great resource.\n\
      Second, I think data scientists need to start moving away from the Kaggle model\
      \ where the dataset is provided for them to apply their models. I believe data\
      \ scientists need to start empowering themselves to be the ones that design\
      \ those datasets, collect the data for them and preprocess them for the best\
      \ possible performance. It is more convenient to think it is the job of data\
      \ engineers to do those things, but I disagree. For data pipelining indeed data\
      \ scientists need the expertise of data engineers, however, the data scientists\
      \ must be central in the discussion of what should be pipelined and how it should\
      \ be preprocessed.\nLastly, I am convinced data scientists should look more\
      \ often to data preprocessing as a way to improve their solutions as opposed\
      \ to tuning their models or comparing models. The positive impact of a delicately\
      \ done data transformation and data massaging can sometimes look like magic,\
      \ however, it is the results of experience and understanding of different data\
      \ preprocessing that leads to significant improvements. I think data scientists\
      \ should invest in their mathematical skills to benefit more from tools such\
      \ as functional data analytics and feature extractions. Both Functional data\
      \ analytics and feature extraction are extensively covered in the book."
  - name: Roy Jafari
    text: "*Q2 - What are your thoughts on imputes and what role does that play in\
      \ preprocessing?* I am not sure what you mean by imputes. I guess, you mean\
      \ imputing missing values? I will answer assuming that is what you meant. Please\
      \ let me know if that was not the case.\n Imputing missing values is indeed\
      \ a topic that is covered in Chapter 11 Data Cleaning Level III- Missing Values,\
      \ Outliers, and Errors. Imputing missing values is one of the four possible\
      \ strategies that one might use when they face missing values. These strategies\
      \ are \u201CLeave as missing\u201D, \u201Cdrop attributes\u201D, \u201Cdrop\
      \ data objects\u201D, \u201Cimpute values.\u201D Furthermore, four types of\
      \ methods are presented for imputing values: impute with general central tendency,\
      \ impute with specific population central tendency, impute with an interpolated\
      \ value, and impute with estimated value using regression analysis.\nThe book\
      \ also covers how to choose what strategy, and what methods are appropriate.\
      \ It will involve understanding the type of missing values (MCAR, MAR, MNAR),\
      \ how the data will be used at the analytics stage, and the type of data.\n\
      One thing that I try to instill in the readers' mind that might be different\
      \ is that when imputing we are not trying to accurately predict what the value\
      \ could have been, we are trying to impute a value with two goals: 1) to be\
      \ able to keep as much real data as possible, 2) to add the least amount of\
      \ bias due to our imputes."
  - name: Roy Jafari
    text: '*Q3 - Common standards and pipeline for data processing for ML?* I am not
      aware of any standards for data pip liens or data processing as that is not
      my area of experience and expertise. I think a data engineer could answer this
      question better.

      I would say that there should be some guidelines for effective data pre-processing.
      I have outlined these in the book. For instance, the biggest one is clarity
      on the structure of the final dataset you will be using for the analysis. You
      would need to know exactly what each row of the dataset you will be creating
      represents before embarking on data preprocessing.'
  - name: Roy Jafari
    text: "*Q4: Growth opportunities in data preparation space - For ex: companies\
      \ provide cleaned data for financial and stock analysis?* I think the best way\
      \ to grow in this space is through actual experience. Resisting the temptation\
      \ to do the data cleaning, integration, and preprocessing in excel and doing\
      \ them either while pooling the data or afterward using scalable python modules\
      \ such as NumPy and pandas, however small your datasets are. You will start\
      \ learning that data preprocessing for each project is like a puzzle that needs\
      \ to be solved. There are many ways to go about the same data preprocessing,\
      \ however, some of them will be more scalable, will use less computation, and\
      \ will teach you new things as well.\nAs far as other growth opportunities,\
      \ I don\u2019t believe there is a community that focuses on data preparation\
      \ and data preprocessing. I do have a YouTube channel for which I create videos\
      \ regarding data preprocessing among other things. But I think, a data preprocessing\
      \ learning community can provide many benefits to its members. I would be interested\
      \ to join and contribute for sure.\nNothing else comes to mind. I hope this\
      \ was helpful."
  - name: Senthilkumar Gopal
    text: Roy Jafari Thanks so much for taking the time to respond and the thoughtful
      responses..
- name: jeromy
  text: Hi Roy Jafari, what are, in your opinion, typical mistakes or anti-pattern
    that people make during the data preprocessing phase (for example using pandas)?
    And what are the best way to resolve those mistakes?
  replies:
  - name: Roy Jafari
    text: "Hi jeromy! Thanks for your question.\nThis is a great question and can\
      \ have a very extensive answer. I\u2019ll try to keep it short by just mentioning\
      \ the three biggest ones that come to mind.\nThe first one is very basic but\
      \ is very easy to happen if data preprocessing has not happened methodically.\
      \ There are times that whoever has created the data has used numerical codes\
      \ for purely categorical attributes. It is a huge mistake to use those values\
      \ as numbers in your models. One of the first steps of data preprocessing is\
      \ to recognize the type of each attribute (nominal, ordinal, or numerical),\
      \ and based on the type of attributes the way they can be included in each analytic\
      \ might be different.\nA second mistake that comes to mind is the assumption\
      \ you need to prepare a dataset for a problem, use that preprocessed dataset\
      \ for any tools, models, or algorithm, and that\u2019s not the case. Each algorithm\
      \ and method uses the data differently and data preprocessing must be done specifically\
      \ for that algorithm. For instance, while outliers are huge issues for regression\
      \ models, they are not a big deal for an MLP (artificial neural network) model.\
      \ If the dataset prepared for regression in which we\u2019ve removed the outlier\
      \ is also used for MLP, we\u2019ve made a mistake because barring computational\
      \ complexity, MLP could have used the information in the outlier to improve\
      \ itself.\nThe third is not checking the practicality of independent attributes\
      \ for predicting the dependent attributes. I have seen time and again that a\
      \ model reaches high accuracy but the model is not usable because the value\
      \ of the independent attributes will be known exactly when we need to know the\
      \ dependent attribute or very close to it. Checking the practicality of the\
      \ independent attribute is very important.\nI know I said three, but here is\
      \ the fourth one. This can happen to data scientists that don\u2019t have up-to-date\
      \ programming skills and they might use looping to perform data preprocessing\
      \ on their models. Not only looping is computationally more expensive, but also\
      \ it is very time-consuming to write, maintain and update the code. My recommendation\
      \ is for a data scientist to learn about NumPy vectorization and broadcasting\
      \ first and any data manipulation they have they should try to use that strategy\
      \ for its implementation as it is the fastest approach. If that is not possible,\
      \ my second recommendation would be to apply functions to their data as opposed\
      \ to doing loops. To keep the code fast and scalable, it is also important to\
      \ learn what to avoid when applying a function to keep the code scalable."
  - name: jeromy
    text: Thank you for the exhaustive and clear answer!
  - name: Carlos Orjuela
    text: I love that fourth point Roy Jafari, is vectorization discussed in the book?
  - name: Roy Jafari
    text: Thanks for your positive feedback Carlos Orjuela. The answer is no, the
      book does not cover vectorization and broadcasting but it does cover mapping/applying
      functions.
- name: Carlos Orjuela
  text: Roy Jafari, do you know of any robust packages that helps to speed up EDA?
    As some task might be repetitive. I heard of some but never actually got to use
    any so I'd like to know your take on it
  replies:
  - name: Roy Jafari
    text: "Thanks for your question Carlos Orjuela. \nApart from matplotlib, seaborn,\
      \ and statmodels modules, which are great, I haven't come across any other outstanding\
      \ package. If you any know any others I would love to know about them."
  - name: Carlos Orjuela
    text: Thanks again Roy Jafari. One that comes to mind is Pandas profiling but
      I've never used it tbh
- name: Roy Jafari
  text: "Thank you Francis Terence Amit for featuring my book and also, thanks everyone\
    \ for their excellent question. \nHere is a 6 minute vide tour of the book: [https://youtu.be/iUHAFPucYZU](https://youtu.be/iUHAFPucYZU)\
    \ \nJust in case there were more unanswered question. \nCheers and happy learning,\
    \ everyone!"
  replies: []

---

Data preprocessing is the first step in data visualization, data analytics, and machine learning, where data is prepared for analytics functions to get the best possible insights. Around 90% of the time spent on data analytics, data visualization, and machine learning projects is dedicated to performing data preprocessing.

This book will equip you with the optimum data preprocessing techniques from multiple perspectives. You'll learn about different technical and analytical aspects of data preprocessing - data collection, data cleaning, data integration, data reduction, and data transformation - and get to grips with implementing them using the open source Python programming environment. This book will provide a comprehensive articulation of data preprocessing, its whys and hows, and help you identify opportunities where data analytics could lead to more effective decision making. It also demonstrates the role of data management systems and technologies for effective analytics and how to use APIs to pull data.

By the end of this Python data preprocessing book, you'll be able to use Python to read, manipulate, and analyze data; perform data cleaning, integration, reduction, and transformation techniques; and handle outliers or missing values to effectively prepare data for analytic tools.
