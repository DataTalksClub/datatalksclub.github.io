---
title: "Blueprints for Text Analytics Using Python"
description: "Book of the Week. Blueprints for Text Analytics Using Python by Jens Albrecht, Sidharth Ramachandran and Christian Winkler"
cover: "images/books/20211018-blueprints-for-text-analytics-using-python/cover.jpg"
image: "images/books/20211018-blueprints-for-text-analytics-using-python/preview.jpg"
start: 2021-10-18 00:00:00
end: 2021-10-22 22:59:58
authors: [jensalbrecht, sidharthramachandran, christianwinkler]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/blueprints-for-text/9781492074076/
  - text: Amazon
    link: https://www.amazon.com/_/dp/149207408X
  - text: Book's GitHub repository
    link: https://github.com/blueprints-for-text-analytics-python/blueprints-text

archive:
- name: Asmita
  text: Hi, my question for the authors is - since there are many tools for NLP practices,
    how can we understand in depth working of those tools, is it also included in
    the blueprint?
  replies: []
- name: Asmita
  text: "Also, in case of different spellings for the same words, and the use of characters\
    \ such as -\xE0,\xE8,\xFC,\xF6 and others is there a tool or method to compare\
    \ and categorize the words into the same, without translating the words into the\
    \ same language and then analysing?"
  replies: []
