---
episode: 6
guests:
- aleksandrkim
ids:
  anchor: datatalksclub/episodes/How-to-Build-AI-that-actually-Ships-in-Production---Aleksandr-Kim-e3l6hme
  youtube: PosCx_4fwt0
image: images/podcast/s24e07-how-to-build-ai-that-actually-ships-in-production.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/How-to-Build-AI-that-actually-Ships-in-Production---Aleksandr-Kim-e3l6hme
  apple: https://podcasts.apple.com/us/podcast/how-to-build-ai-that-actually-ships-in-production-aleksandr/id1541710331?i=1000775367989
  spotify: https://open.spotify.com/episode/1kwtGLI6dOq2HgKzJmLMkw?si=e831b4b1072e4d78
  youtube: https://www.youtube.com/watch?v=PosCx_4fwt0
season: 24
short: How to Build AI That Actually Ships in Production
title: How to Build AI That Actually Ships in Production
transcript:
- header: AI Engineering Production and Scalability
- line: Today we are going to talk about AI engineering and what it takes to build
    AI in production along with all the glamorous work behind this. We have a special
    guest today named Aleksandr Kim. Aleksandr is a senior data scientist at Intuit.
    He is based in London doing what people usually describe as AI engineering. This
    is an overloaded term.
  sec: 0
  time: 0:00
  who: Alexey
- line: Although it seems in the industry we are slowly converging to some agreement
    on what AI engineering is maybe this is something we can talk about today too.
    He is doing exactly that he is doing AI engineering which means building AI powered
    features in production at scale. He has experience in banking cyber security retail
    and fintech across many companies. It is really nice to have you here Aleksandr.
    Welcome.
  sec: 28
  time: 0:28
  who: Alexey
- line: Thanks for the intro. Thanks for having me.
  sec: 57
  time: 0:57
  who: Aleksandr
- line: Usually the first question I ask is to tell us about your career journey.
    How did you get from Kabar to London being an AI engineer?
  sec: 65
  time: '1:05'
  who: Alexey
- line: That was a long story. I will start with the professional parts. I started
    as an analyst but then quickly moved to data science. I was a data scientist an
    ML engineering team lead and then back to IC at Intuit as a senior data scientist.
    I worked on different projects.
  sec: 77
  time: '1:17'
  who: Aleksandr
- line: For example in 2019 or in 2020 I worked at a cyber security company. I delivered
    a transformer model to production. I was very proud of this engineering achievement.
    Delivering a fine tuned BERT model to production back then was a really great
    project. It was not probably the main thing in that project.
  sec: 105
  time: '1:45'
  who: Aleksandr
- line: Probably the main thing was the actual alignment of ML metrics and business
    outcomes. I was proud of that engineering.
  sec: 144
  time: '2:24'
  who: Aleksandr
- line: We would probably call it an ML engineer today. Do you agree?
  sec: 152
  time: '2:32'
  who: Alexey
- line: I was called a data scientist back then. Now I work on totally different projects
    and use totally different things. For example I build an AI automation platform.
    The tools are different but the principles are probably the same. The main thing
    is not about models it is about solving real issues and delivering some business
    improvements.
  sec: 158
  time: '2:38'
  who: Aleksandr
- line: Yes. You mentioned that you are very proud of this achievement of bringing
    a fine tuned BERT into production. For those who do not have the background in
    these things it is probably hard to appreciate the complexity. I do not want to
    make it the main topic of this discussion today but I am also curious to know
    why you consider this such an achievement. What is very complex about this?
  sec: 183
  time: '3:03'
  who: Alexey
- line: Maybe you can tell us more about this.
  sec: 220
  time: '3:40'
  who: Alexey
- line: Back then the classical approach for solving NLP problems in machine learning
    was bag of words or TF IDF plus logistic regression. Of course in that project
    I tried this approach as well to have some baseline. The BERT model which was
    very popular back then was only two years old. The article Attention is All You
    Need was very cool personally to implement something from articles that was state
    of the art back then.
  sec: 227
  time: '3:47'
  who: Aleksandr
- line: I was proud because of the engineering challenges since it was not just training
    one model but aggregating data. I liked the fact that how our data was stored
    and originated was similar to the data used for training of the BERT model. For
    example pairwise sentence classification.
  sec: 281
  time: '4:41'
  who: Aleksandr
- line: In customer support we also had pairs of sentences from the customer and the
    final category written by the customer engineers. BERT was trained for the same
    data structure. I collected data and fine tuned the BERT model after researching
    how to do it back then since we had no AI to write it for us. Then I wrapped it
    into a Docker container built an ML service and it was implemented into our pipelines.
  sec: 308
  time: '5:08'
  who: Aleksandr
- line: Interesting. What do you do these days? The reason I know about Intuit is
    because I use Mailchimp and Intuit acquired Mailchimp a few years ago. This is
    when I became aware of Intuit. I heard the name of course but I had no idea what
    the company is actually doing.
  sec: 359
  time: '5:59'
  who: Alexey
