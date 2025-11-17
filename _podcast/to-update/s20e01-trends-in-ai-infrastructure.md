---
title: "Context: A conversation with an AI-infrastructure practitioner about moving from developer tools to building DStack, exploring real-world trade-offs across hardware, software, deployment, and business models for practical AI adoption.

Core theme (single unifying idea): Practical AI is an infrastructure-first problem — success depends less on chasing the biggest model and more on designing cost-effective, controllable, and efficient stacks (hardware, orchestration, and software) that fit hybrid cloud/on‑prem realities, leverage open-source ecosystems, and optimize distributed training and serving for real-world constraints.

Dominant through-line: Every segment — from cost of ownership and cloud vs on‑prem trade‑offs to open vs proprietary models, decentralization, distributed training bottlenecks, orchestration gaps, and edge/federated use cases — returns to the same tension: how to deliver AI that is scalable, performant, and economically sustainable by choosing the right mix of tooling, deployment model, and optimizations.

Key themes implied by the narrative:
- Cost and control drive architecture choices more than raw model capability.
- Hybrid cloud + on‑prem is the pragmatic reality; orchestration must adapt.
- Open-source ecosystems accelerate feedback, tooling, and business flexibility.
- Efficient distributed training and communication optimizations trump brute-force scaling.
- Decentralization (privacy, local control, edge) is often a matter of fit and trade-offs, not ideology.
- Practical provisioning, automation, and orchestration are the unsolved scaling problems for non–AI‑first organizations."
short: Trends in AI Infrastructure
season: 20
episode: 1
guests:
- andreycheptsov
image: images/podcast/s20e01-trends-in-ai-infrastructure.jpg
ids:
  anchor: atalksclub/episodes/Redefining-AI-Infrastructure-Open-Source--Chips--and-the-Future-Beyond-Kubernetes--Andrey-Cheptsov-e2u7lc2
  youtube: 1aMuynlLM3o
links:
  anchor: https://creators.spotify.com/pod/show/datatalksclub/episodes/Redefining-AI-Infrastructure-Open-Source--Chips--and-the-Future-Beyond-Kubernetes--Andrey-Cheptsov-e2u7lc2
  apple: https://podcasts.apple.com/us/podcast/redefining-ai-infrastructure-open-source-chips-and/id1541710331?i=1000687565459
  spotify: https://open.spotify.com/episode/5MIc1pAXPxVYSr0E4pndU4
  youtube: https://www.youtube.com/watch?v=1aMuynlLM3o

description: Discover DStack to cut AI infrastructure costs with on‑prem GPU training and MLOps alternatives—optimize distributed training, reduce orchestration overhead
intro: 'How can engineering teams cut AI infrastructure costs without sacrificing performance or control? In this episode, Andrey Cheptsov — founder and CEO of dstack and former JetBrains engineer — walks through the motivation behind DStack, an open‑source orchestration alternative designed to lower AI infrastructure total cost of ownership. We trace the cloud vs on‑prem economics (including MLOps limitations like SageMaker), the decision to build open‑source developer tooling, and the trade‑offs between open and proprietary models. <br><br> You’ll hear practical discussion of on‑prem GPU training and distributed training challenges: GPU requirements, PyTorch + NCCL communication bottlenecks, optimization strategies such as DeepSpeed, and tips for fine‑tuning and serving models for non–AI‑first companies. The episode also covers orchestration gaps — Kubernetes and SLURM limitations — plus bare‑metal provisioning, hybrid cloud realities, edge computing scope, and federated learning versus distributed compute. <br><br> If you’re evaluating MLOps alternatives, on‑prem GPU coordination, or ways to reduce AI infrastructure cost, this episode offers concrete perspectives on when to choose on‑prem vs cloud, how DStack fits into the stack, and practical trade‑offs for production ML workloads.'
dateadded: 2025-02-26

duration: PT01H06M04S

quotableClips:
- name: Episode Kickoff & Guest Introduction
  startOffset: 0
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=0
  endOffset: 166
- name: 'Career Background: JetBrains, DataSpell, and Move into AI'
  startOffset: 166
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=166
  endOffset: 327
- name: 'Origins of DStack: Reducing AI Infrastructure Cost of Ownership'
  startOffset: 327
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=327
  endOffset: 505
- name: Cloud vs On‑Prem Costs and MLOps Limitations (SageMaker example)
  startOffset: 505
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=505
  endOffset: 600
- name: Cloud-to-On‑Prem Realities in the Post‑ChatGPT Era
  startOffset: 600
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=600
  endOffset: 778
- name: 'Choosing Open Source: Developer Tools, Feedback, and Community'
  startOffset: 778
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=778
  endOffset: 1053
- name: 'Open vs Proprietary Models: Business Models and Trade‑Offs'
  startOffset: 1053
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=1053
  endOffset: 1297
- name: 'Decentralization in AI: Privacy, Control, and Industry Fit'
  startOffset: 1297
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=1297
  endOffset: 1816
- name: 'Training at Scale: GPU Requirements and Distributed Challenges'
  startOffset: 1816
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=1816
  endOffset: 2086
- name: 'Distributed Training Stack: PyTorch, NCCL, and Communication Bottlenecks'
  startOffset: 2086
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=2086
  endOffset: 2255
- name: 'Efficiency Over Brute Force: Optimization Strategies and DeepSpeed'
  startOffset: 2255
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=2255
  endOffset: 2370
