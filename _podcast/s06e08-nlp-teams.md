---
title: "Leading NLP Teams"
short: "Leading NLP Teams"
guests: [ivanbilan]

image: images/podcast/s06e08-nlp-teams.jpg

season: 6
episode: 8

ids:
  youtube: RJEf6mzxh1w
  anchor: Leading-NLP-Teams---Ivan-Bilan-e1c4929

links:
  youtube: https://www.youtube.com/watch?v=RJEf6mzxh1w
  anchor: https://anchor.fm/datatalksclub/episodes/Leading-NLP-Teams---Ivan-Bilan-e1c4929
  spotify: https://open.spotify.com/episode/0jE1rpmLCYkD3GnUa2E7E3
  apple: https://podcasts.apple.com/us/podcast/leading-nlp-teams-ivan-bilan/id1541710331?i=1000546053682

transcript:
- line: "This week, we'll talk about NLP teams. We have a special guest today, Ivan.\
    \ We already had Ivan as a guest a few weeks ago, where he also talked about NLP\
    \ and gave an introduction to the topic. One of the things he talked about was\
    \ an NLP team \u2013 who is part of an NLP team and their roles. Ivan posted an\
    \ outline of members of NLP teams on LinkedIn and they got a lot of engagement\
    \ and attention. So we thought it would be cool to spend some time talking more\
    \ about this in general \u2013 about leading NLP teams, members of the team and\
    \ so on. Ivan works as an engineering manager at Personio. Do I understand correctly\
    \ that you do not manage an NLP team right now?"
  sec: 114
  time: '1:54'
  who: Alexey
- line: No, not right now.
  sec: 163
  time: '2:43'
  who: Ivan
- header: "Ivan\u2019s role at Personio"
- line: But you used to. So you are currently working on identity and access management.
    This is what Personio is doing, right?
  sec: 144
  time: '2:24'
  who: Alexey
- line: "Yes. Personio is an HR platform. My team, specifically, is responsible for\
    \ basically everything related to the login experience of the users and also the\
    \ access rights. In an HR platform, there\u2019s a lot of personal data that we\
    \ handle, so we have to make sure everything is as secure as possible and that\
    \ it adheres to all the standards. We are an internal product team, so we provide\
    \ tools for other teams at the company."
  sec: 175
  time: '2:55'
  who: Ivan
- line: "We have our own tooling around access rights that other teams can use, which\
    \ can help them in their features and their parts of the application. They can\
    \ check whether a specific user is supposed to have access to a document of some\
    \ sort or to someone\u2019s salary, to name some examples. A manager is only supposed\
    \ to see salaries of his subordinates, but not the other way around \u2013 things\
    \ like that."
  sec: 175
  time: '2:55'
  who: Ivan
- line: "Yeah, that must be quite a complex problem. Ivan\u2019s main technical interests\
    \ include building microservices for data-intensive applications, MLOps for NLP\
    \ and deep learning research. We'll talk about some of these things today. Welcome\
    \ to our event."
  sec: 245
  time: '4:05'
  who: Alexey
- line: "Thanks for having me. I\u2019m looking forward to answering the questions."
  sec: 267
  time: '4:27'
  who: Ivan
- header: "Ivan\u2019s background"
- line: Before we go into our main topic of NLP teams, let's start with your background.
    Can you tell us about your career journey so far?
  sec: 272
  time: '4:32'
  who: Alexey
- line: "Yeah, sure. I come from Ukraine and studied general linguistics for a while\
    \ as I lived there. I moved to Munich about 10 years ago and decided to pick up\
    \ computational linguistics, so it was a continuation of what I was doing before.\
    \ Computational linguistics, as a field, was relatively new back then. It was\
    \ centered primarily on machine learning and how that can be applied to text understanding\
    \ and text analysis in general. Back then it was still done with Perl and eventually\
    \ it moved into Python. Now it\u2019s sort of the industry standard."
  sec: 279
  time: '4:39'
  who: Ivan
- line: Over time, I worked actually on different projects and in different teams.
    I did not only work on NLP and AI. My first jobs were in building interfaces for
    desktop apps, so I worked a lot with C#, C++, etc. Eventually, I worked on web
    scraping for quite a while. Then I moved into data engineering and was working
    on ETL pipelines with Spark and Hadoop. For a while, I also worked as a data scientist,
    which was at a company called Trust, where we were working on aspect-based sentiment
    analysis, on text summarization, and a few other NLP tasks. This is where the
    core of my NLP knowledge comes from.
  sec: 279
  time: '4:39'
  who: Ivan
- line: "That was super challenging because we had to support our solutions for 23\
    \ different languages and some of those languages are super complex. I think the\
    \ most complex languages I worked with would probably be Japanese and Thai \u2013\
    \ Asian languages that are very, very different compared to regular English NLP\
    \ that you would normally do. So that was quite interesting."
  sec: 279
  time: '4:39'
  who: Ivan
- line: Eventually, I went into management. I actually got another degree in Technology
    Management here in Munich, at the CDTM. I've been managing teams for a bit over
    two years. I managed data engineering teams, NLP teams and now it's more of a
    web product-based team at Personio.
  sec: 279
  time: '4:39'
  who: Ivan
- line: Interesting. Do you still use Perl?
  sec: 442
  time: '7:22'
  who: Alexey
- line: No, not really, [laughs] Yeah, it's a language that's hard to read. It also
    depends on who writes the code, because the formatting there is not very strict.
  sec: 445
  time: '7:25'
  who: Ivan
- line: I remember the day when I needed to figure out how a Perl program works. There
    was a web scraper written in Perl that the company where I worked used. It dumped
    data in a specific format that was only possible to read from Perl. So I had to
    hack a program that reads this and converts it to JSON. It really messed with
    my brain. I'm not the same person as before after doing that. [laughs]
  sec: 460
  time: '7:40'
  who: Alexey
- line: Yeah. Perl is actually a very powerful language. I know it's still used in
    cybersecurity to some extent. It's really good for salting passwords and stuff
    like that. But I actually haven't worked with it for quite a few years. It's probably
    changed a lot.
  sec: 490
  time: '8:10'
  who: Ivan
- header: Studying technical management
- line: "You mentioned that you also got a degree in technical management. Was it\
    \ a Master\u2019s degree?"
  sec: 513
  time: '8:33'
  who: Alexey
- line: "It was sort of an honors\u2019 degree. It's like an additional program to\
    \ Master\u2019s that you can take here at CDTM, which is the Center for Digital\
    \ Technology Management here in Munich. It's part of both LMU and EU. So if you\
    \ study at LMU, you can get an additional degree there. That was very interesting\
    \ because it was very hands-on. It included a couple of internships."
  sec: 522
  time: '8:42'
  who: Ivan
