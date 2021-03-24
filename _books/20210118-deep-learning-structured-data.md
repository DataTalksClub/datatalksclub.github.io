---
title: "Deep Learning with Structured Data"
description: "Book of the Week. Deep Learning with Structured Data by Mark Ryan"
cover: "images/books/20210118-deep-learning-structured-data/cover.jpg"
image: "images/books/20210118-deep-learning-structured-data/preview.jpg"
start: 2021-01-18 00:00:00
end: 2021-01-22 22:59:59
authors: [markryan]
links: 
  - text: Book's page on Manning
    link: https://www.manning.com/books/deep-learning-with-structured-data
  - text: Book's GitHub repository
    link: https://github.com/ryanmark1867/deep_learning_for_structured_data

archive:
- name: Wendy Mak
  text: 'I haven''t read the book, so apologies if these are already covered in the
    book. I have a few questions:

    - Are there any real world industrial use cases of DL for tabular data that you
    are aware of? (ie company x is using it to solve problem y etc)

    - in many instances DL does not offer any significant boost to ''traditional''
    methods such as boosted trees etc for structured data, is there any problems where
    DL is a clear winner like in computer vision and NLP?

    - if you have both structured and unstructured data as attributes for modelling,
    how would you combine DL/ traditional methods for best results, or would you use
    DL for the whole pipeline?'
  replies:
  - name: Mark Ryan
    text: "Hi Wendy Mak - great questions:\n- Companies can be a bit coy about exactly\
      \ what model they are using for particular applications, but I have heard that\
      \ companies that have to detect patterns of fraud (for example, in credit card\
      \ transactions) have been using deep learning with tabular data. Tabnet (nice\
      \ description here [https://towardsdatascience.com/implementing-tabnet-in-pytorch-fc977c383279](https://towardsdatascience.com/implementing-tabnet-in-pytorch-fc977c383279)\
      \ ) would suggest that Google is using deep learning for tabular data, but again\
      \ I don't know for sure in what areas. Nvidia has some active research on DL with\
      \ tabular data, but I expect that is directed at finding new markets for GPUs\
      \ rather than to solve their own internal work.\n- You're absolutely right that\
      \ traditional methods have been the \"go to\" for tabular data. In the book I\
      \ have a significant part of one chapter comparing an XGBoost solution of the\
      \ major coding example in the book with the DL solution. In that comparison, XGBoost\
      \ comes out slightly ahead in raw performance (accuracy and avoiding false negatives),\
      \ and DL &amp; XGBoost are roughly tied in terms of code complexity and training\
      \ time. Where DL comes out ahead is flexibility - DL could tackle problems with\
      \ tabular data that includes columns with unstructured text, for example, where\
      \ traditional ML methods would be at best clunky, and I believe it's much easier\
      \ to create a DL system that can handle a very broad range of tabular data. \n\
      - I think that one of the reasons that traditional ML has outshone DL for tabular\
      \ data is that DL has a reputation for being \"hard\". I argue in the book that\
      \ improvements in DL frameworks (e.g. integration of Keras w. TensorFlow as of\
      \ TF 2.0), along with much better DL training for non-specialists (such as the\
      \ [fast.ai](http://fast.ai) DL courses and the [deeplearning.ai](http://deeplearning.ai)\
      \ DL curriculum) eliminate that objection.\n- For tackling a problem that has\
      \ both structured and unstructured data, I would argue to keep an open mind about\
      \ DL for the whole pipeline. I mentioned tables with free-form text columns as\
      \ a simple example. Columns with JSON structures is another example. For more\
      \ use cases with, say, images and tabular data, I don't have direct experience,\
      \ but I think that such use cases would lend themselves to DL end-to-end as well.\n\
      - Finally, I wouldn't advocate DL for all tabular (or all mixed tabular/unstructured)\
      \ problems. If there isn't enough data (at least 10s of thousands of records),\
      \ or if the tabular structure is really simple, I don't see DL being beneficial.\
      \ I also think there are many applications where DL and traditional ML may be\
      \ closely matched and it may boil down to what's the simplest engineering problem\
      \ to solve. The case I try to make in the book is to keep an open mind about DL\
      \ being a valid option for problems involving tabular data."
  - name: Mark Ryan
    text: Thanks for your questions and I hope the responses are useful.
  - name: Wendy Mak
    text: yeap, thanks for the insight :))
