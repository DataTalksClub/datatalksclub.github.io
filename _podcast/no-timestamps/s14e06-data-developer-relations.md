---
episode: 6
guests:
- hugobowneanderson
ids:
  anchor: ow/datatalksclub/episodes/Data-Developer-Relations---Hugo-Bowne-Anderson-e25q88q
  youtube: z7BvslwVRbQ
image: images/podcast/s14e06-data-developer-relations.jpg
links:
  anchor: https://podcasters.spotify.com/pod/pod/show/datatalksclub/episodes/Data-Developer-Relations---Hugo-Bowne-Anderson-e25q88q
  apple: https://podcasts.apple.com/us/podcast/data-developer-relations-hugo-bowne-anderson/id1541710331?i=1000617298688
  spotify: https://open.spotify.com/episode/7bVCKqn9fLt6ETq8hxId5V?si=GZSC3NbvRuyXD85iOQo51Q
  youtube: https://www.youtube.com/watch?v=z7BvslwVRbQ
season: 14
short: Data Developer Relations
title: 'Master Full-Stack ML with Metaflow: DevRel, Open-Source Governance & AI Trends'
transcript:
- line: This week, we'll talk about developer advocacy. We have a special guest today
    – very special – Hugo. Hugo is the Head of Developer Relations at Outerbounds.
    He's also a co-host of the Vanishing Gradients podcast. He's a data scientist,
    educator, evangelist, content marketer, and data strategy consultant. He is a
    very well-known educator. He developed over 30 courses on the DataCamp platform.
    Many of you probably already know Hugo. With these 30 courses, he managed to impact
    over 2 million learners through online education. It's a big honor to have you
    here today. Welcome.
  sec: 93
  time: '1:33'
  who: Alexey
- line: Thank you so much for having me here. It's a great honor to be here. For those
    who don't know, this will go live soon, but we also recorded an open-source demo
    of Metaflow and full-stack machine learning using the sandbox we've built recently,
    which kind of shows all the layers of the machine learning stack and how we can
    interoperate with them. We'll chat about that later, but we can include a link
    to that in the show notes as well. So this is a fun week for me and DataTalks.Club
    as well.
  sec: 134
  time: '2:14'
  who: Hugo
- line: We definitely will do this. Not everyone knows that Outerbounds, or rather,
    it's not obvious to most people that Outerbounds is the company behind Metaflow,
    which is a tool that you guys are working on.
  sec: 159
  time: '2:39'
  who: Alexey
- line: Exactly. Yeah, we'll get to that, but Metaflow is a human-centric tool for
    developing full-stack machine learning applications and software. As a company,
    we support it and build software and a platform that supports it and helps people
    to use it. Sorry, I'd have to fire myself if I didn't say that.
  sec: 174
  time: '2:54'
  who: Hugo
- line: '[chuckles] The questions for today''s interview were prepared by Johanna
    Bayer. As always, thanks Johanna for your help. By the way, because Hugo is based
    in Australia and Johanna is based in Australia, today Johanna can actually join
    our session live. Hi, Johanna. That''s cool.'
  sec: 193
  time: '3:13'
  who: Alexey
- line: Amazing. Thank you for all your work.
  sec: 215
  time: '3:35'
  who: Hugo
- header: Hugo's background
- line: Yeah, let's start. Before we go into our main topic of data developer relations,
    let's start with your background. Can you tell us about your career journey so
    far?
  sec: 216
  time: '3:36'
  who: Alexey
- line: Yeah, and feel free to stop me at any point. I'm not quite sure what level
    of granularity to go into. But I'll kind of give a bit of background that's relevant
    to what we're talking about today, as well. My background is in scientific research
    in mathematics, then cell biology and physics – biophysics – so, studying the
    physics of the cell. I was doing that, not too far from you, actually, for several
    years, here in Berlin. I was doing this in Dresden. There's a big Max Planck Institute
    for cell biology there, where I did the first half of my postdoc. Ostensibly,
    my job was to do applied mathematical modeling – to model cellular biological
    phenomena. At this point, my colleagues (biologists) were able to collect increasing
    amounts of data up – to millions of rows (and beyond, if they're doing genomics
    and that type of stuff).
  sec: 226
  time: '3:46'
  who: Hugo
- line: At this point, I've done a bunch of programming, but I didn't really have
    a strong statistical data bent to myself. This is over a decade ago now. So it
    became clear that to do my job, it would be a good idea to learn as much as possible
    about what was becoming data science at that point. I started playing around with
    RStudio and then notebooks in IPython. At that point, Jupyter Notebooks didn’t
    exist. So I started to learn all the tools that I needed to analyze and model
    data and cellular biological phenomena. Then my postdoc boss moved to the east
    coast of the US – to Yale University and so I worked there with him for a couple
    of years. In both these jobs... I loved the research, but it became clear to me
    that there are lots of good researchers, but there was a gap at both these places
    in terms of actually teaching these tools to all the biologists and all the scientists.
    I mean, I worked with tenured professors at Yale who really didn't have the computational
    skills to do the science that they needed to – wonderful scientists and experimentalists
    – nor did they really have the time or the bandwidth. The incentive system is
    pretty screwy there, as well.
  sec: 226
  time: '3:46'
  who: Hugo
- line: So I carved out time in the department I was working in order to teach what
    I called “practical data science for researchers and scientists workshops”. At
    that point, I met some young entrepreneurs who had started the company DataCamp.
    They had built out a pretty serious base R curriculum and they were looking for
    someone to come in and build out Python courses and do a bunch of product and
    internal data science stuff and that type of stuff. I was applying for academic
    positions at the time and applying for some industry positions. As it turned out,
    I was able to jump in and start really building up Python courses there. I was
    very fortunate to be able to not only build out courses that I could teach myself,
    but collaborate at that point with what was then Continuum Analytics (now Anaconda,
    of course) to build out things like the first set of pandas and Matplotlib courses
    and to work with Andreas Mueller of Scikit Learn on the first Scikit Learn course.
    So I was really getting a huge amount of insight into the open source world and
    being able to collaborate with a bunch of these really interesting, insightful
    tool builders and practitioners as well. I started doing... we'll get to why I
    did this soon, when we're talking about getting into developer relations and getting
    into developer advocacy.
  sec: 226
  time: '3:46'
  who: Hugo