- line: "I had an internship at a company that was selling satellite images. So I\
    \ actually worked on spectral analysis of satellite images, which was quite interesting.\
    \ I also worked at a cybersecurity company called Montego, which is also quite\
    \ fascinating. Yeah, it was very hands-on. You learn a lot from it \u2013 how\
    \ to manage projects. You also get a really good network built out of that. A\
    \ lot of startups and startup founders come out of CDTM here in Munich and in\
    \ Berlin."
  sec: 522
  time: '8:42'
  who: Ivan
- line: That's cool. So you studied project management there. What else did you study
    there? Team management and people management as well?
  sec: 590
  time: '9:50'
  who: Alexey
- line: "Yeah, organizational management \u2013 all of those topics."
  sec: 597
  time: '9:57'
  who: Ivan
- line: So are these things that people can actually learn at university or is it
    like learning to swim by reading a book?
  sec: 601
  time: '10:01'
  who: Alexey
- line: '[laughs] As I said, it was super hands-on and that was cool because all of
    the presentations and courses that we had were then led by some CEOs or founders
    of different companies. They would just bring their own perspective on how they
    approach organization management, or how they built up a startup that is now worth
    a few billion. So that was very, very fascinating to do. When I was there, I don''t
    think I had to read any books. It was mostly learning from the experience of others.'
  sec: 609
  time: '10:09'
  who: Ivan
- line: "I remember before I became manager, I was reading books about it \u2013 books\
    \ or articles \u2013 and it didn't make much sense to me. To me, it read like,\
    \ \u201COkay, do things well and things will work out.\u201D Something like that.\
    \ But now, when I already have this experience and I go back to read this stuff,\
    \ it all of a sudden makes much more sense. I guess this is just one of the things.\
    \ So, that's cool that things like that happen and you can just go there. Did\
    \ you need to take breaks between your work to study?"
  sec: 646
  time: '10:46'
  who: Alexey
- line: No, I tried to do everything at once. [laughs] I was working part time and
    also studying computational linguistics and technology management.
  sec: 679
  time: '11:19'
  who: Ivan
- header: Managing a software team
- line: "Yeah, that's really cool. I'm also really curious about your transitions\
    \ and your career paths. You did quite a few different things. You've worked as\
    \ a data scientist and you managed NLP teams. And now you manage a \u201Cusual\u201D\
    \ software engineering team. I'm wondering \u2013 what led to this decision?"
  sec: 691
  time: '11:31'
  who: Alexey
- line: "It was mainly driven by my career goals. I want to eventually work on a higher\
    \ level as a manager \u2013 either the director level or CTO. I think it's very\
    \ important to have a very good grasp on different parts of software engineering.\
    \ I already have a lot of experience with AI and now, I\u2019m relearning things\
    \ or reminding myself how to manage a team that works on a web application. There\
    \ are still many things that are the same."
  sec: 714
  time: '11:54'
  who: Ivan
- line: "I'm still doing more or less the same tasks. I'm managing the productivity\
    \ of the team, talking a lot about CI/CD, which is important not just for sustained\
    \ engineering, but for AI as well. I\u2019m also talking to them about the availability\
    \ of the web apps that we are working on now. It's the same topic of availability\
    \ of AI models \u2013 how fast the users actually get the input from AI models\
    \ or from web apps. That\u2019s basically, more or less, the same."
  sec: 714
  time: '11:54'
  who: Ivan
- line: The overarching topic is observability. I think observability is important
    for any team. Not just AI or software engineering. We used to have a lot of dashboards
    that we looked at when we were working on NLP models and we are doing the same
    thing now, but we just look at different metrics. But observability is still a
    big part of what we are doing.
  sec: 714
  time: '11:54'
  who: Ivan
- header: NLP teams
- line: "That's interesting. Thanks for sharing. Coming back to our topic of NLP teams\
    \ \u2013 how would you define an NLP team? You just said that many of the things\
    \ that you're doing right now are the same, even though the team you manage is\
    \ not specifically an NLP team or a data science team. It's not a data team at\
    \ all. It's just a team of software engineers. How is an NLP team different from\
    \ the team you have now? And what is an NLP team?"
  sec: 816
  time: '13:36'
  who: Alexey
- line: "Yeah, good question. It's more of an industry question. Do we even have separate\
    \ designation for NLP teams? I think maybe a few years ago, this wasn't the case.\
    \ You would just have a data science team and everything data science is done\
    \ there \u2013 either it\u2019s vision, NLP, or just regular data analysis. I\
    \ think now, in recent years, we are branching off more and more, because NLP\
    \ has also become more and more popular in the last few years. Now you see companies\
    \ that have a dedicated NLP team \u2013 one that works solely on NLP tasks."
  sec: 847
  time: '14:07'
  who: Ivan
- line: "I am actually a big proponent of having cross-disciplinary teams. I would\
    \ prefer to have a team that incorporates data scientists, NLP engineers, and\
    \ ideally a data engineer, maybe even an infrastructure engineer. This is something\
    \ I had a lot of success with in my previous teams. We really had all the talent\
    \ gathered in one team, and we had all the knowledge that we needed to succeed\
    \ there. But still, as I said, some companies still do it \u2013 they have a completely\
    \ separate NLP team that works on delivering NLP pipelines."
  sec: 847
  time: '14:07'
  who: Ivan
- line: "It's good when that team is fully on it, meaning they also are responsible\
    \ for deploying into production, monitoring, and everything else \u2013 this is\
    \ great. But that's not always the case. I also know of cases where it'll be teams\
    \ just building a prototype in Jupyter Notebook and then they just give it away\
    \ to the data engineering team or the ML engineers, who then put it in production.\
    \ What differentiates NLP teams from other teams, I think, is mainly the core\
    \ tasks \u2013 working with text data and then delivering a system around it that\
    \ produces some insights for the user, whether it\u2019s classification or a chatbot\
    \ or some text generation, or things like that."
  sec: 847
  time: '14:07'
  who: Ivan
- header: NLP engineers
- line: So an NLP team doesn't need to have an NLP engineer? As long as a team works
    on some NLP-related tasks, such as a chatbot or a customer service bot, then it
    becomes an NLP team, right?
  sec: 979
  time: '16:19'
  who: Alexey
- line: "Yeah. I mean, that's another question. What is an NLP engineer? I've been\
    \ asking myself in the industry \u2013 is that an established role?"
  sec: 992
  time: '16:32'
  who: Ivan
- line: I wanted to ask about that as well.
  sec: 1004
  time: '16:44'
  who: Alexey
