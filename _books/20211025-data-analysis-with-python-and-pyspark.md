---
title: "Data Analysis with Python and PySpark"
description: "Book of the Week. Data Analysis with Python and PySpark by Jonathan Rioux"
cover: "images/books/20211025-data-analysis-with-python-and-pyspark/cover.jpg"
image: "images/books/20211025-data-analysis-with-python-and-pyspark/preview.jpg"
start: 2021-10-25 00:00:00
end: 2021-10-29 22:59:58
authors: [jonathanrioux]
links: 
  - text: Book's page
    link: https://www.manning.com/books/data-analysis-with-python-and-pyspark
  - text: Book's GitHub repository
    link: https://github.com/jonesberg/DataAnalysisWithPythonAndPySpark

archive:
- name: Tim Becker
  text: Good morning Jonathan Rioux, very interesting book! I have a few beginners
    questions.
  replies:
  - name: Mansi Parikh
    text: from another beginner, these were really nice to read so thanks for asking,
      Tim, and thanks for answering, Jonathan!
- name: Tim Becker
  text: '- When should I start using Spark? I mean how large should my dataset be?
    Does it make sense to start using Spark, if my dataset still fit into memory,
    but I expect the size to increase?'
  replies:
  - name: Jonathan Rioux
    text: "Hi Tim!\nThis is an *excellent* question \U0001F642 I don\u2019t have a\
      \ straight answer, but let me share with you the heuristics that I use when\
      \ deciding for myself.\n1. PySpark is getting much faster for single-node jobs,\
      \ so you might be able to have acceptable performance with Spark on a single\
      \ node right off the bat! See the following link about a discussion about this.\
      \ [https://databricks.com/blog/2021/10/19/introducing-apache-spark-3-2.html](https://databricks.com/blog/2021/10/19/introducing-apache-spark-3-2.html)\n\
      2. Koalas was introduced in Spark 3 and merged into `pyspark.pandas` as of Spark\
      \ 3.2. Now more than ever, you can convert Pandas code to PySpark with a lot\
      \ less fuss. \U0001F642"
  - name: Jonathan Rioux
    text: "3. For memory allocation, I try to have a cluster with enough memory to\
      \ \u201Cstore\u201D my data and have enough room for computation. Data grows\
      \ quite fast, and if you have a feel that the data source will grow (for instance,\
      \ historical data), I find it easier to start with PySpark, knowing it\u2019\
      ll scale.\nIf you need a fast an loose rule for processing data (not counting\
      \ ML applications), I would say that if you can\u2019t get a single machine\
      \ with 3-5x the RAM your data sits on, you probably want to reach for Spark,\
      \ just for comfort."
- name: Tim Becker
  text: '- How much worse is the performance with pySpark if it used on a small dataset.'
  replies:
  - name: Jonathan Rioux
    text: "I think I replied on your previous question \U0001F642 . The \u201CSpark\
      \ single-node performance tax\u201D shrunk *dramatically* since Spark 3.0 and\
      \ even more since Spark 3.2.\n[https://databricks.com/blog/2021/10/19/introducing-apache-spark-3-2.html](https://databricks.com/blog/2021/10/19/introducing-apache-spark-3-2.html)\n\
      In practice, I find that with very small data sets (a handful of hundred of\
      \ rows) you will have much worse performance depending on the operations: that\
      \ being said, it\u2019s often a difference of 0.29 sec vs 0.85 sec which I am\
      \ not too concerned about."
- name: Tim Becker
  text: '- What are the advantages of using databriks?'
  replies:
  - name: Jonathan Rioux
    text: "Databricks has many things for itself!\n1. Databricks provides proprietary\
      \ performance improvements over open-source Spark so your jobs may run faster\
      \ with no changes. I am especially excited about Photon ([https://databricks.com/product/photon](https://databricks.com/product/photon))\
      \ which takes your Spark data transformation code through a new query engine.\n\
      2. The notebook experience out of the box is quite good (and I am saying this\
      \ from the perspective of a person who doesn\u2019t really like notebooks).\
      \ I like being able to create ad-hoc charts from a result data frame and explore\
      \ my data right from the same interface.\n3. Databricks connect ([https://docs.databricks.com/dev-tools/databricks-connect.html](https://docs.databricks.com/dev-tools/databricks-connect.html)\
      \ ) is the simplest (to me) way to connect my IDE on a remote cluster with the\
      \ minimum amount of fuss. It can be a little capricious, but when writing the\
      \ book, I\u2019ve used much worse hacks to connect to a remote REPL with Spark\
      \ enabled\u2026\n4. Databricks provides additional capabilities (Delta Lake\
      \ for data warehousing, MLFlow of ML model/experiments management, etc.) which\
      \ play well with the overall ecosystem.\n5. The ecosystem is quite consistent\
      \ around all three major cloud providers (AWS, Azure, GCP), which help if you\u2019\
      re moving around. :)"
