---
title: "Moving from Academia to Industry"
short: "Moving from Academia to Industry"
guests: [cjjenkins]

image: images/podcast/s06e06-from-academia-to-industry.jpg

season: 6
episode: 6

ids:
  youtube: m4F651BpUFk
  anchor: Moving-from-Academia-to-Industry---CJ-Jenkins-e1bh84o

links:
  youtube: https://www.youtube.com/watch?v=m4F651BpUFk
  anchor: https://anchor.fm/datatalksclub/episodes/Moving-from-Academia-to-Industry---CJ-Jenkins-e1bh84o
  spotify: https://open.spotify.com/episode/5Jvo53ibSoX6rfkfdGq5pJ
  apple: https://podcasts.apple.com/us/podcast/moving-from-academia-to-industry-cj-jenkins/id1541710331?i=1000544589971

transcript:
- line: This week we'll talk about moving from academia to industry. We have a special
    guest today, CJ. CJ worked as a postdoctoral researcher at Martin Luther University,
    which is a university in Germany and then she decided to move into data science.
    Since 2018, she has been working as a data scientist and now she is a data science
    lead. Welcome, CJ. Let's start with your background. Can you tell us about your
    career journey so far?
  sec: 58
  time: 0:58
  who: Alexey
- header: "CJ\u2019s background"
- line: "Yeah. I was an evolutionary biologist for a long time. I did my undergraduate\
    \ Master's and PhD in evolutionary biology. Then, about six months before I finished\
    \ my PhD, I was thinking \u201CI'm not sure I want to stay in academia.\u201D\
    \ But that\u2019s not the time to make life-changing decisions, so I just put\
    \ my head down, finished up, and I was like, \u201CI can figure this out during\
    \ my postdoc.\u201D Then about a year and a half into a three year postdoc, I\
    \ was like, \u201CI don't think I want to do this anymore.\u201D So I shifted\
    \ gears, studied a bunch, and got an awesome job in industry in Berlin. I've been\
    \ a data scientist ever since."
  sec: 88
  time: '1:28'
  who: CJ
- header: Evolutionary biology
- line: "What\u2019s evolutionary biology?"
  sec: 128
  time: '2:08'
  who: Alexey
- line: "Very good question. It looks at how populations of organisms evolve over\
    \ time. When people see \u2018evolutionary biology\u2019 they're like, \u201C\
    And then you ended up in technology?\u201D and I\u2019m like, \u201CHear me out.\u201D\
    \ Because evolution happens to a population instead of an individual, so it's\
    \ rooted a lot in statistics. I think that was one of my edges in getting my first\
    \ data science job, is that I knew more about statistics than anybody else in\
    \ the room. I've been building experiments, running statistics on the data and\
    \ collecting it. I was teaching my students how to do statistics, so \u2013 teaching\
    \ statistics within the courses. So I had a really solid foundation. But on top\
    \ of that, because evolution looks at how populations change over time, it's really\
    \ rooted solidly in math and differential equations, and looking at how population\
    \ dynamics can change. So it's literally just looking at how populations evolve.\
    \ But it gave me a really strong background for things that I ended up using in\
    \ data science."
  sec: 131
  time: '2:11'
  who: CJ
- line: To prepare for this interview, I was going through your LinkedIn profile.
    I actually got the impression that you were also doing data science stuff back
    when you were in academia.
  sec: 196
  time: '3:16'
  who: Alexey
- line: "Depends on how you define \u2018data science stuff\u2019, because I think\
    \ that's an interesting question."
  sec: 213
  time: '3:33'
  who: CJ
- line: "I have a quote. It says you were doing these things: \u201Cmanipulating big\
    \ datasets, analysis of A/B tests, working in environments of large and complex\
    \ data structures, commonly applied advanced statistical and machine learning\
    \ techniques.\u201D Yeah, so this sounds like a usual data science job."
  sec: 216
  time: '3:36'
  who: Alexey
- line: "Yeah. Absolutely. You know, it's funny, because I still rely on a lot of\
    \ those tools. A lot of genomic data is unstructured text files full of sequence\
    \ reads that are three to four gigabytes each. Figuring out how to process those\
    \ in bash requires a certain programming knowledge. But the things that I was\
    \ missing were the deployment component. I had to Google what an API was when\
    \ I first started as a data scientist, and I had to figure out what an infrastructure\
    \ was, what a Docker container was, and all those things. So I had the theoretical\
    \ understanding, and the backing, and a lot of the coding done. But you can ask\
    \ anybody at my first job \u2013 during my first three months, I just like walked\
    \ around with this look of terror like, \u201CI have no idea what I'm doing!\u201D\
    \ [laughs] But I figured it out. Yeah."
  sec: 240
  time: '4:00'
  who: CJ
- header: Learning machine learning
- line: Did you need to learn any machine learning or you basically knew everything
    you needed?
  sec: 285
  time: '4:45'
  who: Alexey
- line: "Oh, no. I had to learn a lot of machine learning. Most of the background\
    \ I had in machine learning was very much based on statistical models. I took\
    \ my first machine learning course, and everybody was talking about how it\u2019\
    s the best, like \u201CMachine learning! Machine learning!\u201D And then I looked\
    \ at it and I was like, \u201CThe first ones you guys talk about is linear regression\
    \ and logistic regression. Those are just statistical methods that I've been using\
    \ for years.\u201D Actually, my first case study for my first job was \u2013 we\
    \ were supposed to build a predictive model so that we could predict transactions\
    \ of individuals. And I sort of cheated because the data was too sparse. So I\
    \ just made a proof of concept by combining the data and then predicting the mean.\
    \ But I use a generalized linear model. It was just a GLM that was tied to a Poisson\
    \ distribution, I think. I can't remember the exact distribution I used, but it\
    \ was just a statistical model."
  sec: 290
  time: '4:50'
  who: CJ
- line: "So basically, for you, the theoretical part of data science, or the theoretical\
    \ part of machine learning, wasn\u2019t scary. You could just watch a course and\
    \ then apply everything you learned and quickly grasp all these things. In that\
    \ sense, the background you had as a researcher helped you a lot."
  sec: 349
  time: '5:49'
  who: Alexey
- line: Exactly. Yeah.
  sec: 368
  time: '6:08'
  who: CJ
- header: "Learning on the job and being honest with what you don\u2019t know"
- line: "Then for the things you didn't know \u2013 you mentioned you didn't know\
    \ anything about deployment, you didn't know what API is, Docker, and all this\
    \ stuff. Yep. Did you have to learn this on the job? It wasn\u2019t before getting\
    \ the job, right?"
  sec: 370
  time: '6:10'
  who: Alexey
- line: "No. I feel like I got really lucky. It's one of those things, like I said,\
    \ and I get asked this a lot from academics, \u201CHow do I move into industry?\u201D\
    \ The unfortunate truth is that I got really lucky with time and place. I moved\
    \ there at a good time, whereas I think the field is really competitive now. They\
    \ also talked about this a lot at N26, which was my first job. They came back\
    \ from my interview and just looked at everybody else in the team and they were\
    \ like, \u201CShe said everything you're not supposed to say in an interview.\u201D\
    \ But I was very open with them. I was like, \u201CHere's a list of things that\
    \ I'm bad at. But I really want to learn from you guys. I don't know everything,\
    \ but I want to learn.\u201D"
  sec: 385
  time: '6:25'
  who: CJ
- line: "But one of those was that I didn't know Python when I started. I had to learn\
    \ that on the job. If I'm being totally honest, I didn't know exactly what a position\
    \ in data science was going to look like. My sister was asking me ahead of time,\
    \ \u201CSo, what are you going to do?\u201D And I was like, \u201CYou know, manipulate\
    \ data\u2026 use data to gain insights. Make data into value.\u201D And she was\
    \ like, \u201CYeah, none of those mean anything.\u201D And I was like \u201CI\
    \ know.\u201D Until I started the job, I wasn't sure what that was gonna be. It\
    \ was a hard crash course. But I think there were a couple things that helped\
    \ me succeed and a couple of them came from academia."
  sec: 385
  time: '6:25'
  who: CJ
