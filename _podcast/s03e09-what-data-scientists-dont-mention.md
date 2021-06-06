---
title: "What Data Scientists Don’t Mention in Their LinkedIn Profiles"
short: "What Data Scientists Don’t Mention in Their LinkedIn Profiles"
guests: [yurykashnitsky]

image: images/podcast/s03e09-what-data-scientists-dont-mention.jpg

season: 3
episode: 9

ids:
  youtube: c6dK1LWpv4g
  anchor: What-Data-Scientists-Dont-Mention-in-Their-LinkedIn-Profiles---Yury-Kashnitsky-e125jjl

links:
  youtube: https://www.youtube.com/watch?v=c6dK1LWpv4g
  anchor: https://anchor.fm/datatalksclub/episodes/What-Data-Scientists-Dont-Mention-in-Their-LinkedIn-Profiles---Yury-Kashnitsky-e125jjl
  spotify: https://open.spotify.com/episode/3KR6zErxqeDuQ2jo8NDvNx
  apple: TODO

transcript:
- line: "This week we will talk about failures and things in our CVs that we typically\
    \ don\u2019t talk about. We have a special guest today, Yury. Yury is currently\
    \ working as a senior machine learning scientist at Elsevier. His main focus at\
    \ work is natural language processing. You might already know Yury from mlcourse.ai,\
    \ which is an awesome machine learning course. You can go check it out. Yury is\
    \ the mastermind behind this course. A couple of months ago, we had an interview\
    \ with Ksenia about transitioning from project management to data science. She\
    \ mentioned that course. on that day, I thought it was a good idea to invite Yury\
    \ to this podcast as well. Finally this day happened. Hi Yury, welcome."
  sec: 90
  time: '1:30'
  who: Alexey
- line: "Hi, Alexey. It\u2019s very cheerful here in The Hague. I am pretty happy\
    \ to join you this Friday afternoon. I\u2019m always fond of talking about career\
    \ and all this stuff. I\u2019m happy to share this experience. Although the topic\
    \ is a bit controversial, it might hurt the marketing interest of some of the\
    \ companies. I\u2019ll be careful here. I don\u2019t promise that I will answer\
    \ all of the questions as open as possible."
  sec: 152
  time: '2:32'
  who: Yury
- header: "Yury\u2019s background"
- line: "We\u2019ll start with your background. Can you tell us about your career\
    \ journey so far?"
  sec: 185
  time: '3:05'
  who: Alexey
- line: I lived in Israel for four years, then a year and a half in Canada. Then I
    went back to Russia. So I made the world around in my childhood. I was growing
    up in Russia and I was fond of aviation and thus I joined the best Russian technical
    university, Moscow Institute of Physics and Technology, the aviation department.
    In the meanwhile, I realized I am fond of programming. Then I watched Andrew Ngs
    course about machine learning. Then I switched from business intelligence. Then
    I switched to PhD studies, I was full-time in academia. That was a crazy time
    but I do not regret it.
  sec: 193
  time: '3:13'
  who: Yury
- line: "Then I joined Russian IT giant, Mail.Ru Group, as a data scientist. I always\
    \ searched for better work-life balance. That\u2019s why we moved to the Netherlands\
    \ through a Telco operator. After that I joined Elsevier. It\u2019s a good place\
    \ to combine research. It\u2019s a nice compromise between academy and industry.\
    \ I\u2019m also fond of quantum computing and quantum machine learning. I\u2019\
    m really a nerd, in a good sense. I have a small child, a daughter, who will turn\
    \ a year and a half soon. She replaced all of my hobbies, I cannot do hobbies\
    \ anymore."
  who: Yury
- line: "So you removed your \u201Chobbies\u201D section from your CV?"
  sec: 298
  time: '4:58'
  who: Alexey
- line: Yeah. No more hobbies.
  sec: 304
  time: '5:04'
  who: Yury
- line: If we ever have an episode about quantum computing, I know who to invite to
    talk about this.
  sec: 307
  time: '5:07'
  who: Alexey
- line: "I\u2019d invite more serious guys."
  sec: 315
  time: '5:15'
  who: Yury
- line: Okay. Did you find the work-life balance you were looking for?
  sec: 320
  time: '5:20'
  who: Alexey
- line: "Absolutely \u2014 here in the Netherlands they don\u2019t die at work and\
    \ I enjoy that."
  sec: 327
  time: '5:27'
  who: Yury
- header: 'Failing fast: Grammarly for science'
- line: "The topic today is \u201Cthings we don\u2019t share in our CVs\u201D. We\
    \ all have stories about failed projects. I have a couple and maybe I will even\
    \ tell one or two during today. But since you are the guest today, I will probably\
    \ first ask you for a couple of stories. One pattern I observed in my career is\
    \ that we as data scientists tend to spend a lot of time on projects that we did\
    \ not go anywhere. We work for a couple of months or something and then the project\
    \ turns out to be useless. We just waste time. Do you have any stories like that\
    \ in your experience?"
  sec: 335
  time: '5:35'
  who: Alexey
- line: "One of the recent stories is a side project for a proofreading service. If\
    \ you want to improve English in your paper, you can order this service. It\u2019\
    s pretty expensive. The project was to automatically assess the language quality\
    \ in a document. Like Grammarly, but more in the scientific domain. We already\
    \ had some solution when I joined. And I realized that the classifier that my\
    \ colleagues built was very close to noise. It was a binary classification of\
    \ whether an article is well written or badly written \u2014 that was close to\
    \ noise when accurately measured."
  sec: 382
  time: '6:22'
  who: Yury
