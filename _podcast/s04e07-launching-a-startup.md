---
title: "Launching a Startup: From Idea to First Hire"
short: "Launching a Startup: From Idea to First Hire"
guests: [carminepaolino]

image: images/podcast/s04e07-launching-a-startup.jpg

season: 4
episode: 7

ids:
  youtube: s-w8_GDgIlU
  anchor: Launching-a-Startup-From-Idea-to-First-Hire---Carmine-Paolino-e15sk4i

links:
  youtube: https://www.youtube.com/watch?v=s-w8_GDgIlU
  anchor: https://anchor.fm/datatalksclub/episodes/Launching-a-Startup-From-Idea-to-First-Hire---Carmine-Paolino-e15sk4i
  spotify: https://open.spotify.com/episode/2zlqwEOamFD8YVGkf4VsFW
  apple: https://podcasts.apple.com/us/podcast/launching-a-startup-from-idea-to-first-hire-carmine-paolino/id1541710331?i=1000531945076


transcript:
- line: This week, we'll talk about building a startup as a technical person. And
    we have a special guest today, Carmine. Carmine and I are ex-colleagues. Carmine
    worked with me at OLX as a senior data scientist. At some point, he left OLX,
    he joined entrepreneur first, which is a startup factory, so to say. Now he's
    a co-founder and the CTO at FreshFlow. Welcome.
  sec: 106
  time: '1:46'
  who: Alexey
- header: "Carmine\u2019s background"
- line: Thank you, Alexey. I'm glad that you could invite me to see you again. Great
    introduction. Just to get to know me a little bit better. I started programming
    when I was a kid at the age of five. I continued this passion my entire life.
    I went to university. I felt quite fortunate that I could actually know what I
    wanted to do. I know that a lot of people struggle with that. I did a computer
    science bachelor at the University of Bologna. I did some gigs as a freelance
    web developer for around a year. Then I published my thesis in a book. The name
    of the thesis was "large scale social network analysis". It was about how to parallelize
    social network analysis algorithms using MPI. A lot of C++. I'm glad I don't have
    to do that again. But it was really fun. If you want to check it out. It's published
    in Springer.
  sec: 136
  time: '2:16'
  who: Carmine
- line: "Then I joined my master\u2019s in the Free University of Amsterdam, which\
    \ was in artificial intelligence. Since then I fell in love with it and continue\
    \ doing data science for five years, including at OLX, at another consultancy\
    \ before, and at another startup before. At OLX I went to OLX-squared, which is\
    \ the moonshot team of OLX, where you can innovate as much as you want. After\
    \ that, I joined the data science for social goods in the Alan Turing Institute,\
    \ which is a research institution in the UK for data science and machine learning.\
    \ I mentored some students there. We helped the World Bank and Ofsted (Office\
    \ of standards for earlier childcare in the UK) with some really exciting data\
    \ analytics. After that, I decided to join entrepreneur first."
  sec: 207
  time: '3:27'
  who: Carmine
- line: You said you started programming as a five-year-old kid. My kid is now five
    years old, so maybe you'll tell me how to teach him a bit of programming at some
    other time.
  sec: 271
  time: '4:31'
  who: Alexey
- line: He has to be really not excited about watching TV.
  sec: 291
  time: '4:51'
  who: Carmine
- line: Interesting. That's not the case.
  sec: 297
  time: '4:57'
  who: Alexey
- header: "Carmine\u2019s startup FreshFlow"
- line: So tell us a bit about your startup. What do you do there?
  sec: 306
  time: '5:06'
  who: Alexey
- line: "I'm the co-founder and the CTO of FreshFlow. FreshFlow is a complete ordering\
    \ system for supermarkets. We solve the enormous food waste problem that we have\
    \ in the world. And also make more money for supermarkets and make more money\
    \ for us. We have this really nice triple bottom line, which makes us a profitable\
    \ business \u2014 not yet, but we will in the future, hopefully \u2014 and also\
    \ will make more money for for the supermarkets and benefit the planet."
  sec: 309
  time: '5:09'
  who: Carmine
- line: Avik, my co-founder, saw a problem when trying to sell to supermarkets another
    computer-vision based solution. He saw that they have a bigger problem, especially
    for fresh products. Fresh products have varying shelf lives. Even the same type
    of product like mangoes, one batch could have a week left, and another batch could
    have two days left. And it's really, really hard to predict that, predict how
    many you need, and at what time. We found that most supermarkets still use people
    on the floor, so-called "fresh product managers". Every single day, they spend
    two hours looking at the shelves, and looking at what they have in the back to
    figure out what they have to order. When we started our first pilot with Edeka,
    which is the largest German supermarket, with one store right now. And we are
    signing with other stores in the future.
  sec: 346
  time: '5:46'
  who: Carmine
- header: Doing user research
- line: "We went there with user research. We learned that at OLX-squared, it was\
    \ a great experience there working with the designers from Koos. We saw that the\
    \ fresh product people go there at 6am in the morning. They have a lot of boxes\
    \ to move around \u2014 they put all the things in place, which takes a couple\
    \ of hours. Then they start the ordering process for the next day. They calculate\
    \ what is going to be the demand the next day. They have to think about it in\
    \ their head. They have to think about weather, seasonality, is there a big event\
    \ in the town. In the specific town where we're doing the pilot, there is a big\
    \ ramp to go to the to the supermarket. If that ramp is full of snow, nobody will\
    \ go to the supermarket. They have all of these things in their heads for 200\
    \ products. It's insane. It is really an incredible work. I'm amazed it works\
    \ at all. They're doing a great job. But we are humans, we're not calculators.\
    \ So we create ordering system, that lives in an iPad app, for all they know.\
    \ It lives mostly in the cloud, to be honest. It uses machine learning and reinforcement\
    \ learning to figure out the perfect order."
  sec: 433
  time: '7:13'
  who: Carmine
