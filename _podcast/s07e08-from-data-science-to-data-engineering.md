---
episode: 8
guests:
- ellenkonig
ids:
  anchor: From-Data-Science-to-Data-Engineering---Ellen-Knig-e1fgfbm
  youtube: 3TTu-hYzxeg
image: images/podcast/s07e08-from-data-science-to-data-engineering.jpg
links:
  anchor: https://anchor.fm/datatalksclub/episodes/From-Data-Science-to-Data-Engineering---Ellen-Knig-e1fgfbm
  apple: https://podcasts.apple.com/us/podcast/from-data-science-to-data-engineering-ellen-k%C3%B6nig/id1541710331?i=1000553736781
  spotify: https://open.spotify.com/episode/4R9F5B4f8vf5r5yQEmwYiu
  youtube: https://www.youtube.com/watch?v=3TTu-hYzxeg
season: 7
short: From Data Science to Data Engineering
title: From Data Science to Data Engineering

transcript:
- line: This week, we'll talk about transitioning from data science to data engineering.
    We have a special guest today, Ellen. Ellen is the head of data engineering at
    WhereIsMyTransport, which is a company that provides mobility and location data
    for emerging markets. She has been working in software engineering, data science,
    and data engineering roles for over a decade. A common theme across her career
    is her passion for building high-quality technology of which data is a core component.
    She also enjoys teaching, speaking, and writing about data topics. Welcome, Ellen.
  sec: 74
  time: '1:14'
  who: Alexey
- line: Thank you. I'm happy to be here.
  sec: 108
  time: '1:48'
  who: Ellen
- header: "Ellen\u2019s background"
- line: Happy to have you on. Before we go into our main topic of transitioning to
    data engineering, let's start with your background. Can you tell us about your
    career journey so far?
  sec: 111
  time: '1:51'
  who: Alexey
- line: "Of course I can. I studied computer science at Uni. It was my first degree\
    \ and I really enjoyed it. I specialized in software engineering and what's called\
    \ in German \u201CWirtschaftsinformatik\u201D which translates to business applications\
    \ of computer science. Then I worked as a software engineer for a bit in different\
    \ countries, but then I got really bored with backend engineering because I felt\
    \ I was doing and building the same kind of \u201Cread data from the database,\
    \ put it into an API \u2013 get data from an API and put it back into the database\u201D\
    \ thing over and over again. At the same time, I started a psychology part-time\
    \ degree. I didn't really enjoy the psychology part that much, but I was really\
    \ surprised that I really enjoyed a statistics course, which is obligatory for\
    \ psychologists."
  sec: 121
  time: '2:01'
  who: Ellen
- line: "At that time, that was when data science became a bit of a hype topic and\
    \ I thought, \u201CHey, maybe that's a cool way to combine my interest in technology\
    \ and statistics,\u201D so I set out on a path to become a data scientist. I did\
    \ a Udacity nanodegree, which is kind of an online bootcamp to level up in machine\
    \ learning and a bunch of other online courses. Then I got a job in a data team\
    \ and insights team at SoundCloud, where I had a pretty wide range of things that\
    \ I did \u2013 everything from data pipelines and scheduling, but SoundCloud at\
    \ the time had its own data scheduler. But also, I did a lot of predictive analytics\
    \ stuff, and plain old dashboarding and everything that's in between that. That's\
    \ why I officially own the title of data scientist or senior data scientist. Then\
    \ SoundCloud had a massive round of layoffs, which was quite painful to me because\
    \ I really enjoyed working there in 2017."
  sec: 121
  time: '2:01'
  who: Ellen
- line: "Then I worked as a data scientist in a few other companies, again, doing\
    \ predictive analytics and dashboarding. I was also doing production-level modeling,\
    \ so everything in between. But I realized that I didn't really enjoy data science\
    \ that much, because it felt very blackboxy to me because I was like feeding some\
    \ model but I didn't really understand what was going on, which is partially due\
    \ to the fact that my mathematics background isn't that strong. So I didn't ever\
    \ really get the theory behind it. But also, I realized that I kind of miss the\
    \ engineering part of it more. That was also the time where data engineering became\
    \ more routine, because companies realized that they need not just data scientists,\
    \ but also people that actually come before them and make data available for data\
    \ science. At the time it was a common frustration for data scientists to not\
    \ have data. Great ambitions \u2013 but no data. Then I got an offer at Native\
    \ Instruments to be one of the first data engineers and I did that for a while.\
    \ I still had the ambition back then to transition back into data science, but\
    \ I left Native Instruments for unrelated reasons before that happened."
  sec: 121
  time: '2:01'
  who: Ellen
- line: Then I got another job at another company as a BI developer. My title was
    data scientist, but really, what I did was develop custom data visualizations.
    I eventually realized that this was kind of a dead end for me, so I remembered
    my software engineering background, which I truly enjoyed except for the part
    that it was so repetitive. At the time, I was speaking to somebody at ThoughtWorks.
    She was the first data scientist at ThoughtWorks Germany at the time and she told
    me that ThoughtWorks was planning to expand its data engineering offering and
    asked whether I would be interested in becoming ThoughtWorks Germany's first data
    engineer and to help expand that offering. I thought this was really exciting,
    especially since ThoughtWorks is a great place for really learning good software
    engineering practices.
  sec: 121
  time: '2:01'
  who: Ellen
- line: "As a data engineer it is always frustrating and as a data scientist that\
    \ always frustrated me that the quality of the code and the collaboration wasn't\
    \ as good as I remembered from my backend engineering days. So I jumped on that\
    \ opportunity and that's when I finally decided to stay in data engineering, which\
    \ I had done on and off before. After ThoughtWorks, I went to where I am now \u2013\
    \ at WhereIsMyTransport \u2013 and built up the data engineering there. This is\
    \ where I am now heading a team."
  sec: 121
  time: '2:01'
  who: Ellen
- header: Why Ellen switched from data science to data engineering
- line: "That's quite a story, thanks for sharing. What I also wanted to ask you and\
    \ the next question that I prepared is \u2013 you were in data science and then\
    \ you switched to data engineering, and I wanted to ask \u201CWhy?\u201D I think\
    \ you partly answered that. You said that data science was a bit too blackboxy\
    \ for you \u2013 you wanted to understand the theory behind this. I mean, at work,\
    \ you don't really need to know the theory, right? You have an algorithm, give\
    \ it some data that you get out of the model and then you spend most of the time\
    \ just doing other things, so you don't really focus on the machine learning part."
  sec: 392
  time: '6:32'
  who: Alexey
- line: "You also mentioned that as a data scientist, the code that you were writing\
    \ wasn't really high quality. This is something that maybe because it isn't the\
    \ focus for data scientists. You focus on other things. Were there other reasons\
    \ why it was clear for you, \u201CData science is not for me. I want to go more\
    \ into data engineering.\u201D?"
  sec: 392
  time: '6:32'
  who: Alexey
