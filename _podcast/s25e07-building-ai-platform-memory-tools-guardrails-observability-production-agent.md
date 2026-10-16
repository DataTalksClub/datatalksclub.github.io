---
episode: 7
season: 25
guests:
- dewangsultania
ids:
  youtube: T1R-IfYrRFY
image: images/podcast/s25e07-building-ai-platform-memory-tools-guardrails-observability-production-agent.jpg
links:
  spotify: https://open.spotify.com/episode/6KBRD5TGLggGuPFvvXGPyR
  youtube: https://www.youtube.com/watch?v=T1R-IfYrRFY
short: 'Building an AI Platform: Memory, Tools, Guardrails, Observability & Shipping a Production Agent'
title: 'Building an AI Platform: Memory, Tools, Guardrails, Observability & Shipping a Production Agent'
description: 'Dewang Sultania discusses session memory, tools and MCP, guardrails, observability, and deploying production AI agents.'
transcript:
- header: "Dewang’s career and Designing AI Systems"
- line: |-
    It's a big pleasure to have you here, Dewang. I want to start by discussing
    your career journey. The topic today is building AI systems and an AI
    platform, but it's also interesting how you ended up writing a book.

    What led you to do this? What has your career been so far, and what are you
    doing now?
  sec: 49
  time: "0:49"
  who: Alexey
- line: |-
    Sure. I'm Dewang. I've been in the industry for around six to seven years.

    I spent five years at Adobe, and now I'm an ML engineer at Netflix, mainly
    working on multimodal AI and deploying machine learning models to
    production. At Adobe, I started in the inference platform team. This was
    before a lot of the huge inference platforms we know today, like Bedrock or
    SageMaker.

    Companies were building internal tools to serve their AI models. That was
    the start of my career. Then I worked a bit on search, and now I'm at
    Netflix working on media ML.

    Before that, I did my master's in computer science at UPenn.
  sec: 75
  time: "1:15"
  who: Dewang
- line: |-
    Regarding the book, since around 2023, when LLMs started getting popular and
    people started building applications on top of them, we were seeing a
    consistent pattern. Getting from a problem statement to a prototype was
    getting easier, but building that prototype into a production service with
    reliable outputs every time, and figuring out how different engineering
    systems could talk to it, was getting harder. There were new patterns you
    had to learn that often didn't apply to traditional ML.

    We thought there were a lot of books about building applications using these
    models, but what about everything around them? How do you connect tools to
    your models reliably? MCPs became a thing.

    What's the advantage of MCP over normal tool calling? These were questions a
    lot of people had.
  sec: 125
  time: "2:05"
  who: Dewang
- line: |-
    We saw a bunch of great blog posts about it, but we felt there was a gap
    that required a book to talk about these things.
  sec: 188
  time: "3:08"
  who: Dewang
- line: |-
    I'm taking notes because there are some things we didn't discuss last week.
    I have this piece of paper with my notes from the previous session. Luckily,
    I didn't throw it away.

    I want to quickly recap what we discussed, because Amar asks whether they
    should watch the first session before attending this one. No, I'll do a
    quick recap, and after this chat you can go and watch it.
  sec: 195
  time: "3:15"
  who: Alexey
- header: "AI platform components and orchestration"
- line: |-
    We talked mainly about building an AI platform and its components. First is
    the model service, or request router: you send a request and get the
    response with the generation from the LLM. Second is the data service, your
    vector search or whatever search you use, which gives you the data.

    Then you have the observability component to know how quickly your system
    works, how well it's performing and what it costs.
  sec: 225
  time: "3:45"
  who: Alexey
- line: |-
    Then we have guardrails, small LLMs you can add in front of your agents or
    LLMs. Perhaps these can be reused across all your applications. Next is
    evaluation: how you evaluate the model, the evaluation harness, and how you
    collect the data for it.

    Then experimentation, which is A/B testing in a way. We talked about session
    and memory management. Then there's a tool service: how do you register a
    tool so all the agents in the organization can use it, if they're
    authorized?

    I think we also talked about the orchestrator.
  sec: 267
  time: "4:27"
  who: Alexey
- line: |-
    I'm not sure whether it's part of the platform, but the orchestrator makes
    and executes these tool calls. Those are the things we talked about. That
    was very brief; if you want details, you can check the previous session.

    Did I miss anything? I think it was a pretty comprehensive list. So we've
    finished the interview?

    Did I miss anything, or is there something in that list you want to mention?
  sec: 329
  time: "5:29"
  who: Alexey
- line: |-
    Perhaps we briefly mentioned something, but you want to say it's a super
    important part.
  sec: 373
  time: "6:13"
  who: Alexey
- line: |-
    Definitely. I would say all the platform components are important, but if I
    were a team starting on day zero, the first thing would probably be the
    model service. That's the heart of everything we've built around it.

    You need LLM inputs and outputs to make sense of every other platform
    component. If you want a session service, there needs to be a model you're
    interacting with. You're storing the chat history and making sure the LLM
    has access to the right prompts or context when you're
  sec: 379
  time: "6:19"
  who: Dewang
- line: |-
    sending the inputs and outputs to it. The model service is at the heart of
    everything. The session service is very important for building the context
    around the model: what parts of the chat history should the model access in
    this conversation at this moment?

    What tools and other things should come into it? You touched on an
    interesting point when you said you weren't sure whether the workflow
    service or orchestrator is part of the platform. I would say it very much
    is.

    I'd love to discuss why you thought otherwise.
  sec: 417
  time: "6:57"
  who: Dewang