- line: This position, fresh product manager, that's a different kind of product manager.
    They actually manage products.
  sec: 535
  time: '8:55'
  who: Alexey
- line: Yeah, it's a lot less about politics and a lot more about how many strawberries
    you have to order.
  sec: 549
  time: '9:09'
  who: Carmine
- line: So, every store in every supermarket have this position? They have to wake
    up at 6am in the morning. They have to do go around, look at the shelves and see
    "These mangoes are getting spoiled. We need to do something about them." They
    do this every day and it's a lot of manual work.
  sec: 557
  time: '9:17'
  who: Alexey
- line: It's very tough work. We were amazed that these ladies could do it that early
    in the morning and also keep fresh to think about all these other factors. Honestly,
    we were struggling to follow them, they were so fast. It was really amazing.
  sec: 589
  time: '9:49'
  who: Carmine
- line: So you were sitting with them, watching how they work, and then try to replicate
    it?
  sec: 611
  time: '10:11'
  who: Alexey
- header: Design thinking
- line: "Yeah, we were shadowing them for a couple of days. We went there for a week.\
    \ This is how we work in general. It's called \"design thinking\". From my experience\
    \ with OLX-squared, and with the book \"Design Thinking\" by Curedale \u2014 highly\
    \ recommend that by the way \u2014 it's very much appreciated by our clients that\
    \ we do that. We are able to really figure out what are the processes, how things\
    \ go in the store, and then deliver the solution that they actually need, instead\
    \ of what we think they need. This is big learning that I had from that experience\
    \ with OLX-squared. Also, EF push another book, which I also recommend, it's called\
    \ \"The Mom Test\". I would say it's a much lighter version of \"Design Thinking\"\
    . It's mostly about how to do sales calls and stuff like that. But it does help\
    \ you figure out what to ask. You want to ask things that actually make the user\
    \ tell you all their processes, and not tell you about the solution. Because there's\
    \ always a difference between what they want and what they need."
  sec: 617
  time: '10:17'
  who: Carmine
- header: Entrepreneur first
- line: I don't think you just woke up one day and realized "Okay, there is this problem.
    Let's solve it". I'm curious, how did you actually come up with this idea? What
    did the process look like?
  sec: 707
  time: '11:47'
  who: Alexey
- line: "It was very interesting. I joined entrepreneur first because I wanted to\
    \ have a startup. I wanted to do it since my bachelor\u2019s. I had a few ideas.\
    \ I tried to ideate with some people and come up with some ideas for a startup,\
    \ but it didn't really materialise. The problem is that you're always so busy.\
    \ We were trying to do it also having a job at the same time. It was really hard.\
    \ You need to really dedicate your life to find a good idea \u2014 unless you\
    \ have a good idea already. Also finding a co-founder is really hard. They need\
    \ to have the same amount of time and the same life circumstances."
  sec: 727
  time: '12:07'
  who: Carmine
- line: When I received the call from entrepreneur first, I didn't know about them.
    This was around February 2020 when I was in OLX-squared. I already got the position
    at the Alan Turing Institute. I was really keen on first doing these two things,
    because they were so cool. They told me that another cohort would start in September.
    That was exactly in line with with the rest of my timeline. I reapplied for the
    September cohort got in. I had an amazing time. Entrepreneur first's tagline is
    "the world's leading talent investor". They call themselves "talent investor",
    because they take you in because what you did in the past is quite interesting,
    the growth that you have is pretty big, or you know something specific that nobody
    else knows. They take a bunch of people like that, they give you a bunch of talks
    on how to do sales, how to do marketing.
  sec: 796
  time: '13:16'
  who: Carmine
- line: This is something that technical people like you and me don't know. We don't
    know what marketing is. I have no idea what marketing people do. It's so nice
    that they also teach you these things.
  sec: 884
  time: '14:44'
  who: Alexey
- line: Absolutely. They have experts in entrepreneur first. For example, for sales,
    or people that exited companies for many, many times. There are Venture Partners
    there because essentially they are venture capital for pre-seed companies. But
    they operate quite differently. So they have experienced venture partners, and
    they talk about these topics. They were even talks by Ben Evans, who is one of
    the best people in the VC space, used to be at Andreessen Horowitz as well. He's
    now a global venture partner there, and many other people that are perhaps less
    known, but really, really good.
  sec: 904
  time: '15:04'
  who: Carmine
- header: "Finding co-founders: the \u201Cexpertize edges\u201D framework"
- line: So, they put you through this training, but I guess that's not the only thing
    they do, right?
  sec: 955
  time: '15:55'
  who: Alexey
- line: Of course. They assist you with a framework on how to find a co-founder. First
    of all, you will know if you're a CTO type or a CEO type, even though there may
    be some exceptions. Usually, if you have a technical background, you're a CTO
    type. If you have more business-minded background or domain edge, they call it
    a CEO type.
  sec: 961
  time: '16:01'
  who: Carmine
- line: A data scientist would be a CTO and a product manager would be CEO?
  sec: 995
  time: '16:35'
  who: Alexey
- line: Yeah, roughly. It could also change. They have so-called "edges", and you
    fit in one or two edges. The edges are catalyst edge, domain edge, and technical
    edge. The catalyst edge is further defined as catalysts doers and catalyst talkers.
    The catalyst doers are very energetic. They can make almost anything. They don't
    have a specific technical edge that is so sharp that only 10 people in the world
    have. But they're more widespread. Data scientists will be full-stack people.
    We, for example, were catalysts doers for EF. Catalyst talkers are flexible business
    people. They are the same thing but on the business side.
  sec: 1001
  time: '16:41'
  who: Carmine
- line: There are also domain edges. They are people that have in-depth knowledge
    of a specific domain. One of the co-founders had deep expertise in the pharma
    space. So he worked. He was General Manager at a company which got acquired by
    AstraZeneca. He worked there for 20 years. He's an absolute master of computer
    vision and pharma. That's a definite domain edge. Tech edges are people that have
    very specific skills in some tech. For example, there was a guy that did his PhD
    thesis on 3d printing human hearts. I don't know how many people do that.
  sec: 1069
  time: '17:49'
  who: Carmine
