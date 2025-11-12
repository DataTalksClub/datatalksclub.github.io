---
episode: 1
guests:
- ranjithakulkarni
ids:
  anchor: datatalksclub/episodes/Building-reliable-AI-products-in-the-era-of-Gen-AI-and-Agents---Ranjitha-Kulkarni-e396m2u
  youtube: x2AAjqz2XmM
image: images/podcast/s22e01-building-reliable-ai-products-in-era-of-gen-ai-and-agents.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/Building-reliable-AI-products-in-the-era-of-Gen-AI-and-Agents---Ranjitha-Kulkarni-e396m2u
  apple: https://podcasts.apple.com/us/podcast/building-reliable-ai-products-in-the-era-of-gen/id1541710331?i=1000731199709
  spotify: https://open.spotify.com/episode/7c22vqYNuNLKKYEfYGOos8?si=NBFT2e80S6WErW_tDDrijA
  youtube: https://www.youtube.com/watch?v=x2AAjqz2XmM
season: 22
short: Building reliable AI products in the era of Gen AI and Agents
title: 'Build & Evaluate Autonomous LLM Agents: RAG, Orchestration, Context Engineering
  & SRE'
transcript:
- header: Event Introduction & Community Links
- line: Hi everyone, welcome to our event. This event is brought to you by DataTalks.Club,
    which is a community of people who love data. Every time I say that, I remember
    that when this automatic speech recognition software processes this, it recognizes
    what I say as Data Docks Club. I need to work on my articulation. These recognizers
    can actually deal with my accent.
  sec: 0
  time: 0:00
  who: Alexey
- line: DataTalks.Club. Anyways, we have quite a few events in our pipeline, although
    recently we had quite a few already. If you want to stay up to date with all the
    events we have, there is a link in the description. Go there, click, and you'll
    see all the events we have. You can also subscribe to our newsletter. We constantly
    send reminders about future events.
  sec: 33
  time: 0:33
  who: Alexey
- line: Do not forget to subscribe to our YouTube channel. This way you'll stay up
    to date with all the future streams. I'm just curious, how many subscribers we
    have. I think this is right now 66,000, which is pretty outdated. So if you want
    to be 66,001, do it now.
  sec: 63
  time: '1:03'
  who: Alexey
- line: Last but not least, you can join our Slack community if you want to hang out
    with other data enthusiasts. Check it out. If you have any questions that you
    want to ask during the interview, there is a pinned link in the live chat. Click
    on that link, ask your questions, and we will be covering these questions during
    the interview. This intro that I do is the same every time, so for me, it gets
    a little boring, and I improvise a little.
  sec: 93
  time: '1:33'
  who: Alexey
- line: Let me clear my throat one second. Sorry, I think I'm good. Ranjitha, are
    you ready?
  sec: 138
  time: '2:18'
  who: Alexey
- line: Yes, Alexey.
  sec: 144
  time: '2:24'
  who: Ranjitha
- line: Great. Today on the podcast we are joined by Ranjitha, staff ML engineer at
    Noird at.AI, previously at Dropbox. You have been building LLM and agent-powered
    products, with earlier work in speech recognition and NLP at Microsoft, and research
    at Carnegie Mellon. You have quite a nice career journey. It's a big pleasure
    to have you here at our event.
  sec: 150
  time: '2:30'
  who: Alexey
- line: The pleasure is mine.
  sec: 176
  time: '2:56'
  who: Ranjitha
- line: Okay. So tell us about your career journey so far. I think I outlined it,
    but this is pretty interesting. I see you have worked at quite a few companies,
    so please tell us more.
  sec: 181
  time: '3:01'
  who: Alexey
- header: 'Early ML Projects: Image Search with OpenCV'
- line: Yeah, definitely. In a nutshell, my career is basically machine learning and
    NLP from the start. It started during my undergrad, which was my first time I
    came across this stuff. That was back in 2010 or 2011, I think. We didn’t really
    have many courses on AI or any structured way of learning back then. My friends
    and I were curious, so we just started building something like an image search
    engine.
  sec: 192
  time: '3:12'
  who: Ranjitha
- line: This was back when we were using Sundance search engine and OpenCV for extracting
    features from images and so on. It was kind of like a bag-of-visual-words approach
    or how this approach was called. So we were extracting features from the images
    and doing segmentation. It was hard to do, but it got me hooked on this whole
    space. I just wanted to learn more.
  sec: 235
  time: '3:55'
  who: Ranjitha
- header: Speech Recognition & Language Modeling Experience
- line: That’s what brought me to CMU to do my masters. I learned a lot from amazing
    professors, colleagues, and some startups that were there locally in Pittsburgh.
    From there, I joined Microsoft, where I worked on speech recognition, language
    modeling for Xbox, Bing Search, Bing voice search, and Cortana. I met some amazing
    people who had been doing this for many years and learned a lot from them.
  sec: 265
  time: '4:25'
  who: Ranjitha
- header: Transition to Recommendation Systems at Dropbox
- line: Then I wanted to broaden my scope in ML a little bit, so that brought me to
    Dropbox. Initially, I started working on recommendation systems.
  sec: 297
  time: '4:57'
  who: Ranjitha
- line: What kind of recommendation systems are there? I’ve been a Dropbox user for
    many years and don’t remember it recommending me a single thing.
  sec: 306
  time: '5:06'
  who: Alexey
