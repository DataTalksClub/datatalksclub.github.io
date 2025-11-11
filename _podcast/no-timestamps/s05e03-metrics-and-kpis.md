---
title: 'KPI Design & Metrics Strategy: Prioritize Impact, Avoid Vanity Metrics, and
  Prove ROI'
short: 'Defining Success: Metrics and KPIs'
guests:
- adamsroka
image: images/podcast/s05e03-metrics-and-kpis.jpg
season: 5
episode: 3
ids:
  youtube: H4P2RfKvXGs
  anchor: Defining-Success-Metrics-and-KPIs---Adam-Sroka-e17gfp0
links:
  youtube: https://www.youtube.com/watch?v=H4P2RfKvXGs
  anchor: https://anchor.fm/datatalksclub/episodes/Defining-Success-Metrics-and-KPIs---Adam-Sroka-e17gfp0
  spotify: https://open.spotify.com/episode/5kTD7LjoXos1fm2LPD7nJc
  apple: https://podcasts.apple.com/us/podcast/defining-success-metrics-and-kpis-adam-sroka/id1541710331?i=1000535667935
transcript:
- line: This week we'll talk about metrics and KPIs. We have a special guest today,
    Adam. Adam is the head of machine learning engineering at Origami Energy. He's
    an experienced data and AI leader. He helps organizations find value from data
    by building high performing teams – data teams, analytic teams – from the ground
    up. Adam also hosts a podcast. Is that right?
  sec: 90
  time: '1:30'
  who: Alexey
- line: Among other things. It’s slightly related to data and technology. But yeah,
    thanks very much for having me on. I am excited to talk about something I don't
    normally get a chance to talk about – KPIs and how to measure success and things
    like that.
  sec: 114
  time: '1:54'
  who: Adam
- line: Welcome. Thanks for agreeing to come on. Before we go into our main topic
    of metrics, let's start with your background. Can you tell us about your career
    journey so far?
  sec: 131
  time: '2:11'
  who: Alexey
- header: Adam’s background
- line: I always start way back in the mists of time when I was a bartender – a competition
    bartender – I absolutely loved doing that. I traveled around Europe making cocktails,
    winning, and sort of being drunk for a living, which was good fun for a while.
    I realized I wasn't going to make enough money to buy a bar by working in one.
    So I thought “I'll go back to uni and get a proper job.” Went back to physics
    – really hot, really enjoyed that. Towards the end of it, I did a bit of coding.
    I went on to do a computational doctorate at the University of Strathclyde. That
    was modeling high power lasers. You might see some laser textbooks on the bookshelf
    behind me there. That was really good fun. It was towards the end of that that
    I started looking at reinforcement learning and data science things, just out
    of interest. I actually used some reinforcement learning in designing components
    for lasers, as part of that research. That was really good fun and it really opened
    my eyes up to what you could do with this kind of stuff. As much as I love physics
    and working with lasers, I realized that I didn't actually care too much about
    the domain.
  sec: 142
  time: '2:22'
  who: Adam
- line: I just liked doing numbers on the computer, and I wanted to explore what you
    could do with some of these tools. What really appealed to me was the idea that
    if you learn some of the data science approach techniques and some of the ways
    of working, you can step into almost any domain – any organization – and offer
    value. Given a little bit of time and data, I can probably show you some charts
    or some models that might highlight some insights that you haven’t seen before,
    without being an expert in that field. Now, that’s quite a dangerous statement
    to make. I do stand by the fact that the absolute best people in the field are
    those that know their domain inside out. You can't really compete with those people
    if they have all the technical expertise and the tools and techniques as well.
    But you can go quite a long way as being a bit of a generalist and just being
    very good at applying statistical approaches and things like that.
  who: Adam
- line: So – physical doctorate, then I went on to start an online retail start-up
    with about six people in the east end of Glasgow. That was great fun. We were
    looking at trying to predict return behavior. Something like 30% of all orders
    for fashion (especially online) get returned. If you attribute, say, even a two
    pound cost per return to each item, for some organizations that adds up to millions
    of pounds worth of returns. They did a lot of clustering and you can really quickly
    spot some negative permanent/lifetime value customers by their early shopping
    behaviors. Actually, they're the same people that get flagged for lots of marketing
    and promotional material, because they spend a lot. It's a really good product,
    but it didn't do very well at that company. I left and then it kind of disappeared
    shortly after. It was just a hard thing to sell to companies. You're essentially
    telling sales executives to sell less stuff and that's quite a hard message to
    get across from this upstart startup in Glasgow.
  who: Adam
- line: From there I went into insurance. I absolutely loved that. That was really
    eye opening because the amount of information you get in car insurance when working
    in the pricing team – you can find out a lot about people. You can pull some really
    cool and interesting models. There's a lot of money involved, so there's lots
    of investment. There’s lots of impact that you can make by doing small changes.
    I talk a lot about that in some of the talks I do for beginners, like “Look, if
    you're trying to make a big impact, try and find massive revenue numbers or huge
    numbers that you can make small percentage changes in. They're the easy wins to
    get started with trying to make huge, 20-30% cuts in things from the get-go.”
    These are usually problems lots of people have already thought about, so thinking
    you're going to come in and completely change the game - apply a little bit of
    hubris. I just think that with insurance, there’s loads of money involved, so
    you can make a big impact. I had a great time there.
  who: Adam
- line: Then I went on to work for a consultancy. That's kind of where my journey
    changed a little bit. I've been a data scientist now for a few years. I was a
    senior data scientist at Incremental Group in Glasgow – a great consultancy. They
    do some really interesting stuff for small to medium enterprise customers. While
    they were offering positions, I restructured the business and I got offered the
    position to act as the data and AI director. That meant taking on the leadership/management
    role of the data science team, but also data engineers had BI consultants as well,
    and a few DevOps people and things like that. That was my first real exposure
    to BI – things like metrics and that kind of consultancy.
  sec: 392
  time: '6:32'
  who: Adam
- line: We were trying to help organizations turn their ‘business as usual’ into stuff
    that was actually measurable. We could build the dashboards and charts. You're
    trying to sell them charts and dashboards – that's how we made our money. But
    that's when I started to come across some of the techniques for helping people
    in these workshops. Take a huge bakery as a customer example. They know how to
    run their business really well. It's family owned, it’s a huge company, it’s been
    working fine for years. Why change anything? Helping them take their ingrained
    experience and ‘gut feel’ and turn it into “What are the actual numbers that a
    layman like me could come along and understand on a chart?” “Okay, these are the
    things that drive performance.” That was quite enlightening for me to learn. I
    definitely wasn't the expert there. I'm definitely not the sort of person who
    claims to be an expert on it. I always think there's more to learn in that kind
    of space. Learning to work with BI teams and data teams in that regard was really
    helpful in a consultative role.
  who: Adam
- line: I was there for three years and very recently gone for the position at Origami.
    The stuff they're doing at Origami is super cool, it’s really interesting for
    me to try and help transform the energy sector. To be able to enable green energy
    to come in more easily, more readily, and do lots of very big, very complicated
    problems. Again, large scale stuff – high impact. I jumped at the chance, really.
    Even though doing consultancy was great fun.
  who: Adam
