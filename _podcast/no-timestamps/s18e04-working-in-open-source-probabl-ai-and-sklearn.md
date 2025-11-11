---
episode: 4
guests:
- vincentwarmerdam
ids:
  anchor: atatalksclub/episodes/Working-in-Open-Source---Probabl-ai-and-sklearn---Vincent-Warmerdam-e2j78fs
  youtube: UPlIETGwTg8
image: images/podcast/s18e04-working-in-open-source-probabl-ai-and-sklearn.jpg
links:
  anchor: https://podcasters.spotify.com/pod/show/datatalksclub/episodes/Working-in-Open-Source---Probabl-ai-and-sklearn---Vincent-Warmerdam-e2j78fs
  apple: https://podcasts.apple.com/us/podcast/working-in-open-source-probabl-ai-and-sklearn-vincent/id1541710331?i=1000654481795
  spotify: https://open.spotify.com/episode/0HT3IQOaTXTMH0OdEBnw9s?si=HrLtx7QKT_amZyUbZuqRzQ
  youtube: https://www.youtube.com/watch?v=UPlIETGwTg8
season: 18
short: Working in Open Source - Probabl.ai and sklearn
title: 'Build Sustainable Scikit-Learn Ecosystems: scikit-lego, Skrub, GAP Encoder
  & DevRel'
transcript:
- header: Episode Overview — Open Source Focus
- header: Guest Reintroduction & Vincent’s Open Source Profile
- line: This week, we'll talk about open source again. We have a very special guest,
    Vincent, for the second time. This is not Vincent's first appearance. You were
    one of the first guests on this podcast more than three years ago.
  sec: 100
  time: '1:40'
  who: Alexey
- line: Three to four years ago. Yeah, something like that.
  sec: 120
  time: '2:00'
  who: Vincent
- line: I was checking the previous podcast episode before we started, and it was
    already season two. Season one had only five episodes, and you were one of the
    first recordings of season two. We didn't have transcriptions back then, so I
    had no idea what we talked about. But the topic was getting started with open
    source. Today, we'll talk about open source again. Vincent, you come to mind when
    I think about open source because of the numerous small libraries you've created
    and discussed.
  sec: 123
  time: '2:03'
  who: Alexey
- line: It's not thousands, just to be clear.
  sec: 169
  time: '2:49'
  who: Vincent
- line: Hundreds?
  sec: 172
  time: '2:52'
  who: Alexey
- line: It's a small dozen, for sure. It is a bunch, but thousands is a lot.
  sec: 172
  time: '2:52'
  who: Vincent
- line: Compared to the average person in the industry...
  sec: 182
  time: '3:02'
  who: Alexey
- line: It's probably above average.
  sec: 189
  time: '3:09'
  who: Vincent
- line: Maybe the 99th percentile?
  sec: 191
  time: '3:11'
  who: Alexey
- line: I did some research and found out I'm in the top 10 for open source contributions
    on GitHub in the Netherlands. I knew three other people in that top 10. I'm kind
    of up there, but not thousands.
  sec: 194
  time: '3:14'
  who: Vincent
- line: Fair enough. That was the bio. I promised to improvise since we don't have
    the bio in the show notes. You will tell us more.
  sec: 226
  time: '3:46'
  who: Alexey
- line: Sure. Thanks for the lovely intro.
  sec: 237
  time: '3:57'
  who: Vincent
- header: Early Community Work & PyLadies Code Sprint
- line: Thanks for being here. Before we start, I want to shout out to Johanna Bayer
    for preparing today's interview questions. Thanks, Johanna. The reason we're speaking
    today is because she met you at a conference, correct?
  sec: 240
  time: '4:00'
  who: Alexey
- header: Scikit Lego Origin, Adoption, and Career Impact
- line: Yes, at a PyLadies Code Sprint. There were many projects, and I was there
    on behalf of Scikit-Learn to help people get their first PR in. Johanna was in
    my Scikit-Learn bubble doing docs work and then asked if I wanted to come on this
    podcast. I recognized the logo and agreed to return. A few years ago, we talked
    about Scikit Lego, one of the projects we discussed.
  sec: 259
  time: '4:19'
  who: Vincent