- line: I started doing a bunch of developer relations advocacy then – a lot of writing,
    speaking, online live coding sessions, and started a podcast called DataFramed,
    which I think some people probably listened to. That was a huge amount of fun,
    once again, getting to do stuff like this – I mean, talking with people who I'm
    interested in about stuff that we're both interested in and having conversations
    with an audience about that. So a lot of community building there. After DataCamp,
    I've been to several places. I was first at a company called Coiled, which is
    a Dask company – Dask is for distributed parallelized compute in Python. I was
    doing a lot of evangelism, developer relations, and marketing stuff there.
  sec: 226
  time: '3:46'
  who: Hugo
- line: More recently, for the past year and a half, although I've been working with
    them for for longer, I'm really excited to be working at Outerbounds, where we're
    working on full-stack machine learning. As we'll get to, I think one of the big
    challenges here, as should be becoming clearer, I think something I love doing
    is helping scientists get access to software tools and education and content that
    helps them to better science. Right? What does that mean in industry now? We're
    trying to tell the productionization story of data science and machine learning
    more and get that out of larger organizations. Meta and Google know how to do
    machine learning at scale. Netflix knows how to do machine learning at scale.
    How do we get that into Mom and Pop ecommerce stores? And how do we get that across
    the board? And what does this full stack look like? And how do we build software
    and education so that scientists can do this in any company and they don't need
    to worry about configuring YAMLs and Kubernetes clusters. How do we build a stack
    of infrastructure that allows scientists to focus on the top of the stack – the
    modeling the data, the things they love, the productionization – without having
    to become the most robust, intense software engineers.
  sec: 226
  time: '3:46'
  who: Hugo
- line: Although, as you and I have discussed, these skills are important as well.
    Also, I've put a link to this in the chat – I host another podcast as well, called
    Vanishing Gradients. The reason behind that was actually, after I did the DataFramed
    podcast at DataCamp, I always wanted to get back into podcasting. It was in between
    jobs that I thought... A lot of my friends work in the space and I was having
    what I thought were a lot of interesting conversations with them, so I thought,
    “Why not record them and put them out there?” So it's really nice. I get to have
    conversations like this with friends and put them out. So definitely check that
    out for those interested.
  sec: 226
  time: '3:46'
  who: Hugo
- line: Google (YouTube) decided that it was spam, so your link did not go through,
    but I just Googled it and posted in the live chat.
  sec: 624
  time: '10:24'
  who: Alexey
- line: Fantastic. It's funny because in my job at Outerbounds, we host Fireside Chats
    around full-stack machine learning and I have noticed that only I as host can
    post links.
  sec: 633
  time: '10:33'
  who: Hugo
- header: Why do tools and the companies that run them have wildly different names
- line: I still don't know how exactly it works. Sometimes people can post links,
    sometimes they can't. Most of the time, they cannot. Only if the host can, which
    I guess makes sense because otherwise people might come and post spam. I'm really
    wondering, Coiled is the company behind Dask, while Outerbounds is the company
    behind Metaflow. Why not just call the company Dask or Metaflow? Why do you come
    up with these names that sound completely unrelated?
  sec: 647
  time: '10:47'
  who: Alexey
- line: That's a good question. I suppose the way I frame it is that other people
    work on these open source projects, right? Metaflow, for example, has 75 historical
    contributors on GitHub, and a bunch of other people still contribute and other
    companies as well. I would say Outerbounds is the company that probably you would
    consider supporting Metaflow a lot, just as Coiled supports Dask. Having said
    that, I think Anaconda still employs a bunch of Dask maintainers as a bunch of
    contributors for Dask work in a variety of other companies as well. I think that's
    actually really important. Because if we think about what open source is – it's
    a pretty broad church. If you think about something like TensorFlow – think about
    the governance of TensorFlow, where it isn't open source in the classical sense
    of how many people get to make decisions. It's very company-backed. So I do think
    it's important to have that distributed.
  sec: 678
  time: '11:18'
  who: Hugo
- line: Also, there's the converse in that, for companies/institutions to adopt open
    source, I think that we want to make sure that a certain number of companies support
    them as well. Definitely before Coiled started, there were companies that,  when
    we were considering Dask versus Spark, like “Well, Spark has more support in the
    industry, from Databricks and that type of stuff.” So we want to just make sure
    that Dask is supported by a handful of places first, as well. So I think there's
    an interplay there. And that speaks to the fact that having these companies can
    actually really support the open source ecosystem.
  sec: 678
  time: '11:18'
  who: Hugo
- line: Okay. Interesting. So it's on purpose that the name of the company and the
    product they work on are not the same. Right,
  sec: 790
  time: '13:10'
  who: Alexey
- line: Yeah, because they are different entities. And Outerbounds, although we support
    Metaflow and work on Metaflow, and have a managed offering as a product and these
    types of things, what we definitely want to help people do is solve machine learning
    and take machine learning from prototype to production and improve that speed
    of iteration there. Whether we do that through Metaflow or not, isn't necessarily
    the primary concern. We happen to be [doing that], currently.
  sec: 797
  time: '13:17'
  who: Hugo
- header: Hugo's other projects beside Metaflow
- line: Do you work on anything else apart from Metaflow? Are there other products?
  sec: 826
  time: '13:46'
  who: Alexey
- line: At the moment, our main product is definitely based around Metaflow, but it
    does interoperate with a variety of different things. So if you're on AWS, we
    make sure that you can have access to all of your resources, all of your data,
    and have that secured in AWS. If you use Kubernetes clusters, we make sure you
    can do that. I think something I showed on the OSS demo spotlight the other day
    was that we integrate with the Argo scheduler, so when you want to push your models
    to production, you can do that using Argo. So we support a huge section of the
    ecosystem.
  sec: 832
  time: '13:52'
  who: Hugo
- header: Transitioning from educator to DevRel
- line: When you were talking about your career journey, that was pretty interesting.
    So you came to develop relations through education. You first noticed that for
    researchers it is difficult to learn about practical data science, so you created
    a bunch of courses there. Then you joined DataCamp and through that, you became
    a developer relations [person].
  sec: 874
  time: '14:34'
  who: Alexey