- line: "Yeah. I don\u2019t think that it is still fully established. I still see\
    \ job ads that just say, \u201Cdata analyst\u201D or \u201Cdata scientist,\u201D\
    \ but the description is everything related to NLP. So I hope the industry takes\
    \ a step towards defining those roles a bit more. That's something I was trying\
    \ to deal with and I showed in the previous presentation. As you mentioned, I\
    \ shared on LinkedIn a post where I was trying to define those roles, \u201CWhat\
    \ are their responsibilities?\u201D and \u201CWhat are the skills that they need\
    \ to have?\u201D"
  sec: 1005
  time: '16:45'
  who: Ivan
- line: "For NLP teams themselves, I think an NLP engineer is very important. An NLP\
    \ engineer is someone who has the experience and knowledge of working specifically\
    \ with NLP tasks and the data science part that specifically works with text.\
    \ Ideally \u2013 this is not always the case \u2013 but ideally, this is someone\
    \ who also has some linguistic knowledge. Meaning that they at least have some\
    \ applied linguistics, or at least the basics of general linguistics, because\
    \ that's super useful to have. It's not a must these days, but it is very useful."
  sec: 1005
  time: '16:45'
  who: Ivan
- line: "Thinking back to my career, when I worked as a data scientist \u2013 data\
    \ scientists was my title, but I was sort of an NLP engineer \u2013 looking back\
    \ at that time, I think linguistics really helped. I was working on the very hard\
    \ problems of parsing text. Especially in different languages, without knowing\
    \ those building blocks of how to do proper dependency parsing, for example, or\
    \ how to do tokenization in languages that don't have any full stops or spaces\
    \ \u2013 like a tide, it's just a wall of text. So that really helped. I think\
    \ without linguistic knowledge, my team and I wouldn't be able to solve those\
    \ issues so easily."
  sec: 1005
  time: '16:45'
  who: Ivan
- header: Becoming an NLP engineer
- line: "Let's say a data team doesn\u2019t have NLP engineers \u2013 people who specialize\
    \ in NLP tasks \u2013 if this team doesn't have such people, how should they go\
    \ about picking up those skills? Should they be a data scientist who goes and\
    \ learns about linguistics? Or how should they do that?"
  sec: 1133
  time: '18:53'
  who: Alexey
- line: "Yeah, that's a really hard question, actually. Because the question itself\
    \ is \u2013 at the current stage, do we need those linguistics people now? There\
    \ are so many things now that allow you to really get by without understanding\
    \ linguistics. Just think about GPT-3 \u2013 where anyone can do it. You don't\
    \ even need to know how to do data science itself. You just use the GPT-3 prompt\
    \ and then you have something built off of it."
  sec: 1156
  time: '19:16'
  who: Ivan
- line: "It depends on what tasks you're working on. If you are working on more regular\
    \ NLP tasks that everyone else is working on, such as basic sentiment analysis\
    \ or summarization and things like that \u2013 most of the time, you probably\
    \ can get by without any linguistic knowledge. But if you're going more into specific\
    \ tasks, like relation extraction or information extraction, and especially if\
    \ you're starting to work with languages that are not so widely covered by research\
    \ in the space, then it really helps to have linguistic knowledge."
  sec: 1156
  time: '19:16'
  who: Ivan
- line: "How you get that knowledge is a good question. There are quite a few resources\
    \ online, of course. You can learn that by yourself. I wouldn't recommend just\
    \ going and learning general linguistics. That\u2019s probably not going to be\
    \ super helpful. There are courses and resources that are more specific to NLP\
    \ itself. I think there are quite a few things, for example, around spaCy \u2013\
    \ I think they have a lot of tutorials around that training phase. You can just\
    \ really go and learn NLP-related linguistic knowledge."
  sec: 1156
  time: '19:16'
  who: Ivan
- line: Okay. So you should focus more on NLP and computational linguistics rather
    than generic linguistics. Then, you also mentioned that you can pick up a library
    like spaCy or Hugging Face and you learn that. Then, along with learning this
    library, you should also pick up some necessary NLP knowledge, right?
  sec: 1270
  time: '21:10'
  who: Alexey
- line: "Yeah. What I'm saying can also seem like heresy to some people. [laughs]\
    \ I know there are two camps of NLP researchers. One camp says, \u201CWe can do\
    \ everything with AI and we don't need linguistics.\u201D And then there's another\
    \ camp that specifically advocates for us to first learn linguistics properly,\
    \ and then apply AI."
  sec: 1293
  time: '21:33'
  who: Ivan
- line: It really depends on what you're doing. If you're doing research at universities,
    I think knowing linguistics will definitely benefit you, because that's probably
    one of the avenues that will help improve current AI. Someone who knows both linguistics
    and AI very well is going to build a better language model than someone who only
    knows AI.
  sec: 1293
  time: '21:33'
  who: Ivan
- header: Computer vision
- line: "Also, maybe if you compare \u2013  in computer vision, you have old school\
    \ computer vision, which is about extracting features with all these things like\
    \ Bag of Visual Words, Swift. I don't know much about these things, but I know\
    \ that these things exist \u2013 like old school computer vision. Then there is\
    \ new school which is just, \u201CWe don't care about these things. Just throw\
    \ everything in a neural network, it will figure this out and work.\u201D And\
    \ interestingly, it does work."
  sec: 1351
  time: '22:31'
  who: Alexey
- line: "Yeah, it does work. Yeah. That's another can of worms that I don't think\
    \ we want to open. \u201CWhat is more complicated, vision or text analysis.\u201D\
    \ Right? Maybe it works because vision is a bit more definitive in some way than\
    \ text. Because with text there are endless amounts of sentences you can generate\
    \ in English and that's only in English. You have so many languages \u2013 there\
    \ are 5000 languages or something like that. I don't want to open this can of\
    \ worms. I'm not saying that text is easier than vision. With vision, it's very\
    \ hard as well. But I think that, in order for us to succeed with text analysis,\
    \ we still need linguistics. For sure."
  sec: 1384
  time: '23:04'
  who: Ivan
- line: "Okay. So would you say that an NLP engineer is somebody who has a data science\
    \ background \u2013 someone who is a data scientist with some knowledge of NLP\
    \ and computational linguistics? Would this be a correct description?"
  sec: 1435
  time: '23:55'
  who: Alexey
- line: Yeah. I would say so.
  sec: 1450
  time: '24:10'
  who: Ivan
- line: "So, it\u2019s like you said \u2013 you were hired as a data scientist, but\
    \ your task was working on NLP things."
  sec: 1452
  time: '24:12'
  who: Alexey
- line: Yeah, mostly.
  sec: 1460
  time: '24:20'
  who: Ivan