- line: "One thing in academia is that you need to be able to teach yourself stuff.\
    \ At that point, I had 14 years experience teaching myself how to do things and\
    \ teaching myself how to learn things. So I did a lot of that. I think one of\
    \ my colleagues is listening, so they can attest to this \u2013 everybody else\
    \ at the company started at 10. The core hours were 10 to 6. And I was usually\
    \ in the office between 6 and 7 and I spent those hours \u2013 between whenever\
    \ I got in and 10, 10:30, when our team did our stand up \u2013 just learning\
    \ new things. Everyone was like, \u201CYou know that you don't need to be in here\
    \ this early?\u201D And I was like, \u201CYou know I don't actually know what\
    \ I'm doing yet, right?\u201D I spent a lot of time figuring it out back then."
  sec: 385
  time: '6:25'
  who: CJ
- line: "I also had incredible colleagues who were willing to sit down and do a lot\
    \ of pair programming with me, which is still my favorite tool with new people\
    \ \u2013 just to sit down and have two people working together to solve the problem.\
    \ Then I could see how to solve the problems by myself. But yeah \u2013 I didn't\
    \ know any of that when I started."
  sec: 385
  time: '6:25'
  who: CJ
- header: Convincing that you will be useful
- line: "That's cool. I'm just trying to think \u2013 some people are listening to\
    \ this and they're thinking, \u201COkay, now I also have this theoretical foundation.\
    \ I know statistics well. I know machine learning well. But how can I convince\
    \ a potential employer that they should hire me and then I learn everything on\
    \ the job?\u201D Let's say, if you don't know Python, if you don't know deployment,\
    \ you don't know API? All you know well is statistics and machine learning. So\
    \ how do you convince an employer to hire you? How do you convince them that you\
    \ will learn everything in, let's say, three months, and you'll be able to start\
    \ being useful?"
  sec: 521
  time: '8:41'
  who: Alexey
- line: "That's a very good question. Again, I think I got really lucky. But from\
    \ the other side now. Now I'm leading and building a data team, so I can speak\
    \ to what I look for in people who might not have a lot of experience. I am specifically\
    \ going to be hiring two new junior people in the spring. But what I'm looking\
    \ for is three things. That they're reasonably smart \u2013 they can pick up on\
    \ concepts quickly. That they have the ambition to learn \u2013 they're open to\
    \ learning and trying new things. And that they can take feedback."
  sec: 565
  time: '9:25'
  who: CJ
- line: "If you're not open to learning new things and you're stuck in your way, it's\
    \ going to be a problem. If you get really defensive when I say something like,\
    \ \u201CHey, maybe you should do this differently.\u201D Then it's going to make\
    \ it hard. But if you have those three things, I don't care what you know. I can\
    \ teach you anything. But if you have those three things \u2013 those are the\
    \ kind of people that you want to invest in as a junior."
  sec: 565
  time: '9:25'
  who: CJ
- line: "So from the counterpoint, if it was somebody who's like, \u201CHow can I\
    \ get my foot in the door?\u201D I think demonstrating those things will work.\
    \ I don't need to see your crazy CV or crazy portfolio, especially for a junior\
    \ position or an entry position. I want to see that you have the ability to pick\
    \ things up quickly and that you can take feedback."
  sec: 565
  time: '9:25'
  who: CJ
- line: How do you test for these things during the interview?
  sec: 642
  time: '10:42'
  who: Alexey
- line: "I'm brutal. [laughs] No, I'm actually really nice. I think this is one of\
    \ the things that you think a lot about as an academic like, \u201CHow do you\
    \ define smart?\u201D This is one of those skills that transfer really well. It\u2019\
    s somebody's ability to absorb and synthesize new information \u2013 they can\
    \ figure out what I'm telling them and then synthesize it with what they already\
    \ know. You can just ask questions like, \u201CTell me about a problem that you've\
    \ worked on.\u201D And then I'll start throwing curveballs at them and be like,\
    \ \u201COh, do you mean like this?\u201D And then I see how they respond to that."
  sec: 646
  time: '10:46'
  who: CJ
- line: "Then, to see if they can take feedback, I just flat out ask them, \u201C\
    Tell me about a time when you were wrong.\u201D I think that's a very different\
    \ question. I had somebody answer this the other day. They told me about a time\
    \ that they had failed. I was like, \u201CThat's not what I was asking. Tell me\
    \ about a time when you were wrong.\u201D I can give you a list of the ways that\
    \ I'm wrong. I'm gonna run a whole series at one of the universities in Stockholm\
    \ about ways that machine learning algorithms in production fail. But being able\
    \ to admit, \u201CHey, I was wrong about this, and this is what I wanted to learn\
    \ from that. Here's how it changed me in the future.\u201D That means that you're\
    \ open to the possibility that you can be wrong, and you're open to other people\
    \ telling you that. I think that's important."
  sec: 646
  time: '10:46'
  who: CJ
- header: "CJ\u2019s first interview"
- line: "Since you mentioned that you will be hiring juniors soon. I guess many people\
    \ are taking notes right now. [laughs] Yeah, but that's tricky to check for these\
    \ three things. But I guess companies also check their theoretical background\
    \ and how well you know all these things. Do you remember how the interview actually\
    \ looked like for you? Like when you were transitioning \u2013 the interview with\
    \ N26."
  sec: 719
  time: '11:59'
  who: Alexey
- line: "Yeah, I remember it very distinctly. I have a good memory. But this one stands\
    \ out in my mind because it was such a weird experience. What was the interview\
    \ process like? \_Okay, it was really easy. [laughs] I got so lucky. I had a friend\
    \ in Berlin who had gone on a Tinder date with a guy at N26 and she was still\
    \ in contact with him. So she told me, \u201CCJ, do you need a hook-up?\u201D\
    \ I applied to four positions at the time. Again, luck. I applied to four positions,\
    \ I had one interview, and I got the job. And it was my number one choice. This\
    \ kind of thing doesn't happen anymore. This is not something that happens these\
    \ days. I got lucky."
  sec: 754
  time: '12:34'
  who: CJ
- line: "At N26, I skipped the recruiting step, because I was a referral. They sent\
    \ me a case study and I spent like a solid week working really hard on it. At\
    \ the time, all of the deployments were in Python. But at the time, they said,\
    \ \u201CYou can do this in Python or R. We don't care about the programming language.\
    \ We just want to see that you know the concepts.\u201D So I did it in R because\
    \ that was my native language. I sent them this case study. A week later, they\
    \ contacted me, \u201CWe\u2019d like to interview you.\u201D I was like, \u201C\
    Okay. Cool.\u201D[swooning] So I sat down with the two data scientists at N26\
    \ at the time and, like I said, it was an hour and a half interview."
  sec: 754
  time: '12:34'
  who: CJ
- line: "I was just like, \u201CHere are all the things that I don't know. I'm really\
    \ excited to learn from you guys.\u201D So all the things that you're not supposed\
    \ to say in an interview. But I think they appreciated the honesty and I felt\
    \ more confident from that point forward, because I was like, \u201CThey know\
    \ exactly what they're getting. I don't have to have imposter syndrome. They know\
    \ my failings before I get in the door. I don't have to pretend to be something.\u201D"
  sec: 754
  time: '12:34'
  who: CJ
- line: "Everybody else was like, \u201CDid you fake it till you made it?\u201D I\
    \ was like, \u201CNo, absolutely not.\u201D Then after that, it was two weeks\
    \ and then I had an interview with the CDO at the time \u2013 chief data officer.\
    \ I'd studied Python in between. I was like, \u201CI have to know Python terms!\u201D\
    \ He, at one point, literally pulled out a computer and was like, \u201CWalk me\
    \ through what this Python code is doing.\u201D I could pick up logically what\
    \ was happening, but I didn't know any of the syntax. So we talked about that\
    \ and then, two days later I had a job offer."
  sec: 754
  time: '12:34'
  who: CJ
- line: Yeah, that's pretty impressive.
  sec: 899
  time: '14:59'
  who: Alexey
