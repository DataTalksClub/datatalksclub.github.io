---
title: "Software Mistakes and Tradeoffs"
description: "Book of the Week. Software Mistakes and Tradeoffs by Tomasz Lelek and Jon Skeet"
cover: "images/books/20210906-software-mistakes-and-tradeoffs/cover.jpg"
image: "images/books/20210906-software-mistakes-and-tradeoffs/preview.jpg"
start: 2021-09-06 00:00:00
end: 2021-09-10 22:59:58
authors: [tomaszlelek, jonskeet]
links: 
  - text: Book's page
    link: https://www.manning.com/books/software-mistakes-and-tradeoffs

archive:
- name: Rui Ramos
  text: "Hi Tomasz Lelek thanks for joining the group \U0001F642 . Does the book focus\
    \ on any specific software development language or is it agnostic to it ?"
  replies: []
- name: Rui Ramos
  text: What is the main audience for the book ?
  replies:
  - name: Tomasz Lelek
    text: 'The book is written in a way that a lot of people involved in the software
      engineering industry may benefit from:

      - Software engineers that have some experience but want to progress to the next
      level. They may benefit mostly from the trade-offs at the lower level (code)

      - Experience software engineers that will be able to relate to mistakes and
      trade-offs shown in this book.

      - System Architects that will benefit from the holistic examples of variety
      of system, and trade-offs at the architecture level.'
- name: Tomasz Lelek
  text: "The concepts covered in this book are language agnostic. However, to create\
    \ a book that is not purely theoretical and shows the practical aspects of software\
    \ development, the code examples are made in a Java language (there is also a\
    \ couple of C# examples). We wanted to follow the \u201Cshow Don\u2019t tell\u201D\
    \ principle. We picked the Java language as it is widely adapted and relatively\
    \ easy to understand."
  replies: []
- name: Kshitiz
  text: Hi Tomasz Lelek and Jon skeet. Thanks for doing this. I was wondering in your
    experience what are the top mistakes developers/engineers make in this industry?
    In case if you can elaborate on it from data science/ML perspective, that will
    be great.
  replies:
  - name: Tomasz Lelek
    text: 'I can point you to a couple of common mistakes in Big Data processing (that
      you may relate to ML as well):

      - Not leveraging data-locality that result in data shuffling (via slow network).
      It may substantially impact the time your models need to be calculated.

      - Data partitioning not optimized for your read pattern. If you are building
      a data science model, there are big chances that you need to load a lot of data
      often. If the data you read is not optimized for the read pattern (the way you
      are analyzing data), it will impact the overall pipeline efficiency (more on
      that in the chapter 8 of our book)

      - Picking a proper format for storing offline data and understanding its trade-offs
      (Avro, parquet, protobuf)

      - Finding the outliers and filtering them out if they may impact the result
      of your ML processing.

      - Dealing with duplicates in your data. Suppose the data pipeline that is producing
      the data for your ML works in at-least-once semantics (that is very probable).
      In that case, there is a high possibility of duplicates - you need to handle
      them (filter out) in your processing.'
- name: Rui Ramos
  text: Tomasz Lelek can you share the platforms where we can obtain the book as soon
    as it is available ?
  replies:
  - name: Tomasz Lelek
    text: "It is already available, please see:\n[https://www.manning.com/books/software-mistakes-and-tradeoffs](https://www.manning.com/books/software-mistakes-and-tradeoffs)\n\
      It\u2019s in all well-known formats (ePub,mobi,PDF) and on paper."
- name: Alexey Grigorev
  text: What are the most common mistakes that software engineers make?
  replies:
  - name: Tomasz Lelek
    text: "This question deserved a book; that\u2019s why we wrote one \U0001F642\n\
      But to summarize:\n- Blindly following some software development principles\
      \ (e.g., DRY) without realizing it also has drawbacks and costs.\n- Handling\
      \ errors and recovery is a tricky topic; it is easy to make mistakes at this\
      \ level.\n- Overengineering - that is designing components to be super flexible,\
      \ without considering the problems with this approach: maintenance overhead,\
      \ guarding against unpredictable usages, and many more\n- Doing performance\
      \ optimizations based on false assumptions. Optimizing code paths that do not\
      \ impact the overall performance of our applications (optimizing not the hot-path)\n\
      - There is a lot of mistakes that are easy to make regarding work with Date\
      \ and Time; we have a dedicated chapter on that topic.\n- In Big Data processing,\
      \ not leveraging data-locality that result in data shuffling (via slow network).\n\
      - Data partitioning not optimized for your write/read patterns.\n- Treating\
      \ 3rd party libraries that we use as something that we don\u2019t take responsibility\
      \ for. If the 3rd party library has a bug, or we are misusing it, and it will\
      \ impact our users, it\u2019s our problem.\n- Not being aware of the consistency\
      \ and availability of the systems we use (DBs, queues, etc.)\n- Not understanding\
      \ delivery semantics of the systems that we integrate with; handling duplication\
      \ of events/messages in a proper way.\n- Treating data/APIs compatibility as\
      \ an afterthought\n- Trying to use technology because it is trendy."
  - name: Krzysztof Ograbek
    text: Tomasz Lelek _Blindly following some software development principles (e.g.,
      DRY) without realizing it also has drawbacks and costs. -_ could you please
      elaborate on this one? What are the drawbacks? What do you mean by "blindly
      following"? I mean DRY in particular.
  - name: Tomasz Lelek
    text: 'Krzysztof Ograbek

      In the era of micro-services, you can sometimes find the duplication of some
      code between separate codebases. When the code is duplicated, it means that
      it can evolve independently. The fact that the code is duplicated now does not
      mean that it represents exactly the same functionality.  If we strictly follow
      DRY, we should create a library or separate services extracting the duplicated
      code. However, once it is shared between separate codebases, it introduces tight-coupling
      and may slow down development. It limits the way the code can evolve now. It
      is no longer independent. This topic deserves more discussion, and in fact,
      chapter 2 of our book focuses exclusively on this.'