- header: NLP engineer vs ML engineer
- line: So, what's the difference between an NLP engineer and a machine learning engineer?
    Is an NLP engineer an engineer in the same sense as a machine learning engineer?
    Do they care more about the engineering aspect or more the training models aspect?
  sec: 1461
  time: '24:21'
  who: Alexey
- line: "That\u2019s a very good question. I hope that in the future, they will be\
    \ more or less the same, because I think that both parts are important. How I've\
    \ seen it so far is that NLP engineers are \u2013 at least in the case of the\
    \ team I worked at \u2013 we were doing a lot of engineering. It was really a\
    \ lot of pure engineering where we were optimizing everything, and not just optimizing\
    \ training but also optimizing inference. What we were doing less of was productionizing\
    \ of the model itself \u2013 the deployment itself. That was mostly done with\
    \ the help of an ML engineer or a data engineer."
  sec: 1476
  time: '24:36'
  who: Ivan
- line: "I've also had a lot of interviews when hiring NLP engineers, data engineers\
    \ and ML engineers, that there is sort of a division that I see where ML engineers\
    \ themselves think of themselves as DevOps for AI \u2013 they are responsible\
    \ for deploying the models, figuring out how to do blue/green deployment of an\
    \ AI model. This is a challenge that I think NLP engineers are not always prepared\
    \ to solve."
  sec: 1476
  time: '24:36'
  who: Ivan
- header: Conversational designers
- line: "Yeah, interesting. We've talked about linguistics, and that somebody who's\
    \ an engineer needs to know linguistics. Do we need people who specialize only\
    \ in linguistics? People who don\u2019t only have this NLP knowledge and know\
    \ how to call methods from spaCy, but those who actually had education as linguists?\
    \ Do we need people like that in the team?"
  sec: 1489
  time: '24:49'
  who: Alexey
- line: "Yeah, for sure. There are some specific tasks that would really benefit from\
    \ that. I think that in the last two years, there was a new role forming in the\
    \ world of data science, called \u201Cconversational designer\u201D. It's basically\
    \ a person who is responsible for making the user experience, and the flow of\
    \ how the Chatbot interacts with the user, feel more realistic. Conversational\
    \ designers, from what I see, are mostly people who come from a more pure, either\
    \ linguistic background, or some societal studies."
  sec: 1579
  time: '26:19'
  who: Ivan
- line: "That knowledge is really important \u2013 how do you properly form an utterance\
    \ that the Chatbot can use? Or how does a chatbot react to some specific questions?\
    \ Things like that. And that's what conversational designers these days work with.\
    \ From what I've seen \u2013 I have a small subset of people I know who are actually\
    \ conversational designers \u2013 but from those I know, they mostly work on defining\
    \ that flow without having to code that much. They're less of a coder and less\
    \ of an NLP engineer, but instead specifically look into how you can build out\
    \ a really nice experience around talking to a chatbot."
  sec: 1579
  time: '26:19'
  who: Ivan
- line: "So I guess it's similar to what we have in general software engineering \u2013\
    \ product designers and UX designers? Except here, they don't focus on the general\
    \ UX (user experience), but instead, they focus on the conversational part \u2013\
    \ the interactions with the chatbot."
  sec: 1490
  time: '24:50'
  who: Alexey
- line: "Yeah, yeah \u2013 that's a really good comparison. Yeah."
  sec: 1686
  time: '28:06'
  who: Ivan
- header: Linguistics outside of chatbots
- line: "Okay, interesting. Not all NLP teams work on chatbots \u2013 there are teams\
    \ that work on other things, like you mentioned, like information extraction,\
    \ and I don't remember what else. So there are areas where we may need to do something\
    \ with text understanding and things like that. Do we need linguists in the teams\
    \ that work in these areas as well?"
  sec: 1692
  time: '28:12'
  who: Alexey
- line: "Good question. It really depends on what area of research you're working\
    \ in, or what specific tasks you work on. I think it wouldn't hurt if you have\
    \ someone who knows linguistics well. As I mentioned before, if you have problems\
    \ where you really need to think about, \u201CHow do you parse a sentence?\u201D\
    \ or \u201CHow do you get something out of the text?\u201D That's where a linguist\
    \ would really help. I think, ideally, you would have this NLP engineer role that\
    \ has both skills incorporated. Someone who knows linguistics enough to be able\
    \ to apply it, but on the other side also knows the engineering part behind it\
    \ to effectively apply it to the problem that we're working on."
  sec: 1718
  time: '28:38'
  who: Ivan
- header: When does a team need an NLP engineer or a linguist?
- line: As you mentioned, when a team starts working on an NLP task, they don't necessarily
    need to immediately get this NLP engineer with linguistics knowledge because you
    can get quite far just by using a library. Let's say a team starts working on
    some NLP tasks and they get by just going and getting Hugging Face, spaCy and
    start using that. At which point do they need to hire a linguist or an NLP engineer?
    How do you decide that? How do you see that they need somebody?
  sec: 1776
  time: '29:36'
  who: Alexey
- line: That's a good question. I guess it also depends on what approach they choose.
    If the problem that you have can be solved by pure AI, then I think that there
    is probably no need for specific linguistic knowledge in the team. But not all
    problems can be solved with AI. That's why in the industry, a lot of problems
    are still solved with robust systems or some statistical approaches. Especially
    if you need to build features or do feature engineering, I think there it would
    be very helpful to have a linguist, or at least an NLP engineer who knows what
    to look for, how to build features, and so on.
  sec: 1811
  time: '30:11'
  who: Ivan
- line: "So it really depends on the problem. We are moving into a direction where\
    \ more and more problems can be solved with just throwing the problem into a neural\
    \ network. It's a question of where we are going to go in the next few years.\
    \ I think GPT-3 showed one thing \u2013 that you can just throw raw power and\
    \ a bit of data into a neural network and will have something amazing working.\
    \ But the question is, \u201CWhere does it end? How far can we go? How many more\
    \ learning parameters can we fit into a language model?\u201D"
  sec: 1811
  time: '30:11'
  who: Ivan
- header: The future of NLP
- line: "It's funny that you mentioned that. We have a question. \u201CWhat is the\
    \ future of NLP?\u201D Now we have libraries like Hugging Face or spaCy which\
    \ simplify things a lot. The API of these libraries is quite good, you can just\
    \ take and use it. Do you think having access to libraries like this will remove\
    \ the need to write NLP pipelines from scratch? Or not?"
  sec: 1907
  time: '31:47'
  who: Alexey
