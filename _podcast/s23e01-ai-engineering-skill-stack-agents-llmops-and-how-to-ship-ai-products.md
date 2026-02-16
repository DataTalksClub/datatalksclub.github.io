---
episode: 1
guests:
- pauliusztin
ids:
  anchor: datatalksclub/episodes/AI-Engineering-Skill-Stack--Agents--LLMOps--and-How-to-Ship-AI-Products---Paul-Iusztin-e3enonn
  youtube: 6bUO43k2lVU
image: images/podcast/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/AI-Engineering-Skill-Stack--Agents--LLMOps--and-How-to-Ship-AI-Products---Paul-Iusztin-e3enonn
  apple: https://podcasts.apple.com/us/podcast/ai-engineering-skill-stack-agents-llmops-and-how-to/id1541710331?i=1000748569537
  spotify: https://open.spotify.com/episode/5MBy03EQj7gwwkSpbkx1N8
  youtube: https://www.youtube.com/watch?v=6bUO43k2lVU
season: 23
short: 'AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products'
title: 'AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products'
transcript:
- header: 'From code to cars: Paul’s journey to AI'
- line: Hi everyone, welcome to our event. This event is brought to you by Data Talks
    Club, which is a community of people who love data. We have weekly events, and
    today is one of such events. This screenshot is very outdated, but do not forget
    to subscribe to our YouTube channel if you haven't yet. We also have an amazing
    Slack community where you can hang out with other data enthusiasts.
  sec: 0
  time: 0:00
  who: Alexey
- line: During today's interview, you can ask any question you want. There is a pinned
    link in the live chat; click on that link to ask your questions and we will be
    covering them during the interview. You should definitely subscribe someday. Please
    also follow Paul on LinkedIn, as he shares a lot of great stuff. I was referring
    to the course you are working on.
  sec: 25
  time: 0:25
  who: Alexey
- line: Today we have Paul, and it is very nice to have him here for the interview.
    Thanks, Paul, for joining us. I have been following you on LinkedIn since you
    first appeared there. We already did one collaboration about your book, the LLM
    Engineers Handbook, about a year ago. It was really good, and I am happy to have
    you on the podcast so we can talk more.
  sec: 58
  time: 0:58
  who: Alexey
- line: We will talk about AI engineering, the book, and MLOps. We will also cover
    LLM Ops and all the things that Paul is known for. The content we create and the
    things we teach are pretty similar, so we will have a lot of things to discuss.
    I have your bio here, so I will read it out loud before we start. Paul is an AI
    engineer committed to helping developers create fully functional, production-grade
    AI products.
  sec: 89
  time: '1:29'
  who: Alexey
- line: He is the author of the bestselling LLM Engineers Handbook and leads the Agentic
    AI Engineering course. He is a founding AI engineer at a startup based in San
    Francisco. I did not know you were a founding AI engineer, which is amazing. He
    is also an author at Decoding AI magazine, where he assists engineers in moving
    beyond the proof of concept stage. With over 10 years of experience, Paul teaches
    comprehensive AI engineering from data gathering to deployment.
  sec: 147
  time: '2:27'
  who: Alexey
- line: You have a long bio, and many people here likely know you already. I learned
    a few new things about you, like your role as a founding engineer. I am sure we
    will talk about that during our time today. I am very happy to have you here.
    Welcome to the show.
  sec: 186
  time: '3:06'
  who: Alexey
- line: It is awesome to be here, Alexey. Should I start from the early beginning,
    moment zero? In high school, I was very lazy and did not do much, so I can easily
    skip that. School was pretty boring for me, and I think the most interesting part
    actually started when I got hired. I usually do not like school or university
    that much.
  sec: 201
  time: '3:21'
  who: Paul
- line: I focus more on my own projects rather than following courses or labs, as
    I get bored easily. I first got hired during my second university year in Timișoara,
    where I am from and currently located. I was hired as a backend engineer in Python.
    Ten years or more ago, I did not start with AI, but I knew that AI is done in
    Python. I just wanted any job that worked with Python, and that was the first
    one I found.
  sec: 264
  time: '4:24'
  who: Paul
- line: That was a good choice because back then, doing data science usually required
    using R. It is good that you started with the right language. I thought if you
    wanted to do data science, it had to be R.
  sec: 312
  time: '5:12'
  who: Alexey
