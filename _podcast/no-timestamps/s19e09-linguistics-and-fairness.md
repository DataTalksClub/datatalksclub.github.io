---
episode: 9
guests:
- tamaraatanasoska
ids:
  anchor: atalksclub/episodes/Linguistics-and-Fairness---Tamara-Atanasoska-e2thdk0
  youtube: sXU9vMDBjmk
image: images/podcast/s19e09-linguistics-and-fairness.jpg
links:
  anchor: https://creators.spotify.com/pod/show/datatalksclub/episodes/Linguistics-and-Fairness---Tamara-Atanasoska-e2thdk0
  apple: https://podcasts.apple.com/us/podcast/linguistics-and-fairness-tamara-atanasoska/id1541710331?i=1000684411354
  spotify: https://open.spotify.com/episode/6S4a85iiRzl7NU1HykXeKT?si=FNoDtj74T2ujQKzKdDWwzA
  youtube: https://www.youtube.com/watch?v=sXU9vMDBjmk
season: 19
short: Linguistics and Fairness
title: "Fairness in AI: Using Fairlearn to Mitigate Credit Scoring Bias & Build Explainable Models"
transcript:
- header: Linguistics and Fairness
- line: This week, we’ll talk about linguistic fairness and a sociotechnical perspective
    on AI. I’m not entirely sure what that means, but we’ll find out.
  sec: 0
  time: 0:00
  who: Alexey
- line: We have a special guest today—Tamara. She works on machine learning explainability,
    interpretability, and fairness as an open-source engineer at Probable. You’re
    actually the third person from Probable we’ve had this year. Guillaume was one
    of them, right?
  sec: 0
  time: 0:00
  who: Alexey
- line: Yes, that’s correct.
  sec: 151
  time: '2:31'
  who: Tamara
- header: 'Guest introduction: Tamara’s background and career'
- line: Tamara is a maintainer of Fairlearn and a contributor to scikit-learn and
    Skope-Rules. How do you pronounce it—Skope?
  sec: 157
  time: '2:37'
  who: Alexey
- line: We pronounce it “Scopes,” but others might say it differently.
  sec: 170
  time: '2:50'
  who: Tamara
- line: We’ll stick with your pronunciation. Tamara has a background in computer science,
    software engineering, and computational linguistics. Welcome to the interview!
  sec: 174
  time: '2:54'
  who: Alexey
- line: Tamara
  sec: 174
  time: '2:54'
  who: Alexey
- line: Thank you for inviting me. It’s great to be here.
  sec: 174
  time: '2:54'
  who: Alexey
- header: 'Tamara’s career journey: Software engineering, music tech, and computational
    linguistics'
- line: Thanks, as always, to Johanna Bayer for helping prepare today’s questions.
    Let’s start with your background. Can you tell us more about your career journey
    so far?
  sec: 198
  time: '3:18'
  who: Alexey
- line: Sure! As you mentioned, I’m an open-source software engineer at Probable.
    I split my time between maintaining Fairlearn and contributing to other projects
    like Skope-Rules and, occasionally, scikit-learn.
  sec: 198
  time: '3:18'
  who: Tamara
- line: Before that, I spent several years in computational linguistics research and
    have been studying it for over four years now. I’m also starting a new research
    project soon, but I’m still defining its scope.
  sec: 198
  time: '3:18'
  who: Tamara
- line: In a broader sense, I’ve worked as a software engineer for the last 15 years.
    I started in civic tech, then spent five years in music tech. Over the past few
    years, I’ve focused on machine learning, specifically natural language processing.
  sec: 198
  time: '3:18'
  who: Tamara
- line: Music tech sounds interesting. Tell me more about that.
  sec: 277
  time: '4:37'
  who: Alexey
- line: I’ve always been passionate about music. I have a background in music and
    play the violin—I even went to music school. In 2015, I started working at Ableton,
    a leading company in music production software. I began in developer relations
    and later joined the hardware team as a software engineer, where I worked for
    about four years.
  sec: 281
  time: '4:41'
  who: Tamara
- line: Did you work on things like guitar pedals?
  sec: 322
  time: '5:22'
  who: Alexey
- line: Not exactly. For example, I worked on Push 2, a digital instrument. It’s a
    console with pads that let you sequence music, create patterns, and access music
    production features without needing to look at a computer.
  sec: 326
  time: '5:26'
  who: Tamara
- line: So, when I see someone at a concert pressing buttons on a panel, is that what
    you worked on?
  sec: 355
  time: '5:55'
  who: Alexey
