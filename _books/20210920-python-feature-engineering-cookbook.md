---
title: "Python Feature Engineering Cookbook"
description: "Book of the Week. Python Feature Engineering Cookbook by Soledad Galli"
cover: "images/books/20210920-python-feature-engineering-cookbook/cover.jpg"
image: "images/books/20210920-python-feature-engineering-cookbook/preview.jpg"
start: 2021-09-20 00:00:00
end: 2021-09-24 22:59:58
authors: [soledadgalli]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/python-feature-engineering-cookbook/9781789806311
  - text: Amazon
    link: https://www.amazon.com/-/en/Soledad-Galli/dp/1789806313
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Python-Feature-Engineering-Cookbook

archive:
- name: Guy Adams
  text: Soledad Galli - thanks for agreeing to answer questions! How automatable is
    the process of feature engineering against unknown/new data?
  replies:
  - name: Soledad Galli
    text: 'How automatable: that is the million dollar question. I think there is a
      lot of effort put into trying to automate feature engineering, with different
      degrees of success.'
- name: Kshitiz
  text: 'Soledad Galli - Thank you for doing this. Looking forward to other questions/responses
    as well.

    I want to understand if there is any systematic approach to engineer features
    for specific problems?'
  replies:
  - name: Soledad Galli
    text: I think the most advanced in that direction are the libraries featuretools
      and tsfresh which include transformers that out-of-the-box return a battery of
      features extracted based on the most used feature calculations. Tsfresh for example
      returns around 1200 features and then goes ahead and selects the most relevant
      ones. Featuretools does more or less the same but returns far fewer features.
  - name: Soledad Galli
    text: Both libraries are geared to time series though.

  - name: Soledad Galli
    text: For classical so to say data, i.e., tabular data, I have not come accross
      libraries like this. Instead other libraries like feature-engine, category encoders
      and sklearn offer a variety of individual transformers from which you can pick
      and choose according to the needs for your data. And then, you can line up all
      trasformers within a scikit-learn pipeline, to run them in sequence.
  - name: Soledad Galli
    text: The thing is, in my opinion, that some datasets may require some special treatment,
      and you know best your data than any python library, so at the end of the day,
      domain knolewdge always help
  - name: Soledad Galli
    text: I think with that I kind of try and answer the 2 questions, no? I don't know
      of a systematic approach other than what I mention here.

- name: Quynh Le
  text: Hi Soledad Galli, thanks for writing the book! Could you share with us which
    feature engineering methods are most popular? Also does feature engineering make
    it more difficult to interpret the model results?
  replies:
  - name: Soledad Galli
    text: 'Quynh Le for imputation, the most popular ones are mean, median imputation
      for numerical variables, usually accompanied by adding a missing binary indicator.
      And for categorical variables replacing NA with the string "missing" or "other".
      For categorical encoding, the most common is one hot encoding. For variable transformations
      I would say, log, box-cox and yeo-johnson, alternatively, discretization. And
      then for scaling: standardization or scaling to the maximum and minimum values,
      whenever needed. For time series I would say lagging the features, or window features,
      where you take usually the mean, max or min from a window of a certain number
      of steps usually behind the point you want to predict. But this is just the tip
      of the iceberg, there is a lot more that you can do to the data.'

