---
episode: 5
guests:
- sahilwalia
ids:
  anchor: datatalksclub/episodes/Decoding-the-Open-Lakehouse---Sahil-Walia-e3ou705
  youtube: k4A1TvfSdKw
image: images/podcast/s25e05-decoding-open-lakehouse.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/Decoding-the-Open-Lakehouse---Sahil-Walia-e3ou705
  apple: https://podcasts.apple.com/us/podcast/decoding-the-open-lakehouse-sahil-walia/id1541710331?i=1000790552313
  spotify: https://open.spotify.com/episode/7e99CVsd78K5zJWFPWMzLM?si=544eca21284b4b2f
  youtube: https://www.youtube.com/watch?v=k4A1TvfSdKw
season: 25
short: Decoding the Open Lakehouse
title: Decoding the Open Lakehouse
transcript:
- header: Defining the Modern Data Platform
- line: Hi everyone. This is our PK event. We have an interview. If you want to find
    out about the events we have there is a link in the description. Check it out.
    You will see all the events we have in our pipeline. Like the video, subscribe
    to our YouTube channel. There is also a Slack community where you can hang out
    with other data people with us. The link is also in the description. If you have
    any questions there is a pinned LinkedIn live chat.
  sec: 0
  time: 0:00
  who: Alexey
- line: Click on that link to ask your questions and we will be covering these questions
    during the interview. Today we will talk about open lakehouse. We have a very
    special guest today Sahil. Sahil is a senior technical architect at Snowflake
    where he works with enterprise customers running Apache iceberg lake houses with
    a focus on data engineering and AI ready platforms. He is also a maintainer of
    Schema Change, an open source database migration project with nearly 500,000 downloads
    per month.
  sec: 28
  time: 0:28
  who: Alexey
- line: He also contributes to Apache OSI an open source project for centralizing
    semantic model exchange. For me this interview is especially interesting because
    I am not professionally a data engineer. I have done a lot of data engineering
    as a data scientist just because I needed it. In order to create a project and
    make sure a data science project runs I needed to do a lot of transformation.
    I needed to do a lot of work in Spark and Presto and similar things.
  sec: 52
  time: 0:52
  who: Alexey
- line: I am a bit out of touch with all these modern things. Sahil it is very nice
    to have you here we can talk about all these things that modern data engineers
    need to use. Welcome to our interview.
  sec: 89
  time: '1:29'
  who: Alexey
- line: Thanks for having me. I am super excited.
  sec: 101
  time: '1:41'
  who: Sahil
- line: Make it a bit louder I can hear you well. Now it is great. Before we start
    and go into our main topic to talk about open lakehouse I want to talk about some
    of these libraries that you maintain and contribute to. I want to learn more about
    your background. Can you tell us more about your career journey so far?
  sec: 104
  time: '1:44'
  who: Alexey
- line: Sounds good. Absolutely. Hey everyone my name is Sahil. I am based out of
    the northeast US. It is right at six thirty in the morning.
  sec: 126
  time: '2:06'
  who: Sahil
- line: I am very fresh right now and very excited. Good morning. Let us start with
    my background. I have been in the industry for over a decade now especially doing
    data engineering. My job essentially started just any other SQL heavy role very
    much analytics heavy.
  sec: 134
  time: '2:14'
  who: Sahil
- line: I was doing a lot of reporting and those kind of things. Early on when I started
    I was building reports writing simple SQL queries and learning joins. I was very
    new and enjoying that. Then I moved on to other roles wherein for example one
    of my roles at Ernst Young was automating parts of the gap reporting. They have
    some codes that they have to comply with where correctness really mattered in
    terms of not only the data having to be correct but also performing well.
  sec: 155
  time: '2:35'
  who: Sahil
- line: That is how I started building. Then I moved to a company called Slalom in
    the consulting space. I was architecting modern data lakes moving heavy legacy
    systems to newer systems at that time say Snowflake. I was building those important
    pipelines and data quality frameworks. My role over the years got more technical
    and I realized that I am more of a technical person who enjoys that.
  sec: 187
  time: '3:07'
  who: Sahil
- line: That kept happening and then I noticed that a lot of companies are dealing
    with many engines that have many opinions. Each engine has its own opinions on
    how they want files to be structured how they want performance to be curated how
    they want pruning to happen and those kind of things. That basically led me to
    all of this. Anyway I am at Snowflake right now as you mentioned Alexey. I am
    a senior technical architect here.
  sec: 219
  time: '3:39'
  who: Sahil
- line: I have been here since 2024. I directly work with customers who run Apache
    Iceberg lakehouses. I am usually in the room talking mostly about data engineering
    and adjacent fields. We discuss what will consume the data where the data will
    come from how the pipelines would run and most of the times performance. We figure
    out how we make things better cheaper and faster.
  sec: 248
  time: '4:08'
  who: Sahil
