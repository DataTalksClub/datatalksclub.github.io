---
title: "Humans in the Loop"
short: "Humans in the Loop"
guests: [linaweichbrodt]

image: images/podcast/s04e06-humans-in-the-loop.jpg

season: 4
episode: 6

ids:
  youtube: o50j_Ndx2Hg
  anchor: Humans-in-the-Loop---Lina-Weichbrodt-e14npgp

links:
  youtube: https://www.youtube.com/watch?v=o50j_Ndx2Hg
  anchor: https://anchor.fm/datatalksclub/episodes/Humans-in-the-Loop---Lina-Weichbrodt-e14npgp
  spotify: https://open.spotify.com/episode/23VxmAEkKUs1kjaludRQAR
  apple: https://podcasts.apple.com/us/podcast/humans-in-the-loop-lina-weichbrodt/id1541710331?i=1000530535704

transcript:
- line: Today, we will talk about the human aspect in ML Ops. We have a special guest
    today, Lina. Lina has over nine years of industry experience in developing scalable
    machine learning models and bringing them into production. She currently works
    as a machine learning lead engineer in the data science group of the German online
    bank, DKB. Previously, she worked at Zalando, which is one of the biggest European
    online fashion retailers, where she worked on a personalization model. It was
    a real-time deep learning presentation model for more than 32 million users. Now
    it's more, right?
  sec: 122
  time: '2:02'
  who: Alexey
- line: "Yes. It\u2019s constantly growing. Zalando is popular."
  sec: 194
  time: '3:14'
  who: Lina
- line: Yeah. Welcome.
  sec: 197
  time: '3:17'
  who: Alexey
- line: Thank you for having me.
  sec: 198
  time: '3:18'
  who: Lina
- header: "Lina\u2019s background"
- line: Before we go into our main topic, let's start with your background. Can you
    tell us about your career journey as well?
  sec: 201
  time: '3:21'
  who: Alexey
- line: "Yes. Originally, I was very entrepreneur-minded and I started to study business.\
    \ I got hooked onto programming and basically never left. I moved over to computer\
    \ science. Since then, I've worked a little bit as an architect at Zalando, which\
    \ was very nice \u2013 it\u2019s an international, big, ambitious company with\
    \ an awesome tech culture. Since a year I've been working at DKB. Basically, have\
    \ a bit of a business mind, and I also come from web analytics and an online marketing\
    \ background. I always have a very customer-centric viewpoint on things. I think\
    \ it\u2019s interesting to marry ideas from customer orientation into engineering."
  sec: 209
  time: '3:29'
  who: Lina
- line: That's how you know all this marketing stuff that we talked about.
  sec: 259
  time: '4:19'
  who: Alexey
- line: Yeah, basically. These are sort of my pet projects and interests - how engineering
    can get inspired by different disciplines.
  sec: 266
  time: '4:26'
  who: Lina
- line: Okay. You said you worked as an architect at Zalando, correct?
  sec: 277
  time: '4:37'
  who: Alexey
- line: No, that was before. At Zalando, I worked as a research engineer.
  sec: 283
  time: '4:43'
  who: Lina
- header: What we need to remember when starting a project (checklists)
- line: Okay. Today, we're talking about humans in loop and keeping people in the
    loop. When we start a project, what important things do we need to remember? What
    is the checklist that we need to go through before we do this?
  sec: 290
  time: '4:50'
  who: Alexey
- line: "What I've observed over the last year is that there are no best practices\
    \ as of yet regarding what makes a good machine learning model. That means it\
    \ can be useful to apply certain checklists to help your stakeholders a little\
    \ bit or when you come up with your own ideas. It will help you if you have a\
    \ framework so that you can see \u201CDoes this make a good ML project?\u201D"
  sec: 314
  time: '5:14'
  who: Lina
- line: "One thing I found quite useful is to write down the business case and check\
    \ it with a stakeholder. The stakeholders sometimes use AI and they think, \u201C\
    Ooh, this is cool \u2013 a self-learning system that will solve anything.\u201D\
    \ So they see it as more of an automated human than a mathematical problem-solving\
    \ engine. What I've found useful is to formalize the business case with them in\
    \ the form of a user story and make sure I really understand what they want. Sometimes\
    \ they think in terms of the solution, they say, \u201COh, yeah. Make it better.\u201D\
    \ They don\u2019t really specify how, because they somehow think AI doesn't need\
    \ a proper business case, but it does. Therefore, I need them to formalize \u201C\
    How do they measure success? What is being optimized? What is the current way\
    \ of doing it? Which kind of improvement would make it worth doing the project?\
    \ Are you looking at 10%? Would a 10% improvement make it worth having an AI model\
    \ there? And did you consider other solutions besides AI models?\u201D"
  who: Lina
- line: "Also make sure that they don't fall into the trap of hearing about \u2018\
    cool new AI technology\u2019 and thinking about where they can use it. For my\
    \ practice at Zalando people may say something like, \u201COkay, we want a personalized\
    \ recommender system that does this and this.\u201D So I say, \u201COkay, but\
    \ what problem do you need that tool for?\u201D So it can sometimes turn out like,\
    \ \u201COkay, I have a cool new hammer \u2013 I will hit any nail with it and\
    \ the outcome will be amazing!\u201D It's better when they come to you with a\
    \ business problem. For example, \u201CWe have a new in-carousel or a new in-section\
    \ with a lot of articles. We don't know which articles to present to the user.\u201D\
    \ Okay, this is easy. With this problem, I can then figure out how to at least\
    \ title this recommendation solution."
  who: Lina
- line: So basically, I recommend that you have a checklist that you go through to
    make sure that none of these steps are skipped and that you adhere to a really
    good business case. Have KPIs and have evaluated alternative solutions to make
    sure that you're all on the same page.
  who: Lina
- line: "The other thing is, sometimes they kind of use you for very experimental\
    \ ideas, \u201CAh, do you're the AI team. Can you do a something something prototype?\u201D\
    \ And this prototype is not actually their core business. Therefore, I would always\
    \ insist on them having or providing core values. That\u2019s because in the end,\
    \ if it doesn't work, it's not that bad for them. They will not invest a lot of\
    \ time into your project. So make sure them have some skin in the game. You want\
    \ something that is core to their business when you select a project \u2013 something\
    \ that really makes a difference for them if you solve it. In cases where your\
    \ group works with another part of the company, ideally, you would also ask them,\
    \ \u201CWill you give me someone from your department?\u201D \u201CWill you give\
    \ me the capacity for this?\u201D Because if they're not willing to do that, chances\
    \ are \u2013 it's not that important to them. Or you need to go one step higher\
    \ to get the buy-in. When all is said and done, if you do this (even if it works)\
    \ then it just works, but they do not have a buy-in or the higher ups in this\
    \ area don't have a buy-in. Therefore, you will either not be able to successfully\
    \ bring it into production or you will have no engagement from the stakeholders\
    \ on the other side when you want to actually run the thing. That\u2019s why you\
    \ need to have a checklist of all these things \u2013 that\u2019s what makes a\
    \ good project."
  who: Lina
