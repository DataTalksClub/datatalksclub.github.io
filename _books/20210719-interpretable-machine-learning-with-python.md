---
title: "Interpretable Machine Learning with Python"
description: "Book of the Week. Interpretable Machine Learning with Python by Serg Masis"
cover: "images/books/20210719-interpretable-machine-learning-with-python/cover.jpg"
image: "images/books/20210719-interpretable-machine-learning-with-python/preview.jpg"
start: 2021-07-19 00:00:00
end: 2021-07-23 22:59:58
authors: [sergmasis]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/interpretable-machine-learning-with-python/9781800203907
  - text: Page on Amazon
    link: https://www.amazon.com/Interpretable-Machine-Learning-Python-hands/dp/180020390X
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Interpretable-Machine-Learning-with-Python

archive:
- name: Carsten Schnober
  text: For a next generation of state-of-the-art ML models, do you think explainability
    will be somehow "embedded" into the models (as opposed to ANNs)?
  replies:
  - name: "Serg Mas\xEDs"
    text: 'Hi Carsten. Don''t know what exactly you mean by "embedded". There''s an
      issue of transparency through the property of model explainability which means
      so called "black-box" models are inherently disadvantaged in this regard. However,
      it''s not the only important transparency property available nor a reason to
      disqualify ANNs because they can be queried in other meaningful ways. That being
      said, if you want state-of-the-art models that retain the same explainability
      properties of white box models, there are glass box models like this one: [https://interpret.ml/docs/ebm.html](https://interpret.ml/docs/ebm.html)
      and many more derived from Bayesian Rule Lists or Trees, not to mention new
      causal modeling methods.'
- name: Shankar Somayajula
  text: "Hi Serg Mas\xEDs How is Interpretable ML different from BI with ML specific\
    \ visualizations? Isn't this EDA on model outputs with KPIs relating to model\
    \ performance -- ML model scoring generates predictions/outcomes which one slices\
    \ and dices as per interest/motivation."
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Shankar. You pose a very interesting question. Indeed I see Interpretable
      ML as a very similar exercise as BI. It can slice and dice model performance
      (often called error analysis) but should ideally delve into issues of fairness,
      uncertainty, robustness, consistency, etc. Of course, many of these look at
      the distribution of model performance from other angles but you can also learn
      from feature importance, feature interactions and partial dependence. These
      help inform model improvements and even business decisions (much like BI can)
  - name: Shankar Somayajula
    text: "Serg Mas\xEDs Thanks a lot for your response. Yes, i agree that there are\
      \ many other areas of focus in addition to performance. Also the feature related\
      \ functionality isn't as straight forward as typical BI use cases and falls\
      \ more into the realm of Data Science/ML.\nI come from a BI background and found\
      \ the ML Classification based Confusion Matrix Metrics good candidates for leveraging\
      \ BI self service practices ... this exploration led to Interpretable AI which\
      \ is indeed a vast field.\nOne of the ways that BI can add value is by way of\
      \ data modeling (not ML modeling) ... by leveraging a data model (sql schema)\
      \ to store the ML outputs with various dimensions/attributes, we should be able\
      \ to do things which are now done via UI/Self Service vizualizations via a backend/api\
      \ call and automate many manual operations.\nSay, we have an ML model and its\
      \ predictions, given a new Dataset for scoring, and a candidate list of relevant\
      \ attributes (col1, col2...col8) for the exercise in question, find the subset/sub-population\
      \ within these attribute slices where &lt;measure=accuracy/f1_score/precision/sensitivity&gt;\
      \ falls below 10% of the value evaluated over &lt;overall data/training data/new\
      \ Data&gt;... This can throw up 3-4 slices like col4=&lt;a&gt;, col6=&lt;b&gt;,\
      \ col6=&lt;c&gt; where this model degradation does indeed happen and then the\
      \ user/expert goes on to visualize/explore those sections of the data using\
      \ the UI. Otherwise discovery depends on analysts stumbling upon the right subset\
      \ of interest visually in a self-service but manual mode of operation."
  - name: "Serg Mas\xEDs"
    text: Yes! We definitely need to store model meta-data much more than is practiced.
      This would include things like performance metrics, fairness metrics, variance
      of performance against hold-out datasets to show reliability, sensitivity analysis
      for uncertain inputs hyper-parameters used in training, data provenance, and
      much more. Ideally we could use data like this to certify models in all sorts
      of dimensions.
- name: Akshaya Natarajan
  text: 'Hi Serg! The book looks really interesting. I have a couple of questions:

    1) I''m currently working with ResNets and most of the times don''t get how to
    interpret certain results. What''s the best way to go about interpreting DL models?

    2) How can we use Interpretability to detect bias in the ML model?'
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Akshaya! Thank you for your questions 1) There are many ways of interpreting
      DL models depending on the data type (image, text, tabular, time series,...)
      and/or model architecture (CNN, RNN,...). You mention Resnets so I take it you
      are interested in Convolutional Neural Networks (images). I would start by understanding
      the layers with intermediate activations. Then chose examples to study and apply
      gradient based methods (GradCam, etc) and Permutation based methods (SHAP,...)
      to interpret the outcomes of the model. 2) It is tough to detect bias in any
      model but images is particularly challenging because so far the only methods
      available focus on disparities of representation and outcomes, and don't go
      deeper. If you are interested I explain fairness in more detail in
      [the talk I did for deeplearning.ai](https://www.youtube.com/watch?v=A0ADFiiZU0k).
  - name: Akshaya Natarajan
    text: Thanks a lot for answering Serg!! Will definitely checkout the video.
  - name: "Serg Mas\xEDs"
    text: Your welcome!
- name: Dr Abdulrahman Baqais
  text: "Hi Serg Mas\xEDs. Thanks for the book and for your time to answer our questions.\n\
    1) Interpretable models is a general term that different stackholders define it\
    \ differently. It is different for a technical team, than a business users, than\
    \ a client than an auditing entity like a government or ethical board.\nThe question\
    \ is : to whom we should provide Interpretable models? Should we have different\
    \ Interpretablity to different types of the above  stakeholders? \n2) In today\
    \ enterprise ML pipeline, shall we include Interpretablity in the ML pipeline\
    \ or operatingodel. Probably after the deployment or maybe as part of ethical\
    \ auditing or should we do it only when it is required.\n3) which roles of ML\
    \ team take care of Interpretablity: DS, ML engineer , a combination of both or\
    \ we need a separate role with advanced math skills probably to do the task?\n\
    4) Can Interpretablity be evolved into a separate business model by itself: something\
    \ like Interpretablity as a service.\n5) Shall we consider Interpretablity as\
    \ a default embedded part of the product shipped to the customer? Or is it a separate\
    \ entity in which we can charge the customers differently? \n6) Shall we sacrifice\
    \ little of accuracy to obtain higher Interpretablity even though can sometimes\
    \ result in profit reduction? \nThank you so much.\U0001F44D \U0001F4AF \U0001F64F"
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Abdul. I much appreciate your questions. I saved you questions for last.  They
      are very good. It's been a long day for me so I hope you don't mind if I answer
      tomorrow.
  - name: Dr Abdulrahman Baqais
    text: "Thank you Serg Mas\xEDs. Sure. Whenever you have time."
  - name: "Serg Mas\xEDs"
    text: Hi Abdulrahman. 1) Indeed. You would use different interpretation methods
      for different stakeholders. The technical team tasked with training and deployment
      should implement and test all pertinent methods to their models. Business stakeholders
      might be interested only in predictive performance and feature importance. However,
      ethical board and auditors might be only interested in results from fairness
      and robustness tests. Government might be interested in sensitivity analysis
      or whatever compliance tests they have coded in their regulation. As for the
      end-user, they might want an explanation attached to their predictions. 2) I
      hope that it will become standard practice to use ML interpretability methods
      in each step of the pipeline. I think in the future modeling will be done primarily
      through drag and drop interfaces which will have more a cockpit feel to it than
      it does right now alerting practitioners of all sorts of issues with data, models
      and outputs and allowing them to correct these as they go along. This embedding-interpretable-ML-in-the-pipeline
      approach will make ML more responsible - although I believe making it ethical
      will require often a better understanding about the data collection process
      which is often outside of the purview of the ML pipeline, so it won't cover
      all bases but I'm hoping that by freeing up some time from ML practitioners
      from the nuts and bolts of programming modeling they can focus on other issues.
  - name: "Serg Mas\xEDs"
    text: 3) Right now engineering is an important skill to have in ML modeling. However,
      in a world where most data engineering and modeling doesn't require programming
      but more interpretation of statistics, engineering belongs more in MLOps and
      ML research roles. However, it would open up the floodgates for folks that are
      data-savvy non-programmers but domain experts to participate in modeling. I
      think it still makes sense for these folks to be knowledgeable in statistics
      (ML engineers aren't necessarily). The focus on interpretation, will heighten
      the importance of statistics, and it is the more the domain of data scientists
      than ML engineers. 4) It already has. I've seen a few startups offer this service.
      5) It should eventually in a model that comes with something like a manifest
      with everything from data provenance to feature importance pre-defined and an
      explanation given automatically with every prediction 6) Definitely. I see the
      value of models that can perform more transparently, fairly and reliably outweigh
      the risks of just having a higher predictive performance. Higher profits may
      come with many risks. A model that is right 99.6% of the time might be right
      for the wrong reasons 0.3% of the time and that can eventually backfire. I rather
      take a model that is right 99.4% of the time but only right for the wrong reasons
      0.01% of the time.
  - name: Dr Abdulrahman Baqais
    text: "Thank you Serg Mas\xEDs for your time and detailed answers. Very insightful."
