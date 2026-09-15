---
episode: 3
guests:
- pauldomanski
ids:
  anchor: datatalksclub/episodes/Running-a-Company-on-a-Multi-Agent-Dispatch-System---Paul-Domanski-e3obkm7
  youtube: fxVSQteBnmg
image: images/podcast/s25e03-running-company-on-multi-agent-dispatch-system.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/Running-a-Company-on-a-Multi-Agent-Dispatch-System---Paul-Domanski-e3obkm7
  apple: https://podcasts.apple.com/us/podcast/running-a-company-on-a-multi-agent-dispatch/id1541710331?i=1000787893474
  spotify: https://open.spotify.com/episode/74xz7IFAivCupH34CzYI7V?si=SvgzV0lFS4KFJW5d4tjNSw
  youtube: https://www.youtube.com/watch?v=fxVSQteBnmg
season: 25
short: Running a Company on a Multi Agent Dispatch System
title: Running a Company on a Multi Agent Dispatch System
transcript:
- header: Welcome and Showcasing Demox
- line: Hi everyone, welcome to our event. This event is brought to you by DataTalks
    Club. There are some links in the description. Go click these links and join our
    community. Subscribe to our YouTube channel and like the video. There is also
    a pinned link in the live chat. Click on that link and use it for asking questions.
    Paul wanted to show us something. This is going to be exclusive because this is
    not going to be in our recorded audio only podcast. I am really curious what Paul
    is going to show us.
  sec: 0
  time: 0:00
  who: Alexey
- line: The main reason you reached out to me originally was because of the Headroom
    repo that I put together.
  sec: 33
  time: 0:33
  who: Paul
- line: This was born out of a post you made where you shared a screenshot on Twitter.
    You had multiple accounts of Claude with different usage limits. I think it was
    one of your projects and I wondered why you needed so many Claude sessions. Here
    we are talking about this, so please show us more.
  sec: 45
  time: 0:45
  who: Alexey
- line: It started with just the usage monitor and the account rotator, which I called
    Headroom. It was essentially just a way to automatically rotate accounts. Can
    you see my screen?
  sec: 75
  time: '1:15'
  who: Paul
- line: Yes. How many accounts do you have?
  sec: 93
  time: '1:33'
  who: Alexey
- line: Right now I am using six Claude accounts, all max 20x. I also have two Codex
    accounts which I am using. The whole reason why I started building this multiplexer,
    which I call Demox, is that it essentially lives on top of Ghosty and CMAX. I
    wanted a connected hub where I could manage all of my agents, almost like an agentic
    operating system that does everything in one place. Instead of having Claude Code
    living in different windows and browser use in another, I wanted a unified layout
    that worked for my specific style of work.
  sec: 94
  time: '1:34'
  who: Paul
- line: As you can see here, I can rotate between accounts manually or I can lock
    accounts for certain jobs. I have all of my projects along the left, my own work
    over here, and I am building onto this within Demox. There were just a lot of
    little things that were not perfect for me when working with agents with multiple
    different surfaces. I feel like we are in this age of malleable software now where
    you can build whatever you want to fit your specific needs, workflows, and tastes.
  sec: 137
  time: '2:17'
  who: Paul
- line: I went ahead with this, and as usual with AI projects, it started off as a
    simple idea and then expanded into something much bigger that is now taking up
    a lot of my time. This is still obviously being worked on, but the goal is to
    have a detachable chat interface with a browser. It will essentially become a
    browser within it as well. I want to replace my entire use of agent management
    and browser within my own little ecosystem.
  sec: 172
  time: '2:52'
  who: Paul
- line: Obviously, all of the agents communicate with each other and are working autonomously
    all the time. I thought that would be a good way to kick things off because it
    shows how quickly things move from my tweet about Headroom towards something that
    is a lot more robust.
  sec: 210
  time: '3:30'
  who: Paul
- line: Demox and CMAX sound suspiciously similar to tmux. Is it a coincidence or
    what are these things?
  sec: 227
  time: '3:47'
  who: Alexey
- line: Terminal multiplexers are essentially running on your computer. Instead of
    running a terminal directly on my Mac, these tmux panes are enduring. They can
    run by themselves if my laptop is closed or if I am offline. Nothing is interrupted
    unless it is reliant on my local tunnel, which it can also do.
  sec: 234
  time: '3:54'
  who: Paul
- line: There is a tunnel that runs directly onto my Mac so it can work with my Mac
    directly. It is essentially just a way to keep my agents working autonomously
    over long periods of time. All of these are actually mounted within tmux as instances.
    They automatically boot up as soon as I open Demox.
  sec: 262
  time: '4:22'
  who: Paul