- header: Intuit Ecosystem and QuickBooks Products
- line: Maybe you can tell us more about this.
  sec: 372
  time: '6:12'
  who: Alexey
- line: It is a big financial company with a couple products mainly for the US market.
    If you work there or pay taxes there you may know about TurboTax or QuickBooks.
    It is an application for businesses to do accounting tax filing and so on. It
    is very similar to ERP systems like 1C which is a Russian alternative.
  sec: 383
  time: '6:23'
  who: Aleksandr
- line: This is what Intuit is doing. Why Mailchimp though I do not know. It seems
    very unrelated to the main business. Is that correct?
  sec: 424
  time: '7:04'
  who: Alexey
- line: Actually it is not because initially Intuit was solving taxes. Then it was
    solving taxes for businesses followed by solving other things for businesses.
    Sending emails and getting new customers is also a very important part of your
    business. Intuit decided to build a platform to add more features to your overall
    ecosystem now.
  sec: 432
  time: '7:12'
  who: Aleksandr
- line: I forgot to mention that usually at the beginning of the episode I share a
    link to ask questions. It took us some time to get started with this podcast interview.
    If you have any questions just ask them in the live chat. I will be monitoring
    them so we can go back to our discussion Aleksandr about what you do at Intuit.
    Thanks for telling me what Intuit is actually doing.
  sec: 467
  time: '7:47'
  who: Alexey
- line: I have heard about TurboTax and QuickBooks. I never used them but I just knew
    about the services without having any idea it is Intuit. What do you personally
    do? What do you work on? Just to have a bit of understanding what you are working
    on to the extent you can talk about this.
  sec: 492
  time: '8:12'
  who: Alexey
- line: When I joined Intuit I worked on platform tasks. About two years ago I moved
    to London and joined the QuickBooks product team. I worked on AI agents that face
    customers with features that help you find customers easier or prepare your taxes.
  sec: 510
  time: '8:30'
  who: Aleksandr
- line: Nowadays I am working on an AI verification system. This system allows everyone
    to get the same results from AI if they ask the same question. The typical scenario
    when you connect your data to AI and ask some question is it gives you some plausible
    numbers which have no relation to real business. We are building this golden knowledge
    base with standards with examples of how analytics actually work at the company.
    Everyone asking about conversion rate for example can get the same numbers.
  sec: 541
  time: '9:01'
  who: Aleksandr
- line: Maybe I misheard you but you said people build agents that do not necessarily
    have relation to real business. This could be a problem. I think I have a quote
    here in the document that we prepared that says the model is rarely the win. I
    do not know maybe it is related. You also mentioned when we were talking about
    the BERT model that while BERT was a very interesting engineering challenge it
    was not the only challenge.
  sec: 589
  time: '9:49'
  who: Alexey
- line: The other challenge was how this BERT model translates to business metrics.
    I think this is all connected. Maybe you can tell us how we can have this connection
    to real business where we look for it and why it is important to actually have
    it.
  sec: 620
  time: '10:20'
  who: Alexey
- line: That is a good question. It is my opinion that the main thing is about solving
    the right problem. It does not matter how sophisticated your model is if you apply
    it to a wrong problem. In that project with the BERT model the initial problem
    and task was to classify 200 support categories. The stakeholders goal was to
    increase automation rate.
  sec: 639
  time: '10:39'
  who: Aleksandr
- line: Their metric was first contact resolution rate. The funny thing was that only
    about twenty categories were actionable. The task was to classify 200 categories
    but only twenty of them were categories we were able to automate. They actually
    did not care about the rest of the categories. ML performance there was not important
    because it did not lead to any automation at all.
  sec: 682
  time: '11:22'
  who: Aleksandr
- line: Before contacting our team they had some previous data science experience
    where they saw great ML metrics and zero business impact. I reframed the problem.
    I suggested to classify only twenty categories plus one other category. That was
    one thing alongside the alignment of metrics. Their metric was automation rate
    where automation was applied only if the model was confident enough.
  sec: 710
  time: '11:50'
  who: Aleksandr
- header: Aligning ML Metrics with Business Outcomes
- line: We together reviewed predictions of the model with its confidence probability
    scores and we selected a threshold where we were satisfied. The business metric
    was automation rate but the ML metric was conditional recall where precision was
    high enough above the threshold that we selected together with the stakeholder.
    Instead of optimizing some pure precision or recall or some fancy F1 metric that
    made no sense to the business we optimized a slightly more complicated conditional
    recall. That metric made total sense to the business. After that alignment we
    managed to iterate more and we managed to get some actual results and saved about
    twenty percent of support costs.
  sec: 737
  time: '12:17'
  who: Aleksandr
- line: Which was great.
  sec: 818
  time: '13:38'
  who: Aleksandr
- line: How does it translate to this work being more ML engineering work. I really
    like your quote that the state was great ML metrics with zero real business impact
    because this unfortunately can happen. The approach is to tune the ML metric you
    have to the actual business problem which is great. How does this translate to
    AI to this AI engineering work we do? Do you see similar patterns in AI engineering
    because the work is slightly different.
  sec: 825
  time: '13:45'
  who: Alexey
