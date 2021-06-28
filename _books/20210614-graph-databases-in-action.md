---
title: "Graph Databases in Action"
description: "Book of the Week. Graph Databases in Action by Dave Bechberger"
cover: "images/books/20210614-graph-databases-in-action/cover.jpg"
image: "images/books/20210614-graph-databases-in-action/preview.jpg"
start: 2021-06-14 00:00:00
end: 2021-06-18 22:59:58
authors: [davebechberger, Josh Perryman]
links: 
  - text: Book's page
    link: https://www.manning.com/books/graph-databases-in-action
  - text: Amazon
    link: https://www.amazon.com/Graph-Databases-Action-Dave-Bechberger/dp/1617296376

archive:
- name: Kshitiz
  text: 'Hi bechbd and Josh Perryman - I am assuming that you guys would have covered
    the application of Graph databases in the book. I have a few questions about it.

    Note - This is coming from someone who has little to no idea about the Graph databases.

    1. Do you see any potential in the processes where Graph databases can replace
    the existing databases?

    2. What areas do you think Graph databases can be useful, which have not yet adopted
    it?'
  replies:
  - name: Josh Perryman
    text: 'I''ll start with state graph dbs have distinct advantages over other dbs
      in two ways: 1) developer productivity and 2) technical performance.

      On developer productivity - graph databases, and the query languages used for
      them (Cypher, Apache TinkerPop''s Gremlin, etc...) make relationships first
      order citizens. This gives developers tools to reason over the relationships
      directly. In other query languages these constructs either don''t exist or are
      late additions. Developers with better language tools have better mental models,
      are able to express those models more clearly, which allows them to code faster,
      make fewer mistakes, and come up to speed on other''s code more quickly. Since
      developer time tends to be the most expensive, any gains here usually have a
      dramatic impact on the bottom line.

      On technical performance, for certain types of queries, especially "multi-hop
      + variable numbers of hops" graph databases can have a dramatically better performance
      over other databases. In some cases, I have take queries in SQL, translated
      them to a graph and seen a performance increase up to 100 times faster.  This
      is use-case specific. But there are a whole category of types of queries for
      which graph dbs excel. This includes recommendation engines and dependency analysis.'
  - name: Josh Perryman
    text: "On 2, the more common problem is people choosing a graph db, then looking\
      \ for use cases and choosing poorly. \U0001F600"
  - name: Kshitiz
    text: Thanks Josh Perryman for the detailed reply here. This is pretty good explanation
      for anyone who is new to graph dbs. I have a follow up question though - Which
      use cases are good to go for graph dbs?
  - name: bechbd
    text: 'So determining a good graph use case really comes down to knowing the answers
      to two questions:

      - Does my domain lend itself to using connected data?

      - Are the questions I''m asking leveraging those connections to provide the
      answer?

      If the answer to both are Yes then you have a candidate use case for graph data.  Since
      graphs are all about utilizing the connections within data.  In general good
      graph use cases do one or more of the following:

      - Navigate (variable) connected data structures

      - Filter or computer the result on the basis of the strength, weight, or quality
      of the relationships in the data

      - Require traversing an unknown number of connections

      Since graphs/graph databases work fundamentally different than something like
      a RDBMS when it comes to connections in data they tend to perform better when
      traversing these connections is a crucial part of the application.  Some examples
      of some good graph questions are:

      - What does this person want to buy?

      - How are these two people/entities connected?

      - Why did X impact Y?

      These sorts of questions are common across so many domains such as recommendation
      engines, fraud, advertising, life sciences, e-commerce, identity graphs, knowledge
      graphs, etc.'
  - name: Kshitiz
    text: bechbd - Thanks for answering this question. Definitely helps in getting
      a better understanding.
- name: Josh Perryman
  text: "Thanks Alexey! I have timezone advantage over Dave, so I'll try to grab the\
    \ easier questions \U0001F601"
  replies: []
- name: Matthew Emerick
  text: Hey, bechbd and Josh Perryman!  Thanks a lot for doing this.
  replies: []