- line: Dropbox web provides suggestions on files we think you might open based on
    your usage.
  sec: 319
  time: '5:19'
  who: Ranjitha
- line: I understand. Since I don’t use Dropbox through the web, for me it’s just
    a folder. But when I open Google Drive, I see recommendations. So Dropbox has
    something similar?
  sec: 334
  time: '5:34'
  who: Alexey
- header: Question Answering & Early Agent Experiments
- line: Yes, it has had it for a while. I worked on that feature and some auxiliary
    things around it, trying to improve the quality. That’s where I dived more into
    neural networks to understand how these things work, because when I started my
    career, neural networks weren’t a thing yet. Later, I moved back into NLP and
    started working on building a first question answering system. This was an incubation
    team at Dropbox that wanted ML expertise.
  sec: 352
  time: '5:52'
  who: Ranjitha
- line: Then my manager and I, both amazing engineers, started a new team focusing
    on agents. This was back in December 2022, before the term “agents” was popular.
    We were trying to innovate, not just on Dropbox, exploring other data sources
    and ways to improve the system. I was fine-tuning T5, and then GPT-3.5 came, which
    disrupted the whole market.
  sec: 394
  time: '6:34'
  who: Ranjitha
- header: 'Joining Noird.ai: Automating On‑call with Agents'
- line: After working on agents at Dropbox, I was drawn to Noird, where I am now.
    I’m fully immersed in the potential of these agents. We are trying to solve the
    problem of engineering on call, taking that away from users and letting agents
    handle tasks. This allows engineers to focus on the more fun part of building
    the system.
  sec: 464
  time: '7:44'
  who: Ranjitha
- line: That’s interesting. As a developer, I would be happy not to be on call. My
    colleagues, who were software engineers, had to be on call, and when they received
    a notification from PagerDuty, they would open their laptop, check the logs, and
    do all this stuff. For them, it’s good not to do these things anymore.
  sec: 497
  time: '8:17'
  who: Alexey
- line: You are lucky. Even though I’ve been doing machine learning forever, I’ve
    had to be on call many times. I totally understand the pain of being woken up
    at 3 a.m.
  sec: 539
  time: '8:59'
  who: Ranjitha
- line: That’s why you decided to join the company?
  sec: 551
  time: '9:11'
  who: Alexey
- line: Exactly. That vision is what brought me here.
  sec: 556
  time: '9:16'
  who: Ranjitha
- line: Do you know where the name comes from?
  sec: 560
  time: '9:20'
  who: Alexey
- line: I actually don’t know. I think the founders are just really into birds.
  sec: 562
  time: '9:22'
  who: Ranjitha
- line: Noird, as I mentioned, “noi” means “new” in German. Maybe “new bird” was already
    taken, so they chose this name.
  sec: 570
  time: '9:30'
  who: Alexey
- line: I will have to ask them about that.
  sec: 577
  time: '9:37'
  who: Ranjitha
- line: It’s very difficult to start a startup now because most domain names are already
    taken. You need a name that’s not taken but also doesn’t sound like gibberish.
  sec: 583
  time: '9:43'
  who: Alexey
- line: Yes, there are a lot of creative names these days.
  sec: 595
  time: '9:55'
  who: Ranjitha
- line: I remember Kaggle. I was interviewed with one of the creators, Anthony Goldbloom.
    They wrote a script to go through all relatively short names, check if they were
    available, and that’s how they came up with Kaggle.
  sec: 601
  time: '10:01'
  who: Alexey
- line: So, what do you do at Noird?
  sec: 629
  time: '10:29'
  who: Alexey
- line: I’m building agents and everything around the agent ecosystem. It’s been just
    four weeks since I joined, and I can already understand the sheer complexity of
    the problem.
  sec: 635
  time: '10:35'
  who: Ranjitha
- line: You just joined?
  sec: 649
  time: '10:49'
  who: Alexey
- line: Yes, just a month ago.
  sec: 651
  time: '10:51'
  who: Ranjitha
- line: Congratulations.
  sec: 654
  time: '10:54'
  who: Alexey
- header: 'Agent Definition: Autonomy, Objectives & LLMs'
- line: Thank you. I’m working on building the whole story of how LLM agents can work
    more reliably so that customers who are happy today are still happy tomorrow.
  sec: 660
  time: '11:00'
  who: Ranjitha
- line: You’ve been in the industry for quite some time. You also started machine
    learning in 2010. My interest started around 2012. I remember taking courses on
    reinforcement learning where the agent was defined differently. So I’m curious,
    how do you define an agent?
  sec: 674
  time: '11:14'
  who: Alexey
- line: 'Right. This is something I usually start all my talks with: “What is an agent?”
    because it’s not a very well-understood concept.'
  sec: 708
  time: '11:48'
  who: Ranjitha
- line: 'Back in reinforcement learning, agents were basically tasked to complete
    a goal or objective. Agents are automated pieces of software that go and complete
    the given task. You tune them to improve performance according to the objective
    function. The core idea remains the same: autonomously completing a given task.'
  sec: 721
  time: '12:01'
  who: Ranjitha
