---
title: "Practical Recommender Systems"
description: "Book of the Week. Practical Recommender Systems by Kim Falk"
cover: "images/books/20210802-practical-recommender-systems/cover.jpg"
image: "images/books/20210802-practical-recommender-systems/preview.jpg"
start: 2021-08-02 00:00:00
end: 2021-08-06 22:59:58
authors: [kimfalk]
links: 
  - text: Book's page
    link: https://www.manning.com/books/practical-recommender-systems
  - text: Book's GitHub repository
    link: https://github.com/practical-recommender-systems

archive:
- name: Emily Tran
  text: "I have never built a recommendation model but I'm curious \U0001F929 \n1,\
    \ how can a recommender destroy an application? In how many ways is it possible?\n\
    2, did you experience some destructive recommenders before? What can you do to\
    \ save the application?\n3, how can you detect such recommenders? \n4, which mistakes\
    \ can I as a beginner do to lead to those destructive models?\nYou see, I'm a\
    \ Master student and might or might not build something like that in the future\
    \ \U0001F64A thanks in advance \U0001F604"
  replies:
  - name: Kim Falk
    text: "Hi Emily Tran,\nThank you for your questions \U0001F642\n1) The ways a\
      \ recommender system can destroy an application are endless. From a pure engineering\
      \ point of view, a RecSys can be very resource demanding and slow down everything,\
      \ which will hurt the application. From a recommender point of view, there is\
      \ nothing that scares people away faster than bad recommendations. The contrary\
      \ can also be the case - if a recommender knows the user too well, the user\
      \ might find it scary. Just to mention a few."
  - name: Kim Falk
    text: 2) Again, it's hard to say what the solution is if you don't know the exact
      problem. In the case where it's low-quality recommendations, you should have
      a look at getting better data and tune your recommender. If it is an engineering
      problem, it is worth considering adding more resources or look to see if you
      can do more things offline such that it won't hurt the performance of the system
  - name: Kim Falk
    text: 3) again depends on the problem. But rule of thumb look for whether you
      have unhappy users
  - name: Kim Falk
    text: 4) consider what metrics you want to optimise for and be sure you test your
      system well. Not just offline, but more importantly, online in production. A
      lot of research indicates that good offline test results do not ensure good
      online results. Be sure to have monitoring up and running before adding or updating
      a recommender such that you can measure any changes in performance.
  - name: Emily Tran
    text: "Thank you very much for your answers. Nr 4 is absolutely helpful for every\
      \ models! I will apply it from now on\U0001F624"
- name: Bayram Kapti
  text: 'Thank you Kim Falk !

    Is it possible to do client side recommendations instead of server side? If so,
    how does client side recommendation compare to server side ?'
  replies:
  - name: Kim Falk
    text: "Anything is possible \U0001F642 As with any data applications it depends\
      \ on what data you have.\nThere are different ideas about how to do it.   One\
      \ way that seems to be discussed a lot recently is to do federated learning.\
      \ Where basically you start out with a model trained on the server, this will\
      \ be sent to each client, where the model will be updated according to the clients\
      \ actions. This model will then be sent back to the server where the client\
      \ models will be assimilated, and then it starts over.\nHave a look at [this\
      \ article](https://arxiv.org/abs/1901.09888)."
- name: Ana Data Science for Social Good Portugal
  text: What is the product lifecycle of a recommendation system (how does it evolve
    in time)? And recommendation engines trends/ usecases that you have seen across
    industries?
  replies:
  - name: Kim Falk
    text: 'As with every data driven product, the life cycle is something the lines
      of:

      1. Understand data/business

      2. Collect data

      3. Prepare data

      4. RecSys Modelling

      5. Offline evaluation

      6. Recsys deployment

      7. A/B testing

      8. Repeat'
