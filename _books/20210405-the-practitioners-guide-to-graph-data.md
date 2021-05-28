---
title: "The Practitioner's Guide to Graph Data"
description: "Book of the Week. The Practitioner's Guide to Graph Data by Denise Gosnell"
cover: "images/books/20210405-the-practitioners-guide-to-graph-data/cover.jpg"
image: "images/books/20210405-the-practitioners-guide-to-graph-data/preview.jpg"
start: 2021-04-05 00:00:00
end: 2021-04-09 22:59:58
authors: [denisegosnell]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/the-practitioners-guide/9781492044062/
  - text: Book's GitHub repository
    link: https://github.com/datastax/graph-book

archive:
- name: Alexey Grigorev
  text: "Hello, everyone!\nThe book of this week is [The Practitioner's Guide to Graph\
    \ Data](https://datatalks.club/books/20210405-the-practitioners-guide-to-graph-data.html)\
    \ by Denise Gosnell\n&gt; Graph data closes the gap between the way humans and\
    \ computers view the world. While computers rely on static rows and columns of\
    \ data, people navigate and reason about life through relationships. This practical\
    \ guide demonstrates how graph data brings these two approaches together. By working\
    \ with concepts from graph theory, database schema, distributed systems, and data\
    \ analysis, you\u2019ll arrive at a unique intersection known as graph thinking.\n\
    - Ask as many questions as you'd like (one question - one thread, please)\n- The\
    \ book authors answer questions from Monday till Thursday\n- On Friday, the authors\
    \ decide who wins free copies of their book"
  replies: []
- name: Alexey Grigorev
  text: "Hi Denise Gosnell! \nWhen we connected on LinkedIn, you mentioned that you\
    \ can tell us how graph databases can be distributed.\nSo. How graph databases\
    \ can be distributed? what are possible approaches?"
  replies:
  - name: Denise Gosnell
    text: 'Alexey Grigorev great question.

      My answer is based on knowledge of the three types of graph data structures:

      1. Adjacency matrices

      2. Edge lists

      3. Adjacency List

      Irrespective of distributed or single instance, each data structure has its
      pros / cons.

      Adjacency matrices are too large to write on disk, but they are the fastest
      for looking up graph data.

      Edge lists are the most compact to distribute, but they require scanning the
      entire edge set to look up relationships.

      Adjacency Lists are the middle ground. They allow for constant time lookup of
      vertices and then reduce the edge scans to those local to the vertices.

      Therefore, when working with distributed graph data, I recommend finding a way
      to implement adjacency lists to distribute your graph across your cluster.'
  - name: Denise Gosnell
    text: 'Cassandra is the distributed system with which I am most familiar (from
      the early Titan DB days in 2013).

      In the book we are reading this week, we are working with adjacency lists across
      Cassandra partitions.

      Chapter 5 goes into detail into how we do it.

      LucidChart Images 5-7 through 5-12 illustrate how we do this.'
  - name: Denise Gosnell
    text: 'Vertices and edges map to partitions in cassandra.

      The key to understanding how to distribute a graph comes from understanding
      how we model the partition and clustering keys under the hood.

      (to use graphs in Cassandra, you don''t have to know the details)

      The vertex tables work just like regular C* tables - nothing special there.
      You have partition keys and clustering columns like normal.

      The fun parts come into to play with the edge tables!

      The partition key of an edge table is:

      - the outgoing vertex''s entire primary key

      The clustering key of an edge table is:

      - the incoming vertex''s entire primary key

      - (maybe a property)

      The images below are from Chapter 5 where we discuss this in detail.'
  - name: Alexey Grigorev
    text: What's a C* table? something Cassandra related?
  - name: Alexey Grigorev
    text: 'So, let''s say we have an adjacency list. From my understanding, a graph
      in this representation looks something like that

      0 =&gt; [1, 2, 5, 10]

      2 =&gt; [3, 4, 5]

      3 =&gt; [0, 3, 10]


      ...

      (these numbers are ids of nodes)

      If now we want to distribute it to multiple partitions, would we use something
      like consistency hashing to map each node to a partition? and keep the entire
      list of outcoming nodes within that node partition? (+some extra properties
      of the node)'
  - name: Denise Gosnell
    text: "Alexey Grigorev I apologize for using shortcuts that are apart of our vernacular\
      \ at DataStax -- switching between Slack universes can be confusing and I forgot\
      \ where I was \U0001F61C\nC* == Cassandra.\nWhen I said, \"C* table\", I was\
      \ referring to a virtual table in Cassandra. A table contains many partitions."
  - name: Alexey Grigorev
    text: Hehe, okay =) got it, thank you!
  - name: Denise Gosnell
    text: 'And - the answer to your second question Alexey Grigorev is yes  - you
      got it!

      However, Cassandra''s use of consistency hashing may be a bit different than
      expected.

      Each table has a partition key that is hashed using murmur3 algorithm. The whole
      hash space forms a continuous ring from lowest possible hash to the highest.
      After that this ring is divided into chunks (vnodes, 256 by default) and these
      chunks are fairly distributed among multiple nodes. Each node hosts its own
      part of the ring and a replicated copy of other vnodes (according to replication
      factor.)

      A visual example from Chapter 5 in the book is shown for how we distribute graph
      data using Cassandra''s hashing algorithms. The images below are images 5-11
      and 5-2, respectively.

      I provided a link to the LucidCharts in the channel if you would like to explore
      them (and some that were cut from the book!)

      In Cassandra, we use'
- name: Toxicafunk
  text: Like Janusgraph with a Cassandra backend for instance?
  replies:
  - name: Alexey Grigorev
    text: Not sure if it's a clarifying question for me or not. But I meant something
      more general - what are possible approaches and how it's implemented in modern
      graph databases
  - name: Toxicafunk
    text: I know that Janusgraph, for instance, can have a Cassandra or an Hbase backend,
      so you get the same distributed approach they have
  - name: Toxicafunk
    text: Generally speaking, a graph database is a nosql database with a network
      (path-based) querying model
  - name: Toxicafunk
    text: "But this is a very good question, I'd love to know what else is out there\
      \ \U0001F604"
  - name: Denise Gosnell
    text: "Toxicafunk yes!\nI worked with Matthias Broecheler on this book.\nMatthias\
      \ invented Titan. Janusgraph is a fork of Titan.\nThe book we wrote details\
      \ how we mapped Adjacency Lists onto Cassandra. This is the same way they do\
      \ it in Titan (Janusgraph) \U0001F642\nI shared details on how we mapped adjacency\
      \ lists onto C* partitions in the thread above. I included images from Chapter\
      \ 5 to show how we translate C* schema as an adjacency list.\nPlease let me\
      \ know if you have any further questions!"
  - name: Toxicafunk
    text: wow! this is exactly what I've been thinking about for the past m,onth,
      thx!
  - name: Denise Gosnell
    text: Toxicafunk awesome!
- name: Toxicafunk
  text: Or do you mean something else?
  replies: []