- line: "So the checklist is \u2013 I hope I didn't miss anything \u2013 first, you\
    \ need to formalize your project in the form of a business story. So you don't\
    \ say \u201CI'll just make it better.\u201D You need to formalize success \u2013\
    \ \u201CHow is success measured?\u201D \u201CWhat kind of improvement are we talking\
    \ about? Is it a 10% improvement or 5%?\u201D \u201CIf we improve it by 5%, is\
    \ it worth the effort or not?\u201D"
  sec: 555
  time: '9:15'
  who: Alexey
- line: "Don\u2019t forget \u2013 \u201CDo you even need AI?\u201D Some things really\
    \ do not need the AI to be involved. Sometimes stakeholders cannot understand\
    \ the difference between something like a personalized pipeline or just a data\
    \ pipeline which puts some stuff together. To them that's already an AI model.\
    \ We know difference. So, you need to quantify alternatives."
  sec: 583
  time: '9:43'
  who: Lina
- header: Make sure the problem is formalized and close to the core business
- line: "You also said, \u201CYou need to be specific about the business problem that\
    \ you're solving.\u201D So it's not just \u201CHey, do something cool. Here's\
    \ this idea.\u201D Instead it should answer \u201CWhat business problem does this\
    \ solve?\u201D \u2013 and the closer the answer is the core business, the better.\
    \ If it's just some cool thing that some executive read about, then it might not\
    \ be worth doing."
  sec: 604
  time: '10:04'
  who: Alexey
- line: "Sometimes I have colleagues who come up to me and say \u201COh, this is so\
    \ cool. We should do a new algorithm.\u201D But in real life, it rarely gives\
    \ a successful product. In the end \u2013 you cannot explain it, you cannot give\
    \ it a title, it's hard to find the UI, etc. You get a lot of edge cases if you\
    \ do not have a good business problem. Let's say \u201CI have new products and\
    \ I want to rank them in a certain way.\u201D That gives me lots of ideas for\
    \ how to think of edge cases. But if you have a very unspecific problem, for example,\
    \ \u201CPersonalize the ranking,\u201D then you will have a lot of weird outcomes\
    \ that are very hard to fix when you want to run it. So the more specific the\
    \ problem is, the easier it is for you to constrain it \u2013 to give it meaning\
    \ \u2013 and have a successful outcome that everybody's happy with."
  sec: 626
  time: '10:26'
  who: Lina
- line: "If it's formalized, you can clearly visualize it. You can see the UI. Maybe\
    \ you can even come up with some sort of mock up for the product. When you have\
    \ this understanding \u2013 when you have this visualization, (even if it's in\
    \ your mind) \u2013 then it's easier to imagine all these corner cases, right?"
  sec: 677
  time: '11:17'
  who: Alexey
- line: Yes.
  sec: 697
  time: '11:37'
  who: Lina
- line: "And the last thing you said \u2013 you need to get a buy in, which means\
    \ you need to have somebody from the business team (from the stakeholders) engaged\
    \ in the project. They need to make somebody available for your questions. Maybe\
    \ if you have a demo, you want to show it to them. So you need somebody available\
    \ for that. If they don't give you this person \u2013 if there is no point of\
    \ contact \u2013 then maybe they don't really care about this project."
  sec: 698
  time: '11:38'
  who: Alexey
- line: Exactly.
  sec: 726
  time: '12:06'
  who: Lina
- line: Did I miss anything?
  sec: 727
  time: '12:07'
  who: Alexey
- line: No, those are the main points. There are more points. There are some cool
    checklists on the internet that I can recommend to you. But the aforementioned
    points are some of the most overlooked, that's why I mentioned them. I recommend
    that you write yourself a personal checklist.
  sec: 729
  time: '12:09'
  who: Lina
- header: Get the buy-in with stakeholders
- line: This is before you even start doing anything, right? You have an idea about
    something cool, you sit down, and you spend some time in front of a Google document
    or Word document, or maybe just a notepad. You try to write everything down, you
    share it with your colleagues, with your stakeholders, and you need to get this
    buy in before you do anything.
  sec: 742
  time: '12:22'
  who: Alexey
- line: I also recommend that you pair with them. In order to really understand the
    domain and the problem, it's a good idea to spend half a day on that. Usually
    we're going after important projects, right? There's rarely a low hanging fruit
    ML solution. Therefore, it's also worth sitting down with them. Then you may find
    that you had some misunderstandings about the problem, for example.
  sec: 772
  time: '12:52'
  who: Lina
- line: "Maybe I'm asking a question that you already answered, but the question is,\
    \ \u201CHow do we communicate?\u201D One thing you said is \u2013 just go and\
    \ sit with them for half a day. But I think it's difficult to do that sometimes.\
    \ Let's say I'm a data scientist \u2013 how do I even talk to these business people?\
    \ They speak a completely different language. They care about things I don't care\
    \ about. I care about logistic regression, while they care about profit and things\
    \ like that."
  sec: 798
  time: '13:18'
  who: Alexey
- line: "I mean, it depends a little bit on how evolved they are. If you have a very\
    \ well-functioning business team that knows about user stories and knows the KPIs,\
    \ you can just tell them, \u201CYou don't need to know anything about machine\
    \ learning. In fact, it's better if you don't. Just describe the problem to me\
    \ in your terms.\u201D They can prepare a document and then you can sit together\
    \ and you ask your questions. If it's a stakeholder team that is not as well-educated\
    \ on user stories or how to write a good business case, you need to go sit with\
    \ them for longer. Basically, you need to find out the business case together\
    \ with them. So it depends, I would say, on how mature they are."
  sec: 827
  time: '13:47'
  who: Lina
- header: Building trust with stakeholders
- line: "What can we do to actually build trust between us? They don\u2019t always\
    \ trust us from the very beginning. I think in order to have good communication\
    \ with stakeholders, they need to trust us and we need to trust them. If we speak\
    \ a different language, then they don't understand us and we don't understand\
    \ them \u2013 we don't have this trust. So how can we actually gain it?"
  sec: 877
  time: '14:37'
  who: Alexey
- line: "Yes. I also find that quite challenging. There are probably books on how\
    \ to develop stakeholder reputations. I have a very good book recommendation \u2013\
    \ if you guys care to know about it \u2013 There's Rebels at Work, it's called.\
    \ It's about leading change from within. It's basically full of ideas on how to\
    \ convince people \u2013 if you have innovative ideas, how to convince other people\
    \ of that. In general, I found it useful to not talk so much about what I can\
    \ do for them, but to first understand their domain."
  sec: 907
  time: '15:07'
  who: Lina
- line: "Also maybe help them with some of their data problems that are unrelated\
    \ to my project. Sometimes they ask me data questions that are unrelated to my\
    \ project and I make myself available and can be a sort of \u2018trusted expert\u2019\
    \ to them. That, of course, is only useful if you plan on working with them in\
    \ the long-term, but that's a pretty good way to gain trust."
  who: Lina
- line: "When I first talk to them, I not only focus on the upsides \u2013 I also\
    \ focus a lot on their concerns. When we talk about the business case, I am pretty\
    \ sure that most of these concerns are actually not valid. They may come to me\
    \ and say, \u201COh, this is gonna be slow.\u201D And I explain, \u201CNo, it's\
    \ not going to be slow. It's going to be really fast.\u201D But maybe they\u2019\
    ve had some bad experiences, so I do not judge their technical knowledge, or lack\
    \ thereof. Instead, I tell them something like, \u201COkay, what do you think\
    \ definitely shouldn't happen when we introduce a very intelligent solution here?\u201D\
    \ And they talk about all kinds of fears they have like, \u201COh, it could be\
    \ very slow!\u201D Or \u201CWeird things could drop entire cases.\u201D"
  who: Lina
