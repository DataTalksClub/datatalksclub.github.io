---
title: Build MLOps-Ready Data Teams & White-Box Dynamic Pricing for Startups
short: Building a Data Science Team
guests:
- dattran
image: images/podcast/s01e03-building-ds-team.jpg
season: 1
episode: 3
ids:
  youtube: ScDIB-3O77A
  anchor: Building-a-Data-Science-Team---Dat-Tran-enlmef
links:
  youtube: https://www.youtube.com/watch?v=ScDIB-3O77A
  anchor: https://anchor.fm/datatalksclub/episodes/Building-a-Data-Science-Team---Dat-Tran-enlmef
  spotify: https://open.spotify.com/episode/0daFpY1z2J4Uop1XdMNsnY
  apple: https://podcasts.apple.com/us/podcast/building-a-data-science-team-dat-tran/id1541710331?i=1000502061864
intro: In this episode, Dat Tran, Partner and CTO at DATANOMIQ, shares his journey
  from economics and gaming to leading AI and data science teams at companies like
  idealo and Axel Springer. He discusses how to scale AI from prototype to production,
  build strong product cultures, and balance generalists vs. specialists when hiring.
  Drawing on his experience founding Priceloop, Dat dives into MLOps in production,
  open-source collaboration, explainable AI, and how to retain top talent in competitive
  markets. Packed with lessons on leadership, data strategy, and sustainable AI systems,
  this episode is a must-listen for data professionals aiming to build real impact
  with machine learning.
transcript:
- header: Intro
- line: Today we have pleasure to have Dat as a guest. Dat needs no introduction.
    If you have a LinkedIn account, you probably already know him. If you don't have
    a LinkedIn account, Dat has a lot of experience in building data teams, and this
    will be the topic today. So he led a team at Idealo. This is a popular price comparison
    tool in Germany. Then he was a head of AI at Axel Springer. This is a big publication
    house. And now he is the CTO and co-founder of Priceloop. So thank you Dat for
    coming to the show today.
  sec: 126
  time: '2:06'
  who: Alexey
- line: Yeah, thanks for having me, Alexey
  sec: 173
  time: '2:53'
  who: Dat
- header: 'Career Path: Economics, Gaming, and Early Coding Skills'
- line: Yes, we'll start with your background. So can you please tell us how you started
    your career? How did you get into machine learning? And how this all led to becoming
    a CTO of your own startup?
  sec: 177
  time: '2:57'
  who: Alexey
- line: Yes, sure. I would say, my career is not very straightforward. I didn't study
    computer science which would probably naturally grow into the area of machine
    learning. I actually studied business — I studied economics at Humboldt University
    and I was more into investment banking.
  sec: 192
  time: '3:12'
  who: Dat
- line: But since I was a child, I was a lot into gaming, and due to gaming, I also
    got into coding. I started to do coding very early. I think I was 12 or 13, I'd
    create my first HTML websites. I did my own forum and other stuff, and then over
    the time, I got into more of these areas and then I learned to program as well.
  sec: 222
  time: '3:42'
  who: Dat
- line: 'While I was in investment banking, I solved a lot of problems with coding
    and programming. It''s like monkey business: you have to copy paste, you sit into
    2 or 3am. And you copy and paste things. Where I just wrote a simple VBA script
    on Excel, which solved my problem within two minutes where my peers were working
    for three to four hours. And I was thinking, “Okay, maybe I should do something
    with software engineering,”'
  sec: 263
  time: '4:23'
  who: Dat
- line: It was well paid, but it's really a monkey business. Then I went back to my
    graduate studies I majored in, in operation research and econometrics. Then a
    friend of mine, he was studying statistics in Munich. And he told me, “Hey, well,
    there’s this cool course – machine learning. You should do it”. I think a lot
    of people did that course at that time.
  sec: 297
  time: '4:57'
  who: Dat
- line: I think it was six years ago, something – six or seven years ago, I did that
    course that was like, “Oh, yeah, that sounds interesting what he's doing.” And
    a lot of the stuff that he said in the course, is something that I already did
    at university, but it was presented differently. Because now he called supervised
    learning for linear regression problems. So I was like, “Okay, so I know some
    of this stuff.” And now I have a little bit of machine learning context, but also
    – how you would actually apply it in the real world — for the business world.
    Because while you're studying just the concepts, you learn theorems. And you don't
    know how to use it in real life.
  sec: 328
  time: '5:28'
  who: Dat
- line: At the end, I had to decide, “Okay, where do I want to go?” Should I do a
    PhD or go to the industry? Luckily, at the time, Accenture was having a new team
    called Advanced Analytics. Then I decided, “Okay, I should apply there, because
    it's a new team”. There I was not doing a lot of data science or something like
    that. It was simple statistics, but six or seven years ago everyone was into big
    data.
  sec: 373
  time: '6:13'
  who: Dat
- line: So you had to learn Spark. In Spark, they had simple stuff like linear regression,
    and logistic regression. But that was not my biggest interest, because I knew
    at the time that big data was just very difficult to do. A lot of people just
    thought that it’s so simple to do, because, yeah… who brought up MapReduce at
    the time, and everybody was thinking, “Okay, in Germany, that would work as well.”
  sec: 404
  time: '6:44'
  who: Dat
- line: But that was very difficult. That's why my focus was more rather into starting
    the data science practice in Accenture. I was one of the first ones who did a
    data science project here in Germany. But then I realized that a company like
    Accenture is not something that I wanted to work for a long time. So I left it
    pretty early. Accenture is a big company, it's a consultancy. There's still a
    lot of overhead that you need to do. For example, you need to do a lot of presentations,
    you need to talk to clients – it's more like product management.
  sec: 430
  time: '7:10'
  who: Dat
- line: And then you have people in India, in Spain — in offshore centers, where people
    do code delivery. But I thought “I'm still pretty young, and I like to code. I
    don't want to spend my whole time just working on concepts and not doing the real
    thing.”
  sec: 466
  time: '7:46'
  who: Dat