- name: Jens Albrecht
  text: 'Hi Asmita, our book focuses on best practises how to work with the tools
    different NLP libraries provide. It still gives some theoretical background on
    the concepts used, though.

    And yes, there is a blueprint for the treatment of different spellings. Just have
    a look at the notebook of Chapter 3 on Git and search for "character normalization":
    [https://github.com/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch04/Data_Preparation.ipynb](https://github.com/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch04/Data_Preparation.ipynb)'
  replies: []
- name: Max Payne
  text: Does you book deal with 'Personally identifiable information'? In either case,
    any thoughts on this field and tips if possible?
  replies: []
- name: Quynh Le
  text: Hi Jens Albrecht, Sidharth Ramachandran, and Christian Winkler thanks for
    writing the book! Could you share with us about the fields you see the most applications
    of NLP?
  replies: []
- name: Christian Winkler
  text: Good morning everybody!
  replies: []
- name: Christian Winkler
  text: 'Max Payne: We don''t explicitly address data privacy and anonymization. That
    could be part of the data acquisition process, but it is very complicated and
    depends on legislation in different countries. Pseudonymization might be a good
    idea to enable aggregation later. We have quite a few commercial projects where
    aggregation in the first step solves these issues - but that of course depends
    on the use case. Apart from data privacy, copyright law in different countries
    might also be something worth considering.'
  replies: []
- name: Christian Winkler
  text: 'Quynh Le: Very interesting question, this probably depends on the field you
    are most interested in. If you concentrate on enterprise data, uncovering the
    structure of large document archives might be exciting. In the social sciences,
    you can avoid performing surveys using NLP and user-generated data. Apart from
    all these applications, the recent achievements in contextualization using transfer
    learning are really impressing.'
  replies: []
- name: Asmita
  text: Hi Christian Winkler Jens Albrecht Sidharth Ramachandran, What is your opinion
    on automating NLP processes? Will automating them lead to some percentage of loss
    when compared to a human validating the process step by step?
  replies: []
- name: Nikhil Shrestha
  text: 'Hi Christian Winkler Jens Albrecht Sidharth Ramachandran, thank you writing
    this book.

    Recently I have been working on some text analytics projects and all of it is
    very interesting.

    So motivation for my question is that we usually see only one side of the problem
    we are facing. Either the negative side or only the positive side. Biggest example
    is when we talk about any sort of safety analysis we only look for accidents that
    have happened rather than researching about the positive aspect of the safety
    which includes campaigns, awareness drives and we never dig deeper into those
    aspect basically.


    My question is if I want to layer the findings of my analysis over time say for
    example: over a period of time how did a specific topic say climate (as in terms
    of semantics, popularity, understanding etc basically negatives AND positives)
    have changed.

    Here I am using climate but we could think of this problem in very wide spectrum
    say a product, software, book, organization etc.

    Hence, is there a way that we could work around something like this?

    Thank you in advance.'
  replies: []
- name: Christian Winkler
  text: Thanks for your question, Nikhil Shrestha. You could use semantic embeddings
    like word2vec for supporting information retrieval. Another option would be to
    use something more full-fledged like [txtai]([https://github.com/neuml/txtai](https://github.com/neuml/txtai))
  replies: []
- name: Christian Winkler
  text: Good question, Asmita! I think it depends on the kind of task you are automating.
    Nowadays, language models based on transfer learning can achieve human performance
    (some are even superior to humans). However, irony and sarcasm is still difficult
    to interpret. In the unsupervised or semi-supervised regime, there is no real
    loss, it just makes interpretation easier. That's also what we see in our daily
    projects - we are using AI more as a tool to supercharge humans.
  replies: []
- name: Nikhil Shrestha
  text: "Thank you Christian Winkler for swift reply on the question, will check the\
    \ resources and update you accordingly.\U0001F642"
  replies: []
- name: Christian Winkler
  text: Hope that helps Nikhil Shrestha and I haven't misunderstood your question
  replies:
  - name: Nikhil Shrestha
    text: "Yes Christian Winkler it pointed me to the direction which indeed will\
      \ help \nThank you for that. \nYou totally understood the question \U0001F64F\
      \U0001F642"
- name: Christian Winkler
  text: We would be happy to answer further questions. Feel free to also ask questions
    about NLP in general - it does not have to be directly related to our book.
  replies: []
- name: Natasha john
  text: "Hi everyone,\nany suggestion for a book talking about self driving cars!\
    \ \U0001F601"
  replies:
  - name: Alexey Grigorev
    text: I think <#C01AXGTRESH|books> would be a better channel for this
  - name: Alexey Grigorev
    text: But if you already know a book about self driving cars and would like to
      invite the authors here to this channel, please let me know =)
  - name: Natasha john
    text: "Of course Alex, thanks for helping \U0001F64F"
- name: Maja
  text: "Hello Christian Winkler Jens Albrecht Sidharth Ramachandran! \U0001F44B Thank\
    \ you for writing this book full of practical solutions. I just have to ask you\
    \ for your opinion on transformers in NLP (BERT, RoBERTa GPT-3) advantages and\
    \ disadvantages. Did you use them?"
  replies:
  - name: Sidharth Ramachandran
    text: Thanks for the question Maja. We do make use of the BERT model in one of
      the chapters of the book. In fact I'm also seeing the use of transformer based
      models heavily in the industry. They work surprisingly well without much preprocessing.
      They are however not good across languages but here too there are variants that
      the community releases online  that are helpful. The question of bias in these
      models must be tackled though and it depends on each use-case to determine how
      critical this is.
  - name: Maja
    text: Thank you so much Sidharth Ramachandran for the answer. I'll look into it!
  - name: Christian Winkler
    text: Finetuning BERT and RoBERTa models often leads to quite similar results.
      A good starting point is the Huggingface page with all the models [https://huggingface.co/models](https://huggingface.co/models)
  - name: Christian Winkler
    text: 'GPT-3 is a different story as it is a commercial model which is mainly
      used for generating text. Alternatively, you could take a look at GPT-J from
      EleutherAI.

      These models are normally too large to train them on your own or even fine-tune
      them.

      And they are still growing. Last week, NVIDIA and Microsoft announced the "Megatron-Turing
      Natural Language Generation model" (MT-NLG) with a whopping 530 billion parameters.'
  - name: Maja
    text: Thank you Christian Winkler so much for everything! I'm going to NVIDIA
      conference, start reading your book when I get it and I have started with Hugginggace.
- name: Asmita
  text: Thank you Jens Albrecht, Sidharth Ramachandran  Christian Winkler  For your
    time!
  replies: []
- name: Nikhil Shrestha
  text: Thank you Jens Albrecht Sidharth Ramachandran  Christian Winkler for sharing
    the knowledge and clearing our doubts.
  replies: []
- name: Maja
  text: Thank you so much Jens Albrecht, Sidharth Ramachandran and Christian Winkler
    for all your guidance and fast replies to our questions!
  replies: []
- name: Quynh Le
  text: Thank you Jens Albrecht, Sidharth Ramachandran, Christian Winkler for coming
    to share about NLP!
  replies: []
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

---

Turning text into valuable information is essential for businesses looking to gain a competitive
advantage. With recent improvements in natural language processing (NLP), users now have many options
for solving complex challenges. But it's not always clear which NLP tools or libraries would work for
a business's needs, or which techniques you should use and in what order.

This practical book provides data scientists and developers with blueprints for best practice
solutions to common tasks in text analytics and natural language processing.