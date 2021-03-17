---
title: "Designing Data-Intensive Applications"
description: "Book of the Week. Designing Data-Intensive Applications by Martin Kleppmann"
cover: "images/books/20210308-designing-data-intensive-applications/cover.jpg"
image: "images/books/20210308-designing-data-intensive-applications/preview.jpg"
start: 2021-03-08 00:00:00
end: 2021-03-12 22:59:58
authors: [martinkleppmann]
links: 
  - text: Book's page on O'Reilly
    link: https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/
  - text: Book's website
    link: https://dataintensive.net/

archive:
- name: Tino
  text: 'Hey Martin Kleppmann :) Thanks for taking the time!
    How important would you consider planning this process in different stages of
    a company? Should a start up immediately plan applications for data-intense use
    cases or should the focus be elswhere?'
  replies:
  - name: Martin Kleppmann
    text: 'Hey :) I would say it depends on what the company
      does. If you''re in the business of processing large amounts of data (e.g. you''re
      crawling large numbers of websites), it''ll be worth thinking about architecture
      up-front.

      But most startups (e.g. typical SaaS apps) don''t initially have a lot of data.
      For these early stage companies, I would specifically advise *against* investing
      in a scalable architecture until you actually need it. The priority of an early-stage
      business is to be flexible and quickly adapt to the needs of customers as they
      are discovered. A complicated architecture is actually harmful here, because
      it reduces flexibility. Personally I''d just stick with PostgreSQL in this situation,
      and keep everything as simple as possible.'
