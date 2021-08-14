---
title: "Running from Complexity"
short: "Running from Complexity"
guests: [benwilson]

image: images/podcast/s04e05-running-from-complexity.jpg

season: 4
episode: 5

ids:
  youtube: sMy8NYZnsy8
  anchor: Running-from-Complexity---Ben-Wilson-e14np51

links:
  youtube: https://www.youtube.com/watch?v=sMy8NYZnsy8
  anchor: https://anchor.fm/datatalksclub/episodes/Running-from-Complexity---Ben-Wilson-e14np51
  spotify: https://open.spotify.com/episode/2TxcU3eF7hjkAEzAJcYMAg
  apple: https://podcasts.apple.com/us/podcast/running-from-complexity-ben-wilson/id1541710331?i=1000529834651

transcript:
- line: Today, we'll talk about running from complexity, which means starting with
    simpler things when we do our machine learning projects. We have a special guest
    today, Ben Wilson. Ben is a Practice Lead Resident Solutions Architect
    at Databricks. That's probably the longest title for any guest I had on this show
    [laughs]. Ben is based in North Carolina and he's been doing data science work
    for the past 12 years in companies ranging from semiconductor manufacturing to
    fashion companies. He is working on a book for Manning, titled Machine Learning
    Engineering in Action, which focuses on how to get machine learning projects into
    production and help them stay there. Welcome, Ben.
  sec: 134
  time: '2:14'
  who: Alexey
- line: Thanks. Great to be here.
  sec: 182
  time: '3:02'
  who: Ben
- line: Yes, it's our pleasure. Before we go into our main topic, let's start with
    your background. Can you tell us about your career journey so far?
  sec: 186
  time: '3:06'
  who: Alexey
- header: "Ben\u2019s Background"
- line: "Oh, it\u2019s one of the weirdest ones. It's even weirder than my job title\
    \ right now. It started straight out of high school. I went into the United States\
    \ Navy and joined a program that involved nuclear engineering \u2013 as a technician.\
    \ I did that for a number of years. I got tired of doing that, so I did a bunch\
    \ of other things in the Navy, but eventually it exposed me to a position in the\
    \ last year and a half that I was on active duty. I rose to interim communications\
    \ officer and dealt with message traffic and computers. It started to fascinate\
    \ me at just how mindnumbingly boring doing manual tasks on a computer can be.\
    \ So I started to learn the automation because \u201CI'm so lazy, I want a computer\
    \ to just kind of do things for me.\u201D"
  sec: 194
  time: '3:14'
  who: Ben
- line: "I started to learn scripting and stuff. That catapulted me. Once I got out\
    \ of the military after almost 12 years of service, I got my first job as a process\
    \ engineer, which dealt with complex manufacturing processes \u2013 running tools\
    \ and equipment lines, and having to \u2018craft recipes\u2019. I got tired of\
    \ that company and went on to another company, which had me doing a very similar\
    \ task, but working more in the R&D side of things with emerging products \u2013\
    \ with a much more complex system. That's where I started to learn even greater\
    \ tools to maximize my own personal laziness. I started to figure out, \u201C\
    Hey, I hate doing this thing so much. It's really complicated.\u201D"
  who: Ben
- line: "We had a contract with a company actually here in North Carolina, less than\
    \ 10 minutes from my house \u2013 the SAS Institute. They had all these great\
    \ training programs and allowed us to use their tooling (for a fee, of course),\
    \ and I started learning the basics of statistical process control. What we used\
    \ to call applied statistics, now we call it data science. I started learning\
    \ all that from those great instructors, and that tooling. This was over a decade\
    \ ago."
  who: Ben
- line: "That started me down a path of working for another series of companies, where\
    \ I started to do data science work \u2013 everything from the largest semiconductor\
    \ factory in North America to a fashion company, where I learned more intense\
    \ data science techniques and got exposure to Apache Spark. My current company\
    \ Databricks, we're a relatively early customer of theirs. I decided to make the\
    \ journey to learn more about my field and my profession at a company like Databricks.\
    \ So that long job title is what I call a \u2018field nerd\u2019. We help companies\
    \ build stuff \u2013 everything from ETL to traditional statistics, applications,\
    \ analytics, and truly cutting edge, ridiculous, deep learning, distributed, ML\
    \ applications. So that's my career journey in a nutshell. I've been doing that\
    \ for just over three years now."
  who: Ben
- line: "This long title \u2013 Practice Lead Resident Solutions Architect \u2013\
    \ you said it's a \u2018field nerd\u2019."
  sec: 400
  time: '6:40'
  who: Alexey
- line: Yeah.
  sec: 409
  time: '6:49'
  who: Ben
- header: Building solutions for customers
- line: So basically you help customers build what they need.
  sec: 410
  time: '6:50'
  who: Alexey
- line: "Yeah \u2013 whatever they need. The topic of today's discussion is highly\
    \ relevant to that, because that's a narrative that I try to push with teams,\
    \ particularly when they're just getting into new tooling. People have a penchant\
    \ for wanting to latch on to complexity, I think. They see the shiny thing in\
    \ the distance, like \u201CI really want to do that!\u201D Without thinking about\
    \ what is involved in actually doing it and how complex it could be. So one of\
    \ the things that we do is work with them and say, \u201CYeah, that's cool. The\
    \ shiny thing over there is really fascinating. But let's think about what we're\
    \ trying to solve here. Let's analyze the process within the frame of vision of\
    \ who our internal customer is. What problem are they trying to solve?\" They\
    \ just want the problem solved. We're there to help try to solve it. They're not\
    \ maintaining the code. They're not maintaining the solution \u2013 we are. We\
    \ need to make our lives simpler, which goes back to what I was saying earlier\
    \ about my own personality of trying to be as lazy as possible. I think laziness\
    \ is good in data science and engineering work, because it means you can go and\
    \ do other stuff. Because what you built is easier to maintain."
  sec: 418
  time: '6:58'
  who: Ben
- line: "You said you help your customers with everything from ETL to traditional\
    \ statistics, analytics, and this shiny, deep learning, new stuff. I guess when\
    \ somebody comes to you with a request, \u201CHey, can you please take this state\
    \ of the art library or model and train it for us?\u201D You probably start thinking,\
    \ \u201CHmm. Maybe you need something simpler.\u201D Is that right?"
  sec: 497
  time: '8:17'
  who: Alexey
- line: "Or maybe the code that we're looking at is so over-engineered and complex,\
    \ that the simple solution is, \u201CHey, let's refactor this to make it more\
    \ maintainable.\u201D A theme in the book that I wrote, which you mentioned before,\
    \ is \u201CWalls of text!\u201D I see that very frequently in data science code,\
    \ which is \u2018the god function\u2019. It's a function that is potentially hundreds,\
    \ if not thousands, of lines of imperative code that is so complicated and hard\
    \ to follow that the simpler thing is to start breaking it up into smaller pieces\
    \ in the refactoring process. You can simplify the code. Not just in the sense\
    \ of, \u201CYeah, it's easier to maintain.\u201D But there might be dead code\
    \ in there. There may be code that could be handled in a more efficient, cheaper,\
    \ and more understandable way. That's something that we do on the professional\
    \ services side \u2013 help customers."
  sec: 529
  time: '8:49'
  who: Ben
- line: "Sometimes we rewrite the code for them. Other times we pair up with them\
    \ and build it together. The end goal is not just to \u2018get something into\
    \ production\u2019, because that doesn't make successful ML. The end goal is to\
    \ build something together with a customer \u2013 something that they can maintain.\
    \ We want to build something that is going to be running in production hopefully\
    \ for years to come \u2013 something that they fully understand. Something that\
    \ they can improve it over time, instead of having this massively complex code\
    \ base where, if something breaks, or they need to put some new functionality\
    \ into it, they kind of throw their hands up and say, \u201CI have no idea where\
    \ to begin with this.\u201D"
  who: Ben
- header: "Why projects don\u2019t make it to production"
- line: In your opinion, what do you think is the most common reason that projects
    don't make it into production?
  sec: 635
  time: '10:35'
  who: Alexey
- line: "Not making it into production generally comes from one of two things, from\
    \ what I see. One is \u2013 nobody cares about it. There's no business buy-in.\
    \ You haven't actually paired up with your internal customer to make sure that\
    \ they're comfortable with what you're building. You haven\u2019t made sure that\
    \ they've bought into what you're building, and you haven\u2019t demonstrated\
    \ exactly what this is bringing to the table in terms that they understand \u2013\
    \ regardless of what the solution is."
  sec: 646
  time: '10:46'
  who: Ben