- line: That is pretty much about it. As time permits I try to contribute to Schema
    Change a very new project Apache OSI. I started contributing there. It is a very
    new community that I started working at.
  sec: 272
  time: '4:32'
  who: Sahil
- line: That is really nice. You mentioned that one of the things I noticed when you
    were describing your career was that when you were consulting you were helping
    clients build modern data lakes. I have heard this term modern data platform.
    It has been around for quite some time. What do we understand by the term modern
    data platform and how modern is it actually?
  sec: 290
  time: '4:50'
  who: Alexey
- line: This term has been around for quite some time. Is it still modern or do we
    just not have a better name for that?
  sec: 316
  time: '5:16'
  who: Alexey
- line: I think that is a very fair question and it is modern in the context of where
    you are living. I will give you an example. There was a time when X platform or
    Y platform was modern at that time but as technology evolved a lot of those platforms
    did not evolve with it. A lot of things keep evolving.
  sec: 324
  time: '5:24'
  who: Sahil
- line: Is this modern data platform more about technologies or is it also about the
    approach and how we do this? What is not modern or what is the old data platform?
    I guess the term modern data platform appeared because there was an old way of
    doing this. Now we say there is a new way of doing this and we call it a modern
    data platform.
  sec: 357
  time: '5:57'
  who: Alexey
- line: I would not specifically say a technology I would say the way of doing things.
    We started with data warehouses then we moved to lakehouses and now we are in
    the interoperable lakehouses world. Data warehouses were mostly schema on write
    and mostly transactional. Then we had the world of lakehouses wherein people were
    just dumping data into S3 buckets but there was no structure around it. There
    were no good practices around it.
  sec: 381
  time: '6:21'
  who: Sahil
- line: When we evolved we arrived at the current state which I would say is interoperable
    open lakehouses. Interoperable means that you want your data to be decoupled from
    compute. Your storage is decoupled from your compute and you are also making it
    open. Data engineering is very much motivated by what is happening in open source.
    A lot of things that happen in data engineering are inspired by open source.
  sec: 412
  time: '6:52'
  who: Sahil
- line: For example storage is Parquet which is open source. Compute starts with Spark
    which dictates a lot more things. Similarly table formats for example Iceberg
    are open formats. They tell you how you can move faster. Companies like Snowflake
    maintain so much rich metadata on top of these open platforms that make them even
    more modern.
  sec: 453
  time: '7:33'
  who: Sahil
- line: What is the more modern part here and what exactly do we compare? Previously
    one option we had was dumping all the data into whatever object storage we have.
    We figure out how exactly to translate it and let analytics engineers model this
    so they can do analysis. Is this what the modern approach is or is it something
    else?
  sec: 488
  time: '8:08'
  who: Alexey
- line: This is a very difficult question to give one definition for. Modern can mean
    several things here. For example does it deliver to your modern sinks? Previously
    a lot of the analytical work we were doing as data engineers was mostly for reporting.
    Now it has evolved that your files or any data you prepare has to be ready for
    ML pipelines.
  sec: 523
  time: '8:43'
  who: Sahil
- line: When we say modern we want to make sure it is contemporary which means it
    meets today's needs. Second are we making sure the platform we use does not lock
    you in? Object storage is your IP and that is where your things live. You should
    be flexible so as things become more contemporary there will be a new technology
    tomorrow. You still own your data and you just port it there.
  sec: 555
  time: '9:15'
  who: Sahil
- line: Let us talk about this lock in part. Let us say I store data in Oracle and
    I do not have this interoperability because my compute and storage are the same
    thing. Once I keep my data in Parquet and store my data in S3 or Google Cloud
    Storage I can run whatever can reach this Parquet to do the analytics for me.
    Many engines can actually do that. Are we aligned?
  sec: 603
  time: '10:03'
  who: Alexey
- line: Yes. You decoupled the storage and the compute. Now you have all the leverage
    you need from an architectural point to move things to a different layer or do
    compaction on the files. We can talk a little bit more about that when we dive
    into Iceberg but essentially you now own your own world. In the old world if you
    wanted to do something architecturally with the data on the physical layer you
    could not do it because you could not control the packaged platform.
  sec: 633
  time: '10:33'
  who: Sahil
- line: Now that is going away. A lot of companies using these platforms are pushing
    the open source community because we need something where we own the data. We
    can do things around it and become more independent.
  sec: 674
  time: '11:14'
  who: Sahil
- header: What Exactly is a Lakehouse?
- line: Now I have a system generating a lot of JSON events. I just dump them to S3
    and run Presto on top of that. Do I already have a lakehouse or is there more
    to a lakehouse? If I take this JSON and convert it to Parquet is it already a
    lakehouse or not yet? What actually is a lakehouse and where does it start?
  sec: 694
  time: '11:34'
  who: Alexey
- line: When you ask that question let us think through this. What you are describing
    is a file storage. Parquet is very rich in metadata. It has file statistics showing
    this is columnar storage and it has its own row groups to maintain data. Parquet
    is very good and you get all the things you need from your data file.
  sec: 721
  time: '12:01'
  who: Sahil
