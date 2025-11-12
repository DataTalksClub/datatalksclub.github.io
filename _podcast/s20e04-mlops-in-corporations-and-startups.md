---
episode: 4
guests:
- nemanjaradojkovic
ids:
  anchor: atalksclub/episodes/MLOps-in-Corporations-and-Startups---Nemanja-Radojkovic-e304g53
  youtube: DX9c__a4jzg
image: images/podcast/s20e04-mlops-in-corporations-and-startups.jpg
links:
  anchor: https://creators.spotify.com/pod/show/datatalksclub/episodes/MLOps-in-Corporations-and-Startups---Nemanja-Radojkovic-e304g53
  apple: https://podcasts.apple.com/us/podcast/mlops-in-corporations-and-startups-nemanja-radojkovic/id1541710331?i=1000699195928
  spotify: https://open.spotify.com/episode/6V8gkTSz7LuPjQYC4rO019
  youtube: https://www.youtube.com/watch?v=DX9c__a4jzg
season: 20
short: MLOps in Corporations and Startups
title: 'Lean MLOps for Startups: SaaS-First MVP Stack, Avoid Vendor Lock-In & Manage
  Tech Debt'
transcript:
- header: Episode Introduction & Topic Overview
- line: This week, we’ll talk about MLOps in corporations versus startups. Our special
    guest is Nemanja, who’s been on the podcast before. Last year, we discussed machine
    learning engineering in finance, which turned out to be one of our most popular
    episodes.
  sec: 60
  time: '1:00'
  who: Alexey
- line: Nemanja later mentioned on LinkedIn, “Hey, how about we record another one?”
    I thought it was a great idea. So, welcome back! It’s a pleasure to have you here
    again.
  sec: 60
  time: '1:00'
  who: Alexey
- line: The questions for today’s interview were prepared by Johanna. Thanks, Johanna,
    for your help.
  sec: 60
  time: '1:00'
  who: Alexey
- line: During our small talk earlier, you gave us a brief update, but maybe you can
    share a more detailed one. For those who didn’t hear the previous podcast, can
    you tell us about your career journey and what you’ve been up to in the last year?
  sec: 60
  time: '1:00'
  who: Alexey
- header: 'Career Journey: Academia → Consulting → Finance Machine Learning Engineering'
- line: Sure! I was born and raised in Belgrade, Serbia, where I completed my bachelor’s
    and master’s studies in electrical engineering, focusing on signals and systems.
    This was my first exposure to machine learning theory.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: After gaining some work experience there, I moved to Belgium to pursue a PhD
    in bioengineering. It might sound like a strange switch, but the theory of systems
    modeling applies across domains. Many data scientists switch fields because the
    underlying principles are universal.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: However, I quickly realized academia wasn’t for me. After a year and a half,
    I accepted an offer from Deloitte Consulting in Belgium, where I worked for about
    three years. My PhD was my first paid job in data science, and at Deloitte, I
    started doing more machine learning engineering, including prototyping models
    and deploying them.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: Back then, MLOps wasn’t a term, but someone had to do it. I learned proper
    Python development practices, project packaging, and deploying on AWS. By 2019,
    I was fully focused on machine learning engineering.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: Over the last five to six years, I’ve worked mainly in the financial industry,
    which is why we had our previous talk. I’ve worked with several big banks, including
    ING, BNP Paribas, Euroclear, and KBC.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: In June last year, I decided to become a freelancer, something I’d planned
    for years. I took a short mission with KBC and then joined a Brussels-based startup
    called Tempo, where I helped industrialize some Python code. Starting February,
    I’ll be working with another company in Ghent.
  sec: 135
  time: '2:15'
  who: Nemanja
- line: I’ve worked across various industries, including healthcare, transportation,
    logistics, and chemicals. Most of my experience has been with Fortune 500 companies,
    but working with a startup has been an eye-opening experience.
  sec: 135
  time: '2:15'
  who: Nemanja
- header: 'Startup Pace: Agility, Speed, and Managerial Insights'
- line: Working in a startup feels like flying. You don’t have the bureaucratic restrictions
    that exist in big corporations. Of course, those restrictions often serve as safety
    nets, but they can also slow things down.
  sec: 363
  time: '6:03'
  who: Nemanja
- line: The last two months have made me want to go back to my previous companies
    and ask, “Why can’t we move at least half as fast?” I think many managers in traditional
    corporations could benefit from spending time in a startup to see how agile and
    fast-paced things can be.
  sec: 363
  time: '6:03'
  who: Nemanja
- header: 'Lean MLOps: Shoestring Strategies for Early-Stage Companies'
- line: When we met at the DataMakers Fest conference, we ended up in the same car
    and started talking. I also attended your talk, which was about doing MLOps on
    a shoestring budget.
  sec: 474
  time: '7:54'
  who: Alexey
- line: The main idea was that you don’t need fancy tools to get started with MLOps.
    You showed how to use basic tools and principles to get going. It felt very startup-like—starting
    simple and adding complexity as needed, versus the corporate approach of planning
    everything in advance.
  sec: 474
  time: '7:54'
  who: Alexey
- line: How well do those ideas translate to the startup world?
  sec: 474
  time: '7:54'
  who: Alexey
- line: They translate very well. Startups have to be lean because they often operate
    on tight budgets. When I delivered that talk, one of the first slides clarified
    what “shoestring” can mean. We usually think of it as a tight budget, which is
    true for startups.
  sec: 565
  time: '9:25'
  who: Nemanja
- line: Some startups might raise significant funding, like $500 million, to develop
    advanced AI, but that’s not the norm. Some startups have tight budgets in terms
    of money, while others are constrained by time or human resources.
  sec: 565
  time: '9:25'
  who: Nemanja
- line: In big companies, there’s usually more money, but you need to choose your
    battles carefully. It’s like having a gun with six bullets—you need to aim and
    shoot carefully. That’s the shoestring in a corporation.
  sec: 565
  time: '9:25'
  who: Nemanja
- line: In a startup, it’s usually about money and the number of people. Decisions
    like hiring or adopting new tools require careful consideration. It’s tempting
    in startups to use many tools because it’s easy to make quick agreements.
  sec: 565
  time: '9:25'
  who: Nemanja
- line: In a startup, you can just talk to one or two people and make a decision.
    This can lead to an explosion of tools and accounts, which is something big corporations
    prevent. In a corporation, you’re told, “This is the way we do it. End of story.”
  sec: 646
  time: '10:46'
  who: Nemanja
- line: For example, in my previous company, onboarding a new vendor was an adventure.
    It involved so many people, and the contract wasn’t even large. The next time
    I needed to onboard a new tool, I’d think twice.
  sec: 646
  time: '10:46'
  who: Nemanja
