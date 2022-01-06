---
title: "Developer Advocacy for Data Science"
short: "Developer Advocacy for Data Science"
guests: [elleobrien]

image: images/podcast/s02e02-developer-advocacy.jpg

season: 2
episode: 2

ids:
  youtube: jv5W4jXk4P4
  anchor: Developer-Advocacy-for-Data-Science---Elle-OBrien-epcbak

links:
  youtube: https://www.youtube.com/watch?v=jv5W4jXk4P4
  anchor: https://anchor.fm/datatalksclub/episodes/Developer-Advocacy-for-Data-Science---Elle-OBrien-epcbak
  spotify: https://open.spotify.com/episode/6Hq0ZGPTkDk1h8orfCU78I
  apple: https://podcasts.apple.com/us/podcast/developer-advocacy-for-data-science-elle-obrien/id1541710331?i=1000506315396

transcript:
- line: This week, we'll talk about the developer advocate role and not just the usual
    type of developer advocate, but a developer advocate in data science. We have
    a special guest today, Elle O'Brien. Elle is a data scientist at Iterative, which
    is a company behind DVC and CML. If you don't know what these three-letter abbreviations
    mean, DVC is Data Version Control and CML is Continuous Machine Learning. I've
    been following Elle for a while on Twitter and recently, we got connected on LinkedIn.
  sec: 177
  time: '2:57'
  who: Alexey
- line: "When I was looking through her profile, I noticed that one of the lines was\
    \ \u201Cdeveloper advocacy and outreach, available for speaking engagements\u201D\
    . It wasn't the only line that was there, but it caught my attention because this\
    \ is something I've been curious about \u2013 this role, what it means, what they\
    \ do \u2013 and I wanted to talk to somebody about it. So I decided to reach out\
    \ to Elle, invite her to our chat, and talk more about this topic. Welcome, Elle.\
    \ Thanks a lot for joining us today. It's a pleasure to chat with you."
  sec: 177
  time: '2:57'
  who: Alexey
- line: Yeah. Thanks so much for having me. This is exciting.
  sec: 245
  time: '4:05'
  who: Elle
- header: "Elle\u2019s background"
- line: Before we go into our main topic of developer advocacy, maybe you can tell
    us a bit about your background? What have you done so far and how did you get
    into data science?
  sec: 250
  time: '4:10'
  who: Alexey
- line: "Sure. It was all kind of indirect. I'm an ex-academic researcher, like many\
    \ people that get into data science. For the last decade, I worked in various\
    \ areas of neuroscience research and I was a math major in college. I was doing\
    \ computational models of biological systems \u2013 I did that as an undergraduate\
    \ for a few years and did research there. I did a Master's degree at the University\
    \ of Washington. Then I did a PhD. I kind of got all over. I worked in a lot of\
    \ different labs and we were modeling a lot of different systems, but it was always\
    \ using the same core tools, more or less, of making computational models."
  sec: 262
  time: '4:22'
  who: Elle
- line: "By the end of that time, I could see that there was something I really didn't\
    \ want to miss in machine learning and data science. Part of it is that there\
    \ are a lot of methods that get used there, like nonparametric statistics, and\
    \ the approach of prediction, rather than inferential statistics, and I really\
    \ wanted to get deeper into that. At the same time, I was also feeling a bit troubled\
    \ by the fact that in so many labs I've worked in, code data sharing, collaboration\
    \ and management were still really difficult. Every lab kind of has its own way\
    \ of doing it and it's a considerable burden. It\u2019s like you have a bunch\
    \ of scientists and none of us are really trained for how to manage data that\
    \ we have to keep for years and years or share with a collaborator or completely\
    \ reproduce our code for somebody else. I feel like there definitely has to be\
    \ a systemic change in the tools that we give scientists. So I wanted to go into\
    \ something that addresses that problem."
  sec: 262
  time: '4:22'
  who: Elle
- line: "That's why when I was done with my PhD, (not this past November, but the\
    \ one before that) I joined Iterative. I wanted to work on data version control.\
    \ That was kind of it \u2013 all of my data science proper is kind of self-taught,\
    \ the way that so many data scientists are \u2013 you follow tutorials, you learn.\
    \ I really like getting to work in the ML Ops space now. Although I am going to\
    \ be joining the University of Michigan in just a few weeks as a full time lecturer\
    \ and research investigator in the School of Information. I'm going to be leading\
    \ some classes and developing a curriculum for the Applied Data Science Master's\
    \ program. So I'm leaning even harder into, \u201CHow can we teach this effectively\
    \ and at scale?\u201D"
  sec: 262
  time: '4:22'
  who: Elle
- line: One thing you mentioned was that you got another PhD, not the one you got
    in November? Does that mean you have two?
  sec: 448
  time: '7:28'
  who: Alexey
- line: "Oh, no. I only have one PhD. [laughs] No, I was just trying to think of dates\
    \ when I said that. But, yes \u2013 I only have one PhD."
  sec: 459
  time: '7:39'
  who: Elle
- line: '[laughs] Okay. So you''ll be teaching, among other things, the tools of how
    to make research reproducible?'
  sec: 470
  time: '7:50'
  who: Alexey
- line: "Yeah, some of it is going to be teaching statistics, some is going to be\
    \ supervising students as they are trying to do end-to-end data science projects.\
    \ In an applied data science program, a lot of people want to go on to be data\
    \ scientists and not academic researchers. I think maybe pursuing tools for academic\
    \ researchers is maybe a research area that I like, and my day-to-day teaching\
    \ will probably be very applied. How do we get Junior data scientists \u2013 data\
    \ scientists that are just about to go to the workforce in a few months, who are\
    \ at a pretty high level of awareness of the issues \u2013 the knowledge of the\
    \ tools and the space in order to be able to make some educated choices about\
    \ how to manage their data science projects?"
  sec: 479
  time: '7:59'
  who: Elle
- line: "You know, that's something that universities (from what I see) are missing\
    \ right now \u2013 end-to-end overview of data science projects. So this is really\
    \ great that you decided to do this."
  sec: 533
  time: '8:53'
  who: Alexey