- line: "The proofreading service had a large data set with original paragraphs and\
    \ then rewritten paragraphs \u2014 clumsy phrases are corrected. You can train\
    \ a sequence to sequence model that would rewrite the original sentence. But it\u2019\
    s rocket science \u2014 you cannot really expect such a sequence to sequence model\
    \ to produce a well-structured language. My colleagues worked on a binary classification\
    \ task, and I turned it into regression problems \u2014 you can measure some distance\
    \ between the pre-edited and the edited version of the text, for example, Levenshtein\
    \ distance. You can predict this distance with a BERT model \u2014 they provide\
    \ four or five fine-tuned language models. I run a couple of experiments with\
    \ a BERT regressor to predict this distance \u2014 how much a paragraph needs\
    \ to be edited."
  who: Yury
- line: "We organized a couple of annotation experiments between me and my colleague,\
    \ a American native speaker. We went through 50 examples each. The conclusion\
    \ was that our model is about 60% accurate, in terms of precision. The idea was\
    \ to highlight badly written paragraphs. Such a highlight would be just 60 percent\
    \ precise. Considering that it\u2019s a BERT model, which is just a black box,\
    \ I insisted on closing the project."
  who: Yury
- line: "The problem with the project was that it was prematurely advertised. The\
    \ company was waiting for a solution so hard. Even data scientists, my colleagues,\
    \ promoted this model like lacroix language quality assessment. They called it\
    \ lacqua brain, like introducing AI to your project. That was a silly thing to\
    \ do, you would not advertise your model so hard unless you know that it\u2019\
    s brilliantly good. It's just heating up this AI hype."
  who: Yury
- line: "It\u2019s a story about failing fast. I summoned all our product owners,\
    \ my boss and then recommended dropping any attempts to build such a service.\
    \ These are the things that are not done with one middle data scientist, one junior\
    \ data scientist, and maybe one senior. For this task you need a group of linguists.\
    \ The Grammarly team is pretty large, they have built their service in several\
    \ years. So, my recommendation was to use third-party tools."
  who: Yury
- line: "This actually was the opposite example \u2014 instead of spending a lot of\
    \ time on working on something for four or six months, you noticed it pretty early,\
    \ than you got all the stakeholders and you told them \u201CHey folks, this is\
    \ not going anywhere, let\u2019s stop it\u201D."
  sec: 642
  time: '10:42'
  who: Alexey
- line: "Exactly. That was a hard decision because it was my first months in the company.\
    \ Nobody knows me and I show up and say \u201CHey guys, we need to close this\
    \ project, it leads nowhere\u201D. I had to think this presentation through. I\
    \ spent the whole day creating this presentation \u2014 it was pretty important."
  sec: 666
  time: '11:06'
  who: Yury
- header: 'Not failing fast: Keyword recommender'
- line: "We have a comment from Pierre. Pierre is saying that that\u2019s why having\
    \ a data product manager is so important. They can say \u201Cthis is not useful\
    \ for us, we shouldn\u2019t spend time doing this\u201D."
  sec: 691
  time: '11:31'
  who: Alexey
- line: "I mentioned I also have a similar story. Back then we didn\u2019t have a\
    \ data product manager. If we had, maybe it would\u2019ve worked out differently.\
    \ I worked at a SEO company. SEO stands for \u201Csearch engine optimization\u201D\
    . In SEO, you have a website, and you want this website to rank for certain keywords\
    \ in Google. If you\u2019re selling some hardware. If somebody goes to Google\
    \ and writes \u201Cmonitors Berlin\u201D, you want to be the first there. That\u2019\
    s the idea behind SEO."
  who: Alexey
- line: "In that company we wanted to build a keyword recommended project. Let\u2019\
    s say we have a customer who has some keywords. We say \u201Cyou seem to be writing\
    \ about monitors, how about writing an article that would compare 4k monitors\
    \ versus 8k monitors\u201D. We\u2019d give suggestions for keywords to rank."
  who: Alexey
- line: "If you think about this, this is a classic recommender system. in a collaborative\
    \ filtering approach, so you have this huge matrix. You have rows which are your\
    \ users you have \u2014 in our case, it was the clients. Then the columns are\
    \ the items. In an e-commerce company, that could be phones. In our case it was\
    \ keywords. You put \u201C1\u201D in the cell if this customer uses this keyword.\
    \ You get this huge matrix and then you use things like alternating least squares\
    \ to factorize this matrix. This way, you encode the users and the items in a\
    \ certain vector space. Then you can compute similarity between these vectors\
    \ and items that could be interesting for this user."
  who: Alexey
- line: "This is all great in theory. We thought that it\u2019s straightforward, we\
    \ should follow this approach. We spent a couple of months training this model\
    \ \u2014 collecting the data, cleaning data, preparing it in the right format,\
    \ evaluating it, tuning it, trying different libraries. It was a lot of fun work.\
    \ This is what data scientists love to do. We really love doing this kind of work\
    \ \u2014 like Kaggle \u2014 especially when there is a good dataset. We had a\
    \ good dataset and we had really great evaluation metrics."
  who: Alexey
- line: "After a couple of months we show it to everyone. We say \u201CThis is so\
    \ cool, let\u2019s implement this\u201D. We go to the engineers who are supposed\
    \ to help us. They look at this and they say \u201CNo. There\u2019s no way we\
    \ are going to integrate this into the existing architecture\u201D. The problem\
    \ there was that the architecture was based on AWS Lambda.  Previously, there\
    \ was a very strict limitation on the size of your projects \u2014 it should be\
    \ below 50 megabytes, which is a pretty tough case considering how many different\
    \ libraries we had. It was very difficult. We spent a couple of months more, working\
    \ with engineers to reduce the size of this package. We even implemented some\
    \ things from scratch \u2014 we didn\u2019t want to depend on some libraries,\
    \ they were too heavy."
  who: Alexey
