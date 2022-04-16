---
episode: 4
guests:
- stefangudmundsson
ids:
  anchor: Machine-Learning-and-Personalization-in-Healthcare---Stefan-Gudmundsson-e1h5gdg
  youtube: IDzhmmKeNG4
image: images/podcast/s08e04-machine-learning-and-personalization-in-healthcare.jpg
links:
  anchor: https://anchor.fm/datatalksclub/episodes/Machine-Learning-and-Personalization-in-Healthcare---Stefan-Gudmundsson-e1h5gdg
  apple: https://podcasts.apple.com/us/podcast/machine-learning-and-personalization-in-healthcare/id1541710331?i=1000557726819
  spotify: https://open.spotify.com/episode/3s78PtlbUmecuMOXwO8aD5?si=991e1811a5204305
  youtube: https://www.youtube.com/watch?v=IDzhmmKeNG4
season: 8
short: Machine Learning and Personalization in Healthcare
title: Machine Learning and Personalization in Healthcare
transcript:
- line: Hello, everyone. This week we'll talk about machine learning in healthcare,
    and in particular, about personalization in healthcare. We have a special guest
    today, Stefan [cross-talk] Okay. Stefan is from Iceland. At some point, he moved
    to Sweden, where he worked at King and H&M. Then he moved back to Iceland and
    joined Sidekick Health as a director of data science and AI. Welcome, Stefan.
  sec: 1
  time: 0:01
  who: Alexey
- line: Thank you.
  sec: 36
  time: 0:36
  who: Stefan
- header: Stefan’s background
- line: Before we go into our main topic of machine learning in healthcare and personalization
    in healthcare, let's start with your background. Can you tell us about your career
    journey so far?
  sec: 38
  time: 0:38
  who: Alexey
- line: Yes, absolutely. I think I better shorten it a little bit. I think I had my
    first job at the age of 12, in the last century. So I'll just do very short snapshots
    of the early career and then focus on the more relevant stuff. I started working
    as a developer, rather young – like 18. It was a part time job when I was in high
    school. That was in ‘96. In ‘99, I was given the task of building my first data
    pipeline for the notorious Y2K problem – that was very interesting. [laughs]
  sec: 50
  time: 0:50
  who: Stefan
- line: Most of my early developing work was around building programs that could control
    the graphics in TV programs, like live sports shows, election programs, and things
    like that. Today, I still think I've written most of my lines in a programming
    language called Delphi that nobody uses anymore.
  sec: 50
  time: 0:50
  who: Stefan
- line: Delphi - that was my first language!
  sec: 118
  time: '1:58'
  who: Alexey
- line: Oh, really? [laughs] It’s a very nice language.
  sec: 120
  time: '2:00'
  who: Stefan
- line: Yeah, it's a nice one. Nobody cares about it anymore. But it was a nice one.
  sec: 125
  time: '2:05'
  who: Alexey
- line: I think C Sharp took over at some point. In 2006 and 2007, I had a great experience
    where I was building an enterprise data warehouse from scratch with a great team
    at the largest telecom company in Iceland. That experience has helped me a lot
    in my current and recent jobs. But if I fast forward over these snapshots, and
    start being more current, and I think I'll start in 2015 – where I made a very
    good decision, but a difficult one. I left a very nice and cozy job as director
    of analytics and modeling in one of the three major banks in Iceland and moved
    with my family to Stockholm, where I joined King, the makers of Candy Crush.
  sec: 128
  time: '2:08'
  who: Stefan
- line: That was a great experience. Most of the time there, I spent building the
    AI team, and the AI research part of that team as well, where we did a lot of
    collaboration with universities and supervised quite a few Master's students.
    We were building some nice products – some failed, some were successful. Maybe
    we will discuss that a little bit later. In 2019, I decided to move over to H&M,
    still in Stockholm. They were in the very early phase of building up a machine
    learning function – machine learning team. As you can imagine, it’s one of the
    biggest retailers in the world with awesome data – where images, text recognition,
    and all of these things come together.
  sec: 128
  time: '2:08'
  who: Stefan
- line: I learned a lot there and we were just focusing a lot on “Okay, what's the
    best team structure? How do we build? What are the best practices in solving all
    of these problems?” That was the early part of that job. When we got more people
    in, I moved more into a similar path as I had been doing at King before – research
    collaboration with universities, Master’s students, and sort of trying to be the
    translator between the state-of-the-art and academia. Meaning between people that
    were only focusing on the latest methods and then the business people that are
    only focusing on money and don't care about the methods. [laughs]
  sec: 128
  time: '2:08'
  who: Stefan
- line: So you're trying to sort of merge these two and then be in-between that to
    create some value out of collaboration. In late 2020, I was offered this position
    at Sidekick Health – a startup/scale-up with a main office in Iceland. But we
    have offices both in Boston and Iceland and Stockholm. The job there was basically
    to build up the data science and AI team in the company and to contribute to making
    what I hope will become a fantastic data-driven company with machine learning
    solutions and digital therapeutics solutions. So that's something I had to basically
    jump on and started there in early 2021.
  sec: 128
  time: '2:08'
  who: Stefan
- line: This is completely off topic, but I can't help but ask you – how are Icelandic
    and Swedish different? Are they very different languages or are they similar?
  sec: 323
  time: '5:23'
  who: Alexey
- line: '[laughs] I sometimes explain this as sort of – 1000 years ago, it was the
    same language and then Sweden and Denmark and Norway decided to evolve, but we
    did not. So we can still read the Icelandic sagas from 1200-something. Yeah, I
    think that''s the main difference. We still have more inflections, more nuances
    that usually evolve out of languages. [laughs]'
  sec: 334
  time: '5:34'
  who: Stefan
- line: True Vikings, right?
  sec: 361
  time: '6:01'
  who: Alexey
- line: '[laughs] I don''t know about that.'
  sec: 365
  time: '6:05'
  who: Stefan
- header: Applications of machine learning in healthcare
- line: '[laughs] Okay. Coming back to our main topic of machine learning in healthcare
    – Usually, when I hear machine learning in healthcare (in general, in healthcare)
    I think about clinical trials. But when people talk about machine learning in
    particular then I imagine X-ray images or some images and then people would run
    deep learning on top of these images. So I think it’s mostly about processing
    medical images. Is this correct? Or are there more applications of machine learning
    in healthcare?'
  sec: 367
  time: '6:07'
  who: Alexey