- line: "The second one is either picking a solution to a problem that\u2019s too\
    \ complicated to maintain or you can\u2019t even get to the point where you can\
    \ run it with stability in production. Or maybe it becomes so expensive to run\
    \ that the return on investment just isn't there. I see that a lot with people\
    \ that try to apply deep learning to problems that probably don't need it. They\
    \ say, \u201CWell, to get my model to train, I need X. I have a terabyte of training\
    \ data.\u201D Okay, that's a lot. \u201CAnd I need to get my model iterations\
    \ faster. So I need a GPU cluster on Spark, and I need Horovod to distribute the\
    \ training \u2013 just to be able to get training cycles to work fast enough.\u201D"
  who: Ben
- line: "Sometimes when you go in and see that \u2013 they're focusing on technical\
    \ issues that they're having, \u201CHow do I get this to run faster?\u201D And\
    \ nobody's taking a step back and saying, \u201CWhat's the actual problem you're\
    \ trying to solve? Oh, Churn prediction? Why do you need an LSTM to do that? Here's\
    \ a Pareto/NBD model that uses Bayesian inference to determine what the probability\
    \ of somebody churning. By the way, we can run that on your entire terabyte of\
    \ data in less than five minutes. Let's go that route instead.\u201D"
  who: Ben
- line: "Sometimes people find themselves at that point mere weeks before they're\
    \ about to go into production. Or when somebody gets the bill from the cloud vendor,\
    \ they say, \u201CWhy is this Project Costing $100,000 a month to run in training?\
    \ The use case is not even going to make us $100,000. Turn it off.\u201D That's\
    \ really demoralizing when a team faces that. Those are the two most common reasons\
    \ that I see."
  who: Ben
- header: Why do people choose overcomplicated solutions?
- line: Why do you think that happens? Why do you think somebody wants to run a complex
    LSTM using a cluster of GPUs on Spark, using Horovod, when they just need Churn
    prediction? Why do things like this happen? Do you know?
  sec: 799
  time: '13:19'
  who: Alexey
- line: "Here's a contentious opinion. This is just my opinion. I think this happens\
    \ because the people just want to flex \u2013 people want to be noticed. All of\
    \ us are fascinated by technology and that's why we get into this field. We want\
    \ to do cool stuff. And that stuff is cool \u2013 LSTMs, deep learning \u2013\
    \ they're fascinating implementations. The tech is really complex and cool and\
    \ it's interesting to use it. However, it's also really hyped up. Everybody's\
    \ talking about building cool things with those algorithms. But what people don't\
    \ understand in this field, or they're not focused on this point \u2013 it's something\
    \ that I mentor people about \u2013 don't focus on the tech. Don't focus on the\
    \ tooling. Don't focus on the platform. That's what blogs talk about. You get\
    \ vendors and creators of open source packages. They're pushing this narrative\
    \ because they want people to succeed with their tools. But take a step back.\
    \ I always recommend to people, \u201CTake a step back from what you're doing\
    \ and just focus on being an engineer. Don't try to be a scientist. Don't go into\
    \ research mode and try to implement a white paper just because you can or just\
    \ because you think it's a cool thing to do. Think of applying ML as an engineer\
    \ would.\u201D"
  sec: 820
  time: '13:40'
  who: Ben
- line: "The parallel, or the corollary, that I use when I'm talking about this point\
    \ is bridge building. If you're talking about building a bridge across a 20 foot\
    \ gap, a scientist might approach that and say, \u201CHey, we can construct this\
    \ bridge out of carbon nanotubes. We can have ultra highway, molecular weight\
    \ polyethylene wrapping around these carbon nanotubes. We can make a bridge that\
    \ weighs less than a car and can support a space shuttle.\u201D And maybe it'll\
    \ work amazingly well. An engineer would never even attempt to do something like\
    \ that. This is going to be ludicrously expensive and we're gonna have to do all\
    \ this research to figure out how to even do that. We're gonna have to build the\
    \ tooling in order to support the construction of the materials to make the bridge\
    \ out of this stuff. An engineer is going to say, \u201CNo, no. Steel is good.\
    \ We've been building bridges this way for over two centuries.\u201D Some engineers\
    \ that are more Luddite-type that might say, \u201CNo, we can just do concrete\
    \ and rebar. Let's do that because it works. It's a 20 foot gap. Let's build the\
    \ minimum required complexity in order to support this. Let's use proven techniques\
    \ to solve the problem of getting cars from one side of a hill to another side\
    \ of a hill.\u201D I see that data science works the same way."
  who: Ben
- line: "When you're working as a professional in a company \u2013 in an ML team,\
    \ or a data science team \u2013 we're there to solve problems. Nobody cares how\
    \ we solve them. Solving it in proven ways, ways that are consistently proven\
    \ to work, is the more wise decision. That\u2019s not to say, \u201CDon't play\
    \ around with the cool new stuff.\u201D Just do that on your own time. That's\
    \ what a lot of us who have been in the industry do. I'm sure you do it as well,\
    \ Aleksey. You know, some new cool tech comes out, and you're like, \u201CI'm\
    \ gonna try that out this Friday evening.\u201D Or \u201CWhen Saturday morning\
    \ comes, I'm gonna dedicate three hours and I'm going to play with this new tech.\u201D\
    \ But generally, you shouldn\u2019t do that sort of thing when you're working\
    \ on a project for a company. That's a fast ticket to get fired, even if you're\
    \ experienced."
  who: Ben
- line: "I guess, another problem could be that the person that is tasked with the\
    \ problem hasn't done this kind of thing before. Maybe they don't have any experience\
    \ with it, so they start looking it up and then see, \u201CLSTM here. LSTM there.\
    \ All these transformers. Okay, maybe I'll just go with this.\u201D Then when\
    \ they need to maintain it, they see that \u201COK. I\u2019m screwed.\u201D You\
    \ mentioned a certain method, I don't remember the name of it \u2013 the more\
    \ traditional one, the Bayesian one. I haven't really heard about this, to be\
    \ honest. When I Google things, I see, \u201COkay, LSTM and some thing I\u2019\
    ve never heard about. Hmm. Which one do I choose?\u201D So maybe that\u2019s how\
    \ people end up with these complex solutions."
  sec: 1048
  time: '17:28'
  who: Alexey
- line: "Exactly. Search engine optimization creates technical debt in data science\
    \ work. What I always recommend, and what I've always done, is \u2013 when I'm\
    \ working on a new project that I have no experience on, and newsflash to the\
    \ viewers, even people with 12, 15, 20, 30 years experience in ML, you're still\
    \ going to run into this constantly. Our industry, our profession, is so broad\
    \ in the amount of things that you could possibly specialize in. Nobody is going\
    \ to know it all. I'm not an expert on NLP, but I know people who are. So if I'm\
    \ working on an NLP project, I'm going to go talk to them. If I'm talking about\
    \ a customer\u2019s project, I'm going to anonymize it, of course. I'm not going\
    \ to say, \u201CHey, I'm working with this customer.\u201D Instead, I'll say,\
    \ \u201CHere's a problem that I'm trying to solve. Here's the expected outcome.\
    \ This is what the internal customer wants to see out of this. How would you solve\
    \ this?\u201D Then I'll ask a couple other people. Maybe I'll assemble a group\
    \ of experts and turn to the communities that we have, communities that you, Aleksey,\
    \ have built \u2013 and some of those other communities that you listed at the\
    \ beginning of this \u2013 there's amazing talent globally. These people are willing\
    \ to just come together and help each other out. We all struggle with every bit\
    \ of this. We all come across the problem of \u201CWhere do I even begin?\u201D"
  sec: 1097
  time: '18:17'
  who: Ben
- line: "If I do a Google search for how to solve a particular problem, I know that\
    \ the first couple of pages are probably going to be hype. There are gonna be\
    \ a lot of blog posts that are sponsored by companies that might not be the right\
    \ solution. Some of the original research is perhaps the best way to solve it\
    \ and simplest way to solve it \u2013 this stuff predates the internet by many\
    \ decades, if not centuries. Bayesian methodology \u2013 this stuff is 19th century,\
    \ when a lot of the research was done. The original papers that implement this\
    \ stuff predates computers. So finding those resources that answer, \u201CHow\
    \ would I deal with a nonparametric distribution if I'm trying to estimate this\
    \ prediction?\u201D This is highly esoteric information and it's really hard to\
    \ find it when you're just searching on the internet."
  who: Ben