- line: And then I moved on after a year. I joined Pivotal. Pivotal is a US software
    company. The main focus was actually to do CloudFoundry. CloudFoundry is similar
    to Kubernetes. I joined Pivotal Data where you have databases like GreenPlum.
    It’s similar to Snowflake or Redshift. It's an MPP database.
  sec: 486
  time: '8:06'
  who: Dat
- line: They also have a data science team, which teaches customers how to do data
    science. It's also consultancy, but more hands-on. At Pivotal I got to know one
    of the best engineers in the world. They taught me a lot of things – what’s programming,
    what’s test room development, DevOps skills, bringing data science into production.
    This was quite new five years ago. At the time everyone was talking about that,
    but no one really understood how you get a data science and machine learning model
    into production.
  sec: 517
  time: '8:37'
  who: Dat
- line: 'I learned a lot about this. I devised my own ideas on how to make it happen.
    Because at the time, no one was really thinking about that. What I was thinking
    was: how do you create this fancy machine learning model? How do you do all the
    hyper parameter tuning? But no one really thought about how “What happens afterwards?”
    What happened after day two? Day one — okay, it''s in production. But what''s
    day 2, day, 3, day 5, day 6? Because it''s not a simple app.'
  sec: 560
  time: '9:20'
  who: Dat
- line: Even an app – when you create an app, you have more feature requests, you
    have feature development, you have bugs coming up, and you need to think about
    that. And this is something that was pretty cool. Other than that, I also had
    to work on nice projects. I did my pet projects as well. I got into window vision
    a lot. And also I work on interesting projects, like, for example, Hydro planning
    prediction. I worked for many interesting customers. And I could also travel to
    many nice locations, because Pivotal was based in Silicon Valley.
  sec: 595
  time: '9:55'
  who: Dat
- line: They had their main European office in London. It was a very cool experience
    that I had with Pivotal. I left Pivotal after two years. I realized, “Consultancy
    is nice, you see different customers, you get to know different problems, but
    actually…” As I said, at Pivotal, I started to think about machine learning in
    production. And I was like, “Okay, how do I actually find a company where I can
    test my ideas?”
  sec: 629
  time: '10:29'
  who: Dat
- header: 'Leadership Role at Idealo: Creating Teams and Sustainable Culture'
- line: I looked at some companies, which were interesting for me at the time. I applied
    for several companies. I interviewed for companies like Deutsche Bahn, Telekom
    and whatever. But then, none of these big companies were really interesting for
    me. At that time, I was actually looking for a Head of Data role, like a more
    managerial role. But when you just have three years of work experience, you never
    get this managerial role. They will ask you, “Okay, you're too young, you don't
    have the experience to showcase this”. There was this position at Idealo and the
    role required to have eight years of work experience.
  sec: 667
  time: '11:07'
  who: Dat
- line: But naive me… Of course, I applied. And luckily, it went through. The CTO
    liked my CV. We had our first conversation. After this conversation I talked to
    the CEO, the CPO, and so on. The process only took two weeks. And the coolest
    thing is — while I was in the meeting with the CEO, and CPO and CTO, when we met
    on-site —  I could do a little presentation about what you can expect from me
    in the next two years.
  sec: 730
  time: '12:10'
  who: Dat
- line: That was a very interesting kind of experience — going through this job application.
    It was not like the usual one. I was literally creating my own role in a sense.
    Then I was hired as a Head of Data. I was responsible with two other co-heads,
    for areas like business intelligence, data warehouse, web analytics.
  sec: 770
  time: '12:50'
  who: Dat
- line: While I was at the interview, I was pitched, “We need a data science machine
    learning team.” Idealo is a data company, but we haven't made use of all the data
    that we have at the moment. My two years at Idealo, from my perspective, were
    really successful.
  sec: 804
  time: '13:24'
  who: Dat
- line: I had a nice team. We did a lot of open source projects. We kind of birthed
    a brand for Idealo — that we have a strong machine learning team. It's not like
    when I left, everything was gone. I tried to build a very sustainable culture
    in the company. I don't want to leave a company with everything, but I want to
    leave a place there that I built up.
  sec: 771
  time: '12:51'
  who: Dat
- line: That was something that I really liked. But after two years of Idealo, I also
    realized, “Okay, I built up this team very successfully. What's next?” I cannot
    stay there forever. I was young. I was like, “Okay, I managed to do that. I did
    my learning but what is the next step?” Then I decided, “Okay, I did it for Idealo.
    But how do you do this on a corporate level? For a holding like Axel Springer?”
  sec: 867
  time: '14:27'
  who: Dat
- line: Axel Springer at the time, one and a half years ago, was like… They didn't
    know what research was. It's not a company that is driven by research. Because
    they just didn't know what research was. But if you want to be a tech company,
    you really need research and an open source component within the holding. Then
    I approached Stephanie Caspar, she's one of the board members at Axel Springer.
    I was telling her, “Hey, these are my ideas. What if we try to create these main
    central functions? With evangelizing around Axel Springer, what AI is about, what
    research is about, and how we actually can work together.”
  sec: 908
  time: '15:08'
  who: Dat
- line: One of the driving factors why I did that was I wanted to turn Axel Springer
    into a tech company. So it's not just taking the AI angle – to turn it into a
    more tech-oriented company. Then I did it. I did it for one and a half years.
    I built an AI team again. I took some people with me from Idealo — they wanted
    to come with me. I had a few people. And my role there was… sometimes it’s called
    a “machine leader”, because I didn't have a lot of people function. But more like,
    “How do you talk to the Managing Directors?”. Shape them so that they go into
    the right direction.
  sec: 966
  time: '16:06'
  who: Dat