- line: "Yeah, it was very easy. It was a lot of luck. But I walked out of the first\
    \ interview \u2013 and keep in mind, up to this point, I've had 14 years as an\
    \ academic, so I've spent my whole life in labs and universities \u2013 and I\
    \ walked out of this interview in this super-cool tech startup. Everyone was walking\
    \ around looking like cool startup tech people in the office. I got to the sidewalk\
    \ and I just bent over laughing so hard, like \u201CI can't believe this is my\
    \ life right now. I can't believe that this is where I am.\u201D But it was time\
    \ to leave academia. So I guess we're moving forward. Yeah. It was bizarre."
  sec: 901
  time: '15:01'
  who: CJ
- header: Transitioning to industry
- line: Did it take a lot of time between when the idea occurred to you that you wanted
    to try something else to your actual first day at N26?
  sec: 936
  time: '15:36'
  who: Alexey
- line: "It was about a year \u2013 a little over a year. I was in London \u2013 which\
    \ is one of my favorite cities in the world \u2013 visiting a friend in January.\
    \ It hit me all of a sudden. It had been building up for a while. It was like\
    \ \u2018death by 1000 cuts\u2019 but that was the final cut where I was just like,\
    \ \u201CI want to be able to choose to live in a city like this someday. If I\
    \ stay in academia, that's never going to be possible. I'm not gonna be able to\
    \ make choices about my life. I'm not gonna be able to choose where I want to\
    \ live. I\u2019m never gonna have enough money to do things like this. So it's\
    \ time to go.\u201D But I looked at my schedule and at that point, in January,\
    \ I had committed to a number of things."
  sec: 947
  time: '15:47'
  who: CJ
- line: "I committed to teaching that spring, I committed to field season that summer,\
    \ I had a couple of PhD students and Master\u2019s students that I needed to get\
    \ into a good position before I left them. And I had a huge talk that I was invited\
    \ to give at this conference at the end of August. So I was just like, \u201C\
    Okay, I'm gonna shelve that idea until August.\u201D I just worked really hard\
    \ as an academic knowing I was going to leave, but continued working really hard\
    \ until the end of August. Then I came back from the conference and completely\
    \ shifted gears. I rewrote my CV, did a Coursera specialization in data science\
    \ to get a more broad view of it. Then I started applying to companies in Berlin\
    \ in the middle of November. I started at N26 in the beginning of February."
  sec: 947
  time: '15:47'
  who: CJ
- header: Tailoring your CV
- line: "Can you tell us a bit about rewriting your CV? Because I told you that, when\
    \ I was reading your LinkedIn \u2013 I don't know how many iterations you did\
    \ there \u2013 but it sounded like very data science related stuff. So I could\
    \ see that you were already doing all this data science stuff before you were\
    \ officially doing it. Yeah, I guess this is more like a framing question \u2013\
    \ how do you put all these 14 years of experience in such a way that people want\
    \ to hire you?"
  sec: 1034
  time: '17:14'
  who: Alexey
- line: "Yeah. It was hard. And again, I'm super lucky. I had really good friends\
    \ who were willing to help me. And because I had really good friends who were\
    \ willing to help me and who had been in industry for a while, I am now always,\
    \ (people are gonna contact me now) but I'm always willing to help other people.\
    \ Random people ping me on LinkedIn and are like, \u201CHey!\u201D And I'm just\
    \ like, \u201CYeah, I'll look at your CV. Yeah, we can talk through the interview.\
    \ Yeah, of course. I'm happy to do it.\u201D I'm pretty active on the DataTalks\
    \ career channel, because I had help \u2013 I couldn\u2019t do this by myself.\
    \ So I feel like I owe the world help in return, because I got really lucky."
  sec: 1067
  time: '17:47'
  who: CJ
- line: "So back to the CV, I was like, \u201COkay, how do we write my CV? It's like\
    \ six pages long. I know nobody's gonna read that in industry.\u201D My friend\
    \ Penny and I did a weekend trip to Italy and she was like, \u201CBring your computer.\u201D\
    \ So we're in Cinque Terre and she hands me a bottle of wine, takes my computer.\
    \ She looks at my CV, and she highlights all of the talks and all of the publications,\
    \ and then she hits the \u2018delete\u2019 button. I was like, \u201COw, that\
    \ really hurts.\u201D And she was just, like, \u201CDrink the wine.\u201D[laughs]\
    \ So I had her to help. I also reached out to a couple of female data scientists,\
    \ and asked them \u201CHow do I do this?\u201D"
  sec: 1067
  time: '17:47'
  who: CJ
- line: "What they said was, \u201CYou need to emphasize the skills that you have,\
    \ and those that you've developed in industry, rather than the things that you've\
    \ done.\u201D So, instead of talking about, \u201CThis is the research I did during\
    \ my PhD.\u201D I changed it to, \u201CHere are the skills that I learned while\
    \ doing the research in my PhD.\u201D I didn't plagiarize, but I would read other\
    \ people's stuff and thought to myself \u201CThat also applies to me.\u201D Or\
    \ like, \u201COh, that's also something that I can put on my list.\u201D Then\
    \ I reformatted it so that the education section was at the bottom \u2013 it didn\u2019\
    t matter anymore where I went to school or what my degrees were, rather what the\
    \ skills that I picked up while I was doing those were. It was genuinely\u2026\
    \ I had good friends and I was very lucky. A nice bottle of wine helped because\
    \ it hurt [laughs]."
  sec: 1067
  time: '17:47'
  who: CJ
- line: I guess most academics have to deal with large datasets at some point. At
    least in STEM, right? For example, I know that my mother, who works in ecology,
    needs to process weather data. She does that in Excel. Sometimes she asks me for
    help to process it. But yeah, I can see how you can reframe this, what she's doing,
    in such a way that it sounds like what data scientists do.
  sec: 1195
  time: '19:55'
  who: Alexey
- line: Yeah, exactly. But I had luck and I had help.
  sec: 1235
  time: '20:35'
  who: CJ
- line: How many iterations did it take for your CV? You said that you had a CV that
    was six pages long. You had this bottle of wine and your friend when you were
    doing this. How many times did you need to redo the whole thing before you started
    applying to jobs?
  sec: 1240
  time: '20:40'
  who: Alexey
- line: "The whole thing, I don't know. I did about 14 iterations. As I said, I did\
    \ this with my friend, Penny. Then I had two different women in industry who just\
    \ were kind enough to look over my CV. Then I had a few other friends from my\
    \ cohort during my PhD \u2013 my friend, Roxy, who had already transitioned into\
    \ industry. I don't want to plug her, but she's doing incredible work and she\
    \ gave me really good feedback. And then I also had my friend Simon, who was also\
    \ transitioning to industry at the same time as me. As a typical academic, I did\
    \ the first iteration and then I sent it out to literally everyone and got all\
    \ of the feedback. I also talked to a couple friends who are recruiters. I was\
    \ just like, \u201CHey, can you take a look at this and see what's important?\u201D"
  sec: 1256
  time: '20:56'
  who: CJ
- line: "Because for a lot of it they were like, \u201CMake sure that you have a PDF\
    \ version (not .docx). Make sure that the font is something that's machine readable\
    \ because a lot of people use scanning software to reduce the number of resumes\
    \ that they have to look at.\u201D So that's why those buzzwords are important.\
    \ I had LinkedIn Premium at the time. My friend Jessica was like, \u201CYou should\
    \ pay for LinkedIn Premium.\u201D Which is something I almost never do. LinkedIn\
    \ asked me to pay for premium twice a week and I'm like, \u201CNo, I'm good.\u201D\
    \ But at the time, I actually did, because it allowed me to see the skills that\
    \ other people were listing as their skills."
  sec: 1256
  time: '20:56'
  who: CJ
- line: "I just sat down and was like, \u201CWhat are my skills? I don't know. I can't\
    \ do anything.\u201D But when I started looking at what other people were listing\
    \ as their skills, I was like, \u201CActually, I can do that. I can do that. And\
    \ I can do that.\u201D So this allowed me to build up this word skill set, based\
    \ on what other people had also done, and that I could then attribute to myself."
  sec: 1256
  time: '20:56'
  who: CJ