- name: Tim Becker
  text: '- If we want to train ML models using pySpark, does the model have to support
    distributed training?'
  replies:
  - name: Jonathan Rioux
    text: "Spark\u2019s ML model collection all work out of the box. They are all\
      \ listed here: [https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html).\n\
      Some algorithms naturally lend themselves better to distributed computing and\
      \ perform (runtime) much better than other. Random Forest for instance distributes\
      \ super well, GradientBoosting a little less so.\nOn top of that, you can also\
      \ use user-defined functions (UDF) to run single-node models in a distributed\
      \ fashion (the model would run on a single node here). This allows for parallelizing\
      \ hyper-parameter selection. I am considering to write an article/do a video\
      \ on the topic as it is quite fun to do!"
  - name: Tim Becker
    text: "thank you \U0001F642"
- name: Tim Becker
  text: "Thank you \U0001F642"
  replies: []
- name: adanai
  text: "Hello Jonathan, just the kind of book I am interested to read further on!\n\
    I have been using Python (pandas/sklearn) for small-medium data related tasks\
    \ (analysis / ML) and it is the only programming language I have some amount of\
    \ exposure to.\nIn order to get started and work further with PySpark, do I need\
    \ to have some prerequisites in understanding the spark architecture in its native\
    \ implementation for working with big data?\n Also, what is the approach to be\
    \ taken to work with the scala/java implementation in case the switch has to be\
    \ made?"
  replies:
  - name: Jonathan Rioux
    text: "Hello!\nTL;DR: I wrote my book for someone like you! \U0001F642\nYou don\u2019\
      t have to use Java/Scala to use PySpark, but you are right in saying that the\
      \ architecture and code approach can be different.\nIn Part 1 of my book, I\
      \ discuss about how you can change your way on thinking about transformations\
      \ vs. actions. Later, in Chapter 11, I discuss about narrow vs. wide transformations\
      \ to help with understanding why the data needs to move from one node to another.\n\
      Everything that you\u2019ve learned so far still carries to the big data world,\
      \ fortunately \U0001F642 With my students and employees, the biggest \u201C\
      click\u201D happens when they understand data locality (which data points need\
      \ to be where in order for an operation to succeed) and they learn to read query\
      \ plans (Chapter 11 as well) and structure code in a readable fashion.\nIf you\
      \ really need to use Java, my now friend Jean-George Perrin wrote _Spark In\
      \ Action_ from the same publisher and with a more data engineering point of\
      \ view. You\u2019ll find that the Spark API looks the same regardless of the\
      \ language."