- line: "Yeah, I'm so excited to do it. But making a data science curriculum is a\
    \ lot of the work that still needs to be done. We have to lay out what is the\
    \ data science curriculum and what has to be there. And I suspect a lot of universities\
    \ are going to be doing this in the next couple of years. It\u2019s like you said,\
    \ in my experience, most of data science I just learned by Googling things."
  sec: 547
  time: '9:07'
  who: Elle
- header: Becoming a developer advocate
- line: "When I talked to you on Twitter and asked about this \u2013 when I reached\
    \ out to you saying, \u201CHey, I want to talk to somebody about this developer\
    \ advocacy role.\u201D You replied that this is such an interesting job and that\
    \ you had no idea that this job existed until you got it. Can you tell us the\
    \ story in a bit more detail? How did it happen with you?"
  sec: 573
  time: '9:33'
  who: Alexey
- line: "Yeah. Throughout my PhD, when I wanted to get to work on data science, I\
    \ would often just make myself weekend projects. For one of them, I had taken\
    \ StyleGAN, which is a big, beautiful GAN that was released by NVIDIA with all\
    \ the code and a trained model too. So I trained it on a bunch of frames from\
    \ videos of myself in different outfits that I had in my closet. Then after it\
    \ was trained, I just moved around the latent space and I patched it together\
    \ and I made a video that was just like morphing on my face with different accessories\
    \ around it. I posted it on Twitter, just because I was like, \u201CLook at this\
    \ cool thing I made!\u201D It did low key viral \u2013 it got like a 1000-something\
    \ likes, which was pretty good for my Twitter at the time. Then a bunch of people\
    \ noticed it."
  sec: 599
  time: '9:59'
  who: Elle
- line: "After I posted it I also said, \u201CHey, by the way, I'm looking for jobs.\u201D\
    \ I figured since I was one month away from graduating, did not have a job, and\
    \ I had this thing on Twitter that was doing well \u2013 I just made a separate\
    \ tweet, \u201CBy the way, consider hiring me.\u201D Then Dmitry, who's the CEO\
    \ at Iterative, saw it and he said, \u201CHey, we're looking for somebody for\
    \ DevRel,\u201D and I guess the audition that I had done was \u2013 I made a piece\
    \ of content involving machine learning that people wanted to see. So that started\
    \ it. From Dmitry, I learned that there are, in fact, teams that make things,\
    \ that are looking for people who will take the tools they make and do something\
    \ cool with them that they show other people. I also learned that just getting\
    \ attention on the internet is a viable career path."
  sec: 599
  time: '9:59'
  who: Elle
- line: "Okay, so basically, you played with a tool, you put it on Twitter, it went\
    \ viral, and then you mentioned, \u201CI'm looking for a job\u201D and \u2013\
    \ boom \u2013 you got it. Right?"
  sec: 725
  time: '12:05'
  who: Alexey
- line: Yes, exactly.
  sec: 738
  time: '12:18'
  who: Elle
- header: A day in the life of Elle
- line: "That's a nice story. But your job is not just DevRel \u2013 you're also doing\
    \ data science things. You're also involved in creating these tools, right? So\
    \ what does your day look like? What do you do at Iterative?"
  sec: 740
  time: '12:20'
  who: Alexey
- line: "There's a lot of different stuff. I also work on the product team for continuous\
    \ machine learning, or CML. So I kind of help organize the launch for that \u2013\
    \ making the website, all of our examples, our tutorial. A lot of the work I also\
    \ do is in our docs for that project and trying to understand user feedback on\
    \ it, as well as making some new features. I'm very proud \u2013 I added a PR\
    \ for support for Bitbucket Cloud recently to that. I do a little bit of development,\
    \ but I'm really learning software development. I developed software for years\
    \ as an academic, but it is just not the same as doing development for an open\
    \ source project. I kind of treat this almost as an apprenticeship that I get\
    \ to learn as I go."
  sec: 759
  time: '12:39'
  who: Elle
- line: There are a lot of conferences that I go to, I do a lot of speaking gigs,
    I do videos, I try to shoot a video at least every few weeks. Now I have a list
    of things that some users want and trying to hit those. What else do I do? Quite
    a lot. Right now, we're hiring more developer advocates. Right now I am a team
    of one, so we're growing. Also because I'm going to be reducing my time doing
    this as I will be working at a University, so we're working on hiring. The hiring
    process takes quite a bit. I also do a lot of blog post writing.
  sec: 759
  time: '12:39'
  who: Elle
- line: "Another thing that takes time, that you don't really see or expect, is that\
    \ you have to create code examples for everything. When we have a new tool or\
    \ feature that I want to highlight, it often takes a couple days to create a good\
    \ technical use case. So, you're sitting there, you're coding, you're getting\
    \ a dataset \u2013 it's kind of like a mini data science project. Then at the\
    \ end, you have to make sure it's all completely reproducible, readable \u2013\
    \ it's like turning in a report. Those are kind of fun, but that's some labor\
    \ that I didn't expect, but it\u2019s a part of it."
  sec: 759
  time: '12:39'
  who: Elle
- header: Being a team of one
- line: So, you're doing a lot of blog posts, a lot of speaking, and videos. I see
    that you post videos constantly on your YouTube channel. Then, you also create
    reproducible code snippets. That's a lot of things. How do you decide which to
    work on next, given that you're just a team of one? There are so many things to
    do. How do you decide what should be the next most important thing?
  sec: 902
  time: '15:02'
  who: Alexey
- line: "It's hard. It's really hard. What I often do is have a schedule in mind of\
    \ \u201CWhen are we planning to release this?\u201D And I know when we have a\
    \ release of something, I'm probably going to have to really pitch in on that\
    \ and maybe add some area of docs, perhaps \u2013 something like that \u2013 also,\
    \ working on all the messaging around the release and blogs for that. So those\
    \ are big landmarks in my time \u2013 I know that I've got to work on a release.\
    \ Then, in between those, I get a bit more freedom to do things like make a video\
    \ about a topic that is kind of timeless, so it doesn't matter if I release this\
    \ now or next year since it would still be interesting."
  sec: 932
  time: '15:32'
  who: Elle
