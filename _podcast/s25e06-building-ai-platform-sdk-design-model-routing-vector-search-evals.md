---
episode: 6
guests:
- suhassuresha
ids:
  anchor: datatalksclub/episodes/Building-an-AI-Platform-SDK-Design--Model-Routing--Vector-Search--Evals---Suhas-Suresha-e3q03oe
  youtube: aSI_dxt8KhY
image: images/podcast/s25e06-building-ai-platform-sdk-design-model-routing-vector-search-evals.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/Building-an-AI-Platform-SDK-Design--Model-Routing--Vector-Search--Evals---Suhas-Suresha-e3q03oe
  apple: https://podcasts.apple.com/us/podcast/building-an-ai-platform-sdk-design-model-routing/id1541710331?i=1000794297354
  spotify: https://open.spotify.com/episode/1TUi9vfXP0lhsKlH73TSjS?si=f6e2a8668afc466c
  youtube: https://www.youtube.com/watch?v=aSI_dxt8KhY
season: 25
short: 'Building an AI Platform: SDK Design, Model Routing, Vector Search & Evals'
title: 'Building an AI Platform: SDK Design, Model Routing, Vector Search & Evals'
transcript:
- header: AI Prototypes to Production and the Book Origin
- line: Hi everyone. Let us get started. I am going to skip our usual introduction
    but as always please like the video and subscribe to our YouTube channel. There
    is also a link for our Slack community where you can hang out with other data
    enthusiasts. It is actually almost 100,000 people.
  sec: 0
  time: 0:00
  who: Alexey
- line: I am really wondering who is going to be the lucky number. Right now we have
    four to go. Perhaps we have your books. Is it true that the person who is going
    to be number 100,000 is going to get a free copy of the book?
  sec: 20
  time: 0:20
  who: Alexey
- line: We can make it happen because it is really amazing. If you are not a part
    of our Slack go join it. For today's interview there is a pinned link in the live
    chat. Click on that link to ask your questions. We will be covering these questions
    during the interview.
  sec: 39
  time: 0:39
  who: Alexey
- line: That is the usual introduction. Usually I use slides for that. Now we will
    start with our interview.
  sec: 61
  time: '1:01'
  who: Alexey
- line: Today we are going to talk about building an AI platform. We will talk about
    how to go from a successful prototype to something that serves real customers.
    We have a special guest today named Suhas. He is a senior machine learning engineer
    at Adobe where he builds large scale generative AI platforms. The main reason
    we are here today is the book that he and his coauthor wrote recently.
  sec: 77
  time: '1:17'
  who: Alexey
- line: It is still in early access but it is going to be published pretty soon. All
    the content of the book is already out. All 10 chapters are available to read.
    How long did it take?
  sec: 107
  time: '1:47'
  who: Alexey
- line: We kind of did it pretty fast to be honest. It took us maybe a year and a
    half.
  sec: 125
  time: '2:05'
  who: Suhas
- line: Do you call a year and a half fast compared to what I have heard? Other folks
    write books slower I think.
  sec: 133
  time: '2:13'
  who: Alexey
- line: The bulk of our time we probably spent six months. Six months is what it really
    took. There is also this production preproduction postproduction and during production.
  sec: 144
  time: '2:24'
  who: Suhas
- line: Manning has a very rigid process. I know this because I also have a book with
    Manning. It took two years.
  sec: 157
  time: '2:37'
  who: Alexey
- line: The content was not the difficult part.
  sec: 163
  time: '2:43'
  who: Suhas
- line: Going through all the reviews and production takes time. At the end you want
    to have a book that is good quality do you not? These processes are in place to
    ensure that the book when it is published is great.
  sec: 169
  time: '2:49'
  who: Alexey
- line: That is exactly right.
  sec: 183
  time: '3:03'
  who: Suhas
- line: The book is called Designing AI Systems is it not? Tell us more about that.
  sec: 189
  time: '3:09'
  who: Alexey
- line: The inspiration for the book came about maybe a year and a half or two years
    ago. My coauthor and I were seeing that there were a lot of books on how to build
    really cool generative AI applications. People would have a lot of blog posts
    and books about it. When we had to deploy these we also built proof of concepts.
    We showed them to our bosses and everyone was super happy.
  sec: 195
  time: '3:15'
  who: Suhas
- line: When we realized we had to take these to production it was so much more work
    than that. We felt that we only spent maybe five percent or even two percent of
    the time actually working on the generative AI stuff. A lot of time was spent
    on so many engineering tasks. We felt this is actually not super easy to get out
    into production.
  sec: 228
  time: '3:48'
  who: Suhas
- line: You can get something out there into production but it is hard to ensure it
    works well and has a high accuracy. It needs to be able to maintain state across
    conversations. It also needs to be able to ground its answers in real documents
    or real data. The system must use tools safely and have the right guardrails to
    scale well. We need to be able to observe how much we are spending on all these
    different AI models.
  sec: 259
  time: '4:19'
  who: Suhas
- line: Having that observability is crucial because we realized all these features
    are not just nice to have. They really become musthaves.
  sec: 300
  time: '5:00'
  who: Suhas