- line: |-
    It's the component that ties everything together. It's the interface where
    people can orchestrate things, such as getting data from the session at a
    particular moment. With simple decorators or a simple SDK, it lets people
    connect the different components we're discussing to build a comprehensive
    application.

    It's more of the user-facing layer of the platform that lets you build
    things in a standardized way.
  sec: 455
  time: "7:35"
  who: Dewang
- line: |-
    Maybe we can start with that, since you wondered why I thought it wouldn't
    be part of the platform. We're talking about the ReAct loop, the
    tool-calling loop. Typically we use a framework like Pydantic AI, my
    favorite, or LangChain.

    There are many of these frameworks. You have a while loop and execute it
    until the model has no tool calls. That's the gist of the orchestrator.

    Perhaps there are other things, such as detecting loops if something keeps
    going...
  sec: 484
  time: "8:04"
  who: Alexey
- line: |-
    Infinite loops, yes.
  sec: 529
  time: "8:49"
  who: Dewang
- line: |-
    There are a bunch of things like that, but many frameworks already solve
    this problem. If we talk about the orchestrator as part of a platform, does
    that mean we come up with our own library and don't use Pydantic AI? Or can
    we build around Pydantic AI to add extra things?
  sec: 531
  time: "8:51"
  who: Alexey
- line: |-
    I think it's the classic build-versus-buy situation. Larger enterprises tend
    to build to avoid vendor lock-in and other things. But for your first
    application or first few applications, buying makes more sense.

    Even at larger enterprises, there are often abstractions built around
    Pydantic AI, LangGraph or something similar for orchestration. The
    workflow-service chapter we wrote was more about understanding what happens
    behind the scenes when you use Pydantic AI, LangChain or LangGraph. We feel
    that understanding this lets you evaluate different vendors and see what
    works best for your use cases,
  sec: 556
  time: "9:16"
  who: Dewang
- line: |-
    especially in platform teams.
  sec: 605
  time: "10:05"
  who: Dewang
- line: |-
    In general, if you want to be an AI engineer, you can get LangChain and it
    will do everything, but I think it's very important to implement this at
    least once to understand the flow. You realize it's not one request you
    send, but many. How does the model decide on the tool calls?

    You need to invoke those things. Implementing this by hand is something I
    think any AI engineer should do at least once.
  sec: 607
  time: "10:07"
  who: Alexey
- line: |-
    I agree. Even if you're part of a platform team at a large enterprise, you
    might have twenty different companies selling you similar things. That
    knowledge helps you evaluate them based on your company's use cases and
    choose the right tool.

    It's very important.
  sec: 641
  time: "10:41"
  who: Dewang
- line: |-
    I'm looking at the topic for this interview: building an AI platform,
    memory, tools, guardrails, observability and shipping a production agent.
  sec: 668
  time: "11:08"
  who: Alexey
- header: "Becoming an AI platform engineer"
- line: |-
    There was something I didn't get a chance to ask last time, and some
    questions we left unanswered, so maybe we can pivot a bit. I still want to
    cover some of those things. As somebody running the community, multiple
    communities actually, people come to me and say they want to become an AI
    platform engineer.

    It's becoming a thing, and people are interested. We only briefly discussed
    this
  sec: 680
  time: "11:20"
  who: Alexey
- line: |-
    concept of an AI platform engineer. We have platform engineers and ML
    platform engineers. Their job is to build a platform for developers or ML
    engineers, for somebody who needs to quickly roll something out into
    production.

    If I want to become an AI platform engineer, what should I do? Should I
    become an AI engineer first and then go into platforms, or can I start with
    platform engineering immediately?
  sec: 716
  time: "11:56"
  who: Alexey
- line: |-
    That's a great question, and I might not do it complete justice because it's
    such a changing field and requirements change every day. I'd say look at
    what popular platforms are doing. Take Bedrock, an LLM platform from AWS.

    What tools does it provide? It provides a data service, a way to handle
    sessions, track costs, observability and guardrails. These aren't things
    unique to LLM applications; they've always been there.

    It's just that, with LLMs, the problems you face as a guardrails engineer or
    someone building guardrails have become worse over time. There are incidents
    where agents break out of the system. Leaked credentials could cause more
    harm today than three or four years ago,
  sec: 754
  time: "12:34"
  who: Dewang
- line: |-
    because agents can worsen the problem by using those credentials or acting
    on your behalf without you knowing. Think of everything but the LLM as the
    role of an AI platform engineer. How do you serve it?

    How do you track costs? Try building applications with Claude or OpenAI at
    the heart, and see which common components belong to different applications.
    If I were building Claude Code, I'd need a way to manage the user's session
    and a way for people to select the right model for a task, or select it
    automatically.

    I'd need to
  sec: 818
  time: "13:38"
  who: Dewang
- line: |-
    store chat history in a scalable way. Think of millions of users. Databases
    and other things solved these problems before LLMs.

    I don't think you necessarily need to start specifically as an AI platform
    engineer. A lot of platform engineering translates very well into AI. You
    need to learn the nuances of the LLM world, where things can go more wrong
    than in traditional engineering.
  sec: 867
  time: "14:27"
  who: Dewang
- line: |-
    Interesting. I give a similar response when people ask how to become an AI
    engineer: first become an engineer, then add a bit of AI. From your answer,
    AI platform engineering is similar.

    First learn platform engineering, then add the AI specifics to the skills
    you already have as a platform engineer.
  sec: 907
  time: "15:07"
  who: Alexey
- line: |-
    Yes.
  sec: 938
  time: "15:38"
  who: Dewang
- line: |-
    When people ask me about AI platform engineering, I haven't been exposed to
    this role, so my suggestion is to build a few AI engineering projects first.
    Develop an agent that does something; develop RAG. Then try to host them and
    see what the common components are.

    Continue building applications, perhaps five in the end, and try to make
    adding each next one very smooth. That was my suggestion. It made sense to
    me because it's what I did when I was in charge of building a machine
    learning platform.
  sec: 943
  time: "15:43"
  who: Alexey
