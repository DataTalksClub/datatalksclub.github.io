---
episode: 1
guests:
- alvaronavaspeire
ids:
  anchor: From-Testing-Phones-to-Managing-NLP-Projects---Alvaro-Navas-Peire-e1oj7n8
  youtube: -xumbiXOlA8
image: images/podcast/s11e01-from-testing-phones-to-managing-nlp-projects.jpg
links:
  anchor: https://anchor.fm/datatalksclub/episodes/From-Testing-Phones-to-Managing-NLP-Projects---Alvaro-Navas-Peire-e1oj7n8
  apple: https://podcasts.apple.com/us/podcast/from-testing-phones-to-managing-nlp-projects-alvaro/id1541710331?i=1000581943071
  spotify: https://open.spotify.com/episode/1LMg70fGthIR2jF4JdmFkb?si=BmEfOtfgSEOpKvp5ENRA2g
  youtube: https://www.youtube.com/watch?v=-xumbiXOlA8
season: 11
short: From Testing Phones to Managing NLP Projects
title: "Transition from QA to Machine Learning & Data Engineering: Projects, Cloud & Interview Prep"
transcript:
- line: This week, we'll talk about career transitioning from quality assurance to
    machine learning. We have a special guest today, Alvaro. Alvaro worked in the
    cell phone industry as a quality assurance engineer, but got tired of it, spent
    a few years unemployed, fell in love with machine learning and eventually got
    hired by a consultancy company.
  sec: 75
  time: '1:15'
  who: Alexey
- line: Right now, Alvaro is managing machine learning and NLP projects. I got to
    know Alvaro when he took part in our machine learning and data engineering Zoomcamps,
    via our courses, and he published some awesome notes. If you're taking the course
    right now, you must have seen his notes – they're really amazing. If you haven't,
    please do check them out. He also helped other students a lot during the course.
    I'm very happy to invite Alvaro to this interview and talk about his career journey.
  sec: 75
  time: '1:15'
  who: Alexey
- line: Thank you very much for having me.
  sec: 123
  time: '2:03'
  who: Alvaro
- header: Alvaro’s background
- line: You're welcome. Thanks for joining us. Let's start with your background. Can
    you tell us briefly about your career journey so far?
  sec: 125
  time: '2:05'
  who: Alexey
- line: Right. I'm from Barcelona, Spain and I studied here. I studied informatics
    engineering, which in the old Spanish education system used to be a mix of computer
    engineering and computer science. We did lots of programming, but we also took
    a look at the hardware side of things. I did that. I started working for a cell
    phone company for a bit here in Spain. I actually did quality assurance – I received
    prototypes, I tested them.
  sec: 133
  time: '2:13'
  who: Alvaro
- line: Then this company changed. They didn’t change hands, but they changed the
    founding model or something. They started focusing more on Latin America. After
    that, I took a gap year and then they actually called me and said, “Hey, would
    you like to come to Mexico and work for us again?” And I said, “Yeah, sure. Why
    not?” I went there, I worked there for almost four years and I decided that I
    did not like that kind of job anymore. I did not enjoy the industry at all.
  sec: 133
  time: '2:13'
  who: Alvaro
- line: I decided to quit and went back to Spain. I was unemployed for two years.
    I studied in the meantime until I found machine learning. And I eventually managed
    to get hired by a company working in machine learning.
  sec: 133
  time: '2:13'
  who: Alvaro
- header: Working as a QA (Quality Assurance) engineer
- line: Interesting. What did your day look like when you worked as a quality assurance
    engineer? You mentioned that you received prototypes and you tested them. Was
    it like, I don't know, getting a phone and then clicking around on it?
  sec: 221
  time: '3:41'
  who: Alexey
- line: Essentially yeah. It's not like software QA – like for software testing. I
    did not do any kind of unit testing or anything like that. I just received a prototype
    and I did field testing. I went outside and checked the GPS, checked the map’s
    navigation, and how it worked. I tested the sound. I tested the microphone recording,
    I tested all the sensors in the phone. I did battery testing to see how well it
    performed. I checked for translation issues.
  sec: 236
  time: '3:56'
  who: Alvaro
- line: The way these kinds of companies work is, actually most of the design and
    construction and pretty much everything is done in China. If you have money and
    you want to build your own brand, what you do is go to China and then you contact
    an ODM – a design house – and they will do everything for you. You only have to
    put in the money, you have to put your branding and you have to take care of the
    importing and the paperwork in your country. You can find that many different
    small unknown brands will sell the same phone in different countries, just with
    different branding. They just went to the same design house, where they already
    offered a ready-made solution and that's how it works.
  sec: 236
  time: '3:56'
  who: Alvaro
- line: Sometimes you can also find exclusive designs, which is what my company did.
    We actually had designs that no one else had, but everything was still designed
    in China. I actually would have liked to go to China and get involved in that
    part of the design and development. Luckily, it was not meant to be. I decided
    to change careers and that's it. But yeah, I just received a prototype, I tested
    it and then made a report and sent it back. Then I would get a software update,
    which I would flash onto the phone and test it again. That's pretty much the workflow.
  sec: 236
  time: '3:56'
  who: Alvaro
- line: I guess you also had some sort of test suits – things you need to test, some
    sort of checklist, right?
  sec: 347
  time: '5:47'
  who: Alexey
- line: Yes, of course.
  sec: 353
  time: '5:53'
  who: Alvaro
- line: So it was some document. It wasn't like, “Okay, let me think about what I
    have to test today, right? Let me test the GPS.” [chuckles]
  sec: 354
  time: '5:54'
  who: Alexey
- line: I mean, at first, it was kind of like that. [laughs] Then, as we got more
    professional, we started doing our own checklists, and we wrote our own tests.
    In particular, for Android phones, you are supposed to pass… you have to certify
    your phone with Google if you want to have Google Apps in your phone. Otherwise,
    you're not allowed to. And you have to meet certain things and you have to pass
    certain tests. So that's called the CTS. I don't remember what it stands for,
    actually. [chuckles] It's been a while.
  sec: 360
  time: '6:00'
  who: Alvaro
- line: But I actually used to do that as well. Most of the CTS testing was carried
    out in China, but sometimes I would have to repeat those tests back at home and
    I would repeat those. Most of those tests, at least, since some of them required
    special equipment, which I did not have. There are also more specific tests like
    RF testing, which you need a special lab for, which, of course, I did not have
    either.
  sec: 360
  time: '6:00'
  who: Alvaro
- line: I can imagine that at some point, it becomes a bit repetitive. You basically
    need to run through the same checklist with a new firmware update, right? Then
    it's like “Okay, let me check the GPS again. Let me check this and that again.”
  sec: 420
  time: '7:00'
  who: Alexey
- line: Yeah, it was very repetitive. Sometimes you would get new tests, because new
    requirements would come in. For instance, we started working in ‘voice over LTE’
    back in Mexico, so we had to do new tests for voice over LTE. Stuff like that.
    New requirements needed new tests. But essentially, it was all testing and refinement
    of the previous tests.
  sec: 434
  time: '7:14'
  who: Alvaro