- line: "It's much easier to join a community and just ask people that may have done\
    \ it before. Send out a flare. Some of these communities, everybody's so helpful\
    \ \u2013 somebody will chime in and say, \u201COh, I solved that same problem\
    \ before. Here's what I used.\u201D You'll still get some people that say, \u201C\
    Oh, yeah \u2013 use deep learning.\u201D But you might get somebody who's a \u201C\
    been there done that\u201D kind of person \u2013 someone who is a little older\
    \ and more experienced \u2013 who will say \u201CNo, no, you can solve this with\
    \ this statistical inference method that's really old, but it's really powerful\
    \ and fast.\u201D That's how I approach avoiding that trap."
  who: Ben
- line: "That's maybe something I will use as a pitch for the DataTalks.club \u2013\
    \ your words."
  sec: 1291
  time: '21:31'
  who: Alexey
- line: Definitely, you should.
  sec: 1296
  time: '21:36'
  who: Ben
- header: The dangers of isolating data science from the business unit
- line: "The other reason why projects don\u2019t make it into production that you\
    \ mentioned \u2013 nobody cares and there is no buy-in. You also said that we\
    \ need to focus on being engineers. But I think when we only focus on being engineers,\
    \ sometimes we get into the trap of \u201CWe have this tool. Let's try to find\
    \ a solution for this tool.\u201D When we're isolated from business units for\
    \ whom we\u2019re solving this problem in the first place. So how dangerous is\
    \ it when we become isolated and work on machine learning projects?"
  sec: 1299
  time: '21:39'
  who: Alexey
- line: "Ooh. Siloing of data science is the fastest track to never getting any of\
    \ your projects actually used in a company. They may be in production and they\
    \ may be running every hour on the hour. But the chances that people are actually\
    \ getting value out of that is going to be super low, if you're not involving\
    \ yourself with the business. I see the modern data scientists as people who are\
    \ coming from a post grad research position \u2013 that is a highly isolated position.\
    \ You're on your own doing your research. You're using the scientific method to\
    \ prove a point or to come up with some conclusion of original research. When\
    \ you come into a business environment from that \u2013 it's like night and day."
  sec: 1338
  time: '22:18'
  who: Ben
- line: "Some people want to default into what they're comfortable with, which is\
    \ isolation, or \u2018siloing off\u2019. \u201CHey, I only speak in the terms\
    \ of data science and mathematics and physics.\u201D But the rest of the business\
    \ doesn't speak that language. Some of them don't understand that stuff because\
    \ they don't need to understand it to do their jobs. That's not what drives the\
    \ company. There are companies that are driven by that, but they're relatively\
    \ rare."
  who: Ben
- line: "An important message that I always have for data scientists coming into the\
    \ field is \u2013 you have to work on your interpersonal skills. You have to get\
    \ to know people. Know how to build a relationship with people in the business.\
    \ You don't have to be their best friend, but getting to a point where you can\
    \ have a frank, open, and honest conversation with the business unit and being\
    \ able to say, \u201CHow can I help you? How can you help me make this better?\u201D\
    \ That collaboration is super critical for any project. That's where you're going\
    \ to get all your best ideas anyway."
  who: Ben
- line: "A model is going to produce some output, whether it's supervised or unsupervised,\
    \ deep learning or traditional or statistical \u2013 it's going to produce some\
    \ numeric output. The chances that this numeric output is going to be perfect\
    \ for the business use case are slim to none. There's usually some post-processing\
    \ that you need to do \u2013 some decision engine that you have to run that prediction\
    \ through. All the logic of that comes from the business, from the subject matter\
    \ experts (SMEs). They're the ones that are helping you do your QA, hopefully.\
    \ They're the ones that are saying, \u201CHey, data scientist, this is good.\u201D\
    \ Or, \u201CHey, this sucks and you need to completely change this.\u201D The\
    \ earlier and the more frequent that that relationship is built and nurtured and\
    \ maintained \u2013 the more successful every project is going to be."
  who: Ben
- line: "You\u2019re customer-focused at that point. You're really thinking about\
    \ that internal relationship, regardless of who's going to use the solution, having\
    \ the SMEs involved is going to not only give the project a higher probability\
    \ of making into production, but it's also going to make the project simpler.\
    \ It\u2019s because you have to explain what you're building to them \u2013 to\
    \ a layperson. They're like the ultimate rubber duck in that sense. You're explaining\
    \ through what you're building and they're gonna ask questions, \u201CWell, how\
    \ does this work?\u201D If you can't explain it to them in terms they can understand,\
    \ it's probably too complicated. If you can't explain it to the business, it's\
    \ going to be a nightmare for the next person that comes into the team to maintain\
    \ that. I always see it as a win-win \u2013 the closer that the relationship is\
    \ between the data science team and the business. The silo walls need to come\
    \ down if you want to be a successful data science team."
  who: Ben
- header: The importance of being able to explain things
- line: "Why do you need to explain something to the business unit anyway? Why do\
    \ they even care how this thing works inside? I can say, \u201CHey, just give\
    \ us your data, then we do some magic, and you get the output. Trust us \u2013\
    \ this output is good. You can use it.\u201D So why do we need to care about whether\
    \ they understand it or not?"
  sec: 1564
  time: '26:04'
  who: Alexey
- line: "They're going to want to understand. If you build that relationship correctly\
    \ and they're emotionally invested in this project, they're gonna want to know.\
    \ That is the goal of the data scientist working on it \u2013 you\u2019ve got\
    \ to get them hyped up about it. Humans are naturally curious. If you show them\
    \ a little peek behind the curtain, they're gonna want to step right through that\
    \ curtain with you and say, \u201CHey, I can't speak in your terms, alright? I\
    \ don't want to hear the nerd talk. But explain it to me like I'm a five year\
    \ old.\u201D Even though that is kind of an insulting phrase, but explain it to\
    \ them in terms that mean something to them \u2013 in the context of the business\
    \ and the problem."
  sec: 1588
  time: '26:28'
  who: Ben
- line: "They might not understand us when we discuss data science work, but we wouldn't\
    \ understand how they talk about what they do and their understanding of the business.\
    \ It's a partnership with people that have expertise in how the company is run,\
    \ or how finance operates, or how sales operates, or operations. Lean on them,\
    \ while they lean on you. You need to both jointly understand the project and\
    \ being able to explain it in a way that you both understand fluently will get\
    \ you there. That\u2019s going to help ensure that the project is more successful."
  who: Ben
- line: So basically, if you can explain to them and if they can understand, then
    maybe they will also have more trust in what you build. Would you agree?
  sec: 1665
  time: '27:45'
  who: Alexey
- line: "Yes. And they'll come up with ideas, too. Some of the best ideas I've ever\
    \ had, for any projects throughout my career, have always come from the subject\
    \ matter experts. It doesn't come from my head. I think of crazy stuff. It might\
    \ seem like it makes sense \u2013 I look at the data, like, \u201COh, there's\
    \ a correlation here between this value and this one!\u201D And then I show that\
    \ to the business unit and they're like, \u201CWhat are you talking about? Those\
    \ have nothing to do with one another.\u201D So I respond, \u201COh, so what is\
    \ important?\u201D And they're like, \u201CWell, you might want to think about\
    \ X.\u201D \u2013 \u201COh, I didn't know we collected that data. Let me bring\
    \ that in. Oh, wow, that just made the model 30% better and it actually solves\
    \ a problem. And it's simpler. I can do that in SQL!\u201D So yeah, it's super\
    \ important to be able to do that."
  sec: 1675
  time: '27:55'
  who: Ben
- line: "So basically, we need to involve the subject matter experts as early as possible.\
    \ Then we need to get the buy-in. We need to make sure that our model is not too\
    \ complex, so we can safely productionize it in such a way that we can maintain\
    \ it afterwards \u2013 in one year in two years \u2013 and so it's not too expensive.\
    \ Is that right? Then we see the value in it, right?"
  sec: 1723
  time: '28:43'
  who: Alexey
- line: Right.
  sec: 1745
  time: '29:05'
  who: Ben
- header: Maximizing chances of making into production
- line: "So how do we go about this? Let's say we have some project idea. What does\
    \ this approach look like? How do we go from the idea to production in such a\
    \ way that we maximize our chances, that in the end it\u2019ll be in production\
    \ and have something that is maintainable?"
  sec: 1746
  time: '29:06'
  who: Alexey
- line: "Hm. You said, \u201C_We_ have an idea.\u201D"
  sec: 1766
  time: '29:26'
  who: Ben
