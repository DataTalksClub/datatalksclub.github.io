---
authors:
- joshfischer
- ningwang
cover: images/books/20220704-grokking-streaming-systems/cover.jpg
description: Book of the Week. Grokking Streaming Systems by Josh Fischer and Ning
  Wang
end: 2022-07-08 23:59:59
image: images/books/20220704-grokking-streaming-systems/preview.jpg
links:
- link: https://www.manning.com/books/grokking-streaming-systems
  text: Book's page
- link: https://www.amazon.com/Grokking-Streaming-Systems-Real-time-processing/dp/1617297305
  text: Buy on Amazon
- link: https://github.com/nwangtw/GrokkingStreamingSystems
  text: GitHub repository
start: 2022-07-04 00:00:00
title: Grokking Streaming Systems

archive:
- name: Ramsi Kalia
  text: 'Hi Josh Fischer and Ning Wang, thanks for answering questions here!

    If I wanted to build an active learning pipeline (for deep learning models), would
    streaming systems work better than batch systems?

    If I have multiple different modes of input, working on different active learning
    models, will streaming systems help ?

    Thanks for your time!'
  replies:
  - name: Josh Fischer
    text: each have their trade offs.  Do you have any requirements that state your
      pipeline needs to be realtime?
  - name: Ramsi Kalia
    text: 'So, actually I''m very interested in working in Industry 4.0 and trying
      to think of situations where streaming systems are employed.

      And the question I asked was way too vague, but I''m wondering that if I was
      working in predictive maintenance, or logistics and handling, would streaming
      systems be better than batch?

      I know this question is still too vague but that''s because I''m not really
      able to grasp at what point you decide that you need stream data instead of
      ignoring it, besides maybe Google live traffic updates, lol,

      Could you suggest some resources for the same?

      I would really appreciate it! tia!'
  - name: Josh Fischer
    text: "I think you should use a streaming system only after you\u2019ve failed\
      \ with other methods of processing data due to issues in latency or that _real-time_\
      \ or requirement.  Stream processing is great for pulling data in and taking\
      \ action on it as soon as it is created, but then you run design decisions/issues\
      \ that will affect how accurate or complete you data is.  One of these issues\
      \ that may come up is called \u201CDelivery Semantics\u201D"
  - name: Josh Fischer
    text: "How\u2019s that for a non answer? \U0001F604 .  I think Ning Wang has good\
      \ knowledge on this topic."
  - name: Ning Wang
    text: "It is an interesting question. i don\u2019t have a direct answer either.\
      \ My feeling is that it really depends on the real use case. Functionality wise,\
      \ Streaming and batch are very similar to each other. The difference is that\
      \ with streaming, events can be processed one by one or with a window, so the\
      \ system could be more flexible and has lower latency. However, batch could\
      \ be more efficient when the data amount is very high. Therefore, one key question\
      \ you need to answer first is: low latency, or high throughput, which one is\
      \ critical for you.\nAnother factor is what Josh mentioned: delivery semantics.\
      \ Batch can be more friendly if you need accurate result, because failure handling\
      \ could be easier with batch as the data is normally stored somewhere and easy\
      \ to replay, instead of flowing through the system.\nI was in an ML lab in college\
      \ but I am not familiar with deep learning at all. For old school pattern recognition\
      \ systems, my personal feeling is that batch might be more efficient for training\
      \ side, but streaming system can be helpful to improve latency and flexibility\
      \ for the prediction side if they are necessary. But I don\u2019t know if it\
      \ makes sense for deep learning systems."