- name: Fine‑Tuning & Serving Models for Non–AI‑First Companies
  startOffset: 2370
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=2370
  endOffset: 2836
- name: 'Orchestration Gaps: Kubernetes Limitations for AI Workflows and SLURM'
  startOffset: 2836
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=2836
  endOffset: 3059
- name: Kubernetes as the Deployment Standard vs Smaller Alternatives
  startOffset: 3059
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3059
  endOffset: 3116
- name: 'Hybrid Infrastructure Outlook: Cloud Dominance and On‑Prem Nuances'
  startOffset: 3116
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3116
  endOffset: 3271
- name: 'On‑Prem GPU Coordination: SSH, Resource Contention, and Real Examples'
  startOffset: 3271
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3271
  endOffset: 3413
- name: 'Bare‑Metal as a Service: Provisioning, Automation, and Firmware Management'
  startOffset: 3413
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3413
  endOffset: 3487
- name: 'Edge Computing Scope: Devices, Local Models, and Definition Ambiguity'
  startOffset: 3487
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3487
  endOffset: 3630
- name: 'Federated Learning vs Distributed Compute: Practicality and Use Cases'
  startOffset: 3630
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3630
  endOffset: 3771
- name: 'Closing Pick: Science‑Fiction Recommendation — The Three‑Body Problem'
  startOffset: 3771
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3771
  endOffset: 3938
- name: Episode Wrap‑Up & Links to DStack and Guest Resources
  startOffset: 3938
  url: https://www.youtube.com/watch?v=1aMuynlLM3o&t=3938
  endOffset: 3964

transcript:
- header: Episode Kickoff & Guest Introduction
- line: This week, we'll talk about AI infrastructure and everything related to it.
    We might touch on trends in AI infrastructure, but we'll see where the conversation
    goes.
  sec: 0
  time: 0:00
  who: Alexey
- line: 'We have a special guest today: Andrey, the founder and CEO of DSec, which
    is an open-source alternative to Kubernetes and SLAM. I’m not sure what SLAM is,
    but we’ll probably talk about that. The idea behind DSec is to simplify the setup
    of AI infrastructure. Before DSec, Andrey worked at JetBrains for 10 years, helping
    different teams develop the best developer tools. Welcome, Andrey!'
  sec: 0
  time: 0:00
  who: Alexey
- line: Thank you, Alexey, for the introduction and for inviting me. I'm excited to
    talk about infrastructure and everything related to it.
  sec: 126
  time: '2:06'
  who: Andrey
- line: We've known each other for quite some time, so it was long overdue to invite
    you. Thanks for accepting the invitation.
  sec: 138
  time: '2:18'
  who: Alexey
- line: 'As always, the questions for today''s interview were prepared by Johanna
    Bayer. Thanks, Johanna, for your help. Let''s start with the main topic: AI infrastructure.
    But before we dive into that, could you tell us about your career journey so far?'
  sec: 138
  time: '2:18'
  who: Alexey
- header: 'Career Background: JetBrains, DataSpell, and Move into AI'
- line: Sure. I started my professional career as a software engineer, though back
    then, I didn't even consider it a professional career—I just enjoyed coding. I
    even skipped school sometimes to work on coding problems.
  sec: 166
  time: '2:46'
  who: Andrey
- line: You started coding in high school?
  sec: 187
  time: '3:07'
  who: Alexey
- line: Yes, exactly. I miss those days when I coded just for fun.
  sec: 189
  time: '3:09'
  who: Andrey
- line: Don’t we all miss those days?
  sec: 197
  time: '3:17'
  who: Alexey
- line: After that, I switched to professional software development and worked in
    different companies. One of the companies I worked for was Experts, based in Saint
    Petersburg. They made professional tools for traders, like for options and stocks,
    and I really enjoyed it.
  sec: 200
  time: '3:20'
  who: Andrey
- line: Then, I joined JetBrains, which was basically a dream job for me as a programmer.
    I know many others feel the same way about JetBrains tools. When I was invited
    to join, it was super exciting.
  sec: 200
  time: '3:20'
  who: Andrey
- line: I spent 10 years there, working with different teams. I started with IntelliJ,
    then helped launch a data group, which is an IDE for working with databases. I
    also worked with other IDEs, including helping launch GoLand as a Go IDE. Eventually,
    I joined the PyCharm team as a product manager.
  sec: 200
  time: '3:20'
  who: Andrey
- line: I was working on DataSpell, which is a dedicated IDE for data analysis and
    data science. It’s also part of PyCharm, and this is where I was first introduced
    to machine learning. That eventually led me to leave JetBrains and focus fully
    on this area.
  sec: 200
  time: '3:20'
  who: Andrey
- line: How did you decide to focus on this technology? What made you choose this
    problem to solve full-time?
  sec: 309
  time: '5:09'
  who: Alexey
- header: 'Origins of DStack: Reducing AI Infrastructure Cost of Ownership'
- line: 'That''s a great question. There are a lot of factors, and it''s certainly
    a topic we could discuss at length. But if I were to summarize a few specific
    reasons:'
  sec: 327
  time: '5:27'
  who: Andrey
- line: 'I remember, during my interviews with various ML teams, I often asked, "What’s
    standing in the way of your team?" There were many challenges, but one thing that
    stood out to me was that there are still two main ways to do machine learning:
    on-premises and in the cloud.'
  sec: 327
  time: '5:27'
  who: Andrey