- line: 'Sometimes the most exciting things would be like, “Oh, we have to do this
    specific field testing, which is: get in a car, start a call, and then drive a
    specific route. You would pass the test if that if the call would not drop, essentially.
    You would also call the carrier – an engineer in the telephone company. They would
    record the actual test as well. They would get all the data and they would tell
    you whether you’ve passed or not. Sometimes those routes would change and it was
    like “exciting”. [laughs] But that''s pretty much it.'
  sec: 434
  time: '7:14'
  who: Alvaro
- line: I guess that's what made you decide at some point, “Okay, it's too repetitive.
    I want to quit.” Right? [cross-talk]
  sec: 490
  time: '8:10'
  who: Alexey
- line: It's more than that. But yeah. I mean, there were issues in the company –
    I was not satisfied with our output and how the company was developing. Lots of
    stuff. But yeah, the work itself was pretty repetitive. The people I worked with
    were very nice, but I did not enjoy that kind of work.
  sec: 498
  time: '8:18'
  who: Alvaro
- header: Transitioning from QA to Machine Learning
- line: And then you decided to quit. But then you also mentioned that you were unemployed
    for some time. So you just quit without looking back – without looking for the
    same type of job to continue. How did you find the courage to just leave?
  sec: 515
  time: '8:35'
  who: Alexey
- line: I cheated in a way. [chuckles] Luckily for me, I have a very strong family
    support system and I had a bit of money saved up. It was scary for me in the sense
    that I did not know what I wanted to do with my life yet. But I was not scared
    of “Am I going to eat tomorrow?” Or “Am I going to have a roof tomorrow?” That
    was not an issue. I quit and I went back to my family. They were very understanding
    and I started studying right away, after a month-long break or something like
    that. That was my longest vacation, sort of. [chuckles]
  sec: 530
  time: '8:50'
  who: Alvaro
- line: Then I started studying front-end, actually. I started looking into front-end
    development. Then I quickly realized that I did not enjoy that at all. I looked
    around at what I could study and then I fell upon machine learning, which I was
    interested in, and I joined a postgraduate degree course and I loved it. I really
    really enjoyed it. And here I am.
  sec: 530
  time: '8:50'
  who: Alvaro
- line: So you kind of knew that you wanted to work in IT? You mentioned frontend
    and then you kind of looked around at what else there was in the IT field and
    then you eventually ended up doing machine learning. Right?
  sec: 597
  time: '9:57'
  who: Alexey
- line: I mean, I wouldn't be opposed to work in a completely unrelated field. But
    I do not know anything about any other fields. [laughs] IT is what I know, essentially.
    IT is such a wide field, such a huge field that you can become specialized in
    a very specific thing and just perform a fulfilling career there, in that specific
    field. I did not feel like I would have to move because I felt like there was
    so much more to explore. So yeah, I didn't contemplate it at first.
  sec: 611
  time: '10:11'
  who: Alvaro
- line: Why machine learning? You mentioned that you were doing frontend and didn’t
    like it, and then you came across machine learning. So what did you like about
    it?
  sec: 651
  time: '10:51'
  who: Alexey
- line: It was challenging. I liked the math. It was pretty hard. But I felt like,
    “Wow! This is substantial,” because most of what I did before in QA, I did not
    really apply what I had learned back at school. I had never worked in software
    development before. I had never done anything of the sort. I was essentially writing
    Excel spreadsheets and that sort of stuff, which I did not enjoy.
  sec: 659
  time: '10:59'
  who: Alvaro
- line: When we started studying and we had to do the project for the course, I realized
    that I was having fun. [laughs] That's it, pretty much. I was already interested
    in artificial intelligence. Because I feel like there's so much more to do yet.
    I felt like this is a very wide field that I can grow in. I think it's worth diving
    in and studying it and getting good at it. That's it. There are so many more things
    that I'm interested in as well. But, you know – you can't do it all. So I chose
    to get into this and to do it properly. So that's it.
  sec: 659
  time: '10:59'
  who: Alvaro
- line: Sounds like you didn't really have a plan, right? You just went “Okay, I kind
    of like it. Let's see what’s there.” And you just explored this one step at a
    time. Or did you actually have some sort of plan?
  sec: 733
  time: '12:13'
  who: Alexey
- line: My plan was… Well, first I wanted to quit and I wanted to have time for myself
    – to get myself cleared out and figure out what I wanted to do with my life. Then
    I thought, “Well, I know I'm an IT kind of guy because that's what I know and
    I actually like it.” I'm interested in the field. I keep up with the tech news
    and everything. So I decided “Let's see what else there is.” I was pretty sure
    I did not want to do QA. I also did not want to do regular IT stuff, like sysadmin
    stuff.
  sec: 744
  time: '12:24'
  who: Alvaro
- line: I did summer jobs before when I was younger, and I didn't really enjoy it.
    So I started looking. I wanted to get into the more development stuff. When I
    tried out machine learning and I learned more about it, I realized the width of
    the field and how much there was left to do. I said, “Yeah, this is a really interesting
    field. I want to get into it.” So I did.
  sec: 744
  time: '12:24'
  who: Alvaro
- line: Okay. So can you tell us how exactly the journey looked like for you? From
    the moment you realized “This is interesting” to the moment you started looking
    for a job in this field.
  sec: 812
  time: '13:32'
  who: Alexey
- header: Gathering knowledge about ML field
- line: Sure. Before I joined any courses, before I started anything, I asked my friends.
    I keep in touch with a lot of university friends. Some of them are in embedded
    development, some of them are in machine learning, and some of them are in other
    similar fields. I just asked around, like, “What do you do? What kind of things
    do you do? Do you like it? Would you change something?” That sort of stuff.
  sec: 822
  time: '13:42'
  who: Alvaro
- line: A couple of friends, when they talked to me about machine learning, recommended
    things like “You should read a couple of books. Check this video out. And then
    probably join a course or two if you're interested in joining a proper course,
    but maybe not a full master's degree. I have a couple of recommendations here
    in Barcelona.” I said “Okay, thank you very much.” I looked at the materials they
    suggested and I joined the project course I was suggested, because the head teacher
    was a very famous guy in the University I studied in. So I joined it, and I loved
    it.
  sec: 822
  time: '13:42'
  who: Alvaro
- line: That was just one course right? It wasn't a degree.
  sec: 891
  time: '14:51'
  who: Alexey
- line: No, it wasn't a degree. It was one course. It was a five month long course
    – it was a pretty long course – but it was a postgraduate course. It's not a full
    degree. So I finished it and I said, “I should learn more. What should I do next?”
    The courses started in November or December and then finished in April/May. So
    I thought, “Well, I cannot join any course or any degree right now because it's
    the end of the school year. So what should I do?” Looking at my options and after
    talking about it with one of my buddies in the course, he suggested that I join
    a summer school course, which I did.
  sec: 895
  time: '14:55'
  who: Alvaro