- line: |-
    Do you agree? I see you're nodding, so it looks like a good approach. You
    mentioned looking at existing platforms such as Bedrock, which makes a lot
    of sense, and I hadn't thought of it.

    Is there anything else people can do? Can they skip building five, six or
    seven agents and jump directly into platform engineering?
  sec: 988
  time: "16:28"
  who: Alexey
- line: |-
    I'd say no. It's very helpful to build applications and see what the common
    components are. I'm a big believer in learning by doing; I like that
    approach because you'd appreciate the problems your customers face.

    Tools are a common thing that probably all five agents use. How do you make
    that secure and scalable? Registering tools, calling them in a sandbox
    environment and executing them safely are common problems all your
    applications would have.

    Building them helps.
  sec: 1015
  time: "16:55"
  who: Dewang
- line: |-
    Apart from our books, there are other books, such as those by Chip Huyen,
    who was a great inspiration when we wrote our book on AI platform
    engineering. Read those and try to understand what common components they're
    building. A lot eventually boil down to a few components: sessions, data,
    tools, guardrails and observability.

    Once you've built examples around them, using other platforms or building
    them yourself, you'd have a good understanding of platform engineering and
    what it entails.
  sec: 1062
  time: "17:42"
  who: Dewang
- header: "Session management and memory"
- line: |-
    You mentioned session and memory management three or four times. From what
    you describe, session management is very important. But we talked more about
    memory management in the last interview.

    Maybe we can discuss session management a bit more. Does it make sense to
    combine them, or are they two completely separate things?
  sec: 1106
  time: "18:26"
  who: Alexey
- line: |-
    Memory management can be thought of as what your LLM is doing within your
    session. If the session has become very long, what short-term and long-term
    things do you want the model to remember about you as an individual? Session
    management, for me, is more at the enterprise level.

    OpenAI might have to handle thousands of sessions across multiple users. How
    does it do that effectively? When you log into the OpenAI or Claude app, it
    can load your chats and store things across different chats.

    You can see that you've had a hundred conversations and go into a particular
    session.
  sec: 1138
  time: "18:58"
  who: Dewang
- line: |-
    Memory is something it might have learned about you across sessions. There's
    long-term memory, and what you were talking about within a session is part
    of memory too. I might have uploaded my book's PDF and talked about it, so
    it knows that in this session I'm trying to learn about AI platform
    engineering.

    I could have a different session about baking a cake, which is completely
    different.
  sec: 1186
  time: "19:46"
  who: Dewang
- line: |-
    Memory is what it would remember about you across those two sessions: this
    person is an...
  sec: 1215
  time: "20:15"
  who: Dewang
- line: |-
    Long-term memory.
  sec: 1223
  time: "20:23"
  who: Alexey
- line: |-
    Long-term memory, yes. An engineer who likes to bake. But the baking session
    would mostly be about the process of baking the cake or cookie.
  sec: 1224
  time: "20:24"
  who: Dewang
- line: |-
    Using the ChatGPT example, if I start a conversation on my phone and
    continue it on my computer, that's possible because of session management?
    The session doesn't live on my phone; it lives somewhere on OpenAI's
    servers. Memory management is all the facts ChatGPT remembers about me.

    In my case, I turn it off because I don't like it, but sometimes it's
    convenient. I might say I live in Berlin, my name is Alexey, I'm thirty-six,
    or whatever—those things I mention
  sec: 1234
  time: "20:34"
  who: Alexey
- line: |-
    when I talk about something. If I have a Windows computer, that could be
    important in some conversations. It might say, 'You have Windows, so I
    shouldn't suggest this tool; I'll suggest that one.'
  sec: 1274
  time: "21:14"
  who: Alexey
- line: |-
    Exactly. Nicely put.
  sec: 1289
  time: "21:29"
  who: Dewang
- header: "Getting teams to contribute evaluation data"
- line: |-
    Let's take questions; we have about ten. Last time we didn't have much time
    to answer them. The first question, from Tommy, is: how can I build a
    good-quality data set for evals in a company where nobody is interested in
    contributing?
  sec: 1292
  time: "21:32"
  who: Alexey
- line: |-
    That probably touched a few nerves. It's a great question, Tommy. Evals are
    the most important thing for an application, because without them you won't
    know how well you're doing tomorrow compared with today.

    Maybe that's the pitch people who understand their importance need to make.
    It's easy to build a prototype and show it works for five or ten queries.
    Imagine deploying it in production.

    Users will send all kinds of queries, and you need to know how the model
    responds. Build those back into the system. Whether you're improving the
    prompt, adding a tool or fine-tuning the model, without a proper eval set
    it's impossible to know whether you're taking the application in the right
    direction.
  sec: 1319
  time: "21:59"
  who: Dewang
- line: |-
    You could be improving for some user queries but getting worse for a
    different cohort of users. Your eval set needs to represent your users and
    have a comprehensive set of things you run. I think of evals as a CI/CD
    system for my model.

    Every failure in production needs to be added back as a unit test. In
    traditional platform or software engineering terms, that's what evals are
    for ML. Without proper evals, you don't really have a CI/CD system.

    Anyone would understand
  sec: 1378
  time: "22:58"
  who: Dewang
- line: |-
    how much can break in production without it. That analogy could probably
    help.
  sec: 1427
  time: "23:47"
  who: Dewang
- line: |-
    How would you demonstrate their importance? The problem is that nobody is
    interested. How can I make people interested and show why evals matter?

    Should I select cases where the model doesn't perform well and show how many
    there are? It takes time to build a comprehensive list.
  sec: 1433
  time: "23:53"
  who: Alexey
