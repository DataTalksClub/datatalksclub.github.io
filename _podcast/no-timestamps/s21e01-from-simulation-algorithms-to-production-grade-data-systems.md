---
episode: 1
guests:
- orellgarten
ids:
  anchor: datatalksclub/episodes/From-Simulations-to-Freelance-Data-Engineering-Orells-Journey-Out-of-Academia-and-Into-Consulting---Orell-Garten-e369a6b
  youtube: pkcpH5N-GP8
image: images/podcast/s21e01-from-simulation-algorithms-to-production-grade-data-systems.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/From-Simulations-to-Freelance-Data-Engineering-Orells-Journey-Out-of-Academia-and-Into-Consulting---Orell-Garten-e369a6b
  apple: https://podcasts.apple.com/us/podcast/from-simulations-to-freelance-data-engineering-orells/id1541710331?i=1000720245457
  spotify: https://open.spotify.com/episode/5HCSIO0mO8Pr5Yv9puZ72R
  youtube: https://www.youtube.com/watch?v=pkcpH5N-GP8
season: 21
short: From Simulation Algorithms to Production-Grade Data Systems
title: 'Synthetic Medical Imaging Data for AI: Startup Data Engineering, MVPs & Freelance
  Transition'
transcript:
- header: Orell’s career and move to freelancing
- line: This week, we'll talk about many different things. We will discuss our guest’s
    career, simulation algorithms, and production-grade data systems.
  sec: 0
  time: 0:00
  who: Alexey
- line: We have a special guest today, Orell. Orell graduated in 2018 with a degree
    in electrical engineering, focusing on simulation algorithms. Then he pursued
    a PhD.
  sec: 0
  time: 0:00
  who: Alexey
- line: When COVID arrived, he decided to leave academia and look for new challenges.
    After that, he joined a startup program to explore how to turn scientific research
    into real products. He learned many things. Today, he is a freelancer in software
    and data engineering. We will talk about how he uses his deep experience in simulation
    to build custom data infrastructure.
  sec: 139
  time: '2:19'
  who: Alexey
- line: Before we start, I want to thank Valeria, who prepared the questions for today’s
    interview. Normally Johanna does that, but she has been busy with summer school.
    So thank you, Valeria, for your help. Welcome, Orell! Let’s start the interview.
  sec: 165
  time: '2:45'
  who: Alexey
- line: Hi Alexey, thanks for having me. I'm excited to be here.
  sec: 190
  time: '3:10'
  who: Orell
- line: My pleasure. Before we dive into building custom data infrastructures, let’s
    talk about your career. I briefly outlined it, but maybe you can share more details
    about your career journey so far.
  sec: 196
  time: '3:16'
  who: Alexey
- line: Sure. In my final years of high school, I was unsure what to pursue. I knew
    I wanted to do something technical like most of us did.
  sec: 214
  time: '3:34'
  who: Orell
- line: Is it very hard in Germany? When do you graduate, at 17 or later?
  sec: 226
  time: '3:46'
  who: Alexey
- line: I graduated at 18, I was actually 19 at the time, but still very young. I
    really had no idea what I wanted to do.
  sec: 233
  time: '3:53'
  who: Orell
- line: I’m originally from Russia, and there we graduate at around 17. When you’re
    17, you have no idea what you’re going to have for breakfast, let alone your future
    career. It’s difficult to decide.
  sec: 238
  time: '3:58'
  who: Alexey
- line: Exactly. You also don’t know what the daily work looks like. You might think
    about engineering or computer science but have no idea what the job entails. I
    coded a bit in my spare time and decided to study electrical engineering because
    people said, “If you want to code, go to electrical engineering. For theoretical
    computer science, go to computer science.” I also dabbled in embedded systems
    with microcontrollers back then.
  sec: 249
  time: '4:09'
  who: Orell
- line: During my studies, I realized that coding and building systems is what I enjoy.
    Then I focused on simulation engineering, developing custom simulation algorithms
    for problems like RF wave propagation.
  sec: 282
  time: '4:42'
  who: Orell