- header: 'Agent Orchestration: Tools, Memory & Knowledge Stores'
- line: Today, LLMs are at the core, powering these agents. LLMs are the brain of
    the agents. What defines a type of agent varies because everyone has their own
    recipes. Agents orchestrate multiple calls to LLMs, tools, knowledge stores, and
    memory. At the end of the day, an agent performs a task autonomously with the
    help of LLMs, tools, memory, and storage to please the user.
  sec: 751
  time: '12:31'
  who: Ranjitha
- line: I experimented with agents the other day. I thought, can I make an agent without
    an LLM? The answer is yes. We can make decisions with other mechanisms. Right
    now, we delegate decisions to an LLM, which acts as the brain. But it could also
    be simple heuristics depending on the type of agent.
  sec: 811
  time: '13:31'
  who: Alexey
- line: In my case, it was an environment with people applying for jobs and employers.
    They interact based on skills and job positions. The goal was to simulate these
    interactions. Without any LLM, it still worked. But adding an LLM lets one entity
    talk to another, like an interviewer asking questions in a simulation.
  sec: 841
  time: '14:01'
  who: Alexey
- line: Yeah, a fun side project.
  sec: 904
  time: '15:04'
  who: Ranjitha
- header: 'Planning Strategies: Single‑step, Multi‑pass & Self‑reflection'
- line: Would you agree with the definition that an agent is just an LLM with tools?
  sec: 910
  time: '15:10'
  who: Alexey
- line: It’s not just that. There is a wrapper around it, and the way you plan it
    can differ. Agents can complete a task in a single step or multiple steps. A step
    might involve calling a tool, processing information, or other actions. Complexity
    grows with multi-step processes.
  sec: 923
  time: '15:23'
  who: Ranjitha
- line: There’s also the concept of iterations and feedback loops. Is it a single
    pass or multipass system? Multipass involves self-reflection and correcting plans
    based on outputs. These multipass systems make the most complex agents, which
    everyone is trying to develop. Many start with single-step or single-pass systems,
    executing a plan to achieve the goal with some amount of self-reflection.
  sec: 971
  time: '16:11'
  who: Ranjitha
- line: You mentioned planning is different across agents. You can have an agent with
    no LLM. If I ask it to create a Django project, it might not execute that. A simple
    LM can create something, but not as elaborately as a reasoning model.
  sec: 1037
  time: '17:17'
  who: Alexey
- line: Exactly. The plan can be dynamic or predetermined. In your example, the agent
    had a fixed task, a fixed set of tools, and an order of steps. That can work with
    some fail statements. Planning doesn’t always need to be dynamic.
  sec: 1068
  time: '17:48'
  who: Ranjitha
- header: 'Implementation Approaches: Prompts, SDKs & Tool Wrappers'
- line: How is this implemented? Frameworks like LangChain or AI Agents SDK allow
    you to define system prompts, user prompts, and tools. The agent invokes tools
    to execute tasks. Where does planning come in?
  sec: 1103
  time: '18:23'
  who: Alexey
- line: With predefined tools and SDKs, the logic of planning is embedded. Prompts
    and tools define how the plan is generated. Most startups or companies define
    their own agentic platform with custom tools and SDKs. It’s very hard to build
    this generically. It’s easier to focus on the problem you’re solving and see what
    type of agent makes sense.
  sec: 1146
  time: '19:06'
  who: Ranjitha
- header: 'Code Agents vs Natural‑Language Agents: Trade‑offs'
- line: Some agents plan in plain English, others in code so-called code agents. The
    choice depends on the task complexity. For natural language problems, natural
    language-based agents work. For very complex tasks with many steps and conditionals,
    programmatic/code agents are better.
  sec: 1198
  time: '19:58'
  who: Ranjitha
- line: I prefer code agents. They reduce ambiguity and improve predictability. Many
    use cases fit well with code agents. It just feels like most of the experimentation
    leads to this type.
  sec: 1233
  time: '20:33'
  who: Ranjitha
- line: Can you talk about the agents you use at work right now, or is it not something
    you can share?
  sec: 1253
  time: '20:53'
  who: Alexey
- line: I mean I can't share too much in detail, but it's basically the…
  sec: 1260
  time: '21:00'
  who: Ranjitha
- line: I'm just curious what you are working on specifically? Like, what kind of
    agents, of course you cannot share or shouldn't share a lot, but also in many
    cases the devil is in the details, right?
  sec: 1268
  time: '21:08'
  who: Alexey
- header: 'Context Engineering: Designing Effective LLM Inputs'
- line: Exactly. I can tell you, like, at a high level basically the agents are trying
    to build the right context to present to the LLM. Right, so a lot of it is I think
    a lot of people are talking about this these days called context engineering.
    But I think this is something that we had to bake in from the time I've been working
    on agents because back then we had models that had a 4k context window. You don't
    have the luxury of stuffing everything into the context, so you have to be very
    deliberate about what it is that you're kind of sending to the LLM.
  sec: 1281
  time: '21:21'
  who: Ranjitha
- line: And what we learned in that process is that when you're doing that, you're
    not losing much. You learn to kind of put the context into LLM's windows by only
    providing, you know, how do you define it, like something like the metadata or
    the way to plan and things like that. So you ask the LLM, "Hey, what are the steps
    to do something like this?" rather than giving it all the data and saying, "These
    are all the documents I have, can you go dig into it and find me the right answer?"
    So it's a lot to do with context engineering. Even at Newbird, we are doing a
    lot of that trying to reduce the noise that you feed into LLMs. And it's a complex
    agentic system that they built even before I joined.
  sec: 1319
  time: '21:59'
  who: Ranjitha