- line: In a startup, it’s different. You might sit next to someone and say, “Hey,
    I just saw this demo. How about we try it?” And the answer is, “Yeah, let’s try
    it.” That’s exactly how it goes.
  sec: 646
  time: '10:46'
  who: Nemanja
- header: 'SaaS-First Approach: Vendor Solutions for Small Teams'
- line: At Tempo, where I’m working now, it’s like, “Should we try this? Should we
    try that? Let’s try Logfire, Grafana, or this other tool.” You experiment and
    keep what works best.
  sec: 714
  time: '11:54'
  who: Nemanja
- line: I think startups should go for vendor solutions, like cloud-based software-as-a-service
    (SaaS), instead of building their own. Big companies often want to build their
    own solutions, but that requires maintenance.
  sec: 714
  time: '11:54'
  who: Nemanja
- line: When you have four to ten people in a company, you don’t want a dedicated
    person for BI or infrastructure. You’d rather use SaaS and avoid hiring someone
    to maintain servers.
  sec: 714
  time: '11:54'
  who: Nemanja
- header: 'Cloud Trade-offs: Startup Credits, Migration Friction, and Lock‑in'
- line: Going on-premise is hard for a startup unless it makes a lot of sense. I think
    it’s a no-brainer for startups to go for the cloud. However, there needs to be
    a clever decision because migrating from one cloud to another can be slow and
    annoying.
  sec: 774
  time: '12:54'
  who: Nemanja
- line: Google, for example, has a “catch them while they’re young” program. They
    offer credits to get startups to use their platform. Many companies take the offer,
    and some stay even if they’re not entirely happy because migrating is costly.
  sec: 774
  time: '12:54'
  who: Nemanja
- line: It’s a strategy. Last time I checked, Google offered significant credits to
    small businesses—maybe around $50,000. For a small company, that could mean free
    cloud usage for a year.
  sec: 830
  time: '13:50'
  who: Nemanja
- line: But there’s a catch. You have to stay within Google Cloud, and some services
    might not be included. It’s a bit of a trick. If you burn through the credits
    in a month, that’s your problem.
  sec: 830
  time: '13:50'
  who: Nemanja
- line: Can’t it become chaotic? It’s so easy to start using a new tool, and then
    you end up with a bunch of tools that barely connect, and everything falls apart.
  sec: 888
  time: '14:48'
  who: Alexey
- header: 'Cloud Complexity: Infrastructure as Code and Operational Overhead'
- line: Yes, the cloud adds extra complexity. I’ve worked mainly on-premise for about
    seven to eight years out of my ten years in data science. I always wanted more
    cloud experience, but when I fully switched to the cloud, I thought, “Wait, I
    want to go back to on-premise.”
  sec: 906
  time: '15:06'
  who: Nemanja
- line: On-premise has its limitations. It’s less flexible, and scaling is a challenge.
    But in the end, the infrastructure is straightforward. You have machines—bare
    metal or virtual machines—switches, disks, and applications running behind firewalls.
  sec: 906
  time: '15:06'
  who: Nemanja
- line: In the cloud, you have key management, identity management, and so many moving
    parts to configure. It quickly becomes overwhelming. Without infrastructure as
    code, it’s a mess. Even with infrastructure as code, it’s manageable but still
    complex.
  sec: 906
  time: '15:06'
  who: Nemanja
- line: If you start configuring things manually, it’s hard to replicate later. For
    example, I once deployed something through the console due to time constraints.
    Six months later, I wondered if I could repeat it. Would I remember all the steps?
  sec: 985
  time: '16:25'
  who: Nemanja
- line: The cloud adds an extra layer of complexity. You might have one tool for dashboards,
    another for logging, and so on. There’s no analytical formula to optimize and
    find the perfect tool stack. It’s more of an NP-hard problem—you just have to
    make the best choice.
  sec: 985
  time: '16:25'
  who: Nemanja
- line: As I understand, you work with young companies—startups—that rely on the cloud.
    But most of your experience has been with big companies. Now, in the last two
    months, you’ve had to make choices for startups.
  sec: 1043
  time: '17:23'
  who: Alexey
- header: 'MVP Stack: Prioritizing Tools for Rapid Prototyping and Launch'
- line: 'Yes, for this startup, the priority was to have certain features ready within
    two months: a visualization dashboard, an industrialized API, and so on. The goal
    was to make it robust and fast so we could move to the next stage and launch the
    product.'
  sec: 1058
  time: '17:38'
  who: Nemanja
- line: Based on experience, I can’t justify trying 20 different tools. Instead, I
    say, “Based on my experience, this is a good choice. Let’s go with it.” If it
    takes a day or two to prototype, I show it and ask, “Does this look good? Let’s
    go with that.”
  sec: 1058
  time: '17:38'
  who: Nemanja
- line: You can’t go wrong with certain tools. For example, if you choose PostgreSQL
    as your database, no one will question it. It’s a proven choice.
  sec: 1109
  time: '18:29'
  who: Nemanja
- line: At the beginning, you might not need complex tools. For example, we recently
    discussed Kubeflow in Slack. Kubeflow is a full-blown Kubernetes-based MLOps platform.
    I’ve never tried it, but I’ve seen demos. It seems like a huge pain with all the
    YAML files and Kubernetes complexity.
  sec: 1109
  time: '18:29'
  who: Nemanja
- header: 'Portability vs Managed Services: Avoiding Vendor Lock‑In (Vertex AI, SageMaker)'
- line: I tried Kubeflow, and it was a huge pain because of all the YAML files and
    Kubernetes complexity. Maybe it makes sense in the long run, but at the beginning,
    you might just need Flask or something simpler.
  sec: 1159
  time: '19:19'
  who: Alexey
- line: In your talk, you showed how to get started with simple tools instead of going
    for big solutions that you might need in two years. Right now, the goal is to
    move quickly and choose the simplest tool for the task.
  sec: 1159
  time: '19:19'
  who: Alexey
- line: The idea is to make sure it’s fast, reliable, and not overly complicated so
    you can move quickly. If you need to spend a week configuring Kubeflow, maybe
    it’s not the best tool for now.
  sec: 1198
  time: '19:58'
  who: Alexey
- line: The richer a solution is in features, the more it locks you in. For example,
    if you’re doing something in Python with scripts on a remote server, you can always
    change the server or provider.
  sec: 1217
  time: '20:17'
  who: Nemanja
- line: But if you’re using something like Google Cloud’s Vertex AI or AWS SageMaker,
    you’re pretty much tied to that platform. If you want to migrate later, you’ll
    need to retrain models. The question is, were those models trained in a reproducible
    way?
  sec: 1217
  time: '20:17'
  who: Nemanja