- line: Yes, but there are different types of consoles. Some are designed for live
    performances with a limited scope, while others, like Push, aim to be full instruments
    where you can lose yourself in the creative flow.
  sec: 369
  time: '6:09'
  who: Tamara
- line: That’s fascinating. I’ve seen these setups with a console and a laptop. Is
    the laptop where the computation happens?
  sec: 401
  time: '6:41'
  who: Alexey
- line: Exactly. For devices like Push, most of the computation happens on the connected
    laptop. There’s been a trend recently toward standalone devices that eliminate
    the need for a laptop, allowing for a distraction-free experience. However, those
    devices are expensive to produce.
  sec: 414
  time: '6:54'
  who: Tamara
- line: It’s definitely more affordable to use a laptop and a panel.
  sec: 491
  time: '8:11'
  who: Alexey
- line: Yes, but for many people, music is their life, and standalone devices offer
    a unique creative experience.
  sec: 516
  time: '8:36'
  who: Tamara
- line: After music tech, how did you transition to language and AI?
  sec: 525
  time: '8:45'
  who: Alexey
- line: It might seem like a strange shift, but it ties closely to my background.
    To explain, I’d need to revisit my life story.
  sec: 536
  time: '8:56'
  who: Tamara
- line: I studied computer science for my first degree, starting at 18. Before that,
    I was a language enthusiast. I attended a language-focused high school—or gymnasium,
    as it’s called in German.
  sec: 536
  time: '8:56'
  who: Tamara
- header: Tamara’s background in language and computer science
- line: Yes, I know the term gymnasium. It’s like a specialized high school.
  sec: 593
  time: '9:53'
  who: Alexey
- line: Exactly!
  sec: 597
  time: '9:57'
  who: Tamara
- line: I studied ethics and languages, exploring language as a phenomenon. I learned
    Latin and other foreign languages, which was fascinating. But I also found computers
    really fun and decided to pursue a computer science degree. However, I never forgot
    my first passion for language, which originally led me to study at the gymnasium.
  sec: 604
  time: '10:04'
  who: Tamara
- line: During my computer science studies in the late 2000s and early 2010s, machine
    learning was emerging, and I became very interested in it. Unfortunately, in Macedonia,
    where I’m from, there weren’t many opportunities to study it back then. I started
    reading books, including On Intelligence, which explored cognition through machine
    learning methods. It was a turning point for me because I realized that language
    is one of the most human cognitive processes.
  sec: 604
  time: '10:04'
  who: Tamara
- line: I began ordering neuroscience books from Amazon, secondhand, and became interested
    in computational neuroscience. I applied to a few programs, but things didn’t
    work out, so I continued working as a software engineer abroad. Despite the challenges,
    this passion never went away.
  sec: 604
  time: '10:04'
  who: Tamara
- line: Music happened in between, but your passion for learning seems to have always
    been there.
  sec: 703
  time: '11:43'
  who: Alexey
- line: Yes. I went to music school when I was young, which was a way to reconnect
    with my early passions. Eventually, I returned to study cognitive systems—a program
    that combined cognitive science, computational linguistics, and machine learning.
    It also included modules on knowledge and reasoning, which made it a perfect fit
    for me.
  sec: 710
  time: '11:50'
  who: Tamara
- line: I first contacted the program in 2014, but it took six years before I could
    enroll. It was a dream come true, and I’m so glad I finally got to pursue it.
  sec: 710
  time: '11:50'
  who: Tamara
- line: Are you still involved in music or music tech?
  sec: 755
  time: '12:35'
  who: Alexey
- line: I still have Ableton Live on my computer and occasionally play around with
    it. However, I’ve never been one to share or post my music. As a teenager, I used
    to DJ at parties and enjoyed that lifestyle, but now it’s just a personal hobby.
  sec: 761
  time: '12:41'
  who: Tamara
- line: So no techno sets at Berghain?
  sec: 784
  time: '13:04'
  who: Alexey
- line: No, that would require full-time dedication.
  sec: 789
  time: '13:09'
  who: Tamara
- line: It seems like a full-time commitment, especially since club events happen
    at night.
  sec: 795
  time: '13:15'
  who: Alexey
- line: Exactly. The music industry is tough.
  sec: 803
  time: '13:23'
  who: Tamara
- line: What is a sociotechnical approach to modeling language?
  sec: 824
  time: '13:44'
  who: Alexey
- line: A sociotechnical approach examines both the social impact of technology and
    how social contexts are interwoven into the technology we create. It’s a broad
    area of academic study, but at its core, it’s about understanding the interplay
    between technology and society.
  sec: 834
  time: '13:54'
  who: Tamara