- line: That project played a role in getting me my current job. Scikit Lego consists
    of Lego-like bricks I built using Scikit-Learn tricks. It started as a side project
    but now has around 30,000 downloads a month and is in production in many places.
    It's one reason the Scikit-Learn core maintainers thought having me at the company
    would be useful. I initially thought it was just a cute plugin, but it turned
    out to be significant during my job interview.
  sec: 259
  time: '4:19'
  who: Vincent
- line: We usually start our interviews with your background. Can you talk about your
    career journey so far?
  sec: 348
  time: '5:48'
  who: Alexey
- header: 'Career Path: Econometrics → DevRel → Core Engineering'
- line: Sure. I studied econometrics and operations research, which is quite math-heavy.
    Around graduation, I discovered machine learning and wanted to try it out. I decided
    to backpack while taking some client programming work with me. I found programming
    as enjoyable as clubbing, which signaled me to pivot my career towards tech instead
    of being a consultant.
  sec: 363
  time: '6:03'
  who: Vincent
- line: I did tech consulting for a while before getting a job offer from Rasa as
    a Developer Advocate. I hadn't heard of that role before, but it sounded interesting
    as a gateway to NLP. The consultancy I was at didn't offer NLP opportunities,
    so I switched.
  sec: 363
  time: '6:03'
  who: Vincent
- line: I was a big fan of spaCy, and two years after working at Rasa, Explosion AI
    (the creators of spaCy) hired me as a Developer Advocate and Core Developer on
    their Prodigy product. I did Developer Relations and core development there for
    two years. Eventually, I joined some Scikit-Learn core maintainers starting a
    company called :probabl., and that ball got rolling quickly.
  sec: 363
  time: '6:03'
  who: Vincent
- line: Now I do open source work and Developer Relations at :probabl. That's a quick
    summary of my career. Along the way, I've organized conferences and meetups and
    built several open source projects.
  sec: 363
  time: '6:03'
  who: Vincent
- line: How what?
  sec: 481
  time: '8:01'
  who: Alexey
- line: That's an American saying, 'That's how the cookie crumbles.'
  sec: 483
  time: '8:03'
  who: Vincent
- line: What does that mean?
  sec: 486
  time: '8:06'
  who: Alexey
- line: It's similar to 'Bob's your uncle,' meaning 'That's the short story.' A cookie
    crumbles in one way; the crumbs fall down and never split in other directions.
    It's an American saying. Sayings are weird. [chuckles]
  sec: 488
  time: '8:08'
  who: Vincent
- header: 'Company Naming: Why :probabl. Is Separate from Scikit-Learn'
- line: There are companies behind open source products that typically don't share
    the same name. For example, Explosion AI created spaCy, and :probabl. is associated
    with Scikit-Learn. Why didn't they just name it Scikit-Learn?
  sec: 513
  time: '8:33'
  who: Alexey
- line: Rasa has 'Rasa' in their product name. Some companies do that.
  sec: 533
  time: '8:53'
  who: Vincent
- line: They do. So, why not name it Scikit-Learn instead of :probabl.?
  sec: 536
  time: '8:56'
  who: Alexey
- line: In :probabl.'s case, Scikit-Learn is a huge project with a vast community.
    Some core maintainers work at :probabl., but the company is not Scikit-Learn.
    There's a distinction.
  sec: 544
  time: '9:04'
  who: Vincent
- line: You could say :probabl. acts as a brand operator. We intend to hire many open
    source maintainers to work on this, but it's a larger community. Claiming the
    name for a company wouldn't make sense.
  sec: 562
  time: '9:22'
  who: Vincent
- line: And Explosion does spaCy but also other stuff.
  sec: 580
  time: '9:40'
  who: Vincent
- line: Prodigy, right?
  sec: 585
  time: '9:45'
  who: Alexey
- line: Yes. Naming your company after your open source project limits you to that
    project. :probabl. will likely do more than just Scikit-Learn. We might offer
    training, consultancy, and possibly other products. There are many reasons not
    to call ourselves Scikit-Learn.
  sec: 586
  time: '9:46'
  who: Vincent
- line: Also, the legal aspect. Scikit-Learn is a name that already exists. It's probably
    registered and trademarked, so we can't use it.
  sec: 586
  time: '9:

    46'
  who: Vincent
- header: Scikit-Learn Governance, NumFOCUS, and Project History
- line: I'm checking the Scikit-Learn website. I don't see any trademark, but it probably
    belongs to NumFOCUS or another organization.
  sec: 628
  time: '10:28'
  who: Alexey
