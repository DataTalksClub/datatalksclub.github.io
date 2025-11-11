---
title: 'How to Build Data Governance in the Cloud: Classification, Catalogs, Policies
  & ROI'
short: Data Governance
guests:
- jessiashdown
- urigilad
image: images/podcast/s03e10-data-governance.jpg
season: 3
episode: 10
ids:
  youtube: tJ3v8h7A7RY
  anchor: Data-Governance---Jessi-Ashdown--Uri-Gilad-e12jmoo
links:
  youtube: https://www.youtube.com/watch?v=tJ3v8h7A7RY
  anchor: https://anchor.fm/datatalksclub/episodes/Data-Governance---Jessi-Ashdown--Uri-Gilad-e12jmoo
  spotify: https://open.spotify.com/episode/2zaLMrgbIgVkVEWY09b1Wn
  apple: https://podcasts.apple.com/us/podcast/data-governance-jessi-ashdown-uri-gilad/id1541710331?i=1000525176805
transcript:
- line: This week we will talk about data governance. We have two special guests.
    This is the first time I have two guests in this podcast, so far it was only one.
    It will be a lot of fun. So we have two guests — Jessi and Uri. They both work
    at Google and they both are co-authors of the data governance book.
  sec: 151
  time: '2:31'
  who: Alexey
- line: Jessi is a senior user experience researcher at Google Cloud. She conducts
    user studies with customers and then she uses these findings to shape Google’s
    data governance program and products. Uri is a product manager at Google and he
    is leading data governance efforts there. Welcome.
  who: Alexey
- line: Thank you.
  sec: 207
  time: '3:27'
  who: Uri
- line: Hello!
  sec: 208
  time: '3:28'
  who: Jessi
- header: Jessi’s background
- line: Before we go into our main topic of data governance, let’s start with your
    background. We’ll start with Jessi. Jessi, can you tell us about your career journey
    so far?
  sec: 209
  time: '3:29'
  who: Alexey
- line: It’s been a long one. I have done a lot of different things. I started out
    as a psychology major. Looking at research, I loved research back in the early
    2000s, there were not a whole lot of jobs for somebody who had a degree in psychology.
    So I bounced around and did a lot of different things — real estate, coaching,
    athletics. Until I finally found this thing called “UX research”.
  sec: 221
  time: '3:41'
  who: Jessi
- line: I am like “what is this UX you speak of”. It was this perfect marriage of
    psychology and useful stuff that you could do for people that was pretty immediate.
    I started in that seven or eight years ago. I worked at T-Mobile on their enterprise
    products for about four years until I moved to Google. I have been working with
    Uri pretty much the entire time I have been here at Google cloud. I’ve worked
    on data governance for the last three years.
  who: Jessi
- header: Uri’s background
- line: Thanks! Uri?
  sec: 286
  time: '4:46'
  who: Alexey
- line: My background is much more banal for a product manager. Jessi, I never knew
    you were in real estate. Every day you learn something new. I started off as an
    engineer in a security company, then I moved to product. People were tired of
    me criticizing the product. They were like “How about you do something about prioritizing
    those criticisms?”. I have spent several years in a security company. I was an
    early employee in ForeScout and Check Point. Most recently before Google I was
    the vice president of product management in a security company for endpoints devices
    called MobileIron.
  sec: 290
  time: '4:50'
  who: Uri
- line: It’s funny how I got to Google. Throughout my career, I cared for data on
    endpoint devices. Google's offer was about crossing the mirror, crossing to the
    looking glass, and getting to care about data at the source — at the server side,
    at the cloud provider side.
  who: Uri
- line: Data governance has been around for a long time. It’s something Google has
    been doing throughout its history. The challenge was to bring data governance
    to Google cloud customers. I am sure we will talk more about that.
  who: Uri
- line: Now you also care about security but from a different angle.
  sec: 384
  time: '6:24'
  who: Alexey
- line: Yeah.
  sec: 398
  time: '6:38'
  who: Uri
- header: Data governance
- line: We mentioned data governance, and the talk today is about it. So what is it?
    To be honest, I still have a really vague idea, what data governance is and why
    we need it.
  sec: 400
  time: '6:40'
  who: Alexey
- line: I will start. I should start with saying what data governance is not only.
    Often people talk about data governance, depending on who you talk to, there are
    a myriad of different definitions. From our perspective, what it's not only —  it‘s
    not only securing your data, so it’s not only about how we govern — what I like
    to call the scary stuff — PII, credit card numbers, things like that. It’s not
    just about securing those and monitoring access to those.
  sec: 417
  time: '6:57'
  who: Jessi
- line: What is PII?
  sec: 460
  time: '7:40'
  who: Alexey
- line: Personally identifiable data.
  sec: 465
  time: '7:45'
  who: Uri