- line: There are, of course. With myself, this is also what comes to mind first –
    a typical vision you have is that there's an X-ray of some broken arm or whatnot
    and then you have deep learning image recognition to tell you “Okay, this is wrong,
    do this.” That is a use case, of course, but there are many more. To name a few,
    there’s disease diagnosis where you really maybe have symptoms and measurements
    but it's not obvious what disease it is – so it would be trying to automatically
    distinguish or recognize that.
  sec: 401
  time: '6:41'
  who: Stefan
- line: There's a lot of work in, of course, through the pharmacy companies and things
    related to that – drug discovery. What kind of drugs can you have? Are they related?
    Can they be tailored to your team settings or something like that? I think we've
    all probably heard about DeepMind and AlphaFold, where they are trying to predict
    the folding of proteins, which can turn out to be a very big game changer to understand
    the biology behind all of this.
  sec: 401
  time: '6:41'
  who: Stefan
- line: Then you can move into more personalized medicine, where you get different
    drugs and slightly different treatments, for example, for your cancer treatment,
    based on your background and medical history and things like that. There are probably
    many more than I'm not mentioning, but that’s just to name a few.
  sec: 401
  time: '6:41'
  who: Stefan
- line: Do you know anything about this AlphaFold? I heard that it exists, but my
    knowledge of biology is so non-existent, that I couldn't fully appreciate it.
    I heard that there was a breakthrough in biology because of deep learning, but
    I don't know anything about biology to really appreciate this very well.
  sec: 494
  time: '8:14'
  who: Alexey
- line: I’m a little bit ashamed to say today, that when I was younger, I thought
    that biology was a little bit inferior – we didn't have enough numbers. [laughs]
    So I'm probably the same. I'm not very good with biology. But I read the paper
    on AlphaFold from DeepMind and it seems very interesting. But I'm on the same
    page as you are – I'm not an expert on this at all.
  sec: 514
  time: '8:34'
  who: Stefan
- line: So did you understand a lot in that paper or your lack of knowledge in biology
    prevented you from this?
  sec: 541
  time: '9:01'
  who: Alexey
- line: No, I think… Well, it's been some time since I read it, so I couldn't really
    quote it. But in my memory, I thought I understood. But that's probably also because
    DeepMind puts a lot of effort into making their content accessible by the public.
    So I've read and taken a much deeper dive on the earlier stuff they did on AlphaGo
    and AlphaZero. And that's very accessible or it can be.
  sec: 546
  time: '9:06'
  who: Stefan
- line: I guess the target audience of this paper are machine learning researchers,
    not biologists, right? Or maybe both?
  sec: 585
  time: '9:45'
  who: Alexey
- line: Probably both. But then, they usually get published in Nature as well. So
    that's where they are [cross-talk]
  sec: 593
  time: '9:53'
  who: Stefan
- header: Sidekick Health – gamified therapeutics
- line: So basically every scientist becomes the target audience. Before this episode,
    I was doing a little bit of research about the company where you work right now
    – Sidekick Health – and I know that this is in the healthcare domain. In my mind,
    I thought maybe you were doing these medical images like other health care companies.
  sec: 602
  time: '10:02'
  who: Alexey
- line: I went to the website, I checked the description, and it said that you're
    doing “gamified digital therapeutics built on science, rooted in behavioral economics,
    and scalable across multiple therapeutic areas”. I must admit that [laughs] most
    of these words do not tell me anything. So I'm not sure I really understood what
    you do. Maybe, can you decipher what it actually means?
  sec: 602
  time: '10:02'
  who: Alexey
- line: I can try. [laughs] No, no. It should be very simple, but you know how sometimes
    the language in web pages are sort of put in a specific custom. [laughs] Yes.
    I mean, that's another field in machine learning and AI in healthcare – in the
    treatment itself. Can we personalize the treatment more? Can we get more out of
    the treatment? We take a step back and think about the fact that we have streamlined
    healthcare in many ways, which is great. We know that when you come in to see
    a doctor, you meet them for five minutes, they diagnose you, you get a treatment
    or a medicine and you're out. There’s nothing more to be done. This is a lot of
    our experience of healthcare.
  sec: 649
  time: '10:49'
  who: Stefan
- line: Often this is just enough. But all the streamlining also means that, if you
    have multiple diseases, you're not really getting that communication. You just
    go to an expert, they treat one thing. And you're really losing the empathy, because
    it's been streamlined so much. And there are studies showing that empathy is a
    big factor and often contributes to better outcomes, or treatments, and all of
    that. So our goal is basically to maximize the quality life years of a person's
    life. That sometimes means we can try to cure a disease or help them live longer.
    It also means there are a lot of people that have chronic diseases, which they
    have to live with for decades. But just being able to educate them and help them
    take the right steps and develop their daily habits in a better way can actually
    increase their quality of life substantially. So that's what we're trying to build.
    We have more touch points with the users and patients than you do in normal healthcare
    because you have this through an app. But in the app, we’re also trying to personalize
    it so you feel better, you're better engaged.
  sec: 649
  time: '10:49'
  who: Stefan
- line: We try to personalize all the contact you get. We take into account if you
    have more than one disease and we try to merge this together in a nice way. But
    that is a huge task and, of course, a work in progress. At the same time, we're
    trying to add this gamification level on top of it, because a big factor in changing
    people gradually over time is the engagement. You need to engage and you need
    to feel excited about what you're doing. What we do there – we have a collaboration
    with a charity and we create an incentive in the app. Every time you finish a
    task that we give you, you are handed out this altruistic reward. You collect
    water drops and then you can donate the water drops to people in need of fresh
    water. Then in the background, we are collaborating with a charity that takes
    care of that. So that's the setup of this – we're trying to merge this.
  sec: 649
  time: '10:49'
  who: Stefan
- line: 'The three main factors of the people in the company are: medical doctors,
    so we have all the background and expert knowledge of the diseases, then there
    are behavioral psychologists that know everything that you should know about getting
    people to take the steps towards change and how to nudge them towards the right
    change. And then there are people like myself and more people in the company with
    a background in the gaming industry. So we''re trying to merge these three together
    to create this encasing solution that can help you improve your life.'
  sec: 649
  time: '10:49'
  who: Stefan