- line: I'm wondering, how did this transition happen? Was it natural for you, as
    a teacher, as an educator, to go there? How exactly did this happen? How did you
    make the decision that “Okay. Actually, you know what? What I'm doing seems to
    be close to DevRel. Let me do this professionally.”?
  sec: 874
  time: '14:34'
  who: Alexey
- line: Yeah, that's a good question. I suppose one way of thinking about it (and
    this isn't the only way) but DevRel kind of is education, right? Someone who works
    in developer relations, their job is to at least create educational content that
    helps people use your software. So it definitely was natural in that sense. The
    other reason it was natural for me, I think – as I said, a lot of the other things
    I've done, I think there are lots of people who are really good at these things.
    I actually think there are lots of people who could be good at DevRel, we just
    haven't carved out the career paths for them. I suppose it was a differentiator
    for me and I could make more impact then in DevRel than in other positions.
  sec: 917
  time: '15:17'
  who: Hugo
- line: I think the key aspects for those wanting to get into DevRel are, of course,
    to enjoy and be good at the computational side and understand data science and
    machine learning. Although there are things – they say that the best teacher sometimes
    is someone who's just learned what they're teaching. Definitely, if you have a
    background in these things and want to pick things up and teach them, that can
    be useful. But to have a command of the technical, scientific side of things,
    and then the other thing is to be an explainer. When I walk down the street and
    I'm having my morning coffee, and I've done something – my mind naturally gravitates
    to explaining that in my own head, in kind of the most straightforward terms possible.
    I have colleagues and friends who don't operate that way, right?
  sec: 917
  time: '15:17'
  who: Hugo
- line: I know a lot of engineers who just want to build cool products – not just,
    they want to build cool products. They don't want to write blog posts and they
    don't really want to break things down. And that's totally cool. If that's you,
    I wouldn't necessarily get into the DevRel side of things. But if you enjoy explaining
    things, and you enjoy the technical side of things, I definitely think um... I
    think there's a hiring challenge in DevRel, generally. And I think that's going
    to increase.
  sec: 917
  time: '15:17'
  who: Hugo
- line: I think the demand side of the labor market for DevRel is going to grow as
    we get more and more tools. People are like, “Am I going to be replaced by GPT-23
    (or whatever)?” Right? And I've got no idea. But what I can tell you is that working
    in DevRel, I think there's definitely a significant chance of being employable
    for a long time. I'm not saying there's less chance in other fields, but I definitely
    think the pie is growing, if that makes sense.
  sec: 917
  time: '15:17'
  who: Hugo
- header: What is DevRel?
- line: What is actually DevRel? What is it?
  sec: 1083
  time: '18:03'
  who: Alexey
- line: It's a good question. I think the best way to think about it – there are multiple
    terms that fly around. There's developer relations, there's developer advocacy,
    there's evangelism. The way I think about it is – we can think about open source
    or not open source software, it doesn't really matter. It's [about] helping developers
    understand how to use software and why, essentially. In my current job, as I said,
    (and this is something we talked about earlier this week) there are scientists
    who are great on the data and modeling side of things, and they need to understand
    certain things about compute, versioning code, versioning models, about orchestration
    – all of these these types of things. So a DevRel function there would be in the
    name of education, to give them access to the information they need about these
    tools, but also to resources for how to learn it and how to implement it. That
    speaks to the sandbox that I demoed at the Spotlight, as well.
  sec: 1087
  time: '18:07'
  who: Hugo
- line: As we discussed, getting set up with this entire infrastructure stack is days
    of work. So if you can do DevRel in the name of education, but have these tools
    that allow people to spin things up in 10 seconds instead of 10 days, that's incredibly
    useful. Another way to think about it, and this is actually one of the several
    reasons I joined Metaflow and Outerbounds – the co-founders, when I first spoke
    with them, showed me some slides on what they referred to as “the wisdom layer
    of Metaflow”. And Ville Tuulos, who you know, and who is the CEO of Outerbounds,
    and used to run machine learning infrastructure at Netflix when they developed
    Metaflow – Ville said to me, “This software, of course, is incredibly important.
    But the reason we want to hire DevRel immediately is because the wisdom layer
    is not secondary. It's equally important.” And I think recognizing that is key.
  sec: 1087
  time: '18:07'
  who: Hugo
- line: I'll give maybe two other examples. Scikit Learn. I mean, it's wonderful software.
    But I think one of the most important reasons for its huge adoption is its documentation.
    Documentation, of course, is part of DevRel – not only in terms of documenting
    methods and arguments and docstrings and this type of stuff, but giving easily
    accessible SEO-findable examples that people can then use in their day jobs. I
    think the Tidyverse in the R ecosystem is the same way. Tidyverse originally with
    ggplot deployer, several other packages had vignettes – the caret vignettes that
    Max Kuhn developed on the machine learning stuff is absolutely wonderful. So all
    of these roll into DevRel.
  sec: 1087
  time: '18:07'
  who: Hugo
- line: I'll shush in a second. I did want to mention the other thing. I just used
    the term SEO (search engine optimization) and this is actually incredibly important.
    What we're seeing now is that DevRel is related to marketing in some way. Right?
    And the cynical take on this is that developers don't trust marketing, so you
    need to invent a new function called something else. Kinda like... No, it's nothing
    like this, but I was thinking of Edward Bernays, who coined the term “public relations”
    because the term “propaganda” had a bad name. So he coined the term that's propaganda
    for propaganda. But that's the cynical take. What's really happening there, I
    think, is that the tools DevRel needs to get to the right audience are some of
    the same tools marketers do.
  sec: 1087
  time: '18:07'
  who: Hugo
- line: There's a joke for a lot of open source developers that when you search something
    about their package, Stack Overflow comes up first, even though it's answered
    in their documentation, so a lot of the time people will just link to the Stack
    Overflow answer with documentation and spell it out there. So that's to say, in
    DevRel you also – and I'm trying to entice people to think more about DevRel –
    you get to do a bunch of fun stuff. You get to develop content, give talks, chat
    with developers, also fold developer feedback back into software and product,
    and also learn about the internet and search engines and all of this type of fun
    stuff as well.
  sec: 1087
  time: '18:07'
  who: Hugo