- line: It's much harder when you do this. Management is very difficult. It's not
    like you have a team and this team is one you've hired. But now you have many,
    many different managers on the same level. How do you make sure that they are
    going in the direction that you want them to go? Also, when looking back at my
    time at Axel Springer, there were a lot of ups and downs. The downside, of course,
    is that it's a big corporate. It was a big challenge for me.
  sec: 1012
  time: '16:52'
  who: Dat
- line: So I started thinking “OK, two years is enough”. To do this whole transformation,
    it takes much longer to do this transformation on an organizational standpoint.
    And also, one thing that I didn't think through was “Hey, to do this kind of transformation,
    you just need much more people under you to drive this transformation, and also
    kind of budget.” You need profit and loss ownership.
  sec: 1045
  time: '17:25'
  who: Dat
- line: But despite that, I managed to drive a lot of things. I managed a couple of
    open source projects. I was one of the initiators of the Axel Springer techcon,
    which is the first big tech conference that we had within Axel Springer.
  sec: 1074
  time: '17:54'
  who: Dat
- line: In pre-Corona when we did it, we had 700 participants from all around the
    world. That was one of the first big things where we could say, “Hey, we're driving
    Axel Springer in the right direction of being a tech company.” And also, the other
    thing we did was the Axel Springer tech blog — where people within the holding,
    within the companies can create articles and blog posts on this tech blog.
  sec: 1092
  time: '18:12'
  who: Dat
- line: This is something that is still living after I'm gone. I really like it, it’s
    still thriving. Because I started it. If I think about this, these are really
    small things, not very big things that I did. Everyone could do them. You just
    need someone to do that, to start this thing. You give people the freedom to write
    articles, go to this conference, and so on.
  sec: 1124
  time: '18:44'
  who: Dat
- line: Some of you know that I resigned from Axel Springer. When I joined Axel Springer,
    I thought, “Ok, I'm not going to stay there forever and I'm either going to do
    my own things or find a niche, managing director / top management positions, so
    that I can drive more things.” Because my credo is “Always know that you need
    more ownership and sometimes older ships come with power.” And power you either
    acquire through a major director position, or you create your own company.
  sec: 1158
  time: '19:18'
  who: Dat
- line: During Corona time the idea came much stronger. I was like, “Everything is
    so slow. Everything at Axel Springer is so slow. It's a COVID world. You cannot
    be there forever. Because you're still 32, not 45 – you don't have a family yet.
    So you really need to go out and think about — what's the next step?”
  sec: 1198
  time: '19:58'
  who: Dat
- header: 'Priceloop Founding: Disrupting Pricing with White Box AI Framework'
- line: Then I was talking to a few friends. One idea was “Okay, maybe you go back
    to Vietnam.” I'm not from Vietnam, I'm from Germany, but maybe go to Vietnam and
    go to a consultancy, because the tech is really strong there, and maybe an idea
    grows out of this
  sec: 1226
  time: '20:26'
  who: Dat
- line: But luckily my current co-founder, Dr. Richard Schwenke approached me. We
    left at the same time from our companies. Richard co-founded Contorion, which
    is an ecommerce for tooling. He co-founded that company, he was the managing director,
    but he sold the company in 2017. And he wanted to create another company, again.
    He's also not that old, and he still really wanted to create a company from scratch.
  sec: 1248
  time: '20:48'
  who: Dat
- line: Because if you're too old, it can be very, very tiring, in a startup to create
    something from scratch again. He approached me with his idea of pricing because
    he created a data science team at Contorion already. They implemented a pricing
    algorithm. They've been dealing with pricing for three years already, and they
    had an uplift of 25% with the things they've been doing.
  sec: 1288
  time: '21:28'
  who: Dat
- line: They did a lot of A/B testing to find the right calibration, hyper parameters
    for the machine learning models, and so on. It's a nice idea — I had pricing at
    university. When you're doing operation research, you also will focus on revenue
    management or dynamic programming. It has a lot to do with pricing. Pricing is
    a decision that you need to do in a control theory.
  sec: 1320
  time: '22:00'
  who: Dat
- line: I was like, “Yeah, that sounds like a good idea.” He was looking for a technical
    co-founder. And I was looking for a business co-founder. So, it was a really good
    combination of us two. We had a discussion around August. And then it was clear,
    “Okay, I'm going to resign from the company.” And he was also “Yeah, okay, I'm
    gonna leave in October as well”. We left at end of September, both at the same
    time. And now we started Priceloop. So, Priceloop is my new venture together with
    Richard. And our goal is to disrupt the pricing industry.
  sec: 1346
  time: '22:26'
  who: Dat
- line: As far as you know, there's many AI software systems out there, also for pricing.
    Most of these pricing servers are actually more closed solutions. You get the
    data from your client, and then you put it into your system – maybe you have a
    login – and it's probably hosted on some cloud provider, and then you give out
    the price.
  sec: 1399
  time: '23:19'
  who: Dat
- line: 'That''s what most of the services do: you give the data, and then you get
    the labels and so on. But what we want to do is, we want to create a pricing framework
    or library at the end. We want to give data science teams, pricing teams a pricing
    framework. So that people like you, maybe OLX, will use us in the future.'
  sec: 1433
  time: '23:53'
  who: Dat
- line: It's so easy to create your own pricing strategies. Then, of course, we have
    commercial solutions on top of that, which we also will offer this to other customers.
    Because if they like to use our framework — we are a company — we also need to
    finance ourselves in some way. But the overall goal is actually to create a whitebox
    solution.
  sec: 1460
  time: '24:20'
  who: Dat
- line: We don't want to take away the pricing manager. We don't want to tell them
    “Hey, if you're going to use this, you don't need to hire a pricing manager or
    you can fire the pricing manager.” No, we want to give them a frame of a tool.
    So that they can make better decisions with their pricing teams. And pricing is
    a core component of many, many companies. And that shouldn't be a blackbox solution.
    That's where I am so far. It's a nice, interesting ride.
  sec: 1492
  time: '24:52'
  who: Dat