- name: Nikhil Shrestha
  text: "Hi Soledad Galli\nThanks for writing the book.\nFeature engineering has always\
    \ been one of my favorite area in whole machine learning.\nI am posting few of\
    \ many questions here:\n1. Depending on data and it's distribution we decide upon\
    \ the feature engineering we can perform. As I also learnt that this can be mastered\
    \ with practice and experience with data. Could you point some resources to understand\
    \ this better. Lets say for e.g. we have a non linearly separable data in binary\
    \ classification problem. data looks like a concentric circle where -ve points\
    \ are in the inner circle and positive are on the outer circle. How can we transform\
    \ such feature to use Logistic Regression.\n2. I did a project on Walmart where\
    \ I used columns like date, weekly sales(dependent variable), store_number, to\
    \ generate two new ordinal columns which actually helped to improve score a lot.\
    \ I used mean, addition, if else statement to do this. Another example for the\
    \ same was formula for calculating social media popularity = (number_of_people_reviewed_for\
    \ movies / number_of people_voted_for_movie) * no_of_faceboooks_likes. It never\
    \ made sense to me as how this transformation helps in making model better, but\
    \ it actually did.\nUsing this technique made me think does FEATURE ENGINEERING\
    \ limits. Can we use any mathematical function using various columns and come\
    \ up with a new column and that will improve the model ? or is there a specific\
    \ pattern in this technique?\n3. There are many articles which says you can even\
    \ use running average of some variables to create a new one out of it. Does this\
    \ apply to certain specific cases ? or we can do is more often generally?\nI hope\
    \ I didn't offend or trouble you with these questions, but I couldn't find answers\
    \ to these. So thank you again Soledad Galli for the book and your expertise in\
    \ this area, also thank you Alexey Grigorev for this platform.\U0001F642"
  replies:
  - name: Soledad Galli
    text: 'Nikhil Shrestha 1) it is not always possible to transform data to make it
      linearly separable. Having said this, there are some techniques that help, like
      some mathematical transformations, or monotonic encodings for categorical variables,
      or using decision trees to replace the values of the variables by the predictions
      of the trees. Probably the latter would work best in the scenario you describe.
      I have a [course on udemy](https://www.udemy.com/course/feature-engineering-for-machine-learning/?couponCode=DATATALKSCLUB)
      on feature engineering where I teach monotonic encoding and how that helps with
      linear models, you might find that interesting. Andrew Ng in his machine learning
      course in coursera also discusses somewhere throughout the course something about
      transforming data to make it linearly separable. And for the encoding with decision
      trees, this article describe its use: [http://proceedings.mlr.press/v7/niculescu09/niculescu09.pdf](http://proceedings.mlr.press/v7/niculescu09/niculescu09.pdf)'
  - name: Soledad Galli
    text: 2) you can certainly use any mathematical transformation to create features.
      The sky is the limit. In fact, the package ts fresh does exactly that, create
      hundreds of features and then select the most relevant. Some Kaggle competitors
      (that won several competitions) also create loads of features and then select
      the most relevant. The thing I would advice here, is to think how are you going
      to use the features and the model. If it is for an organisation, that is tightly
      regulated, and needs to be able to explain the models and the variables to the
      customers and / or auditors, then I would suggest to create features that "make
      sense". If it is for a data science competition where the only thing that matters
      is to produce a high performing model, then you can do whatever you want.
  - name: Soledad Galli
    text: Also to add to the above, when we build models for organisations, usually
      someone within the organsation is going to "consume" that model. For example,
      if we build fraud detection models, the fraud investigators are going to follow
      up applications or claims that are fraudulent. So they do need interpretable models
      and thus, interpretable variables. If the variable is some sort of polynomial
      combination of price, location, and who knows how many other componenents, they
      can't really make sense of it
  - name: Soledad Galli
    text: 3) the running (rolling?) average is very frequently used in forecasting.
  - name: Soledad Galli
    text: "I am not offended or troubled by the questions, that is the whole point of\
      \ the book of the week, right? \U0001F609"
  - name: Nikhil Shrestha
    text: "Soledad Galli wow!!\nNow that you explained this it all sounds so simple\
      \ and intuitive. \nThe problem I was facing was is that I used to hold back when\
      \ transforming thinking:\n- what if this is only computationally heavy, especially\
      \ when working with kaggle datasets\n- my concepts were not that clear before.\
      \ \nNow that concepts are clear I can directly go apply transformation confidently\
      \ in competition and business case datasets, bcoz I know this will Surely work.\
      \ \nAnd yes I meant running average (I made a blunder by writing Rolling) \U0001F92D\
      \nHence thank you very much \U0001F64F\nI will surely take the course you suggested.\
      \ I am sure I will learn a lot from there too.\U0001F64C\nKeep up the good work\
      \ \U0001F642\U0001F44F"
- name: Doink
  text: 'Soledad Galli

    1. Classical Feature Engineering vs Deep Learning approach, which to choose when?

    2. What are the limitations of feature engineering?'
  replies:
  - name: Soledad Galli
    text: Doink I think the first question here is probably off-the-shelf traditional
      machine learning models (which need feature engineering) vs deep learning. Deep
      learning makes sense only when you have loads of data. If your datasets are small,
      deep learning does not really outperform the more traditional and thus simpler
      machine learning models. Andrew ng discusses this in one of the first videos in
      the ai specialization in coursera, in case you want more details.
  - name: Soledad Galli
    text: Regarding the limitations of feature engineering, I would say the first one
      is that it is time consuming. The second one is that to make features that make
      sense, we usually require some domain knowledge of the topic, for which we tend
      to work together with the experts, in my case, with the fraud investigators. For
      time series, also scalability is an important issue.

