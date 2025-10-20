---

episode: 5
guests:
- nemanjaradojkovic
ids:
  anchor: atatalksclub/episodes/Machine-Learning-Engineering-in-Finance---Nemanja-Radojkovic-e2evai8
  youtube: Nl4aibeFwiI
image: images/podcast/s17e05-machine-learning-engineering-in-finance.jpg

description: "Learn ML engineering in finance. Discover financial ML applications, risk modeling, and building production ML systems for fintech."
links:
  anchor: https://podcasters.spotify.com/pod/show/datatalksclub/episodes/Machine-Learning-Engineering-in-Finance---Nemanja-Radojkovic-e2evai8
  apple: https://podcasts.apple.com/us/podcast/machine-learning-engineering-in-finance-nemanja-radojkovic/id1541710331?i=1000643322929
  spotify: https://open.spotify.com/episode/3yQtA8EAndau1yhCFPfwtj?si=ZutO4mLlRfOz_Zgw4GujiQ
  youtube: https://www.youtube.com/watch?v=Nl4aibeFwiI
season: 17
short: Machine Learning Engineering in Finance
title: Machine Learning Engineering in Finance
transcript:
- line: This week we'll talk about machine learning engineering in finances. And we
    have a special guest today, Nemanja. Nemanja was born and raised in Belgrade,
    Serbia, but since 2014, he's been living in Leuven, Belgium. He's an electrical
    engineer turned data scientist and then ML Ops engineer. This is what we'll talk
    about today, machine learning engineering and ML Ops. I met with Nemanja at an
    amazing conference in Porto. When was it?
  sec: 95
  time: '1:35'
  who: Alexey
- line: October 2023.
  sec: 131
  time: '2:11'
  who: Nemanja
- line: Yeah, it took a while to schedule this meeting. [chuckles] At the conference,
    he gave a talk about ML Ops and I also had the chance to interview him, among
    other people, on stage. It was the first time that I interviewed people live on
    stage. That was a super interesting experience. Today, we will finally get back
    to this discussion and talk about machine learning engineering, ML Ops, maybe
    Brazilian jiu jitsu and the purple belt. What else? So yeah, welcome!
  sec: 132
  time: '2:12'
  who: Alexey
- line: Thank you for having me.
  sec: 170
  time: '2:50'
  who: Nemanja
- header: "Nemanja\u2019s background"
- line: Before we go into our main topic of machine learning engineering in finances,
    let's start with your background. Can you tell us about your career journey so
    far?
  sec: 172
  time: '2:52'
  who: Alexey
- line: "Okay. It was a pretty, I would say, nonlinear career journey. I first obtained\
    \ my formal education in the domain of electrical engineering, as you already\
    \ mentioned, in Belgrade, Serbia, where I was born and raised. My first job was\
    \ actually as a salesperson. I was like a traveling salesman for some automation\
    \ equipment for industry \u2013 sensors and controllers and so forth. After that,\
    \ yeah, I realized I didn't want to stay in that career. I wanted to do something\
    \ more technical again."
  sec: 183
  time: '3:03'
  who: Nemanja
- line: "That's when I came to Belgium. I actually came to do a PhD in the domain\
    \ of bioengineering \u2013 switching from electrical engineering to sales, now\
    \ to bioengineering. There, I stayed for about a year and a half and I realized\
    \ that, again, academia is not really the place for me, because especially after\
    \ I worked a bit in the industry \u2013 we didn't click, let's say, together.\
    \ So that's why I wrote that I'm a PhD dropout. I stopped with the PhD and I moved\
    \ to Deloitte Consulting, here in Belgium. I stayed there for, I think, almost\
    \ three years, then switched to a smaller consultancy, called Dataroots \u2013\
    \ back then it was much smaller, now they grew a lot. [chuckles] Yeah, that was\
    \ also a very nice time."
  sec: 183
  time: '3:03'
  who: Nemanja
- line: "From then on, I went briefly on to ING. Sorry, I forgot to mention I work\
    \ for BNP Paribas \u2013 it was my first experience in the financial industry.\
    \ Then I worked for ING for a year and now, hopefully, I settled [chuckles] in\
    \ Europe. here in Brussels. This is a company which maintains the infrastructure\
    \ for trading securities. Basically, I think the easiest way to explain to people\
    \ what we do is \u2013 people usually know SWIFT, the company which you use to\
    \ send money internationally that maintains this network. Basically your money\
    \ hops between different banks and lands in the right place in the end. We are\
    \ like Swift, but for stocks and bonds. Big companies buy and sell stocks and\
    \ bonds through us. We also keep national bonds for many European countries like\
    \ Ireland. I don't know if it is in Belgium and France and so forth, I will make\
    \ a mistake here \u2013 I'm just the ML Ops guy [chuckles] the business guy."
  sec: 183
  time: '3:03'
  who: Nemanja
- line: "But yeah, this is where I am currently. I'm in some kind of ML Ops lead function,\
    \ I would call it like that, here in Europe, and I'm helping to increase the overall\
    \ ML Ops maturity of my current company. This is [what I\u2019ve been doing] for\
    \ the last five years. My title was usually a data scientist, but in practice,\
    \ I was an ML engineer. Now this is formalized with the title. We didn't call\
    \ it ML Ops five years ago, but it was just called \u201Cend-to-end machine learning/engineering\u201D\
    . That's it shortly \u2013 my short trajectory."
  sec: 183
  time: '3:03'
  who: Nemanja
- line: Back then, like, I don't think that even the role of ML engineer actually
    existed.
  sec: 365
  time: '6:05'
  who: Alexey
- line: "It did. I think\u2026"
  sec: 373
  time: '6:13'
  who: Nemanja
- line: "It was more like \u201Cdata scientist\u201D."
  sec: 374
  time: '6:14'
  who: Alexey
- line: "The first time my job was called \u201CML engineer\u201D was in 2019. And\
    \ I know it was the companies that wanted to differentiate, because \u201Cdata\
    \ scientist\u201D was and still is, I would say, a very vague term \u2013 it doesn't\
    \ mean a lot. People use it to describe many different things. But when you say\
    \ you're a machine learning engineer, it\u2019s pretty specific. You're not doing\
    \ stats \u2013 you're doing machine learning. You're not doing dashboarding, because\
    \ people hire data scientists and then get them to do the dashboards. So I like\
    \ this term, \u201Cmachine learning engineer,\u201D but still, I would consider\
    \ it a different role compared to a data scientist."
  sec: 375
  time: '6:15'
  who: Nemanja
- line: "Yeah, definitely. I want to add a few notes \u2013 I see questions. For some\
    \ people, it might be confusing, because here, today, in our community\u2026 by\
    \ the way, this for editors, please cut this later. Today, we actually have a\
    \ course launch. We are launching our data engineering course and I see people\
    \ who joined the stream today thinking that this is related to the course \u2013\
    \ it is not related. The course launch will happen at 5pm tonight. This is just\
    \ an interview. Sorry to disappoint you."
  sec: 415
  time: '6:55'
  who: Alexey
- line: It's not a waste of your time, you can stay. [chuckles]
  sec: 450
  time: '7:30'
  who: Nemanja
- line: "Yeah, this is a very good conversation \u2013 you will definitely learn a\
    \ lot \u2013 but it's not about data engineering, it's not about the course. This\
    \ is a podcast interview. Now I hope the current of people who joined will not\
    \ drop too much. [chuckles] Another thing I forgot to mention because it has been\
    \ a month since the last interview \u2013 I forgot to give a shout out to Johanna\
    \ Bayer, who helped prepare all these amazing questions that we will talk about\
    \ today. So thanks, Johanna, for your help. For editors, please move it before\
    \ the first question. [chuckles] Okay, now we continue."
  sec: 451
  time: '7:31'
  who: Alexey