- line: Thank you. Things like a name, a social security number, date of birth. Recently
    with GDPR, a lot of companies and folks are worried about data governance — governing
    their sensitive data. We talk a lot about this in the book. It’s more than that.
    It’s also about knowing what data do I have. Period. If you don’t know what data
    you have, you cannot really use it. You cannot run analytics. You also cannot
    secure it. You cannot decide where it should go. What should you do with it? whether
    or not it is a duplicate? Should you retain it?
  sec: 467
  time: '7:47'
  who: Jessi
- line: So, data governance encompasses the entire story of what data I have and how
    I can use it best. Whether that means securing it or using it for business analytics
    things like that. Uri, did I miss anything?
  who: Jessi
- line: No. But I would like to offer a different perspective that adds on to what
    Jessi said. First of all, data governance is not new. Data governance, broadly
    speaking, is a practice of people, processes and tools — or the combinations of
    those three —  in order to understand, care, and extract insights from your data.
    The reason I am saying it’s not new — the term became more popular recently. But
    it always was the case where any company would have a customer list and certain
    insights of that list. That has been ever since companies were born. The normal
    insights were like “This customer is behind on his payments” or something like
    that.
  sec: 537
  time: '8:57'
  who: Uri
- line: Now something has been happening surprisingly slowly and yet had implications
    that made data governance a very popular term. Cloud did not happen in one day.
    The cloud transformation transition is still happening — slower than expected
    — but cloud got to the game unlimited infrastructure. That gave the ability for
    companies to say, “I would not only save the payments table, I will save the customer
    behaviors table as well. I will look at all the events that are happening as people
    interact with the product. I will know if people are spending time in my e-commerce
    website in the T-shirts department, maybe I need more choice in T-shirts. If people
    are buying a lot of T-shirts towards the 4th of July, maybe it’s a good time to
    make sure my supply chain is ready for the 4th of July.”
  who: Uri
- line: This trend of saving more data for insight which… I don’t actually know what
    these insights are right now. I will just collect all the data. This has made
    people uncomfortable and caused several things.
  who: Uri
- line: One — the regulator stepped in and said, “You are collecting a lot of information
    about people. This information may identify them. Those people have not signed
    up to be identified.” I don’t want the 4th of July T-shirt website to know my
    buying habits. That is highly personal. It may indicate where I live, it may indicate
    how much money I have. I’m not comfortable with that.
  who: Uri
- line: 'The European regulation says: A) you must explicitly ask people to share
    the information and B) you should separate the people with processes and tools
    that collect PII —  personally identify information — from other systems. That
    will allow me, the customer of the T-shirt website, to say “I’m done with your
    website. I want to be taken off.”'
  who: Uri
- line: Accumulation of highly personal data that can identify you led to some mishaps.
    The most notorious one is the Cambridge analytical scandal. There are others.
    Companies who were making money from data were forced to be more prescriptive
    and cautious about using the data. That chain of thought led to this practice.
  who: Uri
- line: But as I said, it was always there. If you look at the banking industry, they
    must keep — depending on the country — seven years of data. That will allow us
    to go back on transactions and detect fraud. That’s usually proven by a chain
    of transactions or a chain of money movements. Banking and the financial services
    community in general always had rules about how you can collect the data, how
    long to keep it, and who should be able to access it.
  who: Uri
- line: Data governance is taking that practice and making it more accessible. Hopefully,
    as Jessi said, it will become not just a security mechanism but rather an enabler
    that allows people to access more data safely. It defines ground rails that prevent
    them from falling into inadvertently sharing data. It helps with making more useful
    insights and bringing us more useful products. There are a lot of products — not
    just T-shirts or things like that — that are possible because we can understand
    what people want.
  who: Uri
- line: I will try to summarize and you correct me if I am wrong. We have a lot of
    data. We start collecting data. In order for an analyst to understand the data,
    they need to know what we actually have. We need to have a way of knowing, we
    have this, this, this data. This is one part of that — having the data itself
    and having the tools to access the data. Then there are tools to catalog the data.
    The third component, you said, is processes — how people go about accessing the
    data, collecting the data, and storing the data.
  sec: 844
  time: '14:04'
  who: Alexey
- line: You also mentioned that in banks, the rule of keeping the data for seven years
    has been around for quite a while. This is one of the data governance rules, right?
    They say “we must keep the data for seven years”. This is a rule they have to
    follow. And this is how they define data governance. Right?
  who: Alexey
- line: That is a good example of retention — which is how long you retain the data.
    It’s an example of a data governance policy, yes.
  sec: 914
  time: '15:14'
  who: Uri
- line: So we have a bunch of policies like this and then collectively they are called
    “data governance”. Right?
  sec: 923
  time: '15:23'
  who: Alexey
- line: Very good.
  sec: 931
  time: '15:31'
  who: Uri
- header: 'Implementing data governance: policies and processes'
- line: This sounds excellent! As a company I really want to have it. I want our analysts
    to know what data we have and where this data lies, how to access this data. How
    do I implement this?
  sec: 933
  time: '15:33'
  who: Alexey