- line: Some teams couldn't use either because of cost. On-prem infrastructure requires
    a large upfront investment, and you need to ensure you're fully utilizing the
    hardware, which can be difficult to predict. This makes it a risky decision for
    many companies.
  sec: 327
  time: '5:27'
  who: Andrey
- line: On the other hand, cloud infrastructure is expensive, especially for cutting-edge
    AI development. Many companies are concerned about the cost.
  sec: 327
  time: '5:27'
  who: Andrey
- line: The more I worked with different teams, the more I realized that there were
    ways to work around these issues. Tools like Terraform, Kubernetes, and Docker
    have made cloud development much more predictable and less complex. But the problem
    with costs still remains.
  sec: 327
  time: '5:27'
  who: Andrey
- line: That’s why I thought there should be a solution that could greatly reduce
    the cost of ownership and simplify the process for everyone, which led me to start
    working on DSec.
  sec: 327
  time: '5:27'
  who: Andrey
- header: Cloud vs On‑Prem Costs and MLOps Limitations (SageMaker example)
- line: Yes, there are existing tools for machine learning, like SageMaker, but as
    you mentioned, cost becomes a major issue.
  sec: 505
  time: '8:25'
  who: Alexey
- line: SageMaker is a great counterexample. It’s one of the most mature MLOps platforms
    for working with AWS. However, it doesn’t address all the issues, which is why
    many people are hesitant to use cloud services in the first place.
  sec: 515
  time: '8:35'
  who: Andrey
- line: I remember when I joined my previous company as a senior data scientist about
    six years ago. The first thing I wanted was a machine with GPUs, preferably with
    a couple of them. I wrote a proposal for this, and everyone approved it, but it
    never happened. The cost of ownership was too high—the machine had to be housed
    somewhere, and someone had to maintain it.
  sec: 537
  time: '8:57'
  who: Alexey
- line: With the cloud, it’s often easier to just click a button, but then you get
    the bill a month later, and it’s much more expensive than expected. One of the
    first tasks I had as a senior data scientist was porting some code from SageMaker
    to Kubernetes. I guess that's how people used to manage it.
  sec: 537
  time: '8:57'
  who: Alexey
- header: Cloud-to-On‑Prem Realities in the Post‑ChatGPT Era
- line: Yes, and while many of these challenges are still relevant today, there are
    even bigger challenges ahead. The "ChatGPT moment" has introduced new issues,
    which makes AI infrastructure an even more important topic today.
  sec: 600
  time: '10:00'
  who: Andrey
- line: How long have you been doing this?
  sec: 627
  time: '10:27'
  who: Alexey
- line: It’s been about 2 years, maybe a bit more.
  sec: 631
  time: '10:31'
  who: Andrey
- line: I think we've known each other for around 2 years, maybe a little longer.
    So, I’ve basically seen this start.
  sec: 641
  time: '10:41'
  who: Alexey
- line: Yes, I was doing some experiments even while I was still at JetBrains. It
    became official when we did the first project with JetBrains.
  sec: 650
  time: '10:50'
  who: Andrey
- line: 'So, the next question is: how did you begin working on AI infrastructure?
    But I think you''ve partly answered that already. You started at JetBrains, right?
    You saw things related to machine learning, realized there was a problem, and
    started working on it.'
  sec: 669
  time: '11:09'
  who: Alexey
- line: Yes, in a general sense. JetBrains is a very flat company where everyone has
    a dedicated role, but it’s close to programming. Many marketing people at JetBrains
    were originally programmers, which is how I got into marketing and product management.
    Everything at JetBrains revolves around developer tools, so your full-time job
    is to think about the developer experience—gathering feedback from the community,
    passing it to the development team, and spreading the word. For me, transitioning
    from JetBrains to AI infrastructure wasn’t a huge change. I was still working
    on developer tools, just focusing more specifically on AI infrastructure. My title
    might have changed, but not much else.
  sec: 692
  time: '11:32'
  who: Andrey
- line: Well, now you have to figure out how to get funding yourself, right? Previously,
    it was different.
  sec: 767
  time: '12:47'
  who: Alexey
- line: Especially working on open-source, yes.
  sec: 773
  time: '12:53'
  who: Andrey
- header: 'Choosing Open Source: Developer Tools, Feedback, and Community'
- line: Speaking of open-source, why did you decide to work in the open? I see many
    companies starting as closed-source but eventually moving to open-source. Why
    did you choose to follow this model and make all your code open from the beginning?
  sec: 778
  time: '12:58'
  who: Alexey
- line: I think it’s a clear pattern. Many developer tools are open-source, and while
    we don’t always know the exact reasons, there’s a pattern to it. Of course, companies
    have commercial interests, and not many are fully nonprofit. OpenAI, for example,
    started as a nonprofit, but that changed. In the end, the model reflects the best
    way to achieve the company’s goals. Sometimes the goal changes, or the way to
    achieve it changes, and that’s fine. I wouldn’t argue about whether being commercial
    or nonprofit is better. We see that most companies eventually go commercial, and
    many leverage open-source to move forward.
  sec: 809
  time: '13:29'
  who: Andrey
