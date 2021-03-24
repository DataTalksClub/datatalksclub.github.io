---
title: "Machine Learning Bookcamp"
description: "Book of the Week. Machine Learning Bookcamp by Alexey Grigorev. Learn machine learning by doing projects"
cover: "images/books/20201214-ml-bookcamp/cover.jpg"
image: "images/books/20201214-ml-bookcamp/preview.jpg"
start: 2020-12-14 00:00:00
end: 2020-12-18 23:59:59
authors: [alexeygrigorev]
links: 
  - text: Book's page on Manning
    link: http://bit.ly/mlbookcamp
  - text: Book's page
    link: https://mlbookcamp.com/
  - text: Book's GitHub repository
    link: https://github.com/alexeygrigorev/mlbookcamp-code

archive:
- name: Vladimir Finkelshtein
  text: "I\u2019ll take the honor of asking the first question.\nWhy so many introductory\
    \ ML books, including yours, choose not to cover timeseries? It is certainly more\
    \ basic than neural networks and, I imagine, is encountered more often in entry\
    \ level jobs."
  replies:
  - name: Alexey Grigorev
    text: 'Oh actually my first outline included a chapter on time series, tight after
      classification.

      There were a couple more chapters that we ended up excluding, e.g. working with
      text and large scale machine learning.  There was concern about the side of
      the book, so we needed to remove something and ended up removing these things.

      The main reason: they are not essential for an ML engineer / data scientist,
      and rather nice-to-have. Most of the time (in my opinion) we deal with classification
      problems, and sometimes with regression.

      And it''s also possible to pick this topic up after reading the book: the book
      (hopefully) gives enough foundation to read an article about time series and
      understand what''s going on.'