- line: "Finally we did it. And nobody wanted to use it. It was a great project, a\
    \ great idea. It was also an interesting engineering challenge which we overcame.\
    \ But then nobody needed it. And that was very sad. The customers didn\u2019t\
    \ need these recommendations."
  who: Alexey
- line: "In retrospect, what I would have done instead \u2014 I\u2019d spend a few\
    \ days and manually come up with these recommendations. I\u2019d select a sample\
    \ of a few clients. I\u2019d work with the domain expert \u2014 with some SEO\
    \ specialist \u2014 to suggest keywords for these clients. Then we\u2019d just\
    \ send emails to these customers \u2014 just to test if they\u2019d be interested\
    \ in these keywords. If we see that they are interested, it\u2019s good. We spent\
    \ a couple of days verifying it. If we see that they are not, we spent only a\
    \ couple of days doing this manual work. But it saved us months of work."
  who: Alexey
- header: Four steps to epiphany
- line: "I\u2019m currently reading a book called \u201CFour Steps to Epiphany\u201D\
    . It\u2019s on startups and their business models. They describe exactly this\
    \ problem: you think customers want something, but they don\u2019t. Some startups\
    \ cherish this product development model, but it doesn\u2019t work well for startups.\
    \ It\u2019s better to switch to the customer development model. They describe\
    \ this approach where you start with a trial group. You make sure that you are\
    \ creating a feature that these customers need and you are solving their pain.\
    \ Then you keep iterating."
  sec: 1006
  time: '16:46'
  who: Yury
- line: "And in this story, there is actually a very important skill \u2014 not to\
    \ use machine learning."
  who: Yury
- line: "I have not read this book, but I heard about this thing called \u201Cdesign\
    \ thinking\u201D. It\u2019s about what you mentioned \u2014 it\u2019s about thinking\
    \ of the customer first, going from the problem they have and validating things\
    \ as fast as possible."
  sec: 1060
  time: '17:40'
  who: Alexey
- header: Lesson learned when bringing XGBoost into production
- line: "One of the things I mentioned in my story was about the engineering part.\
    \ This is what we, data scientists, don\u2019t like. We like doing Kaggle, trying\
    \ different models, tuning parameters, and coming up with smart features. This\
    \ is fun, right? But when it comes to deploying models, when it comes to the engineering\
    \ part behind machine learning, then for many, it\u2019s not as fun."
  sec: 1080
  time: '18:00'
  who: Alexey
- line: I watched the talk you gave a couple of years ago. You worked in some advertising
    company and you had some issues with the serving layer. Maybe you can talk about
    this story? Can you tell us in more detail what happened there?
  who: Alexey
- line: Indeed! I had exactly the same problem. I kept iterating on improving the
    model while the problem was lying in a different place. As you can guess, it was
    in the infrastructure around the model.
  sec: 1144
  time: '19:04'
  who: Yury
- line: "When I switched from my PhD studies, I joined the Mail.Ru Group. For search,\
    \ everyone uses Google. But in Russia we have a great Google competitor, Yandex.\
    \ Mail.Ru is the greatest Yandex competitor, they also have a search system. Due\
    \ to morphology and all the different challenges of the Russian language, Yandex\
    \ is leading. It owes around 50% of the search market. Google is very close with\
    \ something like 47%. And Mail.Ru has the remaining 3%. But these 3% bring in\
    \ huge revenue, something like dozens of rubles \u2014 dozens or even hundreds\
    \ of millions of dollars per year."
  who: Yury
- line: "We had grading boosting for this search system. It\u2019s a highly optimized\
    \ C++ implementation of grading boosting. Bosting can do classification, regression\
    \ and ranking. With some specific losses, it\u2019s very good for ranking. We\
    \ had the task of content recommendations \u2014 we had several partners, websites\
    \ with different news. There are a lot of them, but you can show only 4 or 5 related\
    \ pieces. So it\u2019s an easy monetization scheme \u2014 you replace one of the\
    \ recommendations with an ad. Gradient boosting was very good in offline experiments,\
    \ in cross validation. But when deployed in production, in the online experiment,\
    \ it wasn\u2019t. We noticed that a heuristic was beating the gradient boosting\
    \ model."
  who: Yury
- line: "The heuristic was very simple. In content recommendation tasks, there is\
    \ a very strong baseline \u2014 CTR, click-through rate. You show some ad a hundred\
    \ times, you measure how many times it was clicked. Let\u2019s say it was 7, then\
    \ your CTR is 7%. If you rank all your content by CTR, it gives you a good baseline.\
    \ In reality you have to exclude nudity and other inappropriate content, but we\
    \ worked with partners, we were pretty sure that this content can be shown. Our\
    \ heuristic was mostly based on CTR. It was a weekly CTR with some trend we added\
    \ plus a monthly CTR with some small coefficient. We also broke it down into 10\
    \ age and gender groups. That was a fairly simple solution."
  who: Yury
- line: "I iterated on improving the model. I used active learning. I created different\
    \ features. I tried to improve the model itself, its architecture, hyperparameters\
    \ and so on. I was still in my PhD program, so I approached the problem as a machine\
    \ learning researcher. In 3-4 months, I realized that it\u2019s a high-load system.\
    \ The model was limited to 80 ms to make a prediction. If it fails, if it times\
    \ out, you cannot show a blank page, you have to replace it with some quick and\
    \ dirty solution. In these serious production systems, you always have a \u201C\
    last hope\u201D solution. It\u2019s a very reliable heuristics \u2014 like sorting\
    \ by CTR. On the weekend, when everyone is off, if the main production system\
    \ fails, this solution must work all the time. These things should work 100% reliably."
  who: Yury
