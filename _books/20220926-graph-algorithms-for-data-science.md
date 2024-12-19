---
authors:
- tomazbratanic
cover: images/books/20220926-graph-algorithms-for-data-science/cover.jpg
description: Book of the Week. Graph Algorithms for Data Science by Tomaz Bratanic
end: 2022-09-30 23:59:59
image: images/books/20220926-graph-algorithms-for-data-science/preview.jpg
links:
- link: https://www.manning.com/books/graph-algorithms-for-data-science?utm_source=twitter&utm_medium=organic&utm_campaign=book_bratanic_graph_11_22_21
  text: Book's page
start: 2022-09-26 00:00:00
title: Graph Algorithms for Data Science
archive:
- name: Luis
  text: I am really looking forward to read this book. Looks super interesting. Does
    it come with small projects?
  replies:
  - name: Tomaz Bratanic
    text: Every chapter apart from the first 2 is a tutorial based project of its
      own
- name: Evren Unal
  text: 'Hi Tomaz Bratanic,

    I heard gnn here and there becoming more popular day to day.

    Does it eventually take place of other deep learning algorithms like cnn and rnn?
    or gnn is to use togeather with other algorithms?'
  replies:
  - name: Tomaz Bratanic
    text: GNN is simply a CNN fitted to any type of graphs... if CNN can be used on
      an image, which is a grid graph with predefined structure, that GNN is a variation
      of CNN that can be used on any graph structure
  - name: Tomaz Bratanic
    text: other algorithms can be used to define features of nodes to be used in GNNs
  - name: Evren Unal
    text: 'As i understand gnn does not replace other algorithms.

      I thing to better understand gnn one should see some examles.'
- name: Ali Shakiba
  text: 'Hi Tomaz Bratanic

    Thanks for introducing the book.

    Many graphs, such as the ones like Web connections or Twitter follower/following
    graphs are very big, although they are sparse. Are Big graphs also covered in
    your book, too? As far as I know, many problems in graph theory are NP-hard and
    many of the polynomial-time algorithms are not useful for big graphs, even assuming
    that something like Floyd-Warshall algorithm running on the graph corresponding
    to the map of the World with all cities with O(n^3) running time is frightening.'
  replies:
  - name: Tomaz Bratanic
    text: I don't deal with very large graphs in my book. For graphs even O(n^2) doesn't
      scale well. Some algorithms have approximate variations. There are also other
      algorithms that scale pretty well like PageRank, or Label Propagation etc...
      In my book, I don't deal with pathfinding at all
- name: Ashish Lalchandani
  text: Hi  Tomaz Bratanic, thanks for being here! My question is, what are the applications
    of graph algorithms in ML? I mean, what kind of problems in ML can be solved using
    graph algorithms? Also, are the graph algorithms used in ML are same as the conventional
    graph algorithms we use in competitive programming/leetcode?
  replies:
  - name: Tomaz Bratanic
    text: More classical graph algorithms have been used to find the most important
      nodes or find groups of nodes... Lately, there has been a shift into extracting
      features from graphs and using them as inputs to ML models. I have no idea what
      kind of graph algorithms are using in competitive landscape. Probably PageRank
      is the most used algorithm out there
  - name: Ashish Lalchandani
    text: What kind of features are you referring to? Also, for graph algorithms in
      competitive programming,  i was referring to BFD, DFS, backtracking, minimum
      spanning tree, etc.
  - name: Tomaz Bratanic
    text: BFS and DFS are basis of some algorithms... I am talking more about unsupervised
      graph algorithms like pagerank, label propagation, node2vec etc
  - name: Tomaz Bratanic
    text: There are a couple of features that you can extract based on the position
      of the node in the network... how important it is, how well connected, how does
      it group by, who are their neighbors etc...
  - name: Ashish Lalchandani
    text: Oh i see, that makes sense now, thanks for explaining! Much appreciated!