- header: 'Team Building Strategy: Experienced Generalists for Early Stage Startup'
- line: A long story. But very interesting. What stood out to me was, first of all,
    you mentioned Andrew Ng and his course on Coursera. I think so many people ended
    up where they are now, because of that course. Including myself. Yeah, it changed
    the lives of so many people. I remember, I started following you on LinkedIn when
    you were already at Idealo. And your team contributed to so many open-source projects.
    I think there was an image quality library. I though “this team is doing great
    on the open source front, pushing out amazing stuff.” The projects also have a
    lot of stars on GitHub, which shows that a lot of people are interested. That's
    a great job. And I'm curious about your startup now. So you said you just started
    it. So Richard and you – do you have somebody else working with you now?
  sec: 1525
  time: '25:25'
  who: Alexey
- line: Yeah. The way we started our startup is not very usual. So since both of us
    are experienced, we finalized our funding and already signed four people. One
    of the machinery engineers just started this week. Three more are coming. We're
    going to make two more offers. We want to be 10 people by Q2 2021. We got a plan
    to do our seed round in 2021. Then we're going to hire more people.
  sec: 1598
  time: '26:38'
  who: Dat
- line: Our goal is to create a strong tactical product team. Which focuses on disrupting
    one of the industries. We believe that the future is in open research, and contribution
    from outside and contributing into ideas for many, many different organizations.
    We see that direction from other startups like Hugging Face — a similar example.
    It’s getting so strong and people are using it in production. Because of the open
    research. And at the moment I haven't seen that in pricing so far.
  sec: 1645
  time: '27:25'
  who: Dat
- header: 'Transition to Consulting: MLOps Production and Day-Two Concepts'
- line: That's an amazing topic. Many, many different companies, ecommerce companies
    will benefit from that. I know that it will all work out. So now you're already
    in the process of building a team. Some people already signed their offers, and
    soon start working. How do you start building a team? How do you approach this
    process? What should you do first? Do you first select a project or you start
    immediately with hiring. How to approach this process?
  sec: 1696
  time: '28:16'
  who: Alexey
- line: It's hard to rationalize my mind. I would say it's a combination of both.
    Some companies just start with hiring people, and then build. And some companies,
    they need a big, big plan, and then they're going to hire people. Our approach
    — this is together. I'm driving it from the technical perspective and we have
    a project. We know what we are going to build, but it's still unclear. Unclear
    in this way that we don't know. We know what the end goal should be – like the
    vision.
  sec: 1737
  time: '28:57'
  who: Dat
- line: But we just don't know, which features will lead to this kind of thing. We
    are hiring for different roles that would take us to that point to get a better
    understanding of our vision. We’re building like an open framework. Like a library.
    Which means it's a strong software engineering project, which means we need very
    good software engineers, who understand how to create abstract libraries.
  sec: 1780
  time: '29:40'
  who: Dat
- line: Since we're dealing with machine learning, we need machine learning engineers.
    Since we're dealing with data, we need data engineers. We need a product manager
    who will prioritize these kinds of things. We need designers who will guide the
    API. We will also need a front end for the commercial solutions. Which means we
    need a UX/UI person who will drive that kind of thing.
  sec: 1812
  time: '30:12'
  who: Dat
- line: There's a lot of roles that need you to think about before. In the beginning
    you also need to think about – do you need very experienced people or inexperienced
    people? Also generalists with specialists? This is the question that you really
    need to ask. At our stage we really need more experienced people, because we are
    an early stage startup. We need to get traction as fast as possible, so that we
    can raise on next funding and also get this product market fit with our customers.
    The second thing is, do we need a generalist versus specialist? Now we need more
    generalists, because as a start up, when you start, you have no lines of code.
    There's nothing, which means, you know, you need to do back end, front end, DevOps,
    and whatever. Whereas when you're a specialist, you focus more on things like
    “I just want to tune this specific hyperparameter.”
  sec: 1839
  time: '30:39'
  who: Dat
- header: 'Hiring: Generalists vs. Specialists based on Organizational Maturity'
- line: It’s an interesting discussion – this specialist versus generalist – and I'm
    wondering. Let's say, if you were still at Idealo. Who would you prefer to hire
    back then? If you wanted to hire somebody in your team? Would it be a generalist
    or specialist? Or would it actually matter?
  sec: 1905
  time: '31:45'
  who: Alexey
- line: When I started at Idealo or?
  sec: 1926
  time: '32:06'
  who: Dat
- line: Let's say you have a team – you're working already in a big company. In a
    startup, it's clear — you want to have generalists – people who can do pretty
    much everything. But let's say it's a midsize company, like Idealo – it's not
    a large corporation, but it's already not a startup. For these kinds of companies,
    who would you prefer to hire?
  sec: 1929
  time: '32:09'
  who: Alexey
- line: I think it depends as well where you are in the organization transformation.
    I think there's this graph where you see how data-driven the company is. If the
    data is very immature, like at the beginning, they don't have a data analyst or
    a data team. Then it makes sense to hire data analysts and data engineers who
    build up the kind of backbone of this.
  sec: 1953
  time: '32:33'
  who: Dat
- line: And then over time you can start to hire more different roles, like data scientists
    or machine learning engineers. Who will bring up the business intelligence. There
    was this famous pyramid, where on the bottom, you have data. You have very messy
    data — you clean the data, and then on top, you have this very thin slice with
    intelligence and then the machine learning part.
  sec: 1983
  time: '33:03'
  who: Dat
- line: If I would map it to Idealo. Idealo was not very mature, but also not completely
    immature. It was in the middle of this transformation. They had a data analyst
    before – they had business intelligence people – they also had data engineering
    who work on a very old database. And then you see that you have to compliment
    this. That means, you don't need generalists in data science, you need more specialists
    in data science. Because the topics are there, but you need people who work on
    that.
  sec: 2015
  time: '33:35'
  who: Dat