- name: Lalit Pagaria
  text: 'How to avoid over-engineering and pre-mature optimization?

    I always feel like writing generic code but ends up making it over engineered.'
  replies:
  - name: Tomasz Lelek
    text: "Regarding premature optimization, I am trying to answer this question in\
      \ chapter 5 of my book. \nThe critical parts for avoiding it:\n- Base your performance\
      \ data on the SLA and/or empirical data. \n- Both data about throughput (req/s)\
      \ and the expected latency (avg, higher percentiles) are needed.\n- Calculate\
      \ the relevance of the paths in your code using latency and the number of requests\
      \  \n- Having this information, we can calculate the importance of each code\
      \ path in our code. It may turn out that the small percentage of code is responsible\
      \ for majority of business value and user traffic (according to Pareto Principle\
      \ it is often a case)\n- We should measure everything after and before changes.\
      \ Performance tests that validate the system holistically are needed. Also,\
      \ low-level microbenchmarks will allow us to experiment with different optimizations\
      \ faster, decreasing the feedback loop.\n- Once we detected this hot path in\
      \ our code, we can focus optimization efforts on the small excerpt of our code\
      \ and be more efficient with optimizations."
  - name: Tomasz Lelek
    text: 'Regarding over-engineering problem, there is no silver bullet. Often, we
      should not try to come up with a generic solution up-front, quote from chapter
      2:

      ```Sometimes starting from the abstraction and adapting all possible usages
      to it may not be optimal. Instead, we can implement our system by creating independent
      components and let them live independently for some time (even if it requires
      some code duplication). After some time, we may start seeing some common patterns
      between those components, and abstraction may emerge. It may be a proper time
      to remove duplication by creating some abstraction instead of starting from
      it.```'
- name: Krzysztof Ograbek
  text: "Hi Tomasz Lelek, thank you for doing this session \U0001F642\nWhat are the\
    \ most common mistakes/misconceptions that software engineers have about Version\
    \ Control Systems?"
  replies:
  - name: Tomasz Lelek
    text: "I was using only GIT VCS, so I don\u2019t have a good comparison between\
      \ them; therefore I won\u2019t give the answer here"
- name: Krzysztof Ograbek
  text: Currently, I am reading Pragmatic Programmer. How is your book different?
    How can a reader benefit from reading both? If you haven't read the book, please
    ignore the question.
  replies:
  - name: Tomasz Lelek
    text: Yes, Pragmatic Programmer is a great book - I strongly recommend it. Both
      books focus on a variety of aspects of how to create better software. My book
      is more hands-on and practical - it has more examples of recent technologies,
      and trade-offs are discussed based on those technologies.
  - name: Krzysztof Ograbek
    text: Glad to see you recommending this book. Thank you, Tomasz Lelek
- name: Tim Becker
  text: Hi Tomasz Lelek, thank you for answering our questions. I was really looking
    forward to ask questions concerning your book. I am a data scientist, however,
    I spend most of my time writing code and I feel it is quite difficult to anticipate
    all consequences of my design decisions. I would really like to improve in this
    area.
  replies:
  - name: Tomasz Lelek
    text: "I think that the best way to increase awareness is through learning. The\
      \ first thing that I would read is a book about possible patterns and abstractions\
      \ in code. I would recommend this one: [https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8](https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8).\
      \ Once your team knows the tools available, it can start applying them in the\
      \ code.\nKnowing the patterns is often not enough because you need the experience\
      \ when to apply them. This experience can be learned by experimenting in code\
      \ - to allow safe experiments and refactoring, you should, of course, use a\
      \ version control system and branches. The second must-have is a \u201Cgood\u201D\
      \ test coverage of your code. Without any tests, the fear that change will break\
      \ something will be too high, and nobody will risk non-trivial refactoring.\
      \ At this stage, pair programming may be very valuable - cooperation on the\
      \ same code may result in very interesting ideas and improvements.\nYou may\
      \ start refactoring once you have tests, code in version control, and a dedicated\
      \ branch.  The new changes should be submitted as Pull Requests to allow all\
      \ the team members to review, learn and propose improvements. This will enforce\
      \ a collaborative effort on the code improvements.\nRegarding code duplication,\
      \ the DRY principle is a good direction for most of the use cases. However,\
      \ there are some specific scenarios when reducing code duplication and adding\
      \ abstraction too early may lead to tight-coupling of now necessary related\
      \ code paths. It will reduce the flexibility of your code and speed of delivery.\
      \ This is a complex topic, and I encourage you to read the second chapter of\
      \ our book to learn more."
  - name: Tim Becker
    text: thank you! I will definitely try this!