- line: For example, we can analyze how deploying technology affects society and also
    how societal norms and biases influence the design of that technology. This perspective
    helps us avoid traps like solutionism and encourages us to think critically about
    the context in which our technologies operate.
  sec: 834
  time: '13:54'
  who: Tamara
- header: Exploring fairness in AI and its impact on society
- line: That sounds quite abstract. Can we narrow it down to AI?
  sec: 892
  time: '14:52'
  who: Alexey
- line: Yes, let’s take AI as an example. Consider tools like Fairlearn, which assess
    fairness in AI models. One real-world application involves credit loan decisions.
    These decisions are often based on models trained on historical data, which can
    carry biases.
  sec: 910
  time: '15:10'
  who: Tamara
- line: For instance, a study conducted by Fairlearn, Ernst & Young, and Microsoft
    analyzed 300,000 data points. It revealed that the model performed differently
    for male and female applicants, highlighting biases in the training data. This
    kind of evaluation helps us identify and address disparities, such as denying
    loans to eligible individuals or approving loans for those unlikely to repay them.
    Both outcomes can have significant consequences.
  sec: 910
  time: '15:10'
  who: Tamara
- line: It’s interesting that giving someone a loan they can’t repay isn’t just bad
    for the bank but also for the individual.
  sec: 1094
  time: '18:14'
  who: Alexey
- line: Exactly. It can lead to severe consequences like debt, repossessions, and
    job losses. This example highlights how fairness is complex and context-dependent.
  sec: 1103
  time: '18:23'
  who: Tamara
- line: Fairlearn focuses on group fairness, examining how algorithms impact sensitive
    groups. However, fairness requires defining the problem, identifying affected
    groups, and interpreting results within a specific context. It’s not a one-size-fits-all
    solution.
  sec: 1103
  time: '18:23'
  who: Tamara
- line: Why do we need this? For example, in hiring, it’s often better to miss a good
    candidate than to hire a bad one. How does this relate to fairness?
  sec: 1196
  time: '19:56'
  who: Alexey
- line: Prediction is higher or not higher.
  sec: 1221
  time: '20:21'
  who: Tamara
- line: Prediction is higher, and if it's a false negative, then it's good to avoid
    hiring someone bad.
  sec: 1225
  time: '20:25'
  who: Alexey
- line: Right, because hiring someone bad isn't good for the company.
  sec: 1231
  time: '20:31'
  who: Tamara
- line: Exactly. If we hire someone who turns out to be a bad fit, it's difficult
    to manage the consequences later. So, it's often better to be more cautious and
    risk not hiring good candidates than to accidentally hire someone unsuitable.
    The same applies to credit scoring. It’s better to deny a loan to someone who
    could potentially repay than to give a loan to someone who won’t be able to pay
    it back.
  sec: 1233
  time: '20:33'
  who: Alexey
- line: Why should we even care about fairness in these scenarios? If we’re running
    a business, shouldn’t we focus on maximizing our success as a company?
  sec: 1233
  time: '20:33'
  who: Alexey
- header: Fairness in AI models
- line: That’s a provocative question. Let me think about it.
  sec: 1280
  time: '21:20'
  who: Tamara
- line: I mean, why does fairness come into play? At the end of the day, I just want
    to optimize revenue.
  sec: 1285
  time: '21:25'
  who: Alexey
- line: I understand, but fairness is tied to values. For example, I once heard a
    presentation by Hilde, an assistant professor in the Netherlands. She talked about
    how we sometimes create models that reflect the values we want to see, even if
    those values aren't explicitly present in the data.
  sec: 1291
  time: '21:31'
  who: Tamara
- line: Maximizing revenue shouldn’t come at the cost of societal harm. Our products
    don’t exist in isolation. We have a responsibility to society. If we analyze problems
    beyond just technical aspects and consider their societal impact, we might find
    balanced solutions.
  sec: 1291
  time: '21:31'
  who: Tamara
- line: For example, Fairlearn provides tools to evaluate fairness. One approach is
    to assess a model's performance across multiple groups rather than using a single
    metric. This lets you visualize disparities and make decisions based on what the
    model is doing. If imbalances exist, you can mitigate them through post-processing
    or by retraining the model with techniques like exponentiated gradient algorithms.
  sec: 1291
  time: '21:31'
  who: Tamara