- name: Jeff Herman
  text: Hi Serg.  There are a lot of different machine learning interpretability techniques
    (LIME, SHAP, Anchors, Permutation Importance, etc), is there one such technique
    that you find yourself using more?  Follow up question, is there one such plot
    or visualization that you use a lot?  For example - I see feature importance with
    tree based models in sklearn used a lot, do you find yourself using one technique
    a lot like SHAP  summary plot?
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Jeff. I personally use SHAP the most during my modeling pipeline but
      I've implemented Anchors into the inference engine of my projects so it has
      probably been used more times by end-users than I have used SHAP making the
      models. SHAP's summary plot I use a lot but I use interaction plots probably
      slightly more because in my line of work understanding feature interactions
      is critical.
- name: Alper Demirel
  text: "Hi Serg Mas\xEDs, thanks for being with us.\nWhat was your goal in writing\
    \ this book? Do you believe you have achieved your goal?"
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Alper. Thank you for your question. My goal was to 1) create a comprehensive
      book about interpretability methods 2) while doing it convince ML practitioners
      of its importance. The first goal was acheived I think although I had to leave
      some important topics out (namely, privacy). As for the second goal, I think
      for years now Ive seen it make appearances in conferences but it still was a
      bit under the radar for industry. You had AI Ethicists and Academic Experts
      and some business folks champion XAI / IML but all the people that actually
      work with data in industry weren't getting that involved. Its hard to believe
      because my book was only published this year but it was the third book ever
      on IML / XAI for practitioners but I think the topic is becoming more top of
      mind to the audience the book was written for. So its a work in progress but
      I believe its making in roads.
