---
episode: 3
guests:
- ioannismesionis
ids:
  anchor: atatalksclub/episodes/Collaborative-Data-Science-in-Business---Ioannis-Mesionis-e2app0c
  youtube: 1pExOVuCF8Q
image: images/podcast/s16e03-collaborative-data-science-in-business.jpg
links:
  anchor: https://podcasters.spotify.com/pod/show/datatalksclub/episodes/Collaborative-Data-Science-in-Business---Ioannis-Mesionis-e2app0c
  apple: https://podcasts.apple.com/us/podcast/collaborative-data-science-in-business-ioannis-mesionis/id1541710331?i=1000632860980
  spotify: https://open.spotify.com/episode/46DN6rAlufvvXaqdOomoTe?si=OMPDN8m5QZWsc5kJY8IcAA
  youtube: https://www.youtube.com/watch?v=1pExOVuCF8Q
season: 16
short: Collaborative Data Science in Business
title: 'MLOps & Data Product Operating Model: Prioritization, A/B Testing & Model
  Monitoring'
transcript:
- line: This week, we'll talk about collaborative data science in business. We have
    a special guest today, Ioannis. Ioannis is a lead data scientist at EasyJet, if
    you’ve heard about this airline – I certainly have because I used it a couple
    of times. In his role, he works on creating data products and solving business
    problems. He also leads the EasyJet MLOps team. Ioannis is also one of the graduates
    of our MLOps Zoomcamp. I was quite surprised that he actually took it – with his
    experience, he should have been one of the instructors. [Ioannis chuckles] But
    I'm pretty happy that you, Ioannis, did take the course because otherwise, we
    wouldn't be talking now otherwise. Welcome!
  sec: 100
  time: '1:40'
  who: Alexey
- line: Yeah. Thanks for having me and for the introduction. It's been a pleasure.
  sec: 150
  time: '2:30'
  who: Ioannis
- header: Ioannis’ background
- line: Before we go into our main topic of business and data science, let's start
    with your background. Can you tell us about your career journey so far?
  sec: 154
  time: '2:34'
  who: Alexey
- line: Yeah, absolutely. Education-wise, I have a bachelor’s in mathematics and a
    postgraduate in data science from Essex University. It's been fun because I wasn't
    always planning to become a data scientist. Essentially, I'm Greek and this is
    important, because in Greece, usually when you have a bachelor’s in mathematics,
    there are not many things that you can do with this degree. You either become
    a teacher – which is, although exciting, wasn't something that I wanted to pursue
    – or you find a way to mix it with some other things. After I finished my Bachelor’s,
    I was thinking about financial mathematics or actuarial mathematics. I didn't
    know what to do.
  sec: 165
  time: '2:45'
  who: Ioannis
- line: Luckily, I got introduced to the notion of data science by watching Netflix
    – actually, the famous Sherlock Series. There was a moment when Sherlock and John
    Watson were on-screen, and John Watson was impressed by Sherlock’s decision-making
    skills. I remember he asked him, “How do you make decisions that fast and so accurately?”
    And Sherlock replied, “You see, but you do not observe.” So that was John's problem.
    That really sat well with me, and I was thinking, “I want to improve my decision-making
    skills.” And this is how I started Googling around “decision-making, inference”
    and all this kind of stuff. I came across data science as a profession. That was
    back in 2016, I think. So yeah, I did a master’s in data science from Essex University,
    followed by a three-month internship, where I was able to develop a machine learning
    model to predict children who are being abused in their current environment. That
    was great because it showed me the power that lies behind data science and machine
    learning in general. I knew that this was what I wanted to do.
  sec: 165
  time: '2:45'
  who: Ioannis
- line: After the internship, I had a four-month experience working as a data scientist
    consultant at a company named AKKA Technologies in Geneva, Switzerland. After
    four months, I decided to move back to the UK, where I started working as a data
    scientist for EasyJet, where I'm still working. I started as a graduate data scientist,
    got promoted to senior data scientist, and right now, I'm still a lead data scientist,
    working with business stakeholders and trying to transform Easy to become the
    world's most data-driven headline. Yeah, that's pretty much me.
  sec: 165
  time: '2:45'
  who: Ioannis
- line: Do you get a discount at EasyJet if you want to go somewhere?
  sec: 321
  time: '5:21'
  who: Alexey
- line: '[chuckles] I think that''s one of the best perks that we have. [chuckles]
    Yeah, the truth is that we do and it''s an excellent discount. I use it all the
    time to travel to different European cities. It''s been great.'
  sec: 325
  time: '5:25'
  who: Ioannis
- line: Because EasyJet is… when it comes to Berlin, I don't know about the other
    cities and I'm based in Berlin – it's one of the airlines I usually use when I
    want to go somewhere.
  sec: 340
  time: '5:40'
  who: Alexey
- line: I'm happy to hear that we're doing something good, then. [chuckles]
  sec: 353
  time: '5:53'
  who: Ioannis
- line: Well, in terms of coverage, it's probably one of the best ones –  at least
    going to Italy or some other countries. Funny that you… [cross-talk] It’s funny
    that you mentioned the Sherlock TV show. Have you seen…? There is another different
    TV show (an American one) called Numbers. Have you seen that one?
  sec: 356
  time: '5:56'
  who: Alexey
- line: Oh, that's interesting. Not really. But noted.
  sec: 381
  time: '6:21'
  who: Ioannis
- line: It's about a mathematician who uses his skills to solve crimes. They use statistics
    and data science. Well, I wouldn't call it “data science” in the sense that you
    and I mean it. But still, it's quite close.
  sec: 385
  time: '6:25'
  who: Alexey
- line: I'm always excited to hear about these use cases where data science is being
    used for good, like the project that you just mentioned – to solve crimes or the
    internship that I did. I think it's great to show how data science can serve the
    people or not be present to replace people’s jobs are some of the things that
    you hear from time to time.
  sec: 408
  time: '6:48'
  who: Ioannis
- line: Yeah, so it's called Numbers. And I think the E is spelled with a 3. So, it's
    like Numb3rs.
  sec: 431
  time: '7:11'
  who: Alexey
- line: I think it rings a bell.
  sec: 440
  time: '7:20'
  who: Ioannis
- header: Ioannis’ role as Lead Data Scientist
- line: Yeah. Anyways, what do you do as a lead data scientist?
  sec: 443
  time: '7:23'
  who: Alexey
- line: Currently, my role as a lead data scientist is a partnership with the business
    stakeholders from Digital Customer and Marketing. These are the departments that
    I oversee from the data science and analytics perspective. I try to understand
    their pain points and translate them into data products and data solutions that
    go into production and solve whatever problem we encounter at the time. You can
    think of my role as having accountability for the projects to ensure that they
    reach production and, of course, we meet the financial benefits that have been
    agreed upon at the beginning of every financial year.
  sec: 448
  time: '7:28'
  who: Ioannis