- line: Of course, you don't need super-specialists. They need to be a little bit
    towards the level of generalist-level. Idealo was very new in machine learning,
    which means, these people I hired, also needed to put things into production.
    They needed to cooperate with data engineers. Because the data engineer didn't
    understand what machine learning was about. You really need to have empathy to
    work these people together – to bring things into production.
  sec: 2055
  time: '34:15'
  who: Dat
- line: For example, if Idealo would’ve already been at that stage – they already
    have machine learning in production, they know how to use it, then it makes sense
    to go towards this super-specialist, which would mean more research-oriented jobs.
    Because they’re only researching and not really like taking care of other stuff.
  sec: 2084
  time: '34:44'
  who: Dat
- header: 'Corporate Transformation at Axel Springer: Research and Open Source'
- line: Going back to your current company, Priceloop. You mentioned you want to hire
    a lot of different people. You want to hire a product manager, you want to hire
    a frontend engineer, backend engineer, UI/UX designer, data engineer. You said
    that machine learning engineer also is starting soon. How do you decide who to
    hire first? Or you know already who to hire – five different roles and you just
    start hiring? Or you'd rather focus on one specific role first?
  sec: 2106
  time: '35:06'
  who: Alexey
- line: Yeah, we open a couple of roles. In my head, we have to start with certain
    roles. Our first goal was to hire machine learning engineers and software engineers.
    And actually machine learning engineers, who are very close to being software
    engineers. Actually software engineers who know a lot about machine learning.
    Then we can hire product managers and data engineers. At the beginning we need
    people who can work on the prototype, who will work on MVP, who do a lot of coding,
    who will work on the product. It doesn't make sense for you to hire like a UX/UI
    designer, when you have no work for them.
  sec: 2141
  time: '35:41'
  who: Dat
- line: So you really need to understand, at which stage you are. And what kind of
    roles do you need now to solve this problem. Then also, who would you need in
    the future. You cannot hire someone just for six months – then you just need a
    freelancer – but we want to create a company that is more sustainable, longer.
    We know we want to keep these people longer.
  sec: 2185
  time: '36:25'
  who: Dat
- line: So what you're saying is start with hiring engineers – backend engineers who
    know machine learning, and then they will build the backbone. They can also probably
    take care of data engineering and all these data pipelines.  Then you add on top
    of that, maybe analysts, UI/UX, product managers, but first you need to have this
    backbone, and then you need to hire an engineer for that.
  sec: 2212
  time: '36:52'
  who: Alexey
- line: Right.
  sec: 2241
  time: '37:21'
  who: Dat
- header: 'Strong Product Culture: Mission, Short Feedback, and Open Source'
- line: You mentioned a couple of things previously. And one thing that stood out
    to me was – you want to build a strong product team. What does that mean to you
    – a strong product team?
  sec: 2243
  time: '37:23'
  who: Alexey
- line: A strong product team for me is a team that is building a product that the
    customer wants. Strong means very customer-centric. Which also means we deliver
    features very fast. And test these things out with our customers very fast. I
    want to build a product that a customer or user would say, “I love to use your
    product!” It’s the same thing, you want to create these libraries and put them
    open source. We're creating libraries, so people will say ”Wow, the thing that
    you built is very useful for us.” This is something that I would like to hear
    in the future.
  sec: 2264
  time: '37:44'
  who: Dat
- line: Being customer-centric, being able to iterate fast, get this feedback, and
    make sure like you have this feed that customers really want to use what you're
    creating. But how do you make sure the team can do that? Is there any secret sauce?
  sec: 2310
  time: '38:30'
  who: Alexey
- line: I wouldn't say there is a secret sauce – it is just how you create the culture.
    If you look at high-performance teams and the culture with their managers, it
    actually just boils down to the culture that you create in this environment. For
    me, we don't want to do a bullshit bingo – like a scrum bullshit bingo. We want
    to have people who work towards a mission. Who like the job. So we need to keep
    these people motivated. Do everything, as much as we can, so that they can work
    on the problem.
  sec: 2329
  time: '38:49'
  who: Dat
- line: And help them when they have problems and when they get lost with the vision.
    Telling them again, “this is the vision that we want to go, this is direction.”
    Have very short feedback cycles. Also, allowing them to do open-source stuff.
    Not a lot of companies here in Germany and overall – are contributing to the open
    source community in some way. Or are doing stuff that is open. This is something
    that I rarely see in startups as well in companies. There are big corporations
    who do that. But overall in Germany not a lot of companies are doing open source.
  sec: 2371
  time: '39:31'
  who: Dat
- header: 'Data Scientist Hiring: Programming, Code Quality, and Soft Skills'
- line: Yes, that's definitely true. With this open source, many developers want to
    do this. But when it comes to actually doing this… sometimes it's difficult. Do
    you try to give some extra motivation? How do you motivate people to actually
    go ahead and release something to open source? Or with writing articles, it's
    also something people want to do. But it's often difficult. You want to write
    an article, but then you end up doing something else instead of writing. How do
    you motivate people to actually do that?
  sec: 2416
  time: '40:16'
  who: Alexey
- line: If you look at my past teams, most of them before joining, never did anything
    open source or wrote an article before. I'm a very pragmatic manager, so I do
    one-on-ones. In this talk, I give them a suggestion, “it would be nice, if you
    wrote something like this.” Or “this would be nice for the community, if we do
    some open source like that.” And I just talk to them and give them inspiration.
    The rest is up to them. First, some of them started to write and then they were
    stuck and I was telling them, “maybe you could do something like this, then do
    that.” Then they just take that as an idea.
  sec: 2456
  time: '40:56'
  who: Dat
- line: If you really want to create this kind of culture, you need to work with people.
    You need to give them inspiration. Some of them don't have the courage to start
    with that. If they found the courage to start, they may be a little bit clueless.
    There's so many articles out there – where do I start? As a manager I wrote a
    lot of articles already. I could start with telling them, “if you want to do that,
    you could look at some of these articles, I think they are good. Try to do the
    introduction like this, or in the main section a diagram like this would be nice.”
    Give feedback and then it works.
  sec: 2501
  time: '41:41'
  who: Dat