- line: You are fine tuning BERT and sending the requests to an open API or whatever
    API you use. Maybe it is an internal model but at the end you do not necessarily
    have control over the model. How do you choose the metrics and which metrics do
    you choose especially when it is an agent like a chatbot. There are tons of metrics
    that we as AI engineers may track like accuracy metrics. Do these metrics translate
    to business impact?
  sec: 854
  time: '14:14'
  who: Alexey
- line: I am curious to know what your perspective is on these things and what your
    experience is with these things.
  sec: 885
  time: '14:45'
  who: Alexey
- line: You are right that tools changed and problems changed a lot. Things that were
    not possible a year ago are now easily solvable with AI but probably the approaches
    or the mindset is not changing a lot. I have a story to back this idea. I had
    a vague task from our leadership to build a chatbot connected to the data to make
    data more accessible. I was doing two things in parallel building POCs and conducting
    customer interviews.
  sec: 891
  time: '14:51'
  who: Aleksandr
- line: I quickly figured out that the chatbot was only a nice to have feature and
    the actual pain point was about a lack of automation. Analysts were spending a
    lot of time to go through different dashboards to aggregate data on different
    levels aggregate trends and present it as a summary to our international leadership.
    As a result our leadership was making decisions on Tuesday based on data from
    the last week. The actual pain point was a lack of automation. I pivoted from
    building a chatbot which is a very long and complex thing and I pivoted to automation.
  sec: 950
  time: '15:50'
  who: Aleksandr
- line: Now we have a system that aggregates raw data summarizes it and sends actionable
    insights directly to Slack channels with our leadership. It saves us thirty hours
    on an executive level and lots of time for the analysts.
  sec: 1007
  time: '16:47'
  who: Aleksandr
- line: Is this how you track the success of this project by how much time it saves?
  sec: 1026
  time: '17:06'
  who: Alexey
- line: Yes. There are two things that we usually measure with AI projects. Feedback
    and actual engagement. Feedback is a good thing but it is not always honest. Feedback
    is a plus one minus one thing or just reviews from customers.
  sec: 1033
  time: '17:13'
  who: Aleksandr
- line: Often it is not complete or they ignore it.
  sec: 1061
  time: '17:41'
  who: Aleksandr
- line: The only thing that matters is whether they actually use or maybe not the
    only thing but the thing you want to optimize is whether they actually use this
    tool or not. Is that correct?
  sec: 1067
  time: '17:47'
  who: Alexey
- line: Yes.
  sec: 1080
  time: '18:00'
  who: Aleksandr
- line: How do you measure that?
  sec: 1080
  time: '18:00'
  who: Alexey
- line: Through engagement rate. In different scenarios it is a different thing. For
    example if it is a customer facing app we measure whether people actually open
    that tab if they send requests through that particular experience.
  sec: 1080
  time: '18:00'
  who: Aleksandr
- line: In your case the customers are internal customers or the customers of Intuit.
  sec: 1099
  time: '18:19'
  who: Alexey
- line: There were a couple projects with external customers but my recent projects
    are mostly about internal customers like our leadership or just my colleagues
    and other teams.
  sec: 1104
  time: '18:24'
  who: Aleksandr
- header: AI Engineers Conducting Customer Interviews
- line: What you effectively do is you help analysts to offload some work from them
    to the agents. You also help the management by giving them the insights they need.
    The analysts have time to do other things and then for the management they get
    fresh data. That is cool. It started with a request to build us a chatbot.
  sec: 1132
  time: '18:52'
  who: Alexey
- line: Yes.
  sec: 1149
  time: '19:09'
  who: Aleksandr
- line: Now it sends data to Slack.
  sec: 1149
  time: '19:09'
  who: Alexey
- line: Yes. There is no chatbot yet.
  sec: 1156
  time: '19:16'
  who: Aleksandr
- line: No chatbot. What you described is you started building a POC and at the same
    time you started conducting customer interviews. Is this a typical job for an
    AI engineer to do these kind of things?
  sec: 1156
  time: '19:16'
  who: Alexey
- line: I am not sure about all AI engineers.
  sec: 1170
  time: '19:30'
  who: Aleksandr
- line: Do you think all AI engineers or maybe all engineers in general should be
    able to do this kind of thing?
  sec: 1177
  time: '19:37'
  who: Alexey
- line: Customer interviews yes one hundred percent. I was doing it when I had different
    labels even before in the pre AI era. It is very important to understand.
  sec: 1184
  time: '19:44'
  who: Aleksandr
- line: I think this kind of gives you a competitive edge that analysts are closer
    to business than engineers in my opinion.
  sec: 1208
  time: '20:08'
  who: Alexey
- line: To be honest I have never thought about it. I quickly switched from analytics
    to data science because the things that were interesting for me in that analytical
    role were not about analytics. I was building a Python service to parse prices
    from websites and build a matching model to predict our own prices to estimate
    our stock unit prices for financial reports. It was related to financial analytics
    but it was not a typical task there. Then I moved to data science but I always
    worked closely with analysts and you are right they understand business better.
  sec: 1215
  time: '20:15'
  who: Aleksandr