- line: "Somebody comes to us and says, \u201CHey, there's this awesome thing. If\
    \ you do this, our company will make millions.\u201D Or it can come from a data\
    \ scientist \u2013 doesn't matter. We just have an idea. Somebody in the company."
  sec: 1770
  time: '29:30'
  who: Alexey
- line: "Yeah, I see. I find that it\u2019s different when it's a subject matter expert\
    \ engaging with the ML team, because they already have the emotional investment.\
    \ It's their idea. They're going to actively want to work with the data science\
    \ team. In that relationship, it's on the data scientists to maintain openness\
    \ \u2013 to support that collaborative discussion and include the SMEs in all\
    \ of the testing and validation that's done. All the way up until production release\
    \ and even after production release."
  sec: 1783
  time: '29:43'
  who: Ben
- line: "But if it's the data science team coming up with the idea, they have to sell\
    \ that. They have to get that buy-in, and getting that buy-in means \u2013 immediately\
    \ after you do your first rough experiment, you need to timebox these things,\
    \ as I always say. Say you have this idea, something like, \u201COh, if we could\
    \ only classify cats and dogs better, then our company would make millions of\
    \ dollars. We need to build a CNN so that we can detect them. We need to test\
    \ out a Mask-RCNN and we're gonna use TensorFlow and Keras to do that.\u201D Cool.\
    \ Take two days \u2013 take the time out in your schedule to try to build a rough,\
    \ rough, rough prototype. This could just be some nasty script code in a notebook.\
    \ Just get something that kind of does what you're thinking of, so that you can\
    \ produce an output that you could put into a presentation and sell it to the\
    \ business. Don't spend months working on one of these Skunkworks projects so\
    \ that you can get it to perfection before you show it to anybody."
  who: Ben
- line: "Afterwards, be very open and honest about it and say, \u201CHey, we only\
    \ spent 48 hours on this\u201D or \u201CWe spent a week on this. It's really rough.\
    \ But here's our concept.\u201D At that point, you have to go into \u2018business\
    \ selling mode\u2019. You have to say, \u201CHere's what we're proposing. Here's\
    \ how we're going to do it, we think. We have to do some experimentation, but\
    \ here's the general idea. Here's what we believe our company is going to get\
    \ out of this.\u201D After that, I always recommend selling it to the business\
    \ unit that cares most about that data or to someone who owns the data \u2013\
    \ owns that business process. Sell it to them first before selling it to executives."
  who: Ben
- line: "Because what you don't want to do is have a high level elevator pitch that\
    \ an executive that will buy into it, thinking that this is going to be a panacea\
    \ to all the company's woes. Then they talk to the SME team later on and they're\
    \ like, \u201CWhat are you guys doing? This is nonsense. This is not going to\
    \ work.\u201D So talk to the people that know the boots on the ground first. Once\
    \ they say, \u201CYeah, this is awesome. We're on board. We\u2019ll totally support\
    \ this. We'll work with you to make this good.\u201D Then pitch it to the executives.\
    \ See if you can get a buy-in. You need some sort of executive sponsor, because\
    \ most ML projects are expensive, not just computationally and in terms of hardware\
    \ and VMs and stuff in the cloud, but also just time and effort. There are so\
    \ many other things you could be doing. This one had better be pretty important."
  sec: 1923
  time: '32:03'
  who: Ben
- line: "So if they sponsor it and say, \u201CYes, this is good. This is where we\
    \ want to go.\u201D Then it constitutes constant involvement of that SME group\
    \ \u2013 from the pre-ideation phase to the planning meetings, where you need\
    \ to answer, \u201CWhat do we need built?\u201D \u201CHow long do we think this\
    \ is going to take to do these different phases of this project?\u201D \u201C\
    What are we going to test?\u201D \u201CWhen's our next meeting?\u201D \u201CWhen's\
    \ our presentation cycle?\u201D Once that's all formalized and understood, go\
    \ off to do two weeks of experimenting, which will go something like, \u201CHey,\
    \ we're gonna try out these five different approaches. We're going to split the\
    \ team up \u2013 each sub-team is going to do one of these things. Then we're\
    \ gonna have a bake-off, internally. And then we're gonna have a bake-off in front\
    \ of the SMEs.\u201D And they're gonna say, \u201COh, we really like number three\
    \ there. That's super awesome.\u201D And then you present them the cost-benefit\
    \ analysis of each of the approaches. Like \u201COkay, number five that we tested\
    \ \u2013 It could be 10 times cheaper than number three, but 1% less accurate.\u201D\
    \ \u201CWhat's the trade off there?\u201D \u201CHow fast can we get it out?\u201D\
    \ \u201CHow easy is it going to be maintained?\u201D Do that analysis beforehand\
    \ so that you have that ready for the meeting and then make a group decision."
  who: Ben
- line: "I don't ever recommend the data scientists to be the ones that make that\
    \ decision. We're there to provide the scientific evidence \u2013 the results\
    \ of our experimentation. Let the business decide, \u201CIf this is cheaper and\
    \ faster, we want that.\u201D Alternatively, the business might say \u201CNo,\
    \ we really care about accuracy here. We need you to build this.\u201D Then, you\
    \ go and build it. But periodically, in ML agile approaches, I always recommend\
    \ that throughout that development process \u2013 after experimentation and the\
    \ decision is made \u2013each one of those sprints that you conclude, whether\
    \ it\u2019s two weeks or three weeks, you should have a working version of whatever\
    \ you're building. Push for that basic MVP at every sprint conclusion, when you\
    \ cut that feature branch and merge it, master it and run everything and get that\
    \ artifact, as well as a bunch of demonstrated predictions \u2013 that's what\u2019\
    s used as a presentation for the business."
  who: Ben
- line: "At a meeting, say, \u201CHere's the status right now, what problems do you\
    \ see?\u201D And they might say, \u201CWell, you're supposed to be predicting\
    \ cats and dogs, but we threw a penguin in there and it says that it\u2019s a\
    \ dog, so there's a problem here.\u201D Show them the results, get their ideas\
    \ of what to test, and eventually by the time you hit production-readiness level,\
    \ the model will be good. It'll be good to solve the problem, but it'll also be\
    \ good because the SMEs have faith in it. They have skin in the game. It's their\
    \ ideas being shown in code. They're going to want to see it succeed. That's that\
    \ inclusive aspect with the business that becomes so important, because people\
    \ are emotional creatures. So when you get somebody who has ownership of a project,\
    \ even if they're not the one writing the code, they're gonna want to see it succeed.\
    \ And they're going to be the champions of it when it\u2019s all said and done.\
    \ They'll use it and they'll help make it better. That's how you make a successful\
    \ ML."
  sec: 2105
  time: '35:05'
  who: Ben
- line: SMEs are subject matter experts, right?
  sec: 2166
  time: '36:06'
  who: Alexey
- line: Yes, yep. Whoever the geniuses are for that domain.
  sec: 2168
  time: '36:08'
  who: Ben
- header: The IKEA effect
- line: "I heard of this thing called \u2018the IKEA effect\u2019, maybe you\u2019\
    ve heard about this as well."
  sec: 2173
  time: '36:13'
  who: Alexey
- line: The IKEA effect?
  sec: 2179
  time: '36:19'
  who: Ben
- line: "Yeah. In IKEA, you buy a thing, but it's not assembled yet. You have to assemble\
    \ it yourself. It's pretty simple \u2013 they have an instruction manual for it.\
    \ Let's say you bought a desk. They include a very simple instruction manual that\
    \ was tested on many, many people. You just put it together, and then maybe you\
    \ have this ugly desk when you\u2019re done. But you really love it because you\
    \ built it yourself. You develop an attachment to this desk. You bought it, and\
    \ you built it yourself. It's standing there \u2013 you can maybe put your laptop\
    \ on it or eat on top of it. Maybe it's not the same quality as something that\
    \ somebody could build it for you, but you love it anyway."
  sec: 2180
  time: '36:20'
  who: Alexey
- line: "Definitely. I think that's a perfect analogy. I think there's a difference\
    \ with that effect if you're buying a desk and it comes in 10 pieces, versus a\
    \ desk that comes in 10,000 pieces. You're gonna love the 10 piece desk, no matter\
    \ how boring and simple it is. It might not be fancy, but it gets the job done.\
    \ You're gonna love it, because you helped build it. The 10,000 piece desk might\
    \ be made out of some rare earth metals and might be super fancy, but it costs\
    \ 10,000 times more than the simple desk. You're still going to be emotionally\
    \ attached to it, but that's not a healthy attachment. Because you're going to\
    \ have everything invested in that thing and you're going to be stressed out about\
    \ how complex it is. When it breaks, you're going to be trying to fix it because\
    \ you built it. It\u2019s your baby."
  sec: 2228
  time: '37:08'
  who: Ben