- line: What are CMAX and Demox?
  sec: 290
  time: '4:50'
  who: Alexey
- line: This is where it came from. CMAX is just a very clean, nice multiplexer. It
    also allows you to open tabs and split your panes. You can have multiple windows,
    and one of them can be a browser for example. This is a very bare bones version.
  sec: 295
  time: '4:55'
  who: Paul
- line: A lot of what I wanted was to have my own customized look and feel about it.
    Mine also does the splitting, and it can split into a project terminal or a bare
    shell where I can just type. The other thing that I built in that was not there
    is an inbox. When I have all these agents moving fast through a lot of work, I
    can lose track of things that need my attention. It actually loads when there
    is something that needs my attention and gives me an inbox notification.
  sec: 318
  time: '5:18'
  who: Paul
- line: I can then go in there and respond to the agent directly. I found that when
    using CMAX, everything would flow so quickly and I was keeping track of so many
    different agents that I would lose track of what one agent was busy with. I started
    building in solutions for stuff like that. With software before, you would just
    put up with all of these little inconveniences because it was really difficult
    to build software. Now we are in a stage where I think it is a lot more achievable
    for even a non-coder to build a system that suits their needs.
  sec: 353
  time: '5:53'
  who: Paul
- line: I am completely a non-coder. Everything that I build is coded just based on
    my needs.
  sec: 393
  time: '6:33'
  who: Paul
- line: That is very interesting. I think everything that you showed right now is
    actually valuable even without video. You can probably stop sharing your screen.
    Most of the things you talked about make sense without video too.
  sec: 398
  time: '6:38'
  who: Alexey
- line: If you are listening to this right now and you want to check what Paul was
    showing, I recommend going and checking YouTube at the beginning where he was
    showing these things. It is interesting how many people are converging to building
    similar stuff. I am building something similar for my workflow, and a friend of
    mine in Berlin is building something similar. Because our workflows are a tiny
    bit different, what I built is not necessarily something you would want to use.
    The main building blocks are the same.
  sec: 417
  time: '6:57'
  who: Alexey
- line: We have a server where these things are running, and we connect to the server
    using SSH. Then we use tmux so the sessions are durable. There is an interface
    on top of this tmux that is specific to our needs and our workflows. I do not
    have so many Claude accounts. I only have one Claude and one Codex.
  sec: 469
  time: '7:49'
  who: Alexey
- line: I recently started experimenting with Groq. I do not know if you use it.
  sec: 491
  time: '8:11'
  who: Alexey
- line: I have not experimented with it yet, but I have heard it is pretty good.
  sec: 497
  time: '8:17'
  who: Paul
- header: Paul's Background in Film and Digital Marketing
- line: It is good. When I run out of usage limits for Claude and Codex, which happened
    last week, I have a backup plan. Tell us more about yourself. You said you are
    a non-coder and you completely coded it. What is your background? What did you
    do before doing all this stuff?
  sec: 499
  time: '8:19'
  who: Alexey
- line: I started off in film actually. I went to film school and was a video editor
    and director. I wrote movies and eventually ended up doing some adverts and TV
    shows. The money in South Africa in that industry was not enough. I started hustling
    with my housemate who was in digital marketing.
  sec: 526
  time: '8:46'
  who: Paul
- line: I started doing a lot of affiliate marketing, Meta ads, and Google ads. I
    have been doing that for the last 10 years. It is interesting how much digital
    marketing and building with AI have in common. It is a lot of finding new angles,
    fresh solutions, optimizing, and fixing things as you go. As soon as AI started
    to become super prevalent, I decided to go all in.
  sec: 554
  time: '9:14'
  who: Paul
- line: I started my agency. I am going to South African businesses and building them
    AI operating systems. I am doing that while building at the same time. I think
    that is extremely important in this game to keep up to date, to always be building.
    That is how you keep sharp and on trend.
  sec: 590
  time: '9:50'
  who: Paul
- line: One Claude Code subscription max is 200 dollars, and you have six of them.
    Codex is the same. In Europe you also need to add VAT on top of that, but roughly
    it is also 200 dollars. My rough calculation is just with these tools it is 1,600
    dollars per month. We all know that these tokens are subsidized.
  sec: 613
  time: '10:13'
  who: Alexey
- line: What you actually get from a 200 dollar subscription is way more expensive
    than this 200. Still, if you do the math, 1,600 is not something that is easy
    to just take out of pocket and pay every month. The return on investment you are
    getting must be totally worth it. How do you get back this money that you spent?
    What are the commercials behind this?
  sec: 656
  time: '10:56'
  who: Alexey