- line: So when you mentioned gamification and creating more engagement – since you
    worked at King. I played some games from King – like Bubble Witch for example
    – King gets people on the hook really well. So I think you really mastered that
    at King. I guess this is one of the things that is quite useful now from your
    past experience that you can apply, right?
  sec: 874
  time: '14:34'
  who: Alexey
- line: Yes, yes. But at the same time, there are critical differences. We don't want
    to keep you in the app for hours, because most of the activity you need to do
    is outside of the app. So that is a very interesting difference between the two
    use cases.
  sec: 904
  time: '15:04'
  who: Stefan
- line: Yeah. If I understood correctly, your main target audience of the app consists
    of patients, not doctors. Or is it both?
  sec: 921
  time: '15:21'
  who: Alexey
- line: No, the main target is the patients. But we are collaborating with pharmacy
    companies or insurance providers as well. Not doctors.
  sec: 930
  time: '15:30'
  who: Stefan
- line: Okay. Not doctors who take in patients every day,
  sec: 937
  time: '15:37'
  who: Alexey
- line: Not at the moment.
  sec: 942
  time: '15:42'
  who: Stefan
- line: Okay. Because I imagine that they don't really care much about gamification.
    They just have so many patients to deal with, so they probably just don't have
    time. So if I understood correctly, what you do is – let's say a person has some
    chronic disease and they need to enter these details in the app, and then the
    app will tell them, “Okay, you need to drink more water, drink less coffee, exercise
    more,” this is what my doctor tells me. [laughs]
  sec: 945
  time: '15:45'
  who: Alexey
- line: '[laughs] Yes, but there''s a little bit more than that. Today, you are given
    a specific PIN code that lets you go in and so that you enter the right program
    right away. But a big, big part of that is – take a typical diabetes patient,
    for example. A big proportion of people dealing with diabetes are dealing with
    problems that come from lack of health literacy. So just having very accessible
    content on, “Okay, you have this disease because of this. You can control it with
    this.” Just having that in a very clear way. Because speaking to a doctor can
    be difficult. As I said, they have five minutes. There is big doctor language
    and they are often very proud of that language – so you don''t understand half
    of what they say. That''s the first step – just to get closer to the people, so
    they feel “Okay, there is empathy here. You really care about me. You can speak
    to me.”'
  sec: 977
  time: '16:17'
  who: Stefan
- line: This involves educating people about “Okay, maybe your diet isn't the best.
    This is your disease. You need to think about the diet and how you rest and how
    you exercise.” But that's just the starting part. Then you need to create a program
    where you go step-by-step with behavioral psychology to nudge people towards creating
    habits. That's a non-trivial task to do. How often do you start something, have
    great hopes, and then you maybe fail? [chuckles]
  sec: 977
  time: '16:17'
  who: Stefan
- line: Every January. [laughs]
  sec: 1076
  time: '17:56'
  who: Alexey
- line: '[laughs] Every January, exactly.'
  sec: 1078
  time: '17:58'
  who: Stefan
- line: '[laughs] And then like, maybe in the first week, I''m so adamant about doing
    exercises. Then it''s winter, I don''t really want to run, maybe I''ll wait for
    summer. But then in the summer...'
  sec: 1081
  time: '18:01'
  who: Alexey
- line: A big part of that is behavioral psychology, and the goal setting is maybe
    not the best. You aim too high, or you don't have small steps to gradually push
    you towards something – you don't have someone constantly reminding you, like
    a friendly app. Or it's just, “It's okay, don't worry. Continue.” We all forget
    one day to continue. “Let's try to do 3000 steps today,” something like that.
  sec: 1093
  time: '18:13'
  who: Stefan
- header: How is working for King different from Sidekick Health?
- line: Interesting. I really want to try it now. [laughs] So we already talked a
    bit about how your previous background was useful, at King for example, where
    you knew how to attract or keep people engaged. But it also seems like it's quite
    different from your previous jobs. Right? Although now, when I think about this,
    actually, this is an app and what you were doing before it was also an app, so
    to some extent, there are some similarities. Can you maybe tell us about the differences
    between what you do now and what you were doing before as a data scientist at
    King?
  sec: 1119
  time: '18:39'
  who: Alexey
- line: Exactly. I think it's much more similar than you would think in the beginning.
    You basically have a program – some kind of solution – and you're in a company
    where you really want to create this data-driven culture from the data science
    perspective. You want decisions to be data-driven. If you're going to change features
    in the app, you want them to be backed by data. And you want some kind of machine
    learning part of it as well. So on a very high level, it's actually very similar.
    You need to create this culture, you need to build up the infrastructure, and
    have the buy-in from the business people that, “Okay, don't just shoot from the
    hip – we need to be data driven.” That's exactly the same in both places.
  sec: 1167
  time: '19:27'
  who: Stefan
- line: But as I sort of hinted earlier, there is a big, big and very interesting
    difference. Because with King, we have social media, we have gaming apps that
    are optimized for just keeping you in the app forever or whatever platform they're
    working on. They give you content, they play on your feelings. That's currently
    all the debate about Facebook that is dividing people into because it's always
    optimized to give you more and more things that you get more emotional about.
    We're not trying this. We don't care if you spend just 10 minutes a day in the
    app just reading the educational content and seeing “Okay, these are my tasks.
    I'll do them.” Then you come in again, “Okay, I'll finish this.” Something like
    that – that's fine. If you just follow the path and get better. That's the main
    difference there.
  sec: 1167
  time: '19:27'
  who: Stefan
- line: There is a main metric for you. Let's say games like Candy Crush, Bubble Witch
    – they aim at maximizing the time you spent in the app, right? Time you spend
    playing.
  sec: 1276
  time: '21:16'
  who: Alexey
- line: Or the money you spend. [laughs]
  sec: 1291
  time: '21:31'
  who: Stefan
- line: Or the money, yes. It depends on how exactly you monetize this particular
    app. But then when we talk about your application – the one you’re working on
    right now – something that comes to my mind is how often people return, like how
    many days they open the app let's say? So probably what you want to have is “people
    open the app every day,” it doesn't matter if it's five minutes or more than that.
    Is this the metric that you want to optimize? Or is there something else?
  sec: 1292
  time: '21:32'
  who: Alexey
