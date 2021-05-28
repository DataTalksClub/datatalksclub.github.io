---
title: "Machine Learning Using TensorFlow Cookbook"
description: "Book of the Week. Machine Learning Using TensorFlow Cookbook by Alexia Audevart"
cover: "images/books/20210503-machine-learning-using-tensorflow-cookbook/cover.jpg"
image: "images/books/20210503-machine-learning-using-tensorflow-cookbook/preview.jpg"
start: 2021-05-03 00:00:00
end: 2021-05-07 22:59:58
authors: [alexiaaudevart, Konrad Banachewicz, Luca Massaron]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/machine-learning-using-tensorflow-cookbook/9781800208865
  - text: Amazon
    link: https://www.amazon.com/Machine-Learning-Using-TensorFlow-Cookbook/dp/1800208863
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Machine-Learning-Using-TensorFlow-Cookbook

archive:
- name: Ksenia
  text: 'Hello Alexia Audevart!

    I am happy to see the advanced book on TensorFlow 2, thank you! Many use-cases
    and examples over the internet come on &lt;TensorFlow 2 and require some time
    and efforts to adapt.

    What common real-world problems are demonstrated and resolved as practical use-cases
    in the book?'
  replies:
  - name: Alexia Audevart
    text: 'Hello Ksenia,

      Thank you for your feedback. We covered many use cases with images and sequence
      data (image classification, applying stylenet, retraining existing models, text
      generation, sentiment analysis, stock price prediction, and so on). A special
      chapter is dedicated to ML in Production.'
- name: Saulius Lukauskas
  text: "Hi Alexia Audevart ! This looks like a great book! I see more and more job\
    \ ads that explicitly require experience in ML frameworks like TensorFlow these\
    \ days over more general software engineering requirements like \u201Cexperience\
    \ in numeric programming using python\u201D. I always wonder about why is this\
    \ the case.  Alexia Audevart, as a person who just wrote the book on the topic,\
    \ what do you think are the peculiarities about TensorFlow that do not translate\
    \ well from other programming/data wrangling paradigms? What concepts one should\
    \ try to learn in a structured way, from a book like yours, because they are \u201C\
    hard to get right\u201D otherwise?"
  replies:
  - name: Alexia Audevart
    text: "Hi Saulius Lukauskas,\nSoftware Engineering is a different paradigm of\
      \ Machine Learning paradigm. So it\u2019s a new skill."
  - name: Alexia Audevart
    text: TensorFlow is one of the more popular Deep Learning framework. But Deep
      Learning is a subset of Machine Learning. ML and DL are *part* of the artificial
      intelligence family.
  - name: Saulius Lukauskas
    text: "Hi Alexia Audevart, thanks for the answer! Maybe I didn\u2019t phrase my\
      \ question properly, I feel like my use of the term Software Engineering was\
      \ a red herring. Maybe I could paraphrase it a bit differently: for a person\
      \ who is familiar with say, python and general machine learning concepts (on\
      \ pen and paper for instance), but not TensorFlow framework per se - what are\
      \ the specifics (or maybe \u201Cgotchas\u201D) of TensorFlow that one should\
      \ be aware of and pay extra attention when studying it?"
  - name: Alexia Audevart
    text: "TensorFlow is a Deep Learning API so you\u2019ll need to start with dense\
      \ neural networks and understand deep learning concepts such as activation functions,\
      \ dense layers, epochs, gradient descent, etc. Then, you can focus on CNN for\
      \ images classification and RNN for sequence data. I think this will be a good\
      \ starting point ;-)"
- name: Saskia Kutz
  text: 'Hi Alexia Audevart! The content of your book and the corresponding github
    account look interesting.

    What are the prerequisites to learn from your book (apart from knowing basic python)?'
  replies:
  - name: Alexia Audevart
    text: 'Hi Saskia Kutz,

      If you know some basics of Python. You can read the book. May be, you can look
      at some Machine learning concepts... Enjoy your reading ;-)'
  - name: Saskia Kutz
    text: Thank you. So your book is about implementing these machine learning concepts
      we all learned about elsewhere?
  - name: Alexia Audevart
    text: This book assumes a basic familiarity with Python and Machine Learning concepts.
      We explained all the Deep Learning concept step by step in all chapters.
- name: Vladimir Finkelshtein
  text: "In the contents, I couldn\u2019t find a chapter on debugging neural networks.\
    \ Is it because there are no common practices yet, or because it is just outside\
    \ of the scope of the book. Can you recommend any reading on that?"
  replies:
  - name: Alexia Audevart
    text: "Hi Vladimir Finkelshtein,\nIndeed, we didn\u2019t write a specific chapter\
      \ on that topic. But you can find some tips in each chapter. TF v2 is by default\
      \ in eager execution mode, so it\u2019s now easier to debug than 2 years ago"