- line: I remember we studied simulations too, like simulating a supermarket to optimize
    customer flow and queuing strategies. For example, deciding whether to have a
    queue per cashier or a single queue. The optimal strategy is usually one queue.
    Was that similar to what you studied?
  sec: 309
  time: '5:09'
  who: Alexey
- line: It’s a bit different. Simulation can mean many things. What I worked on was
    wave propagation audio waves or electromagnetic waves used in radar or mobile
    communications.
  sec: 358
  time: '5:58'
  who: Orell
- line: We used physical equations from physics theory to simulate how waves behave
    in real-life scenarios. This is quite a hard problem because it takes a very long
    time, especially for large scenarios like wave propagation in a city where waves
    bounce off buildings and interact with the environment. It was challenging because
    it involved physics, math, and coding. You have to optimize your code, data formats,
    and strategies, which made it quite interesting.
  sec: 376
  time: '6:16'
  who: Orell
- line: Interesting. But you are not doing this work anymore, right?
  sec: 437
  time: '7:17'
  who: Alexey
- line: No, after my studies I started a PhD but quit when I realized it wasn’t what
    I wanted to do, even within electrical engineering and simulation. Then COVID
    hit, and a friend and I tried to start a startup to monetize simulations and related
    systems.
  sec: 444
  time: '7:24'
  who: Orell
- line: We didn’t succeed, but we learned a lot about data engineering, economics,
    startups, talking to customers, and understanding their needs. When we stopped
    working on the startup, I decided I didn’t want to do a 9-to-5 job. I wanted to
    work for myself and experiment with different opportunities. So freelancing came
    naturally.
  sec: 480
  time: '8:00'
  who: Orell
- line: Can you tell us more about the startup? What exactly were you trying to build?
  sec: 524
  time: '8:44'
  who: Alexey
- header: Startup experience and data engineering lessons
- line: We had a different problem. We focused on medical imaging like MRI and X-rays.
    We wanted to develop AI algorithms to analyze the images because it’s repetitive
    and boring work.
  sec: 544
  time: '9:04'
  who: Orell
- line: We simulated the physics of imaging machines and processes to create synthetic
    data for AI training. That’s what we tried to monetize.
  sec: 544
  time: '9:04'
  who: Orell
- line: However, it didn’t work out for several reasons. One main issue was we started
    with technology, not a problem. Later, we realized it wasn’t seen as a problem
    at the time, especially before chat GPT and generative AI became popular.
  sec: 582
  time: '9:42'
  who: Orell
- line: Medical companies often work only when hospitals specifically request certain
    MRI functionalities. There is little in-house research, so monetizing the technology
    was very difficult.
  sec: 606
  time: '10:06'
  who: Orell
- line: I had a funny experience with MRI. I had back problems, and doctors found
    something concerning on the MRI, but I did not feel constant pain. They said I
    should be in pain all the time according to the scan, but I wasn’t.
  sec: 632
  time: '10:32'
  who: Alexey
- line: Sometimes the body works in surprising ways.
  sec: 661
  time: '11:01'
  who: Orell
- line: Maybe the body compensates. Perhaps it was an old injury that showed on the
    MRI but no longer caused pain because the body adapted.
  sec: 667
  time: '11:07'
  who: Alexey
- line: That could be it, but I’m not a medical professional.
  sec: 681
  time: '11:21'
  who: Orell
- line: You learned a few things about MRI though?
  sec: 686
  time: '11:26'
  who: Alexey
- line: Yes, about MRI and also the medical market, especially in Germany. The medical
    market is capped financially; the money available depends on what people pay into
    the system.
  sec: 692
  time: '11:32'
  who: Orell
- line: If you make money, you take it from someone else in the market, so it’s not
    a win-win situation. Someone has to lose for you to make money, which is not ideal
    for startups.
  sec: 704
  time: '11:44'
  who: Orell
- line: In the ideal world, there is a finite amount of money, assuming governments
    are not printing money. So you are always competing for funds. If someone spends
    on your product, they can’t spend it on another.
  sec: 730
  time: '12:10'
  who: Alexey
