---
title: "What I Learned After Interviewing 300 Data Scientists"
short: "What I Learned After Interviewing 300 Data Scientists"
guests: [olegnovikov]

image: images/podcast/s03e04-interviewing-300-data-scientists.jpg

season: 3
episode: 4

ids:
  youtube: AYi7b-8GPm4
  anchor: What-I-Learned-After-Interviewing-300-Data-Scientists---Oleg-Novikov-e10ctbs

links:
  youtube: https://www.youtube.com/watch?v=AYi7b-8GPm4
  anchor: https://anchor.fm/datatalksclub/episodes/What-I-Learned-After-Interviewing-300-Data-Scientists---Oleg-Novikov-e10ctbs
  spotify: https://open.spotify.com/episode/406wN6xDkYPyLS8i9fUJL5
  apple: TODO

transcript:
- line: "This week we will talk about the interview process, getting hired as a data\
    \ scientist \u2014 and not only data scientists. We have a special guest today\
    \ \u2014 Oleg. Oleg worked as a data science manager at Uber, where he built data\
    \ science teams. He also has experience building several startups in Europe. Recently\
    \ he created NextRound which is a free service for practicing interviews, receiving\
    \ personalized feedback, and learning materials. Welcome!"
  sec: 76
  time: '1:16'
  who: Alexey
- line: Glad to be here! Thank you for having me.
  sec: 107
  time: '1:47'
  who: Oleg
- header: "Oleg\u2019s background"
- line: "Before we go into our main topic of recruitment and interviews, let\u2019\
    s start with your background. Can you tell us a bit about your career journey\
    \ so far?"
  sec: 110
  time: '1:50'
  who: Alexey
- line: I started as a software engineer. I was building websites for a few years.
    Then at some point I heard about the Netflix prize. It was one of the first open
    data science competitions, a few years before Kaggle. I got so engaged in this
    topic of personalization that I ended up pursuing a PhD about recommenders. Then
    I transitioned from an engineer to an analyst in a startup. Eventually I became
    a manager. I led a team of data scientists, product analytics, and engineers working
    on a recommender engine, and building the data infrastructure in that company.
  sec: 120
  time: '2:00'
  who: Oleg
- header: Standing out in recruitment process
- line: "After that I wanted to apply for another data science job in a startup called\
    \ Lyst. I thought I am probably not the most experienced data scientist applying\
    \ for the job. I also needed the visa. I just began brainstorming. How do I make\
    \ myself stand out, so they don\u2019t reject me right away. I don\u2019t even\
    \ get to talk to anyone from the company. I try to reverse engineer the process\
    \ and think about it. When someone applies for a job in my team, what do I do?\
    \ What do I look at in CVs? What are the signals that I am trying to get? Usually\
    \ when you look at someone's CV, it says \u201Cexperience in Python\u201D. It\
    \ doesn\u2019t really tell you much. It\u2019s very subjective. Maybe the person\
    \ read a blog post about this or invented the language \u2014 you never know.\
    \ So, I thought \u201COkay, I need to stand out from the other candidates. And\
    \ I also need to somehow demonstrate that these buzzwords in my CV \u2014  machine\
    \ learning, big data, Python \u2014 are actually something that I am familiar\
    \ with\u201D. This was an E-commerce website and they were hiring for a data scientist\
    \ to improve their recommender agent."
  sec: 162
  time: '2:42'
  who: Oleg
- line: "And I thought \u201CI need to make something different\u201D. So, instead\
    \ of sending a CV, I wrote a blog post about how I would improve the recommender\
    \ engine if I worked there. Since I did not work there, I did not have any data.\
    \ I had to be creative. I took a list of brands that they were selling on this\
    \ website, and I wrote a very simple Python script that gets a list of their followers\
    \ from Twitter. Then I implemented a very simple recommender algorithm in Python.\
    \ It lets you type your Twitter nickname and then you will get recommendations\
    \ based on who you follow. The model was trained on these designers that are being\
    \ sold by this website. So, I wrote this blog post, sent it to them. What I had\
    \ in mind was \u201CI want to show that I understand the very basics of machine\
    \ learning. I can program a little bit\u201D. Essentially, to demonstrate the\
    \ very first chapter of any machine learning book. I sent it to them. Surprisingly\
    \ it worked out and I got the job."
  who: Oleg
- line: "Was it a public post? Did you just publish it on \u201Ctowards data science\u201D\
    \ Or you sent a document to them?"
  sec: 313
  time: '5:13'
  who: Alexey
- line: "I put it on medium but I put it down afterwards. I didn\u2019t know how much\
    \ of it could be public. Even though I used only data accessible everywhere, I\
    \ tried to do a little bit of reverse engineering, like what kind of data is being\
    \ sent from the website, what kind of APIs they are using and so on. So, I put\
    \ it down. At some point there was an article about this from the other side \u2014\
    \ by the recruiter who hired me. It explained this hiring experience from there.\
    \ That was very interesting to it. This is how I got that job. I focused on deployment\
    \ of machine learning models, personalization ranking and a little bit of data\
    \ engineering and scaling the data infrastructure."
  sec: 319
  time: '5:19'
  who: Oleg
- line: After it I joined Uber in Amsterdam as a product data scientist. In a couple
    of years I became a manager again. I led a team of data scientists that worked
    on forecasting models. The goal was to predict the lifetime value of a user and
    quantify the impact of different events on user behavior.
  who: Oleg
- header: "NextRound \u2014 a service for free mock interviews"
- line: "Every time I applied for a job in data science, there was one thing that\
    \ I really hated \u2014  when you get rejected. When you read this rejection email\
    \ and it tells you nothing. You spend hours interviewing, you spend hours working\
    \ on a take home assignment. And then you get some generic standard rejection\
    \ email. Maybe you even get some feedback. But usually it\u2019s completely useless\
    \ and not actionable. You cannot do anything out of it. So, I began to think \u201C\
    What can be better? How can I make this better?\u201D"
  sec: 398
  time: '6:38'
  who: Oleg
- line: "I ended up building a free service where you can practice data science interviews\
    \ with a chabot. Then you will receive detailed personalized feedback based on\
    \ your answers with some links to relevant materials to the topics where you can\
    \ improve. This is what I have been working on in the past few months. You can\
    \ check this out. I have mock interviews for data scientists and product analysts.\
    \ So far there have been little over 500 interviews. This is an interesting experience\
    \ \u2014 just to analyze and calibrate the questions. There is never a correct\
    \ answer. There is an infinite number of correct answers. If you ask some case\
    \ study questions about \u201Chow would you build this kind of model?\u201D I\
    \ keep getting surprised in a positive way every day because you never know what\
    \ to expect."
  who: Oleg