- line: Basically by setting the example. You said you already did that in the past,
    and then you’re just sharing this experience, sharing this motivation that you
    had with the team, then it gets contagious and people just start following that
    and doing that, right?
  sec: 2545
  time: '42:25'
  who: Alexey
- line: Another example is conferences. Before I created this team at Idealo, Ideal
    was never at a machine learning or data conference. If you're thinking about the
    last two, three years, I could see that many Idialos went to conferences. I was
    very proud of Chris Ovanenin. He was one of my first hires. He spoke at Strata
    San Francisco. There were two German companies – Idealo and Flink. I was really
    proud of that. “Wow. We made it to Strata, San Francisco.”
  sec: 2563
  time: '42:43'
  who: Dat
- line: It's a pretty high bar.
  sec: 2603
  time: '43:23'
  who: Alexey
- line: Yeah.
  sec: 2605
  time: '43:25'
  who: Dat
- header: 'Tool: Project Prioritization Matrix (Impact vs. Feasibility); Fail Fast'
- line: That's awesome. Coming back to the hiring process. So you need to hire engineers
    to make sure that the infrastructure is there. The process for collecting data
    is there. But at some point, you want to hire a data scientist. How do you do
    this? What is the process like for you? How does it look like? What are the qualities
    you check? What are the things you're looking for in data scientists?
  sec: 2607
  time: '43:27'
  who: Alexey
- line: My checking is driven by how I feel. I’m looking at the CVs. I don't have
    a checklist where I say, “Yes, yes, yes, yes.” “He studied at Stanford or Harvard
    or whatever”; “He did computer science”, “He has a 4.0 GPA”, and blah, blah, blah.
    I look into the team. If I already hire someone with this quality, I have to look
    for the CV with someone who has a different quality than the other one before.
    Of course, they are similar in some ways and they need a basis. So the basis is
    – you need to know how to program. This is 101 for me.
  sec: 2637
  time: '43:57'
  who: Dat
- line: If you don't know how to code and especially if you don't know about software
    engineering, you are already out of my process. Unless you are a junior. When
    you’re a junior it’s a little bit different, but still I require people to have
    very high coding skills. Other than that, I look at stuff that may be interesting
    for the team. “That person studied mathematics. Wow, cool. That means that person
    knows how to do math.” or “That person already did some open source projects.T
    they know, the open source process.” or “Somebody already did a Kaggle challenge,”
    —  like a real challenge. It means “the person can work under pressure, it's competitive”.
  sec: 2685
  time: '44:45'
  who: Dat
- line: Then I combine these things together, and I say, “this could be a good fit
    to the team,” and “It could be a good fit to the skill set that we're looking
    at in the future.” Then I do a first interview, where I just talk about all the
    experiences, whether that person is interesting. We are also people. We have to
    work together. If someone is just plain boring, this is very difficult for the
    team. That person also needs a hobby. I don't know, go to the cinema, do some
    sports, or whatever, hiking is also healthy. But that person needs to do something.
    You work more time with that person than you spend with your girlfriend or your
    wife. You spend more time with them than with the person that you love. So that's
    why you need to understand that person really well. I also ask 10 basic machine
    learning questions. Some of the questions are in your interview guide that you
    have on GitHub, so I'm not going to discuss them.
  sec: 2737
  time: '45:37'
  who: Dat
- line: There are 160 questions, so 10 of them are there. So if somebody goes through
    all of them, then they will pass your interview.
  sec: 2809
  time: '46:49'
  who: Alexey
- line: Yeah, but they should not copy your answer one on one. Because…
  sec: 2819
  time: '46:59'
  who: Dat
- line: It's a good idea to actually look at the questions and try to answer themselves.
  sec: 2825
  time: '47:05'
  who: Alexey
- line: Right. But what I do is, I ask one question, and then from choices I ask a
    random question.
  sec: 2833
  time: '47:13'
  who: Dat
- line: And when it comes to coding – to programming – is there any specific process
    that you follow for checking? Or how do you do this?
  sec: 2841
  time: '47:21'
  who: Alexey
- line: The second interview is a homework assignment. I send out a homework, which
    is not very difficult. Then they send me the code, whether it is Jupyter Notebook
    or whatever. Then I check it. From this simple task, you could already see how
    much people are working. For example – quotes. Some people don't make sure that
    quotes are the same everywhere. Like double quotes or single quotes. When I see
    that people are using single quotes, near a double quote, then they have a single
    quote, again, I would already see — that person is not really taking care of the
    code.
  sec: 2851
  time: '47:31'
  who: Dat
- line: Small things, yeah.
  sec: 2899
  time: '48:19'
  who: Alexey
- line: Small things, these kinds of small things, you can always see. Also, naming.
    How does this person do the naming? Whether the person does some extraction of
    classes well? Or is the person using a pipeline? From this simple task, you could
    already see how someone would work in the future. There are small things that
    I check, because these small things make a difference at the end.
  sec: 2900
  time: '48:20'
  who: Dat
- line: So basically, whoever is listening, if you want to go to Dat’s company, make
    sure you use the same quotes throughout all the code.
  sec: 2924
  time: '48:44'
  who: Alexey
- line: I don’t think it’s for my company – I think it’s for every company
  sec: 2935
  time: '48:55'
  who: Dat
- header: 'Q&A: Retaining Talent, Managing Hype, and Product Manager Role'
- line: That's interesting… It didn’t occur to me to look at these things. But that's
    an interesting perspective. We just wanted to remind you that you can ask Dat
    a question. You can go there and ask Dat a question. And we already have one question.
    The question is – “For a company that already has an established data team, how
    do you decide which project to take?” You probably have a big list of different
    projects initiatives – how to pick the one to work on?
  sec: 2939
  time: '48:59'
  who: Alexey