- name: WingCode
  text: 'Hi Soledad Galli,

    What are the features usually extracted from:

    1. Image

    2. Video

    3. Audio'
  replies:
  - name: Wendy Mak
    text: tbh for all 3 above kinds of data you typically run it through a neural
      net without really doing 'feature engineering' in the traditional sense. You
      might want to do data augmentation for example especially if you don't have
      much data, and for video depending on the problem you might or might not want
      to analyse individual frames, but the old way of e.g. doing CV by extracting
      edges and whatnot have been more or less replaced by neural nets
  - name: WingCode
    text: Thank you Wendy!
- name: WingCode
  text: 'Is it common for a feature engineering to break down a complex feature into
    a naive feature and then apply feature engineering on the naive feature?

    example 1: Video (complex  type) broken down into a list of images (naive type).
    Apply feature engineering on each image

    example 2: Audio (complex type) broken down into frequency domain(naive type).
    Apply feature engineering on each frequencies.

    example 3: IP address (complex type) broken down into approx geo location coordinates(naive
    type) . Apply feature engineering on geo-location'
  replies: []
- name: Soledad Galli
  text: Hello. Sorry WingCode I am not an expert on the field of Video, Audio and
    Image, so I can't comment.
  replies: []
- name: WingCode
  text: "No problems Soledad Galli \U0001F642"
  replies: []
- name: Tim Becker
  text: "Hi Soledad Galli, thanks for answering our questions \U0001F642"
  replies: []
- name: Tim Becker
  text: '- How do you recommend to treat outliers? What do you think about clipping
    outliers and when is this a good idea?'
  replies: []
- name: Tim Becker
  text: '- How do you deal with feature drift? If I re-train a model and e.g., the
    average of a feature has changed, would you disregard old data?'
  replies: []
- name: Tim Becker
  text: '- How do you investigate seasonality and what features do you use when you
    find seasonality?'
  replies: []
- name: Tim Becker
  text: '- If you have timeseries data with a high frequency and you guess that consecutive
    data points are highly correlated, how do you check this and would you disregard
    some of the highly correlated data points for training?'
  replies: []
- name: Soledad Galli
  text: 'Hello Tim Becker, outliers: you can cap the maximum and minimum values, I
    think this is what I do most often. Or you can remove them from the training data.
    But you would probably get outliers in the test, live data and then you need to
    decide what to do with those if you removed them from the train set. If you cap,
    then that is handled automatically by the feature engineering pipeline. When to
    cap or to clip depends on the data, and the model that you are training. Tree
    based models are robust to outliers, so no need to do much about them. Linear
    models are, so in that case you may chose to remove them. In some cases outliers
    are important, for example if you are investigating credit risk and a person has
    been in court already, it is a bad indicator, yet that happens very rarely, so
    a positive in that variable is indeed an outlier that you don''t want to remove.
    You can choose to leave in the model and see what happens or perhaps better to
    create a rule to treat those cases separately (outside the model). Bottom line,
    I don''t think there is a single way to treat outliers, it depends on the nature
    of the data and the outcome we are after, as well as the mathematical models we
    are using.'
  replies: []
- name: Soledad Galli
  text: 'Feature drift: again, no single answer. Depends on the data, and what you
    are trying to model. I think the first thing would be to understand why the drift
    happened and if we expect this drift to hold or if we expect it to go back to
    original values. Some examples: a drift can happen because the organisation changed
    a policy, e.g., before it only served people of a certain age, now they serve
    all segments. Naturally there will be a drift, but that drift is here to stay.
    So I would probably try and incorporate more data that resembles the new population.
    Another example, during the 2009 depression debt indicators signaled risk of default.
    Several years after the depression, people acquire a lot of debt (not that I agree
    with that economic model) and they did not default. So debt indicator was no longer
    a signal for risk of default. What do you expect to happen in the next 5 years?
    a crisis, say a pandemic? then you could model using the old data. Stability?
    then I would discard the old data.'
  replies: []