- name: pie_f11235
  text: "Hi Martin could you elaborate this (chapter 3) a bit more?\nCounterintuitively,\
    \ the performance advantage of in-memory databases is not due to the fact that\
    \ they don't need to read from disk. Even a disk-based storage engine may never\
    \ need to read from disk if you have enough memory, because the operating system\
    \ caches recently used disk blocks in memory anyway. Rather, they can be faster\
    \ because they can avoid the overheads of encoding in-memory data structures in\
    \ a form that can be written to disk"
  replies:
  - name: Martin Kleppmann
    text: What exactly do you find unclear or do you want to know more about?
  - name: Martin Kleppmann
    text: Data in memory typically has a different representation from data on disk.
      For example, in memory you can use pointers, but pointers to memory addresses
      don't make sense on disk, since after you restart a computer all the data will
      be at different memory addresses.
  - name: Martin Kleppmann
    text: Therefore, you need to convert between the disk-oriented representation
      and the in-memory representation. This conversion incurs a cost. A database
      that doesn't maintain on-disk data structures can save the conversion, because
      it can work with the in-memory representation only.
  - name: pie_f11235
    text: when reading this from the book it gave me the impression is disk-based
      db + cache would be just as equivalent good and therefore we do not need to
      have in-memory db at all
  - name: pie_f11235
    text: 'or if we do then in-memory dbs essentially shall be used as cache.

      I wonder if I miss any point if I think in that extreme?'
  - name: Martin Kleppmann
    text: 'For a more detailed argument I suggest reading the papers referenced in
      this section:

      [https://hstore.cs.brown.edu/papers/hstore-lookingglass.pdf](https://hstore.cs.brown.edu/papers/hstore-lookingglass.pdf)

      [http://www.vldb.org/pvldb/vol6/p1942-debrabant.pdf](http://www.vldb.org/pvldb/vol6/p1942-debrabant.pdf)'
  - name: pie_f11235
    text: ok thanks Martin. let me check them out. I read the lookingglass one but
      not yet the other one. I probably misunderstood the whole thing
- name: Vladimir Finkelshtein
  text: In different data teams (small startup, midsize, large internet company) which
    role is usually responsible for the design?
  replies:
  - name: Martin Kleppmann
    text: I'm afraid I don't have enough first-hand experience of different companies
      to give a good answer.
- name: Vladimir Finkelshtein
  text: It seems like you cover how different tools fit your tasks and other tradeoffs,
    and that is supposed to help you make your tooling choices. I wonder if in reality
    the choices are made based mainly on unrelated criteria. For example, how the
    pricing scheme of these tools matches your usage/budget or whether your team is
    already familiar with the tool.
  replies:
  - name: Martin Kleppmann
    text: 'I think whether a team is already familiar with a tool is an important
      factor. The fewer new tools you have to learn, the better! But it shouldn''t
      be the only factor: if you try to bend a single tool to all possible applications,
      you may run into difficulties too. As always, it''s a judgement call.'
  - name: Martin Kleppmann
    text: In practice, I suspect a lot of decisions are also made based on whether
      a technology is currently fashionable or not (e.g. whether the team members
      recently heard a conference talk about it, or read a tweet about it). That is
      poor practice in my opinion, but I can't deny that it happens!
- name: Martin Mihal
  text: I just check book quickly (chapters, topics etc) - just question before invest
    time into full reading . Are those topics (eg. Scalabality, Maintanance, Replication
    ..) in world of cloud (eg. ..Kinesis, S3 as Data Lake, Athena, Snowflake..) still
    worth to go deep into? All of those tools were created to handle those topic "in
    price"... (I mean it's important to undrstand those topics, question is how deep
    in this complex world we want/need to go)
  replies:
  - name: Martin Kleppmann
    text: 'Cloud services reduce the amount of investment you need to make into operations,
      because someone else is providing the operations team for you. But in order
      to know how to use a cloud service effectively, you still need a good understanding
      of what it can and cannot do. And you often don''t get that understanding from
      reading the vendor''s documentation alone, because a vendor will always pretend
      that their product is great for all purposes, even if it has strengths and weaknesses.

      The purpose of my book is to teach you the fundamentals so that you can figure
      out the strengths and weaknesses of different technologies. That applies equally,
      regardless of whether you''re self-hosting or using a cloud service.'
- name: Slim
  text: Hello, thanks for writing a great book like designing data intensive applications.
    My question is; do you think that relational database is the suitable solutions
    for banking systems. According to some experiences I had with finance companies
    they prefer relational database because of the utility of transactions and it's
    straightforward to use. But sometimes I feel like it needs a graph database due
    to huge number of join and relation between tables which makes things complex.
    What do you think about that?
  replies:
  - name: Martin Kleppmann
    text: Hi Slim! I have never worked at a bank, so I don't have personal experience.
      But my impression is that it doesn't make sense to talk about the suitability
      of a technology for banking as a whole, since banking is a complex business
      where different parts of the business may have very different requirements.
      The needs of the people doing fraud prevention or anti-money-laundering will
      likely be very different from the needs of the people processing mortgage applications.
      The needs of those dealing with investments or trading will be different again.
  - name: Martin Kleppmann
    text: I understand if there is a preference of relational databases since they
      are quite versatile and can satisfy the needs of a fairly wide range of applications
      (though not everything), and sometimes it's better to stick with a tool you
      are deeply familiar with ("the devil you know"), even if it's not quite optimal
      for the use case, than to incur the cost of learning how to use and reliably
      operate a different tool.
  - name: Martin Kleppmann
    text: "Keep in mind that choosing to adopt a certain database is not just a matter\
      \ of the developers choosing one API or query language over another. There is\
      \ also the need to set up backups, disaster recovery, to have ETL to bring the\
      \ data from operational systems into a data warehouse, maybe audit logs, etc.\
      \ etc. \u2014 adopting a new data storage technology also requires figuring\
      \ out all this infrastructure."
  - name: Martin Kleppmann
    text: So I have a lot of sympathy for organisations that are hesitant to adopt
      new technologies, even if they are better suited to the problem than whatever
      they are currently using.
  - name: Slim
    text: 'thanks for this detailed answer :relaxed::relaxed:'
- name: A McCauley
  text: 'Hey Martin :wave::skin-tone-3: great book! What would you say from your experience,
    is one of the most overlooked principles when designing data-intensive applications?'
  replies:
  - name: Martin Kleppmann
    text: I'm afraid I don't have a good pithy answer for this. Different companies/situations
      have different needs and different problems. Part of the ethos of the book is
      that there isn't one single technology or principle that is universally applicable;
      rather, there are trade-offs, and knowing what they are will let you choose
      the right tool for the job.
- name: A McCauley
  text: And what is the most apparent challenge for teams/companies, etc. when designing
    data-intensive applications?
  replies:
  - name: Martin Kleppmann
    text: I think the biggest challenge is perhaps that there is such a bewilderingly
      large number of tools out there, and it can be really difficult to figure out
      which is best for a given task. Hence a primary goal of the book is to help
      you figure out what questions you need to ask in order to choose an appropriate
      technology.
- name: Slim
  text: what's the approach that you recommend in microservices in order to guarantee
    the ACID properties in a transactions. I think it is not possible to guarantee
    ACID in distributed systems especially for rollback or when there is an error
    during the transaction.
  replies:
  - name: Martin Kleppmann
    text: most microservices architecture use transactions only within the bounds
      of a single service, and don't have distributed transactions across service
      boundaries. this can sometimes make it really difficult to keep data consistent.
      there have been attempts to allow cross-service transactions (such as WS-AtomicTransaction
      in the SOAP world) but I fear this is not a good answer, since it introduces
      tight coupling between services.
  - name: Martin Kleppmann
    text: "one approach I've seen recommended is to draw the boundaries between services\
      \ such that cross-service transactions simply are not necessary. this means\
      \ that if you have two services that do need atomic commit, you need to merge\
      \ them into a single service \u2014 i.e. don't make the services too fine-grained."
  - name: Martin Kleppmann
    text: another idea I've seen is to use a persistent log such as Kafka for communicating
      between services (instead of just ephemeral HTTP/RPC requests). this doesn't
      quite give you atomic transactions, but it does give you pretty strong assurance
      that if one consumer reads a message off the log, all of the consumers will
      read that message. you can build some pretty strong guarantees based on that.
  - name: Martin Kleppmann
    text: 'I elaborate on that second idea in this article on Online Event Processing:
      [https://martin.kleppmann.com/papers/olep-cacm.pdf](https://martin.kleppmann.com/papers/olep-cacm.pdf)

      and Ben Stopford has also written about using Kafka for inter-service communication:
      [https://www.confluent.io/designing-event-driven-systems/](https://www.confluent.io/designing-event-driven-systems/)'
  - name: Slim
    text: thanks Martin. I have seen a similair approach mentioned in Microservices
      patterns book written by Chris Richardson.
- name: "Andr\xE9 Duarte"
  text: 'Hey Martin! What would be the top 3 things you would add, remove or change
    from the book if you were to rewrite it?

    Thanks for your time'
  replies:
  - name: Martin Kleppmann
    text: 'Big question! I have been collecting ideas for a second edition but have
      not yet started on it. Some ideas for improvement are:

      - talk more about hosted cloud DB-as-a-service infrastructure, which has gained
      popularity rapidly (but which still requires a lot of technical knowledge to
      use well)

      - there are tons of new tools in areas such as time series, workflow engines,
      new transaction processing engines ("NewSQL")'
  - name: Martin Kleppmann
    text: '- maybe a bit more on decentralised and [local-first](https://www.inkandswitch.com/local-first.html)
      technologies, since interest in those has been growing

      - I was thinking it might be cool to interview people at a couple of major internet
      companies and get them to share examples of their architectures, as case studies
      to discuss in the book'
- name: Sal DiStefano
  text: If you have not checked out Martin Kleppmann [blog](https://martinkl.substack.com/),
    you should. He is also on [Patreon](https://www.patreon.com/martinkl).
  replies: []
- name: Uriah Stephenson-Ward
  text: Hi Martin Kleppmann do you plan on updating or making any revisions soon?
    Is there any specific tech/concepts/etc coming out that you think is exciting
    or will likely become the dominant way of working?
  replies:
  - name: Martin Kleppmann
    text: 'I am collecting ideas for a second edition, but not planning to start work
      on it for at least another year, since the current content is still pretty up-to-date.

      I replied about ideas for a second edition in [this thread](https://datatalks-club.slack.com/archives/C01H403LKG8/p1615222541049600)'
- name: Elias
  text: "Hello Martin, it\u2019s a great honor, and thank you for your book! In the\
    \ last chapter, you are writing about the future of data systems. And many of\
    \ your ideas and approaches from this chapter are already common nowadays (derived\
    \ state, unifying batch and stream, designing apps around dataflows, etc.). But\
    \ from your point of view, in recent years in data systems:\n- what are the things\
    \ you expected to happen that didn\u2019t happen (or you wish happened, or should\u2019\
    ve happened faster/at a bigger scale)\n- and what are the things that happened\
    \ but you were not thinking about them when writing the book? \nThank you!"
  replies:
  - name: Martin Kleppmann
    text: "some of this has happened, but my sense is that the big idea \u2014 redesigning\
      \ interfaces and APIs around dataflow rather than request/response interaction\
      \ \u2014 is still a long way away. there are plenty of REST APIs for online\
      \ services out there, but not many of them let you subscribe to a log of changes.\
      \ the best you can usually hope for is a webhook, and this is really just a\
      \ notification mechanism \u2014 you can't use it to reliably maintain derived\
      \ views onto the data in someone else's API."
  - name: Elias
    text: "Thank you for the answer!\nBut do you still believe this can/will happen,\
      \ or \u201Capplication\u201D and \u201Cdata\u201D worlds are doomed to live\
      \ apart :) (similar to DBMS and OS evolved separately)?"
  - name: Martin Kleppmann
    text: hard to say without a crystal ball. there is a huge amount of existing investment
      in REST API, and hence a huge inertia preventing a move to anything else. on
      the other hand, change data capture in databases seems to be becoming mainstream,
      and when you combine that with stream processing and event subscriptions you're
      not too far off.
- name: Nikolay
  text: 'Hello Martin. I read your article "Please stop calling databases CP or AP"

    Could you please provide some clarification? Does it mean that when we are talking
    about a distributed queue we can not talk about strong consistency ( linearizability)  at
    all. I mean that even if value X is written to queue it will not be immediately
    available for reading even for that client(read your own writes consistency model).
    So distributed queue can not provide strong consistency, can it? if so... what
    the strongest level of consistency can we have in distributed queue.'
  replies:
  - name: Martin Kleppmann
    text: 'Linearizability is a very useful property and it makes sense to talk about
      it. However, it''s a property of a particular *operation* or set of operations;
      a system may well provide some operations that are linearizable and others that
      are not. For this reason it doesn''t really make sense to label the system as
      "consistent" or not in the sense of CAP. Rather, we should say, for example:
      the enqueue and dequeue operations are linearisable.'
  - name: Martin Kleppmann
    text: Defining the "strongest level of consistency we can have" is a bit tricky
      because there is no good formal definition of what "stronger" means. But I do
      think that in practice, linearizable enqueues/dequeues are probably the strongest
      useful consistency model you will find for a queue.
- name: Nikolay
  text: One more question from my side. if we have 2 nodes - A and B. A is a leader.
    B is a follower. client issue write(X,1) to a leader. if the leader uses 2PC in
    order to implement atomic commit. is it possible to have a case when  A and B
    have different observable values before A sends ACK to client?
  replies:
  - name: Martin Kleppmann
    text: observable to whom? to another client that is querying A and B? atomic commit/2PC
      does not guarantee anything about concurrency (it's about handling crashes cleanly,
      not about concurrency). it is entirely possible for a client to query A and
      B while the 2PC protocol is in progress, and to get different responses from
      the two nodes.
- name: Nikolay
  text: I have a question that I guess is related to chapter 12 of the DDIA book.  Most
    databases have their own cache. For example, oracle, postgress has its own buffer
    cache ( its cache of blocks). Cassandra has a row cache. Oracle also has a row
    cache. On another side, we have solutions like Redis, Memcached. As far as I can
    understand database is moving in the direction to have a separate computation
    engine and separate storage engine. Why not have a separate cache engine? I mean
    it would be nice to have the ability to have cache "inside" database(integrated
    cache) but so that we would be able to scale this cache. as far as I can see it's
    not a way of modern databases. So there is probably something wrong with this
    approach. I mean we can not have an integrated scalable cache, can we?
  replies:
  - name: Martin Kleppmann
    text: This would make for an interesting research project! I don't think it's
      possible to say for certain whether this approach makes sense without actually
      trying it and seeing whether it helps and where it breaks down.
  - name: Martin Kleppmann
    text: There is a long-standing debate between implementors of database engines
      and implementors of operating systems about caching of disk pages in memory.
      The OS automatically uses memory that would otherwise be unused to cache recently
      accessed disk blocks. But then a DB may need its own buffer cache (e.g. because
      it needs to control when a dirty page is written back to disk, because it has
      to go to the WAL before the data page is written), so data ends up being cached
      twice, which wastes memory.
  - name: Martin Kleppmann
    text: there is a difference between memcache/redis and these block-level caches,
      which is that application-level caches such as memcache/redis don't just store
      disk blocks, but they store entire precomputed responses to complex queries,
      potentially including some business logic. serving that data from a cache doesn't
      only save on I/O, but also on computation time, which might be significant.
  - name: Nikolay
    text: 'Cool. Thank you very much for your reply. Just want to add that Oracle
      has its own ROW cache. "When a query executes, the database searches the cache
      memory to determine whether the result exists in the result cache. If the result
      exists, then the database retrieves the result from memory instead of executing
      the query. If the result is not cached, then the database executes the query,
      returns the result as output, and stores the result in the result cache.

      When users execute queries and functions repeatedly, the database retrieves
      rows from the cache, decreasing response time. Cached results become invalid
      when data in dependent database objects is modified."'
- name: Nikolay
  text: 'Regarding Chapter 3 of the DDIA book. As I understand LSM is optimized for 
      write compare to B+Tree because LST writes less to disks.

    If I understand correctly in the case of B+Tree each block is mapped to a disk
    file and when we update even 1 byte in B+Tree we have to update the whole block.
    as I know in oracle we will not update each block when we change 1 byte. we will
    write the whole block to disk just in case of checkpoint (every 3 seconds in the
    background) and during update statement, we will only write to WAL. So when I
    do update idx_value = 1 where id = ? database will write only 1 byte to WAL and
    the whole block will be flushed to disk only during checkpoint ( for simplicity
    I skipped part related to oracle undo segment). So it looks like for a simple
    update we will have to write to disk the same amount of bytes in the case of LSM
    and B+Tree, does not it?'
  replies:
  - name: Martin Kleppmann
    text: I wouldn't necessarily say that "LST writes less to disk" (a statement about
      write amplification), but rather that LST writes tend to be a more sequential
      access pattern compared to B-tree writes, and so there can be a performance
      advantage on disks where random-access writes are slower than sequential ones.
  - name: Martin Kleppmann
    text: as far as I know, a disk always writes data an entire block at a time, even
      if you only change 1 byte in a file. (that's why linux calls a disk a "block
      device".)
  - name: Martin Kleppmann
    text: a relational DB will tend to have its own concept of pages that doesn't
      map exactly to physical disk blocks, but is roughly related.
  - name: Martin Kleppmann
    text: it's not the case that every database block/page maps to a separate file
      (file systems would not cope well with such a large number of small files).
      I think DBs usually allocate one big file containing many blocks, and use offsets
      into that file to identify blocks.
  - name: Martin Kleppmann
    text: if you update just one row, you're right that the WAL write will happen
      first, but the page containing the row will also have to be written sooner or
      later, even if the transaction is allowed to commit before it is written.
- name: Nikolay
  text: In chapter 5 of the DDIA book, you described multi-leader replication. Does
    it mean that in the case of multi-leader replication particular client can connect
    only to 1 leader? i mean that if we have 2 DC and lots of clients (say 10K) ...
    each of our clients connects to a particular leader and if that leader is crashed
    ... half of our clients can not connect to another leader?  This part is not clear
    to me. as an example, it works like that in app calendar .. because i can connect
    only to 1 leader( which is on my own machine) . I can not connect to other clients
    :-). but what about 2 Data Center ( 3 DC)?
  replies:
  - name: Martin Kleppmann
    text: it will depend on the specific system, but in general I don't see any reason
      why you can't have one client to connect to multiple leaders. one potential
      setup would be for a client to connect to a leader in the local DC by default,
      and fall back to connecting to a different DC in the case of problems.
- name: Alexey Grigorev
  text: 'I have two questions from ankush khanna who''s travelling now and can''t
    ask the questions himself.

    So the first one:

    What do you think about the future of Serializable Snapshot Isolation?'
  replies:
  - name: Martin Kleppmann
    text: I think it's excellent, and more systems besides PostgreSQL should use it!
- name: Alexey Grigorev
  text: 'Second:

    Your book covers a lot of ground regarding Streaming, but with advancement and
    popularity in streaming will you write more material on topics like Kafka or Pulsar?'
  replies:
  - name: Martin Kleppmann
    text: Perhaps, although other authors have already covered streaming systems in
      great detail, so I'm not sure there is much more for me to add.
  - name: Rishabh Bhargava
    text: 'Just to follow-up on this: which authors would you recommend reading to
      dive deeper into streaming systems?'
  - name: Martin Kleppmann
    text: '"Streaming Systems" by Akidau et al.; "Kafka - The definitive guide" by
      Narkhede et al.'
  - name: Martin Kleppmann
    text: (I think a second edition of the Kafka book is in the works)
  - name: Rishabh Bhargava
    text: Thank you!
- name: Alexey Grigorev
  text: Hi Martin Kleppmann! You were working as a software engineer, but then went
    to academia and started working as a researcher. What motivated you to focus on
    research?
  replies:
  - name: Martin Kleppmann
    text: "I got tired of the short-termism in industry, especially in startups, where\
      \ everything has always got to happen \"right now\". I wanted a setup where\
      \ I would have the space to think, to take the time to really understand things,\
      \ and to work to improve the foundations of how we write software. In research\
      \ I can work on things that may not be practical for another 5\u201310 years,\
      \ and that's fine. In a company you can't normally work with such a long time\
      \ horizon."
  - name: Alexey Grigorev
    text: I can totally relate to that. Thank you for your answer!
- name: Jonathan Diaz
  text: Hi Martin Kleppmann. It's awesome to e-meet you and I actually just finished
    reading DDIA a few days ago! One quote that stuck out to me was in the last chapter
    from Maciej Ceglowski "_Machine learning is like money laundering for bias_" which
    led me down a rabbit hole of finding the source [here](https://idlewords.com/talks/sase_panel.htm).
    What, in your opinion, can we do further so that ML algorithms/technologies don't
    strengthen existing biases? Both for data folks who develop these algorithms and
    those who use them.
  replies:
  - name: Martin Kleppmann
    text: I'm afraid this is not my area; others are working very actively on this,
      but it's fast-moving and I am not up-to-date. I suggest looking up work by folks
      such as Timnit Gebru and Cathy O'Neil.
- name: Manoj Agarwal
  text: Hi Martin Kleppmann I watched your amazing video series on [Distributed Systems](https://www.youtube.com/watch?v=UEAMfLPZZhE&amp;list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB).
    Are videos of any other of your courses available publicly?
  replies:
  - name: Martin Kleppmann
    text: 'This is the only multi-lecture course available so far. I also have this
      playlist of conference talks I have done: [https://www.youtube.com/watch?v=fU9hR3kiOK0](https://www.youtube.com/watch?v=fU9hR3kiOK0&amp;list=PLeKd45zvjcDHJxge6VtYUAbYnvd_VNQCx)'
  - name: Martin Kleppmann
    text: 'it includes some course-like material, such as this 2-hour lecture on formally
      verifying distributed algorithms: [https://www.youtube.com/watch?v=Uav5jWHNghY](https://www.youtube.com/watch?v=Uav5jWHNghY&amp;list=PLeKd45zvjcDHJxge6VtYUAbYnvd_VNQCx&amp;index=26)'
- name: RH
  text: "Hi Martin,\nBackground: I work in a startup with a small engineering team;\
    \ I mostly work on building NLP based microservices (data analysis to devops)\
    \ in Python to serve other parts of our product. We have a few models in production\
    \ which are working quiet well, and en route to building a few more.\n*Question\
    \ 1*: When I joined, we did not have a lot of data (few Gigabytes), but data is\
    \ starting to build up (Terabyte). We currently store most of our data in Postgres.\
    \ Most of the data is large blobs of semi structured texts that are uploaded by\
    \ our customers to be processed and saved (the data format is similar to resumes).\
    \ I believe that Postgres was the right DB to start with because it was very versatile\
    \ and was good for making this happen \u201Cright now\u201D, but not sure what\
    \ the right thing to do is next?  The queries are becoming slower and slower.\
    \ I have thought of saving all the larger blobs of texts in a S3 bucket, and saving\
    \ a retrieval link for that object in Postgres, but that makes retrieval slower.\
    \ We retrieve the data very often.\n*Question 2:* When the data is sent to us\
    \ by the customer, we do not process it in anyway. We just save it the way it\
    \ is sent by the customer. Do you think it is a good idea to process the data,\
    \ and save \u201Cfeatures\u201D from the data in Postgres instead of reprocessing\
    \ the data over and over again. That is, we should save the data the way the customer\
    \ sent it (maybe in a S3 bucket) but we should process and save a version of the\
    \ data that is relevant to our business case (this is something the engineering\
    \ lead does not see value in, and prefer to beef up the servers).\n*Question 3*\
    \  What is a good way to structure a data engineering / systems engineering career\
    \ i.e. what makes a really good data/system engineer?"
  replies:
  - name: Martin Kleppmann
    text: 'q1: it''s difficult to make a concrete recommendation without knowing much
      more about the characteristics of your data, the access patterns and queries
      you use, etc. You might be able to continue using Postgres by splitting the
      database across multiple machines, perhaps using something like Citus. If you
      don''t do many joins in queries, you could consider using a key-value store/document
      DB such as Cassandra or MongoDB, but that would be a much bigger change.'
  - name: Martin Kleppmann
    text: a distributed filesystem or an object store like S3 would make sense if
      the data items are large. this would scale well, but would make it much harder
      to do any indexing (i.e. finding documents based on some value that occurs within
      a document).
  - name: Martin Kleppmann
    text: 'q2: Saving data in raw form, and separately storing data derived from it,
      is a great pattern. If you want to change your processing logic, you can then
      re-run it on the raw data. The datastore to use for the derived data will again
      depend on the data format and your access patterns.'
  - name: Martin Kleppmann
    text: 'q3: my suggestion would be knowing how to reason about trade-offs. there
      is never one true answer, only various options that each have their pros and
      cons. being able to figure out those strengths and weaknesses, and communicating
      them to the rest of the team, seems very valuable to me.'
  - name: RH
    text: Thank you so much for responding to my questions.
- name: Amr Alaa
  text: 'hey Martin Kleppmann

    thanks for having this week with us, I am really enjoying reading these excellent
    questions and your great answers here, I do not think I have an exact question
    actually,

    just if you have a plan for another book, more specific or more advanced

    I believe that in this DATA era that we live in, you should consider a series
    of books or even a bundle of courses to help data engineers acquire more advanced
    skills in theory and in practical also

    thanks again'
  replies:
  - name: Martin Kleppmann
    text: Thanks! I am considering ideas for a book that would go into more details
      of algorithms used in distributed systems. But work has not yet started, so
      there is no timeline for when this might happen.
- name: Alexey Shvets
  text: 'Martin Kleppmann first of all thank you so much for you amazing work and
    legacy. In you video course you mentioned Leslie Lamport as a legend in the field
    of distributed system, but for many people you became a legend who made the field
    structured and accessible.

    My question. What do you think, which programming language will dominate distribute
    systems development in the future? Now it is mostly Java, will it move to Golang/Rust?
    What is your personal preference?'
  replies:
  - name: Martin Kleppmann
    text: I think programming languages are a question on which people have very strong
      opinions because each language is like a tribe, and people couple their identity
      to the tribe they belong to. In my opinion, the language in which a system is
      written rarely makes a big difference; more important is the system architecture.
      Most mainstream languages are probably okay for building many types of systems.
  - name: Martin Kleppmann
    text: In particular, I think questions of expressiveness and details of language
      features do not have a big effect when it comes to system operations. What does
      make a difference is a language's runtime characteristics, such as whether it
      supports threads, and whether it uses a garbage collection runtime. No GC means
      no GC pauses, which can be important for low-latency systems.
  - name: Martin Kleppmann
    text: Rust is interesting to me because it's memory-safe, supports threads, has
      no GC runtime, and is very portable (you can use it to build mobile apps or
      servers or web apps by compiling to wasm). But in the end, it's the needs of
      a particular system that matter. There is no one language that is perfect for
      all systems programming.
- name: Pavel Bukhmatov
  text: 'Hey Martin Kleppmann! Thanks for a book and all the awesome research you
    do!

    What is your opinion on implementing distributed storages using conflict-free
    replicated data types in future? The ideas behind CRDTs seems to be really compelling
    for distributed systems but the sheer complexity might overwhelm practical implementations
    as far as my limited understanding goes. What research / papers / books could
    you suggest on the topic?'
  replies:
  - name: Martin Kleppmann
    text: I am a big believer in CRDTs, and have been doing research on them for the
      last 6 years! I maintain a community website [https://crdt.tech/](https://crdt.tech/)
      that has a lot of resources on CRDTs, and links to all the latest research (including
      my own).
- name: Alisher
  text: "hi, Martin Kleppmann, thanks for the book and all your educational activity!\
    \ \nI'd like to ask you a bit broad question - what do you think are the most\
    \ promising and perspective topics in distributed systems  research in next 5\
    \ years? which topics are underestimated and require more\nresearchers there?\n\
    Thank you."
  replies:
  - name: Martin Kleppmann
    text: Well, this is going to be very subjective, since every person has their
      own priorities! Personally I am excited about the potential of [local-first
      software](https://www.inkandswitch.com/local-first.html), and moving away some
      of the current cloud-centric view of distributed systems. That's what I'm going
      to be working on for the next 5 years, anyway!
- name: Nikolay
  text: Hello Martin Kleppmann. Could you please help to build intuition about [Version
    Vectors](http://en.wikipedia.org/wiki/Version_vector) and [Vector Clocks](http://en.wikipedia.org/wiki/Vector_clock).
    i read about them in chapter 5 but can not understand the difference. i am looking
    for some examples in order to build intuition.I know that it's a long story and
    i read also some articles from Riak founders. But i's not still clear for me ).
    Maybe some good example will let to understand it.
  replies:
  - name: Martin Kleppmann
    text: Ah yes, I have struggled with this as well. I'm afraid a proper explanation
      goes beyond what I can provide here in a few sentences. I should do a blog post
      on this at some point.
  - name: Martin Kleppmann
    text: 'at a high level, the difference is in purpose. a vector clock is used to
      compare *events* in a distributed system, and figure out which happened before
      which, and which are concurrent. a version vector is used to compare *states*
      of replicas, and figure out whether one state supersedes the other. the mechanism
      in both cases is similar: a vector of numbers that are incremented.'
---

NoSQL... Big Data... Scalability... CAP Theorem... Eventual Consistency... Sharding...

Nice buzzwords, but how does the stuff actually work?

As software engineers, we need to build applications that are reliable, scalable and maintainable
in the long run. We need to understand the range of available tools and their trade-offs. For that,
we have to dig deeper than buzzwords.

This book will help you navigate the diverse and fast-changing landscape of technologies for storing
and processing data. We compare a broad variety of tools and approaches, so that you can see the
strengths and weaknesses of each, and decide what’s best for your application.