- line: |-
    Yes, one hundred percent. A simple example could show that the model works
    well on five queries but not on four others. I make a change, and it starts
    working on those four but stops working on the first five.

    Without an eval set containing all nine, it would be impossible to evaluate
    whether my changes are working.
  sec: 1464
  time: "24:24"
  who: Dewang
- line: |-
    Perhaps another example is changing a prompt so that one case improves but
    another gets worse. Without a comprehensive set, we're blind; we don't know
    which direction we're moving. Having that data set helps.

    I come from a data science background, so I understand the importance of
    evaluation. There are also things in data science nobody wants to take care
    of, such as data cleaning.
  sec: 1489
  time: "24:49"
  who: Alexey
- line: |-
    Model deployment isn't always a data scientist's favorite part either. We
    like training models on clean data while somebody else takes care of
    deployment. But somebody needs to take care of the data and deployment.

    Who is that person usually? The data scientist, because nobody else has
    enough knowledge to do it. When nobody is interested in contributing,
    perhaps the first step is to be that person.

    Once you start,
  sec: 1526
  time: "25:26"
  who: Alexey
- line: |-
    you show how important it is and build the practice. DevOps is a set of best
    practices; I don't know if there's a thing called AIOps or whatever, but
    this could be one of the best practices we need. As you mentioned, CI/CD is
    very important.

    If we don't have it, that's a problem.
  sec: 1570
  time: "26:10"
  who: Alexey
- header: "Evaluation data, benchmarks and tool calling"
- line: |-
    In your experience, what are the best practices for building a good-quality
    data set? What tips and tricks would you recommend?
  sec: 1598
  time: "26:38"
  who: Alexey
- line: |-
    First, acknowledge that this is a hard problem and very use-case driven.
    There's the cold-start problem: you don't have users and probably don't have
    the right data. A lot of people use synthetic data generation for that.

    You use a larger LLM, or an LLM, and give it the kinds of inputs and outputs
    your system could expect. You can start with that to address the cold-start
    problem. Otherwise, if you already have an application in production, taking
    ten or twenty percent, or whatever percentage, of
  sec: 1616
  time: "26:56"
  who: Dewang
- line: |-
    user traffic every day and putting it into a training, eval and golden set
    really helps. The second part is your stakeholders. At enterprises, product
    managers can tell you what queries, inputs and outputs a user can expect,
    usually in a product requirements document.

    That can be a great starting reference. Use your stakeholders, users,
    product managers and whoever you're building the application with to figure
    out the inputs and outputs the system expects. Start small and get something
    out.
  sec: 1671
  time: "27:51"
  who: Dewang
- line: |-
    Start there and iterate; it keeps getting better. Data sets and eval sets
    don't remain static. They have to evolve as your users and the people using
    your model evolve.

    The platform needs to support a consistent way to append to the eval set,
    run queries whenever you deploy a model, perhaps through smoke or
    integration tests, report a score and help gate deployment based on it.
    Those are things the platform handles. What you have to handle is the
    inputs, outputs and queries you expect.

    That's usually much harder, because at the beginning you often won't have
    representative queries.
  sec: 1718
  time: "28:38"
  who: Dewang
- line: |-
    Thank you. What's the relationship between benchmarks and evals? Are they
    the same thing?
  sec: 1768
  time: "29:28"
  who: Alexey
- line: |-
    Benchmarks are common use cases across the industry, which work well if your
    use case aligns with them. If you're building a tool-calling system, for
    example, where a model has to identify whether the right tool was called,
    there are open-source data sets and benchmarks to evaluate it. You might see
    that Claude is currently doing best in tool calling, so that will be your
    starting model.

    Benchmarks help you select a starting point. Evals are specific to your use
    case.
  sec: 1776
  time: "29:36"
  who: Dewang
- line: |-
    The tool-calling inputs Claude gets aren't necessarily the same as yours. If
    you're building tool calling on top of internal enterprise APIs and a
    platform, there are no benchmarks for that. You'd start with the
    best-performing tool-calling model, but build an eval set to evaluate how
    well it does on your internal data sets.

    That's how I think of it.
  sec: 1820
  time: "30:20"
  who: Dewang
- line: |-
    Evals are specific to your problem; benchmarks are more general. Since you
    brought up tool-calling benchmarks, there's a related question: are there
    tips for handling incorrect tool calls? If I see that the accuracy of the
    tool calls isn't good, how do I improve it?
  sec: 1850
  time: "30:50"
  who: Alexey
- line: |-
    It depends a lot on the model you're using, and whether it's fine-tuned or
    you're doing prompt or context engineering on top of Claude. Add every
    mistake you see, or a representative set, to your eval. It's a lot about
    iteration.

    If you're using Claude or ChatGPT, add few-shot examples showing the
    mistakes: for this prompt, this was the right tool call, not the other one.
    If you're fine-tuning a model, adding those examples to your training data
    or LoRA training data helps. Those are things that can improve your
    tool-call responses.
  sec: 1883
  time: "31:23"
  who: Dewang
- line: |-
    It's a lot of trial and error, and that's where evals help.
  sec: 1938
  time: "32:18"
  who: Dewang
- line: |-
    Should I be concerned about benchmarks at all? Suppose I develop a
    pizza-ordering system, and sometimes it invokes one tool instead of the
    other. Should I worry about benchmarks, or is there something simpler I can
    do?

    You mentioned annotating data: in this session the correct tool should have
    been this one, but it used that one. Let's make sure it uses the correct one
    next time. Is that one of the ways?
  sec: 1944
  time: "32:24"
  who: Alexey