- name: Soledad Galli
  text: My examples are a bit easy and binary, but I guess you get the yest :)
  replies: []
- name: Soledad Galli
  text: Seasonality inspection, I think visual inspection + domain knowledge is what
    is done more often. If your features have seasonality you can create new features
    capturing aspects of that seasonality (regression in time, seasonal dummies, seasonal
    lag). I have not done that myself, so you need to come back with that questions
    in a few weeks from now if you would like more details, because we are preparing
    a new course on the topic :)
  replies: []
- name: Soledad Galli
  text: You can check autocorrelation with autocorrelation plots. I am not sure I
    would disregard data. I think you can apply filters to decrease a bit the variation
    if it is too much so that the autocorrelation is to high at some points, and also
    create lag features to capture that correlation and use it to your advantage if
    you want to forecast.
  replies: []
- name: Sandhya G
  text: "Soledad Galli What are some suggestions on dealing with large number of features\
    \ which do not have any physical significance. Few things to think of \n1. Use\
    \ lasso to select features\n2. Remove features that have low variance (for floating\
    \ point data)\n3. Remove features that are highly cross correlated\n4. PCA\nAnything\
    \ else?\nSpecifically, this is a chemistry problem, predicting properties using\
    \ chemical structure of the molecule. There are established packages like RDKit\
    \ which dump a 1000s of descriptors for each molecule. \nThanks!"
  replies:
  - name: Soledad Galli
    text: 'You can remove constant or quasi-constant features, for example with this
      class of Feature-engine: [https://feature-engine.readthedocs.io/en/latest/selection/DropConstantFeatures.html](https://feature-engine.readthedocs.io/en/latest/selection/DropConstantFeatures.html)'
  - name: Soledad Galli
    text: 'On the same line, sometimes features are duplicated or we introduce duplication
      after one hot encoding, which can be removed with this other class: [https://feature-engine.readthedocs.io/en/latest/selection/DropDuplicateFeatures.html](https://feature-engine.readthedocs.io/en/latest/selection/DropDuplicateFeatures.html)'
  - name: Soledad Galli
    text: Similarly to Lasso we can use the importance derived from trees to remove
      less relevant features, one implementation of this is the boruta algorithm,
      but it can also be done manually with the SelectFromModel from sklearn for example
      passing RandomForests or other tree based method
  - name: Soledad Galli
    text: you can perform recursive feature elimination or addition. Shuffle features
      and determine performance drift. The possibilities are endless... ok maybe not
      endless but there is quite a bit out there.
  - name: Soledad Galli
    text: 'Here are the methods supported by Feature-engine: [https://feature-engine.readthedocs.io/en/latest/selection/index.html](https://feature-engine.readthedocs.io/en/latest/selection/index.html)'
  - name: Soledad Galli
    text: 'And I discuss all of this in another course that you can find on udemy
      on this link: [https://www.udemy.com/course/feature-selection-for-machine-learning/?couponCode=DATATALKSCLUB](https://www.udemy.com/course/feature-selection-for-machine-learning/?couponCode=DATATALKSCLUB)'
  - name: Soledad Galli
    text: I have not worked on chemistry problems myself, so I am not sure if people
      in this field are doing something more specific.
  - name: Sandhya G
    text: Thank you for the pointers Soledad Galli! I will check out the resources
- name: Nikhil Shrestha
  text: "Hi Soledad Galli \nI am putting my question in 4 steps: \n1. Suppose we have\
    \ some data in CSV and we want to make graph structure or visualization using\
    \ this data \n2. I was thinking of making certain column heading as vertex and\
    \ the values inside column as edges. \n3. For this we can use DictVectorizer to\
    \ create numerous columns.\n4. What can we do for numerical data if want to create\
    \ a graph structure and end result should be explainable to non technical person\
    \ \nI am presently solving something very similar, so I was thinking of a way\
    \ out. \nSo if this approach is completely wrong please suggest me some direction.\
    \ \U0001F64F\U0001F642"
  replies:
  - name: Soledad Galli
    text: I am not familiar with graph data (nodes, edges, relationships) so I can't
      help with this question.
  - name: Soledad Galli
    text: Regarding how to present the data to a non-technical audience, I guess it
      depends on the data, on the project, and what are the key messages to deliver
      to the audience. Bar plots, line plots, bullets with the key messages. If working
      with text word clouds.
  - name: Soledad Galli
    text: I guess many people in this goupr can probably contribute some ideas, so
      don't ne shy :)
  - name: Nikhil Shrestha
    text: "Thank you again \nI was thinking about presenting the audiance in similar\
      \ fashion as you mentioned here. \n\U0001F642"
- name: Avishek Datta
  text: '*1.  While checking for whether a feature has normal distribution or not,
    is it necessary to check for the distribution of the Target Variable as well and
    then transform this Target variable (say, log transform the Target variable)?*

    *2. Again while checking the distribution I observe that one of the features is
    not normally distributed. So I log Transform it. This is a Predictor variable,
    now. Now after the entire model has been trained, do I need to use anti-log for
    that particular feature to take in new feature variables for prediction?*

    *3. Maximum how many transformations can be added in a Pipeline &amp; also a ColumnTransformer?*

    *4. When should one use Winsorization and outlier removal through IQR method?
    Which is more optimal?*'
  replies:
  - name: Soledad Galli
    text: For linear regression models, normal distributions in both predictive features
      and target tend to improve the performance. So I would check the distribution
      (of both) and if it helps apply a transformation.
  - name: Soledad Galli
    text: If you log transform a variable, and then train a model, whenever you make
      a prediction using new / raw data, you need to log transform that same feature
      before passing it to the model, because the model learned patterns from the
      log transformed variable.
  - name: Soledad Galli
    text: you would only apply the inverse of the log transform, if for some reason
      you need to retrieve the original (raw) values of that variable, say to show
      some results to stakeholders.
  - name: Soledad Galli
    text: 3) You can add as many transformations as you need. The sky is the limit.
  - name: Soledad Galli
    text: 4) some linear models are sensitive to outliers, in the sense that can be
      biased by these observations.  You would in general cap outliers if a) you are
      sure they do not add any value, and b) capping improves model performance.
  - name: Soledad Galli
    text: You could cap finding the limits with the IQR, percentiles or mean and standard
      deviation. The choice depends mostly on the variable distribution. IQR returns
      more representative limits when we have  skewed variables.
  - name: Avishek Datta
    text: Thanks for the answers