- header: DevRel vs Marketing
- line: Yeah, interesting. So it's about education, it's about discoverability, and
    it's about producing content that developers can understand and developers can
    trust. Right? [Hugo agrees] As you said, if it's just somebody from the marketing
    department, then maybe they don't necessarily believe that this person speaks
    the same language as them. Speaking about marketing, I'm curious. Is developer
    relations usually a part of the marketing department or a part of the technical
    department?
  sec: 1372
  time: '22:52'
  who: Alexey
- line: It depends on the organization. I've seen both. I've spent most of my time
    in recent years working in early-stage to middle-stage startups. What's interesting,
    in my two most recent startups is, with high DevRel people before – full-time
    marketers. I think for an early- to medium-stage setup, you can get away with
    having the several people do all the marketing as well. As you scale and grow,
    you're going to want to have a pretty serious marketing team, and you can either
    have some of the developer relations people in there, or in an independent unit
    as well. It depends on how you want to structure things. It is always interesting
    when DevRel reports into the CTO and is as close to engineering as possible.
  sec: 1409
  time: '23:29'
  who: Hugo
- line: In my current company, at Outerbounds, we're pretty non-hierarchical, so I'm
    pretty generative. That's actually the other thing worth worth mentioning. DevRel
    is also not just about creating content yourself out of the abstract, but it's
    leveraging and collaborating with your engineers to see what they can bring to
    the world and lowering the barrier to entry for them. Who's the best person to
    write documentation of a new feature? It's not me, it's the engineer who rebuilt
    the feature, right? But, in collaboration with me, depending on them, perhaps
    we can write something together. Or if they're not into writing at all, maybe
    I'll jump on a call with them like this, talk it out, get a transcript and I draft
    something from that. So it's really fun because you have all these touch points
    internally in a project and also externally, with the developers who use it.
  sec: 1409
  time: '23:29'
  who: Hugo
- header: How DevRel coordinates with developers
- line: Yeah. I think you mentioned that not all developers are really into writing
    blog posts and other things or being in talks. But then, other developers who
    need to use the tools that these developers produced, they need documentation.
    They need to know how to actually use this, and then somebody needs to make this
    happen. Then it's you, it's DevRel. [Hugo agrees]
  sec: 1517
  time: '25:17'
  who: Alexey
- line: DevRel makes sure that even if maybe the developer wrote something, “Is it
    actually understandable? Can I take this piece of documentation and do something
    with this? Or maybe it's completely (or maybe not completely) but there are some
    missing things – there are some areas for improvement, there are some unclear
    parts – that could be improved.” Then you give this feedback to developers, or
    maybe go ahead and just improve these things. [Hugo agrees] Does this sound right?
  sec: 1517
  time: '25:17'
  who: Alexey
- line: Yeah. The other thing worth mentioning is, it's fun because you get to stay
    professionally on top of current trends. Recently we've seen, I suppose what we'd
    call a revolution in generative AI, from last year – all your Stable Diffusions
    and these types of stuff, to all the large language model stuff happening now.
    So when that occurs in a company, in a project, you want to figure out how you
    can support these efforts more generally. And because with Metaflow, we really
    think about how to get machine learning and data science in real world software
    stacks, and in robust, reproducible applications, and of course, all the generative
    AI stuff is really built around proof of concepts and not robust software, it's
    been a lot of fun to start working on that type of stuff. I'll link to a few blog
    posts of how we're thinking about supporting the infrastructure that allows people
    to build all this generative AI stuff. I think your audience will find it interesting.
    So yeah, it keeps you on top of current trends as well, which is cool.
  sec: 1570
  time: '26:10'
  who: Hugo
- header: How DevRel coordinates with marketers
- line: Okay. We already discussed that you, as a DevRel person, work closely with
    the developers who create a product (create the code). How closely do you work
    with marketing? Because what marketers do, in my opinion, (I might be wrong) they
    are usually in charge of different campaigns. They might run ads on Google, they
    might work with communities to advertise something through these communities,
    or they might create an event, and then see how well this event performs.
  sec: 1637
  time: '27:17'
  who: Alexey
- line: So they're not necessarily into the actual content, but rather they make sure
    that this content reaches the right people. So how do you work with these people,
    with marketers? I guess you produce content, but then they make sure that this
    content is discoverable and people find it?
  sec: 1637
  time: '27:17'
  who: Alexey
- line: Absolutely. It's usually an iterative process. There are many, many different
    examples or ways to slice this. I'm thinking, part of a marketing team's job is
    to make sure a company, or a product, or a piece of open source software appears
    in places where people will be looking for it. Right. As it turns out, at the
    moment, search engines are really important for that. You want to make sure that
    when you have a digital marketer, that they're aware of who your ideal customer
    or ideal user is, and they can help you figure out what type of searches they
    make and get you in front of their eyes with relevant stuff. Now, as you've ascertained,
    it's the DevRel team, among other potential people (there are content marketers
    as well) but the DevRel, the technical people who develop content, that digital
    marketers will be able to use in order to get that search engine stuff happening.
  sec: 1694
  time: '28:14'
  who: Hugo
- line: So there's a serious back-and-forth there, where, perhaps the engineering
    team and the DevRel tell the marketers, “These are the types of things we're thinking
    of writing about,” and then the marketers will do their SEO research and come
    back and go, “Okay, this has high search traffic, but we're actually really competitive
    with Google itself for this. So maybe we won't win that. Whereas this has medium
    traffic, but it's something that is super relevant and not a lot of people are
    going for it at the moment.” So it's an ongoing conversation in that sense. And
    I'll definitely say that there are a lot of very good marketers out there, but
    not necessarily a lot of great marketers who understand the technical space –
    who would know what XGBoost is, for example, or the difference between gradient
    boosting and other forms of...
  sec: 1694
  time: '28:14'
  who: Hugo
- line: That's not their job, right?
  sec: 1818
  time: '30:18'
  who: Alexey
- line: Exactly. So the way I think about it is that DevRel is kind of the marketing
    team's best friend, in a lot of ways. The more they can work together, the better
    off. And then at some point, perhaps a project or a company will want to have
    a conference that the marketing team is responsible for putting together. Then
    DevRel will play a significant role in constructing the lay of the land for who
    they invite, what actually happens there, what type of talks there are, whether
    there are panels – this type of stuff, as well.
  sec: 1821
  time: '30:21'
  who: Hugo