- line: "Yeah. Those were two of the main reasons, but there was another reason as\
    \ well. I realized that \u2013 at least at the time when I was trying to be a\
    \ data scientist \u2013 if you didn't work in a large company, like maybe OLX\
    \ or Zalando, or one of the really big giant companies, the roles of data scientists\
    \ were pretty frustrating. I'd never wanted to work in such a large company. If\
    \ you start up a data science department, you\u2019re usually just stuck doing\
    \ a lot of really drudgery work and I got tired of that. In a lot of companies,\
    \ and that's the sad truth \u2013 engineering is more respected than data science,\
    \ except for those that really focus on data science. So I realized that whenever\
    \ I did more data engineering work, I had a more comfortable working environment,\
    \ my skills were more in demand and I didn't have to fight so much for getting\
    \ anything or proposing ideas, and things like that. So it was also a question\
    \ of professional respect for me \u2013 I was more comfortable with the environment\
    \ that I was experiencing as a data engineer rather than as a data scientist."
  sec: 458
  time: '7:38'
  who: Ellen
- line: "That's an interesting point. I didn't hear about this in Zalando, or OLX,\
    \ or other companies here in Berlin. But I did hear that a lot from big tech companies,\
    \ like FAANG \u2013 Amazon, Facebook (which is meta now), Google, and so on \u2013\
    \ that, as you said, engineers are more respected. Also I heard only anecdotal\
    \ evidence of that. People tell me that engineers are like first-class citizens\
    \ while data scientists aren't. I am quite surprised to hear that, to be honest.\
    \ But I guess since many people mention it, this is becoming a pattern, which\
    \ is pretty sad."
  sec: 522
  time: '8:42'
  who: Alexey
- line: It is sad, yeah. I don't think it should be that way at all, but it is. Unfortunately,
    I've experienced this with quite a few places.
  sec: 572
  time: '9:32'
  who: Ellen
- header: The overlap between data science and data engineering
- line: "I guess, as a data scientist, you already needed to do some things that data\
    \ engineers would do, right? You mentioned that at SoundCloud, you not only did\
    \ modeling, but also everything that was before modeling, like building data pipelines,\
    \ and after modeling \u2013 deploying the model. How does what you did as a data\
    \ scientist overlap with what data engineers usually do?"
  sec: 581
  time: '9:41'
  who: Alexey
- line: Yes, there's a lot of overlap. As a data scientist, you often don't work with
    perfectly clean and perfectly delivered data. You will still build up your own
    pipelines to make the data accessible, especially as you move into more production-level
    things. I mean, data scientist is a very loose title and what you do in this role
    can be very different. There's often a lot of pipelining work that you do yourself.
    I think it's a good thing that data scientists do that and don't just rely on
    data engineers to handhold them through these steps. There are a lot of transferable
    skills. Also, data engineering is a very broad topic and I never did more Kafka
    real-time data engineering kind of stuff. I've carefully navigated myself around
    that. I've always done what is now considered analytics engineering, which is
    more like preparing data for BI and data warehouses and scheduling, batch processing,
    and all these kinds of things. That was more my realm of data engineering.
  sec: 607
  time: '10:07'
  who: Ellen
- line: "There's this whole other universe of data engineering that I've never really\
    \ touched, where you need a better understanding of distributed systems and things\
    \ like that, which I don't have. That is often more the playground for people\
    \ with a really strong distributed computer science background. That just is not\
    \ my realm. If anything, that's more in the realm of what is now called analytics\
    \ engineering \u2013 that kind of branch of data engineering, I think data scientists\
    \ are really well prepared for. There are obviously things we need to learn, but\
    \ I've often found that people that come from pure software engineering don't\
    \ have a feeling for data \u2013 that they struggle more to move into that space\
    \ than the people that have a data science background. They just need to level\
    \ up on software engineering and collaboration skills."
  sec: 607
  time: '10:07'
  who: Ellen
- line: "What is this \u201Cfeeling of data\u201D in your opinion? What is that?"
  sec: 722
  time: '12:02'
  who: Alexey
- line: "Yeah, that means understanding, it's a lot of things about data. Data, as\
    \ you know \u2013 I don't have to tell you \u2013 it\u2019s very complex. How\
    \ it's produced, all the quirks to test, the statistical aspects of it, understanding\
    \ what the data actually means, how it's structured, how it evolves. From software\
    \ engineering, I remember that data is often just something that we don't really\
    \ worry about \u2013 it\u2019s just something we pipe in and out, but we don't\
    \ really worry about what it is."
  sec: 726
  time: '12:06'
  who: Ellen
- line: "Some JSON or XML file \u2013 you just get it, do something with it, and then\
    \ you spit it out. And then something happens after that. Right?"
  sec: 753
  time: '12:33'
  who: Alexey
- line: "But the big part of data engineering is really worrying about the quality\
    \ of your data, that's probably the biggest challenge for data science. That's\
    \ something that data scientists are very familiar with \u2013 data quality issues,\
    \ how to deal with them, what to do about them, and having these conversations\
    \ with the people that collect the data, produce the data and all these kinds\
    \ of things."
  sec: 762
  time: '12:42'
  who: Ellen
- line: "You also mentioned that you were doing more work of what today is called\
    \ \u201Canalytics engineer\u201D rather than a Kafka distributed system kind of\
    \ data engineer. Do you think this worrying about data quality applies to all\
    \ data engineers, regardless of whether they work with distributed systems, or\
    \ more with DBT kinds of tools?"
  sec: 785
  time: '13:05'
  who: Alexey
- line: "I think it applies to everyone because data quality is just a theme of data.\
    \ I mean, data always has quality issues. You can\u2019t avoid that. I think just\
    \ the extent that people worry about it is different. Maybe it's because I'm not\
    \ that in tune with that community, but I hear fewer concerns about data quality\
    \ from the distributed systems crowd than I hear from the analytics engineering\
    \ crowd, but data quality issues are just a fact of life that you have to deal\
    \ with."
  sec: 808
  time: '13:28'
  who: Ellen
- line: "To summarize: the skills that are transferable from data science to data\
    \ engineering are 1) This pipeline building thing \u2013 you need to prepare your\
    \ model or the data that before you can put it in the model, so you need to have\
    \ a data pipeline. 2) This \u201Cfeeling of data\u201D\u2013 knowing that data\
    \ is not just a simple JSON. Is there something more?"
  sec: 835
  time: '13:55'
  who: Alexey
- line: "Yeah. Generally, the whole explorative and communicative approach \u2013\
    \ data scientists usually have to work really closely with their stakeholders\
    \ and their business demands. That is super important as a data engineer as well.\
    \ You never produce the data for yourself and you never produce it yourself \u2013\
    \ you always get it from somebody and you get it for somebody. Talking with both\
    \ the producers and the data consumers is really key, as is being able to understand\
    \ what they need, even if they don't know exactly what they need or why they're\
    \ producing the data and how they're producing the data."
  sec: 863
  time: '14:23'
  who: Ellen
- header: Skills to learn and improve for data engineering
- line: "Okay. So: pipeline building, getting a feel for the data, and stakeholder\
    \ management and communication. But what were the things where you needed to upskill\
    \ yourself or to learn in order to make the transition? One thing you mentioned\
    \ is that as a data scientist \u2013 and for most data scientists \u2013 it's\
    \ not the focus to produce good quality code. I guess that was one of the areas\
    \ that you needed to upskill yourself, right? Are there other areas?"
  sec: 902
  time: '15:02'
  who: Alexey