- line: Now let us talk about an engine. Let us take Spark as an example. How would
    Spark know what file to read? How would Spark know what file to prune? We need
    a few additional things around here like a catalog.
  sec: 765
  time: '12:45'
  who: Sahil
- line: I can come to the catalog in a bit but we also need some metadata about the
    data. Metadata by definition is data about data. When we come into this world
    of open lakehouses you need some data around these files. You have ten files but
    what are they about? Are those about orders customers or revenue?
  sec: 784
  time: '13:04'
  who: Sahil
- line: Which one are the latest files? From a logical aspect you need metadata about
    it. Now let us come to the catalog. The simplest way of explaining a catalog is
    telling an engine where your latest state of that table exists. You started with
    a small company with one hundred customers but now you have a thousand customers.
  sec: 814
  time: '13:34'
  who: Sahil
- line: You want to make sure when you are querying today you get the thousand customer
    list not the one hundred customer list. You should still have the ability to go
    back in time to see those one hundred customers too. That is the job of the catalog.
    To answer your question Parquet are just files but you need a little bit more
    metadata on top that gives you clarity or navigability within the data for the
    engines.
  sec: 838
  time: '13:58'
  who: Sahil
- line: If I understand you correctly with Spark you can just point it to read from
    an S3 location. You give it an explicit path so there is no catalog involved.
    You just say there are some files here read them process them and save the files
    in another S3 location. If we want to query customers where join date is 2026
    this will not work without a catalog. We need the mapping from these table names
    and partition names to the actual data.
  sec: 863
  time: '14:23'
  who: Alexey
- line: That is some of what the catalog is doing. Let us take your previous example
    when just looking at S3 storage. You are doing the work because you know that
    S3 location but the engine does not. When you do a select star from a table you
    are not doing anything you are just focused on what you want to get the results
    out of. The very simple way of thinking about a catalog is it is the location
    where your latest file exists.
  sec: 914
  time: '15:14'
  who: Sahil
- line: That is not the only thing it does. Alexey is querying that data because he
    owns the company. What if I am querying that data but I do not own the company?
    I should not be going to those data files so I need to have controlled access.
    Permission management is another thing it does.
  sec: 953
  time: '15:53'
  who: Sahil
- line: Now let us say YouTube is querying that particular file and you want to query
    that from Apple Podcast platform as a different engine. That other engine should
    not have access unless you specifically grant it. You might just want to provide
    a timed access to go to a specific location for only sixty seconds. Those are
    the kind of things that a catalog will additionally do. Iceberg is rich metadata
    about the files.
  sec: 977
  time: '16:17'
  who: Sahil
- line: When you talk about querying where dates are greater than or year is less
    than those are the kind of things Iceberg will handle. It will do all the magic
    behind the scenes because it maintains a tree structure for the metadata. It goes
    into the nested layers and only gives you the data you need efficiently.
  sec: 1010
  time: '16:50'
  who: Sahil
- header: Comparing Hive Metastore and Apache Iceberg
- line: I remember using Hive catalog and Glue catalog. They have been around for
    quite some time before Iceberg even appeared. I know that with Hive and Glue you
    can have this mapping from table names to file names. Can we already do permission
    management with Hive and what does Iceberg add on top of these things?
  sec: 1040
  time: '17:20'
  who: Alexey
- line: I will start by saying I do not have a ton of experience with Hive but I think
    you are talking about Hive metastore. Hive metastore maintains the naming mapping.
    In Iceberg it is very different and very advanced. It can do that plus extra things.
    The way it started was to resolve a lot of things at Netflix.
  sec: 1073
  time: '17:53'
  who: Sahil
- line: Netflix was going through a lot of issues having petabyte scale data. They
    just could not reach the right file at the right time. With Hive if you want a
    certain file sitting in an S3 bucket with a thousand files it has to read all
    thousand files under that sub path. It was not rich in metadata. With Iceberg
    it maintains a metadata JSON file at the very top level.
  sec: 1102
  time: '18:22'
  who: Sahil
- line: It talks about the latest state of the data called a snapshot. Within that
    snapshot it has manifest lists containing what file got changed and how many rows
    were added. It maintains file min and max values and then goes to the file level
    statistics. It does not have to do HTTP calls to list S3 contents every time to
    see what is going on. It will just go to its own metadata first to know what the
    files have and then only go to that specific file.
  sec: 1151
  time: '19:11'
  who: Sahil
- line: That is clear. At the end Iceberg is something similar to this Hive metastore
    but we have more granularity. We know more about where the files are.
  sec: 1201
  time: '20:01'
  who: Alexey
- line: I will explain that but I would segregate it into two things. Iceberg by itself
    is a table format. When we say Iceberg it is not a catalog it is a table format.
    The Iceberg REST catalog is an open API that is more similar to Hive metastore
    for clarity.
  sec: 1218
  time: '20:18'
  who: Sahil