- header: Why rejections are generic
- line: "These are rejections that you got. Do you have any idea why they are genetic?\
    \ I think I have some ideas, also being a hiring manager sometimes. But, do you\
    \ have some ideas why these rejection letters are generic? Why can\u2019t companies\
    \ give feedback?"
  sec: 509
  time: '8:29'
  who: Alexey
- line: "There can be many reasons. First of all, I do not know if we can call it\
    \ laziness. But, let\u2019s say, to hire one person you need to interview 20.\
    \ This is realistic. This can be higher or  lower. To provide detailed excellent\
    \ feedback to everyone, it will take some time. Then this is really up to you\
    \ whether you think it is worth it or not. I think it is worth it. Why knows,\
    \ maybe these people join your company. It\u2019s always a closed loop. There\
    \ are not so many data scientists in the world or in a given city. Apart from\
    \ spending time on it, another reason can be just being polite. When you try to\
    \ provide some constructive actionable feedback to a person, you don\u2019t know\
    \ how they will react to this. You try to be polite and it brings you to some\
    \ very standard, some generic feedback that doesn\u2019t really pinpoint you into\
    \ any certain weaknesses. There might be some legal reasons about this as well.\
    \ What was your experience? What are your ideas?"
  sec: 530
  time: '8:50'
  who: Oleg
- line: "Basically what you said. I didn\u2019t think about being polite, I think\
    \ candidates actually are looking forward to receiving feedback. I did not think\
    \ about this angle, maybe I should have. think, the first one is time. Then the\
    \ second is legal. You cannot always give you back because of some legal stuff."
  sec: 611
  time: '10:11'
  who: Alexey
- header: "Starting NextRount \u2014 preparing a list of situations"
- line: "Okay, so you decided, \u201CI hate not receiving feedback, let\u2019s create\
    \ a website where people can practice and receive feedback after?\u201D"
  sec: 641
  time: '10:41'
  who: Alexey
- line: "Yeah. I began thinking of my experience as a hiring manager. What can I offer?\
    \ I wrote down a list of situations that kept happening from company to company,\
    \ from team to team. For example, as a data scientist or an analyst, you are always\
    \ balancing between working on some important model and stakeholders, asking you\
    \ to work on some urgent fixes or urgent ad-hoc analysis. Or you are running an\
    \ A/B test and then you see that some of the metrics improved and some of the\
    \ metrics actually got worse. What do you do? I started writing down a list of\
    \ situations that happened in my life that required some thinking. That was generic\
    \ enough to apply to any company. Then from these situations, from these case\
    \ studies, I created an interview plot. It introduces you to some context, \u201C\
    You are working in this company, your goal is to do this, and a stakeholder comes\
    \ to you and asks you to work on this. What do you do?\u201D"
  sec: 655
  time: '10:55'
  who: Oleg
- line: "Depending on your answer, it will ask you different follow-up questions.\
    \ Maybe switch a topic. Maybe go in depth to get more technical. I reached out\
    \ to about 30 data science hiring managers to get their feedback on these interview\
    \ questions that I prepared. So that it\u2019s not completely biased by my personal\
    \ experience. I got a lot of very interesting feedback from them. Then I just\
    \ published this website. So far so good, everyone likes it."
  who: Oleg
- line: "You said you had 500 interviews. The title for this event today is \u201C\
    what I learned after interviewing 300 data scientists\u201D. We need to update\
    \ it to 500."
  sec: 781
  time: '13:01'
  who: Alexey
- line: Well... these are not interviews, but practice interviews. But then it is
    the same thing.
  sec: 792
  time: '13:12'
  who: Oleg
- header: Steps in the interview process
- line: "Speaking of interviews. I imagine you did quite a few interviews \u2014 at\
    \ least 300. How does a typical interview process look like? What are the steps\
    \ in this process?"
  sec: 804
  time: '13:24'
  who: Alexey
- line: "There is no standard here. It really depends on the company, on the size\
    \ of the company. Usually, after you send your CV, a recruiter checks if your\
    \ experience matches the job description. Then they might have a call with you\
    \ and ask a few things about your experience that weren\u2019t clear from your\
    \ CV \u2014 to make sure that your experience is relevant to a certain role in\
    \ the company. The recruiter might also ask you a few questions about the salary\
    \ expectations and your availability for the new job. After that, if your experience\
    \ seems relevant to this job, some companies will send you a take home assignment.\
    \ Expect to spend a few hours on that. After that, there will be several rounds\
    \ of interviews. One of them will be with the hiring manager \u2014 and most of\
    \ the times you get to speak with the actual manager. After the interviews, there\
    \ will be a debrief when the hiring manager and everyone who interviews you will\
    \ discuss your experience and make the final decision. You will either get a job\
    \ offer or receive this generic rejection email."
  sec: 818
  time: '13:38'
  who: Oleg
- line: You mentioned the CV screening by the recruiter, home assignment and then
    a bunch of technical interviews. What kind of technical interviews are there?
    I imagine data scientists should be developers. They should be able to code. I
    guess one of these interviews checks coding, right? What else?
  sec: 904
  time: '15:04'
  who: Alexey
- line: "It really depends on the role. I even tried to visualize different types\
    \ of job profiles. I took random 50 data science jobs and I found a lot of data\
    \ science jobs that have literally nothing in common. It\u2019s so generic. Data\
    \ science is just an umbrella term that includes machine learning engineers and\
    \ product data scientists. On one side there is an expectation that you will code\
    \ a lot, you will be building and deploying machine learning models that work\
    \ in production. On the other side, the expectation is that you will be running\
    \ A/B tests and writing a lot of SQL \u2014 being more of a PM who is very confident\
    \ working with data."
  sec: 929
  time: '15:29'
  who: Oleg
- line: "So, technical interviews will depend on the role. On the high level, whichever\
    \ company you interview, at some point they will ask you about your previous experience.\
    \ It might be a question, like \u201CTell us about some model that you built in\
    \ the past and that you are proud of\u201D. At some point, most likely you will\
    \ be asked about some hypothetical case study. Very often, this is just a very\
    \ vague and generic question like \u201CHow would you predict user journey?\u201D"
  who: Oleg