- name: Alexey Grigorev
  text: Is there any difference between explanability and interpretability? (I.e.
    between explainable AI and interpretable AI)
  replies:
  - name: "Serg Mas\xEDs"
    text: In theory (i.e. academic literature) it does because explainability and
      interpretability are usually not used interchangeably but, strangely, Explainable
      AI and Interpretable ML are. Not sure about variations like Interpretable AI
      and Explainable ML but they likely, in practice, synonyms. It gets confusing
      because interpretation methods output explanations which we interpret. As for
      definitions of all the terms you mentioned. There are many definitions of *explainability*
      but it's more focussed on the inner workings of the model (the how the prediction
      is made), whereas definitions of interpretability specially when referred to
      as *post-hoc interpretability* is more about why is a prediction is made. For
      that reason it is perfectly content with black box models. As for *Interpretable
      ML* (aka *Explainable AI*) its the collection of methods used to understand/debug
      models on three levels (Fairness, Accountability, Transparency) and even make
      improvements in those aspects.
  - name: Alexey Grigorev
    text: 'Thanks!

      so explainability = I can explain how it works internally

      while interpretability = I can interpret the output and understand why model
      made this particular prediction

      correct? Or not?

      I think I''m still a bit confused...

      Maybe we can try an example? Let''s say we have a resnet model which predicts
      cats and dogs. What would be explainability and interpretability for this case?'
  - name: "Serg Mas\xEDs"
    text: Yes correct, Alexey, although in a Venn diagram Intepretability includes
      explainability because transparency is a property of interpretability. In other
      words, it helps to understand how the model works to explain why it made predictions.
      As for your example regarding the ResNet, methods like  intermediate activations
      help you visualize each layer in action (and activation maximization per filter)
      . These help you with the explainability because you can understand how they
      work. On the other hand, methods that just show you a map of what parts of the
      image, according to the model, tell it is a cat or a dog (such as Integrated
      Gradients, GradCam or SHAP)  help with interpretability because they don't tell
      you how the model works but why it is working (or not!).
  - name: Alexey Grigorev
    text: Clear, thank you!
  - name: Leonoor Tideman
    text: "I love the question Alexey Grigorev because I used to find this genuinely\
      \ confusing \U0001F923\nBased on what I have seen in XAI &amp; IML, most researchers\
      \ and practitioners indeed use \"explainable AI\" and \"interpretable ML\" interchangeably.\
      \ I guess it is partly because the field of XAI &amp; IML is still relatively\
      \ new and pp have not get agreed on one technical definition. When I entered\
      \ the field (2019), one of the few general references was the _Interpretable\
      \ Machine Learning Book_ by Molnar (PhD student in Germany). Molnar was one\
      \ of the first pp to organize all sorts of (sometimes very different) methods\
      \ under the name of \"interpretable ML\".\nThe main proponent of differentiating\
      \ between \"interpretable ML\" and \"explainable AI\" is Cythia Rudin (professor\
      \ at Duke University in the USA). She defines IML as being about models that\
      \ are inherently interpretable (e.g. linear/logistic regression, decision trees),\
      \ whereas XAI is about generating post-hoc explanations (generally in the form\
      \ of feature attributions) for arbitrarily complex black-box models. So, according\
      \ to Rudin, XAI is about using a interpretable model to explain the original\
      \ black-box predictive model. I highly recommend [Rudin's paper](https://www.nature.com/articles/s42256-019-0048-x#Sec2).\
      \ I like her approach, but as mentioned by Serg Mas\xEDs her perspective is\
      \ not widely shared within the community."
  - name: "Serg Mas\xEDs"
    text: Yes call me one of those that don't agree with her view. If anything her
      definitions for XAI and IML should be flipped since the term explainable is
      more optimistic, for lack of a better world, than interpretable. I honestly
      don't think the term explainable belongs anywhere near statistics (and much
      less neural networks) since even the most basic methods from hypothesis testing
      to linear regression coefficients are not infallible and self-explanatory and
      thus require an interpretation within a margin of error.