- name: Ana Data Science for Social Good Portugal
  text: What specificities exist in content and session based recommendation engines?
  replies:
  - name: Kim Falk
    text: I would like to answer this question but it would be many hundreds of pages.
      In short Content-based recommenders mostly use NLP to create embeddings of descriptions
      of the content, and then use those embeddings either to train recommenders or
      simply recommend by finding nearest neighbours to items consumed by the user.
  - name: Kim Falk
    text: 'Session-based recommendations on the other hand are done a bit like the
      language models that predicts next words in something you are writing. If you
      watched movie A, B, C then the next best movie to suggest would be D.

      Have a look at [this survey](https://arxiv.org/pdf/1902.04864.pdf) for more information.'
- name: Bayram Kapti
  text: "What are some indications for an organization to start serving recommendations\
    \ to their users? \nSimilar question, when do you think an organization should\
    \ stay away from serving a recommender system to their users?\nI\u2019m looking\
    \ at this question from two concepts: 1-) organization maturity\n2-) product type\
    \ (user behaviour on the product etc)"
  replies:
  - name: Kim Falk
    text: "I am not sure what to answer here. It depends on the product/content organisation\
      \ wants the user to consume.\nIf there are too many products for users to overview\
      \ themselves, then a recommender system is recommended \U0001F609"
  - name: Kim Falk
    text: It depends on whether the organisation has data enough to implement a recommender
      system, either usage or content data. And if they monitor their system. If they
      don't monitor the system, then they won't be able to measure if the recommender
      improves anything, then they might as well not do it.
  - name: Bayram Kapti
    text: Got it! Sorry for the vague question. But I got a good answer that I was
      looking for.
- name: Ana Data Science for Social Good Portugal
  text: 'What are the challenges of creating and maintaining a recommendation engine
    from 2 perspectives:

    A) data engineering

    B) data science'
  replies:
  - name: Kim Falk
    text: A) There are two aspects for a data engineer, the _offline_ part one where
      you should have a system which collects the data needed to train the model,
      and then actually have the model trained, ensuring that it doesn't blow up or
      worse create bad recs because of some new trends in user behavior. Secondly
      is the online part where you have to create a pipeline which provide personalised
      recs quick enough for the user not to find another page that loads quicker.
  - name: Kim Falk
    text: B) The data scientist needs to understand the data, the business domain
      and come up with good models (and tricks) to make the recommendations good.
- name: xnot
  text: Does the book cover graph based algorithms ?
  replies:
  - name: Kim Falk
    text: In a way:)  graph-based recommenders are based on the same concepts described
      in my book. But actual graph-based algorithms are not described in detail. For
      that, I would refer to Graph-Powered Machine Learning by Alessandro Negro.
- name: xnot
  text: What're the most common mistakes you've seen people make ?
  replies: []
- name: xnot
  text: Do you also go into handling diff types of biased datasets / detecting such
    bias ?
  replies:
  - name: Kim Falk
    text: Popularity bias is discussed, as well as item and user bias in collaborative
      filtering.
- name: xnot
  text: How do you tackle long tail / niche interests with little data ?
  replies:
  - name: Kim Falk
    text: Usually, you would use a content-based recommender algorithm if you have
      little data. But since you say long tail, it has to do with something that also
      has popularity (because if there were no popular items, there would be no long
      tail either). It will always depend on which algorithm you use, but a way to
      do it is to penalise recommendations by popularity. Be careful because the idea
      is to recommend stuff that is not too popular but still something the user would
      like to watch.
- name: Doink
  text: how to do recommendation engine on edge devices using federated learning?
  replies:
  - name: Kim Falk
    text: 'Have a look at [this article](https://arxiv.org/abs/1901.09888)'
  - name: Doink
    text: yes I have seen some papers on this but what is your take on actually getting
      this stuff working in production?
  - name: Kim Falk
    text: Doink Given the chance, I would like to try it out because it sounds very
      interesting. The thing is that most apps/user only interacts with few items
      in a catalogue, so I am not sure how applicable it will be in a production system.
      Because of the amount of data, but also the resources used to train the model.
      Again I'd rather not say it wouldn't work, I just think that many other things
      also need to be working to make it work.
- name: Neal Lathia
  text: "\u2754 What are the most common mistakes people make when building a recommender\
    \ system?"
  replies:
  - name: Kim Falk
    text: "The list is long. The biggest mistake is probably to think it is easy \U0001F642\
      .  As with any data-driven product, it is very hard to evaluate the quality\
      \ of what you are implementing. It's only ever in production your recommender\
      \ gets an accurate estimate of performance."
