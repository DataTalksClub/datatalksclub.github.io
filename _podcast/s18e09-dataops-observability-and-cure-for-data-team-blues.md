---
episode: 9
guests:
- christopherbergh
ids:
  anchor: atatalksclub/episodes/DataOps--Observability--and-The-Cure-for-Data-Team-Blues---Christopher-Bergh-e2n775f
  youtube: HzGpIxV8HtA
image: images/podcast/s18e09-dataops-observability-and-cure-for-data-team-blues.jpg
links:
  anchor: https://podcasters.spotify.com/pod/show/datatalksclub/episodes/DataOps--Observability--and-The-Cure-for-Data-Team-Blues---Christopher-Bergh-e2n775f
  apple: https://podcasts.apple.com/us/podcast/dataops-observability-and-the-cure-for-data-team/id1541710331?i=1000665429770
  spotify: https://open.spotify.com/episode/02VoOk5UkMcvfq7VkSOegb
  youtube: https://www.youtube.com/watch?v=HzGpIxV8HtA
season: 18
short: DataOps, Observability, and The Cure for Data Team Blues
title: DataOps, Observability, and The Cure for Data Team Blues
transcript:
- line: This week, we’re discussing DataOps again. Maybe it’s becoming a tradition
    to talk about DataOps once a year, though we missed last year. It’s been a while
    since we had Chris on the podcast. So, today we have a special guest, Christopher
    Bergh. Christopher is the Co-Founder, CEO, and Head Chef at DataKitchen, with
    over 25 years of experience—probably more now—in analytics and software engineering.
    He's a co-author of the "DataOps Cookbook" and the "DataOps Manifesto." It’s not
    the first time we've had him here. We interviewed him two years ago, also about
    DataOps. Today, we’ll catch up and see what’s changed in these two years. Welcome
    to the interview, Chris!
  sec: 132
  time: '2:12'
  who: Alexey
- header: DataOps and Christopher's background
- line: Thank you for having me. I'm happy to be here, discussing all things related
    to DataOps, why it matters, and what's changed. Excited to dive in.
  sec: 198
  time: '3:18'
  who: Christopher
- line: Great. So, the questions for today’s interview were prepared by Johanna Bayer.
    Thanks, Johanna, for your help. Before we dive into DataOps, could you give us
    a brief overview of your career journey? For those who haven't listened to our
    previous podcast, tell us a bit about yourself. And for those who have, maybe
    a quick update on what's changed in the last two years.
  sec: 211
  time: '3:31'
  who: Alexey
- line: Sure. My name is Chris, and I'm an engineer at heart. I spent the first 15
    years of my career working in software, building both AI and non-AI systems at
    places like NASA, MIT Lincoln Lab, some startups, and Microsoft. Around 2005,
    I got into data, thinking it would be easier and I'd be able to go home at five.
    I was wrong.
  sec: 245
  time: '4:05'
  who: Christopher
- line: You started your own company, right?
  sec: 283
  time: '4:43'
  who: Alexey
- line: Yes, and it didn't go as planned. The challenging part wasn’t doing the data
    work itself. We had talented people for that. The real challenge was the systems
    around the data. We had a lot of errors in production, and we couldn’t move fast
    enough to meet customer demands. I used to avoid checking my Blackberry on my
    way to work because I dreaded seeing problems. If there weren’t any issues, I’d
    walk in happily. If there were, I’d brace myself.
  sec: 287
  time: '4:47'
  who: Christopher
- header: Early challenges in data management and the pre-Hadoop era
- line: Was this during the Hadoop era, before all the big data technology boom?
  sec: 361
  time: '6:01'
  who: Alexey
- line: This was actually before Hadoop. We used SQL Server, and our team was so skilled
    that we turned SQL Server into a columnar database to make things faster. Even
    then, the core principles were the same. We dealt with databases, indexes, queries,
    etc. We just used racks of servers instead of the cloud. What I learned was that
    managing a data and analytics team is tough. I started thinking of it as running
    a factory, not for cars but for insights. How do you keep production quality high
    while making changes frequently?
  sec: 366
  time: '6:06'
  who: Christopher
- header: Evolution of DevOps and its influence on data practices
- line: Interesting. So, you mentioned DevOps. When did the concept of DevOps start
    gaining traction? How did it influence you?
  sec: 509
  time: '8:29'
  who: Alexey
- line: Well, the Agile Manifesto came out in 2001, and the first real DevOps practices
    started around 2009 with automated deployment at Twitter. The first DevOps meetup
    happened shortly after that. It's been about 15 years since DevOps really took
    off.
  sec: 533
  time: '8:53'
  who: Christopher
- line: I started my career in 2010, and I remember manually deploying Java applications
    via SFTP. It was nerve-wracking, just hoping nothing would break.
  sec: 578
  time: '9:38'
  who: Alexey
- line: Right? Was that in the documentation too? "Deploy and cross your fingers"?
  sec: 603
  time: '10:03'
  who: Christopher
- line: Almost, there was a page in the internal wiki on how to do that.
  sec: 618
  time: '10:18'
  who: Alexey