- line: "There were two other areas that I think are really important. One is the\
    \ whole idea of collaborating with other engineers. There's a whole amount of\
    \ tooling like version control, books, CD/CI pipelines, and all these kinds of\
    \ tools that software engineers usually use to collaborate together and to make\
    \ sure that whenever they work in larger teams that the code still runs, still\
    \ tests properly, doesn't break and can be restored if one of them makes a mistake,\
    \ and that they catch mistakes and all that kind of things. Usually, as a data\
    \ scientist, it's very common for us to work alone on our own Jupyter notes or\
    \ whatever we might be using. But there\u2019s this whole collaboration around\
    \ making sure that you can work with your team members in a reliable and consistent\
    \ way. That's something I had to learn."
  sec: 941
  time: '15:41'
  who: Ellen
- line: "There\u2019s also the mentality around pairing and code reviews and things\
    \ that data scientists sometimes talk about and sometimes are aspirational about,\
    \ but aren't that much part of their daily practice. The whole \u201Cneeding clean\
    \ code and good quality code\u201D is just an aspect of that, because you don't\
    \ write it as an end in and of itself \u2013 just to make the code really beautiful\
    \ so you can put it in a frame on the wall. It\u2019s really to help your colleagues\
    \ understand what you were thinking about when you wrote that code. The other\
    \ thing is, the whole \u201Chow to deploy things,\u201D and the whole DevOps aspect\
    \ of data engineering, which is pretty strong actually, how to how to deploy things,\
    \ how to how to spin up and shut down servers or Airflow clusters, or whatever\
    \ you might need to put it another spot, to dealing with our cloud infrastructure\
    \ in an efficient way, and not just by poking around in the UI, but also by automating\
    \ things efficiently. That is the other thing that I really had to learn. That\
    \ was my least favorite part initially, but now I enjoy it."
  sec: 941
  time: '15:41'
  who: Ellen
- line: "Yeah. This poking the UI part is very close to my heart as a data scientist,\
    \ because what we are trying to do at OLX is to educate data scientists to use\
    \ things like Terraform. It's always easier just to go there, click buttons in\
    \ the AWS console, and then you have your lambda function or whatever. But then\
    \ people who need to look after the infrastructure \u2013 after the AWS account\
    \ \u2013 they always come and say, \u201CHey, what are you doing here? Why did\
    \ you do this?\u201D Because they don't have any visibility into what's going\
    \ on."
  sec: 1054
  time: '17:34'
  who: Alexey
- line: "Do you think that for data scientists \u2013 people who do not plan to switch\
    \ to data engineering in the future \u2013 do you think it's also useful to learn\
    \ skills like CI/CD testing, infrastructures, code automation, and all these things?\
    \ Do you think it's useful for them or that it shouldn't be their focus?"
  sec: 1054
  time: '17:34'
  who: Alexey
- line: "I think the data scientist role is a bit bifurcating right now. There's more\
    \ ML engineering and MLOps and all these new fancy titles that are springing up.\
    \ For everybody who wants to work more on this building production service ML,\
    \ it is definitely really important to understand how to do monitoring, how to\
    \ do infrastructure, automation, testable infrastructure and all these kinds of\
    \ things are really, really, really important if you want to have anything in\
    \ production. Because if it's in production, it has to meet the quality standards\
    \ of everything, otherwise if it's in production, it can also be the weak link\
    \ in your ecommerce or whatever infrastructure you have. If you really want to\
    \ stay in a more research focused thing, where all you do is prototyping, which\
    \ I guess still exists, I'm not sure. It's becoming less and less common to have\
    \ these kinds of data science roles where they\u2019re really just putting prototypes\
    \ of visualizations. There I guess you don't need to have these skills, but I\
    \ think the trend is moving in the direction where it's really valuable to have\
    \ the skills."
  sec: 1111
  time: '18:31'
  who: Ellen
- header: Ways to pick up and improve skills (advice for making the transition)
- line: "This part of modeling is only a small part, right? But the vast thing before\
    \ that is \u201CHow do you prepare data?\u201D Then a vast thing after you train\
    \ the model is \u201CHow do you go about deploying this?\u201D The modeling part\
    \ is only like a couple of percent of the actual work. That's why we have ML engineers\
    \ and data engineers \u2013 to help data scientists take care of that. Yeah, interesting.\
    \ How did you actually pick up the skills? Did you just learn by doing projects\
    \ or did you learn it at work? Or did you need to take some courses? How did you\
    \ learn this CI/CD and all these other things?"
  sec: 1176
  time: '19:36'
  who: Alexey
- line: "I mostly learned it at work. Native Instruments and at ThoughtWorks I was\
    \ lucky to have worked with really talented people and ThoughtWorks, in particular,\
    \ has a really strong culture on engineering practices, so I picked up a lot there.\
    \ But also at Native Instruments, I had a colleague who was really dedicated to\
    \ these kinds of practices and brought a lot of this into our team. I was fortunate\
    \ to learn this, but back then, when I moved into data engineering, there weren\u2019\
    t that many courses around these topics. Therefore, it was kind of a necessity\
    \ to learn it at work. But I think nowadays, if you have the chance to take one\
    \ of those courses, you should. Right now, our data engineer in my team is currently\
    \ taking the data engineering bootcamp that you're organizing. I think opportunities\
    \ like that are really helpful for people to pick up these skills in a more organized\
    \ fashion and not just rely on the lucky or unlucky coincidence that your colleagues\
    \ can help you."
  sec: 1223
  time: '20:23'
  who: Ellen
- line: "But do you know how it usually happens? Yes, indeed, we don't have a lot\
    \ of materials for data engineering. For data science, we've had courses for quite\
    \ a while \u2013 for five or more years. For data engineering, this is still emerging.\
    \ Do you think if a data scientist wants to become a data engineer, that they\
    \ already have enough skills to get the job as a data engineer? Or do they need\
    \ to upskill themselves before they can get a job?"
  sec: 1285
  time: '21:25'
  who: Alexey
- line: It's very individual-based. I've seen data scientists that are brilliant and
    really pick up software engineering and DevOps really quickly. And I've seen people
    that really struggled with that. I think that's why it really depends on the individual.
    I would always recommend trying it first. Also, before you make a big career transition,
    figure out if you really want to go in that direction. I think it's always helpful
    to do a side project or try it out at work in a small context where you can find
    that out before you decide that you really want to change your career. That's
    a mistake I've made, actually, sometimes to switch roles too quickly and then
    realize it wasn't for me.
  sec: 1315
  time: '21:55'
  who: Ellen
- line: Is that what happened with data science?
  sec: 1353
  time: '22:33'
  who: Alexey
- line: Yeah, exactly. For me that was a bit of a dead end. I probably could have
    figured that out earlier, but I didn't. I would recommend for people to try it
    out and see if they would consider a new role more attractive. That way, they
    can really jump into it without switching their entire job.
  sec: 1355
  time: '22:35'
  who: Ellen
- line: "Probably for data scientists \u2013 at least for most data scientists \u2013\
    \ they have a way to actually try this. You need to take care of data preparation,\
    \ right? Even if you have data engineers in your team this still needs to happen.\
    \ Maybe you can just work closer with data engineers and learn from them. Then\
    \ you can realize if this is indeed for you and only then decide to transition\
    \ to a data engineer full time."
  sec: 1374
  time: '22:54'
  who: Alexey