- line: To my knowledge, it's its own entity. NumFOCUS is an umbrella for funding
    some open source projects. There are NumFOCUS projects and 'associated' projects.
    I believe Scikit-Learn is an associated project.
  sec: 639
  time: '10:39'
  who: Vincent
- line: So NumPy is a NumFOCUS project, and Scikit-Learn is only associated?
  sec: 664
  time: '11:04'
  who: Alexey
- line: That's my understanding. These distinctions matter because Scikit-Learn has
    been a large community for decades. It's not something a company can just claim.
  sec: 670
  time: '11:10'
  who: Vincent
- line: Before that, the creator originally... It originated from Inria, the research
    lab in France. What's the story there?
  sec: 695
  time: '11:35'
  who: Alexey
- line: I know parts of it. The original version may have started as a Google Summer
    of Code project. Inria played a significant role in its maintenance, with several
    people working on Scikit-Learn and writing papers. Companies also sponsored developers.
    For example, Andreas Müller was supported by NYU for his work on Scikit-Learn.
  sec: 710
  time: '11:50'
  who: Vincent
- line: Microsoft has a similar arrangement now. Companies like Quansight Labs provide
    consulting and contribute PRs. It's beneficial for companies to have core developers
    on their team.
  sec: 710
  time: '11:50'
  who: Vincent
- line: Like Scikit Lego.
  sec: 804
  time: '13:24'
  who: Alexey
- line: Yes, and projects like UMAP. If you want to use the UMAP clustering visualization
    algorithm, you need to install it as a Scikit-Learn plugin. Many projects like
    it are valuable to the ecosystem.
  sec: 806
  time: '13:26'
  who: Vincent
- header: 'Ecosystem Strategy: Plugins vs. Core Scikit-Learn Features'
- line: Contributing something new to Scikit-Learn is difficult because maintainers
    are cautious about maintaining new methods. It's easier to create a plugin that
    follows the API and is maintained separately.
  sec: 841
  time: '14:01'
  who: Alexey
- line: There are concerns beyond maintenance, such as benchmarking and quality. Scikit-Learn
    is seen as an example to follow, so what's included should be high quality. Some
    core algorithms are kept for historical reasons, but not every new paper can be
    included, or it would become unmanageable.
  sec: 875
  time: '14:35'
  who: Vincent
- line: UMAP isn't in Scikit-Learn because it relies on 'numba,' an LLVM compiler
    trick to speed up Python code. Introducing new dependencies can be an issue. Scikit
    Lego, which I helped maintain, looks at Scikit-Learn issues and implements fun
    and useful features that Scikit-Learn can't include.
  sec: 875
  time: '14:35'
  who: Vincent
- line: Scikit Lego is fun and useful for maintainers. It's not taken as seriously
    as Scikit-Learn, but it allows for experimentation and implementation of features
    that Scikit-Learn can't include.
  sec: 875
  time: '14:35'
  who: Vincent
- header: Scikit Lego in Corporate Training and Contributor Growth
- line: Can you tell us more about Scikit Lego? How did maintaining this library lead
    to working at :probabl.?
  sec: 1003
  time: '16:43'
  who: Alexey
- line: As a consultant, I noticed the need for reusable components for tasks like
    selecting columns from pandas. Instead of re-implementing the same thing repeatedly,
    I created a collection of Lego bricks. A colleague and I used these components
    for training and teaching open source, making it a utility for corporate training.
  sec: 1013
  time: '16:53'
  who: Vincent
- line: Using Scikit Lego for corporate training helped me get contributors. Offering
    students the chance to commit to open source as part of their lesson was a win-win,
    making the library better while helping them learn.
  sec: 1013
  time: '16:53'
  who: Vincent
- line: That's smart.
  sec: 1089
  time: '18:09'
  who: Alexey
- header: 'Maintainer Transition: Finding Sustainable Project Stewards'
- line: It's enjoyable and beneficial. As time went on, I used the library less, so
    we looked for a new maintainer. Francesco volunteered, and his fresh perspective
    and enthusiasm improved the project.
  sec: 1091
  time: '18:11'
  who: Vincent
- line: At PyData Amsterdam, I told people we were looking for a new maintainer who
    actually uses the library. Francesco had already contributed and expressed interest,
    so we discussed it further.
  sec: 1142
  time: '19:02'
  who: Alexey
