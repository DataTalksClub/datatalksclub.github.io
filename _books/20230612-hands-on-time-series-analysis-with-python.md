---
authors:
- ashishpatel
- vishwasbv
cover: images/books/20230612-hands-on-time-series-analysis-with-python/cover.jpg
description: Book of the Week. Hands-on Time Series Analysis with Python by Ashish
  Patel
end: 2023-06-16 23:59:59
image: images/books/20230612-hands-on-time-series-analysis-with-python/preview.jpg
links:
- link: https://www.oreilly.com/library/view/hands-on-time-series/9781484259924/
  text: Book's page
- link: https://www.amazon.com/Hands-Time-Analysis-Python-Techniques-ebook/dp/B08GLG46PQ
  text: Buy on Amazon
start: 2023-06-12 00:00:00
title: Hands-on Time Series Analysis with Python

archive:
- name: Alex Litvinov
  text: "Ashish Patel, Nate Silver or Nassim Taleb? \U0001F609"
  replies: []
- name: Alexey Opolchenov
  text: Hi Ashish Patel. Your book was written 3 years ago, is there any major changes
    in time series analisys sinse that time?
  replies: []
- name: Alexey Opolchenov
  text: Ashish Patel Looks like time series analysis sometimes take same aproaches
    as NLP bacause data comes in sequence. Is there any benefit in time series analysis
    from recent ChatGPT hype?
  replies:
  - name: Ashish Patel
    text: '*Transformers in Time Series: A Survey*  : [https://arxiv.org/abs/2202.07125](https://arxiv.org/abs/2202.07125)'
  - name: Ashish Patel
    text: '[https://github.com/qingsongedu/time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review)'
  - name: Alexey Opolchenov
    text: Ashish Patel Thank you, very interesting!
- name: Carlos Pumar
  text: "hi Ashish,\nthank you for opening up the possibility of reading your book!\n\
    While reading thru its contents I wondered:\n- what type of data is used for the\
    \ convolutional layers of the CNN model architecture?\nUsing time series of the\
    \ dependent variable seems intuitive for the input layer of the\nfully-connected\
    \ layer, less so for the convolutional network?\n- does the book also cover concepts\
    \ for identifying the underlying data-generating\nprocess?\n- related to the case\
    \ studies, and specifically re \u201Cbanking\u201D: what is the target variable\n\
    to be forecasted?\n- regarding the statistical methods: does the book cover non-parametric\
    \ methods (e.g.\nbayesian stats) as well?\nthanks again and kind regards,\nCarlos"
  replies: []