- line: It takes work to take something working on your laptop as a proof of concept
    to actually serving users and doing well. Especially now when you started the
    coding agents were not that good. Now you can have a working prototype in one
    evening can you not? Is this prototype good enough for production?
  sec: 308
  time: '5:08'
  who: Alexey
- line: All of these things do get faster with coding agents. Even then sometimes
    folks do not even realize what needs to be done. That is when they fall into the
    trap of not estimating the time properly to get something out. That was one aspect
    of taking something from a demo to production. Where does the platform angle come
    in from?
  sec: 328
  time: '5:28'
  who: Suhas
- header: AI Sprawl and the Need for a Centralized AI Platform
- line: The subtitle of our book is actually a guide to building production ready
    platforms. That is a slightly adjacent thing but a very important thing as well.
    If you are just a startup of one or two people and you only have one or two AI
    applications the platform itself is not necessarily going to speak to you that
    much.
  sec: 349
  time: '5:49'
  who: Suhas
- line: If you are a decent size startup where you have at least five to ten different
    AI projects going around a platform becomes pretty valuable. Without it every
    team has to build all these other aspects I just mentioned. This includes building
    session storage and vector search. They also have to ensure they have MCP integration
    and that tool calls are done in a secure manner. Adding guardrails and other features
    becomes a lot of duplicated effort.
  sec: 388
  time: '6:28'
  who: Suhas
- line: If you are a leader in a company and you want to observe what is happening
    across a lot of AI applications it becomes very difficult if you have fragmented
    efforts. We call this AI sprawl in our book.
  sec: 429
  time: '7:09'
  who: Suhas
- line: What is AI sprawl and what does sprawl mean?
  sec: 448
  time: '7:28'
  who: Alexey
- line: Sprawl refers to things that organically happen across the organization. It
    looks fine initially but then you have too many things to consolidate together.
  sec: 455
  time: '7:35'
  who: Suhas
- line: I will give you a simple example regarding observability of AI systems. Let
    us say five different applications build observability in five different ways.
    The data model for observability is vastly different. One day the CTO wants to
    know how things are looking and someone has to reconcile all these different models
    to build a common observing board. That becomes a new block of work but the worst
    part is the consolidation.
  sec: 466
  time: '7:46'
  who: Suhas
- line: Whenever someone starts a new AI project they do not have anything to start
    off with. They have to start again which leads to more and more sprawl. Let us
    stop the sad stories and think of the ideal scenario. The magic of generative
    AI is that you get something really cool out in a day. Within a few minutes it
    is in production and you automatically get a lot of these things for free.
  sec: 502
  time: '8:22'
  who: Suhas
- line: That is the idea. A lot of the big tech companies do this really well. They
    have really good platforms which is why they are able to move really fast. I will
    give you an example. Take Perplexity for example.
  sec: 542
  time: '9:02'
  who: Suhas
- line: Are you referring to the platform?
  sec: 561
  time: '9:21'
  who: Alexey
- line: I mean the Perplexity app as well as the platform.
  sec: 567
  time: '9:27'
  who: Suhas
- line: I still have not used it but I understand what it is. It is kind of RAG on
    a very large scale is it not?
  sec: 575
  time: '9:35'
  who: Alexey
- line: Take Cursor or another coding agent you have used.
  sec: 581
  time: '9:41'
  who: Suhas
- line: I use all of them except Cursor.
  sec: 586
  time: '9:46'
  who: Alexey
- line: I am trying to think of something that is a good example.
  sec: 592
  time: '9:52'
  who: Suhas
- line: Whenever a new model comes out Anthropic announces it at ten o'clock and by
    ten five these folks have it. They have that model available immediately. I am
    pretty sure they agree in advance so they just delay their announcement after
    the official one. GitHub Copilot speaks with Anthropic so Anthropic tells them
    there is a new model.
  sec: 597
  time: '9:57'
  who: Alexey
- line: That is true but the way they have built their system makes it very easy for
    them to swap out models. When they build their model service they ensure it is
    very easy to switch providers or models. When you are starting to build out an
    application as a proof of concept you do not think of all that. You do not think
    of what happens if you just use Anthropic because you are very focused on your
    idea.
  sec: 622
  time: '10:22'
  who: Suhas
- line: Yes exactly.
  sec: 656
  time: '10:56'
  who: Alexey
- line: That is the origin of the book to be honest. We saw that nobody else was writing
    about the ninety eight percent of the work that needs to be done to take something
    to production. We thought let us write a book.
  sec: 662
  time: '11:02'
  who: Suhas
- line: It is a very good idea. While we were talking I looked up the word sprawl.
    In urban development it means the uncontrolled expansion of a city into low density
    automobile dependent surrounding countryside which increases traffic pollution
    and infrastructure costs. When I was reading this definition I imagined an organization
    where many teams start creating agents. In order to deploy these agents we need
    an evaluation harness.
  sec: 674
  time: '11:14'
  who: Alexey
- line: Each team now has its own evaluation harness. To speed up rolling out to production
    faster they start developing a platform. At the end you have fifteen or twenty
    teams that have their own thing. As a principal engineer you wonder what to do
    with this disconnected infrastructure.
  sec: 715
  time: '11:55'
  who: Alexey