- line: "We also had concrete concerns come up in these fears. For example, when I\
    \ was optimizing process costs, they were saying, \u201CBut please, it should\
    \ not reduce our sales. If you reject people because of certain process cost optimization,\
    \ we do not want the overall sales volume to be rejected.\u201D Then some people\
    \ who had more of an idea about how algorithms work stepped in and added, \u201C\
    Okay, if it only learns from the past, what happens if we want to change something\
    \ in the future? Are we then unable to change the logic?\u201D So they're asking\
    \ questions like this, which I would never address when I pitch the project to\
    \ them."
  who: Lina
- line: "The whole time you're focusing on the upside \u2013 you're pitching your\
    \ cool idea \u2013 but they're sitting there and they don't have space to express\
    \ their concerns. This makes them not want to buy into your solution, because\
    \ their basic questions have not been answered. We can also take a page from the\
    \ book of marketing. When you come to a really good website, they do not sell\
    \ you only on the upsides of a product; they also tell you what it's not. For\
    \ example \u201CIt's good quality\u201D because you may be worried that it could\
    \ be cheaply made \u2013 all that kind of stuff."
  who: Lina
- line: "Or another example \u2013 \u201CNo credit card required.\u201D When I see\
    \ that something is free, I think \u201COkay, but they are probably sneakily going\
    \ to charge me after the free trial is over.\u201D"
  sec: 1098
  time: '18:18'
  who: Alexey
- line: "Sometimes they say \u201CNo extra charges.\u201D Basically it's a similar\
    \ process. That\u2019s why I'm don\u2019t only ask them about what they want to\
    \ achieve, but also the constraints, \u201CIt should not be that. I'm worried\
    \ about that.\u201D I make these concerns into slides and for each, I write down\
    \ what I\u2019m going to do to address it. Then they feel very good about it.\
    \ They feel that they\u2019re being taken seriously and that I'm not doing something\
    \ over their heads. All their concerns are addressed and then you move on to the\
    \ actual solution."
  sec: 1109
  time: '18:29'
  who: Lina
- header: "Don\u2019t just focus on upsides \u2013 ask about concerns"
- line: "Basically, when you pitch ideas, you don't just focus on the upsides. You\
    \ also ask them, \u201CWhat kind of fears you have?\u201D"
  sec: 1142
  time: '19:02'
  who: Alexey
- line: "I don\u2019t call it \u201Cfears\u201D so that they don't feel condescended\
    \ to. That's a bit of risk. You want to meet them on their level. You don't want\
    \ to talk down to them. You're peers \u2013 they know their stuff, you know your\
    \ stuff. You ask them \u201CWhat are your concerns?\u201D Or \u201CWhen we develop\
    \ a solution, what is something you definitely want us to avoid?\u201D More along\
    \ those lines."
  sec: 1153
  time: '19:13'
  who: Lina
- line: "\u201CWhat should we avoid?\u201D"
  sec: 1177
  time: '19:37'
  who: Alexey
- line: "Right. You need to ask them things like, \u201CWhat should we avoid?\u201D\
    \ \u201CWhat is your worst case scenario?\u201D \u201CIf something goes really\
    \ wrong, what do you definitely want us to avoid?\u201D That is also very useful\
    \ for us to know because we find out what their worst fears are. For example,\
    \ we were developing customized OCR for incoming invoices that are scanned. We're\
    \ thinking, \u201COf course that should produce good quality output. The text\
    \ part, the supplier part \u2013 it automatically gets put into SAP.\u201D And\
    \ we're thinking, \u201COkay, this should work well, high accuracy, blah, blah,\
    \ blah.\u201D"
  sec: 1180
  time: '19:40'
  who: Lina
- line: "And they were like, \u201CYou should never lose an invoice.\u201D It didn't\
    \ even occur to us that we could lose an invoice. But they insisted, \u201CYou\
    \ shouldn't lose an invoice.\u201D Basically, A) We know that they're worried\
    \ about that. That is helpful information. B) We can make sure we go through each\
    \ step and say, \u201COkay, what's our scenario if it fails?\u201D Let's say we\
    \ fail to read an invoice. \u201CWhat do we actually do in the OCR? Does it get\
    \ stuck there? Is there a retry? What if it fails permanently?\u201D So this approach\
    \ also helps us to think of our user stories. We make this \u201CWe should not\
    \ lose an invoice\u201D into a user story."
  who: Lina
- line: "Then we go through the different steps. We maybe even make it into a metric\
    \ \u2013 we have \u2018incoming invoices\u2019 and \u2018outgoing invoices\u2019\
    \ and we set up an alert that takes the difference between those two, which should\
    \ be zero. This way, we have something to show them and we also make sure that\
    \ we can proactively avoid their worst case scenario. Because if you do their\
    \ worst case scenario even once \u2013 maybe you don't even realize that you did\
    \ it \u2013 they will call you, \u201CYou know this invoice, the customer called\
    \ \u2013 we never paid it. Where is it?\u201D And we can only respond, \u201C\
    Uh. It's been laying there for two months and no one noticed.\u201D I\u2019m making\
    \ up this scenario, of course, but that\u2019s when you lose trust. Even though\
    \ it's completely normal to have bugs in any software, as we know, you do not\
    \ want to lose this trust. By collecting these user stories early on, we can proactively\
    \ avoid many of these worst case scenarios."
  who: Lina
- line: "We even use that for a demo. Let's say that we were worried about losing\
    \ an invoice. When we demo the solution to them, we can not only say \u201CLook\
    \ at this amazing accuracy!\u201D But we can also say, \u201COh, no! An invoice\
    \ with a corrupted format! What happens then?\u201D And then we show them \u201C\
    Here, there, and then this is how the fallback works.\u201D It also helps you\
    \ with design, because you can already think of things that can go wrong. Sometimes\
    \ you forget to design the bad outcome like, \u201CDoes it need manual intervention?\
    \ Yes or no? Who gets notified?\u201D So this really helps for them to put their\
    \ trust in you. \u201COkay, I've seen the worst case scenario for this solution.\
    \ That would not lead to any invoices missing.\u201D"
  who: Lina
- line: "You said a couple of interesting things. First, you turn these concerns into\
    \ slides. I imagine that maybe, for each concern you have a slide, where you address\
    \ each one. This lets them know that you are listening to them and you want to\
    \ address their concerns. That's the first step. But you don't stop with slides.\
    \ The next thing you can do is take each concern \u2013 each fear \u2013 and turn\
    \ it into a metric. With the lost invoices example, you can take the number of\
    \ invoices coming in and out and if there is a difference, you send an alert.\
    \ That\u2019s how you turn a concern into a metric. Then you can also demo these\
    \ concerns. It's not just happy cases, but also you show the worst case scenarios.\
    \ You take a completely broken invoice and you try to process it through the system\
    \ and then they see, \u201COkay, this is how the system behaves.\u201D In the\
    \ end, they're happy and they trust your system because they\u2019ve seen how\
    \ the bad things get solved. Is that right?"
  sec: 1356
  time: '22:36'
  who: Alexey