- line: When we started, we weren’t sure if open-source was the right decision. But
    the more we talked to teams using different tools, the more we learned. One of
    the main benefits of open-source, especially in infrastructure, is that it allows
    early adopters to give feedback, which helps improve the tool. Open-source is
    one of the best frameworks for this process. There are other ways, but for me,
    as someone who’s always worked with developer tools, it’s easier to communicate
    directly with developers and understand their problems. Open-source fits well
    because I can relate to the development team.
  sec: 809
  time: '13:29'
  who: Andrey
- header: 'Open vs Proprietary Models: Business Models and Trade‑Offs'
- line: I don’t know the full story behind OpenAI either, but I think they initially
    released many things as open-source. GPT-2 was open-source, and they also released
    Whisper and CLIP. But when they released GPT-3, they realized it was a gold mine.
    They thought, maybe this is something we should keep closed, but then others started
    reproducing GPT-3 and matching its performance. Now, OpenAI releases something,
    and the open-source community tries to catch up. What’s your opinion on that?
    With closed-source solutions like OpenAI and GPT-3, which give great performance,
    versus open-source solutions, where you have many different models with various
    characteristics and use cases?
  sec: 1053
  time: '17:33'
  who: Alexey
- line: This is a big topic, and we could talk for hours about it. I’ve given talks
    on the comparison between closed-source and open-source models. It seems like
    many people are living in a bubble when they discuss which is better, proprietary
    or open-source. The world is much larger, and framing the question like that isn’t
    helpful. It’s not about what’s better; there are many factors to consider. It’s
    not even an important question to debate.
  sec: 1148
  time: '19:08'
  who: Andrey
- line: Okay, I’m just wondering where the industry is heading.
  sec: 1239
  time: '20:39'
  who: Alexey
- line: If you think about proprietary and open-source models, they represent two
    different types of businesses. Proprietary AI is a service, centralized with one
    company offering it. There are many engineers working on different aspects of
    that service, and AI, in this case, is not just a model—it’s a service that impacts
    all aspects of our lives.
  sec: 1243
  time: '20:43'
  who: Andrey
- line: Right, so GPT is much more than just a model.
  sec: 1294
  time: '21:34'
  who: Alexey
- header: 'Decentralization in AI: Privacy, Control, and Industry Fit'
- line: Yes, it’s more than just the model. It’s like a new version of Google. Google
    changed our lives because we can search for anything. Now, GPT is changing how
    we work, not just how we search. It’s a disruptive change.
  sec: 1297
  time: '21:37'
  who: Andrey
- line: Open-source AI is a different business. It’s decentralized, where various
    companies and stakeholders contribute to different aspects. For example, in banking,
    privacy and control are essential, and a monolithic AI model doesn’t fit. Open-source
    allows companies to protect their privacy and control. It’s also about competition.
    If businesses don’t protect their margins, they won’t be able to compete. Open-source
    AI is important because it allows companies to maintain their competitive edge.
    Whether open-source AI is better than GPT-3 doesn’t matter as much. It’s about
    the approach that fits the business model.
  sec: 1297
  time: '21:37'
  who: Andrey
- line: So, it depends on the use case.
  sec: 1425
  time: '23:45'
  who: Alexey
- line: Yes, the whole point here is decentralization. Open source is about decentralization,
    and it’s a mega trend that isn’t influenced by quality. The quality is a result
    of this mega trend. We see that open source models are better. It's not that people
    use open source models because they are better than GPT models; they are better
    because people need them.
  sec: 1431
  time: '23:51'
  who: Andrey
- line: But it's not that they are better in terms of performance; they are better
    in other aspects, like being able to control the data flow or hosting them yourself.
  sec: 1460
  time: '24:20'
  who: Alexey
- line: Yes, and that's when we can compare some aspects of models. But to me, it
    doesn’t make sense to compare them side by side. What makes sense for open source
    models is whether they are customizable, and that’s why we use them—they are easy
    to customize. What's even more important is that it’s becoming less of a "rocket
    science" process. The process of retraining and post-training is getting easier
    and simpler because of decentralization. Whether we like it or not, this trend
    is here, and we can’t influence it.
  sec: 1474
  time: '24:34'
  who: Andrey
- line: Do you know if big companies, like Meta, contribute a lot to the open source
    community, especially in AI, with models like LLaMA? Do they publicly share information
    on how exactly they train their models and what their AI infrastructure is?
  sec: 1536
  time: '25:36'
  who: Alexey
- line: I want to answer for sure, but I’d say yes. Typically, this is shared in a
    technical report. Even OpenAI, while not open-sourcing most of what they do, still
    shares some information on how they contribute to the community. This started
    even before, for example, with the "Attention is All You Need" paper from 2017.
    Even though it wasn’t open source, the paper on the transformer algorithm was.
    And then Meta went further, for example, with the LLaMA model. They made the weights
    available with LLaMA 3.1. Some people argue whether "open source" applies to models,
    and some prefer to say "open weights." To be honest, I’m not that picky.
  sec: 1563
  time: '26:03'
  who: Andrey
- line: Even OpenAI shared a lot of details about their post-training and pre-training
    processes. LLaMA also released a technical report on how they trained their models,
    providing a lot of details on the training process. This is also how the community
    learns.
  sec: 1563
  time: '26:03'
  who: Andrey
- line: This is a good example of decentralization—it’s not just about the morals,
    it’s about sharing technical details on how training and post-training were done,
    how many GPUs were used, and the architecture of the model. A lot of details are
    publicly available, and this is one of the best ways to learn.
  sec: 1563
  time: '26:03'
  who: Andrey