- line: In practice, what do you mean when you say that you “partner with business
    stakeholders from Digital Marketing”? What does it look like in practice? Is it
    you proactively reaching out to them saying, “Hey, can we talk?” Or do they reach
    out to you? Or is it a combination of both? What does this collaboration look
    like in your case?
  sec: 489
  time: '8:09'
  who: Alexey
- line: It's a great question. Usually, one of the things that I love about EasyJet
    is that it's a really friendly environment. You can think of it as me having a
    close collaboration in terms of meetings, sitting with them during the business
    days, and trying to understand what decisions they have to make on a daily basis
    and then trying to understand, from their perspective, what their strategies are
    and what their vision is for their department, and understand how data science
    can support reaching their vision. This is how it looks on a day-to-day basis
    – meetings and meetups, etc.
  sec: 512
  time: '8:32'
  who: Ioannis
- line: So they have their usual day-to-day meetings, and you’re like, “Hey, can I
    join you? I just want to observe what you do.”
  sec: 552
  time: '9:12'
  who: Alexey
- line: Kind of, yes. We have a recurring meeting where we discuss what they're doing,
    brainstorm together to have – let's call it a framework, where we discuss their
    day-to-day job and what they're trying to improve and see how I can support them
    with data science.
  sec: 561
  time: '9:21'
  who: Ioannis
- line: So you have a monthly meeting or something like that?
  sec: 582
  time: '9:42'
  who: Alexey
- line: Even more frequent – weekly, actually.
  sec: 585
  time: '9:45'
  who: Ioannis
- line: Weekly, okay. [Ioannis chuckles] There are some leaders from these departments,
    and you talk to them saying, “Hey, what’s up? What are the current problems you
    have? How's it going with the previous projects we implemented for you?” And things
    like that. Right?
  sec: 589
  time: '9:49'
  who: Alexey
- line: Absolutely. The way I frame it is – I think of the heads of the different
    departments, from Digital Customer and Marketing as being my best friends in the
    working environment and try to understand how I can be supportive and how I can
    help them.
  sec: 609
  time: '10:09'
  who: Ioannis
- line: So how can you be supportive?
  sec: 624
  time: '10:24'
  who: Alexey
- line: '[chuckles] Exactly!'
  sec: 626
  time: '10:26'
  who: Ioannis
- line: What does it look like?
  sec: 629
  time: '10:29'
  who: Alexey
- line: Usually, it involves me getting enough business knowledge. If we talk about
    the Digital [department], it involves me understanding how, let's say, how the
    PPC advertisements work or how the SEO organic results work, and trying to understand
    what their aim is – which metrics they're interested in and what they do on a
    day-to-day basis. Then I see, “You know what? If we had a predictive model that
    could do X, Y, and Z, would that benefit you?” And then we have this kind of discussion
    that would essentially create some clarity on the business problem that we will
    then try to tackle.
  sec: 633
  time: '10:33'
  who: Ioannis
- header: The importance of having business knowledge
- line: I’ve heard the term “digital department” [from you] many times but to be honest,
    I have no idea what it actually means. It probably means different things at different
    companies, right? [Ioannis agrees] because different companies need to do different
    things. In your case, you mentioned PPC advertisement – I don't know what PPC
    is – Pay Per Click, right?
  sec: 675
  time: '11:15'
  who: Alexey
- line: Exactly. Pay Per Click.
  sec: 697
  time: '11:37'
  who: Ioannis
- line: So the digital department is also some marketing stuff, right?
  sec: 699
  time: '11:39'
  who: Alexey
- line: Exactly. Pay per click, if you think about it, these are the sponsor ads that
    you see on Google. If you go on Google, and you type “flights from London Gatwick
    to Berlin,” let's say, and you press “enter,” you see the 10 results that appear
    on the first page of Google. What you can see there first are usually the sponsored
    ads. These are the pay-per-click ads, as they’re known. The reason they're called
    “pay per click” is because there is an incurred cost every time a person clicks
    on that specific ad. We're trying to, in a way, optimize sponsored ads that appear
    on top. And we do the same thing for SEO results – we tag the organic URLs that
    appear which are usually below the sponsor ads. In a way, it’s an optimization
    that we're trying to do, so that the flights that we want to promote always appear
    on top and then, hence we can improve the conversion rate.
  sec: 703
  time: '11:43'
  who: Ioannis
- line: The other day, I was checking the cost per click in Google for keywords like
    “MLOps,” or “MLOps courses”. [Ioannis chuckles] Sometimes, for more niche words,
    it's like three euros per click, and then for more broad ones, it's like four
    or five, which was like, “Wow, is it that expensive?”
  sec: 767
  time: '12:47'
  who: Alexey
- line: Yeah, yeah. [chuckles] You have to bid on the right keywords, and then become
    relevant and all this kind of stuff that is happening in Google behind the curtains.
  sec: 794
  time: '13:14'
  who: Ioannis
- line: For you, as a lead data scientist, you need to figure out what these people
    talk about, like, “What does PPC mean?” “What do people care about?” “What is
    optimization?” And then, with this knowledge that you can extract from them (learn
    from them) you then go and share this knowledge with the data science team and
    you say, “Okay, these are the problems that these departments are struggling with.
    Let's think about how we can help them.” Right? [Ioannis agrees] And then you
    translate the problems into the language of data science and then, together with
    the team, you work on solving this. Right?
  sec: 802
  time: '13:22'
  who: Alexey
- line: Exactly. Yeah, absolutely.
  sec: 838
  time: '13:58'
  who: Ioannis
- header: Getting projects to production
- line: In addition to communicating with stakeholders, I think you mentioned other
    things – you make sure that projects reach production. What does that mean for
    you? Okay, you first talked with the stakeholders, you understood that these are
    the pain points they have – what happens next? What do you do next as the lead
    data scientist?
  sec: 840
  time: '14:00'
  who: Alexey
- line: As soon as I have the problem statement defined, we have an operating model
    within EasyJet that really helps us to understand, first of all, what the different
    steps are that we have to take to ensure that this resolution of the problem will
    reach production, and then we make sure that we adhere to all these different
    steps. There's a sequence that we follow. As a lead data scientist, I am accountable
    for ensuring that all of these processes are being followed. We make sure that
    when the data product reaches production, it will have the impact that was expected.
    And yeah, that's pretty much it in terms of my role. I can talk a little bit more
    about the framework if you want me to.
  sec: 863
  time: '14:23'
  who: Ioannis
- line: That’s quite interesting. What are these steps and what is this operating
    model?
  sec: 917
  time: '15:17'
  who: Alexey