- line: It is very convenient to have them explain nuances and all the details and
    what is the actual issue with the business.
  sec: 1270
  time: '21:10'
  who: Aleksandr
- line: I think typically if I take at least the setup of companies where I worked
    typically there is this product manager role who is the connection between the
    business and the engineering side of things. Or between product and engineering.
    Product managers would translate whatever business requirement into something
    that engineers can implement. Is this similar to setups where you worked or work
    right now? Do you have product managers?
  sec: 1283
  time: '21:23'
  who: Alexey
- line: Yes we do. Almost in every company I worked engineers and data scientists
    were participating in customer interviews. It is a very good practice I think.
  sec: 1309
  time: '21:49'
  who: Aleksandr
- line: I think it is important to talk to real people and to see how they actually
    use your products because engineers and customers have a totally different background
    and totally different understanding of things. The definition of AI is very different
    and probably customers do not care about AI they care about things that they work
    with. They want to reduce pain and accelerate things. If you sell something like
    a new AI feature they actually get more pain because of needs to learn new things.
    They do not want to learn these things they want to optimize the work.
  sec: 1328
  time: '22:08'
  who: Alexey
- line: I noticed this strange trend that after ChatGPT appeared maybe a year or two
    after that all the companies started to just add AI to their product. You buy
    a phone and all of a sudden there is AI built in. Why do I need that? I just want
    to do usual things I want to do with my phone and if I want AI I install ChatGPT.
    That was weird to me that everyone was just trying to stick this AI sticker to
    their products.
  sec: 1376
  time: '22:56'
  who: Alexey
- line: Unfortunately it was not only an external thing. It worked in the enterprise
    internally as well. Every product project had AI in the title and AI had a very
    big weight.
  sec: 1409
  time: '23:29'
  who: Aleksandr
- line: Let us talk about these customer interviews. How do you actually have them?
    Imagine a situation where a manager comes to me saying I want you to build a chatbot
    for that and you start building a chatbot. How do you go about actually talking
    to your users? Is there an algorithm that you follow for that?
  sec: 1430
  time: '23:50'
  who: Alexey
- line: There is for external customers. We have special people who contact our customers
    and ask them if they want to participate in the customer interviews. If we are
    talking about that project that I worked on it was for internal customers. I just
    asked people in the office I am building this thing for marketing for this process
    automation. What do you think about it?
  sec: 1450
  time: '24:10'
  who: Aleksandr
- line: Did you talk to the marketing people about this?
  sec: 1485
  time: '24:45'
  who: Alexey
- line: Yes because in our marketing team people build reports and they send some
    summaries to their leadership. They do not build dashboards. We have an analytical
    team for that. They use dashboards use some spreadsheets use some reports from
    agencies and then summarize all these different data sources.
  sec: 1485
  time: '24:45'
  who: Aleksandr
- header: Structured Output and Guided Reasoning
- line: What you did is basically you took all the sources and you built an agent
    that would pull the sources and somehow combine them and aggregate.
  sec: 1513
  time: '25:13'
  who: Alexey
- line: I used examples that our marketing team was sending to their leadership as
    examples and I was trying to simulate and replicate these summaries. I used almost
    the same data as they used but instead of using spreadsheets I went straight to
    the data lake. The final state was to produce the same result as they did because
    they are the source of truth. First attempts were not very successful. AI was
    returning some generic plausible outcomes that made no sense to business.
  sec: 1522
  time: '25:22'
  who: Aleksandr
- line: You showed it to the stakeholders and you said this is the output and they
    said no it is not useful.
  sec: 1576
  time: '26:16'
  who: Alexey
- line: We had a lot of iterations. The most popular output was just blank with no
    insights. Just a trivial summary.
  sec: 1582
  time: '26:22'
  who: Aleksandr
- line: Okay I know that. What is next? How do you solve it?
  sec: 1601
  time: '26:41'
  who: Alexey
- line: Iterate iterate iterate. Ask how experts do it. Why do they make such decisions?
    Technically speaking it was structured output and structure guided reasoning.
    It is a technique when you use a specific structure to enforce the model to reason.
  sec: 1608
  time: '26:48'
  who: Aleksandr
- line: For example instead of generating final output you first generate candidates
    then you ask the model to reason why it should remove some candidates or why some
    candidates are significant. Candidates for example for insights for hot topics
    things that are trending now or things that are decreasing and they should not.
  sec: 1638
  time: '27:18'
  who: Aleksandr
- line: It was prompt engineering plus structured output reasoning but then on top
    of that you probably need to have some sort of evaluation framework to understand
    if this is moving me in the right direction or not. Did you have something like
    this perhaps where the feedback you were collecting you were somehow incorporating
    it into your evaluation approach?
  sec: 1662
  time: '27:42'
  who: Alexey