- header: 'SRE Workflows Modeled by Agents: Logs, Metrics & Remediation'
- line: It's so many tools. If you can imagine being an SRE what would you do right?
    You have to look at so many different data sources, different logs, and metrics.
  sec: 1370
  time: '22:50'
  who: Ranjitha
- line: So I imagine, let's say I am on call and I receive a message saying that this
    system is failing right? And then I open whatever thing for logs, then I investigate
    the logs, then I go to Kubernetes and check the deployment ports or whatever,
    find about the logs and try to find out the reason. I may go to the source code
    to actually see where the issue is coming from, and maybe I do a quick fix or
    roll back to the previous version. Right. So that's what I would do. Does the
    system you have kind of mimic this behavior?
  sec: 1386
  time: '23:06'
  who: Alexey
- line: It does mimic that kind of behavior in its own special way.. It's basically
    this is the way you as an SRE would do something like this, but an agent at the
    end of the day is basically now like 23, 24 of us are building it together, right?
    So all of our personalities go into it, and what wins eventually is something
    that can do it again and again repeatedly, that can solve a problem again and
    again.
  sec: 1424
  time: '23:44'
  who: Ranjitha
- line: What our customers come and say we get a customer email saying, "Yeah, this
    really worked well for us," and those are the things that we learn from. That
    is the feedback we get. As a startup, you don't yet have that much luxury of data
    to look at right? You're waiting for these individual customer feedbacks. Our
    team is amazing in the sense that I'm new to startups, and when I look at it,
    I'm so amazed by it.
  sec: 1459
  time: '24:19'
  who: Ranjitha
- line: Everybody is harping on anything if a user says something is not working,
    everybody goes, "Okay, it should have done this, it didn't do it, and how do we
    fix it?" And that's the kind of mentality that's going to propel the startup forward.
  sec: 1486
  time: '24:46'
  who: Ranjitha
- header: 'Integration Abstractions: Handling Diverse Tooling'
- line: And I just, what occurred to me is every setup, infrastructure, can vary drastically
    from company to company. One company can use Datadog, another uses New Relic,
    the third one uses something built in-house, on-prem, then there's ELK or ElasticSearch,
    there are so many different tools. Some use Kubernetes, some, god knows what,
    whatever deployment. There is such a variety. How do you, like, have to at some
    point restrict and say, "Okay, I work only with this tech," or what do you do?
  sec: 1499
  time: '24:59'
  who: Alexey
- line: True, true. There is that thing where there is a cap after which you say,
    "We will keep these as highest priority," and deprioritize some of them. But the
    challenge and beauty of these agentic systems is that you bake in this generality
    you can abstract away the details of which API you are talking to, what kind of
    data you are looking at. You abstract that away so your implementation is generic
    enough.
  sec: 1543
  time: '25:43'
  who: Ranjitha
- line: It's just a matter of building those connections with the agent. If people
    are building connections when a new kind of data source becomes available, then
    you're mostly good. There are peculiarities, of course, like a particular data
    source might come with its own peculiarities. For example, "No, we will write
    the log in a reverse fashion, where we'll put status codes at the end and the
    error message before." Things like that happen too, and for those things you kind
    of need domain knowledge.
  sec: 1568
  time: '26:08'
  who: Ranjitha
- line: Unfortunately, there's nothing you can magically do about this, and that's
    where you consult SRE. We have an SRE on our team as well.
  sec: 1613
  time: '26:53'
  who: Ranjitha
- line: You don't fully dedicate it to agents yet.
  sec: 1625
  time: '27:05'
  who: Alexey
- line: No, no, no. It's all agents, but yeah. One SRE does I see, I see, a joke.
  sec: 1633
  time: '27:13'
  who: Ranjitha
- line: No. Yeah, so it's something that you're constantly learning from humans who
    have been doing this for ages and trying to imbibe that knowledge into this. But
    the difference is as a human, you might be good at solving one type of those problems
    or one set of tools, right?
  sec: 1640
  time: '27:20'
  who: Ranjitha
- line: Your learning curve is much higher compared to this agentic system, which
    if you build it once, has the capability to spread across multiple tools and multiple
    integrations. So that's the advantage of having this, making an agent do this
    versus a human doing it.
  sec: 1653
  time: '27:33'
  who: Ranjitha
- line: Yeah, interesting. You mentioned one keyword that I see quite often these
    days on LinkedIn and Twitter, sorry, X on social media, basically context engineering.
    What is context engineering and how is it different from prompt engineering?
  sec: 1679
  time: '27:59'
  who: Alexey
- line: Okay, I think it's just a mind shift. It's more of a rephrasing or rewording
    of the whole thing so that you look at it from a different perspective. Prompt
    engineering has always been this thing where I give my instructions in a way to
    make the model work. If I were to put it succinctly, I would say context engineering
    is like a subfield of prompt engineering.
  sec: 1697
  time: '28:17'
  who: Ranjitha