- line: Francesco uses Scikit Lego at work, which makes him a great maintainer. He
    adds features and enjoys maintaining the library, which is crucial for its sustainability.
  sec: 1153
  time: '19:13'
  who: Vincent
- line: You approached people at the conference, asking if they wanted to maintain
    the library?
  sec: 1202
  time: '20:02'
  who: Alexey
- line: Yes, but it was more about finding someone who uses it. Francesco had already
    shown interest and made contributions. Meeting in person at the conference solidified
    it.
  sec: 1217
  time: '20:17'
  who: Vincent
- line: And he uses Scikit Lego at work, right?
  sec: 1263
  time: '21:03'
  who: Alexey
- line: Yes, though some details are private. He finds the library useful and fun,
    which aligns with our goal of maintaining it as a fun project.
  sec: 1268
  time: '21:08'
  who: Vincent
- line: How do you make a library fun to maintain?
  sec: 1309
  time: '21:49'
  who: Alexey
- header: Motivating Volunteer Maintainers and Keeping Projects Fun
- line: We celebrate that it's volunteer work. We encourage implementing features
    if they're in someone's domain or sound fun. We require benchmarks to confirm
    improvements. If it's not fun, it won't be maintained.
  sec: 1311
  time: '21:51'
  who: Vincent
- line: I have a child now, so I won't spend my evenings on uninteresting tasks. Francesco's
    fresh perspective and ideas keep the project enjoyable for both of us. He would
    make a great podcast guest to share his perspective.
  sec: 1311
  time: '21:51'
  who: Vincent
- header: 'Demonstrating Quality: Open Source Work as a Hiring Signal'
- line: You told us about Scikit Lego. How did it lead to your current job?
  sec: 1409
  time: '23:29'
  who: Alexey
- line: The Scikit-Learn maintainer group was looking for someone who could clearly
    explain data science and machine learning without the hype. My resume, including
    Scikit Lego, showed I took testing and quality seriously, which helped in the
    interview process.
  sec: 1424
  time: '23:44'
  who: Vincent
- line: The technical interview was lightweight because they could see my work with
    Scikit Lego. Other factors, like conference talks and keynotes, also helped. Maintaining
    Scikit Lego showcased my dedication to open source and quality.
  sec: 1424
  time: '23:44'
  who: Vincent
- line: I was talking about thousands of small open source libraries and you said,
    'It's not true.' But when it comes to your talks, I searched your name on YouTube...
  sec: 1527
  time: '25:27'
  who: Alexey
- line: Yeah?
  sec: 1541
  time: '25:41'
  who: Vincent
- line: I couldn't finish scrolling.
  sec: 1542
  time: '25:42'
  who: Alexey
- header: 'Calm Code Philosophy: Practical, Low-Pressure Learning'
- line: 'I''m a frequent speaker at PyData. During COVID, I started

    Calm Code, a tutorial website as an alternative to DataCamp. I didn''t like their
    approach of pushing future-proof skills. Calm Code focuses on learning tricks
    to make your day-to-day work easier.'
  sec: 1546
  time: '25:46'
  who: Vincent
- line: That’s why it’s 'calm' – no pressure to learn things. You can learn whatever
    you want.
  sec: 1597
  time: '26:37'
  who: Alexey
- line: Yes, just useful tips to improve your workflow. Making over 700 videos for
    Calm Code helped me practice clear communication. Creating videos is now like
    writing a FOR loop for me.
  sec: 1604
  time: '26:44'
  who: Vincent
- line: Thousands is actually not too far from the truth.
  sec: 1640
  time: '27:20'
  who: Alexey
- header: 'Content Production: Videos, Scale, and Communication Practice'
- line: Yes, counting my work at Rasa and Explosion, it's close to 1000 videos. At
    Explosion, we focused on quality over quantity.
  sec: 1644
  time: '27:24'
  who: Vincent
- line: Also, counting all your work as a Dev Advocate at Rasa, Explosion, right?
  sec: 1650
  time: '27:30'
  who: Alexey
- line: Yes. At Rasa, I made around 100 videos. At Explosion, I made fewer but more
    polished videos. With experience, recording videos became easier. The challenge
    now is coming up with good examples and insights.
  sec: 1659
  time: '27:39'
  who: Vincent
- line: Coming up with examples is the most difficult part, right?
  sec: 1708
  time: '28:28'
  who: Alexey