- name: Mario Tormo
  text: I've just discovered thanks to the title that "to grok" actually exists and
    it has a beautiful meaning (according to the Merriam-Webster dictionary "to understand
    profoundly and intuitively"). How did you find this word?!
  replies:
  - name: Josh Fischer
    text: "Hi Mario,\nThank you for the questions.  Manning Publications has a \u201C\
      Grokking\u201D series that they use for foundational books to answer questions\
      \ like \u201Cwhy do we even do this\u201D in relation to technologies.  While\
      \ working with Bert Bates, our writing coach, he helped us decided which style\
      \ of book we wanted to write. We choose the Grokking Series as we started writing\
      \ it almost  4 years ago and a lot of people were still learning \u201Cwhat\
      \ is a data stream?\u201D and \u201Cwhy/how would I use one?\u201D  We also\
      \ didn\u2019t want to write a book about a specific streaming framework as they\
      \ come and go so fast. So, we wrote this book in hopes of a longer shelf life\
      \ as it will teach others the foundation (and more advanced) concepts to start\
      \ using any streaming framework."
  - name: Josh Fischer
    text: "Grok came from the book \u201CStranger in a Strange Land\u201D: [https://www.amazon.com/Stranger-Strange-Land-Robert-Heinlein/dp/0441790348](https://www.amazon.com/Stranger-Strange-Land-Robert-Heinlein/dp/0441790348)"
  - name: Josh Fischer
    text: 'Here is a little info on Bert Bates, he is a phenomenal teacher and person
      : [https://g.co/kgs/eQczQG](https://g.co/kgs/eQczQG)'
  - name: Mario Tormo
    text: "Heinlein?! That's so cool!  I've read a lot from him but never Stranger\
      \ in a Strange Land.\nI didn't know about the grokking series, but there are\
      \ a lot of grokking books. I must admit I was only acquainted with the \"regional\
      \ dress customs\" books, that have actually also a very beautiful covers.\n\
      Bert looks like he knows what he is doing, specially with Java \U0001F642 Where\
      \ does he teach?"
  - name: Josh Fischer
    text: "He is a self employed contractor.  He is the person who coaches authors\
      \ behind all the Manning and O\u2019Reilly books. He also trains Horses with\
      \ his wife, Kathy Sierra.  Quite the interesting combination of skills, wouldn\u2019\
      t you say?"
  - name: Mario Tormo
    text: Woow! That is a really complete profile. It sounds amazing
- name: Mario Tormo
  text: To which kind of reader is the book aimed, with which prerequisites?
  replies:
  - name: Josh Fischer
    text: We wrote this book for developer with 2 - 3 years of experience, who is
      looking for direction on which path they should take in their career.
  - name: Mario Tormo
    text: What is necessary for not getting lost with the book? What is not necessary
      but could help to get better profit from the book?
  - name: Ning Wang
    text: The code for the book (for the basic concepts in the first a few chapters)
      requires Java 8 to compile/run (on Mac, Linux and Windows). So Java background
      (beginner level) can be helpful for you to play with the demo and understand
      the code better. Streaming systems are for data processing, so any data processing
      related knowledge could be helpful. Our goal is to explain the basic concepts
      in streaming systems, so I hope any level of developers should be able to follow
      with interests of realtime data processing.
  - name: Mario Tormo
    text: "Thanks for your answer! \U0001F642"
  - name: Josh Fischer
    text: I agree with all things Ning said, except we support Java 11 at this time,
      not 8
  - name: Ning Wang
    text: Thx for the correction! My memory lags a lot these days.
- name: Mario Tormo
  text: The cover is beautiful, specially if you compare it with the technical book
    cover standards nowadays. Is the rest of the book illustrated like the cover?
    In case not, what's the style?
  replies:
  - name: Josh Fischer
    text: "The cover is one of my favorite parts of the book.  We don\u2019t match\
      \ the style of the cover, but we did create many diagrams to help teach.  I\u2019\
      ll send some in the comments."
  - name: Josh Fischer
    text: ''
  - name: Josh Fischer
    text: ''
  - name: Josh Fischer
    text: ''
  - name: Mario Tormo
    text: Well, these are also very nice diagrams.
- name: Carise Fernandez
  text: The book looks so delightful! Looking at the chapter previews, I like that
    it's really focused on how streaming systems work, without injecting a particular
    library/framework/etc. Was that a challenge when you were writing the book?
  replies:
  - name: Josh Fischer
    text: You are correct. We (attempted) to do the best we could to explain the fundamental
      concepts behind each streaming system without referencing any of framework.  It
      was quite the challenge.  There were several instances where we had to go digging
      around in different code bases (heron, flink, storm, etc) to make sure we were
      explaining the concepts generally enough that it would make sense for most.  This
      was about the most challenging part of the book for me. Ning, my Co-Author,
      even went above and beyond to build our own simple streaming framework to help
      us teach while we wrote the book.
  - name: Josh Fischer
    text: '[https://github.com/nwangtw/GrokkingStreamingSystems](https://github.com/nwangtw/GrokkingStreamingSystems)'
  - name: Carise Fernandez
    text: Yes, I saw the repo and was very impressed that no cloud account or special
      3rd party frameworks were required. Kudos to you!
  - name: Carise Fernandez
    text: (I read a different streaming systems book awhile ago and while it was helpful
      to think of the batch/streaming abstractions in terms of a particular framework,
      I also felt like I didn't *really* understand what was going on)
  - name: Josh Fischer
    text: The Kudos goes to Ning.  He wrote most of this, he is a phenomenal technologist.
      I can understand the feeling of not knowing what is going on too.  These frameworks
      are extremely complex at times.
  - name: Carise Fernandez
    text: "Thanks again, both to you and Ning for this book. Looking forward to reading\
      \ it \U0001F642"
  - name: Ning Wang
    text: "Thanks! \U0001F604 To be fair, We borrowed a lot of basic logic from [Apache\
      \ Heron ](https://heron.apache.org/)(we are both contributors of the project)."
  - name: Ning Wang
    text: "And you are totally right. It is kinda important to understand what\u2019\
      s really going on in order to build and maintain data processing systems."
  - name: Carise Fernandez
    text: "Nice, I will check it out \U0001F642 to be honest, there are a lot of Apache\
      \ streaming/batch engines/frameworks/etc that makes me wonder if Apache could\
      \ one day put out a mega cheat sheet for them \U0001F602"
  - name: Ning Wang
    text: Yeah. Different data processing frameworks have different goals and trade-offs.
      It is interesting to compare them and (maybe) build a cheat sheet. There are
      also many in-house systems when there are special needs I feel.
- name: GerryK
  text: Hi Josh, the book looks super interesting and the diagrams too. Is there a
    reference on streaming tools or protocols? Like mqtt, spark, kafka?
  replies:
  - name: Josh Fischer
    text: In this book we stay completely agnostic to any framework out there today.  It
      is meant to show people why and when they would use something like Kafka, instead
      of how.
  - name: Josh Fischer
    text: Our targeted reader is a developer with a few years experience who is looking
      for the next stack of technology they want to learn.  This answers the questions
      for streaming frameworks without people getting bogged down in framework specific
      code.   Well that was our hope, at least.
  - name: Ning Wang
    text: Adding one more thing, We hope the existing systems like Kafka and spark
      make more sense to readers after reading the book.
  - name: Mario Tormo
    text: It also makes sure the book is going to stay fresh longer than the tools.
      We all have books about software that doesn't exist anymore... XD
  - name: GerryK
    text: Thanks for your answer both! Makes sense!
- name: Josh Fischer
  text: Ning Wang
  replies: []
- name: Ning Wang
  text: Thanks! Josh Fischer
  replies: []
- name: Abbas Akkasi
  text: Hi, could you please introduce me a good,short, and efficient book to learn
    PySpark ML?
  replies:
  - name: Ning Wang
    text: "Sorry I don\u2019t have a good recommendation. Do you have any? Josh Fischer"
  - name: Josh Fischer
    text: I do not, sorry.
- name: "Philip Die\xDFner"
  text: 'Hello Josh Fischer and Ning Wang, thanks for being here! Nice to see such
    a book teaching the concepts not tied to any framework.

    How did you come to the decision to write the book in the way it is? How much
    work was it timewise?'
  replies:
  - name: Josh Fischer
    text: Thank you for the kind words.  We decided to write a framework agnostic
      book so we would have a book that would last longer than individual frameworks.
      We are hoping to teach people the fundamentals to learn how to plan, predict,
      and diagnose the state of most streaming systems as opposed to being tied to
      one technology implementation.
  - name: Ning Wang
    text: Timewise, it did take more time I feel as we need to step back and think
      about the fundamentals, especially we are both first time writers so it takes
      a lot of time to learn how to write a book as well. We got a lot of helps from
      Manning editors,
  - name: Ning Wang
    text: at the very beginning we were thinking of using a framework but it is hard
      to avoid being a reference book which is not interesting.
- name: "Philip Die\xDFner"
  text: Do you touch upon unfied batch/streaming architectures or do you think one
    can apply learnings from your book when building something like this?
  replies:
  - name: Josh Fischer
    text: We touch on both batch and streaming architectures in this book.
  - name: Ning Wang
    text: yeah we touch a little at the beginning about the architectures and then
      focus on streaming. many concepts are similar in batch.
  - name: Ning Wang
    text: "we don\u2019t touch `unfied` architectures though."
- name: Alexey Grigorev
  text: "Sometimes when a team/companies discovers the benefits of streaming, they\
    \ want to migrate all the microservices to streaming. \nDo you think it's a good\
    \ idea, and if it's not, how to push back?"
  replies:
  - name: Ning Wang
    text: 'It really depends on the use cases. Streaming systems have typical use
      cases (like processing messages stored in a pubsub system), and microservices
      have theirs too (like taking requests and then sending back responses). They
      are also not exclusive to each other, like a streaming system might rely on
      some microservices. For example, a streaming system can process message and
      write data to a k-v store which is a microservice. while streaming (and batch)
      systems are powerful, they have many limitations: complicated since there are
      more moving pieces (hence hard to maintain/optimize), microservice are (ideally)
      very staightforward and much easier to optimize. I sometimes feel each component
      in a streaming system is like a microservice, or a proxy to some microservice.'
  - name: Josh Fischer
    text: "I agree with all things Ning said, \u201Cit depends\u201D \U0001F604"
  - name: Josh Fischer
    text: Another factor to take into consider is how the data flows through a system.  For
      example, do we need that request/response model like we get with REST or  will
      we expect once we send data somewhere that something else downstream will take
      action on it?   This is a question I often find myself thinking about.
  - name: Alexey Grigorev
    text: How do I know if I need this request/response model? Often it seems that
      I do, but with a bit of redesigning it turns out that I don't
  - name: Alexey Grigorev
    text: But on the other hand, that redesign might overcomplicate things
  - name: Ning Wang
    text: Totally. Request/response model is straightforward to understand and operate,
      and this is the major reason to follow the model. Hence the model could be a
      good starting point at least for many cases. To change to (could be partially)
      streaming model, you need to have compelling reason about what you gain by the
      extra complication and make sure the ROI is reasonable/desirable. One typical
      reason might be that the process in a microservice becomes more and more complicated
      and harder to maintain, and streaming could help to break the process into multiple
      stages and make it more maintainable although the architecture is more complicated.
  - name: Josh Fischer
    text: I Agree Ning.  I think a development team should try with other traditional
      methods of moving data around request / response, batch, etc before moving to
      streaming. This way they have an understanding of their current pain points
      and a baseline to measure progress from as they make the transition to a streaming
      system
- name: Alexey Grigorev
  text: Also how to best select if I should deploy my microservice as a web service
    or as a streaming application? What are the pros and cons for each?
  replies:
  - name: Ning Wang
    text: 'My 2 cents: if it is necessary for the data to be processed in multiple
      stages, streaming system might make sense. Otherwise, microservice is likely
      to be more efficient and much more maintainable. Again, microservices and streaming
      systems are not exclusive to each other. Even when multiple stages are necessary,
      it is likely that a combination of microservices and data processing systems
      could be a better option.'
  - name: Ning Wang
    text: For example, a web server might be used to accept user data and store into
      a queue; and a data processing system can subscribe the data and process them
      to get the final results.
  - name: Josh Fischer
    text: "Again, I think this goes back to the idea of \u201Chow does the data flow\
      \ through my architecture?\u201D or \u201CIs it a one way path from start to\
      \ finish or am I expecting that  request/response handshake?\u201D"
- name: Carise Fernandez
  text: Maybe it's getting ahead of everything, but do you have suggestions for next
    books on streaming systems, after we read Grokking Streaming systems?
  replies:
  - name: Josh Fischer
    text: I would check out Pulsar in Action by David Kjerrumgard
  - name: Carise Fernandez
    text: Thank you!
- name: Carise Fernandez
  text: What's it like being an Apache committer? Do you work on it full time? Always
    have been interested in working on open source long term, but intimidated too!
  replies:
  - name: Ning Wang
    text: "It is totally different between learning something interesting and implementing\
      \ it. \U0001F642. also working on open source projects is a chance to work with\
      \ different people from very different background instead of your team mates.\
      \ Definitely not full time for me. And TBH, I am quite busy at Amplitude, and\
      \ I sadly couldn\u2019t spend enough time on Heron these days. \U0001F61E"
  - name: Josh Fischer
    text: "Working on open source had been the most fulfilling work I've done.  Heron\
      \ was my first open source project I've worked on. It's not my full time job.\
      \  I also have been involved as much as of late because if job, family, and\
      \ a startup I'm building.  \nI can see how it's intimidating, but I can promise\
      \ you that if you are willing to take the chance and do the work to solve some\
      \ problems for a community they will be greatful for your contributions.  If\
      \ you stay around long enough people will start to look at you for guidance."
  - name: Carise Fernandez
    text: Definitely a dream of mine to work on an open source project that benefits
      the software development community. I've worked on open source in the past,
      but it was not really something like a software that a community depended on.
      Thanks for sharing your experiences!
- name: Ashish Lalchandani
  text: Hello Josh Fischer and Ning Wang, thank you for being here! My question is,
    what advantages do streaming system provide while deploying ML/DL models, as compared
    to deploying them on local device and sending data to server? Let's say a company
    has face recognition model for its employees. Wouldn't it be cheaper to just deploy
    that model on local device and setup a server containing information about the
    employees, instead of using streaming system(assuming we are using AWS Lambda
    and Kinesis for streaming data) ?
  replies:
  - name: Ning Wang
    text: "Yeah, it could be cheaper to deploy data and code directly to the device.\
      \ Some potential (since it may or may not be better) benefits are: 1. the code\
      \ runs on the device is pretty simple and stable since it is only responsible\
      \ for collecting data. when there are more models/data, you don\u2019t need\
      \ to redeploy the software too often or worry about the device performance (so\
      \ the device cost could be lower when there are a lot of them). 2. you can allocate\
      \ less resource for the simple models and more for the expensive models to achieve\
      \ the performance you need, because now they don\u2019t run on the devices directly."
  - name: Ashish Lalchandani
    text: Okay, that makes sense. Thank you for clarifying!
  - name: Josh Fischer
    text: "I think Ning answered this question well \U0001F4AF"
  - name: Ashish Lalchandani
    text: Yes he did! All the best for your book Josh Fischer Ning Wang!

---

A friendly, framework-agnostic tutorial that will help you grok how streaming systems work—and how to build your own!

In Grokking Streaming Systems you will learn how to:

- Implement and troubleshoot streaming systems
- Design streaming systems for complex functionalities
- Assess parallelization requirements
- Spot networking bottlenecks and resolve back pressure
- Group data for high-performance systems
- Handle delayed events in real-time systems

Grokking Streaming Systems is a simple guide to the complex concepts behind streaming systems. This friendly and framework-agnostic tutorial teaches you how to handle real-time events, and even design and build your own streaming job that’s a perfect fit for your needs. Each new idea is carefully explained with diagrams, clear examples, and fun dialogue between perplexed personalities!