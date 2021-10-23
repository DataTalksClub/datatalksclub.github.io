---
title: "Conquering the Last Mile in Data"
short: "Conquering the Last Mile in Data"
guests: [caitlinmoorman]

image: images/podcast/s05e08-the-last-mile-in-data.jpg

season: 5
episode: 8

ids:
  youtube: HfMpG2zpa2I
  anchor: Conquering-the-Last-Mile-in-Data---Caitlin-Moorman-e1958c1

links:
  youtube: https://www.youtube.com/watch?v=HfMpG2zpa2I
  anchor: https://anchor.fm/datatalksclub/episodes/Conquering-the-Last-Mile-in-Data---Caitlin-Moorman-e1958c1
  spotify: https://open.spotify.com/episode/6SGjBev8koFDRpDvLV76ZQ
  apple: https://podcasts.apple.com/us/podcast/conquering-the-last-mile-in-data-caitlin-moorman/id1541710331?i=1000539421886

transcript:
- line: "This week, we'll talk about the \u201Clast mile of data\u201D and we have\
    \ a special guest today, Caitlin. Caitlin is the VP of data and business operations\
    \ at Trove Recommerce, where she helps brands buy back and resell their products\
    \ at scale. Previously, she led data teams in crowdfunding and in self-publishing\
    \ companies. She's also an admin and a co-founder of an amazing Slack community\
    \ called \u2018Locally Optimistic\u2019. Actually, there is a funny story. When\
    \ I just started DataTalks.Club, one of the first members, Arpit \u2014 he also\
    \ was a guest on this podcast \u2014 asked me \u201CHey, why did you create this\
    \ community, if there is already Locally Optimistic?\u201D I replied \u201CLocally\
    \ what?\u201D Then he invited me to Locally Optimistic, and I found out about\
    \ this Slack community. So, if you're into analytics and data things in general,\
    \ do check it out. But who knows what would have happened if I knew about Locally\
    \ Optimistic? Maybe we wouldn't be talking now."
  sec: 187
  time: '3:07'
  who: Alexey
- line: Yeah, but I think the fact that there are multiple organic emergences of these
    communities really just speaks to how much data practitioners really need that
    community. We're still figuring out so much. I find the community to be so helpful.
  sec: 253
  time: '4:13'
  who: Caitlin
- line: Welcome.
  sec: 276
  time: '4:36'
  who: Alexey
- line: Thank you!
  sec: 278
  time: '4:38'
  who: Caitlin
- header: "Caitlin\u2019s background"
- line: "Before we go into our main topic of \u2018conquering the last mile of data\u2019\
    \ and what it actually means, let's start with your background. Can you tell us\
    \ in a few words about your career journey so far?"
  sec: 280
  time: '4:40'
  who: Alexey
- line: "Yeah. I started my career working for a small, very involved private equity\
    \ firm, which was a really good six-year mash-up of financial modeling skills,\
    \ like investment banking plus bouncing from project to project, the way you might\
    \ in consulting. I did everything from evaluating investments, designing incentive\
    \ compensation plans, serving as a temporary General Manager for one of our companies.\
    \ I spent a lot of time in that role making decisions based on data, but I actually\
    \ didn\u2019t even know where it came from. I would just email someone, describe\
    \ what I need, and then get a CSV back. So, it was very blackbox. I was instead\
    \ really focused on how to use that data to make decisions and really spend a\
    \ lot of my time analyzing it, framing trends, really understanding \u201Cwhere\
    \ we should go from here\u201D and also the typical spending hours creating the\
    \ \u2018perfect chart in PowerPoint\u2019. Ultimately, for a lot of different\
    \ reasons, I decided to leave private equity and settle into a single company."
  sec: 292
  time: '4:52'
  who: Caitlin
- line: "To be honest, I wasn't super thoughtful about it, but I was really lucky\
    \ and I ended up in an analyst role at a self-publishing company. As a data team\
    \ of two, I thought the role was going to be more like FPNA \u2013 in my wheelhouse\
    \ of using data but not creating it. Very quickly, it became a lot more technical.\
    \ I went from very nervously changing \u2018where\u2019 clauses to trying to writing\
    \ PHP for home-coded daily sales emails \u2013 it escalated quickly. That was\
    \ a really amazing experience. It was around the same time Redshift was emerging.\
    \ We were by no means on the cutting edge. Everything was kind of home-baked and\
    \ we didn't have any of the user-friendly tools that we have today. From there,\
    \ I moved to the Bay Area, started working for a company that was in the middle\
    \ of the transition to a much more modern data stack. That began my love affair\
    \ with modern data tooling, enabling teams."
  who: Caitlin
- line: "I ended up leading a team at that barrier startup, ultimately leaving to\
    \ build out a team from scratch, which has been a really fun experience. I still\
    \ really love the technical side. It makes me really happy to just disappear for\
    \ a few days and go write some code. But especially as my role has grown, I am\
    \ keenly aware of that moment where data actually changes decisions and I'm super\
    \ focused on figuring out how we can get more effective at creating those moments\
    \ \u2013 making sure the data is there, making sure that the right people are\
    \ in the room, and to some extent, actually thinking about whether the right answer\
    \ is that one very well crafted PowerPoint slide. Sometimes it is. Those challenges\
    \ are something I am spending a ton of my time thinking about lately."
  who: Caitlin
- line: Do you still have to use PHP?
  sec: 474
  time: '7:54'
  who: Alexey
- line: "No\u2026 no. I don't know whether I ever was actually successful when I did\
    \ need to use it. But I spent a lot of my time beating my head against it."
  sec: 477
  time: '7:57'
  who: Caitlin
- line: You were saying that you're still doing a bit of hands-on work? Sometimes
    a bit of coding, right?
  sec: 489
  time: '8:09'
  who: Alexey
- line: Yeah, much less so very recently, but I do still like to get in there and
    dig around. I wish that I had more time for it now, but that's the reality of
    more strategic roles. Someday, I think that cycle of my career is likely going
    to be continuously going from creating a team from scratch to growing it, and
    then realizing that I'm too far away from it and coming back. I haven't reached
    that point yet. But someday, I'm going to boomerang back.
  sec: 497
  time: '8:17'
  who: Caitlin
- header: The last mile in data
- line: "You said that you're really interested in seeing and understanding how data\
    \ can be used to change decisions. This is what you're focusing on right now.\
    \ The topic today is \u2018conquering the last mile\u2019 and I think these two\
    \ things are related. So I wanted to ask you \u2013 it\u2019s maybe a bit of a\
    \ story \u2013 when I reached out to you and invited you to this podcast to have\
    \ an interview, you wrote to me that you've been thinking a lot about the last\
    \ mile in data. I thought, \u201COK, so what is the last mile?\u201D and then\
    \ I started to look it up. I googled it, and then I checked. So what I want to\
    \ ask you, what is the last mile and where does this analogy come from? Why do\
    \ we use this when we talk about data?"
  sec: 528
  time: '8:48'
  who: Alexey