- line: The first point I would make is that 1,600 dollars is what you would pay for
    a mid-level coder or an engineer. It is not an extremely big amount to pay for
    a single employee. If I frame it like that, I am getting so much out of these
    agents. I have them running sales 24 hours a day. They are researching prospects
    on LinkedIn, tailoring messages to their specific pain points, and running cold
    email for me in the background 24/7.
  sec: 682
  time: '11:22'
  who: Paul
- line: They are working to build my clients' work. With my next client that I am
    onboarding, I am starting to get them to subsidize the costs. I have been covering
    all of my own token costs up until now, but I feel like it is justifiable to expect
    the clients to pay for that as well. Also, considering the size of the programs
    that I install, I am not hunting for lots of small clients. I take on one or two
    big companies and charge accordingly.
  sec: 719
  time: '11:59'
  who: Paul
- line: My ROI comes in with a single closed client. The way I work with clients involves
    long-term contracts. They start off with a three-month program that transitions
    into a maintenance phase. During the maintenance phase, I do not have to dedicate
    as much time, but I am still tweaking their systems. I am also charging on top
    of that to install new agents.
  sec: 748
  time: '12:28'
  who: Paul
- line: After the three months that includes their entire operating system and a couple
    of agents installed, it transitions into a maintenance program with additional
    charges for new agents. Just three or four clients are essentially enough for
    me as a solopreneur to make a decent profit. The goal for me is to scale into
    a fully-fledged agency and have a physical presence in Cape Town. I want to get
    a few systems architects trained up to work alongside me. That is the goal over
    the next few months.
  sec: 778
  time: '12:58'
  who: Paul
- line: Your business is helping clients to do AI automation or AI transformation.
  sec: 816
  time: '13:36'
  who: Alexey
- line: It is becoming AI native. The more I do it, the more I realize that the real
    value is not in building them automations or agents. It is in giving them insight
    into their businesses. It is creating a source of truth that sits above their
    business and provides valuable insights. The other important thing is it gets
    them to ask the right questions.
  sec: 829
  time: '13:49'
  who: Paul
- line: Everybody thinks about asking questions of AI, but that is actually quite
    difficult to do. A lot of people who are not AI native struggle to imagine what
    questions they can ask. I build this oracle to advise them on what they should
    be asking about their business. It looks at their business from a unique perspective,
    identifies what is most important for the CEO to pay attention to, and suggests
    questions to ask. That is where I see the real value, more so than automating
    mundane tasks.
  sec: 859
  time: '14:19'
  who: Paul
- line: Do you focus on a specific vertical or who are the clients you work with?
  sec: 906
  time: '15:06'
  who: Alexey
- line: It ranges. I like the startup feeling and energy. I like chaos because I feel
    like AI cuts through it very effectively. I am pretty industry agnostic overall.
    I have one client who does offline attribution for ads and they have a ton of
    different tracking systems.
  sec: 911
  time: '15:11'
  who: Paul
- line: I am also working with a luxury beverage brand that operates around Europe
    and America. It is industry agnostic, and the problems are kind of similar. I
    find the AI does not need to care about what the business does. It just needs
    to be placed and installed correctly and connected to the right sources to be
    valuable.
  sec: 937
  time: '15:37'
  who: Paul
- header: Sales Pipeline and Client Onboarding
- line: You have your agent doing cold outreach to find clients. Let's say somebody
    booked a meeting with you. You have this meeting and they want to proceed. What
    happens next?
  sec: 969
  time: '16:09'
  who: Alexey
- line: The sales pipeline is quite long, which is to be expected with high ticket
    sales. I do not try to sell anything on a call. I find myself wanting more human
    contact and spending more time in person. It has fed into the way I built this
    agency. I try to get from the call into a room with a decision maker and spend
    time with the team.
  sec: 992
  time: '16:32'
  who: Paul
- line: By room, you mean an actual real-life meeting. You focus on companies that
    have a physical presence in Cape Town or Johannesburg.
  sec: 1027
  time: '17:07'
  who: Alexey
- line: Yes. The most important thing I realized is that in-person work is a lot more
    productive and effective. It also establishes trust and serves a lot of purposes.
    My goal after the first call is to build out a customized prototype for them before
    the call.
  sec: 1046
  time: '17:26'
  who: Paul
- line: That explains why you need so many agents. If you find a company and schedule
    a call, you already have an agent doing research about the company to get public
    data and build a prototype.
  sec: 1072
  time: '17:52'
  who: Alexey