- line: These tools help align models with the kind of world we want to create, minimizing
    harm while maintaining performance. The key is to approach these problems with
    curiosity and care. There are often solutions that work for both business goals
    and societal values.
  sec: 1291
  time: '21:31'
  who: Tamara
- line: Okay, so what exactly does Fairlearn, or similar tools, provide? Let’s take
    credit scoring as an example. Say we have a model, like a decision tree or logistic
    regression, that predicts loan decisions. Fairlearn then analyzes how the model
    performs across different groups, right?
  sec: 1444
  time: '24:04'
  who: Alexey
- line: Exactly. You’d identify sensitive groups to evaluate the model’s fairness.
  sec: 1487
  time: '24:47'
  who: Tamara
- line: Right. For example, if someone belongs to a low-income group, the model might
    predict they’re less likely to repay a loan. That’s a natural pattern we might
    want the model to detect. But for features like gender or other sensitive attributes,
    we don’t want those patterns influencing decisions.
  sec: 1492
  time: '24:52'
  who: Alexey
- line: That’s a crucial point. Determining which groups to protect depends on the
    domain and potential harms. It’s not a one-size-fits-all solution. You need to
    explore the data and assess it case by case.
  sec: 1537
  time: '25:37'
  who: Tamara
- header: Automating fairness analysis in models
- line: Could we automate this? For instance, include all features in the model and
    let Fairlearn flag problematic ones? Then we could decide whether to exclude or
    keep them.
  sec: 1581
  time: '26:21'
  who: Alexey
- line: In theory, yes. You could evaluate the model against all features and identify
    disparities. But interpreting the results still requires human judgment.
  sec: 1603
  time: '26:43'
  who: Tamara
- line: For example, you can use Fairlearn to visualize false positives and false
    negatives across groups and assess the associated harms. However, the decision
    on which features to mitigate or exclude depends on context. It’s not something
    an algorithm can fully automate because these decisions are rooted in societal
    implications. That’s why fairness is inherently socio-technical—it’s about balancing
    technical solutions with societal values.
  sec: 1603
  time: '26:43'
  who: Tamara
- line: That makes sense. So, at the end of the day, a human expert—someone who understands
    the domain—has to evaluate the harm caused by false positives or false negatives
    and decide how to address it.
  sec: 1732
  time: '28:52'
  who: Alexey
- line: Exactly. False positives and false negatives matter differently in different
    scenarios. There are also other metrics, like demographic parity, that might be
    relevant depending on the use case.
  sec: 1776
  time: '29:36'
  who: Tamara
- line: Ultimately, you can’t rely solely on technical solutions. Fairness requires
    understanding the real-world context and making informed decisions. Socio-technical
    systems are created by people, for people, and must account for this complexity.
  sec: 1776
  time: '29:36'
  who: Tamara
- line: So, who should handle this? For example, if we talk about hiring models, I
    heard Amazon used one but later stopped because of bias issues.
  sec: 1840
  time: '30:40'
  who: Alexey
- line: Yes, I’ve heard similar stories.
  sec: 1860
  time: '31:00'
  who: Tamara
- line: Right, and it seems like these issues are still prevalent in areas like loan
    decisions, which are widely used in the industry.
  sec: 1863
  time: '31:03'
  who: Alexey
- line: It is used a lot, I think. I'll check.
  sec: 1888
  time: '31:28'
  who: Tamara
- line: I wanted to ask, who is responsible for making this assessment? For example,
    if a false positive is harmful and a false negative is not, who decides this?
  sec: 1893
  time: '31:33'
  who: Alexey
- line: Well, the team creating this should make the decision.
  sec: 1904
  time: '31:44'
  who: Tamara
- line: But how should I, as a data scientist, make that call?
  sec: 1911
  time: '31:51'
  who: Alexey
- line: That's also my concern. I spoke with someone recently who mentioned feeling
    frozen and reluctant to even approach the topic of responsible AI or use the tools,
    due to fear of making the wrong decision. It’s overwhelming. But I think, as domain
    experts, we should understand the impact of our products on others.
  sec: 1914
  time: '31:54'
  who: Tamara
- header: Balancing technical and domain expertise in decision-making
- line: But, let's say I'm a technical person, and I'm not necessarily a domain expert.
    I’m a data scientist, for example. I learned to use support vector machines, but
    I didn’t study sociology. But at the same time, I’m wondering if that means I
    should shift my responsibility to someone else.
  sec: 1952
  time: '32:32'
  who: Alexey
