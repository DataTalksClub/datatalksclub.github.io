---
title: "Relevant Search"
description: "Book of the Week. Relevant Search by Doug Turnbull"
cover: "images/books/20210712-relevant-search/cover.jpg"
image: "images/books/20210712-relevant-search/preview.jpg"
start: 2021-07-12 00:00:00
end: 2021-07-16 22:59:58
authors: [dougturnbull, John Berryman]
links: 
  - text: Book's page
    link: https://www.manning.com/books/relevant-search
  - text: Book's GitHub repository
    link: https://github.com/o19s/relevant-search-book

archive:
- name: xnot
  text: How do you see the likes of Vespa/Jina in this space? Are they viable candidates
    to base your first search system off of vs ES/Solr ?
  replies:
  - name: Doug Turnbull
    text: Sure, I think they are great tech. And the Lucene world is falling behind
      in a lot of information retrieval. Such as doing good dense vector retrieval
      and thinking in terms of multiple reranking phases. These technologies are good
      rethinkings of the space (hopefully push ES/Solr to be better too)
- name: xnot
  text: Which piece of tech are you most excited about in this space?
  replies:
  - name: Doug Turnbull
    text: "\U0001F914 I still like Elasticsearch a lot, Elastic has invested a ton\
      \ in scaling the product, and it also has forks. IE if something happened to\
      \ Elastic, I feel comfortable that some other version of Elasticsearch (ie open\
      \ distro) would take over. I also really like Elastic the company, the people\
      \ there, the culture. Maybe cause I know them well as people \U0001F602 . So\
      \ it would take a lot for me to switch. I also am comfortable extending the\
      \ engine in great depth to do what I need (such as the Elasticsearch Learning\
      \ to Rank plugin). Some of the features of newer tech do find their way into\
      \ community plugins, etc for ES.\nThat said, it does take longer for cutting\
      \ edge features to make it into the more mature product. And the JSON syntax\
      \ can be very verbose if things reach a certain level of complexity. They are\
      \ also obviously biased more towards analytics than search. I give them lots\
      \ of feedback, and maybe sometimes they listen, lol."
  - name: Doug Turnbull
    text: Lately I have pondered how well a completely (unsharded, but replicated)
      [pylucene](https://lucene.apache.org/pylucene/) cluster would work, as then
      I could manage other data structures on the side for different needs, and most
      of my colleagues are Pythonistas
- name: xnot
  text: I've always felt that companies with huge amount of traffic can have a big
    advantage when it comes to being able to provide a superior search experience.
    Do you agree?
  replies:
  - name: xnot
    text: As a follow up, how can we close that gap?
  - name: Doug Turnbull
    text: "Certainly agree. It\u2019s the secret sauce. I think there\u2019s a famous\
      \ phrase that with enough data you don\u2019t need fancy models, you can do\
      \ much more with simpler methods"
  - name: Doug Turnbull
    text: Closing the gap? Probably the lowest hanging fruit is investing in crowdsourcing
      like from a firm like Supahands ([http://supahands.com](http://supahands.com))
- name: Andrew Kornilov
  text: 'Q: Any plans for the second edition? Some elascticsearch examples are outdated
    a bit already'
  replies:
  - name: Doug Turnbull
    text: "They finally have a new Space Jam movie\u2026 hehe I won\u2019t rule it\
      \ out!\nA second edition would be quite an undertaking, as I\u2019ve learned\
      \ so much since then. I\u2019d want to incorporate so much more about relevance\
      \ measurement, about dense vector retrieval, learning to rank, more machine\
      \ learning\u2026 probably more query understanding types of things"
- name: David Cox
  text: "I\u2019m curious the contexts / types of organizations for which this book\
    \ is relevant?"
  replies:
  - name: Doug Turnbull
    text: "hmm I can\u2019t think of any that aren\u2019t? Maybe risk averse orgs\
      \ where \u2018experimentation\u2019 is not advisable. Like regulatory data that\
      \ just has to meet certain laws. Also when you\u2019re using search for just\
      \ log analytics"
- name: Kshitiz
  text: 'Hi Doug Turnbull and John,

    Q) I know that search is like one of the fundamental component of web. Apart from
    the common use case which is searching for content on the web, are there any other
    use cases of search algorithms?'
  replies:
  - name: Doug Turnbull
    text: "there are a ton, because (a) every field is an index which is not common\
      \ in other databases and (b) the rich package of text analytics.\nFor example\
      \ I\u2019ve used it to automate drug recovery, or to do \u201Cfuzzy joins\u201D\
      \ on different databases that have different variants of names or identifiers\
      \ that can be normalized with text matching.\nAlso when you write flat data,\
      \ but you have no idea how you\u2019ll look it up later, and could want to look\
      \ up on any attribute"
- name: Kshitiz
  text: 'I have another question -

    Q) What are the bottlenecks/improvement areas in the field of search?'
  replies:
  - name: Doug Turnbull
    text: 'bottlenecks: creating the index is time consuming. Generally a search engine
      is much more read scalable than write scalable'
  - name: Doug Turnbull
    text: "improvement areas: dense vector retrieval (like embeddings) is an active\
      \ area of data structures research. Like the \u201CApproximate nearest neighbors\u201D\
      \ topic"
- name: Doug Turnbull
  text: "Shameless plug, if you like my book, be sure to also check out [AI Powered Search](http://aipoweredsearch.com)\
    \ which I\u2019ve contributed 2 chapters to so far (on Learning to Rank and gathering\
    \ search training data from clicks)"
  replies: []
- name: Doug Turnbull
  text: "and ping me if you\u2019re curious about working with me at Shopify!"
  replies: []
- name: Wendy Mak
  text: at what point would you decide it's worthwhile to add your custom ML on top
    of elasticsearch?
  replies:
  - name: Doug Turnbull
    text: "Usually, when I can trust the training data. But there\u2019s lots of forms\
      \ of \u201CML\u201D. There\u2019s augmenting search with ML generated assets.\
      \ And there\u2019s Learning to Rank, ML based ranking. There\u2019s also tools\
      \ like dense vector indices that help you do embedding based retrieval. So you\
      \ might have some enrichment activity that is ML driven making the docs more\
      \ findable, but the ranking itself might be manual, for example"
- name: Wendy Mak
  text: also, maintaining a large ES index can be a real pain-- are there optimizations
    you can do around this? (and what sort of metrics would you use to decide a certain
    piece of information is too 'old' and can be moved off to a different storage?)
  replies:
  - name: Doug Turnbull
    text: "Ah interesting, hmm\u2026 I\u2019ve seen some patterns of [hot / cold indices](https://www.elastic.co/blog/implementing-hot-warm-cold-in-elasticsearch-with-index-lifecycle-management).\
      \ Often this happens in log analytics. In product search, usually merchants\
      \ explicitly delete their old products."
  - name: Doug Turnbull
    text: "maybe you are thinking like document search, something is old and stale?\
      \ I am a big fan of trusting user\u2019s behavior. Is there a way to know whether\
      \ users find the document useful? Do they share it? Copy the link? Does the\
      \ link show up on slack? Can you see if it\u2019s still used?"
  - name: Wendy Mak
    text: yeah, I am sort of thinking of document search-- I used to work for a newspaper
      publisher and we use ES for recommendation + various other stuff (and the dev
      in charge of it had a lot of headaches trying to find the correct balance of
      what to keep or not in the index)
- name: Alexey Grigorev
  text: What do you think about Solr vs elasticsearch? Are they almost the same or
    elasticsearch is a bit ahead?
  replies:
  - name: Alexey Grigorev
    text: Which one would you recommend for a new project and why?
  - name: Andrew Kornilov
    text: "or solr is a bit ahead \U0001F642"
  - name: Alexey Grigorev
    text: Indeed!
  - name: Doug Turnbull
    text: I usually think people worry too hard about what their current search engine
      is, with some exceptions - [stop worrying about Solr vs Elasticsearch](https://opensourceconnections.com/blog/2019/02/28/stop-worrying-solr-elasticsearch/)
  - name: Doug Turnbull
    text: "Solr == a bit buggier, weirder, rarely had a Solr project where I haven\u2019\
      t looked at Solr source code\nES == more modern, more opinionated, not going\
      \ to bend the project to your will as easily, but lets you do almost anything\
      \ you need in a sane way"
  - name: Andrew Kornilov
    text: and they (elastic) also break things quite often
  - name: Doug Turnbull
    text: "true, though they say \u201Cwe are now breaking X\u201D. And then I\u2019\
      m like \u201Cstop taking my toys away\u201D \U0001F602"
  - name: Andrew Kornilov
    text: my upgrate of elastic (between minor versions!) - aggregations latency
  - name: Andrew Kornilov
    text: but they managed to fix :-)
  - name: Andrew Kornilov
    text: well, "fix" == find a workaround
  - name: Doug Turnbull
    text: ouch
  - name: Alexey Grigorev
    text: Okay, thanks! And what about managed elasticsearch from AWS? It seems to
      be the easiest option to get started
  - name: Andrew Kornilov
    text: if you are not aws certified guy, [this one](https://www.elastic.co/cloud/elasticsearch-service/signup) is way easier to start
  - name: Alexey Grigorev
    text: That's nice, thank you!
- name: Dmitriy Shvadskiy
  text: With tons of work/research going into vector search what do you think of Learning
    to rank. Is it still relevant? What are good usecases?
  replies:
  - name: Doug Turnbull
    text: "Depends if by Learning to Rank you mean \u201Cthe problem of ranking solved\
      \ by ML\u201D -&gt; then yes. In the end, we\u2019re just training neural nets\
      \ against the same loss functions.\nIf you mean \u201Cthe traditional family\
      \ of models\u201D (LambdaMART, RankSVM, etc)\u2026 I think both are pretty well\
      \ understood. In particular RankSVM is nice because its a set of linear weights,\
      \ so easy to interpret/understand.\nPlus vector search is only one part of a\
      \ search solution, the inverted index is still valuable for many use cases.\
      \ So all those features combined into a final ranking function is super valuable."
  - name: Dmitriy Shvadskiy
    text: "Thanks. I meant \u201Cthe problem of ranking solved by ML\u201D. But second\
      \ part makes sense. Don\u2019t change it if it works \U0001F600"
- name: Bayram Kapti
  text: "Apologies if this is too rookie, but I\u2019m braNd new for search experiences.\
    \ \nWhere does someone start for improving search experience on a given platform?\
    \ \nWhat\u2019s the place of AI and ML for improving search experience? \nAre\
    \ categorization &amp; labeling considered part of improving search experience\
    \ or are they completely different areas of expertise?"
  replies:
  - name: Doug Turnbull
    text: "No worries!\nBest place to start:\n- How will you define \u201Cgood\u201D\
      \ and can you get data that defines what \u2018good\u2019 is for a query. There\u2019\
      s different strategies. One is to use expert, human raters if, for example,\
      \ your app is very domain specific. Another is to use clicks, etc, which involves\
      \ its own complexities (see Ch 11 AI Powered Search). Another is crowdsourcing\u2026\
      \ That strategy is very specific to the problem\n- Then try to iterate and get\
      \ better!\nLike all kinds of ML, it comes down to the underlying data. How good\
      \ / clean is data for an ML problem. At Shopify, all our merchants have vastly\
      \ different ways they use our underlying data. So that\u2019s a challenge for\
      \ us that would lend us to lean to hard on some parts of content to really \u201C\
      learn\u201D anything to help merchants.\nAbsolutely categorization / labeling\
      \ are HUGE. We have a team member that just manages a team that does this."
  - name: Bayram Kapti
    text: Thanks appreciate thw answers
- name: Dmitriy Shvadskiy
  text: What is a good way to scale judgements collection or ranking feedback for
    Enterprise search. Clicks do not mean the same things as in online shopping scenarios.
    Is thumb up/thumb down on the search result a good way to collect feedback? I
    had to build a judgement list for 1 experiment and it is a slow and painful process
  replies:
  - name: Doug Turnbull
    text: Enterprise search is _tough_ in part because nobody on your company in really
      that incentivized directly to make themselves/their content findable. If anything,
      they have the opposite incentive. They want to not be bothered, lol. Contrast
      this with Web search, where everyone is trying to SEO their content to get in
      front of as many eyeballs as possible
  - name: Doug Turnbull
    text: "It\u2019s _also_ domain specific, making things tougher \U0001F62C"
  - name: Doug Turnbull
    text: For a large org, with a heavily used app, you could use clicks for your
      head queries. BUT of course, as you get down the long tail, that gets tougher
  - name: Dmitriy Shvadskiy
    text: Definitely agree about incentives. It is a pain
  - name: Doug Turnbull
    text: "yeah not my favorite domain\u2026\nI would _probably_ gather feedback informally\
      \ myself from qualitative feedback and turn it into judgments, rather than make\
      \ users rate items"
  - name: Doug Turnbull
    text: And likely give people a very simple button to complain about a whole page
      of results (with very few fields to fill out, if any). Then when they click,
      capture the query + results. And if you can, you can find that person, and get
      more info, and turn that into relevance judgments
  - name: Dmitriy Shvadskiy
    text: Great. Thank you for the idea
- name: Doink
  text: Transformer based Search engines vs ES based search engines which to choose
    when, what types of challenges each have? Cause I think there are lots of BERT
    models used for search
  replies:
  - name: Doug Turnbull
    text: "I think in a way BERT-like search will take over for first pass search,\
      \ that\u2019s text heavy. However, in my experience, no technique ever really\
      \ \u201Cdies\u201D in search. So lots of classic relevance approaches, that\
      \ people use to explicitly manage and understand queries - like simple dictionaries/taxonomies\
      \ managed by specialists - I think will continue. In part this is because of\
      \ the often specialized nature of the search app. Another reason is the focus\
      \ on precision, and in many cases the kind of explicit control a traditional\
      \ taxonomy based approach built on an index like ES is preferred to have really\
      \ fine-grain precision"
  - name: Doug Turnbull
    text: Also not all search is very text-centric, the text might be unreliable/noisy,
      and BERT seems ideal for text passages
- name: Kim Falk
  text: Hey Doug Turnbull, What is the difference between a search engine and a recommender
    system?
  replies:
  - name: Doug Turnbull
    text: "I have _no idea_ \U0001F606"
  - name: Doug Turnbull
    text: "Probably the difference is really how explicit and active the users intent\
      \ is from the user\u2019s PoV, but implementation wise they are just on one\
      \ spectrum"
  - name: Kim Falk
    text: "Good answer \U0001F642"
  - name: Alexey Grigorev
    text: "Doug Turnbull maybe Kim Falk knows? I've heard he's answering questions\
      \ in August [here](https://datatalks.club/books/20210802-practical-recommender-systems.html)."
- name: Alexey Grigorev
  text: Do you know how it works? The query is "movie where a man wakes up on the
    same day" and it correctly identifies it as "Groundhog Day"
  replies:
  - name: Doug Turnbull
    text: "google just amazes sometimes \U0001F642. But as it\u2019s a long form query,\
      \ and likely in the realm of BERT/transformers/question answering kinds of solutions."
  - name: Doug Turnbull
    text: "To me, I\u2019m always first interested in what the loss function was to\
      \ train such a thing, and the specific training task to predict missing terms\
      \ in a piece of text by randomly masking them is quite interesting. [Link](https://towardsdatascience.com/masked-language-modelling-with-bert-7d49793e5d2c?gi=8f06ba1d9231)."
  - name: Alexey Grigorev
    text: Even before defining the loss function, I imagined they needed a lot of
      training data for that. Do you think just relying on clicks would be sufficient
      in this case?
  - name: Alexey Grigorev
    text: Perhaps there's a separate flow for movies and books
  - name: Doug Turnbull
    text: "yes google has looooooots of training data (and lots of smart people working\
      \ on the prob). At high scale, like web search, they probably can rely on clicks.\n\
      I doubt there\u2019s a separate flow, I bet you can generalize these patterns\
      \ regardless of topic\u2026"
- name: Lalit Pagaria
  text: 'How to evaluate search system?

    How to achieve micro second search result on BERT based system with TBs of data?'
  replies:
  - name: Doug Turnbull
    text: "I\u2019m not sure you can achieve micro second search results using BERT\
      \ / TBs of data \U0001F642"
  - name: Doug Turnbull
    text: '[Link](https://softwaredoug.com/blog/2021/02/21/what-is-a-judgment-list.html)'
  - name: Doug Turnbull
    text: On evaluation
  - name: Lalit Pagaria
    text: "I thought there might be magic way to achieve it \U0001F604"
- name: Shankar Somayajula
  text: 'Doug Turnbull

    How do you incorporate fuzzy matches within the search function? Search for relevance
    using entire phrase and overlay with "# of Partial hits based on keywords" within
    phrase? Do you need to maintain a set of tags or keywords (based on topics, say)
    for each inventory item to match against/with the user ask? Is there a hierarchy
    of sorts within the various independent search tasks while combining to get the
    final return resultset?'
  replies:
  - name: Doug Turnbull
    text: "I prefer to learn common misspellings by looking at query -&gt; query refinements\
      \ in log. Or by suggesting spellchecking and seeing what they click thru/what\
      \ they don\u2019t. Then you can build a dictionary of these common corrections"
  - name: Shankar Somayajula
    text: Doug Turnbull I dont mean mis-spellings but regular words but the match
      being partial, not a full or exact match. So if user gives "auburn hair color
      with lavender perfume" ... match to "auburn hair color" with any scent/perfume,
      "red hair color with fast drying feature" etc.
- name: WingCode
  text: "Hi Doug Turnbull ,\n1. How do you handle: \n    a. Different languages? Example:\
    \ Input text is in English but documents to be queried over is in Spanish.\n \
    \   b. Phonetic variations?\n    c. Transliterations in search?\n2. How do you\
    \ search:\n    d. Text input over media content (image, video, audio). Example:\
    \ Input -&gt; \"Lots of explosion\"; Results &lt;Image of an explosions&gt;, &lt;Mission\
    \ Impossible movie&gt;, &lt;Sound of dynamites exploding&gt;;\n    e. Media versus\
    \ media (Search for similar images given an image, video given an video, audio\
    \ given an audio)."
  replies:
  - name: Doug Turnbull
    text: "Ah these are all great and each very complicated questions. For 1b &amp;\
      \ 1c, assuming there\u2019s no homonyms, a good starting point is a simple dictionary\
      \ approach. For example, I\u2019ve done that for British &lt;--&gt; US English\
      \ variants\nEverything else feels very much like a deep learning problem\u2026\
      \ You build a model transforming each to a vector space, and try to build an\
      \ embedding that moves more similar content together, and push dissimilar content\
      \ apart using whatever training data you have."
  - name: Doug Turnbull
    text: "then with that embedding space, I\u2019d use an ANN index (or hack one\
      \ out of an inverted index if possible)"
  - name: WingCode
    text: "Thank you for the answers Doug \U0001F642"

---

Relevant Search demystifies relevance work. Using Elasticsearch, it teaches you how to
return engaging search results to your users, helping you understand and leverage the
internals of Lucene-based search engines.