- line: "The \u2018last mile\u2019 is a term that is colloquially used to refer to\
    \ the last stage of a process, whatever that is. It originally comes from delivering\
    \ physical goods or services to their final customers. Getting a physical product\
    \ into a store or a warehouse is a scale problem. So it's relatively straightforward\
    \ to design and implement solutions for problems where you're dealing with a lot\
    \ of things moving all at once. But then getting that product from the warehouse\
    \ into your house \u2013 getting that pint of ice cream from the grocery store\
    \ to me in under an hour when I order from Instacart. That is the last mile. That's\
    \ where there's a massive amount of complexity, when you think about it operationally."
  sec: 583
  time: '9:43'
  who: Caitlin
- line: "In these classic \u2018last mile\u2019 challenges, often half or more of\
    \ the cost of getting a product to you is really that last mile. It's something\
    \ where if you solve the big problems, it feels like you're most of the way there,\
    \ but really, there's still a lot ahead of you. But if you don't solve that last\
    \ mile, you never get the value out of the thing that you're building. I started\
    \ in data long enough ago that everything before the last mile used to be really\
    \ hard. It was really challenging to actually implement tools. It was really challenging\
    \ to make changes to ETL. All of this was really difficult. When you\u2018re in\
    \ smaller companies, you might not ever actually implement a lot of this stuff.\
    \ I was basically writing queries against a copy of the production database. There\
    \ was no data warehouse \u2013 there were no transformations \u2013 so it was\
    \ writing raw SQL queries every time. That was kind of the way that you would\
    \ operate."
  who: Caitlin
- line: "If you think about this as \u2018the last mile\u2019 analogy, the era of\
    \ that kind of data work was really like when you had to build the railroads.\
    \ It used to be really hard to get from the center of one city to the center of\
    \ another city. You build some railroads and suddenly, that becomes much easier.\
    \ As our tooling has gotten easier in data, it has become much simpler to just\
    \ set up a pipeline that gets all your data into one place. You clean it up maybe\
    \ with DBT, or whatever transformation tool you use. You've got a beautiful warehouse\
    \ that is pretty easy to use. That really opened up the world of like, \u201C\
    What can a data team do?\u201D And it made the challenges seem much more surmountable.\
    \ We have this general theme in a lot of analytics communities that if you can\
    \ empower a great analyst, if you solve value delivery \u2013 you can get delivery\
    \ to it. Yes, it has changed \u2013 the amount that one smart person can accomplish\
    \ is crazy compared to what it used to be."
  who: Caitlin
- line: "Because of the Modern data stack, like Redshift and other things that we\
    \ couldn't do before. You mentioned that a few years back, you didn't have this,\
    \ so you had to do a lot of things without using these tools \u2013 just trying\
    \ things out. Now, you're saying it\u2019s like the railroads. These modern data\
    \ stacks are the railroads. Right?"
  sec: 780
  time: '13:00'
  who: Alexey
- line: "Or like the interstate highways, whatever the primary form of industrial\
    \ transportation is in your particular locality. I'm in the US, it's all interstates\
    \ here. But in many places, it is railroads that are much more efficient and less\
    \ environmentally damaging. We'll say that it's a really great rail system \u2013\
    \ something that gets stuff to the warehouse, gets it to the middle of the city.\
    \ But you still see that in every organization, people are really frustrated that\
    \ data isn't available, or that the data team\u2019s work doesn't feel like it's\
    \ impacting the business, and analysts are feeling like they're doing all this\
    \ work that doesn't seem to be valued. That's where we're seeing the pain of the\
    \ last mile. So we're getting the data most of the way there, but we're still\
    \ not really delivering."
  sec: 804
  time: '13:24'
  who: Caitlin
- line: "When you think about data problems, you can kind of separate out these scale\
    \ problems. \u201CHow do you get it in the warehouse? How do you transform it?\
    \ How do you get to the most basic dashboard and get clearly defined metrics to\
    \ a user?\u201D Then there's the last mile of that, which is \u201CHow do you\
    \ actually get a team to change what they're doing based on the data and enable\
    \ them to make better decisions based on the data?\u201D Much like the last mile\
    \ of delivery is all about how many different houses there are and navigating\
    \ very different terrain because this one is uphill and this one is deep in the\
    \ woods \u2013 it's very similar because you just have so many different stakeholders\
    \ and so many different ways of making decisions. The effort to understand that\
    \ landscape and actually get plugged into it is really substantial. But if you\
    \ aren't getting the data to the decision, then your team just isn't having the\
    \ impact that you want them to have."
  who: Caitlin
- line: "This \u2018last mile\u2019, does it have anything to do with marathons? Because\
    \ this is what I found \u2013 when I was Googling a few minutes ago. I was looking\
    \ it up and trying to understand what \u2018the last mile\u2019 actually is, and\
    \ I found an analogy with marathons. The last mile, when you run a marathon, is\
    \ the most difficult one. You're tired, but it's already pretty close to the end.\
    \ You really have to force yourself to actually run this last mile. Have you heard\
    \ anything like that?"
  sec: 920
  time: '15:20'
  who: Alexey
- line: "I've never thought of that as the source of this analogy. But I think it\
    \ has a lot of parallels. You get to the point where you're like, \u201COh, well,\
    \ I've done most of the work. I ran 25 miles. That\u2019s pretty close, right?\u201D\
    \ Getting things across the line and actually finishing them can be really challenging.\
    \ It can feel much easier to start on the first mile of the next problem than\
    \ it is to tie everything up with a neat little bow and make sure that people\
    \ understand how to use your products. Getting to the point that people are really\
    \ understanding the data and that they understand how to actually bring these\
    \ two things together at the time of decision \u2013 to learn from the data that\
    \ you've provided."
  sec: 956
  time: '15:56'
  who: Caitlin
- header: The Pareto Principle
- line: "Yeah, there's also the \u2018Pareto principle,\u2019 also known as the \u2018\
    80-20 Principle\u2019, where from 20% of the work, you get 80% of the results.\
    \ Or the other way around \u2013 the remaining 20% takes 80% of the effort. Would\
    \ you say the last mile is this remaining 20%?"
  sec: 1005
  time: '16:45'
  who: Alexey
- line: "I think that potentially, it's similar. But I think it's really challenging\
    \ to get value out of data at all, especially if you don't really understand how\
    \ to connect it to decisions. That might look really different in a lot of organizations.\
    \ There are a lot of organizations where users are really savvy and they understand\
    \ the data \u2013 really all they need is access to it. Then you create a really\
    \ solid data set or a really useful dashboard, and the people are good and they're\
    \ going to use the data. They're going to get it into the meetings. They're going\
    \ to make decisions based on it. That is really kind of all you need to do. But\
    \ then there are organizations where, for whatever reason, there are incentives\
    \ to not look at the data, or just a lack of comfort with it, or a lack of fully\
    \ understanding it \u2013 there are lots of reasons for why people don't take\
    \ that last leap. There, it's not really helpful at all to put the data out there\
    \ if people aren't going to use it."
  sec: 1027
  time: '17:07'
  who: Caitlin