- name: Bengsoon
  text: "Hi Tomaz Bratanic thanks for writing this book. I am very new to this sub-space\
    \ of AI ML. \nFrom my very shallow knowledge, graph theory as well as graph database\
    \ have been around for a while, but I noticed that graph based ML etc has only\
    \ risen to fame in the last few years. Is my observation right? If so, why is\
    \ that?\nAlso, what are the practical strengths of graph based ML as well as the\
    \ limitations, especially in production/deployment settings (compared to the conventional/mainstream\
    \ ML algorithms like NN etc) ?"
  replies:
  - name: Tomaz Bratanic
    text: 'Graph ML has risen to fame only in the last years, because most of the
      graph ML algorithms have been developed in only the last couple of years, most
      noticeably embedding and GNN models.

      If relationships are predictable, then graph models can take those relationships
      and use them as features in predictions whereas it is hard to encode those relationships
      in traditional models'
  - name: Tomaz Bratanic
    text: 'take a look at pinterest for example: [https://medium.com/pinterest-engineering/pinsage-a-new-graph-convolutional-neural-network-for-web-scale-recommender-systems-88795a107f48](https://medium.com/pinterest-engineering/pinsage-a-new-graph-convolutional-neural-network-for-web-scale-recommender-systems-88795a107f48)'