- line: "Well, yes. As I said, for many tasks you can get by with those things. Those\
    \ tools that you mentioned are democratizing the industry. They are open sourcing\
    \ everything and this is great. This is enabling smaller teams or smaller startups\
    \ to work more easily on AI. Whether that will fully remove the need of writing\
    \ NLP pipelines? I don't think it will. It's actually very funny. I had a very\
    \ similar conversation five years ago and back then everyone was talking about\
    \ Auto ML. \u201CAuto ML is going to replace data scientists. Because of Auto\
    \ ML we're not going to need to build NLP models.\u201D That is still not the\
    \ case, right? Five years have passed and we're still building NLP pipelines."
  sec: 1941
  time: '32:21'
  who: Ivan
- line: I think this will probably stay the same. We will still have to build NLP
    pipelines, because the complexity will just grow and grow. As complexity grows,
    you probably won't be able to catch up with having high level tools that always
    incorporate the latest thing. You will still need to use NLP pipeline and build
    NLP pipelines in order to be able to have an advantage or an edge. NLP papers
    and AI papers come out every week. New things will come out very fast and the
    faster you react to them, the better.
  sec: 1941
  time: '32:21'
  who: Ivan
- line: "Having an NLP engineering team that can easily take some new paper and incorporate\
    \ ideas \u2013 not the whole thing, but at least some ideas \u2013 into their\
    \ current solution will be super helpful. That's probably not always possible\
    \ with these open source tools."
  sec: 1941
  time: '32:21'
  who: Ivan
- header: NLP pipelines
- line: "In spaCy, there is a method that just \u201Cmakes things good\u201D and then\
    \ it just works. But internally somewhere, it still has an NLP pipeline, right?\
    \ Potentially you can go deeper and try to uncover that and also adjust it to\
    \ whatever you need. By the way, speaking of NLP pipelines, I don't think we mentioned\
    \ what an NLP pipeline is. Can you tell us what it actually is and why Hugging\
    \ Face and spaCy remove the need of building them?"
  sec: 2061
  time: '34:21'
  who: Alexey
- line: "Yeah, good question. It depends on how you define it. My definition would\
    \ be \u2013 if you are an NLP team building an NLP pipeline \u2013 that already\
    \ starts with data. That starts with data annotation. That starts with generating\
    \ good quality data and then refining it. The next step is, if you use AI, you\
    \ basically build up. Let's say you take something like T5, or some other language\
    \ model, and then you have to make it work for your specific task. You basically\
    \ do some task engineering around it, and you make it work with your specific\
    \ data input."
  sec: 2097
  time: '34:57'
  who: Ivan
- line: "Then you also have to define the outcome of that. Depending on how much you\
    \ want to play around with the language model itself, you can also work on neural\
    \ network improvements for your specific task in between. When you have that,\
    \ there's also testing. Testing NLP models is very important. After that comes\
    \ productionizing. So how do you deliver some kind of binary model that can be\
    \ used for inference? How do you deploy it? Then in the end, how do you do observability\
    \ around it? For me, that is the NLP pipeline. It starts with data and ends with\
    \ \u201CHow do you observe how your model performs in production?"
  sec: 2097
  time: '34:57'
  who: Ivan
- line: "What you described \u2013 data annotation, data quality, then task engineering\
    \ and testing the model, then productionizing the model \u2013 spaCy and Hugging\
    \ Face don't seem to remove the need for that. You still have to do all these\
    \ tasks. It's not like you just press a button and all of a sudden have high-quality\
    \ annotated data, right?"
  sec: 2189
  time: '36:29'
  who: Alexey
- line: Yeah, what they remove is the task engineering for the most part. You don't
    have to tinker around with the behind-the-scenes implementation of a specific
    language model. You just use it from the tools themselves.
  sec: 2210
  time: '36:50'
  who: Ivan
- line: "What I had in mind when I heard \u201CNLP pipeline\u201D (I remember using\
    \ this) was the Stanford core NLP library, which is in Java. It's a pretty old\
    \ library. Then there\u2019s a class called \u201Cpipeline\u201D or \u201CNLP\
    \ pipeline\u201D, I don\u2019t remember. In this pipeline, it's first about splitting\
    \ the sentences. So you have a paragraph and in the paragraph, you have different\
    \ sentences. You want to split it to have separate sentences. Then you tokenize.\
    \ You take the sentence and break it into multiple tokens. Then perhaps you want\
    \ to remove punctuation or not remove punctuation. You also want to do some lemmatization,\
    \ stemming \u2013 all these things. This is what I thought of when I heard \u201C\
    NLP pipeline\u201D."
  sec: 2222
  time: '37:02'
  who: Alexey
- line: "That is what\u2019s referred to as \u201Cpre-processing.\u201D I guess I\
    \ just forgot to mention that. So you have the data and then how do you make the\
    \ language model, or whatever role based system you're using, understand the data?\
    \ That's where the step of pre-processing comes in \u2013 this tokenization, lemmatization.\
    \ You don't always need all of the steps."
  sec: 2274
  time: '37:54'
  who: Ivan
- line: "For current language models, you barely need any of those steps anymore.\
    \ It really depends on the task. You're right \u2013 these problems are mostly\
    \ solved. They are mostly solved in tools like spaCy and Hugging Face, where you\
    \ don't really have to think anymore about \u201CHow do you tokenize a sentence?\u201D\
    \ It's done almost totally automatically there."
  sec: 2274
  time: '37:54'
  who: Ivan
- header: GPT-3
- line: What about tools like GPT-3? I guess they also remove some of the steps from
    this pipeline? They make it easier, right?
  sec: 2325
  time: '38:45'
  who: Alexey
- line: "Yeah, GPT-3 is on a whole different level. You don't need to do anything,\
    \ really. The idea of GPT-3 is that it\u2019s a smart lookup table. It has seen,\
    \ I think, like 10% of the whole internet. That's what the data set was used to\
    \ train it. It has seen so much data that you could say that it knows NLP is.\
    \ It knows how to solve some of its tasks. It knows what tokenization is. It just\
    \ has somehow learned it. It's like an internal black box. We don't know how it\
    \ actually works."
  sec: 2335
  time: '38:55'
  who: Ivan
- line: "All you need to do for GPT-3 is write a prompt. For example, if you want\
    \ to do sentiment analysis, you just write \u201CThe day is nice.\u201D Then you\
    \ write the tag: positive. Then you write another sentence and say \u201CI'm sad.\u201D\
    \ Then you write a tag, but you don't write whether it's positive or negative\
    \ \u2013 the model will just autocomplete it for you. It just knows somehow that\
    \ you are asking it to do sentiment analysis, which is insane."
  sec: 2335
  time: '38:55'
  who: Ivan