- line: 'I wanted to add a little bit. You were talking about these tools and the
    processes. You were really hitting on the process that the tools have. I’m an
    analyst. What tool do I use to find my data, to access it, to run analytics? But
    as Uri was hitting on, there are policies — this is also a part of the process.
    The policies say what we do with this kind of data. He was giving the example
    with the banks: this is the kind of data we need to keep for seven years. But
    there is also the process around how we ingest the data. What do we do once it’s
    ingested? That’s a big piece that often doesn''t get done or doesn’t get done
    well.'
  sec: 951
  time: '15:51'
  who: Jessi
- line: Uri was talking about collecting all this data. A lot of companies just collect
    it and dump it, right? Let’s just dump it somewhere in this big storage and then
    later we are going to figure out what to do with it. I’m not saying it’s wrong.
    But you need a process that tells you how to go through that. How to find out
    what it is. classify this.
  who: Jessi
- line: We are going to talk about data catalogs later, so I am hitting on it a little
    bit early. But if we are talking about implementing data governance, first you
    have to start with classifying the data. What are the different data classes that
    I want to identify? This is sensitive stuff. This is business critical.
  who: Jessi
- line: Let’s say that you have revenue data. Depending on what you call it, there
    might be four different kinds — ROI, sales, and so on — different labels that
    you want to clump together in a class. So, it’s about defining what are these
    different data classes that you want to have. Then you go through your data to
    map it to these different classes. At least it’s a first starting point. There
    is a lot more. Uri did you want to add on to this classification part?
  who: Jessi
- line: A little bit. Do not start from a technocratic point of view. You want to
    have data governance. Great! Why? Are you subject to regulation? Are you afraid
    of data exfiltration? Are you in a business that requires you to have a certain
    liability or certain accountability to customers? What’s the core reasoning? It
    may be multiples of those things. As a business, you need to understand what kinds
    of data you hold. Then Jessi went into classification which is the way to go about
    it. So, answer, why am I concerned about data governance? What kinds of data do
    I want to do something about? Then the third part is about policies — the policies
    I want to put in place to answer that “why” with confidence.
  sec: 1104
  time: '18:24'
  who: Uri
- header: Reasons not to have data governance
- line: Can I ask something? You mentioned that, like we should ask ourselves why
    we need data governance. Before we implement this, we need to ask this “why” question.
    I am wondering if there are reasons why we don’t need it. Maybe it is just overkill
    for us? Maybe we are a small company, we don’t have that many analysts? Or maybe
    we do not store sensitive data? What kind of reasons can we have not to implement
    it?
  sec: 1180
  time: '19:40'
  who: Alexey
- line: Jessi mentioned that data is valuable — because otherwise you wouldn’t be
    collecting it. If data is valuable, you want to make sure that you know what you
    have, where it is and how to access it. This is the act of cataloging, an act
    of data governance. I know that I am speaking from a very clear interest, but
    I’d argue that cataloging and understanding what you have is a step that clearly
    is in the path to getting insights. We can agree — and if not, I will try to convince
    you — that data insights are valuable. You will make your business more efficient,
    more streamlined. You will identify new sources of revenues. That will be one
    answer. Jessi seems to have more.
  sec: 1209
  time: '20:09'
  who: Uri
- line: We talked in the beginning of how broad the definition of data governance
    is. Different companies are going to have different levels of intricacy into their
    data governance program. But we would vehemently argue that even if you have five
    employees, you still need some way of knowing what data you have, so that you
    can have insight from it. Maybe your processes are not going to be as complicated
    as in a bank that is collecting a lot of sensitive information.
  sec: 1266
  time: '21:06'
  who: Jessi
- line: We have been doing research on companies. There have been some that are small,
    cloud native. They don’t have a lot of employees, they don’t collect a lot of
    sensitive data and their data governance program is a lot less complicated. There
    are very big financial institutions that have many moving parts. They have to
    think about many employees. You are right, it can be a bit less complicated.
  who: Jessi
- line: But we’d argue that no matter what, if you have any data at all, you have
    to think about how you are going to structure a governance program for that data.
  who: Jessi
- line: You collect data, you store it somewhere, you query it with some system. That
    costs money. You pay money for storage to retain the data and for compute to process
    this data. How do you know if this money is actually doing something for you?
    That’s data governance.
  sec: 1354
  time: '22:34'
  who: Uri
- header: Start with “why”
- line: So, it’s not a question whether we need data governance or not. We do need
    it. But the “why” — the question we should ask ourselves — is what’s the reason
    we need it. It’s clear we need it. But why do we need it? It’s not a decision
    between “yes” or “no”. It’s a decision between what are the problems we want to
    solve first — before starting to implement it.
  sec: 1380
  time: '23:00'
  who: Alexey
- line: Exactly. That’s going to help you figure out how extensive the data governance
    program should be. And Uri is completely right. Yes, you are going to need it.
    But figure out that “why”. Is it because I am collecting a bunch of sensitive
    data? Am I going to need to show regulators a certain something? For our T-shirts
    website, is business asking us for differences in Fourth of July versus other
    times? Do we need to increase our supply chain? Answering those kinds of questions
    will help you figure out what parts of a data governance program to prioritize
    first.
  sec: 1409
  time: '23:29'
  who: Jessi