- line: In bigger companies, they might have people who assess this. I've never worked
    in a big company, but I would love some insight. In smaller places, people’s curiosity
    drives them to ask questions. The tools I’m talking about—like equal odds or demographic
    parity—don’t require Fairlearn to use. These are techniques that can be implemented
    in your own notebook. The advantage of tools like Fairlearn is that they provide
    education and help with thinking about the problem. We’re focusing on improving
    learning objectives and educational materials in the coming months, and we hope
    others will contribute as well. Teaching is one of the best ways to learn.
  sec: 1991
  time: '33:11'
  who: Tamara
- line: As a data scientist, you might feel overwhelmed by the decisions you need
    to make, wondering whether you’re making the right call or doing more harm. But
    by reviewing basic problem definitions and theory, you can start framing the issue.
    There’s a framework to approach these things, but it’s not perfect. None of this
    can be perfect. As machine learning practitioners, we can never fully model the
    real world, so there’s always an irreducible error. And we can’t mitigate everything
    because we don’t have all the information. We have to be curious and live with
    a bit of ambiguity.
  sec: 1991
  time: '33:11'
  who: Tamara
- line: I was reflecting on my personal experience with making these decisions. I
    worked on a moderation team for an online marketplace, deciding whether an item
    should go live for purchase or be blocked. We discussed factors like the model's
    performance, and worked with product managers and fraud experts. We reviewed cases
    and discussed whether the model made the right decision, and what the consequences
    might be.
  sec: 2123
  time: '35:23'
  who: Alexey
- line: I think this aligns with the curiosity you mentioned, but as a data scientist,
    I don’t necessarily have all the domain expertise. That's why we also had fraud
    specialists and product managers. The fraud specialists understood how fraud occurs,
    and the product managers represented the users. In our team, this collaboration
    was really helpful.
  sec: 2123
  time: '35:23'
  who: Alexey
- header: The role of humans in the loop for fairness
- line: 'Yes, and you mentioned something really important: the human in the loop.
    It’s a central component of all AI systems. If we want them to be fair, we need
    humans in the loop. Before any decision can have a real impact, there has to be
    a human involved.'
  sec: 2233
  time: '37:13'
  who: Tamara
- line: In the case I was talking about, there were moderators who looked at the model’s
    output and made the final decision.
  sec: 2254
  time: '37:34'
  who: Alexey
- line: Exactly. That’s already a significant step.
  sec: 2263
  time: '37:43'
  who: Tamara
- line: While you were talking, I got a notification, and I thought, this is a good
    example. We were talking about music and how panels and consoles can be detached
    from a computer to avoid distractions. It’s easy to get distracted by technology,
    as happened to me just now.
  sec: 2267
  time: '37:47'
  who: Alexey
- line: Yes, and if you want to create music—or any art—you really need to be immersed
    in it. The best work happens when you’re fully engaged, like when you’re programming.
    You can work for hours without noticing time passing, without even taking breaks
    for food or water. That’s when you’re doing your best work.
  sec: 2298
  time: '38:18'
  who: Tamara
- line: That hasn’t happened to me in quite some time.
  sec: 2316
  time: '38:36'
  who: Alexey
- line: I think you have a very multidisciplinary job now, and there’s beauty in that.
    It’s a different kind of flow, working with people. I used to call it the high
    of joint work.
  sec: 2319
  time: '38:39'
  who: Tamara
- line: Yes, when I was just a data scientist, before I had any meetings, I could
    show up in the morning, open my laptop, and work. By the time I looked up, it
    was already evening. That was really great.
  sec: 2335
  time: '38:55'
  who: Alexey
- line: That’s the flow state. But we are also tied to our computers.
  sec: 2352
  time: '39:12'
  who: Tamara
- line: So, how did you get involved in the project? Last time we spoke, Probable
    didn’t exist yet. How did it happen? You were doing LPiano back then, right?
  sec: 2358
  time: '39:18'
  who: Alexey
- line: Yes, I was still working on it. It wasn’t a huge shift from music tech to
    AI, but it was a transition. I’d say it felt natural, but it was still a change.
  sec: 2377
  time: '39:37'
  who: Tamara
- line: So, how did it all happen? How did you end up working with Fairlearn at Probable?
  sec: 2378
  time: '39:38'
  who: Alexey
- header: Joining Probable and working on open-source projects
- line: I joined Probable in 2023, during the summer, though it was quite informal
    at first. I attended a meetup in Berlin, a Psyched Learning contributor meetup,
    just for fun. There, I met the founders of the company. I started working on something
    that was really interesting, made a few pull requests, and they were merged. That
    was the start of it. Around the end of last year or the beginning of this year,
    I was still doing research with a group focused on semantic alignment. I kept
    that going until April this year while contributing to open source on the side.
    Programming is something I never wanted to forget, even if academic research doesn’t
    always involve coding.
  sec: 2402
  time: '40:02'
  who: Tamara