- name: WingCode
  text: "Hi Kim. Nice to meet you again here.\n1. Are you planning for a 2nd edition\
    \ of your book?\n2. If yes, what are the additional topics you are planning for\
    \ your second edition of your book?\n3. If all above yes, when can we expect the\
    \ 2nd edition? \U0001F61B"
  replies:
  - name: Kim Falk
    text: 'Hi WingCode,

      Yes, I am planning a 2end edition. What exactly will be the content is still
      up for debate as I''m no further than working on the table of content. But on
      my wish list are chapters on deep learning algorithms, multi-armed bandits and
      reinforcement learning, and Sequence-based. Besides generally updating the rest
      of the material. Do you have any other good suggestions?

      It took my four years to write the first edition, I will be faster the second
      time around, but I wouldn''t expect it before a couple of years.'
  - name: Kim Falk
    text: I better note that I don't think my book is outdated, I think the content
      is still very relevant for somebody who wants to build recommender systems.
  - name: WingCode
    text: Kim Falk Probably more methods and techniques in extracting features from
      non-text media ( video, audio, picture) which can be used for recommendation
      systems?
- name: Alexey Grigorev
  text: 'Doug Turnbull and I were wondering if you know the answer to this question

    &gt; What is the difference between a search engine and a recommender system?'
  replies:
  - name: Kim Falk
    text: "This will be a longer answer \U0001F642"
  - name: Kim Falk
    text: "A search engine takes a seed, and the search engine returns a list of content\
      \ using that seed. In most cases, the seed is a sequence of words. Nowadays,\
      \ Google also allows for searching for images and returns images. A recommender\
      \ system takes a user profile or an item as a seed and returns a list of content\
      \ items. \nBoth search engines and recommender systems can personalise the result.\
      \ So I would say a search engine and a recommender system differs only in what\
      \ the seed is. \nA recommender system can be viewed as a pipeline that does\
      \ the following three steps:\n- candidate selection\n- apply filtering rules\n\
      - rerank result. \nWhere candidate selection is a rough cut of items that might\
      \ be interesting, it filters them based on some internal set of business rules\
      \ and then reranks the remaining items. If you view it this way, then the candidate\
      \ selection could be made by a search engine. In this view, a search engine\
      \ could be a component of a recommender system. I'm sure others would look at\
      \ it as the other way around \U0001F642."
  - name: Alexey Grigorev
    text: Great, thank you!
  - name: Doug Turnbull
    text: "Oh I am glad Alexey Grigorev thought to do this as I was on vacation last\
      \ week \U0001F609"
- name: David Cox
  text: "Kim Falk I work primarily in the healthcare domain. I\u2019m wondering if\
    \ you know of anyone doing good work in this realm related to recommendations\
    \ on patient-doctor matching or patient-intervention matching?"
  replies:
  - name: Kim Falk
    text: I am not familiar with any work applying recommender systems on that problem.
      I heard about patient-medicin matching, but I would have to go and search for
      it again.
  - name: David Cox
    text: Oh, interesting. Thanks!
- name: Mansi Parikh
  text: 'Hi, Kim! Thanks for being available to interact with the community.

    Please excuse my question if it sounds amateurish, but what are the easiest recommendation
    algorithms to implement in a business vs the hardest? And, if you could please
    provide a few options of intermediate difficulty as well, that''d be great. I
    imagine that algorithm selection depends on the quality, structure, and volume
    of data among other factors which you would detail in your book, but if you were
    to just develop a quick proof of concept in a business to demonstrate the power
    of these sophisticated analytics initiatives, what would you choose?'
  replies:
  - name: Kim Falk
    text: 'Hi Mansi Parikh

      Thank you for the question. It depends on what type of data you have. Here are
      two quick ideas on how to start.

      If you have usage data, then have a look at the framework called Implicit or
      LightFM. Both are pretty straightforward to use.

      On the other hand, if you have content descriptions. Then you can use Gensim
      package to create word2vec embeddings and then find similar items based on cosine
      similarity.

      I think the more advanced methods depends on the problem domain.

      Hope that helps.'
  - name: Mansi Parikh
    text: I love this answer. All of this is fairly new to me, and now I have a real
      plan to learn it or at least get some exposure. Thank you, Kim!!! Much appreciated.
  - name: TCG
    text: "Hi Kim Falk, I couldn\u2019t understand the difference between `usage data`\
      \ and `content description` with respect to recommendation.\nLike I\u2019m chalking\
      \ a plan for building a Hotel Recommendation System for which I have data around\
      \ `1gb` with `0.9 million reviews` of `4000 hotels`. Im still a beginner and\
      \ I cannot decide if I should use `LightFM` or  `TensorFlow Recommender` or\
      \ other ML algo."
  - name: TCG
    text: Now that you have given 2 approaches to build on, i.e. `usage data` &amp;
      `content description`. In which domain the Hotel Recommendation falls in?