- line: This is always a very difficult question. It's risky. Let's say you have 100
    projects. You have only limited resources, which means you need to pick the one
    that has the highest return on investment. What I do is – I have this matrix.
    A two by two matrix. On the Y axis, you have the business impact. And on the X
    axis, you have the technical feasibility. Then from these two dimensions, you
    can map up some of the projects. You go into your different dimensions. You're
    thinking – this is impact, is it impacting revenue or cost? So these are the two
    driving factors and cost revenue. And you can also distinguish it as well.
  sec: 2991
  time: '49:51'
  who: Dat
- line: 'And the technical feasibility — is there a lot of legacy involved? Do we
    need data engineers? Do we have a data dictionary? Is the problem solvable? If
    you think about self-driving cars, it''s not an easily solvable problem with just
    data science. You need much more than data science. You need hardware, you need
    infrastructure, you need a whole ecosystem behind that. Then from there, I would
    just prioritize this list and then look at the top three. And then work on the
    top three. Very important: don''t work on just one project. Because if you work
    on one project for one year, and it''s going to fail, you''re going to fail with
    this one project. At Idealo, you only saw the successful project that we open
    sourced. We had a lot of projects that no one saw, because they never went live.
    It''s fine. The only thing is you need to decide on a project. Because you think
    that it has a high business impact and it''s technically feasible. Then you also
    need to iterate fast. To work towards the goal very fast. And then if you see
    that this thing will not work and I’m failing, then you should really cut it down
    and try the other idea. Fail fast.'
  sec: 3042
  time: '50:42'
  who: Dat
- line: Okay, iterate fast, fail fast. It brings us back to the topic we discussed
    previously of strong product teams. So this is one of these aspects. We have a
    couple of questions. I'll share my screen now.
  sec: 3130
  time: '52:10'
  who: Alexey
- header: 'Starting Data Science: Dealing with Poor Data Quality; Collecting Data'
- line: Question from Pratap. “If I'm about to set up a complete data science, AI
    team in a product space – from where I need to start with?”
  sec: 3152
  time: '52:32'
  who: Alexey
- line: I answered this a bit already with my Priceloop question. You need to think
    about what's your product. Is your product a software engineering project? Then
    you need software engineers at the beginning. If your project is just a consultancy,
    then you can hire any role.
  sec: 3174
  time: '52:54'
  who: Dat
- line: A question from Kai, “How do you see the role of corporate IT regarding data
    science?” I'm not sure I completely understand it. Do you have an idea what corporate
    IT is? So probably maybe something like in companies like Axel Springer?
  sec: 3198
  time: '53:18'
  who: Alexey
- line: In the corporate world, in a company like Axel Springer that has corporate
    IT – I don't think an corporate IT system makes sense for a company like Axel
    Springer in the future. Axel Springer is turning into a tech company. Everything
    that is within the company is driven by technology. So there will not be this
    central corporate IT department. And the corporate IT will be like a DevOps role
    — within a whole technology company. And then data science will play a part within
    this technology organization. I hope this answers the question.
  sec: 3215
  time: '53:35'
  who: Dat
- line: Another question is “How do you keep a good team? Good people tend to get
    great offers and might leave soon. So how do you keep them?”
  sec: 3263
  time: '54:23'
  who: Alexey
- line: This is the question that I always had so far. I didn't have the problem of
    people leaving me because I was always ensuring that people are getting paid fairly.
    And also have interesting projects. If you are going to balance these two things
    out, then you can keep the people. When you start to give people shitty projects,
    or when you micromanage them, then they will leave you someday. Also when you're
    not gonna pay them fairly. Then this is also a big problem. That is something
    that I learned over the time. This is what kept the people working for me. Very
    simple ingredient actually.
  sec: 3283
  time: '54:43'
  who: Dat
- line: So, two things, pay well and give interesting projects. Dat, will you prefer
    a mathematician, or a computer specialist for a machine learning position? And
    computer specialists, probably somebody who graduated from the computer science
    department.
  sec: 3332
  time: '55:32'
  who: Alexey
- line: It doesn't matter. If you are a mathematician, you also need to code. Which
    means you need to be on par with a computer scientist. If you’re a computer scientist,
    you need to understand the math behind machine learning systems. Which is not
    so complicated. And then you know – it doesn't matter, actually.
  sec: 3350
  time: '55:50'
  who: Dat
- line: So you need to have a certain set of skills, and it doesn't matter where you
    pick the skills, right? Was it from your university…
  sec: 3373
  time: '56:13'
  who: Alexey
- line: But you could also not study at all? Right? There are many who didn’t study
    at all and they are very good, so..
  sec: 3381
  time: '56:21'
  who: Dat
- line: Yeah, thank you. “How to deal with hype on management when building a data
    science team?” So it's probably like a question of expectation management.
  sec: 3388
  time: '56:28'
  who: Alexey
- line: 'This is the problem when you are a company and you create this new data science
    team, everyone will expect a lot of you. They know that “Wow AI!” They read these
    things – “They can do so much! We’ll increase our revenue and cost” and so on.
    If someone is opening this new data science team, you really need to communicate
    as much as possible. I also do a lot of education for higher management: “this
    is what I can do, and this is what I can''t do.” Otherwise, you will have so many
    expectations that you''re expected to fail in some way.'
  sec: 3400
  time: '56:40'
  who: Dat
- line: So basically work with management and explain them. Cool. “What do you think
    about this establishment of the data product management role?” So I think this
    is a question about this, maybe a new trend? Data product manager? What do you
    think about this role?
  sec: 3441
  time: '57:21'
  who: Alexey