- line: Some might think technical reports are boring, but I personally encourage
    everyone to read them. They are actually very interesting. I’m a big fan of books,
    and while I used to read a lot of fiction, I now find reading fiction less exciting.
    I actually find technical reports much more entertaining.
  sec: 1563
  time: '26:03'
  who: Andrey
- line: Since you find these reports entertaining, I’m curious—what challenges do
    these companies face, and do these challenges also apply to smaller companies?
    Larger companies like Meta, Google, and OpenAI have different challenges from
    smaller ones, right? What are these challenges in general, and how do they affect
    trends in AI infrastructure?
  sec: 1746
  time: '29:06'
  who: Alexey
- line: I consider myself a generalist, so I’m interested not only in the technical
    side of things but also in other aspects. When you ask about challenges, there
    are technical challenges in every team, whether it's an infrastructure team, an
    AI team, or a data team.
  sec: 1784
  time: '29:44'
  who: Andrey
- header: 'Training at Scale: GPU Requirements and Distributed Challenges'
- line: Since we’re talking about AI infrastructure, let’s focus on that. To train
    a model, we need thousands of GPUs. How do we get them in the first place? How
    do we coordinate this? These are all questions we need to consider when starting
    such a project.
  sec: 1816
  time: '30:16'
  who: Alexey
- line: Yes, we need to think not only about technical problems but also financial
    ones. We know for sure that without GPUs, we can’t train models. For example,
    LLaMA 3.1 was trained using 16,000 GPUs. To put that into perspective, Meta likely
    has an order of magnitude more GPUs in total. If they used only a small fraction
    of what they have, they could train LLaMA 3.1.
  sec: 1835
  time: '30:35'
  who: Andrey
- line: The first challenge is infrastructure. However, I want to mention that while
    GPUs and money are important, they are not everything. There are other factors
    to consider. For instance, DeepSig recently released a V3 model in December. They
    used only a small fraction of what Meta used to train LLaMA 3.1, yet they trained
    a model that is significantly better in terms of benchmarks.
  sec: 1835
  time: '30:35'
  who: Andrey
- line: I’ve seen posts about this in my social media feeds just a few days ago.
  sec: 1917
  time: '31:57'
  who: Alexey
- line: Yes, DeepSig’s release happened at the end of December. They trained a model
    with a fraction of Meta’s resources, and the model performed significantly better
    in benchmarks compared to LLaMA 3.1. What I’m trying to say is that while GPUs
    and money are important, they are not the only factors.
  sec: 1926
  time: '32:06'
  who: Andrey
- line: But back to your question—retraining is a large-scale task involving many
    GPUs, and it’s distributed. Distributed training is challenging. If you speak
    to people working in this area, they will tell you how complex the process is.
    When you have tons of GPUs, you need to coordinate everything. If something goes
    wrong on one of the nodes, you have to deal with it.
  sec: 1946
  time: '32:26'
  who: Andrey
- line: The more GPUs you have, the higher the chances something will go wrong, right?
  sec: 2039
  time: '33:59'
  who: Alexey
- line: Yes, and you need to manage that at scale. There are many other issues to
    address, but handling this one is a major challenge.
  sec: 2045
  time: '34:05'
  who: Andrey
- line: Do you know what this actually looks like? There’s probably a computer with
    4 or 8 GPUs, another one with 4 or 8 GPUs, and all these computers are part of
    a network. You need to distribute the training process across all these machines,
    where each computer has several GPUs, and each GPU needs to compute something
    and then send the weights or gradients back to a central location. Is this roughly
    how it works?
  sec: 2053
  time: '34:13'
  who: Alexey
- header: 'Distributed Training Stack: PyTorch, NCCL, and Communication Bottlenecks'
- line: Yes, but like any complex problem, it can be split into smaller tasks and
    solved at different levels of abstraction. Generally speaking, there’s PyTorch,
    a framework mostly developed by Meta, designed for training. Distributed training
    is one of its main use cases.
  sec: 2086
  time: '34:46'
  who: Andrey
- line: So, this is what is used for models like LLaMA, right? It’s based on PyTorch?
  sec: 2125
  time: '35:25'
  who: Alexey
- line: Yes, but I’m basing my response on the latest LLaMA training report. Even
    though earlier versions were trained with something else, I don’t think PyTorch
    was used.
  sec: 2133
  time: '35:33'
  who: Andrey
- line: When we download models from Hugging Face Hub, we use the Transformers package,
    right? That’s based on PyTorch?
  sec: 2154
  time: '35:54'
  who: Alexey
- line: Yes, but the important point here isn’t that it’s PyTorch. It’s just that
    many people, including Meta, are using it. Google, on the other hand, isn’t using
    PyTorch, though I’m not sure about all the specifics of their model training process.
    But PyTorch is just a tool in the framework—beneath it, there’s a backend responsible
    for communication between the GPUs. One popular backend is called NCCL, which
    handles communication for distributed training. For example, when training frontier
    models, this backend can be a major source of frustration, leading teams to sometimes
    reimplement it from scratch to optimize the process.
  sec: 2163
  time: '36:03'
  who: Andrey
- header: 'Efficiency Over Brute Force: Optimization Strategies and DeepSpeed'
- line: 'To summarize, there’s a trend in training large language models: earlier,
    it was mostly about using raw computing power, like Meta with its massive number
    of GPUs. They would throw a problem at a fraction of these GPUs, and they’d process
    it. But not every company has the resources that Meta or Google do. Smaller companies
    like DeepMind are now focusing on being smarter with their resources, rather than
    relying on brute force. We see the trend shifting toward optimization—how can
    companies train models without access to massive GPU clusters?'
  sec: 2255
  time: '37:35'
  who: Alexey