- line: "Exactly. Maybe then also invest more fully into formalized training or courses\
    \ or something like that. I think that's the best path \u2013 to just try it out\
    \ by expanding your scope of work a little bit, seeing if it's for you and how\
    \ comfortable you are and how much joy it brings you."
  sec: 1405
  time: '23:25'
  who: Ellen
- line: "I see two major paths for people who want to get into data science. Usually,\
    \ they either come from more mathematical backgrounds \u2013 maybe they have a\
    \ PhD in physics \u2013 in other words, they come from academia. Then there is\
    \ another path, which is people who are software engineers who want to get into\
    \ data science. I guess there is also a third way now, which is people who graduate\
    \ from universities and become data scientists immediately. I think this is also\
    \ a thing right now \u2013 for many people data science is their first job."
  sec: 1421
  time: '23:41'
  who: Alexey
- line: "For those who are software engineers and become data scientists, it's not\
    \ that difficult to then transition to data engineering because they already have\
    \ all the necessary skills. They know how to use the terminal properly, they know\
    \ batch, they know CI/CD \u2013 all these things that are needed for data engineers.\
    \ But what about the people who are coming from academia or those who have data\
    \ science as the first job \u2013 how can they actually level up their software\
    \ engineering skills? Do you know if there is a good course about that somewhere?"
  sec: 1421
  time: '23:41'
  who: Alexey
- line: "Yeah, there are good courses about this. Data camp is not really recommended\
    \ anymore for various reasons, but that used to be my go-to place because they\
    \ had a really good engineering track. But there are other online courses that\
    \ focus on these things. I would always recommend for data scientists who want\
    \ to level up on programming skills to take one of those intro to software engineering\
    \ courses, and even if it's web development or something totally unrelated \u2013\
    \ something that they may not really be that interested in. But something that's\
    \ not geared at data scientists because in the programming for data scientists\
    \ course, they usually don't put a lot of software engineering fundamentals."
  sec: 1504
  time: '25:04'
  who: Ellen
- line: "So they need something that's more of a track to become a web developer or\
    \ even an Android developer or something like that. They usually teach the software\
    \ engineering fundamentals in those courses. So I would recommend trying that.\
    \ It's always useful if you can go build a small web app or you can build a small\
    \ Android app \u2013 it's not a waste of skill. That's maybe a better way to find\
    \ out if you're interested in these kinds of things and then later purely focus\
    \ on your Python skills and learning yet another deep learning library."
  sec: 1504
  time: '25:04'
  who: Ellen
- header: "What makes a data engineering course \u201Cgood\u201D"
- line: "So what kind of things do you think a good course should contain? I guess,\
    \ build tools \u2013 how exactly you build your software, right? Then testing,\
    \ CI/CD, command line basics \u2013 how you navigate something like Linux, or\
    \ how to use Linux. Bash. Is there something else that you would say is fundamental\
    \ for all software engineers?"
  sec: 1580
  time: '26:20'
  who: Alexey
- line: "Two things, yeah. Git \u2013 which you probably included somewhere in build\
    \ tools, but it's worth pointing out separately. Docker is also really, really\
    \ useful. That may be a separate cause in many cases, but it's definitely a really\
    \ valuable skill. Then there's the whole idea of just collaborative coding or\
    \ clean coding \u2013 knowing the best practices on how you structure coded functions\
    \ and objects or modules \u2013 these kinds of things. How you comment, how much\
    \ you comment \u2013 all these things that software engineers pull their hair\
    \ out and get into holy wars about. But it\u2019s worth understanding. How many\
    \ lines of code should be in a function? All these kinds of questions are really\
    \ useful to get a sense for, even if you're never engaged in any of these holy\
    \ wars."
  sec: 1609
  time: '26:49'
  who: Ellen
- line: So how many lines of code should there be in a function? [laughs]
  sec: 1659
  time: '27:39'
  who: Alexey
- line: "Less than a screen [laughs] that\u2019s my answer."
  sec: 1662
  time: '27:42'
  who: Ellen
- line: '[laughs] Less than a screen. Okay. I remember reading the Clean Code Book
    from Robert Martin. I think his recommendation was like eight lines or something
    like that. This is pretty drastic, right?'
  sec: 1665
  time: '27:45'
  who: Alexey
- line: Yeah. Exactly. Just enough to have one full if then/else than statement. That
    was his recommendation.
  sec: 1676
  time: '27:56'
  who: Ellen
- line: "So basically, you have a function declaration, then just a few lines. Then\
    \ you have \u201Creturn\u201D and that\u2019s it. [laughs]"
  sec: 1682
  time: '28:02'
  who: Alexey
- line: "Yeah, he proposes having nesting of your function so that every line is pretty\
    \ much a function call until you have your really small function. Really strong\
    \ decomputization, which has its benefits and drawbacks, but yeah\u2026"
  sec: 1689
  time: '28:09'
  who: Ellen
- line: Do you think it's a good book nowadays? It's pretty old, right? It's more
    than ten years old I think.
  sec: 1702
  time: '28:22'
  who: Alexey
- line: "It\u2019s pretty old and it's very Java-centric. Unfortunately, I have not\
    \ found a better book. I still keep thinking somebody should write a better book,\
    \ or rather a new, more modern book about it. Maybe also something that\u2019\
    s less controversial nowadays due to politics. But unfortunately, there's still\
    \ nothing better at the moment. I still really recommend it, even though I have\
    \ a lot of pains about it. It's still, unfortunately, the best thing we have as\
    \ far as I'm aware."
  sec: 1708
  time: '28:28'
  who: Ellen
- header: Languages to know for data engineering
- line: "Even though it's Java, right? I started as a Java developer, and for me,\
    \ it was eye opening. I also recommend this book to people, but I realize that\
    \ now it may be outdated. Maybe that's another question \u2013 what kind of languages\
    \ do we need for data engineering? Is Python enough? Or do we need to go with\
    \ Java and Scala and perhaps other languages?"
  sec: 1734
  time: '28:54'
  who: Alexey
- line: "Again, it really depends on what kind of branch of data engineering you want\
    \ to go into. If you go into something that\u2019s more analytics, then yeah,\
    \ I would recommend for data scientists to at least try it out first. SQL and\
    \ Python are often enough, but sometimes you may need Java, depending on what\
    \ scheduler you\u2019re using. But usually you can get very far with Python and\
    \ SQL and maybe JavaScript. But JavaScript is the lower ranking third option.\
    \ If you want to go into the whole Kafka and real-time streaming and distributed\
    \ systems branch of data engineering then yeah, Scala and Java, I guess, are unavoidable.\
    \ I'm not saying they're terrible, even though I don't really like both of these\
    \ languages, but it's just my personal preference. They\u2019re actually really\
    \ good languages if you get into them. I've done a lot of Java development and\
    \ a fair amount of Scala development in my life, but I'm kind of glad I don't\
    \ do either right now."
  sec: 1762
  time: '29:22'
  who: Ellen
- line: '[laughs] It''s the same for me. Well, at least for Scala. I don''t know,
    there are too many ways of doing the same thing and not all of them are obvious,
    I''d say. To me at least. Why JavaScript though? Why do you recommend learning
    JavaScript?'
  sec: 1824
  time: '30:24'
  who: Alexey