- line: Some things are suboptimal here and some things are suboptimal there. You
    want to bring some sort of economy of scale by centralizing it in one place. This
    makes it easier for teams who do not necessarily have this platform yet to also
    roll this out. This is the idea is it not?
  sec: 744
  time: '12:24'
  who: Alexey
- line: That is exactly right.
  sec: 755
  time: '12:35'
  who: Suhas
- header: Definition of an AI Platform and the Build vs Buy Dilemma
- line: Once you have the platform you see all the gains. Our next discussion is how
    you build such a platform. The most common question we get is why someone should
    learn to build a new platform from scratch. There is actually a lot of really
    cool platform stuff out there like LlamaIndex.
  sec: 762
  time: '12:42'
  who: Suhas
- line: Is it a platform though? For me LlamaIndex is a library for doing RAG although
    they offer hosted solutions. Maybe what we can do first is define what a platform
    is before we decide why we should learn to build one.
  sec: 809
  time: '13:29'
  who: Alexey
- line: That is a good question. The way I define a platform is something that developers
    use to build their applications on top of. A good platform should ideally give
    you a lot of value for free. A good generative AI platform should not require
    developers to worry about most production concerns.
  sec: 837
  time: '13:57'
  who: Suhas
- line: They should not worry about how to scale their application or connect to a
    session store or a vector database. Most of these things should be taken care
    of by the platform. The only thing the developer is worried about is adding their
    business logic. They should only be able to focus on delivering their specific
    application really well.
  sec: 872
  time: '14:32'
  who: Suhas
- line: I do not know if you have used Vercel but I was amazed how easy it is. I am
    not affiliated with them but I tried it and it is so easy to create an agent there.
    You define a markdown document with instructions and another file with the definitions
    of your tools. That is basically your entire agent. With one command it gets deployed
    to a serverless environment.
  sec: 907
  time: '15:07'
  who: Alexey
- line: It gets connected automatically to this AI gateway or whatever they call it.
    It scales and you get observability and durability out of the box. I was amazed
    by how cool it is. This is an example of a platform is it not?
  sec: 937
  time: '15:37'
  who: Alexey
- line: Absolutely. You gave the best example. Vercel is fantastic and all the things
    you mentioned are exactly what we write about in the book. We explain how you
    build such a platform to get this magical experience you just spoke about. You
    are just worried about writing your application or business logic.
  sec: 957
  time: '15:57'
  who: Suhas
- line: You get everything else like an agent URL and observability automatically.
    You can define how scalable you want this application to be. All of this is essentially
    just knobs that you can control. You do not have to build any of it.
  sec: 982
  time: '16:22'
  who: Suhas
- line: If Vercel exists why do we need to even care about building a platform?
  sec: 1006
  time: '16:46'
  who: Alexey
- line: That is a great question. You can use Vercel and it is totally fine.
  sec: 1012
  time: '16:52'
  who: Suhas
- line: Except you have to tolerate JavaScript.
  sec: 1017
  time: '16:57'
  who: Alexey
- line: There are limitations. I have not used Vercel extensively so I do not know
    all the limitations. It is very TypeScript and JavaScript focused. If you want
    to get off the main track you have problems. With Python it kind of works but
    it is not the same experience.
  sec: 1020
  time: '17:00'
  who: Suhas
- line: That platform may not be applicable for exactly what you want to do. We felt
    that most of the time the right solution is to use an existing platform. I would
    not advise someone to completely build a platform from scratch especially if they
    are a solo founder.
  sec: 1045
  time: '17:25'
  who: Suhas
- line: Exactly. Do not do that.
  sec: 1065
  time: '17:45'
  who: Alexey
- line: Learning how to build a platform teaches you a lot of things. It teaches you
    what is happening behind the scenes. People like me always love to know what is
    happening behind the scenes.
  sec: 1072
  time: '17:52'
  who: Suhas
- line: That is useful because it also gives you a good understanding of which platform
    to choose. If you are choosing between two or three different vendors for a platform
    you get an idea of what you are getting from them. You understand it because you
    have essentially already built one.
  sec: 1083
  time: '18:03'
  who: Alexey
- line: If you are joining a big tech company knowing this is very important. Many
    midsize to big tech companies have very specific applications that they need to
    build. Most of them build their own platforms. You might actually be hired to
    work on the platform. In those scenarios it becomes very important for you to
    understand how to build a platform from scratch.
  sec: 1103
  time: '18:23'
  who: Suhas
- line: I remember my days working as a data scientist where we had the same story
    with machine learning platforms. Many companies were building their own platforms.
    I wondered why they would do this if there are platforms like SageMaker or Databricks.
    Why on earth would anyone start building their own platform when there are many
    providers available? The problem is integration.
  sec: 1142
  time: '19:02'
  who: Alexey
- line: You already have existing systems and you want a solution that integrates
    well with your internal ecosystem. Sometimes it is much easier to develop something
    inhouse that integrates perfectly. If you pay a vendor you often spend the same
    amount of time integrating their product as you would spend writing your own thing.
    When you build your own thing you know exactly how it works.
  sec: 1167
  time: '19:27'
  who: Alexey