- line: But it is quite hard to keep them all going. Sometimes I feel like I'm actually
    debating for the first time ever that maybe I need to put a limit on how many
    talks I accept, because it does take away from the time that you can be writing,
    and they're all important activities. It's really not obvious or easy. A lot of
    it is just an experiment on the run. And I just feel like we're due for a blog
    now. I feel like we're due for a video.
  sec: 932
  time: '15:32'
  who: Elle
- header: Promoting releases
- line: "So it's more like a feeling. Plus, if there is a certain release, you know\
    \ that you will need to prepare for this release \u2013 prepare some supporting\
    \ material, good recommendations, good use cases. Do you also need to stick around\
    \ on Hacker News or Reddit, or do things like that? When you release something,\
    \ do you publish an article? I think you were posted on the top on Hacker News\
    \ a couple of times, right?"
  sec: 1004
  time: '16:44'
  who: Alexey
- line: "Yeah, we've had that a few times. This is another thing I didn't expect,\
    \ but when you put something on Hacker News or Reddit, whether you posted it or\
    \ it's just trending there \u2013 you have to be there. It\u2019s actually a whole-day\
    \ event when something goes big on social media, which is something that I did\
    \ not expect to take up time. If I post a little thing on social media like, \u201C\
    Hey, we have a newsletter out,\u201D I don't have to monitor that. But when we\
    \ have a release, the next eight hours I'm on three different social networks\
    \ tabbing back and forth going \u201COkay, answer any questions. Respond.\u201D\
    \ So it's actually a pretty big production."
  sec: 1032
  time: '17:12'
  who: Elle
- header: Dealing with toxicity
- line: "Also, in Hacker News, it's anonymous \u2013 people can just register there\
    \ and write pretty much whatever they want. Sometimes the level of toxicity there\
    \ in this community is pretty high, I would say. How to deal with that? It's probably\
    \ not easy."
  sec: 1074
  time: '17:54'
  who: Alexey
- line: "It's not. Actually, that is another thing I didn't expect. You really have\
    \ to pick and choose what Internet communities you can be on. I find Hacker News\
    \ and r/MachineLearning are both places where there is a high level of toxicity.\
    \ If I'm just browsing them, it's usually not long before I find something where\
    \ I'm like, \u201COh, I really wish I hadn't read this today. This does not make\
    \ me feel great.\u201D I thought that I would get a thicker skin for them over\
    \ time, and I didn't. I find that it actually never gets easier. So I kind of\
    \ dig in harder on Twitter because I like Twitter better \u2013 the data science\
    \ community there."
  sec: 1095
  time: '18:15'
  who: Elle
- line: "For Hacker News, I kind of go \u201Cas needed\u201D. I know it would be better\
    \ if I was a regular participant and got more \u201Cinternet points\u201D. But\
    \ I don't do that too much. In Reddit Machine Learning I do answer a couple questions\
    \ about every month to keep the account current. But other than that, I don't\
    \ really hang out there, which is a little bit weird when you're advocating in\
    \ communities that you're not really a part of. But luckily, I'm pretty well embedded\
    \ on Twitter and I have a couple of data science Slacks and you have a data science\
    \ Slacks and those are kind of more comfortable, safe spaces, to share something\
    \ and get feedback. So I definitely take advantage of those two."
  sec: 1095
  time: '18:15'
  who: Elle
- header: Developer advocate job description
- line: "Yeah, thank you. Since I was pretty curious about this role, I decided to\
    \ just take a random job description of a developer advocate for a company and\
    \ see what it says. I found this in some Slack, and it said in the responsibilities\
    \ section, the first point was, \u201CYou need to build an open source community\
    \ for the company from scratch.\u201D Not for the company, but for the product\
    \ they have. Then the second point was \u201CTo drive awareness of this product\
    \ by speaking at three to six industry events quarterly, writing blog posts, tutorials,\
    \ creating videos, building examples of using this product for demonstration purposes,\
    \ and building excitement around this product.\u201D Then there was a third point,\
    \ \u201CBe the voice of the community in our development process.\u201D Is this\
    \ a representative description of the position, or is this something that describes\
    \ more of a full stack position? What do you think?"
  sec: 1187
  time: '19:47'
  who: Alexey
- line: It is quite representative. I would say that it's because I think companies
    still have a lot of work to do on learning how to hire DevRel and what DevRel
    should do. This is probably pretty close to what I expected that I would be able
    to do, as one DevRel. I very quickly realized that this is not actually that realistic,
    if you want to do a good job on all three of those, especially people that don't
    do DevRel or don't have experience in it. I think a lot of technical founders,
    probably, believe that community building is the same as content creation and
    presentation, and they're just completely different skill sets. I've had a lot
    of discussions with other DevRels that have helped me appreciate the distinction,
    which is not appreciated by all or even most companies that are hiring, I think.
  sec: 1259
  time: '20:59'
  who: Elle
- line: "Creating or building a community is something that requires a great deal\
    \ of real-time interaction. You actually have to be in Slack, or in the subreddit,\
    \ or on Twitter. You have to be there. You have to be responding to people constantly,\
    \ having conversations, facilitating bigger discussions, and you have to do a\
    \ lot of moderation. You really have to be a leader of a lot of interactions.\
    \ But on the other hand, creating content and videos, and demonstrations, requires\
    \ a great deal of independent solo-focus time. You cannot really do a good job,\
    \ unless you're really going to just switch them up constantly \u2013 which I\
    \ do \u2013 but it's very, very hectic. I don't think it's sustainable in the\
    \ long term. That's part of why we're growing our DevRel."
  sec: 1259
  time: '20:59'
  who: Elle
- line: "I guess if I could say one thing to people that want to hire a DevRel, it's\
    \ that they should consider separating people who are really strong content creators\
    \ from people who are community managers. Managing communities, reaching out to\
    \ people and keeping them engaged is kind of like engineering almost \u2013 social\
    \ engineering of \u201CHow do I create the right conditions for cool things to\
    \ happen and so that people want to show up?\u201D Content creation is just a\
    \ much more, almost solo-focused activity. I'm not sure why those got put on the\
    \ same level like, \u201COh, obviously, the same person would do these,\u201D\
    \ other than maybe because they're just activities that aren't \u201Cengineering\u201D\
    ."
  sec: 1259
  time: '20:59'
  who: Elle