- name: "Jos\xE9 Bastos"
  text: 'Hi Jonathan, books seems great. Here are my questions:

    - What''s the data type you struggle the most? And the one you have more fun with?

    - What is the most common error/assumption people do when using PySpark and general
    ML pipelines?

    - Best tip to make training more efficient?

    Thank you for your time!'
  replies:
  - name: Jonathan Rioux
    text: "Hi Jos\xE9!\n*What\u2019s the data type you struggle the most? And the\
      \ one you have more fun with?*\nMy favourite by far is multi-dimensional/hierarchical/document\
      \ data (think JSON). I don\u2019t know why, but having that data model within\
      \ the data frame (highly performance nested data frames) is *awesome*. It sometimes\
      \ also feels like a puzzle to extract and work with the data the best way and\
      \ I like a challenge \U0001F604.\nBinary data in Spark can be a little bit of\
      \ a pain (think audio, video, images, etc.). Most of the work revolves around\
      \ treating everything like an independent unit (you could even use a RDD for\
      \ this). I like doing ML on unstructured data, but prepping in a distributed\
      \ fashion can sometimes feel a little bit of a pain."
  - name: Jonathan Rioux
    text: "*What is the most common error/assumption people do when using PySpark\
      \ and general ML pipelines?*\nEasy \U0001F642 *Being too precious with their\
      \ data pipelines/not planning and iterating*. Most data scientists I encountered\
      \ are very hesitant about training a model. I usually go straight with a simple\
      \ pipeline that takes the features ready to go and use a simple model. This\n\
      1. Serves me as an early benchmark.\n2. Removes some of the magic of the model\
      \ and helps me destress about metric anxiety.\n3. Ensures I have a complete\
      \ modelling pipeline working!\nML pipelines are super cool because you build\
      \ the components independently of their application. It makes it easy to add/remove\
      \ some as you go. Because of this, you are responsible to strike the right balance\
      \ of planning and flexibility. I keep a notebook of what I want to do, what\
      \ I expect as results, and I build my code as I go.\n(Plus, if your model takes\
      \ time, you can work on the next iteration while it fits!)"
  - name: Jonathan Rioux
    text: "*Best tip to make training more efficient?*\nDo you mean \u201Cspeed up\
      \ PySpark ML training\u201D?\n1. Read the SparkUI when working with ML model.\
      \ It\u2019ll help see the order of operations and review if you are spilling\
      \ a lot of data.\n2. Sometimes, you can get a *whole lot more performant training*\
      \ by saving the data frame in Parquet on disk and reading it again. It\u2019\
      s like a _super-cache_ that clears the previous operations.\n3. *Use enough\
      \ memory and compute.* Remember that Spark uses memory for both storage of the\
      \ data and compute (+ the rest that makes a computer work). Don\u2019t skimp\
      \ on memory, even if it means using a smaller cluster for data transformation\
      \ and then going all ham on ML."
- name: Asmita
  text: "Hi Jonathan Rioux, I have been working on simple projects as of now. Will\
    \ this book be a good start for learning about PySpark? Also, are there any specific\
    \ hardware requirements for running? \nI read your message about transfirmations\
    \ vs actions, but is it useful for someone who is leaarning from scratch and has\
    \ no idea abojt PySpark and its workings?"
  replies:
  - name: Jonathan Rioux
    text: "Hi Asmita!\nIf you know some Python, then my book will (I hope!) be useful\
      \ yes. \U0001F642 It is to get started with PySpark.\nI recommend a computer\
      \ with at least 8GB of RAM (if you work locally) or access to a cloud provider\
      \ Spark (there are some free offering, such as Databricks community edition).\n\
      Transformations vs. Actions is a pretty important concept in understanding how\
      \ Spark processes data. It is explained right off the bat in Chapter 1, so you\u2019\
      re not expected to know anything about it first."
  - name: Asmita
    text: That's amazing! Thank you for answering my question!
- name: WingCode
  text: 'Hi Jonathan Rioux , thank you for doing this Q&amp;A

    1# How do you estimate the resources needed for a spark job? Is there a tool out
    there which looks at the volume of data with the spark code to determine the number
    of executors, cpu &amp; memory needed? Or is it some rule of thumb and repeated
    iteration to tune out the best config?'
  replies:
  - name: Jonathan Rioux
    text: "Hi Wingcode!\nGreat questions!\n#1: As far as I am concerned, no such thing\
      \ exist at the time\u2026\nSize/volume of the data is important (both disk space\
      \ and memory, because of potential spills), but also the type of operations\
      \ you plan on doing. If the data can be logically represented by small-ish (single\
      \ or a few nodes), your Spark code might need less resources because there will\
      \ be less merry-ing around of the data.\nAs you write your own programs, and\
      \ use the Spark UI to review the resources used by the cluster, you\u2019ll\
      \ be able to adjust as needed. I remember getting a little frustrated at first\
      \ because it can look like a guessing game, but you end up building your own\
      \ mental model for data usage.\nAs an example, for time series (~14 TB of data)\
      \ using ML modelling and heavy feature engineering, I used comfortably 25 machines\
      \ x 60 GB of RAM. Some spill, but it was good enough for me."