- line: Yes. Having access to Scikit-Learn core maintainers helps. I can ask them
    about annoying issues they've seen on GitHub. There are always interesting experiments
    and benchmarks to explore.
  sec: 1712
  time: '28:32'
  who: Vincent
- line: Do you still actively put things out on Calm Code?
  sec: 1765
  time: '29:25'
  who: Alexey
- header: 'Calm Code Platform: Django, Monetization, and Hiring Contributors'
- line: Yes, but I've realized that collaboration is more sustainable. Having collaborators
    with different expertise makes the platform more effective and enjoyable. We're
    building a proper platform for Calm Code, moving beyond just markdown files.
  sec: 1770
  time: '29:30'
  who: Vincent
- line: The Django app is live. We're learning how to handle payments to make the
    project sustainable. The goal is to have a hobby project that provides a small
    income, allowing us to hire external contributors to create content.
  sec: 1770
  time: '29:30'
  who: Vincent
- line: So right now it’s Django?
  sec: 1853
  time: '30:53'
  who: Alexey
- line: Yes, it's a full Django setup. We're adding features and learning as we go.
    The hope is to cover more topics like databases, data analytics, cloud, Docker,
    and Kubernetes.
  sec: 1854
  time: '30:54'
  who: Vincent
- line: I see that there is already some Docker stuff, right?
  sec: 1898
  time: '31:38'
  who: Alexey
- header: 'CI and Cost Optimization: Custom Runners and GitHub Actions'
- line: Barely. There's much more we want to do. I'm interested in exploring when
    it makes sense to use a custom runner for GitHub Actions to save on compute costs
    and optimize performance.
  sec: 1902
  time: '31:42'
  who: Vincent
- line: A runner executes the action on your environment, not on GitHub’s?
  sec: 1938
  time: '32:18'
  who: Alexey
- header: 'Sustainable Compute Examples: Leaf.cloud and Environmental Impact'
- line: Yes. Using a VM you own can offer caching benefits and save costs. There are
    startups like Leaf.cloud offering carbon-negative compute, making it both economically
    and environmentally competitive.
  sec: 1946
  time: '32:26'
  who: Vincent
- line: Leaf.cloud places server racks in apartment basements, using the heat to preheat
    water, saving gas. This setup is carbon negative and cost-effective, as the compute
    is paid for by another party.
  sec: 1989
  time: '33:09'
  who: Vincent
- line: With such setups, you have control and can still achieve great results. Celebrating
    intellectual freedom and innovation is something we aim to highlight on Calm Code.
  sec: 1989
  time: '33:09'
  who: Vincent
- header: 'Teaching Fundamentals: Docker, pip, and Git Challenges for Beginners'
- line: You mentioned that for experienced Python users, pip install is second nature.
    For newcomers, Docker is challenging. In our data engineering course, Docker is
    the most problematic module.
  sec: 2069
  time: '34:29'
  who: Alexey
- line: For beginners, pip, Docker, and Git are major stumbling blocks. It's important
    to teach the conceptual understanding of these tools, not just the commands.
  sec: 2107
  time: '35:07'
  who: Vincent
- line: You want to cover all three, right?
  sec: 2119
  time: '35:19'
  who: Alexey
- line: Eventually, yes. But designing a good course is a one-time effort.
  sec: 2121
  time: '35:21'
  who: Vincent
- line: You already have. I think I saw a logo of GitHub on your...
  sec: 2131
  time: '35:31'
  who: Alexey
- header: 'Conceptual Learning: Mindset Over Commands for Tooling'
- line: I use GitHub in many courses, but Calm Code assumes you're not a complete
    beginner. You need some programming experience.
  sec: 2136
  time: '35:36'
  who: Vincent
- line: That's what we do, too. Where do people actually learn all that stuff?
  sec: 2148
  time: '35:48'
  who: Alexey
- line: Sometimes it's about teaching the mindset, not just the tool. For example,
    how to think about Git conceptually or recognizing common issues.
  sec: 2154
  time: '35:54'
  who: Vincent
- line: For large CSV files, don't use Git for data. Use a different system for versioning.
    Providing this context helps people understand the best practices.
  sec: 2154
  time: '35:54'
  who: Vincent
- line: I've never taken a course for Git, Docker, or Python. I learned by figuring
    out how to do things when needed. Maybe assuming people will learn as they go
    is also a good approach.
  sec: 2210
  time: '36:50'
  who: Alexey