- line: "There is also this third point, like, \u201CBe the voice of the community.\u201D\
    \ Is this something that developer advocates do?"
  sec: 1422
  time: '23:42'
  who: Alexey
- line: "Yeah, I mean, I try. Well, I think the idea is that if you hang around the\
    \ community a lot, you will pick up on what issues people are having \u2013 what\
    \ bugs they have, what feature requests, what big blocks exist that prevent them\
    \ from getting engaged with what you make \u2013 because you want it to be easy\
    \ to get started. If you're around the support channel, perhaps (we have a Discord\
    \ where people come to ask questions), you learn pretty quickly, \u201COkay, what\
    \ are the common stumbling blocks that people are facing?\u201D And \u201CWhat\
    \ are the things that people ask for over and over again that we would be really\
    \ silly to miss those signals?\u201D"
  sec: 1431
  time: '23:51'
  who: Elle
- line: "To some extent, I can do that. But on the other hand, it's the same issue\
    \ of, if I'm in this support channel, then I'm not on Twitter, or I'm not giving\
    \ a talk, or I'm not creating content. Also, building a community is different\
    \ from answering technical questions from users. It's actually something I can\
    \ do, but I feel like to really excel at it, I might need to be more full-time\
    \ embedded in support, or with the users more of the time. With that said, my\
    \ team is very software engineer-heavy, but (I don't know if this is true) there\
    \ are not a lot of people who have experience doing data science, aside from me.\
    \ And I would also include my academic research in this, where we have datasets\
    \ \u2013 we\u2019re modeling it, analyzing it, and we want to have a reproducible\
    \ pipeline that generates our results."
  sec: 1431
  time: '23:51'
  who: Elle
- line: Since I do have that experience and my technical background is probably like
    a lot of data scientists, I can try out our tools and act like a beta tester and
    give pretty incisive feedback about what part of this would just not be intuitive
    for a typical data scientist with our highly variable backgrounds.
  sec: 1431
  time: '23:51'
  who: Elle
- line: Yeah, it makes sense. So basically, it's more a description of a full stack
    role, right? For example, in full stack data science, we have somebody who can
    talk to stakeholders, build data pipelines, train a model, roll the model out
    to production, and then support this model. In a way, it's like five different
    people when we talk about the full stack data scientists. Here, it's the same,
    right? You have a community manager, a content producer, and a person who works
    with support.
  sec: 1561
  time: '26:01'
  who: Alexey
- line: "Yeah. Really, you can analyze a lot of signals coming out of your community\
    \ and we don't even make use of a lot of it. There's so much information you can\
    \ get from your community in so many ways \u2013 metrics and interactions. You\
    \ could easily have a full time job doing that."
  sec: 1607
  time: '26:47'
  who: Elle
- header: DevRel vs developer advocates vs evangelists
- line: I often come across the developer advocate role, and then there is also a
    role also called DevRel. Are they similar? Are they the same? Are they different?
    What do you think?
  sec: 1624
  time: '27:04'
  who: Alexey
- line: "I think they are the same? I am not completely sure. I hope if I'm wrong,\
    \ somebody will come and go, \u201CActually, it's this.\u201D But I think they're\
    \ the same."
  sec: 1640
  time: '27:20'
  who: Elle
- line: "And evangelists \u2013 is this also something that\u2019s in this field?"
  sec: 1652
  time: '27:32'
  who: Alexey
- line: "I think so. Yeah. I think that I would feel pretty similar. Like, \u201C\
    Oh, I have a lot in common with you.\u201D If I met somebody who was an evangelist,\
    \ I would feel like it's quite similar."
  sec: 1658
  time: '27:38'
  who: Elle
- line: "To me, it seems like evangelists are more often on a stage giving talks.\
    \ And evangelizing is basically talking about the product and getting people excited\
    \ about it. This is actually one of the points in this job description \u201C\
    Building excitement around the product.\u201D So this is probably what an evangelist\
    \ would do, right? Get people excited about things."
  sec: 1670
  time: '27:50'
  who: Alexey
- line: "Yes. It's interesting, in the US, the word \u201Cevangelist\u201D is mostly\
    \ used for religious preachers. So I think of somebody who'd be on TV on Sunday\
    \ morning preaching and being like, \u201CCall in for your free Bible today!\u201D\
    \ and it gets people extremely excited. I think of it like that, but for something\
    \ in tech."
  sec: 1703
  time: '28:23'
  who: Elle
- line: "So \u201CCall today for your free AWS credits!\u201D or something like that,\
    \ right?"
  sec: 1728
  time: '28:48'
  who: Alexey
- line: Yes. [laughs] Yeah.
  sec: 1732
  time: '28:52'
  who: Elle
- header: Dealing with the downsides of DevRel
- line: "Actually, the reason I'm interested in this role is because some time ago,\
    \ somebody from AWS reached out to me saying, \u201CHey, we have this position\
    \ called developer advocate.\u201D And I never actually thought about this position\
    \ at all back then. But then I thought, \u201COkay, the description looks kind\
    \ of similar to what I'm doing \u2013 giving talks and producing content. This\
    \ could be an interesting position.\u201D And then, I talked to some people and\
    \ many of them mentioned things like you did, that the people in AWS have to go\
    \ to Reddit, Hacker News and see all this toxicity and deal with that. There\u2019\
    s especially a certain amount of hatred towards AWS in these communities for some\
    \ reasons (I don't know why). So it's not that glorious, from what I understood.\
    \ Some people think it's like a springboard to being famous, right? You're on\
    \ the stage, you're talking all the time. But there are also downsides."
  sec: 1735
  time: '28:55'
  who: Alexey