- line: "The whole company can be in that mindset too. I have seen that effect with\
    \ certain companies that I've interacted with, where they've built that \u201C\
    10,000 piece desk\u201D. They love it. But they also hate it, because they can't\
    \ build any more desks. They can't build the chair that goes along with it because\
    \ they\u2019re too busy fixing the desk over and over and over again. The whole\
    \ data science team spends 90% of their time just fixing and gluing back on little\
    \ pieces that keep on falling off."
  who: Ben
- line: "Yeah, I remember I once bought something, not from IKEA, but from another\
    \ store. It was a German store, so I had high expectations in terms of simplicity\
    \ \u2013 how simple it would be to build the thing. But it wasn't as simple as\
    \ I imagined. It was much more complex. I hated that thing. I gave up on it. It's\
    \ still in the basement, not assembled."
  sec: 2321
  time: '38:41'
  who: Alexey
- line: Yeah. That can happen with ML as well.
  sec: 2353
  time: '39:13'
  who: Ben
- header: Risks of implementing novel algorithms
- line: "Let's say we have something more complex \u2013 maybe a novel algorithm \u2013\
    \ that we want to try. We heard that right now deep learning is very popular,\
    \ so we want to try it for our problem. Should we do this? Is this necessary?\
    \ What kind of risks do we have for doing this?"
  sec: 2357
  time: '39:17'
  who: Alexey
- line: "If you\u2019re going to do that, I'd say use proven deep learning algorithms\
    \ \u2013 if we're talking about CNNs. If you've got an architecture that somebody\
    \ has spent time building and it\u2019s proven out that it actually works, I'd\
    \ say it's pretty low risk. That's the benefit of transfer learning. You can say\
    \ \u201CAlright, I'm going to take Inception v3. I'm going to lock the first 90%\
    \ of the layers for non-training. Open up the last 10%. Add on my own classifier\
    \ stage and retrain it on my data.\u201D That\u2019s fairly low risk, because\
    \ thousands of people are doing that. I've done it dozens of times. It works.\
    \ Building something from scratch, where you find a white paper and there are\
    \ novel algorithms in it \u2013 that's where the risk comes in. I'm guilty of\
    \ it myself \u2013 of not only implementing those, but also creating them from\
    \ scratch myself."
  sec: 2378
  time: '39:38'
  who: Ben
- line: It's fun, right?
  sec: 2439
  time: '40:39'
  who: Alexey
- line: "It is very fun. But it's important to make sure that there's not a solution\
    \ already in existence out there that does what you're trying to do. A lot of\
    \ things that get published, particularly in our field, a lot of people need to\
    \ publish them, because this is a burgeoning growing field. There's a lot of exciting\
    \ research being done. There's also a lot of non-repeatable research being done.\
    \ A lot of stuff that gets published, even if you were to try to re-implement\
    \ exactly what they did, you can\u2019t \u2013 even if they show code, which most\
    \ of them don't. Sometimes they will have a GitHub repository, like, \u201CHey,\
    \ check out the code that I had for my research.\u201D You take that code and\
    \ you run it on the exact same dataset, but on a different environment, and it\
    \ doesn't work. It doesn't produce the same results. That's dangerous."
  sec: 2440
  time: '40:40'
  who: Ben
- line: "What I usually recommend to people who are thinking of implementing novel\
    \ algorithms \u2013 check to make sure it's possible. See if other people have\
    \ done it. You don't want to be the guinea pig, unless you've established street\
    \ cred at your company. What I mean by street cred is \u2013 you've already done\
    \ all the low hanging fruit. You've got dozens of models in production that solve\
    \ actual real-world business use cases at a company. Say you're working for an\
    \ e-commerce site. You've got CLV. You've got Churn. You've got fraud prediction.\
    \ You've got RLV. You've got RFM clustering. You've got recommendation engines.\
    \ You have targeted messaging for marketing. You\u2019ve got all these models\
    \ that are currently running and working and doing great."
  who: Ben
- line: "Now you're out of the easy stuff. \u201COh, I don't know what to do next.\
    \ The business wants us to do this really crazy thing that I spent two weeks trying\
    \ to research how other people might tackle this. I've talked to my people over\
    \ in DataTalks.club. I asked a couple data scientists and asked if anybody tackled\
    \ this.\u201D And the only response that I got was \u201CGood luck.\u201D Or,\
    \ \u201CHey, that's NP-complete. We have no idea how to do that.\u201D If you've\
    \ gotten to that point, that's when you're going into the white papers zone of\
    \ saying, \u201CHey, maybe somebody has done research.\u201D Or \u201CMaybe I\
    \ can actually contact a university and see if any other postgrad researchers\
    \ are working on this problem.\u201D That\u2019s when you may try to assume that\
    \ risk, if you have no other options."
  who: Ben
- line: "But the important thing to do there is communicate to the business, and to\
    \ your management, and probably all the way up to your CTO, of how risky it is.\
    \ If everybody's on board saying \u201CYes, this is the direction that we want\
    \ to go in. Put your research hat on and figure it out.\u201D That's when you're\
    \ doing novel work. And maybe you should publish your results when you're done.\
    \ You know, help out somebody else in the future. Because we are that sort of\
    \ community. But if it's a problem that has been solved by somebody, some way\
    \ \u2013 particularly problems that have been solved by many people over many\
    \ decades, using what some people might think of as \u2018uncool tech\u2019. Like\
    \ \u201CI don't want to use stats models in Python. I want to use machine learning.\u201D\
    \ Everything is stats in what we do. So what's wrong with statistical inference?\
    \ Just learn about it, use it, try it. If it works \u2013 great. You just made\
    \ the business happy. You solved the problem. Now you get to move on to something\
    \ cool or cooler. That's how I see the implementation of original research."
  who: Ben
- header: "If it can be done simply \u2013 do that first"
- line: "So this is how you earn street cred \u2013 by doing uncool stuff first and\
    \ by not using machine learning. Maybe by using the stats model library before\
    \ you even moving to Scikit-Learn. Then eventually, you might get into this area\
    \ where no one has solved this problem before and then you start figuring out\
    \ how to do it."
  sec: 2663
  time: '44:23'
  who: Alexey
- line: "Yeah, and even before the stats packages, there's a shocking number of what\
    \ people would classify as data science work or ML work that you can actually\
    \ solve in SQL. There are plenty of things like that. Quintile bucketing, windowing\
    \ operations, building linear equations \u2013 things where you can say, \u201C\
    Hey, I just need to interpolate this point between these two other points in order\
    \ to provide an inference.\u201D It might execute in seconds, versus the ML approach\
    \ that could take an hour of training and then 10 minutes of validation and all\
    \ of this code that you have to maintain. Whereas, if you can solve the business\
    \ use case with simple SQL statements \u2013 do that. We're here to solve problems,\
    \ not to get fancy."
  sec: 2687
  time: '44:47'
  who: Ben
- line: "I think what you mentioned is, you can see how many people have solved this\
    \ previously, in order to understand how tedious it is. If 1000s of people have\
    \ done this, like the transfer learning CNN example, then it's low risk. There\
    \ are tons of resources \u2013 maybe you can do this with your eyes closed, because\
    \ you did this 12 times already. But if it's only 10 people who have done this,\
    \ and they are the authors of the paper you're reading, then maybe it's a lot\
    \ more risky, and you should try to solve other, easier problems first."
  sec: 2744
  time: '45:44'
  who: Alexey
- header: "Don\u2019t become the guinea pig for someone\u2019s white paper"
- line: "Yeah, and if those 10 people publish something, check to see how many other\
    \ papers reference that paper. That's always something that I do. I learned that\
    \ the hard way, several times. \u201COh, that's published by this university.\
    \ They definitely know what they're talking about.\u201D And then you try to implement\
    \ it or take the actual code and try to run it like, \u201CWait a minute, there's\
    \ an issue here with how this works.\u201D Or they did it in a language that you\
    \ can't transfer easily to another language because of floating point precision\
    \ or something like that. Then you're like, \u201COh, geez. I would have to reimplement\
    \ how this particular package does its calculation here, so that I could interface\
    \ with it. So now I have to write my own core mathematical algorithm to support\
    \ this algorithm that I'm now building on top of that.\u201D It's turtles all\
    \ the way down when you're in that space."
  sec: 2782
  time: '46:22'
  who: Ben