- name: WingCode
  text: 'Kim Falk What are features which can be extracted from the content of:

    1. Audio

    2. Video

    3. Image

    Other than metadata of the content (aggregated features like genres, duration,
    list of cast etc)?'
  replies:
  - name: Kim Falk
    text: The sky is the limit. Audio could be something like is it music or talk,
      is it one person or many, are they angry or happy. The video could be cut into
      scenes, and count number of explosions, kisses, cars, houses ect. generally
      do object detection, if there are humans what are they doing ect. It is also
      relevant how much the camera moves, how dark the images are.
  - name: Kim Falk
    text: With the images you should do object detection, atmosphere, style.
  - name: Kim Falk
    text: This is just a few ideas.
- name: WingCode
  text: What libraries do you recommended for the same?
  replies:
  - name: Kim Falk
    text: Extracting features from Audio, Video and Images are not something I have
      tried, I have used data which was extracted as embeddings, but never done it
      myself. Im not sure which framework to recommend you.
  - name: WingCode
    text: Thank you Kim for all the answers
- name: Shankar Somayajula
  text: Kim Falk Hi, What are the ways by which recommender systems can react in real
    time to topical/dynamic trends? How does one balance the weightages to recommendations
    derived from historical data and those pertaining to recent/near term trending
    data? Basically be data driven (so start off giving mostly historical recommendations
    to user) but with ability to take feedback and react to user preferences which
    are recent (today/this week/...) ... e.g. most of the historical recommendations
    are not working/degradation, so surface near term recommendations/trends instead
    of historical trends/recommendations. Any framework to do this in a data driven
    way (with or w//o manual tinkering)?
  replies:
  - name: Kim Falk
    text: What are the ways by which recommender systems can react in real time to
      topical/dynamic trends? As with most of the answers I have given, this also
      depends on what is the specific domain and scenario. A way could be to to rerank
      your recommendations based on which items have changed most in frequency the
      last hour compared to the last day (last day compared to the last week/month).
      I think a better answer would need more context.
  - name: Kim Falk
    text: How does one balance the weightages to recommendations derived from historical
      data and those pertaining to recent/near term trending data? Depends on your
      domain, but you can create a hybrid model as a linear function of the output
      of the two models and then run tests to see which weights will provide you with
      the better recommendations.
  - name: Kim Falk
    text: To be data driven you will have to create a platform where you allow for
      data to be collected about different settings and then let the data decide what
      the right values should be. Bayesian Multiarmed bandits would be away to leave
      the weights completely up to the machine.
  - name: Kim Falk
    text: Any framework to do this in a data driven way (with or w//o manual tinkering)?
      Im not sure what this framework should do exactly?
  - name: Shankar Somayajula
    text: Kim Falk Thanks for the answers/pointers. Domain is shopping/retail primarily.
      I'll check your answers to other questions also to pick up some useful info.
- name: Lavanya M K
  text: Hi Kim Falk  How to select A/B test users for realtime recommendations?
  replies:
  - name: Kim Falk
    text: The simple answer is that you just take 10% of the traffic for the test
      group. The somewhat harder answer is that it needs to be a random sample which
      is representative of the whole population. If the users has a randomly created
      identifier you can create a hash function which can split the users into 10
      buckets and then simply take all users from that bucket, There are several books
      written about how to do it best, Fx _Tuning Up_ by David Sweet.

---

Online recommender systems help users find movies, jobs, restaurants -- even romance!
There’s an art in combining statistics, demographics, and query terms to achieve results
that will delight them. Learn to build a recommender system the right way: it can make or
break your application!