- name: Matthew Emerick
  text: Would you recommend learning graph databases or relational databases first
    in today's world?
  replies:
  - name: Josh Perryman
    text: "I \U0001F60D this question. I strongly recommend understanding relational\
      \ databases first, and I think that Dave will agree with me on this.\nWe are\
      \ big fans of relational databases. They have been around for decades. Every\
      \ popular one out there is a very mature technology. The performance is astounding\
      \ for most data use cases. The ecosystems (tools, docs) are expansive. Though\
      \ ORMs tend to be mature and very helpful, it still helps to understand the\
      \ data and be able interrogate it directly.\nIn nearly any job a developer will\
      \ start in, there is almost certainly going to be a relational database. If\
      \ you have to have a persistence engine (aka a db of any sort) you are almost\
      \ certainly best off starting with a relational db _because you can find/hire\
      \ developers with experience_*.*"
  - name: Josh Perryman
    text: In our book, we actually assume that the reader has experience with relational
      databases. Several examples in the start begin with a representation in a relational
      schema with example SQL, before "translating" it to a graph representation.  We
      presume that SQL is the _lingua franca_ of the data world, and in our experience
      that's pretty much been the case.
  - name: bechbd
    text: Most of the world runs on relational databases so I agree with Josh that
      learning relational databases first would be what I would also recommend.  I
      also suggest you then learn the other types of databases (Document/Key-Value/Column
      Oriented/Graph) and look at the strengths and weaknesses of each.  These databases
      each perform some types of tasks better than others which is why they were created.  Understanding
      these tradeoffs is really a key piece of information to have when trying to
      decide the best technology to use
- name: Matthew Emerick
  text: How important are graph algorithms in learning graph databases?
  replies:
  - name: Josh Perryman
    text: "I see them as two separate concerns. One can do a lot of data engineering\
      \ and architecture with graph databases with little to no need for understanding\
      \ graph algorithms. In most cases, developers will use functions already in\
      \ place rather than code the algorithms for themselves.\nThere are places where\
      \ it is nice to know the relative benefits of one approach or algorithm over\
      \ another, but this usually only comes with performance tuning, and only in\
      \ the most exceptional of tuning use cases. I've worked with dozens of companies\
      \ on graph db designs and builds, and just about the only time that talk of\
      \ algorithms would come up would be over \U0001F37B after a day of writing code\
      \ and making things work."