- line: It's called Neuromatch Academy. It's a nonprofit association, which does these
    neuroscience conferences and they also do courses. It's meant for neuroscience,
    but they also have this one-month-long module for deep learning for neuroscience.
    Since I was looking for projects to build up my portfolio and to get more actual
    experience developing neural networks, I said, “Let's join it.” That was last
    summer. Not this year – last year. It was a pretty tough course. I liked it. I
    don't remember almost anything from it [chuckles] because it was neuroscience,
    which I don't know. I had issues keeping up, but it was interesting.
  sec: 895
  time: '14:55'
  who: Alvaro
- line: After that, another friend of mine who used to live in Berlin, suggested that
    I join DataTalks.Club and I said, “Oh, sure, I'll take a look.” And I joined the
    Machine Learning Zoomcamp, which I really enjoyed. Then I joined the Data Engineering
    Zoomcamp, which I also really enjoyed because it was a part of the equation that
    I had almost no knowledge about.
  sec: 895
  time: '14:55'
  who: Alvaro
- line: Then there was the Machine Learning Ops, which I had to drop out because I
    was already working and I could not keep up with everything. [laughs] But yeah,
    that's it. I did those three things after the postgraduate course. My goal was
    to build up my portfolio by doing projects, maybe joining Kaggle. [cross-talk
    about pronunciation] Perhaps doing a few of those, which I actually never ended
    up doing because I got hired before I had the chance to start.
  sec: 895
  time: '14:55'
  who: Alvaro
- line: So you didn't have a portfolio? I mean, apart from the course.
  sec: 1045
  time: '17:25'
  who: Alexey
- line: Yeah. Apart from my GitHub, which is my notes and things from the courses
    and the stuff from my postgraduate course as well. That's it. I did not have an
    actual portfolio. But, apparently, we’re in high demand. [chuckles] They’re trying
    to find as many people as possible to get to work right now. I guess I was lucky
    in that regard.
  sec: 1048
  time: '17:28'
  who: Alvaro
- header: Searching for an ML job (improving soft skills and CV)
- line: What was the most difficult thing for you? You did a postgraduate course,
    then you did summer school, then you did two Zoomcamps from DataTalks.Club and
    then you started looking for a job, right? Or when did you actually start looking
    for a job? At what point?
  sec: 1077
  time: '17:57'
  who: Alexey
- line: At the beginning of this year, perhaps. Besides the technical knowledge, like
    how to do actual machine learning, I actually had a few gaps about how to approach
    an interview, how to prepare your curriculum vitae – that sort of stuff. Soft
    skills that you need to actually get hired, which are not actually related to
    what you're supposed to work in. But those are hurdles that you have to pass anyway,
    if you want to get hired. I hired a coach and he helped me figure out stuff.
  sec: 1098
  time: '18:18'
  who: Alvaro
- line: He got me started on how to talk to people, how to not be confrontational,
    but at the same time, how to plant your feet in the ground and how to defend your
    interests. Also how to prepare my CV, because also CVs are becoming more… I actually
    showed you my CV and you said, “I prefer the kind of CV which is like a list of
    things,” which is what I used to have, but then my coach said, “Yeah, that's fine.
    But nowadays, most people don't want to actually look at a list of things because
    they have so many things to sort through – they want something visual, they need
    something visual.”
  sec: 1098
  time: '18:18'
  who: Alvaro
- line: Interesting. [chuckles]
  sec: 1183
  time: '19:43'
  who: Alexey
- line: Yeah. So I did my CV in a more visual manner. That sort of stuff. Anyway,
    I managed to find some opportunities, through some contacts as well, like “I'm
    looking for a job.” – “Okay. I have this guy who's interested. Let me talk to
    him and maybe you can get an interview.” – “Cool. Yeah.” I still applied through
    LinkedIn, but then I also got in touch with my contacts, got in touch with some
    more people, and I eventually started some processes. I started one process before
    I actually was serious with my coach. That did not go well because the person
    who interviewed me started asking pretty tough questions – things like, “So you
    have a data frame, but this data frame in pandas actually exceeds the memory size
    that you've got available in your system. What happens then?” And I was like,
    “I don't know, man. I guess it will crash or something, but I'm not sure what
    will happen then.” [chuckles] You know, that sort of low level stuff that I was
    not prepared at all to do. He told me, “Thank you for the interview, but you're
    in a very junior position and we were looking for someone more experienced.” And
    I was like, “Yeah, sure. Whatever. Thank you for the opportunity.” But that's
    it.
  sec: 1184
  time: '19:44'
  who: Alvaro
- line: Then I did a couple more processes. The two first ones were an interview in
    order to get to know the people and then I was supposed to do a technical exercise.
    The first one, after the exercise, I got rejected. They told me “Thank you, but
    we're not interested.” The second one, they actually made me an offer, but that
    was after I had done the third interview – the third process – which did not have
    a technical aspect beyond a few various questions that they asked me right there
    in the interview. They made me an offer in that third interview. And I said, “Sure,
    let's go for it.” But maybe if I had received the offer before I had done the
    third interview, I might have accepted it. So who knows? Maybe I would have been
    working for a different company right now. All of these companies, except the
    first process, which did not go well – but these three last processes were NLP-related,
    which is funny. It's interesting. Because I did not actually explicitly look for
    NLP projects. [chuckles] It's funny how that works.
  sec: 1184
  time: '19:44'
  who: Alvaro
- line: Did you actually have any NLP experience? In our Zoomcamps, we didn't cover
    that. [Alvaro agrees] Did you study this separately?
  sec: 1322
  time: '22:02'
  who: Alexey
- line: I did some NLP back in my original postgraduate course. I was familiar with
    it. I was not an expert, because actually the NLP part, I did not enjoy it as
    much as some of the other parts of the course. We had different teachers and the
    teachers we got for that part weren’t my favorite. But yeah, I did have some experience.
    It didn't come as something completely new for me.
  sec: 1333
  time: '22:13'
  who: Alvaro
- header: Data science interview skills
- line: We have a few questions. The first question is, “What kind of soft skills
    did you have to prepare for your data science interview?” You mentioned not to
    be confrontational and things like that, but what were these skills exactly? What
    did they look for and what did you need to prepare for?
  sec: 1358
  time: '22:38'
  who: Alexey
- line: I worked through that kind of stuff with my coach. The way we did it was with
    role playing exercises. If you have a friend or you know someone who would be
    interested in helping you out and maybe could play the part of being a tough interviewer
    and put things in a difficult manner to you, I think that would be a very cool
    exercise to do and to prepare for it. But essentially, it all depends on how you
    are. I'm the kind of person who… I don’t know how to sell myself to others. I
    undersell myself. I look at the stuff I do and I think “Yeah, I'm not very good
    at this.” But then I look at some other people's work and I realize, “Woah! This
    guy sucks. Maybe I'm not so bad at it.”
  sec: 1382
  time: '23:02'
  who: Alvaro