- line: Yes, the operating model that we have, I think is one of the best things that
    we have created in EasyJet. I had a speech about that at the MLOps Summit. The
    operating model consists of different stages – I think it's four phases, if you
    will, that highlight all the different steps that we need to take to ensure that
    the model will reach production. The first thing is to get clarity on the problem
    statement, and this is pretty much my role. We like to call this a “single front
    door,” where we take a business problem or an idea into the funnel.
  sec: 923
  time: '15:23'
  who: Ioannis
- line: As soon as we do this, we have a meeting where all the relevant stakeholders
    come together and discuss the idea a little bit more. In attendance, you would
    expect people such as the business analysts and the finance team to understand
    the financial benefits that might be involved with the project, a lead data scientist,
    data engineers – every single person that needs to be involved in that specific
    project. As soon as we do that and we understand, “You know what? There's a real
    possibility of something good in this project,” we can take this on. We prioritize
    based on different ideas that have been submitted over time. And then we create
    something like a priority, “You know what? This problem is the most crucial one,
    so let's try to work on that first.”
  sec: 923
  time: '15:23'
  who: Ioannis
- line: As soon as we pick up a project, we will create the so-called “Definition
    of ‘Done,’” which is at the business understanding phase, where we try to understand
    a little bit more about the requirements that we need pick to make this project
    a success, which business KPIs we need to influence, improve, or increase or decrease,
    and how we can measure the benefits. For the latter, it means, let's say, I give
    you random numbers as an outcome, how do you know whether these random numbers
    are good or not? So we make sure that we create a document (the Definition of
    Done document) that highlights, “This is the data product. This is what production
    looks like. These are the benefits that are going to come about based on this
    calculation methodology.”
  sec: 923
  time: '15:23'
  who: Ioannis
- line: A large document?
  sec: 1057
  time: '17:37'
  who: Alexey
- line: Not that large. Usually it's a single document – we have a template. You can
    think about two to three pages, tops.
  sec: 1060
  time: '17:40'
  who: Ioannis
- line: Two or three, okay.
  sec: 1069
  time: '17:49'
  who: Alexey
- line: Yeah. It's not that bad, I think. It outlines on a high level what things
    we need to make sure to deliver at the end of the day so that we don't have really
    much of a moving target, if you will.
  sec: 1071
  time: '17:51'
  who: Ioannis
- line: I assume you have some sort of a template, right? A Google Document or maybe
    a Confluence page, and then you just copy this page and fill in all the things.
  sec: 1085
  time: '18:05'
  who: Alexey
- line: Fill in the information. Absolutely.
  sec: 1096
  time: '18:16'
  who: Ioannis
- line: And you do this?
  sec: 1098
  time: '18:18'
  who: Alexey
- line: Not me, at this stage. I oversee the entire procedure, but usually, we would
    have a business analyst having workshops with the business stakeholders who are
    going to be the business accountable for the project. We try to capture every
    single requirement in this Definition of Done document.
  sec: 1100
  time: '18:20'
  who: Ioannis
- line: Here, you don't talk about machine learning yet? It’s more about, “Okay, this
    is the project and this is the impact that we expect this project to achieve.
    This is how we measure this impact.” Things like that, right? You don't talk about
    machine learning at all at this stage. Right?
  sec: 1119
  time: '18:39'
  who: Alexey
- line: Nothing at all. It just captures the definition of “done”. It captures just
    the “what” of the product, not the “how”.
  sec: 1142
  time: '19:02'
  who: Ioannis
- line: There’s no discussion of the solution at all, right?
  sec: 1151
  time: '19:11'
  who: Alexey
- line: Nothing whatsoever.
  sec: 1159
  time: '19:19'
  who: Ioannis
- line: Okay.
  sec: 1163
  time: '19:23'
  who: Alexey
- line: Because at the end of the day, we may have a document and we may realize down
    the line that it's not something feasible. We may know what we need to do, but
    after we have established all the requirements, we may realize, “You know what,
    the data is not actually there, which means that this is a no-go.” When that happens,
    although it doesn't happen frequently, this is a “fail fast” scenario. Then we
    say, “You know what, we cannot proceed with that. Let's take the second in line.”
  sec: 1162
  time: '19:22'
  who: Ioannis
- line: But this happens later, right? [Ioannis agrees] At the business understanding
    step you come up with this Definition of Done document for a project, which is
    like two or three pages long, and then I guess you proceed to the next step, which
    is, as you mentioned, checking data and things like that.
  sec: 1188
  time: '19:48'
  who: Alexey
- line: Exactly. As soon as everybody has signed off on this document – the business
    stakeholders, data scientist (which is me, in this case) , the data engineer,
    and every single person involved – then we proceed to the next phase. This is
    where the data science-y involvement starts to kick in – inception. You can think
    of it as the EDA (exploratory data analysis) where we try to ensure that we have
    everything that we need. That includes access to the data, if the data is already
    present, any GDPR concerns that we might encounter, exploring the data sources
    as in different distributions and these kinds of constraints that we might have.
    Yeah, that's pretty much it.
  sec: 1203
  time: '20:03'
  who: Ioannis
- header: The inception phase
- line: At which stage do you actually…? You said that this is when data science kicks
    in. Is this the stage when you think, “Do I even need machine learning here or
    is it more like an analytical project?”
  sec: 1254
  time: '20:54'
  who: Alexey
- line: Absolutely.
  sec: 1269
  time: '21:09'
  who: Ioannis
- line: Okay.
  sec: 1271
  time: '21:11'
  who: Alexey
- line: As soon as we kick off the inception phase, this is where the data scientists
    and analysts come together, and we brainstorm about the solution – we discuss
    the “how”. At this point, we understand whether this is a data science project
    that would involve machine learning or data analytics, or whether it's a hybrid
    between the two different sub-teams (data science and analytics).
  sec: 1272
  time: '21:12'
  who: Ioannis
- line: To be honest, we do have some idea, when the business stakeholders discuss
    the problem, and we may have already decided at this point that this is a data
    science project or a data analytics one. But at the inception phase, we’re absolutely
    certain that, “You know what? This is 100% a data science project,” for instance.
    It’s just the confirmation that we have of when we started.
  sec: 1272
  time: '21:12'
  who: Ioannis
- line: And depending on whether it is a data science project or not, I guess the
    next step would be different, right?
  sec: 1329
  time: '22:09'
  who: Alexey
- line: Absolutely, yeah.
  sec: 1335
  time: '22:15'
  who: Ioannis
- line: Then if it’s not a data science project, you say, “Okay, I'm a data scientist,
    I cannot help you,” and then somebody else takes this over, right?
  sec: 1338
  time: '22:18'
  who: Alexey
- line: Not really. I’m accountable for both the data science and analytics projects.
    The only difference is that if it's an analytics project, the technical lead who
    will work on the project is going to be a data analyst instead of a data scientist.
    I still hold the accountability for making sure that the product is delivered
    end-to-end.
  sec: 1347
  time: '22:27'
  who: Ioannis