- name: WingCode
  text: '2# In spark local mode vs cluster mode (YARN) what are the advantages in
    terms of my job performance? Other than:

    a. Data locality. If my RDD partition and HDFS block is on same node hence no
    shuffle

    b. Reliability. If my local executor is flaky, then my whole job performance/reliability
    suffers. YARN -&gt; multiple machine hence flaky node can be mitigated.

    c. Vertical scaling limit. If I need very high memory, CPU counts which the cloud
    provider doesn''t offer on single instance.

    If I manually set num of partitions (via coalesce or repartition) in local mode
    I can make multiple tasks executing in parallel? Wouldn''t this be faster than
    cluster mode?'
  replies:
  - name: Jonathan Rioux
    text: "I think you hit the nail on the head. Spark in cluster mode (whether YARN\
      \ or k8s, I think the other ones are not used much\u2026), you gain the ability\
      \ to scale beyond a single machine.\n`coalesce()` is, to me, mostly useful when\
      \ you want to limit the number of partitions (for instance, before writing to\
      \ disk. For \u201Cshort lived\u201D data programs, I usually don\u2019t use\
      \ it much as Spark is pretty smart about reshuffling data in the best way possible.\
      \ When using older version of Spark, it helped, but since Spark 3.X I\u2019\
      ve been pretty keen on relying on the default behaviour \U0001F642\nThe whole\
      \ essence of Spark is its ability to scale horizontally. If you have a single\
      \ beefy machine, you might yield better performance from another tool (although\
      \ Spark single node is pretty speedy, see my previous answers)."
- name: WingCode
  text: 3# How significant is the overhead between using Scala for spark versus Python
    for spark (since Python data structures have to be converted to Scala datatypes)
    ? Is it worthwhile to convert frequently run Pyspark in production to Scala spark
    for performance &amp; better resource utilisation?
  replies:
  - name: Jonathan Rioux
    text: "When using RDD and regular Python UDF, you\u2019ll pay a pretty significant\
      \ performance tax from serialization/deserialization (serde) from Spark\u2019\
      s data model to something Python can consume.\nThe data frame API, even in Python,\
      \ maps to JVM instructions and performance is quite similar to Spark in Java/Scala.\n\
      Now, with Pandas UDF and Arrow serialization, you can use Python/Pandas code\
      \ within PySpark with minimal overhead. Python will not always be as fast as\
      \ Java/Scala (Pandas/NumPy owe much of their speed to highly optimized low-level\
      \ code), but the gap is narrowing."
- name: WingCode
  text: 4# Do you think serverless Spark ([https://cloud.google.com/solutions/spark](https://cloud.google.com/solutions/spark))
    is going to be the next big thing for data analysis &amp; ML similar to managed
    Kubernetes engine? Do most of the orgs in your experience, run private Spark clusters
    or use some cloud offering (DataStax, Databricks)
  replies:
  - name: Jonathan Rioux
    text: "I find the expression \u201Cserverless Spark\u201D quite hillarious \U0001F604\
      \ because you always are concerned about the servers being used. Most serverless\
      \ Spark offering rebrand the compute+memory units, which is counter productive\
      \ as most Spark users understand RAM quantities pretty well.\nI think that managed\
      \ Spark is a pretty seducing option for data analysis and data science. Databricks\
      \ is the dominating force here, but I\u2019ve seen some great success/used other\
      \ managed Spark product.\nLooking at the link you provided, I think it\u2019\
      s a pretty seducing offering for the cloud provider because you give them the\
      \ keys to scale for you. In practice, your IT organization might set pretty\
      \ stiff limitations there. I also have not seen auto-provisioning that was so\
      \ fast that I was convinced to move away from \u201Cprovisioning the cluster\
      \ myself\u201D."
  - name: WingCode
    text: "Jonathan Rioux Thank you for all the super detailed answers. \U0001F642"
  - name: Jonathan Rioux
    text: "My pleasure \U0001F642 Thanks for the excellent questions!"