- line: But the main focus when people said prompt engineering was, "I will put this
    instruction at the top, I will move the instruction to the bottom, I will write
    in all caps," things like that. That was the core of prompt engineering most of
    the time. Context engineering is just being more deliberate about what information
    you give to the LLM rather than stuffing everything in. You can’t just give a
    thousand documents and expect it to understand everything fully.
  sec: 1732
  time: '28:52'
  who: Ranjitha
- header: 'RAG Reality Check: Latency, Cost & Garbage‑In/Garbage‑Out'
- line: We still need to reduce the amount of noise that we put into an LLM’s context,
    and that’s what context engineering is.
  sec: 1770
  time: '29:30'
  who: Ranjitha
- line: Yeah, I remember at the beginning of this year seeing posts that RAG is dead
    because we have these models that can take your entire knowledge base and answer
    questions based on that. From what I see, RAG is not dead yet, right?
  sec: 1775
  time: '29:35'
  who: Alexey
- line: Yeah, definitely not.
  sec: 1791
  time: '29:51'
  who: Ranjitha
- line: The main idea is yes, technically, there are models that can take your entire
    knowledge base, code base, or whatever base, but then how good are they at using
    all the information you give them and how fast? You probably don’t want to wait
    too long for the LLM to process a huge prompt with everything. So probably you
    want to be smart about what kind of information you give to an LLM.
  sec: 1798
  time: '29:58'
  who: Alexey
- line: Yes, it is latency, it is cost, and it is also garbage in, garbage out. If
    you put a lot of noise in, then your model only has so much to work with. They
    have become more capable, you can fill up to a 32k context window, but beyond
    that, many models don’t do very well. If you want it to work reliably every time,
    you want to reduce that to a smaller context window, so you don’t burden your
    LLM with runtime processing everything. Doing some preprocessing beforehand helps.
    That’s where experience in machine learning comes in handy when dealing with LLMs.
    RAG is not really dead, but it doesn’t solve everything and has its shortcomings.
  sec: 1827
  time: '30:27'
  who: Ranjitha
- header: 'Retrieval Limitations: Reworking Backends for LLM Context'
- line: We are now realizing a world where RAG has shortcomings because LLMs are really
    smart, but the backend that supplies context to LLMs is an old information retrieval
    system. Historically, it wasn’t designed for this use case. It gives 10 blue links,
    and humans go click on things. Now we are trying to morph it into something that
    fits the problem of feeding context into LLMs.
  sec: 1898
  time: '31:38'
  who: Ranjitha
- line: Would you agree that RAG is one of the simplest examples of context engineering?
    Instead of giving the entire database of 5,000 records, you select the top 10
    most relevant ones, and by providing that, you engineer the context. The LLM knows
    what to focus on instead of going through the entire knowledge base.
  sec: 1936
  time: '32:16'
  who: Alexey
- header: 'Context Engineering Techniques: Chunking, Metadata & Wrappers'
- line: Yes, at a high level, it is that. Along with that, there is a wrapper that
    presents information in a way that is more conducive for the LLM to understand.
    For example, you can chunk documents into lines of 200 lines each. But that is
    almost always lossy. If you just break it by length or by paragraphs, there is
    still engineering needed to embed context into the chunk. You need to know which
    document it is from, what question it tries to answer, and what has been learned
    so far. That improves the quality of your system in RAG cases.
  sec: 1968
  time: '32:48'
  who: Ranjitha
- line: What are other examples of context engineering?
  sec: 2036
  time: '33:56'
  who: Alexey
- line: Well, a lot of agents work by saying, "These are the tools I have available,"
    and "This is how I solved this problem before." Giving examples influences how
    the LLM thinks and produces output in a structured format. All those are examples
    of influencing the LLM by engineering the context so that the output is meaningful,
    rather than, "These are all the logs, go look at it."
  sec: 2042
  time: '34:02'
  who: Ranjitha
- line: In the case of Newbird, what kind of context engineering do you have? Is it
    all variations of RAG where you index all the logs, or are you doing something
    else?
  sec: 2090
  time: '34:50'
  who: Alexey
- line: Yeah, there’s a bit of this and a bit of that. I can’t tell you more than
    that, but we are influencing the LLM. You may not apply RAG everywhere. For search
    use cases with billions of documents, you would apply RAG. But for very task-specific
    things with domain knowledge, you apply the right tools. I view RAG or search
    information retrieval as a tool itself. You use it when needed.
  sec: 2109
  time: '35:09'
  who: Ranjitha
- header: 'Agentic RAG: Using Retrieval as a Tool Within Agents'
- line: When people say RAG is dead, it’s because vanilla RAG, doing embeddings and
    vector search and putting it into LLMs, is a very set workflow. What we are moving
    toward in agents is getting rid of set workflows and making it dynamic. Agentic
    RAG is one step, and agents go further, taking RAG as a tool rather than an end.
  sec: 2171
  time: '36:11'
  who: Ranjitha
- line: So basically, we have an agent. The agent has some tools. One of them is search,
    which performs search in the database that we have chunked and preprocessed, but
    we let the LLM decide when it needs to use it.
  sec: 2201
  time: '36:41'
  who: Alexey
- line: Exactly, if needed.
  sec: 2224
  time: '37:04'
  who: Ranjitha
- line: There are many ways to query this information. You can do a search query,
    or you can say, "It’s in a table, get me stuff from the table," or "It’s in MongoDB,
    get me all documents with this value." These are just tools, and knowing which
    tool to use when is something we teach our agents. They do the orchestration.
  sec: 2224
  time: '37:04'
  who: Ranjitha