- line: What happened is our grading boosting solution was timing out in many cases
    and it was replaced with this last hope solution. In the end, I tested not a grading
    boosting solution, but a mixture of grading boosting and this heuristics.
  who: Yury
- line: "When I fixed it, it skyrocketed. The fix was pretty simple. Initially we\
    \ were starting with CTR \u2014 we\u2019d rank the content by CTR and boosting\
    \ would just re-rank top 1000 documents. We replaced it with 300 \u2014 we only\
    \ re-ranking 300 documents. It was working exactly the same in terms of precision\
    \ and recall, but much faster. Now the project is bringing money and all is good."
  who: Yury
- line: "The lessons that I learned there. First of all, I spoiled my relationships\
    \ with a manager at this point. Four months was too much for such a project. We\
    \ already had a working solution, a nice grading boosting model and there was\
    \ pressure to deliver it earlier. At that time I launched a side project \u2014\
    \ this open machine learning course. I was a bit distracted. My personal lesson\
    \ learned was that sometimes you need to earn a reputation. You need to work hard\
    \ and focus on a single problem. Another conclusion was that you need to go beyond\
    \ your Jupyter notebook. In a project, go to your developers, backend, MLOps,\
    \ DevOps. Make sure you understand what\u2019s happening to the model at each\
    \ stage \u2014 from data collection to training to deployment. Understand the\
    \ entire life cycle of a model. It\u2019s also good to understand technical details,\
    \ to avoid problems related to infrastructure rather than to machine learning\
    \ itself."
  who: Yury
- line: So you had a smart model but most of the time it was replaced by a simple
    heuristic. You found out about that later. I guess you spent a lot of time trying
    to figure out what is going on. I imagine going through all these logs trying
    to figure out what is going on there.
  sec: 1525
  time: '25:25'
  who: Alexey
- header: When data scientists try to be engineers
- line: "These things are not easy for data scientists. Even though I previously worked\
    \ as a Java developer, it was difficult for me as well. The way I was doing things\
    \ was far from best practices. I would SSH to the \u201Cproduction\u201D server\
    \ and I\u2019d do \u201Cgit pull\u201D there. And I\u2019d have a special branch\
    \ called \u201Cproduction\u201D in my git. Everything in this branch was the \u201C\
    production\u201D code. Eventually I even set up a crontab to pull automatically\
    \ every minute, so I wouldn\u2019t need to SSH to the machine. Of course, there\
    \ was no CI/CD, so every time there was a bug, even simple things like syntactic\
    \ mistakes, the whole thing crashed. So I\u2019d need to SSH to the machine and\
    \ revert it. It was annoying."
  sec: 1556
  time: '25:56'
  who: Alexey
- line: At some point I left the company and somebody unfortunately needed to deal
    with all this mess. I heard many complaints. Eventually real engineers took it
    over and re-did everything with proper techniques like CI/CD. I have lunches with
    my colleagues from there, and they still complain. Did you have anything similar
    in your experience?
  who: Alexey
- line: "Exactly. When I switched teams in Mail.Ru Group, I joined a predictive analytics\
    \ group. Overall that was a very successful project. It dealt with marketing.\
    \ We had a business intelligence solution \u2014 an app which would create nice\
    \ dashboards with key marketing metrics: LTV, retention, monthly users, large\
    \ payments. It was related to mobile games and some of the tasks were to identify\
    \ \u201Cwhales \u2014 players who pay thousands of dollars per month. We had a\
    \ nice app for creating reports on these metrics. I was the first guy to introduce\
    \ predictions \u2014 as you create LTV reports, we would then create reports with\
    \ LTV predictions."
  sec: 1691
  time: '28:11'
  who: Yury
- line: "It\u2019s a funny experience. We had this startup vibe in a giant company.\
    \ I was the first guy to set up machine learning pipelines. So I was setting up\
    \ the \u201Cproduction\u201D. I started with a Jupyter notebook, created some\
    \ snippets, and then switched to PyCharm to create a nice project with object-oriented\
    \ programming, tests and so on."
  who: Yury
- line: "But then I\u2019d drop these predictions in a CSV file and another guy, backender,\
    \ would pick them up and rsync them (i.e. copy) to another server. We had very\
    \ similar issues. We had no CI/CD. If something didn\u2019t work, we\u2019d go\
    \ on SSH and fix problems in this production. This backender didn\u2019t like\
    \ us. He was cursing us, data scientists. We earned 50% more than him and it was\
    \ very annoying that he had to deal with all these issues."
  who: Yury
- line: "Then I moved to the Netherlands and I dropped the project. But I think now\
    \ it\u2019s successful, it\u2019s in active development. Now guys actually have\
    \ the best practices there with all the CI/CD, code reviews and so on."
  who: Yury
- line: You have to go through this experience, right? You have to do things incorrectly
    before you learn to do them correctly.
  sec: 1835
  time: '30:35'
  who: Alexey
- header: 'Joining a fintech startup: Doing NLP with thousands of GPUs'
- line: At the same time, I joined a fintech startup. One of the huge advantages of
    companies like Google, Facebook, LinkedIn, Uber is the network. In Russia these
    companies are Yandex and Mail.Ru and maybe Sber. There are many smart guys. At
    some point, one of the directors of a huge department took the course about ML
    I gave at Mail.Ru. And he invited me to join a fintech startup.
  sec: 1844
  time: '30:44'
  who: Yury