- line: But I still don't have the confidence, perhaps, to upsell myself in a way
    that is actually more objective compared to what the actual quality of things
    are. For me, one of the most difficult things was to actually not undersell myself
    – not being “Yeah, I'm not that good at this.” You cannot say that to someone
    who is interested in hiring you. But you actually do not want to lie either. I
    did not want to sell myself in a way that did not reflect reality. That was really
    tough for me.
  sec: 1382
  time: '23:02'
  who: Alvaro
- line: But your Zoomcamp projects were amazing. Your notes were excellent. [cross-talk]
  sec: 1475
  time: '24:35'
  who: Alexey
- line: My notes are fine. My projects – not so much. [cross-talk]
  sec: 1484
  time: '24:44'
  who: Alvaro
- line: Come on. They were good.
  sec: 1487
  time: '24:47'
  who: Alexey
- line: I mean, compared to some. Some people were amazing. Some people were like,
    “Wow! This is a very, very good project.” I think my project was average in both
    camps. But thank you very much for the compliment. I appreciate it. [chuckles]
  sec: 1488
  time: '24:48'
  who: Alvaro
- header: Zoomcamp projects
- line: Can you tell us about these projects?
  sec: 1497
  time: '24:57'
  who: Alexey
- line: The projects I did for the Zoomcamps?
  sec: 1502
  time: '25:02'
  who: Alvaro
- line: Yeah.
  sec: 1504
  time: '25:04'
  who: Alexey
- line: 'Oh, man… I don''t remember already. I forgot. [laughs] The first one was…
    wait, let me remember. Let me think. The project for the machine learning Zoomcamp
    was: I found a dataset, which was kind of fun – it was a speed dating dataset.
    That dataset had a lot of features, so many features. It was interesting because,
    what you had to do is – I believe that the target feature was whether they would
    match, essentially. But there were a few very dependent features from each other.'
  sec: 1505
  time: '25:05'
  who: Alvaro
- line: The exploratory data analysis step was of very high importance, specific for
    that project. I think that I could have improved – I could have done much more
    in that regard. But it was fun. It was a very fun project to do because it was
    something completely unexpected. It was very funny. I found that dataset by chance.
    For my second project… Was that the midterm project or was that the final project?
  sec: 1505
  time: '25:05'
  who: Alvaro
- line: I think that was the midterm.
  sec: 1577
  time: '26:17'
  who: Alexey
- line: Midterm, right? [chuckles] I cannot remember either. Let me take a quick look
    at my GitHub.
  sec: 1580
  time: '26:20'
  who: Alvaro
- line: Yeah, I think you've demoed the midterm project, right? If anyone is interested,
    we have a demo from Alvaro in the playlist, where he shows the project.
  sec: 1586
  time: '26:26'
  who: Alexey
- line: Oh, yeah! My second project was an image classification task. I had a dataset
    where it was a bunch of vegetables – I had fruits and vegetables. It was a very
    standard, run-of-the-mill, image classification project, I think. But I wanted
    to do something with deep learning, so that's what I chose. I think I wanted to
    do something else at first, but I did not have the time. I only had two weeks
    to turn in the project. I'm a very slow developer. That's another issue. [chuckles]
  sec: 1600
  time: '26:40'
  who: Alvaro
- header: Zoomcamp project deployment
- line: Another question we have is “Did you deploy your final projects in AWS?” What
    was your experience with this? Did you actually deploy them in the ML Zoomcamp?
  sec: 1636
  time: '27:16'
  who: Alexey
- line: I did deploy them, but not to AWS. I deployed them to Google Cloud, I believe.
  sec: 1649
  time: '27:29'
  who: Alvaro
- line: Google Cloud, okay.
  sec: 1653
  time: '27:33'
  who: Alexey
- line: Yeah, I used Google Cloud, both in my postgraduate course and then in the
    Zoomcamp, because I was already familiar with it and we were working with Google
    Cloud because they have a very generous credit when you start. 300 dollars or
    something. Yeah, it's very, very good.
  sec: 1654
  time: '27:34'
  who: Alvaro
- line: It's really enough for three months. Too bad it's just for three months, right?
    I could use them for way longer – like for a year.
  sec: 1673
  time: '27:53'
  who: Alexey
- line: I mean, you can do “my email account number one, my email account number two,
    my email account number three,” and then keep doing new accounts. [chuckles] So
    you can get those credits all the time. But yeah, it's not… I don't feel good
    doing that.
  sec: 1683
  time: '28:03'
  who: Alvaro
- line: So it wasn't AWS and it wasn't a problem for you? Right? You deployed everything.
  sec: 1696
  time: '28:16'
  who: Alexey
- line: No, it wasn’t a problem. We did use AWS during the course, because we used
    them to deploy TensorFlow, embedded in lambda and that stuff. The languages.
  sec: 1702
  time: '28:22'
  who: Alvaro
- line: So you used it as well? Or you did this in Google Cloud?
  sec: 1718
  time: '28:38'
  who: Alexey
- line: No. I did use it for the course. I followed the AWS steps for the course.
    But then my final project was in Google Cloud.
  sec: 1722
  time: '28:42'
  who: Alvaro
- header: How to not undersell yourself during interviews
- line: Interesting. So how did you solve this problem of not being able to sell yourself?
    The projects you just described look amazing to me. But then at the same time,
    there were people that had way cooler projects?
  sec: 1732
  time: '28:52'
  who: Alexey
- line: I mean, yeah. I remember when we had to do peer reviewing, I looked at some
    of the projects that I was assigned and I was like, “Wow! This is blowing my mind.
    It’s amazing.” And then some of them were like, “Yeah, this is fine. This is a
    good project.” But some of them were like, way ahead of the rest. Your question
    was how did I solve my issue of underselling myself?
  sec: 1747
  time: '29:07'
  who: Alvaro
- line: Yes. Or did you even solve it?
  sec: 1771
  time: '29:31'
  who: Alexey
- line: I still haven't solved it, I think. [laughs] But I'm working on it. I think
    I'm better at it. I'm still with my coach, and we recently did some exercises
    and he told me “You've made some progress with this. At the beginning, you would
    have crashed right away at the beginning of the interview. But right now you are
    standing your ground.” He commended me for it. So I'm still working on it, but
    I'm getting better.
  sec: 1773
  time: '29:33'
  who: Alvaro
- line: Essentially, you explain what you can do, but you don't try to make yourself
    humble nor prideful. So you’re just trying to state things in a more neutral way
    as possible and do not belittle yourself under any comment that the interviewer
    is telling you. That's essentially it.
  sec: 1773
  time: '29:33'
  who: Alvaro
- line: So it’s basically doing the same thing you just did when you described your
    projects, right? You said what the data set you used was, what the problem you
    were solving was, what kind of tools you used for solving this problem, right?
    [Alvaro agrees] You just give objective facts about the project without saying,
    “Oh, maybe this wasn't the best project I've seen.” You don’t mention that, right?
  sec: 1830
  time: '30:30'
  who: Alexey