- header: Cataloguing and classifying our data
- line: I guess most of the time the answer is data catalog. You need to have this
    catalog of data. You need to know what kind of data you have. You said that we
    need to classify the data — first of all, we need to know what kind of data sources
    we have. Then for each data source, we need to understand each field in this data
    source. Is it personally identifiable or not? Is it business critical? What kind
    of classes can we have there in addition to these two?
  sec: 1454
  time: '24:14'
  who: Alexey
- line: There’s no preset dictionary of classes that you use for every purpose in
    every business. The classes of data are really defined by you. There are examples
    of classes of data which we will go over, but they are defined by you. For each
    group of data, I want to assign a specific policy or a specific governing method.
    Here are common examples from the industry.
  sec: 1499
  time: '24:59'
  who: Uri
- line: We already mentioned one — PII, or personally identifiable information. We
    mentioned PII because the European regulators made the point that you must separate
    PII from other kinds of data. It’s a phone number which can clearly identify you,
    a phone hardware number, an address, or name. It depends on the business you are
    in. In some businesses you may be collecting names and addresses, but not in an
    identifiable manner. Google office is an address, but it does not identify people.
    There are thousands of people working there.
  who: Uri
- line: There is special health information which has been around for a long time.
    It’s the demographics of the patient, the treatments that patient is having, the
    success of those treatments. Especially in medical research, by the way, since
    we all went through an interesting year. The sensitivity of treatments on a specific
    person which can identify them. Maybe there are things they don’t want a processor
    of medical information to know. But these things are useful in determining the
    possible success of a treatment.
  who: Uri
- line: So, we have patient health information, personally identified formation, fiscal
    information, list of transactions and amounts and so on. There are other classes
    of data.
  who: Uri
- line: As we are potentially talking to people who want to start a governance program,
    try not to subscribe to outside defined classes of data. Think about your business.
    Think about what data you possess. Think about how you would like to control,
    make accessible and delete that data. That is how you should think about it. There
    are examples. We literally wrote a book about it. But think about yourself, not
    about others.
  who: Uri
- header: Let data work for you
- line: When it comes to implementing this data catalog, I imagine that I can start
    with creating an Excel spreadsheet or Google spreadsheet. Then I put all the data
    sources there — all the fields, all the classes. That’s probably a reasonably
    good start, but that’s not always the best tool. There are better ones. Do you
    know if there is something purpose-built that can help us?
  sec: 1668
  time: '27:48'
  who: Alexey
- line: =Yes. There are many tools. Uri, I am sure you have a lot of opinions on this.
    There are many tools and people create a lot of their own tools. But one of the
    important things is to really think about the future. How scalable is what you
    are doing? Is it going to have to scale enormously? One of the problems we have
    seen with data governance — it’s manual. Especially if we are talking about cataloging
    and classifying, doing this as an excel spreadsheet is so manual.
  sec: 1703
  time: '28:23'
  who: Jessi
- line: We have talked to companies where data governance often fails. It’s because
    it’s so manual. There’s no one to do that. In fact we talked to a company a couple
    years ago. They had a full-time data steward — a person whose sole job was to
    catalog, classify, do all this kind of stuff. That person quit because they said
    the job was — and I quote — “soul sucking”. That’s a true story, I’m not lying.
    Most other companies don't have a single person who is doing this job.
  who: Jessi
- line: The takeaway from that is to think about the process you are going to start.
    Think about how to keep this going. Who is going to be doing this work? Am I setting
    up a process that is just so time consuming. It’s going to be really difficult
    to keep it going.
  who: Jessi
- line: I want to double down on a lot of what Jessi said. Alexey, what you discussed
    is really okay. I need to get data governance, I will open this spreadsheet, I
    will start putting it data, and I will work for my data. But if you work for your
    data, something is wrong there from the start. The data should work for you, not
    the other way around. That’s not my metaphor, one of the analysts who I worked
    with said that. Make data work for you. This is what data governance is about.
  sec: 1820
  time: '30:20'
  who: Uri
- line: Think about it this way. You need the data governance program. That probably
    means you have data somewhere. You process this data and you store it. Where is
    the data right now? This is something you should know because you pay for that
    storage every day. What systems do I already have that tell me something about
    my data? Take those systems, and then, as Jessi said, extend your timeline into
    the future five years, ten years. See if this is the place where I store the data
    right now. Am I happy about it? Is it performant? Is it scalable? Is it future
    proof? What systems do I have that integrate into this system today?
  who: Uri
- line: I am going to do a little bit of a shameless plug here. When you use a platform
    such as Google Cloud, we have tools already built into the platform. They support
    a lot of the basic workflows and basic needs. Google Cloud has a Google Cloud
    catalog. As you drop data in a file storage or columnar storage, it automatically
    assesses the data and indexes it — we are also known for being a search company.
    This allows you to find what you need. That’s a good starting point you can have
    today. To be fair, other clouds have similar systems. So, assess your situation
    right now. Then, if you need to buy a specialized tool, don’t work for your data.
  who: Uri