- name: Jonathan Rioux
  text: "Hi everyone!\nAs for memory usage, especially when I get to scale a cluster,\
    \ I use this image to remind me of the cluster memory vs. the available memory.\
    \ On top of this, remember that Spark will spill to disk (which is slower, but\
    \ not catastrophic).\nWhen scaling a cluster, I found that most people try to\
    \ skimp on memory. If you plan on using TBs of data, it\u2019s not silly to have\
    \ a lot of RAM (depending on the operations/transformation/modelling), you won\u2019\
    t have fun if you total 500GB of RAM across your cluster."
  replies: []
- name: Lavanya M K
  text: "Hi Jonathan Rioux \n1. Which is the best tool to use pyspark for creating\
    \ eda and data visualization? I usually use zeppelin to do this. \n2. Is there\
    \ any difference in terms of resources utilisation or speed between using scala-spark\
    \ and pyspark?"
  replies:
  - name: Jonathan Rioux
    text: "Hello Lavanya!\n*#1* : Within databricks, you can create charts from data\
      \ frames pretty easily. It uses [plot.ly](http://plot.ly) in the back-end. PySpark\
      \ also has the `summary()` and `describe()` methods you can use for diagnosing\
      \ the data (at a high-level) within columns.\nI haven\u2019t used Zeppelin in\
      \ a long time (and only for the notebook interface) but Jupyter (Spark open-source)\
      \ or databricks notebook (databricks) should provide the same functionality."
  - name: Jonathan Rioux
    text: "*#2* : With the data frame, PySpark and Spark are pretty similar, under\
      \ the hood, PySpark will call the same JVM methods as Spark/Java. In some cases\
      \ (for instance, when using the RDD or UDF), you will have differences (because\
      \ you\u2019re using plain Python/Pandas code and not the optimized Spark routines).\n\
      If you are more comfortable using Python, PySpark will serve you quite well!"
- name: Lavanya M K
  text: 3. How efficient is it to use spark UDFs to perform data processing?
  replies:
  - name: Jonathan Rioux
    text: "I distinguish two types of UDF\n*Python UDF* are used with the `udf()`\
      \ function/decorator. They merry the data from Spark to Python and then use\
      \ Python to process the record. Those UDF are usually slower because of the\
      \ data serialization/deserialization and also because Python can be slower than\
      \ Scala/Java.\n*Pandas UDF* are used with the `pandas_udf()` function/decorator\
      \ and are much faster than Python UDF. They use Arrow for converting the data\
      \ from Spark to Pandas. Furthermore, Pandas can be very fast when using vectorized\
      \ instructions.\nUDF are useful when you need to do something that is hard to\
      \ do with the PySpark API. See them as a specialized tool that unlock additional\
      \ capabilities, not as a replacement for Spark\u2019s core API.\nIn terms of\
      \ efficiency, I read articles claiming that Pandas UDF can sometime be more\
      \ efficient than Spark core data transformation API (!). I have not seen this\
      \ in practice, usually witnessing a small slowdown (going through a few examples\
      \ I wrote for fun \u2014 don\u2019t take this as an official benchmark! \u2014\
      \ I see anything from 0.9-10.2x. I still use them quite a bit for my own data\
      \ analysis and modelling. :)"
  - name: Jonathan Rioux
    text: "Additionally: I often use UDF / Pandas UDF for promoting local Python/Pandas\
      \ code to PySpark. It allows to scale the code (although more slowly) without\
      \ needing a re-write. Bonus for me since I can use the old \u201Cpromoted function\u201D\
      \ as test when rewriting in \u201Cnative\u201D Spark. \U0001F642"
- name: Alexey Grigorev
  text: I remember a few years ago Apache Zeppelin was getting some traction as a
    nice and easy way to do analytics with Spark. But I haven't heard about it for
    a while. Is it still used? What do you think about it?
  replies:
  - name: Alexey Grigorev
    text: I've seen in a thread that you mentioned that Jupyter has the same functionality.
      So it means people prefer to use it more often than Zeppelin?
  - name: WingCode
    text: 'People in our org use both the ways (Zeppelin + Scala OSS Spark, Jupyter
      + PySpark) . Personally feel, Zeppelin is one of the best integrations out there
      if you want to use Scala + OSS Spark with in built viz, versioning, easy configuration
      of spark (mem, cpu, spark mode, reuse same interpreter across users, user access
      controls)

      If you need such features from Spark + Jupyter, I think you need to manually
      configure so many things which is a pain.'
  - name: Jonathan Rioux
    text: "I have not used Zeppelin in a very long time (~2 years) so my opinions\
      \ are tainted a little.\nMost cloud offering has Jupyter integration baked in\
      \ which is ok. Databricks still has IMHO the best notebook integration. I think\
      \ that Zeppelin/Livy had the option to work cross-languages for the longest\
      \ time, but it\u2019s not something I used extensively."
  - name: Jonathan Rioux
    text: "In the end, I think that comfort level and habit are quite important. There\
      \ can be a little bit of tool fatigue at times \U0001F642 But WingCode is right\
      \ that something configuration/configurability can be a pain."
  - name: Lavanya M K
    text: Another drawback of zeppelin is it gets slow in rendering when creating
      visualisation