- name: Emily Tran
  text: Do you need to understand the business 100% to be able to build interpretable
    ML model/neuro network?
  replies:
  - name: "Serg Mas\xEDs"
    text: Maybe not all the business, but the better you understand the business related
      to the data, the better you can interpret the models trained with that data.
      However, in the absence of domain knowledge you can learn so much about the
      data through the model. It can help with EDA.
- name: Marcello La Rocca
  text: "Hi Serg Mas\xEDs\nThanks a lot both for Q&amp;A!\nYour book looks great,\
    \ congrats!!!\nQuestion: as of today, how far would you say we are with the adoption\
    \ of interpretable machine learning? E.g. what percentage of models used in production\
    \ would you estimate are interpretable?"
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Marcello. Interpretable and explainable are loaded terms. In the context
      of my book, all models are "interpretable" in the sense that they can be interpreted
      through model-agnostic or deep learning specific methods. However if by "interpretable"
      you mean that transparent, I would estimate that 90%+ of production models are
      "black box models" so they are more opaque. My book doesn't discriminate against
      this kind of model since post-hoc interpretability is possible in a model or
      system with known inputs and outputs, although I wont lie that transparency
      helps with the reliability of the methods, and ease of interpretation. Therefore,
      what makes a model interpretable is not exclusively its nature (class, architecture,
      etc) but that ML practitioners know how to and are actively interpreting models.
  - name: Marcello La Rocca
    text: Thanks!