- line: I try to get a few questions answered on my signup page. The goal is to find
    out the one question they would ask their company today, which I call the golden
    question. If it is something like why are their costs rising, I have a skill that
    my Claude agents use called a deep research goal. This fans out five or six sub-agents
    on different models to do a quorum of research on the prospect. It finds every
    piece of public information it can find and frames their pain point against what
    else we know about them.
  sec: 1105
  time: '18:25'
  who: Paul
- line: It comes up with an interview that I do with the agents where we discuss what
    the prototype will be. Once I am happy with the demo, I use Claude Design to build
    out the prototypes. I have a baseline reference of how the prototypes should look
    and what they should feature. Essentially, it is a guided tour of the AI operating
    system that takes them through each phase of installation. They are already living
    inside the product.
  sec: 1151
  time: '19:11'
  who: Paul
- line: I always give the product a personalized name that resonates with the company.
    The moment I know when something is working is when people start calling it by
    name. That second meeting after the initial call is generally in person, where
    I sit with the team.
  sec: 1197
  time: '19:57'
  who: Paul
- line: On your first call over Zoom, you show the prototype and give them a link
    to poke around. When you meet in person, they have already been playing with the
    tools and can give you feedback on what needs to be changed.
  sec: 1229
  time: '20:29'
  who: Alexey
- line: Exactly. I also use the transcript of that first call and feed it back to
    the agent. The agent does further research with more context on the business owner
    and updates the demo. The goal is to bring it as close to the vision and solving
    the problem as possible before I set foot in the office. By the time I get there,
    the second showing demonstrates how it has evolved from the rough prototype to
    something aligned with their vision.
  sec: 1265
  time: '21:05'
  who: Paul
- line: This carries through the trust and shows follow-through. It is a lot of time
    that goes into doing this, but once it sells, it is a long-term relationship that
    pays out for a long time.
  sec: 1295
  time: '21:35'
  who: Paul
- header: Token Efficiency and Open Source Models
- line: You have a funnel, and not every potential call results in a second in-person
    meeting. It doesn't mean that these tokens spent on building a prototype are wasted
    because you learn from every single interview.
  sec: 1316
  time: '21:56'
  who: Alexey
- line: I never consider any tokens that I spend to be wasted. I waste a lot of tokens
    because token efficiency is not my strength. I like using the best models and
    definitely need to discipline myself, especially in using open source models.
    The next year is going to be very big for open source models, and people will
    realize you can get 80 to 90% of the way with them. Hugging Face has been valued
    at 14 billion dollars, and they are essentially a marketplace for open source
    models.
  sec: 1340
  time: '22:20'
  who: Paul
- line: I do not think tokens are wasted because the more time I spend working with
    agents, the more fluent I become in their mode of thinking. It all carries over
    as an investment in my future.
  sec: 1390
  time: '23:10'
  who: Paul
- line: What is your go-to model?
  sec: 1416
  time: '23:36'
  who: Alexey
- line: I like to use Fable. For client work, I literally do everything with Fable
    end-to-end. The quality of the output is so important. I find Fable very calming
    and it gives me clarity and insight in a way that doesn't induce panic like Opus
    5 can when it goes off on rambling tangents. I use Codex a lot in chat mode on
    my phone, especially the voice mode while in the car.
  sec: 1416
  time: '23:36'
  who: Paul
- line: 5.6 Soul is a great model that I use for execution and computer use. If I
    could, I would use Fable for everything. It is just far superior for me.
  sec: 1463
  time: '24:23'
  who: Paul
- line: My approach is using Fable for planning or auditing, and Opus or Sonnet for
    execution. For coding it works reasonably well, but for client work I would also
    want to ensure the quality is the best possible.
  sec: 1476
  time: '24:36'
  who: Alexey
- line: I will often have Fable orchestrating a ton of sub-agents on dynamic graph
    workflows. If I am honest, I think Fable does things better if it just works alone
    on a single thread and barges through the work. There are many buzzwords going
    around like loops and harnesses, but I feel like your clarity of vision is more
    important. It is much easier to clarify your own vision with a model like Fable
    because it gives you such good feedback and insight.
  sec: 1501
  time: '25:01'
  who: Paul
- line: I have been in the AI world since 2012. Even for me, keeping up with buzzwords
    is very challenging. You open Twitter and see things popping up every day. As
    someone who is not a developer, how do you manage to keep up with all this stuff
    and decide what to try or ignore?
  sec: 1558
  time: '25:58'
  who: Alexey
- line: I think you have to go down the wrong road a number of times. With Twitter
    initially, I would go after every thread like a Labrador chasing a tennis ball.
    I would go down rabbit holes like building a second brain or rebooting my architecture
    to run on loops.
  sec: 1598
  time: '26:38'
  who: Paul