- line: My first internship was with Google Summer of Code in 2010, and that was a
    long time ago. Open source was always a way for me to have fun, and I stayed in
    touch with the Probable team. When they started building the company, they invited
    me to apply.
  sec: 2402
  time: '40:02'
  who: Tamara
- line: At the time, they were building the open source software engineering team.
    I’m not sure if all titles are the same, but I believe we’re all called open-source
    software engineers. The team was focused on different areas, and my role was to
    work on explainability and language models, which I had experience with before
    it became a major topic. I knew the theory, so I was well-prepared. They needed
    someone to work on the Psyched Learn inspection package, which includes feature
    importance methods like PCA. At that time, the project was still relatively small,
    but we planned to expand it. Probable also supported various libraries compatible
    with Psyched Learn, including Fairlearn.
  sec: 2457
  time: '40:57'
  who: Tamara
- line: What is this inspection package? I don’t think I’ve heard of it.
  sec: 2574
  time: '42:54'
  who: Alexey
- line: It’s not very big at the moment, but it includes methods like partial dependence
    plots. There are also smaller methods, and the goal is to extend it.
  sec: 2578
  time: '42:58'
  who: Tamara
- line: I don’t remember seeing this inspection tool. Is it something new?
  sec: 2585
  time: '43:05'
  who: Alexey
- line: Yes, it might be newer. I remember using it at university, but that was a
    few years ago.
  sec: 2589
  time: '43:09'
  who: Tamara
- line: I’ve been using Psyched Learn for over 10 years.
  sec: 2619
  time: '43:39'
  who: Alexey
- line: Ah, then it’s probably a newer addition. I remember using permutation feature
    importance at university, but that was a while ago. The whole field of interpretability
    and explainability is something I’m slowly building expertise in. It’ll take some
    time.
  sec: 2631
  time: '43:51'
  who: Tamara
- line: I’m planning to focus more on Fairlearn in the next few months. Since joining
    in May, I’ve worked on several projects, including enhancing Psyched Learn’s CheckArray
    and other pull requests. Some are still being reviewed. I’ve worked on improving
    computations for the Biograph algorithms and integration with Fairlearn and Scopes.
  sec: 2640
  time: '44:00'
  who: Tamara
- line: The most interesting part of my work has been ensuring cross-library compatibility.
    This means making all Fairlearn estimators compatible with Psyched Learn, and
    ensuring compatibility as Psyched Learn transitions to version 1.6. People should
    check for compatibility issues as these updates roll out.
  sec: 2694
  time: '44:54'
  who: Tamara
- line: I just checked, and the inspection model in Psyched Learn was introduced in
    version 0.22, released in December 2019.
  sec: 2757
  time: '45:57'
  who: Alexey
- line: Yes, that sounds about right. I remember using permutation features at university,
    but I’m not sure if it was part of Psyched Learn or a different package.
  sec: 2770
  time: '46:10'
  who: Tamara
- header: Scopes library and its integration with Hugging Face
- line: Scopes is an independent library that originated from Hugging Face, though
    it’s separate now. It integrates with Hugging Face’s hub to allow you to bring
    your Psyched Learn models into production. The key benefit of Scopes is its secure
    persistence.
  sec: 2780
  time: '46:20'
  who: Tamara
- line: I’ve seen the discussion on LinkedIn, but I didn’t dive into the details.
  sec: 2831
  time: '47:11'
  who: Alexey
- line: The issue was related to downloading malware through models from Hugging Face
    and similar platforms. This was caused by the known problems with pickle, which
    can allow untrusted types to be executed when models are unpickled. Scopes addresses
    this by ensuring you have full control over which objects are loaded, preventing
    untrusted types from running.
  sec: 2836
  time: '47:16'
  who: Tamara
- line: So, SCOPS stands for PsychoOps?
  sec: 2869
  time: '47:49'
  who: Alexey
- line: I don’t remember.
  sec: 2875
  time: '47:55'
  who: Tamara
- line: Maybe it’s a way to serialize data products, right?
  sec: 2879
  time: '47:59'
  who: Alexey
- line: Exactly. I can't say the word in English—serialization. It’s hard for a Slavic
    tongue. It’s DCR, whatever. People don't understand secure serialization and deserialization.
  sec: 2883
  time: '48:03'
  who: Tamara