- line: Of course it is a journey and it will not work perfectly on the first attempt.
    When I realized how much integration is required I concluded these teams know
    what they are doing. Sometimes there is the not invented here syndrome but I completely
    understand the technical need.
  sec: 1197
  time: '19:57'
  who: Alexey
- line: These are all tradeoffs. Sometimes you have the risk of vendor lockin and
    you cannot easily migrate. Vercel is great but if you start scaling it can become
    very expensive. It is very cheap if you have one customer but with one million
    customers it suddenly becomes costly.
  sec: 1220
  time: '20:20'
  who: Suhas
- line: Exactly. The same thing applies to lower level agentic frameworks. From what
    I see practitioners end up implementing their own frameworks. I often wonder why
    they cannot just use Pydantic AI. The reality is their requirements are so specific
    that they need to stop tool calls at an exact moment.
  sec: 1245
  time: '20:45'
  who: Alexey
- line: For them it is just easier to implement their own agentic framework rather
    than fighting LangChain or Pydantic AI to get what they need. The same applies
    to platforms does it not?
  sec: 1269
  time: '21:09'
  who: Alexey
- line: Absolutely. Even with the platforms we write about in the book we do not build
    everything from scratch. For example when we discuss the data service we do not
    build a vector store from scratch. We show an example of how to build one using
    Postgres. The idea is you can build a platform in such a way that you can easily
    swap in different providers.
  sec: 1283
  time: '21:23'
  who: Suhas
- line: This is commonly done in the industry. I have seen many platforms where you
    are building an application and need to ingest data into a vector store. The platform
    gives you options between Postgres or other databases. A platform does not require
    you to build everything from scratch. You can have different vendors plug in at
    different points of the platform.
  sec: 1325
  time: '22:05'
  who: Suhas
- line: You have to have this plug and play architecture. If you are not satisfied
    with Postgres and want to switch to Elasticsearch you just replace that component.
    The rest of the whole system remains the same.
  sec: 1367
  time: '22:47'
  who: Alexey
- line: Exactly. Or if you no longer prefer Anthropic you can switch to a different
    LLM.
  sec: 1384
  time: '23:04'
  who: Suhas
- line: For you it is just swapping one component. I understand.
  sec: 1390
  time: '23:10'
  who: Alexey
- line: That is correct.
  sec: 1395
  time: '23:15'
  who: Suhas
- header: AI Platform Engineering Skills and Data Service Architecture
- line: I understand that having a platform is good. We have a specific request from
    people in our community. Sometimes people write to me saying AI engineering seems
    interesting but they are more interested in AI platform engineering. They want
    to know what they need to do to work as an AI platform engineer. My suggestion
    is that you first need to understand what AI engineers do and then work backwards
    from there.
  sec: 1397
  time: '23:17'
  who: Alexey
- line: Since I do not have direct experience with platform engineering I want to
    ask you. What should be the path for a backend engineer who is interested in AI
    but prefers platform engineering? How do they transition to being an AI platform
    engineer and what skills do they need to acquire?
  sec: 1431
  time: '23:51'
  who: Alexey
- line: That is a great question. A lot of the book was written from exactly that
    point of view. Another question we get asked often is why someone should learn
    to build an AI platform when it seems similar to building any general software
    platform. Most of the core software concerns seem to be the same. That is where
    we identify what is completely new with generative AI and highlight the specific
    areas you need to master.
  sec: 1467
  time: '24:27'
  who: Suhas
- line: Let us say you are a backend engineer currently working on traditional software
    development and you want to shift to AI platform engineering. It is very important
    for you to first understand how these agents work. Think of the lifecycle request
    of an agent and what happens when a user sends a request. I know agents are wildly
    different in terms of harnesses but many of the underlying steps are similar.
  sec: 1503
  time: '25:03'
  who: Suhas
- line: Things like tool call loops are under the hood of any framework.
  sec: 1539
  time: '25:39'
  who: Alexey
- line: The agentic loop is a pretty standard concept. Understanding those fundamentals
    becomes very important. Once you understand that you can work backwards and identify
    all the services you need to build for a platform. We agreed initially that the
    platform should ensure developers do not have to worry about infrastructure aspects.
  sec: 1550
  time: '25:50'
  who: Suhas
- line: This includes scaling and connecting to a vector database or a model service.
    It also handles invoking services to enforce guardrails. All of these things should
    not be developer concerns.
  sec: 1590
  time: '26:30'
  who: Suhas
- line: These infrastructure components should be built by the platform. You should
    start by understanding how an agentic request flow works. Then you can work backwards
    to map out all the different services you need to build. For example you need
    to build a model service to ensure developers are free to choose between different
    model providers.
  sec: 1610
  time: '26:50'
  who: Suhas
- line: Something like LiteLLM or a similar router.
  sec: 1647
  time: '27:27'
  who: Alexey
- line: You will understand that just routing is not enough. What happens if a request
    fails from a particular provider? You need to handle failovers to ensure the system
    does not abruptly fail. The platform needs to seamlessly switch to another provider
    as part of the request flow and manage rate limits. There are many operational
    concerns to address when you want to take an application to production.
  sec: 1654
  time: '27:34'
  who: Suhas