- line: Exactly. The question is, why didn't we automate deployments back then or
    have extensive regression tests? Nowadays, it's almost unthinkable not to use
    CI/CD or automated tests in software development. Yet, in data and analytics,
    that hasn't always been the case.
  sec: 629
  time: '10:29'
  who: Christopher
- header: What is DataOps and its importance in the industry
- line: Let's step back and summarize what DataOps is. Then we can talk about what's
    changed in the last two years.
  sec: 713
  time: '11:53'
  who: Alexey
- line: 'Sure. DataOps starts with acknowledging some hard truths about data and analytics:
    we''re often not successful, and many people in these roles are unhappy. We did
    a survey with 700 data engineers, and 78% wanted their job to come with a therapist.
    Fifty percent were considering leaving the field altogether. Teams often fall
    into two categories: heroic, working non-stop but burning out, or bogged down
    in so much process that everything moves at a snail''s pace, leading to frustration.'
  sec: 723
  time: '12:03'
  who: Christopher
- line: So, the only option is to quit and start something else, right?
  sec: 802
  time: '13:22'
  who: Alexey
- line: Unfortunately, yes. When a team relies on heroes or strict processes, you
    end up with a few people holding all the knowledge. If they leave, the team struggles,
    creating a bottleneck. DataOps is about finding a balance. You don't have to live
    in constant fear of making mistakes or being a hero 24/7. There's a middle ground
    where productivity thrives.
  sec: 807
  time: '13:27'
  who: Christopher
- line: Fear is when you're scared of deploying changes because things might break,
    right?
  sec: 857
  time: '14:17'
  who: Alexey
- line: Exactly. Fearful teams often have excessive checklists and reviews. Heroic
    teams will deploy changes and hope for the best, ready to fix issues at any time,
    even if it's their kid's birthday. That’s not sustainable. As a manager, I’ve
    learned to praise the heroism publicly but privately work to ensure those situations
    don't happen again.
  sec: 883
  time: '14:43'
  who: Christopher
- line: So, DataOps involves processes and tools to help move without fear and avoid
    heroism, right?
  sec: 952
  time: '15:52'
  who: Alexey
- line: Yes. DataOps aims to reduce errors in production, whether they're caused by
    bad data, code issues, server failures, or delays. Automation, testing, monitoring,
    and observability are all part of this. By focusing on reducing errors and improving
    cycle time, we can eliminate waste and increase productivity. Gartner reported
    that teams using DataOps tools and practices are ten times more productive, which
    aligns with what I’ve seen.
  sec: 970
  time: '16:10'
  who: Christopher
- header: The current state of DataOps and its evolution over the past two years
- line: Two years ago, there was a lot of hype around MLOps. It brought attention
    to other areas like DataOps. Now, the focus has shifted to AI and LLMs, and it
    seems like DataOps isn’t talked about as much. What’s been happening in DataOps
    over the last two years?
  sec: 1126
  time: '18:46'
  who: Alexey
- line: Good question. I think it’s important to differentiate between buzzwords and
    core principles. DataOps, much like DevOps, is built on lean manufacturing principles
    from the Toyota Production System. These concepts are decades old but still relevant.
    The marketing around new terms like Data Mesh or Data Observability often distorts
    their meanings, which can be frustrating. At its core, DataOps is about agility
    and system thinking—whether you’re working with data, ML models, or LLMs, the
    principles remain the same.
  sec: 1224
  time: '20:24'
  who: Christopher
- header: Systems thinking in DataOps and managing day one vs. day two and day three
- line: You mentioned "thinking in systems." What does that mean?
  sec: 1436
  time: '23:56'
  who: Alexey
- line: It’s about considering not just the initial build of a project but also how
    it will operate on day two and beyond. Day one is building something for the customer.
    Day two is running that system with new data. Day three is making changes based
    on evolving customer needs. A lot of data teams focus on day one, but managing
    day two and day three requires systems thinking. You need to build processes around
    quality checks, monitoring, and quick, safe deployments.
  sec: 1464
  time: '24:24'
  who: Christopher
- line: Let's take a data scientist as an example. They pull data, do some transformations,
    and build a model. Day one is about getting that initial version ready. What happens
    on day two?
  sec: 1573
  time: '26:13'
  who: Alexey
- line: Day two is about making sure those models can run reliably with new data,
    identifying issues before they impact customers. It’s also about ensuring that
    new team members can make changes confidently. For example, a 23-year-old just
    out of college should be able to tweak a line of code and deploy it, knowing that
    the system will catch any problems. That requires solid testing, monitoring, and
    automation frameworks.
  sec: 1614
  time: '26:54'
  who: Christopher
- header: Implementing robust systems for continuous integration and delivery in data
    science
- line: So, thinking in systems means having a platform with integrated components
    like regression tests, automated deployment, and monitoring. This setup ensures
    that changes can be made safely and efficiently.
  sec: 1855
  time: '30:55'
  who: Alexey
- line: Exactly. It’s about finding problems before they reach production. You need
    robust CI/CD pipelines, test data reflective of real-world scenarios, and infrastructure
    as code. If you can deploy quickly with low risk and involve new team members
    in a way that doesn’t jeopardize production, you’ll significantly reduce wasted
    time and effort.
  sec: 1905
  time: '31:45'
  who: Christopher