- header: Read the job description!
- line: Okay. So, a product data scientist is somebody who is more an analyst, and
    a machine learning engineer is an engineer. And there is a whole spectrum of things.
    You need to look at the actual job description to figure out what exactly to expect
    during the process. Right?
  sec: 956
  time: '15:56'
  who: Alexey
- line: 'That is the main advice in general. We can stop this podcast right here.
    The main advice is to study the job description. Learn as much as you can about
    the role. Try to match your experience with the role. Say, you have two years
    of experience: for one year you worked as an accountant, for the second year you
    worked as a machine learning engineer. You are applying for machine learning engineering.
    Will you dedicate as much time to your accounting experience as to machine learning
    engineering? No. If you have to put a year of your work experience or 10 years
    of your work experience on a piece of paper, you need to make sure it is as relevant
    as possible to the role you are applying for. At the end, this is all about the
    signal and the noise. You want to emphasize the things that are relevant to the
    job. Remove all the noise about your jobs that you have after college 10 years
    ago that are not relevant.'
  sec: 1033
  time: '17:13'
  who: Oleg
- header: CV is your landing page
- line: "This brings us to the question about CV. This is the very first step in the\
    \ job process. A recruiter or hiring manager looks at your CV \u2014 a piece of\
    \ paper, one or two or three pages. They figure out if this candidate should go\
    \ through the process or they reject them right away. How do we make sure that\
    \ we pass this CV screen phase? You mentioned that you need to make your CV as\
    \ relevant as possible to the job. For that you need to really read the job description\
    \ and see how your experience matches. What else can you do there? How can you\
    \ make your CV stand out?"
  sec: 1108
  time: '18:28'
  who: Alexey
- line: "I would think of CV as your landing page. Think about a website. You see\
    \ an ad on the internet, you click on the link, you end up on some website that\
    \ you have never seen before. In two seconds, you will decide to close it or not,\
    \ if this is something relevant. You will keep looking at it. The way websites\
    \ are designed and implemented has changed a lot in the past 20 years. If you\
    \ compare the internet 20 years ago, next to what it is now, there are a lot of\
    \ changes. There have been a lot of experiments and improvements. Think about\
    \ CVs in the same way. The recruiter that is looking at your CV \u2014 what is\
    \ their goal? The goal is to quickly estimate how valuable you will be in the\
    \ company if you join."
  sec: 1160
  time: '19:20'
  who: Oleg
- line: "Even more specific: their goal is to estimate what will happen if they set\
    \ up an interview between you and the hiring manager. How likely the hiring manager\
    \ is to offer your job or reject you? The goal of a CV for you is to get to an\
    \ interview \u2014 not to get a job. It\u2019s to make sure that the interviews\
    \ will happen and you will get to talk to someone technical."
  who: Oleg
- line: "So, when the recruiter looks at your CV, they might even not be familiar\
    \ with the technical side of it. What they have is the job description. They spoke\
    \ with the hiring manager about the skills required for the role. They have it\
    \ on one hand, and they have your CV on the other side. Then you can think of\
    \ it as of a very simple classification model that just looks for keywords. Do\
    \ you have this word \u201CTensorFlow\u201D in your CV? If the job description\
    \ says \u201Cbe proactive\u201D, are you proactive?"
  who: Oleg
- line: We try to do this matching in your mind and understand what the role requires.
    Unfortunately, job descriptions are also very generic most of the time. But try
    to apply this job description to your past experience. Personalize your CV for
    every role you are applying. Your goal is to pass this screen. Then you will be
    able to chat about your past experience and demonstrate your technical skills.
  who: Oleg
- line: "Recruiters are always on your side. When they look at your CV, when they\
    \ have a call with you \u2014 recruiters are on your side. Their goal is to fill\
    \ the role, to place someone in the role. It\u2019s in their interest for you\
    \ to get this job. If you have a call with a recruiter, ask them about the expectations,\
    \ and ask them about the process. They would be very happy to help you."
  who: Oleg
- line: "If you think about this very first step \u2014 CV screen by recruiter. If\
    \ you think about it as a classifier, there is a very high penalty for false positives\
    \ \u2014 if the company hires a person that is not relevant for a job. This is\
    \ a big problem for both. There is a very big penalty for this kind of error.\
    \ At the same time, there is zero penalty for not hiring a good person, a good\
    \ candidate because. No one will even know if they were good or not. This classifier\
    \ tends to create a lot of false negative errors. A lot of candidates that would\
    \ have gotten on with their job get rejected."
  who: Oleg
- line: "So, in your CV, try to first understand what is important for this role.\
    \ Make sure you highlight it as much as possible and remove everything else. Remove\
    \ all the noise. Whenever you are describing your past experience, be very specific\
    \ about what was your personal contribution to a project. If you write on the\
    \ CV, \u201CI work on predictive models\u201D, \u201CImproving accuracy of predictive\
    \ models\u201D, it says nothing. You\u2019re a data scientist, you are expected\
    \ to do that. What exactly did you do? Even if you write something like \u201C\
    We improved the accuracy of a random forest model by X percent\u201D. What exactly\
    \ did you do? Did you identify the problem? Did you decide to use random forest?\
    \ Be very specific in what was your contribution to whatever project was. This\
    \ is the main advice."
  who: Oleg
- line: Also if you are applying to a company, to maximize your chances of pacing
    through this first step of the CV screening, reach out to your recruiter directly.
    You can try to reach out to someone from the team directly and ask them about
    the company. Ask them about the team in the company. If you know someone, ask
    for a referral. it always helps to pass this first step. At least someone will
    look at your CV. And probably you will secure this, this first screening call
    from the company.
  who: Oleg
- line: "I think it gives an extra signal: somebody from within the company, somebody\
    \ who already passed our hiring process, referred this person. So this person\
    \ must be good. So, let\u2019s take a closer look at the CV..."
  sec: 1551
  time: '25:51'
  who: Alexey
- line: "Exactly. Also, this sounds very obvious but it happens. Check for typos and\
    \ errors. This is really bad \u2014 it just looks very unprofessional. Make sure\
    \ the formatting is consistent throughout the document. Don\u2019t try to lie\
    \ about things, and pretend that you build something that single-handedly. This\
    \ can backfire. You never know, maybe this company is interviewing your colleague.\
    \ This can really backfire. Also, sometimes I see people that put self-evaluations,\
    \ like Python \u2014 five stars expert. It doesn\u2019t make a lot of sense."
  sec: 1563
  time: '26:03'
  who: Oleg