- line: Let us take the data service as an example. You need to understand how vector
    search works end to end. When you see tutorials on vector search people usually
    just explain the basic concept. I will tell you what most people actually end
    up spending their time on. A major part of vector search involves adding a step
    to identify the format of the ingested documents.
  sec: 1692
  time: '28:12'
  who: Suhas
- line: These documents may be PDFs or Word files or Excel sheets. Identifying the
    format and adding specific parsers to extract the content takes a lot of time.
    There are a lot of nuances involved in parsing. Extracting content from a PDF
    is notoriously difficult because they contain complex layouts like tables.
  sec: 1734
  time: '28:54'
  who: Suhas
- line: Sometimes all the text is in one block and other times it is split across
    paragraphs. It is incredibly difficult to extract text and ensure that it reads
    correctly.
  sec: 1766
  time: '29:26'
  who: Suhas
- line: Then you have to manage chunking strategies. You have to ensure you provide
    options so developers can mix and match different chunking strategies for their
    application. If they want to add their own specific logic you must provide a way
    for them to register a new chunking strategy. The platform also needs an interface
    where you can plug in any vector database like Pinecone or Elasticsearch or Postgres.
  sec: 1783
  time: '29:43'
  who: Suhas
- line: The ultimate goal is building an interface where the developer only writes
    one or two lines of code. They just pass the user query to the vector search component.
    The result is a fully prepared tool that the agent can call immediately.
  sec: 1826
  time: '30:26'
  who: Suhas
- line: It can be registered as a tool in some applications. If you know you are doing
    RAG every time it becomes a mandatory step that happens even without the model
    explicitly invoking that tool. How you build it is very application specific.
    The platform should essentially enable developers to do either of these approaches
    seamlessly.
  sec: 1852
  time: '30:52'
  who: Alexey
- line: Let us think of AI observability next.
  sec: 1877
  time: '31:17'
  who: Suhas
- line: I want to do a quick recap first. We are trying to understand the core abstractions
    needed for a generative AI application. The first thing is the model service which
    handles failures and rate limiting and provider switching. That acts as our router.
    The second component is the data service which handles data ingestion and makes
    context easily available for your application as a tool or a mandatory RAG step.
  sec: 1886
  time: '31:26'
  who: Alexey
- header: System Observability and Request Flow Bottlenecks
- line: We spent so much time discussing just those two components. Now you are touching
    on observability which is the third component.
  sec: 1946
  time: '32:26'
  who: Alexey
- line: The model service is a completely new concept for these applications. Vector
    search is not a new concept but many new nuances have come into the picture. You
    have to ensure that the search results are well integrated into the final prompt.
    You cannot stop at just retrieving the relevant documents. You also have to understand
    how to format and insert those chunks correctly into the context window of the
    LLM.
  sec: 1954
  time: '32:34'
  who: Suhas
- line: With observability most of the concepts are the same as traditional software.
    In a distributed system you want to understand how much time each component spends
    during a request lifecycle. For example consider a RAG flow where a user sends
    a request. You send that query to the data service which performs a vector search
    to fetch the relevant documents. You then add those documents into your model
    context and make a call to the LLM.
  sec: 2000
  time: '33:20'
  who: Suhas
- line: The LLM processes the user question alongside your system prompt and the retrieved
    grounding context. It uses this information to generate an answer grounded in
    reality. In this case you need to know exactly how much time was spent in the
    data service and the model service. Let us say you also add guardrails to ensure
    you do not leak personally identifiable information or company secrets. You might
    use a smaller model to check the final answer and you need to track how much time
    that security check takes.
  sec: 2047
  time: '34:07'
  who: Suhas
- line: You want a complete view of the time spent across these different components
    for every request. You need this data as an aggregate across all requests. If
    your boss asks you to optimize latency from an average of two seconds to under
    one second you can pinpoint exactly where to optimize. If the bottleneck is the
    model service you might look at using a smaller LLM.
  sec: 2105
  time: '35:05'
  who: Suhas
- line: You can clearly identify the bottleneck because RAG steps are strictly sequential.
    You can see if you spent one second in one place and twenty milliseconds in another.
    If the data service is the bottleneck you know exactly where to focus your optimization
    efforts.
  sec: 2147
  time: '35:47'
  who: Alexey
- line: That is exactly right. These observability tools become even more important
    with agentic loops. Coding agents can go into a loop for thirty minutes continuously
    executing tool calls until they are satisfied with the answer.
  sec: 2161
  time: '36:01'
  who: Suhas
- line: They do not stop and will keep calling as many tools as necessary. Observability
    lets you analyze how many times a specific tool was invoked during a single query.
    You can identify which tools are taking the most time to execute. This data feeds
    directly back into your optimization strategy. If a useful tool takes a minute
    to execute and the model calls it twenty times you clearly need to optimize it.
  sec: 2179
  time: '36:19'
  who: Suhas
- line: You might rewrite the tool description or change how it performs completely.
    Observability becomes extremely key in generative AI systems. That is why understanding
    the request flow of an actual agent is so important. Once you understand the flow
    you know exactly what infrastructure you need to build.
  sec: 2220
  time: '37:00'
  who: Suhas
- header: LLM Evaluations, Prompt Experimentation, and Cost Tracking
- line: There are a couple of questions from the audience that I will get back to
    later. I want to finish mapping out the essential pieces of the platform first.
  sec: 2252
  time: '37:32'
  who: Alexey