- line: Why did you want to chase all these things? Did you see value in these things
    and want to learn how to be more efficient, or what was the motivation?
  sec: 1621
  time: '27:01'
  who: Alexey
- line: It is Twitter. The way posts are worded makes everything out to be the next
    big thing. Sometimes there is real value in those threads, like understanding
    context engineering. I went down a lot of rabbit holes that weren't massive magic
    bullets, but they were valuable enough that I learned stuff along the way. I have
    developed a strong radar for these posts now and tend not to go down those rabbit
    holes.
  sec: 1640
  time: '27:20'
  who: Paul
- line: I scroll past posts like the leaked Anthropic memory system. I still spend
    a lot of time on X because it is the easiest way to see what is being built and
    what fellow people are doing. That is how we found each other. What you mentioned
    earlier about everybody building agent operating systems is exactly what I have
    noticed. It is kind of like a hive mind.
  sec: 1692
  time: '28:12'
  who: Paul
- line: I used to find this in digital marketing too. I would have an original thought
    and then see it all over Facebook. There is definitely a collective consciousness
    because I am seeing everyone building agent operating systems now.
  sec: 1730
  time: '28:50'
  who: Paul
- line: There is an effect when you start a podcast, you notice everyone else is doing
    a podcast too. Maybe they were doing it before, but you just didn't pay attention.
    Now it looks like everyone is building an agent operating system, but maybe we
    only notice because it is a problem we share.
  sec: 1746
  time: '29:06'
  who: Alexey
- line: The algorithm obviously sees you paying more attention to this type of stuff,
    so it shifts you. That could absolutely be the case. It is very interesting regardless.
  sec: 1788
  time: '29:48'
  who: Paul
- header: Curiosity and the Learning Process
- line: How did you develop this radar? What is your approach to learning? With context
    engineering, dynamic workflows, and graph workflows being buzzwords, how do you
    decide if you need to learn them? You cannot call yourself non-technical anymore
    because you are coding and running many accounts and agents. There was a journey,
    and I am interested in how you approach learning now compared to a year ago.
  sec: 1800
  time: '30:00'
  who: Alexey
- line: The cornerstone of it is relentless curiosity, which is only possible if you
    are genuinely interested in something. I do not feel like I have ever been as
    interested in anything as I am in AI. It is almost a magnetic pull of curiosity
    and it is dangerously addictive. It can make you feel like you are being extremely
    productive.
  sec: 1879
  time: '31:19'
  who: Paul
- line: They call it AI psychosis, where you go down a rabbit hole thinking you are
    achieving something but not moving the needle.
  sec: 1917
  time: '31:57'
  who: Alexey
- line: My early stages of getting into AI were full of that. I was trying everything
    I could get my hands on and building things that were kind of useless.
  sec: 1922
  time: '32:02'
  who: Paul
- line: It is a productive psychosis because it is a journey. You have to try things
    before you know they don't work. If you build something, it might work or it might
    not.
  sec: 1948
  time: '32:28'
  who: Alexey
- line: You have to believe deeply in what you are doing at any given moment. You
    have to believe it is the biggest thing and that it is going to work. Nine out
    of ten times it is probably not going to work out, but you have to be willfully
    delusional and allow yourself to go down the rabbit holes. After doing it enough
    times, you learn from the iteration of failing and trying again, just like agents
    do. You apply that process of learning until you reach something good.
  sec: 1965
  time: '32:45'
  who: Paul
- line: That is how I got to the point where I feel like a lot of what I do with AI
    is productive and brings real value. It is easy to fail without intention and
    clarity of vision, as seen with billions invested in enterprise AI programs that
    failed.
  sec: 2020
  time: '33:40'
  who: Paul
- line: What is your approach to learning now? If you see something genuinely interesting
    on Twitter, what do you do next?
  sec: 2058
  time: '34:18'
  who: Alexey
- line: The first thing I will do is ask Fable to apply the methodologies shared and
    do a direct comparison to our current systems. I have it evaluate it on a bunch
    of different metrics and come up with a rubric to score the new system.
  sec: 2088
  time: '34:48'
  who: Paul
- line: You ask yourself if you can use it for your current system, not just if you
    can learn it. For learning, it has to be practical as the first filter. If it
    can potentially be useful, you ask Fable if this approach will be useful for your
    current workflow.
  sec: 2115
  time: '35:15'
  who: Alexey