- name: Vladimir Finkelshtein
  text: When you mention graph data, do you mainly refer to graph databases or to
    ML algorithms taking graph structure as an input (I am thinking of clustering
    as the simplest example)
  replies:
  - name: Denise Gosnell
    text: "Vladimir Finkelshtein we are mainly referring to graph databases for this\
      \ week's discussion.\nIn chapters 10, 11, and 12, we go into detail into how\
      \ Netflix uses graph structured data to do recommendations for the ML algorithms\
      \ behind the \"Recommendation pane\" on the app. I hope this helps!\nPlease\
      \ let me know if you have any more questions. \U0001F642"
- name: Matthew Emerick
  text: 'Hello, Denise Gosnell!  Thank you for doing this!

    How useful do you see graph data and graph algorithms in the field of artificial
    intelligence?'
  replies:
  - name: Denise Gosnell
    text: "Matthew Emerick You are welcome! Glad to be here \U0001F642\nI am biased\
      \ (ha!).\nI am seeing graph data used more and more as a new type of feature\
      \ within ML algorithms.\nWRT to graph data - properties like \"path distance\"\
      \ between two points or a boolean of \"is x in the 3rd neighborhood of y\" are\
      \ being used as features in ML systems that do things like:\n- Calculate the\
      \ likelihood of fraud in an insurance claim\n- Quantify identity matches between\
      \ two profiles in social networks\n- Provide \"realtime\" content personalization\
      \ when viewing a webpage\nResearchers and engineers are converging to using\
      \ features like the 3 I shared above after they spent time running graph algorithms\
      \ across their data.\nI hope that helps! I'm going to move to your next ones\
      \ :)"
- name: Matthew Emerick
  text: After working through your book, what is you recommended next best step in
    working with graph data?
  replies:
  - name: Denise Gosnell
    text: 'Great question!

      As I see it, the way to apply this to a new problem is to:

      1. Model your domain data as a graph

      2. Check if the known patterns are relevant to your business problem. (Known
      patterns are neighborhoods [chs 3,4,5], hierarchies [chs 6,7], paths [chs 8,9],
      and recommendations [chs 10, 11, 12])

      3. Use graph algorithms to find new correlations in your data.'
- name: Matthew Emerick
  text: Before picking up the book, what prerequisites do you recommend people have
    to get the most out of what you teach?
  replies:
  - name: Denise Gosnell
    text: "Matthew Emerick that depends on which part of the industry you are coming\
      \ from \U0001F642\nThe preface as a longer version of this.\nThe tl;dr - I recommend\
      \ that you\n- Have worked with databases before\n- Understand or have experience\
      \ in doing data ETL\n- Have an open mind to trying new things \U0001F642"