- line: "I tend to think of 80-20 as more figuring out how to tackle particular problems.\
    \ For example, if what you're trying to do is optimize marketing spend, you're\
    \ gonna get 80% of the value out of 20% of the effort in the sense that you can\
    \ answer all kinds of questions \u2013 you can dig really, really, really, really\
    \ deeply. What you need to do is find those high leverage questions, where once\
    \ you answer them, you get the value. But even within that, you still have to\
    \ make sure that the stakeholders \u2013 the operators who are really taking action\
    \ \u2013 fully understand how to use it and that you understand how their decision-making\
    \ process works. You need to enable the data to be in the room at the right time,\
    \ whether that's by a data person being in the room, or making sure that the team\
    \ really understands the tools they have. Or\u2026 there are lots of different\
    \ ways that this might take shape. But ultimately, if you're not at that point\
    \ of decision, or not really well plugged in to how operators are using the data,\
    \ then you can't even get that first 80% of the value."
  who: Caitlin
- line: "Okay. So this is binary. You do all the work, and then there is the last\
    \ mile. Similar to a marathon, if you don't run the last mile, you haven't finished\
    \ the marathon. So you need to make sure that people \u2013 the decision-makers\
    \ \u2013 use your dashboards to make decisions or use your machine learning models\
    \ to affect the customer, or whatever data product you have. You need to make\
    \ sure that decisions are made based on this or else all the effort is in vain.\
    \ Is that right?"
  sec: 1169
  time: '19:29'
  who: Alexey
- line: Yeah.
  sec: 1200
  time: '20:00'
  who: Caitlin
- header: Failing to use data
- line: "When I was preparing for this, I read a few articles. What we are talking\
    \ about here is more like \u201CWe have some data, but we're failing to use it.\
    \ This is the last mile problem that we need to solve.\u201D So, \u201CWe did\
    \ all this work, how can we now use this?\u201D The article said that fundamentally,\
    \ failing to use data isn't a technological problem, but a social problem. I think\
    \ you mentioned something like that \u2013 right now we have all these modern\
    \ data spec tools that make it easier for us. We have these railroads that connect\
    \ to cities. Now, technologically, it's easier. This article is saying all that\
    \ and that it's a social problem. So why do you think that's the case?"
  sec: 1202
  time: '20:02'
  who: Alexey
- line: "I think your data products are fundamentally products. So if you want someone\
    \ to use a product, what they get out of it \u2013 their benefit \u2013 has to\
    \ be greater than what it costs them. This means how hard it is to use, whether\
    \ that's monetary costs, time costs \u2013 any of that. There can be a lot of\
    \ different factors that contribute to that equation being off. Either the benefit\
    \ is too low or the cost is too high. Most of those sources of those issues are\
    \ really social problems. It's about how people think about this or how they use\
    \ it, and not whether the data is available."
  sec: 1255
  time: '20:55'
  who: Caitlin
- line: "There are two ways to make that work out. You either have to make the benefit\
    \ bigger or make the cost smaller. I think of the major driver of the benefits\
    \ of good data-driven decision-making as being cultural. You have to have a culture\
    \ of measuring people's results and rewarding them. Your better decision has to\
    \ matter. If you're in a situation where your budget next year is going to be\
    \ based on how big your budget was this year and how much of it you spent, then\
    \ you should just spend your budget, period. What you're actually doing with it\
    \ doesn't matter that much. If your manager just gives you a list of things to\
    \ do, and you're rewarded by just doing them, then just do them. Ship the feature\
    \ from the campaign. Check the box. On the other hand, if you have a really clear\
    \ target that's driven by metrics \u2013 you're really focused on improving conversion,\
    \ acquiring new users, etc. \u2013 you start to actually care about which activities\
    \ have the highest leverage and (to get back to the Pareto principle) how to drive\
    \ 80% of the results and 20% of the effort. The only way you can understand that\
    \ is if you start to really dig into the data and understand how your various\
    \ campaigns are performing and how various parts of the conversion funnel are\
    \ behaving. If you don't have those incentives, then there's not a lot of benefit\
    \ from using data and \u201CWhy bother?\u201D"
  who: Caitlin
- line: "On the other side of the equation, you have to keep the costs low. So you\
    \ have to know how to find the data. You have to know how to use the tools. You\
    \ have to know how to interpret the data. You have to have trust in it and not\
    \ constantly be concerned about data discrepancies. \u201CIs this real?\u201D\
    \ \u201CIs this true?\u201D Hopefully, you don't rely on an analyst for every\
    \ question you ask. Because all of that just adds cost to the process. By getting\
    \ the balance right, you then get to a place where people use the data and bring\
    \ it into the decision-making process. They're really using it for prioritization.\
    \ Maybe this is also one path to building a culture of experimentation, where\
    \ people really want to test things and understand how they performed, so that\
    \ they can make better choices next time. All of that healthy data culture comes\
    \ from the incentives, the skills and the training, both of which are really people\
    \ problems."
  who: Caitlin
- line: "So, we need to have a healthy data culture. I think you mentioned that to\
    \ have this, data must be discoverable \u2013 people know how to find it. It must\
    \ also be interpretable \u2013 people need to know how to interpret the data.\
    \ Finally, people need to be able to trust the data. Because if they see that\
    \ something is off, they will say, \u201COkay, I don't want to base my decisions\
    \ on this dashboard. It would be better if I base my decisions on my gut feeling\
    \ because I don't trust this dashboard.\u201D So you have to have all this. You\
    \ also said that everything should be measurable and people should be able to\
    \ see the impact of their work as a number. When we have that, then our data products\
    \ make sense. Then we can use them and show people that it's actually better to\
    \ use our data product to make decisions. \u201DLook, if you do this, your numbers\
    \ improve.\u201D This is not a technological problem. Is that right?"
  sec: 1453
  time: '24:13'
  who: Alexey
- line: "Yeah, absolutely. You have to have the baseline. Obviously, the technical\
    \ side of it is table stakes but this is where you get into the last mile. The\
    \ last mile is all the \u2018people part\u2019. It's making sure that people know\
    \ how the incentives are aligned correctly for it. To the extent necessary, you\
    \ might have to actually sit in the room with them and help them understand \u201C\
    How do I understand this campaign data? How do I tell which ones are performing?\
    \ How do I tell what happens if I put more money behind the same campaign? Am\
    \ I getting the same impact from the next dollar as I did from the last dollar?\u201D\
    \ There are real questions people don't understand and the barriers are often\
    \ not because the data is not available. It's often hand-holding, training, and\
    \ helping them to understand."
  sec: 1524
  time: '25:24'
  who: Caitlin
- header: Making sure data is used
- line: Is there any other way? Let's say we have everything measurable. We have an
    analyst who can sit with the decision-maker and explain everything. Is this enough
    to make sure that the data is actually used?
  sec: 1581
  time: '26:21'
  who: Alexey
- line: "I think it depends. It takes a lot of work to understand why the data isn't\
    \ being used. If the data doesn\u2019t exist, then it's not a lot of work to understand\
    \ what the path is to fix this. You know that \u201CI have to bring it into the\
    \ data warehouse. I have to clean it up and make it useful. Create some reporting\
    \ on top of it. And voila!\u201D Once you've got that, if it's not getting used,\
    \ there are lots of different things that might be going wrong. You really have\
    \ to spend some time understanding what those barriers are and what those look\
    \ like."
  sec: 1596
  time: '26:36'
  who: Caitlin