- line: So, Scoops and Fairlearn aren’t really related in the sense of a common theme,
    but you're still involved in both. How did that happen?
  sec: 2902
  time: '48:22'
  who: Alexey
- line: Well, how did it happen? I signed a contract for it, I guess. But I haven’t
    been that involved. We pair-programmed on a few things, adding together. So, Selen
    1.6 introduces API-breaking changes and some other things. People will know in
    the next few days, so they should really check out the compatibility guides. The
    biggest work I did was making Scopeyearn 1.6 compatible, which involved a lot
    of smaller changes. Many of these changes spilled over to Scikit-learn, and then
    they had to be fixed. We had to integrate those fixes multiple times. All this
    compatibility work, I also did with Fairlearn. I got to know a lot of Scikit-learn’s
    internals, especially how the estimators are written and how they should be written.
    I’ll be giving a talk about creating custom estimators in January in Berlin.
  sec: 2917
  time: '48:37'
  who: Tamara
- line: Which meetup is that?
  sec: 2984
  time: '49:44'
  who: Alexey
- line: Uh, PyLadies, I think. It’s exclusive to them. I don’t think our meetup landscape
    in Berlin is thriving right now. There aren’t many places.
  sec: 2985
  time: '49:45'
  who: Tamara
- line: Yeah, it’s been a while since I went to a meetup. I think the last one was
    AI Street Smart. Do you know that one?
  sec: 2999
  time: '49:59'
  who: Alexey
- line: Tamara
  sec: 2999
  time: '49:59'
  who: Alexey
- line: No, I don’t. Does it still exist?
  sec: 2999
  time: '49:59'
  who: Alexey
- line: Alexey
  sec: 2999
  time: '49:59'
  who: Alexey
- line: Yeah, I think it was about 2-3 months ago. Before that, I went to PyData.
  sec: 2999
  time: '49:59'
  who: Alexey
- line: I contacted PyData Berlin, but I never heard back about having a talk there.
    I don’t know how active people are. The pandemic kind of disrupted things, and
    they haven’t fully recovered. That’s why I love PyLadies. I’ve been a part of
    it for over 10 years, and I’m happy to speak there whenever I can.
  sec: 3022
  time: '50:22'
  who: Tamara
- header: PyLadies and community involvement
- line: Are you also one of the organizers, or just an active participant?
  sec: 3048
  time: '50:48'
  who: Alexey
- line: I’m just an active participant. When I moved to Berlin in 2013 and worked
    briefly at Startup Bootcamp, that was my first contact with the community. They
    let me give a talk back then. For me, being a PyLady was central to my move to
    Berlin. I love going back whenever I get the chance. The organizers do a great
    job and sacrifice a lot of their time. We just had a PyPi Ladies event this weekend,
    where I led a Fairlearn sprint. It was nice to see people contributing. We don’t
    have many active contributors because some people find the theory and the math
    behind it intimidating. The codebase is written in a very academic way. We’re
    going to start a big refactoring project, and I’ll replace pandas with Narwhal,
    which is exciting. We’re also refactoring the whole metric frame, so we hope more
    people will contribute. We’ve made lots of “good first issues” for PyLadies Con,
    so maybe others will be interested as well, even if they’re not PyLadies.
  sec: 3054
  time: '50:54'
  who: Tamara
- line: That’s interesting. You read my mind again. I was about to ask how someone
    can contribute to Fairlearn if they’re interested. If you live in Berlin, they
    can join the meetup, right? And there will be opportunities to contribute, as
    you just mentioned.
  sec: 3130
  time: '52:10'
  who: Alexey
- line: Yes, we will have a sprint in Berlin around February, where people can come
    and contribute. In January, I’ll be giving a talk, but people can still talk to
    me. I’m happy to hear from anyone. We have a Discord channel that I check constantly.
    People are welcome to ask questions there. We also have "good first issues" and
    other "help wanted" issues that I keep updating, so people can take those on.
  sec: 3154
  time: '52:34'
  who: Tamara
- line: Okay, so there’s a Discord channel for PyLadies, or for Fairlearn?
  sec: 3184
  time: '53:04'
  who: Alexey
- line: It’s for Fairlearn, but a lot of people from the PyLadies community are also
    there. The Discord has around 370-380 people. It’s a bit quiet, though. On the
    Fairlearn website, fairlearn.org, there’s an invite link in the top right.
  sec: 3190
  time: '53:10'
  who: Tamara
- line: Fairlearn.org.
  sec: 3208
  time: '53:28'
  who: Alexey