- line: "To summarize it. CV is your landing page. On a landing page, people don\u2019\
    t spend more than two second. This is the time span you will get when the recruiter\
    \ looks at your CV. You need to maximize the chances that you will pass this stage.\
    \ You do this by highlighting what is important for the role, you remove everything\
    \ else. You need to be specific about your personal contribution. It will maximize\
    \ the chances that within these two seconds the recruiter will take a look at\
    \ your CV and decide \u201Cokay I want to look more at this CV\u201D. And eventually\
    \ you will pass the screen. After you pass the screening, what happens next?"
  sec: 1626
  time: '27:06'
  who: Alexey
- header: Take-home assignments
- line: "There might be a take home assignment. It will probably take a few hours\
    \ for you to implement. There are controversial opinions about take-home assignments.\
    \ It takes a lot of time. If you are applying to five different jobs, then you\
    \ need to work on five different take-home assignments, it will take the entire\
    \ week. I am not a big fan of take-home assignments for that reason: it\u2019\
    s more of a signal whether a person has time for them. If you\u2019re given a\
    \ take-home assignment, think about it in this way: what is the return of investment\
    \ in spending your time if you get this new job? you applied for this new job\
    \ for a reason \u2014 a better team, a better career opportunity, a pay increase,\
    \ usually it\u2019s at least some 15 percent. If you spend one day working on\
    \ a take-home assignment, it will pay off if you get the job. Think about it from\
    \ this risk/reward perspective. Because it really pays off to invest into preparing\
    \ for interviews and spending your time. Emphasize your strengths and demonstrate\
    \ your skills when you are interviewing. Because if you are not willing to, if\
    \ you think it\u2019s not worth time to work on this, then maybe this is not the\
    \ job that you really want."
  sec: 1671
  time: '27:51'
  who: Oleg
- header: Questions about your past experience
- line: "After the take home assignment, there will be interviews \u2014 from three\
    \ to six rounds of interviews with different potential colleagues. One of them\
    \ will be with the hiring manager. On the technical rounds, you can split these\
    \ into two situations. At some point you will be asked about your past experience.\
    \ At some point it will be some hypothetical questions, most likely about the\
    \ company."
  sec: 1772
  time: '29:32'
  who: Oleg
- line: "If you are asked about your past experience, make sure you have a couple\
    \ of stories that help you demonstrate your skills. It\u2019s really important\
    \ to practice, to know exactly what you are going to say. When you are answering\
    \ these questions about your past experience, it\u2019s not only about \u201C\
    I used a random forest model to predict house prices\u201D. When you tell the\
    \ story, you can also highlight a lot more than your machine learning skills.\
    \ Try to emphasize your strengths between the lines. If you were the one who identified\
    \ the problem and suggested to use a machine learning model to solve this problem,\
    \ say it. If you suggested several modeling approaches, asked stakeholders for\
    \ feedback and then defined the requirements, say that you did. If you found something\
    \ interesting when you worked on a model and you decided to share it with your\
    \ colleagues, and made everyone more efficient, mention it."
  who: Oleg
- line: "It\u2019s not just about the model. Even if it may be presented as a technical\
    \ interview, even if you are asked about some model that you built in the past,\
    \ by answering this question you can highlight a lot more than just your modeling\
    \ skills. Those are the skills that really make the difference between a middle\
    \ data scientist and senior data scientist. This really shows how autonomous you\
    \ are, how proactive you are, that you can make everyone else around you more\
    \ efficient and encourage others. This is really helpful."
  who: Oleg
- header: Hypothetical case questions
- line: "If you\u2019re asked about some hypothetical case\u2026 It\u2019s hard to\
    \ say \u2014 there are so many companies and everyone is doing it differently."
  sec: 1923
  time: '32:03'
  who: Oleg
- line: "You will get asked a question about some vague problem statement: \u201C\
    predict user churn\u201D, \u201Cclassify which users are fraudsters on our platform\u201D\
    , \u201Cpredict how many orders or subscriptions we will have next month\u201D\
    . It\u2019s always a vaguely defined problem statement. When you are answering\
    \ this kind of question, the very first thing is to demonstrate that you are trying\
    \ to understand the business goals. Ask why do we do it? Who will be using this\
    \ model? What are the use cases? How do we define \u201Cchurn\u201D? If you are\
    \ predicting which users will churn \u2014 is it people that will not place an\
    \ order within two weeks? Make it more concrete, so that you understand the problem\
    \ before you rush into the details. Then make sure that your narrative is very\
    \ structured. You start by understanding the goals."
  who: Oleg
- line: "Then \u2014 what kind of data do we need? What kind of model do we choose?\
    \ We built the model, how do we evaluate this? Try to not jump from some very\
    \ abstract things into explaining how a certain modeling approach works and then\
    \ back to showing the results. It\u2019s okay to take some time and think about,\
    \ this also helps you highlight your communication skills.  At each step you want\
    \ to think about, \u201Cwhat is the goal?\u201D. We are building the model to\
    \ predict churn because of this. Then we need to get the data. What kind of data\
    \ do we need? Here you can demonstrate your business, product and common sense\
    \ by just thinking out loud which features will have impact on the output."
  who: Oleg
- line: "Then you can start thinking about the modeling approach. Do we need explainability?\
    \ Yes. Do we need to run it real time? No. What kind of data do we have? That\u2019\
    s why I choose gradient boosting. You always explain your choices. What can happen\
    \ is that the interviewer will sometimes interrupt you and give you some new piece\
    \ of information. They want you to go deeper on some certain topics and see if\
    \ you can identify some edge cases, some limitations of the algorithm that you\
    \ use, some limitations of the evaluation metric that you chose."
  who: Oleg