- name: WingCode
  text: "Hi Jonathan Rioux,\nI had few more questions \U0001F642\n#1 Is there any\
    \ advantages using HDFS 3.X over HDFS 2.X with Spark?"
  replies:
  - name: Jonathan Rioux
    text: "Good question!\nI think that Spark uses Hadoop only for storage, so if\
      \ Hadoop 3.0 is faster, all the better. In practice, I\u2019ve used Spark mostly\
      \ in a cloud setting (GCS, S3, Blob Storage, DBFS, BigQuery, etc.): it really\
      \ boils down to where your data is and how you get Spark provisioned.\nThis\
      \ might be a little out of my wheelhouse but I hope it answered your question!"
  - name: WingCode
    text: "Yes  answered my question  \U0001F642 Thank you Jonathan"
- name: WingCode
  text: '#2 Do you recommend any other profiling tool for OOS spark jobs other than
    the information we get through spark Web UI ?'
  replies:
  - name: Jonathan Rioux
    text: "I\u2019m not sure if it\u2019s available standalone still anymore, but\
      \ I was impressed by the work on the Spark UI the folks at data mechanics ([https://www.datamechanics.co/](https://www.datamechanics.co/))\
      \ did. This is the only other product I\u2019ve used and can comment on.\nUpdate:\
      \ [https://www.datamechanics.co/delight](https://www.datamechanics.co/delight)\
      \ \u2190 there you go, it\u2019s over there :)"
  - name: WingCode
    text: "This is a cool UI, unfortunately the dashboard server is not open-source.\
      \ Thank you for the link Jonathan \U0001F642"
- name: WingCode
  text: '#3 Do you think users of Spark need to have some basic understanding of the
    internals to use it better compared to other data processing tools like Pandas,
    Numpy?'
  replies:
  - name: Jonathan Rioux
    text: "I think that every library user should read the documentation/data model\
      \ of what they use \U0001F609\nSpark has a pretty straightforward data model\
      \ abstraction (the data frame is easy to understand, yet very flexible). For\
      \ starters, understanding this is enough.\nAs you go along, it\u2019ll be insightful\
      \ to gain deeper knowledge of how and where the data is processed, partitions,\
      \ skew, etc. as it\u2019ll help profile and reason about your programs. It\u2019\
      s not necessary (IMHO) at the start, but becomes important if you want to really\
      \ grok Spark."
- name: Doink
  text: Alexey Grigorev  I am seeing some wonderful discussions happening here, wondering
    if these discussions are saved in a separate document for future reference?
  replies:
  - name: Alexey Grigorev
    text: "They are! \nThis is how it looks for previous books - [https://datatalks.club/books/20210517-grokking-deep-reinforcement-learning.html](https://datatalks.club/books/20210517-grokking-deep-reinforcement-learning.html)"
  - name: Doink
    text: '[https://datatalks.club/books/20211011-mastering-transformers.html](https://datatalks.club/books/20211011-mastering-transformers.html)
      here I didn''t see anything hence asked.'
  - name: Alexey Grigorev
    text: I'll publish the answers eventually. It takes some time, that's why I batch-process
      it =)
  - name: Doink
    text: Oh okay got it thank you so much for this, is there a way we can contribute
      like in form of financial donations? You are really doing great work!!
  - name: Alexey Grigorev
    text: 'Thanks for asking! Yes there''s a way to do it: [https://github.com/sponsors/alexeygrigorev](https://github.com/sponsors/alexeygrigorev)'
  - name: Wendy Mak
    text: Out of curiosity, is this automatable ?
  - name: Alexey Grigorev
    text: "I have a script that generates a yaml with messages. It automates like\
      \ 90% of the work. \nThe part that's not automated yet is\n- Selecting the week\
      \ \n- Cleaning the responses a bit, like removing the announcements\n- Putting\
      \ the yaml to the website"
  - name: Wendy Mak
    text: "now wondering if the rest of the 10% is doable with github actions \U0001F602"
  - name: Alexey Grigorev
    text: They probably are, I'm sure it's automatable. Maybe the second one is a
      bit tricky though
  - name: Lalit Pagaria
    text: "Second one good problem for zoomcamp \U0001F642\nAnyway please for rest\
      \ of the tasks (at least coding not ML) if you hands let me know"