- line: "In a lot of ways, it looks more like user research. You build a product,\
    \ you put it out there, and people aren't using it the way that you thought they\
    \ would. So, what's the barrier? \u201CDo they know that it exists? Do they know\
    \ how to use it? Does it solve the problem they actually have?\u201D Really interrogating\
    \ and understanding where the gaps are is the key to being able to fix those gaps.\
    \ Obviously, if people just don't know about it, that's relatively easy to solve.\
    \ If it fundamentally doesn't answer the question they're asking, then that can\
    \ be a little more challenging to solve and it really requires another round of\
    \ work and understanding \u201CWhat are you really trying to do with this data?\u201D"
  who: Caitlin
- line: If it's difficult to use, you either solve it by educating or simplifying
    it?
  sec: 1684
  time: '28:04'
  who: Alexey
- line: "Yeah. Hopefully a little bit of both. It\u2019s all about creating the right\
    \ balance of what's possible in your tools, how much you think people are really\
    \ going to learn and work around. So if the problem is just not knowing how it\
    \ works, then the solution is just teaching them. If it's really hard, then you\
    \ might have to really think about \u201CHow much can I simplify this? Do I need\
    \ to take a different approach? Is there a totally different way to get to the\
    \ same result that would be more user-friendly?\u201D"
  sec: 1690
  time: '28:10'
  who: Caitlin
- header: Communicating with decision makers
- line: "I'm thinking about an example we have at OLX. We do a lot of experiments,\
    \ usually A/B tests. Let's say we have some traffic of users coming in \u2013\
    \ for some users, we show one variant, and for some other users, we show a different\
    \ variant. Then we compare different metrics and see if the new feature gets uplift\
    \ in some metric. Standard A/B tests. Then I think the problem we had at some\
    \ point was that the people who are looking at this, we were showing them too\
    \ much statistical stuff like, P values, test power \u2013 all these statistical\
    \ things. They were just overwhelmed. \u201CWhat does this all mean? All these\
    \ \u2018confidence in development\u2019 or this \u2018P value?\u2019\u201D It\
    \ required a lot of iterations to first teach them, and then to think, \u201C\
    What can we not show them? Do we really need to show all that to them? Do they\
    \ really need to know about the P values and what these P values mean?\u201D Or\
    \ maybe we can just show them \u201COkay, this is significant.\u201D And that's\
    \ it. I guess this is quite in line to what you're saying, right?"
  sec: 1722
  time: '28:42'
  who: Alexey
- line: "It\u2019s very similar. I've been in similar A/B testing situations before\
    \ and even within your users, I bet there's a variation of how much people are\
    \ willing to learn or are interested in learning. It's all about figuring out\
    \ \u201DWho are you optimizing for? How do you trade-off between simplicity and\
    \ functionality?\u201D We did the same thing and for us, that looked like setting\
    \ a default P value for significance, but also allowing people to change it if\
    \ that was something they were comfortable with and understood all that. So the\
    \ experiment was communicated in terms of \u201CSignificant. Not significant.\
    \ Here's how you interpret it.\u201D"
  sec: 1803
  time: '30:03'
  who: Caitlin
- line: "But we had enough toggles for people \u2013 a couple of power users \u2013\
    \ to go in and say, \u201CActually, in this situation, I'm good with this level\
    \ versus this level. This is how we want to measure this test in particular.\u201D\
    \ But, it's really hard to get the right balance and to make it feel really useful\
    \ to people. When you have such a deep knowledge of the data and the space, you\
    \ can often think, \u201COh. Well, I can look at this and the depth of understanding\
    \ I get is really rich.\u201D But often business users just really want a simple,\
    \ super easy-to-interpret result."
  who: Caitlin
- line: "If you let data scientists build the tool, then they will show all these\
    \ things like \u201CThis is the Mann-Whitney U test. This is the power of the\
    \ test. This is the P value. This is the confidence interval.\u201D All these\
    \ technical things. If you talk about machine learning, then \u201CThis was the\
    \ accuracy, precision, recall, ROC curve, AUC.\u201D  Things like this. If you\
    \ show this to the business, and then they say, \u201COkay, what is that? How\
    \ much money is this thing actually going to make? Why are you showing me all\
    \ that?\u201D I guess this is what ultimately matters to them. So, bridging this\
    \ gap is not a technological problem, it's more like a social problem. Like \u201C\
    How do you actually communicate this?\u201D"
  sec: 1895
  time: '31:35'
  who: Alexey
- line: "It's a lot like building any technical product. I think a lot about Zapier\
    \ as a really good example of this. Zapier exists to take something that is technical\
    \ and make it non-technical \u2013 to allow people to leverage APIs to accomplish\
    \ automation without knowing what an API is. It's really hard to get the right\
    \ level of abstraction when you start to talk about something like that. It's\
    \ really difficult to build a thing that's going to let someone who's comfortable\
    \ parsing out text and doing a bunch of interim steps, versus the person who just\
    \ like, \u201CWhen I get an email, can you just send me a Slack also? I just want\
    \ it to be exactly the same.\u201D"
  sec: 1945
  time: '32:25'
  who: Caitlin
- line: It really is a lot like product design. There's the challenge that your data
    teams are really small compared to your product team, most likely. You have to
    learn to find the right points of leverage, find enablers, train power users and
    have them train their teams. You have to find all of these ways to scale the work
    that you have to do. Because you don't have a whole team dedicated to doing a
    lot of research and spending a ton of time on design. It's a scaled down version
    but ultimately kind of the same problem.
  who: Caitlin
- header: Working backwards from the last mile
- line: You wouldn't believe it, but I actually read another article. So I think I
    read 3 in total. I think I talked to you about the first one, which was about
    comparing the last mile to a marathon. The second one was talking about it being
    a social problem VS technological problem. Then the third one said that you should
    prioritize the last mile of the analytical journey and work backwards. This is
    probably quite a long sentence. There are many things to unpack here. So they
    say that they prioritize the last mile and work backwards. Do you know what they
    mean here? Why should we prioritize it and how do we work backwards from that?
  sec: 2040
  time: '34:00'
  who: Alexey
- line: "I interpret that as really focusing first on what success looks like for\
    \ the thing that you're building. For different types of projects, that's going\
    \ to be very different. For your A/B test results dashboard or tool, what you\
    \ want is for a product manager to be able to make the right decision on whether\
    \ to roll out a feature or not. There are other goals around that. You want to\
    \ make sure that they wait long enough to get meaningful results. You want to\
    \ make sure that they are running an experiment in a responsible way \u2013 there\
    \ are some subsidiary goals there."
  sec: 2082
  time: '34:42'
  who: Caitlin