- line: "There are even super ridiculous things in GPT-3. There was a paper recently\
    \ where they were exploring \u201CHow well does GPT-3 do translations?\u201D Basically,\
    \ in the original GPT-3 paper, they just had a prompt, \u201CPlease translate\
    \ this sentence from English to French and then give the sentence.\u201D Then\
    \ the researchers changed the prompt to \u201CPlease translate this English sentence\
    \ as if you are a very good French translator.\u201D Then it gives you a much\
    \ better quality of translation, which just blows your mind that this is possible."
  sec: 2335
  time: '38:55'
  who: Ivan
- line: I think you showed in your presentation that it's possible to rewrite a usual
    sentence as if it was written by a lawyer. Right?
  sec: 2446
  time: '40:46'
  who: Alexey
- line: Right. That's correct.
  sec: 2457
  time: '40:57'
  who: Ivan
- line: That's also insane. So it's translating from normal English to legalese.
  sec: 2458
  time: '40:58'
  who: Alexey
- line: "Yeah. I mean, it's a miracle of these GPT-3 massive language models \u2013\
    \ that they somehow have internalized all of those things without us having to\
    \ teach them what tokenization is or even what translation is. They just somehow\
    \ learned it. The question now is \u201CHow far can we get with this? Can we just\
    \ get away with throwing more compute power, bigger GPUs, and more data and expect\
    \ it to work better and better?\u201D"
  sec: 2468
  time: '41:08'
  who: Ivan
- line: "And \u201CWhen does it become creepy?\u201D I feel like it already kind of\
    \ gives me goosebumps when I watch some of these demos. As you said, it's basically\
    \ a big lookup table and it probably already knows everything \u2013 what is there\
    \ on the internet about you, about me, about everyone who is watching this, right?\
    \ If you ever left a footprint somewhere on the internet, it's on it and it knows."
  sec: 2500
  time: '41:40'
  who: Alexey
- line: Yeah, probably.
  sec: 2523
  time: '42:03'
  who: Ivan
- line: "I remember that I\u2019ve seen a demo that shows it's possible to get emails\
    \ of people."
  sec: 2525
  time: '42:05'
  who: Alexey
- line: Yeah. Right. This was even possible with GPT-2. You could just start writing
    an address and it would autocomplete it with the actual name of someone who lives
    at that address, which is crazy.
  sec: 2531
  time: '42:11'
  who: Ivan
- line: "That's creepy. But I guess if you use GPT-3, then you still have this component\
    \ of task engineering. It's just, in its own way\u2026"
  sec: 2544
  time: '42:24'
  who: Alexey
- line: "It's very simplified now. You don't need to do that much. You just need to\
    \ figure out what\u2019s the best way to tell the model to do your task and how\
    \ much data you actually have to give it. You could even get by with just a few\
    \ examples for some tasks. For more complicated tasks, I can imagine you can still\
    \ need a very well-annotated data set."
  sec: 2553
  time: '42:33'
  who: Ivan
- header: Problems of GPT-3
- line: But it's not cheap, right? It's expensive. You cannot just use it and rely
    on GPT-3 completely.
  sec: 2577
  time: '42:57'
  who: Alexey
- line: Yeah. I mean, I don't know. They are trying to open source it now or something.
    I don't know. But I think you still have to pay for tokens in order to be able
    to use it.
  sec: 2585
  time: '43:05'
  who: Ivan
- line: So, for each request you need to pay.
  sec: 2594
  time: '43:14'
  who: Alexey
- line: "Yeah \u2013 for each request. So it is definitely expensive. It's not just\
    \ a problem with the fact that you have to pay for it, it's also a problem that\
    \ you have zero control of what it's doing and why it's doing it. Like, let\u2019\
    s say if someone finds a way to bias to GPT-3 very easily, then they can easily\
    \ reproduce that on your solution that you've built based on GPT-3. You have zero\
    \ control of that. That's why everyone doesn\u2019t jump on this."
  sec: 2597
  time: '43:17'
  who: Ivan
- line: "Not everyone's using GPT-3. I think it's super good when you want to build\
    \ an MVP of some sort. You can very quickly use GPT-3 to build out some kind of\
    \ demo and then sort of validate it. I've seen a lot of companies do that. Basically,\
    \ after they validated their demo with something easy like GPT-whatever, GPT-2\
    \ even. They just say, \u201COkay, now let\u2019s build something that we are\
    \ in control of. We\u2019ll build our NLP pipeline, we\u2019ll know how it works\
    \ and we have control over it to some extent.\u201D"
  sec: 2597
  time: '43:17'
  who: Ivan
- line: "I guess you can use it for annotating your data as well \u2013 for collecting\
    \ your initial version of the dataset."
  sec: 2670
  time: '44:30'
  who: Alexey
- line: Yeah. I guess. I actually haven't seen anyone using GPT-3 for data annotation.
    I don't know how well that actually works.
  sec: 2677
  time: '44:37'
  who: Ivan
- line: "I think we have a pilot project on that. I think it worked well. I wasn't\
    \ involved in that project, I just heard that we tried it and it worked well.\
    \ We basically trained a simple model on the output of GPT-3. Something like logistic\
    \ regression or something like that \u2013 something super simple. It was a classification\
    \ problem."
  sec: 2685
  time: '44:45'
  who: Alexey
- line: Nice. Yeah. I didn't even think about that.
  sec: 2705
  time: '45:05'
  who: Ivan
- line: "Because writing all these rules for extracting data \u2013 for information\
    \ extraction \u2013 can be difficult. The company where I work, OLX, is a place\
    \ where people can exchange goods. It's basically an online marketplace. You have\
    \ listings and the listings have descriptions. You want to extract some information\
    \ from there. You mentioned that information extraction is a complex task. So\
    \ we tried to use GPT-3, I think, for extracting this and then using these things\
    \ as labels and then feeding it into a SQL model. But I only saw demos \u2013\
    \ I wasn't taking part in that application."
  sec: 2710
  time: '45:10'
  who: Alexey
- line: Interesting.
  sec: 2749
  time: '45:49'
  who: Ivan
- header: Does GPT-3 make everything obsolete?
- line: "I think we talked about this already and we kind of mentioned that. The question\
    \ we have is, \u201CNow we have this GPT-3. Does it mean that we no longer need\
    \ things like Hugging Face, spaCy, and so on? Would you still use Hugging Face\
    \ if you had access to GPT-3 now?\u201D"
  sec: 2750
  time: '45:50'
  who: Alexey