- line: No, exactly. Creating an app is exactly this. You need to just think “Okay,
    if we can make you open the app for 10 minutes every day at three o'clock in the
    afternoon – that would be awesome for us. Then you're probably following the directions.”
    It's only a proxy, but it's probably highly correlated with you following the
    therapy or the program we give you. Plus you are gradually building up a habit.
    The building of a habit takes weeks or months, so just being able to have this
    happening repeatedly is more important than you staying in the app for hours.
    That’s much more important.
  sec: 1322
  time: '22:02'
  who: Stefan
- line: We absolutely don't want to spend time in the app when you should be out working.
    [laughs] But there is another difference also with an environment like Candy Crush
    – you are with patients in treatment. Therefore you have to be much more careful.
    If you're chasing a feature in Candy Crush, “okay, should this level be slightly
    more difficult or slightly easier than it is today?” You just do it and see what
    happens. [chuckles]
  sec: 1322
  time: '22:02'
  who: Stefan
- line: You do an A/B test, right?
  sec: 1389
  time: '23:09'
  who: Alexey
- line: Yes. But in healthcare, you really need to be careful about “Okay, let's make
    sure that this is okay and that we're not jeopardizing anyone's health.”
  sec: 1390
  time: '23:10'
  who: Stefan
- line: The experiment in this scenario could be “Let's ask people to, instead of
    walking 3000 steps per day, let's ask them to walk 4000 steps and then we see
    if it changes the habit.” Right?
  sec: 1401
  time: '23:21'
  who: Alexey
- line: Exactly. That's why companies like King and games like Candy Crush and social
    media are so good at retaining you – they are constantly experimenting and doing
    A/B tests, giving the audience two or three different versions and then you pick
    a winner to that. Then you could actually build up to a better, more engaging
    solution. We are definitely doing A/B testing a lot, but the metric that we're
    optimizing for is not necessarily the click through rate or time spent.
  sec: 1415
  time: '23:35'
  who: Stefan
- line: Have you ever used Duolingo?
  sec: 1452
  time: '24:12'
  who: Alexey
- line: Yes.
  sec: 1454
  time: '24:14'
  who: Stefan
- header: The rewards systems in gamified apps
- line: Yeah. For those who haven't, this is a tool (an app) for learning languages
    that has gamification inside to keep you motivated to learn. My wife is actually
    using it to learn French right now. I can see that they did quite a good job of
    keeping people engaged and making sure that they come back.
  sec: 1455
  time: '24:15'
  who: Alexey
- line: The question we have from Gregoire is, “I’m wondering how difficult it is
    to enforce such behavior that you can push using approaches like Duolingo by adding
    gamification. Do you get help?”
  sec: 1455
  time: '24:15'
  who: Alexey
- line: Yes. We do a lot of user research, of course, where we interview people afterwards
    and ask them “What is working? What is not working? What needs improvement?” And
    people are generally very happy with the reward system. Probably the strongest
    part is the empathy and the companionship you feel with it. [cross-talk]
  sec: 1505
  time: '25:05'
  who: Stefan
- line: We talked about the reward system, right? Maybe you can also say a few words
    about what kind of reward people get for something like walking 4000 steps?
  sec: 1533
  time: '25:33'
  who: Alexey
- line: Yes. We give them a task every day according to a program. Every time they
    finish a task, they collect water drops, at the moment.
  sec: 1543
  time: '25:43'
  who: Stefan
- line: Ah, right. We did talk about that.
  sec: 1551
  time: '25:51'
  who: Alexey
- line: That can be extended if you're looking into something like – maybe we want
    to offer them, through different kinds of charity collaboration, different kinds
    of rewards – so it's closer to your heart. I mean, planting trees in the Amazon
    or something else, so it's more engaging, and you're more enthusiastic about,
    “Okay, I really want to do this donation.”
  sec: 1555
  time: '25:55'
  who: Stefan
- line: In Duolingo, the reward system that they have is just made out of thin air,
    right?
  sec: 1581
  time: '26:21'
  who: Alexey
- line: Yes.
  sec: 1587
  time: '26:27'
  who: Stefan
- line: It's basically a leaderboard where you compete against people you don't know.
    And somehow it works, right?
  sec: 1588
  time: '26:28'
  who: Alexey
- line: It works. You see in many games, where you have these vanity items that people
    really respond to. We just thought that for this kind of app that we're building,
    you need a little bit more.
  sec: 1595
  time: '26:35'
  who: Stefan
- header: The importance of building a strong foundation for a data science team
- line: Can you maybe tell us about what kind of problems your team solves? Maybe
    you can also mention a few of the last projects that you worked on.
  sec: 1613
  time: '26:53'
  who: Alexey
- line: Yes. We have been putting a lot of effort into just building the foundation.
    I started a little over a year ago and then we were a much smaller company with
    just two data scientists. Nothing was in place, basically. We needed to build
    up all the foundation and infrastructure. We built data pipelines, dashboards,
    just as the first steps to make everyone data driven. I have a very (probably
    personally) strong opinion about, “Okay, we want to go into machine learning and
    personalization, but every machine learning project you start without proper analytics
    and proper data is bound to fail.”
  sec: 1622
  time: '27:02'
  who: Stefan
- line: That's why we have been putting a lot of effort into the foundation and building
    up A/B testing capabilities and things like that. That said, we have done a lot
    of that, so we are able to start and have started working on what we think are
    pretty exciting projects. Personalization is going to be a key part of this. We
    have some simple logic today, but we want to make that so much, much more advanced
    – the treatment personalization, the task we give and the modules you get at each
    given point in time is the correct one (the one you need at the moment). People
    are very different. With a chronic disease, you might want to be quite depressed,
    then we need to slow down and say “Okay, let's not put tasks that are too demanding
    on you. Let's give you content where you can do more mindfulness and things like
    that.” So we need to be very adapted to this and then just all the tasks you are
    given, “Okay, we know that people that are similar to you, who like these kinds
    of tasks.”
  sec: 1622
  time: '27:02'
  who: Stefan