- line: "But what you're really focusing on is, \u201CI want a project manager to\
    \ be able to come here, look at their experiment, and understand whether it worked\
    \ or potentially what the business impact was.\u201D Maybe you actually need to\
    \ convert it into dollars. Focusing there helps you really understand what you're\
    \ going to need to build. If you need to communicate it in dollars, then you need\
    \ to start thinking from the beginning of how you're going to build toward that.\
    \ Instead of immediately thinking, \u201CI need an A/B testing dashboard \u2013\
    \ I need to start thinking about what our event data looks like.\u201D You're\
    \ thinking about the user first. That's going to change how you think about the\
    \ data sources, the transformation jobs, what else you need to join in. How you\
    \ want to build the dashboard \u2013 you're really starting with that decision\
    \ that you're trying to drive."
  who: Caitlin
- line: "I think at Amazon they have this \u2018working backwards\u2019 principle.\
    \ I\u2019m not sure if it's at Amazon or somewhere else, but I heard this concept\
    \ before. Let's say you're working on some product. It can be a feature \u2013\
    \ it doesn't even have to be a data product. The first thing you do is you write\
    \ an announcement \u2013 you write a blog post that you would publish when the\
    \ feature is done. You write a couple of pages and once you have that, you then\
    \ work backwards from this announcement. So you work as if this feature already\
    \ existed \u2013 as if you already did it. Then you think, \u201COkay, what do\
    \ I need to do to actually build this feature?\u201D"
  sec: 2187
  time: '36:27'
  who: Alexey
- line: "What you\u2019re saying, as I understood it, is to think of the end user,\
    \ right? In the case of a data product, such as an A/B testing system, it could\
    \ be a product manager who will need to make a decision based on what you show\
    \ them. So they will need to understand if the feature we're testing is making\
    \ an impact and what this impact is, \u201CHow much better is this thing than\
    \ the current thing?\u201D We think about this, and I guess we can start involving\
    \ the user \u2013 the product manager \u2013 immediately. Before even building\
    \ this thing. So you ask questions like \u201CWhat kind of things do you need?\
    \ What kind of problems do you have? How can we solve your problem?\u201D"
  who: Alexey
- line: "If we involve them from the beginning, it makes it easier for us to build\
    \ this thing, because we're already thinking about the end user. So the last mile\
    \ here, as you said, is making sure that the data is used \u2013 or that the product\
    \ is used. If we involve the end user, if we think about the end user from the\
    \ very beginning, then it makes it easier. Did I interpret this correctly?"
  who: Alexey
- header: Understanding how data drives decisions
- line: "Yeah, I think that's exactly right. It's talking to the users \u2013 we were\
    \ talking a lot about how data drives a decision. It's literally sitting in the\
    \ meetings where those decisions are made right now and understanding what that\
    \ process looks like. Maybe, for this A/B testing example, the decision could\
    \ consistently look like \u201CI have to share the results of my test against\
    \ my intended impact metric and then I also have to share these other two to make\
    \ sure that we're not adversely affecting something else too much.\u201D That's\
    \ the kind of insight where, if you understand that this is what the product team\
    \ really needs to make the right decision, you build from that as well."
  sec: 2295
  time: '38:15'
  who: Caitlin
- line: "It\u2019s about sitting in the meetings where these decisions are being made\
    \ and talking to the people who are making them. I love pen and paper. I spent\
    \ a lot of time sketching things out and saying things like, \u201COkay. If it\
    \ looks like this, what does that tell you? What's missing? What does the deck\
    \ you're building look like? What does the deliverable you're creating look like?\
    \ Does this dashboard get you there? Does this tool get you there?\u201D So, it\u2019\
    s really getting hands-on. I love writing the press release first. It's very similar,\
    \ like, \u201CWhat do people say about the thing that you built?\u201D"
  who: Caitlin
- header: Sketching and prototyping
- line: "This sketching \u2013 it\u2019s a lot like prototyping, basically, \u201C\
    How would this look at the end?\u201D Then you show it to the decision maker \u2013\
    \ whoever the end user is \u2013 just using a piece of paper. \u201CDoes this\
    \ look like what you have in your head?\u201D Then they say, \u201COkay. You know,\
    \ it actually looks completely different.\u201D So, you start talking and they\
    \ say, \u201COK. I want this thing here and this thing is not what you understood\
    \ initially, but it's a different one.\u201D Then you start discussing this. Right?"
  sec: 2372
  time: '39:32'
  who: Alexey
- line: "Yeah. That conversation is easier to have if they don't think that you put\
    \ a lot of time and effort into it. Not that you didn't put enough thought into\
    \ it, but \u201CI just sketched this out really quick. So feel free to speak up\
    \ if it doesn't speak to you.\u201D Versus \u201CI created this really robust\
    \ prototype in Figma. It's really beautiful, and you're going to be calling my\
    \ baby ugly if you tell me that this thing doesn't work for you.\u201D It's a\
    \ lot easier to get real feedback if the bar is relatively low."
  sec: 2405
  time: '40:05'
  who: Caitlin
- line: "Maybe these days it\u2019s not so easy, but also using a whiteboard. Get\
    \ around the whiteboard and start drawing there. Then we get a lot of feedback,\
    \ right?"
  sec: 2436
  time: '40:36'
  who: Alexey
- line: Yeah.
  sec: 2452
  time: '40:52'
  who: Caitlin
- header: Showing the benefits of power data
- line: "We have a few questions, so maybe we can start covering these questions?\
    \ So, a question from Aideen. I hope I pronounced your name correctly. \u201C\
    When data challenges the traditional decision system, how can we show the benefits\
    \ of power data? Do you have some experience with this issue?\u201D"
  sec: 2453
  time: '40:53'
  who: Alexey
- line: "Again, this comes back to making sure the right incentives exist in the organization.\
    \ But ideally, you want people to be really incented by good results. Then what\
    \ you need to do is actually show better results. So you're thinking about the\
    \ marketing team and helping them make better choices. Well, the results of that\
    \ are, \u201CWe spent the same amount this month as last month, but we acquired\
    \ 30% more users.\u201D Usually, the results are not that clear. Obviously, if\
    \ you have a culture of A/B testing and the tools for A/B testing, that's an amazing\
    \ place to start \u2013 to be really confident in your results. But a lot of times,\
    \ this is really more anecdotal. You might not have super robust ways to report\
    \ on results. But creating those moments of comparison are still really helpful."
  sec: 2478
  time: '41:18'
  who: Caitlin
- header: Measurability
- line: Would you say it's a must that we have everything measurable? Or can we already
    start convincing people to use our data product when not everything is measurable
    yet?
  sec: 2538
  time: '42:18'
  who: Alexey
- line: "You're never really at the point where everything is measurable, right? So\
    \ being as close as you can get is what you need. For example, I work in an environment\
    \ where we've got a warehouse, through which some activities are basically invisible\
    \ in our data \u2013 they're fully manual. You can't effectively measure how long\
    \ a process took or anything else. But a lot of times, when we make changes to\
    \ process or make changes to our tools, we literally just spent a couple of hours\
    \ doing a time study. Someone sits with a stopwatch and times people and says\
    \ \u201CDid this take more or less time?\u201D Is that precise? No. Is that a\
    \ real experiment? No. But it's better than nothing. And if you are talking about\
    \ sufficiently large changes, then it's compelling. You can tell, \u2018\u2019\
    I cut this time in half. That must be real.\u201D Versus\u2026 it's indistinguishable.\
    \ We should go with the process that's more scalable or the process that's better\
    \ for some other reason, and start to make decisions from there."
  sec: 2549
  time: '42:29'
  who: Caitlin