- header: Agile practices
- line: So what's the next step? Or is it different for different projects?
  sec: 1368
  time: '22:48'
  who: Alexey
- line: Not really. As soon as you have an idea and you have defined the “how” of
    solving the problem statement, this is where we move into the research and development
    phase. These are the hardcore modeling steps in data science, where we follow
    all the different design methodologies – sprint planning, stand-ups, retrospective
    – all the usual suspects are usually there, where we discuss all the different
    stories that we have defined in a Kanban board, for instance. We define sprints,
    “This is the goal for sprint one, sprint two.” This is where we start building
    whatever that solution might look like. We also make sure that the stakeholders
    are closely working with us because you have to make sure that… It's a common
    problem that we're trying to tackle so you want to make sure that the business
    stakeholders are part of the team and they're not just sitting around waiting
    for a delivery in three to six months’ time, depending on the complexity. So we
    make sure that we tackle that as a single team.
  sec: 1375
  time: '22:55'
  who: Ioannis
- line: So that's why you have regular (at least weekly) meetings with them, right?
    You want to keep them updated on, “What is the progress? What is being solved
    right now? What stage are each of the projects?” Things like that?
  sec: 1448
  time: '24:08'
  who: Alexey
- line: Absolutely. Also, at the end of every sprint, which is usually bi-weekly,
    we have a demo where we show, “These are the things that we have delivered.” And,
    if possible, we have an actual demo where they can get a sense of what we're building
    and influence some of the steps that we might take on the future sprint. They
    oversee the project from the beginning all the way to the end so they make sure
    that what gets delivered at the end of the day is something that they will end
    up using.
  sec: 1462
  time: '24:22'
  who: Ioannis
- line: So I guess you also give them some sort of demo – a Streamlit App or something
    like this – that they can play around with so they see, “Okay, this is not what
    I meant.” Or “Yeah, this is what I need.
  sec: 1499
  time: '24:59'
  who: Alexey
- line: Absolutely, yeah.
  sec: 1513
  time: '25:13'
  who: Ioannis
- header: The pilot phase
- line: After the R&D phase, is there anything else?
  sec: 1517
  time: '25:17'
  who: Alexey
- line: Yes. Then we have the pilot phase. In the Definition of Done, we have already
    defined the KPIs and the baseline that we're trying to beat. Usually, there's
    an existing “as-is” process that we're trying to beat with a new solution. Then
    we move into the pilot phase, which usually looks like A/B testing, where we test
    the “as-is” process compared to the “to be” process and ensure that the product
    that we have built improves the KPI of interest.
  sec: 1522
  time: '25:22'
  who: Ioannis
- line: During that time, we also collect feedback from the business stakeholders
    because that can influence a second iteration of the product if needed. After
    the creation of the model, usually, it's the pilot phase, to ensure that we get
    the benefits that we were expecting. If that succeeds, then, I guess, it's deployment.
  sec: 1522
  time: '25:22'
  who: Ioannis
- line: I’m just trying to come up with a joke about the “pilot phase”. [Ioannis and
    Alexey laugh] I’m not creative enough. [chuckles]
  sec: 1575
  time: '26:15'
  who: Alexey
- line: '[laughs] I know what you mean.'
  sec: 1584
  time: '26:24'
  who: Ioannis
- line: 'So okay – the steps are (the phases are): first, it''s the business understanding
    phase, when we come up with this Definition of Done for a project. Then it’s the
    inception phase, where people actually… In the first step, you talk about the
    “what” and not the “how” but in the second step, you discuss their actual solution
    and you also decide if it''s a data science project or more like an analytical
    project. Then, during the R&D phase, you work on the development – the research
    and development of the project. Then you also talked about how exactly you do
    this – all these agile techniques. At the end, there is the pilot phase, where
    you take what you developed and you see if the KPIs you defined in the Definition
    of Done are actually met. Right?'
  sec: 1586
  time: '26:26'
  who: Alexey
- line: Absolutely. Yeah, that's correct.
  sec: 1642
  time: '27:22'
  who: Ioannis
- line: So those are the four steps that you mentioned. Is there a fifth one after
    the pilot? Like, the production part?
  sec: 1645
  time: '27:25'
  who: Alexey
- line: It's usually the production. As you probably already know, “production” is
    a spectrum. Production might mean surfacing some insights into a Tableau dashboard,
    for instance. It can be some predictions being surfaced into an external tool.
    That can be all sorts of different things. Depending on what this means, we have
    the appropriate, let's say, production framework, which is still being developed
    at the moment. Of course, MLOps is certainly still at the beginning. But yeah,
    after we see that the benefits are already there and we beat the baseline, we
    roll this out to the entire market, depending on the project, of course.
  sec: 1652
  time: '27:32'
  who: Ioannis
- header: Other departments at EasyJet and competitors’ business models
- line: The use cases you deal with are mostly related to marketing and similar cases
    – all these campaigns.
  sec: 1698
  time: '28:18'
  who: Alexey
- line: Нes. Mostly Digital and Marketing.
  sec: 1707
  time: '28:27'
  who: Ioannis
- line: So you don't try to work with the actual planes and the schedules?
  sec: 1710
  time: '28:30'
  who: Alexey
- line: Not myself. But that's an excellent question because, as a data scientist,
    I look after Digital Customer and Marketing, but actually we have two or three
    more lead data scientists, where every single one looks after a different division
    of the business. So we have a lead data scientist who looks after Scheduling and
    Network, and another lead data scientist who looks after the Ops when needed,
    and, of course, Pricing and Revenue.
  sec: 1719
  time: '28:39'
  who: Ioannis
- line: I noticed that tickets became more expensive after COVID. [Ioannis laughs]
  sec: 1752
  time: '29:12'
  who: Alexey
- line: I have no idea about this. [laughs] No comments.
  sec: 1757
  time: '29:17'
  who: Ioannis
- line: Well, you have a discount, right? [chuckles]
  sec: 1761
  time: '29:21'
  who: Alexey
- line: Yeah. [chuckles]
  sec: 1764
  time: '29:24'
  who: Ioannis
- line: I remember that a trip to Italy, before COVID, cost… Sometimes it was actually
    more expensive to get the bus that goes from the airport to the city than the
    actual ticket. These days are gone. Now it's more expensive to travel.
  sec: 1765
  time: '29:25'
  who: Alexey
- line: Yeah, I guess inflation as well. Yep.
  sec: 1786
  time: '29:46'
  who: Ioannis
- line: I was always wondering how companies like RyanAir can keep their costs that
    low – when it's like 10 euros for a ticket. But they probably cannot anymore because
    now it's different.
  sec: 1791
  time: '29:51'
  who: Alexey
- line: Exactly. I think it's because of the different business models that different
    airlines operate under. There's a specific mindset that allows, let's say, RyanAir
    to operate with tickets that have an X price compared to EasyJet or Wizz Air –
    different competitors, of course.
  sec: 1801
  time: '30:01'
  who: Ioannis