- line: They came up with an idea to sell Bitcoin in a mobile app. Such banks already
    existed in Europe, but in Russia they had to solve many legal issues. Revolut
    actually existed at that point already, it was built by Russians who then moved
    to Great Britain. They already solved these legal issues to sell Bitcoin in their
    mobile app. This startup was doing the same in Russia.
  who: Yury
- line: "And they bought 4,500 GPUs to mine Bitcoin. Then they realized that you need\
    \ special hardware to mine Bitcoin, the GPUs weren\u2019t cool anymore. They also\
    \ had this factory somewhere in the center of Moscow, but you need cheaper electricity\
    \ \u2014 you need to put these factories to hydroelectric stations somewhere far\
    \ away."
  who: Yury
- line: "They realized they had 4,500 GPUs. They needed to sell better, so they included\
    \ \u201CAI\u201D in their pitch decks. And that\u2019s why I was doing some \u201C\
    AI\u201D for their startup. From day one, I said \u201CNo, I\u2019m not going\
    \ to predict Bitcoin prices. I don\u2019t believe it\u2019s possible. If you have\
    \ a huge team of smark guys, maybe you can build something in 5 years, but I refuse\
    \ to do that alone\u201D."
  who: Yury
- line: "So I was working on sentiment analysis of Bitcoin news. The idea was to create\
    \ something like a \u201Csentiment barometer\u201D, which would show you the daily\
    \ sentiment around Bitcoin. I was playing around with some state-of-the-art NLP\
    \ solutions. That was before Hugging Face released their easy-to-use API. So,\
    \ I would fetch some GitHub repo and spend a day trying to launch something. Eventually\
    \ I managed to beat TF-IDF and logistics regression by 3%."
  who: Yury
- line: "Then the startup had troubles raising money and they decided they do not\
    \ need AI anymore. My solution didn\u2019t end up in production and it wasn\u2019\
    t bringing money. But that was actually a great experience."
  who: Yury
- line: I also learned that labeling can be prohibitively expensive. We had some Australian
    financial experts. We had a special telegram chat with 15 guys. It was fun just
    talking to them. They were labeling this data and that was prohibitively expensive.
    At some point, I switched to Mechanical Turk. I was also labeling some of the
    data myself. We also learned that you can spend too much money just labeling data.
  who: Yury
- line: It will still not be good enough.
  sec: 2076
  time: '34:36'
  who: Alexey
- line: Yeah.
  sec: 2079
  time: '34:39'
  who: Yury
- line: Do you know what happened with all these GPUs?
  sec: 2080
  time: '34:40'
  who: Alexey
- line: At some point they explored the idea to sell it to deep learning researchers.
    On one side you have all these miners with many GPUs and on another side you have
    got deep learning researchers who need cheap compute. You can build this bridge.
    I know one startup already did that. I think this startup also decided to rent
    GPUs. I do not know how they got rid of all these GPUs.
  sec: 2085
  time: '34:45'
  who: Yury
- line: "It\u2019s probably not so easy to get rid of them. That is a lot of GPUs.\
    \ Do you have this startup on your LinkedIn profile?"
  sec: 2118
  time: '35:18'
  who: Alexey
- line: "No. It was 4 or 5 months experience. I didn\u2019t mention them because I\
    \ don't want to hurt their marketing interests, so I don\u2019t want to mention\
    \ this startup."
  sec: 2146
  time: '35:46'
  who: Yury
- line: "Okay. That\u2019s one of the things that data scientists don\u2019t mention\
    \ on their CVs \u2014 small startups that mine bitcoins."
  sec: 2161
  time: '36:01'
  who: Alexey
- line: Exactly.
  sec: 2171
  time: '36:11'
  who: Yury
- header: Working at a Telco company
- line: Then you moved to the Netherlands and worked at a telecom company. Can you
    tell us more about what you did there?
  sec: 2172
  time: '36:12'
  who: Alexey
- line: "Yeah. I switched to NLP. In this telecom company, I worked with a huge dataset.\
    \ According to the definition of data mining, you have a large data set and you\
    \ want to find some useful signal there. We had exactly these problems. The Telco\
    \ operator had many chats, calls, emails with different complaints. There\u2019\
    s actually a lot of useful signals there. There are different problems reported\
    \ by chats, calls, emails. It was all in Dutch, so I used Google translate a lot\u2026\
    \ But you can imagine \u2014 people write that they are pissed off by some of\
    \ these services, they have some technical problems and so on. So I built a service\
    \ that would classify this into different broad groups, like \u201Cbilling\u201D\
    , \u201Cgeneral service\u201D, \u201Cchurn\u201D, \u201Ccustomer satisfaction\u201D\
    , and things like that. That was fun. I had to work with Dutch. At that time there\
    \ were no good pre-trained transformer models in Dutch, so we explored how we\
    \ can train a model in English and then run it with Dutch."
  sec: 2181
  time: '36:21'
  who: Yury
- line: "I worked in a data science department and it was not properly managed. Data\
    \ science for such a company was like a luxurious car. LIke Lamborghini \u2014\
    \ it\u2019s cool, expensive but what if you don\u2019t know how to drive it. It\
    \ was a challenge for the managers of this old company to manage us."
  who: Yury
- line: "We had one project which yielded revenue. It\u2019s called \u201Cbad debt\u201D\
    \ \u2014 it\u2019s very similar to credit scoring. When you go to a shop and you\u2019\
    d like to take a loan for a mobile phone, they run a scoring model."
  who: Yury