- header: When Nemanja first work as a data person
- line: By the way, your first job as a data person was Deloitte, right?
  sec: 498
  time: '8:18'
  who: Alexey
- line: "I would already count the PhD because it\u2019s a job of a research and teaching\
    \ assistant, there was a lot of data science there already \u2013 systems modeling,\
    \ control. That's when I started using Python intensively. I was already doing\
    \ that before but this was when I was getting paid to do Python."
  sec: 504
  time: '8:24'
  who: Nemanja
- line: Okay. And Deloitte is a consulting company, right? You probably needed to
    speak French. [Nemanja disagrees] No?
  sec: 525
  time: '8:45'
  who: Alexey
- line: "No, actually not. In Belgium, not really. [chuckles] It's always advised\
    \ and I think it will certainly open up many more doors if you speak the local\
    \ language (in Belgium, it's Dutch and French, and you should speak English) but\
    \ for the more technical positions like technology consulting, it's okay if you\
    \ speak only English. But for certain clients \u2013 for example, if you're working\
    \ with the government \u2013 you need to be able to speak fluently."
  sec: 536
  time: '8:56'
  who: Nemanja
- line: For NATO, right. I remember this is where their headquarters are, right?
  sec: 565
  time: '9:25'
  who: Alexey
- line: Yeah, in Brussels is the NATO headquarters. Yeah.
  sec: 570
  time: '9:30'
  who: Nemanja
- line: "Yeah, I remember going from the city center to the IBM office and the NATO\
    \ building. It\u2019s huge."
  sec: 572
  time: '9:32'
  who: Alexey
- line: "Yeah, they have a new fancy building \u2013 an even fancier one."
  sec: 580
  time: '9:40'
  who: Nemanja
- line: Anyways. So you have worked at a variety of different companies, Deloitte,
    ING, Dataroots, BNP [Nemanja agrees] Now it's Euroclear, right? [Nemanja agrees]
    Most of them, if not all, involve finances and banking, right?
  sec: 585
  time: '9:45'
  who: Alexey
- line: "In the last four-five years, yes. So not all of them. But also with Deloitte,\
    \ you're a consultant, you switch fields relatively frequently. I was also in\
    \ the biomedical field\u2013 for the vaccines, GSK (GlaxoSmithKline) vaccines,\
    \ we also did projects with Amazon with Abebe, which is the industrial manufacturer.\
    \ So there was a lot of variety there, which takes time to mention. But yeah [chuckles].\
    \ Let's say I settled myself in the last four or five years in the financial industry.\
    \ That's important."
  sec: 603
  time: '10:03'
  who: Nemanja
- header: Typical problems that ML Ops folks solve in the financial sector
- line: So what are the typical problems that data scientists, machine learning engineers,
    or ML Ops folks usually solve in the financial sector?
  sec: 635
  time: '10:35'
  who: Alexey
- line: "You mean use cases. From the business perspective, I would say there was\
    \ a clear common line between all the companies where I was in the financial industry.\
    \ On one side, all of these companies have very strong regulations and they have\
    \ very strong compliance requirements. These fraud and money laundering cases\
    \ are always there \u2013 it's simply imposed, you have to do it. On the other\
    \ side, I think, where most of the business value comes from\u2026 For this compliance,\
    \ fraud, AML \u2013 you have to do it. If you don't do it, you have to pay billions\
    \ in fines. But it's an overhead that does not give some concrete added value\
    \ \u2013 it just saves you from a certain very big penalty that you have to pay.\
    \ On the other side, things that really give value in the financial industry are\
    \ so-called \u201Csmart automation projects\u201D."
  sec: 646
  time: '10:46'
  who: Nemanja
- line: "In essence, it's usually processing semi-structured and unstructured data,\
    \ like documents, emails, and so forth \u2013 whether it is information extraction:\
    \ extract an account number, extract the signature, route the email or a case\
    \ to the right department. It's also very important. All these companies have\
    \ a lot, a lot of people who are manually processing all these things, still.\
    \ There is still a lack of, I would say, proper forms for data information so\
    \ things are arriving in some kind of semi-structured (poorly structured formats).\
    \ Then you have a lot of parsing, a lot of interpretation, and so forth. So those\
    \ are the main things, I would say. Definitely, I think it's 80-90% of the cases\
    \ that we work on."
  sec: 646
  time: '10:46'
  who: Nemanja
- line: "So first is regulation compliance. If you don't do this, you get huge penalties,\
    \ so all the companies have to do that. [Nemanja agrees] They don't want to lose\
    \ money. Then the second category is more internal, right? I imagine\u2026 [cross-talk]"
  sec: 752
  time: '12:32'
  who: Alexey
- line: "Yeah, it\u2019s [things] like process efficiency. But in the end, it impacts\
    \ your customer as well, because if you are doing this, slowly, manually, your\
    \ whole case processing takes a lot of time. So the faster you can do it\u2026\
    \ I also didn't mention RPA. It's not something I do, but robotic process automation\
    \ is also very big in the financial industry. The thing that also connects all\
    \ these companies is that they were, in some way, all pioneers of this digital\
    \ era. They all had, very early, their mainframes and all the digital frameworks.\
    \ And this is now a bit of a curse."
  sec: 768
  time: '12:48'
  who: Nemanja
- line: "Because they have all these old systems \u2013 they were the first ones to\
    \ have all those systems. They have a lot of legacy code, they have a lot of legacy\
    \ infrastructure, and it's very hard to modify  or to improve many of these things.\
    \ They were not really built with enough forward thinking \u2013 in a forward\
    \ compatible manner. So now there's a lot of trouble that is caused by that fact."
  sec: 768
  time: '12:48'
  who: Nemanja
- line: "I imagine that there are also some customer-facing applications. Say I want\
    \ to make a transfer and I have an app \u2013 then I just take a picture of my\
    \ receipt and then\u2026 [cross-talk]"
  sec: 833
  time: '13:53'
  who: Alexey
- line: "Oh yeah. Mobile applications are also a big thing. Indeed. There, you see\
    \ a lot of variety? The mobile applications I mainly saw as a user, because I'm\
    \ currently using two banks in Belgium. I could see there's a big difference.\
    \ Some banks pick this really, I would call it, lean, simple approach, like ING\
    \ in Belgium and others, like the KBC bank, take a completely different approach\
    \ and really put everything in the app, literally. I think you can almost make\
    \ lunch for your kids in the app. [chuckles] You can pay for the parking, you\
    \ can pay for the train tickets, you can order food. You can do so many things\
    \ in the KBC app. And in the ING app, they just chose this, \u201COh, we just\
    \ give you the banking thing.\u201D They have their reasons, probably"
  sec: 847
  time: '14:07'
  who: Nemanja
- header: What Nemanja currently does as an ML Engineer
- line: "As an ML Ops person (ML engineer), what do you actually do? Because I imagine\u2026\
    \ We talked about more use cases, but as an ML engineer/ML Ops person, you don't\
    \ work on the model that recognizes the account details, for example. Right?"
  sec: 897
  time: '14:57'
  who: Alexey
- line: "Yes, correct. That was the second part that I wanted to say. On one side,\
    \ you have the typical business use cases, and on the other side, you have the\
    \ typical work of an ML engineer in finance, which is mainly, I would say, modernization.\
    \ It\u2019s mainly getting things to work. In general, an ML Ops engineer is a\
    \ person that, in my view, tries to abstract all the non-modeling parts of work\
    \ from the data scientists. My idea is that I want to be kind of like a service\
    \ to data scientists to make a kind of a platform or a framework so that they\
    \ can focus on the difficulties that they have in extracting the right entities\
    \ and making the right models. And then I basically handle all the rest. I give\
    \ them a standard project structure for the project, I am the one that makes the\u2026"
  sec: 917
  time: '15:17'
  who: Nemanja