- line: To make learning Docker easy and enjoyable, focus on getting people to a 'minimum
    viable tinkerability' where they're comfortable experimenting.
  sec: 2236
  time: '37:16'
  who: Vincent
- line: Once people reach that level, encourage them to tinker as much as possible.
    That's a philosophy I'm exploring.
  sec: 2236
  time: '37:16'
  who: Vincent
- line: That's a nice idea. I realized today's topic is actually not education, even
    though this is great stuff to talk about.
  sec: 2294
  time: '38:14'
  who: Alexey
- header: Combining DevRel and Core Development Responsibilities
- line: Sure, let's segue back to Scikit-Learn stuff.
  sec: 2302
  time: '38:22'
  who: Vincent
- line: You work at :probabl. as a Developer Advocate and also implement core features.
    How do you manage both roles?
  sec: 2306
  time: '38:26'
  who: Alexey
- line: At Explosion, we experimented with a Dev Rel team but decided everyone should
    be a machine learning engineer. As a good Dev Rel, you should also be skilled
    in your domain and comfortable creating content.
  sec: 2347
  time: '39:07'
  who: Vincent
- line: It's like being a full-stack developer with a focus on Kubernetes. I see myself
    as a machine learning engineer with added skills in creating content.
  sec: 2347
  time: '39:07'
  who: Vincent
- line: 'At :probabl., I''m bootstrapping the Dev Rel

    practice. I have a whiteboarding playlist, a live stream, and a podcast. Once
    these are established, I''ll focus more on open-source contributions.'
  sec: 2347
  time: '39:07'
  who: Vincent
- line: I'm helping with the Skrub effort, doing benchmarks and sharing ideas. I see
    myself as a senior person working on what matters to the company.
  sec: 2347
  time: '39:07'
  who: Vincent
- line: Yet your title is Dev Advocate, right? Or what's your title?
  sec: 2477
  time: '41:17'
  who: Alexey
- header: 'Role Definition: Developer Relations Engineer at :probabl.'
- line: It's Developer Relations Engineer. I joked about preferring 'Senior Person,'
    but it's about fixing problems for the company. Titles like 'senior' or 'junior'
    feel counterproductive. I do a lot of Dev Rel stuff, so Developer Relations Engineer
    is fine.
  sec: 2481
  time: '41:21'
  who: Vincent
- line: Why does Scikit-Learn need a Dev Rel?
  sec: 2533
  time: '42:13'
  who: Alexey
- header: Enhancing Scikit-Learn with Interactive Content and Videos
- line: :probabl. hired me, not Scikit-Learn. Scikit-Learn has great documentation,
    thanks to colleagues like Arturo, who leads the docs effort. But there's always
    more we can do, like interactive code examples and maintainingers' experiences
    through podcasts.
  sec: 2540
  time: '42:20'
  who: Vincent
- line: Scikit-Learn's docs are amazing, but additional content like YouTube videos
    explaining algorithmic details adds value. We recently reached 10,000 views on
    our YouTube channel.
  sec: 2569
  time: '42:49'
  who: Vincent
- line: There is already a ton of content explaining Scikit-Learn. But my job is to
    promote :probabl. and, through it, Scikit-Learn. While the Scikit-Learn community
    creates MOOCs and other resources, we aim to add value in different ways.
  sec: 2647
  time: '44:07'
  who: Alexey
- header: 'Deep Dive Example: Why the Standard Scaler Is Complex'
- line: Via :probabl., I promote Scikit-Learn. For example, we have scalers in Scikit-Learn
    to standardize data. The Standard Scaler subtracts the mean and scales the variance,
    but there are many complexities involved. A video explaining these details helps
    users appreciate the intricacies.
  sec: 2670
  time: '44:30'
  who: Vincent
- line: The Standard Scaler must handle various data types, like sparse matrices and
    data frames, and support partial fit methods for microbatching. These details
    are hard to cover in a tutorial but are valuable for users to understand.
  sec: 2699
  time: '44:59'
  who: Vincent
- line: This is a video coming out this week. Users don't need to know all these details,
    but appreciating them can be helpful.
  sec: 2699
  time: '44:59'
  who: Vincent
- line: I've never realized that such a simple thing could be that difficult.
  sec: 2840
  time: '47:20'
  who: Alexey
- line: The Standard Scaler is Not Standard is the title of the video coming out this
    week.
  sec: 2845
  time: '47:25'
  who: Vincent