- line: May I interrupt you? Sorry. I'm really curious about this slowing down approach.
    Do you have a model that says, “Okay, this user seems like he's not in a good
    mood.” You have a model that detects that?
  sec: 1746
  time: '29:06'
  who: Alexey
- line: At the moment, we have rather frequent questionnaires where you can emphasize
    how you are feeling.
  sec: 1760
  time: '29:20'
  who: Stefan
- line: Yeah. If you can solve something without machine learning, it’s better. Right?
    [laughs] Just ask the user.
  sec: 1767
  time: '29:27'
  who: Alexey
- line: Yeah, [reluctantly] I mean – you should start there. I think that should always
    be the approach – start with something simple. Then you have data and then you
    have everything in place to automate it. Don't try to automate out of thin air.
    But we also have just received a report that the activity in the app is dropping,
    and we have started and want to go much more into that direction – where you have
    your wearable, where you can measure your heart rate variability, your number
    of steps. We already have that, of course – but more and more of this.
  sec: 1773
  time: '29:33'
  who: Stefan
- header: The challenges of building an app in the healthcare industry
- line: Okay. Usually when I think of the healthcare industry, (I might be wrong.
    Don't judge me. I never worked in healthcare.) But usually when I think about
    this, it's regulated – it's quite slow. There is a lot of legacy software, a lot
    of outdated software. But what you described to me is pretty much different from
    that. Right? You realize the importance of having proper analytics data pipelines,
    having A/B tests, etc. Is it because, like you said, it’s a scale-up? It's a rather
    fresh company, right? You now realize the importance of being data driven and
    all that, right?
  sec: 1808
  time: '30:08'
  who: Alexey
- line: Usually innovation is at its best when you have experts from different fields
    coming together. Somehow the space between them – that makes it automatic. And
    I think that's what we have. We have the medical doctors and the behavioral psychologists
    that come with all of the theory and everything around the [inaudible] and psychology.
    But then you have a lot of people coming from the gaming industry, not only myself,
    but the CTO and many of the developers that developed the whole solution from
    the beginning – they all come from the gaming industry. So you have this dynamic
    there that I think is very important. The gaming industry is very data-driven
    in general. People are always testing out their hypotheses.
  sec: 1852
  time: '30:52'
  who: Stefan
- line: We have a question. I mentioned that healthcare is quite a regulated area.
    And usually in healthcare, people take questions about data privacy and this kind
    of stuff very seriously. Does it change the way you work? You have to keep these
    things in mind, like data privacy and all that? How difficult does it become that
    you need to deal with all these kinds of things?
  sec: 1901
  time: '31:41'
  who: Alexey
- line: I absolutely love that question. I think it's the other way around. I think
    all the other industries need to pick up with data privacy, and they are – gradually.
    But we have seen so many instances of data abuse. So I don't see this as a problem,
    I see this as something that’s great – I'm starting at the right end. [chuckles]
    I'm not starting with everything messed up and then gradually trying to clean
    it up. I started with just “Okay, this has to be good.” I think that's just where
    we are moving with every solution. Apple has, for example, completely changed
    their policies – your default settings were usually opt-in instead of opt-out
    and there's a huge change happening in this.
  sec: 1930
  time: '32:10'
  who: Stefan
- line: You basically need to do a lot of prior work to prepare for that. Then once
    you have a framework in place, that can take care of all these data privacy issues
    and you can move as fast as in, let's say, a traditional IT company, right?
  sec: 1980
  time: '33:00'
  who: Alexey
- line: Yes. We just make sure that we are using the best possible solutions. We also
    make sure that “Okay, there is personally identifiable data and that's very locked
    away.” But then we just de-personalize all the data and the data scientists and
    data analysts come in and they can do all of the same work as before – they just
    never see the personalized data.
  sec: 1997
  time: '33:17'
  who: Stefan
- line: There is a question from Nelson, “How do we, in general, deal with issues
    of ethics in healthcare when it comes to machine learning?”
  sec: 2024
  time: '33:44'
  who: Alexey
- line: Sorry, can you repeat that? I didn't follow.
  sec: 2034
  time: '33:54'
  who: Stefan
- header: Dealing with ethics issues
- line: Yeah. The question is, “How do we deal with issues of ethics in machine learning
    and health care?” I guess you mentioned that one of these things is making sure
    that (following Apple’s lead of opt-in instead of opt-out) we keep track of all
    personalized data and unless we really need it, we don't use it. Things like this.
    How else can we deal with all these ethical issues that come together with medical
    data?
  sec: 2036
  time: '33:56'
  who: Alexey
- line: Well, first of all, ethics means that you need people to think independently,
    because ethics is different from just “rules”. Right? I think that's an important
    fact. You need to have people that really care about this. They care about the
    patient – they’re trying to do the best for them. We can hurt them if we don’t
    do this in the best way we can.
  sec: 2066
  time: '34:26'
  who: Stefan
- line: This is the empathy you mentioned, right? You need to be empathetic.
  sec: 2096
  time: '34:56'
  who: Alexey
- line: Yes, exactly. We have, of course, rules like GDPR and HIPAA in the US – they
    are quite strict and very useful and should be used everywhere. [laughs] Of course.
    But I think you will also always need this kind of independent thinking. You're
    always going to end up on a crossroad of “Okay, am I crossing a gray line here
    or not?” Where the rules are not catching up with you. I mean, they always come
    afterwards. So I think that's needed as well.
  sec: 2100
  time: '35:00'
  who: Stefan
- header: Sidekick Health’s personalized recommendations and content
- line: Okay. I wanted to go back to what we were talking about. You said that the
    app is based on the customer profile – patient profile – it makes different recommendations,
    or personalized recommendations, based on that. Can you maybe tell us a bit more
    about that? How does this personalization work?
  sec: 2139
  time: '35:39'
  who: Alexey
- line: Yes. Again, this is, of course, a work in progress. But I think it's quite
    interesting. Think about Spotify and Netflix – there you have recommender systems
    that are always giving you more and more content similar to what you liked before.
    You have this collaborative filtering, where you are, through some nice technique
    –matrix factorization or something more advanced – you know how people similar
    to you watch content that you haven't seen before.
  sec: 2161
  time: '36:01'
  who: Stefan
- line: But I think what we are trying to do – I sometimes explain this internally
    as – imagine Spotify, where you come in and you have a heavy metal profile. You
    listen to rock music. But Spotify has an agenda – they want you to listen to country
    music. So they're trying to nudge you towards that. First they give you occasional
    Johnny Cash songs. But after two months, you're just listening to Dolly Parton.
    [laughs] So that's kind of the recommender system that we are trying to build.
    We're trying to move you gradually towards better behavior and maybe it's not
    as difficult as making someone listen to Dolly Parton, but [chuckles] it's still
    an interesting task. It's sort of a recommender system with an agenda.
  sec: 2161
  time: '36:01'
  who: Stefan
- line: Does Spotify actually do that?
  sec: 2244
  time: '37:24'
  who: Alexey
- line: '[laughs] Do they make you listen to Dolly Parton? I don’t know. [laughs]'
  sec: 2247
  time: '37:27'
  who: Stefan
- line: '[laughs] When it comes to podcasts, I think they''re trying to make me listen
    to Joe Rogan.'
  sec: 2254
  time: '37:34'
  who: Alexey
- line: Maybe, maybe. But that's probably just coming from marketing. I don't think
    they’re doing that [cross-talk]. Or I don't know.
  sec: 2260
  time: '37:40'
  who: Stefan
- line: Maybe they have a hidden agenda there [chuckles] But this is Spotify’s podcast,
    so that's why they advertise it everywhere. Interesting. And in this case – in
    your case – country music would be better habits?
  sec: 2269
  time: '37:49'
  who: Alexey
- line: Yes, kind of. Of course, it's an analogy. So it's not a perfect analogy. I
    just thought it was funny to bring in country music. I'm not a big fan though.
    [laughs]
  sec: 2289
  time: '38:09'
  who: Stefan
- line: '[laughs] So country music is good for your health, right?'
  sec: 2300
  time: '38:20'
  who: Alexey
- line: Yeah. Okay. Now I see where the analogy is breaking. [laughs]
  sec: 2305
  time: '38:25'
  who: Stefan
- line: I'm wondering. You say you have this collaborative filtering – and in this
    case, we have the rows that are users or columns, whatever. So users are users,
    but what are the items that you're recommending? Are they articles? Are they particular
    tasks or things people need to do? Or both?
  sec: 2312
  time: '38:32'
  who: Alexey
- line: We are building up a library of content, sort of. I mean, from educational
    contents – videos explaining something – some content cards that can be read,
    and then exercises and all of these things. So we are building up this catalog.
    We will eventually have a large list of products, basically, to offer you. You
    end up with a typical recommender system from that. But then there is added flavor
    in the end.
  sec: 2333
  time: '38:53'
  who: Stefan
- line: Because I imagine if you start with recommendations of I don't know, “You
    need to do 10 push-ups per day” or something like this, then for an average person
    like me, “Okay, I know it's good for my health, but I'm not going to do that.”
    [laughs] You probably want to start slowly, and push me gradually towards listening
    to country music, rather than “Okay, like here's the country music. Listen to
    it.”
  sec: 2372
  time: '39:32'
  who: Alexey
- line: Yes, exactly. But this touches a little bit on the fact of how you approach
    machine learning. I think just jumping into complicated collaborative filtering
    is not the right way. The first step is maybe just setting an A/B test and seeing
    how two different versions of a content work. Then ask the developers to develop
    the program in such a way that you can actually show two different contents. And
    that's a key thing you need to have (can't speak English anymore, sorry) for building
    up more advanced features – just having the variant availability. So you need
    to start very simple. Then even if you have a variant that beats, on average,
    everything else, you can start there – okay, offer that to everyone. But gradually,
    you're building up knowledge and datasets that you can actually train on later.
    Instead of jumping ahead of myself and thinking that I know I have the vision
    of this awesome model, but I have to hold my horses. It’s not time for it yet.
  sec: 2397
  time: '39:57'
  who: Stefan