- header: Turning a concert into a metric
- line: Do they always need to see the metrics or just a demo enough? What do we do
    next?
  sec: 1427
  time: '23:47'
  who: Alexey
- line: "Most business stakeholders basically just want to believe that it works.\
    \ Once they believe you that it works, they will be fine. I guess it depends on\
    \ your business stakeholders. Some might want regular reporting. But most of the\
    \ cases, once you have the trust and you have established the procedures that\
    \ you will need to set up \u2013 for example, who takes care of cases where there\u2019\
    s manual intervention required \u2013 that should be enough."
  sec: 1442
  time: '24:02'
  who: Lina
- line: So you have trust and they believe you, now you need to work on not losing
    it. Right?
  sec: 1468
  time: '24:28'
  who: Alexey
- line: Yes.
  sec: 1473
  time: '24:33'
  who: Lina
- header: What happens when something goes wrong?
- line: "These procedures that you mentioned \u2013 if something goes wrong \u2013\
    \ how do I tell them about this? How do I tell stakeholders about incidents where,\
    \ let's say, we did lose an invoice. Suppose it was some corner case that we didn't\
    \ think about beforehand. How do you communicate that to them?"
  sec: 1474
  time: '24:34'
  who: Alexey
- line: "I will generally say \u2013 be transparent. But it depends a little on your\
    \ stakeholders. When I worked at Zalando, the business teams were more evolved\
    \ (knew more about software). There you can have post mortem reports and you can\
    \ estimate the impact. When you have internal teams that are mostly used to off-the-shelf\
    \ software, you need to communicate such things a bit differently. They usually\
    \ don't want details, they just want to know that you are handling it and when\
    \ it is (or will be) resolved."
  sec: 1493
  time: '24:53'
  who: Lina
- line: Basically, you need to keep them in the loop.
  sec: 1537
  time: '25:37'
  who: Alexey
- line: "Yes, you need to keep them in the loop. You need to find out who's responsible\
    \ for fixing it. You ideally plan for that beforehand. For example, what I ask\
    \ my team is, \u201COkay, what's the impact when we have an incident and we're\
    \ out for one minute? What about if we're out for 10 minutes? For one hour? For\
    \ 24 hours?\u201D Let\u2019s say something terrible happens and we need to discuss\
    \ with a stakeholder what the impact on the business is. At this point, we have\
    \ an idea about the service level we need to have, as well as about our alerting.\
    \ \u201CDo we really need to have people on the weekend if that thing is down?\
    \ Or does no one really care if we have a slight delay fixing it, as long as that\
    \ nothing is lost?\u201D So you need to think a bit ahead and communicate the\
    \ service level for the business people. But more in terms of what they understand.\
    \ For example, \u201CWhat's the impact on your business if that thing is down?\u201D\
    \ Everybody should be able to answer that question."
  sec: 1540
  time: '25:40'
  who: Lina
- line: "So you just sit with your stakeholders and say, \u201CImagine our thing goes\
    \ down for one hour. How bad is it for whatever process we automate or whatever\
    \ thing we're doing?\u201D"
  sec: 1603
  time: '26:43'
  who: Alexey
- line: "Exactly. Also think about how it would start up again. \u201CDo you have\
    \ a queue? Do you have a cache? Does it start running from there on? Or does it\
    \ catch up somehow?\u201D Basically \u2013 think ahead a bit. Then the impact\
    \ of incidents should be minimal."
  sec: 1615
  time: '26:55'
  who: Lina
- header: Post mortem reporting
- line: "Let's say we agreed with everyone on this, and we say, \u201COkay, the system\
    \ should be responsive within one hour. If something happens for 10 minutes, nothing\
    \ bad happens, but it would come back in one hour.\u201D So you will define all\
    \ these service level agreements and you start writing something. Then when something\
    \ bad happens \u2013 it goes down and somebody has to fix this on the weekend.\
    \ What happens after that? How do you communicate that to the stakeholders? Is\
    \ there any special framework we can use for that?"
  sec: 1634
  time: '27:14'
  who: Alexey
- line: "Internally, of course, we run a post mortem for that. As for how you communicate\
    \ that to the stakeholder, as I said, I think it really depends a bit on the stakeholder.\
    \ Our current business stakeholders do not care about the post mortems. We make\
    \ them for ourselves. It depends on your work environment. However, I found that\
    \ the post mortems for ML are a little bit different than the regular post mortems.\
    \ That's also an interesting thing to consider \u2013 how do we get these ML applications\
    \ back to work. I noticed that there are definitely some differences when compared\
    \ to regular incidents that are from a non-ML component."
  sec: 1683
  time: '28:03'
  who: Lina
- line: "You mean when the system is working, but it's not working correctly. Let's\
    \ say, if we take a credit risk scoring project \u2013 somebody applies for a\
    \ loan. We know that this particular person will be able to pay the loan back,\
    \ but the system says \u2018reject\u2019 without explaining anything. So from\
    \ the standard operational metrics point of view, the system is running. It\u2019\
    s still up, but it predicts garbage. Is that a correct interpretation?"
  sec: 1730
  time: '28:50'
  who: Alexey
- line: "Yeah. That can happen as well. First, you need to detect that. In the example\
    \ you mentioned, it\u2019s useful to have a live test set. This is something that\u2019\
    s useful for cases where the model is actually affecting the outcome, like fraud\
    \ prediction or spread prediction. This is a test where you do not reject people\
    \ but you have it a \u2018small running A/B test with 1% or 2%\u2019 as some people\
    \ call it. Other people call it a \u2018live test set.\u2019 You can use that\
    \ for detection and then you diagnose. In other words, after you find an outcome\
    \ that says \u201CAbsolutely not!\u201D but the person was a great candidate for\
    \ a loan \u2013 what do you do?"
  sec: 1763
  time: '29:23'
  who: Lina
- line: "My first message to everybody is \u2013 please use the post mortem format\
    \ for defining your ML solutions. I've seen even very experienced colleagues jumping\
    \ to complete conclusions based on just some data. Sometimes it\u2019s the same\
    \ as with our stakeholders, \u201COh, this phenomenon probably leads to this and\
    \ that.\u201D I can give you a very funny example that we had when I was working\
    \ at Zalando. It\u2019s a nice example for debugging ML algorithms. Sometimes\
    \ people come to you and say, \u201CWhat is this? This is a bug. This is not how\
    \ it should be. What did you do?\u201D Then you get a screenshot or something,\
    \ or someone sends you an example, and you have to find out what went wrong."
  who: Lina
- line: "We had this funny example where a colleague of ours went to site\u2019s homepage\
    \ and on the men's homepage, he saw a woman\u2019s bag and a woman's shirt. He\
    \ told me, \u201CThis is a very, very bad recommendation. What were you thinking?\
    \ I am offended. What happened?\u201D And we said \u201COkay, let's look into\
    \ this. What happened?\u201D One thing you need to have is some tooling in place\
    \ to read back your ML algorithm. Maybe you need to lock the features that arrived\
    \ in order to be able to later check what the input into the model was. It's also\
    \ very important that you don't jump to conclusions. In the example, he saw a\
    \ bag and a woman's shirt, and I was like, \u201COkay, that's very weird.\u201D\
    \ So the first thing we had to check was \u201CWhat did we do there?\u201D Interestingly\
    \ enough, I found out that this was not even a recommendation box. This was a\
    \ \u2018last seen\u2019 box."
  who: Lina