- line: If you’re not satisfied with your existing infrastructure, go back to the
    “why” — why do I need data governance? Do I need to comply with regulations? Or
    I need to extract more insights? Or I need to be wary about exfiltration? There
    are tools that are built around those concepts. Evaluate them in light of your
    current and future goals. Then decide. Did you want a concrete tool? Like “Do
    this kind of thing”? That conversation is very different for each particular company,
    in each particular vertical. I am sorry if that is disappointing.
  who: Uri
- header: The human component
- line: What I understood is, starting with an excel spreadsheet is not ideal. At
    the end, the person maintains it will quit because it’s a soul sucking job. You
    need to make data work for you. There are tools that look at your data and organize
    it. But I guess this human component will not go away. At the end, you still need
    to make a decision if this particular field is personal or not personal, is this
    field is business critical or not. There still needs to be a person who looks
    at this and makes this classification, right?
  sec: 1983
  time: '33:03'
  who: Alexey
- line: Even more importantly, if this particular field is personal, what do you do
    with it? That can only come from a human. Do you delete it? Do you encrypt it?
    Do you allow it to be accessible only by certain people? That is most definitely
    a human component. That’s the human that the data works for.
  sec: 2042
  time: '34:02'
  who: Uri
- line: And then data does not stand still, it evolves. We add new fields, we remove
    fields, and we add new data sources. Somebody still needs to keep track of it.
    Even though a system could be automatically synchronizing with the data sources
    and see a new field, then send an email saying “Hey, data steward, please take
    a look at this field”. At the end, somebody needs to go there and do a manual
    action.
  sec: 2065
  time: '34:25'
  who: Alexey
- header: Data quality
- line: I want to add to that. We talked a lot about binary concepts, like is this
    data A or B. Is this column protected or not? Should this be accessible to this
    person or not? There are also some fuzzy concepts in data governance. One of which
    is data quality. Data quality is more elusive.
  sec: 2099
  time: '34:59'
  who: Uri
- line: This data source contains PII. It’s entering through this system and going
    to that system. Do I trust it? Is it high quality enough to be used in a machine
    learning model? Is it high quality enough to make a business decision? This is
    a tricky concept. This is also part of data governance. We can talk about that
    as well.
  who: Uri
- line: This is an interesting discussion. How do you know if this data is high quality?
    Is it because the analyst working in that team said so?
  sec: 2149
  time: '35:49'
  who: Alexey
- line: There are mechanical ways to understand quality and more elusive ways. First
    of all, what is the source of the data? I’m working with an insurance company.
    They have proudly mentioned that they are at “World 3.0” now. I am like “What
    does that mean?” This said “We have processed most of the handwritten data. We
    are now reading data written in Microsoft Word 3.0. That’s probably 1990s or slightly
    later. We are making our way through the backlog.” So, some of their data is potentially
    handwritten. Can that be used today in making a decision about a mortgage? For
    an insurance company, that’s an interesting question. Only somebody who is familiar
    with it knows the answer.
  sec: 2162
  time: '36:02'
  who: Uri
- line: Then there’s data coming from an oil rig. Transmission there is iffy. There
    is a lot of noise on the communication channel. Should I be using that in order
    to determine gas leaks?
  who: Uri
- line: Then there’s a data source that is a combination of merging data sources A
    and B. I have a quality signal for both. What is the derivative quality signal?
    Those are technical. You can detect out of bound values, missing fields, errors
    in rows. Those are more technical practices that you can implement fairly easily
    and also give you a quality signal.
  who: Uri
- line: So, it’s up to the producer of the data to say if the data can be trusted
    or not? They have a domain expert, a business expert — somebody from insurance
    or somebody from this oil ring. They can say that. So we still need to trust the
    producer who created the data.
  sec: 2265
  time: '37:45'
  who: Alexey
- line: You can implement a lot of tools that give you a leg up. But I’d argue that
    the final decision of trust should be handled by a human. We are still useful.
  sec: 2287
  time: '38:07'
  who: Uri
- header: Defining policies
- line: So, we have the data sources. We have the data storage, where we put data.
    It can be a data lake or a data warehouse — some place where we keep the data.
    Then we have this data catalog. It can also communicate with our data storage
    and get all this information from there. We have a data steward who maintains
    the data catalog and knows what is going on there. What else do we need to have
    to implement data governance?
  sec: 2305
  time: '38:25'
  who: Alexey
- line: We talked about it a bit. The next step is having the policies on these classifications.
    Once you have your data classes, you have to define what to do with that. Are
    there certain ones that need to stay in this storage? For example, some need to
    be kept for seven years. For the business critical ones, what’s the freshness?
  sec: 2340
  time: '39:00'
  who: Jessi
- line: The policies can be varying. I just listed straightforward ones. We have done
    more research into policies and they are a lot more complicated than we had originally
    thought. For example, here is a simple policy — allow access of this data for
    these folks only.
  who: Jessi