- line: From what I understood there is a REST API that you can query. Let us say
    I want to calculate revenue for customers that joined this year. If I have a lot
    of customers like Netflix I need to be able to include customers that just joined.
    If they are joining a lot I need that granularity to know to include these customers
    when executing the query. The metadata manifests contain this information and
    all of that I can get through this REST API.
  sec: 1242
  time: '20:42'
  who: Alexey
- line: Correct.
  sec: 1289
  time: '21:29'
  who: Sahil
- line: At the end is it just a bunch of Parquet files or is there something else?
    The catalog is one thing and then we have Parquet and that is Iceberg. Are these
    correct?
  sec: 1289
  time: '21:29'
  who: Alexey
- line: Yes. The data is Parquet files. Your metadata file is one JSON file. You have
    some Avro files which maintain the data about the manifests. The metadata has
    pointers to the Avro files.
  sec: 1303
  time: '21:43'
  who: Sahil
- line: Ninety percent would be your Parquet files and you do not maintain any of
    the other places. That is something your Iceberg engine manages and it automatically
    creates when you integrate. You just need to take care of how you manage your
    data engineering pipelines.
  sec: 1327
  time: '22:07'
  who: Sahil
- header: Handling GDPR and Data Deletions in Iceberg
- line: I remember when I needed to create a lot of data pipelines and all our data
    was in Parquet files the biggest problem was GDPR. What if somebody wants to be
    removed from the data of the company? It meant that we would actually need to
    go through all the Parquet files and recreate them. Does Iceberg solve this problem
    or make it cheaper?
  sec: 1354
  time: '22:34'
  who: Alexey
- line: GDPR is very strict. As I understand you need to delete the files as well
    not only the customer data to be forgotten. Iceberg is very strong at saying this
    is a particular file I do not want to reference anymore. It can create a delete
    file. It is very smart and will not touch your data files.
  sec: 1372
  time: '22:52'
  who: Sahil
- line: It will create a separate small protobuf file and attach it to that actual
    file. Whenever the engines are reading they will combine the statistics. It knows
    the whole file but understands it needs to delete these specific records and provides
    the readers the accurate picture at that time. That is what it does at the logical
    layer.
  sec: 1418
  time: '23:38'
  who: Sahil
- line: Your data still is in the physical file. In case you need to actually delete
    the file you have to do a little bit of operations. You delete the file and create
    a new file without the deleted data.
  sec: 1445
  time: '24:05'
  who: Alexey
- line: This thing is called a tombstone. I remember reading about tombstones in Designing
    Data Intensive Applications. The book describes this approach where you do not
    delete but create a tombstone so the data is kept there but cannot be accessed.
    At some point maybe once per month you collect all the tombstones and create a
    small file without any tombstones. I think it is called compaction and Iceberg
    can do this. Is that accurate?
  sec: 1460
  time: '24:20'
  who: Alexey
- line: Exactly. Iceberg does do that and it is very good at it. Let us look at any
    managed offering here from a data engineer perspective. You are a data engineer
    who wants to work with data and make sure pipelines run. Dealing with orphan files
    or managing storage accumulation is something you do not really enjoy.
  sec: 1500
  time: '25:00'
  who: Sahil
- line: These things are very trivial in nature and you do not learn anything from
    doing them every week. Data engineers do not enjoy it especially when things go
    wrong and you get pager alerts. Managed offerings have all of these things automated
    so they will take care of all of this for you. You just define a few things and
    that is the route I usually recommend if you do not want to take that burden.
    You still get the data that is yours but with a more relaxed mind.
  sec: 1539
  time: '25:39'
  who: Sahil
- line: It is just like having a lawn mower but paying someone to come and mow your
    lawn. That is the way I would think about it.
  sec: 1581
  time: '26:21'
  who: Sahil
- line: Apache Iceberg gives us this catalog and extra things on top of that like
    this compaction mechanism. It makes the lives of data engineers easier so they
    do not need to worry about all these things. In addition to Apache Iceberg it
    can give us what we call a lakehouse. If I have a setup where my files are in
    this format and I can query data using whatever agent that can access this data
    then I have a lakehouse. Are we aligned?
  sec: 1592
  time: '26:32'
  who: Alexey
- line: Correct. It makes everything open for you and it is one of the components.
    A lakehouse by definition is not just Apache Iceberg but Iceberg enables it. It
    has to have open storage like S3 or MinIO but I think you covered it all.
  sec: 1629
  time: '27:09'
  who: Sahil
- header: Apache Iceberg vs. Delta Lake
- line: What is a Delta Lake? Is it an alternative to Iceberg or what is it exactly?
  sec: 1653
  time: '27:33'
  who: Alexey
- line: Delta Lake essentially came before Iceberg. Iceberg is relatively popular
    and the community has converged now that Iceberg is leading the way. Delta was
    started as open source and Delta lakes are based on Delta files. It was very well
    adopted but then Iceberg came in. Databricks is very much invested there which
    is why I am hesitant to talk too much about it.
  sec: 1659
  time: '27:39'
  who: Sahil