- line: "I sometimes see that in certain customers. Databricks, the company I work\
    \ for, include the creators of Apache Spark. So distributed computing, people\
    \ put a lot of large scale ML use cases on Spark because it can support truly\
    \ ludicrous amounts of data. Not every algorithm is distributable. I've worked\
    \ with people before who were like, \u201CHey, we need to do a non-negative matrix\
    \ factorization on Spark.\u201D Like, \u201COkay. Well, we have ways of doing\
    \ matrix inversion in Spark through an iterative process.\u201D And they're like,\
    \ \u201CNo, no. We can't use that. We need to actually invert the matrix all at\
    \ one time.\u201D Like, \u201CThat's gonna shuffle all the data to every other\
    \ executor. This is gonna be super expensive. And you\u2019re gonna need a massive\
    \ cluster that can handle this.\u201D And they\u2019re like, \u201CWell, we read\
    \ a paper.\u201D \u201COkay, you read a paper on somebody doing this. Let's give\
    \ it a shot. We'll give it a week. We'll play around with it and try to write\
    \ some code.\u201D And then later on, you realize that, \u201COh, the reason it\
    \ worked was because the Hadoop cluster that this was running on, that had Spark\
    \ running on it, had 10,000 nodes available. This company can't afford that amount\
    \ of VMs to be started in their AWS instance.\u201D So we had to backpedal and\
    \ say \u201CWe can't do this. And here's why.\u201D"
  who: Ben
- line: "It's important when you\u2019re looking through those papers to read the\
    \ fine print and then see if other people have been successful in doing it. That's\
    \ actually what I found a week later \u2013 other people referencing that paper\
    \ saying, \u201CYeah, this is cool. But this was the environment that they ran\
    \ this on. So unless you have this amount of horsepower behind you \u2013 unless\
    \ you\u2019re Google \u2013 you should maybe not do this.\u201D"
  who: Ben
- line: Yeah, I think I saw something similar. There is a company called Criteo. They
    actively use Spark. I don't know if they still have their Hadoop cluster. But
    they liked the fact that they had the largest Hadoop cluster in Europe. So they
    do a lot of talks about this. But mainly for smaller tech companies, not all these
    things are as easily implementable. Criteo has this Hadoop cluster and others
    don't.
  sec: 2956
  time: '49:16'
  who: Alexey
- line: I didn't realize we have so many questions. We have actually six questions.
  who: Alexey
- header: The importance of stat skills and coding skills
- line: "Rosona says \u201CMy impression is that a lot of companies slip through needing\
    \ people with basics stat skills. And now I'm throwing data science at it. Do\
    \ you agree or disagree?\u201D"
  sec: 2994
  time: '49:54'
  who: Alexey
- line: 100% agree. 100%. I think there are two core critical skill sets that some
    companies don't realize that they need in order to make successful data science
    or ML use cases. The first one is statisticians, or rather people with a statistics
    background. It's such an important aspect of our work. You don't need everybody
    to have that background. But you need at least one or two people that really understand
    statistics at an extremely deep level.
  sec: 3005
  time: '50:05'
  who: Ben
- line: "The second one is coders. Get a developer to train up the data science team\
    \ to create ML engineers. I know that that term is thrown around a lot. People\
    \ are like, \u201CWell ML engineers do ML Ops stuff.\u201D What I mean by ML engineer\
    \ \u2013 my own personal definition \u2013 it\u2019s a data scientist who can\
    \ code. Somebody who can do soup to nuts \u2013 you can do the ETL, you can deploy\
    \ to production, and everything in between. Having a statistics background, as\
    \ Rosona said, is also super critical as part of that. Even if you're not an expert,\
    \ you should at least have exposure to that and continuing learning it. Sometimes\
    \ you might even have to read the old school textbooks that were written far before\
    \ digital printing was a thing."
  who: Ben
- line: Yeah, I think I had one of those textbooks. I tried to read it and it was
    so difficult.
  sec: 3091
  time: '51:31'
  who: Alexey
- line: "Yeah, some of them are pretty dry and pretty complex, particularly the pure\
    \ theory ones. The alternative to that is \u2013 wait for you (Alexey) to write\
    \ a book that translates that. There\u2019s a lot of people writing books like\
    \ that: \u201DHey, here's the foundation of this crazy technology, in theory,\
    \ but let's talk about it from an application standpoint.\u201D And that's really\
    \ what people needed to know. But having somebody who understands the theories\
    \ is also helpful."
  sec: 3100
  time: '51:40'
  who: Ben
- header: Structuring an agile team for ML work
- line: "Yeah, thanks. A question from Chetna \u2013 \u201CCould you please advise\
    \ how to structure an Agile Scrum team specifically for machine learning or data\
    \ science work?\u201D So my experience says that typical software Scrum doesn't\
    \ fit well to data science. But I think the example you gave was very similar\
    \ to Scrum in the sense that every two weeks or every end of sprint, you have\
    \ something that you can show to the stakeholders \u2013 to subject matter experts.\
    \ Every time you finish your sprint, you have a working thing, which is very Scrum-like."
  sec: 3134
  time: '52:14'
  who: Alexey
- line: "Yeah, and people don't like to hear that. Teams that I've talked to are like,\
    \ \u201CWe can't do that. That's not how we work.\u201D It can be. It's about\
    \ iterative development in ML. The only way to make that successful \u2013 to\
    \ have that Scrum mentality \u2013 follows along with what we've been talking\
    \ about today. You have to keep it simple. It has to be lightweight. It has to\
    \ be just barely functional at first. But the Scrum mentality of having buildable,\
    \ usable, executable code supports you in keeping the complexity down during that\
    \ development. Because you're simply not going to have enough time. By the way,\
    \ that's why software developers do that as well. You know that, Aleksey \u2013\
    \ you come from a software development background."
  sec: 3170
  time: '52:50'
  who: Ben
- line: "If you're just left to do whatever you wanted to do, like, \u201CHey, that\
    \ project we\u2019re doing\u2026 come back in six months, and we'll show you what\
    \ we've built.\u201D You could build some of the most unmaintainable, crazy code\
    \ that's so over-engineered. Yeah, it meets the requirements, but it does 10,000\
    \ things that they never asked for. So that's why you do that Scrum process of\
    \ saying, \u201CJust build what you really need in order to hit the target for\
    \ this sprint.\u201D And you can do that with ML projects, but it involves building\
    \ very bare-bones, experimental code. This goes into that MVP process, where you're\
    \ just building on iteratively the new functionality. You might say, \u201CWe\
    \ just want the data to be loaded somewhere. We need to just do some basic feature\
    \ engineering. Let's get the feature engineering work and run it through this\
    \ placeholder model.\u201D That placeholder model doesn't have to be an algorithm.\
    \ It doesn't even have to be ML. It can be an \u201Cif-else\u201D statement. It\
    \ can be a simple linear model that is hand-coded, by taking your feature vector\
    \ and passing it through just offset weights that you're applying. Keep it as\
    \ simple as possible."
  who: Ben
- line: "Then, once you get the feature engineering all worked out so that you can\
    \ create a feature vector, maybe the next sprint is \u201CAlright. We know which\
    \ algorithm we're going to go to with \u2013 let's build all that code out \u2013\
    \ and let's tune all the hyperparameters in an automated way. Let's use UpTuner\
    \ or Hyperoptic.\u201D That's the sprint. At the end of that, you still have a\
    \ result. You have predictions that you can show people. The next one might be\
    \ \u201CAlright, now we're doing unit testing. Let's unit test all that feature\
    \ engineering code. Let's write all those tests. Let's make sure that we have\
    \ an integration test from ingest to prediction.\u201D So it's possible. I know\
    \ it's possible because I've done it many, many times."
  who: Ben
- header: Timeboxing research
- line: "The main concern I hear when somebody says, \u201CHey, let's use Scrum for\
    \ research\u201D is that the research is very nondeterministic. You don't know\
    \ if something you do is going to succeed or not. But I think it's still a good\
    \ idea to timebox this thing. So you'd rather spend two weeks to conclude that\
    \ it's not possible, rather than you spend two months or more to conclude that\
    \ it\u2019s not possible. Right?"
  sec: 3341
  time: '55:41'
  who: Alexey