- line: That is true to some extent, but I believe governments do print money. Also,
    money can move around. Spending on one thing can free up spending elsewhere, so
    some win-win possibilities exist.
  sec: 750
  time: '12:30'
  who: Orell
- line: Though someone often loses, it helps if your competitors don’t feel threatened.
    Then they might be more willing to help you.
  sec: 776
  time: '12:56'
  who: Orell
- line: What kind of things did you build for the startup? You said you learned about
    data engineering, economics, and talking to customers. What did you actually do
    regarding data engineering? Did you need a platform?
  sec: 800
  time: '13:20'
  who: Alexey
- line: Yes, but we started small. In startups, you don’t know what people need at
    first. Many bigger companies are also unsure.
  sec: 825
  time: '13:45'
  who: Orell
- line: It’s important to do the minimum work needed to make the data work at the
    moment.
  sec: 825
  time: '13:45'
  who: Orell
- line: For example, if you have no customers, it doesn’t matter if there is a data
    pipeline since it is not used.
  sec: 825
  time: '13:45'
  who: Orell
- line: Sometimes doing things manually, like triggering pipelines, gives you more
    control early on.
  sec: 861
  time: '14:21'
  who: Orell
- line: We had simulation algorithms, which could be considered AI or machine learning
    kernels, and data infrastructure to move data to simulations running on high-performance
    clusters, then retrieve results.
  sec: 861
  time: '14:21'
  who: Orell
- line: It’s crucial to manage data properly to avoid mixing client data, especially
    when clients might be competitors.
  sec: 895
  time: '14:55'
  who: Orell
- line: That is data management, not magic. Keeping it simple is the best approach
    in startups.
  sec: 895
  time: '14:55'
  who: Orell
- line: Was this something you had to learn, or did you already know it from your
    PhD?
  sec: 926
  time: '15:26'
  who: Alexey
- line: Orell
  sec: 926
  time: '15:26'
  who: Alexey
- line: That’s one reason I left academia; nobody cared about the implementation or
    what the work could actually do. It was mostly about formatting the equations
    correctly.
  sec: 934
  time: '15:34'
  who: We had to learn it. In the PhD, it was all about science and algorithms, not
    implementation. It was about trade-offs in equations, not practical code.
- header: Academia vs. startups and starting freelancing
- line: I assume the iteration cycles you have in academia differ a lot from startups.
  sec: 965
  time: '16:05'
  who: Alexey
- line: In startups, you test ideas quickly, build MVPs fast to satisfy customer needs,
    whereas in academia you might have a five-year grant to develop a specific thing.
  sec: 965
  time: '16:05'
  who: Alexey
- line: That’s true. Academia has longer project timelines. Usually, the project has
    a specific goal funded by a grant.
  sec: 999
  time: '16:39'
  who: Orell
- line: However, the overall process isn’t that different because in startups you
    also test hypotheses, but about markets and customer problems.
  sec: 1019
  time: '16:59'
  who: Orell
- line: In academia, the value is in publishing papers. In startups, it’s selling
    products or services. Very similar processes but with different definitions of
    success.
  sec: 1019
  time: '16:59'
  who: Orell
- line: Can you tell us more about the scientific approach? How do you formulate hypotheses,
    and how do you use that as a data engineer?
  sec: 1070
  time: '17:50'
  who: Alexey
- line: In startups, you ask specific, narrow questions.
  sec: 1075
  time: '17:55'
  who: Orell
- line: For example, “Is this a problem for companies with fewer than 10 employees?”
    You must specify the problem clearly.Then you talk to as many companies as needed
    to validate or invalidate your hypothesis.
  sec: 1075
  time: '17:55'
  who: Orell
- line: Data engineering is more complicated because it is behind the scenes. You
    only notice it when something breaks. There are no dashboards or visible results.
    It’s a lot of plumbing to make data flow.
  sec: 1120
  time: '18:40'
  who: Orell