- header: Data science courses
- line: Yeah, cool. Thanks for sharing. You mentioned the Coursera specialization.
    There is a comment in the live chat where people are asking for the name of that
    specialization. What was it?
  sec: 1366
  time: '22:46'
  who: Alexey
- line: Yes. It's old school. It was the John Hopkins Data Science Specialization.
  sec: 1376
  time: '22:56'
  who: CJ
- line: The one with R, right?
  sec: 1382
  time: '23:02'
  who: Alexey
- line: Yeah, exactly. I mean, this was fall of 2017. I think it didn't teach me a
    lot of the coding things I needed to know, but I think it gave me a good broad
    overview. Because it's 10 classes, right? It gives you a broad view of the field
    and all the different things that you can inspect in data.
  sec: 1384
  time: '23:04'
  who: CJ
- line: Would you recommend this course now? Or would you recommend doing something
    else?
  sec: 1408
  time: '23:28'
  who: Alexey
- line: "I think it depends on what you want to go into. I should also mention \u2013\
    \ I'm a bit of a masochist. I didn't have any money. So I looked at it and the\
    \ prices were not per class, but per month. Each one was supposed to be one month,\
    \ so it was like a 10-month class. And I was like, \u201CI can't afford that.\
    \ I don't have that kind of time and money.\u201D So I looked at it and I set\
    \ myself a schedule where I did one course a week. That way, I only had to do\
    \ it for like two months. There was also a four day weekend there, because it\
    \ was fall break. And so I did it. I managed to get all of them done in like two\
    \ months so I didn't have to pay for that much."
  sec: 1415
  time: '23:35'
  who: CJ
- line: "But I was really focused at the time and really ambitious. I think it was\
    \ good for where I am now. Because now, I'm leading both data scientists and data\
    \ analysts and data engineers. And at the time, it was really good, because it\
    \ gave me this broad view. But if it was somebody today, I think a lot of the\
    \ field has become a lot more specialized. So I'd ask somebody, like, \u201CWhat\
    \ are you interested in?\u201D I think everybody should take Andrew Ng's machine\
    \ learning course. I think he does just a fantastic job of explaining things."
  sec: 1415
  time: '23:35'
  who: CJ
- line: This is where I started in machine learning.
  sec: 1488
  time: '24:48'
  who: Alexey
- line: "Exactly. It's really good. I think he does a really good job of explaining\
    \ complex things in a very simple way, which, by the way, is one of the most important\
    \ skills that you need as a data scientist. I think the strongest skill I have\
    \ from academia is being able to explain complex things in a simple way. That\u2019\
    s really good to emulate. But I know a lot of people are really into deep learning.\
    \ I think Fast AI has a really great platform for learning deep learning. I think\
    \ if people are more interested in statistics, there's a couple of Bayesian courses\
    \ that I think could be really good. So it depends on what people are interested\
    \ in now. And then I would send them in a different specific direction."
  sec: 1497
  time: '24:57'
  who: CJ
- line: "So you rewrote your CV \u2013 you said you had 14 iterations \u2013 then\
    \ you took a course marathon. You finished the specialization instead of 10 months,\
    \ you did it in 2. Then you decided to move to Berlin, right? You were in Germany,\
    \ but you weren't in Berlin yet. So you just selected the closest tech hub? Or\
    \ how did that happen?"
  sec: 1537
  time: '25:37'
  who: Alexey
- header: Moving to Berlin
- line: "It was almost more organic than that. When I moved from the US, it wasn't\
    \ even on my radar of places I would ever want to live. But living at the university\
    \ in Halle, which is like an hour and a half south, I would have to go to Berlin\
    \ to fly out. Halle has an airport, but it doesn't really fly anywhere. So, I\
    \ spent a lot of time in Berlin and in that year and a half that I was living\
    \ in Halle, I fell in love with Berlin. It wasn't just that it was the closest\
    \ city, it was the place that I wanted to live then. I started looking for jobs\
    \ in Berlin. But I also had, at that point, in my mind a list of places I wanted\
    \ to be because I really liked the product. At that point, I was already an N26\
    \ customer and I was like, \u201CI think this is a great product.\u201D Especially\
    \ as a foreigner, being able to get a card that works quickly, that you can do\
    \ fully mobile that\u2026"
  sec: 1561
  time: '26:01'
  who: CJ
- line: That you can speak English to the support and they reply in English? [laughs]
    Which is not that common.
  sec: 1620
  time: '27:00'
  who: Alexey
- line: "Exactly. Not common at all in Germany. I liked the product and there were\
    \ a couple of companies I was looking at. I was talking to GetYourGuide, but I\
    \ didn't have a reference there, so I was a little bit behind. Then there was\
    \ a data science consulting company who gave really good talks in Berlin. They\
    \ had a whole fantastic seminar series. I interviewed with them, but just the\
    \ initial interview. So it was like, \u201CI love travel. GetYourGuide seems cool.\u201D\
    \ And GetYourGuide\u2019s blog was amazing, so I was attracted to them. So I only\
    \ applied to those two companies."
  sec: 1625
  time: '27:05'
  who: CJ
- line: "So you did pretty thorough research before applying. It wasn't \u2018spray\
    \ and pray\u2019. You were pretty selective."
  sec: 1660
  time: '27:40'
  who: Alexey
- line: "Yeah, exactly. It's so funny, because it's so different when I was leaving\
    \ N26 \u2013 I did the numbers game, the \u2018spray and pray\u2019. But when\
    \ I was applying for my first position, I did all of this research and would read\
    \ up and look at, \u201CDo these people look happy? Does this founder look good?\u201D\
    \ I told my friend Jessica this and she was like, \u201CCJ, it's got to be more\
    \ like Tinder. You just gotta keep swiping. You can't fall in love with the person\
    \ until they respond. Otherwise, you're gonna get heartbroken by somebody who\
    \ doesn't even know you exist.\u201D That's the advice that I give now, but that's\
    \ definitely not what I did. I was just like, \u201CThis product is super cool.\
    \ I want to work with the people who built this.\u201D Then I met the people who\
    \ were there and I was like, \u201CI really feel like I could learn from these\
    \ people.\u201D And I was right. I learned a ton. I had amazing colleagues. I\
    \ got really lucky."
  sec: 1669
  time: '27:49'
  who: CJ
- header: "Being selective vs \u2018spray and pray\u2019"
- line: "Yeah. You keep saying that you were lucky. But if I summarize what you did\
    \ \u2013 you did 14 iterations of your CV. You took this long specialization in\
    \ two months. You were also very selective \u2013 you selected companies that\
    \ you knew. For example, N26, you already knew the brand. You were a customer\
    \ and you knew the product. Maybe it wasn't just luck in the end?"
  sec: 1716
  time: '28:36'
  who: Alexey
- line: It was a lot of luck. But yeah. It was also a lot of work.
  sec: 1746
  time: '29:06'
  who: CJ
- line: "Yeah. At the beginning, you said you just got lucky and that people just\
    \ helped you. But there is more to it than just that. But now your advice would\
    \ be to apply to more companies \u2013 not selecting a few. Instead, you take\
    \ a city and apply to all open positions? Or how would you approach it now?"
  sec: 1751
  time: '29:11'
  who: Alexey
- line: "Um, no. I think I would still\u2026 I would have increased my numbers. For\
    \ example, after I was leaving N26 \u2013 one of my best friends, who is still\
    \ the head of data analytics at N26 \u2013 he knew I was applying when I was leaving.\
    \ I got my first rejection. I was like, \u201COh, I got rejected.\u201D And he\
    \ was like, \u201CYou're gonna have to get over that. You\u2019re gonna be getting\
    \ a lot of those.\u201D But at that point, I had been so selective the first round\
    \ that I wasn't familiar with this feeling. My little sister always says \u201C\
    Find what you love and do it in the evenings and weekends.\u201D And I'm never\
    \ going to be that person. I was like, \u201CI love what I do. And I'm passionate\
    \ about it.\u201D"
  sec: 1773
  time: '29:33'
  who: CJ