- line: "It's becoming more than just a backend language as well. JavaScript is kind\
    \ of emerging as a general purpose language in a way that Python always aspires\
    \ to be but never quite made it because it doesn't have a front-end component\
    \ really to the same degree. There is tooling also in the no code space, for instance,\
    \ which relies on JavaScript as a scripting language. So it's useful to know,\
    \ but as a really low ranking, I wouldn't give it a high priority that the other\
    \ languages have. But it's useful to know \u2013 just to be able to read a lambda\
    \ function that was written in JavaScript that your colleagues wrote and be able\
    \ to see where you have to maybe modify it or at least talk to them where they\
    \ need to modify it."
  sec: 1845
  time: '30:45'
  who: Ellen
- line: "I guess the reason that these obscure JavaScript functions exist is because\
    \ when you Google something \u2013 when you try to look something up \u2013 often\
    \ the examples are in Python or JavaScript. When I see an example in JavaScript\
    \ and I need to do something quickly, I just copy/paste, check that it works and\
    \ then I forget about it until it stops working."
  sec: 1894
  time: '31:34'
  who: Alexey
- line: Exactly. I think even in BigQuery, for instance, the default UDF language
    (user defined functions) are just JavaScript.
  sec: 1915
  time: '31:55'
  who: Ellen
- line: There is no Python support?
  sec: 1925
  time: '32:05'
  who: Alexey
- line: "I haven\u2019t seen it, no. I think we had to write all our UDFs in JavaScript\
    \ for some reason. JavaScript pops up at the weirdest places. That's why it's\
    \ useful to know."
  sec: 1927
  time: '32:07'
  who: Ellen
- line: "Probably, Google wanted to have broader coverage. I don't know what the latest\
    \ status is, but I think if you take software engineers in general \u2013 people\
    \ who know how to code \u2013 there are probably more people who know JavaScript\
    \ and Python, right?"
  sec: 1940
  time: '32:20'
  who: Alexey
- line: Definitely, yeah.
  sec: 1960
  time: '32:40'
  who: Ellen
- header: The easiest part of transitioning into data engineering
- line: "Perhaps that just gives some wider coverage to Google \u2013 to BigQuery.\
    \ Okay. What do you think was the easiest part of your transition?"
  sec: 1963
  time: '32:43'
  who: Alexey
- line: "The easiest part of the transition was how much demand there was for data\
    \ engineering. I think that still holds. Even if you're not the greatest data\
    \ engineer when you're starting out, people will still get really excited about\
    \ the fact that you exist and that you applied to their company. It's very easy\
    \ to find a job in data engineering. It's not super competitive, which is a good\
    \ thing when you're starting out. It also has its drawbacks because you can easily\
    \ find yourself in a situation where you're way overwhelmed and expected to do\
    \ things that you aren't ready for and where you don't have good mentoring in\
    \ place that can help you in your job. There may not be enough senior or experienced\
    \ people around that can help you with what you're doing. But the easiest part\
    \ is definitely \u2013 just give yourself the title of data engineer and your\
    \ LinkedIn profile invites will explode."
  sec: 1973
  time: '32:53'
  who: Ellen
- line: "Interesting. I observed a similar thing, not with data engineers, though\
    \ \u2013 with infrastructure engineers. We call them \u201Csite reliability engineers\u201D\
    \ but another name is DevOps engineers \u2013 people who take care of infrastructure.\
    \ It's super difficult to find these people. When we open a position for data\
    \ science, in one day, we have 100-200-300 applications. For a week, it can be\
    \ quite a lot. Our recruiters just closed the position after a couple of days.\
    \ But when it comes to site reliability engineers, we open a position and nobody\
    \ applies. The second day, maybe one person will apply. The third day, again,\
    \ nobody. So HR needs to actually reach out to people on LinkedIn and ask them\
    \ \u201CHey, consider our position.\u201D I guess to some extent, this also applies\
    \ to data engineers."
  sec: 2025
  time: '33:45'
  who: Alexey
- line: "I think data science still has this marketing thing like, \u201CIt\u2019\
    s the sexiest job of the 21st century.\u201D So people get excited and everyone\
    \ wants to do that. But I think data engineering is also getting some traction.\
    \ Now people like you realize that it's not what they want to do and people see\
    \ the demand for data engineers. There are also quite a few posts on the internet,\
    \ such as on Hacker News and on Reddit, where the headlines were \u201Cyou don't\
    \ need data scientists, you need data engineers.\u201D You probably saw them as\
    \ well, right?"
  sec: 2025
  time: '33:45'
  who: Alexey
- line: No, I actually did not.
  sec: 2120
  time: '35:20'
  who: Ellen
- header: The hardest part of transitioning into data engineering
- line: This is the type of content that people on Hacker News usually like - very
    controversial stuff. Yeah. So that's interesting. What was the most difficult
    part of the transition for you?
  sec: 2123
  time: '35:23'
  who: Alexey
- line: "The most difficult part for me was losing some of the autonomy I had as a\
    \ data scientist, and then also having to work in these really close, tight-knit\
    \ software engineering teams. I was really used to having a lot of space, working\
    \ the way I wanted to, and not worrying too much about other people being in my\
    \ space, other than my stakeholders \u2013 I knew how to work with them. But I\
    \ was not familiar with working with other software engineers that much \u2013\
    \ at least I hadn\u2019t done it in a long time. So when I got hired as a senior\
    \ data engineer, things were expected of me that I had never done before, in terms\
    \ of collaboration and in terms of leadership and leveling up on those was quite\
    \ hard. That's not something that you just pick up by reading a blog post. But\
    \ that was really a very different way of working and not even understanding what\
    \ was expected of me, because the people I was used to working with were data\
    \ scientists, so they didn't know what to expect of me either. Then there was\
    \ this whole mismatch of expectations on both sides. I figured it out, but it\
    \ was hard."
  sec: 2140
  time: '35:40'
  who: Ellen
- line: Can you maybe give an example? Is it like setting up the way you do things,
    picking up some frameworks, or what exactly do you mean by this leadership?
  sec: 2203
  time: '36:43'
  who: Alexey
- line: "Yeah, it wasn't technical skills at all. I could pick up the tooling that\
    \ worked with most of it before and I could pick up on what was missing easily.\
    \ It was more like, \u201CHow do I communicate? When do I communicate? How do\
    \ I pair with people?\u201D Pairing was probably the hardest part for me to learn\
    \ because I'd never done that before."
  sec: 2217
  time: '36:57'
  who: Ellen
- line: Paired programming, right?
  sec: 2236
  time: '37:16'
  who: Alexey
- line: "Yeah. Paired programming, yes. Work was really heavy on emphasizing pair\
    \ programming, but sharing mainly just boiled down to sharing my thoughts and\
    \ knowing when to ask for help and when to offer help \u2013 and all these kinds\
    \ of small things that I wasn't used to, since I was working mostly by myself\
    \ before. Really, it was knowing how to work very closely with people on a day-to-day\
    \ level, keeping them in the loop, knowing when I need to get myself into the\
    \ loop, and all these kinds of questions."
  sec: 2237
  time: '37:17'
  who: Ellen