- line: So, the takeaway is to make your choices as portable as possible at the beginning.
    Choose tools that are more generic rather than specific to a particular vendor.
  sec: 1274
  time: '21:14'
  who: Alexey
- header: 'Low‑Code Trade-offs: Speed vs Future Flexibility'
- line: Yes, that makes you more portable. Some startups might want to start as fast
    as possible using low-code solutions. If you can only hire a data scientist and
    not a proper software or systems engineer, you might go with a low-code platform.
  sec: 1295
  time: '21:35'
  who: Nemanja
- line: In that case, the data scientist develops a model in a notebook environment
    and deploys it with a click. That can work, but I prefer having the freedom to
    avoid lock-in.
  sec: 1295
  time: '21:35'
  who: Nemanja
- header: 'Career Decision Framework: Choosing Startups or Corporations'
- line: Let’s imagine I am a machine learning engineer with two offers—one from a
    startup and one from a Fortune 500 company. How should I decide between the two?
  sec: 1342
  time: '22:22'
  who: Alexey
- line: Let’s say the startup pays less but offers some stock options. For this scenario,
    imagine our engineer doesn’t need to prioritize money heavily.
  sec: 1348
  time: '22:28'
  who: Alexey
- line: It depends on several factors. Personally, I would lean toward a startup,
    especially depending on the stage of your career. Are we talking about someone
    in the early stages of their career?
  sec: 1378
  time: '22:58'
  who: Nemanja
- line: Maybe we can explore what factors we should consider in making this decision.
  sec: 1391
  time: '23:11'
  who: Alexey
- line: In a corporation, you typically have job security and a narrow scope of work.
    If you’re fine specializing in one area, sticking to it, and working a predictable
    9-to-5 schedule, then a corporation might be the right choice. This is a legitimate
    decision, and I followed it for many years.
  sec: 1397
  time: '23:17'
  who: Nemanja
- line: On the other hand, if you want to move faster, learn quicker, and try out
    more things without spending unnecessary time in meetings, a startup is a better
    fit. However, startups come with risks.
  sec: 1397
  time: '23:17'
  who: Nemanja
- line: For instance, if the atmosphere in a small company is bad, there’s no escaping
    it. In a larger company, you have the option to switch teams or departments, which
    provides some flexibility. Large corporations also offer internal mobility, letting
    you shift between data engineering, machine learning, MLOps, DevOps, and so on.
  sec: 1397
  time: '23:17'
  who: Nemanja
- line: In startups, if things go south, the impact is more immediate. However, in
    the right startup environment—like the one I’m in now—it can be incredibly rewarding.
    That said, I’ve heard stories of less ideal startup experiences.
  sec: 1479
  time: '24:39'
  who: Nemanja
- line: Startups often involve working toward future gains, like the eventual sale
    of the company. For someone early in their career, wanting to learn a lot, I also
    recommend consultancies. Like startups, consultancies expose you to various tools
    and approaches, allowing you to triangulate patterns and identify best practices.
  sec: 1479
  time: '24:39'
  who: Nemanja
- line: In large companies, there’s often a rigid approach to processes. For example,
    I’ve seen CICD pipelines or Python projects set up in ways that were clearly wrong,
    but employees had adapted to them. Sometimes, they didn’t even realize these setups
    were suboptimal.
  sec: 1544
  time: '25:44'
  who: Nemanja
- line: When I pointed out issues to one company, a team member told me she always
    felt something was wrong but lacked the arguments to explain why.
  sec: 1570
  time: '26:10'
  who: Nemanja
- line: Even if something is wrong in a corporation, you don’t always have the flexibility
    to change it.
  sec: 1609
  time: '26:49'
  who: Alexey
- line: Exactly. If you’ve only ever seen one way of doing things, it’s hard to imagine
    alternatives. You might feel something is off but lack the knowledge to propose
    a better solution. That’s where external experience can help. Someone from outside
    can show a better approach.
  sec: 1614
  time: '26:54'
  who: Nemanja
- line: If you graduate, join a corporation, and stay there for ten years, you only
    know one way of doing things. It might not be the best way, but it’s all you’ve
    learned. In a startup, you explore multiple approaches, gaining broader exposure.
  sec: 1631
  time: '27:11'
  who: Nemanja
- header: 'End‑to‑End Ownership: Multidisciplinary Work in Startups'
- line: Startups also pivot frequently. A small, young startup might shift directions
    completely based on client demands. One client might leave, and another might
    request something entirely different. This kind of abrupt change keeps things
    exciting but also challenging.
  sec: 1650
  time: '27:30'
  who: Nemanja
- line: For me, startups feel like a pack of hunters navigating the wild, chasing
    something big and uncertain. There’s a strong sense of camaraderie and ownership.
  sec: 1688
  time: '28:08'
  who: Nemanja
- line: In the last two months at Tempo, I’ve done work that would require two or
    three separate teams in a large corporation. Beyond my core tasks—industrializing
    Python code—I provisioned infrastructure, created pipelines, and managed repositories
    on my own.
  sec: 1688
  time: '28:08'
  who: Nemanja
- line: In many big companies, you can’t even create a repository without submitting
    a ticket. It feels bureaucratic, like waiting in line at city hall. You know how
    to do the task, but the system won’t let you.
  sec: 1743
  time: '29:03'
  who: Nemanja
- header: 'Corporate Processes: "Agile" vs Bureaucratic Planning Cycles'
- line: Big corporations often label their processes as "agile," but it’s often just
    waterfall broken into smaller increments. For example, if you miss a quarterly
    planning session, you’re told to wait three months for the next one.
  sec: 1777
  time: '29:37'
  who: Nemanja
- line: I have PTSD; you have flashbacks. Flashbacks now? Oh, sorry, it’s not for
    this quarter.
  sec: 1813
  time: '30:13'
  who: Alexey
- line: Yeah, yeah, yeah. No, but—how should I say—I said in advance I’m going to
    bash corporations a bit, but I had a lot of good times there. I had a lot of very
    good teams, very good friends, which I really love.
  sec: 1821
  time: '30:21'
  who: Nemanja
- line: And, yeah, these corporations, as I said, they give you some stability. They
    give you some... I would say you know what to expect there. And you learn some
    things, also.
  sec: 1835
  time: '30:35'
  who: Nemanja
- line: For example, this whole networking thing in a big company—it’s even more important
    than your hands-on knowledge. It’s about building a network within the company
    and having, what I would call, “my guy” in DevOps or “my guy” in networking.
  sec: 1847
  time: '30:47'
  who: Nemanja