- line: And then there’s the case where many companies aren’t training models but
    just need to use them. If I need a model and don’t have a specific use case, I
    could take an existing model and fine-tune it—or maybe I don’t need to fine-tune
    it at all. For many companies, especially those not AI-first, the challenges are
    different. They’re more focused on fine-tuning and serving the model. What do
    you think the challenges are for these companies that are just using models rather
    than training them?
  sec: 2255
  time: '37:35'
  who: Alexey
- header: Fine‑Tuning & Serving Models for Non–AI‑First Companies
- line: Correct, although I’d be cautious about labeling companies as small or medium.
    I think it’s more about whether a company is AI-first or not. Once you figure
    that out, everything becomes much clearer. If a company is AI-first, they’re likely
    to customize models to optimize performance, and the choice between pre-training
    or fine-tuning depends on their resources. If a company isn’t AI-first, like a
    large bank focused on privacy, they might not need to dive deeply into AI but
    still want to use it in their services. Some banks may even decide to become AI-first,
    just like how many banks once went software-first or mobile-first.
  sec: 2370
  time: '39:30'
  who: Andrey
- line: Becoming AI-first requires a complete shift. To do that, you’d need to rethink
    the entire structure of the company.
  sec: 2443
  time: '40:43'
  who: Alexey
- line: Yes, some companies, like certain banks, may decide to become AI-first. They’d
    need to define what that means for them. For example, you might have banks that
    are not AI-first, but then new AI-focused banks emerge. But to get back to your
    main point, the challenge for most companies is that they don’t need to train
    models from scratch. Instead, they focus on customization and fine-tuning, especially
    in industries like finance. They might not have the resources for extensive training,
    but they’ll want to leverage AI in their operations, and fine-tuning helps with
    that. Open-source solutions are making this process easier, enabling companies
    to use existing models and tools rather than building everything from the ground
    up. Even AI-first companies will use these open-source tools to optimize development
    and efficiency.
  sec: 2450
  time: '40:50'
  who: Andrey
- line: So, for these companies, the majority are non-AI-first companies, looking
    for existing solutions rather than building everything themselves?
  sec: 2632
  time: '43:52'
  who: Alexey
- line: Interestingly, those companies that initially built their own models have
    started switching to existing solutions. They realized that maintaining their
    custom-built solutions wasn’t sustainable, and the open-source alternatives are
    more efficient.
  sec: 2652
  time: '44:12'
  who: Andrey
- line: Exactly, they try to implement something themselves, but then find that other
    solutions can solve the problem more effectively. Once they realize that, they
    prefer to adopt a pre-built solution instead of maintaining their own.
  sec: 2662
  time: '44:22'
  who: Alexey
- line: Yes, absolutely. Everyone is looking for ways to improve what they already
    do, but with less effort. But when it comes to AI tools, it's not just about being
    AI-first or not. For example, take Kubernetes. We see it as a foundational platform,
    not just for AI-first or cloud-first companies, but for everyone. It’s universal
    and adaptable to various use cases, whether expert-level or beginner-level. It’s
    about reducing the cost of ownership by investing in one universal tool. This
    approach is challenging to implement, but it's what we strive for—making it flexible
    and accessible for all types of use cases.
  sec: 2673
  time: '44:33'
  who: Andrey
- line: Okay, but if we already have Kubernetes, why do we need another universal
    tool? I remember back when Kubernetes was mentioned, I was intimidated. I didn’t
    want to go near it, but once I understood how it worked, it turned out to be much
    easier. The main challenge is that not every company has the team to manage Kubernetes.
  sec: 2788
  time: '46:28'
  who: Alexey
- header: 'Orchestration Gaps: Kubernetes Limitations for AI Workflows and SLURM'
- line: 'Yes, exactly. This is one of the topics that requires more discussion. But
    at a high level, we’re focused on teams that are constrained by Kubernetes or
    other orchestration tools. Many teams experience specific pain points when working
    with Kubernetes, especially for AI use cases. Kubernetes wasn’t designed with
    AI in mind—it’s optimized for containers, but AI workflows often involve more
    complex processes like training. For instance, AI engineers don’t typically think
    in terms of containers; they think in terms of nodes and GPUs. This is why specialized
    tools like SLURM exist. It simplifies the process, and engineers prefer it because
    it’s tailored for AI workflows. This is one of the challenges we’re trying to
    solve: rethinking container orchestration for AI.'
  sec: 2836
  time: '47:16'
  who: Andrey
- line: So, the problem with Kubernetes is that it’s not optimized for AI use cases?
  sec: 2864
  time: '47:44'
  who: Alexey
- line: Exactly. Kubernetes is great for general container orchestration, but it doesn’t
    handle the specific needs of AI workflows. That's why we believe it’s time to
    rethink how container orchestration works for AI. We’re trying to create a tool
    that addresses these specific needs while remaining flexible and universal.
  sec: 2868
  time: '47:48'
  who: Andrey
- header: Kubernetes as the Deployment Standard vs Smaller Alternatives
- line: As a software engineer, should I stay away from Kubernetes, or is it still
    a good tool to have in my toolkit?
  sec: 3059
  time: '50:59'
  who: Alexey