- name: Wendy Mak
  text: I would like to ask about testing in ml code-- from the table of contents
    it doesn't seem like your book covers it?  (yet I think this is an important but
    often missed topic... )
  replies:
  - name: Alexey Grigorev
    text: What do you mean by testing? Unit and integration testing or something else?
  - name: Wendy Mak
    text: yeah, unit/integration testing
  - name: Alexey Grigorev
    text: 'In my opinion, these topics are not super specific to ML, and there are
      other good books that cover these topics (maybe somebody could suggest some?)

      So that''s why I didn''t include it. I might be wrong - of course my biases
      and my own experience influenced a lot the table of contents'
  - name: Alexey Grigorev
    text: I'd be happy to be wrong about it!
  - name: Elle O'Brien
    text: 'i think testing for ML code/models/data is young! i think there will be
      ML-specific tests eventually as part of the development process, but they''re
      not yet standardized or widespread. Check out this blog: [https://www.jeremyjordan.me/testing-ml/](https://www.jeremyjordan.me/testing-ml/)'
  - name: Elle O'Brien
    text: 'I have a discussion video with the author of the testing blog, Jeremy Jordan:
      [https://youtu.be/k0naEYedv5I](https://youtu.be/k0naEYedv5I)'
- name: Neal Lathia
  text: ':question: What motivated you to write a book? Alexey Grigorev'
  replies:
  - name: Alexey Grigorev
    text: 'Oh I''m not sure I have a simple answer for that!

      It''s not my first book. I previously wrote two books - "Mastering Java for
      Data Science" and "TensorFlow Projects" (I was a co-author there, with 4 other
      people)

      The first wasn''t really successful - Java is not that popular for ML and I
      also didn''t invest much time in promoting it

      The second was interesting - I really liked the approach of learning different
      concepts through projects

      So when Manning reached out to me saying that they want to write a book with
      project-based learning (like the TF projects one), I agreed - I wanted to use
      this approach, but this time using a language more popular than Java :smiley:'
  - name: Alexey Grigorev
    text: 'That''s only a part of the story of course, I also like writing, I was
      blogging for a while - in Russian, this website is abandoned now. But I really
      like this feeling of sharing knowledge. And writing also helps me personally
      to learn things really well.

      You probably know that as well, that''s why you''re also blogging'
  - name: Alexey Grigorev
    text: And last but not least, Luca Massaron's influence was a really important
      factor when I decided to write a book. I've always admired Luca's work and also
      wanted to write books like him. So, thanks, Luca!
  - name: Neal Lathia
    text: Amazing!
  - name: Neal Lathia
    text: 'I also did my earliest ML work with java :see_no_evil: - back in the days
      of using the weka library :joy:'
- name: George Melvin
  text: 'Hello! First, let me say that I think that Book of the Week is a fantastic
    idea :clap::skin-tone-2:

    Here''s my question: I''ve recently been thinking a lot about versioning in the
    ML lifecycle - data versioning, model versioning, feature engineering code,...
    - and wondered how you solve The Versioning Problem to ensure effective model
    monitoring, debugging, updating?'
  replies:
  - name: Alexey Grigorev
    text: 'That''s a complex topic, and I''m trying to take a pragmatic approach to
      versioning.

      In my opinion, most of the projects, especially at the beginning, don''t need
      versioning. I''m mostly talking about data versioning because typically you
      need to use some tools for that. So it adds an extra layer of complexity for
      projects. If a project dies, spending time on adding this complexity is wasted.

      When it comes to model versioning, it''s a similar situation. I typically do
      simple versioning e.g. with a timestamp which I include in the response, but
      there are probably better ways of doing it.'
  - name: Alexey Grigorev
    text: 'Elle O''Brien probably you might want to add something :smiley:'
  - name: Elle O'Brien
    text: 'Of course I have thoughts on this! As Alexey Grigorev mentions, the need
      for versioning is proportional to the complexity of your project- meaning, number
      of people involved, how fast your data/modeling pipeline is changing, and how
      big the space of models you want to explore is.

      When it''s a small project with a static dataset, you can very well get away
      with Alexey''s approach. More power to you.

      DVC (note: i am part of this project and have a vested financial stake in it!
      so i''m biased) is one of several tools for versioning datasets, code, and models.
      It basically extends Git versioning and makefiles to datasets and models. Even
      though we say "data version control" in the name, many people actually use it
      for models :slightly_smiling_face: If your dataset is static, or is only modified
      via append-only operations that are easy to filter by timestamp, there is less
      need for true "data versioning". Keeping track of the way data is transformed
      to features and then to a model is where Git versioning + makefiles really shines,
      in my opinion.

      I hope that helps some. Curious what others think!'
  - name: George Melvin
    text: "Alexey Grigorev Thanks for your thoughts around this topic - it is a challenging\
      \ problem and a tricky one to get right. I certainly agree about waiting until\
      \ the R&amp;D stage is more mature and there\u2019s a better sense of the viability\
      \ of a model."
  - name: George Melvin
    text: "Elle O'Brien Thanks for sharing your thoughts - I agree with what you say\
      \ on relating the need for versioning to diff velocity in pipeline management.\
      \ I\u2019ve never quite realised the issue in these terms though so thanks for\
      \ the insight!\nI have used DVC in the past and really like the functionality,\
      \ especially when working on experiments. I\u2019ve not leveraged it for deployments/rollbacks,\
      \ however, which is where the biggest challenges (for me) lie. Would be interested\
      \ to hear from others if they\u2019ve had success."
- name: Elle O'Brien
  text: 'I have a question: do you think classical hypothesis-testing statistics (using
    p-values to assess statistical significance, for example) is an important skill
    for most data scientists? Does it have a role in most modern data science jobs?'
  replies: []
- name: Elle O'Brien
  text: I guess I see it as... a lot of ML involves linear regression (or variants
    on it). If you only care about prediction, you don't need hypothesis testing.
    But if you care about understanding what relationships in your data are meaningful,
    you probably do. How often does this really come up, though?
  replies:
  - name: Alexey Grigorev
    text: 'Not really often. Typically we need this in experiments

      E.g. if we have a new recommender system, we want to test it in online settings
      - do A/B test or A/B/C test, etc.

      The data isn''t necessarily normally distributed, so sometimes we need to do
      a Mann-Whitney U test instead of the usual T-test. So knowing these kinds of
      things might be important for that

      On the other hand, we have a stats engine for running experiments, so actually
      this kind of knowledge is not required on a daily basis. We just needed to implement
      it once and that was enough

      So it''s not something we need often, it''s more like a nice-to-have skill.
      We also don''t typically check these kind of things during the interviews -
      at least for data scientists.

      Data analysts, on the other hand, might actually get a few stats questions during
      the interviews'