- line: You have people with whom you have good connections. It shouldn’t be like
    that because everything should work through requests and processes, but in the
    end, you know that out of ten people, there’s this one person you know, and they’ll
    get things done faster for you.
  sec: 1855
  time: '30:55'
  who: Nemanja
- line: 'So yeah, again, it’s like a city hall: if you know the right people.'
  sec: 1870
  time: '31:10'
  who: Nemanja
- line: I summarize what you said. In a corporation, you get stability, financial
    safety, and a narrow scope of work. You become a specialist in one thing. Plus,
    there’s some guidance and framework, which, if you’re just starting, can teach
    you how to do things.
  sec: 1883
  time: '31:23'
  who: Alexey
- line: You also have internal mobility. But there’s less flexibility in technology
    because many decisions have already been made. It can feel like a city hall or
    town hall because there are so many different teams.
  sec: 1898
  time: '31:38'
  who: Alexey
- line: To get something done, you often need to create tickets, which adds bureaucratic
    overhead. As you mentioned, there’s quarterly planning, and if something isn’t
    planned for this quarter, you may have to wait for the next.
  sec: 1910
  time: '31:50'
  who: Alexey
- line: In startups, you move and learn faster. There are fewer meetings and less
    bureaucracy. You work with greenfield projects without legacy frameworks or structures.
    While frameworks can be helpful, they can also slow you down.
  sec: 1928
  time: '32:08'
  who: Alexey
- line: But wait, a good framework should make you move faster. In a corporation,
    one of my roles was creating frameworks to speed things up.
  sec: 1959
  time: '32:39'
  who: Nemanja
- line: For example, if we knew that over the next two or three years we’d have similar
    projects—like building models for email classification and deploying them—then
    we’d create templates to make deployments faster.
  sec: 1980
  time: '33:00'
  who: Nemanja
- header: 'Platform & Frameworks: Automating Developer Workflows'
- line: That’s how it should work. But something goes wrong when companies slice and
    dice domains of responsibility too much.
  sec: 1997
  time: '33:17'
  who: Nemanja
- line: Ideally, developers or application builders shouldn’t even know a DevOps or
    platform team exists. They should have everything automated and ready to go, only
    needing to submit a few initial requests to set up infrastructure.
  sec: 2021
  time: '33:41'
  who: Nemanja
- line: Of course, nobody should be able to spin up 100 VMs with 100 GPUs unchecked,
    but the process can be streamlined.
  sec: 2040
  time: '34:00'
  who: Nemanja
- line: These downsides aren’t inevitable in corporations. They have the resources
    and people to do better.
  sec: 2054
  time: '34:14'
  who: Nemanja
- header: 'Team Scale Advantages: Redundancy, Support, and Internal Mobility'
- line: One advantage in corporations is being part of a big team. If you go on holiday,
    someone else can pick up your work. In startups, this is much harder because they’re
    so lean.
  sec: 2072
  time: '34:32'
  who: Nemanja
- line: In a corporation, there’s always someone to help you troubleshoot or answer
    questions. In a startup, it’s more chaotic.
  sec: 2103
  time: '35:03'
  who: Nemanja
- line: 'There’s a general rule: don’t be the first data scientist in an organization
    if you’re a junior. It’s fine if you’re senior, but if you’re the only person,
    look somewhere else.'
  sec: 2109
  time: '35:09'
  who: Nemanja
- line: So what you’re saying is that startups have more chaos, and you need to be
    comfortable with it.
  sec: 2126
  time: '35:26'
  who: Alexey
- line: Exactly. It’s like a warpath. You need to be robust. It’s never boring, though!
  sec: 2132
  time: '35:32'
  who: Nemanja
- header: 'Startup Intensity: Learning Curve, Burnout Risk, and Rewards'
- line: But also, what you didn’t mention—and what I experienced—is that it’s never
    boring. Yes, and you have this cool end-to-end ownership of things.
  sec: 2148
  time: '35:48'
  who: Alexey
- line: 'You feel this: "Okay, I produce some code, and I see it in action." It doesn’t
    need to go through ten steps of approval or whatever.'
  sec: 2155
  time: '35:55'
  who: Alexey
- line: But on the other hand, because of the constant firefighting mode—constantly
    pivoting, constantly working on something—things break, and you try to fix them.
  sec: 2161
  time: '36:01'
  who: Alexey
- line: At least, that was my experience. At the end of the day, I felt exhausted.
    I gave more than 100%, and it was super difficult for me to do anything after
    work.
  sec: 2169
  time: '36:09'
  who: Alexey
- line: After one year, I was like, "I’m burned out." In corporations, that doesn’t
    happen.
  sec: 2193
  time: '36:33'
  who: Alexey
- line: You don’t have to move at that speed. In startups, you’re running all the
    time, whereas in a corporation, it’s more like a walk in the park.
  sec: 2200
  time: '36:40'
  who: Alexey
- line: Yeah, but that’s what I’m saying. Both have their pluses and minuses.
  sec: 2216
  time: '36:56'
  who: Nemanja
- line: For me, it’s refreshing that I can move at my maximum speed. But again, I’ve
    only been doing this for two months.
  sec: 2222
  time: '37:02'
  who: Nemanja
- line: If I kept this pace for a year, I’d probably also be close to burnout. But,
    you know, in Eastern Europe, we don’t have burnout.
  sec: 2230
  time: '37:10'
  who: Nemanja
- line: Right? What is that?
  sec: 2242
  time: '37:22'
  who: Nemanja
- line: We don’t accept it.
  sec: 2249
  time: '37:29'
  who: Alexey
- line: But the amount of things I learned—because I needed to build so many things
    from scratch and solve real problems with real clients—was incredible.
  sec: 2249
  time: '37:29'
  who: Alexey
- line: Yeah, that’s true.
  sec: 2267
  time: '37:47'
  who: Nemanja
- header: 'AI‑Assisted Coding: Productivity Gains and Technical Debt Risks'
- line: But you know what I see as a risk now with LLMs and AI-assisted coding?
  sec: 2274
  time: '37:54'
  who: Nemanja
- line: It’s a kind of trap. I realized how quickly I could do many things for which
    I’m not really an expert, and it works.
  sec: 2279
  time: '37:59'
  who: Nemanja
- line: But I’m thinking, okay, this has only been two months. What if I work like
    this for two years?
  sec: 2286
  time: '38:06'
  who: Nemanja
- line: My primary competence is Python, but suddenly, I’m doing Ansible scripts,
    GitHub pipelines, and HTML with AI's help.
  sec: 2292
  time: '38:12'
  who: Nemanja
- line: AI helps me so much that I can handle 10–20 different areas. But what happens
    when this code needs to be maintained?
  sec: 2303
  time: '38:23'
  who: Nemanja