- line: '[laughs] So he actually looked at these items previously, right?'
  sec: 1928
  time: '32:08'
  who: Alexey
- header: "Apply the 5 why\u2019s"
- line: "I thought that he must have. So let's use the post mortem format to debug\
    \ this Okay. It's the \u2018last seen\u2019 box \u2013 some of my colleagues spend\
    \ some time debugging the problem, not noticing it's not recommendation box. First\
    \ thing, apply the strategy, \u201CCheck, check, check, OK.\u201D Then you find\
    \ out it's actually not a recommendation box. Then we need to have all the information\
    \ to debug this, so we checked his history, \u201CHas he actually seen these items?\u201D\
    \ Turns out, he had not seen these items. That would explain why he thought it\
    \ was a recommendation when it wasn't, because he was surprised to see these items.\
    \ He had no recollection of them. If we apply the post mortem format, Okay, next\
    \ step. \u201CWhy was this in his \u2018last seen\u2019 box?\u201D \u201CWell,\
    \ because it in his history.\u201D \u201CCheck \u2013 It was not in his history.\u201D\
    \ If it had been in his history, we would have another hypothesis. \u201CWhy did\
    \ he not remember?\u201D Apply the five why\u2019s, \u201CWhy did he not remember?\u201D\
    \ One reason could be that maybe this box keeps his \u2018last seen\u2019 actions\
    \ from half a year ago and he came back and he doesn't remember. Then a product\
    \ conclusion could be \u201CThis box should only be shown for five days.\u201D"
  sec: 1931
  time: '32:11'
  who: Lina
- line: "This would be a very different way to fix the problem. Then, if you apply\
    \ the five whys, you come to another conclusion. \u201COkay, he had not seen these\
    \ items.\u201D So we had to figure out, \u201CWhy was he seeing this in his \u2018\
    last seen\u2019 box?\u201D And then we found out that he had a shared account\
    \ with his wife. His wife had been browsing these items on her app. This \u2018\
    last seen\u2019 box had a cool feature \u2013 it collected both the desktop and\
    \ app data together and showed it to him."
  who: Lina
- line: "So now we can have different conclusions based on this. A) Should we maybe\
    \ have gender tome. He is on the men\u2019s section, so maybe the \u2018last seen\u2019\
    \ box should be made aware of its context and show only male stuff on the male\
    \ part of the site. Thus he would have only seen men\u2019s stuff. B) We could\
    \ consider \u201CWhat if it's a shared account?\u201D Clearly, multiple people\
    \ browse on this account. \u201CShould the \u2018last seen\u2019 box behave differently\
    \ somehow if we can detect that this is a shared account of multiple family members?\u201D\
    \ When you think of Netflix \u2013 they found that this is a problem, so they\
    \ split the accounts. \u201CShould something similar be considered?\u201D \u201C\
    Are there other features that need this or just this box?\u201D"
  who: Lina
- line: "By going through the five why's, you can immediately understand how you might\
    \ accidentally go in the wrong direction. I had a few examples where some colleagues\
    \ jumped to conclusions. Because it's an algorithm, you just look at it and you\
    \ say \u201CIt's probably because of this.\u201D They are all engineers, but somehow,\
    \ sometimes, we don't apply a very structured approach with ML and really make\
    \ sure to check each step. \u201CCan this be true? Would that make sense? How\
    \ could I find that out? Maybe I need some tooling around that as well, which\
    \ I need to build.\u201D"
  who: Lina
- line: "So I recommend a very structured approach. I recommend that you write yourself\
    \ some tooling. For example if you need to log the input features to do this kind\
    \ of debugging, then you should. I also recommend that you get user feedback about\
    \ bugs. Interestingly, we have a lot of bugs in our ML solutions. Sometimes it's\
    \ edge cases. Sometimes it's whole groups of people. For example, here it\u2019\
    s users with shared accounts. Sometimes it's people of special sizes to stay in\
    \ the ecommerce area. But we have that sometimes when we look into bias \u2013\
    \ we look at how well the algorithm works on different subgroups, like \u201C\
    Does it respect all small subgroups?\u201D Or \u201CDo some of these subgroups\
    \ have bad experiences?\u201D Basically \u2013 get some user feedback, either\
    \ from clicks or I also recommend that you try to use your own product. We know\
    \ this approach from software engineering, when you basically \u2018eat your own\
    \ dog food\u2019. You really should use your own service. I did find quite a few\
    \ bugs when we were using our own service. Also, maybe make a channel, so that\
    \ internal colleagues can easily report bugs to you, \u201CHow would you get this\
    \ bug support?\u201D \u201CHow do you make it known that there\u2019s a bug when\
    \ you roll something out?\u201D Maybe you can add that to the announcement of\
    \ the roll out, \u201CAll internet colleagues, if you see anything weird, here's\
    \ the email that we use for bugs.\u201D So try to get this feedback from anywhere\
    \ you can."
  who: Lina
- line: "There was a funny story a few episodes ago. We had a guest that worked at\
    \ a telecom company. The company also sold phones and they did some credit scoring.\
    \ So as he worked there, he applied for an iPhone and got rejected. So then went\
    \ to his colleagues and asked, \u201CHey, what's going on?\u201D Then he was able\
    \ to debug the model."
  sec: 2201
  time: '36:41'
  who: Alexey
- line: Oh, excellent! Did he find the root cause?
  sec: 2230
  time: '37:10'
  who: Lina
- line: Yeah, it turned out that it was because he was on a temporary residence permit.
    He just moved to the Netherlands. That was the reason. That was the strongest
    feature in the model.
  sec: 2232
  time: '37:12'
  who: Alexey
- line: "That\u2019s interesting, because people who just move somewhere probably\
    \ all need a new phone. Right? Or new phone plan. So that\u2019s an interesting\
    \ question \u2013 is that is rejection-worthy or not?"
  sec: 2244
  time: '37:24'
  who: Lina
- line: But sometimes people who just move somewhere, they may buy a lot of phones
    and go back to their home country without paying the loan.
  sec: 2257
  time: '37:37'
  who: Alexey
- line: It's an interesting question. Maybe you need some other feature to make sure
    you don't catch these types users. For example, maybe the people that live within
    the EU and move for work are probably not a problem. I'm not sure. But it's an
    interesting question that you can then send back to the business person or you
    find the bug in your own application that you can solve.
  sec: 2268
  time: '37:48'
  who: Lina
- header: "If a lot of users say it\u2019s a bug \u2013 it\u2019s worth investigating"
- line: Maybe it's not a bug. You just have to live with knowing that you will not
    get that phone.
  sec: 2293
  time: '38:13'
  who: Alexey