- line: That’s cool. Doing reinforcement learning with lasers, I think that's the
    coolest thing I heard today.
  sec: 533
  time: '8:53'
  who: Alexey
- header: Adam’s laser and data experience
- line: I did some cool stuff in my PhD, I won't lie. The core of my project was looking
    at using ray tracing techniques for laser software. In other words, using ray
    tracing software to design lasers. There are a few projects there. Z Max is the
    one that we used that worked for a huge, huge organization called Tallas. Z Max
    is lens design software – you can build basically any kind of lens and do lots
    of very clever stuff with it. You can't model laser material or laser-gain material
    in it. That was always a big thing that upset people. That was a shame - everybody
    in the company uses Z Max but it doesn't do laser materials, so the laser team
    was upset.
  sec: 540
  time: '9:00'
  who: Adam
- line: Another piece of software that allowed me to manipulate it was MATLAB. Once
    I'm in MATLAB, I can do what I like. It was annoying because I built this stuff
    to automate Z Max and then a couple years after I finished, it became a part of
    the product. They actually had a big open library to do some of the stuff that
    I've done. I'd spent months building it that way. It was a bit ropey because I
    wasn’t a very good software engineer. Still am not. Yeah, it was great fun. Anyway,
    we got to a point where I did a few really cool projects, but one of them was
    looking at designing components that don’t only give the best performance for
    laser output via beam shape and power and things like that. But we're actually
    really resilient to misalignment.
  who: Adam
- line: Lasers are basically rubbish – all lasers are rubbish. There's an industry
    joke, which I actually think crosses over to data science and machine learning.
    A lot like in laser manufacturing, there's this thing that “Do it if it’s the
    best way to do something, or if there's no other way of doing it.” Essentially,
    with lasers it’s “Is there any other way of doing what you're trying to do? Don't
    use a laser. But if you have to use a laser, then go for it.” I feel like that's
    true for machine learning as well. If there's no other way of doing it – if you
    can do it with a basic model, something really simple – try and use that first.
    I bring that into the way that I work now. When designing these components, you
    would typically go and ask someone that's done it for four years, “What did you
    use for these parameters, blah, blah, blah.” Use their experience – they want
    to really help. We got this big piece of software that can simulate lasers now,
    because I've built it. Then I attached some sort of very rudimentary reinforcement
    learning thing with a few parameters to allow it to churn through.
  who: Adam
- line: I actually started with genetic algorithms to design the system, and then
    I did a little bit of stuff with reinforcement learning. This was back in 2014,
    and I was kind of self-taught. It wasn't as far on as it is now. Something I'd
    love to go back and do. It came up with some interesting stuff. Some of it was
    mainly poorly formulated – within the realm of the software, it was fine, but
    it would have been impractical to manufacture. It gave some novel insights and
    some that stuff was used or it's been investigated a bit further. I think. I'm
    not in the company anymore. I'm out of the loop. What they have done with it –
    Who knows?
  who: Adam
- header: Metrics and why do we care about them
- line: Coming back to the boring topic of metrics – I imagine that when you worked
    on reinforcement learning with lasers, you needed to track some metrics to measure
    the success of your project. What is a metric? Why do we care about metrics?
  sec: 726
  time: '12:06'
  who: Alexey
- line: Back to that thing of “why?” Like Peter Drucker says, “If you can't express
    it in numbers, you can't manage it.” There are a lot of ways to look at this and
    it's a point in the sand. I'm a big fan of getting going with metrics before you've
    got the right one, or before you've got them measured properly. I feel that people,
    sometimes friends, spend too much time trying to find the perfect metric. They
    do too much planning without actually getting going. Think about calibration errors
    – as long as you keep measuring the same way, you can kind of see where they are.
    Once you figure it out later, you can go back and rectify things.
  sec: 744
  time: '12:24'
  who: Adam
- line: A metric is essentially just a form of measurement. It's something to measure
    against. You take an output and turn it into a number so that you can apply it
    on a chart and start seeing where it goes. For example, in laser design, you want
    high power and that's got to be above a threshold. It's a really easy example
    to use. You have a technical specification that the laser – the piece of equipment
    that you're building – must meet. It must operate to minus 30 degrees and to plus
    70 degrees. It must withstand the force of exit. I must have a pulse length no
    longer than this and no shorter than this. Bah, bah, bah, bah, blah, there's also
    safety standards. These are all numbers – they're threshold metrics, a lot of
    them. You have to hit all these threshold metrics. That's really handy for something
    like a reinforcement learner, because you just fire all those in and you say,
    “Build me a system that hits these metrics.”
  who: Adam
- line: Now, in a system like that, we've got maybe 10 threshold metrics. There are
    probably an infinite number of solutions to that, right? You can find lots of
    solutions within that space. The challenge comes in when you want to find the
    optimal solution. Then you've got a really difficult problem to solve. That is
    where you start comparing your metrics to one another and try to improve them.
    When you're in high dimensional metrics, it becomes a messy bit. That's where
    a lot of things like running businesses and turning your models into business
    value are. I’m a big fan of using merit functions. Essentially, much as you would
    with a model, you take certain values – some of your metrics – and give them a
    weight. You add them up and you give that a score. People can get really lost
    in the weeds with defining what those weights are and how important certain things
    are. You can gain your own metrics by just keeping tweaking the nodules until
    you get what you want. There's a really good XKCD comic about that, which says
    you can just keep stirring the numbers until it gives you the output you desire.
    Don't do that, obviously – pick something and go for it.
  who: Adam
- line: That's what you do in machine learning, right?
  sec: 905
  time: '15:05'
  who: Alexey
- line: Exactly.
  sec: 906
  time: '15:06'
  who: Adam
- line: Poke it with a stick until it works, right?
  sec: 907
  time: '15:07'
  who: Alexey
- line: Yeah. I was trying to convert things into a valid merit function. I think
    that gives you a certain number to push to – to measure against. It allows you
    to say, “Well, this thing is objectively better than that thing because of X.”
    If you even go back to basic consulting, any consultant you ever get into your
    company will always draw the grid of impact and cost as their two axes and then
    plot all your potential projects. This is a good thing to do with your potential
    data science or data projects that you might be doing. This is genuinely a worthwhile
    approach. You plot, “How hard is this thing to do?” against “How much impact is
    it going to have?” and then you just pick all the ones at the top – all the ones
    that have high impact and low cost. You do them first and you work your way through.
    If you calculate those axes and put numbers 0 to 10 on them, naturally, you can
    get a score, right? One number. Then you just rank them in order. That's a really
    good way of prioritizing the projects you're going to do. I get flack for that,
    because people argue that you can't put time bounds with data science. You can't
    put tightly defined things based on that. Maybe we can get into that and running
    teams a bit later. That's something that I think is really valuable to do.
  sec: 911
  time: '15:11'
  who: Adam
- line: Basically, a metric is a number that converts an output of some system to
    a value, right? Then it tells you how the system is doing and we can use it to
    compare multiple systems – multiple things. Then we can say, “Okay, this thing
    is objectively better than that thing, because the metrics say so.” Is that right?
  sec: 988
  time: '16:28'
  who: Alexey