- name: Alexey Shvets
  text: 'Questions:

    1. What do you like the most in your book?

    2. What part of the book would you like to improve/include if you had more time/energy?'
  replies:
  - name: Alexey Grigorev
    text: 'Hey Alexey, thanks for your questions

      &gt; What do you like the most in your book?

      I like that it''s project-based. For me personally this approach works better
      than "theory first, application second". Instead, I first introduce the problem
      and then show how to solve it

      &gt; What part of the book would you like to improve/include if you had more
      time/energy?

      First of all, I need to find the energy to finish it :sweat_smile:

      When it comes to improving, there are a lot of small things that could be rephrased,
      edited, etc, but it takes too much time.

      Probably instead I''d rather spend this time writing something new once I finish
      this one'
  - name: Alexey Shvets
    text: Alex thanks for your answers! Honestly I love your approach and your book!
      I will definitely buy a hard copy as soon as it will be released!
- name: Alper Demirel
  text: How do you get the motivation to work with the book? How do you focus?
  replies:
  - name: Alexey Grigorev
    text: 'My content development editor is doing a great job pinging me every week
      and asking about the progress. That definitely helps.

      But what helps even more is the positive feedback I''m getting about the book.
      After reading some of the messages on LinkedIn, Twitter or here in this Slack,
      I feel very motivated to work on it.

      With focus it''s more difficult though - my kid makes sure I don''t get any
      focus time :slightly_smiling_face: so the only time I can really focus is after
      10 pm. Also sometimes I wake a bit earlier and work on the book while everyone
      is asleep'
  - name: Alper Demirel
    text: 'Thanks sir for reply, love to your child :star-struck:'
- name: Karthy
  text: I have seen many books about machine learning. How is your book different
    from other books? What value do you bring to the machine learning community with
    your book?
  replies:
  - name: Alexey Grigorev
    text: 'First, I have a very specific audience in mind - software engineers who
      want to get into machine learning. Being a developer myself, I know the kinds
      of problems devs have when transitioning, so I try to teach ML in a way that
      will work for them.

      I do that by keeping the book very practical. The amount of theory is kept to
      the minimum, and I cover the stuff that is really required at work. For example,
      I talk about model deployment quite early in the book. I also spend a lot of
      time talking about evaluation metrics.

      The format is project-based, so we first start with a problem and then find
      a solution to the problem. This helps to keep the book focused.

      Interestingly, this way worked also for other kinds of audiences - I got quite
      positive feedback from data analysts who want to transition to data science
      and even from product managers.'
  - name: Alexey Grigorev
    text: 'Okay I really like my answer, I''m going to copy it to notion and use it
      as my elevator pitch when somebody asks me what makes my book stand out :smile:'
  - name: Karthy
    text: Thanks for your replies. I am looking forward to  read your book.
- name: Sejal Vaidya
  text: "This book introduces machine learning to engineers like me really well, and\
    \ gives a good insight on designing workflows. \nDo you plan to write any other\
    \ book after this, that could cover Machine Learning at Scale? \nHere, I refer\
    \ to some of the questions asked above regarding Versioning, Monitoring, Testing,\
    \ as well as use of more Distributed technologies."
  replies:
  - name: Alexey Grigorev
    text: 'I don''t think I have enough experience with these kinds of things to write
      a book about them.

      But I do have some ideas of what the next thing may look like.

      I want to write about the architectural design of ML services, like how to design
      and architect a recommender system and things like that.

      Some topics I brainstormed about included these:

      - A/B testing

      - Vandalism detection

      - Unsupervised near-duplicate detection

      - Duplicate detection in online marketplaces

      - Serving deep learning models at scale

      - RTB online learning

      - Personalized newsfeed ranking

      - E-commerce search

      - Recommender engine

      - Visual search

      - Fraud detection in marketplaces

      - Matching in two-side marketplaces

      - Dynamic pricing

      I''ll probably narrow it down to 8-10 topics. Then start with a course first
      and see how it goes. If I like it, I might convert it to a bunch of articles,
      and if it works out and I don''t lose motivation, I''ll convert them into a
      book.

      That''s just an idea, let''s see if I actually decide to do it after finishing
      with ML bookcamp'
  - name: Sejal Vaidya
    text: Thank you for answering and sharing your plan! That's an interesting list
      of use-cases. Would love to see more architectural content on those topics.