- line: I want to make sure I do not do injustice but the community has converged.
    Databricks does support Iceberg as well but there are a few challenges. Overall
    Delta Lake was good but Iceberg is generally considered more open. It was not
    driven by one particular vendor like Databricks or Snowflake. A lot of commits
    at Delta were motivated by Databricks but anyone can participate in Iceberg.
  sec: 1698
  time: '28:18'
  who: Sahil
- line: As a matter of fact Iceberg founders Daniel Weeks and Ryan Blue work for Databricks
    today. We have committers from Snowflake Apple Netflix and LinkedIn. Now it is
    truly a community project. It is truly open source and the Apache licensing is
    pretty strict.
  sec: 1758
  time: '29:18'
  who: Sahil
- line: As I understood with Apache Iceberg I can keep data in whatever object store
    and use whatever compatible engine. It can be Snowflake Databricks or BigQuery
    if they support it. I do not have this lock in. You mentioned interoperability
    and with Apache Iceberg I can get it.
  sec: 1782
  time: '29:42'
  who: Alexey
- line: That is right.
  sec: 1806
  time: '30:06'
  who: Sahil
- line: I actually wanted to talk about open lakehouse. Right now I have openlakehouse.io
    open in front of me. Are you somehow affiliated? What is open lakehouse and what
    is openlakehouse.io?
  sec: 1811
  time: '30:11'
  who: Alexey
- line: I think it is a company I am not familiar with to be very honest. Is that
    what you are looking at?
  sec: 1831
  time: '30:31'
  who: Sahil
- line: Yes it is sponsored by Databricks. I guess that is why you are not aware of
    them perhaps. What is an open lakehouse?
  sec: 1841
  time: '30:41'
  who: Alexey
- line: We did talk about lakehouses. Just a reminder for everyone a lakehouse is
    anything where you have structured and unstructured files that you can put in.
    The challenge was they were not very open and you wanted to do a lot more with
    your data. You wanted other applications to read it and write to it but you got
    stuck with one specific engine. An open lakehouse provides all those features
    where you can dump your data and organize it with rich metadata.
  sec: 1851
  time: '30:51'
  who: Sahil
- line: You have compaction time travel and ACID compliance. Lastly it can be plugged
    into any engine that supports the specification. The specification contains the
    rules on how data should be accessed written deleted and merged. One dilemma I
    want everyone to be aware of is that when we say open the focus is that data is
    open and can be accessed by other teams.
  sec: 1897
  time: '31:37'
  who: Sahil
- line: Iceberg tells you what things you can do in order to write or read. Write
    could mean updating a record merging a record or adding files. Both engines would
    say they can write to Iceberg but the definitions may be different. I would just
    suggest focusing on what your team does today or will do in the next few years
    and what kind of operations you need. Have a matrix to see what you want to achieve
    and whether a particular platform delivers that.
  sec: 1946
  time: '32:26'
  who: Sahil
- line: A lot of customers later realize a platform only supports features at a certain
    level. It does not mean they will not support it eventually but each engine has
    to come to that state of maturity. Open source leads it but ultimately engines
    have to implement it and think from their ecosystem perspective.
  sec: 2012
  time: '33:32'
  who: Sahil
- header: Do You Need a Lakehouse for Small Data?
- line: I have a more practical question in mind. Let us say I want to build an open
    lakehouse. Let us take DataTalks.Club as an example. We have a few thousand events
    per day mostly people coming to the website and browsing. We also have a learning
    platform where people submit their homework.
  sec: 2041
  time: '34:01'
  who: Alexey
- line: I want to do some analytics on top of that. I want to understand what people
    are doing and how to convert visitors to community members. If people are doing
    the homework I want to know how to make them more successful. I want to have dashboards
    to understand where we are. Do I need a lakehouse for this?
  sec: 2074
  time: '34:34'
  who: Alexey
- line: Is this scale large enough to actually think about adopting Iceberg or do
    I need to be Netflix?
  sec: 2108
  time: '35:08'
  who: Alexey
- line: That is a very good question. At your scale if you are dealing with less than
    ten million records overall you should not even think about Apache Iceberg.
  sec: 2117
  time: '35:17'
  who: Sahil
- line: If my dataset fact tables contain less than ten million I should not even
    think about Apache Iceberg?
  sec: 2138
  time: '35:38'
  who: Alexey
- line: Iceberg makes you open and provides analytics but it has its own management
    layer too. When you are a smaller team doing things at a smaller level you do
    not want a lot of complexity unless you really need your data to be open. If you
    only have under one million records why would you go through all of this setting
    up just to get to the analytics?
  sec: 2147
  time: '35:47'
  who: Sahil
- line: It is not a one click setup that I am looking at. I need this REST catalog
    and there are some things on top of that.
  sec: 2192
  time: '36:32'
  who: Alexey