- name: Marcello La Rocca
  text: 'Question 2: What''s your favourite interpretable alternative to NNs? What
    about GAMs (generalized additive models, with or without pairwise interaction),
    do you think they can be as effective as claimed, in comparison to NNs?'
  replies:
  - name: "Serg Mas\xEDs"
    text: 'Neural networks come in many flavors so it depends. I wouldn''t use anything
      other than CNNs for images - it actually surprisingly interpretable. With graph
      data you have more options like SVMs but NNs are my default. For univariate
      time series, statistical methods (Garch, ARIMA, etc) are much better than RNNs
      but not necessarily for multivariate. As for text, transformers rule in accuracy
      and even interpretability (an improvement from RNNs - even bidirection ones).
      Last but not least, for tabular data I do so as an example in the book because
      I know lots of people use NNs with tabular but honestly I can''t think of any
      good reason to use NNs on tabular data considering better alternatives. My preferred
      model classes for tabular are decision trees and ensembled decision trees (random
      forest, XGboost, etc). They tend to perform equal or better than NNs, overfit
      much less and are easier to tune - you can use monotone and interaction constraints
      also to place guardrails. As for GAMs, they are good alternatives if you require
      more transparency however there''s a trade-off with predictive performance.
      That being said, there''s a gradient boosted GAM that attempts to not compromise
      on performance which I cover in my book: [https://interpret.ml/docs/ebm.html](https://interpret.ml/docs/ebm.html)'
  - name: Marcello La Rocca
    text: 'Thanks a lot Serg, that''s super thorough!

      I''ll take a look at EBMs, thanks!

      You mentioned transformers: I haven''t had a chance to dig into the topic, but
      I am extremely curious to, as I have read (high level) how they improve over
      RNNs. And I didn''t know they are even more interpretable! I''ll be eager to
      read about this aspect too.'
  - name: "Serg Mas\xEDs"
    text: "Yes, the problem with transformers is since they scale much better, they\
      \ are pretty much fed the entire Internet \U0001F602 and that has inevitably\
      \ led to many questions about bias (see Timrit Gebru et al's paper [https://dl.acm.org/doi/10.1145/3442188.3445922](https://dl.acm.org/doi/10.1145/3442188.3445922))"
- name: Lalit Pagaria
  text: Is there any legal framework/requirements for interpretable AI mandate by
    governments?
  replies:
  - name: "Serg Mas\xEDs"
    text: Good question Lalit. Many governments throughout the world have "frameworks"
      of some kind but in most cases they aren't requirement and when they are not
      (namely, European Union) wording is very ambiguous. For instance, GDPR for the
      EU has enacted a "right to meaningful information about the logic involved"
      for algorithmic decision-making but an explanation can come in many forms and
      levels of detail. What precise methods to use and how to deliver this explanation
      is not defined.
  - name: Doink
    text: "Serg Mas\xEDs is GDPR written by technical folks or bureaucrats?"
  - name: "Serg Mas\xEDs"
    text: "I think more of the latter but even technical folks don\u2019t have all\
      \ the answers yet. We still haven\u2019t figured out what constitutes the best\
      \ framework for providing explanations on all levels (fairness, accountability\
      \ and transparency). This might also vary according to the use case since some\
      \ need a bigger focus on fairness and others on accountability, for instance"
- name: Krzysztof Ograbek
  text: "Hi Serg Mas\xEDs, thank you for doing this! 2 Questions:\n1. Do you think\
    \ that ML world would benefit from having more people with a non-tech background.\
    \ I mean like artists, philosophers, etc. How could we attract such people into\
    \ the field?"
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Krzysztof. No problem. 1) definitely! I think we can open up the floodgates
      once we remove the programming requirement. I envision future ML systems would
      be drag and drop so that anybody that has an interest (hopefully more domain
      knowledge) can partake in the process.
  - name: Krzysztof Ograbek
    text: Just a follow quick follow up question. Don't you think that math is the
      main reason why AI is so scary to non-tech?
  - name: "Serg Mas\xEDs"
    text: "Math is daunting yes to many but don\u2019t think its the main deterrent.\
      \ I think there are more scientifically-minded data-savvy people without the\
      \ programming skills than those without the math skills. Mind you by math skills\
      \ I\u2019m not talking about graduate physics level math skills but college\
      \ statistics + linear algebra + calculus. Of those three, statistics is the\
      \ most important for data science. I think it\u2019s better to understand linear\
      \ algebra and calculus intuitively for practical use cases than know how to\
      \ prove a theorem."