- line: "For him, it's probably a bug. So I'm of the really strong opinion that \u2013\
    \ if a lot of users say it's a bug, (maybe not for the case with the phones) there\
    \ might be an argument for the company to trade off risk. But in general, I've\
    \ seen a lot of cases where some people say \u201CIt\u2019s not a bug \u2013 I\
    \ won\u2019t fix it.\u201D That is not an acceptable answer in my book, if a lot\
    \ of people are complaining about it. You also will not find out if a lot of people\
    \ are complaining about it if you don\u2019t go looking for these use cases, which\
    \ is horrible. I tried to get my product people on board to run a sort of \u2018\
    user-oriented debugging.\u2019 Say a user comes with sort of WTF moment \u2013\
    \ you make this into a post mortem. That's good practice, which helps improve\
    \ usability and the awesomeness of your product."
  sec: 2300
  time: '38:20'
  who: Lina
- line: Now I'll have to bleep the video. [laughs]
  sec: 2350
  time: '39:10'
  who: Alexey
- line: "Oh sorry. I meant \u201CWTF moments\u201D. You should hear me off-video,\
    \ I'm way worse."
  sec: 2354
  time: '39:14'
  who: Lina
- header: Post mortem format
- line: "I wanted to ask you a bit about this \u2018post mortem\u2019 format. We also\
    \ have a question in chat. What does the format look like? I think one thing that\
    \ you mentioned is that you need to ask the \u201Cfive why's\u201D \u2013 you\
    \ don't jump to conclusions immediately. So you need to spend some time trying\
    \ to understand what the actual root cause is. This framework of \u201Cfive why's\u201D\
    \ can help you do that. In other words, you don't stop at the first \u2018why\u2019\
    \ and use the answer as a conclusion, but instead you keep digging. What else\
    \ do you need to do in order to have this structured approach in a post-mortem\
    \ for a data science project?"
  sec: 2366
  time: '39:26'
  who: Alexey
- line: "One thing you may need is more technical information. Sometimes you need\
    \ the cookies. Sometimes a screenshot is enough. It depends a little bit on your\
    \ domain. Basically try to find a way to get the necessary information in order\
    \ to debug the issue in your application. Maybe an interesting hint is \u2013\
    \ don\u2019t only use incidents, also use these \u2018very bad user experiences\u2019\
    \ that you wouldn't need, so there is no exception. Nothing is in the logs, so\
    \ you need user inputs, which are a little bit hard to get. Get the bad experiences\
    \ \u2013 then you can gather the necessary information to debug. Sometimes it\
    \ may be cookie information, sometimes it's a log in whatever your service gets\
    \ as relevant inputs. I would say that's it."
  sec: 2414
  time: '40:14'
  who: Lina
- line: "Otherwise, it's a typical engineering post mortem format. I'm always borrowing\
    \ from different disciplines. Sometimes, we, as ML people, can be software engineers,\
    \ but sometimes we have like, physicists, or economists \u2013 and they might\
    \ not know this format. So for these quips, It's a typical format that software\
    \ backend engineers use to debug their incidents. We can utilize that \u2013 just\
    \ adapt it a little bit. It's quite useful."
  who: Lina
- header: Action points
- line: "Do you remember what the format is? What does it look like? I think I saw\
    \ that usually it has some sort of timeframe. You ask \u201CWhat happened?\u201D\
    \ but without any finger pointing or blaming \u2013 just factual description."
  sec: 2508
  time: '41:48'
  who: Alexey
- line: "First you get the facts. If it's a backend service, it's likely \u201CThe\
    \ service was down from that time to that time.\u201D As in our women\u2019s bag\
    \ example, it might be a screenshot, or it might be return values. We put all\
    \ the factual information together and then we do the investigation where we go\
    \ step-by-step through everything \u2013 \u201CThe user saw a blouse and a women\u2019\
    s bag on the frontend home page. Why?\u201D \u201COkay, this is surprising.\u201D\
    \ Maybe you go through investigation, and then there's a lower part where you\
    \ can add details about the different investigation parts, such as logs. Then\
    \ there's a very important section, which is called \u2018action points.\u2019\
    \ Normally, post mortems are called \u2018blameless post mortem,\u2019 say you\
    \ say \u201CNo one is at fault.\u201D"
  sec: 2523
  time: '42:03'
  who: Lina
- line: "Then there are action points. These action points mean that you try to make\
    \ changes to your application that ensure that this kind of unfolding chain of\
    \ events doesn't happen again. This can be a process change. For example, \u201C\
    We found out how you work \u2013 there was no \u2018four eyes\u2019 principle\
    \ implemented.\u201D Or \u201CYou did not have good unit test coverage of edge\
    \ cases for your solution.\u201D Then you make these actual points that focus\
    \ on that, \u201CI recommend edge case testing,\u201D for example. Or \u201CI\
    \ recommend a very specific change.\u201D Often it's also very process-oriented\
    \ \u2013 you do not only fix this very specific bug, but you think of the category\
    \ of bugs, or this type of problem. Is there a way to fix that? Then you write\
    \ the action points, someone from the team reviews it \u2013 it's like the coach\
    \ change. They give you a review on which action points should be implemented.\
    \ Then you make them into tickets and actually implement them. This helps with\
    \ a constant cycle of improvements."
  who: Lina
- header: Debugging vs explaining the model
- line: "Thank you. We have a question. We talked about debugging machine learning\
    \ problems and figuring out, \u201COkay, the model made this decision. Why did\
    \ this happen?\u201D Do you know any off-the-shelf or open source debugging tools\
    \ for that?"
  sec: 2651
  time: '44:11'
  who: Alexey
- line: "Yes. It depends what you want to do with it. There's model explanation, which\
    \ is a whole other research area, like sharp values and these kinds of libraries\
    \ that you can use. The question is usually what you want to achieve with them\
    \ \u2013 explanations or debugging. With debugging, we want to find the root cause\
    \ of a problem or an error. Usually, it's not to explain the algorithm. There\u2019\
    s no off-the-shelf tool to explain the root cause of a bug or a design error.\
    \ You really just have to go through the format and you see what you can use to\
    \ debug your own logic."
  sec: 2669
  time: '44:29'
  who: Lina
- line: "What the question is referring to is probably a tool to get explanations\
    \ for the model, which is something that is often used to explain it to stakeholders\
    \ or to reason about the internal workings of the model, which is a slightly different\
    \ purpose. For that, you can Google \u201CExplainable AI\u201D the results will\
    \ explain much better than I can. There's a bunch of libraries. But for the debugging,\
    \ it\u2019s really quite different. Usually the mistakes stem from the fact that\
    \ you didn't consider certain modeling assumptions. So, you actually have to change\
    \ your model, or you have certain filters in place, or the UI is not correct \u2013\
    \ so it\u2019s much broader when it comes to debugging. The root causes are often\
    \ not in the model itself, but from a wrong assumption you made, or you did not\
    \ consider certain inputs that have to be treated separately. It's seldom the\
    \ algorithm that\u2019s the problem."
  who: Lina
- line: Or maybe the data changed.
  sec: 2772
  time: '46:12'
  who: Alexey
- line: Or data problems, exactly. That can also be an issue. Yeah.
  sec: 2775
  time: '46:15'
  who: Lina
- line: "For example, in one of the features maybe a unit changed \u2013 instead of\
    \ kilometers, you have meters."
  sec: 2779
  time: '46:19'
  who: Alexey