- line: "There was also a small cool story about this project. In my first days in\
    \ the Netherlands, I went to a KPN store to buy a mobile phone for my wife. iPhone,\
    \ of course. And their system rejected my application for the loan. The model\
    \ was built by my colleagues, so I went to them, and asked \u201CWhy was I refused?\u201D\
    \ I was literally able to go through the learned coefficients with shapley, visualize\
    \ them and understand why I was rejected. The killer feature was \u201Cresidents\
    \ permit\u201D. I had a temporary permit for less than one year. What scammers\
    \ typically do \u2014 they come to the Netherlands from some other country, take\
    \ hundreds of mobile phones in loans and then leave and sell these phones elsewhere.\
    \ So if your residence permit is shorter than one year, you can be rejected."
  who: Yury
- line: That was the project yielding revenue, several millions per year. That was
    a Card Blanche for us to do research to explore ideas. That was cool! I had a
    perfect team there. All the guys around me were so nice. The working style was
    so relaxed, especially after Russia. Friday is working from home.
  who: Yury
- header: Having too much freedom
- line: You were looking for work-life balance, right?
  sec: 2394
  time: '39:54'
  who: Alexey
- line: "Yes, I moved to the Netherlands for work-life balance. But we had too much\
    \ freedom. I used this time to do research. I also launched an initiative with\
    \ Amsterdam data science on exploring transfer learning in NLP. That was nice\
    \ because it led me to my new job. My would-be boss wrote an email to me, \u201C\
    I know you from Amsterdam data science. Would you like to join as a senior machine\
    \ learning scientist?\u201D"
  sec: 2396
  time: '39:56'
  who: Yury
- line: "Maybe it is a bit philosophical, but if you have too much freedom and you\
    \ are lacking some sense of impact, that\u2019s also not good for your motivation.\
    \ With all these lockdowns, I switched to another company."
  who: Yury
- line: "As a consequence, I now ask a question about that during job interviews.\
    \ The question is \u201CHow many projects yielding revenue do you actually have\
    \ running right now in production?\u201D"
  who: Yury
- line: What if they say zero? Then it is a red flag?
  sec: 2467
  time: '41:07'
  who: Alexey
- line: "Well, maybe yes. I like coming up with PoCs and doing research, but at the\
    \ same time I don\u2019t want to feel this lack of impact."
  sec: 2474
  time: '41:14'
  who: Yury
- line: "I liked your metaphor about a luxurious car that is cool but expensive. It\u2019\
    s probably not easy to find people in management who know how to drive this car.\
    \ Especially in more traditional companies, like telecom companies. What I often\
    \ see \u2014 these companies work with consultants like McKinsey, BCG or others.\
    \ The consultants say, \u201CYou don\u2019t seem to be doing AI, but you should\
    \ be. Hire us and we will tell you how.\u201D They hire these consultants. Then\
    \ the consultants say, \u201CYou need to hire 2-3 data scientists\u201D. So they\
    \ hire them. The consultants are very expensive, so companies end their contracts\
    \ with them. And now a company has 2-3 data scientists and needs to figure out\
    \ what to do with them. I didn\u2019t personally experience that, but I heard\
    \ these stories from other people."
  sec: 2488
  time: '41:28'
  who: Alexey
- line: In the end, most of these projects were not successful. People would just
    be left alone with a lot of freedom. They would spend some time playing Kaggle.
    But you can only play Kaggle so much. You can do it for 2-3 months, but then you
    start feeling bad about doing this at work.
  who: Alexey
- header: The importance of digital presence
- line: "We actually have a question from Wahid. It\u2019s not related to our topic\
    \ today, but I\u2019m curious to know your take on that. We already talked about\
    \ Kaggle \u2014 doing this at work when your company doesn\u2019t know how to\
    \ keep you busy. The question is, how important is it to have a digital presence\
    \ for landing a data science job? Something like GitHub pages, a personal data\
    \ science blog, active Twitter account, Kaggle and things like this."
  sec: 2600
  time: '43:20'
  who: Alexey
- line: "I wouldn\u2019t say it\u2019s of critical importance, but it\u2019s a good\
    \ additional feature. The most important part in an interview is being able to\
    \ describe your projects and the impact in those projects. It gets more and more\
    \ important as your role matures. When you are a junior, you might be challenged\
    \ to write a Fibonacci generator or take a derivative of some crazy function.\
    \ But as you mature, they get more interested in how you can change the company\
    \ and the processes. That\u2019s why it\u2019s good to show your experience from\
    \ other projects. Especially if you changed the way the company runs some processes.\
    \ That\u2019s very important to describe it."
  sec: 2629
  time: '43:49'
  who: Yury
- line: "So the first exercise I\u2019d recommend to everyone is just to go through\
    \ your LinkedIn profile and just analyze your past experience. Be able to describe\
    \ your projects in detail. Using active verbs. I think Google has a nice instruction\
    \ on how to reflect these in your CV. State what was your role in the project."
  who: Yury
- line: "I still think this is important. My public activities helped me a lot \u2014\
    \ like having an open machine learning course and having a GitHub repo with 7000\
    \ stars would not hurt."
  who: Yury
- line: I cannot imagine the scenario where it would hurt. Well, maybe I actually
    can. You mentioned that one of your managers was not really happy about that when
    you had an important project at work.
  sec: 2723
  time: '45:23'
  who: Alexey
- header: Work-life balance
- line: "Indeed. There is a very subtle trade-off. I always kept a couple of hours\
    \ per day for any creativity \u2014 reading blogs, writing blogs and things like\
    \ that. For me, it\u2019s also a way to avoid burnouts. Honestly, I am not fascinated\
    \ with the idea of working hard for the company. Why would you?"
  sec: 2735
  time: '45:35'
  who: Yury