- line: "By \u201Cthem\u201D you mean data scientists, or who?"
  sec: 972
  time: '16:12'
  who: Alexey
- line: Sorry, I didn't understand the question.
  sec: 976
  time: '16:16'
  who: Nemanja
- line: "Yeah. When you say, \u201CI give \u2018them\u2019,\u201D you\u2019re referring\
    \ to data scientists, right?"
  sec: 978
  time: '16:18'
  who: Alexey
- line: "Yeah, data scientists \u2013 we work together in a team. We usually have\
    \ two-three data scientists and an ML Ops engineer per project. We work together\
    \ \u2013 it's not like passing things over the fence. It's really working together\
    \ and reviewing the code together. Everything is very closely coupled. My part\
    \ is to create a repo, create the project structure, create the CI/CD pipelines,\
    \ figure out how they need to deploy, what will be the target deployment platform\
    \ for this \u2013 will it be a cluster or maybe we'll look into and select the\
    \ cloud model."
  sec: 984
  time: '16:24'
  who: Nemanja
- line: "One more thing to mention here as a side note, in the financial industry,\
    \ I think still mainly on-premise architecture. There are some movements towards\
    \ the cloud and, I would say, there\u2019s definitely a persistent direction there.\
    \ But still, there are a lot of core systems that are on-premise. For me, it's\
    \ also, \u201CWill we deploy on the cloud, or deploy on the on-premise cluster,\
    \ or on the OpenShift cluster?\u201D There's also networking, \u201CHow do you\
    \ open up certain firewalls for this application to communicate with this API?\u201D\
    \ And on and on. Those are the main things."
  sec: 984
  time: '16:24'
  who: Nemanja
- line: "So it sounds like it's more or less a typical job of an ML engineer, except\
    \ that you said that there is a lot of modernization work, which I don't know,\
    \ depends on the organization\u2026 [cross-talk]"
  sec: 1061
  time: '17:41'
  who: Alexey
- line: Yeah, definitely. I think the ML engineering role is like a software engineering
    role, which is very generic. [Alexey agrees] And the more you go to data science,
    the more it becomes business-specific. I can really see that I have very little
    exposure to the actual business side of all the projects, which I miss pretty
    much. When I was doing data science work, I was always much deeper into the communication
    with the business. But I can live in my bubble of code, [chuckles] and DevOps
    platforms. So yeah, it's pretty much similar, but yet, there is this thing of
    modernization, of change management, of seeing how to not fit ML Ops into the
    classical DevOps, because these companies have pretty established DevOps practices
    and governance. Now you need to see how to somehow integrate (how to smuggle in)
    ML into this whole thing.
  sec: 1075
  time: '17:55'
  who: Nemanja
- header: The obstacle of implementing new things in financial sector companies
- line: "And these existing DevOps practices, platforms, existing governance\u2026\
    \ What is there? I assume that it's not the most modern solutions. It's probably\
    \ time-proven things that\u2026 You mentioned OpenShift. [cross-talk]"
  sec: 1132
  time: '18:52'
  who: Alexey
- line: "It's really a mix of things. I think when they buy something, it's the newest\
    \ one. It's usually so. When they say, \u201CNow we're gonna go with this,\u201D\
    \ we take the best one. But that will probably not change over the next 10 years.\
    \ That's the thing. Things are slowly moving, slowly changing. I think just the\
    \ internal IT landscape is so big, that everything has a big impact and you already\
    \ have a lot of applications. To move, let's say, from one logging (centralized\
    \ logging) we have Splunk now. This is a modern solution, I would say \u2013 I\
    \ don't know if there's something especially better. But imagine if suddenly you\
    \ want to switch to another thing \u2013 that will be a big cost. That's, I think,\
    \ the main issue \u2013 the main obstacle there is the slowness and the whole\
    \ planning goes into big time windows."
  sec: 1152
  time: '19:12'
  who: Nemanja
- line: Is it specific to the financial industry? Or is it more about the traditional
    corporate environment?
  sec: 1209
  time: '20:09'
  who: Alexey
- line: "It's not in all corporate environments. Definitely not. I think it's very\
    \ specific to the financial industry. I think it\u2019s the case for any overregulated\
    \ industry \u2013 an industry which has very big involvement of regulators, of\
    \ governments, and international bodies. They are very, very risk averse. It's\
    \ better not to do something than to introduce some kind of risk. In these companies,\
    \ you also have all these trainings \u2013 every month or so, you have some kind\
    \ of risk training: how to spot risk, how to handle risk, how to manage\u2026\
    \ Risk, risk, risk. Risk mitigation everywhere. You learn to always think about\
    \ that."
  sec: 1217
  time: '20:17'
  who: Nemanja
- line: "Yeah, I remember I worked at UBS. That's a bank. I think it's \u201CUnited\
    \ Bank of Switzerland\u201D. Well, it doesn't matter. It\u2019s a financial Institution\
    \ \u2013 a very conservative institution. I was working there as a Java developer.\
    \ We would release every month. If a release doesn't go through that month, it\
    \ means it will go to the next month."
  sec: 1258
  time: '20:58'
  who: Alexey
- line: "Next month. Okay. We\u2019re not that rigid. [Alexey chuckles] For us, it's\
    \ release cycles. There's a whole department, called \u201Cchange and release\
    \ management\u201D. When you want to release something to production, you first\
    \ need a review from your own team to create this kind of change and to say which\
    \ exact commit (which exact build) you will release. You need to show that it\
    \ was first released with a test, and that it worked and that this was released,\
    \ let's say, at least a week before the release to prod \u2013 that it was properly\
    \ tested."
  sec: 1281
  time: '21:21'
  who: Nemanja
- line: Then you have some three different teams where one person from that team needs
    to approve. But if it fails, you can do a rollback. There's a procedure to do
    a rollback. And you can have an emergency change if you need a bug fix. To do
    something, you can have an emergency change. Of course, you need to follow the
    procedure for the emergency change. [chuckles] The important thing is that, in
    the end, you always know what is in production, who put it there, and when they
    put it there.
  sec: 1281
  time: '21:21'
  who: Nemanja
- header: Going through the hurdles of DevOps
- line: Okay. So these are the existing DevOps practices and the governance framework
    that you mentioned, right? [Nemanja agrees] Which sounds like a bit of a hassle,
    to be honest. But there are reasons for that, right?
  sec: 1345
  time: '22:25'
  who: Alexey
- line: "It slows you down. But I would say, you learn how to do it \u2013 you learn\
    \ how to do it quickly. Every time, it's faster. The first time you do it, people\
    \ don't know you. It's all about people\u2019s trust. The first couple of times\
    \ people are really looking at your pull requests in detail. \u201CWhat is this\
    \ guy doing? Who is this guy? What does his code look like?\u201D And every next\
    \ time, when you start deploying frequently, you get all these approvals much\
    \ faster, because people say, \u201COkay, this guy never crashed anything. There\
    \ were no incidents,\u201D and so forth."
  sec: 1361
  time: '22:41'
  who: Nemanja
- line: "You know who to ping \u2013 it's the little people connections \u2013 you\
    \ really know who to ask on MS Teams, \u201CHey man. I have this change. Can you\
    \ please approve?\u201D Lately, this was not really an obstacle. In these corporations,\
    \ it's always\u2026 You need to help people. After a couple of years, you become\
    \ really productive when you really make your network. Then things start going\
    \ very fast."
  sec: 1361
  time: '22:41'
  who: Nemanja