- header: 'Use Cases: When RAG Is Enough vs When Agents Are Needed'
- line: Since we started talking about this, the industry is converging to RAG tools.
    What kind of business problems are good for these solutions? When is classical
    RAG enough, when is RAG one of the tools, and when do you not need RAG or AI at
    all?
  sec: 2259
  time: '37:39'
  who: Alexey
- line: That’s a good question. I think RAG works well for reducing a really large
    search space into something small. RAG does well when you have a large search
    space and the task is simple, like question answering based on a piece of content.
    Imagine Dropbox with millions of documents; you don’t need to organize data neatly.
    You want to find a keyword or an answer to a question.
  sec: 2293
  time: '38:13'
  who: Ranjitha
- line: RAG is less good when context matters, like what you were doing until now,
    the time of day, or what is happening right now. For a needle-in-a-haystack problem
    with lots of knowledge, RAG is still useful. When problems get complex, with multiple
    data sources, dynamic planning, or multiple API integrations, you move to agents.
  sec: 2339
  time: '38:59'
  who: Ranjitha
- line: By dynamic planning, I mean whenever an input comes, you want your LLM or
    agent to plan its trajectory based on the input.
  sec: 2400
  time: '40:00'
  who: Ranjitha
- line: Like when I get a task, I might subconsciously think about the sequence of
    actions I need to execute. If a PagerDuty notification comes, I look at it and
    decide, "I need to go there first, then here, then here."
  sec: 2406
  time: '40:06'
  who: Alexey
- header: 'Dynamic Planning Example: Calendar & Meeting Assistant'
- line: Exactly. So a very simple, easy-to-understand example would be a calendar
    assistant. You talk to it and say, "I want to schedule a meeting for half an hour
    tomorrow with my manager or my skip level." There are many hidden understandings
    or context that I assume the LLM knows about me, such as the meeting duration,
    my time zone, who my manager is, and their working hours. The LLM has to figure
    these out and check the calendar to see when both are free.
  sec: 2430
  time: '40:30'
  who: Ranjitha
- line: It might also consult another source to find out who the manager is. Then
    it has to check if they have a Google Calendar or an Outlook calendar. The LLM
    is coming up with this plan as the input changes. For example, if my input changes
    to "Summarize my meeting notes from yesterday," it won’t go to the calendar. It
    will go into Zoom transcripts and summarize meetings that happened yesterday.
  sec: 2478
  time: '41:18'
  who: Ranjitha
- line: Does a tool like that exist? I was building something like this at Dropbox
    before I left. Lots of people are actually building this kind of assistance.
  sec: 2520
  time: '42:00'
  who: Ranjitha
- line: I imagine so. I often use voice recognition with ChatGPT to communicate and
    then check the result. I could just say, "Summarize what we talked about yesterday
    on the podcast with Ranjitha about agents," and it would fetch the transcript,
    summarize it, and give it to me. Easily doable.
  sec: 2533
  time: '42:13'
  who: Alexey
- line: Okay, I want to have that. Let’s meet for a hack project. You said Dropbox
    has it.
  sec: 2574
  time: '42:54'
  who: Alexey
- line: Do I need to put all the things into it?
  sec: 2580
  time: '43:00'
  who: Alexey
- header: Dropbox Dash & AI Productivity Assistants for Enterprises
- line: Right now, the product I was building, I don’t know what has changed since
    I left, is Dropbox Dash. It is AI-powered search and assistant. It helps with
    productivity use cases and connects to all the SaaS you use at work. You should
    check it out.
  sec: 2586
  time: '43:06'
  who: Ranjitha
- line: I guess I need a paid account, right?
  sec: 2606
  time: '43:26'
  who: Alexey
- line: I do not know the answer to that right now.
  sec: 2612
  time: '43:32'
  who: Ranjitha
- line: I am checking and there is a "Contact Sales" link. That’s a problem because
    Dropbox is used by enterprises, which is their main target audience. Multiple
    people use the same folders or Dropbox.
  sec: 2618
  time: '43:38'
  who: Alexey
- line: Yes, because the content there is much more expanded and discovering other
    people’s documents becomes more challenging. It’s a better fit for enterprises.
  sec: 2636
  time: '43:56'
  who: Ranjitha
- header: 'Framework Choices: Build from Scratch vs Use Libraries'
- line: At the beginning, we discussed frameworks. I mentioned Pedantic AI and OpenAI
    Agents SDK. Do we need to learn frameworks? If yes, which ones make our life easier,
    or should we implement everything from scratch?
  sec: 2648
  time: '44:08'
  who: Alexey
- line: I’ve tried a few frameworks, but at work I don’t really use them. One I liked
    is called Small Agents, a Hugging Face transformers library. It is programmatically
    thinking and helps bootstrap agents. I would still suggest building from scratch
    because frameworks can become complex, and you may not understand what the agent
    is doing.
  sec: 2676
  time: '44:36'
  who: Ranjitha
- line: An agent is a bunch of tools and instructions. You can implement your own
    memory and data queries. That’s my suggestion.
  sec: 2739
  time: '45:39'
  who: Ranjitha
- line: What do you think about LangChain?
  sec: 2752
  time: '45:52'
  who: Alexey