- header: Utilizing Scrum practices in data science (the importance of MVPs)
- line: You already talked a little bit about Agile methodologies that you use during
    the R&D phase and I was wondering if maybe you can talk more about this? How do
    you structure your day-to-day work when it comes to working on data science projects?
    In my experience, I remember… It was some time ago, and we tried Scrum. Maybe
    I'll take a step back. My background was originally a Java developer, and Scrum
    works well for well-defined developed software engineering projects.
  sec: 1821
  time: '30:21'
  who: Alexey
- line: But when it comes to data science, it's a little bit more ambiguous, because
    you don't know whether what you will have at the end (the thing you build) will
    work or not. In software engineering, it's usually less nondeterministic, let's
    say. Usually, you know that you will eventually build the thing that solves the
    problem, you just don't always know how long it will take.
  sec: 1821
  time: '30:21'
  who: Alexey
- line: When it comes to data science, you not only don't know how long it will take,
    but you also don't know whether it will actually work in the end. [Ioannis agrees]
    How do you structure your processes around this problem? You mentioned agile sprint
    planning and Kanban – so I'm curious to know in more detail how exactly you structure
    the work.
  sec: 1821
  time: '30:21'
  who: Alexey
- line: Yes, absolutely. Of course, I was working as a technical lead (as a senior
    data scientist) which means that, now, as a lead data scientist, I don't schedule
    all the agile ceremonies. But as a technical lead, when I was a senior, I did
    have that experience. What I was following was all the different agile methodologies
    that have been introduced – I was making sure to stick with them. What you said
    about being ambiguous is actually true. Because in data science, you don't really
    know what you're building until you go and actually build it. This is when you
    realize whether it works or not.
  sec: 1911
  time: '31:51'
  who: Ioannis
- line: So what we try to do to make the process a little bit simpler – to ensure
    that it's working – is we have the notion of MVPs (minimum viable products) which
    means that, in the Definition of Done document, we have the list of all the requirements
    that we know we have to build, which means that we kind of already have a sense
    of what we're building and which direction that we'll be taking. And because we
    know what we're building, it's a bit easier to estimate the time that it might
    take for us to deliver a single requirement or a single feature. That doesn't
    mean that we're always following Scrum – personally, I'm an advocate of Kanban,
    because of the complexities that have to do with data science and machine learning.
    But usually, we’re pretty good at estimating whether a specific feature is going
    to take, let's say, a week and a half. Even though we may not strictly follow
    the Scrum methodology, we actually have a Kanban board, and we try to put some
    timelines into our schedule to ensure that, “You know what? We'll have something
    built by the end of this two-week sprint.”
  sec: 1911
  time: '31:51'
  who: Ioannis
- line: Of course, we do this with all the different agile ceremonies that we mentioned
    – we have sprint planning, which ensures that we have the different complexities
    allocated to the different stories. Of course, there are many ways to do that.
    At the end of the day, we do have some sense of how long something is going to
    take because of the notion of MVP, and we try to stick to these two-week sprints.
  sec: 1911
  time: '31:51'
  who: Ioannis
- line: So you group all your work into these two-week sprints and at the beginning
    of each sprint, you do some sort of planning where you decide, “Okay, for these
    two weeks (for this sprint) we take this, this, and this. It will take probably
    the entire two weeks to do.” Right? And then during the week…
  sec: 2064
  time: '34:24'
  who: Alexey
- line: Exactly, depending on the resources.
  sec: 2091
  time: '34:51'
  who: Ioannis
- line: The resources are the people who work on this, right?
  sec: 2094
  time: '34:54'
  who: Alexey
- line: Yeah. Something to add here, which also helps us estimate the different stores
    and how much they're going to take, also comes at the inception phase. At the
    inception phase, we dive into the data and try to understand a little bit about
    the quality of the data, how much preprocessing we might have to do, or how much
    time a specific implementation might take depending on the complexity of the project.
    The inception phase also gives us an understanding of how much time this specific
    implementation is going to take. That helps us estimate the timing a bit.
  sec: 2100
  time: '35:00'
  who: Ioannis
- header: A typical sprint at EasyJet and other Agile practices
- line: Can you maybe walk us through the entire sprint? So, the sprint starts with
    planning and I think it ends with a demo – what happens in between?
  sec: 2138
  time: '35:38'
  who: Alexey
- line: Yes. In between, we have daily stand-ups. Of course, it can be a written stand-up,
    or an actual 15-minute stand-up, usually in the morning, where the entire team
    comes together and we say, “I've been working on this story. This is the progress
    I’ve made so far. This is the plan that I'm going to work on today (or for the
    next couple of days). These are the blockers (if any) that I'm encountering at
    the moment.” Usually, when this happens, you have a senior member jump in to support
    – we make sure that all the blockers are removed so we can deliver the project
    or the feature on time.
  sec: 2147
  time: '35:47'
  who: Ioannis
- line: Of course, depending on the complexity of the project, that can be an everyday
    stand-up or every other day – it really depends. But I think what works the best,
    according to my experience, is having two stand-ups per week so that it gives
    time for the people to work on the different stories. And, of course, if something
    goes wrong, you can always reach out to a teammate to ask for support. That's
    pretty much it in terms of stand-up. And of course… [cross-talk]
  sec: 2147
  time: '35:47'
  who: Ioannis
- line: It’s not a very heavy process, right? What I understood is that you have this
    estimate – the start of the sprint where you estimate. Then you have some stand-up
    meetings during the week. Then, at the end, you have the demo. Right? That's basically
    the process. So it's not very heavy. [Ioannis agrees] Because I know in Scrum,
    there are all sorts of other things like grooming. I don't even remember what
    else, but I remember that the backlog grooming can get quite heavy if you follow
    the book and try to implement everything.
  sec: 2222
  time: '37:02'
  who: Alexey
- line: That's true. But I think the notion of Agile is actually being agile and seeing
    what works for your team and what doesn't. We have tried with different meetings,
    according to what has been proposed over time. But we have identified that this
    framework that we have works great for our team and we follow this specific framework.
    One of the things that Ben Diaz, who is the Director of the Data Science and Analytics
    team, says is, “We have to be agile at being agile.” I think that summarizes everything.
    [chuckles]
  sec: 2262
  time: '37:42'
  who: Ioannis
- line: What does estimating look like for you? Do you use something like PlanningPoker
    or things like that?
  sec: 2297
  time: '38:17'
  who: Alexey
- line: It depends. Different teams use different techniques. We have T-shirt sizing,
    sometimes we follow the Fibonacci sequence to allocate points. We also have Scrum
    masters who support us in that way. We make sure that we don't use days as a way
    of estimation. So, whatever has worked for the different team members over time,
    it's usually the technical leader of the project who decides which method they
    want to use.
  sec: 2306
  time: '38:26'
  who: Ioannis