- line: Yeah. I imagine that, since there are these processes that were set up ages
    ago, that they're thought through, and they exist for a reason. And you, as an
    ML engineer/ML Ops person, need to stick to these processes, right? You work on
    ML Ops, you work on these machine learning pipelines, CI/CD pipelines, or whatever,
    and what you do needs to stick to the guidelines from the DevOps people. [Nemanja
    agrees] How difficult is this? How difficult was it to map the ML Ops processes
    to this DevOps framework?
  sec: 1419
  time: '23:39'
  who: Alexey
- line: "Well, I would say that we are still not fully not where I want us to be.\
    \ Definitely. There's still improvement to be made. But it's a journey. As I said\
    \ just a moment ago, it was hard at the beginning. But luckily\u2026 I mean, I\
    \ did not come into an empty room. There were already people in the company who\
    \ did a lot of previous deployments, so we \u201Cpiggybacked\u201D for a while\
    \ on the team of data engineers who were doing really frequent deployments. They\
    \ explained and they guided us through the whole process until we became independent\
    \ enough to do it ourselves. You know what we say, \u201CA living person gets\
    \ used to everything.\u201D [chuckles] This is also true here."
  sec: 1462
  time: '24:22'
  who: Nemanja
- line: "You stop noticing it at some point. When I talk to somebody from a startup\
    \ and they hear, \u201COh, you have to do all these things.\u201D For us, it's\
    \ no longer something that is an issue. It's like, \u201COkay, this is how you\
    \ do it.\u201D It's more like muscle memory \u2013 you click here, you make this,\
    \ you prepare that, and you go to production. I heard much worse stories from\
    \ certain companies, where you have to literally have a sheet of explanations\
    \ for every little change, and then you need to have a JIRA ticket source and\
    \ ServiceNow TFS tickets \u2013 doesn't matter. There is much more bureaucracy\
    \ in certain other places, so I think we have a decent sweet spot here."
  sec: 1462
  time: '24:22'
  who: Nemanja
- line: "Yeah. I remember\u2026 Back to my UBS experience. To be fair, it was a long\
    \ time ago. It was 10 years ago or more. There is a comment that says, \u201C\
    Today, in finance, CI/CD is a part of the daily routine,\u201D which is a good\
    \ thing. It\u2019s everywhere now. But I remember one thing that we were super\
    \ careful with, which was the open source tools that we used. We had to do these\
    \ things you mentioned, but instead of every change \u2013 say we wanted to introduce\
    \ a new open source package that wasn't used before (a library) \u2013 we had\
    \ to write an explanation why this library would be applied. Is it a good license?\
    \ Do you have [something like that]?"
  sec: 1555
  time: '25:55'
  who: Alexey
- line: "Yes. There is [something like that] to a certain extent. But currently, the\
    \ default is \u2013 we have Artifactory, which is an internal package registry,\
    \ JFrog Artifactory \u2013 and it mirrors the public pipeline. I think only if\
    \ it registers some kind of a critical vulnerability, then it is going to blacklist\
    \ a certain package. Recently, there was a situation where I wanted to ask for\
    \ another package index \u2013 not a package from PyPI, but it was a separate\
    \ index. There, I had to give an explanation. But it was a short chat with the\
    \ person that was in charge of this. I could really just fill out a form and then\
    \ it worked. So it was not too hard."
  sec: 1604
  time: '26:44'
  who: Nemanja
- line: "I imagine that if you want to use PyArrow instead of plain Pandas, you don't\
    \ need to\u2026 [cross-talk]"
  sec: 1648
  time: '27:28'
  who: Alexey
- line: No, it's okay. We don't have an issue with that. Yeah. But if it's a completely
    separate thing, which is not on any kind of a public repository, then you have
    to justify why you need to manually import something. Yeah.
  sec: 1656
  time: '27:36'
  who: Nemanja
- header: Working with an on-premises cluster
- line: "How difficult is it to work on-premise? I imagine that there is this OpenShift\
    \ cluster and then, I guess, there are all these procedures, standards, templates\u2026\
    \ It should be pretty smooth, right?"
  sec: 1671
  time: '27:51'
  who: Alexey
- line: "Yes. Currently, we are working mainly on a classical, I would say, Hadoop\
    \ cluster. There's the OpenShift cluster, but there is something next to it. We're\
    \ not currently deploying there. But yeah, there is a certain project structure\
    \ for deployment there. There is a standard pipeline if you want to go there.\
    \ So it's pretty much already ironed out by the data engineers before us, and\
    \ we are just reusing that same approach. Working on premise is\u2026 I don't\
    \ know."
  sec: 1686
  time: '28:06'
  who: Nemanja
- line: "I like it. It's really close to the metal \u2013 it's simple, in a way. You\
    \ have the machine, you have the operating system, and you don't have all these\
    \ disarrays of services that you have on the cloud. They are also helpful in many,\
    \ many cases, but\u2026 You get to learn a lot about Linux. You get to learn a\
    \ lot about bash scripting, about networking, SCPing, SSHing, and these things.\
    \ Yeah, I like it. I got used to it. But I would say that it\u2019s much simpler\
    \ in some ways, but it requires, I would say, more knowledge of computers and\
    \ operating systems \u2013 Linux and networking. But that's the main difference."
  sec: 1686
  time: '28:06'
  who: Nemanja
- line: "But do you actually need to order hardware? [Nemanja disagrees] I imagine\
    \ that you want a new thing\u2026 [cross-talk]"
  sec: 1764
  time: '29:24'
  who: Alexey
- line: "No. Not my team, my team. There's a whole\u2026 The thing is, on-premises\
    \ requires a team to maintain the infrastructure. [Alexey agrees] That's the main\
    \ deal with smaller companies, I would say, is that they would have to hire somebody\
    \ to maintain a data center. For smaller companies, it's a problem. For bigger\
    \ companies, especially in the financial industry, that's really not a problem.\
    \ I think that's the main attractiveness of cloud \u2013 that you can easily start\
    \ and have some kind of a data center (a rented one) and then you can expand it\
    \ and so forth."
  sec: 1770
  time: '29:30'
  who: Nemanja
- line: "But recently, there was a certain number of machines being added. Or you\
    \ say, \u201COh, I don't have the capacity,\u201D and there's a whole team that\
    \ manages that. So there's a platform engineering team. You say, \u201CGuys, this\
    \ is what we need. Here\u2019s the money. [chuckles] Please do the work.\u201D\
    \ And they just tell you, \u201COkay, now you have all these machines added. Include\
    \ them in the pipeline.\u201D That's it."
  sec: 1770
  time: '29:30'
  who: Nemanja
- line: "For your needs, you can just assume that it kind of works like cloud \u2013\
    \ when you need resources, you will have them \u2013 unless it's super gigantic\
    \ that you need to ask in advance."
  sec: 1825
  time: '30:25'
  who: Alexey
- line: "Yeah. In a way, it's like cloud, but you don't click and make things \u2013\
    \ you ask people. You have to make a request to people and they do these things\
    \ for you. Usually, that's also one of the things, to find the right request to\
    \ make, to know who is in charge of what and where \u2013 that's a bit of a journey\
    \ to learn and understand."
  sec: 1837
  time: '30:37'
  who: Nemanja
- header: "\u201CML Ops on a Shoestring\u201D (You don\u2019t need fancy stuff to\
    \ start w/ ML Ops)"
- line: "So we met in Porto at a conference, Data Makers Fest, and you gave a talk.\
    \ [Nemanja agrees] It was a very nice talk. I attended that talk. I think I was\
    \ even a moderator. I don\u2019t remember. [chuckles] [Nemanja agrees] Yeah. In\
    \ that talk, you showed that you don't need a lot of fancy stuff to start with\
    \ ML Ops, right? [Nemanja agrees] Can you maybe give us the main ideas from that\
    \ talk? It was also interesting for me personally. How did you arrive at this\
    \ idea and why? What caused you to come up with that?"
  sec: 1862
  time: '31:02'
  who: Alexey