- line: Correct. I would totally have said that. “This is not the best project. But
    you know…” I just did that, when I told you about the projects for the Zoomcamp
    – I undersold myself by telling you that it was a very run-of-the-mill project.
    Which I think it is, because it's just a very simple image classification problem.
    But at the same time, in an actual work interview, you shouldn't say that. You
    just say, “This is an image classification problem. I used these tools to solve
    it. And this is the task to solve.” And that's it. You let the interviewer make
    her own opinion about the project, rather than offering your opinion about it.
  sec: 1856
  time: '30:56'
  who: Alvaro
- header: Alvaro’s experience with interviews during his transition
- line: Were the projects of any use, actually, when you had interviews? Did anyone
    care about your portfolio? Did they ask you about the projects?
  sec: 1898
  time: '31:38'
  who: Alexey
- line: Actually, they didn't, [chuckles] which was very interesting. They were more
    interested in the technical exercises. I've talked about four interviews – four
    processes. The first one, which was just an interview that didn't go well. Then
    the middle two, which involved doing homework of sorts – they gave me some questions
    and I had to turn them in a week later. And the final interview, which also involved
    technical questions, but they were very simple and I got hired with them. For
    the last three – I was kind of surprised at the last interview because I thought
    that the questions they asked me were very simple. But they needed people and
    they hired me.
  sec: 1907
  time: '31:47'
  who: Alvaro
- line: The middle two processes, where I had a week to solve the problems they gave
    me – one of them was a bunch of hard questions and they told me, “You can look
    them up if you want to, but keep in mind that we'll do a follow-up interview and
    we'll ask you more questions, and you won't have the chance to look them up. So
    do whatever you feel like.” I was like, “Okay, sure.” So I tried to solve them
    all without looking anything up other than my specific notes that I had for my
    previous courses. I did have to look up a few things on Google, but then I just
    started them again, covering the Google results up. And that's essentially what
    I did. But then, that second interview never came. So I don't know what it could
    have been like.
  sec: 1907
  time: '31:47'
  who: Alvaro
- line: The second one was a project, essentially. They gave me a weather dataset
    – a time series, essentially – and they asked me to figure out how to predict
    weather in an approximate manner. It was a fun exercise, because I had never done
    anything with time series before. So it was fun. And that's it. For the process
    with the time series, that's the one company that actually made me an offer, but
    I rejected because I had a better offer from the other company.
  sec: 1907
  time: '31:47'
  who: Alvaro
- line: Did any of the interviewers care about your knowledge in cloud? Did they ask
    you about the cloud? Or it was just these questions that you mentioned?
  sec: 2041
  time: '34:01'
  who: Alexey
- line: The first one (the one that went badly) I believe that the interviewer asked
    me some cloud questions, but I honestly don't remember what they were. And in
    the last interview, they asked me if I was familiar with some of them, like, “Are
    you familiar with Azure?” And I said, “I haven't worked with Azure. But I have
    worked with Google Cloud on AWS before. Essentially, they're all similar. They
    just have their own specific quirks to each platform. But that's it.” I don't
    remember if there were any more specific questions, so no. But [cross-talk]
  sec: 2054
  time: '34:14'
  who: Alvaro
- line: So they just asked if you know cloud and you said “yes,” and they were satisfied
    with that.
  sec: 2090
  time: '34:50'
  who: Alexey
- line: Yeah, which is why I was surprised when I got the offer for the last interview
    because I thought “Is that it? You’re not asking anything else?”
  sec: 2095
  time: '34:55'
  who: Alvaro
- header: Alvaro’s Zoomcamp notes
- line: That’s how I also do it, to be honest. I don't know if it makes sense to go
    into the specifics of cloud. If you worked with a cloud, then okay. We have a
    comment. It's not a question but just a comment. “I am in the current cohort of
    the ML Zoomcamp. I always go back to Alvaro’s notes after finishing a week and
    revise what I learned in a week. Great notes.” I do fully agree. Maybe, in a way,
    your notes are like projects. You also mentioned that you were preparing for the
    hard questions – you were referring to your notes. I wanted to ask you – tell
    us your secret. How did you make these notes so good? What was your process?
  sec: 2102
  time: '35:02'
  who: Alexey
- line: Man… You probably won’t like what I'm going to say, but I'm actually not very
    happy with my notes. Because…
  sec: 2150
  time: '35:50'
  who: Alvaro
- line: '[chuckles] Underselling?'
  sec: 2158
  time: '35:58'
  who: Alexey
- line: No, no, no. This is actually not underselling. Let me tell you why. I think
    they are too wordy. I think they're not notes. I think they're more like a literary
    work, in a way. The way I approached them is almost like I'm trying to write a
    book, which is not what I intended to do, actually.
  sec: 2159
  time: '35:59'
  who: Alvaro
- line: You maybe can convert them to a book. [chuckles]
  sec: 2178
  time: '36:18'
  who: Alexey
- line: I don't know – I've never written a book before. But the thing is, notes are
    supposed to be something that you can refer to. It's like an extension of your
    brain, right? You don't remember a specific thing, but you know where to look
    for it and you go and look there. Then you remember everything.
  sec: 2181
  time: '36:21'
  who: Alvaro
- line: But in my latest notes, especially for the Data Engineering Zoomcamp, if you
    look at those – they are way too long in the sense that it's actually hard to
    go look for specific stuff in those notes because they are so long. I actually
    had to create indexes for each lesson because they were so long. Honestly, I'm
    not happy with them. I mean, I am happy with the content. I think I did a good
    job formatting them.
  sec: 2181
  time: '36:21'
  who: Alvaro
- line: I actually had a lot of fun doing them and I learned a lot. But they do not
    accomplish what they are supposed to do, which is being an easy and quick reference
    to go look for stuff.
  sec: 2181
  time: '36:21'
  who: Alvaro
- line: Like a second brain, right?
  sec: 2238
  time: '37:18'
  who: Alexey
- line: Yeah. It's actually something I'm very interested in but have not managed
    to explore. I know there are these tools like Obsidian and ReNote and all these
    amazing tools that are out there, which are used for scientific research and everything.
    I’d really like to dig into those but I honestly haven't had the time to learn
    how to approach it because they are a little complicated at first. There are a
    few concepts like settled casting and that sort of stuff if you want to look into
    it. But yeah, I just started writing in Markdown without any specific linking
    between sections.
  sec: 2239
  time: '37:19'
  who: Alvaro
- line: Then, with any gaps I could find like “This specific concept is such and such,”
    then I would add links to external pages if I thought they were meaningful in
    any way or could help me or someone else. But that's it. As for the process and
    how it went the way I work is – I actually really enjoy looking at online videos
    because you can pause them. I suck at listening and taking notes at the same time.
    A video is great because you can pause it at any time. You can listen for a little
    bit, then pause it and write down why you just listened to. If you didn’t catch
    something… [cross-talk]
  sec: 2239
  time: '37:19'
  who: Alvaro
- line: You have like two screens – on one screen you have the video and on another
    screen, you have your editor. Then you listen and you type. Right?
  sec: 2309
  time: '38:29'
  who: Alexey