- line: Yeah, interesting. So you do some sort of planning poker, right? Or?
  sec: 2337
  time: '38:57'
  who: Alexey
- line: Yeah, yeah.
  sec: 2344
  time: '39:04'
  who: Ioannis
- line: And what does it look like? I imagine that there's a meeting, and in this
    meeting, you have different people –you, a scrum master, project lead, data scientists
    can implement this, and then somebody (for example, you, as the project lead)
    says, “Now, let's talk about this task (this story) that we are going to take
    in this sprint, which is about changing the color or changing the chart on this
    dashboard (or whatever).” Right?
  sec: 2346
  time: '39:06'
  who: Alexey
- line: Yeah, whatever that may be.
  sec: 2377
  time: '39:37'
  who: Ioannis
- line: Everyone says, “Okay, I think this is a very easy task.” Right?
  sec: 2379
  time: '39:39'
  who: Alexey
- line: Exactly, that you put that number on top. Depending on which one you think
    is the most complex, you put the corresponding numbers. Yeah, this is pretty much
    it. Every single team member… Of course, there are always outliers, but usually,
    you have all the different stories and you say, “Okay, which one do we think is
    the most complex one?” This gets allocated with that specific number, and then
    we increase the complexity depending on the methodology that we use.
  sec: 2384
  time: '39:44'
  who: Ioannis
- line: Yeah, interesting. In your experience, does it work well?
  sec: 2410
  time: '40:10'
  who: Alexey
- line: I think so. There have been examples where it has worked out perfectly and,
    of course, there are always [chuckles] the bad examples where you can see that
    you're quite tough when it comes to timelines. But I think the bottom line is
    that you have to adjust and be mindful of the fact that not everything is expected
    to go well on every single project. As soon as you manage your expectations, I
    think you're good.
  sec: 2415
  time: '40:15'
  who: Ioannis
- line: When it comes to business stakeholders, I assume you don't invite them to
    your stand-ups, but you probably invite them to demos, right?
  sec: 2449
  time: '40:49'
  who: Alexey
- line: Yes, that's correct. I think that's a great way for the business stakeholders
    to get a sense of what we're building because they can get an early interaction
    with the tool and the direction that we're taking. They also feel like a part
    of the team and that makes them more engaged in what we're building and quickly
    sense that we're a team and we're trying to tackle this problem together instead
    of us acting like consultants, “This is what we're building for you. Just use
    it.”
  sec: 2461
  time: '41:01'
  who: Ioannis
- header: Explaining results to non-technical people (the importance of soft skills)
- line: I also imagine that the business stakeholders – it could be the Head of Marketing
    or Head of Digital, or some other Head – don't necessarily know what every C-curve
    means or precision-recall and things like that. [Ioannis agrees] When it comes
    to demos that are maybe a little bit more technical, they sit there and are just
    like, “Okay, I don't understand this, but I trust that you’re doing your work.”
    How do you deal with this – when stakeholders do not necessarily understand what
    the team is talking about? Or do you maybe educate the stakeholders, educate the
    team, or both? What helps?
  sec: 2493
  time: '41:33'
  who: Alexey
- line: I think, in cases like that, you really have to be a chameleon and this is
    where soft skills come into place. When we have a demo session at the end of every
    sprint, we have to make sure that we never use technical language with them, because
    you have to adjust your context for a non-technical audience. I don't think there's
    been a single project where we have thrown some technical jargon, if you will,
    at all.
  sec: 2535
  time: '42:15'
  who: Ioannis
- line: You educate the team members. You can say, “Look, if you say ‘ROC curve,’
    they will be like, ‘Okay, what is that?’” So you teach them how they can present
    findings, the projects, and the demos, in a way that stakeholders will understand.
  sec: 2572
  time: '42:52'
  who: Alexey
- line: Exactly. We never use any technical language with them. And if there's something
    that you need to explain that might require some technical knowledge, we always
    make sure that we use examples that can be easily interpretable compared to a
    technical implementation that you have seen. For instance, if you think about
    recommender systems and you want to understand how a specific person is closely
    related to another, you wouldn’t say, “As a measure of understanding how close
    two individuals are, we use the Keegan distance.”
  sec: 2594
  time: '43:14'
  who: Ioannis
- line: Instead, you put forward two examples where you say, “You see that these two
    people look similar?” And you don't really need to define similar in this context,
    because they can see that all the different roles, for instance, look the same,
    compared to another individual that is completely on a different cluster. So when
    you want to explain these kinds of technical details, you can always use an example
    that would make sense for a non-technical audience.
  sec: 2594
  time: '43:14'
  who: Ioannis
- line: Well, I assume that this is also a skill – presenting your findings in a way
    that non-technical people can understand. [Ioannis agrees] It can be even more
    difficult to learn this skill, to master this skill – let's say, even more difficult
    than learning machine learning, at least for technical people.
  sec: 2659
  time: '44:19'
  who: Alexey
- line: Potentially, yes. [laughs]
  sec: 2679
  time: '44:39'
  who: Ioannis
- line: People who are used to terminals and notebooks and all this stuff – going
    in and presenting something to business stakeholders might not be something that
    they're used to doing. So how do you educate people? How do you help them learn
    this skill or master this skill?
  sec: 2680
  time: '44:40'
  who: Alexey
- line: I don't think there's an easy way. I think this comes with experience and
    just making sure that you always enhance your soft skills. One of the things that
    usually helps is thinking about all the different inner sentences that people
    usually say, “Pitch it to me like I'm a five-year-old.” Or I think Einstein had
    said, “If you can’t explain something in simple terms, you don't know it that
    well.” So, I guess it's just a matter of reminding people that the people that
    we have on the other side of the call don't have the technical experience that
    you have, so try to speak their language and explain what you're doing like you're
    speaking to a five-year-old. I guess there's no easy way to do this, it just comes
    with experience and constant feedback, of course.
  sec: 2710
  time: '45:10'
  who: Ioannis
- line: And I guess having a five-year-old helps. [chuckles]
  sec: 2764
  time: '46:04'
  who: Alexey
- line: Yeah. [laughs] I can only imagine.
  sec: 2775
  time: '46:15'
  who: Ioannis
- line: Maybe if you don't have a kid who's five years old, you have no idea how much
    knowledge they actually have. [Ioannis agrees, chuckles] I have a son. He's seven
    years old. He sometimes asks me things like how GPS works. And I have no idea.
    Let's say if I go on the internet and type, “How does GPS work?” then the explanation
    would be super technical. Then I think, “Okay, how do you explain this to my son?”
    So it's a skill. Well, one hack I found quite useful is just asking ChatGPT. I
    guess everyone uses this now.
  sec: 2777
  time: '46:17'
  who: Alexey