- header: 'Framework Trade‑offs: LangChain, OpenAI Agents SDK, Small Agents'
- line: LangChain has its uses, but I haven’t used it much for agents. Early on, it
    couldn’t handle ambiguity in natural language. It has improved and has new agents
    to experiment with.
  sec: 2760
  time: '46:00'
  who: Ranjitha
- line: I experienced debugging nightmares with LangChain. OpenAI Agents SDK is lightweight,
    so I understand what’s happening. With LangChain, it’s often unclear.
  sec: 2805
  time: '46:45'
  who: Alexey
- line: Yes, it’s a complex mesh of multiple things talking to each other in natural
    language, which can get confusing.
  sec: 2841
  time: '47:21'
  who: Ranjitha
- line: I agree with your suggestion to implement agents from scratch. It helps understand
    how multiple agents can work, and that one agent can be a tool for another agent.
    It clarifies how these systems actually work.
  sec: 2853
  time: '47:33'
  who: Alexey
- header: Agent Marketplaces & Tool Protocols (MCP)
- line: Eventually, agentic platforms will be usable as-is. At Dropbox, we dreamed
    of an agentic marketplace where people can build agents and buy or interact with
    each other’s agents.
  sec: 2880
  time: '48:00'
  who: Ranjitha
- line: MCP solves the problem of having one protocol to communicate with tools, but
    that’s it.
  sec: 2915
  time: '48:35'
  who: Ranjitha
- line: You mean marketplaces where, for example, an AI site reliability engineer
    can access data from New Relic, AWS CloudWatch, and other systems. MCP makes this
    easier.
  sec: 2929
  time: '48:49'
  who: Alexey
- line: Yes, MCP is useful if you don’t want to provide full API specs for custom
    tools. It abstracts your tools. The agent marketplace is different; it’s a complete
    agent solving a task. ChatGPT plugins are similar but not exactly the same.
  sec: 2964
  time: '49:24'
  who: Ranjitha
- header: 'Evaluation Strategy: Custom Datasets & System Benchmarks'
- line: How do you evaluate agents? For RAG, evaluation is simpler because the flow
    is fixed. With agents, we need to evaluate the answer, tool calls, parameters,
    and more.
  sec: 3077
  time: '51:17'
  who: Alexey
- line: Good question. RAG is not easy either; it takes time to build a system. Public
    benchmarks like SQuAD evaluate model capability, not your system. You need to
    create your own dataset that represents real users.
  sec: 3102
  time: '51:42'
  who: Ranjitha
- header: 'Testing Agents: Mocking Tools, Integration & Regression Tests'
- line: 'Agents multiply the challenge with multiple LLM prompts. You also need to
    evaluate if the tools are doing what they are supposed to do. We approached it
    like software engineering tests. The agentic system is like a software system:
    input gives predictable output.'
  sec: 3200
  time: '53:20'
  who: Ranjitha
- line: Integration tests mock inputs and assert outputs. For a calendar agent, 200–300
    test cases help ensure reliability. For S agents, mocking logs, metrics, and data
    sources is more complex but doable.
  sec: 3259
  time: '54:19'
  who: Ranjitha
- line: You mock tools to avoid external service calls. You check if the agent actually
    tries to communicate with them. For example, setting up a meeting calls the HR
    system to find a manager.
  sec: 3313
  time: '55:13'
  who: Alexey
- header: 'Goal‑based Evaluation: Outcome Assertions Over Exact Paths'
- line: 'I wouldn’t evaluate each path too strictly because LLMs can accomplish the
    same goal differently. Tool calls must consult the true source. For example, two
    ways exist to find a skip level: directly or by traversing an org chart. Both
    are acceptable. Adding more data sources increases variability.'
  sec: 3362
  time: '56:02'
  who: Ranjitha
- line: Evaluation focuses on whether the goal was achieved, not the exact path. Creating
    a calendar invite with correct parameters is the assertion. Domain knowledge is
    necessary.
  sec: 3443
  time: '57:23'
  who: Alexey
- header: 'Specialization Challenge: Why Generic Agent Solutions Lag'
- line: Making a generic solution hasn’t happened yet because these tasks are very
    specific.
  sec: 3491
  time: '58:11'
  who: Ranjitha
- line: We prepared many questions, but we only covered a few today. It was super
    fun talking to you. You are very knowledgeable, and I learned new things. Time
    flew by. Thanks a lot for joining us today, and thanks everyone for joining as
    well.
  sec: 3497
  time: '58:17'
  who: Alexey
- header: Closing Thoughts & Future Outlook for Agent Engineering
- line: It’s a good question, about replacing SEs with agents. Maybe if I were an
    SE, I would say, “We’ll get back to you. Watch our space at NewWord.ai.”
  sec: 3546
  time: '59:06'
  who: Ranjitha
- line: Thanks a lot. We’ll see you soon in our next events.
  sec: 3563
  time: '59:23'
  who: Alexey
description: Build autonomous LLM agents with RAG, orchestration & context engineering
  - master SRE automation, testing, evaluation metrics and latency/cost tradeoffs.