- line: You have to talk to many people to understand their problems, but it is harder
    to find out what companies truly need because each is very different.
  sec: 1120
  time: '18:40'
  who: Orell
- line: That’s very interesting. I am noting what companies need because I want to
    come back to that later. Before that, I want to talk about your transition from
    startup builder to freelancing data engineer. You enjoyed data engineering in
    the startup and wanted to focus on it independently.
  sec: 1174
  time: '19:34'
  who: Alexey
- line: Can you tell us how that happened and how you started freelancing?
  sec: 1174
  time: '19:34'
  who: Alexey
- line: It happened naturally. Near the end of our startup journey, I received a LinkedIn
    request from someone wanting to pay me for consulting, which was very exciting.
  sec: 1220
  time: '20:20'
  who: Orell
- line: I just wonder, you did a startup as a co-founder. What was your role were
    you the CTO?
  sec: 1239
  time: '20:39'
  who: Alexey
- line: Yes, mostly like CTO. At that stage, roles weren’t well-defined everyone did
    everything.
  sec: 1247
  time: '20:47'
  who: Orell
- line: How did your experience as a co-founder translate to the customer request
    you received? Did you highlight your data platform skills? What exactly did the
    customer ask for? For others hoping to get LinkedIn leads, how did you make it
    happen?
  sec: 1259
  time: '20:59'
  who: Alexey
- line: It happened through a contact from the startup days. We’d discussed their
    problems earlier, and later they came back and asked if I could help. It was a
    small thing, maybe a week of work, but it was a big deal to have someone pay for
    my skills. Even after a failed startup, my skills had value. That helped me see
    freelancing could work. From there, I focused on doing the best work, networking,
    and sharing on LinkedIn. Building a network made it easier to reconnect and get
    referrals, especially once COVID eased. Of course, you need to deliver quality
    work, but that’s usually not the main problem.
  sec: 1284
  time: '21:24'
  who: Orell
- line: You mentioned doing customer interviews and then closing your business, but
    this client still had a problem and asked you to help. What was the problem, if
    you can share?
  sec: 1379
  time: '22:59'
  who: Alexey
- line: It was a prototype for a data engineering IoT project. That’s about all I
    can share.
  sec: 1409
  time: '23:29'
  who: Orell
- line: How did you have the needed skills? Was it from your startup?
  sec: 1422
  time: '23:42'
  who: Alexey
- line: Yes, it was close. After the simulations didn’t work out, we tried other things.
    My electrical engineering background showed I could handle embedded systems. We
    tried different cloud platforms. I learned a lot that year before I got the request.
    But the biggest thing is system thinking, not just technology choices. AWS, GCP,
    or Azure usually doesn’t matter as much as design and making the right trade-offs.
  sec: 1428
  time: '23:48'
  who: Orell
- line: Did that project actually take just one week?
  sec: 1495
  time: '24:55'
  who: Alexey
- line: Yes, about a week. We delivered the prototype and then the client decided
    where to go next. It fizzled out, maybe the solution wasn’t what they needed,
    but that’s not really my story to share.
  sec: 1502
  time: '25:02'
  who: Orell
- line: So for you the main thing was seeing that your skills were in demand and people
    would pay for them. What happened next?
  sec: 1520
  time: '25:20'
  who: Alexey
- header: Early freelancing challenges and networking
- line: 'Then came a tough time: a three or four month drought with very little project
    work. I barely covered my bills. The market in Germany soured: projects disappeared
    or got cancelled, budgets were frozen. That just happens sometimes.'
  sec: 1533
  time: '25:33'
  who: Orell
- line: Many companies went bankrupt during this time.
  sec: 1586
  time: '26:26'
  who: Alexey
- line: Yes, that too. I also didn’t set a clear deadline for myself like, give it
    a year to decide if freelancing was viable. I just kept going, which in hindsight
    was risky. You can’t do it until the money runs out; you need a buffer.
  sec: 1593
  time: '26:33'
  who: Orell