- line: "I would say, yes, because GPT-3 still isn't able to solve everything. It\
    \ is able to solve most of the tasks to a good extent. But the question is, \u201C\
    Can it actually solve everything you need for it to be used in production \u2013\
    \ for it to be actually given to the clients?\u201D I don\u2019t think that's\
    \ the case right now. Even if you do that, there's a lot of danger that it will\
    \ just go rogue on you and you have no idea how to control it. It may become biased\
    \ to some specific user group or something like that."
  sec: 2770
  time: '46:10'
  who: Ivan
- line: "Yeah, I\u2019m wondering what would happen then. Let\u2019s say Open AI finds\
    \ out that it's broken because somebody messed up with it and they decided, \u201C\
    Okay, now it's bad. Let's shut it down.\u201D Then to everyone who relies on this,\
    \ \u201CYeah, sorry.\u201D"
  sec: 2816
  time: '46:56'
  who: Alexey
- line: Yeah. The open source engineering group called Open AI is basically working
    on rebuilding GPT-3 from scratch. So now we have things like GPT-J, and GPT-Neo.
    It's like smaller versions of GPT-3, but they are fully open source. Anyone can
    use them. You can also look up sort of how they built it. So that's a step in
    the right direction. I think this will always be the case. Even if Open AI comes
    out with GPT-4 and it's again proprietary, there will again be someone who will
    be able eventually to crack the code and open source it for everyone.
  sec: 2836
  time: '47:16'
  who: Ivan
- header: What NLP actually is?
- line: "Yeah, interesting. Another question we have is \u201CWhat do you think NLP\
    \ is more about? Is it more about writing better pipelines and improving these\
    \ pipelines and then implementing some research papers? Or is it more about theoretical\
    \ linguistic knowledge and its application?\u201D I think at the beginning you\
    \ mentioned that it can get quite far without much linguistics knowledge. So what\
    \ do you think NLP actually is? Is it about applying these libraries? Or is it\
    \ about using linguistics?"
  sec: 2884
  time: '48:04'
  who: Alexey
- line: "Yeah. That's a good question. I think it depends on whether you're talking\
    \ about industry or academia. If we're talking about industry \u2013 for smaller\
    \ companies or small startups, there's really no financial incentive to innovate\
    \ in terms of linguistic application of NLP. They're more interested in building\
    \ these NLP pipelines and building a product. That's where tools like high efficiency\
    \ come in, which help them a lot."
  sec: 2919
  time: '48:39'
  who: Ivan
- line: "But if we\u2019re talking about bigger companies, such as Google \u2013 I\
    \ know that at Google Brain, for example, there are people who are working on\
    \ linguistics applications to NLP. A lot of academia also works on that, because\
    \ from an academic perspective, we will not advance NLP if we only work on building\
    \ bigger AI models. We really need to see how else we can incorporate linguistic\
    \ knowledge into AI research. That's where academia is actually doing a lot. A\
    \ lot of universities are working on that specific part."
  sec: 2919
  time: '48:39'
  who: Ivan
- line: "So basically you are saying that the future of NLP is not just throwing more\
    \ hardware at GPT-3, or perhaps a GPT-4 (if it's even a thing), but more like,\
    \ \u201COkay, now we learned how to throw hardware at all of the internet and\
    \ then make the tool learn it. Now, how can we simplify it? How can we achieve\
    \ a similar thing without having to burn a lot of GPUs?\u201D"
  sec: 2992
  time: '49:52'
  who: Alexey
- line: "Yeah. You could say there's a race going on now. Organizations like Open\
    \ AI are trying to push the limits of building bigger and bigger language models,\
    \ whereas some universities are trying to rely more on linguistics. I don't know\
    \ what will come out of that, who will win, or if there will even be a winner\
    \ \u2013 maybe it will just always be like that. There's an NLP Research Institute\
    \ and I know they are exploring a lot about \u201CHow do you merge linguistics\
    \ with AI to build better AI models and better language models?\u201D I think\
    \ this is the right direction to go into because this will definitely help advance\
    \ the field."
  sec: 3023
  time: '50:23'
  who: Ivan
- line: "This \u201CAllen AI\u201D, they do quite a lot of work in NLP, right?"
  sec: 3078
  time: '51:18'
  who: Alexey
- line: "Right. The institute is called Allen AI, I think. They also have an open\
    \ source toolkit called \u201CAllen NLP\u201D."
  sec: 3084
  time: '51:24'
  who: Ivan
- line: "I remember seeing competitions on Kaggle from them. It was actually the first\
    \ Kaggle competition I ever took part in. It was about \u2013 in school, you have\
    \ multiple choice questions, which consist of a question and four answers. The\
    \ task that they had was \u201CBuild a model that would select the right answer.\u201D\
    \ You have a question and you have four answers. The task was to rank them, basically,\
    \ to give the correct answer. It was not a usual problem, let's say. It was a\
    \ lot about indexing Wikipedia and then using this knowledge base to rank all\
    \ these answers. It was quite a fun one."
  sec: 3093
  time: '51:33'
  who: Alexey
- line: Yeah. AI NLP also incorporates many other things like building knowledge graphs
    and things like that. That's also part of NLP and AI.
  sec: 3145
  time: '52:25'
  who: Ivan
- header: Does NLP solve problems better than humans?
- line: "Yeah. That competition was six years ago. Do you think with all these GPT-3\
    \ things \u2013 is it a solved problem now? Can we just answer multiple choice\
    \ questions? Or is it still not a solved problem?"
  sec: 3160
  time: '52:40'
  who: Alexey
- line: "Yeah, I don't think so. I don't think there is any problem we have fully\
    \ solved. There are papers that state something like \u201CAI models are as good\
    \ as humans\u201D or \u201Cbetter than humans\u201D. But this is all evaluated\
    \ on a very small subset of data. It's really hard to say whether it\u2019s actually\
    \ true or not. So I wouldn't say we solved all of those problems. Even if we did,\
    \ we probably would have solved it only for English, but there are so many other\
    \ languages we need to solve it for."
  sec: 3177
  time: '52:57'
  who: Ivan
- header: State of language translation
- line: Yeah. What do you think about language translation? There is a question that
    says it seems to be one of the toughest NLP tasks. Do you think we will be able
    to achieve human-level results in language translation?
  sec: 3212
  time: '53:32'
  who: Alexey
- line: Yeah, good question. I knew someone who worked at DARPA in the US and basically
    language translation mostly came to us from solving these problems for military
    purposes. This is where it mostly started, I think. Now you actually have more
    product-based solutions. You have Google Translate, of course. You also have deepL,
    which is trying to solve this problem. I think the path to solve it is to try
    to make it an actual product that can make money. That will get you more funds
    to put back into research and then improve it even more and more. I think this
    is the way we are going right now.
  sec: 3225
  time: '53:45'
  who: Ivan