- line: It's as specific as it can get.
  sec: 1126
  time: '18:46'
  who: Alexey
- line: Absolutely. They give you this framework in order to start the conversation
    with the people. If you're domain edge, you will definitely talk about your domain.
    If you're tech end, you talk about that specific thing. If you're a catalyst,
    it's a bit more fluffy. You talk about what you're a most expert at and see what
    are the inter-weaving threads that you can find with other people. They are very
    interesting conversations. It's really like one of the best times ever. You can
    talk about crazy things from one day to another, you can have 10 conversations
    in one day where they span from "how to solve the climate issue" to "how to make
    a dashboard for FinTech companies". And there could be anything in between. You
    also go with your own gut feeling, trying to see who you will fit with, what kind
    of ideas are you most drawn to. You, of course, bring your ideas and you test
    them a little bit.
  sec: 1130
  time: '18:50'
  who: Carmine
- line: They have mentors who have a call with you every week. There are two mentors,
    actually. One is the relationship mentor. You can ask about "how can I approach
    people" or "there's something wrong in our relationship with my current co-founder,
    how can we fix it". You get the other mentor only if you have a team. They are
    quite experienced in the startup space. They will tell if what are you doing good,
    or what are you doing wrong in terms of market sizing. They help figure out if
    the idea has any chance of working. Every single week they give you a score between
    one and four. It tells you how you're going to do on the final examination. It's
    called the "Investment Committee", which happens in January.
  sec: 1213
  time: '20:13'
  who: Carmine
- header: The structure of EF program
- line: 'This entire thing starts in September. In January, you have investment committee.
    EF program is divided in few phases. The first phase is the form phase, which
    takes eight weeks. Here you try to find your co-founder. After the form phase,
    you have the company building phase: you have to prepare all the material for
    the Investment Committee. The Investment Committee is a bunch of venture partners
    from EF. We actually had Benedict Evans in our committee, amongst others, so it
    was a bit intimidating. It was very, very helpful and very, very useful for us
    in the future. Fortunately, we passed.'
  sec: 1283
  time: '21:23'
  who: Carmine
- line: That was my previous co-founder. I had a few teams in EF. My current co-founder,
    THE co-founder, is a machine learning scientist with a similar background, but
    much younger. He's 26. He just graduated from ETH Zurich. He was quite active
    in the entrepreneur space. This is now his third company. It's quite insane at
    26
  sec: 1326
  time: '22:06'
  who: Carmine
- line: They decide if they want to invest or not, right? That's the final examination.
  sec: 1335
  time: '22:15'
  who: Alexey
- line: That's the final examination.
  sec: 1339
  time: '22:19'
  who: Carmine
- line: If they want to invest, then you get the money. If they don't, then...
  sec: 1341
  time: '22:21'
  who: Alexey
- line: Then bye, bye.
  sec: 1346
  time: '22:26'
  who: Carmine
- line: I've heard some people still try to pursue the idea, to find other ways and
    find other investors.
  sec: 1349
  time: '22:29'
  who: Alexey
- line: Yeah. People that didn't get the investments, got other grants, or were incubated
    in other incubators, or went for competitors of EF. In the end, if you want it,
    you can do it. That's, that's a big lesson.
  sec: 1358
  time: '22:38'
  who: Carmine
- line: You mentioned that your co-founder has experience in pharma.
  sec: 1378
  time: '22:58'
  who: Alexey
- line: That was my previous co-founder. I had a few teams in EF. My current co-founder,
    THE co-founder, is a machine learning scientists with a similar background, but
    much younger. He's 26. He just graduated from ETH Zurich. He was quite active
    in the entrepreneur space. This is now his third company. It's quite insane at
    26.
  sec: 1326
  time: '22:06'
  who: Carmine
- line: "I don't know what's more insane \u2014 programming at five or that."
  sec: 1386
  time: '23:06'
  who: Alexey
- line: Thanks, and I hope that these credentials will come up in our products. He's
    very impressive in that sense. He founded a company in motion analysis, then another
    one in cryptocurrency, in China, while he was studying. And now FreshFlow. He's
    the CEO, he's only on the business side. And we decided that just because it fits
    more with what our backgrounds are. I have longer technical experience, and he
    has longer entrepreneurial experience. It works. And it's great to have a technical
    co-founder. We were an exception. That's why I said "spoiler alert" before.
  sec: 1428
  time: '23:48'
  who: Carmine
- header: Coming up with the idea
- line: How, when, and why this idea of your business came to your mind? From what
    I understood about your co-founder, he's doesn't strike me as a person who spent
    his life overseeing a supermarket. How did you actually get this idea?
  sec: 1487
  time: '24:47'
  who: Alexey
- line: As I said before, he was developing a computer vision recognition product
    during his thesis. He started to sell it to different supermarkets, he started
    to have calls with different supermarkets, being entrepreneurial-minded as he
    is. During these calls, he realised that there are a lot of problems in how these
    supermarkets order food. So something was already on his mind. At the same time,
    when I broke up with my team, the pharma guy, he also broke up with his teammate
    at the time. We found each other the last week before the closing of the form
    phase. We really wanted to have a startup.
  sec: 1509
  time: '25:09'
  who: Carmine
- line: "We were friends from the beginning with Avik. We were always having beers.\
    \ We were also trying to ideate with other people, obviously. You want to stick\
    \ to what EF people say \u2014 try to find a business person that started from\
    \ business. We were talking with a couple of people, but we found that we were\
    \ ideating much faster with each other. We started ideating about product recognition\
    \ \u2014 if we could use what he's done in his thesis. We started thinking, \"\
    We could do something for pricing. We can recognise if products are going bad\"\
    . I was thinking also in a \"social good\" sense because it's dear to my heart\
    \ to do something about climate change. It was a big topic between my projects\
    \ in EF. In the end, we started to see that there are a lot of problems with estimating\
    \ shelf lives and keeping track of what is going bad."
  sec: 1575
  time: '26:15'
  who: Carmine