- header: Reducing waste and inefficiency through DataOps processes
- line: You mentioned that some waste is inevitable. How do DataOps processes help
    minimize this?
  sec: 2053
  time: '34:13'
  who: Alexey
- line: DataOps helps by implementing processes and tools that focus on reducing errors
    and cycle time. Things like version control, automated testing, and observability
    are crucial. However, adoption is slower than I’d hoped. Even with more companies
    using tools like DBT, there’s still a lot of heroism and fear-based decision-making.
  sec: 2136
  time: '35:36'
  who: Christopher
- header: Challenges in adoption and the impact of AI tools like ChatGPT
- line: Maybe everyone’s just too busy playing with ChatGPT now!
  sec: 2344
  time: '39:04'
  who: Alexey
- line: That’s a part of it. There’s a lot of focus on generating things—models, dashboards,
    ETL code—with AI tools. But, focusing on optimizing the creation process only
    tackles a small part of the problem. The majority of time is spent on rework,
    fixing issues, and miscommunication. Reducing waste is where the real productivity
    gains are.
  sec: 2349
  time: '39:09'
  who: Christopher
- header: Automating deployment and using CI/CD to minimize errors
- line: How do DataOps processes help in reducing this waste?
  sec: 2559
  time: '42:39'
  who: Alexey
- line: It’s about automating deployment, using version control, and having tests
    that run in development before production. Just using Git isn’t enough; you need
    end-to-end tests and automated checks. Often, data engineers might use these practices,
    but data scientists or analysts may not, leading to inconsistencies. The whole
    team needs to be on board with these practices.
  sec: 2582
  time: '43:02'
  who: Christopher
- line: That makes sense. Still, it's surprising that more teams aren't using CI/CD
    and Git. To me, it seems like common sense.
  sec: 2670
  time: '44:30'
  who: Alexey
- line: It is, but there are varying levels of adoption. Some might use Git and basic
    CI/CD but lack comprehensive testing or integration with all their tools. Others
    might have pockets of good practice but not across the entire team. What we need
    is for data and analytics teams to adopt a more critical view of their processes,
    as software engineers do.
  sec: 2787
  time: '46:27'
  who: Christopher
- header: Shifting focus from development to production in DataOps
- line: You’ve shifted your focus from development to production. Why is that?
  sec: 3029
  time: '50:29'
  who: Alexey
- line: We found that most teams had built things in production without much consideration
    for development best practices. It was easier to start by observing and monitoring
    production systems. We also realized that the senior-most leaders, like Chief
    Data Officers, often don’t last long in their roles. So we shifted our focus to
    individual contributors—data engineers and scientists who can start implementing
    these practices.
  sec: 3031
  time: '50:31'
  who: Christopher
- header: Importance and role of Kubernetes and data versioning best practices
- line: 'A question from the audience: How important is learning Kubernetes in the
    industry? Has it been widely adopted?'
  sec: 3162
  time: '52:42'
  who: Alexey
- line: Kubernetes is important, but it’s complex. Learn Docker first. If you’re managing
    a smaller team, you might not need Kubernetes. It’s beneficial if you’re running
    many processes, but there are lighter-weight options that might work better for
    smaller use cases.
  sec: 3162
  time: '52:42'
  who: Christopher
- line: 'There are also tools like Google Cloud Run and other serverless options that
    might be simpler to use. Another audience question: How is data versioned in the
    industry these days, and what’s your advice?'
  sec: 3245
  time: '54:05'
  who: Alexey
- line: I’m not a big fan of versioning data itself. I prefer immutability—keeping
    the raw data unchanged and versioning the code that acts upon it. Focus on having
    immutable data with functional access methods and version the processing logic
    instead.
  sec: 3377
  time: '56:17'
  who: Christopher
- header: The role of mindset and culture in reducing turnover and improving DataOps
    practices
- line: 'That approach aligns with functional programming principles, where immutability
    simplifies concurrency issues. Final question: Should the solution for high turnover
    in teams be more about mindset and culture rather than just tooling?'
  sec: 3495
  time: '58:15'
  who: Alexey
- line: Absolutely. Culture and mindset are critical. Tools alone won’t solve the
    problem. Teams need to advocate for better processes and leadership needs to prioritize
    building systems that reduce frustration and increase efficiency. It's about making
    work more enjoyable and sustainable.
  sec: 3514
  time: '58:34'
  who: Christopher
- line: We could keep discussing this for hours, but we’re out of time. Chris, thanks
    for joining us so early in the morning and sharing your insights. I really enjoyed
    our conversation. Thanks, everyone, for tuning in. Looking forward to catching
    up again in a couple of years.
  sec: 3680
  time: '1:01:20'
  who: Alexey
- line: Thanks for the opportunity. I enjoyed it. Take care, everyone!
  sec: 3844
  time: '1:04:04'
  who: Christopher
- line: Goodbye!
  sec: 3847
  time: '1:04:07'
  who: Alexey
---