- line: But depending on the purpose of accessing the data, it might change who can
    have access. We heard an example from a company that sells furniture. They had
    said, “We have somebody's email address. They bought a couch. We are going to
    ship them the couch. So the person handling these shipping addresses can have
    access to that data. Now we have a sale on couch covers. We would like to market
    this to folks who have recently bought a couch. But we — even if it’s the same
    analyst as previously — can’t access these emails for marketing purposes unless
    that customer explicitly gave permission.” How do I create a policy that captures
    that nuance for this particular use case of this data, that it cannot be used
    for that?
  who: Jessi
- line: So once you have your classes, you are going to have to think about what I
    do with those. What policies I am going to put on this? As Uri said at the very
    beginning, this all goes back to your “why”. This is how I figure out the key
    things that I really need to care about. If regulations are top of mind and that’s
    the most important, then my policy should fall in line with that. As you can see,
    you can go down a million rabbit holes of “govern this”, “govern that”, “classify
    this”, “classify that” policies. So, be able to map back to “What do I have to
    do?” and “What’s the most important?”. Start there.
  who: Jessi
- line: You have organized your data. You have understood your data. You have attached
    tags to further understand and index your data. Now you describe a couple of policies
    — what is allowed to do with my data. The way I like to think about this — policies
    are not “thou shalt not” or “thou shalt”. They should not be thought of as prescriptive.
  sec: 2524
  time: '42:04'
  who: Uri
- line: Policies should answer the question “How do I make sure the CIO, the CISO,
    the CEO feel comfortable about everybody in the company accessing this data?”.
    The way to make those C-suit people feel comfortable is saying “Anybody can access
    the data, but only this specific group can access personally identifiable data.
    Or we make sure to scrub away any location information. It never even enters our
    system and therefore the data is safe.” Those guardrails enable democratization
    of the data and enable people to extract insights.
  who: Uri
- line: The tricky thing about insight — you don’t know what you don’t know. You may
    not know that if you collect the playback events of a music app, then   suddenly
    a year later you can predict trends in music. That’s valuable. Then you can replenish
    your catalog and you can make more attractive music.
  who: Uri
- line: Now, since we are talking about tooling, there are mechanisms that allow you
    to do it. Jessi mentioned how you can make email available for everyone but make
    sure that when somebody accesses data, they can easily mass-mail about the new
    couches. But the system makes sure that only those people who opted in for email
    communications will actually get the notification.
  who: Uri
- line: There are other things like training machine learning models. Many machine
    learning models don’t need personal emails. They do need a way to identify this
    is person A, this is person B. You can hash the emails. Hash in a one-way function
    which creates a unique identifier, but makes sure that you do not expose any personal
    information. You still can differentiate between humans to do things like count
    distinct and aggregate by and so on. This will create a hopefully useful machine
    learning model to predict shopping plans.
  who: Uri
- header: Implementing policies
- line: So, these policies are “it can be accessed”, “it cannot be accessed”, “which
    team can access it”, “this should be hashed”, “this should not be hashed”. Is
    it something that is implemented on top of the catalog? Or is it built into the
    catalog? How does it usually look in practice?
  sec: 2704
  time: '45:04'
  who: Alexey
- line: There are variations. There are systems that say “you should access all data
    through the catalog”. The catalog will normalize everything. The catalog will
    be your workbench. The catalog also cares for how the data is shaped before you
    see it. It maintains those guidelines. That’s one approach. The thing I like about
    this approach is it’s a central point for governance. It equalizes all the data.
    The downside is, it puts a constraint about the tools you can use. You can only
    use the catalog as an interface or tools that interface with the catalog.
  sec: 2728
  time: '45:28'
  who: Uri
- line: I’m a little bit biased here, but I’d recommend a system that makes sure the
    actual storage system implements the governance — with a control plane and the
    dashboard and so on.
  who: Uri
- line: By doing it in storage, implementing governance means you can use any tool
    that can access the storage and still be safe. That opens up compatibility with
    much more tooling. At the end of the day nobody should be working to figure out
    the guidelines. They should be invisible. And they should enable you to use whatever
    tool you want to do to generate the business purpose you came to the data for.
  who: Uri
- header: Shopping-card experience for requesting data
- line: But there should be some central place where I as an analyst or I as a data
    scientist can go and say “I need this piece of data”. Then somebody, a lawyer
    or data protection officer, or data producer, can evaluate my request and say
    “You don’t really need this data, use this instead” or “Your use case is valid,
    the access is granted”. We need a tool that allows that. Should it be on top of
    the catalog or elsewhere?
  sec: 2822
  time: '47:02'
  who: Alexey
- line: It can be on top of the catalog. It can be on top of the storage. It can be
    agnostic to both. We recently launched a product called Dataplex. I’m biased,
    but it’s a good example. Dataplex sits beside all the storage systems in Google
    and tells you, “These users have access to this data. Are you happy about this?”
    and “This data is accessible for these users. Are you happy about that?”.
  sec: 2855
  time: '47:35'
  who: Uri