- line: I see. It's too mathematical. 'Compute the mean, subtract the mean...'
  sec: 2849
  time: '47:29'
  who: Alexey
- line: On the spectrum of math, this is lightweight, but so much can go wrong.
  sec: 2858
  time: '47:38'
  who: Vincent
- line: Yeah, I never realized that.
  sec: 2866
  time: '47:46'
  who: Alexey
- line: Looking at Scikit-Learn source code helped me understand how to implement
    things in Scikit Lego. It equips me to know which parts are worth diving into.
  sec: 2868
  time: '47:48'
  who: Vincent
- line: What is Skrub? You mentioned it several times.
  sec: 2907
  time: '48:27'
  who: Alexey
- header: 'Skrub Overview: Table Vectorizer and Pragmatic Tabular Defaults'
- line: Skrub is a Scikit-Learn plugin in an experimental phase. Gaël Varoquaux and
    others are working on it. The goal is to simplify handling tabular data with components
    like the table vectorizer, which automatically determines the best way to process
    different types of data.
  sec: 2911
  time: '48:31'
  who: Vincent
- line: This is how you pronounce his last name?
  sec: 2922
  time: '48:42'
  who: Alexey
- line: I'm not sure. Let's call him Gaël. The table vectorizer is an example of Skrub's
    goal to handle tabular data efficiently. It applies sensible defaults to different
    types of data, providing a reasonable benchmark with minimal effort.
  sec: 2924
  time: '48:44'
  who: Vincent
- line: These components are too experimental for Scikit-Learn but offer pragmatic
    and useful solutions.
  sec: 3013
  time: '50:13'
  who: Vincent
- line: Sounds quite cool.
  sec: 3025
  time: '50:25'
  who: Alexey
- header: 'Skrub GAP Encoder: Clustering Dirty Categories to Avoid One-Hot Explosion'
- line: One feature in Skrub is the GAP encoder, which handles dirty categories by
    modeling them as text and clustering similar items. This prevents the explosion
    of one-hot encoding and offers efficient data processing.
  sec: 3027
  time: '50:27'
  who: Vincent
- line: For example, job titles with typos can be grouped into topics, reducing the
    complexity of encoding. Skrub aims to provide tools for efficient data processing,
    making it easier to achieve solid benchmarks.
  sec: 3040
  time: '50:40'
  who: Vincent
- line: In our courses, we address questions about handling large numbers of categories.
    Skrub offers practical solutions, allowing users to start with minimal effort
    and then fine-tune their approach.
  sec: 3129
  time: '52:09'
  who: Alexey
- line: Skrub may not be perfect for every use case, but it provides a solid starting
    point. Users can dunk a data frame in and get a reasonable benchmark, appreciating
    the tools used under the hood.
  sec: 3154
  time: '52:34'
  who: Vincent
- line: Instead of listing all options, the answer could be, 'Try this library and
    see what it comes up with.' This approach helps users understand the encoders
    and appreciate the process.
  sec: 3166
  time: '52:46'
  who: Alexey
- line: While Skrub can't handle every unique case, it provides sensible defaults
    for common scenarios, like encoding dates and times.
  sec: 3186
  time: '53:06'
  who: Vincent
- line: Scikit-Learn existed without a company behind it for a long time. Why start
    one now?
  sec: 3216
  time: '53:36'
  who: Alexey
- header: 'Why Form a Company for Scikit-Learn: Funding and European Tech Goals'
- line: My perspective is that relying on academic funding models is risky for such
    a central open-source project. Creating a company can provide more stable funding
    and support for Scikit-Learn. Additionally, there's tremendous value in the project,
    and some companies might be willing to pay for it.
  sec: 3227
  time: '53:47'
  who: Vincent
- line: Having more European tech companies is also a goal. It would be nice to have
    more tech companies from Europe, similar to how France has Hugging Face and Mistral.
    Being a company exposes you to industry problems, which is beneficial for the
    project.
  sec: 3227
  time: '53:47'
  who: Vincent
- line: A company makes sense for these reasons. The exact business model is still
    developing, but training and consulting are likely components.
  sec: 3227
  time: '53:47'
  who: Vincent
- line: And the business model is still yet to be determined? The exact business model.
  sec: 3375
  time: '56:15'
  who: Alexey