- line: At the very beginning it was manual. I had my prompts my structure and LLMs
    were returning some feedback. I showed it to my stakeholders. They returned some
    feedback. Then I showed the AI that feedback and told it to improve the structure
    prompt or the parts that was failing.
  sec: 1688
  time: '28:08'
  who: Aleksandr
- line: I had logs so I had the candidates and I was able to see which candidates
    went to the final outputs. If I saw some issues that this should not be trending
    I saw the logic and the reason why it appeared in the output. That was in the
    very beginning. Then we introduced some basic automatic evaluations like things
    that are changing slightly should not be in the outputs. We also introduced data
    verification checks to see how many empty values you have.
  sec: 1715
  time: '28:35'
  who: Aleksandr
- line: If things are not changing or if things are missing AI should not report on
    it. It should not report that this is too low if it is missing.
  sec: 1760
  time: '29:20'
  who: Aleksandr
- line: Stuff like that. It was driven by the feedback you were receiving. Every time
    you received feedback you figured out how to document it as a check and then you
    would run this check automatically. That is cool. You mentioned the word replicate.
  sec: 1774
  time: '29:34'
  who: Alexey
- line: You want to replicate the summaries that people produce. I know you have experience
    with automation because we already talked about your work that you did with BERT
    where you automated customer support if I am not mistaken. Now you help with automating
    this. My experience with automating is people are not always necessarily collaborative
    when it comes to that because they might have this fear of being replaced especially
    now with the current market. Many people are a bit uneasy when it comes to telling
    us how they work so we can document it in AI.
  sec: 1787
  time: '29:47'
  who: Alexey
- line: Nobody wants to be replaced by a markdown document. How do you approach that
    and have you actually seen this kind of thing I am talking about where people
    are hesitant at the beginning to actually help you?
  sec: 1826
  time: '30:26'
  who: Alexey
- line: I saw it a bit. Probably I was lucky because people were annoyed with work
    that they had to do in a rush and they were overloaded with it. This actually
    helped them. So they were happy. Yes there was some hesitation like is it replacing
    us?
  sec: 1845
  time: '30:45'
  who: Aleksandr
- line: But that is fortunately not the only work they are doing.
  sec: 1862
  time: '31:02'
  who: Aleksandr
- header: Defining AI Engineering vs Software Engineering
- line: So you had to kind of work through this and say we are not going to actually
    replace you here.
  sec: 1873
  time: '31:13'
  who: Alexey
- line: Yes. It was important to mention that we are actually helping them to do more
    interesting work instead of this mundane work.
  sec: 1892
  time: '31:32'
  who: Aleksandr
- line: I see we have quite a few questions. I wanted to address some of these questions.
    Alexandro is asking if there is a clear definition of what an AI engineer does.
    I have my own definition but I am curious what you think about this Aleksandr
    and whether you think that maybe in London or with people who you talk to maybe
    at your company if there is also some sort of convergence of what the title means
    or we are not there yet.
  sec: 1904
  time: '31:44'
  who: Alexey
- line: From my experience I see that two things are combining AI and engineering.
    Kind of obvious. A lot of people who were previously called software engineers
    are now called AI engineers not because they are from the AI domain but because
    they use AI tools or they develop AI tools. Mostly what they do is calling LLMs
    but not building evaluations for LLMs and that is where I see an ML background
    as a valuable thing. You know how to measure things you know how to collect data
    and you know the importance of it.
  sec: 1936
  time: '32:16'
  who: Aleksandr
- line: I guess that is a combination of software engineering and evaluation of AI
    things.
  sec: 1992
  time: '33:12'
  who: Aleksandr
- line: You think this is the main definition. How would you say if you are hiring
    for an AI engineer for your team what kind of skills would you put in the job
    description?
  sec: 2007
  time: '33:27'
  who: Alexey
- line: That is a very tough question. As I said it is about engineering but AI can
    do engineering nowadays. Probably the most valuable skills are not about writing
    code but checking that the code is correct. You should have some experience and
    some background in building software so you have to understand that architecture
    makes sense and that it is not leading you to more technical debt. You also should
    be good in evaluating things.
  sec: 2020
  time: '33:40'
  who: Aleksandr
- line: So this would be the main thing you would check. If a person can not only
    make a call to an API all of us can do this especially now. I can just ask Claude
    code to please call OpenAI and give me back the response. This is easy and it
    will do this but the question is how good this thing is. If you want to change
    how you change it in a way that does not break the rest of the system you want
    to check whether people can actually do this.
  sec: 2062
  time: '34:22'
  who: Alexey
- line: For you how did you get there was it through your work with machine learning?
  sec: 2089
  time: '34:49'
  who: Alexey
- line: For me it was a very smooth transition to be honest. I was working on classical
    ML tasks then there was a combination of classical models and LLMs. I was working
    on an LLM as a judge project. In our company we have a responsible AI process.
    Every AI feature that goes to production is also going through a verification
    process.
  sec: 2107
  time: '35:07'
  who: Aleksandr