- name: Sara Lane
  text: 'Hi Mark,

    Thanks for making yourself available for our questions.

    What inspired you to write a book about deep learning with structured data?'
  replies:
  - name: Mark Ryan
    text: Hi Sara - when I was learning about deep learning, almost all of the examples
      used in the teaching materials had nothing to do with problems from my actual
      job. Like many people, my job is all about tabular data. A sample DL application
      to classify images isn't relevant to my work. NLP is a bit more relevant, but
      what I really wanted was examples that I could apply to my job. Further, when
      I asked experts why DL wasn't suitable for tabular data, the answers they gave
      me weren't all that convincing, so I went looking for better answers, and that
      ultimately led to the book.
- name: Sara Lane
  text: Also, do you see deep learning eventually surpassing machine learning (ex.
    XGBoost) in terms of raw performance with tabular data? If so, can you specify
    what changes you think are going to happen to cause that?
  replies:
  - name: Mark Ryan
    text: Will DL surpass non-DL (e.g. XGBoost) in terms of performance? Maybe. I
      think it's a research area that isn't getting a lot of attention. However, I
      think that the real question is overall cost of implementing a model in production.
      If XGBoost requires tons of feature engineering and needs tweaking when the
      table structure changes, while DL can produce an adequate model without so much
      feature engineering, then DL may be better for an application even if its raw
      performance in terms of accuracy isn't as good as XGBoost. XGBoost may continue
      to win Kaggle competitions over DL but DL may be better to solve real-world
      tabular data problems for businesses.