- line: "Yeah, that's interesting. I was also thinking about, if you work in ecommerce\
    \ \u2013 at least if we're talking about a website only \u2013 then all these\
    \ clicks are relatively easy to measure. I mean capture, track them and put them\
    \ somewhere in your data warehouse and then have all these dashboards. But if\
    \ we\u2019re talking about some manufacturing line somewhere, or a warehouse where\
    \ the actual people move things \u2013 not robots, but actual people \u2013 then\
    \ it becomes tricky. You cannot put trackers on people, and watch how they move\
    \ because A: they will not like it and B: it's probably not cheap. Right?"
  sec: 2619
  time: '43:39'
  who: Alexey
- line: "It can be really hard, but I really love a good proxy metric. \u201CWhat's\
    \ the closest we can get to measuring this thing?\u201D I think anything related\
    \ to employees is a great example of this. We're never gonna have a large enough\
    \ sample of employees that we're running A/B tests on employee engagement, but\
    \ we're gonna throw a survey out there and see how people feel. Ultimately, you\
    \ kind of make your best decision. But, in most businesses, there are a ton of\
    \ parts of the business that are really easy to measure. I think that's a really\
    \ good place to start for these cultural changes. You want people to use data,\
    \ start with the data you have. Then you'll get to a point where you're starting\
    \ to talk about \u201CHow do we optimize these less visible parts of the process?\u201D\
    \ Then, hopefully, you've got the trust from everybody, and you've got enough\
    \ culture of data-oriented thinking that you can start to find ways to feel good\
    \ about those areas as well."
  sec: 2670
  time: '44:30'
  who: Caitlin
- header: Driving change in data
- line: Marketing is probably a good start in many cases. Because you basically have
    some sort of web page and you can play with different wording there or different
    positional things. Even with that, you can already start measuring and then show
    that you can measure this. Then people see that it is useful to have things like
    this, and then you start using this as a convincing argument. People start believing
    you and then you take care of more complex things. Right?
  sec: 2735
  time: '45:35'
  who: Alexey
- line: "Yeah. I think Emilie Schario does a really good job talking about, when you're\
    \ trying to drive change with data, how to focus on as narrow a slice as possible.\
    \ I'll have to dig this up, because I\u2018m not sure where she wrote this. But\
    \ I'm going to credit it to her. As you think about how much you can scope down\
    \ your work, you want to really focus on, \u201CI want to enable this salesperson\
    \ to make this better decision based on the data. And so, I'm going to focus entirely\
    \ on that until that end is accomplished.\u201D That means all the infrastructure\
    \ work that\u2019s necessary, all of the transformation work \u2013 whatever it\
    \ takes to get there."
  sec: 2771
  time: '46:11'
  who: Caitlin
- line: "But when you narrow in, then you've got a really clear success story. You've\
    \ got an advocate in that stakeholder. You've got everything that you need to\
    \ start to build the case for a bigger role for data in general. You move on to\
    \ the next team and you say, \u201COkay, how can I help marketing address this\
    \ decision? How can I help product address this decision?\u201D"
  who: Caitlin
- line: "And I didn\u2019t hear the last name, Emily..."
  sec: 2843
  time: '47:23'
  who: Alexey
- line: Emilie Schario, I'll add a link.
  sec: 2847
  time: '47:27'
  who: Caitlin
- header: Asking high-leverage questions
- line: "Okay. I'll put this in the description. We also have a question from Kurt,\
    \ who is asking, \u201CYou have emphasized asking high leverage questions. Do\
    \ you have any tips on finding these points as both an analyst and an executive?\u201D"
  sec: 2850
  time: '47:30'
  who: Alexey
- line: Part of this is having enough bandwidth for analysts to do a little digging
    and understanding this themselves. If the business isn't looking at data, then
    you probably don't know the highest points of leverage off the top of your head.
    But if you spend a little time in the data, I think you'll start to understand
    that. Often, the best place to start is actually not with the data in your data
    warehouse, but with your financials.
  sec: 2872
  time: '47:52'
  who: Caitlin
- line: "So it\u2019s sitting down with someone from your accounting and finance team\
    \ to understand, \u201CWhat does our performance look like? What's our biggest\
    \ cost center? Where are we spending money?\u201D Wherever you're spending money\
    \ is a really good place to bring the data to understand how you can do that more\
    \ effectively and more efficiently. Either spend less or get more for what you're\
    \ spending. That has consistently been a good approach for me to identify those\
    \ points of leverage."
  who: Caitlin
- line: "You don't have to solve the biggest problems first. Sometimes the biggest\
    \ problem is really hard. But you have to solve a big enough problem that people\
    \ care about it. So you have to find that sweet spot between \u201CWe spend X\
    \ dollars a month on marketing, so I want to focus on improving the efficiency\
    \ of our marketing spend, even though we spend 10x on our warehouse employees.\
    \ But we don't know what they're doing, so I'm not ready to tackle that problem\
    \ yet.\u201D [laughs]"
  who: Caitlin
- header: Resistance from users
- line: "I also imagine that you can get some resistance. Let's say you're starting\
    \ with financials, you find the biggest cost center \u2013 this is the warehouse.\
    \ You go to the warehouse manager, and you're saying \u201CHey, how about using\
    \ data?\u201D And they respond, \u201CHow about no.\u201D [laughs] I imagine that\
    \ this can happen, right? So what would you do in this case, if there is some\
    \ resistance from people? If they are not really eager to use the data?"
  sec: 2965
  time: '49:25'
  who: Alexey
- line: I think that there are two separate answers. If I am independently trying
    to push this project through and push this cultural change, I would not start
    with that particular warehouse manager. I want my first project to be with someone
    who has already bought in with me. And I'd rather work on something smaller, or
    something harder, and have someone who's in the boat rowing in the same direction
    with me, than try to convince the primary stakeholder that this is a good idea.
    You want to find someone who will be your advocate, someone who really wants this.
    In most organizations, you're going to be able to find one person who really wants
    more data and wants to make decisions with that data.
  sec: 2999
  time: '49:59'
  who: Caitlin
- line: "So if it's totally up to me, I just say, \u201COK, cool. Thank you. I am\
    \ excited to talk more about this in the future.\u201D And we come back when there's\
    \ much more of a snowball of a more healthy data culture coming and they're more\
    \ likely to buy in. If this has to be the first area, then I assume that it\u2019\
    s coming from someone else. If a COO hands this off to you, and says to \u201C\
    Work with this person in the warehouse and figure it out.\u201D Then you have\
    \ to be a lot more delicate around how to get that person on board and how to\
    \ convince them of the value of it."
  who: Caitlin
- line: "I would say, generally, always focus on upside, not savings. Don't talk about\
    \ how \u201CWe could ultimately need half as many people in the warehouse and\
    \ that's why we should do this.\u201D Talk to them enough to understand what they're\
    \ not doing that they wish they could do. Then you can start to talk about it\
    \ and say, \u201CWell, if we were more efficient in this part of the process,\
    \ then you would have enough people to do this other thing that you want to do.\u201D\
    \ Or find ways that show that driving better performance really benefits that\
    \ person instead of potentially feeling like something's being taken away from\
    \ them. I think that's usually the most impactful part of getting somebody in\
    \ the boat."
  who: Caitlin