- line: We also have a LinkedIn page that I created recently, as we didn’t have one
    before. I’ve been posting "good first issues" there as well.
  sec: 3210
  time: '53:30'
  who: Tamara
- line: So, I can find the link on the website? If I scroll all the way down, I’ll
    see the Discord icon?
  sec: 3223
  time: '53:43'
  who: Alexey
- line: Yes.
  sec: 3227
  time: '53:47'
  who: Tamara
- line: If I click on it, it will bring me to the Discord community? Cool. And you
    said you have "good first issues" on GitHub?
  sec: 3228
  time: '53:48'
  who: Alexey
- line: Yes, there are "good first issues" and also "help wanted" issues. I’ve been
    labeling a lot of things with "help wanted." "Help wanted" is more suited for
    people who have some experience contributing and don’t need to learn GitHub workflows
    or how maintainer reviews work. There are also lots of things to contribute, like
    documentation, where people can explain things for education purposes. We also
    have statistical work for experienced statisticians. For example, there’s an issue
    about testing the statistical integrity of the methods, which would be great to
    get help on.
  sec: 3239
  time: '53:59'
  who: Tamara
- line: Right, the same ideology as Scikit-learn. It has to be time-tested.
  sec: 3341
  time: '55:41'
  who: Alexey
- line: Yes, exactly. This is why creating custom estimators makes sense. I think
    Scikit-learn had 207 estimators last time I checked. People might wonder why we
    would create a new one, but there are many cases where you might want to, or you
    might want to make a meta-estimator. Fairlearn shares the same ethos. But when
    it comes to fairness, we need to be careful about what we implement.
  sec: 3351
  time: '55:51'
  who: Tamara
- line: I just posted the link to Discord. Someone asked to share it.
  sec: 3383
  time: '56:23'
  who: Alexey
- line: It’s wonderful that people want to contribute. When I first opened the Fairlearn
    documentation, I thought, "Oh my God, all this academic jargon!" But once you
    start working with it and looking at the code, even if you don’t come from a scientific
    background, it becomes clearer. The best part is that you can use it within existing
    Scikit-learn pipelines. The main work I’ve done in the last 6 months was ensuring
    compatibility, so if it doesn’t work with your particular pipeline, just open
    an issue, and we’ll take care of it. We’re releasing a new version this week,
    so there will be new updates. I’ll be doing that tomorrow.
  sec: 3397
  time: '56:37'
  who: Tamara
- line: By the way, the final thing—when I edit the transcript with ChatGPT, GPT sometimes
    breaks the name "Fairlearn" into parts when it sees a dot. It replaces the name
    with a line break, which I find a bit funny. Do you know why that happens?
  sec: 3442
  time: '57:22'
  who: Alexey
- line: That’s funny! It’s a tokenization issue.
  sec: 3475
  time: '57:55'
  who: Tamara
- line: Yeah, it treats it as an unusual token because it has a dot at the end.
  sec: 3479
  time: '57:59'
  who: Alexey
- line: Yes, that’s an issue. You have to add it to the dictionary as a full name
    sometimes. I’ve seen that happen with my stuff too.
  sec: 3485
  time: '58:05'
  who: Tamara
- line: Okay. Well, that’s all we have time for today. Tamara, thanks a lot for joining
    us and sharing your knowledge, experience, and interesting stories about music.
    It was really nice talking to you, and I’m happy we finally had this conversation.
    Thanks to everyone for joining and listening in.
  sec: 3494
  time: '58:14'
  who: Alexey
- line: Thank you. I hope everyone considers contributing, even if it’s just for less
    time-consuming issues. If you have any questions, feel free to reach out to me
    on LinkedIn. I’m happy to help anyone with questions.
  sec: 3518
  time: '58:38'
  who: Tamara
- line: And if you're in Berlin, check out the PyData meetup.
  sec: 3534
  time: '58:54'
  who: Alexey
- header: Upcoming PyData talk about custom estimators
- line: In January, right? I’ll be talking about writing custom estimators in Scikit-learn,
    but I’ll also show a custom estimator from Fairlearn, so it’s kind of related.
  sec: 3545
  time: '59:05'
  who: Tamara
- line: Alright, that’s it for today. Thanks, everyone!
  sec: 3554
  time: '59:14'
  who: Alexey
---

Links:

* [Linkedin](https://www.linkedin.com/in/tamaraatanasoska/){:target="_blank"}
* [GitHub](https://github.com/TamaraAtanasoska){:target="_blank"}