- line: "That\u2019s really true. It's really true. And I did not plan for that. I\
    \ think I always thought \u201Cinternet points = good\u201D. But then when it\
    \ was my job, I have to say, it's really scary when something is trending or going\
    \ big, because there's just a tremendous amount of online abuse. It happens quite\
    \ a lot. I actually experience a great deal of fear sometimes when things are\
    \ going big, or sometimes it's kind of panicky, and it's not really that fun.\
    \ Like you said, I know Hacker News is like \u201Cthe place to be\u201D, but it's\
    \ not a place I really feel great reading. I don't feel better. Sometimes I'll\
    \ come across stuff that's quite extreme when I\u2019m on it, and I'm really troubled\
    \ by what I read. It's really hard to feel like, every day, I'm going to show\
    \ up and try to evangelize there when I don't even want to be there. So those\
    \ things are really, really difficult. Like you said, they're not glorious."
  sec: 1819
  time: '30:19'
  who: Elle
- line: So how can you deal with that? Let's say somebody is really excited about
    this position or this role, but there are these downsides. Do you have any recommendations
    to people on how to deal with this online abuse on the internet?
  sec: 1885
  time: '31:25'
  who: Alexey
- line: "I mean, I don't. Part of it is just because I don't know that many DevRels\
    \ yet. I'm still kind of growing into the community a bit. I feel like there's\
    \ got to be some solidarity and experience in that and people supporting one another.\
    \ Part of it is that I think platforms have to get better at moderating. I feel\
    \ like it is really easy to get harassed on even places that have a nicer community,\
    \ like Twitter, where everybody has their face and their name most of the time.\
    \ It's still very easy to get harassed and I've seen it happen to a lot of people\
    \ in machine learning \u2013 DevRel or not. When you have a big opinion, people\
    \ will come for you. I think that, if you are underrepresented in some way, like\
    \ if you're a woman, or you are not white, I feel like they can come for you even\
    \ harder. So that can be pretty tough."
  sec: 1904
  time: '31:44'
  who: Elle
- line: "On some forums, I'm anonymous \u2013 my Hacker News, I've made it pretty\
    \ not traceable to who I am. But sometimes you can't avoid it. If you're posting\
    \ like, \u201CI made this!\u201D and there's only three people on this project\
    \ \u2013 they can figure it out. But I also just make sure to try and make a safe\
    \ online presence. I try to check pretty regularly, like, \u201COkay, if somebody\
    \ were to try to harass me or dox me, what could they find?\u201D And I try to\
    \ keep that pretty minimal. Sometimes I'll make sure that, if I see an embarrassing\
    \ picture of me somewhere that's from like, 2009 \u2013 I will write to that website\
    \ and be like, \u201CWould you please take down this picture of me?\u201D Things\
    \ like that."
  sec: 1904
  time: '31:44'
  who: Elle
- line: "But I just feel like there has to be some solidarity for that being a rough\
    \ experience for anybody \u2013 DevRel, professional \u2013 you're not just a\
    \ person who makes things for the internet. So commiserating with people helps\
    \ a bit. It has to be known that it's a job hazard. I feel like if I was supervising\
    \ somebody with this, and they said, \u201CI really need a break from Hacker News\
    \ for a bit.\u201D I would grant that. I would. I think that's valid, because\
    \ you can burn out. I'd even say \u201CIf you're not okay posting here, maybe\
    \ we\u2019ve got to find other avenues.\u201D But I know that for early stage\
    \ startups, it's really the material benefit. Being on the front page of Hacker\
    \ News does change things for you. I recognize the business value of it, and I\
    \ will still do it because I'm all in on my startup. But I just made peace, I\
    \ guess, that \u201COkay, I'm doing this for what it takes.\u201D [laughs]"
  sec: 1904
  time: '31:44'
  who: Elle
- line: Yeah, it's sad. But there are definitely advantages for this role, right?
    Do you think it is a springboard to becoming famous or not really?
  sec: 2068
  time: '34:28'
  who: Alexey
- line: "I mean, maybe a \u201Clow key\u201D kind of fame."
  sec: 2079
  time: '34:39'
  who: Elle
- line: Yeah, I mean in the community and not like on national TV or anything like
    that. [laughs]
  sec: 2084
  time: '34:44'
  who: Alexey
- line: "Yeah. I feel like it's really interesting that as I've done this job, I get\
    \ a lot more followers. I get a lot more talk invitations and I love that. But\
    \ then my family has no idea what that means. The people that I'm close with don\u2019\
    t sense anything different other than that I'm invited to a lot more talks. But\
    \ getting invited to talks is really rewarding \u2013 you get to be on panels\
    \ with amazing people and the more talks you\u2019re in, the more you meet people\
    \ and hear perspectives that you would never have heard before."
  sec: 2090
  time: '34:50'
  who: Elle
- line: "So that\u2019s the benefit, putting aside the risk of burnout \u2013 that\
    \ part is so cool. But at the same time, having a lot of followers gets scary,\
    \ because the more followers you get, the more you're worried about disappointing\
    \ them. Sometimes I feel like I post less risky or adventurous things than I would\
    \ if I had like 100 Twitter followers."
  sec: 2090
  time: '34:50'
  who: Elle
- line: "Again, you have some responsibility and can also turn bad because of the\
    \ things we just talked about \u2013 the online abuse and all that, right?"
  sec: 2148
  time: '35:48'
  who: Alexey
- line: "Right, they're actually here for your brand. When you are a DevRel, what\
    \ you're monetizing is your brand. For some people that's very close to their\
    \ personal life. But for me, it's not. I don't want to tweet a lot about my personal\
    \ life. They really are here for a certain brand of things. So it's kind of a\
    \ personal choice about how much you want to reveal about yourself. But in a sense,\
    \ it means like, \u201CYeah, it's me, but it's also not me.\u201D It's cultivated\
    \ and it's intentional. I do edit \u2013 it's all very intentional. I think that\
    \ if you're a DevRel and you want to have sustainability, you have to be careful\
    \ about what kind of things you want to share regularly."
  sec: 2158
  time: '35:58'
  who: Elle
- header: Skills for DevRel
- line: For somebody who wants to become a DevRel, what kind of skills do they need
    to develop?
  sec: 2211
  time: '36:51'
  who: Alexey