- line: To be very clear in Snowflake if you run a create table statement you just
    need to mention the catalog equals Snowflake. Snowflake will handle all of it
    even the storage for you. You do not have to connect to your S3 or any special
    catalog. It is very simple but the question is do you want it at your scale? A
    lot of companies are actually choosing to do it right now because they know they
    will grow tomorrow.
  sec: 2201
  time: '36:41'
  who: Sahil
- line: Keep in mind it is a managed offering. The benchmarks tell that Snowflake
    performance is essentially the same for Iceberg tables compared to standard Snowflake
    tables. Another challenge you face with Iceberg is that query performance is generally
    slower than a standard engine. There have been a lot of performance improvements
    and the difference was only ten to twenty percent in some benchmarks. If you are
    serving a team where wait times matter ten to twenty percent is still a lot.
  sec: 2239
  time: '37:19'
  who: Sahil
- line: There was another thing and I probably should let you finish before I ask
    the follow up.
  sec: 2300
  time: '38:20'
  who: Alexey
- line: Another thing is if you are getting a lot of streaming data it creates a lot
    of metadata files every time you commit. Sometimes your actual Parquet data files
    are smaller but the accumulated metadata is higher. That is not a good approach
    so we encourage balancing it out by using a Kafka queue and committing on a schedule.
    If it is a smaller data set and high frequency commits I would not recommend it.
  sec: 2307
  time: '38:27'
  who: Sahil
- line: In my case I would be better off just having a separate Postgres and doing
    analytics there. When I have ten million records in my fact tables then I can
    think about what makes sense for me to do later.
  sec: 2358
  time: '39:18'
  who: Alexey
- line: Absolutely.
  sec: 2375
  time: '39:35'
  who: Sahil
- line: I see a few questions and this is what I wanted to cover. You contribute to
    Apache projects like OSI. It was renamed to open semantic interchange.
  sec: 2377
  time: '39:37'
  who: Alexey
- line: I contributed to a few PRs. It is still incubating so it is not a full Apache
    project yet.
  sec: 2396
  time: '39:56'
  who: Sahil
- header: Understanding Apache OSI (Open Semantic Interchange)
- line: Can you tell us more about this project?
  sec: 2411
  time: '40:11'
  who: Alexey
- line: Let us take an example where Alexey queries revenue for the last ten days.
    That is the only question Alexey asked but the definition could mean so many things.
    Does it include business days or not? Do I need to make sure the revenue includes
    tax or not? In technology several platforms consume the data but in the world
    of LLMs definitions may vary.
  sec: 2414
  time: '40:14'
  who: Sahil
- line: When a model queries your table you want to make sure the returned result
    is as deterministic as possible. It should not be fluctuating when queried differently.
    The core thesis here is defining how your semantic view should look. You are defining
    trusted queries and how specific questions should be answered. These are the dimensions
    the metrics and how calculations will be done on top of it.
  sec: 2463
  time: '41:03'
  who: Sahil
- line: These definitions can live in different engines but you want them to be portable.
    Today you have a semantic view defined in Snowflake but you want dbt or Databricks
    to use it. You do not want to create the same definition in Databricks. What OSI
    does is act as a code converter or transpiler. You put it in one file and it exports
    another file compatible on the other side while the definition stays the same.
  sec: 2520
  time: '42:00'
  who: Sahil
- line: If I use multiple compute engines like Snowflake Databricks and BigQuery I
    can have one centralized data catalog. Then I can have OSI sitting between my
    catalog and all these engines.
  sec: 2555
  time: '42:35'
  who: Alexey
- line: Exactly. I think I did not mention that Iceberg is the physical layer while
    the logical layer still stays with you. If you were using Postgres only Postgres
    knows how that table looks through create table or view statements. Those statements
    are not portable to any other engine. To port it you create that semantic view
    essentially and it maintains the logical layer.
  sec: 2586
  time: '43:06'
  who: Sahil
- line: Where I was going with this example is having one central catalog and different
    compute engines that can access it. Does Apache Iceberg not already offer interoperability
    out of the box? Why do I need OSI on top of that?
  sec: 2616
  time: '43:36'
  who: Alexey
- line: These are two different things. Iceberg is a table format that simply defines
    how the table should look. On top of it sits the catalog which handles governance
    and tells how to access the table files and latest states. Catalogs can be many
    things like Glue or Nessie which are compatible with Iceberg. Iceberg is the storage
    layer and the catalog is about access.
  sec: 2640
  time: '44:00'
  who: Sahil
- line: The logical layer like a semantic view was not portable because definitions
    could vary between systems. What OSI is doing at a very simple level is letting
    you maintain the business logic of your code from one system to another.
  sec: 2681
  time: '44:41'
  who: Sahil
- line: What exactly do you mean by business logic? Is it our dbt transformations?
  sec: 2713
  time: '45:13'
  who: Alexey