- line: |-
    Yes. If you're fine-tuning your own model, add more examples to the training
    set, either directly from its mistakes or using synthetic data generation.
    You can tell a very large LLM, 'Here are some queries and the output
    tool-call parameters.

    Generate hundreds of examples for me,' and add those to your training set.
    That helps the model learn the right tool call for those queries and
    improves your eval. Benchmarks help select the primary model you want to
    use.
  sec: 1985
  time: "33:05"
  who: Dewang
- line: |-
    If I have to use an open-source model, and Qwen or Gorilla or whatever is
    the latest or best-performing tool-calling model, I can start with it. But
    it could perform poorly on my benchmark, while the second-best model
    performs better on my personal eval. It's a lot of iteration.

    Platforms come in again here, because they should let you easily pick any
    model,
  sec: 2028
  time: "33:48"
  who: Dewang
- line: |-
    do inference, run the evals, connect the dots and give you the numbers. You
    shouldn't have to reinvent the wheel every time you want to run the same
    thing.
  sec: 2057
  time: "34:17"
  who: Dewang
- line: |-
    That makes sense. General-purpose benchmarks evaluate general-purpose tools,
    rather than pizza-delivery tools. They could be amazing with general-purpose
    tools but not best for your specific case.

    There's also a lot of art in defining tools. Maybe it's less important now
    than a few years ago, but tools should still be properly described. It's
    context engineering again.
  sec: 2067
  time: "34:27"
  who: Alexey
- line: |-
    Context engineering and tool descriptions matter a lot. How many tools
    you're sending to the model might matter a lot. How you find the tools
    related to your query and send them to the model matters, as with
    retrieval-augmented generation.

    You could build a system where descriptions and queries are indexed to find
    the right set of tools. You have to evaluate both independently and the
    whole system together. If retrieval fails, generation can't do anything
    because it never saw the tool.

    Even though context lengths increase every day, it's still
  sec: 2097
  time: "34:57"
  who: Dewang
- line: |-
    true that LLMs perform much better with the right context than a long
    context where they have to find a needle in a haystack. In terms of latency
    and accuracy, there's still value in giving the right amount of context for
    a query. Tool descriptions help, which is why MCPs took off: they
    standardized a lot of these things.

    GitHub MCP comes with tool descriptions and explains what a pull request, an
    approval or a merge commit is.
  sec: 2144
  time: "35:44"
  who: Dewang
- line: |-
    People who are experts in a tool describe it, so you can add that MCP to
    your Claude system and let it take care of it. Before, if I had to build a
    GitHub integration, I'd write my own descriptions. If you had to build it,
    you'd write yours, and then your own functions to execute those tools.

    That's something else to think about and invest in.
  sec: 2183
  time: "36:23"
  who: Dewang
- header: "MCP, command-line tools and context limits"
- line: |-
    What do you think about MCP versus CLI? Which do you prefer? For GitHub, you
    can have GitHub MCP or GitHub CLI, and it's similar for everything else.

    What's your opinion?
  sec: 2209
  time: "36:49"
  who: Alexey
- line: |-
    It's a hotly debated topic. I see them coexisting, rather than it being
    either-or, for a couple of reasons. Not everything you build, or every tool
    you need, has a CLI, especially internally.

    If an internal platform is only exposed as an SDK or API, you wouldn't want
    to build a CLI on top just so your LLM can execute it. It's probably easier
    to expose it as an MCP service. With popular tools such as GitHub, where
    CLIs are available,
  sec: 2227
  time: "37:07"
  who: Dewang
- line: |-
    you can use them. They have to coexist, at least at the moment. MCPs also
    help distribution.

    If I provide an MCP JSON, it's easy as a company to distribute it as a
    package to users who want to integrate it. CLIs still have to be installed.
    You have to let your LLM figure out how to install one and where to put it.

    In Claude Code, MCP integration is very easy; CLI integration still requires
    some work.
  sec: 2273
  time: "37:53"
  who: Dewang
- line: |-
    That's where I am. I think it's a world where both will coexist.
  sec: 2313
  time: "38:33"
  who: Dewang
- line: |-
    For a CLI, you need a shell. What if your agent doesn't need a shell? What
    if it's a pizza-ordering app?
  sec: 2317
  time: "38:37"
  who: Alexey
- line: |-
    Yes, that too.
  sec: 2329
  time: "38:49"
  who: Dewang
- line: |-
    Have you heard about DoorDash CLI?
  sec: 2331
  time: "38:51"
  who: Alexey
- line: |-
    No, I haven't.
  sec: 2335
  time: "38:55"
  who: Dewang
- line: |-
    I think it was trending on Twitter a couple of months ago: you can ask your
    code to order pizza, and it uses the CLI to do it. Are you based in San
    Francisco?
  sec: 2338
  time: "38:58"
  who: Alexey
- line: |-
    Yes, I live in Berkeley, which is very close to...
  sec: 2351
  time: "39:11"
  who: Dewang
- line: |-
    Here in Germany we don't have DoorDash, but it's a delivery system. Going
    back to tools, you mentioned that too many tools pollute your context. How
    many is too many?
  sec: 2355
  time: "39:15"
  who: Alexey
- line: |-
    It depends on your model. Ideally, you'd have only the tools related to your
    query, but that's not always possible. Going back to the pizza-ordering app,
    there's an order-pizza function, but also a payment function and other
    things.

    You won't always get only the order-pizza function in your context; there
    will be others.
  sec: 2378
  time: "39:38"
  who: Dewang