- name: Neal Lathia
  text: "\u2754 What are the most impactful use cases for graph data?"
  replies:
  - name: Denise Gosnell
    text: Neal Lathia I am going to pick up with this question on Tuesday morning!
      Thank you!
  - name: Denise Gosnell
    text: 'Neal Lathia Thank you for the question.

      I have a bias behind my answer. My bias is that "impactful use cases" are those
      which are deployed into production settings. And, the majority of my experience
      from production deployments is in the data management space and less in production
      data science.

      From that perspective, the most popular ways that companies around the world
      are using graph data in production is:

      1. Customer 360 style apps

      Chapters 3, 4, and 5 go into detail on how a bank (and insurance companies,
      governments, etc) I''ve worked with use "neighborhoods" to create a "360" view
      of important entities of the business.

      Specifically, the most popular question that I have seen graph data used to
      answer is: "what are all the pieces of information we know about this entity
      (usually a person)?"

      Those queries typically inform one of 2 systems in my experience:

      - Customer Service interfaces (showing all recent interactions across different
      channels like social, web, and/or in-store)

      - Analyst Investigation interfaces (like fraud or marketing analysts)

      There are other popular use cases, but customer 360 is the most common deployment.
      The other 3 super popular ways graph data is use in a production system are:

      1. Recommendations (eg: netflix or shopping cart recommendations)

      2. Hierarchies (eg: employee trees)

      3. Path Finding (eg: how are these 2 pieces of information related?)

      I hope this helps. Please let me know if you have any additional questions.
      Thank you!'
  - name: Alexey Grigorev
    text: 'What''s customer 360? This?

      [https://globalz.com/customer-360-single-customer-view/](https://globalz.com/customer-360-single-customer-view/)'
  - name: Alexey Grigorev
    text: I guess wikidata could be something similar, right?
  - name: Denise Gosnell
    text: Alexey Grigorev you got it!
- name: Nick McClure
  text: 'I actually own this book! I''m on chptr 3. In chptrs 1 &amp; 2, the book
    talks about the importance of recognizing when a problem needs graph-DBs/graph-data.
    I''m worried about being over zealous about using new technologies sometimes.

    Can anyone give an example of an instance or case where they considered graph
    data / DBs and decided not to?'
  replies:
  - name: Denise Gosnell
    text: 'Nick McClure great! Thanks!

      I am going to pick up with this question on Tuesday morning'
  - name: Denise Gosnell
    text: 'Nick McClure great question!

      And -- I would love for everyone in here to jump on and add ways they have used
      graph databases in production.

      (my response in this thread)'
  - name: Denise Gosnell
    text: 'One example I personally built was the United States Health Graph

      - [Co-occurance graph of digital services](https://github.com/denisekgosnell/denisekgosnell.github.io/blob/master/data-day-2017/health/providers_100k_v1_small.jpeg)

      - [Referral Network of US Physicians ](https://github.com/denisekgosnell/denisekgosnell.github.io/blob/master/data-day-2017/health/top_grossing_referral_physicians_small.jpeg)

      There are many others, but these two are my favorite because they each generated
      business outcomes that saved millions of dollars.

      First - the co-occurance graph of digital services was constructed and analyzed
      in 2015. This graph had the largest connected cluster around "online therapy
      services". In 2015, this demonstrated the upcoming trend of traction for using
      online digital interactions for therapeutical services, like talk therapy. It
      is very heartwarming to see how many people in 2021 are benefiting from the
      US Healthcare industry''s investment in digital care for mental health professional
      services.

      The second graph, the referral network, unveiled a billion dollar fraud ring
      in Florida! This fraud ring is observable in the visualization linked above.
      We noticed 2 aspects about a specific doctor in florida.

      #1) the doctor received and outlier amount of reimbursements from medicare (data
      available from the CMS)

      #2) the patient network was distributed atypically across the entire united
      states

      [Here is a screen shot of the article from the Miami Herald](https://github.com/denisekgosnell/denisekgosnell.github.io/blob/master/data-day-2017/health/1BFraudCase.png)

      I would love to hear from others on how they have used graph dbs!'
  - name: Nick McClure
    text: Thank you for the graph examples! I am excited to use the technology- but
      were these examples were you ended up *not* using graph technology? Specifically
      I am asking about over applying it where it was not needed.
  - name: Jessie Yaros
    text: "I\u2019ve read that if you're not so interested in the relationships among\
      \ items, or if you\u2019re data doesn't lend itself to being modeled as a network\
      \ of connections, then you may not want to try for graphs over rdbms. Total\
      \ noob here though- that\u2019s just what I've heard."
  - name: Denise Gosnell
    text: "Nick McClure thank you for the clarification!\nHere is a list of projects\
      \ that we didn\u2019t use a graph db for:\n1. Business metrics dashboard (eg:\
      \ viewing week over week trends of company metrics)\n2. Searching for products\
      \ by name, or any other filter like color, size, etc\n3. Inventory management\
      \ of a product catalogue \nThe common theme in the examples above is that the\
      \ data fits into one table."
- name: Denise Gosnell
  text: "Hello everyone! I am jumping in here for a bit to answer questions. \U0001F642\
    \nTo start - we open sourced two parts of our book.\n1. [All our images are here\
    \ in LucidCharts](https://lucid.app/folder/invitations/accept/0b959629-50f6-4b1e-96ce-98df831ea9c0)\n\
    2. [Our code examples in notebooks are here](https://github.com/datastax/graph-book)\n\
    Thank you so much Alexey Grigorev for inviting me into this week's session. See\
    \ you in the threads!"
  replies:
  - name: Alexey Grigorev
    text: Thank you for agreeing!
- name: Denise Gosnell
  text: Oh! If you would like to get chapters 3 through 5, [you can download them
    for free from DataStax](https://www.datastax.com/resources/ebook/oreilly-graph-guide)
  replies: []
- name: Vladimir Finkelshtein
  text: "I am wondering if recent theoretical solution of graph isomorphism problem\
    \ had any impact on the practical side. I imagine it is relevant for pattern searches\
    \ in the graph, but then I guess that for most common patterns, there were already\
    \ decent algorithms\u2026"
  replies:
  - name: Denise Gosnell
    text: 'Vladimir Finkelshtein that is a great question.

      can you post a link to the recent solution you are referring to?

      in production systems, I haven''t seen pattern matching extend beyond triangle
      predictions. There are many creative ways to apply graph isomorphisms, but none
      that I have seen be deployed in a company''s data architecture.'
  - name: Vladimir Finkelshtein
    text: "[https://en.wikipedia.org/wiki/Graph_isomorphism_problem](https://en.wikipedia.org/wiki/Graph_isomorphism_problem)\n\
      I am not sure if it is relevant for graph databases. I just remember when it\
      \ was announced, quasipolynomial bound was a very big deal for people in CS,\
      \ but I still don\u2019t know what are the applications of it \U0001F642"
  - name: Vladimir Finkelshtein
    text: I was imagining that if you query the database for certain relationships,
      it means that you need to find subgraphs isomorphic to the graph.
- name: Toxicafunk
  text: 'Hi Denise Gosnell, thank you for doing this!

    What are your thoughts on Apache Tinkerpop and particularly on the Gremlin graph
    traversal language to be used on mutliple backends as constrasted against somtehing
    like Neo4j''s Cypher which is, presumably, optimized for a single backend? (I
    understand Cypher is used on other backends besides neo4j but I am assuming it
    works best on neo4j)'
  replies:
  - name: Denise Gosnell
    text: "Toxicafunk great question, thank you for asking it!\napache tinkerpop is\
      \ the most widely adopted graph traversal language as it is used by most graph\
      \ DBs. There are even popular gremlin to cypher compilers.\nYes, cypher works\
      \ best on Neo4J.\nIrrespective of the optimization of the query language, the\
      \ graph industry is in need of an _easier_ to use language than both Cypher\
      \ or TinkerPop. I love gremlin, but there is a super steep learning curve (as\
      \ evident in a 400+ page book on how to use it! \U0001F606 )\nI am currently\
      \ working with Apollo to see how we can potentially look at the GraphQL language\
      \ as an easier way to express graph traversals and graph shaped problems. However,\
      \ under the hood, the functional programming approach to gremlin for server\
      \ side optimizations is brilliant and has yet to be matched with another tool.\
      \ Marko, Daniel, and Stephen (and others!!) created a beautiful and brilliant\
      \ language for solving graph problems. We just need an easier interface for\
      \ using it, IMO.\nI am most excited about the innovation in the space of graph\
      \ query languages. I am excited to see what others invent!"
- name: Vladimir Finkelshtein
  text: I am sure we will hear about many use-cases of graph databases. When should
    we not use them? Are there simple examples of data, where relationships are better
    stored and queried in a relational database?
  replies:
  - name: Denise Gosnell
    text: 'Vladimir Finkelshtein thank you for asking this one.

      tl;dr: if you only care about properties of your data (like, what is the age
      distribution of my customers?) than a graph database is overkill.

      Use a graph only when the _relationships_ between your primary entities are
      central to your question.

      For a longer explanation --  we go into detail on this in chapter 1. After working
      with 100s of teams around the world, I created the image below as a way to think
      around this question.

      This is image 1-5 from Chapter 1. The link to the live LucidChart is in this
      channel.'
  - name: Denise Gosnell
    text: Please let me know if you have any further questions, thanks!
- name: Jessie Yaros
  text: Omygosh, I just joined this community this week, and I am so amazed that this
    is the first book of the week I'm exposed to! Thanks to Denise Gosnell and Alexey
    Grigorev. I actually added your book to my amazon wishlist a few weeks ago, so
    this is a wonderful coincidence. I've been using graph theory and algorithms in
    my phd research, but am really hoping to transition and be able to employ 'graph
    thinking' and tools in the real world. I'm curious if you have advice/ideas on
    the types of industries or even job titles that are most likely to value background
    in working with graphs. I'm finding that its rare to find job postings that require,
    or even mention wanting candidates who have a graph theoretical background or
    experience with graph algorithms. With how excited people seem to be about graphs,
    do you envision these types of tools and skillsets will become ever more popular/
    in demand? Or am I totally looking in the wrong places, potentially using the
    wrong keywords?!
  replies:
  - name: Denise Gosnell
    text: 'Jessie Yaros -- i _love_ these questions - thank you!

      I will pick up with yours first thing on Wednesday, if not sooner.'
  - name: Denise Gosnell
    text: "Jessie Yaros great question!\nThere are two places to look:\n1. Jobs for\
      \ now\n2. Jobs for the future \nJobs to look for now will be: data scientists,\
      \ data strategists, data analyst, data architects, etc\nIn the future, the concept\
      \ of a \u201Cdata mesh\u201D is likely to become a prominent aspect of every\
      \ company\u2019s data architecture. A \u201Cdata mesh\u201D graphs the movement\
      \ of data around a company from one place to another. This is higher up than\
      \ instances of graph data, but the entire flow of data is a graph. I recommend\
      \ following Martin Fowler\u2019s work on this topic in the coming 5 years to\
      \ see how it evolves.\nI also recommend the following industries for interesting\
      \ graph data: logistics, entertainment, and healthcare.\nIf you are looking\
      \ for a job, happy to help connect you to people looking for graph folks. Just\
      \ lmk!"
  - name: Jessie Yaros
    text: 'Denise Gosnell Awesome - just followed his blog - thanks for the rec -
      haven''t heard of data mesh yet!

      And uhhhhhhhhhm yeah I''d love some connections/introductions! I''m based in
      LA so I''ve been thinking entertainment may be a good option but in my heart
      of hearts, I think healthcare might be a better fit with my neurosci background
      and health interests. I have a few ideas for clinical graph projects that I''d
      really love to tackle, once i wrap up writing my dissertation haha. My advisor
      says I have to stop creating more projects for myself! I''ll connect with you
      on LI, and would love to hear more of your thoughts!'
  - name: Alexey Grigorev
    text: Denise Gosnell I know almost nothing about data mesh, but it seems it's
      more an organizational structure than some technology. So I'm wondering where
      do graph databases come into play when it comes to datamesh?
  - name: Denise Gosnell
    text: "Alexey Grigorev great question! I think of a data mesh at a higher level\
      \ up from the actual data base.\nIn a data mesh, you still have \"edges\" and\
      \ \"vertices\".\nThe edges represent streaming or batch jobs that move data\
      \ through one flow to another. The vertices are data stores. These data stores\
      \ are anything from:\n&gt; custom views (dashboards), to \n&gt; databases (like\
      \ relational, or graph databases, or s3 buckets), to \n&gt; tools (like marketo,\
      \ salesforce, workday, etc). \nThe data architecture of an entire company is\
      \ essentially a graph - and therefore folks are starting to recognize that we\
      \ are really building a massive data mesh."
  - name: Alexey Grigorev
    text: okay, that makes sense now, thank you for clarification!
  - name: Denise Gosnell
    text: "You're very welcome Alexey Grigorev \U0001F642"
- name: Jessie Yaros
  text: "Do you have strong opinions on the best graph databases. graph query languages\
    \ to start working with? I've dabbled with neo4j (and cypher), but am curious\
    \ whether other options like TinkerPop, might have larger appeal in industry.\
    \ I'm noticing that more platforms seem to use gremlin than cypher, so I've been\
    \ wondering which would be better to invest in learning.\nEdit: I see now you\
    \ are with Datastax but still would love your thoughts \U0001F642 . Another question\
    \ this brings up, is whether there are major differences in working with a db\
    \ marketed as NoSQL vs Graph. Are NoSQL just more versatile? Could that cause\
    \ steeper learning curves?"
  replies:
  - name: Jessie Yaros
    text: 2nd Edit- I just read your other thread that goes into gremlin/neo4j !
  - name: Denise Gosnell
    text: 'Jessie Yaros I recommend knowing gremlin, GraphQL, and SQL. Those 3 languages
      will teach you everything you need to know to query databases and use graph
      technology.

      Cypher is only used by Neo4J and was designed off of SQL.'
  - name: Jessie Yaros
    text: Awwww well that makes sense, why Cypher seems intuitive to me --since I
      know SQL. So at least that's one down! Thanks for the tips!
- name: Jessie Yaros
  text: Do you think that GQL will change the game once its released? Would you expect
    most (property) graph databases to try and implement its usage?
  replies:
  - name: Denise Gosnell
    text: "Jessie Yaros I am biased with my response here. But! I have been following\
      \ GQL for 5+ years and haven\u2019t seen any results. As with any new tech,\
      \ expect the language to take at least 3-5 years from being released to being\
      \ relevant with adopted use."
- name: Jessie Yaros
  text: Denise Gosnell Do you believe that there will always be different/ideal use
    cases for property graphs and RDFs/knowledge graphs? Or do you think that one
    type might become more dominant? LPG's seem so much more intuitive to me, but
    knowledge graphs have become such a buzz word!
  replies:
  - name: Denise Gosnell
    text: "Jessie Yaros personally, I see each of the technologies as being useful\
      \ for different problems. So I expect both will stick around \nLPGs are much\
      \ more popular today than RDFs.\n\u201Cknowledge graphs\u201D are a catch all\
      \ term with lack of specificity in the two domains."
  - name: Jessie Yaros
    text: "Denise Gosnell Yeahhh I do see some people using the term knowledge graph\
      \ interchangeably with RDF, which was confusing to me since I assumed you could\
      \ build a KG with both! And I'm glad to hear that LPGs are more popular. When\
      \ I started working with graphs for brain connectivity, I wasn't aware yet that\
      \ they were of the LPG type. So when I went to a few talks on knowledge graphs,\
      \ expecting the LPG format, i was like, waiiiit. What are these triplets. \U0001F605"
  - name: Denise Gosnell
    text: Jessie Yaros I can relate!!
  - name: Jessie Yaros
    text: "\U0001F923"
- name: Vladimir Finkelshtein
  text: What are some public graph datasets you can recommend for practice with graph
    databases?
  replies:
  - name: Denise Gosnell
    text: 'Vladimir Finkelshtein the GitHub with my book comes with datasets :relaxed:

      I get my graph data from:

      1. Snap: [http://snap.stanford.edu/](http://snap.stanford.edu/)

      2. Kaggle: [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)

      3. Or, this GitHub

      : [https://github.com/awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)'
  - name: Vladimir Finkelshtein
    text: Thanks for the links. The datasets in kaggle (and most public datasets I
      have seen) usually come as single tables, so I am not sure how many interesting
      relationships between entities I can explore in the majority of them. You mentioned
      that you used graph database to build referral network of physicians. I am pretty
      sure, this is not public, but I was wondering if there is anything of this type
      where people can explore how it works.
  - name: Jessie Yaros
    text: At least for me its been an adjustment reinterpreting data in terms of how
      we can represent it in  graphs, since we are so used to thinking about data
      in a relational table like manner. But even data in one table can be thought
      of in terms of relations, (rather than thinking of relations as being only joins
      between tables). For instance, you might have a simple table with just one column
      for customers and one column for favorite movies. You could then re-represent
      that information in graph format by having nodes for each customer, and nodes
      for each movie, where you link customers to the movies they like. Then you could
      do fun stuff like looking for customers that have similar movie preferences,
      and could make educated movie recommendations based on that!
  - name: Denise Gosnell
    text: 'Vladimir Finkelshtein and Jessie Yaros if you want "graph ready, no etl"
      datasets, head straight to SNAP from Stanford

      The US Referral network data is hosted by the CMS:

      [https://www.cms.gov/Regulations-and-Guidance/Legislation/FOIA/Referral-Data-FAQs](https://www.cms.gov/Regulations-and-Guidance/Legislation/FOIA/Referral-Data-FAQs)'
  - name: Vladimir Finkelshtein
    text: Thanks a lot
  - name: Vladimir Finkelshtein
    text: "Jessie Yaros indeed, you can represent movie ratings datasets as a graph,\
      \ but I never thought about movie recommendations as a graph problem (I realize\
      \ now it\u2019s 3 chapters in the book of the week \U0001F603). For example,\
      \ matrix factorization techniques for recommendation engines - they do indeed\
      \ factorize the adjacency matrix of a graph you described, but the latent features\
      \ that they discover don\u2019t clearly have much to do with the graph, as far\
      \ as I know. These latent features are more naturally seen as vectors. Some\
      \ other techniques, like cosine similarity between users can be expressed in\
      \ the graph via paths, but it will be more cumbersome then just using vectors.\n\
      I was thinking of older approaches in e-commerce like finding association rules\
      \ as graph based, but my impression was that they are not widely used any more,\
      \ because they are too slow.\nBut I guess, part of the purpose of this book\
      \ is to change this mindset. I am wondering if any interesting things can be\
      \ said about movies by inspecting properties of neighborhoods in this graph.\
      \ Anyway, just some thoughts\u2026"
  - name: Jessie Yaros
    text: 'Cool to know! I''ve heard of matrix factorization but don''t more more
      than the name. I know some people are doing graph embeddings to vectorize graphs
      pre ML pipelines... wondering if that is similar?

      Im not sure how often graph rec engines are using metrics of overall similarity
      vs just traversing paths based on shared movie interests to make those recommendations...'
  - name: Denise Gosnell
    text: "Vladimir Finkelshtein I like using graphs to do recommendations because\
      \ the algorithm essentially comes down to a group count! so much easier to think\
      \ about (at least in my head) than matrix factorizations and cosine similarities\
      \ \U0001F604"
  - name: Denise Gosnell
    text: 'Jessie Yaros the graph rec engines are just traversing paths and counting
      - and, you can use weights on the edges if you wanna get fancy.

      TBH, I like counting instead graph paths instead of matrix and vector spaces
      that are hard to visualize. :woman-shrugging:'
  - name: Jessie Yaros
    text: "Yeah! It\u2019s nice how intuitive it is."
- name: Alexey Grigorev
  text: 'A slightly unrelated question:

    What do you do as a chief data officer? And, in your opinion, is it different
    from other companies with a similar role?'
  replies:
  - name: Bayram Kapti
    text: I am interested in this question as well!
  - name: Denise Gosnell
    text: 'Great question Alexey Grigorev and Bayram Kapti

      As a CDO, the top 2-3 outcomes are:

      1. Ensure continual delivery of business critical data, metrics, and feeds throughout
      the enterprise to support decision making. (this looks like establishing CI/CD
      around data sources, tools, and custom built software)

      2. Minimize cost and risk within the tech stack and supporting resources. (here
      you run into compliance, budget, knowledge management, etc)

      3. Maximize efficiency and access to tools and information (eg: process and
      operations, data sprawl wrangling, etc)'
  - name: Denise Gosnell
    text: 'This creates more of a data mesh architecture at the business level than
      the granular use of graph data.

      so, graph knowledge not required - but it does make it easier to wrap your head
      around an entire company''s data processing.'
  - name: Bayram Kapti
    text: Thanks for the insights Denise! Much appreciated!
  - name: Denise Gosnell
    text: "Bayram Kapti anytime! happy to help \U0001F60A"
- name: Alexey Grigorev
  text: "What kind of skills does a CDO need? Apart from good knowledge of graphs\
    \ \U0001F603"
  replies:
  - name: Denise Gosnell
    text: "Alexey Grigorev A CDO needs to be able to:\n- Manage Budget\n- Optimize\
      \ investments\n- Minimize risk / expenditures\nGraph knowledge not required\
      \ \U0001F61E"
  - name: Denise Gosnell
    text: Being a CDO essentially feels like the master builder of a company wide
      marble run set. :)
  - name: Alexey Grigorev
    text: That's a nice marble run set! Thank you for your answer
  - name: Denise Gosnell
    text: Alexey Grigorev of course, you are welcome!
- name: Alexey Grigorev
  text: Denise Gosnell you mentioned data mesh in one of the threads. Recently it
    became quite popular. Do you have some ideas why?
  replies:
  - name: Denise Gosnell
    text: 'Alexey Grigorev yes!

      I hypothesize that data mesh architectures became very popular because:

      - Data is sprawled out all over a company and siloed by business function

      - Data is heavy to move

      - Data is more valuable when connected

      Those facts all-together are driving more companies to create streaming highways
      from one silo of data to another instead of lifting and shifting all data into
      one big new system.'
  - name: Alexey Grigorev
    text: 'So I guess the main downside of the central lake/platform is that you need
      to move the data across the entire org, and that''s often difficult and expensive.

      If I understood you (and what I heard about data mesh previously), the main
      idea is now each team/department can have their own lake.

      These lakes have to be connected somehow - in such a way that an analyst knows
      how to pull these datasets together to do their analysis.

      And graphs help to connect the dots - to connect different "lakes" to each other
      and have this big picture.

      Am I close?'
  - name: Denise Gosnell
    text: 'Alexey Grigorev you got it!

      There is a data mesh slack channel if you wanna hang out there and see how folks
      are discussing the idea: [https://join.slack.com/t/data-mesh-learning/shared_invite/zt-nrh42jd1-B~YAplAKzHl3hyP039UQSw](https://join.slack.com/t/data-mesh-learning/shared_invite/zt-nrh42jd1-B~YAplAKzHl3hyP039UQSw)'
  - name: Alexey Grigorev
    text: "Thanks! I'm actually there already, but the amount of information there\
      \ is a bit overwhelming \U0001F603 So thanks for making it clear to me, and\
      \ kudos to Scott Hirleman (he/him) for organizing the community!"
  - name: Denise Gosnell
    text: "I didn't know Scott Hirleman (he/him) was in this slack universe! he is\
      \ _everywhere_ \U0001F601"
- name: Vladimir Finkelshtein
  text: 'NLP related question (sorry if completely off topic): I have heard some time
    ago of an approach to embed the vocabulary of a language in a graph: words as
    vertices and (weighted) edges representing semantic (or any other) similarity
    between two words. So it would be logical to use such graphs for NLP problems.
    Do you know of any such applications?'
  replies:
  - name: Denise Gosnell
    text: 'hey hey Vladimir Finkelshtein - i love the conversation, keep it coming!

      I am not well versed in this style of graph for NLP.

      How would you calculate similarity between two words? What is the cut-off for
      storing an edge to represent similarity? And, how would you query or use this
      structure once you created it?

      Thanks!'
  - name: Vladimir Finkelshtein
    text: "I am not well versed in NLP either. There are many notions of similarity,\
      \ and many complicated ways to compute them. NLP libraries like NLTK have them.\
      \ One can also train word embedding and calculate distances between words there.\
      \ I don\u2019t know if this is actually used, but a naive way of thinking (just\
      \ to get the idea) is to take a big text corpus, and define similarity between\
      \ two words as the number of times they appear together in the same paragraph\
      \ divided by total number of paragraphs each of the words appears in. This way,\
      \ bus will be more similar to driver than to elephant. Of course, this is too\
      \ naive. Wikipedia entry on semantic similarity has many references to different\
      \ ways to compute it.\nSetting thresholds which edges to include is a matter\
      \ of fine-tuning.\nAs for uses, I don\u2019t have a good idea, that\u2019s why\
      \ I asked. One example off the top of my head: say you have a news article,\
      \ and you look at all the words that appear in the news article, and look at\
      \ the subgraph in your database that these words induce (I hope it\u2019s clear\
      \ what I mean here). My intuition tells me that if one finds a big clique in\
      \ this subgraph, these would be the words that represent the main topic of the\
      \ article. The less connected words are the ones that are not good for specifying\
      \ the topic. So something like this could be used for topic classification or\
      \ keyword extraction.\nSorry if the explanation is too messy, it\u2019s just\
      \ an idea. It just seems very natural to use this structure in NLP context."
  - name: Vladimir Finkelshtein
    text: Basically what I describe above, is a version of kmeans clustering, but
      done not in Euclidean space but on a graph. Cliques are the dense clusters.
  - name: Denise Gosnell
    text: "Vladimir Finkelshtein I know NLP well as I implemented semi-discrete matrix\
      \ decomposition for my PhD.\nAs we are outlining here, the crux of the problem\
      \ is how modeling word similarity in a graph would be a better (faster? more\
      \ accurate? more expressive?) way to determine topics within a corpus.\nI agree\
      \ with how you outline the problem.\nAnd, that clique detection would be the\
      \ algorithm to use once the data is in the graph.\nHowever, every word has a\
      \ measurement of similarity to any other word. Thus, the whole graph is _technically_\
      \ a clique. So, the fine-tuning of edge weights for inclusion in the graph,\
      \ or algorithm if we take the approach to store everything and filter on processing.\n\
      You are outlining a really interesting problem. And, it would be very valuable\
      \ to understand if the graph based approaches are measurably better than other\
      \ matrix based representations. Could be a good topic for a PhD! \U0001F605"
  - name: Vladimir Finkelshtein
    text: 'If I had to bet, it will be slower for sure, but it has a chance to be
      more expressive. All the word embeddings that we have now are in Euclidean space,
      and it is very restrictive in what kind of distances it allows between points
      in space. For example, there is no good way to draw a world map in a plane without
      totally distorting a lot of the distances. Graphs give you complete freedom
      in this sense.

      As for concern of everything being a clique, I agree that choosing a good threshold
      might be hard and depend on very good notion of similarity. One could also try
      to replace finding a clique by finding dense regions (in terms of sum of edge
      weights).'
- name: Jessie Yaros
  text: Another one for you Denise Gosnell ! How do people model temporal or timeseries
    data in graphs?  Most of the graph stuff I'm familiar with is more static in nature,
    but I know in reality many networks are more dynamic... Like,  for instance are
    edges assigned time point values, or could whole graphs be made for individual
    time points and then be stitched together? Or something fancier??
  replies:
  - name: Denise Gosnell
    text: 'Jessie Yaros I love the questions, keep ''em coming!

      tl;dr: time in graphs is usually represented as a property on an edge. And,
      an edge is stored every time there is data to capture.

      We go though this in detail in chapters 2 and 7. Throughout ch 6 and 7, we walk
      through what we built for one of the US energy companies who care about the
      time of communication between two sensors in the energy grid.

      The image below is 7-1, showing how we store multiple edges between two sensors
      in Seattle''s energy network: one edge per transmission between two sensors.
      The property on the edge is the time when the communication occured.'
  - name: Jessie Yaros
    text: Ooooh so coooool, thank you!!
- name: Rich
  text: 'Hi Denise Gosnell,  Thanks so much for hosting this channel on Graph Data.  I
    just recently discovered your book and I''m reading through it now.  I''ve been
    exploring this topic from the Semantic Web aspect where products such as AnzoGraph
    (multi-model) use the standards based RDF and SPARQL along with the use of Ontologies
    and Knowledge Graphs.  How do these technologies fit into or extend the utilization
    of Graph Data as presented in your book?

    While reading your book I also ran across a reference to the Unified Modeling
    Language (UML, fig 2.1).  I''ve been a Software Engineer for many years and built
    many object models using UML so it extends well beyond relational data models.  At
    the time we went onto persist our object model into an Object Database such as
    Objectivity (and their follow-on graph database InfiniteGraph).  In many ways
    I view the uprising of Graph Data as a new spin on an object model and Object
    Databases (adding the graph related algorithms such as Centrality, etc.).  What
    is your take on this view?

    Lastly, I''ve been a user of Python NetworkX which has an abundance of different
    graph algorithms.  To your knowledge, can their implementation sit on top of an
    existing graph database for persistence?  As a Data Scientist I''ve been looking
    at ways to incorporate ML into this Graph Data world and I''m still getting my
    arms around it.  Do you have an recommendations beyond your excellent book?

    Thanks for your time......Rich'
  replies:
  - name: Denise Gosnell
    text: "Hey Rich - thank you for the questions!\n&gt; RDF / SPARQL -- How do these\
      \ technologies fit into or extend the utilization of Graph Data as presented\
      \ in your book?\nThe world of RDF &amp; semantic graphs is a set of adjacent\
      \ technologies to property graphs. [I recommend this excellent discussion on\
      \ the topic. ](https://www.youtube.com/watch?v=OTPTq5_ifvY)TBH, I wouldn't do\
      \ the topic of RDFs justice and refer to the work directly written by Jans Aasman\
      \ or Juan Sequeda on the topic \U0001F642\n&gt; In many ways I view the uprising\
      \ of Graph Data as a new spin on an object model and Object Databases. What\
      \ is your take on this view?\nAt the end of chapter 2, we detail our view \U0001F60A\
      \ We present the \"GSL - graph schema language\" that is very close to UML.\
      \ The GSL is a way to visually communicate the details of your graph schema,\
      \ just like UML or ERDs outline relational database.\nThe tricky parts of the\
      \ GSL (or communicating about graph schema in general) are representing the\
      \ multiplicity of edges in your graph; something my co-author and I spent a\
      \ long time working through for our book (longer than we care to admit \U0001F606\
      \ ).\nI would love to know you thoughts / criticisms / improvements to the GSL.\
      \ It sounds like we both see the importance in this type of innovation for the\
      \ industry.\n&gt; NetworkX - To your knowledge, can their implementation sit\
      \ on top of an existing graph database for persistence? Do you have an recommendations\
      \ beyond your excellent book?\nYES! I love python and also use NetworkX! \U0001F604\
      \nHowever, in production data architectures, the common pattern is to connect\
      \ to a graph database via spark and use spark's library of graph algorithms.\
      \ Spark supports [graphFrames and graphX](https://spark.apache.org/graphx/)\
      \ and is much more widely adopted within data science teams. Therefore, I have\
      \ more experience working with those libraries.\nI recommend becoming familiar\
      \ with [Spark's GraphX libs](https://spark.apache.org/docs/latest/graphx-programming-guide.html)\
      \ as they are supported by multiple graph databases."
  - name: Rich
    text: "Hi Denise Gosnell, Thanks for the great references.  I did watch the video\
      \ you suggested and it did clear up the difference between Property Graph and\
      \ RDF implementations.  If you don't mind here is what I learned:\n1. Property\
      \ Graph appear to be more project based given they don't use a Taxonomy or Ontology\
      \ that would be defined for the Enterprise.  The RDF approach is geared more\
      \ toward a coherent method for the entire Enterprise as opposed to perhaps a\
      \ siloed approach.\n2. I also thought I hear that RDF allowed for an embedded\
      \ Object definition much like an Object-Oriented language would support.  \n\
      3. RDF were more complicated to use and implement but I think this was based\
      \ on the broader scope of what these usually entail (building a Taxonomy and\
      \ an Ontology).  \nJans also said that Gartner was thinking that Graph databases\
      \ would become the predominate platform within ~ 10 years.  What are you thoughts\
      \ on that prediction?\nOn that same theme not sure if you've heard of the \"\
      Data-Centric\" architecture ([http://www.datacentricmanifesto.org/](http://www.datacentricmanifesto.org/))\
      \ but this is what Dave McComb is pushing a move to Ontologies and Graph databases.\n\
      One last question.  Could you provide any additional resources on \"Entity Resolution\"\
      ?  I'm reading though this in your book now.\nThanks again for your thoughtful\
      \ comments and insights.\nRich"
  - name: Denise Gosnell
    text: "Rich thank you for the follow up!\nwrt to Gartner's predictions - my passion\
      \ and life's work centers on graph data and databases. So, I hope they are right!\
      \ I am seeing graphs used more and more as the next secret weapon for advancing\
      \ feature development and signal investigations at large companies. Thus, I\
      \ agree with this prediction. However, I am a source of bias here as this topic\
      \ is what people come to ask me about.\nI had not heard of data-centric architectures\
      \ with this specific label. After reading the manifesto - this sounds very near\
      \ and close to the same momentum behind the data mesh community. Looks like\
      \ a lot of overlap! \U0001F642\nFor entity resolution - what kind of resources\
      \ are you looking for - algorithms, applications, latest papers, etc? My PhD\
      \ is on this topic -- specifically the application of it to trace identity throughout\
      \ social networks, or social fingerprinting -- so I would love to share more."
  - name: Rich
    text: 'Thanks for the quick reply Denise Gosnell.  The more I look at the Graph
      data and the related semantic model the value proposition makes sense to me.  The
      ''schema on read'' seems like a very important feature.  I do wonder about the
      scalability.

      I came across the Data-Centric movement when doing some work for the DoD last
      year.  While I think the idea is a very good one, I believe many large organizations
      will struggle to migrate away from their stove piped relational world.  Dave
      has published a book on the topic here ([https://www.semanticarts.com/publications/](https://www.semanticarts.com/publications/))
      which also seems to fit into an architecture I''ve seen called Data Fabric (looks
      like an earlier cousin of Data Mesh).  The "schema on read" featured of Graph
      databases controlled via an Ontology fits well within his focus on pairing down
      the many Enterprise schemas but having an extendable core model.

      On the Entity Resolution problem, I''m looking at a new opportunity that involves
      this task.  I''ve used NER before to identify entities within a body of text
      but this area of study is new to me.  Any resources you think would be helpful
      would be much appreciated.  Of course, you have a great example I''m working
      through in your book.

      Many thanks again.....Rich'
  - name: Denise Gosnell
    text: "Rich do you know when the \"data centric\" manifesto started? I would love\
      \ to learn more.\nAnd yes - looks like \"data fabric\" is the earlier cousin\
      \ of data mesh \u2705\nwrt to NER and Entity Resolution -- what data sources\
      \ are you using in your new task? If you are looking at a large corpus of text,\
      \ the latest to consider might be [how to do so with Spark.](https://towardsdatascience.com/named-entity-recognition-ner-with-bert-in-spark-nlp-874df20d1d77)\n\
      I have had the luxury to work with more structured data like telecommunication\
      \ records (or I choose to boil the problem down to entities). Thus, like I outline\
      \ in chapter 11, my experience in Entity Resolution is closer to matching and\
      \ ranking algorithms. I find [Dr. Amy Langville's book](https://g.co/kgs/W3CLXR)\
      \ to be very helpful in understanding the math and science of ranking, which\
      \ comes into play when you are deciding if your algorithms are correct (or not)."
  - name: Rich
    text: 'Hi Denise Gosnell,  My apologizes for the belated response.  I looked back
      through Dave McComb''s blog post and see the oldest entry is in 2015 ([https://tdan.com/the-data-centric-revolution/18780](https://tdan.com/the-data-centric-revolution/18780)).  Based
      on my conservations with him he started down this Data-Centric path after seeing
      some of these large ERP systems being built (SAP, etc.).

      If you have a moment I wanted to get your thoughts on one additional thing.  I
      was reflecting back on some of my graph related work and wondered if "Similarity-Based
      Networks" could be a good framework for Entity Resolution?

      Thanks again for the book and great dialogue here.  It has been very beneficial.  Rich'
- name: Denise Gosnell
  text: 'I am loving all of the questions this week! Thank you all so much for inviting
    me in here and making me feel so welcome :heart:

    You are welcome to ask-me-anything! I am on the east coast of the USA and will
    be around until the end of the day on Friday for Q&amp;A.'
  replies: []
- name: Vladimir Finkelshtein
  text: You defined social fingerprint in your research. Does it mean that graph data
    should be treated like dataset of fingerprints from the point of view of privacy?
    Is there a way to anonymize graph data?
  replies:
  - name: Denise Gosnell
    text: 'Vladimir Finkelshtein yes! The interactions we generate on social media
      are uniquely identifying for any individual in the world. Your words of "graph
      data is a dataset of fingerprints" is a really great way to describe it.

      The way to anonymize graph data is very similar to how advancements in blockchain
      are progressing - by uniquely changing the ID of your vertex for every network
      interaction.'
  - name: Toxicafunk
    text: that's what monero does I think
  - name: Denise Gosnell
    text: Toxicafunk yes! monero is it; I couldn't remember the name. You are correct,
      thank you!
  - name: Jessie Yaros
    text: We have neural fingerprints in fmri research!
  - name: Toxicafunk
    text: How does that work Jessie Yaros?
  - name: Denise Gosnell
    text: coo cool Jessie! I would love to hear more
  - name: Jessie Yaros
    text: 'Sure! There is not a specific method for neural fingerprinting, but seems
      to be a catchall term used in studies that use brain connectivity data to identify
      individual participants. For fun I''ll link two papers that do it differently.
      One uses similarity between connectivity/association matrices/graphs, and another
      uses a ML classifier I think. I may give it a try with graph embeddings and
      some sort of clustering technique with my own dataset, we see we see

      [https://www.nature.com/articles/nn.4135](https://www.nature.com/articles/nn.4135)

      [https://www.sciencedirect.com/science/article/pii/S2589004219305474](https://www.sciencedirect.com/science/article/pii/S2589004219305474)'
- name: Dr Abdulrahman
  text: 'Thank you Denise Gosnell for writing such a needed book especially from practitioner''s
    perspective.

    Few questions I have:

    1) Do you think graph data and graph algorithm will dominate and becomes more
    popular? Are not they complex and have a high learning curve?'
  replies:
  - name: Denise Gosnell
    text: 'Dr Abdulrahman great questions, thank you!

      I am seeing that utilizing the connectedness of data is a valuable trend that
      will become a regular part of the ML and data science workflow for feature detection.

      However, you are correct. There is still a steep learning curve wrt to using
      graph technologies like algorithms, query languages, and databases.'
- name: Dr Abdulrahman
  text: 2) What is the hidden technical dept that organizations might face adopting
    graph data/algorithms? Technical issues, skill shortage, difficult to scale, hungry
    for computation power..etc
  replies:
  - name: Denise Gosnell
    text: 'Dr Abdulrahman The largest hurdles to overcome, today, are:

      &gt; 1. data ETL into a graph shape

      &gt; 2. graph query languages

      I have found that each #1 and #2 have a root in skills shortages, which is why
      I wrote this book. I poured my heart and brain onto the pages to hopefully help
      out the community to feel better prepared to address them. :heart:

      I am not finding that "computation power" is an issue because getting bigger
      machines seems to be somewhat easy compared to the other aspects of the problem.

      The VC circles are currently investing in both sides of that adoption issue.
      Thus, I hope to see significant improvement in those areas in the next 5 years.'
- name: Dr Abdulrahman
  text: 3) If I understand correctly, forr graph algorithms to work, I must have all
    the graph at once to see the whole relation? It can not be used on batched mode.
    Am I Right? Otherwise, relations might not appear.
  replies:
  - name: Shankar Somayajula
    text: 'One can load/build up the graph incrementally in a batched fashion.

      Rather than think of the graph in terms of complete/incremental/batch sense,
      one can analyze the graph in its full/complete form or in a custom/scaled down/localized
      form as applicable to the analysis.

      You can issue some commands on the graph and reduce it as you please (reduce
      in terms of edges and/or vertices) ... The resulting graph becomes a sub-graph.
      Graph Algorithms can be issued on the sub-graph. Think of this as a custom/localized
      application of the Graph Algorithm.

      Global and Local versions of the same algorithm can co-exist and lead to novel
      usages of graph.

      E.g: Find the go-between in terms of complete Graph and see who the intermediaries
      are at a global level using "Betweenness" algorithm/resultant KPI ranking. Now
      subset the graph to a region and/or only keep certain types of transactions
      and then apply the same algo ... see new intermediaries ranked in terms of their
      "Betweenness" role in the custom scenario. Some of these local intermediaries
      may not have a big enough footprint to be visible/noticeable on the global scale
      but still be important from a fraud or compliance perspective when viewed locally.

      HTH'
  - name: Denise Gosnell
    text: 'exactly what Shankar Somayajula said, thanks!

      I have nothing to add :partying_face:'
  - name: Dr Abdulrahman
    text: Thank you Shankar Somayajula. and Denise Gosnell
  - name: Vladimir Finkelshtein
    text: As was mentioned somewhere, you can work with adjacency matrix instead of
      a graph, they have the same information. And many graph operations like counting
      paths and examining neighborhoods are then done by matrix multiplication. And
      there is no problem to do parallel/batched computation with big matrices, by
      splitting it into blocks. This is the formal version of what Shankar Somayajula
      said, I think.
- name: Alexey Grigorev
  text: "Good morning/day everyone!\nAs Denise mentioned yesterday, she'll still be\
    \ taking questions today, so we'll announce the winners of her book tomorrow.\
    \ \nHave a great day!"
  replies:
  - name: Mansi Parikh
    text: thanks, Alexey, for asking all of those questions today as they surely helped
      beginners like me!
- name: Alexey Grigorev
  text: 'I think we still have some time for more questions.

    So, why do you think graph databases are not getting a wide-spread adoption? There
    are many use cases that they can solve, but people tend to go with traditional
    relational DBs.

    (Or maybe I''m wrong and they are getting a lot of adoption, but I just don''t
    see it?)'
  replies:
  - name: Denise Gosnell
    text: 'Alexey Grigorev great question!

      I think the adoption of graphs is blocked by the mental model which is ingrained
      in our heads:

      &gt; data maps to a table.

      We think and perceive the world in a network. I am friends with Casey. Casey''s
      family lives in Chicago. Chicago is my mom''s hometown... etc.

      We perceive our world in relationships and our thoughts flow through them, similarily.

      But, the earliest adoption of relational technologies enforced a mental shape
      of data which we are having a hard time navigating away from today: data goes
      in a table.

      OH! Bonus fact -- the CODASYL group in the 1960s was the first formal group
      to organize database technology. They started with hierarchies first (or graphs)
      - but we didn''t have the computational power to make them easy. So, they died
      and went for relational instead (enter Codd''s work in the 1970s!)'
  - name: Jessie Yaros
    text: WOAH that is sooo interesting. And a sure testament to how --at least at
      first-- there was an attempt at organizing data more like we mentally do it.
      And how it can be hard to now rewire both at the individual and institutional
      level!
  - name: Jessie Yaros
    text: So its kind of like how neural nets came back when we actally had the processing
      power to support them?! Bodes well for graphs....
- name: Alexey Grigorev
  text: What are the most useful/practical graph algorithm that data scientists should
    know about?
  replies:
  - name: Denise Gosnell
    text: "Alexey Grigorev honestly? bi-directional search for shortest path algorithms.\n\
      That one isn't solved well (yet) in OSS graph algorithm libraries, and is known\
      \ to be the fastest way we can do path finding.\nThen, #2 is connected componenets.\n\
      I make these two recommendations, bi-directional search for pathfinding and\
      \ connected components, because when they are used together that is the fastest\
      \ way you can answer the question:\n&gt; \"How is a connected to b\"?\nWhich\
      \ is the main thing people want to use graphs to answer.\nThe pseudo code works\
      \ like this:\nQ: Is `a` connected to `b`?\nPseudo Code:\n&gt; 1. Run Connected\
      \ Components on the graph: this assigns a label to a vertex. All vertices that\
      \ are connected together by any edge get the same label. Two vertices have different\
      \ labels if there is no possible path between them.\n&gt; \n&gt; 2. Is the label\
      \ of `a` the same as `b`? If no -- return \"not possible\". If yes, run bidirectional\
      \ search\n&gt; \n&gt; 3. Bi-directional search: starting at `a` run one iteration\
      \ of breadth-first-search. Store the results in a set: `a_neighbors`. Then,\
      \ go to `b` and run one iteration of breadth-first-search. Store the results\
      \ in a set: `b_neighbors` . Run the intersection of `a_neighbors`  and `b_neighbors`\
      \ . If the intersection is empty, go back to `a` and continue down BFS, and\
      \ compare to the next iteration of BFS to `b` . Continue until you find a common\
      \ vertex in the intersection of `a_neighbors`  and `b_neighbors` \n&gt;"
  - name: Denise Gosnell
    text: 'I would love to see this implemented in any OSS library!

      I hope that description helps!'
- name: Alexey Grigorev
  text: maybe the last one - what are the most popular graph databases and which are
    the most typical use cases for each?
  replies:
  - name: Denise Gosnell
    text: "Alexey Grigorev since I work for a graph database vendor, folks might not\
      \ trust my opinion. \U0001F642\nThere are many things to consider when looking\
      \ at graph databases - I would recommend starting with [this excellent article\
      \ in TDS](https://towardsdatascience.com/comparing-graph-databases-5475bdb2e65f)on\
      \ the topic :)"
- name: Denise Gosnell
  text: "Thank you all very much for letting me join this world and talk about graphs\
    \ this week. The pleasure is all mine as I thoroughly love and enjoy this topic.\
    \  Feel free to ping me in here anytime, or drop me an email: <mailto:denisekgosnell@gmail.com|denisekgosnell@gmail.com>\n\
    Let's stay connected! \U0001F61C"
  replies:
  - name: Shankar Somayajula
    text: Denise Gosnell You've been very sporting and generous with your knowledge
      in answering all the questions. Cheers, Great Advocacy :-)
  - name: Alexey Grigorev
    text: Thank you for answering our questions - and also for one extra day of your
      time!

---

Graph data closes the gap between the way humans and computers view the world. While computers
rely on static rows and columns of data, people navigate and reason about life through relationships.
This practical guide demonstrates how graph data brings these two approaches together.
By working with concepts from graph theory, database schema, distributed systems, and data analysis,
you’ll arrive at a unique intersection known as graph thinking.