- line: Let us not take the dbt transformation example as it may not be right. Let
    us come back to the original example where you select top ten customers from the
    last ten days. How do you qualify those top ten customers? That is the only question.
  sec: 2722
  time: '45:22'
  who: Sahil
- line: You mean select top ten customers is the only thing you give to the system.
    You are not actually writing a full select statement. You need a definition of
    what revenue is and how exactly you convert this query into an actual SQL query
    that gets executed.
  sec: 2748
  time: '45:48'
  who: Alexey
- line: Exactly. From an LLM perspective it does not know what top ten means or how
    to calculate it. The way you start is by giving some example queries to it in
    a semantic view. In that semantic view you define a set of queries that will get
    asked often by the agents. You also specify that a column name can be a synonym
    like first name or contact for phone number.
  sec: 2773
  time: '46:13'
  who: Sahil
- line: You provide a whole definition of how your data structure looks. That logic
    previously only lived in Snowflake. If you wanted to do the same thing on Databricks
    you had to write the same logic in Databricks SQL. You were doing that operation
    twice. OSI converts it directly so you just port it and use it there. It reduces
    a lot of friction for teams so your logical definition stays constant.
  sec: 2812
  time: '46:52'
  who: Sahil
- line: Just to make sure I understood correctly let us say the use case is ad hoc
    analytics. Top management opens this application and writes give me revenue for
    the last ten days for top ten customers. OSI takes this query and maps what top
    ten and revenue mean. It converts this natural English query into some logical
    query. This query will be converted to the specific SQL dialect depending on where
    the data is located like Postgres or Snowflake. We have this intermediate representation
    that is convertible to other things.
  sec: 2867
  time: '47:47'
  who: Alexey
- line: It is convertible to other things. You still have to create that one semantic
    view that can be ported. That is the key point.
  sec: 2930
  time: '48:50'
  who: Sahil
- header: Managing Schema Changes in Data Warehouses
- line: What is this other thing you are working on? Was it Schema Change?
  sec: 2940
  time: '49:00'
  who: Alexey
- line: As we all know data evolves. A lot of teams had issues when they created an
    additional column in a table but had no way to know when or how it changed. Previously
    if I issued an alter statement to a database it ran through but there was no way
    to track it. Schema Change solves several things including providing a Git like
    structure. You can manage within GitHub how the file version changed and who made
    those edits.
  sec: 2945
  time: '49:05'
  who: Sahil
- line: It uses imperative coding to manage versions. Simply put you are maintaining
    version files and telling the system you previously had ten columns and now added
    an eleventh. There are files that you always run and files you want to repeat.
    It allows you to manage schema changes easily on Snowflake similar to technologies
    like Flyway or Liquibase.
  sec: 2989
  time: '49:49'
  who: Sahil
- line: I use Django and in Django we have migrations. When you were describing it
    I realized it is just like Django migrations but for warehouses.
  sec: 3032
  time: '50:32'
  who: Alexey
- line: Django is kind of a batteries included thing. If you use something like FastAPI
    or Flask they do not have migrations built in so you would use Liquibase. I am
    not a Django expert so I will not talk a lot about that.
  sec: 3045
  time: '50:45'
  who: Sahil
- line: Django has been the choice for me to develop web applications for the last
    sixteen years. It has been around for quite some time and is something I know
    quite well. Did you start this project or did you inherit it?
  sec: 3068
  time: '51:08'
  who: Alexey
- line: I did not start this project. I was at Slalom working with a top electronic
    manufacturer and they were using Schema Change. I worked there for one and a half
    years and kept using Schema Change for other projects because it was so powerful.
    It helped us manage how data evolved for auditability which made me very interested.
    I interacted with the authors and started contributing.
  sec: 3091
  time: '51:31'
  who: Sahil
- line: I am working there right now. If your audience wants to contribute or has
    any ideas let us know. We are happy to review and work through those.
  sec: 3144
  time: '52:24'
  who: Sahil
- line: I looked it up and right now it is under the Snowflake Labs organization.
    Has it always been under Snowflake Labs when you started using it?
  sec: 3167
  time: '52:47'
  who: Alexey
- line: The reason is it mostly works entirely on open source Snowflake. It is very
    much inspired by Flyway which can be used with multiple technologies. Snowflake
    also provides Database Change Management which is relatively the same but more
    declarative in nature. Schema Change is more imperative. It started under a person's
    name but eventually moved under Snowflake Labs.
  sec: 3174
  time: '52:54'
  who: Sahil
- line: We do not have a lot of time left but I am interested in your journey from
    a user to maintainer. You briefly mentioned you used it for a year and a half
    and then became a contributor and eventually a maintainer. Can you tell us more
    about this journey?
  sec: 3220
  time: '53:40'
  who: Alexey
- line: Is this for the audience to learn how they can become better contributors?
  sec: 3252
  time: '54:12'
  who: Sahil