- line: |-
    It depends on how well your model performs and your latency requirements,
    because as context increases, latency also increases. It depends on how much
    you want to solve the retrieval problem versus giving it to the LLM to
    figure out. Models are getting better at handling larger contexts, but it
    comes at a latency cost.

    If I have five hundred tools in my prompt every time, responses will be
    slower and less accurate. I'd tie that back to evals. Have representative
    evals for those queries or tools in the prompt, see how your model performs,
    and fine-tune to find the right size for your model and use case.

    Sadly, there isn't a one-size-fits-all solution to this problem.
  sec: 2419
  time: "40:19"
  who: Dewang
- line: |-
    Makes sense.
  sec: 2477
  time: "41:17"
  who: Alexey
- header: "Single-agent and multi-agent systems"
- line: |-
    In object-oriented programming or design, there's the single-responsibility
    principle: an object should have one responsibility. If it has two, it's a
    bad object, or a bad class, and you need to split it into multiple classes.
    I think that can apply to agents.

    If we have customer support and pizza ordering in the same app or chat, it's
    performing multiple things, and we think of splitting it. There's a question
    about that: when should we consider a multi-agent system over a single-agent
    system?
  sec: 2479
  time: "41:19"
  who: Alexey
- line: |-
    It depends on the use case. I wouldn't start by asking whether I need a
    single-agent or multi-agent system. I'd start with the business problem I
    need to solve and the tools available.

    We shouldn't build a multi-agent system just because it's cool or performs
    better in some terms. Going back to pizza ordering, if all I need is to
    order a pizza and there's one order-pizza function, there's no need for
    multiple agents doing the same thing. One agent is enough.

    But if I have something like
  sec: 2529
  time: "42:09"
  who: Dewang
- line: |-
    a personal assistant app, such as Muse, it can book reservations, go onto
    Instagram and sort my reels, and figure out my subscriptions and optimize
    them. Multi-agent systems help in those cases because the pizza-ordering
    subagent shouldn't be concerned with the restaurant-reservation subagent. An
    orchestrator with subagents tasked with different specific jobs helps.

    If you only have one task, don't split it into a multi-agent system.
  sec: 2579
  time: "42:59"
  who: Dewang
- line: |-
    That's maybe a good starting rule of thumb. If you're building something
    where multiple tasks need to happen in parallel, and you want outputs from
    multiple systems orchestrating and talking to each other, then we can build
    multi-agent systems for that.
  sec: 2618
  time: "43:38"
  who: Dewang
- line: |-
    As you were speaking, I looked up whether Muse is open source. It isn't.
    Grokbot isn't open source; Dots isn't open source.

    I guess the open-source options we have are OpenClaw and Hermes. Have you
    checked how they work? Is it a multi-agent setup, or are they plugins with
    everything in one context?
  sec: 2641
  time: "44:01"
  who: Alexey
- line: |-
    Do you mean OpenClaw?
  sec: 2668
  time: "44:28"
  who: Dewang
- line: |-
    OpenClaw, yes.
  sec: 2670
  time: "44:30"
  who: Alexey
- line: |-
    OpenClaw is an interesting one. It has different sandboxes for running
    tools, so I'd say it's a multi-agent system. There are different entry
    points, and an orchestrator sends your request to the right subagent tasked
    with executing that tool.

    It's a subagent, super-agent kind of architecture. Multi-agent has become an
    all-encompassing term. There doesn't necessarily have to be an orchestrator:
    in some cases, multiple agents can handle your request by talking directly
    to each other.

    It's a multi-agent system in the sense that multiple LLMs run and execute
    different things for you in parallel.
  sec: 2671
  time: "44:31"
  who: Dewang
- line: |-
    It makes sense for a personal assistant that can do anything. But how often
    do we have similar use cases where we need a multi-agent system? In your
    experience, can you think of times when you needed multi-agent versus
    single-agent systems, and perhaps a proportion?
  sec: 2732
  time: "45:32"
  who: Alexey
- line: |-
    Let me think of enterprise apps building agents to use those apps. It
    depends on how complicated the application is. Take Acrobat.

    Acrobat AI Assistant has been out for three or four years now. There are
    multiple PDF-editing options, image-editing options through Express and
    other things. Those agents need to be multi-agent because a user could be
    editing a PDF or be more concerned with getting it signed.

    Those are two different responsibilities that two agents could theoretically
    handle. That's where a multi-agent system comes in more.
  sec: 2755
  time: "45:55"
  who: Dewang
- line: |-
    Even a coding agent is multi-agent. I'm trying to think of popular examples.
    Take a tool-calling or search agent where, given a user query, all I'm
    concerned with is finding the right search query and searching for that on
    Google.

    That particular problem is single-agent, although that agent could be part
    of a multi-agent system. If I'm only building the search capability, I don't
    need multi-agent search. I can figure out the query, search Google and get
    the response.
  sec: 2814
  time: "46:54"
  who: Dewang
- line: |-
    In my courses, when someone says they have an amazing idea with five agents,
    I say: imagine that each agent needs its own eval set. Each subagent has to
    work well, and you also need an eval set for the master agent, main agent or
    orchestrator. It's so much work to make everything function properly that,
    in many cases, it helps to step back.

    What's the most important thing I'm trying to solve? Usually there's one
    thing you want to
  sec: 2855
  time: "47:35"
  who: Alexey
- line: |-
    make sure works, and it makes sense to focus on it. But for general-purpose
    agents, or your Acrobat example, multi-agent makes total sense.
  sec: 2905
  time: "48:25"
  who: Alexey
- header: "Understanding data and error analysis"
- line: |-
    Another question, from Jamie: how do you get better at understanding data? I
    don't know if it's specifically related to platform engineering, but it's a
    general question. In my experience as an AI engineer, understanding the data
    always beats trying to be smart about prompts and things like that.

    Fixing the root problem of wrong data gives a better return on investment,
    but it's difficult. How do I get better at this?
  sec: 2918
  time: "48:38"
  who: Alexey