- line: "I'm looking for a space where I can be passionate and invested in what I'm\
    \ doing. Sometimes too invested. Even then, I would go through job ads and be\
    \ like, \u201CDoes this look like a cool product? Does this look like a place\
    \ I could really pursue and really be invested in?\u201D But in the second iteration,\
    \ when I applied to like 20 positions, and went through the interview process\
    \ \u2013 I got a lot of rejections. But I applied to many more places. I think\
    \ the market\u2019s a lot more competitive now than it was four years ago."
  sec: 1773
  time: '29:33'
  who: CJ
- header: Moving on to new jobs
- line: Yeah. The second job you had was also in Berlin. It was Klarna, right?
  sec: 1860
  time: '31:00'
  who: Alexey
- line: It was. Yeah. I moved from one FinTech company to another.
  sec: 1864
  time: '31:04'
  who: CJ
- line: OK. So was it difficult for you to make the move?
  sec: 1869
  time: '31:09'
  who: Alexey
- line: "I hate onboarding. But was it difficult to make the move? It was easy to\
    \ make the decision. The Klarna interview process was a lot longer. I had four\
    \ interviews back-to-back. I walked out of each of the rooms for the interview\
    \ and I was like, \u201CI was not the smartest person in that room.\u201D That's\
    \ a great position to be in when you start somewhere new. If you can start in\
    \ a position where other people are teaching you things, then your growth potential\
    \ is huge. So I was like, \u201CThis is a company I want to go to.\u201D Because,\
    \ at the time, there were 36 data scientists and data science and machine learning\
    \ are really embedded in the product. And so I was like, \u201CThis is a place\
    \ where I can really learn a lot and learn from really cool people.\u201D"
  sec: 1874
  time: '31:14'
  who: CJ
- line: "But the first two weeks are the same as everywhere, right? Even in my current\
    \ position, in the first two weeks, you go from a place where you know a lot and\
    \ you are comfortable in your space because you know the product and you know\
    \ the company. You know who to ask if you have crop problems. But then you go\
    \ from that to a space where you know nothing. You have to relearn all of those\
    \ things and you have to relearn those connections. You don't even know where\
    \ to go to get the information. The first two weeks at Klarna, it was very much\
    \ \u201CUgh. All of my friends are at N26. I knew everything there. I was very\
    \ comfortable. Why did I put myself in a position where I'm once again uncomfortable?\u201D\
    \ So, I hate onboarding. But after I got up to speed I really enjoyed my work\
    \ there."
  sec: 1874
  time: '31:14'
  who: CJ
- line: And this is how you moved to Sweden, right? Through Klarna?
  sec: 1968
  time: '32:48'
  who: Alexey
- line: Yeah.
  sec: 1971
  time: '32:51'
  who: CJ
- line: Okay. Because they had a different position in Sweden? And this was how you
    moved?
  sec: 1972
  time: '32:52'
  who: Alexey
- line: "Ah, no\u2026? There's no way for me to say this without sounding arrogant.\
    \ I told my manager \u2013 she and I are still really good friends \u2013 I told\
    \ her \u201CI really want to try out Stockholm.\u201D I was living in Berlin for\
    \ a while and I wanted to try Stockholm. She was like, \u201COkay.\u201D So I\
    \ started looking for a new position in Stockholm and about two weeks into looking\
    \ for a new position in Stockholm, she was like, \u201CI can't afford to lose\
    \ you. I'm just gonna move you to Stockholm. You can work remotely.\u201D And\
    \ I was like, \u201CCool.\u201D"
  sec: 1977
  time: '32:57'
  who: CJ
- line: Ah. So it wasn't for a position. There is also an office there. Is there not?
  sec: 2009
  time: '33:29'
  who: Alexey
- line: Yeah. The main office for Klarna isn't in Stockholm. So it wasn't for a different
    position within Klarna. It was for the same position on the same team, but she
    was willing to move me because I wanted to go.
  sec: 2014
  time: '33:34'
  who: CJ
- header: Plan for transitioning to industry
- line: "Oh, that's nice. Let's say somebody right now lives in a small town in Germany.\
    \ This person works as a postdoc at some university, doing some science. They\
    \ hear that data science is cool, so they think, \u201COkay, maybe I want to do\
    \ that.\u201D Of course, they want to move to Berlin or some other city. For that\
    \ person \u2013 what should they do? How should they approach from where they\
    \ are now to a company, or a startup in Berlin?"
  sec: 2028
  time: '33:48'
  who: Alexey
- line: "Yeah. That's a very good question. I think the biggest thing you can do is\
    \ things like \u2013 try to start engaging with the data science community in\
    \ Berlin. I think it's one of the great things about Berlin \u2013 and Stockholm,\
    \ but very much in Berlin \u2013 is that it's such a thriving data science community\
    \ and people across different companies are super stoked to talk and work with\
    \ each other. So the first step \u2013 or the first piece of advice now would\
    \ be \u2013 go to virtual meetups, or go to them in person if you can manage to\
    \ be in Berlin. Start meeting people, start talking to people about their work."
  sec: 2069
  time: '34:29'
  who: CJ
- line: "In my experience, because it's such a great data science community, most\
    \ people are super stoked to help. Also everybody's hiring, right? So they\u2019\
    re going to be like, \u201CHey. I heard you are interested in this. Maybe you\
    \ should apply to this one.\u201D Or like, \u201CHey, I'm looking for people like\
    \ you. Maybe we should talk more.\u201D But I think getting into that community\
    \ would be the first step, if somebody was working as a postdoc and needed to\
    \ get in there. A remark I've always said is that I'm remarkably bad at networking,\
    \ because I have friends who are like, \u201CYou gotta work the angles. You gotta\
    \ meet the people, so they can figure out how they could do the things.\u201D\
    \ And I\u2019m just like, \u201CI'm not that. I want everyone to be my friend.\u201D\
    \ So I tend to talk to a lot of people and I have a lot of people in the data\
    \ science community. But it's never like, \u201CMake sure that everybody's good.\u201D\
    \ It's just like, \u201CHi! You want to get a beer? I'm CJ.\u201D I think that\
    \ can take you a really long way."
  sec: 2069
  time: '34:29'
  who: CJ
- line: "Then, what else? Or that\u2019s enough?"
  sec: 2167
  time: '36:07'
  who: Alexey
- line: "I honestly think that's enough. Because, like I said, I think for entry level\
    \ data science positions most people are looking for the same thing \u2013 they\u2019\
    re looking for smart people who are willing to learn. Once you start interacting\
    \ with people in the data science community, and it's obvious that you're willing\
    \ to learn, then I think everybody's hiring \u2013 especially right now. I think\
    \ that would be a good way. Then once you have your foot in the door the rest\
    \ is history."
  sec: 2170
  time: '36:10'
  who: CJ
- header: Requirements for getting hired
- line: We also mentioned like half an hour ago when we started, that now, many companies
    don't just do one interview and hire people. The process is more complicated these
    days and the requirements are a bit higher. So what do you think the minimum requirements
    to start the job are nowadays? What do you need to actually know?
  sec: 2203
  time: '36:43'
  who: Alexey
- line: "Excellent question. I can say from the Klarna hiring pipeline, you probably\
    \ have to be better at writing code than I was when I started. I think that's\
    \ the most obvious one. I think the technical test is a lot more arduous, even\
    \ for really junior people. I think learning and understanding what clean code\
    \ is, and what good coding practices are for data science \u2013 I think that\u2019\
    s going to be crucial."
  sec: 2228
  time: '37:08'
  who: CJ
- line: And how does one do that? Do you know?
  sec: 2255
  time: '37:35'
  who: Alexey
- line: "I didn't learn how to do that till after I started. But the way that I learned\
    \ how to get better at programming \u2013 and I still do this \u2013 a data scientist\
    \ friend of mine asked me this today, \u201CHow do I get better at writing code?\u201D\
    \ And I was like, \u201CFind somebody who's better than you are and just pair-program\
    \ with them every week.\u201D I have a fantastic colleague that I worked with\
    \ at both N26 and then they followed me to Klarna. They are much better at Python\
    \ programming than I am. They've been doing it since they were little. So I blocked\
    \ the time on our schedule for like a solid year when we were at Klarna for an\
    \ hour every week."
  sec: 2259
  time: '37:39'
  who: CJ