- line: Oh, yeah, of course. Absolutely. I still remember the days when ChatGPT wasn't
    out – I remember, I was a graduate data scientist at the time. I got the opportunity
    to present something to business stakeholders. I think this is when he found out,
    not in a nice way, that my ways of presenting and soft skills are not as good
    [as I thought]. I remember there was a really cringe moment where I was trying
    to explain why having 99% accuracy as a wider term doesn't mean anything unless
    you know about the balance with the labels. Yeah, I think it didn't go well. I
    think this pushed me a little bit to try to understand how I can present to someone
    who doesn't have technical expertise. I think it comes with experience at the
    end of the day.
  sec: 2818
  time: '46:58'
  who: Ioannis
- line: Actually, we can think of ourselves as five-year-old kids too, when it comes
    to learning new things. For example, when I read this article about how GPS works,
    I'm clueless. Okay, there are a bunch of us that try to explain it, but I don't
    really understand what's happening there. So the explanation that ChatGPT gave
    to my son was actually helpful for me to also understand that. I don't know if
    I should say that, but maybe we can think of stakeholders as kids. [chuckles]
  sec: 2865
  time: '47:45'
  who: Alexey
- line: '[laughs] Yeah, I think I know what you mean. I''m really happy that all the
    stakeholders that we have at EasyJet are really literate in terms of data science
    and mathematics. That makes our work really, really easy. So I''m so thankful
    for that.'
  sec: 2903
  time: '48:23'
  who: Ioannis
- header: Ioannis’ experience with the MLOps Zoomcamp
- line: Yeah. Great. Also, I actually wanted to spend a bit of time talking about
    the MLOps Zoomcamp course, because I was…
  sec: 2918
  time: '48:38'
  who: Alexey
- line: Yeah, of course!
  sec: 2927
  time: '48:47'
  who: Ioannis
- line: I was really surprised when I looked at your background – I thought, “Why
    would Ioannis even consider it?” Because with your experience – you're already
    doing all the things you talked about right now – I'm wondering, what inspired
    you to take our course? Why did you decide to take it?
  sec: 2929
  time: '48:49'
  who: Alexey
- line: Yeah, absolutely. The thing is, as a lead data scientist, my role has become
    a little bit more managerial compared to the amount of time that I have to spend
    doing technical stuff. And if you ask me, having a bachelor of mathematics, I'm
    a geek at heart, which means that every opportunity I get to get my hands dirty
    with some data and build something myself – I always take it. MLOps specifically
    is, from my experience – I'm usually involved in, let's say, building the models
    and I didn't get much exposure to the productionization side of things. I was
    just intrigued by the course and the content. Of course, I was using MLflow, but
    then we had Prefect – the data engineering team – and we have been using airflow.
    And I'm like, “Let me get into that engineering side of things a little bit more
    and also get the opportunity to get my hands dirty.” I think this is what clicked
    for me. And I'm like, “Yeah, let me go for it.”
  sec: 2950
  time: '49:10'
  who: Ioannis
- line: Well, as somebody who was a lead data scientist in the past, one problem for
    me was always time. [Ioannis chuckles] With all this stakeholder management, how
    do I actually find time to still be hands-on and experiment with things? [Ioannis
    agrees] And then sometimes, I wanted to take a course, but then I didn't have
    time, because there’s only 40 hours that you spend at work. How did you solve
    this problem?
  sec: 3022
  time: '50:22'
  who: Alexey
- line: Yeah, that's a great question. I think one of the good things about my decision
    to become a data scientist is that I genuinely love the profession. I would be
    a data scientist as a hobby if my day job was something different. This means
    that even when I finish my work, I don't feel drained from all the information
    that I had to go through throughout the day.
  sec: 3053
  time: '50:53'
  who: Ioannis
- line: I genuinely enjoy working as a data scientist, which means that I consider
    that as an activity rather than, let's say, something that will consume my time.
    So yeah, it was just great. I had my morning cup of coffee, and during the weekends,
    I took my laptop, went to a nice coffee place and just watched your courses and
    tried to do the assignments. It's been fun. And I got a little experience out
    of it, to be honest. So yeah, it was just great.
  sec: 3053
  time: '50:53'
  who: Ioannis
- line: So instead of watching Netflix, you watched the courses.
  sec: 3112
  time: '51:52'
  who: Alexey
- line: What was that?
  sec: 3117
  time: '51:57'
  who: Ioannis
- line: Instead of watching Netflix, you watched the courses. Or… Maybe in addition
    to.
  sec: 3118
  time: '51:58'
  who: Alexey
- line: Yes! [laughs] Absolutely.
  sec: 3121
  time: '52:01'
  who: Ioannis
- line: Okay. Well, it sounded like the course was useful for you, right? Was it mostly
    like… I don't know if I should call it that – entertainment? Or more like self-educating?
    Or did you also get something out of this course and apply it at work?
  sec: 3124
  time: '52:04'
  who: Alexey
- line: It was a little bit of both. It was entertainment in the sense that I got
    confirmation that what I'm doing is correct. But also, I got the opportunity to
    play with technologies that I otherwise wouldn't have time to. One of the examples
    is Prefect, for instance. Because as a lead data scientist, I’m not that involved
    in the engineering side of things, so I wouldn’t get the opportunity to play with
    Airflow or Prefect. So I think it had a good balance of both –  getting the confirmation
    that what I'm doing is correct, but also learning something new. This is really
    important because as you mentioned in the beginning, I'm leading the MLOps team
    within EasyJet. Even though I give the guidance and have an influence on where
    we're going as a data science and analytics team with our MLOps journey, it was
    great for me to understand a little bit about the technical landscape. I feel
    that that's the best way to influence a specific direction. So that really worked
    well.
  sec: 3144
  time: '52:24'
  who: Ioannis
- header: On Evidently
- line: Actually, before our conversation (before our interview) I had a chat with
    Elena from Evidently and she said, “Oh, Ioannis is coming to your podcast? Make
    sure to ask about Evidently!” [chuckles]
  sec: 3213
  time: '53:33'
  who: Alexey
- line: Absolutely. Evidently, I think – and I'm not afraid to say this, but I think
    Evidently is the best Python library out there for model monitoring. This is something…
    the final assignment that I did for the MLOps Zoomcamp also gave me the opportunity
    to play with the Evidently library a little bit more. I had the time to play with
    Evidently, I think, two years ago, when it was still, in a way, the dev version.
    I remember the first time that I reached out to them, because I said, “You know
    what? I have implemented that and it doesn't look correct.” There was actually
    a bug and this is how the networking kicked in. But yeah, Evidently – absolutely
    the best Python library for model monitoring.
  sec: 3228
  time: '53:48'
  who: Ioannis
- line: Do you use it at EasyJet as well?
  sec: 3280
  time: '54:40'
  who: Alexey