- name: Vladimir Finkelshtein
  text: "For most classical ML models, one can\u2019t use data with missing values.\
    \ In some use case, imputing missing values is a bad practice, and may bias the\
    \ model too much.\nI keep hearing that it is allowed in neural networks to leave\
    \ missing values (I guess you just don\u2019t activate some neurons if you have\
    \ nans). However, I have not seen any code that does this. Do you cover such examples?\
    \ Or is it as simple as adding categorical columns that some values is missing/present?"
  replies:
  - name: Alexia Audevart
    text: 'No, we did not address this topic because we used ready-made datasets.
      May be you can find some useful inputs in this research paper : [https://hal.inria.fr/hal-03044144/file/how_to_deal_with_missing_data_in_supervised_deep_learning_.pdf](https://hal.inria.fr/hal-03044144/file/how_to_deal_with_missing_data_in_supervised_deep_learning_.pdf)'
  - name: Vladimir Finkelshtein
    text: "Hm, I like the comparison they did, but I didn\u2019t like that they do\
      \ it on MNIST. When one has random missing pixels in MNIST, a good imputation\
      \ will be taking average color of observed neighboring pixels. So it\u2019s\
      \ not surprising that they learned something that beats zero and mean imputations.\n\
      Thanks for the paper, it also has references to surveys, they seem to be worth\
      \ checking.."
- name: Vladimir Finkelshtein
  text: "I know you are biased towards tensorflow. If someone was just starting with\
    \ deep learning, would you recommend them tensorflow or pytorch? What will be\
    \ more common in 3 years from now? Google trends doesn\u2019t seem to favor tf."
  replies:
  - name: Alexia Audevart
    text: "I\u2019m just starting to use PyTorch so I don\u2019t have enough experience\
      \ to give you a complete comparison. PyTorch is more pythonic than TF. In 3\
      \ years a lot of things could happen... I totally agree with this article: [https://www.tooploox.com/blog/pytorch-vs-tensorflow-a-detailed-comparison](https://www.tooploox.com/blog/pytorch-vs-tensorflow-a-detailed-comparison)"
- name: Riddhi Dasani
  text: "Hi Alexia Audevart ,\nWonderful content Indeed , Thank you for writing this\
    \ . \U0001F64F\nI was wondering can I recommend this book to people who are preparing\
    \ for [Tensorflow Developer Certificate](https://www.tensorflow.org/certificate)\
    \ .\nYour book from the content seem to have all concepts covered , But your experiences\
    \ on readers who completed this exam after reading the book ."
  replies:
  - name: Alexia Audevart
    text: "Hi Riddhi Dasani,\nThank you for your message. This book coupled with Laurence\
      \ Moroney\u2019s MOOC on Coursera is a good way to get the TF certification.\
      \ \U0001F4AA"
  - name: Riddhi Dasani
    text: Awesome , Good to know . Thanks Alexia Audevart
- name: Alexey Grigorev
  text: Can you tell us about projects you have in the book? How did you select the
    datasets for these projects?
  replies: []
- name: Alexey Grigorev
  text: "And what's your favourite chapter? \U0001F642"
  replies:
  - name: Alexia Audevart
    text: "Hi Alexey Grigorev,\nMy favourite recipe is without hesitation Deep Dream\
      \ in the CNN chapter. It\u2019s magic to create a psychedelic image by using\
      \ abstract art.\nWe want readers that they learn by doing so in each recipe,\
      \ we explore a dataset\n(We\u2019ve used many datasets which are included into\
      \ Keras, public open datasets,  Kaggle datasets, CSV files, and so on...)"
- name: Matthew Emerick
  text: Hey, Alexia Audevart! Thanks for doing this and congratulations on the book.
    What projects did you want to include but couldn't?
  replies: []
- name: Matthew Emerick
  text: Will you write another book?
  replies: []
- name: Matthew Emerick
  text: Are there any books you recommend we read before yours?
  replies:
  - name: Alexia Audevart
    text: "Hi Matthew Emerick,\nI think this book covers different aspects of what\
      \ we have to know in deep learning. However, each day, researchers make new\
      \ discovers on that topics... so we can create every day new recipes.\nI think\
      \ ML and DL in production would be the next challenge.\n If you speak French,\
      \ you can read my first book about AI and NeuroSciences."
  - name: Alexia Audevart
    text: '[https://www.apprendre-demain.fr/](https://www.apprendre-demain.fr/)'
- name: Lamjed Debbich
  text: Hello Alexia Audevart! Great book, I am wondering, what this book can bring more for experienced
    Data Scientist ?
  replies:
  - name: Alexia Audevart
    text: "Hi Lamjed Debbich,\nIn Data Science, you need to have IT skills, Maths\
      \ &amp; Stats skills and Business skills.\nThis book introduces you to a specific\
      \ part of Machine Learning (the ability for a machine to learn something without\
      \ being specifically programed to) called Deep Learning.  I think that this\
      \ skill will be more and more essential for a data scientist. I Hope I have\
      \ answered your question correctly \U0001F60A"
  - name: Lamjed Debbich
    text: Thankyou Alexia Audevart
- name: Ksenia
  text: 'It is super compelling that in addition to the TensorFlow ecosystem, one
    will learn from the book how to take TensorFlow into production!

    I am wondering whether you shared some recipes or hints for real-time model performance
    monitoring peculiar to TF ecosystem?'
  replies:
  - name: Alexia Audevart
    text: 'Hi Ksenia,

      We have addressed some tips and guidelines ta take TF models into production
      but not the one you mention. Maybe my next book will be about ML in production
      ;-)'
  - name: Ksenia
    text: Alexia Audevart looking forward to it!
- name: Glenn
  text: Hi Alexia, congrats on your book! It must be feel very exciting to write on
    such an interesting topic. If you had to add one more chapter, what would it be
    about?
  replies:
  - name: Alexia Audevart
    text: 'Hi Glenn,

      Very good question! I think we covered all the fundamental topic... May be we
      can go deeper into the attention architecture.'

---

The independent recipes in Machine Learning Using TensorFlow Cookbook will teach you how to
perform complex data computations and gain valuable insights into your data. You will work
through recipes on training models, model evaluation, sentiment analysis, regression analysis,
artificial neural networks, and deep learning - each using Google’s machine learning library, TensorFlow.

This cookbook begins by introducing you to the fundamentals of the TensorFlow library,
including variables, matrices, and various data sources. You’ll then take a deep dive into
some real-world implementations of Keras and TensorFlow and learn how to use estimators to
train linear models and boosted trees, both for classification and for regression to provide
a baseline for tabular data problems.