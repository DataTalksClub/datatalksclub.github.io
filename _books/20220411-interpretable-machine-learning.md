---
authors:
- christophmolnar
cover: images/books/20220411-interpretable-machine-learning/cover.jpg
description: Book of the Week. Interpretable Machine Learning by Christoph Molnar
end: 2022-04-15 23:59:59
image: images/books/20220411-interpretable-machine-learning/preview.jpg
links:
- link: https://christophm.github.io/interpretable-ml-book/
  text: Book's website
- link: https://www.amazon.com/Interpretable-Machine-Learning-Making-Explainable/dp/B09TMWHVB4/ref=sr_1_1?qid=1647836815&refinements=p_27%3AChristoph+Molnar&s=books&sr=1-1&text=Christoph+Molnar
  text: Buy on Amazon
- link: https://github.com/christophM/interpretable-ml-book
  text: GitHub repository
start: 2022-04-11 00:00:00
title: Interpretable Machine Learning

archive:
- name: Daniel
  text: "Hi Christoph Molnar, thank you very much for doing this. I would like to\
    \ know:\n- Who is the target audience for this book?\n- Meanwhile there are several\
    \ approaches available to explain AI algorithms. I guess there is no free lunch\
    \ and it depends on the use case, but out of your experience: Do you have any\
    \ personal favorite among all the tools/ techniques? Maybe one that tends to be\
    \ used most often? \n- With the rise of bigger and more and more complex models\
    \ it's probably getting even harder and harder to explain these black box models.\
    \ What do you think are the most challenging things with regard to explainable\
    \ AI in the future? Any ideas how to solve it and where this finally leads us?\n\
    - Is there any specific advice you have for beginners in ML with regards to explainable\
    \ AI? \nMany thanks in advance! \nCheers\nDaniel"
  replies:
  - name: Christoph Molnar
    text: "Hi Daniel, thanks for these questions.\n1. Interpretable Machine Learning\
      \ is for everyone who wants to learn how we can explain machine learning models.\
      \ I know that many data scientists who build predictive models themselves are\
      \ readers of the book. Then there are students and teachers of machine learning,\
      \ but also technical managers and many other people.\n2.  Really depends on\
      \ what you want to do. Shapley/SHAP is a good all-rounder for both explaining\
      \ individual predictions, but also summarizing what the model does in general.\
      \ If you want to know feature importance, the Permutation Feature Importance\
      \ is a good go-to approach.\n3. We have many interpretation tools that are model\
      \ agnostic, so your models becoming more complex is not necessarily the biggest\
      \ issue. One of the challenges I see is in adapting the interpretability to\
      \ the target audience: People trained in understanding linear regression models\
      \ might easily understand any explanation in the form of a weighted sum. But\
      \ others would have a hard time. Another challenge: For some interpretation\
      \ methods it's not 100% clear how we should interpret them, or if they even\
      \ do what we want them to. For example, saliency maps for neural networks are\
      \ quite problematic. \n4. I think explainable AI can be a great tool, especially\
      \ when you want to learn ML. Explainable AI tools can give you some more intuition\
      \ about the workings of machine learning. For example, you should see the effect\
      \ of regularization in feature effects and importance. Feature effect curves\
      \ will reveal differences in how different models model relationships between\
      \ features and the target: A feature effect curve for an SVM looks completely\
      \ different from a decision tree. For beginners, I believe it makes sense to\
      \ invest some time also in explainability."
  - name: Daniel
    text: Thank you! :)