- line: It's the only tool when it comes to deployment.
  sec: 3070
  time: '51:10'
  who: Andrey
- line: It is the only one. Regardless of whether you use AWS, Azure, or even Alibaba
    Cloud, you end up using Kubernetes.
  sec: 3076
  time: '51:16'
  who: Andrey
- line: I personally don't use it, but the projects I work on are smaller. I don't
    want to pay for a large Kubernetes cluster, but for companies with more than one
    person, it probably makes sense.
  sec: 3091
  time: '51:31'
  who: Alexey
- line: Yes, there are edge cases, but I’m speaking in more general terms.
  sec: 3106
  time: '51:46'
  who: Andrey
- header: 'Hybrid Infrastructure Outlook: Cloud Dominance and On‑Prem Nuances'
- line: 'Here''s a question: Do you think the future will be a hybrid of bare metal
    and cloud, or will it be cloud-only?'
  sec: 3116
  time: '51:56'
  who: Alexey
- line: Predicting the future is not easy, and some people enjoy making these predictions.
  sec: 3126
  time: '52:06'
  who: Andrey
- line: If we extrapolate current trends, though...
  sec: 3137
  time: '52:17'
  who: Alexey
- line: Cloud is the trend, and it’s the only trend.
  sec: 3141
  time: '52:21'
  who: Andrey
- line: Is it because people don't want to have a GPU machine under their desk?
  sec: 3152
  time: '52:32'
  who: Alexey
- line: I don’t know, 16,000 of them... It's more predictable for enterprises to use
    cloud. On the other hand, AI is a wildcard here. Nobody really knows what will
    happen. Many companies are currently investing in on-prem solutions due to AI.
    We’re seeing this trend, especially in AI-related fields. But I’m not an expert
    in that area. Personally, I prefer not to use the term "on-prem." It’s a confusing
    term. For example, you could have your own rack in your building and call it on-prem,
    or you could call it a data center. But when you refer to it as a data center,
    it could also be called a cloud. There are many difficulties with these terms.
    That's why, when I speak to myself, I avoid saying "on-prem" or "cloud" and just
    refer to them as different versions of cloud.
  sec: 3158
  time: '52:38'
  who: Andrey
- line: So, what I think...
  sec: 3268
  time: '54:28'
  who: Alexey
- line: Yeah.
  sec: 3268
  time: '54:28'
  who: Andrey
- header: 'On‑Prem GPU Coordination: SSH, Resource Contention, and Real Examples'
- line: When I think about on-prem, particularly for data teams, data science teams,
    and ML teams, I recall my first company in Germany. We had a machine with GPUs,
    and everyone had access to it. We would SSH into the machine, but then we had
    to coordinate GPU usage. If someone was using a GPU, others had to wait. In the
    end, it became a nightmare to coordinate. That’s what comes to mind when I think
    of on-prem GPU machines and the challenges involved.
  sec: 3271
  time: '54:31'
  who: Alexey
- line: Yes, you're right. On-prem means dealing with a lot of challenges yourself—maintaining
    the servers, managing updates, and orchestrating everything. With the cloud, much
    of this is handled as a service, but with on-prem, it's your responsibility.
  sec: 3322
  time: '55:22'
  who: Andrey
- line: It’s kind of like on-prem when you rent a machine from a remote provider but
    still have SSH access. For example, there's a provider in Germany called Hetzner
    where you can rent a machine with GPUs or powerful CPUs. You get SSH access to
    that machine, but it’s still remote. You’re still dealing with the same challenges
    we mentioned before. If you have a team of ten people and just a few machines,
    coordinating GPU usage for training models becomes a hassle. That’s another form
    of on-prem, right?
  sec: 3352
  time: '55:52'
  who: Alexey
- line: Yes, that’s one way to look at it.
  sec: 3406
  time: '56:46'
  who: Andrey
- line: Bare metal, right?
  sec: 3411
  time: '56:51'
  who: Alexey
- header: 'Bare‑Metal as a Service: Provisioning, Automation, and Firmware Management'
- line: Yes, bare metal as a service is another option. Some companies offer bare
    metal as a service, where they handle the provisioning and firmware updates for
    you. But if you want to run a service yourself across multiple bare metal providers,
    you'll need to automate the process and ensure everything stays up to date. It's
    a shared responsibility between the provider and yourself.
  sec: 3413
  time: '56:53'
  who: Andrey
- line: So, the best example of on-prem is a GPU machine under my desk?
  sec: 3468
  time: '57:48'
  who: Alexey
- line: By the way, we didn’t talk about edge computing. We can discuss that briefly
    if we have time.
  sec: 3473
  time: '57:53'
  who: Andrey
- line: We have time for another 5-10 minutes.
  sec: 3484
  time: '58:04'
  who: Alexey
- header: 'Edge Computing Scope: Devices, Local Models, and Definition Ambiguity'
- line: 'One last topic: edge computing and how it differs from cloud computing.'
  sec: 3487
  time: '58:07'
  who: Andrey
- line: What exactly is edge computing? Is it similar to devices like this one?
  sec: 3498
  time: '58:18'
  who: Alexey
- line: Well, to be completely fair, there might be experts who will correct me, but
    based on what I know, there’s no universal agreement on what exactly constitutes
    edge computing. I’d even say there’s a lot of confusion around it.
  sec: 3503
  time: '58:23'
  who: Andrey