- line: |-
    That's the million-dollar question. As a student, AI or LLM engineering is
    often about having a clean data set and specific evals, then making the
    model better at learning the data and getting the best eval results. In
    industry, it's quite the opposite.

    Model training becomes the smaller problem. Cleaning and shaping the data,
    getting an eval set in the first place, aligning stakeholders on it, and
    taking the model to deployment safely become harder.
  sec: 2960
  time: "49:20"
  who: Dewang
- line: |-
    Playing with the data, looking through different lenses and doing
    exploratory data analysis helps. I've seen people point Claude at the data
    and ask it to create charts and help them understand the distribution and
    whether it's representative. Claude can write a lot of code for you, but you
    have to understand the charts.

    What does the distribution look like? What doesn't it cover from your users'
    experience of the product? What queries isn't it capturing?

    How do I align stakeholders to capture those inputs and outputs?
  sec: 3013
  time: "50:13"
  who: Dewang
- line: |-
    Those are still human jobs to understand and figure out. Training comes
    afterward, and I'd say that's a lot more standardized now. You can call APIs
    and get a model trained, then look at eval results, decide whether it's good
    enough to ship and work with deployment teams to get it into production.

    That's the whole workflow. For understanding data, opening an IDE and
    playing with it helps.
  sec: 3060
  time: "51:00"
  who: Dewang
- line: |-
    For me, it's often error analysis. You have a data sample where the system
    isn't behaving as you want, and you try to understand why. You often find
    the data is incomplete or wrong.

    Working backward from errors frequently points to data issues, and then you
    think about how to fix them.
  sec: 3098
  time: "51:38"
  who: Alexey
- header: "LLM judges and evaluation data versioning"
- line: |-
    At least that's my experience. Another interesting question is about judges:
    who's judging the judge? What metrics evaluate the judges?
  sec: 3134
  time: "52:14"
  who: Alexey
- line: |-
    We see LLM-as-a-judge all the time, but how do you evaluate the judge
    itself? One rule is that using the same family of models to produce the
    response and judge it usually creates bias. A good starting rule of thumb is
    to use a different model family.

    A Gemini judge might favor a Gemini output, for example. I wouldn't treat
    the judge as anything other than a way to represent what the human in the
    loop expects from the outputs. Does the judge represent that human?
  sec: 3146
  time: "52:26"
  who: Dewang
- line: |-
    I'd say the human responsible for the application, or its stakeholder,
    evaluates the judge. Do their expectations of the outputs align with what
    the judge evaluates? Suppose I'm a user who sees search results and doesn't
    think they're good.

    I give feedback. I look at whether my LLM-as-a-judge aligns with that user
    feedback, and that's how I improve it.
  sec: 3198
  time: "53:18"
  who: Dewang
- line: |-
    It's the human who evaluates the LLM-as-a-judge. That could mean broad
    feedback from actual users, or stakeholders within the company giving
    evaluations. That's what's evaluating the judge for me.

    I've seen that pattern multiple times with LLM-as-a-judge.
  sec: 3231
  time: "53:51"
  who: Dewang
- line: |-
    Makes sense. We don't need another judge to judge the judge; at the end, you
    need a human. When we build the judge, we align it with our judgment, or
    human judgment.

    We know this sample is bad, so the judge should agree. This case is good, so
    the judge should say it's good. That's alignment: getting the judge to agree
    with your judgment.

    Some time passes, you stop doing this, and the judge keeps running. You
    might wonder how it's doing. Then we need to include a human in the loop
    again.

    I might sample the judge's evaluations,
  sec: 3252
  time: "54:12"
  who: Alexey
- line: |-
    go through them and see whether they're good. If the app has a feedback
    mechanism, we can look at cases where the judge says it's good but the user
    says it isn't. Why is that?

    The best metric would be agreement with the user.
  sec: 3315
  time: "55:15"
  who: Alexey
- line: |-
    Exactly. Tying it back to our initial discussion, judges should be treated
    like the model we've deployed. Add human feedback, user feedback or things
    that didn't work back into the loop as tests.

    The same goes for the judge. It isn't very different from the deployed
    model; it's part of the system, and the same principles apply.
  sec: 3339
  time: "55:39"
  who: Dewang
- line: |-
    When you do this, another interesting thing happens. You have an evaluation
    data set and observe cases where the model doesn't do well. You add them to
    the evaluation set, and your metric drops.

    Everyone asks why the model is now performing poorly. How do we handle that?
  sec: 3368
  time: "56:08"
  who: Alexey
- line: |-
    I think this is where model and eval-set versioning become important.
    Whenever we add something to the data set, it needs to be versioned. Version
    one's metrics are still what they were, but version two represents a cohort
    that version one didn't.

    When I add queries back, I have a V2 eval set. We still need to evaluate on
    V1, report the metrics and show that V1 is still working as intended. The
    new user cohort we weren't thinking about is where metrics are dropping, and
    that's what we need to address.

    It also helps with
  sec: 3392
  time: "56:32"
  who: Dewang
- line: |-
    figuring out what needs addressing. When we solve it, running it back on V1
    to make sure it hasn't regressed is as important as making it work for the
    second set of users.
  sec: 3440
  time: "57:20"
  who: Dewang
- line: |-
    Until you fix those problematic use cases, you go back to V1 and check
    you're not regressing there? This is an important responsibility for the AI
    platform, perhaps the evaluation component. It should contain the
    data-versioning capabilities to do that.

    If I don't version my data, all I see is a drop in performance.
  sec: 3454
  time: "57:34"
  who: Alexey
- line: |-
    Correct. Exactly.
  sec: 3485
  time: "58:05"
  who: Dewang