- name: Tomaz Bratanic
  text: 'btw... I have tons of free articles on medium if you want to take a look
    at free content before deciding about the book: [https://bratanic-tomaz.medium.com/](https://bratanic-tomaz.medium.com/)'
  replies: []
- name: Tomaz Bratanic
  text: Ashish Lalchandani GerryK Luis You have been selected as the winners of the
    free copy of the book. Please DM me and I will give you instruction to obtain
    a free copy of the book
  replies:
  - name: Alexey Grigorev
    text: Thanks for joining us this week!
  - name: Tomaz Bratanic
    text: My pleasure
  - name: Ashish Lalchandani
    text: "Thank you Tomaz Bratanic!! Thanks for answering our questions \U0001F600\
      \ Thanks Alexey Grigorev Francis Terence Amit for hosting book of the week,\
      \ much appreciated!"
- name: shaolang
  text: 'hi, Tomaz Bratanic

    Congrats on launching the new MEAP!

    Are graphs algorithms:

    1. affected by the direction (bi- or uni-) of the edges? If so, what are the gotchas
    we should be aware of, especially when dealing with uni-directional edges?

    2. more effective than the "traditional" unsupervised learning algorithms for
    clustering, k-means, etc., other than the fact that data in graphs don''t necessarily
    need to conform to the same structure?

    Recently, I''ve also come across another graph database -- Tigergraph -- that
    touts itself more capable because of the number of hops it can make it much greater
    than Neo4J, e.g., it can detect frauds from nodes/edges that are 6-8 hops away
    from destination. If number of hops are really that important, are there algorithms
    that can make up for such scenarios.'
  replies:
  - name: Tomaz Bratanic
    text: 1. algorithms are definitely affected whether edges are undirected or directed.
      You can think of a undirected edge as two directed edges, where each points
      in the opposite direction. The main difference between undirected and directed
      edges is the semantics... for example, if I am friends with you, does that directly
      imply that you're also a friend with me. If the direct implication can be made,
      then you are most likely dealing with an undirected edge. In practice you will
      see a lot of undirected edges.
  - name: Tomaz Bratanic
    text: 2. Clustering is a big category of graph algorithms, so it's hard to say
      if they are better. It has more of to do with your data input. If you are dealing
      with vectors, you will most likely use something like k-means, but if you are
      dealing with a connections between data points, then you might use something
      like Label Propagation.
  - name: Tomaz Bratanic
    text: 3. detect frauds from nodes/edges that are 6-8 hops away from destination...
      that's just marketing talk. Any database can do 6-8 hops or joins, even SQL.
      The question is how fast and at what scale
  - name: shaolang
    text: 'thanks for taking my questions, Tomaz Bratanic!

      1. As direction matters in edges, does that mean results from the algorithms
      may differ depending on where the starting point is? Using your friend example
      and assuming it''s unidirectional, the algorithm would be able to detect we
      are friends when the query starts from you (node), but it can''t detect if the
      query starts from me (node)?'
  - name: shaolang
    text: '(skipping 2)

      3. Are you saying that Neo4J can do 6-8 hops too at reasonable speed and scale?
      While I always take a pinch of salt, their marketing implies that Neo4J can''t
      even complete the query. To make Neo4J complete this many hops, would we need
      to write convoluted Cypher to achieve it?'
- name: GerryK
  text: 'Hi Tomaz Bratanic, thanks for being here.

    - Are you refering to any tools for visualisation for better understanding the
    graph concept?

    - Do you see more and more projects/companies using graphs?'
  replies:
  - name: Tomaz Bratanic
    text: '1. I don''t talk about viz tools in the book, but my favourite tool to
      analyse and visualize small graphs is Gephi

      2. I think that more and more companies are using graphs, some because they
      see the value, some because it is become more and more of a "hot" technology'
- name: Prashant Choudhary
  text: 'Hi Tomaz Bratanic

    ML models are probabilistic in nature. Using ML models to extract information
    from unstructured text would not be 100% accurate. Mostly 80-90% accurate. In
    contrast, Data in graphs should be factual and correct. Knowledge Graphs become
    data source for various apps like goggle, chatbot where you need the information
    to be factually correct. What are your thoughts?'
  replies:
  - name: Tomaz Bratanic
    text: It depends on your use-case. The more messier your knowledge graph, the
      messier the output. Extracting information from text is hard. First of all,
      not all of the extracted information conforms to the graph structure, and secondly,
      even 80-90% accuracy is sometimes hard to achieve. What might be a big problem
      with constructing a graph from text is entity disambigation for example
  - name: Taher Hassonjee
    text: A little late to the conversation, but this is exactly what my company does.
      We turn any unstructured text into a custom CSV output. If you're interested,
      I'm happy to give you access and get your feedback
  - name: Tomaz Bratanic
    text: do you extract triples?
  - name: Taher Hassonjee
    text: Not yet but on the roadmap
- name: insop
  text: "Hi Tomaz Bratanic\nThank you for introducing [Graph Algorithms for Data Science](https://datatalks.club/books/20220926-graph-algorithms-for-data-science.html)\
    \ , I would be very interested in reading recommendation and fraud detection chapters\
    \ from your book.\n- one general question, what would be the difference that you\
    \ are covering in your book and GNN (graph neural network) and graph CNN? \n-\
    \ and what are the applications for each of those can be applied?\nThank you very\
    \ much,"
  replies:
  - name: Tomaz Bratanic
    text: 'GNNs are the state of the art methods of graph ML at the moment. My book
      builds up all the knowledge to get to GNNs, but doesn''t delve too much into
      them. If you are interested in recommendations and fraud detection I would recommend
      the following book: [https://www.manning.com/books/graph-powered-machine-learning](https://www.manning.com/books/graph-powered-machine-learning)'
  - name: Bhupendrasinh Thakre
    text: Tomaz Bratanic do you also go through hands on learning in your book or
      theory only
  - name: Tomaz Bratanic
    text: it's mostly hands on learning
- name: Julius
  text: The book that was mentioned in the week 1 video about being the best book
    to read as regards DE. Please I didn't get the spelling
  replies:
  - name: Alexey Grigorev
    text: 'You need to give more context. Which week 1? Was it course? Which one?

      Also, this is not the right channel for asking these questions. Here we invite
      book authors and ask them anything'

---

Graphs are the natural way to understand connected data. This book explores the most important algorithms and techniques for graphs in data science, with practical examples and concrete advice on implementation and deployment.

In Graph Algorithms for Data Science you will learn:

- Labeled-property graph modeling
- Constructing a graph from structured data such as CSV or SQL
- NLP techniques to construct a graph from unstructured data
- Cypher query language syntax to manipulate data and extract insights
- Social network analysis algorithms like PageRank and community detection
- How to translate graph structure to a ML model input with node embedding models
- Using graph features in node classification and link prediction workflows

Graph Algorithms for Data Science is a hands-on guide to working with graph-based data in applications like machine learning, fraud detection, and business data analysis. It’s filled with fascinating and fun projects, demonstrating the ins-and-outs of graphs. You’ll gain practical skills by analyzing Twitter, building graphs with NLP techniques, and much more. You don’t need any graph experience to start benefiting from this insightful guide. These powerful graph algorithms are explained in clear, jargon-free text and illustrations that makes them easy to apply to your own projects.