- name: Krzysztof Ograbek
  text: 2. Is your book beginner-friendly?
  replies:
  - name: "Serg Mas\xEDs"
    text: "2) yes but It\u2019s not like a zero to hero book. It\u2019s starts at\
      \ around 0.01 \U0001F602 because I don\u2019t have a glossary for basic concepts\
      \ like what is machine learning, supervised learning or Python. The expectation\
      \ is that the reader has some ML 101 knowledge. Besides that the first three\
      \ chapters are introductory and go over the most basic models and their properties"
- name: Doink
  text: "Serg Mas\xEDs 2 Questions\nHow to deal with the tradeoff between fairness\
    \ and explainability\nIf I apply differential privacy then how to maintain fairness,\
    \ explainability and make sure that there isn't a high privacy loss."
  replies:
  - name: "Serg Mas\xEDs"
    text: "Hi Doink! 1) it depends on the type of fairness. One could argue that procedural\
      \ fairness is upholded better the simpler the model. For instance it two Branch\
      \ decision tree for credit scoring based on income is very straightforward,\
      \ and it\u2019s fair because it\u2019s the same rule for everyone. However it\u2019\
      s outcome fairness could be dismal because people that can pay back their loan\
      \ will get rejected. Personally the level of Procedural fairness I look for\
      \ is no double standards among similar people but otherwise outcome fairness\
      \ is what we should shoot for which is statistical parity among demographic\
      \ groups. The problem is Explainability is at odds with outcome fairness but\
      \ not procedural fairness. That being said you have to reduce model complexity\
      \ as much as possible by feature section/engineering, regularization, etc to\
      \ help with explainability and generalization"
  - name: "Serg Mas\xEDs"
    text: "2) for fairness there are many bias mitigation methods you can try and\
      \ assess using fairness metrics. For differential privacy you can tweak the\
      \ strength (eps) and then assess its effectiveness. There are many ways to assess\
      \ explainability. There aren\u2019t great metrics for it but if the model overfits\
      \ minimally and also is outcome fair it is likely very explainable. How to get\
      \ all three? Combine fairness methods + assessments, differential privacy (inc\
      \ assessment) and standard performance metrics (compare with hold out) into\
      \ your pipeline and optimize with all metrics in mind. You can make your own\
      \ weighted metric that combines several metrics in one and hyper parameter tune\
      \ for that. There\u2019s definitely a trade-off so bear that in mind with your\
      \ weighting."
- name: Alexey Grigorev
  text: Was there something you wanted to include in the book but eventually decided
    not to?
  replies:
  - name: Alexey Grigorev
    text: If yes, what was it and why you decided not to cover it?
  - name: "Serg Mas\xEDs"
    text: "So much! First there was two chapters originally planned on Interpretation\
      \ methods for NLP but two months after I started writing the book I found out\
      \ that Denis Rothman was about to release his XAI book (and it included some\
      \ NLP because that\u2019s his area of expertise) so I decide not to. I regret\
      \ this decision and I\u2019m considering adding one NLP chapter in the 2nd edition.\
      \ The other mayor decision was not to include a chapter on privacy preserving\
      \ ML because the book was getting too long and this topic is so big. I might\
      \ just carve some on space for an introduction to this topic in the second edition\
      \ but would have to remove a chapter. Lastly, there\u2019s a bunch of other\
      \ topics like error analysis, data augmentation techniques, causal explanations\
      \ through advanced counterfactual methods and semantic segmentation that I considered\
      \ covering, but there\u2019s only so much I can cover in a 700 page book! There\u2019\
      s so much more that meets the eye with IML. When I told some of my colleagues\
      \ that I was writing a book on IML they said sure \u201CI know SHAP and LIME\u201D\
      \ but it\u2019s much more than that (mind you SHAP and LIME is only 2 out of\
      \ the 14 chapters, and if I truly wrote about every method available it would\
      \ had been easily at least 40 chapters)."
  - name: Alexey Grigorev
    text: Maybe instead of second edition, you could have another book "advanced IML"
      =)
  - name: "Serg Mas\xEDs"
    text: Good idea, Alexey!