- line: Absolutely. We will use it to their sense of embedding that within our MLOps
    framework. It's still a work in progress but we have made tremendous progress
    throughout all these years. I think, especially now that we're trying to define
    our MLOps capabilities, Evidently is the best thing that could have happened to
    me and to EasyJet to that extent.
  sec: 3283
  time: '54:43'
  who: Ioannis
- line: Just curious – I know Evidently, right now, has its own dashboard, but what
    you do is probably based on some sort of other monitoring framework, like Grafana
    or something like that, right?
  sec: 3311
  time: '55:11'
  who: Alexey
- line: Yeah, I mean, right now we're thinking about using the Tableau dashboard and
    I have a proof of concept that I'm about to present to the EasyJet MLOps team.
    But before that, because I had already implemented a proof of concept, we weren't
    using Grafana – we didn't have the UI. To be honest, I had implemented a custom
    function that would trigger an email alert to the technical lead of the project
    in case there was data drift or model drift detected. It was, I think, two to
    three years ago.
  sec: 3325
  time: '55:25'
  who: Ioannis
- line: You mentioned Tableau, and it's interesting how versatile this tool is. [Ioannis
    chuckles and agrees] It's not just a dashboard, you can even build simple, rudimentary
    monitoring in Tableau. I remember we had problems with data quality and then our
    analyst quickly came up with a dashboard that shows how many records there are
    each day in the important tables. Then, what he did next was configure Tableau
    to send an alert if the number for one of the days was less than expected. He
    did that in like 30 minutes or something. That was amazing.
  sec: 3361
  time: '56:01'
  who: Alexey
- line: Okay. That's great. It indeed sounds amazing. Goodness.
  sec: 3404
  time: '56:44'
  who: Ioannis
- line: I mean, at the end, it's just a bunch of SQL queries and then knowing where
    to put these queries and which button to click to create an alert, he knew how
    to do this. Not everyone knows that. But it was a quick and dirty solution that
    worked pretty well. It's amazing.
  sec: 3407
  time: '56:47'
  who: Alexey
- line: Yeah, that's good. It's always exciting when someone delivers something that
    fancy in such a short period of time.
  sec: 3423
  time: '57:03'
  who: Ioannis
- header: Ioannis’ resource recommendations
- line: Yeah, I think we should be finishing soon. So maybe I'll ask you one thing.
    We talked a lot about communicating with business stakeholders, we also talked
    about Agile processes. We talked a little bit about MLOps. Are there any good
    resources that you can recommend to our listeners who want to learn more about
    these topics?
  sec: 3429
  time: '57:09'
  who: Alexey
- line: About which topic specifically?
  sec: 3456
  time: '57:36'
  who: Ioannis
- line: Well, about any of those that we discussed – let's say, about processes, about
    communicating with business stakeholders? When you were learning how to do your
    job well, maybe you came across some books or courses that helped you.
  sec: 3459
  time: '57:39'
  who: Alexey
- line: There is a single resource that I would recommend to every single aspiring
    data scientist/data analyst to watch out for. I'm not sure if you know Cassie
    Kozyrkov – she’s the Decision Intelligence Advocate for Google, at least she used
    to be – she resigned. But Cassie Kozyrkov and her course on YouTube, Making Friends
    with Machine Learning, I think, is the best resource out there, in order to understand
    how you can communicate technical details to a non-technical audience. I think
    the way she speaks and expresses these kinds of technical details in such a nice
    and direct way, is one of the best skills that someone can get. And I think, watching
    her YouTube videos helped me to really understand “What would be the best way
    to explain a technical term to someone that is not familiar with my world and
    data science in general?”
  sec: 3478
  time: '57:58'
  who: Ioannis
- line: I spent, I think, countless hours watching her videos, trying to analyze the
    way that she approaches things, terms, or explains how linear regression works.
    So if you want, Cassie Kozyrkov from Decision Intelligence from Google – her YouTube
    videos, Making Friends with Machine Learning. At least this is how to communicate
    to a non-technical audience. When it comes to technical details, I think different
    books like, Pattern Recognition from Gibson is one of the best books that you
    can go with. It's really heavy, so you have to make sure that you're comfortable
    with mathematics.
  sec: 3478
  time: '57:58'
  who: Ioannis
- line: In many senses – because I remember we used this book for my machine learning
    classes and it was heavy for the class too. [chuckles]
  sec: 3584
  time: '59:44'
  who: Alexey
- line: It was heavy, indeed. But I'm telling you, if you spend time and you actually
    focus – let's say you have a two-hour block of time and you go through that, it's
    one of the best things that you read to understand the mathematics behind machine
    learning and how it really works. Of course, LinkedIn helps a lot with different
    posts and resources that are being recommended. I think on a day-to-day basis,
    LinkedIn is my go-to resource website.
  sec: 3594
  time: '59:54'
  who: Ioannis
- line: Cassie… I think this is how I know her – from LinkedIn. I don't know if she's
    active anymore, but she used to be quite active on LinkedIn and this is where
    I went to see her content.
  sec: 3622
  time: '1:00:22'
  who: Alexey
- line: She is amazing, yeah – podcast, YouTube, LinkedIn, of course. I think she
    was all over the place. I think now she's building something on her own. This
    is why she left Google. And I'm really interested to see what this is going to
    be. I know this is about decision-making and decision intelligence, which is something
    she has established on her own. So yeah, I'm really looking forward to seeing
    her content.
  sec: 3636
  time: '1:00:36'
  who: Ioannis
- line: Yeah. Thanks, Ioannis, for joining us today, and for sharing all that you
    shared with us today. Yeah, it was amazing. Thanks for finding time. And thanks,
    everyone else, too, for joining us and being active here. I think… I actually
    forgot – we had only one question that I accidentally forgot to mention. Is it
    okay, Ioannis, if Dave reaches out to you on LinkedIn and asks this question?
  sec: 3660
  time: '1:01:00'
  who: Alexey
- line: Yeah, absolutely. I'm always open. I'm super active on LinkedIn. Any question,
    whatever that may be – feel free to reach out on LinkedIn and I’ll make sure to
    get back to you.
  sec: 3694
  time: '1:01:34'
  who: Ioannis
- line: Okay, thanks. And with that, I guess we’re finished.
  sec: 3707
  time: '1:01:47'
  who: Alexey
- line: Amazing. Thanks for having me!
  sec: 3711
  time: '1:01:51'
  who: Ioannis
- line: Yeah. Thanks. Bye, everyone.
  sec: 3714
  time: '1:01:54'
  who: Alexey
description: Discover MLOps tactics to prioritize data products, run A/B testing and
  enable model monitoring for faster validation, reliable rollouts and stakeholder
  buy-in.
---

Links:

* [LinkedIn](https://www.linkedin.com/in/ioannis-mesionis/){:target="_blank"}
* [Github](https://github.com/ioannismesionis){:target="_blank"}
* [Website](https://ioannismesionis.github.io/){:target="_blank"}