- line: "Let\u2019s hope nobody from your current managers is listening to that. Oh,\
    \ your current managers are from the Netherlands. They take these things easy\
    \ in Europe and care about work-life balance."
  sec: 2761
  time: '46:01'
  who: Alexey
- line: "Maybe some of my colleagues will also listen to this. But anyway I understand\
    \ if you work 12-14 hours per day for your own startup. If you believe in that,\
    \ if you think it\u2019s revolutionary. You still have little chance to rocket\
    \ with this startup. But I understand that if you work for your own startup, you\
    \ can live at work. But I honestly don\u2019t understand putting so much effort\
    \ into someone else's company. Unless you are motivated with some stocks, it makes\
    \ sense. That\u2019s why I always leave a couple of hours per day, knowing that\
    \ I would be distracted by some cool stuff like reading about causal inference\
    \ or quantum machine learning or things like that."
  sec: 2773
  time: '46:13'
  who: Yury
- line: "One more hack \u2014 arrange a meeting with yourself every day from 9 am\
    \ to 1 pm. You create a meeting with yourself, and it\u2019s your focus time.\
    \ Sometimes, of course, you have important meetings and you are asked to reschedule.\
    \ But most of the time you can do your stuff. As a data scientist you can go into\
    \ code. I used the time also to work a bit on my side projects, on my public activities,\
    \ blogging, shooting videos and so on. Indeed I had a negative experience with\
    \ that as well. When I worked at Mail.Ru, I was maybe too involved in running\
    \ this open machine learning course. My main task at work suffered. So there is\
    \ a very subtle trade-off here."
  who: Yury
- line: "But I certainly recommend having some public activities and nice talks. If\
    \ you have solved some problem with A/B tests, share your experience. If you can\
    \ describe all the nitty-gritty details, the caveats and how you resolve the issues\
    \ \u2014 that might be very valuable. If you create 5-7 talks like that, you can\
    \ already be recognized within closed circles. That would definitely help. But\
    \ it\u2019s really hard to put a label on how valuable that is in terms of money.\
    \ It\u2019s very personal."
  who: Yury
- line: "It just gives you a lot more opportunities that you otherwise would have.\
    \ If you want to measure this in terms of money, then the next time you change\
    \ a job, you can get a higher salary bump. You can just apply for a job and then\
    \ you will get a job. But if you have some online presence, people will recognize\
    \ you. Then you can ask for more money. Then this is how you can measure it. Of\
    \ course, to do a proper evaluation, you\u2019d need to run an A/B test. You need\
    \ to take a group of people who don\u2019t have public activity, a group of people\
    \ who have public activity and then make them change their jobs. And then see.\
    \ Running this experiment would probably take some time. But my gut feeling is\
    \ that it helps."
  sec: 2907
  time: '48:27'
  who: Alexey
- header: Quantifying impact of failing projects on our CVs
- line: "You mentioned that you should go through your LinkedIn profile, take your\
    \ projects, and try to quantify the impact you had in these projects. But what\
    \ if these projects had a negative impact? You wasted six months of time working\
    \ on something that resulted in nothing. And you decided that you want to look\
    \ for a new job. That's the kind of thing we don\u2019t mention in our CVs, right?\
    \ I wouldn\u2019t say on my CV that I wasted so much time on my company working\
    \ on this project that resulted in nothing. I don\u2019t become more attractive\
    \ by saying that. Do you have any recommendations on how we can qualify our impact\
    \ when our projects are not that great?"
  sec: 2970
  time: '49:30'
  who: Alexey
- line: "All the stories that we share here are about inconvenient truths. LinkedIn\
    \ profile is about self-promotion. It pursues some marketing goals \u2014 which\
    \ is a euphemism for \u201Clying\u201D. Let\u2019s say \u201Cself-promotion\u201D\
    , to make it more politically correct. It\u2019s not lying, but it\u2019s not\
    \ 100% truthful either."
  sec: 3046
  time: '50:46'
  who: Yury
- line: "But I think it\u2019s worth mentioning a negative experience. You can still\
    \ sell it. The next time I\u2019m in an interview, I\u2019d describe this language\
    \ quality project where I made a decision to close the project while it\u2019\
    s not too late."
  who: Yury
- line: First, I have a gut feeling that not so many candidates describe such negative
    experiences. This can help you show off a bit by describing the negative projects.
  who: Yury
- line: "But if you just want to put it on LinkedIn, then you don\u2019t need to be\
    \ very specific about all the financial goals in the projects and things like\
    \ that. Just describe it in general. I have some on my LinkedIn profile and I\
    \ also have some pretty general descriptions \u2014  because of all the issues\
    \ discussed here. Just be sure that when you talk with your  next potential employer,\
    \ you can defend this project and you can share the lessons learned from the project."
  who: Yury
- header: "Business trips to Perm: don\u2019t work on the weekend"
- line: We still have some time left. Maybe you have one or two stories you want to
    share.
  sec: 3161
  time: '52:41'
  who: Alexey