- line: Units are really important. Being a physicist, units are super important.
    Even in business metrics and things like that. Because you have to make sure you
    are comparing like-for-like.
  sec: 1011
  time: '16:51'
  who: Adam
- header: Examples of metrics
- line: Can you think of some simple examples of metrics? I think you mentioned revenue?
    What are the other commonly used metrics that you saw when working at a consultancy
    company? You probably worked with many clients. Are there some metrics that most
    of the clients have?
  sec: 1021
  time: '17:01'
  who: Alexey
- line: Yes. There's all the ones you hear about, sort of “Accounting 101.” You've
    got revenue, profit, costs. You can go a little bit deeper than that. If you start
    working with sales functions and marketing teams, there's a very common language
    lots of them use, and you'll hear about “the pipeline.” In a sales team, they'll
    typically be expected to gauge projects that are going to land. That is, they
    will rate them by probabilities. They’ll say, “Right, this project will land,”
    and they'll give it a weight. Say it's a 300 grand project and it's 50% likely
    to come in. So the revenue of landing that project will be 300 grand. But what
    they will then do is multiply that by the 50% and say that that’s the ‘weighted
    revenue’. This is a really common metric. So, the weighted revenue is 150 grand
    if you trust your probability ratings, which no one ever does. That's a pretty
    hard thing to do accurately, right? If you trust your probability ratings and
    your estimations of the project size, you can then say, “Yeah, the 10 million
    pound long shot that I've got down as a 5% probability, is more valuable than
    the 300 grand that I've got a 90% probability on, because you can multiply them
    off.” You pay attention to the weighted revenue and then make your decisions and
    focus your efforts on that kind of thing.
  sec: 1042
  time: '17:22'
  who: Adam
- line: You've also got things like marketing interactions – that one is really good.
    You get qualified leads and sales. Qualified leads and market-qualified leads.
    If you've got websites or people download your content, that's a marketing interaction.
    That's a great metric to measure or maybe even turn into a KPI for your marketing
    team. You want people to download your stuff, right? It's maybe not the only thing
    you want, though. If you're just ticking that box off, you can go and get 10 to
    100,000 more interactions by doing a few TikTok videos than you can by writing
    really good content. Those TikTok videos might not, and probably won't, convert
    to any actual money. This is the point where someone that attends an hour-long
    webinar or a day-long event is far more likely to give more of their time and
    commitment over to you. So you go from market directions to leads and market-qualified
    leads.
  who: Adam
- line: Marketing organizations might have criteria and they use all these funny acronyms
    like BANTR. It was, “Did it have a budget? Do they have the authority? Is there
    a need? Is there a timeline? And is there any risk?” They will have these acronyms
    and you answer these questions to see if they tick off all the boxes. Then it
    goes from a lead to a marketing-qualified lead. Sales have another checklist and
    they'll take it a step further. This is what they call ‘the pipeline’ – as you
    go down the steps, you’re getting ever closer to actual money in the bank. You
    draw this for most organizations with a sales function.
  who: Adam
- line: These are really handy things to learn, especially as a data scientist, because
    every relation charges money. Well, the vast majority of organizations charge
    money and they sell things to people. They're the things that your company is
    going to care about. You also have costs and stuff like debt. When you get to
    professional services, you can start to come up with some pretty interesting derived
    metrics. You can go from simple stuff that you'd understand to things like “burn-down
    rate”
  who: Adam
- line: In the professional services business, I've got 100 consultants – say they
    will cost X pounds a day to hire out to people. Well, I've got a backlog of work
    that we're churning away at. At what rate do I churn through my whole backlog
    of work? That burn-down rate – if I'm churning through 50 grand worth a day because
    I've got so many people, I need to be selling at least 50 grand a day. Otherwise,
    we're going to start having redundancies for people. Thus, if your burn-down rate
    is higher than your sales rate, you've got this situation where you're going to
    run out of work for people to do and eventually bankrupt yourself or make people
    redundant. That thing is called ‘maintainability of earnings’. We're now into
    the tertiary layer, where these kinds of derived metrics will come out. They're
    interesting things and they’re bound to some organizations – it depends a bit
    on where you go. You'll have similar stuff.
  sec: 1246
  time: '20:46'
  who: Adam
- line: We did a lot of professional services. I worked at and ran a professional
    services company, so that's where I'm more comfortable, I'd say. But you get the
    same thing for manufacturing – things like Lean and Six Sigma – they look at how
    many defective products in x1000 builds and things like that. These are all good
    metrics to look at because they allow you to turn fluffy terms like “quality”
    into something you can measure. When a new person gets brought in to improve the
    quality of our product – what does that mean? “What do you mean quality? Define
    quality.” That’s always my first question. That can get really hairy. If you start
    doing big projects and investing money to improve quality without defining what
    that means, you'll get arguments down the road as to whether or not he was effective.
  who: Adam
- header: KPIs
- line: One thing you said was that some of these metrics are so good that you want
    to turn them into a KPI. So what is a KPI and how do we turn the metric into a
    KPI?
  sec: 1361
  time: '22:41'
  who: Alexey
- line: =Back to the sales example, you might say weighted revenue, the number of
    sales, and revenue might be KPIs – you pick a few. It's quite important that you
    pick a few. I actually encourage people to pick some that maybe conflict or maybe
    aren't quite necessarily all in line with one another, because it helps encourage
    good behavior. But KPIs are essentially the things that you are going to put in
    front of the CEO to say, “Thumbs up, thumbs down – is this team/function/project/whatever
    doing well? Is this a good thing? Should we put more money into it?” There are
    a lot of rules around making good KPIs. But you want them to be easy for people
    to understand and grasp quite quickly.
  sec: 1373
  time: '22:53'
  who: I always think of KPIs as sort of the metrics that you want to look at from
    a top-down point of view. So from bottom up where anyone could use metrics in
    their own work, I have my own metrics that I don't really use for anyone else
    – the way I work, things that I do that I need to check off. I’m a big fan of
    checklists, but they don't align with everyone. They don't guarantee good behavior
    across teams and people might not understand them. Whereas KPIs are things that
    organizations may have highlighted to say “This is going to drive behavior.” They're
    essentially metrics – key performance indicators – where you are measuring the
    performance of a team or an individual or a function against.
- line: Make a nice chart – make it nice and easy. I might look at a map and there
    are like seven different colors on it and it's trying to tell me things that are
    confusing, but if I see a heat map and it's just going from blue to red, then
    I know very quickly exactly what I'm looking at. Turning stuff into KPIs that
    are easy and visual, that becomes really important. Then you just use them as
    milestones or checkpoints. You frequently measure whatever it is you're looking
    to monitor against those KPIs, and you would hope that they drive performance.
  who: I always think of KPIs as sort of the metrics that you want to look at from
    a top-down point of view. So from bottom up where anyone could use metrics in
    their own work, I have my own metrics that I don't really use for anyone else
    – the way I work, things that I do that I need to check off. I’m a big fan of
    checklists, but they don't align with everyone. They don't guarantee good behavior
    across teams and people might not understand them. Whereas KPIs are things that
    organizations may have highlighted to say “This is going to drive behavior.” They're
    essentially metrics – key performance indicators – where you are measuring the
    performance of a team or an individual or a function against.