- line: We started ideating in that sense. "Can we do something with computer vision
    that looks at fresh products, and tells you if they are going bad?" We thought,
    "maybe we can do an app?" With this idea, we went to the so-called "super check-in",
    which is like a mini Investment Committee. So, it's an app that you can use as
    a consumer. You can go in the store with it, take a photo of a fresh product.
    For a packaged product, you can take a photo of the barcode and the expiration
    dates. But for fresh products, we will do the analysis of the ripeness in the
    app using computer vision. Then it will give you a discount to apply at checkout.
    That didn't fly very well with the Investment Committee.
  sec: 1648
  time: '27:28'
  who: Carmine
- line: "So we went back to the drawing board. We learned from that. First of all,\
    \ it was hard for people to get another app just to get discounts. It's not enough\
    \ to have just discounts. Then we learned that it's not that easy to figure out\
    \ the shelf life of fresh products just using computer vision. So we pivoted.\
    \ We started thinking and realised, \"Oh wait, I remember this conversation that\
    \ I had with these people. I remember that wasted stockouts are a huge problem.\"\
    \ We wanted to avoid all that because our edges are in computer vision \u2014\
    \ we did a lot of computer vision. But we saw that this could be a much bigger\
    \ problem. Then we started looking at the numbers about food waste. And it's completely\
    \ mind-boggling! Just to give you an idea. Food waste is actually accounting for\
    \ six times more carbon emissions per year, than the entire aviation industry."
  sec: 1714
  time: '28:34'
  who: Carmine
- line: That's a lot.
  sec: 1795
  time: '29:55'
  who: Alexey
- line: It's insane. When I read that, I was like, "I can believe this. This is crazy."
    We're wasting $1.7 trillion per year on food that never gets sold. But someone
    has to buy it. The supermarkets have to buy it. And out of all food waste, supermarkets
    contribute to 10% of that. So if we can contribute to 10% of six times the aviation
    industry, we're almost fixing the aviation industry.
  sec: 1796
  time: '29:56'
  who: Carmine
- line: We got really, really excited. Then we saw that there are some exceptional
    companies in the US that are doing something similar. Some of them are Shelf Engine
    and All Fresh. They are doing well. And we really, really appreciate what they're
    doing. We wanted to follow suit and started our own company FreshFlow here.
  sec: 1835
  time: '30:35'
  who: Carmine
- header: How important is going through a startup accelerator?
- line: Nice. A question from Anika. How important is to go through a startup accelerator?
    Would you be able to do this without entrepreneur first?
  sec: 1859
  time: '30:59'
  who: Alexey
- line: No. As simple as that. You need to be extremely lucky to have the kind of
    connections that entrepreneur first gives you. Maybe go to a very specific place.
    For example, in Avik's case, ETH helped a lot because they have an entrepreneur
    club. If you're interested in that, you join the club, and you see a lot of people
    with ideas and professors that can help. People actually create their startups
    during university time. If you're in the Ivy League, there are a lot of people
    who start startups. But there was no such thing in Free University of Amsterdam
    and University of Bologna. I didn't find anything like that. Having these kinds
    of possibilities changes the game completely. I have a lot of friends now from
    entrepreneur first, just because we vibe so much together. We're also ambitious
    and creative and risk-taking.
  sec: 1871
  time: '31:11'
  who: Carmine
- line: So it's about building connections, it's about networking, right? If you have
    already a strong network, from your university, then you don't need it. I know
    that in Berlin there are startup meetups or founder dating meetups. It's possible
    to build this network. But entrepreneur first helps you do that.
  sec: 1946
  time: '32:26'
  who: Alexey
- line: "Yeah. I would say it's still hard. Even though you would have the network,\
    \ then you need to find a co-founder that is really driving with you. You need\
    \ to have the time to think about the idea and really develop it \u2014 and try\
    \ to do it as quickly as possible. That's always the conundrum of being in a startup.\
    \ You want to always be one step ahead of you are. That requires a lot of time.\
    \ I'd say without entrepreneur first it would have been really, really hard."
  sec: 1973
  time: '32:53'
  who: Carmine
- header: Finding your first client
- line: How did you find your first client? Running a pilot with Edeka is awesome.
    Is it your first client?
  sec: 2004
  time: '33:24'
  who: Alexey
- line: Technically, we had also another client, which came from Avik's previous dwellings
    in the supermarket space. This other client is actually Volg, which is the third-largest
    supermarket chain in Switzerland. In Volg we tried a slightly different product.
    We did a pilot, and it went well. For the first client in Germany, Edeka, we entered
    through the Edeka foodtech campus, which is a startup accelerator by Edeka. They
    also give you mentorship and they connect you to the right Edeka stores that are
    perhaps more open-minded to new things. After explaining our idea, we got in.
    We connected to the right people in Edeka and we refined our idea and our product.
    And then we started working with Edeka Cassius.
  sec: 2013
  time: '33:33'
  who: Carmine
- line: Was it before you graduated from entrepreneur first? Or after?
  sec: 2079
  time: '34:39'
  who: Alexey
- line: After.
  sec: 2084
  time: '34:44'
  who: Carmine
- line: So you don't need to get a client to graduate, right?
  sec: 2085
  time: '34:45'
  who: Alexey
- line: "Well, it'd be beneficial. But they bet on us. First of all, we formed the\
    \ last week of form phase. We had only four weeks to get our narrative together,\
    \ get the pitch deck, get all of the things together \u2014 all of the possibilities\
    \ for the future and the business model. Quite a lot of work in a short amount\
    \ of time. After that, you start building. We started building the algorithms\
    \ and other things at the same time. It was quite busy anyway."
  sec: 2090
  time: '34:50'
  who: Carmine