- line: "So, the big one \u2013 it\u2019s both the technical work and the communication.\
    \ You have to be credible as somebody who knows tech. But I don't think it's important\
    \ that you start working at a team or a company knowing everything about their\
    \ product, I feel like if you know how to learn, that\u2019s enough. I feel like\
    \ the biggest skill I got from my years and years of academic research was like,\
    \ \u201COkay, I can jump into a new lab or a new project and I don't know anything\
    \ in their stack, but I can learn it pretty quickly.\u201D I'm not an expert in\
    \ any of these, but I can get started in a couple minutes. I know how to be a\
    \ beginner. Anything new that comes across the desk, I'm not afraid to try. I'm\
    \ not afraid to ask stupid questions and figure it out."
  sec: 2218
  time: '36:58'
  who: Elle
- line: "The kind of experience that you get is not necessarily from knowing everything.\
    \ I don\u2019t know everything in the ML Ops world. There are lots of tools in\
    \ this space that I've never tried and I'm pretty comfortable saying, \u201CYeah,\
    \ I don't know how that works. I don't know what it is.\u201D But you have to\
    \ have some credibility about your own knowledge of the space so that people will\
    \ trust you as an expert \u2013 someone that should have influence. There are\
    \ lots of different ways to do it. On the other hand, you just have to be clear.\
    \ I think the biggest difference between experienced technical communicators and\
    \ not experienced technical communicators is that after a while, you learn what\
    \ details to cut so that people really just focus on what's important."
  sec: 2218
  time: '36:58'
  who: Elle
- line: "Sometimes you just have to not be afraid to be simple and plain in your language,\
    \ because getting people to understand is much more important than showing everything\
    \ you know. The communication has to be there. It's a combination of \u201CCan\
    \ you at least look like you know something about what you're doing?\u201D and\
    \ \u201CCan you be clear to people who are really coming from a lot of very different\
    \ backgrounds?\u201D \u201CCan you try to put yourself in the shoes of somebody\
    \ new and say things in the way that they need to hear it?\u201D"
  sec: 2218
  time: '36:58'
  who: Elle
- line: Okay, so basically being able to learn and being able to teach are the two
    key skills, right?
  sec: 2363
  time: '39:23'
  who: Alexey
- line: I think so. Yeah.
  sec: 2369
  time: '39:29'
  who: Elle
- line: How important is it to have a technical background? For example, the videos
    you make are about technical tools. You need to know all these things at a pretty
    good level, right? You also need to be able to answer questions, not just at the
    beginner level, but also about your own product and how this product can work
    with some other things. So you need to have a certain technical background to
    be able to do that, right?
  sec: 2371
  time: '39:31'
  who: Alexey
- line: Elle
  sec: 2371
  time: '39:31'
  who: Alexey
- line: Yeah.
  sec: 2371
  time: '39:31'
  who: Alexey
- header: Diversity of backgrounds
- line: Alexey
  sec: 2371
  time: '39:31'
  who: Alexey
- line: If somebody without a technical background wants to start a DevRel role, would
    that be a problem for them? How important is it to have that, in your opinion?
  sec: 2371
  time: '39:31'
  who: Alexey
- line: I think it is not important to have a formal technical background. I think
    that there are a lot of ways to learn. The things that I would want to see would
    be blogs. Start with a blog about something that you're teaching yourself. Teach
    yourself something. And it can be something that's kind of basic, and then you
    can write a blog about it and how you learned it and what you did. Make a little
    tutorial for somebody else and it kind of serves as a note for yourself and a
    bit of a lesson. When you try to teach someone, you learn it even better. It really
    can be fairly simple stuff that you start with. I think that technical skills
    can be gained.
  sec: 2420
  time: '40:20'
  who: Elle
- line: "I know people that have transitioned into data science jobs, DevRels and\
    \ not, with their background being like, \u201CI have a Master's in marine biology\u201D\
    \ or maybe something that's maybe tech adjacent. I also know people that don\u2019\
    t have a tech background. I work with a guy who, (not at not at Iterative, but\
    \ at Michigan), who has a History PhD. He taught himself software development\
    \ and data science skills \u2013 now he's one of the instructors."
  sec: 2420
  time: '40:20'
  who: Elle
- line: "So I think there is a lot of room for people who are coming in from a nontechnical\
    \ background. In fact, it can be an asset, in a way, that you really do get the\
    \ experience of being a beginner, and you can learn \u201CWhat was it like? When\
    \ I was a beginner at this, what parts of this were really confusing for me?\u201D\
    \ Then you take note of that and you take that with you. For me, all the times\
    \ I didn't know something were actually the most informative for this job."
  sec: 2420
  time: '40:20'
  who: Elle
- line: "So basically, if somebody is not super technical or doesn't work as a software\
    \ engineer right now, one way of getting this position and becoming a developer\
    \ advocate would be learning in public, right? You just learn something, put it\
    \ online \u2013 write an article about your experience. This is how you would\
    \ go about it, right? You start communicating about your learning process, then\
    \ people notice you, and then maybe your tweet goes viral. Like you mentioned,\
    \ \u201CBy the way, I'm looking for a job.\u201D This is a good recipe for getting\
    \ a job as a developer advocate, right?"
  sec: 2532
  time: '42:12'
  who: Alexey
- line: "Yeah. Definitely what I recommend to people is to start blogging on a platform\
    \ that you like. Medium is a good one. Towards data science, it\u2019s a really\
    \ good place for that. There's a lot of beginner ones there. Post on Twitter.\
    \ If you're in the r/ community, I really recommend r/bloggers. You can also go\
    \ to language-specific sites and aggregators. But just start making things."
  sec: 2575
  time: '42:55'
  who: Elle
- line: "Yeah, it makes sense. You talked to other developer advocates and DevRels\
    \ \u2013 what kind of backgrounds do they have? What kind of background did they\
    \ have before becoming DevRels? Is there some pattern that you saw? Were they\
    \ usually software engineers in the past? Or is there really no pattern?"
  sec: 2605
  time: '43:25'
  who: Alexey
- line: "In my experience \u2013 and this is not all of them, by far \u2013 but I\
    \ noticed that there's a lot of people that are kind of creative, like working\
    \ on a lot of different things, like learning things. There's often a little bit\
    \ of silliness, too. A lot of us really like having a light-hearted tone and we\
    \ like making things that are going to make people laugh. I think a lot of the\
    \ best DevRels are people that maybe would have been comedians or something in\
    \ another life. You don't have to be funny to be a DevRel, but I do notice a lot\
    \ of my favorites are really funny people. But other than that, I do think that\
    \ one of the cool things about data science in general \u2013 DevRel or not \u2013\
    \ is that there are a lot of different backgrounds here."
  sec: 2629
  time: '43:49'
  who: Elle