- line: The big thing for me is, you want to make sure your KPIs are aligned to the
    company strategy. Typically, we would say “Your company should have a strategy
    of what it's trying to do,” then your function or whatever needs to align to that
    strategy, but more specific to what they do. You just follow that hierarchical
    alignment all the way down to the individual. To a point where you, as an individual,
    can say “My quarterly objectives/my performance/my bonus/ my appraisals are all
    aligned to something like a metric or KPI that feeds higher-up KPIs, which feed
    all the way up to delivering part of our company strategy.”
  who: I always think of KPIs as sort of the metrics that you want to look at from
    a top-down point of view. So from bottom up where anyone could use metrics in
    their own work, I have my own metrics that I don't really use for anyone else
    – the way I work, things that I do that I need to check off. I’m a big fan of
    checklists, but they don't align with everyone. They don't guarantee good behavior
    across teams and people might not understand them. Whereas KPIs are things that
    organizations may have highlighted to say “This is going to drive behavior.” They're
    essentially metrics – key performance indicators – where you are measuring the
    performance of a team or an individual or a function against.
- line: Basically, a KPI is an important metric. This is a metric that we want to
    put maybe in a dashboard, and then maybe on a screen, and then everyone can watch
    it.
  sec: 1556
  time: '25:56'
  who: Alexey
- line: =These are something like “number of customers spoken to.” That's something
    that can be an alright sales metric, but sometimes it's a vanity thing “Well,
    I did this!” But it's putting ‘busy’ over ‘important’. There's a really good quote
    from, I think, McNamara. Unfortunately, it's about the Vietnam War, but it's a
    good quote around metrics, in my opinion. He says, “We should be careful not to
    make the measurable important, but to make the important measurable.” That's basically
    saying, “Don't get numbers that are easy to count, get the ones that we make the
    most important.” So when someone says, “My project’s 5000 lines of code,” that’s
    an easy number to get and it's not important. I think even Bill Gates said something
    like, “That's like measuring an airplane by weight.” That's not a good thing to
    measure an airplane by. Lines of code is not a good metric to measure your code
    products by. Make what’s important measurable. That's what can actually be quite
    difficult, depending on what you’re doing – especially in software.
  sec: 1567
  time: '26:07'
  who: Yeah, or on a report. Basically I think that's what a KPI should be. But they
    end up being just more numbers that you, as a data professional, have to go and
    find, collate, produce, and put in a report and no one will ever read. People
    love them, but the challenge with KPIs is exactly that people love them. They
    just want all of them, so they make KPIs that may be too specific or too niche.
    I always think – when you're defining KPIs, what behavior are you trying to drive?
    If they don't drive a behavior, cut them out. They must drive individuals or teams
    to behave a certain way. There should be consequences, both positive and negative
    for that behavior, which goes in the line with or against the KPI. That or KPIs
    should be used to make decisions. That number should go towards making a decision.
    Unless it's a vanity metric, which is a common thing you hear.
- header: KPI examples
- line: You said that a KPI should drive some behavior. In your example, you were
    working at a startup and you were trying to minimize the number of returns. So
    would the number of returns could be a good metric that drives behavior? The behavior
    is that people get the clothes that fit and they don't need to return it. Is this
    a good example?
  sec: 1684
  time: '28:04'
  who: Alexey
- line: Yeah. They get really dangerous though, don't they? This is one of the things
    about KPIs – you have to be very careful. When I was consulting, one of the things
    we encouraged people to think about was malicious actors within your company or
    within your customers or wherever. Think about people that could unlock a really
    big bonus – a 10x salary bonus. Say you started a new position and someone could
    get 10 times their salary if they hit the KPI for the year. What would they do
    if they were malicious, or they were cheaters? Think about, “Okay, so you've set
    a KPI to reduce the number of returns. Alright, then. Make it cost 100 pounds
    to return any item to this shop. We’re not gonna get any returns anymore.” Or,
    actually, I'm just not going to sell anything. I stopped selling stuff and stopped
    getting returns at the same time. It’s a stupid example, but it highlights the
    point, right? So, think about malicious actors.
  sec: 1713
  time: '28:33'
  who: Adam
- line: That is a bit of a physicist thing. Anyone presents any kind of model to you,
    and you immediately go to the extremes to try and break it and see if it still
    works. That's a really good thing to do with KPIs. It's not good enough to think
    about the spirit in which they're written. The spirit in which that has been said
    is “I want to reduce returns because that's going to save the company money.”
    But if you don't link that to sales in some way, or inversely get the sale, or
    you don’t give the same person a KPI to drive sales up, you could get into a really
    sticky spot. That's why competing KPIs are really good. If I increase sales, I'm
    going to increase my returns. So actually having both of them as KPIs – increase
    one, reduce the other. Use that on that stupid example I've just come up with.
  who: Adam
- header: Derived KPIs
- line: Okay. That's interesting. Yeah. So, we should try to make them less hackable?
    A good idea – maybe in this case, we can derive some other metric from both returns
    and sales that covers what we really want to do. We want to maximize the margin,
    right? Because when people return things, we lose money. We don't want to lose
    money, so let's do something that maximizes the margin.
  sec: 1830
  time: '30:30'
  who: Alexey
- line: =If I'm talking to a data scientist, I don't have to explain the difference
    between supervised and unsupervised machine learning. But when my mom asked me
    what I do for a living, I say “Work in IT.” You have to think about the level
    that you're communicating at. When you're communicating at that higher level,
    or maybe a bit zoomed out, or people with less time or that just aren't as close
    to it, I consider reporting both numbers. Don't just report the derived metric,
    report both of them. Yes, sales have gone up and returns have gone down. I get
    that. That's great. You've used up maybe one extra thing. It's easy when you're
    talking about that. When you get to more complicated stuff, you don't want to
    report 10 KPIs on a chart because that gets confusing. There's a balance to be
    made. You have to really think about your audience. But that's true of anything,
    I think, when data is part of the game.
  sec: 1861
  time: '31:01'
  who: Depending on whom you're working with. There are two approaches and I think
    they're both valid, depending on your situation. I mentioned maintainability of
    earnings, which is like a tertiary derived KPI. If I said that to anyone on the
    street, they wouldn’t have a clue what I'm on about. Say I'm talking to a huge
    organization about one small part of this derived metric, their executives might
    not really understand it. Think about your audience. Derived something over the
    other, like sales over returns, or something like that. That's good if the people
    I'm sharing it with, or using it with, understand what it is really easily.
- header: Creating metrics — grocery store example
- line: We already have quite a few questions, and I think I want to combine two questions
    into one. The first one is, “What is the process of coming up with the best metrics?”
    Then another question is “What KPIs are important for retailers and grocery stores?”
    I don't know if you have experience with retail stores. Maybe you do. I was thinking
    that maybe we can try to come up with some metrics that are important for grocery
    stores – for retail. And then also go through the process of coming up with these
    metrics.
  sec: 1964
  time: '32:44'
  who: Alexey