- line: Just really sell on the benefits and find something that bothers them that
    you can help with. Start to kind of build that rapport and that trust. Honestly,
    in data roles, this is almost always manual Excel processes. Find what they do
    in Excel and find a way to make that better, even if it has nothing to do with
    the project you're working on. [laughs] Start to make them your advocate. Start
    to make them appreciate you.
  who: Caitlin
- line: "I was saying that, if you're looking for low-hanging fruit, this could be\
    \ the marketing department. I think marketers have realized by now the importance\
    \ of using data for making decisions. Things like \u201CWhich channel is more\
    \ effective? Where should I put more money?\u201D They will probably be more welcoming\
    \ to you, your work, and using data in general. They're probably using some data\
    \ already, but they will be happy to use more of it. Especially in growth marketing,\
    \ I think. I took a course in growth marketing and I was surprised by how much\
    \ stats there were \u2013 A/B testing and tracking data. It's basically some data\
    \ analysis plus a marketing sort of position. So, I was surprised by that."
  sec: 3165
  time: '52:45'
  who: Alexey
- header: Understanding domain experts
- line: "Okay, we have another question. \u201CWhat kind of questions do you ask domain\
    \ experts to understand their domain? And can you recommend some literature on\
    \ that?\u201D"
  sec: 3226
  time: '53:46'
  who: Alexey
- line: "Oh, that's a really big question. I think it depends a lot on the domain\
    \ and the person that you're talking to. I think coming to any conversation with\
    \ just a really genuine curiosity can get you a really long way. Framing questions\
    \ from genuine curiosity can make all the difference when you say something as\
    \ open-ended as, \u201CSo what do you do here?\u201D That can be a really curious\
    \ question or that could be a really judgmental question. You have to make sure\
    \ that you're genuinely coming from a place of wanting to understand and wanting\
    \ to really get a grasp on what they do and what's hard for them and what challenges\
    \ that the team overall is facing and just building rapport."
  sec: 3237
  time: '53:57'
  who: Caitlin
- line: "That will depend a lot on how much you know about the person and the organization\
    \ and how embedded you are. Sometimes it really just starts with not talking about\
    \ what they do at all and getting to know them as a person and building a relationship\
    \ before you start to build a work relationship. This would be just coming from\
    \ a real, open-minded place of wanting to understand what they do \u2013 that\u2019\
    s the biggest part. Ideally, after you start to understand what they do, you could\
    \ document their job for them and just ask all the questions you would want to\
    \ know and kind of write the \u2018handbook\u2019 to this person's job. Certainly\
    \ don't frame it that way to them, because that sounds a little bit scary [laughs]\
    \ and a little bit like maybe you're trying to onboard the next person."
  who: Caitlin
- line: "So you have to be quite good at understanding people. How you approach them\
    \ and even in what tone you ask a question. Because if you ask a question like\
    \ \u201CWhat do you do here?\u201D it can sound curious or it can sound judgmental.\
    \ So you really have to be careful."
  sec: 3335
  time: '55:35'
  who: Alexey
- line: "Yeah. I certainly don't want to frame that in a way that intimidates anyone.\
    \ I've worked with a lot of data teams, and we definitely over-index on introverts.\
    \ I am a strong introvert. I wouldn't necessarily say that early in my career,\
    \ I felt super confident about my social skills. I was not a person that someone\
    \ would say, \u201COh, yeah. She has great EQ \u2013 very high emotional awareness.\u201D\
    \ That's something that I've had to build over time. I think if you just genuinely\
    \ really focus on the curiosity side of it \u2013 it'll work out. Maybe I wouldn't\
    \ worry too much about the missteps but, even for yourself, frame your questions\
    \ as wanting to understand and not immediately as wanting to make better. I think\
    \ that makes all the difference in the way that you approach the situation."
  sec: 3358
  time: '55:58'
  who: Caitlin
- line: So the recommended literature would be some books about emotional intelligence?
  sec: 3410
  time: '56:50'
  who: Alexey
- line: "Yeah, maybe. Or I think it also depends on the area. If you're working on\
    \ something super-specific and if you're working with digital marketers, then\
    \ read a book on digital marketing. If what you're trying to understand more generally\
    \ is \u201CHow do I influence without authority?\u201D Then there are some really\
    \ good books around how to do that. There's Dale Carnegie's \u2018How to Win Friends\
    \ and Influence People\u2019. It's the classic, but there are others, if that's\
    \ not your particular cup of tea. You can find books that are more focused on\
    \ just \u201CHow do you build rapport with people? How do you really build those\
    \ soft skills?\u201D That might make you feel more comfortable as well."
  sec: 3417
  time: '56:57'
  who: Caitlin
- line: Yeah, I actually tried reading this book at some point. It was difficult for
    me.
  sec: 3465
  time: '57:45'
  who: Alexey
- line: "Yeah, I've actually never finished it either. I don't love it. But it is\
    \ the classic and people who have read it generally speak very highly of it. So\u2026\
    \ I don't know."
  sec: 3471
  time: '57:51'
  who: Caitlin
- line: "It's like the book \u2018Getting Things Done\u2019. Some people love it.\
    \ Some people hate it."
  sec: 3483
  time: '58:03'
  who: Alexey
- line: Yeah. Yeah.
  sec: 3488
  time: '58:08'
  who: Caitlin
- header: Linear projects vs circular projects
- line: "It's always binary, it\u2019s never in between. Okay. We have the last question.\
    \ We still have a couple of minutes. So a question from Eileen is \u201CSometimes\
    \ data projects can\u2019t give expected results and this is normal. But this\
    \ is creating trust problems in data projects. What do you think about this? How\
    \ do you approach it? Would you approach it in such a way that it doesn't create\
    \ trust problems?\u201D"
  sec: 3491
  time: '58:11'
  who: Alexey
- line: "=Something like building a data pipeline to bring something into the warehouse.\
    \ That's probably pretty linear. You know there is an API \u2013 it might not\
    \ have all the data you want in it, but you can look at the docs pretty quickly\
    \ and understand that. A circular project is one where until you know what's in\
    \ there, you don't know if you're gonna be able to do it. A lot of data science\
    \ projects fall into this \u201CUntil I test it, I don't know how good my results\
    \ are going to be.\u201D And a lot of analysis projects are like this because\
    \ it\u2019s like \u201CI want to answer the question \u2013 why was conversion\
    \ up last month? I have no idea if I actually have the data to answer that and\
    \ I won't know until I dig into it really substantially.\u201D"
  sec: 3516
  time: '58:36'
  who: Yeah. I actually wrote two blog posts with Alexis Johnson Gresham. I can share
    links to those about this exact problem because I think it's a really difficult
    one. Alexis first shared this phrase with me, which was really a light bulb moment,
    around linear projects versus circular projects. Even within data, you have both
    of them. There are linear projects, where you can chart out the next step. You
    have a high level of certainty that if you do step one, you can do step two. After
    you do step two, you can do step three. And then there are circular projects,
    where you don't know what you don't know. And a lot of data projects fall into
    this category.
