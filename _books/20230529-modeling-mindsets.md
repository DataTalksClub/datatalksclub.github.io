---
authors:
- christophmolnar
cover: images/books/20230529-modeling-mindsets/cover.jpg
description: Book of the Week. Modeling Mindsets by Christoph Molnar
end: 2023-06-02 23:59:59
image: images/books/20230529-modeling-mindsets/preview.jpg
links:
- link: https://christophmolnar.com/books/modeling-mindsets/
  text: Book's website
- link: https://www.amazon.com/dp/B0BMGSF52B
  text: Buy on Amazon
start: 2023-05-29 00:00:00
title: Modeling Mindsets

archive:
- name: "Carolina Quiroz Ju\xE1rez"
  text: 'Hello everyone!

    Thank you to the author for his generosity and Francis Terence Amit. I''ve modeled
    the scheduling problem of battery energy storage systems (BESS) using RL and NN.
    However, I didn''t pursue using a method as Bayesian inference. How does using
    the latest may change the problem definition? Is Bayesian inference an appropriate
    method to solve control problems in Engineering? For instance control of BESS.'
  replies:
  - name: Christoph Molnar
    text: 'Hi Carolina, that''s a great opening question.

      In general, I see machine learning as more "solving a task"-focus and it''s
      less important how the task was solved. The classic statistical inference might
      put more focus on modeling the distributions of your target/features. Bayesian
      inference in particular would put more emphasis on modeling the *distributions*
      of the parameters involved in the model. So if you''d approach the project more
      from Bayesian inference "lense" you would automatically get also things like
      uncertainty quantification for your parameters and interpretable estimates of
      how input and output relate to each other.

      But I suspect you chose RL for a good reason. And that''s also what I talk about
      in the book: Different mindsets have different strengths and limitations. And
      RL''s strength is learning to interact within a system. A purely  Bayesian inference
      approach (without any RL) might not solve the same problem.

      I also write in the book that these modeling mindsets should be seen as archetypes
      and in practice you use a mixture of approaches.'