- line: I was lucky enough in university to have a teacher who was obsessed with deep
    learning. He guided me and told me exactly what I needed to learn. I did my best
    to find places in the real world where I could learn everything I needed. I first
    started my journey as a software engineer hired for the backend, but I quickly
    jumped to frontend, React, and infrastructure. It was a small company, so I had
    the chance to work on everything.
  sec: 326
  time: '5:26'
  who: Paul
- line: That really sparked my love for system engineering, software engineering,
    and seeing things end-to-end. Afterwards, I knew I wanted to learn AI. As I was
    in Timișoara, I did not have a global mentality yet. I was just a kid wondering
    where I could find jobs in the town I lived in. I managed to grab one of the few
    AI research jobs available in my town.
  sec: 371
  time: '6:11'
  who: Paul
- header: Deep learning and the autonomous driving challenge
- line: I was lucky because of my teacher, Călin Pappa; without him, I would not have
    been in AI so early. I started doing deep learning on autonomous driving from
    day zero. I worked with 3D object detection, 3D tracking, and fusing multimodal
    data from images, radar, and lidars. It was very overwhelming, and I sometimes
    had to read a paper 20 times just to understand it. I was pretty good at math
    and understood the fundamentals, so I wasn't starting from zero.
  sec: 428
  time: '7:08'
  who: Paul
- line: In Romania, we do a lot of hardcore math, so we are well-prepared. Anyway,
    deep learning is on a completely different level. It is normal to be completely
    overwhelmed when you start in a new field. I was perseverant and okay with the
    fact that I needed to read some material many times. Back when we did not have
    LLMs, you had to search Google for every concept you did not understand.
  sec: 471
  time: '7:51'
  who: Paul
- line: Those were terrible times, but it allowed me to build fundamentals on how
    neural networks work. The work wasn't focused on software engineering as much
    as the research side. I was preparing datasets, training neural networks, and
    even deploying them. I had a chance to test Nvidia DGX systems and deploy them
    on a car to build a prototype autonomous vehicle. It was very naive, but it was
    cool for back then.
  sec: 504
  time: '8:24'
  who: Paul
- line: I eventually realized that I am not that into research. To be honest, it was
    really boring for me to just do experiments and compare metrics. I didn't want
    to just read papers and implement potential improvements repeatedly. I knew I
    wanted to go back into engineering. At the time, it was very confusing how to
    combine AI with engineering.
  sec: 541
  time: '9:01'
  who: Paul
- line: There were no jobs titled "AI Engineer" or "MLOps Engineer" that I was aware
    of. I was lucky enough to get a new job where they combined the two. We mostly
    took pre-built models and trained and deployed them. We did not necessarily tweak
    their architecture like I did in my research job. I realized that was another
    job title within the data space, and things started to click.
  sec: 576
  time: '9:36'
  who: Paul
- line: After a few months, I got into contracting. You basically open your own company
    and start selling your skills and services to companies worldwide. This was completely
    eye-opening for me because I could start working at companies from Germany, the
    UK, Israel, and the US. I did not necessarily want to move, so I could work from
    here while reaching a global market. I started working on really cool projects
    that had a huge impact.
  sec: 616
  time: '10:16'
  who: Paul
- line: I think that was the biggest breakthrough for me, as it was the beginning
    of a global mindset. COVID was very helpful in making that possible because it
    made this type of collaboration a lot more normal. Since then, I have only worked
    like that. I haven't worked for a company with an office in Romania since then,
    and I mostly work from home. I changed a couple of companies, but I mostly work
    in ML engineering and LLM Ops.
  sec: 668
  time: '11:08'
  who: Paul
- header: The transition to global product engineering
- line: I don't really want to label these roles too much because in non-corporate
    environments, you end up doing all of them. You need to take a model and build
    all the software around it to ship it. You build the infrastructure, scale it,
    and monitor it yourself. I worked at a service company from Israel where we built
    multiple smaller companies. That was very eye-opening for classical machine learning,
    NLP, and computer vision.
  sec: 729
  time: '12:09'
  who: Paul
- line: Then I started working at a generative AI company in the Hollywood industry
    called Metaphysic. They were recently acquired and were building software for
    editing high-quality professional videos for the movie industry. They focused
    on doing the movie end-to-end and actually shipped real-world movies. I only remember
    the exact name, but they were popular films. I was mostly focused on building
    internal tooling to make those models accessible.
  sec: 781
  time: '13:01'
  who: Paul