- line: Because marketers can organize a conference, but they don't necessarily know
    which content will appeal better to the audience, right? And they need your input
    for that.
  sec: 1860
  time: '31:00'
  who: Alexey
- line: Exactly. But I also want to say that there are some pretty technical marketers
    as well. I've met some wonderful product marketers who's job is to (and they're
    usually from somewhat technical backgrounds) who know how to speak the technical
    talk as well. So I don't want to say, “No marketers are computational,” or anything
    like that. But they're not as easy to find.
  sec: 1870
  time: '31:10'
  who: Hugo
- line: Yeah. We should probably invite one of those folks to our podcast.
  sec: 1893
  time: '31:33'
  who: Alexey
- line: Yeah, absolutely.
  sec: 1899
  time: '31:39'
  who: Hugo
- header: What skills a DevRel needs
- line: But what are the skills that... let's say, I work as a data scientist and
    I am interested in exploring the DevRel space. I think I enjoy writing, and I
    think I enjoy giving talks, and I've heard that being a DevRel is about that.
    So I kind of want to go into that space – into that direction. What kind of skills
    do I need for that?
  sec: 1901
  time: '31:41'
  who: Alexey
- line: Well, I think you have a wonderful skill set, Alexey, for DevRel. Because
    you do it. I mean, the other thing that I probably didn't speak to enough is that
    DevRel is about community building. And this is something you do a huge amount
    of. So it isn't only about one-to-many broadcast mode, and then many-to-one –
    it's about getting all the connections between the community and interacting.
    I think, as I said before, the most important skills are having a base of technical
    skills that you can leverage. There are always things you can learn on the fly,
    as well. A willingness and a strong desire to learn more things.
  sec: 1925
  time: '32:05'
  who: Hugo
- line: And if you're working in data science and machine learning successfully, you
    probably already have that, because things are moving so quickly. So neither of
    these things are really special in this skill set, per se – in this audience.
    A desire and an ability to explain things in simple terms, and to community-build,
    as well. So it’s about enjoying having these kinds of multi-network conversations,
    between engineers and developers and data scientists and people doing machine
    learning, and that type of stuff.
  sec: 1925
  time: '32:05'
  who: Hugo
- line: Okay. So in summary – technical skills. If I already work as a data scientist,
    I got that covered. But then in addition to that, I need to know how to actually
    explain my work. It's not just “Okay, I finished my Jupyter Notebook. I put this
    to Metaflow and productionize and then my job is done.” Then I actually want to
    and am able to explain how these things work (and I enjoy doing this). Then I
    would probably be a good fit for a DevRel position?
  sec: 2009
  time: '33:29'
  who: Alexey
- line: Absolutely. And in a variety of media. Being a relatively good writer, I think,
    is important, as is enjoying going out there, speaking, doing videos, podcasts
    such as this, as well.
  sec: 2043
  time: '34:03'
  who: Hugo
- line: Okay. So was it related to the community-building aspect? Or is it something
    a bit different?
  sec: 2063
  time: '34:23'
  who: Alexey
- line: Yeah, I would say community-building as well. Because what you want to do
    is be able to take information and techniques and methods, and bring them to a
    broader community and get the community discussing, getting feedback from the
    community for the project as well.
  sec: 2069
  time: '34:29'
  who: Hugo
- line: How do I become...? Sorry.
  sec: 2087
  time: '34:47'
  who: Alexey
- line: I was just gonna say, the other thing worth mentioning – and this is always
    a challenge for a lot of data scientists and machine learning engineers who are
    thinking of getting into DevRel. It's not clear in a lot of organizations. Once
    you get into DevRel, you get to do a lot of cool data science and machine learning
    projects, but they're more for content and developer relations, as opposed to
    solving internal business problems. So that's something that you have to give
    up to a certain extent. There's a trade-off there.
  sec: 2090
  time: '34:50'
  who: Hugo
- line: Depending on the organization, there may be a structure which allows you to
    do internal data science as well. But if you're working on the data science team,
    you're also working on the data science team and not the DevRel team, right? There
    can be mixed incentives when you're reporting into two different teams as well.
    So you definitely get to do less impactful internal data science when working
    in DevRel. But as part of that trade-off, you get to do all these fun things we're
    talking about.
  sec: 2090
  time: '34:50'
  who: Hugo
- header: The challenges that come with being an educator
- line: So does that mean that you get less in-depth knowledge into certain things?
    Because when you solve a business problem, there are some problems, some bugs
    or some things don't work, and then you start digging deeper until you figure
    this out. This is how you learn and become proficient in some domain or with some
    library. But as a DevRel, whose focus is on creating educational content, maybe
    you don't necessarily dig that deep?
  sec: 2149
  time: '35:49'
  who: Alexey
- line: Yeah, you still end up dogfooding a lot of things that you're building, though
    in order to get to the point where something works for you and is reproducible.
    You've got to make it reproducible for other people as well. So you can end up
    getting pretty seriously in the weeds.
  sec: 2187
  time: '36:27'
  who: Hugo
- line: It can be even more difficult, right? Reproducibility.
  sec: 2204
  time: '36:44'
  who: Alexey
- line: Yeah, absolutely.
  sec: 2208
  time: '36:48'
  who: Hugo
- line: I remember it's one thing when you do this work – you commit it and it's working
    fine – but it's another thing if you want to actually teach others how you did
    this. Then it's a totally different thing. Then you'll notice, “Wait a minute,
    most of these things are more complex than they should be. How about I try to
    rewrite them?” And then you spend like a week doing this. That's kind of a different
    level of challenge, right?
  sec: 2210
  time: '36:50'
  who: Alexey
- line: Absolutely.
  sec: 2239
  time: '37:19'
  who: Hugo
- header: 'Becoming a good writer: nature vs nurture'
- line: Well, you mentioned that in order to become a good DevRel, you need to be
    a good writer and you also need to be a good speaker. But how do I become a good
    writer if I'm a data scientist? Is it something I'm born with and I either have
    it or don't? Or is it something I can become better at?
  sec: 2241
  time: '37:21'
  who: Alexey