- line: "At every step it\u2019s a good practice to start with understanding the goals,\
    \ explaining the goals. \u201CWhat am I trying to achieve here?\u201D And then\
    \ go detailed enough so that it doesn\u2019t sound like common sense, but you\
    \ sound like an engineer. For example, when you need to explain what features\
    \ you would use to build a model, don\u2019t say \u201Cchurn rate\u201D, say something\
    \ like \u201Cusers that didn\u2019t play within a certain period\u201D. Don\u2019\
    t say \u201Cconversion rates\u201D. It\u2019s something that you can quantify,\
    \ something that you can implement in SQL or in Python or whatever. It\u2019s\
    \ not just a common sense answer. You can really think of this extra step and\
    \ put it in code and implement this. This is a very common reason for rejections\
    \ when data scientists just start throwing a lot of different ideas. We can do\
    \ this and this and that, but don\u2019t go deep enough into any of them. At the\
    \ end, you need to implement things."
  who: Oleg
- header: Technical rounds
- line: "So you can get from 3 to 6 rounds of different nature. Some of them will\
    \ ask about your past experience. You need to prepare some stories for that, like\
    \ how you did something, how you identified the requirements, how you help your\
    \ colleagues, things like this. Then there are hypothetical case questions. I\
    \ usually call them \u201Ccase studies\u201D. They ask you, \u201CWe want to identify\
    \ users who stop using our services\u201D. They sound vague, and this is on purpose.\
    \ You need to figure out how to get more requirements. Then there could be some\
    \ other types of rounds like I SQL, maybe machine learning, maybe python and things\
    \ like this."
  sec: 2198
  time: '36:38'
  who: Alexey
- line: "It really depends on the company and on the role. For some roles, you will\
    \ be asked about machine learning in detail \u2014 how broad is your knowledge\
    \ of different algorithms? If you say that you are familiar with one of them,\
    \ how deep do you know this certain algorithm? The limitations? Can you explain\
    \ how it works? In what situations it works best? And so on. If you are applying\
    \ for more analytical or product data science roles, then it\u2019s very likely\
    \ that there will be some SQL questions. Most likely you will not be asked simple\
    \ things like joins. Expect questions on window functions. I think it became a\
    \ standard."
  sec: 2265
  time: '37:45'
  who: Oleg
- line: It is terrible! I have to Google this every time. People expect you to know
    that.
  sec: 2316
  time: '38:36'
  who: Alexey
- line: "I think it\u2019s okay. This is my personal perspective \u2014 I think it\u2019\
    s okay that if your code doesn\u2019t work. But at least you understand what it\
    \ is, how it works. You can Google it, you know, what to Google for. This is enough\
    \ because you will be able to Google it at work. But at least you know that there\
    \ is such a thing, that there is \u201Crank\u201D or that there is a \u201Clag\u201D\
    . But you don\u2019t have to remember the exact syntax."
  sec: 2322
  time: '38:42'
  who: Oleg
- header: Handling rejections
- line: It often happens that I forget how to use window functions. For this company
    this is a super important thing and they decide to reject me. How can I handle
    this rejection? What happens if I get rejected?
  sec: 2350
  time: '39:10'
  who: Alexey
- line: "First of all, don\u2019t take it personally. It\u2019s not an exam. it doesn\u2019\
    t say that you are bad. It doesn\u2019t say that you aren\u2019t qualified. It\
    \ probably says that there was someone else who is more relevant for this certain\
    \ role \u2014 and nothing else. You never know who you are competing with. Maybe\
    \ there was someone with five years more of experience than you have. Or maybe\
    \ someone who has more relevant experience for a certain industry. It should never\
    \ harm your self-esteem. Also, realistically, interviews are far from perfect.\
    \ The outcome is sometimes arbitrary. Maybe they made a mistake \u2014 this also\
    \ happens. You never know. If you get rejected, ask for feedback, if you weren\u2019\
    t given feedback. This will hopefully help you identify what are the things that\
    \ you can improve."
  sec: 2371
  time: '39:31'
  who: Oleg
- line: "Also, depending on the company, you can just reapply to the same company\
    \ in a different team right away. Usually it\u2019s allowed. It shows that you\
    \ are not a good fit for a certain role, but you are still a good fit for some\
    \ different role at the same company. If you are thinking about reapplying for\
    \ the same role, if it is a large enough company and it keeps hiring data scientists\
    \ for a certain role, usually after some cool-off period, after a few months,\
    \ you can reply. You can think of it as a learning experience. Try to get as much\
    \ from it from a learning perspective: take notes, write down the questions that\
    \ you were asked. It will help you become more confident in the future interviews.\
    \ The feedback will help you study and prepare for the future interviews."
  who: Oleg
- header: What to do after receiving an offer?
- line: "Let\u2019s say I had a couple of rejections, but I learned from them. Then,\
    \ on the fifth interview, I finally got the offer. What happens then? What do\
    \ I do now? Do I jump into accepting and call all my friends, saying \u201CHey\
    \ I got this job!\u201D Do I need to do something there?"
  sec: 2496
  time: '41:36'
  who: Alexey
- line: We celebrate. If you get an offer, first of all, learn what you are offered.
    The offers can be very different depending on the country and a company. It can
    be just the salary, it can be salary and some equity compensation, it can also
    mention some bonus, it can also have some sign-on bonus. Try to learn how it compares
    to other companies. There is glassdoor, there are other websites where you can
    try to estimate and find some baselines on how relevant this offer is.
  sec: 2522
  time: '42:02'
  who: Oleg
- line: "Then I think it\u2019s always a good idea to negotiate because it doesn\u2019\
    t harm. They will not change their mind if you try to negotiate a little bit.\
    \ Your success with negotiations really depends on whether you have another offer.\
    \ If you have two competition offers. then it can happen that they will match\
    \ the competing offer, if it\u2019s still within their budget. If you're negotiating\
    \ and it sounds like it\u2019s not possible to negotiate on the base salary, ask\
    \ if it\u2019s possible to get a sign-on bonus. If you don\u2019t have competing\
    \ offers, then most likely you don\u2019t have a lot of negotiation power. Maybe\
    \ you will be able to get a few thousand extra, maybe not. That is why it\u2019\
    s good to interview in a few companies at the same time \u2014 to have this leverage."
  who: Oleg
- header: Do recruiters pay attention to age?
- line: Yes. Having multiple offers is probably the best way to negotiate. We have
    quite a few questions. One of the questions I see in chat is from Natalia, about
    age. Do you know if recruiters pay attention to the age of candidates? If somebody
    is 40 years old, is it a bad signal for the recruiter?
  sec: 2636
  time: '43:56'
  who: Alexey