- line: We have already quite a few questions from listeners. From what you described,
    your career path has made you more of an engineer. You don't really care about
    labels like AI engineer or ML engineer, as long as you can build things. You do
    whatever it takes to get the job done. I was doing something similar, although
    my title was data scientist by inertia.
  sec: 867
  time: '14:27'
  who: Alexey
- header: 'Survival guide: Data science vs. AI engineering'
- line: What do you think about the title "Data Scientist" and its current employability?
    A listener with seven years of experience is finding it difficult to find new
    jobs with that title. Is the AI job market changing how we should frame our experience?
  sec: 913
  time: '15:13'
  who: Alexey
- line: This is tricky because it has multiple dimensions to it. The data science
    role itself is still employable, but you need to repackage it differently. Algorithms
    and hiring managers care about how the game is played. You need to understand
    what people are looking for regarding keywords and specific skills. You may even
    have the skills, but you need to reframe them to match how people actually search
    for them.
  sec: 942
  time: '15:42'
  who: Paul
- line: Going into contracting work was a huge breakthrough for me because I wasn't
    looking for jobs in a particular place. I was looking for jobs in almost all the
    world. That provides a huge leap in possibilities compared to a local search.
    For me, that usually boiled down to Europe and North America. In this current
    world, your location doesn't really matter at all for most jobs.
  sec: 995
  time: '16:35'
  who: Paul
- line: Traditionally, data scientist meant a focus on exploratory work and modeling
    rather than engineering. At my previous company, OLX, we needed both roles. Most
    of the effort for data scientists was on data preparation and experiments, while
    ML engineers focused on deployment. I think that with LLMs, the tasks data scientists
    used to do have become much easier. Can an ML engineer now do the work of a data
    scientist with an LLM?
  sec: 1047
  time: '17:27'
  who: Alexey
- line: For things like term prediction in smaller companies, are data scientists
    really needed? I heard the same sentiment from others who are out of a job. Does
    the data scientist role only kick in for very tricky improvements?
  sec: 1122
  time: '18:42'
  who: Alexey
- line: I agree that data scientists kick in when you want to take a model from 97%
    to 98% accuracy. However, we live in a very hyper-based market where everyone
    is trying to do things with LLMs. They often don't care about traditional data
    science anymore. Executives sometimes just want to use an LLM for everything instead
    of XGBoost. This is the current trend in the industry.
  sec: 1147
  time: '19:07'
  who: Paul
- line: I understand this trend is often wrong. I recently consulted for a company
    building a property evaluation model to predict apartment prices. They tried using
    an LLM for that, and it didn't work. Any data scientist would have told them to
    just use XGBoost. Why did they even think about an LLM for those tasks?
  sec: 1193
  time: '19:53'
  who: Alexey
- line: I was into this hype five years ago when I wanted to use neural networks for
    simple regression problems. They just don't work well for that and are complete
    overkill. Often you don't have enough data, and the mapping is much easier than
    what a complex model assumes. Throwing a billion-parameter model at a regression
    problem is probably even worse. Sometimes you cannot change their opinion until
    they see that things don't work anymore.
  sec: 1238
  time: '20:38'
  who: Paul
- line: You just need to be adaptive and understand the game that you're playing.
    I checked LinkedIn for Germany and found more jobs for data scientists than ML
    engineers. However, the numbers are suspiciously low for a big country.
  sec: 1291
  time: '21:31'
  who: Paul
- header: The full-stack AI engineer skill stack
- line: What do you think are the must-have skills required for an AI engineer in
    2026? How do you see yourself as a founding AI engineer? Can you tell us what
    you actually do on a daily basis?
  sec: 1349
  time: '22:29'
  who: Alexey
- line: I am an engineer at a startup where I have to do everything. This will change
    from company to company, but I can describe my daily routine. We built a vertical
    AI agent for finance which contains a UI built in TypeScript and React. It contains
    a FastAPI backend plus all the AI logic like agents and RAG. We host everything
    on AWS, and I handle all the infrastructure myself.
  sec: 1388
  time: '23:08'
  who: Paul
- line: The reality is that I do everything end-to-end. I was very reluctant to attach
    frontend work to the AI engineer job at first. However, as I understand how powerful
    tools like Claude are, I think the AI engineer is the new software engineer. You
    need to be a full-stack AI engineer to some extent. You need to do frontend, backend,
    and build AI agents and workflows.
  sec: 1443
  time: '24:03'
  who: Paul