- line: We want a complete understanding of what components this platform requires.
    So far we have covered the model service and data service and guardrails and observability.
    Observability allows you to trace the request flow and understand exactly how
    much time is spent at each step. What else is important to include in our architecture?
    I think we previously mentioned evaluation and durability.
  sec: 2265
  time: '37:45'
  who: Alexey
- line: Let us discuss evaluation next because it is closely tied to observability.
    Typical software systems are very deterministic so your failure rates are based
    on standard HTTP status codes. As long as you get a successful response code you
    assume the service is functioning well. That is not true for AI applications because
    you might deploy a chatbot that is totally useless. It might be working perfectly
    from a traditional software engineering perspective with zero failure rates.
  sec: 2301
  time: '38:21'
  who: Suhas
- line: It just constantly recommends the user go read the documentation instead of
    actually helping.
  sec: 2341
  time: '39:01'
  who: Alexey
- line: Exactly.
  sec: 2347
  time: '39:07'
  who: Suhas
- line: If it does not actually help the user then it cannot be considered a success.
    That is where AI evaluations become critical. It is very important to sample a
    percentage of your production requests. You should evaluate those samples using
    either automated or human scorers.
  sec: 2347
  time: '39:07'
  who: Suhas
- line: Because we have observability we already collect these system traces. Once
    we have these traces we can run them through a system to determine if we actually
    achieved the goal of the request. We can evaluate if the model genuinely helped
    the user. We can sample thousands of logs to get an accurate idea of how good
    the system actually is.
  sec: 2378
  time: '39:38'
  who: Alexey
- line: Exactly.
  sec: 2407
  time: '40:07'
  who: Suhas
- line: That data feeds directly back into experimentation because evaluation and
    experimentation are fundamentally linked. You analyze the failure data to create
    a feedback loop for whatever you need to change. If you feel the model is underperforming
    you might switch to a different provider. You might decide to completely change
    your orchestration harness.
  sec: 2414
  time: '40:14'
  who: Suhas
- line: For example you might discover that running the data service before the model
    even calls any tools improves performance. You can clearly see the tradeoffs because
    adding certain steps might increase latency while boosting user satisfaction.
    The final angle to consider here is operational cost.
  sec: 2446
  time: '40:46'
  who: Suhas
- line: Cost tracking is tied directly into the observability platform. This is where
    we measure expenses because the majority of the cost happens in the model service.
  sec: 2478
  time: '41:18'
  who: Alexey
- line: There is also cost associated with vector search operations. Many developers
    use local embedding models where they only pay for raw compute power. A lot of
    companies also offer managed embedding models as a service.
  sec: 2490
  time: '41:30'
  who: Suhas
- line: Cloudflare has a service called Vectorize where you pay per request. It is
    very convenient but eventually at scale you are paying for every transaction instead
    of just compute. Different guardrails also contribute to the overall cost so you
    have to sum everything up.
  sec: 2510
  time: '41:50'
  who: Alexey
- line: You have to aggregate all those expenses and add them to your tradeoff matrix.
    If you optimize entirely for cost you have to make sacrifices in performance or
    latency.
  sec: 2535
  time: '42:15'
  who: Suhas
- line: I want to speed things up a bit to ensure we have time for questions. You
    mentioned experimentation as another core component of the platform. We need tools
    to compare Model A and Model B in production. What else does the platform need?
  sec: 2554
  time: '42:34'
  who: Alexey
- line: I would not just call it Model A and Model B because the model itself is rarely
    the only variable. These days the variables include the model and the system prompt
    and the tool definitions.
  sec: 2572
  time: '42:52'
  who: Suhas
- line: We should call it Version A and Version B.
  sec: 2584
  time: '43:04'
  who: Alexey
- line: We use the term artifact to describe the complete combination of the harness
    and tools.
  sec: 2590
  time: '43:10'
  who: Suhas
- line: It includes all the orchestration logic plus the model itself.
  sec: 2597
  time: '43:17'
  who: Alexey
- header: Session Memory, Tool Registries, and Agent Orchestration
- line: You should treat that complete bundle as versioned code. It is critical to
    know that a specific combination of the harness and prompt yields a specific performance
    metric. When you introduce variations you can version them and trace the exact
    impact on accuracy and latency. The platform should provide this infrastructure
    so teams can experiment rapidly without relying on local files.
  sec: 2637
  time: '43:57'
  who: Suhas
- line: What else should we have in the platform?
  sec: 2644
  time: '44:04'
  who: Alexey
- line: The next important component is session and memory management.
  sec: 2649
  time: '44:09'
  who: Suhas
- line: One of the audience questions actually asks how to manage short term and long
    term memory for the application. This memory management is exactly what we are
    discussing. Why do we even need it?
  sec: 2655
  time: '44:15'
  who: Alexey
- line: The simplest explanation is that large language models are completely stateless.
    Every time you send a request you have to pass in all the context required for
    the model to answer correctly. The model does not retain memory on its own so
    you have to build that infrastructure. Think of standard chat applications where
    you maintain multiple active sessions simultaneously. The simplest requirement
    is ensuring the model remembers previous turns within a single conversation session.
  sec: 2673
  time: '44:33'
  who: Suhas