- name: Tim Becker
  text: '- Do you have advice for some general guidelines to get started with that
    will help to improve the quality of my code?'
  replies: []
- name: Tim Becker
  text: '- I would like to increase the awareness in my data science team that software
    design is very important. To be flexible, keep the code and models maintainable
    and many more things. How would you try to convince my team?'
  replies: []
- name: Tim Becker
  text: '- When refactoring a software package that has been writing without former
    planning and without a specific design in mind, where would you start with the
    refactoring? How would you approach this task?'
  replies: []
- name: Tim Becker
  text: '- What can be the advantages of code duplication? I recently saw a lot of
    it and it is creating a mess ...'
  replies: []
- name: Krzysztof Ograbek
  text: "Tomasz Lelek, you already recommended Pragmatic Programmer and Design Patterns\
    \ books. And of course, yours \U0001F642 Do you have more recommendations? What\
    \ about Clean Code? Amazon recommend it along with Design patterns \U0001F642"
  replies: []
- name: Krzysztof Ograbek
  text: 'I''ve seen this pro tip for Software Engineers to learn one new programming
    language each year. What''s your opinion on this? How is it beneficial? Out of
    curiosity: How many languages do you know? How many do you actually use?'
  replies: []
- name: Krzysztof Ograbek
  text: "One more \U0001F642 As programmers we get stuck quite often. Do you have\
    \ any routine, that helps you to move forward when you're stuck?"
  replies:
  - name: Tomasz Lelek
    text: Discussion with another person about the problem will allow you to see a
      different perspective. Also, writing down your ideas will help you organize
      your thoughts and allow you to come up with a better solution to your problem.
- name: Tomasz Lelek
  text: 'Clean code is also a good book at the beginning of the programming journey.

    I think that a programming language is only a tool. It is crucial to learn new
    things, but we should focus more on understanding our systems than learning a
    new language every year. I strongly recommend:

    [https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321)'
  replies: []
- name: Larisa Biriescu
  text: "Hi Tomasz Lelek. I don't know if you treat this subject into your book but\
    \ how do you deal with the more \"human\" errors that may appear while working\
    \ on a project? Errors that derive from poor understanding of the customer's needs,\
    \ unrealistic requirements (or omission of some of them)? I find it more tricky\
    \ to deal with people rather than with code \U0001F605."
  replies:
  - name: Tomasz Lelek
    text: "Of course, that\u2019s a complex topic and deserves a separate discussion\
      \ (or book \U0001F642 In my context, I find it useful to have a decision log\
      \ (document with pros/cons of a decision). In such a document, everyone can\
      \ contribute and understand the requirements and possible solutions: all its\
      \ pros and cons. Everyone can take part in the discussion and vote for a specific\
      \ solution. It may help with those errors, plus everything is explicit, meaning\
      \ that requirements are discussed in more details."
  - name: Kshitiz
    text: Tomasz Lelek - I understand that it is not in context of the book, but this
      maintaining a decision log seems like an interesting approach. Can you explain
      it a bit how do you do it? Like which tools do you use, what type of decisions
      are considered for this? It sounds like an exhausting exercise but it can build
      an excellent mind map for a team if executed well over a long time.
  - name: Tomasz Lelek
    text: The simpler the tool, the better. The tool used for this needs to allow
      full collaboration. I found Google Docs useful for it (or wiki page). Each decision
      can have a dedicated page/document. The person responsible for research can
      describe possibilities with pros and cons. Next, every team member refers to
      those propositions and vote (or propose a new one).
- name: Krzysztof Ograbek
  text: "Thank you Tomasz Lelek for your great answers. Thank you Alexey Grigorev\
    \ for having this channel \U0001F642"
  replies: []

---

In Software Mistakes and Tradeoffs you’ll learn from costly mistakes that Tomasz Lelek and Jon Skeet
have encountered over their impressive careers. You’ll explore real-world scenarios where poor
understanding of tradeoffs lead to major problems down the road, to help you make better design decisions.
Plus, with a little practice, you’ll be able to avoid the pitfalls that trip up even the most experienced
developers.