- line: "All of the meetings in my calendar are named bizarre things, but our meeting\
    \ was called \u2018stuff and things\u2019. We would meet up and pick one Leetcode\
    \ problem and then we would pair-program for an hour every week. This way I could\
    \ learn how he approached things, and I could learn about algorithm things that\
    \ I didn't know. At that point, my first manager was really strict on clean code\
    \ and so I learned a lot of clean coding practices from that. Peer reviews, like\
    \ getting a good peer review process and learning from how other people would\
    \ do things. I think all of that's really good."
  sec: 2259
  time: '37:39'
  who: CJ
- line: "But for me, all that happened after I started in industry. If I was a postdoc,\
    \ the advice I would give is \u201CFind somebody who's better than you are, who\
    \ you can learn from, and really go at that.\u201D But that's also something that's\
    \ really different between academia and industry. One of my colleagues at Klarna\
    \ was brand new, out of academia, and he did a math PhD. He and I had a long conversation\
    \ about how he needs to get better at collaborating. Because in academia when\
    \ you collaborate, it's like, \u201CWe're going to do this project together. I'm\
    \ going to go into this room and do this part of the project by myself. You're\
    \ going to go into that room and you're gonna do that part of the project by yourself.\
    \ Then we're gonna smush it together at the end.\u201D And I was like \u201CIn\
    \ industry, when we say \u2018collaborate\u2019, it means we're gonna sit next\
    \ to each other. There's gonna be one keyboard and you're gonna have to feel comfortable\
    \ looking stupid. You have to feel comfortable admitting that you don't know everything.\u201D\
    \ I think that's a big barrier to get over. But once you get over that, you learn\
    \ so much. So that would be my big thing."
  sec: 2259
  time: '37:39'
  who: CJ
- line: So your suggestion would be to look around and find people who are better
    at coding than you and pair up with them. Then perhaps offer something in return.
  sec: 2388
  time: '39:48'
  who: Alexey
- line: Yep, exactly. Cookies are a great offer.
  sec: 2400
  time: '40:00'
  who: CJ
- header: Publications, portfolios and pet projects
- line: "[laughs] Yeah. And it goes back to the first step, which is networking. Would\
    \ that be enough? So networking, and learning to code. There is a comment about\
    \ a publication being in a top data science journal that says \u201Cfirst authors\u201D\
    . Do you think that would be an important thing to do?"
  sec: 2402
  time: '40:02'
  who: Alexey
- line: Nobody cares. There's one team in Klarna that does research exclusively. They
    do really awesome research and they're a super fun group of guys. I have an ongoing
    debate with one of them about the utility of Bayesian statistics. They're super
    great, but I think most people in industry don't have a background in academia,
    so they don't care about the publications that you've done. I always look at people's
    papers if I see that they've published on LinkedIn. Before I interview them, I'll
    get a background so I understand what they know. But unless you're applying for
    a research position in industry, that's not a skill that's valued, I don't think.
  sec: 2424
  time: '40:24'
  who: CJ
- line: What do you think about a project portfolio and pet projects? Do you think
    it's important to have in order to get a job in data science?
  sec: 2463
  time: '41:03'
  who: Alexey
- line: "When I'm looking for people, it's not. But I think with other people it might\
    \ be. I think if the person you're interviewing with has a background in engineering,\
    \ then I think it makes a difference because they like being able to see what\
    \ you've done. If I see that, my first thought is like, \u201CI like that you've\
    \ put in the effort. But that is so far away from real-world data that you're\
    \ not gonna be able to use a lot of those techniques in real world production.\u201D"
  sec: 2472
  time: '41:12'
  who: CJ
- line: "I had a junior data scientist I worked with at Klarna and she was brand new.\
    \  She just started and came out of her Master's. I even had her do the training\
    \ data. I was like, \u201CHere's a giant training data set.\u201D And she was\
    \ like, \u201CI had no idea how much of this was going to be cleaning the data.\
    \ The datasets always come nice and clean when we do them in school.\u201D I was\
    \ like, \u201CYeah. No. That\u2019s what it looks like. I'm terribly sorry.\u201D\
    \ That's why I think I put less value on that. In my experience, a lot of pet\
    \ projects for data science tend to pull from the really easy to find and really\
    \ clean datasets, and those aren't always very meaningful."
  sec: 2472
  time: '41:12'
  who: CJ
- line: "The projects you did in academia weren't clean. You had to clean them a lot.\
    \ That could be a good portfolio project, right? You could say, \u201COkay, I\
    \ have this massive amount of genomic data of three or four gigabytes.\u201D Then\
    \ you needed to do some bash stuff to digest that."
  sec: 2544
  time: '42:24'
  who: Alexey
- line: "Yeah.\_Even now, when I have a massive data set and I'm trying to figure\
    \ out how I need to parse it, I'll usually turn to bash first. But I think that's\
    \ harder to translate, right? Because if I tell somebody like, \u201COh, yeah.\
    \ You built some de novo transcriptomes on long and short sequencing reads.\u201D\
    \ That means something to somebody in biology. If I'm going for a biotech job,\
    \ yeah \u2013 it's super important. Put it in there. But I wasn't going for a\
    \ biotech job, I was going for a fintech job. Those words don't mean anything\
    \ to the people I'm applying to."
  sec: 2568
  time: '42:48'
  who: CJ
- line: "People always tell us \u201CYou should tailor your CV to the job you're applying\
    \ for.\u201D And I tend to tailor my speaking style to who I'm applying for. If\
    \ I think the person isn't going to understand the jargon, I'm not going to use\
    \ it. I think that that's worked for me in the past, but it depends on what you're\
    \ doing and what you're looking at."
  sec: 2568
  time: '42:48'
  who: CJ
- header: Adjusting to industry
- line: "Yeah, thanks. We have a question about when you transitioned from academia\
    \ to industry, \u201CDid you have to adjust your way of communicating and interacting\
    \ with colleagues? Was it difficult for you?\u201D"
  sec: 2624
  time: '43:44'
  who: Alexey
- line: "Oh yeah. I really hope that nobody who was at N26 when I first started is\
    \ in this conversation, because it was incredibly difficult. They will tell you\
    \ all of the mistakes that I made. But they were mistakes that were easy to learn\
    \ from. One of them was \u2013 I say this to people now, especially if they're\
    \ giving talks \u2013 nobody likes feeling stupid. But it was really hard for\
    \ me to just\u2026 this is so arrogant. It was hard for me to adjust to the idea\
    \ of knowledge that I thought everybody knew. I\u2019ll use an example where I\
    \ was talking to a project manager. We were talking about this A/B test he had\
    \ done and he really wanted to understand whether or not it was significant. So\
    \ I ran this distilled analysis for him. Then I was talking about p values and\
    \ he's just like, \u201COkay, CJ. I need to stop. I have no idea what a p value\
    \ is.\u201D And I was like, \u201COh, okay. Let\u2019s take a step back.\u201D\
    \ [laughs] So things like that."
  sec: 2644
  time: '44:04'
  who: CJ
- line: "But also\u2026 everything. Like the whole idea of Slack, I can\u2019t even\
    \ tell you. I started and I was brand new to the industry, brand new job, brand\
    \ new city \u2013 complete change. I was scared to post emoji responses on Slack\
    \ to what other people were saying for the first week. I was just like, \u201C\
    Oh my God. What if it's an inappropriate thing? What if I'm doing this wrong?\u201D\
    \ That was a whole means of communication that I had to learn better. There was\
    \ so much. But a lot of it was cultural and I think the biggest thing for me is\
    \ this realization that in academia, everybody has a similar experience."
  sec: 2644
  time: '44:04'
  who: CJ