- line: Because I’ve seen people online bragging about how one person can do three
    weeks’ work alone. But how much of that code is technical debt?
  sec: 2315
  time: '38:35'
  who: Nemanja
- line: What part of the code will become a monster to maintain a year later?
  sec: 2321
  time: '38:41'
  who: Nemanja
- line: Ninety percent of it, probably.
  sec: 2332
  time: '38:52'
  who: Alexey
- line: Exactly. That’s why I joke that we had "schema-on-write" with SQL, then "schema-on-read"
    with NoSQL.
  sec: 2339
  time: '38:59'
  who: Nemanja
- line: Now, with AI coding, it’s "learn-on-write" and later "learn-on-maintain."
  sec: 2350
  time: '39:10'
  who: Nemanja
- line: When the code breaks, you have to go back and learn it all over again.
  sec: 2357
  time: '39:17'
  who: Nemanja
- line: It’s going to make things very interesting.
  sec: 2363
  time: '39:23'
  who: Nemanja
- line: For a startup, it might be okay, depending on how much technical debt you
    let accumulate.
  sec: 2370
  time: '39:30'
  who: Alexey
- line: Yeah, but imagine you see some weird code in a company. You run git blame
    and ask, "Who wrote this?"
  sec: 2375
  time: '39:35'
  who: Nemanja
- line: Often, I ask, "Why did you do this exception handling in this way?" And the
    person explains the reasoning.
  sec: 2381
  time: '39:41'
  who: Nemanja
- line: What if that person is you?
  sec: 2393
  time: '39:53'
  who: Alexey
- header: 'Technical Debt Management: Notes, Awareness, and Security Implications'
- line: Yeah, that also happens. But I think LLMs are drastically increasing the amount
    of technical debt we’re creating.
  sec: 2401
  time: '40:01'
  who: Nemanja
- line: You can move fast. I’ve done certain simple applications super quickly.
  sec: 2414
  time: '40:14'
  who: Nemanja
- line: But for a startup, isn’t it okay to move fast and deal with technical debt
    later?
  sec: 2426
  time: '40:26'
  who: Alexey
- line: Of course, you need to keep in mind that you’ll have to repay this debt, but
    you accept it.
  sec: 2433
  time: '40:33'
  who: Alexey
- line: Yes, but someone needs to be aware of the risks.
  sec: 2444
  time: '40:44'
  who: Nemanja
- line: Whenever I do something quick and dirty, I leave a note saying, “This needs
    to be checked.”
  sec: 2451
  time: '40:51'
  who: Nemanja
- line: But if you’re a junior, you might not be aware of what you’re leaving behind.
  sec: 2457
  time: '40:57'
  who: Nemanja
- line: It’s easy to move fast and leave ports open or create security holes.
  sec: 2463
  time: '41:03'
  who: Nemanja
- line: For example, if your startup’s value is 90% in its data and that data gets
    leaked, you’ve killed your startup.
  sec: 2472
  time: '41:12'
  who: Nemanja
- line: Moving fast is fine if you take informed risks. You need to have a strategy
    and be aware of vulnerabilities you’re living with.
  sec: 2487
  time: '41:27'
  who: Nemanja
- line: If you rely on LLMs without much thought, you’re risking a lot.
  sec: 2515
  time: '41:55'
  who: Nemanja
- line: So, be ready to repay that debt at some point.
  sec: 2526
  time: '42:06'
  who: Alexey
- line: Yes, it’s like a loan—you use it to leverage something and deliver value quickly,
    but you need to be aware of repayment.
  sec: 2532
  time: '42:12'
  who: Nemanja
- line: That’s why it’s not a good idea for a junior to join a startup as the only
    data scientist.
  sec: 2557
  time: '42:37'
  who: Alexey
- line: With LLMs, juniors can do a lot, but their lack of experience means they might
    not realize what’s suboptimal.
  sec: 2562
  time: '42:42'
  who: Alexey
- line: Without someone to guide them, it can create big problems.
  sec: 2586
  time: '43:06'
  who: Alexey
- header: 'Early‑Career Advice: Mentorship, Pairing, and Role Selection'
- line: For juniors, is it better to join a corporation or a more established company?
  sec: 2592
  time: '43:12'
  who: Alexey
- line: Any company where there are at least two or more seniors to learn from is
    ideal.
  sec: 2605
  time: '43:25'
  who: Nemanja
- line: As a junior, you’ll learn anywhere in your first 2–3 years, but after that,
    you might feel saturated.
  sec: 2611
  time: '43:31'
  who: Nemanja
- line: In consulting, jumping from client to client is normal. But in other fields,
    jumping from job to job might look bad on your CV.
  sec: 2628
  time: '43:48'
  who: Nemanja
- header: 'Minimal MLOps Stack: Python, CI/CD Orchestration, and Dagster'
- line: 'We have quite a few questions. One is: What tools do you use for your MLOps
    projects, and how do you balance time between new and old tools?'
  sec: 2650
  time: '44:10'
  who: Alexey
- line: Right now, my approach is to keep things as minimal as possible.
  sec: 2674
  time: '44:34'
  who: Nemanja
- line: I mainly use Python for scripts and training, and I try to handle orchestration
    through CI/CD pipelines.
  sec: 2682
  time: '44:42'
  who: Nemanja
- line: I’m starting a project with Dagster for orchestration, which I’m excited about.
  sec: 2701
  time: '45:01'
  who: Nemanja
- line: You need some kind of orchestrator. I’ve used MLflow and recently helped a
    startup set up their internal MLflow tracking server.
  sec: 2708
  time: '45:08'
  who: Nemanja
- line: 'For MLOps frameworks, there aren’t many components: model registries, feature
    stores, etc.'
  sec: 2727
  time: '45:27'
  who: Nemanja
- line: I haven’t set up a feature store yet but try to pick top tools that are mature
    and established.
  sec: 2739
  time: '45:39'
  who: Nemanja
- header: 'Observability Choices: Logfire, Prometheus/Grafana, and Streamlit'
- line: For observability, I recently used Logfire, which I really liked.
  sec: 2755
  time: '45:55'
  who: Nemanja
- line: Logfire is from the creator of Pydantic. It sends detailed logs and tracebacks
    with minimal setup.
  sec: 2763
  time: '46:03'
  who: Nemanja
- line: Compared to something like Grafana and Prometheus, Logfire was working within
    an hour.
  sec: 2784
  time: '46:24'
  who: Nemanja
- line: It collects application logs, system logs, memory, and CPU usage.
  sec: 2803
  time: '46:43'
  who: Nemanja
- line: It also has plugins for frameworks like FastAPI and TensorFlow, which add
    extra functionality.
  sec: 2810
  time: '46:50'
  who: Nemanja