- line: "They are not supposed to know it. Just don\u2019t put it on your CV. Don\u2019\
    t put your picture, don\u2019t put your age. Don\u2019t say it \u2014 it\u2019\
    s illegal in most of the countries."
  sec: 2678
  time: '44:38'
  who: Oleg
- line: They are not supposed to reject you on this basis, right?
  sec: 2701
  time: '45:01'
  who: Alexey
- line: Of course! I think this is not a reason to not hire anyone. But if you have
    your date of birth or even the picture in the CV, I would just remove them. This
    kind of personal information on your CV is just noise. It has nothing to do with
    how valuable you will be for the company. Just remove it.
  sec: 2710
  time: '45:10'
  who: Oleg
- line: "The same goes with the picture, your marital status, your address\u2026"
  sec: 2737
  time: '45:37'
  who: Alexey
- line: No, absolutely not.
  sec: 2745
  time: '45:45'
  who: Oleg
- header: "Getting a job with a PhD \u2014 it\u2019s a cold start problem"
- line: "Okay, yeah. So, if this does not tell you how good you are at your job, do\
    \ not put it in your CV. Probably you still need to keep the name\u2026 So, we\
    \ have a question from Diksha. I\u2019m a PhD scholar with zero industry experience,\
    \ but I have knowledge required by industry experts. How do I land a good data\
    \ science job?"
  sec: 2746
  time: '45:46'
  who: Alexey
- line: "Think about it as a cold start problem \u2014 when you don\u2019t have initial\
    \ data and you need to build some model. You need to create some synthetic data.\
    \ You can go to Kaggle or  some other places that offer you data. Ideally, you\
    \ want to be creative and come up with some problem that can be solved with machine\
    \ learning \u2014 or whatever is your specialization. I started by telling this\
    \ story about how I got a job \u2014 by building this fake and simple recommender\
    \ engine. This is exactly that. For hiring managers what matters the most is whether\
    \ or not you have some experience in the data science process. Like if you are\
    \ building machine learning models, then it starts with identifying the problem,\
    \ goes through building the model, evaluating the model, then communicating the\
    \ results, and identifying the next steps. It\u2019s not as important whether\
    \ it was your personal project or it was a commercial experience. Ideally, this\
    \ should be some commercial experience when you work with the team of other data\
    \ scientists, you have some supervision from your colleagues. If you don\u2019\
    t have it, just create this experience. Identify problems. Try to be creative.\
    \ There are a lot of things to be solved with predictive models, with different\
    \ kinds of models. Write a blog post about this and mention it on your CV. The\
    \ best thing you can do is \u2014 try to build something for the company you are\
    \ applying for. This will certainly make you stand out."
  sec: 2777
  time: '46:17'
  who: Oleg
- line: "What you are saying is, Kaggle is great, but if you check what the company\
    \ is doing. Like you did \u2014 you thought \u201CWhat kind of problems they have?\u201D\
    \ And you come up with a problem, then you solve this problem, you wrote the blog\
    \ post and showed it to the hiring manager. Then they were amazed and hired you."
  sec: 2884
  time: '48:04'
  who: Alexey
- line: "Exactly. It\u2019s not 100% that you will get hired. But if you spend time\
    \ building models to have something in your CV, to be able to tell this story\
    \ about your past experience, you will also learn by doing this. Don\u2019t think\
    \ \u201CIt's such a waste of time. They will not hire me. I will spend a weekend\
    \ or I will spend the week working on this project and writing this blog post.\
    \ And then, at the end, it will not work out. Then it was a waste of time.\u201D\
    \ No, you learned. You\u2019re a data scientist. This is what you chose to do.\
    \ This is interesting. This is exciting. And you learn some new things. You will\
    \ benefit in any way, if you do it."
  sec: 2904
  time: '48:24'
  who: Oleg
- header: Should I answer rejection emails?
- line: 'Thank you. Another question we have: Some rejection emails look quite human.
    The question is, is it worth answering such emails? Do the recruiters even look
    at what you write to them after the rejection?'
  sec: 2950
  time: '49:10'
  who: Alexey
- line: "\u201CThank you\u201D. There is no point in arguing. That is probably the\
    \ worst thing you can do. Just say that you appreciate the feedback. This is the\
    \ best thing you can do because maybe you will apply to the same company and it\
    \ will be the same recruiter. Maybe you will apply to a different company and\
    \ this recruiter will change jobs as well. This happens very often. Try to not\
    \ burn bridges. Even if you think it was unfair to you, try to learn from it.\
    \ I think you can only appreciate and send a \u201CThank you\u201D email. And\
    \ thank for feedback if you found it actionable and useful."
  sec: 2971
  time: '49:31'
  who: Oleg
- header: Negotiating when my salary is low
- line: "Thank you. Another question we have from Muhammad is related to negotiations.\
    \ How do I negotiate when my current salary is quite low? I think we covered that\
    \ \u2014 by having two offers. But let\u2019s say, I just have one offer and my\
    \ current salary is low. What can I do to make sure that I try to get the best\
    \ possible offer from this company?"
  sec: 3017
  time: '50:17'
  who: Alexey
- line: "Just try to put yourself in the shoes of the company. Think about them. They\
    \ offer you some number. You can either accept it or not \u2014 and then they\
    \ lose you. They will need to hire someone else. They are not supposed to know\
    \ what your current salary is. Also in a lot of countries it\u2019s just illegal\
    \ to request this. If they ask you, you don\u2019t have to answer. You can always\
    \ just answer \u201CThe offer I am expecting from you is a good signal of how\
    \ important data science is for the company\u201D. You don\u2019t have to tell\
    \ the exact number that you are making right now. Try to make it more like \u201C\
    Here are my skills, you interviewed me, you made me an offer, you found me valuable\
    \ for the company. But I find it low. So, I am hesitant about accepting it. What\
    \ we can do about this?\u201D"
  sec: 3046
  time: '50:46'
  who: Oleg
- line: "So, try to negotiate. When you have another offer you can always say \u201C\
    If you don\u2019t do this, I will go to the other company\u201D. But in negotiations\
    \ you always have an option of not accepting an offer. So, if you don\u2019t have\
    \ another offer and you just have one, you always have an option of staying at\
    \ your current place or not accepting. This is the best alternative. You can just\
    \ say \u201CFor this number, it doesn\u2019t make sense for me to change a job.\u201D"
  sec: 3113
  time: '51:53'
  who: Alexey