- name: Avishek Datta
  text: '*5. After applying discretization on a feature, is it necessary to check
    for the skewness of the discretized feature and then transform it, if necessary
    (say log transform or root transform?*'
  replies:
  - name: Soledad Galli
    text: There are discretization methods that already, by definition, return intervals
      that are homogeneously distributed, for example equal frequency discretization.
      I would apply these methods instead of discretizing into something that is skewed
      and then transforming the variable further.
- name: Shankar Somayajula
  text: 'Hi Soledad Galli.. Thanks for taking questions.

    Using the fraud model as an example, once users of your model see the results
    of latest fraud model incorporated and see the benefits e.g. successful identification
    of fraud [instances... How do they respond to gaps in terms of missing fraud?
    Can they ](http://instances.be) articulate new features which are variations of
    existing features and see them incorporated w/o an explicit modeling process (via
    UI or some other post processing activity)? How does one keep the (domain) features
    updated? Is Iterative development fast enough to respond to real time fraud behavior/events?'
  replies:
  - name: Soledad Galli
    text: I think this depends on the organisation. Different organisations may have
      different procedures. You can have a team of fraud investigators continuously
      analysing the landscape and creating new features or new rules I would better
      say. The data scientist could be performing data analysis on recent data and
      seeing if something new comes up. I think continuously monitoring of the landscape
      evolution is probably key. And then, you could combine different models to try
      and detect different aspects of fraud.


---

Feature engineering is invaluable for developing and enriching your machine learning models.
In this cookbook, you will work with the best tools to streamline your feature engineering
pipelines and techniques and simplify and improve the quality of your code.


Using Python libraries such as pandas, scikit-learn, Featuretools, and Feature-engine,
you’ll learn how to work with both continuous and discrete datasets and be able to transform
features from unstructured datasets. You will develop the skills necessary to select the best
features as well as the most suitable extraction techniques. This book will cover Python recipes
that will help you automate feature engineering to simplify complex processes. You’ll also get
to grips with different feature engineering strategies, such as the box-cox transform,
power transform, and log transform across machine learning, reinforcement learning,
and natural language processing (NLP) domains.