- line: 'But you may need to show that you have some traction early on. We already
    had some traction at the time: we had a few leads with other supermarket chains
    in Italy, and in Germany. It didn''t go through at the end, but we had around
    4-5 leads. There needs to be some traction for sure.'
  sec: 2130
  time: '35:30'
  who: Carmine
- line: How long did it take to get the first client? The time between coming up with
    the idea and securing the first client.
  sec: 2156
  time: '35:56'
  who: Alexey
- line: Unfortunately, the supermarket space is not that fast. The sales cycle is
    quite long. Our contract with our first Edeka store was signed in April. And we
    graduated from EF in January. We officially registered as a company also in April.
    It just takes time to do that. There's a lot of paperwork here in Germany.
  sec: 2167
  time: '36:07'
  who: Carmine
- header: Finding investors
- line: I also prepared a question about investors. I guess you answered that. So
    entrepreneur first acts as an investor. There is a board and they decide whether
    they should invest in you. Is it the only investor you have?
  sec: 2200
  time: '36:40'
  who: Alexey
- line: Ish. There are things that we will announce later. But at the moment, officially,
    there is only them. We're lining up angel investors at the moment. And we have
    an amazing guy as an angel investor, which we'd love to announce, but it's in
    the works.
  sec: 2217
  time: '36:57'
  who: Carmine
- line: You don't have to announce now, but maybe you can tell us about the process.
    How do you actually do this? With an entrepreneur firstly, this committee decides
    if they invest or not. But once you don't have the support from EF, how do you
    go about finding an investor?
  sec: 2240
  time: '37:20'
  who: Alexey
- line: EF gives you a fundraising manager after you graduate. They help you with
    structuring the narrative to find the investors. They also give you a platform
    called "Demo Day", which, in Corona times, is just a web page with some YouTube
    videos. It used to be that you go to a theatre and give a pitch in front of 100
    invited investors.
  sec: 2259
  time: '37:39'
  who: Carmine
- line: 'We decided to not go for them. We found that we need to be proven with the
    numbers and the measures that we get from the pilots in order to gain traction
    since it''s such a slow industry. Also, it''s very hard to sell to supermarkets.
    Because imagine you''re substituting the core parts of the entire ordering system
    of the supermarket. Think about what a supermarket does: you get stuff in and
    you get stuff out. You have to present them well. So we fix the "get stuff in".
    And then they have to think about "present them well" and "get stuff out". It''s
    pretty hard to sell. And we want to raise on our terms later.'
  sec: 2290
  time: '38:10'
  who: Carmine
- line: What are the places where people can look for investors? Are there meetups?
  sec: 2356
  time: '39:16'
  who: Alexey
- line: Well, investors approached you actually.
  sec: 2362
  time: '39:22'
  who: Carmine
- line: How do they find you? Do you just post on LinkedIn "Hey, I'm looking for investors"?
  sec: 2366
  time: '39:26'
  who: Alexey
- line: They search for you on LinkedIn. Just by the fact that you have a "co-founder"
    in the name. Also, they may have bots that parse the register of companies in
    Germany. The VC firms know all the companies. They have a bunch of analysts who
    go through all these companies. They look them up, they see what they're doing.
    If they think it's good enough, they will shout an email.
  sec: 2372
  time: '39:32'
  who: Carmine
- line: It's not that hard to find an investor. But finding good investors is up to
    you. There are investors that you want to have on your board. They have specific
    expertise. For example, investors in the foodtech industry are great for us. Other
    high-profile investors are usually less hands-on, they care rather than control.
    You need to do a little bit of the work to get them, perhaps approach them yourself.
  sec: 2407
  time: '40:07'
  who: Carmine
- header: Consequences of having a bad investor
- line: You said that there are just investors and there are good investors. What
    could be the consequences of going with a bad investor?
  sec: 2413
  time: '40:13'
  who: Alexey
- line: You may get a bad term sheet, where they take a lot of your equity for not
    so much money. You may get people on the board who are trying to control too much.
    There's not so much trust, but it's rather a culture of "We give you the money.
    We want the money back immediately. Grow as fast as possible. Blah, blah." It's
    common that investors want to do that. It's their job, ultimately. But some of
    them do that in an empathetic, nurturing way that is more enjoyable for everybody.
    And some do it in a more predatory way. At the moment, we don't have anybody on
    the board, because EF gave us a convertible note. So it's very, very chill and
    very quiet. Maybe Avik, my co-founder, would have more insights into this question.
  sec: 2464
  time: '41:04'
  who: Carmine
- header: Splitting responsibilities between co-founders
- line: You have pretty similar profiles. Even though he's more entrepreneurial, both
    of you are engineers. How do you split your responsibilities? What do you do?
    What does he do?
  sec: 2544
  time: '42:24'
  who: Alexey
- line: At first, we wanted to do everything together. But then we decided it was
    not going to help much because we'd have to synchronise ideas on every single
    little thing. And the productivity gains aren't much higher. But it's good at
    first to think about the major things together.
  sec: 2563
  time: '42:43'
  who: Carmine
- line: 'But now, I''m fully the CTO. I do all the tech except the mobile app. He
    does all of the sales and business development: the outreach to possible clients,
    talking to them, talking to investors, making the pitch deck. I do all the pipelines,
    the code, data mangling, the dashboards, connections to the app, machine learning
    algorithms, and experiments. All the engineering stuff.'
  sec: 2588
  time: '43:08'
  who: Carmine
- header: Hiring
- line: Do you have other people in the company now?
  sec: 2627
  time: '43:47'
  who: Alexey
- line: Yeah, we do. We had the mobile developer, a freelancer. He created the app.
    Amazing guy. Unfortunately, his contract ended. But we hope that in the future
    we can work together. He did an amazing job. We also have a working student from
    the University of Mannheim. He helps Avik with the business side. We're going
    to start hiring more people soon.
  sec: 2630
  time: '43:50'
  who: Carmine