- line: Well, I mean, nature vs nature, right? This is an age-old question. I'm probably
    a Bayesian at heart, so I think framing the conversation around likelihoods is
    the most useful way of thinking about it. Some people are naturally good at writing,
    explaining, and that type of stuff. But that's also because people enjoy it more,
    so people have done more of it and that type of stuff. But I think anyone... where
    there's a will, there's a way, as we say. So anyone who wants to become a good
    writer, can. I do think the way you do it is by doing it. Of course, there are
    courses you can take, but I think that by actually trying to explain things, trying
    to write things down – if you get some form of writer's block, you can record
    yourself talking through something, then get a transcript of that. These types
    of things. Or try to explain it to someone and get a transcript of that. I think
    one of the best ways to become a writer (to improve your writing skills) – well,
    there are two ways.
  sec: 2264
  time: '37:44'
  who: Hugo
- line: One is to collaborate with other people and with Google Docs, or whatever
    it is these days – Notion. Pick your tool, right? Collaborative writing is in
    a wonderful state. The other is by reading more and, I think, noticing what you
    like about what you're reading and what you're not noticing. When you read something
    and you don't understand something, I think a lot of us have a tendency to think
    that's our fault. I'll be like, “Am I too dumb to understand?” And then I go,
    “No, actually, I'm dumb in some ways, but not in this way. And this probably isn't
    written... they haven't explained it well,” and by trying to figure out what they
    haven't necessarily explained well and then how I'd do it differently.
  sec: 2264
  time: '37:44'
  who: Hugo