- line: There are lots of options out there, and many blog posts cover possible configurations.
  sec: 2825
  time: '47:05'
  who: Nemanja
- line: 'Yeah, so I think, yeah, that sounds—it''s the first time I hear about this.
    So previously, like for logs, the tool I would go with would be ELK: Elasticsearch,
    Logstash, Kibana.'
  sec: 2834
  time: '47:14'
  who: Alexey
- line: Or sometimes instead of Logstash, you have something else, but it's not Point
    B.
  sec: 2841
  time: '47:21'
  who: Alexey
- line: It's very new. It's like less than a year old, and it's like the big, big
    new project from the Pantic people.
  sec: 2846
  time: '47:26'
  who: Nemanja
- line: When it comes to Grafana, you don't use it usually?
  sec: 2852
  time: '47:32'
  who: Alexey
- line: No, I started and I gave up. It looks like too mature, so I'm not a BI person.
    And, for example, yeah, recently I used Streamlit for some visualization.
  sec: 2857
  time: '47:37'
  who: Nemanja
- line: I really like how Streamlit works. Of course, it's so simple. It's so simple,
    but the only thing I have a problem with—like also MLflow and Streamlit—is the
    moment you want to get to the point of authentication.
  sec: 2862
  time: '47:42'
  who: Nemanja
- line: Like, they do have some basic authentication, but it's hard to get like full
    enterprise-level stuff, you know.
  sec: 2870
  time: '47:50'
  who: Nemanja
- line: Like, I don't know, integrating with Active Directory or whatnot. For that,
    you need to take some kind of a paid version.
  sec: 2876
  time: '47:56'
  who: Nemanja
- line: Databricks has it or whatever, yeah.
  sec: 2883
  time: '48:03'
  who: Nemanja
- header: 'Product Modularity: Desire for Standalone Model Registries & Observability'
- line: Yeah, it's not that simple. I remember trying to talk to Databricks people,
    saying, "Hey, I just want MLflow with authentication. I don’t need anything else,
    just MLflow."
  sec: 2891
  time: '48:11'
  who: Alexey
- line: Yeah, but, you know, it only comes with the Databricks platform, so you kind
    of have to take the whole thing.
  sec: 2897
  time: '48:17'
  who: Alexey
- line: Yeah, yeah, that's also, I think, a bad decision. If any vendors are listening,
    I think every product should be as modular as possible.
  sec: 2903
  time: '48:23'
  who: Nemanja
- line: And that you can just take that part, you know. If you have like a really
    good model registry, you should let people use just your model registry.
  sec: 2909
  time: '48:29'
  who: Nemanja
- line: Or just very good observability, just let people use that one and don't force
    them to buy everything.
  sec: 2916
  time: '48:36'
  who: Nemanja
- line: Maybe Databricks doesn’t really care about MLflow that much. They care more
    about selling because this is where they make money.
  sec: 2921
  time: '48:41'
  who: Alexey
- line: And people eventually just go with Weights & Biases or something like that
    for their registry or whatever.
  sec: 2927
  time: '48:47'
  who: Alexey
- header: 'Skill Investment: Foundational Tools (Linux, Python, Bash) vs New Tech'
- line: 'Like, this question actually has three questions. So, the second one is:
    what''s your advice on investing time in new or old tools?'
  sec: 2940
  time: '49:00'
  who: Alexey
- line: 'I guess the question is like: how do you, um, well, balance between old and
    new tools?'
  sec: 2945
  time: '49:05'
  who: Alexey
- line: Yeah, well, I would say the old tools are the ones that have survived everything—the
    every apocalypse.
  sec: 2950
  time: '49:10'
  who: Nemanja
- line: You should definitely always learn about them. I would say Linux, you should
    know Linux, Python—these things are foundational.
  sec: 2955
  time: '49:15'
  who: Nemanja
- line: Bash scripting, if you know these things. A bit of networking, a bit of Ansible
    or some of these tools are very, very useful.
  sec: 2961
  time: '49:21'
  who: Nemanja
- line: A bit of frontend development, just to know how HTML, CSS, and JavaScript
    work together to make a very simple application.
  sec: 2966
  time: '49:26'
  who: Nemanja
- line: All these things give you a lot of depth.
  sec: 2971
  time: '49:31'
  who: Nemanja
- line: Maybe you shouldn't go with Java 6, right?
  sec: 2976
  time: '49:36'
  who: Alexey
- line: I also don't think that. There are people who are still—there are young people
    learning mainframe development, you know.
  sec: 2983
  time: '49:43'
  who: Nemanja
- line: And you still have a lot of mainframe code. So, it's like a gamble. What's
    your risk appetite?
  sec: 2988
  time: '49:48'
  who: Nemanja
- line: Do you want to target a certain niche? Yeah, you can learn probably HLL or
    Perl and find a job with it.
  sec: 2994
  time: '49:54'
  who: Nemanja
- line: And there will not be a big pool of candidates for that. But then, you have
    to be ready to be hungry for a couple of months potentially while waiting for
    the right job.
  sec: 3000
  time: '50:00'
  who: Nemanja
- line: But if you're still coding and you're hungry, it's worth it, right?
  sec: 3060
  time: '51:00'
  who: Alexey
- line: But, if you want to play it safe, it's very simple. You open up job postings,
    make a little scraping script, download a lot of job postings, and see what the
    repeated keywords are.
  sec: 3068
  time: '51:08'
  who: Nemanja
- line: And you learn those. That’s basically what I did. That’s how I got into Python.
  sec: 3075
  time: '51:15'
  who: Nemanja
- header: 'Market Signals for Learning: Job Postings, Airflow, and Targeted Skills'
- line: Yeah, and if you do that and see that all companies use Airflow, and that’s
    all they want...
  sec: 3087
  time: '51:27'
  who: Alexey
- line: But Airflow is okay—it works, but not the best user experience. There are
    so many other orchestrators.
  sec: 3092
  time: '51:32'
  who: Alexey
- line: Even though 70% of companies still stick to Airflow, I understand why most
    banks still stick to Java, right?
  sec: 3098
  time: '51:38'
  who: Alexey
- line: 'Even though there are other languages. So, in this case, I do the scraping.
    I see these are the tools: Java, Airflow. How do I try to include new things here
    that not all use?'
  sec: 3105
  time: '51:45'
  who: Alexey
- line: I would say, from time to time, you need to tick some boxes. That’s what I
    did with Azure.
  sec: 3129
  time: '52:09'
  who: Nemanja
- line: Although I’m not currently working on Azure, I got feedback from recruiters
    that in Belgium, a lot of companies are using Azure.
  sec: 3135
  time: '52:15'
  who: Nemanja
