---
title: "Deep Learning with fastai Cookbook"
description: "Book of the Week. Deep Learning with fastai Cookbook by Mark Ryan"
cover: "images/books/20211206-deep-learning-with-fastai-cookbook/cover.jpg"
image: "images/books/20211206-deep-learning-with-fastai-cookbook/preview.jpg"
start: 2021-12-06 00:00:00
end: 2021-12-10 22:59:58
authors: [markryan]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/deep-learning-with-fastai-cookbook/9781800208100
  - text: Amazon
    link: https://www.amazon.com/Deep-Learning-fastai-Cookbook-easy/dp/1800208103

archive:
- name: Raghav Bali
  text: "Thanks Alexey Grigorev  for yet another interesting week. \nQuestion I have\
    \ regarding the book:\n\"What according to you is a major drawback while using\
    \ fastai as compared to TF or PT (apart from the fine grained control we have\
    \ from these 2 frameworks)?\"\nAgain kudos Mark Ryan for such a detailed book,\
    \ the TOC looks quite comprehensive \U0001F44D"
  replies:
  - name: Mark Ryan
    text: 'Hi Raghav Bali - fastai is a great platform, particularly for beginners.
      That being said, I see two noteworthy drawbacks: (1) compared to TF/Keras or
      vanilla PyTorch, there are not as many examples of fastai being deployed in
      production, (2) regressions. Compared to Keras, it is easier to hit regressions
      with the fastai platform (that is, something that used to work that stops working
      after a platform update), and you need to be prepared to work around regressions
      if you come across them in fastai. An example of a regression in fastai is the
      code to set the random seed, which stopped working as expected after an update.
      In addition to these drawbacks, the documentation for fastai is not as comprehensive
      as Keras documentation, but the fastai course forum [https://forums.fast.ai/](https://forums.fast.ai/)
      helps to make up for that.'
  - name: Raghav Bali
    text: Awesome... Thanks for the detailed answer
- name: WingCode
  text: 'Hi Mark Ryan,

    What is the advantage of using DataBunch or abstracted data types in fastai versus
    using pandas DataFrame &amp; converting it to numpy for training the model?'
  replies:
  - name: Mark Ryan
    text: Hi WingCode - the advantage of the abstracted data structures in fastai
      is that they are integrated into the deep learning workflow and make it easy,
      for example, to look at a sample batch or examine individual elements in a dataset.
      Simply put, they help make it easy to focus on the essential tasks of creating
      and training a deep learning model without having to write a lot of additional
      code.
  - name: WingCode
    text: "Thank you Mark for the answer \U0001F642"
- name: John Trengrove
  text: Hi Mark Ryan does the book have examples for combining vision / tabular /
    text models together?
  replies:
  - name: Mark Ryan
    text: Hi John Trengrove - that is a great question. There are examples in the
      book of vision, tabular, text and recommender system models, but there aren't
      examples that combine these data types.
- name: WingCode
  text: 'In the book''s TOC,

    ```Chapter 5

    Training a recommender system on a small curated dataset

    Training a recommender system on a large curated dataset```

    How does [fast.ai](http://fast.ai) training differ for a recommender system on
    small curated dataset vs a large curated dataset? Do you use a collaborative filtering
    in the 1st one since it''s a small one and can fit into memory? For the 2nd one,
    do you use some content based approach?'
  replies:
  - name: Mark Ryan
    text: Hi WingCode - the recommender system with the small dataset was an attempt
      to demonstrate an MVP of fastai's recommender system support. The resulting
      model works but it is of limited practical value because the columns in the
      dataset don't mean much to humans (it's a movie rating dataset with no movie
      titles). Once the reader has been through that example, it motivates the second
      example with the large dataset (which is more than 10 times bigger than the
      small dataset and has a much more complex structure). The second example takes
      many more steps to get it to work, but the result is more satisfying - you see
      the recommender system making predictions about the rating a particular user
      will give for a movie that is generally thought to be excellent (L.A. Confidential)
      vs. a movie that is generally thought to be terrible (Showgirls).
  - name: Mark Ryan
    text: The reason for doing an MVP first and then a bigger example is that some
      of the existing material on fastai doesn't take the time to do an MVP and jumps
      right into the full-blown solution with a big, complex dataset. The problem
      with skipping the MVP is that it's hard to figure out the reason for the additional
      steps for the big, complex dataset if you haven't already grasped the minimum
      set of steps.
  - name: WingCode
    text: "Yes that makes sense Mark. Thank you again \U0001F642"
  - name: Allan
    text: "Mark Ryan I think the approach of showing the MVP approach first makes\
      \ a lot of sense, for the reasons you described. It also gives the reader a\
      \ good example of how things might be done for a real-world problem or project\
      \ they might be working on\u2026 start first with something simple and small\
      \ to evaluate/validate the approach before moving on and investing the time\
      \ on something more realistic and complex."
- name: Carlos Orjuela
  text: Hi Mark Ryan, how's the Cookbook different compared to Jeremy's book. What
    can we expect from it? Thanks
  replies:
  - name: Mark Ryan
    text: 'Hi Carlos Orjuela - the book by Jeremy Howard and Sylvain Gugger is a master
      work. It not only covers exhaustive details about fastai, it also takes the
      reader through many aspects of the theory of deep learning. It also includes
      a whole chapter on AI ethics. By contrast, my book is focused on using fastai
      to solve practical problems. It includes details on setting up an environment
      to use fastai and then has a chapter each on the 4 major application areas supported
      by fastai: tabular data, text data, recommender systems, and image data. In
      each of these chapters, you''re led through a working code example for a fastai
      curated dataset and then working through an example for a standalone dataset.
      My book wraps up with a chapter on model deployment and then a chapter on more
      advanced topics (including callbacks, augmented data, and more additional deployment
      tips).'
  - name: Mark Ryan
    text: So, Jeremy Howard's book can teach you many general deep learning concepts
      and covers all kinds of nuances and details about fastai. It is also a complement
      to the deep learning for coders course [https://course.fast.ai/](https://course.fast.ai/).
      My book is focused on step-by-step application of fastai to solve practical
      problems.
  - name: Carlos Orjuela
    text: "Thanks Mark Ryan for the detailed response \U0001F642"
- name: Haseeb Arshad
  text: HiMark Ryan!!! What is the best part of this book? Is this book good for beginners
    to start and learn about fastai? Thank you!
  replies:
  - name: Mark Ryan
    text: 'Hi Haseeb Arshad - thanks for your question. As for the best part of the
      book, it is probably not right for me to say so as the author, but if you look
      at the reviews on Amazon you will see some of the things that people liked about
      the book: [https://www.amazon.com/Deep-Learning-fastai-Cookbook-easy/dp/1800208103#customerReviews](https://www.amazon.com/Deep-Learning-fastai-Cookbook-easy/dp/1800208103#customerReviews).
      I do believe that the book is good for beginners to learn about fastai - it
      takes you from the very start of setting up an environment all the way to deploying
      a trained model.'
- name: Carlos Orjuela
  text: Hi Mark Ryan, gathering from your previous answers and in particular from
    the drawbacks [Fast.ai](http://Fast.ai) has in your opinion, the focus of your
    book helps to pave the way of showing more practical examples and deployment into
    production tips, is that a fair assumption? Thanks again
  replies:
  - name: Mark Ryan
    text: Hi Carlos Orjuela - the book covers practical examples and talks about ways
      to work around some of the drawbacks of fastai. It also describes the many strong
      points of fastai, such as (1) the way fastai provides comprehensive support
      for tabular datasets and (2) how fastai makes it easier than Keras to ensure
      that data goes through the same transformations when the model makes a prediction
      as the data went through when the model was trained. The book has a whole chapter
      on deployment. Deployment is a huge topic, so this chapter doesn't cover all
      deployment options. In particular, many production deployments would be via
      a cloud platform like AWS, Google Cloud, or Azure, and the book does not explain
      how to do that.
  - name: Carlos Orjuela
    text: Thanks again for your reply Mark Ryan
- name: Allan
  text: Thanks Mark Ryan for taking the time to answer questions here. From the table
    of contents it looks like a great book! Would you say that [fast.ai](http://fast.ai)
    is mainly appropriate for someone who wants to build practical deep learning models
    without necessarily needing to understand the underlying DL theory?  If one wants
    to understand deep learning well, would you say, as I think Jeremey H posits,
    that by taking a top-down approach and becoming a practitioner first, that one
    is then in a better position to dive-in and understand the details and inner workings?
  replies:
  - name: Mark Ryan
    text: Hi Allan - I think it's fair to say that Jeremy Howard's philosophy about
      learning deep learning is that it's best to start by doing. His course (and
      the fastai framework) emphasize getting something to work in code first and
      then go back and dig into the theory / math. He contrasts the fastai approach
      with the traditional approach to learning deep learning, which starts with abstractions
      and theory that can be offputting to somebody who is trying to use deep learning
      to solve a real-world problem. I think that Howard wants fastai to be used by
      people who don't have an academic background in machine learning but do have
      deep subject area expertise and access to interesting data sets.
- name: Tim Becker
  text: Hi Mark Ryan, I was wondering if there is a difference between deploying fastai
    models and TF, Keras models? I can imagine that you might end up with large docker
    containers?
  replies:
  - name: Mark Ryan
    text: Hi Tim Becker - in the book I did a simple "from the ground up" web deployment
      of some fastai models using Flask. In this scenario, fastai was easier than
      Keras. To do the same kind of deployment with Keras for a tabular model, I needed
      to worry about the pipeline and I needed to load the model repeatedly. With
      fastai, the pipeline was taken care of automatically and I only had to load
      the model when the web page initially loaded, leading to a smoother experience.
- name: Tim Becker
  text: If you already know how to build models with keras, where would deliberately
    choose fastai?
  replies:
  - name: Mark Ryan
    text: 'The question of Keras vs. fastai is a good one. Keras definitely has some
      advantages over fastai, including a much larger user community and better documentation.
      If that''s the case, why would somebody who has already used Keras go through
      the effort of learning to use fastai? I can think of two reasons (a) gateway
      to PyTorch for somebody who has been working in the TF sphere. fastai provides
      a low-impact way to ease into PyTorch for somebody who is familiar with the
      TF ecosystem and wants to take a peek at the "other side". (b) full-throttle
      support for tabular datasets. It''s certainly possible to create models trained
      on tabular data using Keras (I spent another book on that topic: [https://www.amazon.com/Deep-Learning-Structured-Data-Mark/dp/1617296724/ref=sr_1_1?keywords=deep+learning+with+structured+data&amp;qid=1638993209&amp;sr=8-1](https://www.amazon.com/Deep-Learning-Structured-Data-Mark/dp/1617296724/ref=sr_1_1?keywords=deep+learning+with+structured+data&amp;qid=1638993209&amp;sr=8-1)
      ) but fastai makes it much easier.'
  - name: Tim Becker
    text: Mark Ryan Thank you for your answers, very interesting! Could you elaborate
      a little bit what you mean by additional support for tabular data?
  - name: Allan
    text: This is very helpful!
- name: Allan
  text: Mark Ryan I see from the TOC that there is a chapter on extended [fast.ai](http://fast.ai)
    and deployment features? Can you expand on what is covered there?
  replies:
  - name: Mark Ryan
    text: Hi Allan - there is a chapter in the book on deployment. This covers how
      to deploy fastai models trained on tabular and image datasets in a simple web
      application using the Python Flask library. These deployments include everything
      - the Flask module, the HTML and CSS files, and the trained models, as well
      as detailed instructions on how to set them up. The final chapter of the book
      gives additional detail on web deployment - for example, showing you how to
      show thumbnails of the images the model is making predictions on and showing
      you how to make a deployment on your local machine available to the external
      web. The final chapter also covers (a) fastai callbacks - these make the fastai
      training process efficient by avoiding non-productive training epochs and ensuring
      you exit the training run with the optimally trained model (b) fastai's built-in
      support for augmenting image data (c) various features for getting additional
      details about models trained with fastai, such as confusion matrices and data
      points where the model did worst.
  - name: Allan
    text: Thanks Mark Ryan , sounds like a very practical couple of chapters that
      adds a lot of value!
- name: Allan
  text: "Also, a little bit off topic\u2026 but I was wondering what your take is,\
    \ in general, on PyTorch vs Tensorflow - putting aside the fastai/keras layers\
    \ that make each of them easier to use.  It seems a lot of folks these days are\
    \ moving toward and favoring PT\u2026 \U0001F642"
  replies:
  - name: Mark Ryan
    text: 'Hi Allan - the conventional wisdom is that TF is used more by industry
      and PyTorch is used more by academics. The Stack Overflow 2021 survey backs
      this up: [https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-other-frameworks-and-libraries](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-other-frameworks-and-libraries).
      I''d say that it''s hard to compare PyTorch and TF without bringing Keras into
      the discussion. After all, it is now the official high-level API for TF, and
      it''s used extensively, even by specialists. Search the Stack Overflow survey
      for Keras and you will see it, while fastai and Lightening (another high-level
      framework for PyTorch) are both missing. This could be because professional
      developers use PyTorch directly and don''t have use for a higher level framework,
      or it could be that developers working in industry are still predominantly on
      TF/Keras.'
  - name: Mark Ryan
    text: I can't predict the future, but I think it would be a safe bet to say that
      while PyTorch will be adopted more by industry, TF/Keras isn't going anywhere
      and will still be a significant part of the landscape in 10 years.
- name: Mark Ryan
  text: 'Hi - for anybody who is interested in more content on fastai, Keras (plus
    GPT-3, Codex, Rasa and other topics), please check out:

    - my YouTube channel: [https://www.youtube.com/channel/UC33c02d4_ssg0tGO3EXKG8g](https://www.youtube.com/channel/UC33c02d4_ssg0tGO3EXKG8g)

    - my Medium blogs: [https://markryan-69718.medium.com/](https://markryan-69718.medium.com/)'
  replies: []
- name: Allan
  text: Thanks for taking the time to answer questions here Mark Ryan !
  replies:
  - name: Mark Ryan
    text: Thanks Allan - I really enjoyed the chance to answer the questions this
      week. I appreciate the time that people took to share these great questions.
- name: Mark Ryan
  text: Congratulations to the winners, much thanks to Alexey Grigorev for hosting
    me here, and thanks to everybody who participated this week.
  replies:
  - name: Alexey Grigorev
    text: Are you working on another book right now? =) I bet you are and we can invite
      you again soon =)
  - name: Mark Ryan
    text: Hi Alexey Grigorev - I'm not actively writing right now, but I have a couple
      of ideas in the works, so I look forward to coming back again to talk about
      the next book.

---

The book begins by summarizing the value of fastai and showing you how to create a simple
'hello world' deep learning application with fastai. You'll then learn how to use fastai
for all four application areas that the framework explicitly supports: tabular data, text
data (NLP), recommender systems, and vision data. As you advance, you'll work through
a series of practical examples that illustrate how to create real-world applications of
each type. Next, you'll learn how to deploy fastai models, including creating a simple
web application that predicts what object is depicted in an image. The book wraps up with
an overview of the advanced features of fastai.