- name: Matthew Emerick
  text: How useful are graph databases in graph-based machine learning?
  replies:
  - name: Josh Perryman
    text: bechbd this one is all you
  - name: bechbd
    text: 'From what I have seen graphs and machine learning tend to work together
      in three ways.:

      - Graph algorithms - Graph algorithms, specifically ones around cluster/centrality/label
      propagation/random walks tend to provide some novel insights into data that
      are not easily achieved using other mechanisms.  I have frequently seen where
      the output from these sorts of algorithms are used as one of the features input
      into ML models.

      - Embeddings - Graph embeddings are like other embeddings in as much as you
      are looking to take a high dimensionality space and represent as a low dimensionality
      vector which maintaining the similarity differences.  In graphs these tend to
      either be node embeddings where the node and its neighborhood/connections are
      represented or whole graph embeddings.

      - Graph ML - Graph based machine learning is a hot topic in AI as some of the
      newer algorithms such as Graph Neural Networks allow you to take graphs as input
      to produce highly effective predictive models, especially when the domain/question
      are benefitted from the rich connections in the data.

      I actually gave a talk on this last week which should be available on YouTube
      tomorrow [https://www.youtube.com/watch?v=SLKW5Q_URq4](https://www.youtube.com/watch?v=SLKW5Q_URq4)'
  - name: Lalit Pagaria
    text: Thanks for answering it Dave. Really informative.
- name: Julian Stevens
  text: Can a graph database be implemented alongside my current relational database,
    i.e., can I create a pipeline between my relational database and a graph database?
  replies:
  - name: bechbd
    text: 'This is a very common pattern.  Graph databases make a great compliment
      to relational technologies when the questions being asked leverage the weight,
      quality, or quantity of connections between entities.  I sort of think about
      it as RDBMS systems are great at handling the "What" questions in an application
      and graph databases are great at handling the "Where/Why/How" questions.  As
      a colleague once put it to me "RDBMS will tell you how much it costs to buy
      everyone in the room a beer, graph databases tell you why they chose the beer
      they are drinking".

      As far as the best way to setup the pipeline between the two that really depends
      on the tools that the specific vendor has in place.  I would say that in most
      cases I have seen the RDBMS system tends to be the system of record for data
      (either because its a better fit for many questions or because it was there
      first) and any data/mutations are sent via either a CDC type mechanisms or by
      reading from something like a Kafka topic to the graph databases.'
- name: David Cox
  text: Very interesting book! Admittedly, I have never really dove into graph databases.
    What are the advantages of graph databases for data scientists?
  replies:
  - name: bechbd
    text: 'I think the advantages for graphs for a data scientist really depend on
      the domain that they are working in.  Graphs (and by extension graph databases)
      really allow full expressivity of data in domains (e.g. social networks, fraud,
      supply chain, identity resolution, supply chain optimization, etc.) where the
      connections between entities are as (or more) important than the entities themselves.

      From a data science perspective these sorts of domains often require looking
      at interdependencies between entities, inferring meaning using connections,
      and then using these to try and predict behaviors.  Because graphs treat these
      connections as first class citizens in the data they enable data scientists
      to perform these sorts of tasks faster/easier than before as well as enabling
      some new techniques/algorithms (e.g. centrality/clustering) that are not really
      capable of being performed on other database types.'
  - name: David Cox
    text: This is very helpful!! Thanks!!
- name: Jessie Yaros
  text: Thanks for being here bechbd and Josh Perryman ! I've been getting really
    into graph theory lately, so I love anything about graph databases! I'm wondering
    if you guys have any preferences in specific graph databases. Do the options out
    there tend to excel in specific areas that can guide people on how to choose one
    for specific use cases? I've only dabbled with neo4j, because that was the first
    one I was aware of. But now I know how many options are out there and its overwhelming.
  replies:
  - name: bechbd
    text: "I currently work on the Amazon Neptune team so I am going to steer away\
      \ from recommending specific databases but I can provide a high level overview\
      \ on the process I use to evaluate a graph database.\nThe first thing to think\
      \ about is if your use case is a good graph use case.  I addressed some of the\
      \ specifics here in the earlier comments so I'll skip over the details for now.\n\
      The next thing I usually think about is if this needs to be a one time or batch\
      \ type use case or if I need to run the use case many times.  If you are only\
      \ doing this one time or its a batch type process you probably need to take\
      \ a look at if a graph database is even needed or if you can use something like\
      \ GraphX/NetworkX to achieve your needs.\nIf you decide that a graph database\
      \ is appropriate for your issue then you will want to next decide if you have\
      \ an RDF or a Property Graph problem.  RDF databases are based on triple patterns\
      \ (subject/object/predicate) and use IRIs to uniquely identify entities in the\
      \ graph.  They are queried by SPARQL (almost exclusively) and are really great\
      \ at solving issues such as MDM and knowledge graph use cases and are very popular\
      \ in certain industries such as life sciences/finance.  Property graphs consist\
      \ of nodes/edges/properties and excel at pattern matching and path finding type\
      \ problems.\nOnce you have decided on what type of database you are looking\
      \ at you then need to decide take a look at a variety of factors:\n- OSS vs\
      \ Commercial - There are advantages/disadvantages on both sides of the fence\
      \ here but understanding the true cost , skillset, and availability constraints\
      \ of the team is important to keep in mind \n- Hosted vs On-Premise \n- Managed\
      \ vs. Self managed\n- Data size\n- HA/Scalability\n- etc."
  - name: Jessie Yaros
    text: Thank you for this! A lot to think about.
- name: Jessie Yaros
  text: I also asked Denise Gosnell when she was here, and would love your takes as
    well - what would the top languages and or tech tools/ frameworks you recommend
    to become proficient and flexible across uses of graph databases? (I know there
    seems to be different graph query languages across many databases... so i wonder
    how transferrable these separate languages are...)
  replies:
  - name: bechbd
    text: 'Denise is just awesome.

      I mean as far as top languages for development the ones I run across most frequently
      are Java/Python.  As far as query languages/tools, unless you are doing RDF
      the tooling and languages tend to be very specific to a database.  While there
      are a few open source query languages in the property graph world (TinkerPop
      Gremlin and openCypher) each database tends to implement their own sub or super
      sets of these languages (e.g. Neo4j Cypher != openCypher) so its hard to say
      which one to learn.  Generally I think the bigger concept to stride for is to
      make the shift from thinking about data as tables/columns and start to view
      it as a network/mind map.  This is transferable across any of the different
      tools and is much more impactful than learning X or Y framework.'
  - name: Jessie Yaros
    text: bechbd In my PhD work i use graph theory a fair bit, so I've gotten uses
      to thinking in terms of networks! But as you mentioned in the prior comment,
      my specific use cases have all allowed for the batch approach! So I've mostly
      used networkx and other python/matlab packages for network analysis, though
      I'm very interested in the database approach for the future.  I've found there
      are a lot more advanced algorithms and implementations available in python/R
      packages/ github repos than I've seen in say, Neo4j's graph data science library.
      Are there recommended ways of taking portions of networks from graph dbs and
      porting them into python for use with such packages? Are some dbs perhaps more
      compatible for this? I realize you may not be able to answer latter question
      because of Neptune affiliation, but thought I'd see!
  - name: bechbd
    text: Yeah I have no specific knowledge of why Neo has chosen the algorithms that
      they have chosen but I suspect that its a combination of the computational complexity
      of running them at large scale and the frequency of use.  Something like a graph
      coloring algorithm is rather computationally complex (O(c^n) or something like
      that) and is rarely used so putting it into a database would be prohibitively
      complex for little return on value.  To get subgraphs into something like Network
      X is usually relatively easy in either cypher/openCypher or Gremlin by casting
      the results to a list of maps and then returning those.
  - name: Jessie Yaros
    text: Thank you!
- name: Jessie Yaros
  text: And piggybacking on that, do you think GQL will ever become a thing that helps
    harmonize use across graph db choice? Or is it more pipedream?
  replies:
  - name: bechbd
    text: My hope is that GQL becomes a real standard but the adoption of it is yet
      to be seen.  Adoption will depend on vendor support as well as what flexibility
      it provides for vendor specific extensions (i.e. SQL).  I think the reality
      is that we are multiple years (5ish hopefully) away from this truly becoming
      a settled standard with wide ranging support
  - name: Josh Perryman
    text: 'I''m part of a "Property Graph Schema Working Group" which is focused on
      schema part of this question. The group is composed of representatives from
      academia and industry, including prominent graph database vendors and folks
      like me: users of the technology.

      From my experiences there seems to be a near-universal desire for standardization.
      This is understood as necessary step in growing the use of the technology. We
      are moving in the direction of having more generally accepted standards, but
      the timeline is best thought of in years like Dave indicates.'
- name: Toxicafunk
  text: I've noticed data governance tools like Amundsen or Apache Atlas both have
    GraphDBs as their backend storage system but I've haven't been able to find any
    deep dive into how our why GraphDBs are useful or desirable for governance. Yes,
    I kind of get why intuitively, but do you have any insight/specifics on the subject
    or some useful links?
  replies:
  - name: bechbd
    text: I think this is mainly due to the flexibility that graphs provide in terms
      of schema evolution and queryability(if thats even a word).  The implicit schema
      of graphs lends itself to easy ingest of data with differing properties or differing
      data types for properties in ways that something like a RDBMS would not.  The
      ability to query and trace paths, especially of unknown depth, through data
      to find its origins is also not something easily achieved in Document or RDBMS
      databases.
- name: Tino
  text: "Hey all! How important would you think is graph db knowledge for data scientist?\
    \ I know that a lot of company let rather their data engineers or others do this\
    \ work \U0001F642"
  replies:
  - name: bechbd
    text: I think understanding the fundamentals of graphs and graph databases is
      important for data scientist to understand how their work fits into the larger
      picture of productizing the models/work they have done.   Additionally, depending
      on the graph/graphdb/data being worked on it may be easier to retrieve/load
      data for the projects you are working on from a graph database versus many CSV/Parquet
      files
- name: Ken Lee
  text: Totally new to Graph DB although have been hearing its name for quite some
    time. I am a machine learning engineer and just wondering what are the use cases
    of Graphs in machine learning context? TQ
  replies:
  - name: bechbd
    text: 'No problem, I actually put some answers to a similar questions [here](https://datatalks-club.slack.com/archives/C01H403LKG8/p1623683981273700?thread_ts=1623675871.268200&amp;cid=C01H403LKG8)'
  - name: bechbd
    text: Additionally I gave a talk last week on this subject which you can view
      [here](https://www.youtube.com/watch?v=SLKW5Q_URq4)
  - name: Ken Lee
    text: thanks and appreciate!
- name: Ajay kumar saini
  text: "Thanks for being here bechbd and Josh Perryman , I\u2019ve productionized\
    \ multiple graph database (Agensgraph, Dgraph). One problem I faced in both graphs\
    \ is the performance of graph traversal queries(connected component size, degree\
    \ etc.) in highly connected data with large component size. How is it handled\
    \ in other graph databases? Is the performance of these query  degraded in other\
    \ graph DBs as well given graph has to iterate lots of nodes?"
  replies:
  - name: bechbd
    text: 'Well I guess there are two parts to this question, the performance of graph
      traversals on large data sizes and the performance of graph algorithms on large
      data sizes.

      In general the performance of any graph traversal is directly related to the
      number of vertices and edges that it must touch.  The earlier you can add the
      most selective filters in a query the better off the performance will almost
      always be.  However this does still mean that starting at point a may take X
      ms while starting at point B may take 2X ms if you have to touch twice as many
      elements in the graph to get the answer.  Many people don''t expect this but
      it is a very common quality across graph databases.  The same is true with non-graph
      databases but the nature of traversing connected data and the corresponding
      branching factor at each level seems to amplify this in graph databases.

      As for the time to run graph algorithms on large datasets, this tends to boil
      down to just the nature  of the computational complexity of the algorithms themselves.  Even
      the simplest one you mentioned there, degree,  requires touching each vertex
      once and each edge twice.  Something like connected components is O(V+E) complexity.  In
      my experience many people don''t understand the complexity of the algorithms
      and therefore have expectations that no database can meet when it comes to scale
      and latency of those types of operations.  Generally we see people end up with
      a sort of almost lambda type architecture where they use a batch process to
      calculate these sorts of statistics/attributes and then save them back into
      a node/vertex as a property.  These properties are then used to serve some sort
      of real time/transactional use cases'
- name: Tim Becker
  text: "Hello \U0001F642 Thanks for doing this. In the introduction of your book\
    \ you mention that graph databases are good for complex data. Do you have any\
    \ way of quantifying how complex the data is and which database type to choose\
    \ based on the complexity?"
  replies:
  - name: Josh Perryman
    text: 'TL;DR: no, I don''t think there''s a way to quantify complexity based just
      on the data in and of itself.

      But I think it is less about the data and more about the questions.

      In my present work, and this has held for much of my past years of experience,
      we chose the data engine based on the question we are asking of the data at
      different parts of the application. Where we need full descriptions of the objects,
      we use a relational database. Where we need to work with the relationships between
      things we use a graph. Where the need is for performance and the data involved
      in light and slowly changing, we use a cache. Where we''re asking questions
      of large swaths of the data, some analytics database.

      We get into this in the first chapter where we survey _*types*_ of questions
      and I think it hold here as well. We need to understand the types of questions
      that are important for users of the data.'
- name: Tim Becker
  text: How much knowledge concerning traditional databases do you need to get the
    most of your book?
  replies:
  - name: Josh Perryman
    text: 'I think very little is needed, if the intent is to start building software
      using graph databases.

      The main expectation we have is a basic capability in writing software. Most
      of the book will be opaque to those who don''t have some familiarity with writing
      and operating simple software programs.

      On the data side, we use relational databases, with some SQL, as a connecting
      point to common developer experience. But this knowledge isn''t essential. If
      someone has complete an introduction to software development course in a popular
      language (Java, C#, Python, JavaScript) and has completed one or more non-trivial
      projects, projects where there''s more than one "section" or "class" or "module"
      or "function" in the code, then they should be able to follow along reasonably
      well.

      Our target is developers with some level of professional experience, even if
      they aren''t a full-time software developer. If you have at least 3 months writing
      code mostly full time in a professional setting, then the book is ideal to quickly
      expose you to the techniques of working with connected data.'
- name: Tim Becker
  text: Do you have any recommendation on how to get started with db in general? Something
    that would be good to read before starting with your book.
  replies:
  - name: Josh Perryman
    text: "SQL, and relational databases, are the language and tools of the data world.\n\
      I think it good to be familiar with how relational databases function and there's\
      \ so much material for this that I hardly know where to start. I recommend looking\
      \ around your world and note the following:\n- *What databases are in use around\
      \ me?* Common ones are MySQL, Oracle, Microsoft SQL Server and PostgreSQL. These\
      \ are the top 4 on [db-engines.com](http://db-engines.com) and have been there\
      \ for many, many years.\n- *What programming languages are in use around me?*\
      \ Common ones are Java, C# (.NET), Python and JavaScript. I rather like Python\
      \ for someone just learning, or JavaScript for those who think they are interested\
      \ in web development. But any of these four are broadly supported with vast\
      \ communities.\n- *What tools / frameworks are in use around me?* The use of\
      \ an \"Object-Relational Mapper\", or ORM, is most common. Every major language\
      \ has one or more. \nBased on that I'd like for a tutorial that covers the database\
      \ engine of choice, and uses the programming language of choice. Usually the\
      \ framework or ORM tool will have a good tutorial as well. These types of learning\
      \ aids can either be bound books, or online courses. Choose that based on your\
      \ preferred learning style.\nI think that the trick here isn't to pick \"the\
      \ right one\" but to pick the technical stack (engine + language + tools) which\
      \ is common in your part of the world. This will give the best opportunity for\
      \ applying your new skills quickly."
- name: Tim Becker
  text: How useful is a good understanding of graph theory to follow your book or
    is the brief introduction in chapter 1 sufficient?
  replies:
  - name: Josh Perryman
    text: I feel that Graph Theory is of minimal use in the actual day to day work
      of using graph databases. Graph Theory provided the primitives (vertices, edges)
      but working with connected data is more about understanding how to work with
      data than a mathematical theory. In my mind they are wholly separate from one
      another for practical work.
- name: Tim Becker
  text: "btw, I read through chapter one to get an understanding of what the books\
    \ is about and I already learnt a lot, so \U0001F44D"
  replies:
  - name: Josh Perryman
    text: Tim, thank you for reading and joining us on this journey!
  - name: Tim Becker
    text: Josh Perryman Thank you for answering all my question, I appreciate it!
- name: Amruta
  text: Does anyone know any good books on Graph Theory (especially for beginners)?
  replies:
  - name: Marcello La Rocca
    text: "Hi Amruta!\n-  you can certainly find the basics in \"Introduction to Algorithms\"\
      \ [https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844)\
      \ Which however covers much more than graphs, and from an algorithmic perspective.\n\
      - If you are more interested in a mathematical angle, I recommend Trudeau's\
      \ \"Introduction to Graph Theory\", a classic: [https://www.amazon.com/Introduction-Graph-Theory-Dover-Mathematics/dp/0486678709](https://www.amazon.com/Introduction-Graph-Theory-Dover-Mathematics/dp/0486678709)\n\
      - About graph visualization, I liked this one: [https://www.amazon.com/Graph-Drawing-Algorithms-Visualization-published/dp/B00Y2UUWDO](https://www.amazon.com/Graph-Drawing-Algorithms-Visualization-published/dp/B00Y2UUWDO)\n\
      - I have another good one in my bookshelf, but I can't remember the title \U0001F926\
      \ I'll try to find it, but meanwhile here there is also a good source for more\
      \ resources, if you are (or will be) interested in more advanced books [https://neo4j.com/blog/top-13-resources-graph-theory-algorithms/](https://neo4j.com/blog/top-13-resources-graph-theory-algorithms/)"
  - name: Amruta
    text: Thankyou so much Marcello La Rocca! Very helpful...Especially the second
      suggestion! :)
  - name: Marcello La Rocca
    text: "You are welcome! Glad it helped \U0001F642"
- name: Shankar Somayajula
  text: 'Hi, Thanks for the opportunity bechbd and Josh Perryman to ask questions.
    Are there any simple/beginner tutorials in using graphs for Inference? Use graph
    (properties and processing) to tease out causal linkages between products or data
    elements?

    Also can one relate this to sub-graph/directionality of the edges of the graph
    ...

    { (customers with attributes) a, b }  (buys) c =&gt; (buys) p ... or (strong signal
    for c =&gt; p)

    but not vice versa...

    i.e. { (customers with attributes) a, b } (buys) p NOT =&gt; (buys) c .... or
    (weak signal for p =&gt; c)'
  replies:
  - name: bechbd
    text: 'I do not know of any tutorials specifically around this but I bet if you
      looked for RDF graphs and OWL you will probably find some.

      How this relates to the sub-graph/directionality is really a domain specific
      concept.  Property graphs generally let you traverse edges in both directions
      but that may or may not make sense depending on the domain.  For example in
      something like a social network you might have two people connected by a friends/follows
      edge.  If the network is like facebook, the relationship is reciprocal and traversing
      the edge in both direction makes sense (i.e. Person A and Person B are friends).  In
      the network is like Twitter, Person A might follow Person B but that does not
      mean Person B follows Person A'
---

Relationships in data often look far more like a web than an orderly set of rows and columns.
Graph databases shine when it comes to revealing valuable insights within complex, interconnected
data such as demographics, financial records, or computer networks.

In Graph Databases in Action, experts Dave Bechberger and Josh Perryman illuminate the design and
implementation of graph databases in real-world applications. You'll learn how to choose the right
database solutions for your tasks, and how to use your new knowledge to build agile, flexible,
and high-performing graph-powered applications!