- line: If you run out of money, you’d be living under a bridge. Germany has a good
    safety net, but not everywhere does.
  sec: 1618
  time: '26:58'
  who: Alexey
- line: That’s why you should start lean and keep fixed costs down, so your savings
    last. For any startup, you want at least six months of operating expenses in the
    bank.
  sec: 1632
  time: '27:12'
  who: Orell
- line: What expenses do freelancers have, besides the bank account?
  sec: 1657
  time: '27:37'
  who: Alexey
- line: Tax accountant, hardware, software subscriptions, occasional travel for customer
    meetings, perhaps platform accounts. Plus, you often have to wait 30–45 days for
    payment after invoicing, so even in the best-case scenario, you go weeks without
    getting paid. You still need to pay rent, food, and living costs at that time.
  sec: 1663
  time: '27:43'
  who: Orell
- line: Is Leipzig getting more expensive now?
  sec: 1734
  time: '28:54'
  who: Alexey
- line: Yes, though it’s still cheaper than Berlin or Munich. But prices are up, there’s
    little housing and lots of demand, a typical problem in Germany.
  sec: 1740
  time: '29:00'
  who: Orell
- line: How much runway do I need before freelancing six months?
  sec: 1784
  time: '29:44'
  who: Alexey
- line: Six months is a good baseline, longer is better, but six months to a year
    is reasonable. Sometimes you get lucky and are fully booked immediately, but that’s
    rare unless you have a giant network.
  sec: 1790
  time: '29:50'
  who: Orell
- line: How did you solve this for yourself?
  sec: 1839
  time: '30:39'
  who: Alexey
- line: Networking. I mentioned that I’m self-employed whenever it fits in business
    and tech contexts. If people don’t know you’re available, they can’t reach out.
  sec: 1850
  time: '30:50'
  who: Orell
- line: After the first project, months went by before you found more work. You said
    networking helped long term. What else worked in the beginning?
  sec: 1941
  time: '32:21'
  who: Alexey
- line: At first, I applied for freelance projects via recruiters. It's common in
    Germany, less so elsewhere. That’s how I got my biggest client last year. Once
    you land work, more follows, and momentum builds. If you have nothing, it gets
    harder and rates can be pressured down.
  sec: 1967
  time: '32:47'
  who: Orell
- header: Freelance data engineering and messy industrial data
- line: What do you actually do as a freelancer? Data engineering is broad do you
    specialize?
  sec: 2062
  time: '34:22'
  who: Alexey
- line: I focus on the software side of data engineering, not dashboarding or PowerBI.
    I build data pipelines, preparing and managing data so it’s ready for analytics
    or warehousing. Most of my clients are industrial with many types of machines
    and formats, even different variants from the same manufacturer. I do a lot of
    custom integration and transformation.
  sec: 2075
  time: '34:35'
  who: Orell
- line: Do clients know what they want, like a specific dashboard, and you help make
    that data available, or do you help them discover what they need?
  sec: 2149
  time: '35:49'
  who: Alexey
- line: It depends. Some clients come with specific ideas and I help implement them,
    sometimes consulting on what else makes sense. Other clients only know they have
    data and want analysis, so we begin with exploration. It often isn’t clean or
    standard. Sometimes a CSV is enough for a basic first step, showing what’s possible
    and surfacing problems. The key is always understanding their business goals and
    providing real value.
  sec: 2184
  time: '36:24'
  who: Orell
- line: On your LinkedIn, you say you help clients start small, focus on immediate
    value, and then scale. Can you walk us through an example, even a hypothetical
    one?
  sec: 2294
  time: '38:14'
  who: Alexey
- line: 'The first thing I always do is look at the data: what’s in it and what does
    the schema look like? Usually, even providing documentation about the data brings
    immediate value for companies.'
  sec: 2340
  time: '39:00'
  who: Orell
- line: I imagine, based on what we've been talking about, you have some equipment
    sitting in a factory some industrial machine. The goal is to understand if the
    machine is performing correctly, but you have no idea what kind of sensors it
    has, what data it's sending, what the schema is, or if it's binary or JSON. I'm
    just making this up; I have no idea how these machines work. But that's what you
    need to figure out, right?
  sec: 2359
  time: '39:19'
  who: Alexey