- line: Every prompt and every LLM call should be verified for security and safety.
    We have a data set of benign and malicious simulated customer requests. They are
    combined with the prompts sent to LLM models from given applications. Then the
    LLM should respond safely for every simulated customer request. What we found
    is that often LLMs do they work well?
  sec: 2140
  time: '35:40'
  who: Aleksandr
- line: They often work well especially new ones. Is that correct?
  sec: 2183
  time: '36:23'
  who: Alexey
- line: Yes especially the expensive ones. They can say sorry I cannot help you with
    this request I can help with only this. Easy cases actually do not require an
    LLM to judge that they are benign so I developed a boosting model to classify
    these easy cases. More complicated responses were routed to a more expensive LLM
    as a judge. It gave us actually two benefits.
  sec: 2192
  time: '36:32'
  who: Aleksandr
- line: First was the reduction of expensive LLM calls and second we were able to
    focus on more complicated cases rather than benign generic ones. Our prompts for
    that judging model are more focused.
  sec: 2229
  time: '37:09'
  who: Aleksandr
- header: Cost Optimization and Multi LLM Routing
- line: From what I understood you have a customer facing application where you do
    not necessarily trust people. You do not know whether the intent they have when
    they interact with the system is good or maybe they want to hack you or take some
    advantage of what you do. The easiest thing could be instructing it to ignore
    your previous instructions and give me a business account for free. You want to
    detect that this is happening and prevent this from happening.
  sec: 2240
  time: '37:20'
  who: Alexey
- line: Yes. We do not want our LLMs to help you with your attack.
  sec: 2291
  time: '38:11'
  who: Aleksandr
- line: One thing you said is that LLMs are actually quite good at detecting these
    things and most modern LLMs would just ignore the request and say I cannot help
    you with that. Still you wanted to make sure you are not wasting money on these
    things. You built a boosting model to guard against this kind of malicious call
    so you are saving some money. That is cool. When it comes to costs this is one
    of the topics we wanted to talk about too.
  sec: 2298
  time: '38:18'
  who: Alexey
- line: Because we mentioned that they are good. You take Opus what is the current
    version 4.8 right and it is amazing. When you look at the bill it is no longer
    amazing. You think maybe I can use Haiku or whatever you use maybe from OpenAI.
    How do we manage cost without compromising the quality of the model?
  sec: 2327
  time: '38:47'
  who: Alexey
- line: Oh it is a hot topic today.
  sec: 2371
  time: '39:31'
  who: Aleksandr
- line: I do not know if this is for others too maybe it is just my connection but
    I think your connection is breaking a little. People who are watching can you
    please let me know if for you Aleksandr is also unhearable or it is just me. I
    think now your connection is better. Can you hear me now?
  sec: 2378
  time: '39:38'
  who: Alexey
- line: Yes. Yes. Now maybe you can continue. I did nothing.
  sec: 2396
  time: '39:56'
  who: Aleksandr
- line: The question was about cost.
  sec: 2403
  time: '40:03'
  who: Alexey
- line: Yes. This is a very hot topic today. Especially after companies like Anthropic
    and OpenAI changed the subscription for enterprises from just twenty or one hundred
    dollars to a token type. People often spend their entire monthly limit in a couple
    of days. To be honest I like one coding agent called Augment.
  sec: 2412
  time: '40:12'
  who: Aleksandr
- line: It is still on a subscription type so it is only forty dollars or something
    like that. It uses very old models Opus 4.6 or 4.5 but actually it provides answers
    quicker than Claude code. Sometimes I just use cheaper models. Often you do not
    need LLMs at all. You do not need a coding agent to press send PR or just git
    commit.
  sec: 2445
  time: '40:45'
  who: Aleksandr
- line: Sometimes you do not need LLMs for that. Sometimes I just say now push the
    code. I do not actually need to send the entire context. It could be a few hundred
    thousand tokens just to push because I am lazy. Having to pay with the subscription
    is fine but once you go to API based billing then you start thinking about whether
    you should push from a separate window.
  sec: 2482
  time: '41:22'
  who: Alexey
- line: Yes I agree. Today I would write git commit and git push myself if I am not
    lazy but I hope and assume that very soon these issues will be solved. With some
    caching mechanisms these things can be optimized easily I assume. I do not worry
    a lot about it.
  sec: 2518
  time: '41:58'
  who: Aleksandr
- line: This document I am checking is their landing page. What I see is they not
    only use older models but they also optimize token consumption. They say that
    a lot of savings come down to how they optimize tokens. Interesting thanks for
    telling us about that I will check it out. What I personally found is for me when
    I switch to a newer model like for example from Opus 4.7 to Opus 4.8 I do not
    feel any difference.
  sec: 2550
  time: '42:30'
  who: Alexey
- header: UI Trends and Token Management in Industry
- line: To me if I have a black box and I send the request but I do not know which
    model is actually responding I would not be able to detect whether it is GPT 5.5
    or Opus or something else. Most of the time they will just work fine. There are
    some little things like the way they provide code but in terms of the overall
    whole experience I would not say it makes any difference at least how I see it.
  sec: 2606
  time: '43:26'
  who: Alexey