- line: That’s it. I watch a little bit of the video, then I pause and then I go to
    my editing window (VS code) and I just write there. If there's something more
    visual or anything that I don't feel confident doing a diagram for, I just do
    a screenshot and then I copy/paste it in the notes – I just add a link to the
    picture and that's it. That's how I work, essentially.
  sec: 2319
  time: '38:39'
  who: Alvaro
- line: So yeah, listen a bit, pause, write down, go back then maybe think a little
    bit if something's not clear, watch it a couple more times. This is why it takes
    me so long to write the notes, especially in the data engineering Zoomcamp. It
    was a very dense course and there was so much content to go through. Luckily,
    I was not working, so I could spend all day long writing notes. [laughs]
  sec: 2319
  time: '38:39'
  who: Alvaro
- line: '[cross-talk] That''s your secret to the process, right? [chuckles] Be unemployed
    and just write down everything on the video. You said that you also did quite
    some research. If something is maybe not explained at all or not explained well,
    you would link like some other resource that explains this thing. It''s not just
    notes from the course, but also notes with some extra things from you.'
  sec: 2373
  time: '39:33'
  who: Alexey
- line: Yeah, because I wanted to understand why we were doing some things in a specific
    way. Sometimes I would have to expand the explanations in the videos with my own
    research, so that's what I did. However, in the Machine Learning Zoomcamp, at
    the beginning, my notes were very short because they were more like actual notes.
    It was basic stuff that I already knew, so I didn't feel the need to write notes
    for those things. I actually split the content of the notes between the actual
    notes and GitHub gists, which are – if you are not aware of those, for anyone
    who's listening in – it's this part of GitHub that allows you to put actual snippets
    of code and stuff like that. But they're not actually attached to any repo.
  sec: 2405
  time: '40:05'
  who: Alvaro
- line: It's just there and I thought, “I can do some cheat sheets and stuff like
    that.” And I would split writing notes between the gists and the notes. Some of
    the gists are good. I use the GitHub gists and the Conda gists. I used them all
    the time – those gists are great for me. But others I did – I did another one
    for Python, which I never use because it sucks. It's faster and better for me
    to just look up something for Python or pandas or SciPy or anything.
  sec: 2405
  time: '40:05'
  who: Alvaro
- line: You mean look up on Google, right?
  sec: 2488
  time: '41:28'
  who: Alexey
- line: Yeah. Looking it up in Google is actually faster than actually looking at
    the gist.  My way of writing notes keeps evolving. It was a continuous experiment,
    in a way.
  sec: 2490
  time: '41:30'
  who: Alvaro
- line: Was it actually useful for you, personally? We as the community do appreciate
    it, because it helps to go back to them after the videos. But for you, personally
    – looking back now, was it useful for you?
  sec: 2503
  time: '41:43'
  who: Alexey
- line: Oh, yeah. They were very useful. They are not super useful in the specific
    way that notes are supposed to be, which are, as a quick reference to things.
    However, the process of building those notes was super helpful for me because
    when you actually write down stuff and you have to think of how to explain those
    things, it actually helps the ideas and the content to remain in your memory.
    In that regard, they were extremely helpful. Yeah. Keep in mind that if you ask
    me for anything specific from the notes, I will probably not remember because
    my memory is not that great, but I will go “Oh, yeah. This was written in that
    part. So I can go check it out online and go look it up.”
  sec: 2518
  time: '41:58'
  who: Alvaro
- line: Actually, you know what? When somebody asks questions now about ML Zoomcamp
    and I think, “OK, in which video was it?” and then I will go to your notes. [chuckles]
  sec: 2563
  time: '42:43'
  who: Alexey
- line: '[laughs] It''s actually something that I do too. Videos are great for explaining
    stuff, but if you want to look something up quickly, they''re not so good. You
    have to scrub through the video to actually find the point where people are talking
    about something specific. People started adding those timestamps in the videos,
    which are super helpful. But it''s still faster to view some reading material.
    It''s better if you look at the video first, and then once you read it, then you
    can have some written reference, which is much faster than going back to the video.'
  sec: 2575
  time: '42:55'
  who: Alvaro
- header: Alvaro’s coach
- line: There is a comment, “Why do you think you're not a good communicator? I'm
    listening to you now and you're great.” [chuckles]
  sec: 2613
  time: '43:33'
  who: Alexey
- line: Thank you.
  sec: 2622
  time: '43:42'
  who: Alvaro
- line: I guess the coach also helped as well. [Alvaro laughs] Do you think having
    a coach in a situation like yours is important? Would you be able to do this without
    a coach?
  sec: 2613
  time: '43:33'
  who: Alexey
- line: I might. Yeah. I think it was good. I could afford it and I thought, “Why
    not? It's going to be a faster way than doing it by myself.” But probably you
    can do it on your own. Maybe you can find some self-help books or anything that
    takes you. I actually have a couple that I can recommend that I should read. I
    still haven't had the time – how to talk to people, how to negotiate, and stuff
    like that.
  sec: 2635
  time: '43:55'
  who: Alvaro
- line: We actually have some pending exercises with my coach, actually,  on how to
    negotiate for a pay raise, which we haven't done yet [chuckles]. That's going
    to be critical for my future if I want to earn more money. [laughs] But is it
    important or mandatory? No, I don't think so. It all depends on how you are and
    what resources you've got. It's on a case-by-case basis, I believe.
  sec: 2635
  time: '43:55'
  who: Alvaro
- line: There is also a question about the coach, “Did the coach (your specific coach
    in this case) give any input on dealing with the hiring process, or was it more
    about soft skills and stuff like that?”
  sec: 2690
  time: '44:50'
  who: Alexey
- line: Sorry, can you repeat the question again? [cross-talk]
  sec: 2709
  time: '45:09'
  who: Alvaro
- line: Yeah, maybe I'll rephrase it in the way that I understood it. “Was the coach
    specifically helping you with hiring for a data science position, or was it more
    like a communication coach to help you with soft skills?”
  sec: 2711
  time: '45:11'
  who: Alexey
- line: It was both. He did help me to actually target... He knows that I'm an aspiring
    data scientist and that I wanted to work in machine learning. But the coach does
    not know anything about machine learning. Everything he knows about it, he's learned
    from me or by some other of his clients. He knows computer stuff – he studied
    computer engineering as well. He's been working in this kind of field for so long
    that he hasn't kept up with this specific field.
  sec: 2728
  time: '45:28'
  who: Alvaro
- line: Most technical interviews are going to be essentially similar. The technical
    stuff changes between them, obviously, because they're different fields but the
    way you approach people and the way you talk to people and how you should prepare
    for them is very similar, I believe, between all of them. At least I'm not aware
    that you should approach an interview in a different manner, depending on what
    kind of field you're working on. Honestly, I don't think so.
  sec: 2728
  time: '45:28'
  who: Alvaro
- line: We did work on specifics in machine learning in the way that I would tell
    the coach what I think is interesting about machine learning and what I think
    the potential is and stuff. He told me “Oh, then in that case, if this is your
    opinion, then this is how you should explain it to the interviewer, because that
    will give the interviewer a better view of who you are.” That sort of stuff. But
    the specifics of interviewing are just generic, I think.
  sec: 2728
  time: '45:28'
  who: Alvaro