- line: "Yeah, being funny is probably a good way to build a connection with the audience.\
    \ And this is what you need to do as a DevRel, right? To build a connection so\
    \ people can relate to what you're saying, listen to your stories, and actually\
    \ go and want to try the product you're advocating for. This is probably the pattern\
    \ you're seeing \u2013 that these people are relatable and easy to connect with.\
    \ Okay."
  sec: 2686
  time: '44:46'
  who: Alexey
- header: Is DevRel for me?
- line: "So the background doesn't really matter in this case, right? There are some\
    \ people who were computer software engineers in the past, some from marketing,\
    \ or somebody that even has a background in history. But let's say that this role\
    \ sounds interesting to me and I want to become famous, go to conferences, talk\
    \ to people, be on the stage \u2013 be in the spotlight. How do I understand that\
    \ this is indeed for me? It does sound amazing, except for the parts that we talked\
    \ about. So let\u2019s say that I think it might be for me, but I don't want to\
    \ quit my job right now, only to find out in two months that it's not for me.\
    \ Is there a way to check if I would enjoy this kind of work or not?"
  sec: 2715
  time: '45:15'
  who: Alexey
- line: "To some extent, yes. A lot of people who are full-time developers or data\
    \ scientists maintain blogs and they maintain their Twitter presences. I feel\
    \ like that is very close to what the job is like. But, at the same time, anytime\
    \ you take something that was your hobby and turn it into your full time job,\
    \ it's just completely different. It's like the people on Instagram who are like,\
    \ \u201CI'm quitting my job to be a full-time Baker and post videos on Instagram!\u201D\
    \ And then they go, \u201COh, man\u2026 I didn't expect there to be so much growth\
    \ hacking and all these things I do just to try to get people to look.\u201D I\
    \ didn't really know about that and in that way, I think it's actually harder\
    \ for me than I expected. But maybe if you're somebody who's really strategic,\
    \ and enjoys being strategic about your content, that could be a good signal."
  sec: 2772
  time: '46:12'
  who: Elle
- line: "If you find that you want to be blogging all the time \u2013 that is a good\
    \ sign. Or if you're into the community management side, if you really want to\
    \ be leading a community and interacting with people all day \u2013 if you just\
    \ want to hang out on your Discord server much more than you want to code, that\
    \ could be a good sign. But, it's just a little hard, I think, until you're really\
    \ putting in a lot of hours over a long time. Because, for me, all these things\
    \ take up more time than I ever expected. That\u2019s maybe the biggest downside.\
    \ It's definitely a job I would still recommend to a lot of people. But to be\
    \ totally honest about it, it is hard to not have as much time for things like\
    \ research and development because you\u2019re spending so much on content and\
    \ growing your audience."
  sec: 2772
  time: '46:12'
  who: Elle
- header: Growth hacking and metric boosts
- line: You mentioned that people don't consider that it will involve a lot of growth
    hacking and things like that. But it actually does involve these things, right?
  sec: 2886
  time: '48:06'
  who: Alexey
- line: It can. Yeah.
  sec: 2896
  time: '48:16'
  who: Elle
- line: Do you have any growth hacking tips?
  sec: 2898
  time: '48:18'
  who: Alexey
- line: "None. I am not a good growth hacker. After a certain point, I just talked\
    \ to Dmitry and I was just like, \u201CI really don't know how to growth hack.\
    \ I don't have that skill set. And I'm not really that interested in learning\
    \ it either. So I think if you want that, it's gonna have to come from somebody\
    \ else.\u201D That's another thing \u2013 that's a skill set that people might\
    \ assume I have, like \u201COh because you write blogs and make videos, you know\
    \ all about social media and how to keep up an audience.\u201D And I really don't.\
    \ I guess my philosophy is \u2013 I don't believe in cheap views. I know you can\
    \ write a clickbait title to get people to show up, but I don't believe they'll\
    \ keep showing up if you do that."
  sec: 2901
  time: '48:21'
  who: Elle
- line: "That's another thing. Sometimes people really care about metrics. They want\
    \ to see your audience taking off. Yeah, I did have more views on my YouTube channel\
    \ when I could release a video every single week, but I simply can't keep up that\
    \ pace. I'm really absolutely dogmatic. Maybe I will do things sustainably and\
    \ slowly and I do not want my metrics to spike. I want organic, real growth that\
    \ I can sustain. And I will do that by continuing to release quality content at\
    \ a schedule that I can manage. So that's my philosophy. But if you're a startup\
    \ \u2013 yeah, you want big numbers sometimes. You want to be able to show your\
    \ investors big numbers. So there's a whole other side of it that other DevRels\
    \ are probably more qualified to answer than me."
  sec: 2901
  time: '48:21'
  who: Elle
- line: "But you do make your videos quite entertaining and interesting. I don't know\
    \ if you have this rainbow colored\u2026"
  sec: 3008
  time: '50:08'
  who: Alexey
- line: I have the owl. Yeah. I always have the owl.
  sec: 3019
  time: '50:19'
  who: Elle
- line: That is maybe one of the growth hacks, because this is like the mascot. Every
    time I go to the DVC channel, I see this little guy.
  sec: 3025
  time: '50:25'
  who: Alexey
- line: "Divi? Yes. It really is the mascot. I just love Divi so much. Actually, when\
    \ I was a kid, I used to make a lot of videos that I would post on my social networks\
    \ of just being silly. This feels like that. I just get to goof off with this\
    \ completely ridiculous technicolor owl. I just wish I could be in the room when\
    \ they decided \u201CWe're going to sell this.\u201D I just love it and I want\
    \ everybody to see this."
  sec: 3043
  time: '50:43'
  who: Elle
- line: "That could be one of the growth hacks that you can share the next time somebody\
    \ asks you. \u201COkay, just bring the rainbow color or something that attracts\
    \ people.\u201D Because this is on every video, right? Was there one without it?"
  sec: 3072
  time: '51:12'
  who: Alexey