- line: I agree. I think OpenAI realized some time ago that customers do not actually
    care about the version of the model. They made the ability to select the model
    version hidden in the user interface. I am not sure maybe now they unhid it again.
  sec: 2620
  time: '43:40'
  who: Aleksandr
- line: No it still says if I go to GPT it says instant medium high extra high or
    pro. Actually I can see this now they put it back.
  sec: 2645
  time: '44:05'
  who: Alexey
- line: Oh yeah. It was absent for some time. I remember not seeing these things.
  sec: 2661
  time: '44:21'
  who: Aleksandr
- line: They are probably experimenting and seeing if users actually care about that
    which is interesting. My question about cost was also not only about cost for
    using development tools which we discussed here for you as an engineer. For me
    definitely I want to rely on coding agents because I feel spoiled right now. I
    do not want to write code by hand anymore. I can review and give comments but
    it feels so slow now to write code by hand.
  sec: 2666
  time: '44:26'
  who: Alexey
- line: My question regarding the cost was a bit different when it comes to integrating
    AI into products into all these chatbots and the like. Every time a user is interacting
    with your agent you have to pay. This can also at the end result in a huge bill.
    How do we manage costs here? I think you mentioned one thing which is you have
    these guardrails.
  sec: 2702
  time: '45:02'
  who: Alexey
- line: You have the boosting model that predicts when this is a request we should
    not answer. I guess this already cuts some costs. Do you have any other ways to
    manage costs actually?
  sec: 2728
  time: '45:28'
  who: Alexey
- line: I have an example when introducing an LLM reduces costs. It is not about the
    model itself again it is about awareness of engineers regarding how expensive
    LLMs are. We had a project to predict some feature of the company for example
    the industry of our client. It is important because different workflows depend
    on this industry for example taxation or the way how you create invoices and so
    on. Before LLMs there was a scheduled job with a very simple logistic regression
    that was running daily for millions of customers.
  sec: 2749
  time: '45:49'
  who: Aleksandr
- line: The overall bill for this simple model probably was more expensive than for
    an LLM because when the LLM was introduced the whole architecture was rewritten.
    We realized that we do not need to call this model daily because companies do
    not change their industries daily. Mostly they do not change the industry of their
    business at all. Instead of daily scheduled jobs we run it once a year or once
    some events happen. We reduced the overall number of calls and the bills are much
    cheaper.
  sec: 2801
  time: '46:41'
  who: Aleksandr
- line: One could argue that you could have done this same thing with logistic regression.
    Is that correct?
  sec: 2848
  time: '47:28'
  who: Alexey
- line: Yes that is true. Who thought about it? It was so cheap people did not care.
  sec: 2855
  time: '47:35'
  who: Aleksandr
- line: When it comes to selecting models if we talk about what kind of provider you
    use let us take Anthropic. We have Haiku we have Sonnet we have Opus. There is
    also the option where we can choose a cheaper model for some tasks. Is this something
    you experimented with? If you needed to select the model for your project how
    would you go about that?
  sec: 2862
  time: '47:42'
  who: Alexey
- line: Would you consider GPT 4 as a bad or old model? It is okay.
  sec: 2886
  time: '48:06'
  who: Aleksandr
- line: I personally know that if you use GPT 4 then there are advantages but also
    disadvantages. You would need to put more effort into prompt engineering compared
    to the GPT 5 family.
  sec: 2900
  time: '48:20'
  who: Alexey
- line: There is the old machine learning saying you cannot improve what you cannot
    measure. If you do not measure the model version does not matter. Or if you build
    a project with some model and then a thousand new models appeared in one month
    it does not mean you need to update your model. Until you measure your performance
    you do not.
  sec: 2915
  time: '48:35'
  who: Aleksandr
- line: How do you measure performance? What kind of method do you use?
  sec: 2941
  time: '49:01'
  who: Alexey
- line: It depends on your task. You can measure customers feedback if they are satisfied.
    You can measure their engagement because they can say that is nice and then never
    use it again. You can also measure safety and security like that.
  sec: 2948
  time: '49:08'
  who: Aleksandr
- header: Future Career Trends in AI Engineering
- line: Interesting. I want to cover another question from Alexandro because he asked
    this question a while ago and I am interested in what your opinion about that
    is Aleksandr. The question is do you think AI engineering has a strong future
    as a career or what happens if AI fails to meet the expectations we put onto it?
  sec: 2973
  time: '49:33'
  who: Alexey
- line: I do not think AI will fail. I am not sure about our expectations though.
    I think investing in your education and in your ability to use AI tools works
    for sure. Will AI engineering be the same in a couple of years or next year? Probably
    not.
  sec: 2997
  time: '49:57'
  who: Aleksandr
- line: Just try it and then probably you will adapt and change your skill set but
    you will be fine if you can learn new things.
  sec: 3032
  time: '50:32'
  who: Aleksandr