- line: So you would say that data engineering is more of a team sport than data science?
    And engineering in general, I guess. Because usually, you have a lot more engineers
    than data scientists, for a team, you maybe have one data scientist, and then
    a bunch of backend engineers, right?
  sec: 2269
  time: '37:49'
  who: Alexey
- line: Exactly, exactly. And usually you also have more data engineers than data
    scientists. So there's a whole different approach to working together.
  sec: 2288
  time: '38:08'
  who: Ellen
- header: Common data engineering team distributions
- line: In your experience, do data engineers usually work in one team? For example,
    maybe there is one platform or data engineering team? Or are they spread across
    different teams?
  sec: 2300
  time: '38:20'
  who: Alexey
- line: "I\u2019ve seen both options. I prefer the model where there's not a data\
    \ engineering platform team, I think. Unless you have a really large company where\
    \ you really need a data platform infrastructure and you need people dedicated\
    \ to that thing. In smaller companies, I think it works better if the data engineers\
    \ are embedded either with the other data folks or as part of a wider platform\
    \ team. But what I've usually worked with is kind of embedded into the more general\
    \ data teams that consisted of analysts and data engineers and data scientists\
    \ \u2013 maybe ML engineers, and all sorts of data specialists."
  sec: 2313
  time: '38:33'
  who: Ellen
- line: In this setup you usually see more engineers than data scientists, right?
  sec: 2351
  time: '39:11'
  who: Alexey
- line: Yes, usually. But there can also be a lot of analysts, for example. That's
    a common thing to see. It depends on the setup.
  sec: 2358
  time: '39:18'
  who: Ellen
- header: People who are both data scientists and data engineers
- line: Okay. There is a question. Do you know if there is a name for the role for
    people who are both data engineers and data scientists? Does such a thing even
    exist at all?
  sec: 2370
  time: '39:30'
  who: Alexey
- line: Um, I've not encountered it as such, but I think the closest I've seen is
    really an analytics engineer. Again, it depends on what you consider a data scientist
    as being a data engineer because the overlap might be on all sorts of things.
    If it goes to the end, it could also be an ML Ops engineer, for example. That
    could also be an intersection between a data engineer and a data scientist. There
    are a bunch of titles, but it really depends. Maybe the person could clarify a
    bit. It really depends on what you're doing at this intersection.
  sec: 2384
  time: '39:44'
  who: Ellen
- line: "I think, as a data scientist, you \u2013 or at least I did \u2013 need to\
    \ do a lot of data engineering. The data is not just magically a CSV file that\
    \ you can use that is clean. You need to do a lot of work before you can put this\
    \ into a machine learning model and train your model. For me, I even needed to\
    \ set up a workflow scheduler and to do all that."
  sec: 2422
  time: '40:22'
  who: Alexey
- line: "I think in startups, it's pretty common that they hire a data scientist and\
    \ then it turns out that this data scientist actually needs to do data engineering\
    \ work before they can start with the data science. I also saw a title in LinkedIn\
    \ \u2013 some people put this title \u2013 the title is \u201Cdata science engineer.\u201D\
    \ I don't know how common it is or if it\u2019s even a thing, or maybe they just\
    \ decided to put it there because this is how they felt. I don't think it's a\
    \ common thing."
  sec: 2422
  time: '40:22'
  who: Alexey
- line: "I've seen that too. I haven't seen it in a job description. I\u2019ve only\
    \ seen it in people's profiles."
  sec: 2485
  time: '41:25'
  who: Ellen
- header: Pet projects and other ways to pick up development skills
- line: "Yeah. It\u2019s probably people who ended up doing data stuff even though\
    \ they were hired as data scientists. Okay. Chetna is asking if you have any tips\
    \ for people who do not have development experience \u2013 how can they transition\
    \ to data engineering? I think we talked about that already. It involves picking\
    \ up all these skills, like general engineering skills. I think it was build tools,\
    \ testing, CI/CD, Git, Docker, clean coding, command line, testing. Is there anything\
    \ else?"
  sec: 2489
  time: '41:29'
  who: Alexey
- line: "Yeah. Especially if you don't have some engineering experience, I would recommend\
    \ just doing pet projects on the side. That's very common for software engineers\
    \ to do. They just build something random that they think is fun or useful. Find\
    \ some friends to work together with, because that makes a big difference if you're\
    \ not just working by yourself, but if you're also working with two, three other\
    \ people. Pick something that you really find fun. For instance, I\u2019ve built\
    \ a lot of Twitter automation things back when I was trying to get into data engineering.\
    \ I didn't use any of the skills I learned about Twitter and Twitter analysis\
    \ at the time. But it was really useful to learn to deal with annoying things\
    \ like ORs  and figuring out how that works and using Git properly and all these\
    \ kinds of things. If you have time \u2013 not everybody has the luxury to have\
    \ that kind of time \u2013 but if you do, it's really helpful."
  sec: 2534
  time: '42:14'
  who: Ellen
- line: What was one of these tools? Maybe you can give us an example? Is it like
    pulling data from Twitter for doing some analytics, or something else?
  sec: 2592
  time: '43:12'
  who: Alexey
- line: "Yeah. That was a while ago. That was before Cambridge Analytica, but I read\
    \ the papers that Cambridge Analytica was based on \u2013 Kosinski papers from\
    \ Cambridge University. He did a lot of identifying Big 5 profiles out of Twitter\
    \ data and since I was a psychology student at the time, I wanted to see if I\
    \ could replicate it. So I pulled data from Twitter and that was supposed to be\
    \ turned into a visualization of the Big 5 features as a web app. We never finished\
    \ that thing, but that's kind of the direction we wanted to be going."
  sec: 2600
  time: '43:20'
  who: Ellen
- line: "Okay, yeah. Thanks. A question from Harry, \u201CI am currently in the same\
    \ station. I am a data scientist and I want to move into data engineering. Would\
    \ you recommend doing projects that depict real-life data engineering tasks? Do\
    \ you think it would help in getting jobs?\u201D I think the short answer is \u201C\
    Yes,\u201D but maybe you can also give a longer answer, like what kind of projects\
    \ can be done in addition to what we just discussed \u2013 like pulling data from\
    \ Twitter. What else can data scientists do in order to move into data engineering?\
    \ What kind of projects can they do?"
  sec: 2640
  time: '44:00'
  who: Alexey
- line: "Generally, if you do side projects, I think it's really helpful to not think\
    \ about what is the most marketable but really, what is the most fun to you, because\
    \ you need to keep up your motivation for a while. Usually that comes if you build\
    \ something that's interesting to you, even if it may not be the most marketable\
    \ thing. For instance, there\u2019s a project I've seen a friend build when the\
    \ pandemic was fairly fresh \u2013 he had a computational biology background and\
    \ he wanted to help with identifying genetic markers for vaccines. As you can\
    \ see, that was a while ago. He got some datasets around the COVID genome and\
    \ some other genomes and then he built a whole ML pipeline \u2013 data engineering\
    \ pipeline \u2013 around extracting that data and building it up with CD/CI tools,\
    \ and understanding data, translating it into different formats, and extracting\
    \ the genome data, and re-encoding it. I didn't understand the biology part of\
    \ it, so I can only give a very bad representation, but that was kind of what\
    \ he did. I thought it was pretty cool."
  sec: 2681
  time: '44:41'
  who: Ellen