- line: So, it’s very good to have a certain certification. So, I thought, okay, I’ll
    get a certification in Azure.
  sec: 3143
  time: '52:23'
  who: Nemanja
- line: I would say, do at least the bare minimum to understand a tool. You don’t
    have to become an expert in Airflow.
  sec: 3149
  time: '52:29'
  who: Nemanja
- line: How much time does it take to know something about it? A couple of days of
    playing with it.
  sec: 3155
  time: '52:35'
  who: Nemanja
- line: Then you can say, “I know something.” You can do a course and check the box.
  sec: 3160
  time: '52:40'
  who: Nemanja
- line: For example, with PySpark, four out of five interviews I had asked me about
    PySpark.
  sec: 3180
  time: '53:00'
  who: Nemanja
- line: They even had Spark clusters—though not always. Two out of five times, they
    had Spark clusters.
  sec: 3186
  time: '53:06'
  who: Nemanja
- line: But I never spent more than 1% of my time doing anything with Spark.
  sec: 3192
  time: '53:12'
  who: Nemanja
- line: But it’s like, “Do you have the box?” You said yes, and it’s not important,
    but it’s still part of the process.
  sec: 3199
  time: '53:19'
  who: Nemanja
- header: 'Data Engineering Reliability: Quality, Lineage, and LLM Unpredictability'
- line: I think it’s similar with people in AI. Data engineering is much older than
    MLOps engineering, and still, you hear many senior data engineers saying, "Hey,
    we’re still facing the same issues with data quality, lineage, and so on." So
    yeah, we’re not a fad anymore; we’re not the popular kids. But there’s still work
    to do.
  sec: 3343
  time: '55:43'
  who: Nemanja
- line: When I transitioned into machine learning engineering—originally, I was a
    data scientist—my goal was to build tools for the data scientist I used to be.
    I wanted to create something that would make my former self’s life easier. But
    even today, I haven’t seen companies make that experience seamless.
  sec: 3350
  time: '55:50'
  who: Nemanja
- line: There’s still so much left to do. With LLMs, the challenges are even more
    complicated. For example, you can hijack many chatbots to write code or do things
    they weren’t intended for. You might start on an e-commerce site and suddenly
    manipulate it into doing something else if you’re clever enough.
  sec: 3363
  time: '56:03'
  who: Nemanja
- line: And to be honest, the fact that I can’t fully rely on LLMs for validation
    makes me hesitant to use them at all. It feels too unpredictable. As an engineer,
    I want systems to be predictable, work 100% of the time, and be repeatable unless
    someone pulls the plug on a server. Having to wonder whether an LLM might hallucinate
    and return YAML instead of JSON? Call me back when that’s sorted out.
  sec: 3389
  time: '56:29'
  who: Nemanja
- line: That’s interesting because machine learning, in general, isn’t deterministic
    either. But at least we’ve learned to make it reliable, right? As ML engineers,
    we’re still figuring that out with LLMs.
  sec: 3402
  time: '56:42'
  who: Alexey
- line: Yeah, exactly. At least with classical machine learning, the output is structured
    in a predictable way, and I can control it. But with LLMs, sometimes it feels
    like you’re just begging—like, "Please, just give me a valid response. My career
    depends on it!" There’s even a meme about that.
  sec: 3412
  time: '56:52'
  who: Nemanja
- header: 'On‑Premise vs Cloud: Privacy, Cost Efficiency, and Migration Strategy'
- line: 'Right. So maybe let’s take one last question. You mentioned you have experience
    with on-premise systems. Most corporations you’ve worked with have preferred on-premise
    over cloud solutions. Luka is asking: Do you think on-premise will be the future
    for companies that care about data privacy? Especially in fields like finance
    or healthcare, where data privacy is critical.'
  sec: 3429
  time: '57:09'
  who: Alexey
- line: Yes, absolutely. That’s one of the main reasons companies are hesitant to
    fully embrace the cloud. In the financial industry, for example, most companies
    are still on-premise but are gradually moving to the cloud. However, they’re very
    cautious about what they migrate.
  sec: 3449
  time: '57:29'
  who: Nemanja
- line: Technically, these migrations could be done in a few months, but they often
    take years because of necessary discussions around privacy, encryption, and security
    risks like man-in-the-middle attacks.
  sec: 3472
  time: '57:52'
  who: Nemanja
- line: That said, there’s been a trend in recent years of companies moving back to
    on-premise. If you have a skilled team of engineers, you can save millions. For
    instance, the creator of Ruby on Rails, DHH, has written about how his company
    moved back to on-premise and drastically reduced costs.
  sec: 3484
  time: '58:04'
  who: Nemanja
- line: Right. AWS Lambda, for example, is great when you’re just starting out and
    don’t have a predictable workload. But once your workload stabilizes, it makes
    sense to switch to dedicated machines that are always running. It’s the same with
    cloud versus on-premise. At some point, you realize it’s cheaper in the long run
    to manage it yourself.
  sec: 3524
  time: '58:44'
  who: Alexey
- line: Exactly. But to do that, you need the right expertise. A data scientist using
    a low-code platform probably won’t have the skills to manage an on-premise setup.
  sec: 3543
  time: '59:03'
  who: Nemanja
- line: Alright, one quick question to wrap up. We talked about Spark earlier, and
    you mentioned you didn’t have to use it extensively, but it’s often a key topic
    in interviews. Have you used Dask? Do you think it’s a good alternative for distributed
    training?
  sec: 3569
  time: '59:29'
  who: Alexey
- line: I’ve experimented with Dask, but only locally. Once, I had some parallel processing
    to do and tried chunking a big DataFrame with Dask. But for some reason, it ended
    up being slower than just using Pandas.
  sec: 3587
  time: '59:47'
  who: Nemanja
- line: That might have been due to how I used it. Performance depends on what you’re
    doing—whether you’re aggregating, merging, or something else. For aggregations,
    Dask might be faster. But for smaller operations like merging, performance can
    tank.
  sec: 3598
  time: '59:58'
  who: Nemanja
- line: I’ve written about this before, comparing tools like Spark and Ray. With distributed
    systems, if you’re just doing a group-by and aggregate, it’s fine. But when you
    start merging small tables across clusters, it can become a disaster.
  sec: 3604
  time: '1:00:04'
  who: Nemanja
- header: 'Distributed Compute Alternatives: Dask, Spark, and Performance Trade‑offs'
- line: Dask is a mature tool, and I know it works in a distributed manner like Spark.
    However, I haven’t seen it widely used in the industry. Companies usually default
    to Spark for distributed processing. My limited success with Dask doesn’t mean
    it’s bad—just that I didn’t know how to use it properly.
  sec: 3609
  time: '1:00:09'
  who: Nemanja