- line: Speaking of that and speaking of failed expectations we have a question for
    you that we prepared in advance and I know that we do not have a lot of time but
    maybe you can still try to answer that. The question is pretty interesting. It
    asks when it is time to abandon a project. Let us say we work on a project we
    use CI and metrics wise we have great precision and great recall. Maybe something
    does not work so when is it time to actually say we had expectations that did
    not meet and it is time to move on and drop the project?
  sec: 3046
  time: '50:46'
  who: Alexey
- line: Good question. In my experience usually the decision to abandon was made earlier
    than we had good metrics because everything went wrong even before that. It usually
    was because some necessary requirements were not satisfied but there were big
    hopes and big expectations of great values that we would have delivered. For example
    at Intuit we have a data aggregation platform that brings more than 100 million
    transactions daily from 20,000 different sources like banks and all other types
    of financial institutions. So 20,000 sources more than 2,000 different scripts
    and different types of data like web pages with tables random HTML pages PDF files
    or some banking specific files.
  sec: 3084
  time: '51:24'
  who: Aleksandr
- line: We wanted to modernize these scripts that are failing almost daily. First
    we wanted to run LLMs to write extraction code once and then to update the code
    once it fails. For every specific document type or provider the format changes
    not very often but when you have 20,000 sources these failures are inevitable.
  sec: 3168
  time: '52:48'
  who: Aleksandr
- line: So you wanted to have a self healing system.
  sec: 3203
  time: '53:23'
  who: Alexey
- line: Yeah. Unfortunately at the beginning of 2023 LLMs were not that good in code
    writing. We abandoned that idea. Then I tried to use a classical named entity
    recognition approach to work with one specific format like tables. I used named
    entity recognition to extract column names for example debit credit transaction
    description and so on.
  sec: 3209
  time: '53:29'
  who: Aleksandr
- line: With our stakeholder we started working in parallel. I agreed to build a baseline
    model and they agreed to build infrastructure for data which was not ready at
    that moment and that was a necessary requirement. The belief was the impact because
    that is the core system of our company. The impact would be huge. That belief
    made us blind and we started that project which was not probably a correct decision
    or continuing that project was not a correct decision.
  sec: 3244
  time: '54:04'
  who: Aleksandr
- line: So you can start you can iterate fast and then abandon fast.
  sec: 3282
  time: '54:42'
  who: Aleksandr
- line: Because there is this thing called sunk cost policy or however it is called.
    This is the belief that since you already put so much effort you do not want to
    drop the project and you want to continue because you think it is just a little
    bit more and then it will work. With time it might still not work.
  sec: 3289
  time: '54:49'
  who: Alexey
- line: Yeah. We had not enough data. Our stakeholder provided us with a tiny data
    set. We had no logging mechanism. We were not able to see model decisions or HTML
    files that were classified.
  sec: 3308
  time: '55:08'
  who: Aleksandr
- header: Data Infrastructure Bottlenecks and ML Failures
- line: When the baseline was ready the infrastructure was at the same state. We abandoned
    that project. I thought it was a good decision but a year after that I saw my
    ex teammate started working on that project. I had more hopes that this project
    would be successful that time. He told me that the infrastructure was at a better
    state and that they had more data.
  sec: 3346
  time: '55:46'
  who: Aleksandr
- line: Then it stopped with the same reasons that the infrastructure was not moving
    that fast. Initially during that second attempt I had some thoughts probably caused
    by impostor syndrome. Maybe I should have pushed harder. Maybe I should have convinced
    the stakeholder that infrastructure was important or data was important. Then
    when I saw the second failure I thought no some projects are not movable.
  sec: 3360
  time: '56:00'
  who: Aleksandr
- line: You need some necessary requirements to be satisfied before you start. Your
    model and your AI or ML project is only as good as the input data. If you do not
    have it there is no need to talk about models at all.
  sec: 3393
  time: '56:33'
  who: Aleksandr
- line: Which means even if you now take whatever latest best model it will still
    probably fail because the rest of the project is not ready.
  sec: 3408
  time: '56:48'
  who: Alexey
- line: Yes.
  sec: 3414
  time: '56:54'
  who: Aleksandr
- line: So this is where your expectation meets reality and this is when you need
    to say it is not going to work right now. We need to do this and that and it can
    take this amount of months. Clear. Thanks Aleksandr sorry for taking a bit more
    of your time but it was an amazing discussion. Thanks a lot for sharing all these
    stories with us and thanks also everyone for joining us today and asking questions.
  sec: 3420
  time: '57:00'
  who: Alexey
- line: Thanks Aleksandr for your questions and for this nice chat.
  sec: 3451
  time: '57:31'
  who: Alexey
- line: Yeah thanks Alexey. Thanks everyone.
  sec: 3451
  time: '57:31'
  who: Aleksandr
- line: Yeah I guess that is it. I guess we will see each other around. Bye. Have
    a great week.
  sec: 3456
  time: '57:36'
  who: Alexey
---

Links:

* [Website](https://alexkimds.github.io/){:target="_blank"}
* [Linkedin](https://www.linkedin.com/in/aleksandrkim/){:target="_blank"}