- line: "Yep. Yeah, I hear that from people all the time. I've gotten that as feedback\
    \ from the book \u2013 the first couple of chapters, like \u201CWell, how can\
    \ you tell in just three weeks whether something's gonna work or not?\u201D Maybe\
    \ you can't. Maybe if you spend three years working on the problem, you'll figure\
    \ it out. You'll get something that's workable and all that good stuff. But as\
    \ data scientists, companies aren't expecting us to do original research, generally.\
    \ Some are. But generally, they just want a problem solved. And it's not just\
    \ the problem that you're working on right now that they want solved. They probably\
    \ have 100, 200 thousand problems that they want solved. If you're not timeboxing\
    \ that research and saying, \u201CHey, we're going to either shelve all of our\
    \ research for a later date so we can work on something else.\u201D Or we're just\
    \ going to say, \u201CHey, we've given it our best shot, and we've tried it out.\
    \ We can't figure it out. Maybe we need to hire somebody with experience in this\
    \ field. Maybe we need to have more discussions in the community.\u201D and say,\
    \ \u201CHey, how do other people solve this?\u201D That might take time. But if\
    \ you have that timebox, you can then move over to another project while somebody\
    \ is taking a couple of hours a week of just continuing that research phase, but\
    \ not devoting an entire team to trying to figure something out over months."
  sec: 3373
  time: '56:13'
  who: Ben
- header: Mentoring
- line: "There is another question from Rosona about your mentoring. I don't remember\
    \ if you mentioned something about mentoring today. But \u2013 \u201CIs it a formal\
    \ thing you do or is it something through Databricks?\u201D"
  sec: 3458
  time: '57:38'
  who: Alexey
- line: I do a number of different things. But for mentoring, we have programs at
    Databricks. We have several for software development, where we have people in
    the field that come from a data science or statistics background that are trying
    to learn how to get better at software development skills. There's a bunch of
    programs that we do like that, which are formalized meetups and project work.
    We allow people to learn in the best way that they can, which is learned by breaking
    it and then fixing it.
  sec: 3476
  time: '57:56'
  who: Ben
- line: "We also have programs where we teach ML to people from a data engineering\
    \ background and a software development background. There's a kickoff that we're\
    \ doing \u2013 we just started the next round this week actually, which is formalized\
    \ at the end with a capstone project. That capstone project is full end-to-end\
    \ production ML, which is unit-tested, integration-tested, monitored, with A/B\
    \ testing built around it. Deployments, CI/CD \u2013 everything that you can think\
    \ about from production ML. That's what we help people build. So they focus on\
    \ solving a problem with an open source data set."
  who: Ben
- header: "Ben\u2019s book"
- line: "Thanks. So I know we should be wrapping up. But I also want to ask you about\
    \ your book. Maybe you can tell us a bit about it and how it\u2019s related to\
    \ the topic today?"
  sec: 3553
  time: '59:13'
  who: Alexey
- line: "I think everything that we talked about today is covered in the book in some\
    \ way. And then add another 610 pages on top of that. It's kind of a monster of\
    \ a book. The first part of the book is talking about process, \u201CHow do we\
    \ think through a problem? How do we have those conversations with a business?\
    \ How do we do that Scrum implementation from ML?\u201D And it also talks about\
    \ \u201CWhat is actually important about solving problems?\u201D and \u201CHow\
    \ do we engage with people to help collectively and collaboratively solve those\
    \ problems?\u201D"
  sec: 3567
  time: '59:27'
  who: Ben
- line: "Part two is more focused on implementation of esoteric things that a lot\
    \ of people don't focus on. It's not the fun, cool stuff. People who really like\
    \ reading books about \u201CHow do I build an algorithm?\u201D That's key, core\
    \ data science work. You need to know how to build your random forest, or your\
    \ logistic regression, or how to implement a statistical model. But so many people\
    \ have written books about that. I wasn't interested in writing that. In fact,\
    \ what I normally say is, \u201CHey, go read Aleksey's book on how to do this\
    \ \u2013 if you want to see applications of ML algorithms, and then there\u2019\
    s explanation of how to do that.\u201D I'm focusing more on \u201CHow do you automate\
    \ away the annoying part of that?\u201D Which is \u201CHow do you do automated\
    \ tuning when you have 1000 time series models that you need to predict? How do\
    \ you automate that? How do you distribute the training and auto tuning of each\
    \ of those? And then what do you do with them? How do you produce visualizations\
    \ that are not specifically for data scientists? How do you produce a visualization\
    \ that tells a story to a business?\u201D"
  who: Ben
- line: "Then part three is more the development stuff, like \u201CHey, why is code\
    \ quality so important? Why is testing so important? Here's how to do this type\
    \ of stuff. Here's some gotchas that I see.\u201D Because I'm kind of spoiled,\
    \ being a consultant at a pretty big company. I interact with a lot of companies,\
    \ so I see how a lot of data scientists do stuff. There are repeated patterns\
    \ that I see, so I just try to address some of those. \u201CThink about computational\
    \ and space complexity. This is why it's important. This is why code quality is\
    \ important. Modularity, abstraction.\u201D If you're not doing these things in\
    \ your ML code, it's gonna be a nightmare to maintain. That's pretty much the\
    \ book. It's all the stuff that people usually don't talk about when they talk\
    \ about ML."
  who: Ben
- line: You said 600 pages?
  sec: 3726
  time: '1:02:06'
  who: Alexey
- line: Yeah, something like that. They're trying to get me to make it go down.
  sec: 3731
  time: '1:02:11'
  who: Ben
- line: "Yeah, I know what you\u2019re talking about."
  sec: 3734
  time: '1:02:14'
  who: Alexey
- line: "\u201CIt\u2019s so expensive to print!\u201D"
  sec: 3739
  time: '1:02:19'
  who: Ben
- line: Do you have a couple more minutes? Because we have three more questions.
  sec: 3740
  time: '1:02:20'
  who: Alexey
- line: Sure.
  sec: 3745
  time: '1:02:25'
  who: Ben
- header: "\u2018Uncool techniques\u2019 at AI First companies"
- line: "One question from Akshat. \u201CIt makes sense to solve problems with uncool\
    \ techniques. But there are companies who are AI First \u2013 they want to show\
    \ off and say that they have AI capabilities. So what about them?\u201D"
  sec: 3747
  time: '1:02:27'
  who: Alexey
- line: "Good luck. I mean \u2013 you're gonna have to spend money for that talent.\
    \ I'd say less than 5% of companies that I'm aware of, or that I've interacted\
    \ with, have the budget and the resources to acquire and retain that level of\
    \ talent. If you're an \u2018AI First\u2019 company and all you want to do is\
    \ the most cutting-edge, most complex implementations of things \u2013 that's\
    \ great, more power to you. I just hope you have the budget for each of those\
    \ people. You're going to need what they call \u2018full stack data scientist\u2019\
    , or what I call an ML engineer. You're going to need people that have been and\
    \ there done that, and that know how to do those complex implementations or that\
    \ can build novel algorithms. And they're not cheap."
  sec: 3765
  time: '1:02:45'
  who: Ben
- line: "Here in the United States, at least, you could be looking at having to pay\
    \ somebody half a million dollars a year in salary. Who knows how to do that?\
    \ Who can successfully do that? Most companies don't have that budget, or they\
    \ see that price tag, and they're like, \u201CWhoa, wait a minute. That's more\
    \ than we pay our senior staff developers. No, we're not gonna do that. We're\
    \ gonna hire people straight out of a Ph.D. program, and then we're just gonna\
    \ tell them to do this.\u201D Good luck. It's not gonna go well. Those people\
    \ are probably going to quit because they're going to be under so much stress.\
    \ They're not going to really know how to do all of that. You need the right talent.\
    \ You need to bring in the new people, so that they can train, but you need to\
    \ have processes built around mentoring and cross-training, pair programming.\
    \ All I can say is \u201Cgood luck\u201D."
  who: Ben
- header: Should managers learn data science?
- line: "Right, thanks. A comment from anonymous, \u201CI always hear about data scientists\
    \ having to explain things in simple language to their managers. Do you think\
    \ it's high time that managers have a crash course on data science?\u201D"
  sec: 3874
  time: '1:04:34'
  who: Alexey