- line: Yes, we actually had that in Zalando. We have a colleague who was working
    on the fraud model. On the live path, the unit of one of the very important features
    changed from seconds to milliseconds, but not in the test data. That completely
    screwed everything up. For that, you don't need model explanations, you need monitoring
    of the input data distribution and compare them between training data and live
    data. So, as you see, it depends what exactly we're talking about. I hope that
    answers your question.
  sec: 2788
  time: '46:28'
  who: Lina
- line: So there is a variety of things that can go wrong.
  sec: 2819
  time: '46:59'
  who: Alexey
- line: Exactly. Can we go back to the person and see if their question was answered?
  sec: 2826
  time: '47:06'
  who: Lina
- line: "BK62 \u2013 If you're listening, can you please let us know if your question\
    \ was answered or not? If you want to add something, please let us know."
  sec: 2832
  time: '47:12'
  who: Alexey
- header: Are there online versions of checklists?
- line: "There is another question from the same person about any of the checklists\
    \ you mentioned. \u201CAre there online versions of these checklists?\u201D Have\
    \ you seen any of those?"
  sec: 2840
  time: '47:20'
  who: Alexey
- line: "Maybe I should make a blog post. There's one checklist, which is of kind\
    \ of nice \u2013 it's a Hands on ML. They have a checklist and the first chapter\
    \ I think is also online. Some of the additions to these checklists are actually\
    \ just from my personal experience, so that part is not online yet. But I have\
    \ seen different people have different forms of their checklists. You can combine\
    \ to make your own personal \u2018best of\u2019."
  sec: 2854
  time: '47:34'
  who: Lina
- line: On Monday, we talked about AI Canvas, which is some sort of business Canvas.
    Maybe you saw this canvas. You have a piece of paper where in the center, you
    write the business value. On the left, you have data, etc. And you have all these
    different blocks. Maybe this also acts as a kind of checklist, because you have
    to fill all these different blocks. And then you can make sure that every aspect
    is covered.
  sec: 2884
  time: '48:04'
  who: Alexey
- line: Yeah, that sounds like a good tool.
  sec: 2921
  time: '48:41'
  who: Lina
- line: "But yeah, I also like to think about that for us engineers. Maybe it's even\
    \ simpler if you have at least a checklist. Then you just tick, tick, tick. \u201C\
    Okay, here is where I am missing something. Let's go and fix it.\u201D You probably\
    \ should write a blog about it."
  sec: 2925
  time: '48:45'
  who: Alexey
- line: You have to ping me on this.
  sec: 2942
  time: '49:02'
  who: Lina
- header: Make sure to log your inputs
- line: "Yeah. We'll have a transcription of this. Maybe it will be easier then to\
    \ convert it. So BK 62 said that \u201CYes. You answered my question. You mentioned\
    \ writing your own tooling. So I want to see if there's anything already available\
    \ that can be built on top of.\u201D"
  sec: 2946
  time: '49:06'
  who: Alexey
- line: "Oh, okay. So that question was probably just on the explanation part. Just\
    \ one addition to my answer \u2013 It\u2019s very specific to what your inputs\
    \ are. Basically, make it observable. Make sure you log your features. Make sure\
    \ you have some way to find out what the inputs were after the fact \u2013 what\
    \ did your models say? Also, it\u2019s important to know how to connect it all\
    \ to the necessary debugging system. If you have a feature store, you have to\
    \ know how to look up what were the features were at the time or log them. Something\
    \ like that."
  sec: 2968
  time: '49:28'
  who: Lina
- line: People are saying that everyone's waiting for your blog post on that.
  sec: 3006
  time: '50:06'
  who: Alexey
- line: Oh, okay. Yes. If there's interest then I may get into this. Yes.
  sec: 3010
  time: '50:10'
  who: Lina
- header: Talking to end users and using your own service
- line: "We have two more questions. \u201CDo you also talk to end users or just limit\
    \ research to project managers?\u201D I think we talked about that \u2013 you\
    \ actually talk to end users."
  sec: 3019
  time: '50:19'
  who: Alexey
- line: "It depends on what project I'm working on. I do talk to end users in some\
    \ cases. I also do mystery shopping. Mystery shopping is basically when you go\
    \ through the process yourself. I was optimizing the credit process application\
    \ in my current job \u2013 so I applied for a loan. Just on check 24. I went through\
    \ the different processes to see what the user experience is \u2013 \u201CWhat\
    \ kind of values I have to give? What do the other banks do for this process?\
    \ What\u2019s the flow like? So yes \u2013 speak to end users. I also speak to\
    \ experts about the topic, because sometimes they act like a summary of a bunch\
    \ of end users. They can also tell you a bit of meta information. So, all of the\
    \ above. Yes."
  sec: 3030
  time: '50:30'
  who: Lina
- line: I hope your SCHUFA score wasn't affected when you did this.
  sec: 3077
  time: '51:17'
  who: Alexey
- line: "That\u2019s one thing I checked, actually. Because I was like, \u201CThis\
    \ should not be affected. They always promised it won\u2019t \u2013 and I checked\
    \ it.\u201D Indeed, when we do requests, it does not get worse. I can confirm\
    \ that it is not affected."
  sec: 3081
  time: '51:21'
  who: Lina
- line: "For those who are not from Germany \u2013 in Germany, there is this core\
    \ credit score that tells how trustworthy a person is when it comes to credit.\
    \ I think it's nationwide, right?"
  sec: 3093
  time: '51:33'
  who: Alexey
- line: "Yes, I checked. I checked our database. I also got my free SCHUFA \u2013\
    \ you can get it once a year for free. They hide it on a sub page because they\
    \ want to charge you for it. Free life hack of the day, you can get it on the\
    \ sub page. Once a year, they send you the detailed information for free. You\
    \ just have to wait and it comes in paper format 14 days later. I checked against\
    \ that and I also had output of all the other banks. It\u2019s quite interesting.\
    \ They have different scorecards that they calibrate based on their business case.\
    \ We get slightly different scores from each bank. So that was quite fascinating\
    \ to sort of reverse engineer that a bit regarding how this process works."
  sec: 3106
  time: '51:46'
  who: Lina
- line: That person we talked about that applied for a phone, I think he also did
    mystery shopping without realizing it.
  sec: 3139
  time: '52:19'
  who: Alexey
- line: '[laughs] He did. See and he encountered a problem. Yeah.'
  sec: 3143
  time: '52:23'
  who: Lina
- header: Your ideas vs Stakeholder ideas
- line: "Then there is a follow up question. It actually was two questions. \u201C\
    Do you get your own ideas when discussing a data project?\u201D"
  sec: 3149
  time: '52:29'
  who: Alexey
- line: "To suggest problems to the stakeholders as projects? Yes, because I'm just\
    \ observing the space, see what other people are doing, and basically try to go\
    \ to the stakeholders and say \u201CDo we need this? Do you think this is useful?\u201D\
    \ It's very hard to generate such project ideas. Sometimes the stakeholders don't\
    \ know what they don't know. It's like a \u2018chicken and egg\u2019 problem.\
    \ I am looking at what possible applications other people are doing and try to\
    \ see if we have the same problem. But ideally, the business people should come\
    \ to you; you should not come up with the problem yourself. Because you're usually\
    \ wrong. You're just one person. To think that you're the user is usually a wrong\
    \ assumption. But you can definitely try just seeing \u201COkay, these cool ML\
    \ applications are possible. Does that make sense for my company?\u201D Then yes.\
    \ Maybe the person can clarify the question a little bit, to see if I answered\
    \ it."
  sec: 3159
  time: '52:39'
  who: Lina