- header: The importance of delegating
- line: Since the topic of hiring is already on your mind. How do you decide who to
    hire first? You needed an app, you hired a freelancer. But for a permanent employee,
    how do you decide who to hire first?
  sec: 2673
  time: '44:33'
  who: Alexey
- line: 'It''s the same thing for the app and for the permanent person. It''s very
    simple. When you hire, you know what you need. But a good principle is don''t
    try to do everything yourself if you''re not an expert in it. Ask for help. "Asking
    for help" in this case means hiring someone. At first, I thought I could pick
    up Flutter and do the app. But it would have pushed us several months back: I
    would need to learn a new language, then code the app in that language. I would
    probably do a worse job than what Jeremiah did. So, in the end, it doesn''t really
    make sense. We had the investment already. So why not use it and spare my time
    to do something that I can do much better.'
  sec: 2697
  time: '44:57'
  who: Carmine
- line: As a co-founder, you need to know how to delegate, right? You need to let
    things go and not try to do them yourself. I am pretty sure you will do an app,
    but it will just take more time.
  sec: 2770
  time: '46:10'
  who: Alexey
- line: Exactly. You may want to be the one doing all of it. But it's not shameful
    at all to ask for help. And it's appreciated by the clients as well, they see
    the product faster. By the investors, because they see their money back faster.
    So, by everybody.
  sec: 2785
  time: '46:25'
  who: Carmine
- header: Making work attractive to hires
- line: I don't know if you had this problem. But I imagine that you as a startup,
    the package you can offer to candidates is less attractive than what big established
    companies such as Zalando, Amazon or OLX can offer. How can you manage to make
    this offer package attractive? Have you thought about this? How to attract people
    to work at a startup?
  sec: 2813
  time: '46:53'
  who: Alexey
- line: We hired internationally. We were not afraid to go into different countries.
    And fortunately, our mobile dev joined because he loved the technology, and he
    wanted to do something in that technology. He used to do it in his free time.
    He felt that he can at least have some money out of it.
  sec: 2845
  time: '47:25'
  who: Carmine
- line: This is a special case of an extremely passionate person who really wanted
    to bring something to the world. And maybe also have fun and some money. In general,
    our offer was attractive, because we'd pay the same rates in all parts of the
    world. For example, for an Indian developer, that would be an amazing salary.
  sec: 2874
  time: '47:54'
  who: Carmine
- line: So for somebody from Berlin, it will be an okayish one. If they go to a bigger
    company, maybe they would offer more. But for somebody from a place where the
    average salary is lower than in Germany, for them is great.
  sec: 2902
  time: '48:22'
  who: Alexey
- line: COVID opened this amazing possibility of remote working to everybody. We just
    opened our eyes and we were like, "Wait, we can do this". So we just took advantage
    of that.
  sec: 2919
  time: '48:39'
  who: Carmine
- header: Plans for the future
- line: Nice. What are your plans for the future?
  sec: 2932
  time: '48:52'
  who: Alexey
- line: More clients, more product, more shipping, more launches, more money, more
    investors more hires, bigger clients. And grow from there. This is of course the
    plan. But in the longer-term future, we want to be the grocery food retailer OS
    where it's a one-stop-shop for all of their logistics and supply chain needs.
    We also want to go in the other steps in the chain, So go up to the distribution
    centers, the fulfilment centers, and maybe go beyond that towards even the farmers.
    There's so much that can be done at all these levels to predict what kind of food
    needs to be on the shelves of the supermarkets.
  sec: 2936
  time: '48:56'
  who: Carmine
- header: Just-in-time supply chain
- line: We can have so much impact by having one solution that would enable the just-in-time
    supply chain of Toyota. For example, I need a banana right now, because I'm hungry.
    My system will know, "it's Friday, it's 6pm, Carmine just had a long day and wants
    a banana". It then preemptively would predict that months in advance. The farmer
    will be like, "Okay, I need to produce this many bananas".
  sec: 3014
  time: '50:14'
  who: Carmine
- line: I think Amazon is doing that already. I sometimes feel like Amazon can read
    my mind. I ran out of shampoo recently. I went to buy it. And then, on the first
    page, it was already recommending me the shampoo.
  sec: 3050
  time: '50:50'
  who: Alexey
- line: Interesting. That's another side, the recommendation side, which is quite
    similar to forecasting. I learned a lot of things at OLX that come back here in
    this work. It would be much more towards forecasting. With the just-in-time supply
    chain, you have a lot less inventory space. That means less need for huge warehouses,
    less need for transportation. Trucking and all burn a lot of fossil fuels. That's
    not great for the environment. It's not just the problem of "the rotten food releases
    CO2 to the planet".
  sec: 3064
  time: '51:04'
  who: Carmine
- line: A lot in the supply chain can be fixed by ordering the exact amount. Ordering
    the exact amount is really, really hard. If you order too much, you're producing
    just waste. The retailers do that, because they don't want to have empty shelves.
    That's really bad. That means losing customers. The customers will go to another
    store if their shelves are empty. With fresh products, you have them in boxes.
    So if you have the last bananas or the last two bananas, it's basically like the
    shelf is empty. Because nobody takes the last two bananas.
  sec: 3114
  time: '51:54'
  who: Carmine
- line: Yeah, I know. I wouldn't.
  sec: 3156
  time: '52:36'
  who: Alexey
- line: Exactly. You think something is wrong with them. Given this consumer behaviour
    and other factors, they need to keep stocking the shelves. It's really hard to
    stock them to look full even at the end of the day and there's nothing in the
    backroom. We found that it's not the case. Because it's really tough. So we tried
    to fix that problem.
  sec: 3159
  time: '52:39'
  who: Carmine
- header: What would you have done differently?
- line: Would you do anything differently now if you were starting again?
  sec: 3189
  time: '53:09'
  who: Alexey