- line: Knowing SQL and how to design a database is essential to shipping a product.
    I know this is overwhelming, but that's the reality. I expect that most companies
    will expect this from their engineers. As you go into bigger companies, you will
    start to be more niche. Then maybe you'll tackle fine-tuning or writing GPU kernels,
    but those are really specialized at the moment.
  sec: 1482
  time: '24:42'
  who: Paul
- line: Most jobs will probably be taking closed-source or open-source models and
    building the software around them. This means starting from the UI to the backend
    and translating manager needs to software. Personally, I think the job of an AI
    engineer is harder because you need to own more. Before, if you were a backend
    engineer, FastAPI was your only domain. Everything outside of that was someone
    else's problem.
  sec: 1519
  time: '25:19'
  who: Paul
- line: I was like that, and it was really hard for me to accept this change. You
    don't really need to write all that code yourself, though?
  sec: 1576
  time: '26:16'
  who: Alexey
- line: I think a very important skill is knowing how to use AI tools to actually
    build the system. You translate requirements to build the software and understand
    how to structure it. I want to highlight the skills needed to evolve and maintain
    the software without building a mess. These are skills in themselves which are
    not that straightforward. I treat AI agents like interns who have a lot of energy.
  sec: 1583
  time: '26:23'
  who: Paul
- line: If I don't watch them, they go crazy. A few days ago, my agent deleted a test
    because it was not passing. It said it was an existing regression and thought
    the problem was solved by removing the test. I noticed it when it said 90 tests
    were passing instead of 100. Sometimes it says it doesn't have enough tokens to
    solve the problem.
  sec: 1669
  time: '27:49'
  who: Paul
- line: AI engineers now are people who do everything it takes to build AI into the
    product. They don't only know how to make calls to OpenAI or Gemini, but they
    know how to build everything around it. They handle the full end-to-end experience
    including the backend and frontend.
  sec: 1721
  time: '28:41'
  who: Alexey
- header: Mastering RAG and knowledge management
- line: I also think that you need some good data engineering skills. You need to
    write data pipelines to populate your agent's memory and index it properly. I
    think that actually the hardest part of an engineer is around knowledge management.
    How can you model your knowledge in such a way that it's accessible by your agent?
    That's where things such as RAG and knowledge graphs kick in.
  sec: 1752
  time: '29:12'
  who: Paul
- line: I think that is the most interesting part where the algorithmic knowledge
    is needed. Fine-tuning is not always the way to go right now. Managing your data
    so it is easily thrown into the context of the agent is a very hard problem. Otherwise,
    tools like Claude can solve most of the frontend and backend. If you put the right
    ecosystem in place, you don't need to write as much code anymore.
  sec: 1812
  time: '30:12'
  who: Paul
- line: You still need to take a look at the code, right?
  sec: 1844
  time: '30:44'
  who: Alexey
- line: You still need to be the architect. You need to understand how the layers
    are organized. I am thinking about this sometimes because I may run out of premium
    requests on GitHub Copilot. I have backups like Claude, but I wonder how quickly
    I could fix something myself. For important projects, I try to understand everything
    that is happening in the project.
  sec: 1851
  time: '30:51'
  who: Paul
- line: Right now, tools like Claude Pro are discounted and cheaper than using a plain
    API. At some point, companies will stop subsidizing it and you will pay more.
    In that case, knowing what is happening in your codebase is also important?
  sec: 1910
  time: '31:50'
  who: Alexey
- header: 'The generalist edge: Learning with AI'
- line: I always read the code that is generated. I usually use Claude or Cursor in
    edit mode and read everything that they output. I don't think that you need to
    write code, but you will read and understand a lot more code. Since I started
    using Claude, I know a lot more TypeScript and SQL. My knowledge expanded because
    I am exposed to so many more elements.
  sec: 1937
  time: '32:17'
  who: Paul
- line: I read a lot more than if I were trying to write a line of TypeScript that
    I haven't touched in years. I don't need to care about small syntax details like
    semicolons. I care about how the code should look and how things should scale.
    You should care more about important things than syntax.
  sec: 1984
  time: '33:04'
  who: Paul
- line: You have 10 years of experience and you are a generalist. Since your first
    job, you were doing backend, frontend, and infrastructure. For you, it is natural
    to say that an AI engineer basically owns everything. But for people who do not
    have this variety of generalist experience, what would you recommend they do?
    How can they have this end-to-end ownership of their code?
  sec: 2007
  time: '33:27'
  who: Alexey