- line: "Yeah. It connects with my experience in the financial industry. The title\
    \ of the talk was \u201CML Ops on a Shoestring\u201D. I think now, since two days\
    \ ago, it's available on YouTube \u2013 if you just Google \u201CData Makers Fest\
    \ Nemanja\u201D\u2026"
  sec: 1899
  time: '31:39'
  who: Nemanja
- line: We'll put it in the description.
  sec: 1915
  time: '31:55'
  who: Alexey
- line: "Yeah. It\u2019s there. Basically, the idea was, as I say there, we all operate\
    \ on a certain budget. This can be a time budget, it can be a money budget, or\
    \ a people budget and so forth. If you're in a larger organization and you want\
    \ to implement ML Ops, you need some kind of a prioritization scheme, or some\
    \ kind of prioritization exercise. That talk was about that, \u201CHow do you\
    \ start? What would be the minimal set of ML Ops features \u2013 of environments,\
    \ of components \u2013 that you need to implement in order to say, \u2018Okay,\
    \ now we're doing some kind of ML Ops.\u2019\u201D If I remember correctly \u2013\
    \ I don't want to repeat the whole talk here. [chuckles]"
  sec: 1917
  time: '31:57'
  who: Nemanja
- line: "In general, we said, \u201COkay. First thing, you need to have a development\
    \ environment and a production environment.\u201D That's the basic thing. \u201C\
    Ideally, you should have a test environment, so that you can independently develop,\
    \ independently productionize, and independently test.\u201D In the middle, as\
    \ the central control tower, you do have a DevOps platform, where you integrate\
    \ all your code, where you launch, where you have the whole audit trail of all\
    \ the changes of what anybody did. I remember, I called it then, the \u201Ccover-your-ass\
    \ Ops,\u201D basically, in order to play the Git blame game, ultimately. Next\
    \ to that, you need to have, I would say, as the very bare minimum, some kind\
    \ of a monitoring solution to know if your application is alive. [chuckles] If\
    \ it just dies, it will not tell you that. You need to have a model registry and\
    \ you need to have some kind of a version data registry. I think that was one\
    \ of the things I stressed two times."
  sec: 1917
  time: '31:57'
  who: Nemanja
- line: "This is also something where it's often an afterthought \u2013 we don't often\
    \ realize that data produces code and that not versioning data means not versioning\
    \ your code in ML. So that was one of the things if you want to have, what I then\
    \ called, \u201Cthe crown jewel,\u201D which is having reproducible ML pipelines.\
    \ Why are reproducible ML pipelines necessary? Not because you will actually have\
    \ to reproduce a model. I never had to reproduce a model a year later or anything\
    \ \u2013 that was never a requirement. They always say, \u201CYeah, we should\
    \ be ready to reproduce a model,\u201D but actually, if you can reproduce a model,\
    \ that means you have control over your ML process. That's the main thing. That\
    \ just proves that you know what you're doing. And if you cannot reproduce anything,\
    \ then who knows what's in production? That was the main thing. I did not say,\
    \ \u201COh, you should do it like this and you should stop here.\u201D [chuckles]\
    \ But if you had to choose the minimum set of ML Ops components, that was my proposal."
  sec: 1917
  time: '31:57'
  who: Nemanja
- line: But not only that. Now, if somebody has not seen the talk, and listens to
    us talking about that, they imagine this complex thing with all these tools that
    do all the things that we mentioned. But what you showed us in the talk was that
    these components, although they sound complex, they're actually not. You can start
    super simple.
  sec: 2080
  time: '34:40'
  who: Alexey
- line: "Yeah. For example, the model registry can be just an S3 bucket. And that's\
    \ okay for beginnings. I like this. This is more like what they call \u201Ca consultancy\
    \ talk\u201D. I learned recently (well, not recently) a term they call a \u201C\
    tactical solution\u201D. It's basically an ugly solution which works, until you\
    \ reach your \u201Cstrategic solution\u201D. That's why it's called \u201Ctactical\u201D\
    . What you really want is MLflow or Databricks, but in the meantime, you have\
    \ just some kind of a mess of Excel files or something. When you call it a tactical\
    \ solution, it immediately sounds like a solution and like something \u201Ctactical,\u201D\
    \ something clever and thought out. You know? So I would say this S3 bucket is\
    \ a good tactical solution for a model registry, and also for versioning data\
    \ and whatever."
  sec: 2105
  time: '35:05'
  who: Nemanja
- header: Tactical solutions
- line: "Yeah, I love how it sounds, \u201Ctactical solution\u201D. [chuckles] You\
    \ would call this a \u201Ctemporary solution\u201D but then, five years later,\
    \ it's still there. [chuckles] Because\u2026 [cross-talk]"
  sec: 2157
  time: '35:57'
  who: Alexey
- line: "There's a famous quote. They say, \u201CThere's nothing more permanent than\
    \ temporary solutions.\u201D"
  sec: 2166
  time: '36:06'
  who: Nemanja
- line: "Yeah. So, \u201CThere is nothing more strategic than a tactical solution.\u201D\
    \ [Nemanja chuckles] That's nice. So what led you to this idea? What is your experience\
    \ [that led] to give this talk? What did you see in your experience that caused\
    \ you [to think of this]?"
  sec: 2172
  time: '36:12'
  who: Alexey
- line: "As I said, I work in the financial industry, where you're moving very slowly.\
    \ Imagine that you have a bunch of bad guys and every bullet costs you 10,000\
    \ euros. You need to think very carefully how you're gonna use your ammo. That\
    \ was the thing, \u201CWhat is the bare minimum so that you just tick the boxes\
    \ and can say, \u2018Okay, I\u2019m safe. My process is controlled. I have reproducible\
    \ training. And then I will move forward to user experience and have a nice dashboard.\u2019\
    \u201D For example, if you need to implement monitoring \u2013 your boss says,\
    \ \u201CHey, do we have monitoring of our ML models?\u201D At the very minimum,\
    \ you need to have some kind of log of your models and of their predictions, even\
    \ if it's in a text form. You can spin up a Jupyter notebook and analyze that.\
    \ But if you don't have that, then nothing \u2013 no Power BI fancy dashboard\
    \ \u2013 will help you. So start from the very bare minimum to cover your butt,\
    \ and then move forward to the fancy things and making your life easier."
  sec: 2190
  time: '36:30'
  who: Nemanja
- line: "So the idea here, if I try to summarize it, is to kind of close the loop\
    \ on the process as far as possible, so you have a process there\u2026 [cross-talk]"
  sec: 2261
  time: '37:41'
  who: Alexey
- line: "Yeah, you need to have a complete framework in a simple manner. In Agile,\
    \ that whole thing\u2026 I don't really Agile\u2026 [chuckles] I don\u2019t call\
    \ it Agile \u2013 we call it \u201Cthe prototyping approach\u201D, which means\
    \ you make a first end-to-end prototype, and then you iterate and improve bits\
    \ and pieces. As a whole, it needs to be\u2026 you cannot have a Porsche without\
    \ one tire. You have the fancy doors, you have the fancy motor, but without one\
    \ tire, it's not gonna go. So first make it operational and then pimp it. [chuckles]"
  sec: 2271
  time: '37:51'
  who: Nemanja
- line: "Yeah, I like\u2026 Agile \u2013 I mean, it's good to be able to start. Let's\
    \ say, there is a new team, and you want to make sure the processes are there,\
    \ so that what people are doing is not chaotic, right? So you establish the framework,\
    \ you start using it and then you make it complex as you grow \u2013 as you become\
    \ more mature."
  sec: 2306
  time: '38:26'
  who: Alexey