- line: Look, I still do a bit of consultancy myself on the side, actually. If anyone's
    really keen and wants to go through the workshops with me, I can come up and do
    it – just reach out. I need to know what kind of grocery store this is. What is
    the company's strategic goal? Now that is a rubbish word to use, I think. I say
    it a lot because I've been a consultant, but ‘strategic’ and ‘tactical’ and all
    that stuff really does annoy me. What I mean is, ultimately – What is this company
    trying to do? What is this organization trying to do? Because if this grocery
    store is maybe a third sector organization trying to provide healthy foods to
    a deprived area, revenue’s not going to be a metric for the KPIs I’m going to
    use. I might look at your number of new customers or the number of return customers.
    Things like “Can I reduce the average basket cost compared to the closest supermarket?”
    “Can I count the number of meals produced per family?” If that is my strategic
    objective – to bring a healthy low cost food option into a community, that's great.
  sec: 2000
  time: '33:20'
  who: Adam
- line: If I'm a company that wants to grow, then profit might not actually be my
    objective. For anyone who's worked in a start-up, ‘profit’ is this long distance
    thing no one thinks about for quite a while. Because you might have lots of investment
    to be the next Liddle and you're going to disrupt the UK supermarket space by
    coming in and putting sites down across towns. Then you’re trying to get things
    like cost leaders – products that will bring people in the store to try and capture
    people from the biggest supermarkets. In that case, ‘new customers’ is going to
    be really important – just the volume of people coming through my door. Again,
    marketing interactions and stuff like that. “How many people can I sign up for
    my club card and my loyalty scheme?” That's a really important metric to me, because
    I'm hopefully going to be able to get them back. People I can get data off of,
    like their email addresses – “Can I pester them with offers and deals?” That's
    about widening my net, drawing more people to the store. That’s not the kind of
    stuff my lovely, healthy-eating, local supermarkets are going to do.
  who: Adam
- line: How do we go about defining that? Well, I come in, usually waffle on for a
    bit like I have here, get the whiteboard out, and then start asking the people
    at the top of the organization or the top of the team or the function, depending
    on what level we're doing this in, “What's important to them? What do they think
    good looks like?” Steal other people's hard work as well, as I say some of the
    time. Who's done what you're trying to do? Well, can you find blog posts by them?
    What did they do? What are their metrics?
  who: Adam
- line: You mentioned North Star metrics to me in the lead-up to this, I think Spotify’s
    North Star metric is something like “number of minutes listened to.” That is it.
    “How many minutes of audio are people listening to on their software?” Brilliant.
    Just increase that number. That's really all they want to do, because that captures
    so much stuff. There's loads of ways of doing that. Yet, people aren't really
    obsessed with it, there’s only 24 hours a day to listen to music all the time.
    And to get people like me to share it and spread it to other people. That's all
    gonna pyramid up into that one number at the top and lots of stuff underneath
    it. So – you come in, do a bit of a workshop. You don't have to have an idiot
    like me do that – you can do that yourself. You just talk about what's really
    important. “What are we trying to achieve?” Once you've got that, think about
    “Okay, well. Actually, is profit on the table? Is profit still really important
    to us?”
  who: Adam
- line: In most cases it will be. So we'll maybe keep ‘profit’. But “Do I want my
    individual customers in the grocery store to spend more each?” “Do I want the
    people coming in for their weekly shop to also buy gift cards and expensive electrical
    items?” That's a great way to increase the average basket price. Or “Do I just
    want more people through the shop?” and things like that. Once you've got those,
    these are the important things to us, put more than you need up on the board and
    then basically rank them in order. You don't want to have like 50 KPIs – you just
    want a handful. If every individual can't remember them… again, these need to
    drive behavior. The people whose behavior they are driving, they need to be able
    to remember all of their KPIs. If I've got 15 KPIs, I'm not going to keep them
    all in my mind. If I've got five, I can probably keep track of “All right, I need
    to do these things and I can see why that's important.”
  sec: 2239
  time: '37:19'
  who: Adam
- line: They should then help smooth conversations and stuff going forward about decisions.
    Someone wants to do something and it seems a bit weird, you can go “Right. Does
    that affect KPIs?” If it's all nicely lined up, it makes the decision-making process
    easier. Then, don't be afraid to get going and to change. You have to find a balance
    of “try them out” without ‘perfection is the enemy of good’. Try them out and
    get some data. Give them a shelf life, but have a set review point. In other words,
    give them a chance, but not forever. Say 6 weeks, 12 weeks, and go “In six weeks,
    we're gonna have a look at these. Did anything change for the better? Has it helped?”
    Don't be afraid to change them. Don't be too precious about them.
  who: Adam
- line: One of the other great things you can do is look at historical data, if you've
    got it. This becomes really important. How you're collecting the data is really
    important. It's all well and good to say “I want my customers to be really satisfied.”
    But I don't have any means of contacting them. I can't send them surveys. It's
    all anonymous web transactions that even get email addresses on them. Okay, that's
    not gonna be a great KPI, because you're going to struggle to get the data. I
    actually have a sporting events company as well, and we've run events and ‘satisfaction’
    was one that we wanted. We had to run focus groups to get that as a feedback thing.
    But I have to incentivize people to attend them, because I'm taking time from
    them. That was really difficult.
  who: Adam
- line: But it was really important to me. If I put that in as a KPI for my organization
    going forward, even just doing the KPI becomes a whole industry in of itself.
    If it's difficult to do, it's going to start causing people to cut corners, and
    you want to automate that as much as possible, really. Being a data nerd, you
    should want to do that anyway.
  who: Adam
- header: Metric efficiency
- line: How do we evaluate the efficiency of a metric? I think you mentioned that
    metrics should be easy to measure. If it's difficult to measure, then people will
    try to get away from measuring it. So how do we measure effectiveness? You came
    up with a list of metrics, and then you said we need to reduce the number to just
    ‘a bunch’. How do we go from that to a smaller set of metrics? I guess we need
    to evaluate each one, and then reduce. How do you usually do this?
  sec: 2424
  time: '40:24'
  who: Alexey
- line: For the ones we've come up with, say we've then got a shortlist of five metrics
    – or five KPIs. I would then, as a warm up to the workshop, say “If it can be
    shared with me, bring in old board reports or old performance review stuff from
    the team or the organization.” Typically I do this at the company level when they
    have these management information board reports. So bring them in and then you
    can look at historically, “Okay, can we create these metrics?” And then I would
    maybe go away with that data and create a few slides saying “This is what I roughly
    think these metrics might have been if we had the data.” Then, have an open discussion,
    “Would we have made a different decision having seen this trend line of this metric?”
    That's the other thing – obviously, collecting the data is important, we all know
    that. But you also have to report on it. You have to make it super visible. Lots
    of people, or companies, have this weird thing about having KPIs and then never
    sharing them with the staff. They make sure the executive team knows them and
    no one else. Why? Make them obvious.
  sec: 2467
  time: '41:07'
  who: Adam