- line: There are other systems. Just to give a shout out to Collibra for example,
    which is a data catalog data governance system. They implement a shopping cart
    experience, which is as you described. I need the financial information for the
    last two years in order to perform the analysis. I searched for financial information
    in the last two years. I am presented with certain data mods. Now I can request
    access to that. You get a shopping-cart-like experience with authorizing and auditing.
    This is another concept of data governance, which records this transaction, which
    is also important.
  who: Uri
- line: Alexey, a lot of what you were describing, it’s manual too. As Uri said, you
    have to have people involved. That’s important. But think about how much of this
    can I automate or make easier for myself. I have classified my data. I have added
    tags. These tags do certain things with the data. Then it’s not on us, the data
    producer.
  sec: 2930
  time: '48:50'
  who: Jessi
- line: We have talked to a lot of data producers or data engineers who spend so much
    time dealing with requests of analysts and data scientists, wanting this data
    set. Why do you need it? They give it to them and then they don’t use it. I am
    sure many people are familiar with that.
  who: Jessi
- line: When implementing this process, make some of that not so manual. If that is
    a tool that you use or just the way that you have classified it and tagged it.
    That will help you also.
  who: Jessi
- header: Proving the value of data catalog
- line: Thank you. We have a question. It’s also about the data catalog. How can we
    systematically evaluate data governance initiatives such as having a data catalog
    for data access? How can we prove their value to the business?
  sec: 3019
  time: '50:19'
  who: Alexey
- line: 'I would go back to the business objectives. Start at the highest level. You
    are storing a lot of data. You are spending effort and compute resources — it
    costs money to process this data. You can use the catalog to answer this question:
    “What’s the relationship between the money you spend on storing the data and the
    usage of that data?”. The catalog can answer it and show you the most used tables.
    Then you can make decisions such as “There’s a lot of data that nobody is touching.
    Let’s move it to cold storage, which is cheaper.” That could be one way.'
  sec: 3036
  time: '50:36'
  who: Uri
- line: There is another way. I am subject to a regulation. This regulation can take
    a bite out of my revenues, if I do not comply. How do I comply easily, cheaply,
    without a lot of audit and manual labeling?
  who: Uri
- line: If you go back to “what governance do I need?”. A lot of times folks think
    they have to have this entire governance program. They need all these tools and
    this storage and all this head count. It’s super complicated and super expensive.
    And then your C-suite says “Hell, no. That’s way too much. We are not going to
    do that.” Oftentimes that’s where this question comes from. But if you can look
    at what is the minimum. We wrote a book on this. So, we don’t think data governance
    should be a bare minimum thing.
  sec: 3113
  time: '51:53'
  who: Jessi
- line: But if you are trying to implement something, you need to start somewhere.
    Look at what is that minimum that doesn’t require a huge amount of head count,
    that doesn’t require a lot of manual stuff and a ton of expensive tools. That’s
    the place to start.
  who: Jessi
- line: As Uri said, once you can start doing some of these things, once you can start
    showing the value of it. We have all this data. Now we are able to get more insights
    from it. Then it will start to sell itself. Then you can see how I expand from
    there.
  who: Jessi
- line: How to find this minimum?
  sec: 3188
  time: '53:08'
  who: Alexey
- line: Again, look at your business objectives. I need data governance. Fine. Why?
    Because regulation. Because insights. Because things. Determine that from your
    objective. What you need to solve for successfully will be that minimum. The maximum
    will be how do I solve this in a way which is future-proof, caters for buying
    other business units or accumulating 10x data from YX sources. That will be the
    maximum. That’s the difference between planning for now and planning for the future.
    As a general approach, in the world of lean startups, you need to plan for “now”
    plus 1x. Because you do not want to be surprised.
  sec: 3201
  time: '53:21'
  who: Uri
- line: That makes sense. For the first iteration, you plan as much as possible for
    now, but allow yourself to also plan for the future a bit. Don’t be so ambitious.
    Then prove that this thing is valuable and only then expand. Right?
  sec: 3255
  time: '54:15'
  who: Alexey
- line: Yes.
  sec: 3274
  time: '54:34'
  who: Uri
- header: Using data catalog
- line: We have a question from Danish. Could you explain with examples what a data
    catalog could contain and how we can leverage it? We talked a bit about it.
  sec: 3277
  time: '54:37'
  who: Alexey
- line: Here is what I want data catalog to do for me. I want data catalog because
    it has a lot of technical metadata information associated with data — table names,
    data set names, column names. Let’s begin with that. Collect all that, index all
    of that, do it without effort or with little effort. If I have a new table and
    I need to go to the data catalog and register that table — that becomes the manual
    labor you, Alexey, mentioned earlier. I don’t think anybody wants a data catalog
    that creates more work for you.
  sec: 3296
  time: '54:56'
  who: Uri
- line: The better data catalog has a logical layer or business layer on top of this
    technical information. A lot of my data contains information about customers.
    Here is a customer entity, it includes these kinds of things. Customer entities
    can be found in these systems, in these datasets, in these tables.
  who: Uri