- name: Antonis Stellas
  text: 1. How would you describe the current/common mindset for approaching a data
    project (let's say a regression problem) and how it would be transformed if we
    would use a modeling mindset?
  replies:
  - name: Christoph Molnar
    text: 'Like I defined it in the book, there is *always* a mindset behind a model.

      Because you have to put in some assumptions for your model if you want to use
      the results.

      Person 1  defined a performance metric, benchmarked a couple of models, the
      linear regression model shows the lowest error on the validation data.

      Person 2: You want to know how feature X influences target Y. You include in
      the regression model all the confounders for the relation between X and Y.

      Even though person 1 and person 2 used a linear regression model, they came
      from different mindsets and used different assumptions. Person 2 may interpret
      the coefficient for X as causal effect. Person 1 can make clear statements about
      what  they would expect for the performance of the model.

      Person 1 in this case came from supervised ML mindset and person 2 from causal
      inference.'
- name: Antonis Stellas
  text: 2.  Do you think that a dataset is basically a model? a model that describes
    our project/problem (in a particular snapshot of time or range of time)
  replies:
  - name: Christoph Molnar
    text: 'A dataset alone doesn''t constitute a model. Data is often noisy and high-dimensional
      and most information in it will be irrelevant to the problem that you want to
      solve.

      You need models to make data usable. As definition for "model" the book used:
      "a mathematical model that consists of variables and functions"'
  - name: Djordje Benn-Maksimovic
    text: "One of my professors once described \u201Cmodel\u201D with the analogy\
      \ of a map: it is useful precisely because it abstracts from / simplifies reality\
      \ and focuses on those features of reality that are relevant to the problem\
      \ you\u2019re trying to solve. \nI liked that analogy."
- name: Djordje Benn-Maksimovic
  text: 'Assuming that the later chapters are also about mindsets: How does e.g. deep
    learning differ from machine learning _as a mindset_?'
  replies:
  - name: Christoph Molnar
    text: "Ah good question, as I myself was torn whether or not to include it as\
      \ its own mindset.\nBecause why should neural networks be a \"mindset\", but\
      \ SVMs or trees are not?\nIt's the only chapter where the mindset emerges from\
      \ the use of a specific type of model, in this case the neural networks.\nI\
      \ think it's worth exploring deep learning as a mindset because if you only\
      \ use neural networks, it shapes a lot how you approach a project:\n- Deep learning\
      \ encourages modeling tasks end-to-end: from raw data to the final outcome.\
      \ No feature engineering, complex pipelines, etc.\n- An emergent property of\
      \ neural networks is embedding: the learned weights of a neural network store\
      \ useful information that can be used in feature engineering (like word embeddings)\
      \ to initialize other neural networks or generate insights.\n- Deep learning\
      \ comes with a high modularity which makes it possible to custom-build a model\
      \ for a use case.\nAll these properties make deep learning a coherent framework\
      \ for modeling.\nThe modeler doesn't have to \u201Cleave\u201D neural networks\
      \ to solve a task."
  - name: Djordje Benn-Maksimovic
    text: Thank you!
- name: luca pugliese
  text: A better understanding of the meaning of modeling mindset, in particular,
    the possibility to categorize them as I undrstand it is done in the book, could
    be a valid aid in model interpretability tasks? Moreover, can be useful also for
    other important aspects of ML like results explainability, model obervability,
    fairness?
  replies:
  - name: Christoph Molnar
    text: 'I would say that interpretability is just one aspect of the modeling mindsets.

      For classic statistical modeling, interpretability is in focus and often there
      is a mapping between a coefficient (weight) in a model and something in the
      "real world". Like a parameter for how a treatment affects the predicted disease
      outcome.

      Machine learning on the other hand is more driven to solve a task based on some
      performance metric -- what the model looks like and whether it''s interpretable
      or not is then irrelevant.

      But that''s only for archetypes of mindsets. An archetype is the extreme, pure
      form of something. I myself come from a background of both (mostly frequentist)
      statistics and later also machine learning. So the other book I wrote, Interpretable
      Machine Learning, I would say is somewhere in between these archetypes.'
- name: Yuanwei Xu
  text: While it is interesting to explore different modelling mindsets, isn't it
    true that data also dictates the kind of models? For example if the task involves
    images, texts or other unstructured/semi-sturctured data, it is probably best
    approached by deep learning methods, this is a modelling mindset driven by data
    and task. In general, where do you see data-centric AI fit into this?
  replies:
  - name: Christoph Molnar
    text: 'I agree with that. Same goes for certain tasks that are better solved with
      a certain mindset. If your goal is to make a prediction, unsupervised learning
      shouldn''t be your go-to approach (although could be used for things like feature
      engineering).

      Image data, for example, is much better approached with deep learning than anything
      else. In theory you can use non-deep learning approaches which was done in the
      past. But then you need hand-crafted features and so on and it just doesn''t
      work as well as deep learning does.

      For the other part: I didn''t know the term data-centric AI, so I had to look
      it up. For the book, I included only mindsets where some type of model is part
      of it. My first impression is that it''s mostly used in supervised ML settings
      (correct me if I''m wrong). So my first intuition would be to categorize this
      with supervised ML.'
  - name: Yuanwei Xu
    text: Thank you for your answer. The term was first described by Andrew Ng, basically
      it argues that before looking at algorithms, one should focus on improving the
      quality of data. And indeed it has been used in supervised settings like identifying
      and correcting inconsistencies in labeled data.
- name: Vitaly
  text: Hi Christoph! What is the best way to reach you if we would like to see your
    book translated and published in another language?
  replies:
  - name: Asif
    text: intrested
  - name: Christoph Molnar
    text: I sent you an e-mail
- name: luca pugliese
  text: I am intrigued by approaches combining more than a type of mindset, how and
    if this can be beneficial for the analysis, in particular to increase the robustness
    of a model outcomes. Can You tell us, as an example, which are the adavantages
    of doing a conformal prediction instead of a simple punctual prediction in a supervised
    classification problem? And when is advisable to do conformal predictions instead
    of predictions?
  replies:
  - name: Christoph Molnar
    text: 'Conformal prediction is a method for quantifying uncertainty in the form
      of prediction sets/intervals. I would see conformal prediction as a mixture
      of frequentist inference and supervised ML mindset, because the interval has
      a frequentist interpretation and conformal prediction also takes ideas from
      supervised ML.

      You can always do both: Get the most likely prediction and the prediction set/interval.

      A concrete example: You automatically classify financial transactions for banking
      customers, like "restaurant", "rent", ... When the classifier is unsure (based
      on some threshold), you could ask the customer to classify it. But instead of
      showing them all options, you could show them a set of transactions that contains
      the right class with (on average) with 95% probability'
  - name: luca pugliese
    text: 'Thank you. Useful example. :thank_you:'
- name: luca pugliese
  text: Thanks to Christoph Molnar for the interesting subject proposed in his book!
  replies: []
- name: Christoph Molnar
  text: "Thanks everyone for participating.  \U0001F64F\nI enjoyed your questions\
    \ and hope I could provide meaningful answers.\nIf you are interested in the print\
    \ version of the book, [you can find it on Amazon](https://bookgoodies.com/a/B0BMGSF52B)."
  replies: []
- name: Rizdi Aprilian
  text: With the advent of semi-supervised learning, in which that unsupervised learning
    merges together with supervised learning to alleviate the issue of limitation
    of labeled data availability, are there some feasible ways to do some changes
    on mindset or maybe joining both mindsets together is more than sufficient for
    this problem?
  replies:
  - name: Christoph Molnar
    text: 'A big problem in supervised ML can be that it''s difficult or expensive
      to collect labels. But if you otherwise have lots of unlabeled data, semi-supervised
      learning is a good approach.

      I suppose "this problem" again refers to lack of labels? Another approach is
      self-supervised learning where you learn to construct X from X (very simply
      speaking). But self-supervised learning is often categorized  as unsupervised
      learning as well.'
  - name: Rizdi Aprilian
    text: 'My apology for not referring the problem you mentioned, so yes this points
      to the label lacking issues.

      Following your response, I think seeing semi-supervised case with the perspective
      of unsupervised learning mindset could be more suitable.'
- name: Ajay Kumar
  text: "Hi Everyone\u2026 my question is how different modelling mindset works for\
    \ the different domains or industries to solve there business problem\u2026?"
  replies:
  - name: Christoph Molnar
    text: 'I tried to describe the modeling mindsets so they are independent of the
      industries and domains.

      But part of the mindset is that they are a bit like cultures. So in certain
      domains one mindset mind dominate. But also for the reason that the different
      mindsets have different strengths and limitations.

      But in general I would say it''s mostly task-dependent. If you want to analyze
      data to make a decision, frequentist inference might be a good approach. And
      this approach is both used in medicine to test whether a treatment works better
      than another treatment. But also in many other industries and the approaches
      used can be very similar.'
- name: Tim Becker
  text: "Hi Christoph Molnar, I know I am a little bit late. I hope you still consider\
    \ to answer my questions.\n- Can you elaborate on the concept of the \"T-Shaped\
    \ Modeler\"? How does this idea relate to the different mindsets discussed in\
    \ your book?\n- Are there any common misconceptions about these modeling mindsets\
    \ that you'd like to clarify?\n- Can you provide examples of successful implementations\
    \ of these modeling mindsets in real-world scenarios?\nThank you very much \U0001F642"
  replies:
  - name: Christoph Molnar
    text: 'T-Shaped modeler: A modeler that is an expert in a few mindsets (depth),
      but has at least a little bit of knowledge of the others (breadth). In the book
      I write that this is the most feasible form. Because being an expert in all
      mindset is difficult. But if you only know one, then you might often reach walls
      in projects and you might not even know that it''s because of limits of your
      current mindset.

      One misconception I see is to equate a model or method with only one mindset.
      So someone might say "logistic regression isn''t machine learning, it''s statistics".
      And that''s an unhelpful approach to think about modeling. Because you can end
      up with a logistic regression model when you approach the model with a frequentist
      mindset, but also when you used supervised ML mindset. But in both cases the
      use and interpretation of the model would differ.

      Any model comes from some mindset. So any application of modeling data is a
      real-world application of a mindset. It''s just not often explicit which mindset
      was behind the modeling. And often in real-world scenarios a mix of mindset
      is used. For example in a successful project you might build a prediction model
      (supervised ML) but you also got some insights through clustering (unsupervised
      ML) and you also tested your sample whether there are significant differences
      between certain groups (frequentist inference).'
  - name: Tim Becker
    text: "thank you four your answers \U0001F642"
- name: Alexey Grigorev
  text: I remember seeing your post on LinkedIn about using GPT for writing this book.
    How did you use it and how much of the content is written/edited by GPT?
  replies:
  - name: Christoph Molnar
    text: 'When I wrote this book only GPT-3 was available. So the only thing I used
      was to get inspiration for the short stories that are at the beginning of each
      chapter.

      I used GPT-4 a lot more for the book I''m currently writing (about Shapley values).
      But mostly for editing the book, like fixing grammar and shortening sentences
      a bit.'
  - name: Alexey Grigorev
    text: Thank you!

---

Books on modeling often jump right into math and methods. Drowned in detail, it can take years to appreciate the assumptions and limitations of the various modeling mindsets. Written in a clear and concise style, Modeling Mindsets introduces approaches such as Bayesian inference, supervised learning, causal inference, and more.

After reading this book, you will have a much better understanding of the different approaches to modeling and be able to choose the right one for your problem.