- line: "Oh, I'm completely committed to featuring Divi in every video. I also just\
    \ want people to know that this isn't that serious. I used to go to a Data Visualization\
    \ Meetup Group, back when we could meet in person, and it was held in a cupcake\
    \ shop. It was this bright pink cupcake shop. It was just the perfect kind of\
    \ \u2013 it's cool. We don't all have to be like hackers. We can just be people\
    \ who are going to try this together. So I like comedy that way."
  sec: 3089
  time: '51:29'
  who: Elle
- header: Importance of teaching
- line: "We don't have a lot of time left, so let me quickly check if we have questions.\
    \ Yeah, we don't. Except from Angel who was saying that he wasn't a troll. Sorry\
    \ about that. Yeah. I'm also interested in this \u2013 you mentioned that you're\
    \ going to be teaching soon. In your opinion, how are these two things related\
    \ \u2013 being a DevRel and being a good teacher? Does a DevRel always need to\
    \ be a good teacher?"
  sec: 3126
  time: '52:06'
  who: Alexey
- line: "I think on some level, yes. But not in the same sense of being able to put\
    \ together a classroom lecture. Of course, you also don't have to grade anybody.\
    \ But you do have to spot \u201CWhere are people struggling to learn something?\
    \ What are the spots that I really need to help them on?\u201D Honestly, when\
    \ I make YouTube videos, one of the coolest things about it was that I would get\
    \ questions from students in other countries. They would write and be like, \u201C\
    Hi, I'm an undergrad doing this. What should I do?\u201D And you end up kind of\
    \ advising a lot of people. That part is really sweet and really rewarding. It's\
    \ cool. So that part, I think, is a lot like teaching."
  sec: 3164
  time: '52:44'
  who: Elle
- line: "Of course, teaching comes with a lot more things. You have to make a syllabus\
    \ and you have to grade, you have to create a curriculum \u2013 all that. But\
    \ I kind of wanted that. I think everybody who does data science needs to know\
    \ something about the craft of it, like \u201CHow do you manage developing your\
    \ code and your data?\u201D I want to make sure that that's not just the thing\
    \ that data scientists learn after the fact, on the job. I want to be intentional\
    \ about \u201CWhat's in the curriculum?\u201D If you pay for a Data Science Master's,\
    \ \u201CWhat do you get?\u201D I want to control that. So that's kind of why I'm\
    \ going back into a university, because I want to help standardize this a bit."
  sec: 3164
  time: '52:44'
  who: Elle
- line: Honestly, one of the things I was most worried about was losing the international
    audience. I feel like, as a DevRel, you have students all over the world and it's
    all free. It's all accessible for them. So one of the things I made sure of when
    I took the job was that I would continue to have copyright over all of my teaching
    materials so that I could share them. Because I don't want to stop providing materials
    to students that happen to be outside of the university.
  sec: 3164
  time: '52:44'
  who: Elle
- line: So you plan to record videos and put them online?
  sec: 3286
  time: '54:46'
  who: Alexey
- line: Definitely some. I have found that YouTube is a really good channel and I
    like it a lot. Also, I find that there's less toxicity as a creator there. And
    it's really fun interacting with people. People wait for your videos and you get
    regulars, and that's really cool. I'm definitely planning on continuing to have
    YouTube videos. If people are asking a question in class a lot, I'll probably
    just make up a video explaining it and put it out like a three minute video. It's
    just a great reusable resource for people.
  sec: 3291
  time: '54:51'
  who: Elle
- line: Yeah, that's great to hear that you managed to convince the university to
    allow you to do that. I'm personally looking forward to seeing those videos. I
    think we need more videos like that. Especially, at University, we need more lectures
    that prepare students for real life. Because most of the time, like you said,
    people just learn at work. But a university is supposed to prepare them for work,
    right?
  sec: 3328
  time: '55:28'
  who: Alexey
- line: "Yeah, definitely. Like I said, I was in school for like 10 years and I still\
    \ never had anybody really teach me how to use Git, even though every lab wrote\
    \ code. I think they realize now that there's a gap. One of the worst things,\
    \ when I was doing my PhD, you'd hear people say constantly things like, \u201C\
    Oh, yeah. You'll be ready for industry.\u201D And then I got there and I just\
    \ wasn't. [laughs]"
  sec: 3357
  time: '55:57'
  who: Elle
- line: "[laughs] Yeah, I've heard that story so many times. I was also a person who\
    \ shared the same story. Except it wasn\u2019t a PhD, I was talking about a Master\u2019\
    s, but this is a really common theme."
  sec: 3386
  time: '56:26'
  who: Alexey
- header: Finding Elle online
- line: Okay. Thanks a lot for coming today and sharing your experience with us. Do
    you have any last words? Where can people find you?
  sec: 3399
  time: '56:39'
  who: Alexey
- line: "Last words? Yeah, you can follow me on Twitter or LinkedIn. We've got a YouTube\
    \ channel, which we can probably provide a link for. Basically, I hope that more\
    \ people become DevRels, especially people who have really different backgrounds.\
    \ I just tend to find that sometimes, when you're an outsider from somewhere,\
    \ it gives you a really good perspective about what it's like to learn and that\
    \ can make you one of the most effective teachers. Also people who really understand\
    \ how to tell stories, how to make great graphics, great videos \u2013 all of\
    \ that. It's like getting to be like your own little video studio. It can be really\
    \ creative and really rewarding. That is why it can be worth going through all\
    \ of the really difficult parts, too. So I hope that this has been helpful for\
    \ you in figuring out if it might be something for you. Or if you're a company\
    \ that is looking to hire, I hope it's helped clarify some of the different parts\
    \ of DevRel and how it's actually quite a few independent facets. Sometimes you'll\
    \ find a unicorn who can do it all and sometimes it takes a team."
  sec: 3407
  time: '56:47'
  who: Elle
- line: Yes. Thanks a lot for being here today and sharing your experience. And thanks
    everyone else for being here as well. Let's see each other again next week. Thanks,
    Elle. Goodbye.
  sec: 3492
  time: '58:12'
  who: Alexey
---