- header: 'Potential Business Models: Training, Consulting, and Partnerships'
- line: 'There are ideas like training and consulting. Collaborations with

    cloud providers might happen, but it''s still early. You can check the TechCrunch
    article for more details.'
  sec: 3379
  time: '56:19'
  who: Vincent
- line: '[The article] was published on February 1st?'
  sec: 3418
  time: '56:58'
  who: Alexey
- line: Earlier this year. That's when the official announcements started.
  sec: 3423
  time: '57:03'
  who: Vincent
- line: Yeah. The website mentions 'Open source services – provide training, certification,
    and expert solutions for enterprise AI challenges.'
  sec: 3430
  time: '57:10'
  who: Alexey
- line: Yes, that covers it.
  sec: 3439
  time: '57:19'
  who: Vincent
- line: We don't have a lot of time left. What's your next personal project?
  sec: 3444
  time: '57:24'
  who: Alexey
- header: 'Upcoming Work: Calm Code Book on Expectations vs. Reality in Data'
- line: Calm Code will have a book about expectations versus reality in the field
    of data. It will cover overpromised aspects of data science and share anecdotes
    and stories.
  sec: 3454
  time: '57:34'
  who: Vincent
- line: Back in the day, data science was touted as the sexiest profession. Looking
    back, many promises were overhyped. The book will address these stories and focus
    on culture and preventing failures.
  sec: 3470
  time: '57:50'
  who: Vincent
- line: I want to write about the clash between expectations and reality in data science.
    The book will include anecdotes and stories from the field.
  sec: 3491
  time: '58:11'
  who: Vincent
- header: 'Live Experiments: Converting Tree Models to SQL and Streaming Work'
- line: We also have a live stream at :probabl. where we explore new technologies.
    For example, I'm looking into converting tree-based models into SQL queries for
    efficient processing.
  sec: 3497
  time: '58:17'
  who: Vincent
- line: I'm exploring whether converting tree-based models into SQL queries can optimize
    large batch jobs. It's an experiment we'll figure out on the live stream.
  sec: 3571
  time: '59:31'
  who: Vincent
- line: Do you prepare for the live stream or is it complete exploration?
  sec: 3624
  time: '1:00:24'
  who: Alexey
- header: 'Live Stream Format: Preparation, Live Coding, and Demos'
- line: I prepare, but part of the stream is live coding and sharing insights. It's
    important to be prepared, especially when demoing other projects.
  sec: 3627
  time: '1:00:27'
  who: Vincent
- header: Episode Closing and Final Remarks
- line: Okay, that's all we have time for today. Thanks for joining us and sharing
    your experience and future plans.
  sec: 3675
  time: '1:01:15'
  who: Alexey
- line: Have a good one!
  sec: 3713
  time: '1:01:53'
  who: Vincent
- line: Yeah, you too. Have a great week!
  sec: 3715
  time: '1:01:55'
  who: Alexey
description: 'Discover scalable scikit-learn ecosystems with scikit-lego and Skrub:
  learn GAP Encoder, contributor growth, CI optimization and DevRel sustainability.'
intro: How do you build a sustainable scikit-learn ecosystem that serves both users
  and contributors? In this episode Vincent Warmerdam — Research Advocate at Rasa,
  open source contributor and creator of Calm Code and the Koaning blog — walks through
  practical decisions that keep ML tooling healthy over time. We cover scikit-lego’s
  origins and adoption, governance and NumFOCUS roles, and the trade-offs between
  adding features to core scikit-learn versus plugins. <br><br> Key topics include
  maintaining contributor growth and steward transitions, motivating volunteer maintainers,
  DevRel combined with core engineering, and demonstrable open source quality as a
  hiring signal. Vincent also explains Skrub’s table vectorizer and the GAP Encoder
  approach for clustering dirty categorical values to avoid one-hot explosion, plus
  examples of CI and cost optimization (custom runners, GitHub Actions) and sustainable
  compute choices. You’ll get actionable guidance on teaching fundamentals (Docker,
  pip, Git), producing interactive content, and potential business models around training
  and consulting. Tune in to learn concrete strategies for building, funding, and
  scaling scikit-learn-compatible tools and communities without sacrificing long-term
  sustainability.
---

Links:

* [probabl. YouTube channel](https://www.youtube.com/@UCIat2Cdg661wF5DQDWTQAmg){:target="_blank"}
* [Calmcode website](https://calmcode.io/){:target="_blank"}
* [probabl. website](https://probabl.ai/){:target="_blank"}