- line: That would be the worst case if you have no idea about the data situation
    at all. Usually, you have some sense of what sensors are installed and what the
    values mean, but often the documentation doesn’t match the actual data. That’s
    the first challenge. You also want to know things like, "We get an error every
    12 hours on that machine—what's happening?" So you try to find patterns or problems
    you can identify. Before doing any automation, you have to understand what the
    data looks like, how different machines work together in the same manufacturing
    line, that kind of thing.
  sec: 2396
  time: '39:56'
  who: Orell
- line: A lot of machines now are intelligent or at least connected, so their data
    is usually available. Sometimes you need custom vendor-provided software to decode
    it, but often it’s just log files, terminal outputs, or JSON containing sensor
    values. There are different technologies REST APIs, MQTT, sometimes even Kafka
    so it’s all over the place. That makes it interesting, but also challenging, and
    requires quite a bit of infrastructure to integrate all these different data processes.
  sec: 2453
  time: '40:53'
  who: Orell
- line: But you probably don't start with the infrastructure part. You first figure
    out what kind of data there is, how to access it, how to get the data, and then
    you build the first MVP, right? You put the data into a CSV file and say, "Here's
    a dashboard I can build. Does this work for you?" Is this what you do?
  sec: 2514
  time: '41:54'
  who: Alexey
- line: Yeah, basically. It might sound really simple, but it works pretty well. You
    just pull files for one day, or depending on how big they are, for a set period
    onto your computer, and then analyze them locally. Then you can say, "Okay, on
    this day, in this hour, we see this problem or this insight." You start building
    scripts that transform the data and make sense of it. Once that's done, you move
    to a more automated approach, where you ingest the data automatically and process
    it on a schedule or with stream processing, depending on the needs.
  sec: 2536
  time: '42:16'
  who: Orell
- line: So this is when you start building the infrastructure part.
  sec: 2578
  time: '42:58'
  who: Alexey
- line: Yes, exactly. If you start investing in infrastructure before you know what
    you want to do, your infrastructure is probably not what you actually need and
    is likely overengineered. You end up supporting all possible use cases, but realistically,
    you only need a few.
  sec: 2578
  time: '42:58'
  who: Orell
- header: Staying practical, learning tools, and growth
- line: How do you keep yourself in check and avoid overengineering when it's not
    necessary?
  sec: 2607
  time: '43:27'
  who: Alexey
- line: Good question, it's a tough one. You have to keep reminding yourself to keep
    things simple. Also, regular meetings help. They don’t have to be daily or even
    weekly, but having a tight feedback loop with your clients keeps things simple.
    With weekly meetings, you can't implement overly complex solutions all at once.
    If you show or talk about what you did and the results every week, you’re forced
    to keep it simple and deliver each week. Then, when necessary, you can gradually
    increase complexity.
  sec: 2614
  time: '43:34'
  who: Orell
- line: Isn't that the idea behind Scrum with these demo days or whatever they're
    called where you're forced to focus on a demo, and to build a demo, you need a
    minimal working pipeline? Then you do the demo, adjust as needed, and iterate.
  sec: 2657
  time: '44:17'
  who: Alexey
- line: Yeah, that’s what Scrum or Agile would look like in an ideal world, but a
    lot of companies use the terminology without really following the practice it
    ends up as micromanagement. For me, it’s about working with clients to find the
    way that works best. No one is forcing me to be Agile or do Scrum; it’s about
    figuring out the best approach together. I can’t just disappear for 6 months and
    come back with the perfect solution, which might not even be needed. That would
    be expensive and bad for my reputation.
  sec: 2690
  time: '44:50'
  who: Orell
- line: I guess your startup experience helped make you more pragmatic and focused.
  sec: 2751
  time: '45:51'
  who: Alexey
- line: 'Yes, definitely. That was one thing I learned in the startup: be pragmatic,
    keep it simple, deliver quickly, and go from there.'
  sec: 2758
  time: '45:58'
  who: Orell