- line: So it was more about how to approach the hiring manager interview, around
    how to answer behavioral interview questions. [Alvaro agrees] But not how to answer
    “What's the difference between random forest and XGBoost?”
  sec: 2836
  time: '47:16'
  who: Alexey
- line: Yeah. The coach is unable to help me with that because he doesn't know that.
    That falls on me. [chuckles] I'm the one who's supposed to know that.
  sec: 2849
  time: '47:29'
  who: Alvaro
- header: The importance of mathematical knowledge to a transition into ML
- line: Do you think knowing these mathematical or implementation details is important
    for the interview process – for passing the interview process for a data science
    position?
  sec: 2859
  time: '47:39'
  who: Alexey
- line: It depends on what your role is, what you're being hired for, and obviously,
    the kind of person who interviews you. For instance, just today I got an email
    from one of the people that’s working right now on my project, and this guy did
    an analysis. He's been testing different neural networks for about two months
    right now. We gave him our model and he took a look at it and analyzed it. He
    essentially deconstructed and reconstructed it and he gave us all the specifics
    of the neural network. That's amazing. It's going to be very helpful for our project.
    So knowing the ins and outs – the very specifics of machine learning or the implementation
    side of things – can be useful, for instance, in this specific aspect. But on
    the kinds of things I do right now, which I'm more of a managing role, essentially.
  sec: 2871
  time: '47:51'
  who: Alvaro
- line: I also have to do some technical stuff, but honestly, much less than I was
    expecting. That is not so important because I'm working with people who already
    know how to do so. So it all depends, I think, on what you want to do and what
    you're being hired for. Sometimes, I think a very hard part of this is you are
    not exactly quite sure what you're being hired for or what the person who's interviewing
    you expects from you. That can be a handicap. But yeah, it can be useful to know
    these things.
  sec: 2871
  time: '47:51'
  who: Alvaro
- header: Preparing for technical interviews
- line: I actually wanted to talk about what you do at work right now, but we have
    so many questions. We can just go with the questions. The most upvoted question
    we have is “How to prepare for technical questions in an interview other than
    portfolio projects?” Taking notes or what?
  sec: 2972
  time: '49:32'
  who: Alexey
- line: Honestly, whatever works for you, man. [laughs] Sorry, I think I saturated
    the mic. Preparing for technical questions is such a hard thing to do because
    you cannot know what you're going to be asked unless you know what you're being
    hired for. For instance, if the company that's going to hire you works in NLP
    projects, then it makes sense to study NLP specifically. What's NLP? What does
    it entail? What kind of tasks do you solve? How do you approach those tasks? Whatever.
  sec: 2995
  time: '49:55'
  who: Alvaro
- line: But sometimes you don't really know what to do. It all depends what kind of
    technique you are most comfortable with when studying – taking notes from videos,
    that's fine. Reading your past notes, which is what I did. Doing some exercises,
    building up your portfolio is also good, because not only do you have something
    to show, but those skills are also being ingrained into your brain when you carry
    out those projects. So it depends on how you want to approach those. Whatever
    works for you, honestly.
  sec: 2995
  time: '49:55'
  who: Alvaro
- line: Even though they didn't specifically ask you about these projects, it was
    still useful for you to master the skills, right?
  sec: 3060
  time: '51:00'
  who: Alexey
- line: Right.
  sec: 3066
  time: '51:06'
  who: Alvaro
- line: But I guess it's pretty unusual. Maybe they just didn't ask you about them
    but they did look at them. Everything is public on your GitHub. Maybe they just
    went through this and just didn’t ask. [cross-talk]
  sec: 3068
  time: '51:08'
  who: Alexey
- line: Yeah, they did ask me some things. In the company I work for, actually, the
    two people who hired me are not working for the company anymore, which is kind
    of funny. But I was asked a few technical questions. They were just very simple,
    like, “If you have this kind of task, how would you solve it?” And I would do
    a very high level approach to the task. That sort of thing. But nothing super
    specific and there were no coding exercises in this particular instance. In those
    previous processes, I had to turn in code. So it all depends.
  sec: 3080
  time: '51:20'
  who: Alvaro
- header: Alvaro’s typical workday
- line: Can you tell us what your typical work day looks like?
  sec: 3113
  time: '51:53'
  who: Alexey
- line: Sure. I read e- mail [laughs] A bit of it. And I also check out Teams, when
    my computer decides to run it because holy crap – Teams is such a hog.
  sec: 3118
  time: '51:58'
  who: Alvaro
- line: You're on a Mac, right?
  sec: 3133
  time: '52:13'
  who: Alexey
- line: Right now I'm on a Mac, but my work computer is a PC.
  sec: 3134
  time: '52:14'
  who: Alvaro
- line: So it’s Windows. And it doesn’t run Microsoft Teams?
  sec: 3139
  time: '52:19'
  who: Alexey
- line: It only had (only!) eight gigs of RAM, which I thought was not enough. Then
    I recently upgraded to 24 gigs of RAM, which is amazing. Right now I think I can
    finally run Teams properly. [chuckles] But yeah, my usual day. Right now I'm in
    charge of a project. What I do is, I've set up a way of managing it. I've got
    an Excel sheet. I've also got Microsoft Planner, which is a Trello-like thing
    that is included with Office. It also integrates well with Teams, so it's good
    because you're in your specific team and then there's a tab with the tasks there,
    which is great.
  sec: 3142
  time: '52:22'
  who: Alvaro
- line: Right now there's only two of us, it's only me and some other guys, so we
    divide what we want to do. We work from home and each one of us works on a specific
    thing and then at the end of the day or halfway through the day, we update each
    other on what we've done. And that's it. For instance, back in April/May that
    was the zenith of the project – the point with the most development going on.
    There were five of us and each one was coding different stuff. We had to agree
    on what had to be done, and then we had to agree on the tasks. So that's essentially
    it.
  sec: 3142
  time: '52:22'
  who: Alvaro
- line: It's more of a project management kind of thing than actual machine learning.
    There's less of us right now – there's only two people – and we'll have a third
    person coming soon, but not yet. So I also have to do some more technical stuff.
  sec: 3142
  time: '52:22'
  who: Alvaro
- header: Alvaro’s team’s tech stack
- line: What kind of tech stack do you use?
  sec: 3252
  time: '54:12'
  who: Alexey
- line: Right. We are on Azure. Well, more like our client works with Azure, so we
    make use of the resources of the client. All of our code is in Python. We use
    Python and also Keras, which is a library (if you don’t know) where you set up
    your dataset, you set up a task, and AutoKeras will look for the best model for
    you. So it's like everything is done for you pretty much automatically. You do
    have to fine tune things, but essentially, that's what we did.
  sec: 3255
  time: '54:15'
  who: Alvaro