- line: "Yeah, but I would say that the main issue I have with Agile is that it forces\
    \ you, in a way, to try to make something\u2026 I would call it \u201Cdemo-driven\
    \ development\u201D. You need to immediately have something to show. I think it\
    \ forces you, in a way, to create some kind of technical debt because you want\
    \ to make something quick and dirty and you're thinking from demo to demo if your\
    \ sprint is like two weeks. I think the beginning of a project should start in\
    \ some kind of\u2026 not \u201Cwaterfall mode\u201D, but something like, \u201C\
    Okay, let's set it up. Let's set up the groundwork.\u201D If you're building a\
    \ bridge, you cannot first throw a log over the river and then build a bridge\
    \ on top of that log. You need to do a lot of groundwork and things \u2013 you\
    \ cannot do it in sprints. Many things\u2026 You also have the standard \u2013\
    \ you know the diagram that they show in Agile training? You first have a tricycle,\
    \ then you have a bicycle, then you have a car, and you have an airplane. What\
    \ I always ask is, \u201COkay, have you ever seen an airplane that started as\
    \ a tricycle?\u201D It doesn't exist, you know? At one point you had to break\
    \ down the whole tricycle and make an airplane. So I think that's a bit of\u2026"
  sec: 2328
  time: '38:48'
  who: Nemanja
- line: "I see what you mean. We can just say that everyone can deploy whatever they\u2019\
    re working on to production. It's kind of a process, right? But does it bring\
    \ us anywhere? So you need to\u2026 [cross-talk]"
  sec: 2403
  time: '40:03'
  who: Alexey
- line: "What can you really know about a complex problem in two weeks?  [Alexey agrees]\
    \ I mean, there are so many things to explore. I think you can use it to set up\
    \ some kind of\u2026 If it's like the fifth project you're doing \u2013 if you're\
    \ doing some kind of mobile app or something, where you know that 50-60% of it,\
    \ you can already start and do it, and then later, you will tweak the GUI or something.\
    \ Fine. But in machine learning, so many times, you start \u2013 it takes you\
    \ a month to get the data, to understand the business, to do this and that. On\
    \ my ML Ops part \u2013 okay, I can immediately make the project, I can make CI/CD\
    \ pipelines, I can make the API function, and then have a \u201CHello World\u201D\
    \ model \u2013 say hello from the API. But then it's going to wait for a month\
    \ or two for a concrete model to sit in there. So certain parts, yes, but the\
    \ exploratory research and development things\u2026 I don't think they fit very\
    \ well into the whole agile philosophy."
  sec: 2414
  time: '40:14'
  who: Nemanja
- line: "So that\u2019s why you have two-three data scientists per one ML engineer?"
  sec: 2474
  time: '41:14'
  who: Alexey
- line: Usually, yes.
  sec: 2476
  time: '41:16'
  who: Nemanja
- line: Because doing the data science stuff takes more time.
  sec: 2478
  time: '41:18'
  who: Alexey
- line: "Yeah, indeed. Indeed. Because there is\u2026 My work is usually more reusable.\
    \ They all develop similar models, but they all have to go and talk to other people\
    \ in the business and understand their needs \u2013 back and forth, back and forth.\
    \ They have many more meetings with the business people than I do. I don't have\
    \ meetings with the business people. I just talk to the data scientists. Yeah,\
    \ there's the data, there's the cleaning, the understanding \u2013 this iterative\
    \ process is much more. For me, it's pretty exact \u2013 my API works or it doesn't\
    \ work. It doesn't deploy or doesn't start. I don't need another person's opinion\
    \ to know if my API works \u2013 or authentication or whatever. That's my fortune,\
    \ I would say. [chuckles]"
  sec: 2484
  time: '41:24'
  who: Nemanja
- line: "So if I overly simplify it, then \u2013 let's say you have three data scientists.\
    \ After a month of work, they come in with three models, but your role here is\
    \ to make sure that all these three models can be deployed in a similar fashion.\
    \ These three models are different \u2013 they solve very different business problems\
    \ \u2013 but your role is to make sure that there is one platform (one piece of\
    \ infrastructure, whatever) where all these three models can easily fit. For you,\
    \ it doesn't matter what this model is doing."
  sec: 2534
  time: '42:14'
  who: Alexey
- line: "Indeed. I mean, we agree from the beginning. We say, \u201COkay, let's see.\
    \ You want to use spaCy? Do you want to use Scikit Learn, PyTorch?\u201D and whatnot.\
    \ Then we immediately start to accommodate their approach, their ML frameworks,\
    \ in this overall framework. Also, a lot of my work is really code review \u2013\
    \ ML code review \u2013 because you don't want just any kind of code. For data\
    \ pipelines, I try to make sure that they are always modular, that they are testable,\
    \ that they're not just one giant script. So there's really a lot of interaction.\
    \ And it's not really a one way process. Because also when I have my own pull\
    \ requests, I also submit them to review for them, because they also use Python.\
    \ They also helped me sometimes spot mistakes in my code. So yeah, it's really\
    \ teamwork in that sense."
  sec: 2565
  time: '42:45'
  who: Nemanja
- header: Platform work and code work
- line: Do I understand correctly that you have two categories of work? You have the
    platform work and then you also have the code standardization, code review work,
    [Nemanja agrees] where you help data scientists with their projects. Then in addition
    to that, you maintain the platform where data scientists can deploy.
  sec: 2619
  time: '43:39'
  who: Alexey
- line: "Well, I don't really maintain the platform. My main work \u2013 what I actually\
    \ create in this company \u2013 the approach and\u2026 I maintain the applications\
    \ in production. I\u2019m the one who deploys, and I'm the one who pays attention\
    \ if there's alerts (if something doesn't work), I go there, and I need to fix\
    \ something. That's what I do. It's not their problem. But the platform is, in\
    \ terms of hardware, it's not part of my work. But I also something\u2026 [cross-talk]"
  sec: 2640
  time: '44:00'
  who: Nemanja
- line: More like an approach.
  sec: 2665
  time: '44:25'
  who: Alexey
- line: Sorry?
  sec: 2666
  time: '44:26'
  who: Nemanja
- line: "It\u2019s more like not physical\u2026 It\u2019s more like an approach."
  sec: 2665
  time: '44:25'
  who: Alexey
- line: "Indeed. Yes. There's also a library, which I maintain with my fellow ML Ops\
    \ colleague, which\u2026 We created this library, which is like a framework on\
    \ top of FastAPI, which then also allows for the creation of new projects. We\
    \ saw, \u201COkay, every other project, we're doing this.\u201D So we put it all\
    \ in one library so that tomorrow, data scientists could maybe even independently\
    \ create a whole API with their model. That'll be some kind of ultimate goal."
  sec: 2672
  time: '44:32'
  who: Nemanja
- header: Programming and soft skills needed to be an ML Engineer
- line: "I noticed that we have quite a few questions from the audience. Question\
    \ number one and two \u2013 I'll combine them. \u201CWhat kind of programming\
    \ skills and soft skills do you need to have as an ML engineer?\u201D"
  sec: 2704
  time: '45:04'
  who: Alexey
- line: "I think ML engineering is, first and foremost, more on the hard skill side.\
    \ I think it's very close. It's very distant from data science, I would say. I\
    \ think it's useful to know data science because you need to talk to data scientists\
    \ \u2013 they are your clients, let's call it like that. [chuckles] But I would\
    \ say python programming. If you're in the cloud, then knowing the cloud services\
    \ of that specific cloud you're working on. If you're on-premises, then it's Linux\
    \ commands, bash scripting, networking (a bit of networking \u2013 you don't have\
    \ to be an expert, but you have to be able to survive in that environment). So\
    \ that's why I'm just working on the projects."
  sec: 2719
  time: '45:19'
  who: Nemanja