- line: I would like to have it here in Germany. Most of the product managers are
    not really good. There are some really tough product managers, who understand
    what data-driven is, and they understand what machine learning is all about. But
    most of the product managers are business-driven. If you're a product manager,
    you should also be tech-oriented. In the US, there are much more tech-oriented
    product managers. They were software engineers, they were machine learning engineers
    before, and then they became product managers. Here, there are many people who
    are doing marketing and then they also did product management, and now they’re
    doing project management, but project management is not a product management role.
    Managing a project is different from managing a product.
  sec: 3468
  time: '57:48'
  who: Dat
- line: The last question is “How to start doing data science in a new company, when
    data quality and organization in the company is not good? What are the required
    steps before starting hiring?”
  sec: 3529
  time: '58:49'
  who: Alexey
- line: It’s difficult, if the data is not really good, it can be very challenging
    to create a data science team. If you're doing that, if you are at this stage,
    then you should hire data engineers to clean up the data. Also, have a proper
    data quality process. If you don't have clean data, you can create new data. For
    example, for a lot of our projects at Idealo, we didn't have the data. We collected
    the data and this takes. Sometimes it takes half a year or a year to collect enough
    data to solve a problem. But you have to start someday, because many companies
    just think you come in as a data scientist, you think that we have the data already.
    And then we're just gonna do that. But it’s not going to work this way.
  sec: 3543
  time: '59:03'
  who: Dat
- line: Yes, I can only agree with that. And It also brings back to your point that
    when you have this backbone with data pipelines and all that before, you know,
    thinking about machine learning and hiring data scientists.
  sec: 3608
  time: '60:08'
  who: Alexey
- line: Yeah. Thanks a lot for taking time to come here and share your knowledge with
    us and your expertise. Thanks a lot and thank you everyone for attending and you
    questions. And we will put the video out soon. And yeah – that’s all, I think.
    Any last words from you?
  sec: 3619
  time: '60:19'
  who: Alexey
- line: No. Thanks for having me. I think it’s always nice talking to you Alexey.
    See you then someday live in person – after Corona.
  sec: 3640
  time: '60:40'
  who: Dat
- line: Hopefully it will be soon. Good bye.
  sec: 3650
  time: '60:50'
  who: Alexey
description: Build MLOps-ready data teams and white-box dynamic pricing for startups—hiring
  plan, production ML practices, and human-led pricing to boost revenue.
---

## Books

* [**Extreme Programming Explained** by Kent Beck (1999)](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658): Introduces Extreme Programming practices and **pair programming** as a core engineering ritual.
* [**Test-Driven Development: By Example** by Kent Beck (2002)](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530): Canonical guide that formalized **TDD** as a development workflow.
* [**Introduction to Operations Research** by Churchman, Ackoff & Arnoff (1957)](https://www.amazon.com/Introduction-Operations-Research-Charles-Churchman/dp/0395042001): Foundational text establishing **operations research** as a discipline.
* [**The Theory and Practice of Revenue Management** by Talluri & van Ryzin (2004)](https://link.springer.com/book/10.1007/b139000): Definitive reference for **revenue management** and dynamic pricing models.
* [**High Output Management** by Andrew S. Grove (1983)](https://www.amazon.com/High-Output-Management-Andrew-Grove/dp/0679762884): Management classic informing **effective 1:1s** and pragmatic leadership.
* [**The Lean Startup** by Eric Ries (2011)](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898): Popularized **“fail fast”** and validated learning for product development.
* [**First Things First** by Stephen R. Covey, A. Roger Merrill, Rebecca R. Merrill (1994)](https://www.amazon.com/First-Things-Stephen-R-Covey/dp/0684802031): Popularizes the **Eisenhower priority matrix** (urgent/important) used in **2×2 prioritization**.

## Research Papers

* [**Hidden Technical Debt in Machine Learning Systems** (Sculley et al., 2015)](https://arxiv.org/abs/1706.04972): Seminal paper that seeded **MLOps/Day-Two** thinking for production ML.
* [**Random Search for Hyper-Parameter Optimization** (Bergstra & Bengio, 2012)](https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf): Shows **random search** often outperforms grid search for **hyperparameter tuning**.
* [**On the Input-Output Stability of Time-Varying Nonlinear Feedback Systems** (Zames, 1966)](https://ieeexplore.ieee.org/document/1089830): Core **control theory** result frequently adapted to **dynamic pricing/control** formulations.

## Programs / Reports

* [**DARPA Explainable AI (XAI)** (Program page, 2017)](https://www.darpa.mil/program/explainable-artificial-intelligence): Flagship initiative that catalyzed modern **white-box / XAI** research.

## Essays / Models

* [**The AI Hierarchy of Needs** by Monica Rogati (2017)](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007): Influential essay behind the **Data/AI pyramid** framing (data → features → ML → AI).
* [**Eisenhower Decision Principle** (Background)](https://www.eisenhowerlibrary.gov/eisenhowers/quotes): Historical basis for the **Eisenhower matrix** used in **impact/effort prioritization**.

## Courses

* [**Machine Learning (Coursera) by Andrew Ng**](https://www.coursera.org/learn/machine-learning): Landmark MOOC that standardized introductory **ML curricula** and terminology.

## Tools

* **GitHub**: Platform hosting Dat’s open-source interview guide and community projects.
* **Slido**: Live Q&A tool for collecting audience questions.
* **VBA (Visual Basic for Applications)**: Excel automation language used in Dat’s early analytics work.
* **Jupyter Notebooks**: Interactive Python environment used for assignments and demos.
* **AWS Lambda**: Serverless compute platform from Amazon Web Services enabling on-demand ML functions.
* **AWS Glue Data Brew**: Visual data-preparation tool for cleaning and transforming datasets.
* **Kubernetes**: Container-orchestration system introduced by Google (2014) for scalable deployment.
* **Cloud Foundry**: Open-source PaaS (VMware / Pivotal) enabling app deployment at scale.
* **Greenplum Database**: MPP analytic DBMS (Pivotal) based on PostgreSQL.
* **Snowflake**: Cloud data-warehousing platform (founded 2012).
* **Amazon Redshift**: Cloud data-warehouse service from AWS (2013).