- header: "The lost-in-the-middle problem and platform support"
- line: |-
    We have time for one more question. There are seven, so unfortunately I have
    to select one. I selected this because I don't know what it is: how can we
    solve the lost-in-the-middle problem in RAG-based applications?

    Do you know what that problem is?
  sec: 3487
  time: "58:07"
  who: Alexey
- line: |-
    I think the lost-in-the-middle problem refers to a paper that came out in
    2023. It talked about LLMs tending to focus more on the start and end of the
    prompt, and less on the middle. I don't know how true it is with today's
    models; they're getting better at this problem.

    But what we said earlier about giving the exact right context is still
    important. It helps accuracy and also latency if you're building a
    latency-sensitive application.
  sec: 3507
  time: "58:27"
  who: Dewang
- line: |-
    It goes back to the same topics: a good, representative evaluation set to
    help you find the exact problem. If RAG isn't giving the right context to
    the LLM, your retrieval needs fixing to find the right inputs. Printing the
    complete prompt often helps.

    We don't always see exactly what's going to the LLM. We see that a RAG
    application produced a particular output for an input, but print and log the
    whole prompt that goes to the LLM.
  sec: 3548
  time: "59:08"
  who: Dewang
- line: |-
    Use that in your error analysis.
  sec: 3598
  time: "59:58"
  who: Dewang
- line: |-
    Including tool descriptions, skills and all that stuff?
  sec: 3600
  time: "1:00:00"
  who: Alexey
- line: |-
    Everything. I know it's hard to read through it all, but logging a couple of
    examples, perhaps three, helps you see exactly what's going to your LLM.
    What could the LLM have done without?

    What wasn't important for the query? Try to find where it's coming from and
    what you can eliminate. Is the retriever providing unnecessary context?

    Am I loading more skills than I need? Then I reduce the skills for that
    session. It's a lot of trial and error.
  sec: 3606
  time: "1:00:06"
  who: Dewang
- line: |-
    It's the LLM version of the error analysis you mentioned: seeing the exact
    inputs and outputs, finding what wasn't required to solve the problem and
    removing unnecessary bits to reduce the cost.
  sec: 3649
  time: "1:00:49"
  who: Dewang
- line: |-
    Logically, focusing on the beginning and end makes sense. In a Claude Code
    session, the agent needs to remember the instructions, and perhaps my first
    prompt about the task we're solving. Then there's analysis to understand
    what needs to happen, which might be less important.

    But the latest input I give to steer it, or things it discovers itself, are
    much more important than things in the middle. It makes sense for models to
    focus on those. For RAG, I guess things like reranking?
  sec: 3661
  time: "1:01:01"
  who: Alexey
- line: |-
    Exactly.
  sec: 3710
  time: "1:01:50"
  who: Dewang
- line: |-
    Throughout this discussion, we've mentioned evals perhaps a hundred times.
    In data science it was always similar: should I use XGBoost or logistic
    regression? It depends on cross-validation.

    Now we say evals instead of cross-validation, but the idea is the same. You
    need a good evaluation data set that represents your problem. Whatever the
    question—this model or that one, reranking or not—the answer is always...
  sec: 3713
  time: "1:01:53"
  who: Alexey
- line: |-
    Evals.
  sec: 3751
  time: "1:02:31"
  who: Dewang
- line: |-
    OK.
  sec: 3753
  time: "1:02:33"
  who: Alexey
- line: |-
    To finish our discussion, evaluation is a very important component of an AI
    platform. It's responsible for making it easy to do evals while developing a
    model. We had questions about people not wanting to do evals and how to make
    it easier.

    If it's a platform capability and capturing production data is simple, then
    we have evals automatically? It's the platform's responsibility to make it
    easy for us.
  sec: 3754
  time: "1:02:34"
  who: Alexey
- line: |-
    Exactly.
  sec: 3799
  time: "1:03:19"
  who: Dewang
- line: |-
    Is there anything else we should mention before we finish?
  sec: 3800
  time: "1:03:20"
  who: Alexey
- line: |-
    Go read our book. We'd love more feedback on it. Reach out to me on LinkedIn
    with any questions.

    This was great chatting with you. Thank you for inviting me.
  sec: 3807
  time: "1:03:27"
  who: Dewang
- line: |-
    One small announcement: we'll have the book as the Book of the Week next
    week in DataTalks.Club. From Monday to Thursday, if you have questions about
    AI systems or AI platforms, bring them to Slack. There were questions we
    didn't get to answer today.

    Both Suhas and Dewang will answer questions in our Slack, so bring yours and
    we can continue the conversation. Thanks for joining me; it was a very
    interesting discussion. Thanks to everyone for joining, asking questions and
    being active.
  sec: 3825
  time: "1:03:45"
  who: Alexey
- line: |-
    Thank you so much. Thank you, everyone.
  sec: 3869
  time: "1:04:29"
  who: Dewang
---

Dewang Sultania joins Alexey Grigorev for the second conversation with the authors of *Designing AI Systems*. They discuss the platform services needed to move from an LLM chatbot to an agent that takes actions: session memory, tool integration, execution policies, observability, and deployment.

Links:

* [Designing AI Systems](https://www.manning.com/books/designing-ai-systems){:target="_blank"}
* [Book code](https://github.com/designing-ai-systems/designing_ai_systems_repo){:target="_blank"}
* [Dewang on LinkedIn](https://www.linkedin.com/in/dewang-sultania/){:target="_blank"}
* [Dewang on GitHub](https://github.com/iron-stark){:target="_blank"}
* [Part 1 with Suhas Suresha](s25e06-building-ai-platform-sdk-design-model-routing-vector-search-evals.html)