- line: "I think it's important for a data scientist, or rather for any engineer \u2013\
    \ from a front end software developer all the way to an ML engineer \u2013 anybody\
    \ who's working with tech that is esoteric in nature. You should be able to explain\
    \ it to your parents, or to your children, or to your spouse\u2026 you should\
    \ be able to explain what you do and how you built something in terms that any\
    \ human, who has sufficient understanding of business operations, can understand\
    \ what you're doing. Now, that's not the question that was asked. It's \u201C\
    Should my manager be able to understand terms in what I'm doing?\u201D Yes and\
    \ no. It's up to the tech lead, I think \u2013 whoever the most senior data scientist\
    \ is \u2013 to work with that manager and educate them, and say, \u201CHey, when\
    \ we're in our stand-ups and when we're talking about these things, this is what\
    \ that actually means.\u201D I've done that at companies I've worked for in the\
    \ past. I don't have to at Databricks because of what we do, and who we hire."
  sec: 3893
  time: '1:04:53'
  who: Ben
- line: "But at previous companies \u2013 yes. Sometimes the manager doesn't want\
    \ to ask, or they say, \u201CHey, I need this explained in simple terms.\u201D\
    \ It could be because they are afraid to ask what somebody is talking about in\
    \ a meeting. They don't want to look like they don't know what they're talking\
    \ about. So the tech lead should be the one telling them like, \u201CHey, I'm\
    \ willing to teach you all of this stuff so that you can follow along exactly\
    \ with what the team is talking about.\u201D They'll probably be grateful. And\
    \ if they get angry at that, then maybe your company sucks and you need a new\
    \ job [laughs]. I mean, I would extend the olive branch to that manager and say,\
    \ \u201CHey, do you want to learn more about this?\u201D And every single time\
    \ that I've had that interaction, they're usually so grateful. They're like, \u201C\
    Oh, this is amazing. That's exactly what I was hoping for. Can we meet for an\
    \ hour after work?\u201D And I\u2019m like, \u201CYeah, let's create a cheat sheet\
    \ for you: here's this concept, here's what it actually means in laypersons terms.\u201D\
    \ People that I've worked with in the past have filled multiple pages front and\
    \ back with translations like that. That\u2019s their Rosetta Stone to talk \u2018\
    data science nerd talk\u2019."
  who: Ben
- line: I think it's not reasonable to expect from a manager that, if you just send
    them a course of Andrew Ng or someone else, that they will learn the ins and outs
    of it.
  sec: 4037
  time: '1:07:17'
  who: Alexey
- line: No.
  sec: 4049
  time: '1:07:29'
  who: Ben
- line: "I don't think they will ever do that, because they're busy. They're busy\
    \ with planning budgets and hiring \u2013 a ton of things. They are just too busy\
    \ to learn machine learning. It's not their core competency."
  sec: 4049
  time: '1:07:29'
  who: Alexey
- line: Right.
  sec: 4068
  time: '1:07:48'
  who: Ben
- line: "So it's your job (the data scientist's) to educate them. To tell them \u201C\
    Okay, we mentioned this thing during the stand-up \u2013 this is what it actually\
    \ means.\u201D"
  sec: 4069
  time: '1:07:49'
  who: Alexey
- line: Yes, right.
  sec: 4076
  time: '1:07:56'
  who: Ben
- header: Do data scientists need to specialize to be successful?
- line: "Okay. Last one. From Chetna \u201CI've often heard people suggesting that\
    \ to be successful as a data scientist, one should find a niche, for example,\
    \ become an NLP expert, recommendations expert, etc. What are your thoughts about\
    \ this?\u201D"
  sec: 4078
  time: '1:07:58'
  who: Alexey
- line: "It depends on what you want to do with your career. Some companies will only\
    \ ever do one thing. If you're working at an e-commerce site, you'll be exposed\
    \ to a handful of algorithms that you'll be constantly working with. If you go\
    \ and work for a social media site, you may have some overlap of those fields\
    \ of specialization. But there'll be additional ones that will added on top and\
    \ there'll be some that won't be done at all. If you go work for CERN in the south\
    \ of France \u2013 you're not gonna be using any of that stuff. So there are differences\
    \ between pure scientific data science work and commercial data science work.\
    \ It really depends on what you want to do."
  sec: 4095
  time: '1:08:15'
  who: Ben
- line: "But what I always recommend is \u2013 get really good with the core basics\
    \ of data science work. What I mean by \u2018core basics\u2019 is Bayesian modeling.\
    \ You don't have to be an expert in it, but know how those things work, why to\
    \ use them, when to use them. Learn ensembles. When I say \u2018learn ensembles\u2019\
    , I don't mean learn how to apply an API \u2013 anybody can learn that. I mean\
    \ learn how a decision tree is built, why it's built that way. What the hyper\
    \ parameters do. What does it mean that your feature vector has to look like?\
    \ When you move on to from decision trees, how are random forests made? What does\
    \ the code actually look like for constructing that? And everybody should know\
    \ how linear systems work, like generalized linear models. They should understand\
    \ how they optimize, why they're built the way that they are, and what all those\
    \ hyper parameters do."
  who: Ben
- line: "Once you have that, I think every data scientist should strive to become\
    \ experts in those three areas within the first two years of their employment.\
    \ Then they can move into growing that knowledge with advanced statistics of statistical\
    \ models. Like, \u201CHow do time series models work?\u201D You don't have to\
    \ know all of them. There's dozens and dozens of them. But know a few of them.\
    \ Then, as you're moving in knowledge from that, that's when specialty usually\
    \ happens \u2013 four or five years in. Alexey, is that about right? After four\
    \ or five years is when you start to specialize, right? If your company is working\
    \ on NLP, you may become the NLP guru. If you're working on computer vision problems,\
    \ you may become really good with Open CV and TensorFlow and Keras with CNNs.\
    \ That might be your bread and butter, if you want to do that and that's what\
    \ you're passionate about. Yeah \u2013 go all in."
  who: Ben
- line: But when you get to the 10 to 15 year mark as a data scientist, I find most
    people branch out and try to become a specialist in another field as well. It's
    just good for career progression to be able to mentor more people, and to be able
    to contribute more to different problems. It also paves the way to becoming the
    Chief AI Officer or the Chief ML Officer at companies, which I expect will eventually
    become more ubiquitous. That's sort of the pinnacle of career growth for people
    if they want to stay in the field. You have to know how a lot of different things
    work.
  who: Ben
- line: "And you probably can still be successful as a data scientist without specialization\
    \ \u2013 without a niche."
  sec: 4302
  time: '1:11:42'
  who: Alexey
- line: "Yeah, generalists work really great. You don't have to have the ability to\
    \ implement some package from scratch from memory. Having that level of deep understanding\
    \ of something is not required. Some nerds like myself, can think, \u201CHey,\
    \ I want to create a new algorithm that solves this problem where I want to port\
    \ single node or single machine algorithm to a distributed system.\u201D I just\
    \ find stuff like that fun, so I do it, if customers have a use case for it. But\
    \ you don't have to go into that level of specialization. You can be a generalist\
    \ and say, \u201CYeah, I know how to build NLP models. I know how to do association\
    \ roles. I know how to do collaborative filtering. I can implement XGBoost on\
    \ any problem that you have, and I know how to tune it properly. And I know how\
    \ to monitor that.\u201D Yeah, generalists can become pretty successful."
  sec: 4310
  time: '1:11:50'
  who: Ben
- header: How to find Ben online
- line: Okay, thanks. So, let's finish. How can people find you?
  sec: 4371
  time: '1:12:51'
  who: Alexey
- line: "LinkedIn. I\u2019m also the new co-host to the podcasts on Dev Chat TV \u2013\
    \ Adventures in Machine Learning. You can hear me ask a bunch of people. You've\
    \ been on that show, actually. And we're probably gonna have you back. Are you\
    \ around?"
  sec: 4377
  time: '1:12:57'
  who: Ben
- line: Yes.
  sec: 4393
  time: '1:13:13'
  who: Alexey
- line: "Yeah, come check me out there. Find me on LinkedIn. And yeah \u2013 check\
    \ out the book if it sounds interesting. It's in early access and I think it's\
    \ getting published in November \u2013 that\u2019s the plan right now. So yeah,\
    \ you can buy it now."
  sec: 4394
  time: '1:13:14'
  who: Ben
- line: Okay, cool. Thanks a lot for joining us today and for sharing all your knowledge.
    And thanks everyone for watching us and asking questions. Do remember that we
    have three more talks this week. They're all amazing. Check them out if you haven't
    and register for the remaining events. That's all and thanks again. It was nice
    chatting with you.
  sec: 4411
  time: '1:13:31'
  who: Alexey
- line: Yeah, it was nice for me as well. Thanks, Alexey.
  sec: 4435
  time: '1:13:55'
  who: Ben

---

Links:
- [Ben's book](https://www.manning.com/books/machine-learning-engineering-in-action){:target="_blank"} (get 35% off with code "ctwsummer21")