- line: "But I think soft skills are also important for this \u201Cchange work\u201D\
    , I would call it \u2013 if you want to bring something new to your company, and\
    \ you want to raise the maturity of ML Ops in your company, you need to have this\
    \ kind of \u201Cevangelical\u201D [chuckles] trait to go around\u2026 \u201CMissionary\u201D\
    \ or what do you call it \u2013 you need to go around and talk to people and bother\
    \ people and ask and pull their sleeve, and you need to be persistent. Then, ultimately,\
    \ [you need to be] a nice person \u2013 not get into conflicts with people because\
    \ you're annoyed [chuckles] that something doesn't exist. [cross-talk]"
  sec: 2719
  time: '45:19'
  who: Nemanja
- line: "But just in case\u2026 You have Brazilian jiu jitsu."
  sec: 2800
  time: '46:40'
  who: Alexey
- line: "[laughs] That will be the end of the story. [both laugh] I will not get anything\
    \ \u2013 I will not get a simple Python pipeline in the end. [chuckles] But yeah,\
    \ I think these skills are important to create change in any kind of organization\
    \ \u2013 to be able to build networks, and present things. If you want to get\
    \ a certain kind of\u2026 Let's say you want to get the fancy vendor-based project,\
    \ sorry\u2026 All registry \u2013 You need to convince your boss and your boss\
    \ speaks business language."
  sec: 2804
  time: '46:44'
  who: Nemanja
- line: "So that\u2019s something I want to make a talk out of \u2013 how to change\
    \ organizations, and how to really sell internally certain technology solutions,\
    \ and how to fight for those things. One of the main things, I think, is to align\
    \ your goals with the goals of your superiors and to speak their language. As\
    \ I said, in the financial industry, it's about risk. So if you can show how your\
    \ solution reduces risk, for example, for the company, that's what they like to\
    \ hear. That's what they can sell upwards. So you need to help them sell that\
    \ upwards. I think those are the main skills."
  sec: 2804
  time: '46:44'
  who: Nemanja
- line: That sounds like your skills (your experience) working as a salesperson helps,
    right?
  sec: 2882
  time: '48:02'
  who: Alexey
- line: "Yeah, a bit. A bit. That helps. Consulting also helps, because in consulting,\
    \ there's a lot of sales also. In consulting, you have a day job of implementing\
    \ the things you need to do and then you have a lot of work in selling new proposals\
    \ to new clients and explaining how you bring value, how you do this and that.\
    \ There's always this translation work there. If you just talk about technology,\
    \ nobody cares. I mean, nobody cares \u2013it's always hard to follow. But if\u2026\
    \ [cross-talk]"
  sec: 2889
  time: '48:09'
  who: Nemanja
- line: "Data scientists maybe care, but if you talk about top management, they care\
    \ about\u2026 [cross-talk]"
  sec: 2917
  time: '48:37'
  who: Alexey
- line: "The people that open up the purse to pay for your solution, they want to\
    \ know, \u201CHow will you make me sleep better at night?\u201D I think that's\
    \ [chuckles] the main thing."
  sec: 2921
  time: '48:41'
  who: Nemanja
- header: The challenges of transitioning from and electrical engineering and sales
    to ML Ops
- line: "Okay. There is an interesting question from Debora, which\u2026 We talked\
    \ about sales a little bit. \u201CWhat was the most challenging aspect of transitioning\
    \ from doing sales and doing electrical engineering, to a machine learning role,\
    \ especially in terms of technical skills?\u201D"
  sec: 2935
  time: '48:55'
  who: Alexey
- line: "Well, I think for me, the sales part was more of a deviation, in a way. My\
    \ formal education in electrical engineering was\u2026 I already had machine learning\
    \ there. I already had a bit of python. Electrical engineer, in the domain of\
    \ signals and systems \u2013 so it's systems modeling, which is something I already\
    \ did there. \u201CMachine learning\u201D was still an emerging term, but then\
    \ later, when I started doing machine learning, I was like, \u201COh wait, I know\
    \ these things.\u201D [chuckles] We have the mathematics, the signal modeling,\
    \ single processing, control \u2013 on top of that, we did control, \u201CHow\
    \ do you go from modeling the system to controlling the system?\u201D Which is,\
    \ I would say, an extra next step."
  sec: 2952
  time: '49:12'
  who: Nemanja
- line: "I can\u2019t say that I had some kind of a big struggle and battle to get\
    \ into it. Maybe the hardest thing for me was understanding this probabilistic\
    \ way of thinking. Because most of my engineering was pretty exact \u2013 you\
    \ calculate a number, and you calculate a solution to this. Then to understand\
    \ distributions, and how, for example, you add two probabilities \u2013 I still\
    \ remember that I just could not get my head around it. When you have one distribution\
    \ and another distribution, if you add it together, is it one of the top of the\
    \ other? [chuckles] What does it look like? I remember, I was actually arguing\
    \ with my professor and I was wrong. [laughs] I was convinced he's wrong. [chuckles]\
    \ But he found a gentle way to tell me, \u201CNo.\u201D [chuckles]"
  sec: 2952
  time: '49:12'
  who: Nemanja
- line: That's why that person is a professor. Right?
  sec: 3047
  time: '50:47'
  who: Alexey
- line: Yeah. It could have come to my mind, maybe. But no, I was so convinced that
    he was wrong. [chuckles]
  sec: 3050
  time: '50:50'
  who: Nemanja
- line: "But sometimes it also helps not to\u2026 How do you say it\u2026? \u201C\
    Put anyone on a pedestal.\u201D [Nemanja agrees] Just because of their formal\
    \ role."
  sec: 3057
  time: '50:57'
  who: Alexey
- line: "Yeah, indeed. But this guy doesn't\u2026 [cross-talk]"
  sec: 3064
  time: '51:04'
  who: Nemanja
- line: "It doesn\u2019t mean that they are right, right?"
  sec: 3067
  time: '51:07'
  who: Alexey
- line: Yeah. Yeah.
  sec: 3069
  time: '51:09'
  who: Nemanja
- line: "I guess for you, this sales role \u2013 this deviation that you mentioned\
    \ \u2013 it was more difficult than the transition."
  sec: 3070
  time: '51:10'
  who: Alexey
- line: "Yeah. It's like a first job. I was like, \u201COkay, let's do something,\
    \ whatever.\u201D It's close to sales of the technical equipment. What I should\
    \ have programmed, I was just telling that. And I was good at that because I was\
    \ not a typical sales guy \u2013 because I was like a \u201Cnerdy\u201D guy that\
    \ actually knew the equipment. I actually knew what they needed to do with that.\
    \ Then the technical guys I was selling it to were like, \u201COh, you really\
    \ know something. Oh, you have a degree!\u201D [chuckles] [cross-talk] \u2026\
    configure, and I even helped them solve technical problems with that equipment\
    \ and that's something they appreciate. I would say, if we're talking about business-to-business\
    \ sales, like this was, it's very important to work on long-term relationships,\
    \ and not just push, push, push to sell. This means even to decline a sale if\
    \ you really think it's not solving somebody\u2019s problem."
  sec: 3079
  time: '51:19'
  who: Nemanja
- line: "But I imagine that the work of electrical engineers is not actually soldering\
    \ components, but more like\u2026 a computer, right? [chuckles][Nemanja agrees]"
  sec: 3135
  time: '52:15'
  who: Alexey