- header: How to Contribute to Open Source Projects
- line: Yes because I think your story is motivating. In DataTalks.Club we are big
    supporters of open source and want to give as much spotlight to open source tools
    as possible. I contribute a lot to open source and want people who listen to this
    to also do that. Perhaps your story will motivate somebody to become a contributor
    first and then eventually a maintainer.
  sec: 3260
  time: '54:20'
  who: Alexey
- line: Context really matters. When you start with open source contributions it feels
    like nothing because your pull requests might not get merged or your issues handled.
    A lot of people in open source are spending their own time outside of their full
    time job. You need to start working on a technology like Schema Change and you
    will automatically find scenarios that are not working. You have two options either
    make it a community wide project or fork it and deploy it in your own environment.
  sec: 3285
  time: '54:45'
  who: Sahil
- line: My story and the way I recommend others start is by looking at first good
    issues. Any open source project will have simple issues that anyone can start
    with. Start contributing to the developer mailing list. Data engineering is very
    much open source whether it is Apache NiFi for ingestion Spark for transformations
    Iceberg for tables or Kafka for streaming. Go through those and look at what entices
    you and fits your use case.
  sec: 3341
  time: '55:41'
  who: Sahil
- line: Start communicating on the developer list to understand how teams make decisions.
    Contribute to proposals and start creating pull requests to build trust. Once
    you build trust the community will vote if they want to make you a committer.
    Once they make you a committer you go on to mentoring other communities. For example
    OSI needs mentors because it is incubating.
  sec: 3394
  time: '56:34'
  who: Sahil
- line: You get a lot of visibility from your work. It takes a lot of time but it
    is motivating too.
  sec: 3441
  time: '57:21'
  who: Sahil
- line: You managed to nail it perfectly within the time constraint. Do you have time
    for one more little question?
  sec: 3449
  time: '57:29'
  who: Alexey
- line: Absolutely.
  sec: 3456
  time: '57:36'
  who: Sahil
- line: As a maintainer I am curious because sometimes people ask their AI assistant
    to fix an issue on open source. Not many maintainers welcome these kinds of automated
    contributions. What is your opinion on automated pull requests?
  sec: 3456
  time: '57:36'
  who: Alexey
- line: This is a very good point that you bring up. I have noticed in Iceberg and
    the OSI community that people just want to become a contributor by asking code
    agents to write something and post it. You need to ask yourself why you are contributing
    and if you are solving real issues. All the communities I have seen are welcoming
    AI contributions but there should be material behind it. You need to own and understand
    what you are writing.
  sec: 3488
  time: '58:08'
  who: Sahil
- line: I have seen original authors pushing back on things written using AI code.
    You need to be very thorough. These committers are investing their time to review
    your pull requests. If it does not bring substance and you just overload them
    with pull requests it shows you as a weak candidate. People should remember open
    source is truly open and people can see what you committed.
  sec: 3544
  time: '59:04'
  who: Sahil
- line: If you are doing bad things it is not good for you. I ask people to be very
    thoughtful in what they contribute. I am very much in favor of asking AI to evaluate
    what you wrote or to suggest how to author a solution. I think AI systems have
    made us a little bit dependent and we do not use our own minds as much. Use AI
    to your advantage but do not use it to your disadvantage.
  sec: 3593
  time: '59:53'
  who: Sahil
- header: The Role of AI in Open Source Contributions
- line: Maintainers spend their time reviewing these requests so you want to show
    an equal level of commitment. Do not just open an AI tool and tell it to solve
    whatever open issue it is. Ideally it should be a problem you understand exactly
    and are actively engaged in.
  sec: 3640
  time: '1:00:40'
  who: Alexey
- line: Exactly. Sometimes someone will open a pull request that makes logical sense
    but the community previously decided it is not a right candidate for the next
    release. For interoperability you want other engines to comply with it and you
    know some will lag behind so you make those decisions. People need to really understand
    the whole ecosystem. You need to understand the developer list and what the community
    is truly trying to deliver.
  sec: 3666
  time: '1:01:06'
  who: Sahil
- line: Use AI only to your advantage and maintain that context. Do not completely
    delegate context management to AI.
  sec: 3706
  time: '1:01:46'
  who: Sahil
- line: Sahil thanks a lot for a wonderful discussion. Thanks for explaining many
    things to me. I have a clearer picture now because my understanding of modern
    lakehouses was quite outdated from the Glue and Hive times. Thanks for joining
    us today and I see that the audience also enjoyed our conversation.
  sec: 3721
  time: '1:02:01'
  who: Alexey
- line: Thank you Alexey it was great chatting with you.
  sec: 3754
  time: '1:02:34'
  who: Sahil
- line: Have a great day ahead. I know it is early for you so the early bird gets
    the worm.
  sec: 3756
  time: '1:02:36'
  who: Alexey
---

Links:

* [Linkedin](https://www.linkedin.com/in/sahilwaliasyracuse){:target="_blank"}
* [Github](https://github.com/sahil-walia){:target="_blank"}
* [Website](https://medium.com/@sahil-walia){:target="_blank"}