- line: "If you get to be a postdoc, then you know that every single person has done\
    \ a PhD \u2013 there might be some edge cases \u2013 but everybody knows what\
    \ it's like to think, \u201COkay, I have $2 in my hand and that's all the money\
    \ I have to feed myself for the next two weeks.\u201D Right? You have this shared\
    \ experience. And things like, \u201COkay, I defended my dissertation. It was\
    \ incredibly difficult. I cried in the hallway.\u201D But everybody has these\
    \ shared experiences. As you move forward in your career in academia, you have\
    \ these shared experiences that you can bond over. That doesn't exist in industry,\
    \ right?"
  sec: 2644
  time: '44:04'
  who: CJ
- line: "I remember, we were in the bank and we're talking about doing an overdraft\
    \ experiment, and they're like, \u201COh, we'll just issue a couple people 250\
    \ euros in overdraft.\u201D And the people in the bank were like, \u201CWho's\
    \ ever going to use 250 in overdraft. That's no money at all.\u201D And I just\
    \ looked at them like, \u201COh, you've never been poor.\u201D We didn't have\
    \ these things that were shared, things that you can rely on in terms of the culture\
    \ in academia. So I had to shift the way I was communicating with colleagues.\
    \ Not just the tools and not just the idea that I assumed everybody knew a thing,\
    \ but also the shared experience that no longer existed."
  sec: 2644
  time: '44:04'
  who: CJ
- line: Somebody is writing in Slack that they're going through the exact same thing
    with Slack right now.
  sec: 2816
  time: '46:56'
  who: Alexey
- line: '[laughs] It''s terrifying. It was so terrible. All of my colleagues there
    at the time will tell you that I just walked around with this terrified look on
    my face for the first two weeks. And I don''t have a poker face, so everybody
    knew. [laughs]'
  sec: 2823
  time: '47:03'
  who: CJ
- line: "Also, I think, \u2013 in academia, at least \u2013 in the places where I\
    \ was a student or where I visited, it's always rooms. You have rooms where people\
    \ sit \u2013 it's not open spaces. So it's a room with two or three people, but\
    \ it's always a room. Then when you get to industry, it's usually a floor without\
    \ walls and people sit together. Was it also difficult for you to get used to?"
  sec: 2838
  time: '47:18'
  who: Alexey
- line: "Surprisingly, no. But I think that's just a \u2018me\u2019 thing. I could\
    \ see how that would be a problem for other people. But when I get in the zone\
    \ and I'm really focused \u2013 the same thing is true when I'm reading a book.\
    \ There could be bombs exploding around me and I have no idea. When I get focused,\
    \ it doesn't matter what's happening around me. I also like the social aspect\
    \ of it a lot. Like I said, one of my best friends is still the head of data analytics\
    \ at N26."
  sec: 2865
  time: '47:45'
  who: CJ
- line: "At the time, the data team was only 10 people. So the data science team and\
    \ the data analytics team sat right next to each other. Our chairs were right\
    \ next to each other. Day two, we were immediately best friends. So he made me\
    \ laugh, and I have a really loud laugh. But he made me laugh so much that, as\
    \ the data team grew and the data science team ended up in a different space,\
    \ and we weren't sitting next to each other anymore, like half of the office commented,\
    \ \u201CNow that Robin and CJ aren't sitting together, everything is a lot quieter\
    \ around here.\u201D He wasn't making me laugh as much and so the whole area quieted\
    \ down. So I could see how it would affect other people. But the open space wasn't\
    \ a weird thing for me."
  sec: 2865
  time: '47:45'
  who: CJ
- header: Bad habits from academia
- line: "Okay, yeah. I'm also curious, from the skills you had before in academia\
    \ \u2013 we talked about many that were actually useful like being able to clean\
    \ data, to process large amounts of data, and all the statistical things. But\
    \ what about things that weren't useful? Things that were maybe even harmful?\
    \ Were there things like that or no?"
  sec: 2930
  time: '48:50'
  who: Alexey
- line: "Yeah. Oh, I was asked this the other and I forget what my answer was. Things\
    \ that weren't useful. The competitiveness. Like I said, in industry people tend\
    \ to collaborate more. So hiding what you don't know and trying to compete with\
    \ your colleagues \u2013 I think that\u2019s really not useful in industry. I\
    \ think that it can be really harmful. But that's something that's innate in academia,\
    \ because everybody is like cutthroat to beat each other. Yeah. Again, I was really\
    \ lucky that my team was really collaborative at N26. But even then, it took me\
    \ a couple of weeks to feel really comfortable looking stupid in front of other\
    \ people."
  sec: 2958
  time: '49:18'
  who: CJ
- line: "In academia, everybody's really smart, but you're also spending a lot of\
    \ time trying to be smarter. You don't show as many vulnerabilities, so it took\
    \ me a couple of weeks to really feel comfortable. Being like, \u201CI don't know\
    \ this. Can you help me figure it out?\u201D I think that potentially can be really\
    \ harmful. I think the same thing was true of this colleague at Klarna who had\
    \ just come from a math PhD. It took him about two months to admit that he didn't\
    \ know something. He really struggled with that and it was the same problem where\
    \ it's like, \u201CThis is not how we were taught to behave.\u201D But this is\
    \ how you need to behave in order to be successful in this new environment."
  sec: 2958
  time: '49:18'
  who: CJ
- line: "Is that any way to\u2026 you just need to do this, right? You just need to\
    \ be in that environment, learn, and try to adjust, right?"
  sec: 3056
  time: '50:56'
  who: Alexey
- line: "Yeah. The way that I'm doing it now \u2013 because I'm facing a similar problem\
    \ at my current position, where I'm leading people and trying to get them to feel\
    \ comfortable talking to each other and feel comfortable being stupid in front\
    \ of each other. The way that it worked at N26 for me \u2013 we had this Russian\
    \ data engineer who still rules with an iron fist, he's fantastic. He read the\
    \ fine print and found out that you could do a team dinner once a month. There's\
    \ a budget for it. But once a month, you could take the team out to dinner. The\
    \ data team was the only team at N26 who did this often. Once a month, we all\
    \ went out to dinner and just hung out with each other."
  sec: 3065
  time: '51:05'
  who: CJ
- line: "I think a lot of it is being able to break down the barriers, establishing\
    \ that these people are your friends, and that they're not judging you. Then the\
    \ dumb questions can come and then you can feel comfortable asking that. But I'm\
    \ doing the same thing right now where there's a lot of knowledge silos at my\
    \ current company and I\u2019m like, \u201CWe're all gonna go hang out and eat\
    \ dinner. We're gonna go hang out drinking. I'm throwing you guys an event to\
    \ do this.\u201D Just so that I can get people to feel more comfortable looking\
    \ stupid. I also talk about how I fail. I try to get people to feel comfortable\
    \ enough looking dumb in front of each other that they are willing to ask each\
    \ other questions, even if they think in their mind, \u201CThis is a dumb question.\u201D\
    \ If you don't ask, you won't know the answer."
  sec: 3065
  time: '51:05'
  who: CJ
- line: Okay, yeah. Thanks. So basically, people just need to be comfortable with
    each other, get used to each other, and it just takes a bit of time. You don't
    feel comfortable immediately. You just need to give yourself a bit of time and
    then things become easier.
  sec: 3144
  time: '52:24'
  who: Alexey
- line: I hope so. That's been my experience. And it seems to be slowly working in
    my current company.
  sec: 3161
  time: '52:41'
  who: CJ
- header: Topics with long-term value
- line: "Yeah, thanks. This is an interesting question from Mateus, \u201CHave you\
    \ had time to research or explore a topic that may not have an immediate impact\
    \ on your job, but led to long-term value?\u201D"
  sec: 3165
  time: '52:45'
  who: Alexey
- line: Like actual data science topics?
  sec: 3186
  time: '53:06'
  who: CJ
- line: I think so.
  sec: 3188
  time: '53:08'
  who: Alexey
- line: Yes. Natural language processing is one of my favorite things and I employed
    it within other data. But I haven't done many full natural language processing
    assignments. At N26, and then at Klarna as well, I used that time in the morning
    to study and learn new things, like trying new Kaggle competitions and learning
    new techniques. Although I've never deployed a full NLP model, I know that those
    things are useful. Now I'm leading people, so I'm not doing as much as an individual
    contributor, but we have a couple of assignments that will be NLP assignments.
    So I know I can now help other people, my people, to learn the skills that they
    need so that they can succeed in this assignment. Even though I haven't actually
    used it myself yet.
  sec: 3192
  time: '53:12'
  who: CJ