- line: "That's an electrician. That's an electrician. Electrical engineers \u2013\
    \ I mean, you have the power line, you have the high voltage electricity, you\
    \ have microelectronics, you have physical electronics\u2026 Biomedical engineering\
    \ was also there, so we learned about medical imaging, for example. That's also\
    \ a very interesting domain. Not soldering."
  sec: 3144
  time: '52:24'
  who: Nemanja
- header: The ML Ops tech stack for beginners
- line: "[chuckles] Okay. Another question, \u201CWhat is the general tech stack for\
    \ machine learning for a novice/beginner?\u201D"
  sec: 3171
  time: '52:51'
  who: Alexey
- line: What's the question? Can you repeat?
  sec: 3179
  time: '52:59'
  who: Nemanja
- line: "Yeah. The question is, \u201CWhat is the tech stack for machine learning\
    \ for a novice/beginner?\u201D I'm just wondering. It's quite a broad question.\
    \ I guess the question is asking, \u201CWhat kind of technology [do you need to\
    \ know] if you're a beginner in machine learning?\u201D Tech stack. [cross-talk]"
  sec: 3182
  time: '53:02'
  who: Alexey
- line: "For a beginner, I would still say \u201CPython, above everything\u201D. Python\
    \ is definitely the glue language, which connects everything. It's even getting\
    \ injected into browsers and into Excel recently. [chuckles] So I think you cannot\
    \ make a mistake if you invest your time to learn Python properly. With libraries,\
    \ it changes all the time\u2026 It changes all the time. So your basic skill is\
    \ to be Googling [chuckles] and being ready to change. SQL is definitely something\
    \ that stays. Pandas has a long tradition, but now you see people using more and\
    \ more Polars, and this and that."
  sec: 3203
  time: '53:23'
  who: Nemanja
- line: "But still, you see that Pandas has such a strong legacy that some other projects\
    \ have accepted the Pandas API \u2013 the Pandas way of doing things, although\
    \ it's not pandas. On PySpark, I think you also now have some kind of a Pandas\
    \ API \u2013 you can also use Modin on Ray as a Pandas (it looks like Pandas,\
    \ but it's not Pandas). In that sense. I think it's also just fine to start with\
    \ that. I think it's good\u2026 I would say open up the job postings and look\
    \ at what people are looking for. Definitely do that. That's how I did it every\
    \ time. You open it up\u2026 For example, how I started learning Python \u2013\
    \ at university we did a lot of MATLAB. I was like, \u201COkay, I like MATLAB,\
    \ actually. It's a really cool tool.\u201D But then I was looking for jobs and\
    \ I was like, \u201COkay, who\u2019s looking for a MATLAB person? Nobody, apart\
    \ from some German car manufacturers or parts manufacturers for cars.\u201D Nobody\
    \ was using MATLAB and I was like, \u201CLet's look for the positions I want.\
    \ Oh, everybody\u2019s asking for Python. Let's learn Python.\u201D I would say,\
    \ \u201CDon't obsess.\u201D No one tool across the stack that will be good. They\
    \ are all pretty similar. [Alexey agrees] In the end, it's easy to transition\
    \ from one to the other."
  sec: 3203
  time: '53:23'
  who: Nemanja
- line: "I would say learn Pandas, Python \u2013 those are the basics \u2013 and they're\
    \ still being used everywhere, and all the rest is just derived from there. It's\
    \ good to know how to do something in the cloud. I had a lot of pet projects \u2013\
    \ I made websites \u2013 I think it's good to know how to make a simple website.\
    \ Just basic HTML, CSS, JavaScript. It can look as ugly as hell, but if you know\
    \ just a bit of that \u2013 how to compose everything together \u2013 I think\
    \ it's valuable."
  sec: 3203
  time: '53:23'
  who: Nemanja
- line: It depends on how much time you have. If you have unlimited time and you're
    young, I would just say to go wild and learn everything. [chuckles] Focus on projects.
    Focused on making something end-to-end, and you will see what's required there.
    You will be forced to [find out].
  sec: 3203
  time: '53:23'
  who: Nemanja
- header: Working on projects to determine which skills you need
- line: "Yeah, I think that's the best [advice]. Instead of thinking, \u201CWhat kind\
    \ of tech do I need to learn?\u201D Think, \u201CWhat kind of projects do I want\
    \ to make?\u201D [Nemanja agrees] \u201CWhat kind of problems do I want to solve?\u201D\
    \ And then, \u201COkay, this is the problem I want to solve. I want to detect\
    \ when the cat\u2019s drinking water is gone. I want to detect that moment.\u201D\
    \ Then you have an idea of what you can implement. And then you think, \u201C\
    Okay, what do I need to implement that?\u201D"
  sec: 3379
  time: '56:19'
  who: Alexey
- line: "Yeah. But the thing is, I think it's mainly a question of not what the best\
    \ tool for the job is, because you have many rich domains, and you have many tools\
    \ that are good for the job. But then the question is, \u201CWhat will get me\
    \ hired?\u201D [chuckles] [Alexey agrees] When I think about what to learn, I\
    \ think, \u201CWhat's gonna increase my chances of getting hired?\u201D And then\
    \ you need to just explore. Be a data scientist about the tech stack. What's the\
    \ best way to be a data scientist about the tech stack? It\u2019s to go and look\
    \ for job descriptions, and see what people are asking for."
  sec: 3414
  time: '56:54'
  who: Nemanja
- line: "Always know that every job description has three times the required [things]\
    \ than what is actually needed in the stack. If they find somebody that knows\
    \ a third of what they\u2019re asking for, they will hire him immediately. [chuckles]\
    \ They always just write a nice wish list for Santa, but nobody knows all these\
    \ things. In the end, Googling and, I would say, thinking on your feet \u2013\
    \ this is usually what gets you."
  sec: 3414
  time: '56:54'
  who: Nemanja
- line: "I remember my first job. Actually, I was already, so for my second job \u2013\
    \ I was a Java developer. I opened like 20\u201330 different job descriptions\
    \ and then noted what is common among them. Every single one of them had a tech\
    \ (piece of technology) that no one else had. And then like\u2026 [cross-talk]"
  sec: 3477
  time: '57:57'
  who: Alexey
- line: "There\u2019s a data science project! Make a web scraping application that\
    \ scrapes LinkedIn jobs, or Monster.de or whatever you're using, and do some kind\
    \ of NLP and analyze [the requirements]. And make a website out of it and you\
    \ can maybe earn money out of it. People can then follow the daily trends in the\
    \ tech stack per domain. You say, \u201COkay, for a machine learning engineer,\
    \ these are the most common keywords (excluding the stop words, of course [chuckles]).\u201D\
    \ And yeah, there it is. We just gave you an idea. Perfect. [chuckles]"
  sec: 3501
  time: '58:21'
  who: Nemanja
- line: "That\u2019s cool."
  sec: 3536
  time: '58:56'
  who: Alexey
- line: Yes, when you earn money, give us a cut. [chuckles] We have the recording.
  sec: 3537
  time: '58:57'
  who: Nemanja
- line: Okay. I think that's all we have time for today. We should be wrapping up.
    Thanks. It's always a pleasure talking to you.
  sec: 3544
  time: '59:04'
  who: Alexey
- line: Likewise.
  sec: 3553
  time: '59:13'
  who: Nemanja
- line: Thanks for joining us today and sharing your experience with us, giving all
    that advice. So thanks a lot. We're looking forward to connecting with you again,
    either in person, in Porto, or some other conference or elsewhere. Yeah, thanks.
    And thanks, everyone for joining too. Bye.
  sec: 3555
  time: '59:15'
  who: Alexey
- line: Ciao!
  sec: 3579
  time: '59:39'
  who: Nemanja

---

Links:

* [LinkedIn](https://www.linkedin.com/in/radojkovic/){:target="_blank"}