- line: "I'll share more about this, but the very high-level overview is first just\
    \ to set expectations. Acknowledge ahead of time that it is a circular project.\
    \ You don't know if it's going to be successful. You lose a lot of trust by saying\
    \ you can definitely do something and then not delivering. But people understand\
    \ if you say, \u201CI'm not sure if this is possible, I need to dig into it.\u201D\
    \ Break it down into as small pieces as possible, so that you can quickly make\
    \ progress and report back and say, \u201CI've gotten this far. Looks good so\
    \ far. Next stumbling block is this.\u201D Or \u201CI spent two days on it. I\
    \ think it's gonna be really hard for this, this and this reason. Here are alternatives\
    \ and things we could do to make it less difficult or more possible.\u201D"
  who: Yeah. I actually wrote two blog posts with Alexis Johnson Gresham. I can share
    links to those about this exact problem because I think it's a really difficult
    one. Alexis first shared this phrase with me, which was really a light bulb moment,
    around linear projects versus circular projects. Even within data, you have both
    of them. There are linear projects, where you can chart out the next step. You
    have a high level of certainty that if you do step one, you can do step two. After
    you do step two, you can do step three. And then there are circular projects,
    where you don't know what you don't know. And a lot of data projects fall into
    this category.
- line: "Really lean into that communication and alternatives. \u201CHere's what we\
    \ can do.\u201D Rather than \u201CHere's what we can't do.\u201D Or \u201CHere's\
    \ what we\u2019ve learned.\u201D Hopefully, you then start to also build a culture\
    \ of \u201CFailure is learning.\u201D and \u201DLet's talk about it. Let's be\
    \ really excited that now we know this thing is not possible with the data we\
    \ have. At the minimum, like we don't ever have to think about that problem until\
    \ something dramatically changes. We don't have to put resources against this\
    \ again. It's not on the backlog anymore. We've checked whether it's going to\
    \ work, and it's not.\u201D So, find some ways to help people celebrate the learning."
  who: Yeah. I actually wrote two blog posts with Alexis Johnson Gresham. I can share
    links to those about this exact problem because I think it's a really difficult
    one. Alexis first shared this phrase with me, which was really a light bulb moment,
    around linear projects versus circular projects. Even within data, you have both
    of them. There are linear projects, where you can chart out the next step. You
    have a high level of certainty that if you do step one, you can do step two. After
    you do step two, you can do step three. And then there are circular projects,
    where you don't know what you don't know. And a lot of data projects fall into
    this category.
- header: Recommendations for data analyst students
- line: "Do you have a couple more minutes? There is one more question that popped\
    \ up, and it\u2019s very interesting. So Kurt is asking, \u201CI'm currently a\
    \ data analyst student. Do you have any recommendations, resources, or habits\
    \ that helped you achieve success in your career?\u201D"
  sec: 3690
  time: '1:01:30'
  who: Alexey
- line: Getting started in data is really interesting. It's really hard, outside of
    a data role, to even remotely approximate what it's going to be like. Public data
    sources are completely different from the data you're going to run into in a company.
    My biggest advice is just to be really curious and to think a lot about why things
    matter. The logistics of being a data analyst, you can learn on the job, no problem.
    You'll learn how to write queries. You'll learn how to approach problems. But
    building that curiosity and that sense of impact and tying results back to the
    business is often the hardest part.
  sec: 3710
  time: '1:01:50'
  who: Caitlin
- line: "Sometimes that looks like taking more business classes or taking the time\
    \ to understand the scale of impact that you can get from a data source in whatever\
    \ project you're working on. If you're in an econometrics class \u2013 do all\
    \ of your analysis and then understand \u201CWhat would this mean if this were\
    \ true holistically? If this policy went out, what would the real impact of that\
    \ be?\u201D And how you think about that versus other options. That skill is,\
    \ hands down, the most useful skill for a data analyst to have."
  who: Caitlin
- line: So it would be more business skills, business acumen, and the understanding
    of how business works, versus just being really good at SQL and being really good
    at other things that analysts do technically?
  sec: 3797
  time: '1:03:17'
  who: Alexey
- line: "Yeah. The technical skills are useful, but also are not nearly as hard to\
    \ teach. Most good analytics leaders know \u201CIf I find someone who is really\
    \ smart and understands the importance of the data, I'm going to be able to teach\
    \ them SQL.\u201D Whereas the reverse might not always be true."
  sec: 3810
  time: '1:03:30'
  who: Caitlin
- header: Finding Caitlin online
- line: Where can people find you? Locally Optimistic?
  sec: 3833
  time: '1:03:53'
  who: Alexey
- line: Locally Optimistic, yeah. I should really join your Slack as well. I was thinking
    about that earlier this week. I will join today and I'll be there if there's a
    particular channel that you tend to chat with people in, but I'm also always Locally
    Optimistic. Always happy to chat there.
  sec: 3836
  time: '1:03:56'
  who: Caitlin
- line: In your blog post, did you draw your pictures yourself?
  sec: 3852
  time: '1:04:12'
  who: Alexey
- line: "No, we have an amazing Illustrator who does all of our blog posts. It\u2019\
    s like my favorite thing about the blog."
  sec: 3856
  time: '1:04:16'
  who: Caitlin
- line: Yeah, the illustrations are amazing. You were saying that, at some point,
    you would just take a piece of paper and start sketching. So I thought maybe it
    is actually you who create all these illustrations. But, no.
  sec: 3863
  time: '1:04:23'
  who: Alexey
- line: "Sadly, I am not quite that artistically talented. My sketches really encourage\
    \ people to say \u201CThat's not quite right.\u201D [laughs]"
  sec: 3877
  time: '1:04:37'
  who: Caitlin
- line: "I see. [laughs] Okay, thanks a lot. Thanks for joining us today. Thanks for\
    \ sharing your experience. Thanks for answering questions. And also thank you,\
    \ everyone, for joining us and for asking questions. Yeah \u2013thank you, Caitlin."
  sec: 3886
  time: '1:04:46'
  who: Alexey
- line: Yeah, thank you so much. This has been awesome.
  sec: 3898
  time: '1:04:58'
  who: Caitlin
- line: Yes, thanks. Have a great rest of your day and have a good weekend.
  sec: 3901
  time: '1:05:01'
  who: Alexey
- line: You too.
  sec: 3905
  time: '1:05:05'
  who: Caitlin


---

Links:

- [Emelie's talk](https://docs.google.com/presentation/d/1wW5KN5hRsfOyzCL-vPY3vIJz1eGwCl8eWHuJNv7KI58/edit#slide=id.gea794867e6_0_1133){:target="_blank"}
- [Linear vs Circular Projects, part 1](https://locallyoptimistic.com/post/linear-and-circular-projects-part-1/){:target="_blank"}
- [Linear vs Circular Projects, part 2](https://locallyoptimistic.com/post/linear-and-circular-projects-part-2/){:target="_blank"}