- line: It needs to spark my imagination. I need to see the idea and think it could
    solve a problem I am currently having. When you try and adopt these ideas wholesale,
    you end up sinking so much time to make so little progress. I have Fable bring
    to light if there is utility in the idea when combined with our existing systems
    in a symbiotic way.
  sec: 2152
  time: '35:52'
  who: Paul
- line: I have become very familiar with the term blast radius. I ask if the blast
    radius of implementing an idea is going to screw up my whole estate and have agents
    rebuilding our entire infrastructure. If so, I ask Fable to err on the side of
    caution. I looked into using Devon, a coding harness with an engineering bent,
    and realized it would be inharmonious to integrate into my current workflow. Right
    now, what is most important and how I am learning the most is from actual real
    businesses' needs.
  sec: 2197
  time: '36:37'
  who: Paul
- line: The problems are specific, unique, and real. I am spending a lot less time
    learning from Twitter and a lot more time learning from building work for clients.
  sec: 2253
  time: '37:33'
  who: Paul
- header: Red Teaming and Code Audits
- line: I have a problem sometimes when I see a Codex usage reset coming tomorrow.
    If I still have 60% left, I come up with a crazy idea to burn the tokens. Do you
    have this problem with your six Claude and two Codex accounts? Do you worry that
    some sessions are not fully utilized?
  sec: 2272
  time: '37:52'
  who: Alexey
- line: The first thing I will do is send out red teams. I will get Codex to red team
    my codebase for reliability. I have a prompt that does a comprehensive simplification
    audit of a codebase and comes out with a list of P0 and P1 fixes that should be
    implemented. I will have a Codex agent blast through those audits and findings.
    I usually have around 50 findings queued up that I send Codex to smash through
    if I know a reset is coming.
  sec: 2318
  time: '38:38'
  who: Paul
- line: That is why I built Headroom. The agents make decisions on how to utilize
    my usage effectively and which account to choose.
  sec: 2385
  time: '39:45'
  who: Paul
- line: If you have six accounts and some are closer to zero than others, does it
    do any smart dispatching to use a specific account for a task?
  sec: 2401
  time: '40:01'
  who: Alexey
- line: Absolutely. Fable makes it interesting because you can only use 50% of your
    weekly limit on Fable. I have created rule sets so the agents do not let the seven-day
    limit run out while there is still Fable left. They utilize Fable to ensure we
    get the full 50% usage. It will also try to watch the five-hour limits.
  sec: 2420
  time: '40:20'
  who: Paul
- line: It won't assign the same accounts to multiple agents churning through tokens
    because that hits the five-hour limits. When an account is at 7% of its limit,
    it rotates to a more suitable account. The trick is rotating the login in place
    so you do not lose context and kill sub-agents.
  sec: 2450
  time: '40:50'
  who: Paul
- line: Can you keep the context?
  sec: 2481
  time: '41:21'
  who: Alexey
- line: You can keep the context. I use automated baton handoffs. When an agent is
    at a 30% context limit, it builds out a comprehensive context window and passes
    it on to the next agent.
  sec: 2481
  time: '41:21'
  who: Paul
- line: You ask it to create a handoff document because you are about to stop the
    session and another agent is going to take over.
  sec: 2511
  time: '41:51'
  who: Alexey
- line: This happens automatically. I think it is a little bit of paranoia, but after
    context has churned twice, degradation starts to set in and you lose context from
    earlier parts of the session. It works better for me to rotate at a 30% context
    window automatically.
  sec: 2522
  time: '42:02'
  who: Paul
- line: You called yourself a non-coder, but you have an engineering mindset. You
    observe when something is not working and ask agents to come up with a fix. As
    someone with a non-technical background, how do you choose technologies? Do you
    rely on agents or how do you go about this?
  sec: 2545
  time: '42:25'
  who: Alexey
- line: I try and focus on what I am good at, which is not the technical deep elements
    of choosing the right code language. I feel like we are moving towards a space
    where none of that is going to be relevant. I rely on my agents completely and
    rely on outcomes. I know what good looks like and how I want it to behave. I am
    a blind systems architect in that I know how I want the system to work from a
    high level, but I have no idea about the intricacies.
  sec: 2580
  time: '43:00'
  who: Paul
- line: I haven't needed to know that. AI unlocked the ability to build things that
    used to require layers of technical ability. I can marry my creative perspective
    to technical problems.
  sec: 2635
  time: '43:55'
  who: Paul
- header: Building Software Without Knowing the Tech Stack
- line: For Headroom, how did you choose the technologies like Python? Did you ask
    the agent to implement it and go with its suggestion, or did you ask for a list
    of technologies and their pros and cons?
  sec: 2666
  time: '44:26'
  who: Alexey