- name: Vladimir Finkelshtein
  text: "Deep learning is known to be vulnerable to adversarial attacks. The main\
    \ focus until now was on the image domain, and there the ability of adversaries\
    \ to execute the attacks is limited (e.g. they usually can\u2019t change individual\
    \ pixels on your camera, etc..). But this is not the case with the tabular data.\
    \ Aren\u2019t better security and interpretability of the shallow model almost\
    \ always more important than extra few points in the accuracy?"
  replies:
  - name: Mark Ryan
    text: Hi Vladimir Finkelshtein model security and interpretability are important.
      For model security, I haven't seen any comparisons between XGBoost and DL on
      tabular data, though I have seen some work on DL on tabular data vulnerability
      to adversarial attacks ([https://arxiv.org/abs/1911.03274](https://arxiv.org/abs/1911.03274)).
      For interpretability, that's an area that's getting a lot of focus in DL in
      general, so I expect it won't be a bottleneck for DL on tabular data in particular.
      As for accuracy, I don't think it will be the deciding point either way. Overall
      "cost of ownership" - how much feature engineering is required and how robust
      is the overall application to changes in schema/table structure - will decide
      whether DL is better than XGBoost for a particular real-world application.
  - name: Vladimir Finkelshtein
    text: "Thanks for the example. Hopefully, there will be more success with defenses\
      \ soon.\nIf everything boils down to \u201Ccost of ownership\u201D,  wouldn\u2019\
      t AUTOML be the best choice for the majority of the use cases? In particular,\
      \ it will be the one to make the choice of the technology :)"
  - name: Mark Ryan
    text: AutoML may indeed reach the point where us mere humans won't have to make
      choices between DL and something else for tabular datasets. I don't think AutoML
      is near that yet for real-world problems.
  - name: Sara Lane
    text: AutoML isn't there yet. I'm working on a project now comparing Azure AutoML
      to Azure hyperdrive (hyperparameter tuning) and I'm getting better results with
      the hyperdrive. Admittedly, I think that usually the AutoML is better, but clearly
      that's not always the case.
- name: Alper Demirel
  text: 'Hello Mark,

    First of all, thank you for offering us such an opportunity.

    - How effective do you think DL is for regression solutions?

    - Is there information about hyperparameter tuning in the book?'
  replies:
  - name: Mark Ryan
    text: Hi Alper Demirel and thanks for your questions. Insightful question about
      regression. I've had better luck with classification than regression on DL with
      tabular data, particularly with data sets that are on the lower end of "good
      enough" for DL (10's of thousands of records). I expect that DL would be OK
      for regression given enough data to get a signal, but I only have one example
      of my own to go on, and that was for a dataset of about 1.5 M records.
  - name: Mark Ryan
    text: The book does have a section about hyperparameter tuning in the context
      of the major code example, how the parameters were chosen and which ones a reader
      may want to tweak as they expand on the major code example.
  - name: Alper Demirel
    text: Thank you very much for your answers sir
  - name: Alper Demirel
    text: I'm looking forward to reading your book
- name: Vladimir Finkelshtein
  text: "So according to your previous answers, the main advantage of DL in structured\
    \ data is automatic \u201Cfeature engineering\u201D/non-linear representation\
    \ of the data. Do you think we can see in the future some pre-trained embeddings\
    \ for different domains (like the ones for text/images)? For example, one could\
    \ collect all the health related features from many big data sets, and run it\
    \ through an autoencoder. I know it\u2019s very vague and speculative, but can\
    \ such a thing possibly be beneficial?"
  replies:
  - name: Mark Ryan
    text: 'I think the advantages of DL for tabular data are less feature engineering
      as well as flexibility to deal with a broad variety of tabular data (able to
      deal with tables that colums that have free-form text or encompass BLOBs). Another
      benefit that could be useful is using DL to exploit the metadata in database
      catalogs - I think there''s potential to do some interesting things like using
      the catalog to crawl all the tables in a database and then using DL to automatically
      generate models on the subset of column/table combinations that are "interesting"
      (with the definition of "interesting" TBD). Such a scenario, where the table
      structures are not known ahead of time, requires the flexibility of DL.

      I think what you are suggesting is a kind of transfer learning for tabular data.
      That''s an interesting idea - as far as I know, nobody has investigated that
      yet.'
  - name: Vladimir Finkelshtein
    text: 'After googling a bit, it seems like some folks are trying to use transfer
      learning, but in somewhat nonnatural way - by first transforming tabular data
      to image and then doing transfer learning on images. I wonder if this is because
      CNN is more powerful in finding features than other architectures.

      I do think that in some instances such trick may be natural. For example timeseries
      with seasonality can be represented as a nice image.'
  - name: Mark Ryan
    text: Thanks Vladimir Finkelshtein - I hadn't heard of people taking that approach
      (tabular -&gt; image -&gt; transfer learning on the images). I wonder what the
      source of the transfer learning was in this use case.
  - name: Vladimir Finkelshtein
    text: '[https://towardsdatascience.com/fast-and-accurate-learning-with-transfer-learning-on-tabular-data-how-and-why-dfe4e752bb2d](https://towardsdatascience.com/fast-and-accurate-learning-with-transfer-learning-on-tabular-data-how-and-why-dfe4e752bb2d)
      for example here it seems they just used ImageNet, so I guess anything can work.'
  - name: Vladimir Finkelshtein
    text: 'here is the paper:'
  - name: Vladimir Finkelshtein
    text: '[https://arxiv.org/pdf/1903.06246.pdf](https://arxiv.org/pdf/1903.06246.pdf)'
  - name: Mark Ryan
    text: thanks Vladimir Finkelshtein!
- name: Rishabh Bhargava
  text: 'Hi Mark, thanks for writing this book - looking forward to checking it out
    soon. In the meantime, a couple of questions for you:

    - I know you mentioned [TabNet](https://arxiv.org/pdf/1908.07442.pdf) earlier,
    but are there any neural net architectures that you see becoming the de-facto
    standard for structured data problems? As an example (and generally speaking),
    CNNs are the go-to architectures in Computer Visions and RNNs/Transformers in
    NLP.

    - Are there specific industries or use cases involving structured data where Deep
    Learning should be used more, but isn''t? I''m trying to understand if there are
    cases when folks are spending a lot of time feature engineering, but one can rely
    on DL to save the day 🙂'
  replies:
  - name: Mark Ryan
    text: 'Hi Rishabh Bhargava - for architectures for DL with tabular data, I''ve
      seen LSTMs used for examples in financial services. The extended example in
      my book uses an architecture where each class of column (continuous, categorical,
      or text) gets a distinct set of layers, so in that example there are really
      3 architectures, one for each kind of column, wrapped into a single model. For
      the future I wouldn''t be surprised to see transformers used in some DL for
      tabular data applications. Transformers seem to be eating the world, so why
      not tabular data?

      For your second question, I think it''s not so much a case of DL not being used
      for tabular data as not being considered for tabular data. Regulated industries
      (where model changes need to be submitted to a standards/regulatory body before
      going into production) are shy about DL because of its reputation for not being
      interpretable. There''s great work being done to make DL more transparent and
      thus more palatable for regulated industries, but I don''t think the research
      in that area has reached the point where it can convince all the stakeholders
      that DL is ready for regulated industries.'
  - name: Rishabh Bhargava
    text: Would love to see Transformers for these problems!
- name: Ritobrata Ghosh
  text: Mark Ryan, can you provide some insights why Deep Learning, when applied to
    tabular data, doesn't always give better results than ensemble methods such as
    Random Forests?
  replies:
  - name: Mark Ryan
    text: 'Hi Ritobrata Ghosh - this article has a good summary of why DL can lag
      behind other methods (including columns often being correlated in tabular data,
      making it harder to tease out the features that are really independent): [https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33](https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33)'
  - name: Ritobrata Ghosh
    text: Thanks for pointing out the resource. I will give it a read.
  - name: Vladimir Finkelshtein
    text: "I don\u2019t fully understand the claims in the article. Imbalances in\
      \ data can be addressed with class_weight with reasonable effectiveness. Maybe\
      \ I am wrong, but the main problem of correlations between the features is the\
      \ convergence of the learning (also for shallow ML models), but I imagine that\
      \ this could be addressed with regularization.\nMissing values are mentioned\
      \ as a reason, but it is not clear why xgboost deals with it better than deep\
      \ learning.\nThe whole story about embeddings of features not being dense -\
      \  that seems just to be a matter of network architecture. Tokenized text is\
      \ also not embedded densely, so one needs to construct something that will find\
      \ nice embeddings.\nIt seems to me that everything sums to: neural networks\
      \ are just harder to tune and one has very little intuition how to do it. They\
      \ rarely work out of the box, unlike decision trees."
- name: Matt Welke
  text: Mark Ryan I'm just getting into data science and ML now. I feel a bit overwhelmed
    with all the options out there for machine learning and deep learning. People
    throw around a lot of words that don't mean anything to me. But I know my work
    has lots of data in tabular format. We have massive SQL data warehouse. Do you
    think your book would help me find useful things I could do with it when finished
    the book?
  replies:
  - name: Mark Ryan
    text: 'Hi Matt - I was in your shoes, getting into modern ML (I had a background
      in symbolic, early 90s style AI, but that had the distinct characteristic of
      not working) and trying to solve problems with data in relational databases.
      If you want to see how to apply ML to tabular data and you haven''t done any
      ML, I suggest starting with an ML overview (like Andrew Ng''s introductory ML
      course) and get some experience with Python. With that you should be able to
      try out a classic ML approach like XGBoost on some problems with tabular data.
      I would be delighted if you were to also get my book, but it does assume basic
      ML knowledge and the code example assumes some ability with Python.

      When you''re ready to try out deep learning, the [fast.ai](http://fast.ai) intro
      course [https://course.fast.ai/](https://course.fast.ai/) is a great starting
      point.

      I hope this is helpful. You probably have a treasure trove of potential applications
      of ML in that data warehouse.'
  - name: Matt Welke
    text: 'Thanks for the reply. My work reimburses me for educational books, so I''ve
      actually already purchased yours. 😛 I''m just planning my path.
      I started by taking a Coursera course on GCP data engineering, since that''s
      what I do at work. It introduced me to a few of the GCP ML products. Then, I
      got more familiar with Python. Right now, I''m reading the Manning book "Machine
      Learning Bookcamp" and I''m liking it so far. The first project you code along
      with in the book used used tabular data.'
  - name: Matt Welke
    text: I'm thinking your book on ML with structured data is my next book.
  - name: Matt Welke
    text: Thanks for the tips. I might take that course too. I definitely fit into
      the "without a PhD" category. I only have a college diploma. I spent some time
      yesterday on Wikipedia learning what normal distributions were lol.
  - name: Matt Welke
    text: One step at a time, eh.
  - name: Mark Ryan
    text: That sounds like a great plan. Thanks very much for buying the book and
      I hope that you find it useful.
  - name: Alexey Grigorev
    text: 'hey Matt Welke glad to hear that you like ML Bookcamp :) if you have
      any questions about it, you can use `#ml-bookcamp` or `#books`
      or just write me in DM

      (Sorry Mark for hijacking your thread)'
  - name: Matt Welke
    text: 'Oh true that''s how I found this Slack server. 😛'
  - name: Matt Welke
    text: Yeah I've only completed the first two chapters I think. I'm super busy
      this month finishing up studying for my GCP data engineer cert (I take the exam
      on the 30th). So I'm just doing that for now, and I'll sink my teeth back into
      ML in February.
- name: Ritobrata Ghosh
  text: Mark Ryan, How will you rate and rank DL frameworks and methods available
    for working with tabular data (NVIDIA Rapids, [fast.ai](http://fast.ai) Tabular,
    TabNet, etc.) keeping in mind these important factors- effectiveness, ease of
    use, and resource efficiency?
  replies:
  - name: Mark Ryan
    text: Hi Ritobrata Ghosh - I've used fastai and Keras for DL on tabular problems,
      and done some experiments with Rapids. I have looked at TabNet but not used
      it to tackle a problem. Between fastai and Keras, fastai is easier to get started
      with because it provides a bunch of support for tabular data, like automatically
      identifying categorical and continuous columns. The advantage of Keras is that
      it's better documented and there's a larger community of developers working
      with it (overall, not just on tabular problems). Rapids is essentially a way
      to do what you would do with Pandas but with much better performance thanks
      to exploiting GPUs. I got great perf results with Rapids but when I ran into
      some install / config issues trying to use  it in different environments. For
      example, I could get it to work in Paperspace Gradient, but not for multiple
      sessions, and it worked in Colab but not consistently. Since perf wasn't critical
      path for what I was working on, I didn't pursue it.
  - name: Mark Ryan
    text: Overall, I would recommend fastai for somebody starting with DL for tabular
      data, and starting with Keras for a more production-oriented application, but
      assuming fastai gets used more, it could be good for production as well.
  - name: Mark Ryan
    text: 'Here''s a high-level overall comparison of fastai &amp; Keras: [https://youtu.be/3d6rGGyPR5c](https://youtu.be/3d6rGGyPR5c)'
  - name: Ritobrata Ghosh
    text: Thanks for the suggestions, I will go through them.
  - name: Ritobrata Ghosh
    text: Actually, I am a heavy user of PyTorch and its ecosystem and derived tools.
      I would like to stick with it.
  - name: Ritobrata Ghosh
    text: With [fast.ai](http://fast.ai)'s tutorials and documentation, I did not
      have any issues getting started with it for tabular data.
- name: Ritobrata Ghosh
  text: Mark Ryan, what do you think of PyTorch Lightning (and its API and efficiency)
    with respect to working with tabular data?
  replies:
  - name: Mark Ryan
    text: 'Hi Ritobrata Ghosh - I have not used Lightening, but from what I understand,
      its relationship to vanilla PyTorch (from a user perspective) has some similarities
      to Keras'' relationship to TensorFlow. I have used &amp; like fastai (see responses
      above), and it seems to have some overlap in use cases with Lightening. This
      exchange includes some contrasts between Lightening and fastai: [https://forums.fast.ai/t/fastai2-vs-pytorch-lightening-pros-and-cons-integration-of-the-two/71341/11](https://forums.fast.ai/t/fastai2-vs-pytorch-lightening-pros-and-cons-integration-of-the-two/71341/11)'
- name: Ritobrata Ghosh
  text: Mark Ryan, would you recommend RAPIDS AI for non-Deep Learning tasks? This
    question is kind of naive. I mean, for really large datasets, even datasets with
    10 gigs of data, Pandas doesn't work out of the box. You have to tune it, tweak
    function parameters, etc. if you don't have large memory at your disposal. So,
    People use Dask, or DataTable (from [H2O.ai](http://H2O.ai)) for these tasks.
    Do you recommend continue using those tools or move to RAPIDS, or would using
    RAPIDS for non-DL tasks would be an overkill?
  replies:
  - name: Mark Ryan
    text: 'Hi Ritobrata Ghosh if you have GPU capacity and a large dataset RAPIDS
      seems to be a good fit even if you''re not doing deep learning. I saw really
      good performance with RAPIDS compared to Pandas, when I was able to get RAPIDS
      working consistently. Paperspace has a RAPIDS-enabled Gradient notebook environment
      that makes it fairly painless to experiment with RAPIDS: [https://gradient.paperspace.com/integrations/nvidia-rapids](https://gradient.paperspace.com/integrations/nvidia-rapids)'
  - name: Ritobrata Ghosh
    text: 'That''s what I wanted to know. And I didn''t notice Paperspace having a
      ready-made RAPIDS environment. I will certainly head over there soon and get
      my hands dirty. Thanks a bunch.

      The nextt time I handle tabular data for a project, I will seriously consider
      RAPIDS over DataTable.'
- name: Alexey Grigorev
  text: 'Some time ago I took active parts in Kaggle competitions and for tabular
    data the winners usually use xgboost or some other GBT method. However, there''s
    always one or two people in the gold who used a neural net for their solution

    So clearly it''s possible to get great performance with neural nets, but it''s
    not the usual choice. Why do you think it''s the case?

    Is it more difficult to do it with neural nets, or just xgboost is the to-go method
    for tabular data, so other models don''t get so much attention?'
  replies:
  - name: Mark Ryan
    text: 'Hi Alexey Grigorev - I think DL is not considered for tabular data problems
      because (a) the Kaggle success of non-DL that you refer to (b) somewhat dated
      perception that DL is more difficult to develop with than non-DL (c) model intepretability
      - a legit concern, but becoming less so, (d) unlike other use cases where DL
      has blown the doors off alternatives in terms of performance, DL and non-DL
      have similar performance in many tabular data problems.

      What needs to change for DL to be taken more seriously as an option for tabular
      data problems? Better understanding in business of research on making DL more
      interpretable and a more realistic assessment of how Kaggle results do (and
      do not) apply to real-world applications with non-curated, "wild" datasets.

      I hope that my book contributes to a more balanced approach to applying DL to
      tabular datasets.'
  - name: Alexey Grigorev
    text: Thank you!
  - name: Alexey Grigorev
    text: When it comes to interpretability, xgboost is as black-boxy as neural nets
      in my opinion
  - name: Ashutosh Sanzgiri
    text: Alexey Grigorev Could you elaborate on why you think xgboost is "black-boxy"?
      Tools such as LIME and SHAP work fine with xgboost models.
  - name: Ritobrata Ghosh
    text: 'Alexey Grigorev, anything that goes beyond Lin Reg and Log Reg, is not
      fully interpretable,  IMO.

      And to solve pressing real world problems, I don''t think we should limit ourselves
      to using algorithms based only on interpretability. IMO, we should shift our
      focus more to problem-solving than interpratability.

      I also understand that in some fields, interpretability is crucial or even mandatory.
      We have to stick with Log Reg in those fields for a while.'
  - name: Alexey Grigorev
    text: 'Yes, I agree that we don''t have to stick to logreg for the rest of our
      lives

      I''d also add decision trees to that list of out-of-the-box interpretable models'
  - name: Doink
    text: I think all classical ML Algos are interpretable right?
  - name: Alexey Grigorev
    text: by classical you mean linear? or not-deep-learning?
  - name: Doink
    text: By classical I mean Linear, Logistic Regression, SVM, KNN, Naive Bayes,
      Decision Tree, Random Forest, Tree Ensembles. Not Neural Nets
- name: Sara Lane
  text: Can you tell us about your favorite DL-with-structured-data project that you
    worked on and why it was your favorite?
  replies:
  - name: Mark Ryan
    text: 'Hi Sara Lane - I really enjoyed the project described in the book because
      it involves a subject area (transit) that I''m very interested in, and the dataset
      was incredibly real-world &amp; messy. However, I have to say my favourite DL
      with tabular data project was one I did when I was back at IBM. I was responsible
      for the support team for Db2 relational database, and I wanted to predict from
      past support tickets when a client would escalate (make a duty manager call).
      The dataset (support ticket records) was interesting, and I was motivated to
      make the solution work because I fewer duty manager calls meant fewer interruptions
      for me on weekends. I describe the project in more detail in this article: [https://medium.com/@markryan_69718/deep-learning-on-structured-data-part-3-9bff73cc77c4](https://medium.com/@markryan_69718/deep-learning-on-structured-data-part-3-9bff73cc77c4)'
  - name: Sara Lane
    text: I read the article - fascinating, thanks for sharing! Curious - can you
      venture a guess as to which fields made the difference?
  - name: Mark Ryan
    text: Hi Sara Lane - the subject column (a free-form text description of the problem
      entered by the client who opened the ticket) had a surprising impact. When I
      started doing models with this dataset I expected this column would be pretty
      useless because it varied so much (from "help - db crashed" to an SQL error
      code to a long summary of symptoms) and a third of the time it wasn't even English
      text. But with even with rudimentary NLP on this column it ended up helping
      the model quite a bit, given a sufficient volume of ticket data to train on.
  - name: Sara Lane
    text: Wow! So interesting! You're right, I wouldn't have expected that, especially
      since like you said a third of the time it wasn't even English. Now I'll think
      twice when typing in the subject for a support ticket...
  - name: Sara Lane
    text: 'I''m thinking about this more, I''m wondering if maybe the ability to clearly
      and concisely express one''s issue in the subject column is connected to communications
      skills in general. Meaning that if someone can clearly state their problem in
      the subject column, it''s more likely that the issue will be resolved without
      reaching a crisis level. But if someone has poor communication skills, that
      will reflect in the subject column and will also more likely result in a Duty
      Manager call.

      This is probably an over-simplification, but I think it''s an example of how
      deep learning can often demonstrate connections that we were never aware of.'
- name: Ritobrata Ghosh
  text: Mark Ryan, in your opinion, what are the paths forward to alleviate the problem
    of ineffectiveness of DL in tabular data?
  replies:
  - name: Mark Ryan
    text: Hi Ritobrata Ghosh - despite the title of this article [https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33](https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33)
      - I think the problem isn't so much the universal ineffectiveness of DL for
      tabular data. I think the problem is the common perception that DL isn't even
      worth considering for tabular data. How to alleviate that problem? Keep an open
      mind, take advantage of the frameworks that exist now to do proofs of concept
      with DL on tabular data, and don't assume that what works best for winning Kaggle
      competitions will work best for production solutions for businesses.
  - name: Ritobrata Ghosh
    text: I have asked this from a research perspective. What should be DL practitioners'
      approach to alleviate the ineffectiveness of DL in case of tabular data?
  - name: Mark Ryan
    text: Thanks - that's a great way to look at it. From a research perspective I
      think there are two approaches that could yield results. The first is to look
      at how the metadata about tables that exists in relational database catalogs
      could be harnessed. I think catalog information is a huge, untapped resource
      - every table has it and there's a core of catalog info that is common across
      just about all database vendors. Second, and I think this is harder, I think
      there is more work that could be done on formalizing what combinations of columns
      / characteristics of tabular data lead to better outcomes w. DL. For example,
      in his book on fastai, in the section about DL w. tabular data, Jeremy Howard
      states that it works well when you have categorical columns with lots of distinct
      values. Enhancing heuristics like this with a more comprehensive analysis would
      be very useful.
  - name: Ritobrata Ghosh
    text: 'Thanks so much for the response. I have never thought about using relations
      in an RDB can be seen as inputs to a DL model. That''s a great idea. I have
      not come across a paper that does this.

      And I remember Jeremy Howard''s video and also the chapter involving tabular
      data. He asks the learner to rely on heuristics before putting the data through
      a DL model. And that really works well.'
- name: Mark Ryan
  text: "Thanks to everybody who participated this week and thanks very much to Alexey\
    \ Grigorev for providing the venue. I really enjoyed the questions and the exchange\
    \ of ideas.\nIf you get the book I encourage you to leave a review on Amazon -\
    \ thanks!: [https://www.amazon.com/Deep-Learning-Structured-Data-Mark/dp/1617296724/ref=sr_1_1?c[\u2026\
    ]+learning+with+structured%2Cstripbooks-intl-ship%2C312&amp;sr=1-1](https://www.amazon.com/Deep-Learning-Structured-Data-Mark/dp/1617296724/ref=sr_1_1?crid=2NBP30UIUGEOS&amp;dchild=1&amp;keywords=deep+learning+with+structured+data&amp;qid=1611328706&amp;s=books&amp;sprefix=deep+learning+with+structured%2Cstripbooks-intl-ship%2C312&amp;sr=1-1)"
  replies:
  - name: Alexey Grigorev
    text: Thank you Mark for agreeing to take part in this event and finding time
      to answer our questions!
  - name: Alper Demirel
    text: 'Thank you very much for your answers 🤩'

---

Deep learning offers the potential to identify complex patterns and relationships hidden in data of all sorts. Deep Learning with Structured Data shows you how to apply powerful deep learning analysis techniques to the kind of structured, tabular data you'll find in the relational databases that real-world businesses depend on. Filled with practical, relevant applications, this book teaches you how deep learning can augment your existing machine learning and business intelligence systems.