- line: If you work at a company, you always know when the next paycheck comes, so
    you’re more relaxed and might want to engineer the perfect solution. But at a
    startup you don’t have a year you have next month, and if you don’t do something,
    you’re out.
  sec: 2770
  time: '46:10'
  who: Alexey
- line: Yeah, you have to think like a businessperson, not just an engineer. As an
    engineer, you want to build all the cool things and new tech because it's fun
    and a learning experience, but it doesn’t always deliver value. Even as a full-time
    employee, you might have more time for experiments and demos and get paid for
    it but as a freelancer, you have to experiment and try new tech on your own time.
  sec: 2803
  time: '46:43'
  who: Orell
- line: How do you set aside time to grow as an engineer and play with new technologies?
  sec: 2852
  time: '47:32'
  who: Alexey
- line: I block time in my calendar Friday afternoon, the weekend, or whenever fits
    my life. You have to make time for this, otherwise it doesn’t happen. Even when
    you block time, sometimes other things are more important. Keeping up with developments
    by following people on LinkedIn, being part of communities, and listening to podcasts
    helps you stay current, even if you don’t know all the details. So when you encounter
    a problem where a new tech might help, you remember it and can decide if it’s
    worth exploring.
  sec: 2858
  time: '47:38'
  who: Orell
- line: So you need a broad overview of what’s possible in your domain.
  sec: 2928
  time: '48:48'
  who: Alexey
- line: Yes, it helps you make better decisions and know your options, even if you
    don’t know the details. You’ll often fall back on what you know best, and that’s
    fine.
  sec: 2934
  time: '48:54'
  who: Orell
- line: How do you structure this learning time, considering you also run a community
    and always have things to do?
  sec: 2962
  time: '49:22'
  who: Alexey
- header: Freelancing challenges and client acquisition
- line: If you hear about new tech like DuckDB which some say is super cool, lets
    you do everything locally, and can be faster than Spark how do you find time to
    try it and really learn, so you might use it one day?
  sec: 2999
  time: '49:59'
  who: Alexey
- line: DuckDB is awesome, by the way! What I do is start with the 'get started' tutorial
    there’s almost always one. It teaches you the basic ideas and the way to think
    about technology. The easier it is to try, the easier to get hands-on. With DuckDB,
    you only need a computer. No server needed, they even have example data. So getting
    started is very easy. Sometimes I struggle with what to build, but tutorials usually
    give ideas. Then if I see a problem that fits, I’ll try that technology. Sometimes,
    I solve problems I’ve solved before using the new tool, comparing approaches,
    benchmarking, code length, whatever. That’s a good way to learn, and it prevents
    you from being stuck thinking about what new thing to code.
  sec: 3033
  time: '50:33'
  who: Orell
- line: If you want to learn, how do you pick a project? It's tough sometimes the
    customer problem matches a new tech, and you can use it. But sometimes you might
    not use the best tool.
  sec: 3145
  time: '52:25'
  who: Alexey
- line: That’s always how it is. It's better to have something that works even if
    it's not perfect than to wait for the perfect solution that might not exist for
    years. You can always swap tools later, though it's not fun. If the tool works,
    it’s probably good enough, unless you’re in the top 5% for performance.
  sec: 3183
  time: '53:03'
  who: Orell
- line: We have questions. Even though you don’t work with AI/ML, have you come across
    LLMs used for data cleaning or ingestion?
  sec: 3222
  time: '53:42'
  who: Alexey
- line: I see the idea often, but the main problem with data cleaning is domain knowledge.
    For an industrial company, you need to deeply understand what the values mean
    data cleaning always changes the data, so it’s not raw anymore. You have to know
    what the data means for the business, and that’s tough for an LLM. I usually talk
    to clients for hours to really get it. Maybe an LLM could flag things that look
    out of place, but I don’t think it’s the best solution right now.
  sec: 3234
  time: '53:54'
  who: Orell