- line: Those types of things, I think, are incredibly important. But I definitely
    think through writing, you become a good writer. And it is a huge differentiator,
    man. I was very surprised when I started working in cell biology. The number of
    incredible research scientists (and I won't name any names or institutions) but
    the number of really amazing scientists who don't know how to write properly.
    I mean, maybe because their minds are on other things as well, but they all share
    what they call “final drafts” with things where the sentences aren't complete.
    So I think it is a really strong differentiator there as well.
  sec: 2264
  time: '37:44'
  who: Hugo
- line: What helped me is having an editor who would point out, “Hey, look. This paragraph
    is completely not understandable. I tried to read it three times. I still don't
    get it. Let's work on this paragraph to really understand what you meant here
    and let's try to write in simple sentences without all this passive voice, long
    constructions, and so on.” So that was helpful. What I did later is work with
    data scientists to actually kind of do the same thing. When they submit a draft
    say, “Okay, look. This sentence is a bit confusing. Can we make it clearer?” That
    is very helpful for both of you. Right?
  sec: 2417
  time: '40:17'
  who: Alexey
- line: At the end, you make sure that the readers actually understand. One thing
    you mentioned about the writer's block. I used to have it until ChatGPT came out.
    Now it's much easier to get started. I just ask it, “Hey, I want to write something
    about that. Can you give me an outline?” Then it gives me an outline and then
    I'm like, “Okay. Now I already have some things. They are not necessarily good,
    but I can iterate on these things. But I have something.” So then it's very helpful.
    I never tried speaking to myself and recording it and then transcribing. I think
    it's a very good idea.
  sec: 2417
  time: '40:17'
  who: Alexey
- line: Yeah. I journal a lot as well. I do that with journaling. Sometimes when I'm
    just too tired to write, I'll just... I think I've got the idea from Twin Peaks.
    I don't know if anyone's seen that TV show. Dale Cooper, the Kyle MacLachlan character,
    dictates his diary into a dictaphone in the 90s.
  sec: 2506
  time: '41:46'
  who: Hugo
- line: Well, I think now with all these tools from OpenAI – you can just dictate
    something to your phone, then have Whisper transcribe it and then have GPT summarize
    it into an article. So then you already have a draft to start with, and then you
    start working on it, reworking it with your own style, with your own extra content.
    Yes, it's amazing. I actually recently used Whisper. I attended a parents' evening
    in school. It was in German, and my German is very far from perfect. I did not
    understand everything, but I recorded this. I put this into Whisper and I took
    the output of Whisper and put it to GPT, which just summarized everything. I thought,
    “Wow!” Then I asked it to translate from German to English. That was also cool.
  sec: 2523
  time: '42:03'
  who: Alexey
- line: Amazing. That's so cool. I just noticed Johanna had a couple of questions
    in the chat that are really relevant to how to approach writing.
  sec: 2573
  time: '42:53'
  who: Hugo
- line: Let me read them.
  sec: 2586
  time: '43:06'
  who: Alexey
- line: Oh, yes. Of course.
  sec: 2587
  time: '43:07'
  who: Hugo
- line: Yeah. That's the Johanna who helps us write questions.
  sec: 2589
  time: '43:09'
  who: Alexey
- line: In Melbourne, right?
  sec: 2593
  time: '43:13'
  who: Hugo
- header: Hugo's approach to writing and suggestions
- line: Yeah. And she's doing this now online. Thanks, Johanna. The question Johanna
    has is, “How do you approach creating a piece of writing or tutorial? Do you start
    with structure or do you have some other approach?
  sec: 2594
  time: '43:14'
  who: Alexey
- line: Structure is pretty early, depending on whether I'm collaborating with people
    or doing it myself. Sometimes, by myself, I'll just start writing. I have an idea
    and start writing. I think when collaborating with people, getting a structure
    down beforehand is very important just to align. You want to make sure you're
    “rowing in the same direction”. But I think before structure is figuring out who
    your target audience is, and then what your goals are. Let's say I wanted to write
    something about using Whisper with Metaflow – how to build production software
    that transcribes audio, let's say, leveraging Kubernetes clusters. Something like
    that.
  sec: 2607
  time: '43:27'
  who: Hugo
- line: I could start drafting that or write a structure, but the structure might
    be incredibly different based on whether I'm writing it for a data scientist or
    a platform engineer. If I'm writing for a platform engineer, maybe they want to
    know about how to configure all the Kubernetes clusters in order for the data
    scientists to be able to do their work as quickly as possible. Whereas if I'm
    writing it for a data scientist or a machine learning engineer, perhaps we're
    abstracting over all that information. So I think that is incredibly important.
  sec: 2607
  time: '43:27'
  who: Hugo
- line: In terms of goals, I think, for a company or an open source project, perhaps
    you want to start asking questions before writing a structure, such as, “Am I
    writing this to just build awareness of this open source software? Or am I doing
    it in order to support people who already use it? Or am I doing it for credibility
    in the space? Or am I doing it to generate excitement?” And so all of these types
    of different questions are important to figure out what your goal is, what your
    target audience is, and then start structuring it, and then move through it.
  sec: 2607
  time: '43:27'
  who: Hugo
- line: One thing I sometimes do when I write a structure is essentially write what
    the TLDR should look like beforehand and then write down what the headings are
    (what the h2s are). Then I break it up and then start filling things out. And
    if you're collaborating, then you can figure out who wants to write which part
    and then edit for each other, and that type of stuff. Those are the kind of general
    ways that I've started to think about it.
  sec: 2607
  time: '43:27'
  who: Hugo
- header: Establishing a goal for your content
- line: How do you understand what kind of goal you have? Maybe somebody comes to
    you and says, “Hey, we don't have any posts in our blog. Let's create blog posts.”
    And then you're like “Okay, let's create.” Then you think, “Okay. What is actually
    my goal?”
  sec: 2769
  time: '46:09'
  who: Alexey
- line: That's a great question. The way I think about that is – blog posts are there
    to serve goals of projects or companies and the audience – whoever the audience
    may be. So if an open source project wants to start a blog – if they don't have
    a large audience yet, I suppose the first thing they want to do is develop awareness.
    That's why they're doing this blog. As opposed to, let's say that they want blog
    posts because there are too many issues on the issue tracker, which are solved,
    but they need blog posts to point people to in order to say, “Hey, this is the
    solution to it.” Then that's a different thing. I would even push back and say,
    “You shouldn't create a blog out of a vacuum – for no reason.” If you're creating
    content, there is a goal embedded in your logic, so it's my job to figure out
    what your goal is.
  sec: 2793
  time: '46:33'
  who: Hugo
- line: A very different example is – I speak with a lot of founders who want to find
    things out about early stage DevRel, and a question that founders of companies
    (venture-backed, seed round, series A companies) that are building developer tools
    almost always ask is, “If I don't have one already, should we have an open source
    offering between what already exists and our product?” And my question is, “Why
    do you want to do that?” And a lot of the time they say, “It's for community building.”
    And my response to that is, “Well, that's an option then. But there are other
    ways to build community as well.” So once we get back to the goal, maybe writing
    blog posts isn't the way to solve your business problem or what your project needs
    at that point. So root causes the desire, and then generatively thinking through
    the potential options. Blog posts will usually form part of it, but then you've
    got that goal as part of that process as well.
  sec: 2793
  time: '46:33'
  who: Hugo
- header: Choosing a form of media for your content
- line: And speaking of that. If your goal is building awareness, then you can do
    it through an article, through a conference talk, or through a YouTube video,
    or through 1000 other ways. How do you actually select the right medium? If the
    company comes to you and says, “Hey, write a blog post for us?” Should you challenge
    that and say, “Maybe for this, you should just do a conference talk because there
    will be 1000 or 2000 developers watching it. Maybe you should do that instead
    of an article.”?
  sec: 2923
  time: '48:43'
  who: Alexey
- line: Yeah. I think, not to seem too business-y about it, but it's just a shorthand.
    I mean, you look at the return on investment – the ROI. You want several strategies.
    You want to make hypotheses, and then do experiments around those hypotheses and
    then figure out if they worked or not, right. The truth is, because search engines
    have such high ROI, you are going to want to do blog posts that are indexable
    by Google (and Bing these days, maybe) whatever it is. But conference talks are
    incredibly important. I think, also, low hanging fruit of organizing meetups and
    that type of stuff in terms of community building and developing awareness or
    sponsoring meetups?
  sec: 2959
  time: '49:19'
  who: Hugo
- line: It's a good question now, when returning to a lot of in-person conferences
    and that type of stuff, whether you want to go and do in-person conferences. Because
    let's say you fly across the country. Let's say you're in the US and you live
    on the West Coast, going to a conference on the East Coast. In the end, that's
    days of travel and hotels and that type of stuff – is that as impactful as doing
    a set of virtual conferences? You can do that in an afternoon. So thinking through
    those things is super important. I do think there's... and this is one of the
    things that's unquantifiable – what happens when you're in a room with people,
    and the conversations that happen then. Just having a coffee with someone and
    those types of things. The hallway track at in-person conferences is so important.
    So I think there is value there, but it's not necessarily as quantifiable, which
    is tough.
  sec: 2959
  time: '49:19'
  who: Hugo
- line: Yeah. For me, personally, that's the most interesting part of the conference
    – not the actual talk, but what happens before and after. All these hallway conversations.
  sec: 3062
  time: '51:02'
  who: Alexey
- line: Yeah. I always wondered whether we could just... ideally, we could just remove
    all the talks, right?
  sec: 3074
  time: '51:14'
  who: Hugo
- line: Yeah. Like that would be enough.
  sec: 3080
  time: '51:20'
  who: Alexey
- line: Then no one would go to the conference.
  sec: 3081
  time: '51:21'
  who: Hugo
- line: '[laughs]  Right.'
  sec: 3083
  time: '51:23'
  who: Alexey
- line: Yeah. You could say people watch them beforehand or watch them after, or something
    like that. But it's almost an excuse. It's a proxy to get people together, even
    though everyone knows that's not the reason they're there. Right? But if you didn't
    have it, they wouldn't travel.
  sec: 3085
  time: '51:25'
  who: Hugo
- header: Is DevRel intercompany or intracompany?
- line: Yeah, right. I understand. Well, I see that we have a few questions. One question
    from Ella is about the DevRel role and whether it's intercompany or intracompany.
    Is it somebody who speaks more outside or within the company, or is it both?
  sec: 3102
  time: '51:42'
  who: Alexey
- line: That's such a good question. It should be both. At the moment, where I work,
    a lot of it is external. That's because internally, we're relatively small. Internally,
    everyone knows what's going on – they have a lot of domain expertise, for the
    most part. Whereas when you grow to a certain size and you start hiring a marketing
    team and a sales team, DevRel actually has an incredibly important function in
    getting resources internally to get everyone up to speed with what the company
    does and what they think. As DevRel, if you can educate your sales team, your
    account executives and business development representatives, and all of these
    different roles – if you can educate them on the software and product even more
    so that they can talk the talk, even if they can't walk the walk, there are huge,
    huge returns there. So I think it's both, but it's dependent on the size of the
    company.
  sec: 3124
  time: '52:04'
  who: Hugo
- line: The other thing worth mentioning is that it's between companies as well. Because
    of the state of full-stack machine learning and that essentially what's required
    at the moment, and what's best practices, is a suite of interoperable best-of-breed
    tools as opposed to all-in-one platforms – at Metaflow, we interoperate with a
    bunch of experiment trackers such as Weights and Biases and Comet. So I get to
    work with these great people. I did a fireside chat yesterday with the head of
    product and a co-founder at Tabular, who work on Iceberg, which is out of Netflix
    as well – just like Metaflow. We were working on some blog post showing how Tabular
    can work with Metaflow to do really high throughput machine learning from there
    – from Parquet through to Iceberg, through to Metaflow. So it's really, really
    fun to work with a variety of different companies in the space as well.
  sec: 3124
  time: '52:04'
  who: Hugo
- line: So it's external, internal, and intercompany. External could be – you work
    with other companies, or external could be you where you educate developers, right?
    So it's both.
  sec: 3258
  time: '54:18'
  who: Alexey
- line: Exactly. The other thing worth mentioning is that, at a company that's 10
    to 20 people, you end up doing a variety of different things. But as a company
    grows, people become more specialized, right? For better or for worse. Becoming
    increasingly specialized... I get bored easily, so I love doing a variety of different
    things, so maybe that's why I'm attracted towards early- to middle-stage startups.
  sec: 3271
  time: '54:31'
  who: Hugo
- line: The other thing that I didn't mention, and it's not necessarily part of the
    skill set for DevRel, you don't need anything major, but start working on a portfolio.
    Make sure your GitHub repository is looking nice. Write some blog posts and maybe
    publish them on Towards Data Science. Go give a talk at a local meetup before
    proposing something for a conference. Find some of the cool work you're doing
    internally, wherever you work, and try to bring that to the world. See how it
    feels, as well.
  sec: 3271
  time: '54:31'
  who: Hugo
- line: Experiment with your career. Maybe you start giving talks and you're like,
    “I don't really enjoy that.” But you enjoy all the other parts of DevRel. And
    that means if you're interested in applying for a DevRel position, you can say,
    “Hey, I don't really enjoy giving talks that much., but this is what I can offer.”
    So experiment with what works for you.
  sec: 3271
  time: '54:31'
  who: Hugo
- line: Maybe now I add a shameless plug. If any of you listening are a data scientist
    or ML engineer or data engineer, and you're working on solving some business problem,
    and you want to talk about that, there is a meetup – our meetup – where you can
    do this. So reach out.
  sec: 3353
  time: '55:53'
  who: Alexey
- header: The Vanishing Gradients podcast
- line: Well, you also have a podcast. We still have 3 minutes. Maybe you can tell
    us about that podcast before we finish?
  sec: 3372
  time: '56:12'
  who: Alexey
- line: This was actually an idea that I had when I was building a lot of courses
    and technical content for developers. There isn't necessarily a lot of room when
    developing this stuff for long format conversations around what the industry actually
    looks like on the ground. And because a lot of my friends, as I said, a lot of
    my colleagues, work in the space doing a lot of interesting stuff, I have a lot
    of these conversations all the time. There are a lot of challenges in this space
    that aren't obvious from when you look at KDnuggets, or go to the Open Data Science
    conference or PyData or look at Towards Data Science. So I wanted to have a space
    for me and like-minded people to have longer conversations. It is pretty across
    the board.
  sec: 3382
  time: '56:22'
  who: Hugo
- line: It's called Vanishing Gradients, and it's on whatever app you use. I think
    it should be. If it isn't, please let me know. But  I've had people from T-Mobile,
    from Pfizer and Novartis, data scientists from Twitter and Reddit, Facebook –
    so a number of different places. Each episode is kind of themed in some way, as
    this podcast is. But I suppose if you enjoyed this conversation, and you want
    to know what happens when the tables are turned, when I'm interviewing someone
    else, you can really get a sense of what the space looks like on the ground as
    well. I'd really welcome your feedback on it – if it resonates or what you'd like
    to hear more of, also. Its URL we've included, but it's vanishinggradients.fireside.fm.
  sec: 3382
  time: '56:22'
  who: Hugo
- line: Okay then. We will make sure to include these links in the show notes, in
    the description. So if you listen to this podcast in recording, you will find
    them.
  sec: 3490
  time: '58:10'
  who: Alexey
- header: Finding Hugo online
- line: What's the best way to find you?
  sec: 3503
  time: '58:23'
  who: Alexey
- line: On LinkedIn or Twitter. It's Hugo Bowne-Anderson, of course on LinkedIn, and
    it's @hugobowne. The other place, if you're interested, we can share the link
    as well – if you're interested in the full-stack machine learning stuff that we're
    doing at Outerbounds, we've got a Slack where you can come and chat with us as
    well. And that's slack.outerbounds.co. We'll include that in the show notes as
    well.
  sec: 3506
  time: '58:26'
  who: Hugo
- line: CO not COM.
  sec: 3531
  time: '58:51'
  who: Alexey
- line: Yes, exactly.
  sec: 3534
  time: '58:54'
  who: Hugo
- line: Yeah, I would put com, usually. Okay, I think that's all we have time for
    today. Thanks, everyone, for joining us today. Thanks a lot to you, Hugo, personally,
    for sharing all your experience with us.
  sec: 3536
  time: '58:56'
  who: Alexey
- line: Well, thank you, Alexey. Thank you, everyone, for joining. It was really great
    to do it. It's the weekend now for me. It's 7 pm on Friday.
  sec: 3556
  time: '59:16'
  who: Hugo
- line: Well, have a nice weekend. And for those who are not in Australia, have a
    nice Friday, and then a great weekend.
  sec: 3565
  time: '59:25'
  who: Alexey
description: 'Master Metaflow, DevRel and full-stack ML: demo, AWS/Kubernetes integrations,
  open-source governance and career tips to build reproducible ML pipelines.'
---

Links:

* [Hugo's personal page](http://hugobowne.github.io/){:target="_blank"}
* [Vanishing Gradients](https://vanishinggradients.fireside.fm/){:target="_blank"}
* [MLOps and DevOps: Why Data Makes It Different](https://www.oreilly.com/radar/mlops-and-devops-why-data-makes-it-different/){:target="_blank"}