- line: You have to be junior at something at some point. Until last month, I had
    never designed a UI in my life. I have done it now because there was no choice
    and people told me to do this end-to-end. You need to adapt to what is needed.
    I told them that I never did this in my life, so now I am a junior at doing UI
    work.
  sec: 2070
  time: '34:30'
  who: Paul
- line: I try to collaborate with others as much as possible. They are doing the heavy
    lifting, but I am trying to understand their process and the code. Learn from
    people who already know the skill and be okay with the fact that you don't know
    it yet. Be open with them and ask dumb questions. Put yourself again as a junior
    in there and learn.
  sec: 2108
  time: '35:08'
  who: Paul
- line: It is cool to know that you can create a UI if you need to.
  sec: 2148
  time: '35:48'
  who: Alexey
- line: I still think I suck at doing beautiful designs, but it is a beginning. I
    already have the basic skills in place. You can quickly build something for an
    internal tool and let people use it. Then you can iterate on things based on their
    feedback. Most probably, a real designer will do the UI in Figma, and you will
    implement it.
  sec: 2154
  time: '35:54'
  who: Paul
- line: That is essentially a full-stack job. Now with AI, you can hook an MCP to
    Figma. Claude can just read all the design from there and build it for you. You
    don't have to be a pro in this; you just need to have the full context to connect
    the dots.
  sec: 2206
  time: '36:46'
  who: Paul
- line: I want to summarize the must-have skills required for an AI engineer in 2026.
    First, using AI assistants. Second, reading a lot of code and knowing how to design
    your codebase so AI cannot break it. Software engineering experience really helps.
    You also need an open-minded mentality to explore frontend and backend.
  sec: 2236
  time: '37:16'
  who: Alexey
- line: I guess being a generalist and owning multiple things is key. Ownership is
    a personal trait you need for this. Is there anything else, like using LangChain
    or setting up evaluation frameworks?
  sec: 2292
  time: '38:12'
  who: Alexey
- line: Evaluation is probably one of the most important skills. Even if the code
    is purely generated, a human will always be introduced in the loop. You need to
    understand how to connect them to look at the data and measure correctness. As
    these tools progress, we will care more about how the functionality works than
    how the code looks. If you don't know how the code works, you need a good measurement
    strategy.
  sec: 2321
  time: '38:41'
  who: Paul
- line: I expect AI evaluations to be a skill that will just grow and grow. I expect
    data scientists in the future will do very complex evaluation layers. My bet is
    huge in this direction. I am coming from the data science background where I was
    exposed a lot to search and recommendations. That knowledge translated really
    well to AI engineering work.
  sec: 2366
  time: '39:26'
  who: Paul
- line: The training part is not really required now, but the validation part is.
    Having a proper validation set is how we did it before. We had this gold standard
    dataset and we applied the model and saw the results. Now we do the same but with
    our AI models or agents. For me, it was really helpful.
  sec: 2416
  time: '40:16'
  who: Alexey
- line: I also think that being data literate is very important. You need to know
    how to split your data and how to properly do evaluations. You should understand
    correlations, causations, and probabilistic statistics. Knowing how to visualize
    your data is also super important. You will need to design and understand things
    more than you will need to write code.
  sec: 2454
  time: '40:54'
  who: Paul
- line: If you just need to design and evaluate things, you don't need all those specialists
    who write code. You just need a few people who actually architect it. You go a
    little bit higher level. In corporate environments, you will probably still see
    specialized people who fine-tune models. Those are specialized areas which probably
    pay really well if you go in there.
  sec: 2499
  time: '41:39'
  who: Paul
- header: Technical pillars for shipping AI products
- line: The core skills for AI engineers are being able to create and evaluate agents.
    You also need open-mindedness to use AI assistants to build everything around
    them. Knowing how to create agents and evaluate them while building data pipelines
    is key. If you want your agent to use data via RAG, you need to know how to ingest
    that data and make it available.
  sec: 2548
  time: '42:28'
  who: Alexey
- line: When it comes to technologies, I personally don't like LangChain. I like Pydantic
    AI, but I am curious what tech stack you would recommend right now. A listener
    wants to transition to an AI engineer role and build some projects. They want
    to focus on using the recommended stack. Which tools would you recommend for their
    projects, or does it even matter?
  sec: 2587
  time: '43:07'
  who: Alexey