- name: Matthew Emerick
  text: "Hey, Christoph Molnar! We really appreciate you doing this. \nDoes choosing\
    \ an interpretable algorithm add a layer of algorithmic complexity to a model?"
  replies:
  - name: Christoph Molnar
    text: 'It can. That depends on how your chosen interpretation approach works.
      So-called post-hoc or model-agnostic methods are applied after the model was
      trained. So it does not add to the model prediction or training complexity.  You
      can read more about model-agnostic [in this chapter of my book](https://christophm.github.io/interpretable-ml-book/agnostic.html)

      Other interpretation tools can modify how the model is trained. For example,
      adding monotonicity constraints. Those methods may increase the algorithmic
      complexity'
- name: Kwang Yang Chia
  text: 'Hi Christoph Molnar! Thank you so much for doing this. I would like to know:

    1. What industries would greatly benefit from explainable AI more so than others?

    2. Considering the popularity of deep learning (and therefore the popularity of
    black-box models), where would explainable AI fit in Data Science?

    3. What are the typical methods that make black box methods more interpretable?'
  replies:
  - name: Christoph Molnar
    text: "1. Good question. As a rule of thumb I would say that interpretability\
      \ is required when only making predictions is not enough, but you also want\
      \ to learn from your model about the world. Anything science-related. Imagine\
      \ you build a prediction model for whether some crop will grow on a certain\
      \ location. Maybe the model is really good at prediction. But you might also\
      \ want to know what the important factors were, understand what makes a plant\
      \ thrive and what factors limits its growth. Marketing is another example: A\
      \ churn model is much more useful when you have an idea why the customers are\
      \ turning the backs on your company.\n2. As a data scientists you can be in\
      \ the position to convince others (like management) that your model is robust\
      \ and brings benefits. I know some places which would not accept black box models,\
      \ since they don't trust such opaque models. Interpretability can close this\
      \ gap, and make black-box models more appealing for many business cases.\n3.\
      \ A big question to ask, I could copy the content of my book here  \U0001F604\
      . But the short answer: Shapley values/SHAP and LIME are popular methods that\
      \ can explain individual predictions. LIME and  SHAP are quite flexible and\
      \ can produce explanations for tabular data, text data and image data. Then\
      \ we have methods that can explain the average behavior of a machine learning\
      \ model. The permutation feature importance can tell you for example how important\
      \ a feature was for the correct prediction or classification (on average for\
      \ the entire dataset). If you want to know the effect that a feature has on\
      \ the prediction Some data scientists would not use black box models in the\
      \ first place, but instead use model that are already interpretable: Generalized\
      \ additive models, decision rules and decision trees, ..."
  - name: Kwang Yang Chia
    text: "Thank you for your answers! Very informative, and I learned something new.\
      \ \U0001F604\nJust one more question - Are there any developments that seek\
      \ to improve the interpretability of current models (e.g. anything that helps\
      \ with the interpretability of Deep Learning models, for example?)"
  - name: Christoph Molnar
    text: 'There are many, and it''s difficult to keep an overview here.   Here just
      one example: [https://proceedings.neurips.cc/paper/2015/file/ced556cd9f9c0c8315cfbe0744a3baf0-Paper.pdf](https://proceedings.neurips.cc/paper/2015/file/ced556cd9f9c0c8315cfbe0744a3baf0-Paper.pdf)

      Deep Convolutional Inverse Graphics Network -&gt; This paper proposes to disentangle
      image representations within a neural network. Instead of allowing any neuron
      to learn anything, they try to force individual neurons to be responsible for
      separate attributes like pose or light.'
  - name: Christoph Molnar
    text: Disentanglement in general is a big topic for increasing deep learning interpretability.
  - name: Kwang Yang Chia
    text: "Thank you for the insight! Really appreciate it \U0001F604"
- name: Jasmin Classen
  text: "Hi Christoph Molnar , thanks so much for doing this. My question(s) would\
    \ be: \nFrom your experience, what are the most common Use Cases where you would\
    \  use explainable ML in practice? What audiences of your model could benefit\
    \ from this? E.g. gaining trust from technical vs non-technical stakeholders,\
    \ for your own / team-internal projects to understand your own model, anything\
    \ else?  Maybe you have some concrete examples when you used explainable ML in\
    \ practice?"
  replies:
  - name: Christoph Molnar
    text: "A common use case is also model debugging: With interpretation techniques,\
      \ you can quickly see if something goes completely wrong. Like one of the features\
      \ being, unexpectedly, one of the most important features could hint at something\
      \ like target leakage. I used interpretability for checking if my model makes\
      \ sense, get ideas for feature engineering, and so on.\nFor example, I once\
      \ built a classifier for financial transactions. It was an interpretable model,\
      \ so we could check against domain expertise whether the decision rules within\
      \ that model made sense. This was very reassuring to see, before we gave the\
      \ model into production \U0001F601"
  - name: Jasmin Classen
    text: Cool, thanks so much! Have you ever used any of the methods to help stakeholders
      understand your models?
  - name: Christoph Molnar
    text: 'I''ve used random forest feature importance and partial dependence plots.

      None of the newer methods because I have moved on to doing research. I know
      of many practitioners who regularly use Shapley values, permutation feature
      importance, LIME and so on.'
  - name: Jasmin Classen
    text: Thanks so much, really interesting!
  - name: Vladimir Finkelshtein
    text: "Often, when I train my first models, the most important feature is usually\
      \ the one, which I later discover drifted in distribution the most between training\
      \ and validation sets \U0001F61E So it is a nice way to know what you are overfitting\
      \ to."
- name: Vladimir Finkelshtein
  text: Your book contains many established and somewhat acceptable methods in the
    industry like LIME, SHAP and counterfactuals, etc. Are there some approaches that
    you see as promising and would include in the 3rd edition of your book?
  replies:
  - name: Christoph Molnar
    text: 'One topic I wanted to add is eep learning-specific attention mechanisms.

      Then mostly I will have to update many of the old chapter, because a lot of
      great research is coming out scrutinizing these more established methods.'
- name: Vladimir Finkelshtein
  text: How do the interpretability algorithms handle interdependencies in the data?
    For example, if I trained logistic regression and included features `X` and `X***3*`
    (which might make sense for certain use case), it does not help me to know what
    would have happened if I increased `X` and decreased `*X***3`. What if I trained
    a model where I am not aware of interdependencies between features, but they exist
    and are more complicated?
  replies:
  - name: Christoph Molnar
    text: 'Poorly. Most methods handle interdependencies poorly.

      And the interdependencies problem is both a technical but also a deeper problem.
      Interpretation often means isolating a single feature, and studying how changing
      this feature changes the prediction.

      But with dependencies, does it even make sense to study the feature in isolation?

      That''s why I would recommend to study the interdependencies before using interpretability
      methods. You can have a look at the correlations between the features, but also
      use more complex dependence measures such as HSIC.

      In the case of your example, you could technically wrap this transformation
      where you compute `x**3`  and make it part of the model. Then you could study
      how increasing `x` changes the prediction through both logistic regression terms.'
  - name: Vladimir Finkelshtein
    text: "Our company in industrial data science (metallurgy) has quite a few use\
      \ cases where it makes sense to explicitly study one feature in isolation, where\
      \ almost all of the features in the model are very heavily interdependent. There\
      \ is academic research about these interdependencies for decades and only small\
      \ subset of them is understood. Once you consider hundreds of features, there\
      \ is basically no way to know what\u2019s going on. We know for fact that everything\
      \ is correlated with almost everything, but the relations are very complex to\
      \ model, so recreating your suggestion with `x**3` is unfortunately out of question\
      \ \U0001F61E"
- name: Integralytic Team
  text: Christoph Molnar Thank you for sharing your book this week. What would you
    recommend with regard to explaining NLP models, particularly using Spark NLP and
    Spark ML? We are trying to understand how to explain which words or word combinations
    influence NLP predictions.
  replies:
  - name: Christoph Molnar
    text: "I think NLP is the topic that got the least attention in my book \U0001F605\
      \ (pun intended)\nTechnically, LIME and SHAP work. In the case of text, they\
      \ both work by similar mechanisms: For a given text and classification, they\
      \ create snippets of this text with some of the words missing, then get the\
      \ model prediction / classification score. Changes in the prediction are then\
      \ attributed to the individual words.\nIf you are using a deep learning approach\
      \ with some attention mechanism you could also look at visualizing the weights\
      \ (although some say that attention make poor explanations)."
  - name: Christoph Molnar
    text: 'For Shapley values there seems to be a Spark version: [https://pypi.org/project/shparkley/](https://pypi.org/project/shparkley/)

      I haven''t tested it.'
  - name: Integralytic Team
    text: Thank you!
- name: Clara B.
  text: What is in your eyes the most neglected area in machine learning interpretability
    research or the area with still the highest potential?
  replies:
  - name: Christoph Molnar
    text: 'Studying how users interpret the results and what the best interpretation
      output for a given audience is.

      These real-world studies are difficult to do. There are some human studies,
      but they are usually conducted with Amazon mechanical turk or with surveys of
      students.'
  - name: Christoph Molnar
    text: And the tasks are quite artificial, so it's difficult to translate results
      into how people would understand the black-box interpretations in a real application.
- name: Clara B.
  text: Will your book be translated to other languages?
  replies:
  - name: Christoph Molnar
    text: 'Interpretable Machine Learning has translations into Chinese, Japanese,
      Spanish, Bahasa Indonesia, Korean, and Vietnamese. See her: [https://christophm.github.io/interpretable-ml-book/translations.html](https://christophm.github.io/interpretable-ml-book/translations.html)'
- name: Max Payne
  text: 'Hi, does your book touch upon ExplainableAI (i.e. deep learning/NN instead
    of ML)

    If not, how different would the two be?'
  replies:
  - name: Christoph Molnar
    text: 'It does! First, all model-agnostic methods can also be used for deep learning
      as well by.

      And an entire part of the book is dedicated to interpreting deep learning approaches:
      [https://christophm.github.io/interpretable-ml-book/neural-networks.html](https://christophm.github.io/interpretable-ml-book/neural-networks.html)

      This part covers:

      - Visualizing learned features (feature visualization)

      - Pixel attribution aka saliency maps

      - Concept detection (TCAV)

      - Adversarial examples

      - Influential instances'
- name: build-failing
  text: "Hello Christoph Molnar, it would be great if you could consider answering\
    \ the following questions regarding interpretability of deep learning models:\n\
    1. Looking at things from a deep learning for computer vision standpoint, the\
    \ go-to techniques for explainability are: CAM, and the improved GradCAM, GradCAM++.\
    \ \n2. Does the book go over these topics as well? Or would you be covering these\
    \ topics in the next edition?\n3. Recently, there have been significant research\
    \ efforts on the use of causal attribution to addressing explainability. I would\
    \ like to know your thoughts on the same.\n4. On the ML front, does the book cover\
    \ simple yet intuitive techniques such as partial dependency plots--on the various\
    \ features so that we can make a more informed decision on the set of features\
    \ that the model is actually using in its decision-making process.\nThank you\
    \ in advance."
  replies:
  - name: Christoph Molnar
    text: '1. and 2. Grad-CAM and similar appraoches are covered in this chapter:
      [https://christophm.github.io/interpretable-ml-book/pixel-attribution.html](https://christophm.github.io/interpretable-ml-book/pixel-attribution.html)

      3. I haven''t covered causal attributions so far. My take at the moment is:
      You have to approach causality already when you fit your model. Meaning you
      need a causal model when you want to have a causal interpretation.

      4. The book covers many of the simpler approaches:

      PDP: [https://christophm.github.io/interpretable-ml-book/pdp.html](https://christophm.github.io/interpretable-ml-book/pdp.html)

      Permutation Feature Importance: [https://christophm.github.io/interpretable-ml-book/feature-importance.html](https://christophm.github.io/interpretable-ml-book/feature-importance.html)'
  - name: build-failing
    text: Thank you very much for your detailed reply, and for pointing me to these
      references.
- name: CJ
  text: As model risk becomes increasingly important to businesses, interpretability
    will likely need to be more incorporated into business practice. Does your book
    address the various use cases for interpretability?
  replies:
  - name: Christoph Molnar
    text: 'The book is more centered around the methods rather than specific use-cased.
      Some motivation for why we need interpretability can be found here: [https://christophm.github.io/interpretable-ml-book/interpretability-importance.html](https://christophm.github.io/interpretable-ml-book/interpretability-importance.html)'
- name: naaavI
  text: What is your approach to ensembles results explanation? Especially with different
    approaches inside? Christoph Molnar
  replies:
  - name: Christoph Molnar
    text: 'For ensembles you can also use model-agnostic methods. You view your ensemble
      as one model: Input data comes in and you get the prediction. Then you can still
      calculate, for example, permutation feature importance or explain individual
      predictions with Shapley values.

      With model-agnostic interpretation methods it does not matter how many models
      are inside the ensembles or how complex they are.'
- name: naaavI
  text: Do you really uncover unsulervised learning algorythms results interpretation
    for absolute beginners?
  replies:
  - name: Christoph Molnar
    text: Not sure I interpret the question correctly. Is your question whether beginners
      can understand the results of interpretation methods?
  - name: naaavI
    text: Yeah, a kind of.
  - name: Christoph Molnar
    text: I do think there needs to be some training how to interpret the outputs
      correctly. For example what it means if permutation feature importance is zero.
      Or how to interpret Shapley values.
- name: naaavI
  text: 'What i your definition of explanation ?: i mean - explain how the figures
    are calculated , or how to interpret results in different business cases?'
  replies:
  - name: Christoph Molnar
    text: The word "explanation" is a bit fuzzy and used differently by different
      people. In the context of explaining black box models, it's often used as "explaining"
      how the model made a prediction. And explanation is often equated to attributing
      the prediction to the input features.
- name: Tim Becker
  text: Hi Christoph Molnar, could you provide us with some intuition on how SHAP
    and LIME methods work and point out the differences between the methods? Are there
    situations when you would select one over the other?
  replies:
  - name: Christoph Molnar
    text: 'Intuition LIME: We can explain a single prediction by approximating the
      complex prediction function with a simpler model, like a linear regression model.
      Idea is: We fit this linear model only with data that is very close to the data
      point that we want to explain.

      Intuition Shapley: We want to fairly attribute the prediction for a data point
      to the individual feature values of this data point. Shapley values tries out
      different combination of feature values to determine how much each of the feature
      values contributed towards the prediction.

      Similarity between SHAP and LIME: Both can be expressed as linear models. By
      choosing a certain kernel for LIME, you can get the same results as for Shapley
      values. But in practice, LIME uses other kernels to weight the data points in
      the neighboorhood.

      Which to use: I think that Shapley values has a more solid theory. LIME has
      the big unsolved problem how to define what the neighbourhood of a data point
      is.'
- name: Vladimir Finkelshtein
  text: 'Machine learning algorithms are always ranked/judged/hyped by their performance
    on some benchmarks datasets. On the other hand, with explainability algorithms,
    there is an example of its output, but I have not seen a systematic evaluation.

    Is there some idea of a metric for explainability algorithms? Like, we give models
    list of problems, where we already know what the explanations should be and rank
    the models? Perhaps, one can create synthetic problems, where we know causality?'
  replies:
  - name: Christoph Molnar
    text: 'There are various metrics that can be used to assess how well explainability
      methods work:'
  - name: Christoph Molnar
    text: 'Fidelity: Some explanation methods like LIME build a prediction model themselves.
      With fidelity you can measure how close the predictions of your explanations
      are to your model predictions.

      Sparsity: You can count how many features were used for your explanation. Shorter
      explanations should be easier to understand for users.'
  - name: Christoph Molnar
    text: 'Then there are human- or task oriented metrics:

      - How well can a user predict what the model will do, when the user is allowed
      to see explanations for the model?

      - How much faster are users with their task when they are also given expllanations'
  - name: Christoph Molnar
    text: 'But the main problem: There is no ground truth as we have with supervised
      machine learning.

      I would say, interpretable machine learning / explainable AI is more like descriptive
      statistics: For example, you can compute either the mean or the median.  But
      nobody tells you whether the mean or the median is the correct way to describe
      your distribution. Similarly, the interpretation computes different "descriptive
      statistics" of your model. Our goal as researchers is to make it clear what
      the correct interpretation is.'
- name: Arkadiusz Modzelewski
  text: Christoph Molnar First of all, thank you for the opportunity to ask questions
    and for a great book. I currently work as a machine learning specialist, but I
    also often think about recruiting for a PhD. One topic that I am very interested
    in is precisely explainable artificial intelligence. Would you perhaps have any
    tips for someone who wants to go for a PhD? Or do you see any areas in explainable
    and interpretable artificial intelligence that are particularly worth looking
    into as part of a research path? I see now that authors answer questions until
    Thursday, but maybe there will be an exception, so I try to ask :D
  replies:
  - name: Christoph Molnar
    text: 'I have seen so many labs starting to work on interpretability. So the field
      is becoming much more crowded.

      I would not work on another paper that tries to improve Shapley values or that
      introduces another saliency map algorithm.

      I think the most valuable is to bring more rigor to the field: Analyze what
      the limitations of existing methods are. Make sure that we better understand
      when Shapley values or other methods fail or may lead to a misleading interpretation.
      But to be honest, it can be harder to publish such papers, since it''s often
      easier to just invent some new method, unfortunately.'
- name: Arkadiusz Modzelewski
  text: 'I recently read this article: Stop Explaining Black Box Machine Learning
    Models for High Stakes Decisions and Use Interpretable Models Instead ([https://arxiv.org/abs/1811.10154](https://arxiv.org/abs/1811.10154))
    The author seems to have a rather strongly critical approach to explaining black
    box methods. Are you perhaps familiar with this article and could you let us know
    what your opinion is on the subject?'
  replies:
  - name: Christoph Molnar
    text: 'I''ve read the paper.  I don''t agree with all points, but I do agree that
      we should not use black box models for high stakes decisions.

      I wouldn''t say that what the authors call "inherently interpretable" models
      are the solution. They can also fail and are often not as interpretable as one
      thinks. I would even g say that for many of these high stake decisions we should
      not use ML at all, like bail decisions.'
  - name: Arkadiusz Modzelewski
    text: Christoph Molnar Thanks a lot for your answers!

---

Machine learning has great potential for improving products, processes and research. But computers usually do not explain their predictions which is a barrier to the adoption of machine learning. This book is about making machine learning models and their decisions interpretable.

After exploring the concepts of interpretability, you will learn about simple, interpretable models such as decision trees, decision rules and linear regression. The focus of the book is on model-agnostic methods for interpreting black box models such as feature importance and accumulated local effects, and explaining individual predictions with Shapley values and LIME. In addition, the book presents methods specific to deep neural networks.

All interpretation methods are explained in depth and discussed critically. How do they work under the hood? What are their strengths and weaknesses? How can their outputs be interpreted? This book will enable you to select and correctly apply the interpretation method that is most suitable for your machine learning project. Reading the book is recommended for machine learning practitioners, data scientists, statisticians, and anyone else interested in making machine learning models interpretable.