- name: Hironori Sakai
  text: 'Hi Jonathan Rioux . I have a question about dependency management for PySpark.
    When we need a library for a PySpark Job, then we may 1) install the library on
    all nodes or 2) submit all required library with `--py-files` option. I do not
    think that these options are realistic if the dependency is quite large. (e.g.
    install/update `spacy`. It requires around 30 libraries.)

    My question is: what is the best approach to submitting a PySpark Job requiring
    a large dependency?

    (If we use Scala, we do not have such a problem, because we can pack all needed
    packages in a JAR file.)'
  replies:
  - name: Jonathan Rioux
    text: "This is such a good question! `--py-files` IIRC does not work with libraries\
      \ that have C/C++ code, such as `spacy` .\nIt boils down to which environment\
      \ you are using. Are you on a cloud installation (databricks, EMR, Glue, HDInsights,\
      \ Dataproc, etc.) ? If this is the case, you can specify and install dependencies\
      \ at cluster creation time or runtime. This also has the advantage that you\
      \ can \u201Cversion\u201D the dependencies of your cluster. I used dataproc\
      \ (GCP) for a pretty significant project a few years ago and this is the route\
      \ we took. Databricks has `dbutils` where you can install libraries on the cluster\
      \ with a simple command from the notebook.\n(Databricks, on top of this, has\
      \ runtime versions that has predictible libraries and versions. I am a big fan\
      \ of those, just to avoid thinking about which one to use \U0001F604 see for\
      \ example spacy 3.1.2 on databricks runtine 10.0ml: [https://docs.databricks.com/release-notes/runtime/10.0ml.html](https://docs.databricks.com/release-notes/runtime/10.0ml.html))\n\
      If you are \u201Con-prem\u201D or the cluster is not meant to be ephemeral,\
      \ you need to be a little more careful with dependencies management. Again,\
      \ this is product dependent (what do you use to manage your hardware provisioning)\
      \ but I would assume that orchestration tools can help with this. I think that,\
      \ in this case, you need to be more conservative with your dependencies to avoid\
      \ some clash if multiple users are there.\nThis is one of the cases where I\
      \ envy the JVM/jar world\u2026 \U0001F642"
  - name: Jonathan Rioux
    text: 'See `dbutils` here: [https://databricks.com/blog/2019/01/08/introducing-databricks-library-utilities-for-notebooks.html](https://databricks.com/blog/2019/01/08/introducing-databricks-library-utilities-for-notebooks.html)'
  - name: Jonathan Rioux
    text: 'Another example: installing dependencies on GCP dataproc.

      [https://cloud.google.com/dataproc/docs/tutorials/python-configuration#image_version_20](https://cloud.google.com/dataproc/docs/tutorials/python-configuration#image_version_20)'
  - name: Hironori Sakai
    text: '&gt; I would assume that orchestration tools can help with this.

      Thanks for your answer! I did not have this viewpoint.'

---

When it comes to data analytics, it pays to think big. PySpark blends the powerful Spark big data
processing engine with the Python programming language to provide a data analysis platform that can
scale up for nearly any task. Data Analysis with Python and PySpark is your guide to delivering successful
Python-driven data projects.

Packed with relevant examples and essential techniques, this practical book teaches you to build
lightning-fast pipelines for reporting, machine learning, and other data-centric tasks.
No previous knowledge of Spark is required.