- line: It all starts with a problem and I use Whisper flow. I am constantly talking
    to my agents. Headroom came out of me constantly having to copy the URL, log into
    the right Claude account, and paste the authentication code back into the CLI.
    It felt inefficient. It always starts with a little annoyance or inefficiency.
  sec: 2684
  time: '44:44'
  who: Paul
- line: I express that feeling to the agents and they help me brainstorm and execute
    the solution. I judge it based on the outcome.
  sec: 2734
  time: '45:34'
  who: Paul
- line: At the end, it doesn't matter if it's Python or TypeScript. You just state
    the problem and ask to solve it using the best possible way within your constraints.
    If it works the way you want, you do not care what technology it uses.
  sec: 2755
  time: '45:55'
  who: Alexey
- line: Not at all. I didn't even know that Demox was built on TypeScript until yesterday.
    It is not something I consider to be a needle-moving element. Even if AI isn't
    perfect and some visual elements are annoying to fix, I do not think this stuff
    is important. It is about having a clear understanding of what you want and expressing
    it clearly so agents can understand.
  sec: 2778
  time: '46:18'
  who: Paul
- line: When you see that an account's limits are going to reset soon, you ask for
    a comprehensive simplification audit. How do you know it is needed? Do you know
    from experience that agents tend to overcomplicate things?
  sec: 2834
  time: '47:14'
  who: Alexey
- line: Even with my limited knowledge of coding, I know that agents are not very
    efficient and can build up massive piles of technical debt. The thing I am always
    trying to protect is context because when agents lack context, they start breaking
    everything. Without fail, if you run an audit with Codex, it will have findings.
    It has never said the code is perfect. The key is to take that audit, set it as
    a measuring stick, and stick to it over days or weeks.
  sec: 2859
  time: '47:39'
  who: Paul
- line: I used to have agents implement the audit but would lose track of what was
    done. Now, I have Fable report daily on our progress toward completing the audit
    findings. That works wonders in keeping a measurable North Star for the agents
    to work toward. I do not need to know what each finding does; I just know if there
    is improvement toward that North Star score.
  sec: 2910
  time: '48:30'
  who: Paul
- line: Having a background in marketing really helps because you need to measure
    things. In marketing, you deal with real money and need to know the return on
    investment. This data-driven mindset is very helpful.
  sec: 2974
  time: '49:34'
  who: Alexey
- line: Especially with performance-based marketing like affiliate marketing, your
    ROI is your living. After years of trying to squeeze a profit out of Meta ads,
    you develop that data-driven methodology.
  sec: 3016
  time: '50:16'
  who: Paul
- header: Building Software Without Knowing the Tech Stack
- line: What did you do before marketing?
  sec: 3050
  time: '50:50'
  who: Alexey
- line: I was a film director on film sets. That feeds in because it is about having
    a vision, writing a story, and turning it into reality by coordinating people.
  sec: 3057
  time: '50:57'
  who: Paul
- line: That is like project management.
  sec: 3084
  time: '51:24'
  who: Alexey
- line: It involves an obsession for detail and making sure your vision is adhered
    to without compromising. Good filmmakers are extremely stubborn about making their
    vision a reality. The same applies to building with AI.
  sec: 3089
  time: '51:29'
  who: Paul
- line: I see the parallels. You have business acumen to measure and keep things moving.
    People with managerial experience are quite good at managing agents because they
    know they need to be explicit with tasks. You can come from all sorts of backgrounds
    and have useful experience for making an agentic team work.
  sec: 3115
  time: '51:55'
  who: Alexey
- line: I wonder how long that is going to be the case. Inference is getting better
    and better at inferring what you mean even if you are vague. A model like Fable
    never ceases to blow me away with how close it gets to your idea even without
    explicit prompting. It still remains vitally important right now to be clear in
    instructions. I wonder how long it will be important before things like Neuralink
    reduce bandwidth and instantly materialize our thoughts.
  sec: 3201
  time: '53:21'
  who: Paul
- line: Do you also use AI for other things with friends or family?
  sec: 3277
  time: '54:37'
  who: Alexey
- line: I am planning my wedding. I use AI a lot with my six-year-old son. I let him
    describe what he wants to see, like a monster with horns, and bring his imagination
    to life using ChatGPT. I also built a custom-made physical board game stuck to
    the wall with his favorite video games. He gets to roll a coin every day if he
    behaves well, and it keeps him excited.
  sec: 3288
  time: '54:48'
  who: Paul
- header: Using AI for 3D Printing and Personal Projects
- line: Do you have a 3D printer?
  sec: 3385
  time: '56:25'
  who: Alexey