- line: Yes. I would not use open-source infrastructure. I'd directly use GCP. We
    switched to it from Kubeflow, an open-source MLOps infrastructure. It was fantastic
    when it worked. But then we upgraded it to 1.3, and it started breaking in different
    ways. Also, 1.2 gave us a lot of trouble with the installation. I spent one and
    a half months taking care of Kubeflow. For a startup, it's not a great idea. At
    the end, I just said "fine, we use GCP". I'm glad we went for GCP. It has much
    better interfaces and software compared to AWS.
  sec: 3193
  time: '53:13'
  who: Carmine
- line: We're using BigQuery, Cloud Run, and Cloud Functions. It's an event-driven
    architecture. Everything that comes in gets pushed around in these pipelines.
    We use FireStore for the app API. It's lightning-fast. It's beautiful. And it
    just works.
  sec: 3261
  time: '54:21'
  who: Carmine
- line: So, for people who are starting a startup, you'd advise going with a managed
    solution, right?
  sec: 3282
  time: '54:42'
  who: Alexey
- line: Yeah. Go with a managed solution instead of an open-source solution. At least
    at first. Also, Google and AWS give startups some credits if you're invested by
    an accredited investor of them. We received 100k in credits from Google. It means
    that we can use their most expensive solutions, and sleep well at night.
  sec: 3291
  time: '54:51'
  who: Carmine
- line: So they bet on you, they bet that you will grow. That's why they invest 100k
    in their services in you. That's very nice.
  sec: 3328
  time: '55:28'
  who: Alexey
- line: Yeah. And in the end, if you like their services, you will continue. This
    is one of the things in the tech space that we could have done differently.
  sec: 3337
  time: '55:37'
  who: Carmine
- header: Advice for people starting a startup
- line: Do you have any other advice for people who would like to start building a
    startup now?
  sec: 3351
  time: '55:51'
  who: Alexey
- line: Everybody says the same. "It's going to be hard. You're going to have tough
    times." It is true. Just be prepared. Be emotionally intelligent. Sometimes a
    sales call doesn't go well. It's not you, okay. It's not personal. Maybe sometimes
    you don't talk about the specifics of your solution. There's no need. Sometimes
    you can say just "IP". There could be a concern that you cannot address at the
    moment because you're just too small. You don't know certain things.
  sec: 3367
  time: '56:07'
  who: Carmine
- line: "You struggle at first because you want to have the best clients \u2014 in\
    \ order to have the best contracts \u2014 in order to have the best investors\
    \ \u2014 in order to be able to hire the best people. But you're not there yet.\
    \ And you're always trying to get to that point. It's really hard to cope with\
    \ all the loads that you put on yourself. Be mindful of that."
  sec: 3412
  time: '56:52'
  who: Carmine
- header: "Don\u2019t focus on skills only"
- line: And, I would say, find a co-founder who's on the same page with you, somebody
    you can communicate really well with. They don't have to be the best salesperson
    in the world if they're on the business side. Or they don't have to be the best
    technical person in the world. It helps, but up to a certain percentage.
  sec: 3429
  time: '57:09'
  who: Carmine
- line: My girlfriend is a recruiter. She recently did a presentation that says that
    you should hire for 10% skills. The framework is, how much skills, behaviour,
    and motivation play out in the final performance of employees. The skills are
    about 10% to 20%, and the rest is motivation and behaviour. So, hire people for
    motivation and behaviour. If you get motivation, behaviour, and skills, you're
    golden. But you're going to speak every day with your co-founder. If he's motivated
    enough, he's going to figure it out. If his behaviour is great, he's going to
    figure it out as well. So that's another advice. Try to get people who don't fixate
    too much on skills.
  sec: 3470
  time: '57:50'
  who: Carmine
- header: Getting motivation
- line: How do you get continuous motivation to do this stuff in a startup when things
    don't work as good as you expect?
  sec: 3554
  time: '59:14'
  who: Alexey
- line: "This is kind of in you. I don't know if there is a way to get motivation.\
    \ For example, I really care about climate change and the food waste problem.\
    \ It seems to be the underdog of the climate change spectrum of problems. It's\
    \ right there in front of us, and it is massive \u2014 six times the number of\
    \ CO2 emissions of the aviation industry. If you think about food waste as a country,\
    \ in terms of carbon emission it will be the third country in the world. After\
    \ the US and China, there'll be food waste, and then it will be India with half\
    \ of the carbon emission of food waste. That's just insane. It seems we have to\
    \ do this. Also the opportunity space is pretty big. The food retail industry\
    \ is now the process of digitalization, and the opportunity for companies like\
    \ ours is great. And then you work with the right people. That's what you need.\
    \ But motivation comes from the inside \u2014 from what you care about."
  sec: 3579
  time: '59:39'
  who: Carmine
- header: Am I ready for a startup?
- line: 'The next question: "I''m 30 years old. I want to be a CTO in the startup
    that I''m launching with a CEO." I guess, it''s pretty similar to what he did.
    His main focus is machine learning and knows little about front-end development,
    DevOps, and all these things. The question is, do you think it''s enough to start
    as the CTO or not?'
  sec: 3665
  time: '1:01:05'
  who: Alexey
- line: It could be tough sometimes. But if you use a managed solution, and you can
    spend some time learning new concepts, I don't think it's a problem that you have
    only the machine learning background. What I said before, the framework that they
    used in my girlfriend's company, 10%-20% skill, 50% motivation, and then the rest
    is behaviour.
  sec: 3695
  time: '1:01:35'
  who: Carmine
- line: Do you think he should learn something now before becoming a founder?
  sec: 3724
  time: '1:02:04'
  who: Alexey
- line: For sure. Much better now. Because then you have the pressures from investors,
    from clients, from your co-founder and your hires. So please, start as soon as
    possible.
  sec: 3728
  time: '1:02:08'
  who: Carmine