- line: That handles the short term memory requirements.
  sec: 2721
  time: '45:21'
  who: Alexey
- line: The second requirement is building a cross session understanding of the user.
    Developers often implement a RAG pipeline across a user's historical sessions.
    You see this when you ask a question and the system searches across all your previous
    chats. The platform is continuously indexing all the various conversations you
    have had. When you ask a new query it performs a vector search on that index to
    fetch relevant historical context.
  sec: 2728
  time: '45:28'
  who: Suhas
- line: Sometimes when I use coding agents to write documentation they spontaneously
    decide to write tests for that documentation. I have to correct them and tell
    them tests are not needed. The agent then creates a long term memory stating it
    should not write tests for documentation and saves it for the project.
  sec: 2771
  time: '46:11'
  who: Alexey
- line: That is exactly the third concept I was getting to.
  sec: 2796
  time: '46:36'
  who: Suhas
- line: We call this concept model managed memory. You offer long term memory as a
    standard tool and the model itself decides when to invoke it. This saved memory
    is then automatically appended to the context window on every subsequent turn.
  sec: 2801
  time: '46:41'
  who: Suhas
- line: You obviously still need traditional session management to run cross session
    searches. What else do we need in the platform?
  sec: 2820
  time: '47:00'
  who: Alexey
- line: We absolutely need a dedicated tool service. Agents and tools go hand in hand
    because the execution loop is what actually defines an agent. You need a centralized
    tool registry and automatic tool discovery. The platform must also guarantee the
    safe execution of these registered tools.
  sec: 2831
  time: '47:11'
  who: Suhas
- line: There are many new protocols available today like the Model Context Protocol.
    You have to ensure that developers can easily add MCP tools to the platform. A
    dedicated tool service becomes incredibly important for managing all these integrations.
  sec: 2864
  time: '47:44'
  who: Suhas
- line: Tool usage is another direct contribution to the overall cost. If we use an
    external MCP server that costs money we need to track it through the observability
    pipeline.
  sec: 2890
  time: '48:10'
  who: Alexey
- line: We already covered guardrails briefly earlier in the discussion. Developers
    must be able to write custom guardrail policies that the platform automatically
    enforces.
  sec: 2897
  time: '48:17'
  who: Suhas
- line: Should the orchestration harness itself be a core part of the platform?
  sec: 2916
  time: '48:36'
  who: Alexey
- line: What exactly is a harness? Is it the same as a framework like LangChain?
  sec: 2924
  time: '48:44'
  who: Alexey
- line: For an agent the harness is anything built outside the core model call. Everything
    wrapping the model is basically the orchestration harness that makes the agent
    useful. The standard agentic loop is a perfect example of a harness. Not every
    application actually requires an open ended tool loop.
  sec: 2931
  time: '48:51'
  who: Suhas
- line: There are tons of applications that use a simple directed acyclic graph approach.
    You know exactly what sequential steps the AI needs to execute so you just fix
    those steps in place. That fixed pipeline becomes a very simple harness.
  sec: 2957
  time: '49:17'
  who: Suhas
- line: The platform should let developers build these distinct workflows seamlessly.
    Automation tools like n8n let you define a strict sequence of execution steps.
    That fixed sequence represents the DAG approach. This is fundamentally different
    from giving an agent access to tools and letting it decide what to call.
  sec: 2976
  time: '49:36'
  who: Alexey
- line: There are many different ways of building orchestration. In our book we demonstrate
    writing a custom agentic loop in just fifty lines of Python code. What makes that
    simple harness scalable is the underlying platform infrastructure. When the code
    calls the model service the platform completely abstracts away the complexity.
  sec: 3000
  time: '50:00'
  who: Suhas
- line: It automatically handles provider failovers and dynamic request routing invisibly.
    You can write and optimize the core harness logic yourself. You still get the
    full power of the platform handling the heavy infrastructure lifting for free.
  sec: 3025
  time: '50:25'
  who: Suhas
- header: Invocation Modes and Durable Execution for AI Agents
- line: That explains why Vercel lets you define your prompt as a markdown document
    and your tools as JavaScript files. The complex orchestration is already built
    directly into the platform.
  sec: 3056
  time: '50:56'
  who: Alexey
- line: The platform also needs to offer different invocation modes for the deployed
    agents.
  sec: 3062
  time: '51:02'
  who: Suhas
- line: We define three distinct invocation modes for different use cases. Traditional
    software applications execute processing and return the final result synchronously.
    That synchronous mode is still valuable for fast classification tasks. If you
    are building a chatbot you cannot force the user to wait for the entire response
    to generate. The platform absolutely needs to support native streaming outputs.
  sec: 3069
  time: '51:09'
  who: Suhas
- line: The third mode is asynchronous execution which is crucial for deep research
    tasks. If you use advanced models for deep research they do not return an answer
    immediately. The system tells you to check back in ten minutes while it works
    in the background. The user application simply polls the server to check the status
    of the long running task. The agent handles whatever complex execution is required
    to generate a satisfactory answer in the background.
  sec: 3110
  time: '51:50'
  who: Suhas