- header: The importance of having the right approach in A/B tests (strong analytics
    and good data)
- line: When it comes to A/B tests, it feels to me (maybe I'm wrong) but they're less
    personalized, right? You're trying to test the same piece of content – or two
    pieces of content in this case, if we're talking about an A/B test on the entire
    population or maybe on one segment of your users. But this is not the same as
    a personalized recommendation.
  sec: 2473
  time: '41:13'
  who: Alexey
- line: But it is very linked. Because if you offer everyone an A/B test to begin
    with, there are so many low hanging fruits, but you're just improving your program
    easily if you just take the winner of two in every test. But then you gradually
    reach a point where you see, “Okay, now I'm increasing this but decreasing this,”
    or “This is good for this part of the population, but not this one.” Now you're
    starting to think, “What's the difference between these groups?” And then for
    a mobile game, for example, you see, “Okay, these are the payers. These are not
    the payers.” Now, we can start to personalize.
  sec: 2492
  time: '41:32'
  who: Stefan
- line: You offer this to the payers and not to the non-payers. And then “Okay, this
    is smart. How about more segments?” And you add a few more segments. Now you have
    four or five segments. That makes sense. But it's starting to get complicated
    to maintain all of these different versions. So that's where you move into, “Okay.
    Now, I actually have a lot of training data from all of this testing. Can I just
    optimize the collaborative filtering or just clustering to begin with? Okay, and
    I'll just look at the 100 nearest neighbors of you.” That's the first approach.
    There, you will be similar to them. So I think this is important. The people gradually
    take the baby steps.
  sec: 2492
  time: '41:32'
  who: Stefan
- line: Here, the fundamentally important thing is having this platform for experimenting,
    right? If you don't have this and if you directly jump into collaborative filtering
    or something like the latest deep learning model for recommender systems without
    having that – you're moving in the dark. Right?
  sec: 2580
  time: '43:00'
  who: Alexey
- line: Yeah, exactly. In my mind, the two most important inputs into starting machine
    learning is to have strong analytics. You need to be able to analyze what is happening.
    You need to break down the A/B test and understand the data that you have. Then,
    of course, you need good data. If either of these is missing, in my experience,
    this is usually the deciding factor. If you have all of them, the machine learning
    project will go well. If you are ignoring either of them, you will probably fail.
  sec: 2601
  time: '43:21'
  who: Stefan
- line: And you fail quite late after spending many months. Right?
  sec: 2633
  time: '43:53'
  who: Alexey
- line: Exactly. [cross-talk]
  sec: 2638
  time: '43:58'
  who: Stefan
- line: That's even worse than just failing, right? Just training a model and finding
    out that it's not working on your refined data is one thing, but spending many,
    many months trying to build a model only to find out that users actually don't
    like it, that’s even worse.
  sec: 2641
  time: '44:01'
  who: Alexey
- line: Exactly. That's what you gain with taking the baby steps. You're always creating
    value. You know where you stand today – you're going from A to B – and you know
    where you want to be (approximately) and if you just jump to building that B part,
    you're doing exactly what you explained. But if you try to form a path from A
    to B that gives you the most value along the way, you will learn much faster and
    you will create value along the way too. Then you will get a much better buy-in
    from everyone around you. Because often, when you're starting a machine learning
    project, there isn't just one person doing something. You really need buy-in to
    have more resources, more computing power, and all of these things that you actually
    need.
  sec: 2656
  time: '44:16'
  who: Stefan
- line: I think companies – like gaming companies, IT, tech companies, e-commerce
    companies – have learned that it's important to have analytics, to have an experimentation
    platform and all that. But what do you think is the state in the healthcare industry?
    Do companies, or vendors, that operate in this industry also realize the importance
    of these things? Or is it a bit behind?
  sec: 2700
  time: '45:00'
  who: Alexey
- line: It depends on where you are in the industry. The old pharmacy world has been
    doing this for decades. [cross-talk] There is definitely a question for this.
    People are aware of this. I mean, all the kinds of biases that you create when
    you don't really have an A/B test, or RCT, which is some clinical trial lingo
    for it. So there's a question for all that, and they know that “Okay, if you're
    not doing perfect splits in A and B and even C, you will create biases.” There
    is a survival bias, when you're only measuring the people that actually do something
    and all the people that didn't do something, they just left your platform. I mean,
    there are so many pitfalls there. So there's definitely knowledge about this.
    I'm not knowledgeable enough, but there might be a difference between “Okay, how
    do you transform that to feature improvement?” So that's slightly different, because
    typical clinical trials are huge, they cost a terrible amount of money and they
    take years versus when you're developing an app – that's no good.
  sec: 2729
  time: '45:29'
  who: Stefan
- line: I think the general population learned about clinical trials now when COVID
    vaccinations were tested, right? Everyone was asking “Why does it take so long
    to develop a vaccine?” Because of these clinical trials. They need to test that
    this thing actually works.
  sec: 2811
  time: '46:51'
  who: Alexey
- line: “Why does it take so long?” [chuckles] It was done, of course, in record time
    – one year – when it should have taken ten.
  sec: 2827
  time: '47:07'
  who: Stefan
- line: It usually takes a lot more to actually run all these tests, right? Hopefully,
    they worked. [laughs] We'll find out soon, right?
  sec: 2836
  time: '47:16'
  who: Alexey
- line: '[laughs] We’ll find out, yes. [cross-talk]'
  sec: 2847
  time: '47:27'
  who: Stefan
- header: The importance of having domain knowledge to work as a data professional
    in the healthcare industry
- line: So if I want to work in the healthcare industry as a machine learning engineer
    or a data scientist or a data engineer, how much do I need to know about healthcare
    in general? Do I need to have MD status to work there?
  sec: 2853
  time: '47:33'
  who: Alexey
- line: I think it differs a lot between what exactly you're doing. Probably, in some
    parts of it, you really need to have domain expert knowledge. But from my experience
    in just data science, it's more important just to have the right approach. You
    come to a problem and then you know, “Okay, this is the kind of approach I need
    to have. I need to take this (as we talked about earlier) take these baby steps,
    build up the knowledge, be humble about ‘maybe my solution is wrong – maybe there's
    something wrong here and there.’” And just this way of working is probably more
    important than domain knowledge in many cases. But there are definitely some cases
    where that's probably not enough.
  sec: 2868
  time: '47:48'
  who: Stefan
- header: Making a data-driven company
- line: You mentioned that you have medical doctors who are domain experts, in your
    case, then behavioral scientists who are also domain experts, and then the engineers,
    the data scientists, who take care of the way of working, as you mentioned. Then
    what you do is basically get everyone in the same room – virtual room, I guess,
    because you're in different countries – and you figure out, “Okay, how do we use
    this knowledge from these people and put this knowledge into their way of working
    when it comes to data, building these analytical platforms, data pipelines and
    so on?” Was it difficult for you to actually learn this?
  sec: 2921
  time: '48:41'
  who: Alexey
- line: No, not at all. All of these people are very data-driven just by nature. The
    biggest challenges may be to tell a medical doctor, “Okay, now we're testing a
    feature in the app. Let's just test it.” “What?! No, no. Wait!” [laughs] When
    we do medical things, we are much more careful, but it's all about the risk involved.
    If you're testing a feature that doesn't have any risk involved, then I think
    you should take the gaming industry approach – just test it. Your gut feeling
    may be correct half of the time at best. Just test and ask the users. They will
    tell you much faster and much more accurately about what they like and what they
    don't like. So but that was a little bit of a challenge.
  sec: 2965
  time: '49:25'
  who: Stefan
- line: Also, when you're building up a question in a company, one of our main objectives
    is to build a data-driven company. And that means that you have to be quick enough
    with the answers – the business is making a decision now. But many data scientists
    sort of, – they've studied through university, “Okay, I need to be perfect in
    what I do.” And if you are, you're basically killing the objective of being data-driven.
    You need to be able to act fast, give somewhat accurate numbers, but they're not
    perfect – there's a little bit of a contradiction in that and that's also something
    that needs a lot of communication.
  sec: 2965
  time: '49:25'
  who: Stefan
- line: If we want to be data driven, we need to act fast, we need to iterate. We
    start with data pipelines that are just spaghetti code – just to get something
    out. Then you gradually make a proper pipeline out of it and everything you need.
    But if you start with “No, I want to build this in AirFlow.” There's just radio
    silence for months for the business. [laughs]
  sec: 2965
  time: '49:25'
  who: Stefan
- header: Risks for Sidekick Health
- line: Right. You mentioned risk. As I understand, for your case, the risk is not
    that high, because you're not recommending medicine. Right? You're not saying
    “You have to take these pills.”
  sec: 3088
  time: '51:28'
  who: Alexey
- line: It depends. Some parts of the problem can be very sensitive.
  sec: 3102
  time: '51:42'
  who: Stefan
- line: Okay. So there are some risks?
  sec: 3108
  time: '51:48'
  who: Alexey
- line: Yes.
  sec: 3110
  time: '51:50'
  who: Stefan
- line: You cannot recommend eating sweets to people with diabetes, right?
  sec: 3112
  time: '51:52'
  who: Alexey
- line: No, no. An example we often use to remind ourselves of this is – if you have
    heart failure problems, it's not good to drink too much water, because your lungs
    cannot process all of that, so you end up with liquid in your lungs. But in most
    other programs, it's good to drink more water. We could not just create an A/B
    test “Let's suggest 10 glasses of water.” We always need to have this discussion
    with the medical doctors to see, “Okay, we want to test this. Does it make sense?
    Is it safe?” And when it's safe, we can be very agile about it. When it's not
    safe, we need to be much more careful.
  sec: 3115
  time: '51:55'
  who: Stefan
- line: Yeah, makes sense. Makes total sense. But you don't recommend medicine, right?
    It's more about lifestyle rather than taking a certain kind of pills?
  sec: 3159
  time: '52:39'
  who: Alexey
- line: Well, we are collaborating with pharmacy companies, but then there is a specific
    medicine that they have been prescribed from a doctor before.
  sec: 3170
  time: '52:50'
  who: Stefan
- line: So you still need to go to a doctor and then say, “Okay, this app recommended
    me to take a pill.”
  sec: 3179
  time: '52:59'
  who: Alexey
- line: Yes, we can [cross-talk]
  sec: 3183
  time: '53:03'
  who: Stefan
- line: Sometimes it's annoying. I know I need to have this medicine – I just need
    to go to the doctor and all the doctor does is give me a prescription.
  sec: 3188
  time: '53:08'
  who: Alexey
- line: '[laughs] Yes, a lot of legal processes also.'
  sec: 3198
  time: '53:18'
  who: Stefan
- header: Sidekick Health growth strategy
- line: Yeah, but it’s better this way rather than just going to the pharmacy by doing
    self-diagnosis and buying something that can cause more harm than good. I've heard
    you're hiring. Can you tell us more about that?
  sec: 3201
  time: '53:21'
  who: Alexey
- line: Yes, we've been growing very rapidly. When I started, we were maybe 13-something.
    I think we're 130-40 today and we'll probably be 250 by the end of the year. And
    we are rapidly growing the data science and AI team. We are about 10 at the moment
    – I think we will double in size at the end of the year. That's counting everyone
    – all the data engineers, all the machine learning engineers, data analysts, data
    scientists – everyone included there. So yes, we are looking for good people.
    We know that this is a domain where there’s fierce competition. We are fully aware
    that we need to build a world-class solution. There is no middle ground. Either
    you're a top-class app or you’re dead. There's nothing in between. So we need
    to hire great people for that.
  sec: 3219
  time: '53:39'
  who: Stefan
- line: You're hiring in Germany, in Sweden and in Iceland. Right?
  sec: 3279
  time: '54:39'
  who: Alexey
- line: Yes, that's the focus now. So as I said, we have offices in these countries
    but also in Boston, but we're focusing our efforts in and mostly Berlin and Stockholm
    and also in Reykjavík. As you might know, there are fewer people in Iceland than
    most other countries.
  sec: 3283
  time: '54:43'
  who: Stefan
- header: Using AI to help people live better lives
- line: You're the first guest we had from Iceland. Not that many people – I don't
    think I know anyone apart from you. [laughs] I noticed that we have a question
    from Slido. The question is (I don't know if you know about this) “What are your
    thoughts on brain/computer interfaces like Neuralink?” Do you know anything about
    this?
  sec: 3303
  time: '55:03'
  who: Alexey
- line: I don't know enough to say anything intelligent about that, I'm afraid. [laughs]
    Sorry about that.
  sec: 3331
  time: '55:31'
  who: Stefan
- line: Do you think AI could be used to treat or cure psychiatric disorders like
    bipolar disorders?
  sec: 3342
  time: '55:42'
  who: Alexey
- line: That's a very interesting question. Of course, I'm not sure. But it could
    probably help, at least. A disease like bipolar disease, you're affected a lot
    by just “Okay, now there's more brightness. Now there's more darkness.” You get
    more swings. So if you can predict that and know about that in advance, for example,
    if you could monitor the heart rate variability or something like that. This is
    an indication that you're going too high – it's been rising or increasing over
    the past week. Yeah, it could definitely help. But cure is a different thing,
    probably.
  sec: 3353
  time: '55:53'
  who: Stefan
- line: More like learning how to live better? Like you said, with chronic diseases
    it's all about learning – educating people how to lead a better life with these
    diseases. And this is what you do, right? You educate people how to form habits
    such that they can lead a better life? Okay, I think on that note, we can wrap
    up, maybe? Is there anything that you want to mention before we finish?
  sec: 3404
  time: '56:44'
  who: Alexey
- line: No, I can't really think of anything. Just thanks a lot for the talk. It was
    very nice to talk to you. And it's always nice to talk about this kind of subject.
  sec: 3438
  time: '57:18'
  who: Stefan
- line: If somebody has questions, what's the best way to reach out? LinkedIn?
  sec: 3449
  time: '57:29'
  who: Alexey
- line: Yes.
  sec: 3455
  time: '57:35'
  who: Stefan
- line: Okay, then that's all for me. Thanks again for joining us today, for sharing
    your expertise with us. And thanks, everyone, for joining us as well. Thanks for
    asking questions. And have a great weekend!
  sec: 3456
  time: '57:36'
  who: Alexey
- line: Yep. Bye guys. Thanks. Bye-bye.
  sec: 3469
  time: '57:49'
  who: Stefan
---

Links:

* [LinkedIn](https://www.linkedin.com/in/stefanfreyrgudmundsson/){:target="_blank"}
* [Job listings](https://sidekickhealth.bamboohr.com/jobs/){:target="_blank"}