- line: Make Power BI / Tableau dashboards and mount them in your SharePoint or your
    Slack – put them in places that people can check them really quickly. “What are
    the current marketing interactions?” and stuff like that. This way everyone's
    informed and involved. Actually, in a few places I’ve worked, they've done this
    and I tell customers to try this – During your ‘All Hands,’ if you do a weekly
    or a monthly one, have the executives explain the KPIs regularly. What they mean,
    what the executives think of them. It brings everyone on that journey.
  who: Adam
- line: Then ‘effectiveness’ – this can be a tricky one. I've done a lot of work with
    charities back at Incremental Group. One of the things they really struggle with
    is what they call ‘outcomes’ – “How do we measure our outcomes?” For a childcare
    charity, I interacted with children with difficult pasts and tried to keep them
    on a path to education and good health and all that. Have them stay out of trouble.
    How do you measure the outcome over the course of that person's life? There's
    no control group. That becomes a really difficult thing. You have to agree upfront,
    “Right, we're going to set these as targets.” KPIs should trend towards something.
    It's not good to have KPIs that sit stagnant – you want them to go one of two
    ways. Effectiveness then is looking in one of the regular reviews, going back
    and saying, “Are we using this? Is this a useful number to us? Does anyone actually
    care? Have we made decisions based on this number? Or do we always just say ‘Yeah,
    but actually, we'll ignore that because of this.’” And if that's the case, bin
    them. Don't keep them because you thought they were a good idea. Iterate on them,
    improve. Agile, right? Make better ones.
  who: Adam
- line: Try and find something that works for you. That's why I say ‘steal other people's
    hard work.’ Look at what other people have done, but make it yours. Take it and
    try and tweak them to fit your situation because it'll be different. This isn't
    easy stuff, alright? This is why companies like KPMG get paid millions to do this
    kind of stuff. Because it's not straightforward – it's a difficult process. The
    advantage of consultancies – and I'm not a consultant anymore, so I can extol
    their virtues without sounding like a salesman – the advantage of consultancies
    is that they’ve done this more than once. A lot of consultancies will have done
    this multiple times and have frameworks and processes to help you with this as
    a grocery store. Maybe you've never done this. Maybe this is your first time thinking,
    “How do I measure my business? This sounds like a thing I want to do.” Become
    a bit more forward thinking. Do it from scratch, be advised by using people's
    experience and go from there.
  who: Adam
- header: North Star metrics
- line: Thank you. You mentioned the North Star metric. In the case of Spotify, this
    is the number of minutes listened. In the case of YouTube is ‘how many minutes
    of video have people watched. So, the North Star metric is what exactly? Is it
    just a single number that’s the most important KPI for the company?
  sec: 2699
  time: '44:59'
  who: Alexey
- line: Yeah. Often you’ll find, like the Spotify one, you can capture lots of different
    things rolled into something super simple. That's the best metric and the best
    KPI – ones that are really simple. Simple to the point where you can tell anyone
    on the street in a couple of minutes what your company does and what the metric
    means, and they'll understand. That's the number you want to go up or down and
    that's pretty much it. It’s trying to find something that that does that for your
    organization. Like the North Star, you use it to guide your decision-making and
    your other metrics should align to it. It should capture, in essence, what you're
    trying to do. Some of them – like for these big companies, they're very good at
    this – some of them are marketing tools a little bit as well. The metric itself
    is a bit of a marketing tool in the sense that “That is our mission statement.
    This is what we're doing. Here's how good we are.” It becomes easy for me to look
    at that and go “That's a big number. Oh, it’s gone up.” or “It's doubled in three
    years, blah, blah, blah.”
  sec: 2721
  time: '45:21'
  who: Adam
- header: Threshold metrics
- line: You also mentioned at the very beginning, when we were talking about lasers,
    you said there’s a thing called “threshold metric”. What is a threshold metric?
  sec: 2794
  time: '46:34'
  who: Alexey
- line: =They can also be more vague – I've named a lot of very binary examples there.
    I'm trying to think of some that aren't binary. You might even have things like
    customer churn rate – the number of users you lose every month. You might not
    actually care too much. If your plan is to acquire loads of users, then churn
    rate might not be super important to you in the short term, but it will be in
    the long term. But in the early stages, it’s just “acquire, acquire.” So instead
    of saying “We'll just ignore churn,” you might say, “We need to keep churn above
    or below 5%,” or something like that. “If it ever crosses 5%, we do a review.”
    Then we start to think “Do we now need to introduce something else to drive behavior?
    Do we need to change the way we operate? Do we need to change the way we work?”
  sec: 2805
  time: '46:45'
  who: For me, threshold metrics – as I've seen for most KPIs, you want them to be
    above or below a certain point. That is, you always want them to go either up
    or down. This shows improvement in growth. But there are some that just need to
    be at a certain level. If I'm running an airline – passenger deaths – I want this
    metric to be zero and I want it to stay at zero, right? That's it. If it goes
    up – as soon as I cross that threshold, I have to do something about it. That's
    an extreme example, but probably a good one. These will be like health check factors
    within your organization. Things that, if you cross the threshold, there's a significant
    issue that needs addressed. For a SaaS company, this might be a data leak. You
    might have data breaches.
- line: Until it hits that 5% warning light, we'll kind of be happy with that. You
    measure it, you do all the reporting on it, and then if it's a thumbs up, it's
    a thumbs up. You carry on. That's how I see threshold metrics. You're not going
    to actively drive a threshold metric – you just want to make sure it stays up
    on the right side of the threshold.
  who: For me, threshold metrics – as I've seen for most KPIs, you want them to be
    above or below a certain point. That is, you always want them to go either up
    or down. This shows improvement in growth. But there are some that just need to
    be at a certain level. If I'm running an airline – passenger deaths – I want this
    metric to be zero and I want it to stay at zero, right? That's it. If it goes
    up – as soon as I cross that threshold, I have to do something about it. That's
    an extreme example, but probably a good one. These will be like health check factors
    within your organization. Things that, if you cross the threshold, there's a significant
    issue that needs addressed. For a SaaS company, this might be a data leak. You
    might have data breaches.
- header: Health metrics
- line: Is it a similar concept to the “health metric”?
  sec: 2928
  time: '48:48'
  who: Alexey
- line: Yeah, or like “hygiene factors'' as they get called sometimes. Those are things
    like, “This must exist. If it doesn't exist, the game’s off. This has to happen
    no matter what.” These could be regulatory things. These could be health and safety.
    These are quite common in these kinds of fields.
  sec: 2932
  time: '48:52'
  who: Adam
- line: So, what is a health metric?
  sec: 2950
  time: '49:10'
  who: Alexey
- line: It's just things like downtimes – that’s a really common one for SaaS businesses
    – the downtime over a number of days, months, years or whatever. Or the percentage
    of servers that are up and stuff like that. If that is trending the wrong way,
    you know you've got an issue in the health of your service. It's asymptotic almost,
    in that it is either good or it's something's going wrong. You don't want 200%.
    It's not a thing that’s gonna drive your business. As long as it's sorted, you
    can kind of ignore it.
  sec: 2952
  time: '49:12'
  who: Adam