- line: I think it comes back to one of the points that we discussed about making
    the problem specific. If you make the problem specific, it's easier to talk to
    the stakeholder.
  sec: 3214
  time: '53:34'
  who: Alexey
- line: "Ah. Okay. Okay. Yeah, it's so it can be a collaborative problem. When fleshing\
    \ out what the problem is \u2013 we're actually very involved. I think if you're\
    \ very hands off, ML really requires that the problem be very well defined. I've\
    \ seen quite a few projects fail because the ML works, but the problem was not\
    \ well enough defined. Or it could never work because the problem was not well\
    \ enough defined. Then in the end, users will blame you or the ML in general.\
    \ So I think it's really up to us to say \u201CThis is the requirement. The requirement\
    \ is that the business case is well defined.\u201D"
  sec: 3227
  time: '53:47'
  who: Lina
- header: Should data practitioners educate the team about data?
- line: "Thanks. We have a question about data knowledge. I'm not sure if we talked\
    \ about this \u2013 maybe a little bit. \u201CRegarding data knowledge within\
    \ the company \u2013 is it data practitioners\u2019 responsibility to educate\
    \ the team on what data there is and what problems it can solve?\u201D"
  sec: 3268
  time: '54:28'
  who: Alexey
- line: "Wow. The person asking is probably working in such an organization \u2013\
    \ I can hear the pain behind the question. I feel you. Basically, we need the\
    \ counterpart to be well-versed in data. But sometimes they're not, so what do\
    \ you do? Perhaps you only take jobs in companies which are already quite advanced?\
    \ Usually, we still need to do a little bit of outreach and educate people. A\
    \ part of my work is, let's call it \u2018community building\u2019 in the company\
    \ and talking to other like-minded people. I try to have a bit of a movement of\
    \ data people who all want to work in the same direction. Also get business people\
    \ interested in using data. Of course, try not to spend too much time on it. Unfortunately,\
    \ with the state of data literacy at the moment \u2013 it\u2019s also a somewhat\
    \ on us to do a little bit of education. Or you can pick a company where this\
    \ is not a problem, which are few in number, I would say."
  sec: 3289
  time: '54:49'
  who: Lina
- line: "But then you learn how to deal with this, you get experience. Then maybe\
    \ if you go to a company where the people are less mature in terms of data literacy,\
    \ then you already have experience \u2013 you know how things should look like\
    \ \u2013 you can share this experience in the company, so they can move to that\
    \ level of maturity. Is that right?"
  sec: 3366
  time: '56:06'
  who: Alexey
- header: "People skills and \u2018dirty\u2019 hacks"
- line: "Yes. In general, I think we always need to have quite good people skills\
    \ in our job, because it's so cross-functional. The main thing I'm working on\
    \ during the last few years is not only the technical part, but I try to be better\
    \ at convincing and motivating. Sometimes, when we start off, we don't necessarily\
    \ need that or have that as engineers. It's quite useful to invest a little bit\
    \ of time into this. It\u2019s also useful for data-related problems. I also have\
    \ some dirty-tech tricks. If you work with dirty data, I used to have techniques\
    \ where I tried to convince people to fix data so that I can use it. But that\
    \ never worked, because the data is not used \u2013 it's not attached to a big\
    \ business case. Now, I have a set of dirty hacks that I just apply. For example,\
    \ I start using dirty data, which mostly works, but not always. Then I say \u201C\
    I'm using this data, please fix this!\u201D"
  sec: 3388
  time: '56:28'
  who: Lina
- line: So there's a bunch of things that you also acquire on the way. It takes a
    bit of convincing, but also a bit of dirty tricks that you would just bring with
    you.
  who: Lina
- line: "Just to make sure I understand the dirty trick, (so that I can use it later).\
    \ Say there is a data source that is not claimed, and the ones who produce it\
    \ don't want to clean it, because nobody uses it. They say \u201CWe don't want\
    \ to spend our time because we don't see any impact.\u201D So you start using\
    \ it and then you come to them and say, \u201CHey, you see \u2013 I actually use\
    \ it. How about you clean it now?\u201D"
  sec: 3458
  time: '57:38'
  who: Alexey
- line: "\u201CIt\u2019s a nice product, it mostly works. But look at this very unfortunate\
    \ side effect in 10% of the cases.\u201D Yes. Unfortunately, I used to not do\
    \ that. I used to speak a lot and blah, blah, blah \u2013 nothing happens. But\
    \ that was the way that got it done. But also be careful with this. In general,\
    \ I'm also careful with it. For example, every new data source I add, there's\
    \ a cost to it. There's a cost of maintaining the data source \u2013 there\u2019\
    s a cost of having a new stakeholder monitoring it. In general, I apply the strategy\
    \ where each data source, or each feature, needs to prove itself in order to be\
    \ added \u2013 especially new data sources. But every once in a while, you really\
    \ want it because it's useful, like some sort of event that is very good. So,\
    \ just mix and match your approach."
  sec: 3482
  time: '58:02'
  who: Lina
- line: "Maybe we should have a follow-up conversation about \u2018dirty hacks\u2019\
    ."
  sec: 3529
  time: '58:49'
  who: Alexey
- line: "I cannot tell you. I would have to you know\u2026 dispose of you afterwards.\
    \ [laughs]"
  sec: 3537
  time: '58:57'
  who: Lina
- line: "[laughs] I can imagine a title, like \u2018dirty communication hacks\u2019"
  sec: 3539
  time: '58:59'
  who: Alexey
- line: "\u2018With Lina\u2019"
  sec: 3547
  time: '59:07'
  who: Lina
- line: "\u201CDon't try it on your colleagues.\u201D"
  sec: 3548
  time: '59:08'
  who: Alexey
- line: Then we have 30 people tuning in after 11 at night expecting different contents.
  sec: 3551
  time: '59:11'
  who: Lina
- line: So. Do you have any last words before we finish?
  sec: 3557
  time: '59:17'
  who: Alexey
- header: Where to find Lina
- line: "Thank you for having me. And if anyone wants to connect more \u2013 I'm hanging\
    \ out in the MLOps channel sometimes. Also on LinkedIn. Or if anyone wants to\
    \ write a blog post together or just generally share? Yeah. Look me up."
  sec: 3566
  time: '59:26'
  who: Lina
- line: "Okay, great. My next question was \u201CHow can people find you?\u201D and\
    \ you just answered that. I think I ran out of questions. I just want to thank\
    \ you in return for joining us today, sharing your knowledge, your checklist,\
    \ your one dirty hack. Maybe we will talk about other, but I think that the one\
    \ you gave was already useful. Thanks everyone who joined, listened to our conversation,\
    \ and asked questions. Don\u2019t forget, we have two more talks. Tune in tomorrow\
    \ and on Friday. That\u2019s all. Thanks a lot, Lina."
  sec: 3582
  time: '59:42'
  who: Alexey
- line: See you.
  sec: 3618
  time: '1:00:18'
  who: Lina
- line: Goodbye. Have a great day.
  sec: 3620
  time: '1:00:20'
  who: Alexey
- line: You too.
  sec: 3621
  time: '1:00:21'
  who: Lina

---