- line: You mentioned three modes so the first one is streaming and the second is
    asynchronous polling. Are those the three modes?
  sec: 3158
  time: '52:38'
  who: Alexey
- line: The three modes are synchronous and asynchronous and streaming.
  sec: 3169
  time: '52:49'
  who: Suhas
- line: By synchronous you mean standard request and response architecture.
  sec: 3174
  time: '52:54'
  who: Alexey
- line: With synchronous execution the user sends a request and waits for the agent
    to compute the full answer before returning it. With streaming the user progressively
    receives tokens without waiting for the complete generation. In asynchronous mode
    the user makes a request and immediately receives a polling URL. The system tells
    the client to keep checking that URL while the agent works in the background.
  sec: 3174
  time: '52:54'
  who: Suhas
- line: I think there is also a fourth one like a batch execution mode.
  sec: 3222
  time: '53:42'
  who: Alexey
- line: Batch execution is crucial for running massive evaluations or processing complex
    document ingestion pipelines.
  sec: 3229
  time: '53:49'
  who: Suhas
- line: Where does durable execution belong in this architecture? Is it a completely
    separate component?
  sec: 3243
  time: '54:03'
  who: Alexey
- line: Durable execution is something that needs to be built directly into the orchestrator.
  sec: 3258
  time: '54:18'
  who: Suhas
- line: Durable execution is the ability to pause and continue execution after an
    interruption. If you need approval from the user or a data center catches on fire
    you want the execution to safely resume elsewhere. I assume that functionality
    is fundamentally tied to session management and orchestration.
  sec: 3270
  time: '54:30'
  who: Alexey
- line: Durability should actually be built into all the services across the platform.
    If something fails at the model service layer you need automatic retries and failovers
    managed there. If a failure happens at the orchestration layer the gateway itself
    needs the ability to safely retry the user request. The reliability of a platform
    is not localized to just one single stage. It is a core architectural requirement
    that spans all the services we are discussing.
  sec: 3295
  time: '54:55'
  who: Suhas
- line: I have listed the model service and data service and observability and guardrails
    and evaluation. I also have experimentation and session management and the tool
    service and the orchestrator. Is there something missing from this architecture?
  sec: 3346
  time: '55:46'
  who: Alexey
- line: That is a very comprehensive list of nine distinct components. You can build
    ninety nine percent of your applications using just these systems.
  sec: 3368
  time: '56:08'
  who: Suhas
- header: The Nine Core AI Platform Components and Memory Management
- line: A simple proof of concept is just defining the prompt and the tool calls in
    one evening. All these other infrastructure components still need to happen before
    production deployment. A truly good platform abstracts all this complexity away
    entirely. It allows us to take an application developed in one evening straight
    to production with minimal friction. That is the ultimate goal of building this
    platform.
  sec: 3374
  time: '56:14'
  who: Alexey
- line: That is exactly right.
  sec: 3418
  time: '56:58'
  who: Suhas
- line: We need to wrap up soon but I want to answer an audience question regarding
    memory management. The question asks if memory is mandatory for all agents and
    why it should be treated as a separate architectural service.
  sec: 3423
  time: '57:03'
  who: Alexey
- line: If you are running a coding agent locally you can simply save memory as local
    files on your laptop. If you are building an enterprise application serving tens
    of thousands of users from remote servers you need a robust persistent store.
    You have to connect your agents to a production database like Postgres or MongoDB
    to store those conversations securely.
  sec: 3455
  time: '57:35'
  who: Suhas
- line: The application developer needs a standardized abstraction to read and write
    to those databases seamlessly. Handling persistent state safely across thousands
    of concurrent users is a major production concern. That is exactly why you need
    a dedicated session service handling the infrastructure layer.
  sec: 3499
  time: '58:19'
  who: Suhas
- line: I can add that some applications completely lack the need for memory. It is
    highly use case dependent so I would not consider it a mandatory architectural
    step for every single agent.
  sec: 3532
  time: '58:52'
  who: Alexey
- line: That is absolutely correct.
  sec: 3545
  time: '59:05'
  who: Suhas
- line: I have to run now so I want to thank you for joining us today and sharing
    your experience. We are going to raffle off a few copies of the book to people
    who signed up for this event. The lucky person who becomes member one hundred
    thousand in our community is also going to get a copy.
  sec: 3552
  time: '59:12'
  who: Alexey
- line: We are going to invite your coauthor for an interview soon to answer the remaining
    audience questions we missed today. Thank you everyone for joining this excellent
    discussion.
  sec: 3588
  time: '59:48'
  who: Alexey
- line: Thank you Alexey and I hope everyone has a great rest of the day. I am going
    to jump to another meeting that I am already late for.
  sec: 3617
  time: '1:00:17'
  who: Suhas
---

Links:

* [Book](https://www.manning.com/books/designing-ai-systems){:target="_blank"}
* [Code](https://github.com/designing-ai-systems/designing_ai_systems_repo){:target="_blank"}
* [LinkedIn](https://www.linkedin.com/in/suhas-suresha/){:target="_blank"}
* [Twitter](https://x.com/inceptor92){:target="_blank"}
* [Github](https://github.com/suhas1992){:target="_blank"}
* [Website](https://suhassuresha.com/){:target="_blank"}