- line: So it's like a threshold. You don't want a high number of downtimes, for example.
  sec: 2998
  time: '49:58'
  who: Alexey
- line: Yeah. But with a health metric, there's some leniency. Whereas with the threshold,
    you would say hardline – there's a problem.  With health metrics, you might say,
    “Okay, there's gonna be some downtime because we can't control everything.”
  sec: 3002
  time: '50:02'
  who: Adam
- line: Yeah. Are there any other kinds of metrics that are important to know? We
    talked about KPIs. We talked about the North Star metric. We talked about threshold
    and health metrics. Are there any other types of metrics that are important?
  sec: 3017
  time: '50:17'
  who: Alexey
- line: Yeah, there are probably very industry-specific ones and things like that.
    I'm trying to get very general cases, or the actual theory behind them. This is
    the kind of thing that a really good BI consultant would be able to help you with
    and say, “This is how I would turn this in. This is what I've seen before.” Then
    we would start using other people's experience. As for kinds of metrics, I'm not
    sure. I draw very much on the specifics of what's important to the particular
    business.
  sec: 3032
  time: '50:32'
  who: Adam
- header: Data team metrics
- line: We also wanted to talk a bit about metrics that are specific to machine learning
    and data science. Let's say we have a data science team. What should the data
    science team care about? We can take the grocery shop example. Let's say the grocery
    shop went through a digitalization process. We have a data science team in the
    grocery chain. What are some important things for the data scientists to know
    for their work?
  sec: 3072
  time: '51:12'
  who: Alexey
- line: =Try and convert everything you do – model, accuracy, and all that – try and
    convert it back to money or seconds. And leave it at that. Ultimately, if the
    CEO of the grocery store group comes along, he's probably got a background in
    selling groceries or running businesses. He doesn’t have a background in machine
    learning and data. So if you tell him, “I've improved my random forest accuracy
    by 6% by doing this, that and that,” that doesn't mean anything to these people.
    But if you say, “I've improved the model and it leads to 10,000 pounds a month
    improvement across our whole revenue.” Okay, I can see the return on investment.
    This is something that I did very early on. Then once you're in that mind space,
    it helps you as a data scientist individually as well, to not waste time on stuff
    like polish and gold plating.
  sec: 3108
  time: '51:48'
  who: Yeah, this is good, actually. What you'll find is – if you leave it to the
    data scientists, they'll come up with a load of metrics that are very technically
    focused, and they will be around model performance. It'll be around accuracy and
    things like that. These metrics are important – they are important. But I often
    joke that no one cares – no one outside of the data team will care about them.
    In a data team, in a wider organization, it’s different if technology or data
    is the core of what your company does. That's a slightly different thing. But
    in the grocery store example, or when I was in insurance, it was a nice to have
    or an add-on or added value.
- line: That's something else a lot of data scientists are really guilty of, “Keep
    tweaking the model!” It’s fun, right? It's interesting. That's right, we love
    it. But sometimes, the 80/20 is good enough. You just get the bulk of it done.
    Get to a point where you've paid off the bulk of the work and you know that it's
    going to take the same amount of time to do other ‘diminishing returns’ type stuff.
    Think in pounds and seconds – save them. The reason I like pounds is because everyone
    understands that – it’s the universal language of business. The higher ups will
    understand it. Seconds is a good one as well, because you can talk about ‘time
    saved’ and things like that. That's easy for people to get.
  who: Yeah, this is good, actually. What you'll find is – if you leave it to the
    data scientists, they'll come up with a load of metrics that are very technically
    focused, and they will be around model performance. It'll be around accuracy and
    things like that. These metrics are important – they are important. But I often
    joke that no one cares – no one outside of the data team will care about them.
    In a data team, in a wider organization, it’s different if technology or data
    is the core of what your company does. That's a slightly different thing. But
    in the grocery store example, or when I was in insurance, it was a nice to have
    or an add-on or added value.
- line: You don’t have to explain to the people in the sales department what you mean
    by “Your F1 score” and stuff like that. Or your ROC/AUC, right? These are all
    numbers that we love, because we get them. If you're talking to me, please tell
    me your ROC/AUC and your F1 scores – I like all that. But if I'm then going to
    help you try and sell your next project to the function lead, let's do it in pounds
    or seconds. They're the numbers that are on slides. Always think “I'm going to
    present my argument in four or five slides. Then my boss (or whoever I'm presenting
    it to) is going to copy exactly those slides and present them off on the chain.”
    If you think about that – is your boss's boss going to be able to explain your
    F1 score to their boss? If the answer's ‘no’, let's go back to pounds, seconds,
    or whatever. Again, in some organizations everyone's actually super technically
    literate. It might be that you’re the star and everyone's a data scientist, in
    which case, throw it out the window, go nuts. You'll find your own way there,
    but it is a useful approach for other cases. A rule of thumb.
  who: Yeah, this is good, actually. What you'll find is – if you leave it to the
    data scientists, they'll come up with a load of metrics that are very technically
    focused, and they will be around model performance. It'll be around accuracy and
    things like that. These metrics are important – they are important. But I often
    joke that no one cares – no one outside of the data team will care about them.
    In a data team, in a wider organization, it’s different if technology or data
    is the core of what your company does. That's a slightly different thing. But
    in the grocery store example, or when I was in insurance, it was a nice to have
    or an add-on or added value.
- header: 'Experiments: treatment and control groups'
- line: You also mentioned measuring and control groups, so I guess this is something
    that’s also important. Once you have a model, you want to measure it. How do we
    usually go about this? Maybe you can just go a bit into the details of how we
    can do this?
  sec: 3342
  time: '55:42'
  who: Alexey
- line: So do a sort of “implement a model how-to”?
  sec: 3362
  time: '56:02'
  who: Adam
- line: Yeah. We have a metric. We have a model. If we say “AUC is 80%,” nobody will
    care, right? We need to come to the business people and say, “Hey, my model generated
    that percent of uplift in minutes. Now my new recommendation system at Spotify
    causes 10% more minutes to be listened.” So how do we actually measure that?
  sec: 3367
  time: '56:07'
  who: Alexey
- line: =What we did in insurance companies, and what lots of SaaS companies do is
    – market teams are used to this – A/B testing or ‘champion challenger modeling’,
    we called it. For a very small percentage of our customers, if you've got high
    enough customer numbers, a very small percentage would randomly get selected as
    the ‘challenger group’. They would be served a different model to the one that's
    in deployment. Maybe there's no model in deployment at the moment, that’s fine.
    95% of the customers that come through, they go through that normal procedure,
    but 5% get siphoned off. And it has to be random. Be very careful about how you
    randomize things. Because using things like birthdays and stuff like that, sometimes
    causes issues that turn out that it’s not quite random. So, 5% of them get through
    the new model. Then, once you've built up enough data, you can compare like-to-like.
    Because they were the same timeframe, they're the same thing. If the challenger
    model beats the champion – the one that's currently running – you then promote
    it to the main model. Then change something else. Don't change too many things
    at once. Change one thing at a time, and you'll be able to slowly but surely see
    impact, over 2-, 3-, 5-week period depending on your sales volume, your customer
    volume. That's a really good way of seeing, if you're in a live environment, how
    to measure your impact and things like that.
  sec: 3395
  time: '56:35'
  who: It's really hard actually. That is really, really difficult. If you're lucky
    enough to live in a world where you've got a good simulator and the cost of simulation
    is low – then simulate it. Reinforcement learning is great, but that's a rare
    case. If you've got good historical data, whereby your actions don't make much
    of an impact on the state of the world, i.e. the stock market, you can play against
    the historical data. That's really good, like back-testing and looking at the
    way that it affects that. That's a really good approach. Again – really difficult.