- name: Ella
  text: Hey there authors, my question is on how to start gathering time series data,
    if I want to scrape from a website that I have no access to, just interested in
    its datapoints over time? And if I were to start now to collect data, I have no
    historical data to work with for it to be a time-series, right?
  replies:
  - name: Ashish Patel
    text: 'Hello Ella, Sure, I can help you with that.

      There are a few ways to gather time series data from a website you cannot access.

      One way is to use a web scraping tool. Several web scraping tools are available,
      both free and paid. Some popular web scraping tools include:

      ===============================================================================

      &gt; - *Beautiful Soup:* This is a free and open-source Python library for web
      scraping.

      &gt; - *Selenium:* This is a free and open-source tool for automating web browsers.

      &gt; - *WebHarvy:* This is a paid web scraping tool that offers a variety of
      features, including support for multiple browsers and languages.

      Once you have chosen a web scraping tool, you will need to configure it to scrape
      the data from the website that you are interested in. This may involve specifying
      the URL of the website, the elements that you want to scrape, and the format
      in which you want the data to be saved.

      Once the web scraping tool is configured, you can run it to scrape the data
      from the website. The data will be saved in a file, which you can then import
      into a time series analysis tool.

      Another way to gather time series data from a website you cannot access is to
      use a data API. A data API is a web service that provides access to data.

      There are a number of data APIs available, both free and paid. Some popular
      data APIs include:

      ===============================================================================

      &gt; - *Quandl:* This is a free and open-source data API that provides access
      to financial data.

      &gt; - *Google Finance:* This is a free data API that provides access to financial
      data.

      &gt; - *Yahoo Finance:* This is a free data API that provides access to financial
      data.

      Once you have found a data API that provides access to the data you are interested
      in, you must sign up for an account and obtain an API key. Once you have an
      API key, you can use it to make requests to the data API. The data will be returned
      in a JSON format, which you can then import into a time series analysis tool.

      If you do not have any historical data to work with, you can start collecting
      data now and use it to create a time series. However, it is important to note
      that the accuracy of your predictions will depend on the amount of data that
      you have. The more data you have, the more accurate your predictions will be.

      Here are some additional tips for gathering time series data:

      ===============================================================================

      &gt; - Use a variety of sources: It is important to use a variety of sources
      when gathering time series data. This will help to ensure that you have a complete
      and accurate dataset.

      &gt; - Check for errors: It is important to check for errors in your data. This
      can be done by using a data validation tool.

      &gt; - Clean your data: It is important to clean your data before you use it
      for analysis. This can be done by removing any outliers or missing values.

      &gt; - Document your data: It is important to document your data. This will
      help you to understand the data and to make it easier to share with others.

      *Timeseries Dataset GitHub :* [https://github.com/WenjieDu/TSDB](https://github.com/WenjieDu/TSDB)

      I hope this helps!

      *Regards,*

      *Ashish Patel*'
  - name: Ella
    text: Thank you for the resource, and the comprehensive response. Much appreciated!
- name: Alex Litvinov
  text: 'Hi Ashish Patel,

    what do you think about [https://otexts.com/fpp3/](https://otexts.com/fpp3/)?'
  replies:
  - name: Ashish Patel
    text: This is one of the Nice Book Alexey Grigorev
- name: Harshit Lamba
  text: Hello authors, my question revolves around prediction of black swan events.
    My presumption is that data itself isn't sufficient for prediction of such events
    (such as earthquakes, market crashes etc.) as there are many more external factors
    responsible for these. How do we go about developing models for such scenarios?
    Do we have any use-cases in the book to deal with these? Do any research papers
    published hold the promise of addressing such use-cases?
  replies:
  - name: Ashish Patel
    text: 'Hello Harshit Lamba! You are correct that data alone is not sufficient
      for predicting black swan events. As you mentioned, there are many external
      factors that can contribute to these events, and these factors are often difficult
      to quantify or measure. As a result, it is very difficult to develop models
      that can reliably predict black swan events.

      That said, there are a number of research papers that have been published on
      the topic of black swan event prediction. Some of these papers have proposed
      methods for using machine learning techniques to identify potential black swan
      events. Other papers have focused on developing methods for mitigating the impact
      of black swan events.

      One example of a research paper that has proposed a machine learning-based method
      for black swan event prediction is the paper *["Black Swan Event Prediction
      with Machine Learning" by Ethan Pickering and colleagues](https://spectrum.ieee.org/weather-predicting-black-swan)*.
      In this paper, the authors propose a method for using a Bayesian neural network
      to predict the occurrence of black swan events. The authors evaluated their
      method on a dataset of historical data, and they found that their method was
      able to predict black swan events with a high degree of accuracy.

      Another example of a research paper that has focused on mitigating the impact
      of black swan events is the paper "Black Swan Event Mitigation with Portfolio
      Diversification" by John Cochrane. In this paper, the author argues that portfolio
      diversification can help to mitigate the impact of black swan events. The author
      shows that by diversifying a portfolio across a wide range of assets, investors
      can reduce their exposure to the risk of any one asset experiencing a black
      swan event.

      The research on black swan event prediction is still in its early stages, and
      no single method has been shown to be universally effective. However, the research
      that has been conducted to date suggests that machine learning techniques and
      portfolio diversification can be used to help mitigate the impact of black swan
      events.

      The book "Hands-on Time Series Analysis with Python" by Ashish Patel, does not
      specifically address the topic of black swan event prediction. However, the
      book does cover a number of topics that are relevant to black swans'' event
      prediction, such as forecasting, anomaly detection, and risk management.

      Overall, the research on black swan event prediction is still in its early stages,
      but there is a growing body of research that suggests that machine learning
      techniques and portfolio diversification can be used to help mitigate the impact
      of black swan events.'
- name: Daniel
  text: "Hi Ashish Patel,\nthanks for providing this opportunity since time series\
    \ forecasting is such a fascinating topic.\nMy questions are the following:\n\
    - *Uncertainty*: Most models provide you with a point estimation. However we live\
    \ in very instable times. I am aware of some options that helps to express uncertainty\
    \ (e.g. confidence intervals, conformal prediction etc.), but out of your experience:\
    \ Are there any approaches that you usually refer to/ that turned out to be most\
    \ useful? \n- *Explainability*: Another area that I feel gets more and more important\
    \ is model explainability. While e.g. fbprophet is known to be a blackbox, how\
    \ are you usually handling this issue? Which approaches do you use if a customer\
    \ comes up with such a demand to not only provide predictions but also to explain\
    \ how the model comes to a certain prediction? \n- *Classical vs. advanced methods*:\
    \ While in NLP or CV Transformer models nowadays outperform almost all other approaches,\
    \ there is a highly controversial discussion ongoing about the usefulness of Transformers\
    \ with regard to TS. The majority still holds the view that classical methods\
    \ such as ARIMA or LightGBM are better suited and outperform Transformers in most\
    \ TS use cases. What are your experiences? \nLooking forward to your answers.\
    \ Many thanks in advance! \U0001F60A \U0001F64F \nBest regards\nDaniel"
  replies:
  - name: Ashish Patel
    text: "*Hi Daniel,*\nThank you for your questions. I am happy to answer them.\n\
      - Uncertainty: There are a number of approaches that can be used to express\
      \ uncertainty in time series forecasts. Some of the most common methods include:\n\
      \    \u25E6 Confidence intervals: Confidence intervals provide a range of values\
      \ that are likely to contain the true value of the forecast. The width of the\
      \ confidence interval indicates the level of uncertainty in the forecast.\n\
      \    \u25E6 Prediction intervals: Prediction intervals provide a range of values\
      \ that are likely to include the true value of the forecast, even if there are\
      \ unexpected changes in the underlying data. The width of the prediction interval\
      \ is typically wider than the confidence interval, as it takes into account\
      \ the possibility of unexpected changes.\n    \u25E6 Conformal prediction: Conformal\
      \ prediction is a non-parametric approach to uncertainty estimation that does\
      \ not make any assumptions about the underlying distribution of the data. This\
      \ makes it a particularly useful method for forecasting data that is not normally\
      \ distributed.\nIn my experience, the most useful approach to expressing uncertainty\
      \ in time series forecasts depends on the specific application. For example,\
      \ if the forecast is being used to make important decisions, then it is important\
      \ to use a method that provides a narrow prediction interval.\nHowever, if the\
      \ forecast is being used for less critical purposes, then a wider confidence\
      \ interval may be sufficient.\n- *Explainability*: Explainability is another\
      \ important consideration when developing time series forecasts. Explainability\
      \ refers to the ability to understand how a model makes its predictions. This\
      \ can be important for a number of reasons, such as:\n    \u25E6 *Trust*: Users\
      \ are more likely to trust a model if they can understand how it works.\n  \
      \  \u25E6 *Interpretability*: In some cases, it may be necessary to interpret\
      \ the model's predictions in order to make decisions.\n    \u25E6 *Debugging*:\
      \ If the model is not performing well, it can be helpful to understand why in\
      \ order to improve it.\nThere are a number of ways to improve the explainability\
      \ of time series models. Some of the most common methods include:\n&gt; - *Feature\
      \ selection:* Feature selection can be used to identify the most important features\
      \ for the model. This can help to reduce the complexity of the model and make\
      \ it easier to understand. \n&gt; - *Interpretation tools:* There are a number\
      \ of tools that can be used to interpret the predictions of a time series model.\
      \ These tools can be used to visualize the model's predictions and to understand\
      \ the relationships between the features and the predictions. \n&gt; - *Communication:*\
      \ It is important to communicate the results of the model to the users in a\
      \ clear and understandable way. This can be done through reports, presentations,\
      \ or other means.\nNote: *[Lime](https://github.com/marcotcr/lime)* will help\
      \ in this case to ExplainableAI of Time Series\n- Classical vs. advanced methods:\
      \ The debate over the usefulness of classical vs. advanced methods for time\
      \ series forecasting is likely to continue for some time. There is no clear\
      \ consensus on which approach is better, as the best approach depends on the\
      \ specific application.\nIn my experience, classical methods such as ARIMA and\
      \ LightGBM can be very effective for time series forecasting. However, advanced\
      \ methods such as Transformers can also be effective, especially for forecasting\
      \ complex data sets.\nThe choice of which approach to use should be made on\
      \ a case-by-case basis, taking into account the specific requirements of the\
      \ application.\nI hope this answers your questions. Please let me know if you\
      \ have any other questions.\n*Best regards,* \n*Ashish*"
- name: raki
  text: 'Interesting thanks.

    How can MLOps principles be applied to the deployment of time series models in
    a production environment? Are there any specific challenges or considerations
    when it comes to deploying and maintaining these types of models ? Like when a
    model should be retrained, I could guess depends on the problem could be that
    a company wants to retrain every day?'
  replies:
  - name: Ashish Patel
    text: 'Hello raki,

      *Thank you for your questions. I am happy to answer them.*

      *MLOps principles can be applied to the deployment of time series models in
      a production environment by:*

      *================================================================================*

      &gt; - *Automating the entire ML lifecycle:* This includes data collection,
      preprocessing, feature engineering, model training, evaluation, and deployment.

      &gt; - *Ensuring reproducibility:* This means that the same results can be obtained
      from the same data and code, which can be difficult to achieve with black-box
      models like Transformers.

      &gt; - *Monitoring the model performance*: This includes tracking the accuracy
      of the model''s predictions, as well as any changes in the underlying data that
      could impact the model''s performance.

      &gt; - *Retraining the model as needed:* This is important because the underlying
      data may change over time, which can impact the model''s accuracy. The frequency
      of retraining depends on the specific application. For example, a model that
      is used to forecast daily sales may need to be retrained more often than a model
      that is used to forecast quarterly earnings.

      *Some of the specific challenges or considerations when it comes to deploying
      and maintaining time series models in a production environment include:*

      *================================================================================*

      &gt; - *Data quality*: The quality of the data used to train the model is critical
      to the accuracy of the model''s predictions.

      &gt; - *Model complexity*: Complex models can be difficult to understand and
      interpret, which can make it difficult to debug and improve the model.

      &gt; - *Model bias*: Models can be biased, which can lead to inaccurate predictions.

      &gt; - *Model drift*: The underlying data may change over time, which can impact
      the model''s accuracy.

      By following *MLOps principles*, organizations can improve the *accuracy, reliability,
      and maintainability* of their *time series models.*

      *Here are some additional tips for deploying and maintaining time series models
      in a production environment:*

      *================================================================================*

      &gt; - *Use a cloud-based platform:* This can make it easier to manage and scale
      the model, as well as to access and store the data.

      &gt; - *Use a continuous integration/continuous delivery (CI/CD) pipeline:*
      This can automate the process of deploying the model to production, which can
      help to ensure that the model is always up-to-date.

      &gt; - *Use a monitoring system:* This can track the performance of the model
      and alert you if there are any problems.

      &gt; - *Have a plan for retraining the model:* This will help to ensure that
      the model remains accurate over time.'
- name: Michael Enudi
  text: 'Hello Authors, congratulations on your published work.

    I noticed that many python books on time series don''t pay as much details or
    attention to Volatility clustering as R books on time series.

    Is there a reason for that?

    Are there other tools besides classical methods of Arch and Garch family of tools
    to analyze variability in volatility and how to predict such?'
  replies:
  - name: Ashish Patel
    text: '*Hi Michael Enudi,*

      *Thank you for your kind words.*

      There are a few reasons why many Python books on time series don''t pay as much
      attention to volatility clustering as R books.

      &gt; - R has a number of packages that are specifically designed for volatility
      clustering analysis, such as the `rugarch` package. Python does not have a dedicated
      package for volatility clustering analysis, so it is often covered in more general
      time series books.

      &gt; - *Volatility clustering* is a more advanced topic in time series analysis,
      and it is not essential for understanding the basics of time series forecasting.
      Many Python books are aimed at beginners, so they may not cover volatility clustering
      in detail.

      &gt; - *Volatility clustering* is a relatively new topic in time series analysis,
      and it is still being researched. As a result, there is not as much literature
      on volatility clustering in Python as there is in R.

      There are a number of other tools besides classical methods of ARCH and GARCH
      family of tools to analyze variability in volatility and how to predict such.
      Some of these tools include:

      &gt; - *Power GARCH*: This is a generalization of the GARCH model that allows
      for more flexibility in the modeling of volatility.

      &gt; - *Exponential GARCH*: This is a variant of the GARCH model that uses an
      exponential decay function to model the autocorrelation of the squared errors.

      &gt; - *TARCH*: This is a threshold autoregressive conditional heteroskedasticity
      model that allows for different levels of volatility depending on the value
      of the underlying time series.

      &gt; - *VARX*: This is a vector autoregressive model that allows for exogenous
      variables to impact the volatility of the time series.

      The choice of which tool to use depends on the specific application. For example,
      if the goal is to forecast volatility for a *financial asset,* then a model
      such as the *GARCH* or *Power GARCH* model may be appropriate. However, if the
      goal is to forecast volatility for a non-financial asset, then a model such
      as the *TARCH* or *VARX* model may be more appropriate.

      It is important to note that no single tool is *perfect for all volatility forecasting
      applications*. As a result, it is often necessary to use a combination of tools
      to get the best results.

      *Best Regards,*

      *Ashish Patel*'

---

Learn the concepts of time series from traditional to bleeding-edge techniques.  This book uses comprehensive examples to clearly illustrate statistical approaches and methods of analyzing time series data and its utilization in the real world. All the code is available in Jupyter notebooks.

You'll begin by reviewing time series fundamentals, the structure of time series data, pre-processing, and how to craft the features through data wrangling. Next, you'll look at traditional time series techniques like ARMA, SARIMAX, VAR, and VARMA using trending framework like StatsModels and pmdarima. 

The book also explains building classification models using sktime, and covers advanced deep learning-based techniques like ANN, CNN, RNN, LSTM, GRU and Autoencoder to solve time series problem using Tensorflow. It concludes by explaining the popular framework fbprophet for modeling time series analysis. After reading Hands -On Time Series Analysis with Python, you'll be able to apply these new techniques in industries, such as oil and gas, robotics, manufacturing, government, banking, retail, healthcare, and more.