- line: Most people might associate it with something like a Raspberry Pi, right?
    Or perhaps something else?
  sec: 3527
  time: '58:47'
  who: Alexey
- line: Yes, edge computing can refer to any customer-facing or site-facing device.
    It’s essentially any device that’s not in the cloud, but some people even consider
    certain cloud services as part of edge computing. For instance, edge AI is often
    mentioned by cloud companies, but it's essentially just normal cloud computing
    with localized compute capabilities. Using AWS, for example, could be considered
    edge computing by that logic, because you have AI in your region. On the other
    hand, edge can also refer to devices like mobile phones, laptops, smart home devices,
    video cameras, or drones flying around.
  sec: 3532
  time: '58:52'
  who: Andrey
- line: Hopefully, nothing is flying around right now!
  sec: 3600
  time: '1:00:00'
  who: Alexey
- line: Maybe not, but the point is that edge refers to remote devices. These devices
    often require smaller models because it’s difficult to run large-scale models
    on them.
  sec: 3604
  time: '1:00:04'
  who: Andrey
- header: 'Federated Learning vs Distributed Compute: Practicality and Use Cases'
- line: I think there are companies doing federated learning, right? For example,
    if there's a customer-facing device like a drone or a probe, you can't send all
    the data somewhere for training. Instead, the training happens on the device,
    and then the results are centralized later. Is this something that applies to
    LLMs or AI in general? I know it’s used in manufacturing setups.
  sec: 3630
  time: '1:00:30'
  who: Alexey
- line: Well, many people might disagree with me on this, but I would say that federated
    learning is a very niche use case. It's often debated, kind of like the discussion
    around 5G versus cloud computing. It's basically a distributed computing topic.
    Today, we call it distributed compute rather than federated learning. While it
    does share similarities with blockchain and decentralization, it can sometimes
    feel like a religious belief in the tech world. There are evangelists who promote
    the idea that everything should be decentralized, but even with blockchain, we’re
    not there yet. We see some things moving in that direction, but not everything.
  sec: 3664
  time: '1:01:04'
  who: Andrey
- line: Yeah, I’m not really following that space, but it’s interesting. Well, maybe
    just one more question for you.
  sec: 3755
  time: '1:02:35'
  who: Alexey
- line: Sure, sure. Closing this topic down, distributed computing is a big area,
    and there are a lot of experts who really believe in it.
  sec: 3762
  time: '1:02:42'
  who: Andrey
- header: 'Closing Pick: Science‑Fiction Recommendation — The Three‑Body Problem'
- line: So, last question for you. You mentioned you like science fiction. What’s
    your favorite book?
  sec: 3771
  time: '1:02:51'
  who: Alexey
- line: That’s one of the toughest questions. It’s much easier to talk about challenges
    in distributed training than to pick just one book!
  sec: 3779
  time: '1:02:59'
  who: Andrey
- line: Well, pick one if you can!
  sec: 3790
  time: '1:03:10'
  who: Alexey
- line: Alright, if we’re talking science fiction, I’d definitely say The Three-Body
    Problem.
  sec: 3791
  time: '1:03:11'
  who: Andrey
- line: Yeah, I’ve heard of it.
  sec: 3808
  time: '1:03:28'
  who: Alexey
- line: It’s by Liu Cixin, a Chinese author. I’m probably pronouncing it wrong, but
    he’s well-known in the sci-fi world. Even if you're not into science fiction,
    this book is widely recognized.
  sec: 3814
  time: '1:03:34'
  who: Andrey
- line: I haven’t heard of him. I’m not really into science fiction, but I did read
    Ringworld a year ago, which was interesting. I’m looking to expand my reading,
    though.
  sec: 3842
  time: '1:04:02'
  who: Alexey
- line: I totally recommend The Three-Body Problem. It’s actually a trilogy, not just
    one book. The first book is named after the three-body problem in physics, which
    refers to a mathematical challenge of predicting the motion of three celestial
    bodies, like three suns.
  sec: 3856
  time: '1:04:16'
  who: Andrey
- line: I’m looking up the article on Euler’s Three-Body Problem now. It’s a difficult
    problem in physics and astronomy.
  sec: 3905
  time: '1:05:05'
  who: Alexey
- line: Yes, the book goes beyond math, though, and explores philosophy, politics,
    and existential problems. It’s a great read for anyone looking to kill some time.
  sec: 3920
  time: '1:05:20'
  who: Andrey
- header: Episode Wrap‑Up & Links to DStack and Guest Resources
- line: Sounds interesting! Thanks a lot, Andrey. We only touched on a fraction of
    the topics we wanted to discuss today, which is no surprise, given how much we
    wanted to cover. But it was great talking with you. Thanks for accepting the invite,
    and I really enjoyed our conversation. I’m looking forward to working more with
    you in the future.
  sec: 3938
  time: '1:05:38'
  who: Alexey
- line: Thank you! It was a pleasure, and I look forward to it as well.
  sec: 3964
  time: '1:06:04'
  who: Andrey
---

Links:

* [Twitter](https://twitter.com/andrey_cheptsov/){:target="_blank"}
* [Linkedin](https://www.linkedin.com/in/andrey-cheptsov/){:target="_blank"}
* [GitHub](https://github.com/dstackai/dstack/){:target="_blank"}
* [Website](https://dstack.ai/){:target="_blank"}