- line: "Google is investing a lot into translation. There are other companies investing\
    \ a lot in that. But we will be able to solve it fully \u2013 I don't know, it's\
    \ hard to say. There are more and more products coming out of that. But, right\
    \ now, I think if you look at that translation task, we are kind of good for maybe\
    \ eight to ten languages and that's it. It's mostly European languages and maybe\
    \ Chinese. It's kind of okay-ish. It can be used, but if you go beyond that \u2013\
    \ we're far, far away from being able to solve that issue. That mainly comes from\
    \ the fact that we don't have enough data for it. It's not enough textual data\
    \ to train AI on."
  sec: 3225
  time: '53:45'
  who: Ivan
- line: "But also, I'm quite impressed now with the results I get from Google Translate\
    \ as a user. I live in Germany where people speak German. My German is not that\
    \ good. So what I usually do is write something in Google Translate \u2013 I usually\
    \ use English because translating from English to German works much better than\
    \ translating from Russian to German. Even though now, last year, it works really\
    \ well from Russian to German as well, even though I think English and German\
    \ are a lot closer to each other than Russian and German. It still works really\
    \ well."
  sec: 3331
  time: '55:31'
  who: Alexey
- line: "Eight years ago, when I lived in Poland, I needed to translate from Polish\
    \ to Russian. These are very similar languages \u2013 they are very close. But\
    \ I think what happened internally is they translated first from Polish to English,\
    \ and from English to Russian, so a lot of things would be lost in translation.\
    \ But now, if I need to translate something from Polish to Russian, it's very\
    \ good. Translation from Ukrainian to Russian works as if a person translated\
    \ it. It works really well. Sometimes I read websites in Ukrainian \u2013 there\
    \ is a lot of content in Russian and some articles in Ukrainian. I would understand\
    \ Ukrainian, but sometimes it\u2019s just simpler to translate. It works really\
    \ well \u2013 as if it was written in Russian. So that's really impressive."
  sec: 3331
  time: '55:31'
  who: Alexey
- line: "Yeah, I think Google Translate actually switched to using language models\
    \ that they've trained. I don't know how many years ago, but at least four or\
    \ five. That's where the quality was really visibly much better. Google can do\
    \ it because they have so much data \u2013 they index the whole internet. It's\
    \ easier for them to just train a language model for it. I think with translations\
    \ now, the top solutions are all pure AI. I don't think there's much linguistics\
    \ in that."
  sec: 3417
  time: '56:57'
  who: Ivan
- header: NLP Pandect
- line: But I guess if I try to translate from Russian to some Indian language, then
    maybe it's not a very common translation pair. Okay. I just noticed that we don't
    have a lot of time left and there was something I really wanted to ask you.
  sec: 3451
  time: '57:31'
  who: Alexey
- line: "I wanted to ask you about your project on your GitHub called \u201CNLP Pandect\u201D\
    . Did I pronounce it correctly?"
  sec: 3451
  time: '57:31'
  who: Alexey
- line: Yeah. I guess. I don't know how to pronounce it because it's old Greek. I
    think it's Pandect.
  sec: 3480
  time: '58:00'
  who: Ivan
- line: Can you tell us more about this project? What is it?
  sec: 3486
  time: '58:06'
  who: Alexey
- line: "Yeah, sure. This is something I started last year during lockdown because\
    \ I was bored [laughs]. The idea was \u2013 we all know there are these awesome\
    \ lists. This is a very typical thing on GitHub. People create a list of things\
    \ and nice links. So I wanted to do something like that for NLP. There were already\
    \ some awesome lists for NLP, but I just thought they were a bit bland \u2013\
    \ there's just a list of URLs. So I tried to make it more user-friendly."
  sec: 3488
  time: '58:08'
  who: Ivan
- line: "I came up with this idea to have a different name for it. Pandect means encyclopedia\
    \ in ancient Greek. I also created some visuals around it. If you go to the end\
    \ of Pandect on GitHub, all the sections are done with nice fonts and there are\
    \ all the Greek symbols of gods and things like that. So it sort of gives it a\
    \ theme. Then I also tried to really fine-grain classification of things to put\
    \ there. If you go to NLP Pandect, you can just easily search for a specific NLP\
    \ task and get a list of tutorials, a separate list of books \u2013 you can read\
    \ that \u2013 or a separate list of GitHub repositories. I also did an analysis\
    \ of all NLP tools and all ML tools. All of that you can find there."
  sec: 3488
  time: '58:08'
  who: Ivan
- line: "It doesn't end with NLP Pandect as I also work with many other things. I\
    \ have two more projects related to this. There is also Microservices Pandect.\
    \ There's a lot of information there about how to build and maintain microservices,\
    \ and how to do DevOps around them. One that I started more recently is for engineering\
    \ managers. There's an Engineering Manager Pandect, which incorporates a lot of\
    \ resources for leadership \u2013 \u201CHow do you lead technical teams? How do\
    \ you solve people issues and things like that?\u201D"
  sec: 3488
  time: '58:08'
  who: Ivan
- line: Okay, thanks. I just realized there was so much I wanted to ask you. We covered
    only like half of that. But we talked about other things. So that was fun. Thanks
    a lot for joining us today. Thanks a lot for sharing everything with us.
  sec: 3620
  time: '1:00:20'
  who: Alexey
- line: Yeah. Thank you for inviting me
  sec: 3635
  time: '1:00:35'
  who: Ivan
- header: Finding Ivan online
- line: "By the way, if somebody wants to reach out to you \u2013 how can they do\
    \ that?"
  sec: 3637
  time: '1:00:37'
  who: Alexey
- line: "Yeah. The best way is to find me on LinkedIn. That's where I\u2019m most\
    \ active. I'm also on Twitter, but I don't post there that much, so LinkedIn is\
    \ probably the best way."
  sec: 3641
  time: '1:00:41'
  who: Ivan
- line: Okay, yeah. Thanks a lot. Thanks for joining us today. And thanks, everyone,
    for asking questions. Have a great rest of your day.
  sec: 3654
  time: '1:00:54'
  who: Alexey
- line: Great. Thanks a lot.
  sec: 3663
  time: '1:01:03'
  who: Ivan
---

Links:

- [NLP Pandect](https://github.com/ivan-bilan/The-NLP-Pandect){:target="_blank"}
- [Engineering Manager Pandect](https://github.com/ivan-bilan/The-Engineering-Manager-Pandect){:target="_blank"}
- [Microservices Pandect](https://github.com/ivan-bilan/The-Microservices-Pandect){:target="_blank"}
- [Ivan's presentation about NLP](https://www.youtube.com/watch?v=VRur3xey31s){:target="_blank"}