- line: That's quite an interesting perspective. So even though it wasn't immediately
    useful back then, you still help your colleagues. That's cool. What about Kaggle?
    Was it helpful for you?
  sec: 3247
  time: '54:07'
  who: Alexey
- line: "No, because I don't actually compete. I just use it as a source of cool datasets\
    \ and neat ideas. Then I can play around with those datasets and ideas and try\
    \ them out. Also, I'll try it out myself first and try to solve it. But I was\
    \ in the hiring pipeline at Klarna and obviously, I'm hiring now, and it's really\
    \ interesting to see not just how I answered the question, but how other people\
    \ do. That gives me a much deeper experience, because then you're like, \u201C\
    I didn't think about it from that angle. But now that I've thought about it from\
    \ your angle, I've now incorporated that into my own mentality of ways I could\
    \ approach this problem in the future.\u201D"
  sec: 3262
  time: '54:22'
  who: CJ
- line: So Kaggle was useful, but not as a competitive platform.
  sec: 3301
  time: '55:01'
  who: Alexey
- line: Not winning any of them. Yeah. It's really useful to learn how other people
    are doing things.
  sec: 3304
  time: '55:04'
  who: CJ
- line: "There is an insane amount of knowledge there. There\u2019s just so much stuff\
    \ there, in each competition. There's forums there and in the forums there are\
    \ discussions \u2013 and there is an insane amount of information there."
  sec: 3309
  time: '55:09'
  who: Alexey
- line: Yeah, for sure.
  sec: 3327
  time: '55:27'
  who: CJ
- header: "CJ\u2019s textbook"
- line: Um, I know that you wrote a textbook. What was the textbook about?
  sec: 3328
  time: '55:28'
  who: Alexey
- line: "This is such a funny story. When I saw you put this down in the list of questions.\
    \ I was like, \u201CYes, I wrote a textbook.\u201D But it's really funny and it\
    \ wouldn't have happened if I didn't have another really good collaborator. So\
    \ I was teaching this course during my PhD. Parasitology was the course \u2013\
    \ the study of parasites. My PhD is on host parasite coevolution, so it was natural\
    \ that I would be teaching parasitology. But the teacher, the professor, retired\
    \ basically halfway through the semester. So we were sort of left in this position\
    \ where I had to write the course. If you've never written a course from scratch,\
    \ it's incredibly difficult, and it takes a ton of time. It probably put me back\
    \ about a semester from graduating."
  sec: 3334
  time: '55:34'
  who: CJ
- line: "But, I had this colleague, and I had the knowledge. I was like, \u201CI know\
    \ a lot about parasites. I've been studying this for the last 10 years. I know\
    \ a lot about ecology. I know a lot about the evolution of them.\u201D I had some\
    \ ideas for what we could do for the actual class. So I would write and then she\
    \ would edit it in such a way that made it friendlier to the students. We put\
    \ together this whole class on a shoestring budget. We were driving the whole\
    \ thing. We wrote the tests, set up the website \u2013 did the whole thing."
  sec: 3334
  time: '55:34'
  who: CJ
- line: "At the end of the semester, because I was a graduate student, I believed\
    \ that everything I did was worthless. But she has a much better sense of self-worth.\
    \ So she approached the department, and she was just like, \u201CHey, we wrote\
    \ this course. Do you guys want it?\u201D And they're like, \u201CNo, we're not\
    \ buying anything from you. You guys are free labor.\u201D And she was like, \u201C\
    Cool, fuck you.\u201D Then we went to a textbook company \u2013 I looked this\
    \ up the other day \u2013 Hayden Macmillan or something like that. I forget the\
    \ exact textbook company. But she approached them and she's like, \u201CHey, we\
    \ wrote this course. We can turn it into a textbook if you guys are interested.\u201D\
    \ And they're like, \u201CYeah. Sounds great.\u201D"
  sec: 3334
  time: '55:34'
  who: CJ
- line: "So next thing I know, Kim and I \u2013 Kim was my colleague, she's incredible.\
    \ Kim and I are on this phone call talking about cover art for our textbook. I\
    \ was just like, \u201CI don't know how I got here, but this is great.\u201D So\
    \ yeah \u2013 we co-authored this textbook together. Then they set our deadline\
    \ and I remember that four days before the deadline, we had to take all of the\
    \ stuff that we'd written and put it into chapters that made sense. We had a schedule.\
    \ We just sat on her couch \u2013 her husband took care of us \u2013 we just sat\
    \ on her couch for four days rotating between pairs of yoga pants every 12 hours\
    \ while he fed us and did laundry. And we just wrote for four days [laughs]. But\
    \ yeah, it's \u201CThe Evolution and Ecology of Parasitology."
  sec: 3334
  time: '55:34'
  who: CJ
- line: So what was on the cover? A parasite or something like that?
  sec: 3492
  time: '58:12'
  who: Alexey
- line: "Oh, it\u2019s this fantastic photo from one of our students of a parasite\
    \ underneath a microscope. It was pretty cool."
  sec: 3496
  time: '58:16'
  who: CJ
- line: "Slightly unrelated topic, but there is a comment from Aaron, \u201CThere\
    \ are tools for a team to feel comfortable with each other. The tools are liberating\
    \ structures, serious games that people can practice to acquire trust, learning\
    \ vulnerability, and so on.\u201D"
  sec: 3505
  time: '58:25'
  who: Alexey
- line: Totally.
  sec: 3523
  time: '58:43'
  who: CJ
- header: Wrapping up
- line: Do you want to add anything before we wrap up?
  sec: 3525
  time: '58:45'
  who: Alexey
- line: "No. I think, you know\u2026 I feel very lucky because I've been surrounded\u2026\
    \ You asked me before, \u201CHow do you keep finding good people to give talks?\u201D\
    \ I was like, \u201CI've been working with awesome people that are willing to\
    \ teach me cool things.\u201D In that regard, it's taken a lot of hard work and\
    \ I work long hours often. I'm super stoked to be teaching people now. But I also\
    \ feel very fortunate that I've encountered so many awesome people and that I\
    \ get to do something that I love."
  sec: 3528
  time: '58:48'
  who: CJ
- line: Yeah. Thanks for supplying speakers for DataTalks.club.
  sec: 3559
  time: '59:19'
  who: Alexey
- line: Yeah, anytime.
  sec: 3563
  time: '59:23'
  who: CJ
- line: So if you have more speakers, please let me know. [laughs]
  sec: 3564
  time: '59:24'
  who: Alexey
- line: I always have more speakers.
  sec: 3566
  time: '59:26'
  who: CJ
- line: Okay. Thanks. So, how can people find you?
  sec: 3570
  time: '59:30'
  who: Alexey
- line: I'm easy to find on LinkedIn, CJ Jenkins. I think I'm almost always the top
    choice. But yes, CJ Jenkins on LinkedIn.
  sec: 3573
  time: '59:33'
  who: CJ
- line: OK. Thanks a lot. Thanks for joining us today. Thanks for sharing your experience
    with us. And thanks, everyone, for being active and for asking questions. There
    are quite a few comments in the live chat. So thanks for being active and have
    a great weekend.
  sec: 3582
  time: '59:42'
  who: Alexey

---

Links:

- [CJ's LinkedIn](https://www.linkedin.com/in/christina-jenkins/){:target="_blank"}
- Positions for master students: [one](https://www.linkedin.com/jobs/view/2805710562/?refId=s0%2B1cPS1YR3X957qK7Ha5w%3D%3D&trackingId=gcvkgfWd3Y%2B5XGClan6u1g%3D%3D&trk=d_flagship3_company){:target="_blank"} and [two](https://www.linkedin.com/jobs/view/2805710559/?refId=s0%2B1cPS1YR3X957qK7Ha5w%3D%3D&trackingId=bv9f9o1RhJe5wvALsrDExQ%3D%3D&trk=d_flagship3_company){:target="_blank"}