- line: "If it\u2019s true, you can say \u201CI have a good performance, there\u2019\
    s a good chance that I will get promoted next year. I\u2019m not sure if it\u2019\
    s worse for me to join with an offer like this. Maybe you could offer me a sign-on\
    \ bonus that would offset this? This is the bonus that I am expecting in my current\
    \ company\u201D. So try to explain that you are losing something, you have a better\
    \ option than the offer that they offered you. And they have to offer something\
    \ else for you."
  sec: 3150
  time: '52:30'
  who: Oleg
- header: Should I apply for jobs that require 5 years of experience?
- line: "Thank you. Another question we have from somebody who just finished their\
    \ PhD. The position they want to apply to requires 3-5 years of experience in\
    \ industry. They don\u2019t have it obviously because they just graduated from\
    \ PhD. Do you think it still makes sense to apply for this position that requires\
    \ some industry experience? Or is it not worth spending the time?"
  sec: 3189
  time: '53:09'
  who: Alexey
- line: "It sounds like it is some entry-level position, if it is 3 years of experience.\
    \ It wouldn\u2019t  harm if you apply. It also depends on your PhD. This definitely\
    \ happens when people with no commercial experience get hired at this kind of\
    \ roles. As long as you believe that you could perform well in this role, If when\
    \ working in your PhD you have gotten relevant experience. If you were working\
    \ on something very theoretical and never implemented machine learning models,\
    \ if you think your programming skills are not good enough, and it\u2019s very\
    \ clear that the role expects you to program a lot, then don\u2019t apply. But,\
    \ in general, job descriptions are flexible. Sometimes they are very standard.\
    \ If you have one year of experience or less, you should definitely give it a\
    \ try."
  sec: 3218
  time: '53:38'
  who: Oleg
- line: "I liked your point, that it\u2019s a cold start problem. You need some synthetic\
    \ data to bootstrap your profile. Try to get some experience, not necessarily\
    \ from the industry. If this matches the candidate profile they are looking for,\
    \ maybe the hiring manager will just go for this. Even though you don\u2019t have\
    \ three years of experience, but because the project you did is so great, they\
    \ will at least talk to you."
  sec: 3279
  time: '54:39'
  who: Alexey
- header: Tricking applicant tracking systems
- line: "Another question: I heard that these days, named entity recognition and some\
    \ other things are used for screening CVs. It\u2019s not a human that looks at\
    \ the CV but a robot. You need to just to maximize your chances for applying for\
    \ a job. Do you just need to copy the keywords you see on the description and\
    \ paste them in your CV to maximize your chances?"
  sec: 3317
  time: '55:17'
  who: Alexey
- line: "Whatever you do, don\u2019t put the keywords that you are not familiar with.\
    \ You probably have more experience than some five keywords. Or you cannot put\
    \ a year of experience or more than a year of experience in one page of paper.\
    \ Try to really make it as relevant as possible and remove everything that is\
    \ not relevant. Sorry, I forgot what was the question?"
  sec: 3346
  time: '55:46'
  who: Oleg
- line: If you should just copy and paste things from the description.
  sec: 3375
  time: '56:15'
  who: Alexey
- line: "What automatic screen, what happens often is: you submit a CV in PDF. Then\
    \ it\u2019s automatically parsed and stored in some applicant tracking system.\
    \ The parsing is used to have a database with structured data. This is a data\
    \ problem. You have a thousand CVs in very different formats \u2014 PDFs and images.\
    \ You want to have it in some structured format in a table where you have the\
    \ name, years of experience and current role. So, the CVs are parsed by applicant\
    \ tracking systems. But I have never heard of some automatic tool that rejects\
    \ people based on their CVs. This is a myth that for some reason became very popular.\
    \ Even if it happens, this is very rare. So, in 99% cases a human being will look\
    \ at your CV."
  sec: 3379
  time: '56:19'
  who: Oleg
- line: "Unless there are 300 or 400 applicants for a position \u2014 which happens\
    \ these days. Probably what recruiters do is just whoever applied first they just\
    \ go through this. So they still don\u2019t reject automatically based on some\
    \ tracking system."
  sec: 3443
  time: '57:23'
  who: Alexey
- line: "That is true for some roles: there are a lot of applicants. It\u2019s not\
    \ that you get rejected automatically because your CV was not in the right format,\
    \ but because there was a hundred other people."
  sec: 3463
  time: '57:43'
  who: Oleg
- line: "Sometimes it\u2019s not humanly possible to look at all the applicants. That\u2019\
    s unfortunate."
  sec: 3477
  time: '57:57'
  who: Alexey
- header: What else Oleg learned after interviewing 300 data scientists
- line: I wanted to ask you a few things. What did you actually learn after interviewing
    300 data scientists?
  sec: 3494
  time: '58:14'
  who: Alexey
- line: "A lot of things. First of all, I cannot walk into an interview with some\
    \ certain expectations and answers. Sometimes the answers I hear are correct and\
    \ probably are even better and more efficient than what I expected. This happens.\
    \ You should never have this bias, like \u201CThis is the correct answer that\
    \ I am expecting. If it\u2019s not true, then this is wrong.\u201D This happens\
    \ all the time. This is a very humbling experience. Also, for most of the questions,\
    \ no matter how you phrase it, especially if it\u2019s some very vaguely defined\
    \ case study, usually there are four, five, six different paths of answering the\
    \ question."
  sec: 3504
  time: '58:24'
  who: Oleg
- line: "There are a number of ideas like \u201Crandom forests are always better than\
    \ linear regression\u201D, right? There is something like this in the air. But\
    \ this is not true. In some cases, simple parametric models may perform better.\
    \ Even if they require you to spend more time doing processing. Even if they have\
    \ a lot of reasons to not perform well. There are cases when a parametric model\
    \ is just better. Because it\u2019s able to extrapolate and this cannot. This\
    \ kind of answer I receive quite often, when you introduce some context. When\
    \ it\u2018s clear that you need to extrapolate, when it\u2019s very clear that\
    \ the data will be beyond the range of the training data set. Also, there is a\
    \ common misconception that deep learning is better than trees and trees are better\
    \ than parametric models. Try to understand the problem, try to really understand\
    \ the limitations of algorithms."
  who: Oleg