- line: What was the biggest challenge about going freelance?
  sec: 3341
  time: '55:41'
  who: Alexey
- line: Acquiring clients. If you solve that, freelancing can be flexible and rewarding
    but if you haven’t solved it, it’s painful. Most people already have the skills
    from full-time work, but client acquisition is a different skill set.
  sec: 3346
  time: '55:46'
  who: Orell
- line: Are you an introvert or an extrovert?
  sec: 3463
  time: '57:43'
  who: Alexey
- line: I’m an introvert. I can do networking but find it exhausting. After networking
    events, I need downtime. But you have to do it, or you won’t get clients.
  sec: 3467
  time: '57:47'
  who: Orell
- header: Tools, problem-solving, and manual work
- line: What is your daily tech stack or main skills?
  sec: 3509
  time: '58:29'
  who: Alexey
- line: My main tools are Python and C++ though Python is 90% of my work now. C++
    is mostly for industrial hardware or high-performance computing from my simulation
    days. Recently, I use DuckDB a lot for both prototyping and actual pipelines it's
    flexible and integrates well with Python. I use Linux, DBT, Docker depends on
    the client. Software engineering skills help, but my main focus is problem-solving,
    not the specific tech stack. The language is just a preference; the real skill
    is figuring out the problem and delivering a suitable solution.
  sec: 3517
  time: '58:37'
  who: Orell
- line: So the main skill in your working life is problem solving?
  sec: 3653
  time: '1:00:53'
  who: Alexey
- line: Yes. The tech part comes later. First, figure out the real problem, then decide
    the best or a good enough solution. Sometimes, manual work is fastest for the
    first iteration just filtering or classifying data by hand. This helps you learn
    about the data and its edge cases, which are hard to code for. That’s where experience
    and intuition are valuable, and maybe where LLMs could help in the future.
  sec: 3659
  time: '1:00:59'
  who: Orell
- line: For me, with a data science background, manual exploration is super useful.
    It might sound boring, but it's worth it for learning the data.
  sec: 3740
  time: '1:02:20'
  who: Alexey
- line: Absolutely. Thanks for having me. I hope my story motivates some people to
    try freelancing. I enjoyed the conversation.
  sec: 3763
  time: '1:02:43'
  who: Orell
- line: Thanks to Orell and everyone for joining. Don’t forget we have more events
    coming up. If you have guest suggestions, let me know! Enjoy the summer and see
    you next time.
  sec: 3811
  time: '1:03:31'
  who: Alexey
description: 'Learn synthetic medical imaging & data engineering: build MVPs, integrate
  simulation-HPC, optimize ETL, and shift to freelance with client-acquisition tactics.'
intro: 'How do you turn simulation research into usable synthetic medical imaging
  data for AI, build a minimal viable data pipeline, and pivot into freelance consulting?
  In this episode Orell Garten — an electrical engineer trained in simulation algorithms
  who left a PhD during COVID and explored productization through a government-funded
  startup program — walks through that journey. We cover his simulation work in RF
  and wave propagation, the startup pivot to synthetic medical imaging data for AI,
  and the go-to-market lesson of problem-first versus technology-first. <br><br> Listen
  for practical data engineering guidance: minimal viable data work, simulation–HPC
  integration, secure data management, and an MVP workflow built on manual extraction,
  CSVs, and local analysis. Orell also discusses scientific-method product discovery,
  preventing overengineering with weekly feedback, and tool choices (Python, C++,
  DBT, Docker, DuckDB). He explains launching a freelance practice via LinkedIn, prototype
  delivery for IoT data engineering, client acquisition, and managing runway and cashflow.
  If you’re building synthetic data pipelines, medical imaging datasets, or transitioning
  to freelance data engineering, this episode delivers concrete tactics, risks to
  plan for, and hands-on techniques you can apply immediately.'
---

Links:

* [LinkedIn](https://www.linkedin.com/in/ogarten/){:target="_blank"}
* [Github](https://github.com/orgarten){:target="_blank"}
* [Website](https://orellgarten.com){:target="_blank"}