- line: Then we run those scripts – those Python scripts are being run on Databricks
    cluster, and we orchestrate those scripts with something called Azure Data Factory,
    where you design your DAX – which is essentially your work. You create your workflows
    on Azure Data Factory, so when something's triggered, then it calls a specific
    script, which then calls another script and that sort of stuff. Everything's written
    to a SQL database. Pronounced like “sequel”. Sorry, I'm used to saying the spelling.
    It's supposed to be SQL (sequel) in English.
  sec: 3255
  time: '54:15'
  who: Alvaro
- line: Is it? Like sequel? I think both work, right? I hear both options.
  sec: 3328
  time: '55:28'
  who: Alexey
- line: Okay, then whatever. SQL or sequel, whatever. [chuckles] Yeah, Microsoft SQL
    database on Azure. That's where all the data is being kept. It’s a stack that
    the developers were more familiar with, so that's what we went with. The project
    was supposed to be delivered in September and we had to deliver our first prototype
    in June, which was a shock. We had to speed up the process by three months. Right
    now we're extending it. We're adding more new stuff. But yeah, it's been a challenge.
    [chuckles]
  sec: 3335
  time: '55:35'
  who: Alvaro
- header: The importance of a technical background to transitioning into ML
- line: For somebody who wants to go through the same process as you – somebody who
    doesn’t necessarily come from a very technical background. I don't know how technical
    your background was, but I guess… forgive me if I'm wrong, but my interpretation
    of what you did is that it does not require a lot of technical expertise. Sorry,
    I don't mean to offend you.
  sec: 3371
  time: '56:11'
  who: Alexey
- line: It did require some but I know what you mean. Please go ahead.
  sec: 3397
  time: '56:37'
  who: Alvaro
- line: The question is – for somebody who wants to follow your path, maybe not necessarily
    from a less technical background or a more technical background, how do they do
    this? What would your recommendation be in this case? Would you suggest they just
    leave and spend two years being unemployed and take courses, and take notes? [chuckles]
  sec: 3404
  time: '56:44'
  who: Alexey
- line: That's what works for me, but it all depends on what works for you. I do have
    a technical background because I did computer engineering and science whatever.
    I studied that, even though my actual work was not as technical. I did have to
    know how to do some stuff. I had to read all these Google documents, which explained
    what the homologation process was and what the requirements were. I had to know
    what kind of modifications were not supposed to be done on the phone in order
    to pass those tests. So it did require some knowledge about how Android is layered
    and that sort of stuff. But I don't believe that you need a technical background
    in order to work in this field, but it helps a lot. I mean, it all depends on
    what kind of role you want to do.
  sec: 3425
  time: '57:05'
  who: Alvaro
- line: If you want to be an actual data scientist, like working in most of the high-level
    stuff, like experimenting with models and such, it helps a lot to have a mathematical
    background, because that's all very theoretical, in a way. There's lots of research
    going on and lots of new stuff is coming out all the time. So it really helps
    a lot if you have a mathematical background there. Actually, in my company, my
    colleague right now, he's a mathematician – he studied mathematics. There are
    quite a few mathematicians in the company.
  sec: 3425
  time: '57:05'
  who: Alvaro
- line: However, on the other side, if you want to do the actual data engineering
    part – if you want to actually do things like being very good at Spark, or you
    want to be very good at Kafka, or you want to be very good at any of the tools
    that are being used in machine learning workflows – then you don't need such a
    technical background, because it's all about knowing the tool and learning how
    to use it. I believe that you can come from any particular background and work
    on that.
  sec: 3425
  time: '57:05'
  who: Alvaro
- line: However, it helps if you have some technical background because then you already
    know all the high concepts and when you have to change to another tool – sure,
    you have to learn new stuff but it won't come in a weird manner to you. If you
    are learning Docker, you can use Docker. Fine, and now you have to use Kubernetes.
    Okay, then I'm learning Kubernetes. But if you know what a Linux kernel is and
    how it relates to the underlying utilization, or sandboxing parts of stuff, it
    helps to understand why some things work the way they do. But they're not entirely
    necessary. So on that part of things, I think that you don't need a technical
    background for it. So it depends on what you want to do.
  sec: 3425
  time: '57:05'
  who: Alvaro
- line: The way I understood you – you already knew how to program, right? [Alvaro
    agrees] This is something you studied in university with you computer science
    degree but [cross-talk]
  sec: 3591
  time: '59:51'
  who: Alexey
- line: I did lots of Java. Which… Java sucks. Sorry. [laughs]
  sec: 3600
  time: '1:00:00'
  who: Alvaro
- line: Yeah, but it's quite easy to pick up Python after any programming language.
    So if you have experience with any programming language, be it Java or C++ or
    whatever – JavaScript – then just starting Python should be easy. For you, I guess,
    that was the case.
  sec: 3604
  time: '1:00:04'
  who: Alexey
- line: Python was really easy. There are some quirks to Python, like the way you
    do iterations in loops, which is quite unique, I believe. But programming in Python
    is a joy. It’s very, very easy.
  sec: 3626
  time: '1:00:26'
  who: Alvaro
- line: Alvaro’s CV
  sec: 3626
  time: '1:00:26'
  who: Alvaro
- line: Okay. There is also a request if people can have a look at your CV. Maybe
    you can have a stripped down version. Maybe not right now. If you want to show
    it right now, okay. It will be an exclusive. We will not include this in the audio
    version, so maybe you can also send us a link that we can include to the audio-only
    version.
  sec: 3640
  time: '1:00:40'
  who: Alexey
- line: Sure. Let me copy the CV and post it to a Dropbox folder.
  sec: 3665
  time: '1:01:05'
  who: Alvaro
- line: Okay, that's awesome.
  sec: 3677
  time: '1:01:17'
  who: Alexey
- line: '[Discussing sending the file with Alexey]'
  sec: 3680
  time: '1:01:20'
  who: Alvaro
- line: It's not the best CV. There are lots of ways you can do a CV. I just went
    to Canva – it's a website for graphic design. I found a template I liked and I
    modified it to my needs. That’s it.
  sec: 3716
  time: '1:01:56'
  who: Alvaro
- line: Okay, the link is in the live chat and I will also put it in the description.
    If you watch it in replay, you will see this. And I think that's it for today.
    I want to thank you for joining us today, for sharing your experience, for telling
    us about your career journey. Thanks for being here. And thanks, everyone, for
    asking your questions.
  sec: 3731
  time: '1:02:11'
  who: Alexey
- line: Thank you very much, everyone. And thank you, Alexey, for having me.
  sec: 3755
  time: '1:02:35'
  who: Alvaro
- line: Have a great weekend!
  sec: 3759
  time: '1:02:39'
  who: Alexey
---

Links:

* [Alvaro's CV](https://www.dropbox.com/s/89hkt3ug0toqa2n/CV%20nou%20-%20angl%C3%A8s.pdf?dl=0){:target="_blank"}
* [Github profile](https://github.com/ziritrion){:target="_blank"}
* [LinkedIn profile](https://www.linkedin.com/in/alvaronavas/){:target="_blank"}
