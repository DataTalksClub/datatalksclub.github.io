---
title: "Advanced Algorithms and Data Structures"
description: "Book of the Week. Advanced Algorithms and Data Structures by Marcello La Rocca"
cover: "images/books/20210531-advanced-algorithms-and-data-structures/cover.jpg"
image: "images/books/20210531-advanced-algorithms-and-data-structures/preview.jpg"
start: 2021-05-31 00:00:00
end: 2021-06-04 22:59:58
authors: [marcellolarocca]
links: 
  - text: Book's page
    link: https://www.manning.com/books/advanced-algorithms-and-data-structures
  - text: Book's GitHub repository
    link: https://github.com/mlarocca/AlgorithmsAndDataStructuresInAction

archive:
- name: Alex
  text: "Hi there, Marcello La Rocca! Pleasure having you around here \U0001F604\n\
    As an aspiring data scientist, I hear many different opinions regarding algos\
    \ and data structures: some say they are really a must in order to succeed, and\
    \ others say it is not fundamentally needed in order to carry out a decent job.\
    \ What\u2019s your opinion on this? Is it really that important to manage them\
    \ well? Or can you decently make it without going too deep on the subject?\nThanks\
    \ a lot!"
  replies:
  - name: Rodney Silva
    text: I also had this doubt when I started to learn data science. It's good to
      know the basics,but rarely someone will ask about algorithms during interviews.
  - name: Marcello La Rocca
    text: 'Hi Alex, thanks, it''s a pleasure for me as well!

      (Thanks a lot to Alexey Grigorev for inviting me!)

      So, that''s a great question, thanks for asking!

      The short version is, it depends on what you are working on and where.'
  - name: Marcello La Rocca
    text: 'I believe you strictly need some knowledge of the basis everywhere today,
      and then in some roles is naturally more likely than others to have to deal
      with algorithms in depth: anything related to research, any job where you have
      to deal with high volumes of data, there you are more likely to need some more-than-basic
      knowledge about algorithms and data structures; also in backend jobs it''s probably
      more likely than in frontend ones (although you should take this with a grain
      of salt, like al generalizations).

      Orthogonally to those considerations: some companies, regardless of the position,
      have interview processes that are heavily based on questions on algorithms and
      data structures, so depending on what''s your target, you might want

      to get to a certain level on the subject.'
  - name: Marcello La Rocca
    text: 'That said, I can also give you some reasons why (IMHO) studying about algorithms
      and data structures can can help any developer being "their best possible version":

      1. Performance: choosing the right algorithm can speed your application up dramatically:
      if we take something like search, on large volumes of data it makes a world
      of difference going from linear search to binary search to (possibly) Grover
      algorithm. Likewise, for a simpler task like adding elements to a list, if you
      do know that adding to the head or to the tail of the list changes the performance
      of the task, you are less likely to fall for mistakes that can slow down and
      crash you app (I''ve seen this several times in production, last time was not
      longer than a few months ago)

      2. Security: if you choose the wrong algorithm, an attacker can use it to crash
      your server/node/application. Consider, for instance, the hash DoS attack, where
      the use of a hash table as a dictionary to store variables sent with POST requests
      was leveraged to overload it with a sequence causing a huge number of collisions,
      and this in turn would make a server unresponsive. Another interesting example
      was how flawed random number generators  allowed hacking online poker sites.

      3. Efficiency in designing code: if you already know there exist building blocks
      for whatever you''d like to accomplish, you will be faster in developing it,
      and the result will be cleaner (especially if you reuse code). For instance,
      if you know what caches are for and how to use them, you won''t likely need
      to write your own custom container, rather you''ll directly go and search for
      an existing library that does what you need.'
  - name: Alex
    text: awesome, thanks a lot for the reply! that being said, I understand that
      your book is focused on advanced algos and data structures. is there any book
      recommendation for non-technicals (I come from Economics) to get a good grasp
      on the subject first?
  - name: Marcello La Rocca
    text: "Morning Alex !\nSo, if you'd like to get started with algorithms, certainly\
      \ _Grokking Algorithms_ can be a good starting point.\nBesides that, it really\
      \ depends on what you'd like to learn, and what kind of algorithms you'd be\
      \ interested in... can you tell me a little more?\nLike, for instance, would\
      \ you be interested in machine learning, or algorithms to process data, or networks...\
      \ you tell me \U0001F642"
  - name: Alex
    text: "Awesome! Will add that one to my collection as well \U0001F604\nIn regards\
      \ to what kind of algorithms, I\u2019d say pure CS algorithms related to data\
      \ processing would be great given my job requirements.\nThanks again, Marcello\
      \ La Rocca!"
  - name: Marcello La Rocca
    text: 'Hi Alex, sorry for the delay, I wanted to search out some links that I
      wanted to send you.

      So, if you are interested in data-oriented algorithms, I''d suggest [https://www.manning.com/books/algorithms-and-data-structures-for-massive-datasets](https://www.manning.com/books/algorithms-and-data-structures-for-massive-datasets)

      If you are also interested in the basics of Machine Learning, don''t miss [https://www.manning.com/books/grokking-machine-learning](https://www.manning.com/books/grokking-machine-learning)

      Both are great books!

      But if you also would like to have an overview focused on the non-technical
      angle, I wanted to suggest you might take a look at these MOOCs:

      [https://www.edx.org/course/artificial-intelligence-for-everyone](https://www.edx.org/course/artificial-intelligence-for-everyone)

      [https://mit-online.getsmarter.com/presentations/lp/mit-machine-learning-online-short-course](https://mit-online.getsmarter.com/presentations/lp/mit-machine-learning-online-short-course)

      Is that something that might interest you? Meanwhile, I''ll try to think harder
      about other resources I could recommend to you!'
  - name: Alex
    text: Thanks a lot, Marcello! I really appreciate the reply. Will give them a
      look for sure :) have a lovely day!
  - name: Marcello La Rocca
    text: 'Nice!

      Thanks, you too!'
- name: Tino
  text: "Hey Marcello La Rocca \U0001F642 Do you see a trend in interview questions\
    \ which refer to algos and data structures? I heard Google e.g. relies heavily\
    \ on this whereas other companies less. So should advanced knowledge be interviewed\
    \ by more companies? And does this help to understand pre-implemented classes/algorithms\
    \ like in scitkit-learn, etc.  easier?"
  replies:
  - name: Marcello La Rocca
    text: 'Hi Tino, thanks for your question!

      Yes, definitely, many large companies rely, for their interview process, on
      algorithms (and in general on challenge-like questions, the kind of questions
      you can find on codewars etc., just to be clear).

      I myself had my fair share of algorithmic questions when I interviewed with
      the likes of Google and Twitter! There are also many other companies (including
      [tundra.com](http://tundra.com), where I currently work) that tries different
      ways, balancing algorithmic questions with questions closer to the daily work
      that candidates would have to perform in case they joined the company.'
  - name: Marcello La Rocca
    text: 'In general it depends a lot on where you are applying, so my best advice
      is to target your preparation on the job/company you are applying

      (incidentally, I''m writing a piece with some advice for interviews on [https://dev.to/mlarocca](https://dev.to/mlarocca),
      hopefully it will be out next weekend, if you''d like to take a look)'
  - name: Marcello La Rocca
    text: 'As for the second part of your question: knowing the inside out of algorithms
      in libraries it''s not strictly necessary, but it can help you to decide better
      which algorithm to apply, and to understand better what to expect in terms of
      final result, but also resources needed.

      For instance, especially with stochastic algorithms and heuristics, it''s important
      to understand if you can expect to get always the best possible result, or even
      a correct result, and how much resources you''ll need (usually compared to other
      alternatives)'
  - name: Tino
    text: "Hey Marcello La Rocca that is amazing! Thanks so much for the insights\
      \ \U0001F642"
  - name: Marcello La Rocca
    text: "You are welcome! \U0001F642"
- name: Agrita Ga
  text: "Hei Marcello La Rocca. \U0001F44F Are there any algorithms or data structures\
    \ - in your opinion - that are underused or underappreciated? Or, then as well,\
    \ algorithms/data structures that are heavily misused or overused (due to buzz\
    \ or just because of familiarity)?"
  replies:
  - name: Marcello La Rocca
    text: "Hi! This is a very good question, really interesting. Let me give it some\
      \ proper thought, and I'll try to answer it at my best at the end of the round\U0001F642"
  - name: Marcello La Rocca
    text: 'So, here we are: this is probably one of the most challenging questions
      for today, so I left it for last! Thanks a lot Agrita Ga for asking!

      Let''s see, the first part: *underused algos/DSs.*

      For sure, I''d argue that there are many of the simplest ones that could be
      used more and improve performance, while sometimes they are just overlooked.

      For instance:

      - The binary search algorithm can provide a huge speedup in search if the collection
      to search is stable and can be ordered once, but often this is just overlooked
      and linear search on an unordered set is used.

      - Speaking of, adaptive sorting algorithms are massively underused and underknown!
      When you have a list/array that is changing slowly (low write/search ratio)
      and you need to keep it sorted, using an adaptive algorithm can outperform quicksort
      by several orders of magnitudes.

      - I''d say maybe Disjoint sets are also underused (but also underappreciated,
      which I''ll tackle next)'
  - name: Marcello La Rocca
    text: 'So, part 2: *underappreciated* algorithms:

      1. Disjoint sets, because they are clever and fast, but since there are already
      slower but simpler alternatives which are still linear or sublinear, they tend
      to be implemented sparingly

      2. Discrete Fourier Transform. I mean, it''s certainly well appreciated, but
      not many people appreciate how fundamental it is'
  - name: Marcello La Rocca
    text: "part 3: overused and misused\nThat's a tricky question \U0001F604\nThis\
      \ usually depends on the problem you re trying to solve, any algorithm can be\
      \ an overkill for some problems.\nFamiliarity is of course one of the most likely\
      \ reasons to overuse something (see the Maslow's hammer rule \U0001F642 ), but\
      \ that's mainly subjective.\nRelated to hype, instead, today I'd say that some\
      \ machine learning algorithms, or machine learning in general, are somehow more\
      \ likely to be misused.\nFor instance very powerful algorithms (well, more like\
      \ _categories_) like deep learning can be used because of buzz when the data\
      \ volume would instead suggest a different approach less prone to overfitting,\
      \ like logistic regression or random forests.\nOr maybe sometimes a machine\
      \ learning model is sought or developed, when some good old-fashioned statistics\
      \ analysis could serve better.\nIt really depends on the situation, no algorithm\
      \ or technique is intrinsically bad of course, but it's important to run a proper\
      \ requirement analysis upfront and do some research to understand what suits\
      \ best the problem we are facing."
  - name: Marcello La Rocca
    text: 'Thanks again Agrita Ga, this was a challenging and interesting question,
      it was fun to reason about it!

      I''ll try to think about other examples, and maybe I''ll add to the thread.

      Also if you have follow up questions, please, by all means!'
  - name: Agrita Ga
    text: "Delighted and ecstatic to hear this was interesting for you!\nAnd obviously\
      \ great to pick up your brain on this. \U0001F9E0\nI also feel that sometimes\
      \ misuses or using something due to familiarity comes from some personal boilerplate\
      \ function repos (I'm guilty of this), when you need to do quick and dirty coding\
      \ and don't think about efficiency that much - at least while it does not impact\
      \ actual correctness of outputs. But then again, I guess, the keywords here\
      \ are _quick and dirty._ \U0001F605 \nAnd ahh, the great hype around machine\
      \ learning. Quite often the hype and fanciness stays with the model in a notebook\
      \ when one has to deploy (read: also maintain and debug) overly complex, super\
      \ fancy machine learning model where the problem could have been solved in way\
      \ easier manner."
  - name: Agrita Ga
    text: Related question to this thread, so won't create new one (but if you think
      this deserves separate thread, I'll separate it out) - your thoughts on dataframes
      as data structures? Obviously it serves a purpose - data people think in dataframes,
      but maybe in general - overused?
  - name: Marcello La Rocca
    text: "Hmm... \U0001F914\nDo you mean something like Panda's or Spark's dataframes?\n\
      Yeah, it's a good take - I mean everything can be useful or overkill, depending\
      \ on the task.\nI'd say that whenever you need to manually run some analysis,\
      \ inspect data, even prototype a model, then a dataframe is very convenient.\n\
      Using it in the middle of a data pipeline, instead, would feel a bit like overkill\
      \ to me - but it might just be a personal preference, of course.\nWhat do you\
      \ think instead?"
  - name: Agrita Ga
    text: 'Yes, exactly - R''s, panda''s, spark''s, etc. dataframes.

      As I originally started with R, I have to say that I''m very skewed into liking
      dataframes and often designing logic that is somewhat dataframe specific. However,
      I remember when Spark introduced dataframes, some developers had hard time adjusting
      from RDDs to DataFrames - as they explained, you have to manipulate data in
      a different sequence that did not come naturally to them.

      This is why I asked your thoughts on overused, as personally I sometimes feel
      that when you have gotten really used to dataframes, it''s sometimes hard to
      switch back.

      Additional note and this is really not related to data structures, rather quick
      food for thought - with data manipulations I feel that dataframes (with all
      the in-built functions) gives us cleaner code and greater visibility what''s
      actually happening. However not saying that this also comes with speed.'
  - name: Marcello La Rocca
    text: 'Absolutely, I 100% agree.

      And it''s always tricky when you have to switch to a different way of doing
      things... I guess the important part is making sure one is switching for a good
      reason, not just to embrace the latest trend/news.

      But for dataframes, I fully underwrite your comment, it does help writing cleaner
      and better structured code, and that''s why I was thinking that anything that''s
      highly interactive or anyway with a relevant human factor is good use case for
      it.'
- name: Matthew Emerick
  text: 'Hello, Marcello La Rocca. Thank you very much for doing this.

    How do you differentiate between an easy/fundamental/intermediate algorithm and
    an advanced algorithm?'
  replies:
  - name: Marcello La Rocca
    text: 'Hi Matthew Emerick, it''s a pleasure! Thanks a lot for your questions.

      Let me try to answer them in order (and inline).'
  - name: Marcello La Rocca
    text: "The first one is very interesting: I suppose there isn't a single answer\
      \ to this, and that it's a bit subjective.\nThere are, however, some criteria\
      \ that can be used, for example\n- If an algorithm/data structure is built upon\
      \ other algos/DSs, or it's a more advanced version of another DS: for instance:\n\
      \    \u25E6 A priority queue is a more complex version of a queue\n    \u25E6\
      \ _Dijkstra_'s algorithm use priority queues as part of it's logic\n    \u25E6\
      \ _Breadth First Search_ is a simplified version of _Dijkstra_'s, which in turn\
      \ can be seen as a simplified version of _A*_. And so on...\n- If an algorithm\
      \ requires previous knowledge, or math knowledge: take the discrete Fourier\
      \ transform, just on top of my head\n- How complex is an algorithm: at a glance,\
      \ looking at the code or just its description, you can immediately see that\
      \ _BTrees_ are more complicated than _Binary Search Trees_."
- name: Matthew Emerick
  text: What are the main problems these algorithms solve?
  replies:
  - name: Marcello La Rocca
    text: 'In general? Well I think there are several categories...

      It can be storing and querying data (many data structures revolve around this,
      in the end), or it can be processing data (DFT, ransac, but also ML algorithms)'
  - name: Marcello La Rocca
    text: Of course feel free to follow up on this topic!
- name: Matthew Emerick
  text: What algorithms do you cover that most books do not?
  replies:
  - name: Marcello La Rocca
    text: "Terrific question, thanks for asking!\nFirst, I think the unique value\
      \ is that we cover a set of advanced algorithms that can't be found in any single\
      \ other book: from space-aware search to machine learning to genetic algorithms.\n\
      If we look at the individual algorithms/DSs, I think\n- no other book covers\
      \ `SS+-trees` and `OPTICS` (a clustering algorithm), distributed clustering\
      \ using `MapReduce`\n- few or no books books cover `k-d trees` and `R-trees`,\
      \ algorithms to draw graphs in the plane, `DBSCAN` (another clustering algorithm)\
      \ , `Tries`, `Bloom filters` \nBut also I'd say that, last but not least, for\
      \ the rest of the material, I tried to present it with a different angle, explaining\
      \ the theory but also discussing how to use these algorithms in practice"
- name: Matthew Emerick
  text: What do you recommend we read before reading your book?
  replies:
  - name: Marcello La Rocca
    text: '_[Grokking algorithms](https://www.manning.com/books/grokking-algorithms)_
      is a nice introduction to algorithms for beginners and people just approaching
      the topic.

      Another book that I loved and always recommend to have a quick bootstrap is
      Skiena''s _[The algorithm design manual](https://www.amazon.com/dp/B00B8139Z8/)_'
- name: Matthew Emerick
  text: What do you recommend we read after?
  replies:
  - name: Marcello La Rocca
    text: 'Depending on what you liked most on the book, there are many different
      topics that one could follow up. I tried to add links within each chapter to
      books and papers that can help the readers dig deeper into each topic.

      Just for the sake of it, a few suggestions that I also mentioned at the end
      of my book:

      - Grokking Artificial Intelligence Algorithms

      - Algorithms and Data Structures for Massive Datasets

      - Grokking Machine Learning'
- name: Rodney Silva
  text: I know that data structures is a very difficult topic in computer science.
    What do you think is the best way to study with this book in order to absorb all
    the knowledge presented?
  replies:
  - name: Marcello La Rocca
    text: 'Hi Rodney Silva! Thanks for bringing this up, that''s a good question,
      I''m glad I get the chance to talk about this.

      So, first of all, I''d say: what do we mean when we think about absorbing all
      the knowledge?

      I know not everyone might share this view, but the way I see algorithms (and
      the way I was thought about it), the goal should not be remembering by heart
      every detail of each algorithm .

      When I was in college and I followed algorithms 101, my lecturer was clear to
      us: "your goal is to learn that these algorithms do exist, and know what they
      do and when they should be applied. This way, whenever you will need them, you
      can pick up this textbook from your shelf and refresh your memory".'
  - name: Marcello La Rocca
    text: 'So every time I do a class or a talk about algorithms, I tell the same
      to the audience: try to grasp the fundamentals of each topic, and then you can
      take it from there when you need it.'
  - name: Marcello La Rocca
    text: "Complementary to that, we tried to provide the possibility of an incremental\
      \ approach to the readers, organizing chapters so that you can stop at different\
      \ points, or skip sections, depending on what you are really interested about:\n\
      - There is an introductory section for each (most) chapters explaining a problem,\
      \ trying to solve it in different ways, and showing pros and cons of a few data\
      \ structures/algorithms\n- Then the chapter usually focuses on a single data\
      \ structure, going deep into its logic, and then the implementation details\n\
      - In some chapters, there are clearly marked advanced sections where we explain\
      \ the theory behind the algorithm just described \n- In most chapters, there\
      \ is a section about practical ways of using the algorithm or data structures\
      \ just introduced."
  - name: Marcello La Rocca
    text: So, for instance, you could skim first skim through chapters reading about
      the problems, then try to use the code (you can get implementations from our
      [repo](https://github.com/mlarocca/AlgorithmsAndDataStructuresInAction) on github,
      or use a library implementing the same algo), then go deeper into into the theory
      and try to implement a DS/algo yourself (good exercise especially if you are
      preparing for interviews), and finally you can delve into the theory to understand
      why something works that way.
  - name: Marcello La Rocca
    text: 'Or, alternatively, you could also use this book as a catalog matching problems
      to algorithms, skim through it to understand what you could reuse and in what
      situations, and then when you find yourself facing a (now) familiar problem,
      you can resort to the book and delve into the details.

      I''d say we tried to write the book in a way that gives you some leeway and
      lets you decide how to learn best, given your needs'
- name: luckylittle
  text: "Hi Marcello La Rocca, I have a question about graphs and implementing them.\
    \ Mathematical representation makes it clear on the paper, but what\u2019s the\
    \ best way to store them into a data structure and how should we store edges?\
    \ What are the different approaches and potential pros and cons, please?"
  replies:
  - name: Marcello La Rocca
    text: 'Hi luckylittle, thanks for your question and sorry for the delay! (I guess
      you''ll only find it tomorrow morning, sorry!)

      Luckily enough, I spent some time writing an intro to graphs in chapter 14,
      and I go through the details of exactly these questions: you can read more about
      it here: [https://livebook.manning.com/book/algorithms-and-data-structures-in-action/chapter-14/v-14/30](https://livebook.manning.com/book/algorithms-and-data-structures-in-action/chapter-14/v-14/30)

      To give you a short answer, yes indeed, that''s a very good point, there is
      a difference between the math representation and the actual implementation.

      It is possible to implement graphs as algebraic data structures (so following
      the mathematical definition): these implementations, if correct, provides a
      few advantages (like guaranteeing you''ll have a consistent and valid graph),
      but usually have two main disadvantages:

      1. Performance (they are slooooow)

      2. Notation might be _a tad_ verbose and cumbersome (although in some languages,
      mostly functional languages, you can get around this)'
  - name: Marcello La Rocca
    text: 'More practical implementations of course do exist, and the main difference
      between them is exactly how you store edges (a critical point):

      1. Adjacency lists: each vertex has an adjacency list where outgoing edges are
      stored

      2. Adjacency matrix: rows and columns are labeled with vertices, and cell (v,u)
      contains the edge from v to u, or it''s empty if there is none

      3. Incidence matrix, a matrix whose rows are vertices and columns are edges;
      each cell it''s either a 0/1 (0 if the edge is not incident on the vertex, for
      edge e=u-&gt;v,  cells (u,e) and(v,e) would be 1), or can hold the edge''s weight.

      Each representation has pros and cons:

      1. adjacency list is used for sparse graphs, and better if the graph is dynamic
      (vertices-wise)

      2. adjacency matrix always require quadratic space, but for dense graphs this
      is asymptotically irrelevant, and it can speed up some algorithm (Floyd-Warshall,
      transitive closure etc...)

      3. incidence matrix is convenient for multigraphs, and also can speed up some
      algorithms'
  - name: Marcello La Rocca
    text: 'Then, beyond the representation, or once you choose it, there is another
      question connected to the implementation: for instance, in the adjacency list
      representation, how do you implement edges?

      Do you need a class for them, and keep references to the vertices? And then
      how do you ensure consistency when you update the graph?

      A talk a bit about this at the link I shared above, but you can also check out
      a practical implementation (and read about the design) here: [https://github.com/mlarocca/jsgraphs/blob/master/readme/tutorial.md](https://github.com/mlarocca/jsgraphs/blob/master/readme/tutorial.md)'
  - name: luckylittle
    text: "Oh wow, this is very comprehensive answer. I had a look at chapter `14.1.2\
      \ Graphs as Algebraic Types`  and it is fantastic - exactly what I need. Let\
      \ me also have a look at your GitHub. Many thanks \U0001F64F"
  - name: Marcello La Rocca
    text: Perfect! You are welcome, glad I could help!
- name: Matthew Emerick
  text: Just want to thank Marcello La Rocca again for doing this and especially for
    the detailed answers to my questions.
  replies: []
- name: Vladimir Finkelshtein
  text: What are some major recent advances in algorithms? I have read somewhere that
    multiplication of large numbers is now done in n log n, but I guess this only
    has importance as a trivia question.
  replies:
  - name: Marcello La Rocca
    text: "Hi Vladimir Finkelshtein! Thanks for your question, this is a really interesting\
      \ topic.\nSo, first things first. Well, actually, last things first, as I'd\
      \ like to start from the second part of your question.\nI suppose you refer\
      \ to this method [https://hal.archives-ouvertes.fr/hal-02070778/document](https://hal.archives-ouvertes.fr/hal-02070778/document)\n\
      to multiply two integers, presented a few yeas ago.\nI'm not sure it has been\
      \ validated by peer reviews yet, but that would certainly be a breakthrough\
      \ in their field.\nAnd by the way, it would be a super-important one also in\
      \ practice, because multiplying large integers is crucial in many fields, especially\
      \ in cryptography - often used when encrypting streams of data or communications.\n\
      On the other end, while knowing its existence could be interesting for mere\
      \ trivia questions, I doubt it would be relevant as an interview question: the\
      \ method uses a _fast Fourier transform_ with 1729 dimensions, it would take\
      \ more than an interview to explain it \U0001F604"
  - name: Marcello La Rocca
    text: 'A few more of recent breakthroughs (well, for a given value of "recent")

      - Grover''s algorithm (1996) [https://arxiv.org/abs/quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043)

      - Soft heaps (Chazelle, 2000) [https://dl.acm.org/doi/abs/10.1145/355541.355554](https://dl.acm.org/doi/abs/10.1145/355541.355554)

      - Quantum Approximate Optimization Algorithm (QAOA) (2014) [https://arxiv.org/abs/1411.4028](https://arxiv.org/abs/1411.4028)

      - Transformers (2017) [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

      - Disproof of Hedetniemi''s conjecture (2019) [https://arxiv.org/abs/1905.02167](https://arxiv.org/abs/1905.02167)

      - Fully-dynamic planarity testing in polylogarithmic time (2020)  [https://dl.acm.org/doi/10.1145/3357713.3384249](https://dl.acm.org/doi/10.1145/3357713.3384249)'
  - name: Vladimir Finkelshtein
    text: "I meant that the previous multiplication algorithms already gave something\
      \ close to n log n. And the implicit constants are not specified in either algorithm.\
      \ In encryption people rarely use numbers with more than 1024 digits, so it\
      \ is unclear if the asymptotic improvement will be relevant on this scale.\n\
      Thanks for the list. Surprised to see Shitov\u2019s result here. It is not clear\
      \ to me what is the application of it outside combinatorics though."
  - name: Marcello La Rocca
    text: "Oh I see, sorry for misunderstanding.\nWell, as you said, if it is going\
      \ to be relevant in practice, it's going to depend on the constant multiplication\
      \ factors, and on the actual implementations. Also consider that we might higher\
      \ security in the future, so the scale could go up (if we have the hardware\
      \ to support it).\nAbout Shitov's result: indeed, that's mostly a theoretical\
      \ result, but still, quite impressive (also, I'm partial to graphs theory \U0001F604\
      \ )"
- name: Rodney Silva
  text: What was the most difficult chapter to write in this book? Why?
  replies:
  - name: Marcello La Rocca
    text: "Hey Rodney Silva, thanks for the question!\nI think the hardest chapters\
      \ to write for me were chapter 10 (similarity search trees) and chapter 13 (distribute\
      \ clustering using MapReduce).\nBoth because the topics were more complex, because\
      \ I had to do a lot of research on them to make sure I had a good understanding\
      \ and I could explain all the topics in the best possible way, and because there\
      \ was little or no material at all available about these topics.\nFor SS+trees\
      \ and OPTICS, in particular, I had to dig research papers, with no implementation\
      \ of these algorithms to compare to, or to be used to validate mines.\nSo it's\
      \ been challenging but also fun \U0001F603"
- name: Agrita Ga
  text: If you'd write vol II of the book or if you'd add more chapters, which algorithms
    and/or data structures you'd be most excited to cover?
  replies:
  - name: Marcello La Rocca
    text: 'Thanks for asking Agrita Ga !

      Interesting, let me think about this...

      I think it would be great to write another book focusing on graphs, like taking
      and expanding what I have from this book, going deeper into some topics I just
      touched in this book, like Bellman-Ford, Floyd-Warshall, the maximum flow algorithms.

      But also having a part of the book about dynamic graphs, a hot topic today.'
  - name: Marcello La Rocca
    text: Perhaps what I'd enjoy even more would be writing a book about genetic algorithms,
      with a first part expanding chapter 18 of AAaDS (like, 1 chapter for crossover,
      one for natural selection, and so on), and then including many more in-depth
      examples of practical problems that one could solve using GAs
- name: Amruta
  text: 'Hey Marcello La Rocca!

    Hope you are doing well!

    I have a very basic question to start with, What was your major motivation/idea
    behind authoring this book?'
  replies: []
- name: Amruta
  text: 'Also, there are many books being written on Data structures and Algorithms
    in recent times, how is your book different/unique from the others?

    Last question, Which algorithms are your favorite/preferred ones? Do you have
    any list ?'
  replies: []
- name: Marcello La Rocca
  text: "Hi Amruta, I'm great thanks! How about you?\nThanks a lot for your questions!\
    \ Let me try to answer them in order (in this thread).\nSo, the first question\
    \ is a tricky one \U0001F604\nFirst, you need to know that I have been working\
    \ on this book for 5 years!\nIt's been long enough for me to forget why on Earth\
    \ I had started... or arguably even to start regretting it \U0001F602\nI'm just\
    \ kidding, of course... well, more or less. It's kind of hard to remember exactly\
    \ when the idea started taking form. I can say that algorithms (and in particular\
    \ graph theory and evolutionary algorithms) are my passion beyond work; back then\
    \ I was regularly writing on a blog platform, Sitepoint - mostly I was writing\
    \ about _JavaScript_. So I thought I wanted to prove myself and write about something\
    \ I really liked, because it could be fun, it would give me a chance to learn\
    \ more about these topics, and last but not least, it might help me in my career."
  replies:
  - name: Marcello La Rocca
    text: '```there are many books being written on Data structures and Algorithms
      in recent times, how is your book different/unique from the others?```

      That''s an excellent question, thanks for giving me a chance to tackle it!

      Some reasons I think makes this book different:

      1. The unique set of topics it covers. There are some topics that can''t be
      found in any other books, like SS+trees and distributed clustering algorithms,
      but also I''m not aware of any book that starts from he basics and covers in
      a single place tries, k-d trees, cache, graphs, evolutionary algorithms, etc...

      2. The approach used is some sort of middle ground between textbooks and practical
      guides. Or better, it tries to get the best from both worlds, explaining the
      theory but also giving a clear practical approach to the reader, describing
      the problems that can be solved with an algo/DS, and how you can employ them.
      We even go into profiling and all the considerations that should be made to
      decide what data structure best fit a given problem, and I believe that''s one
      of the greatest pros of this book.

      3. The book is structured (or at least, we tried to structure it) such that
      you can read it at many different levels, depending on what you are interested
      in: an overview, practical approaches, or in-depth theoretical considerations'
  - name: Marcello La Rocca
    text: "```Which algorithms are your favorite/preferred ones? Do you have any list\
      \ ?```\nThat would be a long list!!! \U0001F604\nOK, let me think... the ones\
      \ that I really really like the most...\n- Genetic algorithm, that's probably\
      \ my favourite (also being a meta-algorithm, it comprises a lot of variety!)\n\
      - Dijkstra's and A* (know them by hearth by now)\n- MapReduce (OK, that's a\
      \ _programming model_, to be _picky_) because it's so simple and elegant but\
      \ so powerful at the same time\n- The fast Fourier transform (because when you\
      \ actually get to understand it, it's like \U0001F92F )"
  - name: Amruta
    text: Thankyou so much Marcello La Rocca for explaining my questions in such detail!
      Your answers are really helpful for beginners in this field (like me). Appreciate
      them :)
  - name: Marcello La Rocca
    text: "You are welcome Amruta! \U0001F642\nI'm glad it helped, feel free to ask\
      \ any time if you have follow ups or if you just could use some advice!"
- name: Rodney Silva
  text: How much time did it take to research and write this book?
  replies:
  - name: Marcello La Rocca
    text: "Good question Rodney Silva! \U0001F642\nSo, it took me 5 years to get from\
      \ the initial idea to having it published.\nI had finished writing it a little\
      \ longer than a year ago, then it took some time to polish it, and make it production-ready\
      \ (with a lot of help from the publisher and the hard work of a lot of great\
      \ people).\nIn terms of work-hours, I think I spent somewhere between 2000 and\
      \ 3000 hours working on it. Maybe something more.\nFor each chapter, I'd start\
      \ with an idea for the topic, then come up with a few viable examples that would\
      \ demonstrate the algorithm, and possibly discuss it with the editors.\nOnce\
      \ I had an outline for the chapter, I'd start researching the topic in-depth\
      \ (also to see if and how it was covered in other publications).\nThis could\
      \ well take a week or two, depending on how much free time I had.\nThen I'd\
      \ write the code for the chapter, also to make sure I understood the topic in-depth,\
      \ and test it through.\nWhen I was confident enough, or in parallel, I would\
      \ start to write the _story_, i.e. the narration of the chapter. Then we'd go\
      \ through several reviews of the intermediate drafts"
- name: Lalit Pagaria
  text: Does your book cover LSM tree, Bloom filter and Indexing (B+ tree, inverted
    index etc)? Even though they are closely associated with DBs but seeing their
    use for highly scalable system design.
  replies:
  - name: Marcello La Rocca
    text: 'Hi Lalit Pagaria, thanks for your question!

      So:

      - LSM tree, no

      - B+ tree, a little (they are introduced when talking about R-trees)

      - Bloom filters yes, there is a chapter on them

      The whole part 2 is dedicated to multidimensional data and there is a chapter
      on k-d trees, also used for DB indexing. An another chapter, the one with an
      intro to B-trees and R-trees, focusing on SS+trees, which are also at scaling
      on high dimensional datasets (arguably better than k-d trees and R-trees)'
  - name: Lalit Pagaria
    text: "Thanks Marcello La Rocca. I never knew about SS+ Tree. Looks like good\
      \ reason to read you book \U0001F642"
  - name: Marcello La Rocca
    text: 'Thanks Lalit! You can take a peek of these similarity search trees here
      on Manning''s livebooks

      [https://livebook.manning.com/book/algorithms-and-data-structures-in-action/chapter-10/v-14/107](https://livebook.manning.com/book/algorithms-and-data-structures-in-action/chapter-10/v-14/107)

      I hope you enjoy it!'
- name: Doink
  text: 'Marcello La Rocca I wanted to extend Agrita Ga question''s a bit more you
    mentioned that Deep Learning and in general Machine Learning algorithms are overused
    and misused so do you feel we stick to logistic regression or what alternatives
    do you suggest. Also what is your take on Federated Learning paradigm of doing
    things? Federated Learning tends to follow a somewhat Map Reduce type of pattern.
    Will we see you covering Federated Learning in your second volume?

    Mainly which techniques would you prefer for distributed scalable algorithms which
    can protect privacy.'
  replies:
  - name: Marcello La Rocca
    text: "Hello Doink, thanks for following up on this.\nSo wait, no, I wouldn't\
      \ argue we should in general stick to logistic regression! \U0001F604\nWhat\
      \ I'm saying is that each problem has different characteristics and it might\
      \ be best solved with a different algorithm.\nIf your dataset is \"small\" (let's\
      \ say less than a million data points?) then probably a powerful model like\
      \ deep learning might overfit it (well, you could try to mitigate using regularization,\
      \ like dropout, but still, there will be a threshold for the size of the data\
      \ below which some models will overfit)\nAnyway, it's hard to tell precisely\
      \ in advance, and the best guideline to follow is \"listening to the data\"\
      : trying out several models, training and testing them and comparing the results\
      \ to see what model fits best and generalizes best your data."
  - name: Marcello La Rocca
    text: 'Then there is another orthogonal question that is about transparency, i.e.
      interpretability, of these models.

      To that extent, deep learning models are black boxes, and it''s hard to interpret
      them, which can lead to all kinds of unwanted biases and unexpected behaviors.

      From that point of view, I think that today we should really make an effort
      to design and use interpretable models, especially when health or life-changing
      decisions are made with the help of a model.

      A powerful interpretable alternative to neural networks are for instance GAMs,
      described for instance here: [https://www.facebook.com/watch/?v=477576069385721](https://www.facebook.com/watch/?v=477576069385721)

      Recently Denis Rothman wrote a wonderful book about explainable AI, you can
      take a look here

      [https://www.linkedin.com/feed/update/urn:li:activity:6802898159904276480/](https://www.linkedin.com/feed/update/urn:li:activity:6802898159904276480/)

      [https://www.amazon.com/gp/product/1800208138](https://www.amazon.com/gp/product/1800208138)

      A free resource on the topic

      [https://christophm.github.io/interpretable-ml-book/](https://christophm.github.io/interpretable-ml-book/)'
  - name: Marcello La Rocca
    text: 'About _federated learning_, I think that''s an extremely promising technique;
      it''s also not applicable (or advisable) in all situations, but indeed whenever
      data sharing would not be possible (either because of privacy or because the
      data is too heterogeneous) it seems like the way to go.

      Side benefit, as you note, distributing the load allows scaling out your system
      (at a price, of course, because the sum of the total resources needed might
      be higher than the ones of a centralized model - though not necessarily more
      expensive than that - and the final result might not be as good as the theoretical
      centralized equivalent).

      Privacy-wise, as an alternative I could only think about anonymizing data...
      but one way or another, if you share it, you reveal something about your source
      (sort of a fingerprint).

      But although harder, I suppose that even a model could be "reverse-engineered"
      to discover some statistics about the dataset on which it was trained. So it
      all depends on the level of security/privacy you need.

      Anyway, yeah, if I wrote a follow up book, definitely both interpretable ML
      and federated learning could be among the topics I''d like to cover!'
  - name: Doink
    text: 'Marcello La Rocca I love the long answers. Regarding Federated Learning
      for what kind of applications do you feel it''s advisable and for which use-cases
      do you feel they are not advisable?

      Also are you aware of the other approaches in the privacy preserving ML framework
      such as differential privacy, homomorphic encryption,secure multiparty computation
      and trusted execution environment?

      Also Privacy and Fairness don''t go hand in hand.'
  - name: Marcello La Rocca
    text: "\U0001F604\nFederated Learning: I think it heavily depend on the context,\
      \ as we discussed when privacy is a concern or data is too big to be processed\
      \ in a centralized way.\nHard to say _a priori_ which industries or categories...\
      \ just thinking out loud, I think something like a joint venture between several\
      \ companies, where no single company wants to share its data with the others,\
      \ could be the ideal case.\nBut also anything related to health, for instance\
      \ something that requires collecting data from several hospitals across the\
      \ Country: this could allow developing a much better model, without sharing\
      \ PIIs outside of each medical center."
  - name: Marcello La Rocca
    text: "```Privacy and Fairness don't go hand in hand```\nWell, I mean, true sometimes,\
      \ but we could struggle to find ways to make it work. Sometimes it might feel\
      \ like privacy might be used as an excuse to deny fairness, but that's another\
      \ story \U0001F914"
  - name: Marcello La Rocca
    text: '```Also are you aware of the other approaches in the privacy preserving
      ML framework such as differential privacy, homomorphic encryption,secure multiparty
      computation and trusted execution environment```

      I have to admit I''m no expert on this field, I''ll be sure to dig and read
      more about these approaches, they look fairly interesting.

      Maybe Alexey Grigorev can answer better about this?'
  - name: Alexey Grigorev
    text: "No, unfortunately I can't! But if there's a book about differential privacy,\
      \ I can try to invite the authors \U0001F603"
- name: luckylittle
  text: Marcello La Rocca Sorry to ask about graphs again. I had a look at your lightweight
    library to model graphs - `JSGraphs` , specifically the *BFS* ([https://github.com/mlarocca/jsgraphs/blob/master/readme/tutorial.md#bfs](https://github.com/mlarocca/jsgraphs/blob/master/readme/tutorial.md#bfs))
    and based on the examples there, you are showing examples of directed graphs (all
    the edges point in a direction), e.g. first example is *1* -&gt; *3* -&gt; *4*
    -&gt; *6* -&gt; *7*. Can these methods be theoretically used in scenarios with
    mixed graphs (some edges are bidirectional, few are not) - specifically to obtain
    connections between cities, e.g. some big cities are hubs connected to other big
    cities, but some villages only have one road in?
  replies:
  - name: Marcello La Rocca
    text: "Hey luckylittle, no reason to be sorry! On the contrary - graph theory\
      \ is one of my favorite topics!!! \U0001F604\nThe scenario you describe is normally\
      \ modeled with a directed graph, where one-way roads are modeled with a single\
      \ directed edge, and two-way roads, instead, correspond to a pair of directed\
      \ edges.\nDirected graphs are more flexible, in this sense, because an undirected\
      \ graph can be translated to a directed one using this trick (using a pair of\
      \ directed edges for each undirected edge); the opposite instead is not true.\n\
      Then if we move to multigraphs, those can have multiple directed edges between\
      \ each pair of vertices. To have a parallel, one could think about a situation\
      \ where multiple edges can only be used under some conditions... like maybe\
      \ the villages in your examples are connected by roads, but also through canals,\
      \ or there are flights between them, or sideroads that can only be traveled\
      \ with a dirt bike... you get the idea \U0001F642\nThe good news is that _BFS_\
      \ can work with all these graphs \U0001F642\nDoes that answer your question,\
      \ and did I understand it correctly?"
  - name: luckylittle
    text: "I'm glad that I tickled your fancy with your favourite topic \U0001F606\
      \ It certainly does explain a few things which I was not entirely sure about."
  - name: luckylittle
    text: On a different note, I had a look at this very subject in your book (via
      Manning's 5 minutes free preview, so really just skimmed through it!) and in
      that short period of time I had a feeling of reading an "academic" journal.
      Would you say that your book is going to explain these advanced topics in a
      way that non-academic people will understand? Maybe I should have another look
      tomorrow...
  - name: Marcello La Rocca
    text: 'That''s a good point. So, we tried to balance the "textbook" part with
      a more practical approach. So yeah, there will be a theoretical part that''s
      gonna cover the topic a bit more in-depth than average "hands-on" books.

      But in each chapter there is also room for examples and a more practical approach.

      For graphs in particular, since I was only writing a quick introduction, that
      feeling of "academicness" (I think I just made up a word, but bear with me)
      is probably stronger than in other chapters.

      For comparison, I''d suggest you could take a look at _Grokking Algorithms [https://livebook.manning.com/book/grokking-algorithms/chapter-6/](https://livebook.manning.com/book/grokking-algorithms/chapter-6/)_

      which has a less formal approach, and you can pick whichever works best for
      you right now

      (actually I always strongly recommend _Grokking Algorithms_ as a primer on algorithms)'
  - name: luckylittle
    text: Awesome, thanks for the tips and explanation. Keep doing a good job!
- name: Rodney Silva
  text: What is the most complex data structure to master  in this book? Why?
  replies:
  - name: Marcello La Rocca
    text: "Hey Rodney Silva,  nice question \U0001F642\nMy vote would go to k-d tree\
      \ and Ss-trees, because they work in multidimensional spaces and for our brains\
      \ (well, at least for mine) it is hard to wrap around these concepts, as it\
      \ is hard to visualize them.\nAlso, and especially for Ss-trees, the logic of\
      \ the algorithms is quite complex, and it requires a fair amount of studying\
      \ and writing down examples to get all the possible cases right."
- name: Wendy Mak
  text: Hi Marcello, in your book repo you used 3 different languages to illustrate
    the various algorithms-- is there language(s) that you find easier to implement
    algorithms in?
  replies:
  - name: Marcello La Rocca
    text: "Hi Wendy Mak, that's an excellent question, thanks for giving me a chance\
      \ to discuss this!\nFirst thing I need to say, is that I consider myself language-agnostic:\
      \ in my career I used many programming languages, and more or less I like them\
      \ all - or hate them all, on bad days \U0001F604\nI strongly believe that programming\
      \ languages are tools, and so you need to pick the right one for the task you\
      \ are presented.\nFor instance, the three languages I currently used on the\
      \ repo could hardly be more heterogeneous: Java, JavaScript and Python!\nEach\
      \ of them has different characteristics, so for instance Python is great to\
      \ quickly write prototypes, because you don't have to worry too much about the\
      \ type system and it has a very rich and intuitive syntax for lambdas, generators,\
      \ list comprehension etc.\nOn the other hand, though, a strongly typed language\
      \ like Java take care of the static checking for you, which allows me to be\
      \ more confident that my program is going to work (because types are checked\
      \ by the compiler) and also to write less tests (because, say compared to JavaScript,\
      \ if a function takes a int, I don't need to test what happens when someone\
      \ tries to pass it a string \U0001F926 )"
  - name: Marcello La Rocca
    text: 'OK, anyway, sorry for the digression. In a nutshell, which one is easier
      heavily depends on personal preference and on what one is more used to. And,
      needless to say, on what you are going to implement.

      So for me, for instance, for _containers_ it was probably easier to write them
      in Java (mostly for the reasons in my previous comment) while for anything machine-learning-related,
      a Python notebook was much easier (existing libraries and frameworks are another
      very relevant factor here)'
- name: Wendy Mak
  text: also, if you are practicising implementing algorithms from scratch, how do
    you build test cases to check that it's doing the correct thing? (since an incorrect
    or suboptimal implementation might still give you the correct answer?)
  replies:
  - name: Marcello La Rocca
    text: "Ah! Tricky one! \U0001F60A\nSo... well, it is tricky, it's actually the\
      \ trickiest part. Just yesterday I was saying exactly this, that for example\
      \ Ss+trees were the hardest for me to implement, because there was no existing\
      \ implementation that I could use as a cornerstone.\nBut in my experience this\
      \ is the norm, in my daily work I'm often in the same situation, and actually\
      \ writing (good) tests is often the most time-consuming part of my work.\nSo,\
      \ what you can do in these cases?\nWell, you can start by going through the\
      \ logic of the algorithm, reason in terms of edge cases, see if  your code works\
      \ when you get empty inputs (or null), unexpected values, large inputs, check\
      \ that it fails when it's supposed to, and finally try the regular cases.\n\
      If you are using a suite/framework, running test coverage can help you understand\
      \ if you tested all the possible cases (but also, beware of the myth of 100%\
      \ coverage...)\nIncidentally, this sanity check is a process that can help you\
      \ a lot also in interviews (you should always try to test your whiteboard code,\
      \ starting from edge cases)."
  - name: Marcello La Rocca
    text: 'Bringing this to the next level, you might want to embrace TDD (test driven
      development) or BDD (behavior driven development). This means that you''d start
      by writing your tests based on the domain knowledge and requirements analysis
      you have, and only after you lay down enough tests to express how things should
      go in your expectation, only then you start writing the code (well, more or
      less - no need to be inflexible on this kind of things, but you get the idea)

      Honestly I highly encourage TDD. Last piece of advice: have your test fail.
      This works perfectly with TDD: it''s important that you check that your tests
      initially (or at some point, before you finish implementing a feature) fail
      - this makes you more confident that you wrote a good, proper test (otherwise
      sometimes, by mistake, you can find out that your test is not actually checking
      what you were expecting)'
- name: Doink
  text: Marcello La Rocca How to balance understanding depths and breadths of internals
    of any algorithm?
  replies:
  - name: Marcello La Rocca
    text: "\U0001F914 I'm not sure I understood your question correctly: what to you\
      \ mean by depths and breadths? Do you mean having a high level understanding\
      \ (breadths) vs knowing the inside-outs, the smallest details (depths) of an\
      \ algorithm?"
  - name: Doink
    text: Marcello La Rocca Yes
  - name: Marcello La Rocca
    text: 'Thanks for clarifying!

      Then I''d say the most important thing (IMHO) is to learn the "breadths" part,
      getting a high level idea of what an algorithm do, where you can apply it, what
      problems you can solve.

      Given that our memory is limited, it''s unlikely one can remember the details
      of all algorithms.

      Instead, if one understands it at a high level, when the time comes one will
      be able to pick up that algorithm and go in depth to understand the algorithms
      internals and implement or adapt it.

      Of course there are exceptions, for instance if you are specializing in a field,
      or if you are preparing for interviews, then you might wanna go in depth. Or
      likewise, for the basics: it''s better to get an in-depth understandings of
      basic algorithms, before starting to study the ones built upon them.'
- name: Rodney Silva
  text: What's your educational background?
  replies:
  - name: Marcello La Rocca
    text: "Hey Rodney Silva, thanks for asking\nSo I studied software engineering\
      \ in high school, then got my master degree in _computer science_ (in my alma\
      \ mater it was part of the Math department, so we were focusing more on math,\
      \ algorithms, computability and complexity theory etc. than SE).\nI'm also a\
      \ PhD dropout (robotics and machine learning).\nAs for programming languages,\
      \ I started with _Turbo Pascal_ in high school, then since college I studied/worked\
      \ with:\n- Java\n- Haskell\n- C\n- C++ \n- Scheme\n- Fortran\n- JavaScript\n\
      - Php\n- C#\n- COBOL\n- Python\n- Scala\n- Go\nI might be missing some more\
      \ \U0001F604\nBut of course I'm not proficient in all of them, I daily work\
      \ just with Java/JavaScript/Python/Scala"
  - name: Alexey Shvets
    text: Marcello La Rocca which programming language do you personally like the
      most?
  - name: Marcello La Rocca
    text: "Tricky question Alexey Shvets! \U0001F92D\nOK, let's say that only considering\
      \ the joy of programming and abstracting from any practical considerations,\
      \ I'd pick `Scala`, because it's elegant and expressive, it's functional (I'm\
      \ totally partial to functional programming) but it's also concrete (and OO\
      \ \U0001F609 )"
- name: Ajay kumar saini
  text: "Hi Marcello La Rocca Thanks for doing this. I have few following questions\
    \ (forgive me if you\u2019ve already answered them, I am still going through your\
    \ response \U0001F642 )\n- Which data structures or algorithms you use most frequently\
    \ in daily engineering work?\n- Do you think using advanced data structure or\
    \ algorithm could reduce code readability or code onboarding time?\n- When one\
    \ shouldn\u2019t use a particular data structure or algorithm even though it fits\
    \ their use case?"
  replies:
  - name: Marcello La Rocca
    text: 'Hi Ajay kumar saini thanks to you for your excellent questions!

      Let me try to answer them here in order'
  - name: Marcello La Rocca
    text: "```Which data structures or algorithms you use most frequently in daily\
      \ engineering work?```\nNice one \U0001F642\nOf course the basic containers\
      \ are ubiquitous, can't spend a day without using hashing or hash maps, for\
      \ instance.\nIf we are talking about the advances ones, and the ones in the\
      \ book, I'd say right now machine learning and as such gradient descent.\nCache\
      \ would be a close second."
  - name: Marcello La Rocca
    text: "```Do you think using advanced data structure or algorithm could reduce\
      \ code readability or code onboarding time?```\nI think using the right data\
      \ structure, and advanced data structures too, could _improve_ code readability:\
      \ especially if you reuse existing (well tested) libraries or anyway you do\
      \ a good job encapsulating the data structure's logic in its own class, it will\
      \ make your daily code shorter, cleaner and clearer for who reads it.\nAs for\
      \ the onboarding time, I think it can also speed it up: the most time when you\
      \ are onboarding at a new position is spent, in my experience, in catching up\
      \ with domain knowledge.\nSo if you don't have to worry about the details of\
      \ algorithms (be it sorting, queueing, running _ransac_ on your radar data or\
      \ whatever \U0001F604 )  you can focus on the domain knowledge and catch up\
      \ more quickly.\n(please feel free to let me know if I haven't captured well\
      \ the sense of your question)"
  - name: Marcello La Rocca
    text: "```When one shouldn't use a particular data structure or algorithm even\
      \ though it fits their use case?```\nExcellent question! There could be many\
      \ complementary questions you could and should ask when deciding if a given\
      \ data structure/algorithm fits your problem; some are strictly technical, some\
      \ are more business-related - let me enumerate some of them (just thinking on\
      \ my feet here):\n- Are you operating in a multithreaded environment, and is\
      \ the DS thread safe?\n- What's the performance of this DS/algo? Does it scale\
      \ with the size of the input I have?\n- Is there a library (well tested and\
      \ widely adopted) that implements this DS/algo\n    \u25E6 If so, is it open\
      \ source?\n    \u25E6 Not open source:\n        \u25AA\uFE0E Can I trust it?\n\
      \        \u25AA\uFE0E Is there any privacy concern?\n        \u25AA\uFE0E Is\
      \ there any safety treat in using it?\n- If no existing implementation exists\
      \ or can be used: \n    \u25E6 Is there someone within the company that has\
      \ the knowledge to write it?\n    \u25E6 Is it worth using this DS/algo over\
      \ a given alternative (which might be less ideal, but you wouldn't need to implement\
      \ from scratch)?\nAnd so on... \U0001F609"
  - name: Doink
    text: 'how much of data structures does one actually write? Isn''t everything
      sorted by a well tested library?

      Also how often does one have to deal with thread safety?'
  - name: Marcello La Rocca
    text: '```how much of data structures does one actually write?```

      That heavily depends on the kind of position.

      You could spend an entire career working in machine learning, without having
      to write a single ML algorithm. You can of course make great progress and killer
      apps that puts together NLP and object recognition or gesture recognition, and
      never write a transformer nor gradient descent: you can do it all by plugging
      together ML libraries.

      Same goes for algorithms, every developer uses a lot of great algorithms every
      day without even realizing it (just think about the graph algorithms implemented
      by your compiler or by the garbage collector or, to stay more code-related,
      the containers in the standard libraries).'
  - name: Marcello La Rocca
    text: '```Isn''t everything sorted by a well tested library?```

      Well... not so fast.

      Yeah, it''s possible that you can find everything you need already implemented
      and tested. Even more, if you find such a library, you should rather use it
      and avoid re-inventing the wheel and rewriting something from scratch.

      But, that''s not always the case. A few examples of situations where you might
      need to write your own implementation:

      - You (or your company) are adopting a fairly recent language, for which there
      aren''t many libraries already available.

      - You need to implement a niche algorithm (because it''s a bottleneck in your
      pipeline and you can use any improvement). This can happen also with more popular
      or even mainstream languages, for instance try to find implementations for OPTICS,
      DeLiClu or Ss+trees in Python or JavaScript

      - You need to customize an algorithm for your peculiar needs. I''d say this
      is by far the most common case. You might still be able to use a generic implementation,
      but adapting it might be too slow or consume too much memory.

      And I probably also miss other good cases'
  - name: Marcello La Rocca
    text: '```Also how often does one have to deal with thread safety?```

      That again depends on the position... I can tell you that I currently work on
      the backend of web applications, and I have to deal almost every day with writing
      thread-safe code.

      And in my previous jobs on data infrastructure, I found it even more important.

      *Remember that thread-safety is a precondition to scaling out.*'
  - name: Ajay kumar saini
    text: "Thanks Marcello La Rocca for your insightful answers \U0001F642."
  - name: Ajay kumar saini
    text: Hi Marcello La Rocca I saw in previous threads  that you are also learning
      quantum computing. Any good recommendation for practical resources for beginners?
  - name: Marcello La Rocca
    text: "Hey Ajay kumar saini, of course!\nSome great books\n[https://manning.com/books/learn-quantum-computing-with-python-and-q-sharp](https://manning.com/books/learn-quantum-computing-with-python-and-q-sharp)
      \n[book 1](https://manning.com/books/quantum-computing-for-developers), \
      [book 2](https://oreilly.com/library/view/programming-quantum-computers/9781492039679), \
      [book 3](https://amazon.com/gp/product/0521879965), \
      [book 4](https://amazon.com/Quantum-Computing-Introduction-Engineering-Computation/dp/0262526670), \
      [book 5](https://amazon.com/Quantum-Computation-Information-10th-Anniversary/dp/1107002176). \
      (here a bit more info on each of them [in this Twitter thread](https://twitter.com/mlarocca/status/1321421052367523841))"
  - name: Marcello La Rocca
    text: 'Free resources:

      [https://qiskit.org/learn/](https://qiskit.org/learn/)

      [https://www.youtube.com/c/qiskit/playlists](https://www.youtube.com/c/qiskit/playlists)
      (in particular [https://www.youtube.com/playlist?list=PLOFEBzvs-VvrXTMy5Y2IqmSaUjfnhvBHR](https://www.youtube.com/playlist?list=PLOFEBzvs-VvrXTMy5Y2IqmSaUjfnhvBHR)
      and [https://www.youtube.com/playlist?list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY](https://www.youtube.com/playlist?list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY))

      [https://www.springer.com/journal/42484](https://www.springer.com/journal/42484)

      [https://anchor.fm/quantumcomputingnow/](https://anchor.fm/quantumcomputingnow/)

      [https://docs.microsoft.com/en-us/azure/quantum/tutorial-qdk-intro-to-katas](https://docs.microsoft.com/en-us/azure/quantum/tutorial-qdk-intro-to-katas)'
  - name: Marcello La Rocca
    text: I hope it helps!
  - name: Ajay kumar saini
    text: "Thanks for sharing. It does \U0001F642"
- name: Jasper
  text: "Thank you for adding me! \U0001F642"
  replies: []
- name: Filmetto App
  text: 'Hello Marcello La Rocca, hope you fine, and thanks for doing this question/answers!

    I would like to ask you:

    For you, for who is this book? Let say, for example, I am a newbie data engineer,
    and want to go further in this career path, does your book will help me?

    What is the knowledge the reader will need to have before approaching your book?

    Thanks!'
  replies:
  - name: Jasper
    text: "Although I haven't read the book yet, I did browse through the chapter\
      \ contents on github. During my previous course at college on data structures\
      \ we discussed various of the mentioned algorithms and learned about implementing\
      \ them.\nThis book is a treasure of knowledge, in particular if you want to\
      \ do high level design of systems and go beyond the basics. I can definitely\
      \ recommend it for your career. I grew so excited about the book that I'll likely\
      \ end up buying it if I don't win a copy. \U0001F604"
  - name: Marcello La Rocca
    text: "Thanks a lot Jasper for your kind words! I really appreciate them, and\
      \ hearing comments like this is the best motivation to write a follow up!\n\
      Any chance you'd like to repeat that in a review on Amazon? \U0001F642 Just\
      \ kidding! \U0001F604 (although well, if you would like to, it would be a great\
      \ review \U0001F642 )"
  - name: Marcello La Rocca
    text: 'Filmetto App thanks for your questions! Let''s see:

      ```For you, for who is this book?```

      Ideally it''s for beginners with some experience in coding/computer science.
      I''d say it''s for anyone who would like to discover more about algorithms and
      good practices in software engineering.'
  - name: Marcello La Rocca
    text: '```Let say, for example, I am a newbie data engineer, and want to go further
      in this career path, does your book will help me?```

      What I tried to do in this book is, besides talking about algorithms, also showing
      good practices, how to approach a problem in a systematic and rational way,
      how to reason about requirements and through that choose what''s the best data
      structure or algorithm to apply, and how to profile your implementation to find
      bottlenecks and compare different implementations to pick the best one.

      If I managed to do all that I was hoping for, then I think it might indeed help
      you in that situation.'
  - name: Marcello La Rocca
    text: '```What is the knowledge the reader will need to have before approaching
      your book?```

      The strictly required knowledge is just some basic math and basic programming
      (understanding conditionals, loops etc.).

      There is no expectation of previous knowledge of any specific programming language,
      because the book uses pseudocode to explain each algorithm (so the emphasis
      is on the logic of the algorithm, not the implementation details).

      And actual code is also provided on github in 3 (for now, more coming) different
      programming languages, so there will be great choice.

      For what concerns CS knowledge, of course if you had taken a CS 101 course it
      would help, but the book also has appendices explaining algorithms basics, from
      big-O notation and asymptotic analysis to core data structures (arrays, lists,
      stack, queue etc.).

      That should help even the beginners catch up - otherwise reading something like
      _Grokking Algorithms_ before this book would also be a great alternative)'
  - name: Jasper
    text: "*[Marcello La Rocca](https://app.slack.com/team/U01U72KABBR), being an\
      \ author myself (although fiction and not non-fiction) I know how important\
      \ good reviews are. I'd gladly repeat my comments there for you, but unfortunately\
      \ I don't have a copy of the book. I would love to review it though and see\
      \ if I can get more people interested in buying the book there from you.* \U0001F600"
  - name: Filmetto App
    text: "Thank you so much for taking the time to respond to my questions. It's\
      \ very clear and actually make me more willing to acquire your book \U0001F604"
  - name: Marcello La Rocca
    text: Thank you both, I really appreciate it!
  - name: Marcello La Rocca
    text: 'Jasper don''t worry about the review, they are not even open yet, it will
      be possible to write them only after the book is actually available (not just
      for pre-order). So, depending on the store, that might be end of June or beginning
      of July.

      And anyway of course you should have a chance to read your copy first! BTW,
      good luck (to both of you) with the extraction!'
- name: Rodney Silva
  text: Why do you think computer science bachelors suffer so much to pass in algos/ds
    interviews from Faang?
  replies:
  - name: Marcello La Rocca
    text: 'That''s a very interesting question.

      Rodney Silva Just to understand better the scope of the question, do you mean
      bachelors suffered compared to master graduates? Or compared to other backgrounds?'
  - name: Rodney Silva
    text: They suffer in general, for other backgrounds I think it's even more difficult
  - name: Marcello La Rocca
    text: "Rodney Silva sorry for the delay!\nSo yeah, this is a very interesting\
      \ issue, to me it's also a problem.\nI've had my fair share of interviews at\
      \ Faang, some of them I failed, some others I passed. And then I have also been\
      \ on the other side, the interviewer side.\nOne thing I could see is that most\
      \ of the time the interview process is focused on topics that are not part of\
      \ the daily work of people.\nSo for many of these interviews, you get asked\
      \ questions about coding challenges, and you have to write code on a whiteboard\
      \ - which isn't exactly the normal setup in our day-to-day activities, right?\n\
      If you ask me why it is that people struggle so much with these interviews,\
      \ I think a few reasons might be:\n- algo/dss are not part of the normal work\
      \ for many positions\n- b/c of that, people tend to forget them after a while\n\
      - In general algorithms are sometimes (maybe even often) neglected in people's\
      \ career, in favor of more practical topics\n    \u25E6 for those who had college\
      \ education, algorithms usually are studied early in the curriculum\n    \u25E6\
      \ for those who went through other paths, often algorithms were not even part\
      \ of  their studies\n- Moreover, these interviews ask you to face these challenges\
      \ in a very short time - some people are good at thinking on their feet and\
      \ coming up with quick answers, for other people this is more stressful and\
      \ difficult. \n- And so if one can't come up with an answer quickly, is also\
      \ more likely to panic and block, of course\nSo you see, in short, the only\
      \ way to cope with the last couple of points above is practicing hard, but not\
      \ everyone has the chance to spend so much time, nor people expect to need it,\
      \ before being in such an interview."
- name: Tim Becker
  text: 'Hi Marcello La Rocca! Really cool book! And thank you for answering our questions.
    I appreciate it a lot. I also have a few:

    - In your opinion, which are the algorithms and data structures a data scientist
    would benefit from knowing the most?

    - What is your background and how did it lead you to writing this book? What was
    your motivation to learn more about algorithms?

    - Why did you use Java and Javascript for most of the examples (github)?

    - If you are working on a programming task, how to you approach the challenge
    of finding the best algorithm or data structure for the task?'
  replies:
  - name: Marcello La Rocca
    text: "Hi Tim Becker! Thanks a lot, I appreciate it \U0001F642\nLet's go with\
      \ your question below:"
  - name: Marcello La Rocca
    text: "```In your opinion, which are the algorithms and data structures a data\
      \ scientist would benefit from knowing the most?```\nAh, tricky one... They\
      \ would benefit from all of them? \U0001F604\nOK, kidding, I don't expect you\
      \ let me get off the hook so easily \U0001F61B\nLet's see... of course, all\
      \ algorithms related to machine learning, because it would help them to understand\
      \ better how to apply these techniques.\nProbably MapReduce programming model\
      \ is also going to be gold.\nThen besides that I'd say it really depends on\
      \ the area one is focusing on \U0001F914"
  - name: Marcello La Rocca
    text: "```What is your background and how did it lead you to writing this book?\
      \ What was your motivation to learn more about algorithms?```\n I have a master\
      \ degree in computer science, major in AI and algorithms.\nThen I spent most\
      \ of my career working on web applications and data processing, but I always\
      \ tried to keep up to date and do some research on algorithms.\nEvolutionary\
      \ algorithms, graph theory, are my passion (within CS), and writing a book about\
      \ them seemed a good way to combine business and pleasure"
  - name: Marcello La Rocca
    text: '```Why did you use Java and Javascript for most of the examples (github)?```

      And Python as well (OK, a bit less!)

      So, JavaScript: because when I started working on this book, a long time ago,
      the idea was to focus on "Algorithms and DSs in JavaScript", or in general for
      the frontend.

      So I had written a lot of code in JavaScript, and moreover I was working on
      a library for graphs in JavaScript (lately rewritten into [https://github.com/mlarocca/jsgraphs](https://github.com/mlarocca/jsgraphs))

      Then Manning accepted to publish the book and we pivoted to a more broad audience,
      so I wanted to add a typical backend language, and Java was the mainstream one
      with which I was the most comfortable'
  - name: Marcello La Rocca
    text: "```If you are working on a programming task, how to you approach the challenge\
      \ of finding the best algorithm or data structure for the task?```\nAh, that's\
      \ tricky! How much time do we have to talk about this? \U0001F604\nSo there\
      \ are many aspects to keep in mind, but one thing applies IMHO: while you don't\
      \ always need the absolute best possible solution, the most important thing\
      \ is to avoid all the bad solutions.\nLet me explain: it might change little\
      \ if you use `mergesort` instead of `quicksort`, but it's more important that\
      \ you avoid `selectionsort`, which is definitely going to be slow.\nOr even\
      \ more, it can be fine using one of many heuristics that only slightly differ\
      \ in their running time, but the important thing is to avoid brute-force search."
  - name: Marcello La Rocca
    text: "More specifically, I try this approach.\n- First, I clarify the requirements,\
      \ both in terms of goals and resources available\n- Then, I start reasoning/researching\
      \ about the possible solutions\n    \u25E6 I look for existing libraries that\
      \ I can use\n    \u25E6 If nothing off-the-shelf works, I search inside the\
      \ company who could have the knowledge to implement a custom solution\n    \u25E6\
      \ Then weigh the options and how much time they would take\n    \u25E6 I try\
      \ to pick the best affordable option, say the one that could get me the most\
      \ value within those requiring a reasonable time (depending on requirements)\
      \ or anyway those that are below the median.\n- Then once implemented I profile\
      \ my code, and see if the algorithm is a bottleneck. If it is, and there is\
      \ an available algorithm that (with some effort) can give an asymptotic improvement,\
      \ I go for it. Of course this iterative approach only works if at the first\
      \ step I choose a quick solution (either off-the-shelf or quickly implementable)"
  - name: Tim Becker
    text: "Marcello La Rocca thank you \U0001F642 a lot to think about"
  - name: Marcello La Rocca
    text: "You are very welcome! Please feel free to ping me any time if you have\
      \ follow up questions \U0001F642"
- name: Rodney Silva
  text: Do you think this book can have new editions in the future?
  replies:
  - name: Marcello La Rocca
    text: "Well, it's possible of course, it will depend on the publisher too.\nBut\
      \ I think not necessarily, maybe it's more likely to have a volume 2 \U0001F642\
      \nThe reason is that these concept age well, the book is (programming) language\
      \ agnostic so it shouldn't become outdated any time soon.\nOf course there can\
      \ be advancements in the field meanwhile, but those won't likely invalidate\
      \ or deprecate what's discussed in the book (for instance, Ss+trees and R-trees\
      \ didn't made k-d trees obsolete, they are still relevant and preferable in\
      \ some situations)"
- name: Rodney Silva
  text: What kind of new advances would you like to see in the future for data structures?
  replies:
  - name: Marcello La Rocca
    text: "Ah, good one! Rodney Silva\nThe one advance that I'd love to see is on\
      \ the _P vs  NP_ problem.\nI know, it's a theory-intensive topic... but hey,\
      \ if someone proved that P=NP (which I doubt is true, but you never know!) then\
      \ we would have at least an algorithm that could be used to solve all problems\
      \ in NP in polynomial time - that would be have huge practical consequences!\n\
      More realistically, I'd be excited to see new progresses in quantum algorithms,\
      \ I think that's going to be a hot topic in the next years, and many game-changing\
      \ discoveries could be made there.\nRestricting to data-structures in particular...\
      \ I'd be looking forward to seeing new natively-distributed data structures\
      \ that leverages even more parallelism. And maybe for Graphs, I'd like to see\
      \ some open problems solved, maybe Zarankiewicz's conjecture proven, that would\
      \ be nice (well, at least for me, since I worked on the topic \U0001F604 )"


---

As a software engineer, you’ll encounter countless programming challenges that initially
seem confusing, difficult, or even impossible. Don’t despair! Many of these “new” problems
already have well-established solutions. Advanced Algorithms and Data Structures teaches
you powerful approaches to a wide range of tricky coding challenges that you can adapt and
apply to your own applications. Providing a balanced blend of classic, advanced, and new
algorithms, this practical guide upgrades your programming toolbox with new perspectives
and hands-on techniques.