- line: No, I don't, but I would love to.
  sec: 3385
  time: '56:25'
  who: Paul
- line: I got a printer three months ago. Three months ago, ChatGPT couldn't design
    a toy car to print. Now it can. There is a tool called AutoSCAD that can write
    code to generate an object and render it. You would love it.
  sec: 3392
  time: '56:32'
  who: Alexey
- line: I need to do that. There are obscure video game enemies my son loves that
    they do not make toys for. A 3D printer would be cool to make those.
  sec: 3447
  time: '57:27'
  who: Paul
- line: In Germany, you can get a Bamboo A1 Mini for 130 euros. If something is broken,
    I can take a picture and ask AI how to fix it.
  sec: 3458
  time: '57:38'
  who: Alexey
- line: That is why it is more important than ever to maintain human connections.
    We don't really need help from others for technical reasons, but we need it for
    emotional reasons and collaboration.
  sec: 3499
  time: '58:19'
  who: Paul
- line: A friend came over, saw the printer, and now he has one too. We discuss what
    to print.
  sec: 3521
  time: '58:41'
  who: Alexey
- line: You are doing good marketing. I will have a printer as well. How is it going
    with affiliate commissions and adverts? Is the podcast a hobby?
  sec: 3539
  time: '58:59'
  who: Paul
- line: I only spend money on the podcast, so I am not earning anything from it. The
    way DataTalks.Club works is that when people sign up for the podcast, courses,
    or events, they get into the newsletter. Every week there is an ad in the newsletter.
    I try to make sure sponsors are a good fit for the community, like promoting products
    for data engineers, not random items like chairs.
  sec: 3569
  time: '59:29'
  who: Alexey
- line: It doesn't work for them if you place misaligned ads either.
  sec: 3660
  time: '1:01:00'
  who: Paul
- line: I am satisfied with my Herman Miller chair anyway. Do you listen to podcasts
    yourself?
  sec: 3672
  time: '1:01:12'
  who: Alexey
- line: Sometimes, but not actively.
  sec: 3691
  time: '1:01:31'
  who: Paul
- line: When I was starting the podcast, I listened actively to side hustle podcasts.
    Now I listen to audiobooks on Audible.
  sec: 3696
  time: '1:01:36'
  who: Alexey
- line: I advise you to listen to Anna Karenina read by Maggie Gyllenhaal on Audible.
    It is my favorite audiobook.
  sec: 3734
  time: '1:02:14'
  who: Paul
- line: Are there any books related to what we talked about today that you can recommend?
  sec: 3752
  time: '1:02:32'
  who: Alexey
- line: I don't read a lot of self-help or technical books. I read for pleasure and
    emotional enrichment. I do like biographies like Steve Jobs. I find inspiration
    in what humans can achieve. Currently, I am reading The Power Broker, which is
    about the man who built New York City. He was a terrible man but an incredible
    achiever.
  sec: 3759
  time: '1:02:39'
  who: Paul
- line: It is interesting that great achievers are sometimes not the people you want
    to be around. It is the same with some musicians; I admire their art but the people
    are terrible.
  sec: 3822
  time: '1:03:42'
  who: Alexey
- line: Separating the art from the artist is quite nuanced. Have you taken any courses
    about AI and managing agents or is it all learned by doing?
  sec: 3848
  time: '1:04:08'
  who: Paul
- header: The Importance of AI Evals
- line: I looked into evals with Hamel. Evals are one of the most important aspects
    of AI that we haven't spoken about. I learned a lot about LLM as a judge to ensure
    agents produce consistently good output. His courses are very productive. He is
    writing a book available on O'Reilly Learning.
  sec: 3874
  time: '1:04:34'
  who: Alexey
- line: I definitely think I'll give that a read. Evals relate to a human's perception
    of output, which models won't just solve. They will never perfectly infer what
    a person wants.
  sec: 3928
  time: '1:05:28'
  who: Paul
- line: Everyone can code something, but properly evaluating it is something we need
    to know how to do better as a community. Thanks Paul for joining and sharing your
    experience.
  sec: 3964
  time: '1:06:04'
  who: Alexey
- line: Thank you. It was a great pleasure talking to you.
  sec: 3987
  time: '1:06:27'
  who: Paul
---

Links:

* [Linkedin](https://www.linkedin.com/in/paul-domanski-ai/){:target="_blank"}
* [Twitter](https://x.com/domanski_ai){:target="_blank"}
* [Github](https://github.com/domanski-ai){:target="_blank"}
* [Website](https://domanski.ai/){:target="_blank"}