- line: "One recommendation I usually give when people ask me, \u201CHow can I learn\
    \ more about building data pipelines if I am a data scientist?\u201D I usually\
    \ suggest building a scraper. Let's say we want to build a model for predicting\
    \ the price of an apartment or a car, right? We have a lot of websites that sell\
    \ cars or where you can find apartments. You can set a scraper that goes to these\
    \ websites every day, pulls the data from there, puts them in a CSV file, and\
    \ then puts them in the cloud. Then you can schedule it with Airflow. So you can\
    \ have multiple steps there and the first step is the actual scraper that would\
    \ go there and pull the data. Then the other step is \u2013 you have the pages,\
    \ now you need to process these pages somehow. Then you extract, or parse, this\
    \ data. Then the other step would be to maybe put this in a CSV file. Then you\
    \ have a CSV file in your S3 or Google Cloud, or whatever cloud you use. I think\
    \ it's important here to use a cloud and to use tools like Airflow or other schedulers.\
    \ And then one of the steps there could be taking all this data and training your\
    \ model. Then it's not just a CSV file that you download from Kaggle and train\
    \ your model. It's still a toy pipeline, but you have a pipeline that you schedule\
    \ \u2013 that you run \u2013 every day, and one that you can use to actually learn\
    \ all these things \u2013 learn Airflow or whatever other scheduler. Do you know\
    \ of other similar projects? Does something come to mind?"
  sec: 2747
  time: '45:47'
  who: Alexey
- line: "Not really, no. But again, I think the general approach that you used was\
    \ really good \u2013 about building a real life pipeline with following whatever\
    \ best practices are. But really, I would reiterate the point that you should\
    \ pick some data that you find interesting. That was probably the best advice\
    \ I've been given by experienced data scientists when I got interested in this\
    \ space. I asked about recommendations for projects and I was recommended to pick\
    \ a dataset that I really wanted to find something out about. I think the same\
    \ applies \u2013 if you build a data engineering pile, build it for something\
    \ where you actually care about the outcome. You won't always have that luxury\
    \ at work. Sometimes you build a data pipeline for data you're really not interested\
    \ in. So at least when you're doing it in your spare time \u2013 care about the\
    \ data."
  sec: 2861
  time: '47:41'
  who: Ellen
- line: "I saw a post on LinkedIn about somebody who was looking for a flat in Berlin,\
    \ which is not very easy these days. What they did is also built a scraper. They\
    \ would look, \u201COkay, where are the flats?\u201D Basically, they get all the\
    \ data first, and then they see the flats with the price they are interested in,\
    \ the areas, the neighborhoods they're interested in. Then they look at flats\
    \ that stay there for a while and this way, they use this need to find a flat.\
    \ Based on that, they built this scraping pipeline and it helped them to find\
    \ a flat."
  sec: 2909
  time: '48:29'
  who: Alexey
- line: "That's awesome. That\u2019s a really cool project."
  sec: 2959
  time: '49:19'
  who: Ellen
- header: Dealing with cloud processing costs (alerts, billing reports, trial periods)
- line: "I don't know, maybe it's a bit off topic, but there\u2019s a question from\
    \ Brahm. \u201CMost cloud platforms, data processing cost structures are not really\
    \ transparent. Do you have any suggestions to manage data processing costs?\u201D\
    \ I guess this is also important when you learn to use these things. So do you\
    \ have any suggestions?"
  sec: 2962
  time: '49:22'
  who: Alexey
- line: I'm not sure that I would agree that they're not transparent. Usually the
    cloud providers provide very, very detailed billing information if you click into
    the billing console. Especially if you just have a side project, you can easily
    burn a lot of money if you don't shut off your instances and they keep running
    or whatever you might be doing.
  sec: 2984
  time: '49:44'
  who: Ellen
- line: "My recommendation is \u2013 most cloud platforms have a budgeting alert for\
    \ each function, so if you want to manage your costs, find out where you can get\
    \ you an email and get a warning for whatever \u2013 half of the money that you're\
    \ willing to spend, or a quarter of the money that you\u2019re willing spend.\
    \ That way you get pinged via email. Other than that, really dig into the billing\
    \ console, because there's a wealth of information in there. You can run it down\
    \ to the nitty gritty details of what exactly you're spending on \u2013 each processing\
    \ cycle of your AFL cluster. That information is there. It's a bit of a science\
    \ in and of itself to dig into that information. It may be a good data analysis\
    \ project, just to figure out how to extract what you're interested in from your\
    \ billing reports."
  sec: 2984
  time: '49:44'
  who: Ellen
- line: You can pull this data, right? Then you have another pipeline to practice.
  sec: 3059
  time: '50:59'
  who: Alexey
- line: "Exactly. You can build a pipeline \u2013 it's very meta. You can build a\
    \ pipeline about your pipeline costs. [laughs]"
  sec: 3065
  time: '51:05'
  who: Ellen
- line: "[laughs] I don't think this is a thing in AWS, but in Google Cloud, you have\
    \ a trial period where they don\u2019t charge you any money for the first couple\
    \ of months. They give you some money \u2013 some free credits \u2013 and you\
    \ can do whatever you want. If you run out of these free credits, they don\u2019\
    t start charging you. They send you an email saying, \u201CHey, you\u2019ve run\
    \ out of credits. Do you want to upgrade or not?\u201D It's a pretty safe environment\
    \ to learn things there. In AWS, I don't think that's the case. They do have a\
    \ free tier, but some things are part of the free tier and some things are not.\
    \ If something is not a part of the free tier, then you need to spend money on\
    \ it."
  sec: 3072
  time: '51:12'
  who: Alexey
- line: "You also need to be careful \u2013 let's say if you spin up a Kubernetes\
    \ cluster or something like that, you need to be careful once you've done whatever\
    \ you wanted to turn it off. Or else, you'll get a bill at the end of the month\
    \ that you won\u2019t like. I think the support is pretty good. Some of the students\
    \ had these problems \u2013 they forgot to shut down a Sage Maker instance with\
    \ a GPU, which is quite expensive. Then they just wrote support saying, \u201C\
    Hey, I accidentally forgot to do this. Would you be so kind as to remove that?\u201D\
    \ And they actually did, saying \u201COkay, yeah. Things happen.\u201D"
  sec: 3072
  time: '51:12'
  who: Alexey
- header: Advice for getting into entry level positions
- line: "Other questions. \u201CIn your perspective, what amount of project experience\
    \ should we get to start applying for entry level roles in the industry?\u201D"
  sec: 3166
  time: '52:46'
  who: Alexey
- line: That's a very generic question. Would it help? Is this for data engineering?
  sec: 3177
  time: '52:57'
  who: Ellen
- line: Let's imagine that a student has a general software engineering background.
    So they probably learned data structures, algorithms, programming, so they also
    know SQL. Now they want to start working as data engineers, what do they need
    to do?
  sec: 3183
  time: '53:03'
  who: Alexey