- name: WingCode
  text: "Hi Serg Mas\xEDs. Thank you for the Q&amp;A!\nHow do you determine bias when\
    \ you don't have access to the model but have access to the input (training data)\
    \ &amp; output of the model (model predictions), in case of machine learning\
    \ as a service platform (example: [AWS Personalize](https://aws.amazon.com/personalize/))\
    \ ?"
  replies:
  - name: "Serg Mas\xEDs"
    text: "Hi WingCode. Great question! There are two kinds of fairness that pertain\
      \ ML: outcome and procedural. Although for procedural you would at least have\
      \ to train a proxy model (with some disclaimers), the model is really not necessary\
      \ to ascertain bias when measured on the outcomes alone because you can use\
      \ the labels to determine bias on the data level and the predictions to do so\
      \ on the model level. What the metrics do is statistically measure disparities\
      \ between groups. What can make this challenging is when you don\u2019t know\
      \ what the groups are or don\u2019t even have the data pertaining the groups.\
      \ Say, gender feature was removed or differential privacy was applied to the\
      \ training data."
  - name: WingCode
    text: "Thank you for the answer Serg! \U0001F642"
- name: Agi Kajanaku
  text: "Hi Serg Mas\xEDs, can you elaborate more on how you would approach connecting\
    \ ml model usage to peripheral hardware?\nThank you!"
  replies:
  - name: "Serg Mas\xEDs"
    text: Hi Agi Kajanaku! Sorry I'm not sure what you mean by peripheral hardware?
      Mouses and keyboards? Or more like IoT devices like cameras, sensors, lights,
      locks and smart speakers? And what do mean about ml model usage? like reporting
      usage back to the cloud? Or running models in the cloud?
  - name: Agi Kajanaku
    text: "Hi Serg Mas\xEDs, apologies for the lack of clarity \U0001F605 I was thinking\
      \ more of devices like cameras and sensors and mostly running the model but\
      \ open to reporting usage too. I understand I might have missed the week mark\
      \ but if you do happen to have time, would love to learn more. Thanks!"
  - name: "Serg Mas\xEDs"
    text: "Hi Agi Kajanaku I started writing a response and then forgot to press the\
      \ send button. Now it\u2019s gone \U0001F605  Anyway, the best approach to model\
      \ training while preserving privacy in IoT devices is federated learning which\
      \ is a distributed approach. Because of this private data is never sent to the\
      \ cloud. That being said, this approach has its limitations because IoT devices\
      \ aren\u2019t known to have a lot of compute. In other words, sensors definitely\
      \ are feasible - and cameras less so. What can happen with cameras is you pretrain\
      \ models with generic data and then the IP camera doesn\u2019t send streaming\
      \ video to the cloud but run inference on the pretrained models. Occasionally\
      \ it can connect to the cloud to download model updates. Using generic computer\
      \ vision models work with things like detecting dogs and people, but not specific\
      \ people or objects like for instance, if you wanted the camera to detect one\
      \ of the people that lived in the house at the entrance and then open the door.\
      \ Facial recognition would require training a model with personal data rather\
      \ than generic and that would mean cloud involvement for now. In my apartment\
      \ I\u2019m using a Raspberry Pi, which has a more powerful processor, precisely\
      \ for that but that is of course one more device besides the IP camera."
---

Do you want to understand your models and mitigate risks associated with poor predictions
using machine learning interpretation? Interpretable Machine Learning with Python can help
you work effectively with ML models.