- line: But then you will never start. You will always think, "I'm not ready yet.
    I need to learn this thing. I have this new framework. There is this new book
    that everyone says it's good." How do you know that you already?
  sec: 3739
  time: '1:02:19'
  who: Alexey
- line: You don't. You will never feel ready. I have more than 10 years of experience
    in software engineering. And yet I didn't think I was ready for a startup. Until
    I joined the FN, I was like, "Wait a second, I'm actually not that bad. I can
    actually do this." You can also jump in and figure it out on the spot.
  sec: 3753
  time: '1:02:33'
  who: Carmine
- line: If you go for entrepreneur first. If you get in, start as early as possible.
    Not necessarily technical stuff. But things like figuring out the problem space.
    Start doing something if you can. But also don't be afraid of just jumping in.
    I actually think that just jumping in will propel you to know these things by
    itself. It's a bit of a balance. I know, this answer sucks. Because "what is it
    exactly that you're trying to recommend?" But either works if you have enough
    motivation.
  sec: 3781
  time: '1:03:01'
  who: Carmine
- header: Importance of a business school
- line: What do you think about the importance of a business school?
  sec: 3825
  time: '1:03:45'
  who: Alexey
- line: Not important whatsoever.
  sec: 3830
  time: '1:03:50'
  who: Carmine
- line: You'll be fine without going to a business school and without an MBA. Right?
  sec: 3834
  time: '1:03:54'
  who: Alexey
- line: What I learned from other friends who did MBAs is that you don't need one
    for a startup. They teach concepts for running large-scale businesses. In a startup,
    you have a set of challenges that are specific to your markets. You don't need
    to know these grand schemes of things kind. You don't need to know a lot about
    a specific business case or a specific thing in a very structured way. It's is
    much more about shipping it as soon as possible. That's what you want to do.
  sec: 3842
  time: '1:04:02'
  who: Carmine
- line: So it's more about the mindset, right?
  sec: 3886
  time: '1:04:46'
  who: Alexey
- line: Yeah.
  sec: 3888
  time: '1:04:48'
  who: Carmine
- header: Advice on finding a co-founder
- line: What happens if you don't find a co-founder?
  sec: 3907
  time: '1:05:07'
  who: Alexey
- line: Then you're out.
  sec: 3910
  time: '1:05:10'
  who: Carmine
- line: You have to have a co-founder?
  sec: 3915
  time: '1:05:15'
  who: Alexey
- line: You have to have a co-founder when you are in the form phase. They give eight
    weeks. Use them correctly. If you go for EF, try to get into a team as soon as
    possible. Don't waste your time thinking, "is this the right person?". Figure
    it out, get some answers, of course, don't get into it with the first person that
    you meet. But if you vibe enough, just go for it. That's kind of the startup mentality.
    Just go for it.
  sec: 3917
  time: '1:05:17'
  who: Carmine
- header: Do I need EF if I already have an idea?
- line: Would you recommend starting with EF if you already have a clear idea?
  sec: 3957
  time: '1:05:57'
  who: Alexey
- line: I would actually start with EF even though you have a pre-existing idea. I
    also had a pre-existing idea. I actually tried it in the first few weeks of EF
    with another team. We figured out that the market wasn't ready for that idea.
    Being in EF will teach you how things work in the real world. Sometimes you're
    stuck in your own bubble. We worked at OLX, we may know a lot about marketplaces
    and data science. But not about the business side of things, like how investors
    think about who to invest in and so on. It will give you that kind of mentality.
  sec: 3969
  time: '1:06:09'
  who: Carmine
- header: Having a prototype before the pitch
- line: The last question for today. Did you already have a prototype before your
    pitch?
  sec: 4026
  time: '1:07:06'
  who: Alexey
- line: For the first pitch, for Super Check-in, we had a demo for recognizing the
    ripeness on bananas only. It was web-based, with TensorFlow JS. But we didn't
    have a demo for the forecasting solution.
  sec: 4031
  time: '1:07:11'
  who: Carmine
- line: You just need to be able to pitch this idea, have this idea very clear, so
    that the investors can imagine how it will look like?
  sec: 4058
  time: '1:07:38'
  who: Alexey
- line: They want to see that the market is big enough. And that you're the right
    people for the job. And you can find clients. They usually trust you on the tech
    side if you have the credentials for it. They look at your CV, they're not going
    to make a technical interview.
  sec: 4071
  time: '1:07:51'
  who: Carmine
- line: That's good. We can put a few things more there. No, that's bad advice.
  sec: 4098
  time: '1:08:18'
  who: Alexey
- header: Contacting Carmine
- line: So the last one. How do people find you?
  sec: 4105
  time: '1:08:25'
  who: Alexey
- line: "I'm on Twitter @paolino. I'm also on LinkedIn, just search for my name Carmine\
    \ Paulino. I have a website that I don't update \u2014 paulino.me. Also freshflow.ai\
    \ is our website for FreshFlow. If you want to email me, my personal email is\
    \ carmine@paulino.me. If you want to email me for work, it's carmine@freshflow.ai."
  sec: 4109
  time: '1:08:29'
  who: Carmine
- line: Thank you very much for joining us today and for sharing your experience with
    us. Also thanks to everyone for watching, for being active, and for asking all
    these questions.
  sec: 4138
  time: '1:08:58'
  who: Alexey
- line: Thank you so much, Alexey. It was really nice.
  sec: 4148
  time: '1:09:08'
  who: Carmine
- line: Yeah, it was really great. Thanks a lot, everyone and have a great weekend.
  sec: 4150
  time: '1:09:10'
  who: Alexey

---


Books:

* The Mom Test by Rob Fitzpatrick
* Design Thinking by Robert Curedale

Links:

* [FreshFlow](https://freshflow.ai/){:target="_blank"}
* [Carmine's LinkedIn](https://www.linkedin.com/in/carminepaolino){:target="_blank"}
* [Carmine's Twitter](https://twitter.com/paolino){:target="_blank"}