- line: Especially if you have a relevant background in studies, I would always recommend
    going directly for the entry level positions because I'm not a fan of people who
    have a full degree and then start to get into unpaid internships or doing a lot
    of side projects just to get into the field. That may happen to career changers,
    unfortunately, quite a bit. But if you have a relevant degree, then definitely
    try to aim for the entry level positions directly.
  sec: 3211
  time: '53:31'
  who: Ellen
- line: You will have done enough coursework and enough projects in university to
    be employable. Not every company offers entry level positions in data engineering,
    but those that do, they will be prepared for graduates. Or if you graduate from
    boot camp or something like that, then I would also directly aim for an entry-level
    position. If you don't have a relevant degree, but you have some other degree,
    then try to not do so many projects in your spare time, but try to get internships.
    That work will be a lot more relevant in terms of experience you get quickly,
    rather than just trying to motivate yourself. I've seen people that have purely
    graduated from their own projects, but those people are unusually driven. I've
    seen a lot more people fail with that approach than I've seen people succeed.
  sec: 3211
  time: '53:31'
  who: Ellen
- line: "You mentioned that there are not so many entry level positions for data engineering\
    \ and I think it's true. At least this is my perception, usually data engineering\
    \ companies want to see experienced people \u2013 as you mentioned, especially\
    \ if you're talking about Kafka and things like that. They already need to have\
    \ solid software engineering experience and know a bit of distributed systems\
    \ before they can be hired to this position. Do you think this is the case? Let's\
    \ say that since there are not so many entry level positions, would it be a good\
    \ idea for people who graduate from university to first work as a backend engineer\
    \ before they start working as a data engineer?"
  sec: 3298
  time: '54:58'
  who: Alexey
- line: "That's a really good question. I think it used to be that pretty much every\
    \ position that I've seen for that was at least mid-level, if not senior, because\
    \ the companies started out with building the data engineering teams. I think\
    \ that's changing now. There are increasingly more entry level positions, but\
    \ it depends on the type of company. Unless you're really confident in your skills,\
    \ or maybe you want to find your own thing \u2013 that's an exception \u2013 but\
    \ otherwise, I would really recommend starting in either a consultancy or a larger\
    \ company that already has an established data engineering department."
  sec: 3346
  time: '55:46'
  who: Ellen
- line: "For instance, I worked a lot in my life in agencies and consultancies, and\
    \ those were always good career accelerators for me. I've seen the same happen\
    \ for people that work in big tech companies like Zalando, Delivery Hero \u2013\
    \ all these big building companies, or whatever the local equivalent might be.\
    \ Those tend to be career accelerators because you usually have a really well-structured\
    \ learning environment. They have enough seniors and they're prepared to take\
    \ on juniors. They are prepared to mentor and develop their juniors. It's very\
    \ hard if you're starting out \u2013 and this is something that I\u2019ve also\
    \ seen quite frequently \u2013 if you're a junior and you get hired as the first\
    \ junior somewhere. There may not be a senior around and they just expect you\
    \ to start. It sounds really exciting, but in most cases I've seen that happen,\
    \ it was a recipe for frustration on all sides and a stalled career."
  sec: 3346
  time: '55:46'
  who: Ellen
- line: "Interesting. So consultancies are good career accelerators. Perhaps it\u2019\
    s because \u2013 let's say you have clients, and I imagine that there are not\
    \ enough seniors to work with all these clients, so that's why they have this\
    \ training in place to take this workload from seniors and put them on juniors.\
    \ That's why they want the juniors to be ready to do the work as fast as possible,\
    \ right? Then you have many projects \u2013 you need to be able to move quickly\
    \ from one project to another and that's how you get to see a lot of different\
    \ things. Is that right?"
  sec: 3442
  time: '57:22'
  who: Alexey
- line: That and it's also a very financial thing. Juniors simply cost less. With
    a consultancy, there's a big financial incentive for them to have this pyramid
    structure where they have a few seniors that do the architectural work and mentor
    the juniors, but the bread-and-butter work is usually done by juniors. So, most
    consultancies out there have their business model around up-leveling juniors.
    That leads to a lot of them having structured entry level programs. There are
    a lot of expectations around mentoring and that's ingrained into the culture.
  sec: 3479
  time: '57:59'
  who: Ellen
- header: Which cloud platform should data engineers learn?
- line: "Yeah, thanks. Maybe the last question. If somebody wants to learn cloud \u2013\
    \ should they go with AWS, Google Cloud Platform, Azure, or something else?"
  sec: 3516
  time: '58:36'
  who: Alexey
- line: "I don't think there's a real [difference]. I don't think it matters that\
    \ much because they're all very similar, actually. If you know your way around\
    \ one cloud, you can easily find your way around the next cloud, at least in my\
    \ experience. Either find the one that's used at your company and get really comfortable\
    \ with it and dig deep into it \u2013 learn all the functions that you can get\
    \ a hold of \u2013 or find one that has the best free options that are relevant\
    \ to you and just learn that one."
  sec: 3528
  time: '58:48'
  who: Ellen
- line: "I guess another option would be in your city or in your country \u2013 look\
    \ at what is the most common one, or the most popular one. For example, in Berlin,\
    \ if I look at job descriptions, I think AWS is more popular than Google Cloud.\
    \ Maybe if you're in Berlin, then going with AWS makes more sense. But I\u2019\
    ve heard that in other cities in Germany, maybe Azure is more popular than AWS."
  sec: 3560
  time: '59:20'
  who: Alexey
- line: "It depends on the sector of the industry you're working with. A lot of startups\
    \ use GCP because they have very generous startups offerings. For instance, we\
    \ barely pay anything for our Google Cloud offerings. A lot of larger tech companies\
    \ or more established tech companies that are not traditional enterprises, but\
    \ are grown and mature startups \u2013 a lot of them use AWS. In Germany, a lot\
    \ of the enterprisey companies use Azure. So it really depends on which branch\
    \ of the industry you want to be in or which one you happen to be working with."
  sec: 3586
  time: '59:46'
  who: Ellen
- header: Finding Ellen online
- line: Okay, thanks. Before we finish, how can people find you if they have questions?
    LinkedIn, Twitter?
  sec: 3621
  time: '1:00:21'
  who: Alexey
- line: "Yeah \u2013 either way works. Is there a way you can share my contacts with\
    \ the audience?"
  sec: 3630
  time: '1:00:30'
  who: Ellen
- line: Yes, I will. I will put this in the description.
  sec: 3635
  time: '1:00:35'
  who: Alexey
- line: Cool. Yeah. I can just share my Twitter and my LinkedIn profile with you and
    then I'm happy to talk if people want to get in touch.
  sec: 3639
  time: '1:00:39'
  who: Ellen
- line: "Okay, then I guess that's it. So thanks a lot for joining us today. Thanks\
    \ a lot for sharing your experience. Thanks, everyone, for joining us and watching\
    \ this \u2013 for asking questions. Yeah, that would be it."
  sec: 3647
  time: '1:00:47'
  who: Alexey
- line: Thank you. That was really fun. I really enjoyed this conversation.
  sec: 3659
  time: '1:00:59'
  who: Ellen


---

Links:

* [Twitter](https://twitter.com/ellen_koenig){:target="_blank"}
* [LinkedIn](https://www.linkedin.com/in/ellenkoenig/){:target="_blank"}