- line: I realized that I dodged the question “What kind of KPI should software data
    science teams care about?” I talked a lot about communicating your output to other
    people. But internally, there's quite a lot you can do as well. You can look at
    that outcome value and look at the impact made. One KPI I love for data teams
    is “number of reusable BI tools/applications/bits of software/pipelines” that
    are being used and reused. If I build a function to help me get data from somewhere
    and manage it a certain way, if that gets turned into your utility, you can use
    it as your next project in the same team. That's a really good KPI to look at.
  who: It's really hard actually. That is really, really difficult. If you're lucky
    enough to live in a world where you've got a good simulator and the cost of simulation
    is low – then simulate it. Reinforcement learning is great, but that's a rare
    case. If you've got good historical data, whereby your actions don't make much
    of an impact on the state of the world, i.e. the stock market, you can play against
    the historical data. That's really good, like back-testing and looking at the
    way that it affects that. That's a really good approach. Again – really difficult.
- line: There's a really good post, by Domino Data Lab. I'll try and find it to share.
    They talk a little bit about this. I think they’re old now, but they talk about
    some of these ones – they're really good. Also still a bit hard work for what
    software teams use. They're not always going to work, but things like ‘models
    deployed’ that can be quite good. How much stuff is in production? Are you putting
    things in production? How many service users, internally, are using your models?
    It's all well and good to have a super cool neural network, but nobody uses it.
    Don't waste time, right? Sorry, we lost that question a little bit.
  who: It's really hard actually. That is really, really difficult. If you're lucky
    enough to live in a world where you've got a good simulator and the cost of simulation
    is low – then simulate it. Reinforcement learning is great, but that's a rare
    case. If you've got good historical data, whereby your actions don't make much
    of an impact on the state of the world, i.e. the stock market, you can play against
    the historical data. That's really good, like back-testing and looking at the
    way that it affects that. That's a really good approach. Again – really difficult.
- header: Accelerate metrics and timeboxing
- line: We already talked about measuring the effectiveness of teams by how many users
    of the service there are, and how many parts of the pipeline are used. The question
    is, “As a manager, do you find accelerate metrics, like ‘lead time’ ‘deployment
    frequency’ useful for measuring your team's performance?
  sec: 3602
  time: '1:00:02'
  who: Alexey
- line: 'Depends on the team… I do. Yes, but it depends on the team. I''ve run fairly
    big teams of data professionals – by the 10s – and I found that a lot of them
    really resist being managed. I don''t know why. But it seems to be a thing: in
    data, we don''t like to be managed. I don''t know if it comes out of academia.
    I was like this as well when I started. You kind of want freedom to explore and
    solve problems and do stuff. That just doesn''t work. It doesn''t really work
    for many organizations. Sometimes it does, but most of the time, it doesn''t.
    One of the things I learned from Elizabeth Halljoy, who is head of insight for
    Greco – she''s done really good things and they''ve got a great data team there.
    She did a talk a while ago about how they do everything. I''ve kind of changed
    it a bit, so if I misquote now, please forgive me.'
  sec: 3626
  time: '1:00:26'
  who: Adam
- line: Essentially it’s “Timebox everything into two weeks.” I do this with my teams
    and it's great. If I say to you, “How long is it going to take you to build me
    a reinforcement learner for that thing?” You would say “What? I don't know. Infinite?
    If you want a rubbish answer – 30 seconds. If you want a really good answer –
    six years. I don't know.” Instead of that – which is where we all get stuck and
    say we want the freedom to explore and we don't for how long – you just say “You've
    got two weeks. Build me something that's better than what's currently in play.”
    That becomes a really good way to discretize what you're doing and turn it into
    something you can measure. Then when you're in that mind frame, it lines up much
    more cleanly with the traditional agile stuff. You're not going to get user stories
    and things like that. It's more like running spikes all the time. But it will
    allow you to integrate your data teams more readily with those kinds of agile
    management practices and things like that. I find that works really, really well.
  who: Adam
- line: Then everyone can trust it. Your product manager, for example, can know that
    if they want an improvement on the sales model, then the cost is two weeks. But
    there's no guaranteed outcome from those two weeks. You set the guaranteed outcome
    as a report on what was tried and how it performed. There's no guaranteed improvement.
    But your product owner, who's running the team and is responsible for deadlines,
    knows that it's their budget. They say “Right, two weeks on that, two weeks on
    that,” and then they can reprioritize on other things. That's quite a good way
    of doing it. But it really depends on the team. If you're in a team of software
    engineers that have learned data then it’s really, really good. If you're in a
    team with lots of data professionals that hate software engineering, then…
  who: Adam
- header: Conclusion
- line: Anything else you want to add before we wrap up?
  sec: 3795
  time: '1:03:15'
  who: Alexey
- line: It's been great talking to you. Sorry for rambling all over the place. I find
    this stuff really exciting and interesting. If anyone does want to talk about
    it in more detail, please reach out. If you caught the restart, I've just had
    my first child, so I'm useless. It came back to me in the last couple of weeks.
    But I'll hopefully catch up. Yeah, catch me on LinkedIn, Twitter, or wherever.
    I'd love to hear what other people are doing with KPIs. I'd love to hear anyone
    that thinks I'm speaking rubbish. If anyone really disagrees with what I've said,
    I'd love to hear it, because that's the only way I think we learn, is when we
    get challenged on stuff. So please, if you think I'm speaking rubbish – they're
    the best conversations for me to have, so I'd love to hear it.
  sec: 3800
  time: '1:03:20'
  who: Adam
- line: Okay. Thanks a lot. Thanks for joining us and finding time to actually talk
    to us. I know it's not easy for you. So thanks a lot. And thanks to everyone for
    being active, for asking questions. Sorry that we didn't cover everything. But
    I hope it was useful for you. Have a great weekend, everyone.
  sec: 3840
  time: '1:04:00'
  who: Alexey
description: Discover KPI design, metrics strategy & ROI proof - avoid vanity metrics,
  build dashboards, prioritize impact, and measure experiments to prove value.
---


Links:

* [Domino's article about measuring value](http://blog.dominodatalab.com/measuring-data-science-business-value){:target="_blank"}
* [Adam's article about skills useful for data scientists](https://towardsdatascience.com/how-to-apply-your-hard-earned-data-science-skillset-812585e3cc06){:target="_blank"}
* [Adam's article about standing out](https://towardsdatascience.com/how-to-stand-out-as-a-great-data-scientist-in-2021-3b7a732114a9){:target="_blank"}