intro: 'How do you build and evaluate truly autonomous LLM agents that balance retrieval,
  orchestration, and real-world SRE needs? In this episode, Ranjitha Gurunath Kulkarni
  — Staff ML Engineer at NeuBird.ai with earlier LLM and assistant work at Dropbox
  and Microsoft and an LTI master’s from Carnegie Mellon — walks through practical
  engineering trade-offs for autonomous LLM agents and retrieval-augmented generation
  (RAG). <br><br> We cover a clear agent definition (autonomy, objectives, LLMs),
  agent orchestration tools and memory/knowledge stores, planning strategies from
  single-step to self-reflection, and implementation choices: prompts, SDKs, tool
  wrappers, and the code‑vs‑natural‑language agent trade-offs. Ranjitha digs into
  context engineering techniques (chunking, metadata, wrappers), RAG realities (latency,
  cost, GIGO), and when retrieval alone suffices versus when full agents are needed.
  She also maps SRE workflows to agents (logs, metrics, remediation), integration
  abstractions, framework trade-offs (LangChain, OpenAI Agents SDK, Small Agents),
  and evaluation strategy: custom datasets, mocking tools, regression tests, and goal‑based
  outcome assertions. <br><br> Listen to learn practical guidance for building, testing,
  and deploying autonomous LLM agents, and which architectures and evaluation approaches
  work best for production systems.'
dateadded: '2025-10-21'
duration: PT00H59M23S
quotableClips:
- name: Event Introduction & Community Links
  startOffset: 0
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=0
  endOffset: 192
- name: 'Early ML Projects: Image Search with OpenCV'
  startOffset: 192
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=192
  endOffset: 265
- name: Speech Recognition & Language Modeling Experience
  startOffset: 265
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=265
  endOffset: 297
- name: Transition to Recommendation Systems at Dropbox
  startOffset: 297
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=297
  endOffset: 352
- name: Question Answering & Early Agent Experiments
  startOffset: 352
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=352
  endOffset: 464
- name: 'Joining Noird.ai: Automating On‑call with Agents'
  startOffset: 464
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=464
  endOffset: 660
- name: 'Agent Definition: Autonomy, Objectives & LLMs'
  startOffset: 660
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=660
  endOffset: 751
- name: 'Agent Orchestration: Tools, Memory & Knowledge Stores'
  startOffset: 751
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=751
  endOffset: 910
- name: 'Planning Strategies: Single‑step, Multi‑pass & Self‑reflection'
  startOffset: 910
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=910
  endOffset: 1103
- name: 'Implementation Approaches: Prompts, SDKs & Tool Wrappers'
  startOffset: 1103
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1103
  endOffset: 1198
- name: 'Code Agents vs Natural‑Language Agents: Trade‑offs'
  startOffset: 1198
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1198
  endOffset: 1281
- name: 'Context Engineering: Designing Effective LLM Inputs'
  startOffset: 1281
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1281
  endOffset: 1370
- name: 'SRE Workflows Modeled by Agents: Logs, Metrics & Remediation'
  startOffset: 1370
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1370
  endOffset: 1499
- name: 'Integration Abstractions: Handling Diverse Tooling'
  startOffset: 1499
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1499
  endOffset: 1770
- name: 'RAG Reality Check: Latency, Cost & Garbage‑In/Garbage‑Out'
  startOffset: 1770
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1770
  endOffset: 1898
- name: 'Retrieval Limitations: Reworking Backends for LLM Context'
  startOffset: 1898
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1898
  endOffset: 1968
- name: 'Context Engineering Techniques: Chunking, Metadata & Wrappers'
  startOffset: 1968
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=1968
  endOffset: 2171
- name: 'Agentic RAG: Using Retrieval as a Tool Within Agents'
  startOffset: 2171
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2171
  endOffset: 2259
- name: 'Use Cases: When RAG Is Enough vs When Agents Are Needed'
  startOffset: 2259
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2259
  endOffset: 2430
- name: 'Dynamic Planning Example: Calendar & Meeting Assistant'
  startOffset: 2430
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2430
  endOffset: 2586
- name: Dropbox Dash & AI Productivity Assistants for Enterprises
  startOffset: 2586
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2586
  endOffset: 2648
- name: 'Framework Choices: Build from Scratch vs Use Libraries'
  startOffset: 2648
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2648
  endOffset: 2760
- name: 'Framework Trade‑offs: LangChain, OpenAI Agents SDK, Small Agents'
  startOffset: 2760
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2760
  endOffset: 2880
- name: Agent Marketplaces & Tool Protocols (MCP)
  startOffset: 2880
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=2880
  endOffset: 3077
- name: 'Evaluation Strategy: Custom Datasets & System Benchmarks'
  startOffset: 3077
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=3077
  endOffset: 3200
- name: 'Testing Agents: Mocking Tools, Integration & Regression Tests'
  startOffset: 3200
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=3200
  endOffset: 3362
- name: 'Goal‑based Evaluation: Outcome Assertions Over Exact Paths'
  startOffset: 3362
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=3362
  endOffset: 3491
- name: 'Specialization Challenge: Why Generic Agent Solutions Lag'
  startOffset: 3491
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=3491
  endOffset: 3546
- name: Closing Thoughts & Future Outlook for Agent Engineering
  startOffset: 3546
  url: https://www.youtube.com/watch?v=x2AAjqz2XmM&t=3546
  endOffset: 3563
---

Links:

* [Linkedin](https://www.linkedin.com/in/ranjitha-gurunath-kulkarni){:target="_blank"}