- line: "Another thing I learned from 300 interviews: it would be nice to reverse\
    \ the timeline. To know what feedback you would get after the interview \u2014\
    \ even before going to the interview. It sounds like a plot for some movie. But\
    \ this is exactly what I\u2019m trying to solve with NextRound. You try interviewing,\
    \ you get your feedback: there are your strengths, here are your weaknesses, here\
    \ are the materials to improve. Then, on the next iteration, you go to a real\
    \ interview. Having this feedback and having applied this feedback and having\
    \ read these materials will help improve. Because this is how modeling works.\
    \ You run iterations. You tune a few parameters and expect it to be better. I\
    \ think interviews itself is a really good learning experience. This is not very\
    \ obvious \u2014 it\u2019s usually perceived as an exam, an assessment."
  who: Oleg
- line: "Another thing: it\u2019s very important to ask questions on the interviews\
    \ as a candidate. This is a two-way street. You\u2019re also choosing. You\u2019\
    re deciding if you will like working in the company. And the company decides whether\
    \ you will be a valuable team member. For some reason, the time is distributed\
    \ for 45 minutes, it\u2019s an exam, and then for 5 minutes at the end, if you\
    \ are lucky, you will be able to ask a few questions."
  who: Oleg
- line: "If you get these five minute, use as much of this time as possible. it\u2019\
    s in your interest to learn about the company. By asking questions you can also\
    \ highlight your strengths. By asking questions about the company, about the workflow\
    \ in the company, about the teammates you can highlight that you care about the\
    \ culture. That you care about the flexibility, you are proactive. If you are\
    \ working as a data scientist and you ask what happens if a data scientist and\
    \ the team suggest some product idea, like what is the process? How bureaucratic\
    \ is it? How much time does it take from an idea to going to production? If you\
    \ ask these kinds of questions, you try to demonstrate your strengths. It\u2019\
    s also a way of emphasizing your personality traits, like proactiveness or stakeholder\
    \ management, even in the last five minutes of the interview."
  who: Oleg
- header: How a horse's ass determined the design of a space shuttle
- line: "This is a great tip to use questions to highlight your own strengths. One\
    \ last thing \u2014 this is something we promised to people who registered for\
    \ this event. This is the teaser that you used. How a horse's ass determined the\
    \ design of a space shuttle and what does it have to do with your CV?"
  sec: 3864
  time: '1:04:24'
  who: Alexey
- line: "This is a very famous story. The legend says that the distance between the\
    \ rails on the railroad is the same as the width of a two-horse carriage. This\
    \ makes sense because people used to carry goods and themselves on carriages.\
    \ They did not have engines, they had horses. Then they applied the same size\
    \ with the same tools when they started using railroads. Then several decades\
    \ or a century later, a space shuttle was built. But they had to carry the parts\
    \ of the space shuttle from the factory to the launch site. They could not do\
    \ it by car, they had to do it by train. The details of the space shuttle had\
    \ to fit the train. This is how the width of a two-horse carriage defined the\
    \ design of the space shuttle \u2014 through this limitation. I don\u2019t know\
    \ if it\u2019s true, but this is a very famous story."
  sec: 3889
  time: '1:04:49'
  who: Oleg
- line: "So, every time I look at the CV, I think about this story. CVs in this current\
    \ format \u2014 as a one or two pages of A4 paper \u2014 became popular in the\
    \ late 20th century when everyone has got a printer and Microsoft Office. This\
    \ was an easy way to hand them to the interviewer, to have this review of your\
    \ experience on a piece of paper. This was the way people shared information before\
    \ \u2014 there was no internet in that time. Now it does not make any sense because\
    \ no one prints the CVs. I don\u2019t even remember when was the last time I saw\
    \ a printed CV. But the format is still the same. You can think about how other\
    \ industries evolved in this time. Again, you can think about landing pages. How\
    \ web page design has changed. At the end, a CV is a landing page. The goal of\
    \ a CV is to show your experience, to help recruiters and companies see how relevant\
    \ your experience is for a certain team. The format has not changed at all during\
    \ this time. We just spoke about putting your picture, your age and your home\
    \ address on the CV. These things are completely irrelevant. This is just an example\
    \ of something when something archaic still defines how people apply for jobs\
    \ now, as much as this two horses influence the width of a space shuttle."
  who: Oleg
- line: So, what you are saying is we should ditch our CV and build landing pages?
  sec: 4070
  time: '1:07:50'
  who: Alexey
- line: "No. What I am saying is, I would think of a CV as a landing page. Something\
    \ that can get your attention in the first few seconds and make you read further.\
    \ It\u2019s something valuable for you, for the company, for the recruiter. Maybe\
    \ at the bottom somewhere you can add some details that are not as relevant for\
    \ the job. But you can think of it as a webpage design. On the other side, you\
    \ can think of a CV as future engineering. Hiring and applying for a job is classification.\
    \ There is a binary outcome: you either get an offer or don\u2019t. The decision\
    \ is based on this prediction on how well you will perform at the job. Your past\
    \ experience and your raw unstructured data. Your CV is the features."
  sec: 4076
  time: '1:07:56'
  who: Oleg
- line: "What do we do with future engineering? We try to find future importance.\
    \ We try to remove outliers. We try to clean up the data. Think about the signal\
    \ to noise ratio. Put as much signal relevant for the job for a certain role,\
    \ remove all the noise. If you think about models\u2026 My background is in personalization.\
    \ Try to personalize the CV for every role you apply. Try to maximize this relevancy\
    \ score between the job description and your CV. Don\u2019t make it in the same\
    \ way, it was in the 80s."
  who: Oleg
- line: "Make sense. We still have quite a few questions but I suggest taking these\
    \ questions to slack and answer them there. I\u2019d like to thank you for joining\
    \ us today and sharing your experience of what you learned from interviewing 500\
    \ data scientists with us. And thanks everyone else for joining us today. I wish\
    \ everyone a great weekend and see you next week."
  sec: 4166
  time: '1:09:26'
  who: Alexey
- line: Thank you for joining me. Thank you for having me.
  sec: 4191
  time: '1:09:51'
  who: Oleg
- line: Goodbye.
  sec: 4194
  time: '1:09:54'
  who: Alexey

---


Links:

- Oleg's service for interviews: [https://nextround.cc/](https://nextround.cc/){:target="_blank"}
- LinkedIn: [https://www.linkedin.com/in/olegnovikov/](https://www.linkedin.com/in/olegnovikov/){:target="_blank"}