- line: I do not think the framework matters that much to be honest. I personally
    use LangChain, but more for their utilities. They have nice utilities to access
    specific models and structure outputs. Otherwise, I usually build my own code.
    I think owning the planning and execution is easier to own on your end in the
    long run.
  sec: 2629
  time: '43:49'
  who: Paul
- line: It is better than delegating it to a framework which just adds useless abstractions.
    Frameworks like LangChain have to implement abstractions to make it possible to
    go from OpenAI to Anthropic. You are not working with a plain API, which adds
    some levels of abstraction. LangChain is very confusing for me because it is abstraction
    over abstraction. I completely agree regarding the utilities they provide.
  sec: 2666
  time: '44:26'
  who: Paul
- line: These utilities are more useful when you experiment. Once you go towards a
    serious project, you will need to write them from scratch. You will need custom
    logic that is very particular to your data. Trying to hijack those abstractions
    will be a pain. I tried to do that and ended up with a Frankenstein that was hard
    to understand.
  sec: 2716
  time: '45:16'
  who: Paul
- line: Other tools that I would recommend are durable workflows like Prefect or Dagster.
    They are used during ingestion and during retrieval. They are similar to data
    orchestrators but modeled for this agentic world. Instead of having one orchestrator
    for data and one for agents, you can have one for everything. They provide queues
    and retries and basically make your code resilient.
  sec: 2749
  time: '45:49'
  who: Paul
- line: You also need some sort of LLMOps tool to monitor your code and store your
    traces. I usually use Arize Phoenix, which is open source. I have not heard about
    Arize Phoenix before.
  sec: 2791
  time: '46:31'
  who: Paul
- line: Other tools I heard good things about are LangSmith, BrainTrust, or LangFuse.
    I usually stick to a tool once I find one I like. From what I heard, they are
    all pretty similar. I use Logfire because it is a one-line integration with Pydantic
    AI. Typically, if you use a framework's own observability platform, the integration
    is super simple.
  sec: 2814
  time: '46:54'
  who: Paul
- line: Is it easy to configure different tools together? I used LangChain and LangGraph
    and it was just one line of code to add a trace. You just need to understand what
    a trace, a span, and a thread are. A thread is like a collection of traces because
    they compile the whole conversation. I see.
  sec: 2871
  time: '47:51'
  who: Paul
- line: When I start a conversation with ChatGPT, the agent is thinking. There are
    a few back and forth calls to OpenAI and then the answer. This is the first trace.
    Each request and response between you and the AI is a trace?
  sec: 2911
  time: '48:31'
  who: Alexey
- line: Yes, and it usually involves multiple steps behind the scenes. Everything
    that happens between a request and response is a trace. Your whole conversation
    is a thread which is a collection of user inputs and answer outputs. These tools
    provide you with a way to log a thread ID and collect conversations. Then you
    can sample data at the conversation level.
  sec: 2948
  time: '49:08'
  who: Paul
- line: To answer the anonymous question, you can use a tool for orchestrating your
    agents. It is useful to know how they work so you can implement them yourself
    later. For a start, you can just use a framework and then switch to whatever works
    when they stand in your way. It probably will not happen for a simple personal
    project?
  sec: 3033
  time: '50:33'
  who: Alexey
- line: It depends, but most probably not. I would personally stick to one database
    instead of choosing many specialized ones. Your project will likely be good enough
    in one database like MongoDB or Postgres. You can do almost everything in them.
    Of course, at enterprise scale, you might need Neo4j or Qdrant.
  sec: 3071
  time: '51:11'
  who: Paul
- line: Most applications are not there yet. Pick any project and work on this end-to-end.
    How do I pick projects for my portfolio? I want to transition to an AI engineer;
    what kind of agents should I implement? I always like to touch a problem that
    I am passionate about in my real life.
  sec: 3218
  time: '53:38'
  who: Paul
- header: Portfolio secrets and the "second brain"
- line: I think those kinds of problems are a lot nicer to solve than something generic.
    You get more drive to actually solve them and you are already the domain expert.
    Otherwise, owning the data can become super tricky and you can lose a lot of time.
    This is one dimension you should think about. You may have seen my "second brain"
    projects.
  sec: 3245
  time: '54:05'
  who: Paul