- line: That aligns with my experience. About five years ago, Dask couldn’t handle
    group-by operations well, but I think it’s improved since then.
  sec: 3668
  time: '1:01:08'
  who: Alexey
- header: Closing Remarks and Next Steps
- line: Anyway, thanks so much for your time. This was an amazing discussion. It’s
    always a pleasure to have you as a guest. Maybe we can make this a recurring thing?
  sec: 3701
  time: '1:01:41'
  who: Alexey
- line: I’d love that. It’s always great chatting with you.
  sec: 3714
  time: '1:01:54'
  who: Nemanja
- line: Thanks again, and thanks to everyone who joined us. I hope you enjoyed it.
    See you next time!
  sec: 3720
  time: '1:02:00'
  who: Alexey
- line: Bye, everyone!
  sec: 3726
  time: '1:02:06'
  who: Nemanja
description: 'Learn Lean MLOps strategies for startups: build a SaaS-first MVP stack,
  avoid vendor lock-in, and manage technical debt for faster, portable ML launches.'
intro: How can an early-stage startup ship ML features fast without getting locked
  into cloud vendors or drowning in technical debt? In this episode, Nemanja Radojkovic—an
  electrical engineer turned data scientist and MLOps engineer, DataCamp instructor,
  and long-time practitioner—walks through pragmatic, lean MLOps strategies for startups.
  <br><br> We cover shoestring tactics for rapid prototyping, a SaaS‑first MVP stack
  and its trade‑offs, cloud credits versus migration friction, and how to avoid vendor
  lock‑in with managed services like Vertex AI or SageMaker. Nemanja unpacks priorities
  for an MVP stack, low‑code speed versus future flexibility, minimal stacks (Python,
  CI/CD orchestration, Dagster), and observability options (Logfire, Prometheus/Grafana,
  Streamlit). The conversation also addresses technical debt management, data engineering
  reliability, on‑premise vs cloud decisions, and distributed compute choices (Dask,
  Spark). <br><br> Listen to learn concrete frameworks for choosing tools, balancing
  portability and managed services, and practical steps to manage tech debt while
  moving quickly. This episode is for startup engineers and founders who need actionable
  guidance on lean MLOps, SaaS‑first approaches, vendor lock‑in avoidance, and building
  a resilient MVP stack.
dateadded: '2025-03-15'
duration: PT01H01M06S
quotableClips:
- name: Episode Introduction & Topic Overview
  startOffset: 0
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=0
  endOffset: 135
- name: 'Career Journey: Academia → Consulting → Finance Machine Learning Engineering'
  startOffset: 135
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=135
  endOffset: 363
- name: 'Startup Pace: Agility, Speed, and Managerial Insights'
  startOffset: 363
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=363
  endOffset: 474
- name: 'Lean MLOps: Shoestring Strategies for Early-Stage Companies'
  startOffset: 474
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=474
  endOffset: 714
- name: 'SaaS-First Approach: Vendor Solutions for Small Teams'
  startOffset: 714
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=714
  endOffset: 774
- name: 'Cloud Trade-offs: Startup Credits, Migration Friction, and Lock‑in'
  startOffset: 774
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=774
  endOffset: 906
- name: 'Cloud Complexity: Infrastructure as Code and Operational Overhead'
  startOffset: 906
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=906
  endOffset: 1058
- name: 'MVP Stack: Prioritizing Tools for Rapid Prototyping and Launch'
  startOffset: 1058
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1058
  endOffset: 1159
- name: 'Portability vs Managed Services: Avoiding Vendor Lock‑In (Vertex AI, SageMaker)'
  startOffset: 1159
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1159
  endOffset: 1295
- name: 'Low‑Code Trade-offs: Speed vs Future Flexibility'
  startOffset: 1295
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1295
  endOffset: 1342
- name: 'Career Decision Framework: Choosing Startups or Corporations'
  startOffset: 1342
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1342
  endOffset: 1650
- name: 'End‑to‑End Ownership: Multidisciplinary Work in Startups'
  startOffset: 1650
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1650
  endOffset: 1777
- name: 'Corporate Processes: "Agile" vs Bureaucratic Planning Cycles'
  startOffset: 1777
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1777
  endOffset: 1997
- name: 'Platform & Frameworks: Automating Developer Workflows'
  startOffset: 1997
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=1997
  endOffset: 2072
- name: 'Team Scale Advantages: Redundancy, Support, and Internal Mobility'
  startOffset: 2072
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2072
  endOffset: 2148
- name: 'Startup Intensity: Learning Curve, Burnout Risk, and Rewards'
  startOffset: 2148
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2148
  endOffset: 2274
- name: 'AI‑Assisted Coding: Productivity Gains and Technical Debt Risks'
  startOffset: 2274
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2274
  endOffset: 2401
- name: 'Technical Debt Management: Notes, Awareness, and Security Implications'
  startOffset: 2401
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2401
  endOffset: 2592
- name: 'Early‑Career Advice: Mentorship, Pairing, and Role Selection'
  startOffset: 2592
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2592
  endOffset: 2650
- name: 'Minimal MLOps Stack: Python, CI/CD Orchestration, and Dagster'
  startOffset: 2650
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2650
  endOffset: 2755
- name: 'Observability Choices: Logfire, Prometheus/Grafana, and Streamlit'
  startOffset: 2755
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2755
  endOffset: 2891
- name: 'Product Modularity: Desire for Standalone Model Registries & Observability'
  startOffset: 2891
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2891
  endOffset: 2940
- name: 'Skill Investment: Foundational Tools (Linux, Python, Bash) vs New Tech'
  startOffset: 2940
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=2940
  endOffset: 3087
- name: 'Market Signals for Learning: Job Postings, Airflow, and Targeted Skills'
  startOffset: 3087
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=3087
  endOffset: 3343
- name: 'Data Engineering Reliability: Quality, Lineage, and LLM Unpredictability'
  startOffset: 3343
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=3343
  endOffset: 3429
- name: 'On‑Premise vs Cloud: Privacy, Cost Efficiency, and Migration Strategy'
  startOffset: 3429
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=3429
  endOffset: 3609
- name: 'Distributed Compute Alternatives: Dask, Spark, and Performance Trade‑offs'
  startOffset: 3609
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=3609
  endOffset: 3701
- name: Closing Remarks and Next Steps
  startOffset: 3701
  url: https://www.youtube.com/watch?v=DX9c__a4jzg&t=3701
  endOffset: 3666
---

Links:

* [LinkedIn](https://www.linkedin.com/in/radojkovic/){:target="_blank"}
* [Github](https://github.com/baskervilski){:target="_blank"}