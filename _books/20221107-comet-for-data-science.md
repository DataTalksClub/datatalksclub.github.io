---
authors:
- angelicaloduca
cover: images/books/20221107-comet-for-data-science/cover.jpg
description: Book of the Week. Comet for Data Science by Angelica Lo Duca
end: 2022-10-28 23:59:59
image: images/books/20221107-comet-for-data-science/preview.jpg
links:
- link: https://www.packtpub.com/product/comet-for-data-science/9781801814430
  text: Book's page
- link: https://github.com/PacktPublishing/Comet-for-Data-Science
  text: GitHub repository
start: 2022-10-24 00:00:00
title: Comet for Data Science
archive:
- name: Angelica Lo Duca
  text: Hello everyone! It's a pleasure for me to meet you! If you have any questions,
    I'll be glad to answer them.
  replies:
  - name: Ifra
    text: Hi Angelica Lo Duca , great to have you here! I came to know about comet
      platform recently and very curious to know that how ML on comet is different
      from traditional machine learning?
  - name: Angelica Lo Duca
    text: 'Hi Ifra thanks for your question! Comet helps you track your ML experiments
      and see the results directly in the Comet dashboard. For example, let''s suppose
      that you want to choose the best model for a classification task. You need to
      test different models, for example KNN, RandomForest and so on. Once you have
      tested your models, you choose the one with the best performance. This is the
      standard way. In Comet, the flow is the same, but you track each experiment
      in Comet, by adding just one or two lines of code. As a result, you can perform
      the comparison between the different experiments directly in Comet. You could
      watch this video to have an idea of how Comet works: [https://www.youtube.com/watch?v=GHyX9VeuPn0&amp;t=2s](https://www.youtube.com/watch?v=GHyX9VeuPn0&amp;t=2s)'
  - name: Angelica Lo Duca
    text: Comet also provides other features, for example, you can add it directly
      to your deployment environment
  - name: Angelica Lo Duca
    text: I hope that I've answered your question. For more details, you can also
      watch the other episodes of the Series 11 weeks of Comet for Data Science [https://www.youtube.com/watch?v=GHyX9VeuPn0&amp;list=PLLT9c0_6kiT6rRQHs1TVA0ZzaE5B3v8KF](https://www.youtube.com/watch?v=GHyX9VeuPn0&amp;list=PLLT9c0_6kiT6rRQHs1TVA0ZzaE5B3v8KF)
  - name: Ifra
    text: "Yes you did Angelica Lo Duca, thank you so much! I'll surely check out\
      \ the read!\U0001F642"
- name: Alexey Grigorev
  text: Just curious, why did you decide to write a book about comet? Did you compare
    it with other ML platform before making this decision?
  replies:
  - name: Angelica Lo Duca
    text: Hi Alexey! Thanks for your question! Indeed, before meeting Comet, I organized
      my ML experiments in a directory on my local computer, and I compared the different
      models manually. This process took a lot of time, so I decided to search for
      some tools that could help me solve my problem. I discovered Comet and other
      similar platforms. I started to test Comet and I realized that working with
      Comet is simpler than doing things manually. To be honest, I didn't try other
      platforms because I was really excited by Comet! Then, I wrote an article about
      Comet on my blog. Next, someone from Packt Publication contacted me asking if
      I was interested in writing a book about Comet. And so the book was born.
- name: Eunice
  text: 'Hi, Angelica Lo Duca; thank you so much for joining. In your experience,
    how much did using Comet help you save time in the ML/DL delivery process?

    Would you recommend using Comet for an MVP or more advanced projects?'
  replies:
  - name: Angelica Lo Duca
    text: Hi Eunice! Thanks for your question! I think that using Comet in the ML/DL
      lifecycle saves a lot of time because you can use Comet both for model tracking
      and model updating. For example, you can store the best model in the Comet Registry
      and then use it in production. When you update your model, you just need to
      update it in the Comet Registry. The figure attached shows how you can integrate
      Comet with the GitLab CI/CD pipeline. I hope that I answered your question.
  - name: Angelica Lo Duca
    text: Regarding your second question, recommending using Comet for an MVP project,
      yes, absolutely!
- name: Hareesh
  text: "Hi Angelica Lo Duca, \nI am just curious to know if Comet has capabilities\
    \ to put ML models into production ? \nMy follow-up  question is more regarding\
    \ EDA, is comet automating EDA ? If so, are there options that would help us identify\
    \ outliers in data ?\nThanks. \nHT"
  replies:
  - name: Angelica Lo Duca
    text: Hi Hareesh, thanks for your questions! Yes, you can integrate Comet in the
      production workflow. Comet provides a Registry where you can store the best
      model. Thanks to the Comet REST API, you can download the best model in your
      production environment. In addition, Comet is fully integrated with GitLab thus
      you can use the GitLab CI/CD workflow to move your ML to production. Chapters
      6 and 7 of the book explain this aspect.
  - name: Angelica Lo Duca
    text: Regarding EDA, Comet is not designed to support it natively. However, Comet
      is integrated with some external libraries such as pandas profiling to perform
      EDA in Comet.
  - name: Angelica Lo Duca
    text: I hope that I have answered to your questions.

---

This book provides concepts and practical use cases which can be used to quickly build, monitor, and optimize data science projects. Using Comet, you will learn how to manage almost every step of the data science process from data collection through to creating, deploying, and monitoring a machine learning model.

The book starts by explaining the features of Comet, along with exploratory data analysis and model evaluation in Comet. You’ll see how Comet gives you the freedom to choose from a selection of programming languages, depending on which is best suited to your needs. Next, you will focus on workspaces, projects, experiments, and models. You will also learn how to build a narrative from your data, using the features provided by Comet. Later, you will review the basic concepts behind DevOps and how to extend the GitLab DevOps platform with Comet, further enhancing your ability to deploy your data science projects. Finally, you will cover various use cases of Comet in machine learning, NLP, deep learning, and time series analysis, gaining hands-on experience with some of the most interesting and valuable data science techniques available.

By the end of this book, you will be able to confidently build data science pipelines according to bespoke specifications and manage them through Comet.