- line: These are all about owning your digital data and doing search on top of it.
    This includes your personal notes, tasks, and to-dos. If I have my Notion, that
    would be my digital data. It is your projects, journals, and everything that you
    save. It is complicated because data is siloed and you need a unified way to access
    it.
  sec: 3319
  time: '55:19'
  who: Paul
- line: I recently built an agent that downloads a zip archive from GitHub and goes
    through the code. It knows the codebase and you can ask it questions. It uses
    tools like grep and reading files to explain how code works. I discovered that
    if you clone this with Claude, it is actually easier. But it was fun to implement.
  sec: 3391
  time: '56:31'
  who: Alexey
- header: The future of the LLM engineer’s handbook
- line: You could use a GitHub MCP server and put it in your chat. This is how you
    learn things. Tell us briefly about the book and if you have any plans to update
    it. My book was written two years ago when the space was very different. People
    were figuring out RAG, not agents.
  sec: 3481
  time: '58:01'
  who: Paul
- line: The book is built around the idea of owning a system end-to-end. We explain
    how to gather data from the internet and curate it. We co-authored it with Maxime
    Labonne, who is a legend in fine-tuning. We did not include anything about agents
    and orchestration because it wasn't really a thing then. Back then, GPT-3.5 wasn't
    very good at producing code.
  sec: 3525
  time: '58:45'
  who: Paul
- line: They did not even have tool fine-tuning or reasoning. Because of that, we
    are actually working on a new book. I just wrapped up the outline this weekend.
    It is a refresh, but it will be a completely new book. We realized we needed to
    change so much that a second edition was not enough.
  sec: 3595
  time: '59:55'
  who: Paul
- line: The idea is very fresh, so I cannot tell a lot more details. We learned a
    lot from the first edition about what is worth discussing. We want to make something
    super refined this time. We said let's just create a new book; it's easier. Where
    do you plan to share the updates?
  sec: 3627
  time: '1:00:27'
  who: Paul
- line: LinkedIn, X, and Substack are the places. I want to openly talk while I build
    it and ask questions when I am not sure. Building in public helps to get feedback
    earlier. The course is an Agentic AI engineering course. We focus on how to think
    about workflows and agents.
  sec: 3674
  time: '1:01:14'
  who: Paul
- line: We cover orchestration, context windows, memory, and tools. We have three
    chapters including foundational knowledge and capstone projects. One project shows
    how to write professional content using evaluator-optimizers. The other is a deep
    research agent that gathers data from the internet, GitHub, and YouTube. We manage
    to create articles up to 30 pages long.
  sec: 3724
  time: '1:02:04'
  who: Paul
- line: We did a lot of context engineering to show how to control the output. We
    show how to control the style and structure of the document. As an engineer, you
    often need to output documents or reports. This problem translates to many common
    engineering tasks. In part three, we have many lessons on AI evals.
  sec: 3811
  time: '1:03:31'
  who: Paul
- line: We show how to deploy everything to GCP and scale it. It is really end-to-end,
    but with no UI. We shipped it as an MCP server and leveraged the UI from Cursor
    and Claude. I would do the same because I am not a UI expert. I shared Paul's
    LinkedIn in the live chat and description.
  sec: 3863
  time: '1:04:23'
  who: Paul
- line: Decodingai.com is also a great place to find your work. I checked and you
    have over 90,000 followers on LinkedIn. Great job on that. I need to catch up
    with you. We unfortunately don't have more time today. I think I can speak with
    you forever.
  sec: 3901
  time: '1:05:01'
  who: Alexey
- line: Maybe we can do this another time and continue. Once you go through the book
    milestones, it would be interesting to talk. I am a book writer myself and it's
    been a while since I did it. For me, it was a "never again" situation, but years
    pass and it has to be done.
  sec: 3933
  time: '1:05:33'
  who: Alexey
- line: Thanks, Paul, for joining us and answering our questions. We managed to tackle
    only three or four from the audience, so there are 14 left. I can share these
    with you for your future posts. If you follow Paul on LinkedIn, he will answer
    these questions in his next posts. Thanks everyone for joining us today.
  sec: 3974
  time: '1:06:14'
  who: Alexey
- line: Thank you again, Alexey, for inviting me. Thanks to everyone for joining this
    chat and see you next time. Have a great week everyone.
  sec: 4014
  time: '1:06:54'
  who: Paul
---

Links:

* [Linkedin](https://www.linkedin.com/in/pauliusztin/){:target="_blank"}
* [Website](https://www.pauliusztin.ai/){:target="_blank"}