- name: Ashutosh Sanzgiri
  text: Hi Alexey, I am curious as to how you selected the datasets to illustrate
    the various ML techniques in your book. It is always a challenge to pick datasets
    that are more than "toy", and somewhat "real world". I see that a few datasets
    from Kaggle (did you select contests in which you can continue to make submissions?).  Do
    you provide next steps for readers to continue with their learning. Sorry, I have
    only skimmed the book and seen the sections that Manning decodes for you.
  replies:
  - name: Alexey Grigorev
    text: 'When selecting datasets I was thinking about these things:

      - how practical is the problem? How close is it to real world?

      - how often this dataset is used in other books and tutorials?

      I wanted to use something practical, but not something super common

      So I didn''t want to use iris, titanic, mnist or Boston housing. Also I decided
      not to include the flights delay dataset, but was pretty close to doing it'
  - name: Alexey Grigorev
    text: "As for the next steps, at the end of each chapter, I suggest to\n- try\
      \ the same thing with some other datasets\n- explore a few extra things on your\
      \ own \nI recommend to do these exercises to take most out of the book"
  - name: Alexey Grigorev
    text: The data is not from competitors, but from kaggle datasets, so it's not
      possible to submit the solution to kaggle
  - name: Ashutosh Sanzgiri
    text: Thanks for your replies, Alexey!
- name: Octavian Mocanu
  text: 'Hi Alexey, my question is what kind of deployments do you present, e.g. using
    SageMaker,  KubeFlow... Maybe also some comparatives? Thx :slightly_smiling_face:'
  replies:
  - name: Alexey Grigorev
    text: 'I was thinking about SageMaker, but there''s already too much AWS in my
      book :smiley:

      So I have these options:

      - in chapter 5, there''s a simple flask+docker webapp deployed with aws elastic
      beanstalk

      - in chapter 8, which I''m writing right now, I show how to do it with AWS Lambda
      and Kubeflow

      Oh and it was so nice of AWS to release an update when I was writing chapter
      8, so now I need to adjust it to use Docker :sweat_smile:

      Yes, I''ll include a short comparison, when to use which option'
- name: Vladimir Finkelshtein
  text: Since you mentioned that projects are the focus of your book, have you considered
    a chapter on how the project is born? How does one arrive to formulating the questions
    asked in the project? Maybe some examples of bad questions that could be asked
    about dataset. How does one choose the ML metrics and relate them to the business
    goals? How is the project planned? I noticed that all ML books tend to focus on
    the technical side, and later the data scientist are always criticized for their
    lack of soft skills.
  replies:
  - name: Alexey Grigorev
    text: 'I do a bit of that in the first chapter - I describe CRISP-DM. I''m not
      sure if I should do extensive coverage of it and have a separate chapter...
      I probably won''t. It''s too late to change the outline anyways.

      But I do want to have a separate chapter on data collection - that will be the
      last chapter of the book (chapter 9)'
  - name: Alexey Grigorev
    text: I took a note of what you asked, it's definitely a good topic - perhaps
      we can cover these topic in more details in some of our events, or a blog post
  - name: Alexey Grigorev
    text: Thank you!
- name: dreyy
  text: For someone new to machine learning and have followed some tutorials. I noticed
    most of the time is spent of processing the data and how the algorithms work isn't
    really explained. Do you consider this when writing the book?
  replies:
  - name: Alexey Grigorev
    text: Yes! The datasets that I use are somewhat prepared already, but I also include
      some data preprocessing steps as well. The focus is on developing the intuition
      behind the ML algorithms, but it's not possible to completely avoid data preparation
  - name: Alexey Grigorev
    text: Btw, you can also check the code of the book to see how much data prep is
      there - [https://github.com/alexeygrigorev/mlbookcamp-code](https://github.com/alexeygrigorev/mlbookcamp-code)
- name: Octavian Mocanu
  text: 'Maybe it was already mentioned, but I think another aspect that is not always
    considered in ML books is A/B testing ML models, which in production setups is
    really important. (Here, too, SM offers this possibility :slightly_smiling_face:
    , but, for sure, it''s not the only framework). WDYT?'
  replies:
  - name: Alexey Grigorev
    text: 'I think you''re right! Could be a nice chapter to add, and indeed not so
      many books cover it (my previous one about Java does cover it btw :smile:)

      I somehow had to make this decision and not include it because it felt to me
      that it''s not a crucial skill for ML engineers / data scientists. And aslo
      often it''s not even tested during the interviews (probably because the interviewers
      also have no clue about it)'

---

Machine Learning Bookcamp: learn machine learning by doing projects and get the skills needed to work as a data scientist or machine learning engineer.