- line: "I have a couple more funny projects. They get us back to my youth. I don\u2019\
    t like business trips. So I can share a story about my job with a Russian system\
    \ integrator. In my master's, I joined a company \u2014 an Oracle partner in Russia.\
    \ They had a very primitive monetization scheme. Half of their revenue came from\
    \ reselling Oracle licenses. Many small companies across Russia who want to collaborate\
    \ with Oracle went through this system integrator and bought the licenses. Another\
    \ 49% of the revenue was coming from a corporate studying center. They gave courses\
    \ on database management, Java and so on. And only 1% of all the revenue came\
    \ from the actual development. That\u2019s approximately the role of data science\
    \ in general in business, just 1% of the whole revenue. I was still a student,\
    \ and I spent more than a year in a corporate center. I need to be grateful to\
    \ this employer, they invested a lot in me. I studied a lot of things, even Hadoop."
  sec: 3175
  time: '52:55'
  who: Yury
- line: "But when I joined the actual projects, I went to Russian city Perm. It\u2019\
    s almost Siberia, it\u2019s very close to the Ural mountains that separate Europe\
    \ from Asia. Perm is a bit to the east from the Ural mountains. It\u2019s where\
    \ Siberia starts. So I went on a business trip there."
  who: Yury
- line: "I worked as a business intelligence architect, so the work itself was actually\
    \ pretty good and sometimes challenging. You work with a corporate data warehouse\
    \ and you need to build some logic around the warehouse. The final goal is to\
    \ make reports easily with a couple of clicks \u2014 you create a nice dashboard\
    \ that you show to your manager, CEO or anyone. I needed to think a lot."
  who: Yury
- line: "But I needed to go on business trips. It was really crazy. They sent us to\
    \ Perm in winter, when it\u2019s -30. The project manager didn\u2019t take into\
    \ account that we live in a hotel during the weekend. So their financials weren\u2019\
    t actually thought through well. So they just made us work during the weekends\
    \ as well. There was a taxi that would pick us up at 7:30 a.m. It\u2019s -30 and\
    \ windy, so we jump into the taxi, the taxi drives us to the company. Then we\
    \ sit there till 8 p.m. Then another taxi takes us back to the hotel. You don\u2019\
    t see the sun at all."
  who: Yury
- line: "I had three business trips like that. One of them was just three weeks in\
    \ a row, with weekends, so 21 days in a row. At some point I said \u201CNo. I\
    \ don\u2019t care\u201D. After spending Saturday at work, I got a hockey stick\
    \ and played ice hockey with guys from Perm. I just said \u201CNo, I\u2019m not\
    \ working on Sunday\u201D. I could have been fired, but I didn\u2019t care."
  who: Yury
- line: "The lesson I learned is that you need to be careful with business trips.\
    \ I also have a feeling that you have to work more on a business trip, to satisfy\
    \ your customer. To be honest, I just don\u2019t enjoy this business model where\
    \ you have to satisfy your customers. Data science projects are very risky. You\
    \ always have a risk that the project is not profitable. Then you gradually turn\
    \ into your customer's slave. I don\u2019t like that feeling."
  who: Yury
- line: "As for business trips, maybe someone would argue that it\u2019s a way to\
    \ explore the country, see the world. I know your company belongs to Naspers.\
    \ We have their headquarters here in Amsterdam. I know a guy from this company.\
    \ It\u2019s a crazy lifestyle. One week you are in Brazil, another week you are\
    \ in Guinea, then you go to Russia. It\u2019s very challenging for your work-life\
    \ balance."
  who: Yury
- line: "Now things are different. They don\u2019t need to travel that much. Thigs\
    \ are in zoom anyways. But maybe next year the life will get back to normal and\
    \ they are back on the plane again."
  sec: 3495
  time: '58:15'
  who: Alexey
- line: They will get back to their normal.
  sec: 3511
  time: '58:31'
  who: Yury
- header: "What doesn\u2019t kill you makes you stronger"
- line: "Maybe somebody will not. It\u2019s time to wrap up. Do you have any last\
    \ words before we finish?"
  sec: 3516
  time: '58:36'
  who: Alexey
- line: "I wanted to say that these failures are fine \u2014 unless you are fired.\
    \ I think it\u2019s a very nice experience. It\u2019s good to understand that\
    \ all the people around you \u2014 they are not robots. They are not bringing\
    \ millions every year to their companies. It\u2019s important to understand that\
    \ they also have their failures. It\u2019s good for your self-esteem. At the same\
    \ time these failures are very important. It\u2019s okay to make mistakes. You\
    \ can listen to talks like this one, but it\u2019s important to feel it with your\
    \ own skin. What doesn't kill you makes you stronger."
  sec: 3526
  time: '58:46'
  who: Yury
- line: Right. So you have to try doing these things, SSH into your production environment
    and then deploy things through Git, to know how good things can feel like when
    you do it properly. Well, I am not recommending doing this actually, but by doing
    this you see the benefits of doing things the right way.
  sec: 3589
  time: '59:49'
  who: Alexey
- line: "I can only wish you good failures that don\u2019t make you leave the company."
  sec: 3616
  time: '1:00:16'
  who: Yury
- line: How can people find you?
  sec: 3624
  time: '1:00:24'
  who: Alexey
- line: Twitter.
  sec: 3630
  time: '1:00:30'
  who: Yury
- line: I will put this in the description. Thanks for finding time to join us today.
    I know you have a tight schedule. This is the third talk you gave today. I imagine
    that now you want to take some rest from talking and drink some hot tea. Thanks
    for talking about these things. Not everyone would be comfortable talking about
    failures. Also thanks everybody for joining us today and for watching our chat
    with Yury.
  sec: 3635
  time: '1:00:35'
  who: Alexey
- line: My pleasure! Thanks for having me.
  sec: 3687
  time: '1:01:27'
  who: Yury

---


Links:

- [Yury's course](https://mlcourse.ai/){:target="_blank"}
- [Yury's Twitter](https://twitter.com/ykashnitsky){:target="_blank"}