- line: Catalogs also usually care for lineage of the data. That’s another kind of
    metadata which says where the data came from, where the data is going next. They
    do this by both analyzing your SQL and data warehouse as well as analyzing other
    flows of data in and out of your organization. Obviously we want to be able to
    search rather than list all of this data. Those are like the core things, the
    features I see in many partners.
  who: Uri
- line: Democratizing data quality is an interesting trend. People can five star certain
    data sets, if they are happy with them or not. Shopping-cart experience which
    we mentioned earlier. Policy management is sometimes a part of a data catalog,
    sometimes not because you already have a view of your data. Many data catalogs
    also include additional business metadata. For example, I don’t only want to know
    if there is a customer entity. I also want to add if that’s an internal customer
    or external customer information. Those are things that are normally found in
    a catalog.
  who: Uri
- line: Again, think about the catalog as the dictionary that leads you to all of
    your data — where it is and what it means. So, you go from a table in a dataset
    to what does this table mean, where did it come from, who uses it, how often can
    you use it. That will be the kind of information in a data catalog.
  who: Uri
- header: Data governance = data catalog?
- line: I think most of the time today we spend talking about data catalog. I am wondering,
    is data governance all about having this data catalog? Or are there other things
    that are important?
  sec: 3466
  time: '57:46'
  who: Alexey
- line: We talked about even more basic concepts as well. Data is stored somewhere.
    That’s something the catalog often scrapes. Data is processed somewhere either
    in a data warehouse or data analytics engine. Those are things that are part of
    your strategy. Then, there’s a policy engine which is either part of the storage
    system or a data catalog. Data catalog became synonymous with data governance
    because it’s a tool used by two groups — data analysts and data stewards. Each
    of them has a different purpose in mind. One understands the data in order to
    query it. The other understands the data in order to govern it. That’s why a lot
    of data governance tools exist in the catalog or have catalog as a part of it.
  sec: 3485
  time: '58:05'
  who: Uri
- header: Wrapping up
- line: We should be wrapping up. Anything else you want to mention before we finish?
  sec: 3544
  time: '59:04'
  who: Alexey
- line: Thank you for having us. This was great!
  sec: 3552
  time: '59:12'
  who: Uri
- line: Yeah. This is fun!
  sec: 3554
  time: '59:14'
  who: Jessi
- line: Any tips?
  sec: 3557
  time: '59:17'
  who: Alexey
- line: Read the book.
  sec: 3560
  time: '59:20'
  who: Uri
- line: How can people find you, if they have questions?
  sec: 3564
  time: '59:24'
  who: Alexey
- line: I know we are both on LinkedIn. That is probably, at least for me, the easiest
    way.
  sec: 3574
  time: '59:34'
  who: Jessi
- line: LinkedIn, Twitter, and the normal communications channels we all have.
  sec: 3583
  time: '59:43'
  who: Uri
- line: Thanks a lot for joining us today, for sharing your knowledge. Thanks everyone
    else for joining and listening, for asking questions.
  sec: 3594
  time: '59:54'
  who: Alexey
- line: Thank you too.
  sec: 3640
  time: '1:00:40'
  who: Jessi
- line: Bye.
  sec: 3640
  time: '1:00:40'
  who: Alexey
- line: Bye.
  sec: 3640
  time: '1:00:40'
  who: Uri
description: 'Learn data governance in the cloud: build data classification, catalogs
  & policies, automate tagging, add stewards and measure ROI for trusted, compliant
  data'
intro: 'How do you build data governance in the cloud that enables access, meets regulation,
  and demonstrates ROI? In this episode Jessi Ashdown, Senior UX Researcher for Google
  Cloud, and Uri Gilad, Product Manager for Data Governance at Google Cloud, walk
  through practical approaches to data governance in the cloud—grounded in real user
  research and product experience. <br><br> They define governance beyond security
  and PII, explain how GDPR and high-profile events like Cambridge Analytica accelerated
  adoption, and outline the core components: people, processes, and tools. Key topics
  include data classification and taxonomy, building scalable data catalogs versus
  spreadsheets, policy design (retention, freshness, purpose-based access), enforcement
  models, and access workflows. They cover roles such as data stewards and producers,
  data quality signals, automation (tagging and requests), and what to measure for
  ROI—catalog metrics, cost versus usage, and compliance value. You’ll also hear an
  MVP strategy for minimum viable governance and what to include in a catalog (technical
  metadata, lineage, business glossary). <br><br> Listen to gain actionable steps
  to scope a cloud data governance program, prioritize by the “why,” and implement
  classification, catalogs, and policies that balance control and democratized access.'
---

Links:

- Book: <https://www.oreilly.com/library/view/data-governance-the/9781492063483/>{:target="_blank"}
- Jessi's LinkedIn: <https://www.linkedin.com/in/jashdown/>{:target="_blank"}
- Uri's LinkedIn: <https://linkedin.com/in/ugilad>{:target="_blank"}
- Uri's Twitter: <https://twitter.com/ugilad>{:target="_blank"}
