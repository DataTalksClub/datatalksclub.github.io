---
title: "Cleaning Data for Effective Data Science"
description: "Book of the Week. Cleaning Data for Effective Data Science by David Mertz"
cover: "images/books/20210621-cleaning-data-for-effective-data-science/cover.jpg"
image: "images/books/20210621-cleaning-data-for-effective-data-science/preview.jpg"
start: 2021-06-21 00:00:00
end: 2021-06-25 22:59:58
authors: [davidmertz]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/cleaning-data-for-effective-data-science/9781801071291
  - text: Amazon
    link: https://www.amazon.com/dp/1801071292/
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Cleaning-Data-for-Effective-Data-Science

archive:

- name: Alex
  text: "Hi there, David Mertz! I\u2019ve recently come across a realization that\
    \ I, as data analyst, spend so much time extracting, cleaning and preprocessing\
    \ data in order to analyze it as effectively as possible.\nHow would you frame\
    \ the usefulness of this book for someone who is not directly related to data\
    \ science?"
  replies:
  - name: David Mertz
    text: 'An eminent colleague of mine (Alex Martelli) provided a very nice review
      of the book. He is very fond of it, but humorously scolded me for the phrase
      "data science" which he thinks is always sloganeering ... He prefers "data engineering."

      While I wouldn''t go full in with that chastisement, this book definitely is
      on the engineering side of things. I only minimally touch on specific machine
      learning models, but entirely on the concrete effort needed to get data ready
      for being modelled, visualized, statistically analyzed, or otherwise put to
      work. I guess my disagreement with Alex might simply be that I believe that
      concrete science (like physics, biology, chemistry, ecology, etc) is always
      just as messy and requires just as much engineering. Hence, I think the word
      "science" is okay.

      To your actual question, I try to provide as much as I can for how to make your
      data USEFUL, without great attachment to the admittedly buzzword-ish phrase
      "data science" per se.'
- name: Lalit Pagaria
  text: 'David Mertz thank you for doing this.

    1) We have so many end to end tools for ML pipeline. But I have observed pre processing
    part in it always semi manual. I also find very less tools solving this. Why is
    so? My main focus is towards Text besed NLP domain.'
  replies:
  - name: David Mertz
    text: 'I am not really optimistic about something like *Autoclean* coming to exist
      on the analogy of *AutoML*.  To simplify greatly, AutoML is kinda just "throw
      a bunch of different models at a problem, and compare the metrics.  Cleaning
      data requires a much more nuanced understanding of *why* the data has gone wrong,
      and how to remediate it.

      There''s an epigraph that I start an early chapter with, from Hadley Wickham
      (borrowing Tolstoy, of course): Tidy datasets are all alike, but every messy
      dataset is messy in its own way.'
  - name: Lalit Pagaria
    text: Thank you David. It is insightful
- name: Lalit Pagaria
  text: 2) For text cleaning (specifically large documents and paragraphs in QA domain)
    what framework do you suggest?
  replies:
  - name: David Mertz
    text: I'm afraid I largely have to plead ignorance here. I use, and write about
      things like NLTK, but I also haven't worked as much in NLP for a number of years.  There
      could be more tailored tools for this domain that I am not aware of in my attention
      on mostly tabular, mostly numeric, data.
- name: Lalit Pagaria
  text: "3) Fun question, is it possible to use BERT based model to clean text itself\
    \ (using model for pre processing)? Of course with proper training using good\
    \ dataset. \U0001F642"
  replies:
  - name: David Mertz
    text: Maybe. A colleague who advised me during writing really felt I should have
      a chapter on using models for the data cleaning itself.  I haven't worked with
      BERT as of date, but in general I felt that this topic was *interesting* but
      still at the stage of *promising* rather than ready for produciton.
- name: Ken Lee
  text: 'David Mertz thanks in advance for answering this question of mine.

    You mentioned the use of version tracking of data. It''s a good practice, definitely
    agreed. Any great tools that you would recommend for this purpose? Heard of DVC
    but never use it before.'
  replies:
  - name: David Mertz
    text: 'I have myself mostly just used regular Git tracking of data, for example
      with GitHub LFS.  That is relatively minimal change sets for textual data formats.

      However, I know there is an important limit in this approach.  While it is good
      for saving linear sequences of changes, it doesn''t completely scale to more
      complex branching patterns when data has shared provenance.  I do not know if
      DVC handles that well, but I probably should.'
  - name: Ken Lee
    text: Thanks David! Will definitely check out about Github LFS
- name: David Cox
  text: David Mertz Love the idea for this book and excited to check it out! It looks
    like it has a lot of great recommendations for how to handle different file types
    and common errors. My questions are around tools and technologies for helping
    speed-up the cleaning process. For example, do you have recommendations or insights
    on the benefits and drawbacks of different tools such as Open refine, Trifacta,
    Cloudingo, etc.?
  replies:
  - name: David Mertz
    text: "Much of what I talk about doing with Python, R, or other tools with a programmer\
      \ focus, can be done in those UI front ends as well.  In the book, while I give\
      \ particular examples, I try to remain tool agnostic.  So even though I might\
      \ show some Pandas code to perform a certain step, I do not mean it to be a\
      \ book about Pandas.  Doing that step with Open Refine, or Trifacta, or Cloudingo,\
      \ is just another option, much as would be doing it in the R tidyverse.\nThat\
      \ said, I will remain more fond of the kinds of tools I write about personally.\
      \  Part is simply my old-timey attachment to command line and programming language\
      \ tools.  The UIs like those you mention are targeted at folks somewhat less\
      \ comfortable with programming.\nBut beyond mere personal preference, these\
      \ \"friendly\" UI tools have some real drawbacks.  On the one hand, many are\
      \ commercial, which means both that they have extra costs per-seat, but even\
      \ more importantly, means that they have some vendor lock-in.  Once you've developed\
      \ complex work-flows in one tool, it becomes more difficult to switch tools.\n\
      Maybe even more important than the lock-in concern is when you reach limitations\
      \ of a tool.  For 90% of what you need to do in data cleanup and preparation,\
      \ those tools will probably do it.  However, once you reach that other 10%,\
      \ it becomes very difficult to add a new data manipulation, and usually means\
      \ going back to the programming tools that they are meant to avoid.\nIn contrast,\
      \ with Pandas, or scikit-learn, or the R tidyverse, you can also certainly hit\
      \ limitations in the provided capabilities.  But adding more\u2014well, it still\
      \ might be a pain in the ass, but it's a PITA using the same toolset\u2014it\
      \ is always possible to write custom functions that plug into the hooks provided\
      \ by those general libraries.  The tools are designed around such extensibility\
      \ in significant part."
  - name: David Cox
    text: "Thanks, David Mertz! Very helpful. I think one of the big challenges I\
      \ run into with my team is simply the time it takes for proper data cleaning\
      \ (says all data scientists everywhere \U0001F602). Do you have any recommendations\
      \ or best practice suggestions on building efficient and automated pipelines\
      \ for these data cleaning tasks?"
  - name: David Mertz
    text: 'I do. But basically, it takes 300,000 words to express them :-)

      ... I should go do a word count on the book to fine tune that number.'
  - name: David Cox
    text: Hahahaha...fair enough!
- name: Asmita
  text: Hi David Mertz, I have recently dived into the Data Science field and realised
    obtaining an efficient set of input data consumes the maximum time.  Like you
    said every messy dataset is messy in its own way, and this might result in the
    same process being performed on all datasets irrespective of it works or not.
    While understanding the data, and feature engineer, visualisation can help, how
    else can we figure out which technique of cleaning will give a better result?
  replies: []
- name: Asmita
  text: Also what advise would you give to someone who is new to the concept and is
    learning about the process of cleaning data ?
  replies:
  - name: David Mertz
    text: 'For better or worse, I think there really is just a lot of trial and error
      needed to find best practices, which are often specific to your domain and problem
      set.

      At some end of the process, you do something like train a model and have metrics
      to judge quality.  If those measures do not show success, ONE thing you should
      try is massaging the data preparation/cleaning process.

      Visualizations can definitely often help.  Finding the right angle in which
      to present data can many times make the problems really stand out.  But that''s
      very much an iterative process as well.  Many visualizations which are completely
      sensible in principle, even valuable, may not be the ones that actually expose
      the problems.'
  - name: Asmita
    text: So is it always trial and error, even with experience helping out one understand
      the data and insights that can be obtained?
- name: Neal Lathia
  text: "\u2754 At what stage of trying to clean &amp; make sense of data would you\
    \ give up and get the upstream system to log better data?"
  replies:
  - name: David Mertz
    text: 'This feels like a social question at least as much as a technical question.
      I might have a variety of kinds of relationships with the upstream provider,
      and the influence I might have over their processes varies hugely.

      Unfortunately, we as data scientists or data engineers often have little influence
      on that upstream. This can be true within one organization, but that much more
      so when different companies, agencies, etc are at different ends of the data
      pipeline.

      I don''t think a cut-off or threshold is the best way to think of it. Rather,
      universally, yes there are problems. But almost always there is *some* utility
      in the current data. So it tends to be about incremental, and ongoing, improvements
      to the upstream data, inasmuch as we influence that.'
- name: Vladimir Finkelshtein
  text: "Apart from manual inspection or anomaly detection is there a way to know\
    \ that the data needs more cleaning?\nI have seen this idea in some content from\
    \ Andrew Ng, in image classification they purposefully added some amount of mislabeled\
    \ images and calculated the reduction in the performance of a model. This should\
    \ give an estimate of how much performance could be gained from correcting certain\
    \ amount of labels. I wonder if similar approach can work with tabular data by,\
    \ say, randomly assigning extremal values in some columns\u2026"
  replies:
  - name: David Mertz
    text: "I think some of these concepts from machine learning models don't entirely\
      \ apply to data engineering (cleaning) steps. We don't really have straightforward\
      \ metrics in the same way \nOf course we can repeat statistical tests, or perform\
      \ new ones, but doing so is informed by domain knowledge or task purpose, rather\
      \ than by any independent measures of goodness/badness.\nIf you assign random\
      \ values to data cells to validate your remediation, it's completely predictable\
      \ how much you'll detect from the probability distributions you use for randomness.\
      \ But you don't really learn anything new thereby."
- name: David Cox
  text: Another question I'll pop out here, in case others are interested. How do
    you go about making decisions on how much/what to clean for operational databases
    versus pushing to data lakes and cleaning if/when needed? Asked differently, the
    volume of data many orgs handle makes it difficult to clean everything. What is
    your general strategy for picking what data to clean to maximize operational and
    innovative efficiencies?
  replies:
  - name: David Mertz
    text: "This is a great question! I'd be very interested to read how others in\
      \ this thread weigh these concerns.\nFor myself, I find that data cleaning is\
      \ sufficiently task driven that it often not possible\u2014but more specifically,\
      \ not even meaningful\u2014to \"clean the data\" without that's to some particular\
      \ goal."
  - name: David Cox
    text: Agreed! I'll be interested to hear what others indicate, as well. Some of
      the artful balance we are trying to strike is figuring out what data might be
      meaningful/relevant to various business decisions/operations before they specifically
      request it so that we can more efficiently respond to higher probability data
      requests.
  - name: Heeren Sharma
    text: "I totally agree with this approach as well. I think cleaning is highly\
      \ contextual and use case driven. Some teams take this decision based on the\
      \ frequency with which the particular data is being used. However in my personal\
      \ experience, devil lies in the detail. A financial data which needs to be used\
      \ once a year but needs to be of correct quality and on the other hand, tweet/retweet\
      \ stream where you are reading continuously but doesn\u2019t care much about\
      \ text encoding (or other elements) of each and every tweet. So all is about\
      \ use case binding for me as well."
- name: Shankar Somayajula
  text: 'Hi David Mertz, Cleaning data in a BI context usually refers to assigning
    defaults or unassigned dimension tags/keys to records which fail regular lookups...
    i.e. Have a special dimension value for each dimensional attribute so that this
    gets assigned in case nothing else works e.g. case when &lt;regular logic&gt;
    then &lt;regular values/labels&gt; else &lt;unassigned/default label here&gt;
    end. This effectively ensures that important event/fact/transactional information
    is retained and not lost if/when one enforces the fact to lookup/dimension joins
    in downstream applications.

    Coming to your book (from the ToC): Why impute missing values via some process
    rather than simply assign them a default/special category of "unassigned"? Can''t
    we view Data Science usage as yet another example of downstream usage of data
    (just like Business Intelligence)?'
  replies:
  - name: David Mertz
    text: 'Use of sentinels for missing (or unreliable) data is definitely relevant
      and sensible.  It''s downstream from the point where that is done that value
      imputation or discarding rows becomes an important decision.

      For example, numeric values like 999.9 and -1 are often used to mark missing
      data in formats that require numeric columns.  As long as those do not overlap
      with plausible measurement values, they are good sentinels.

      However, when you want to perform visualization, or statistical summary, or
      machine learning modeling, on the data, those sentinels become problems... specifically
      *because* they are implausible data values.  At that point, doing things like
      imputing median values in their place is often more useful (when accompanied
      by appropriate footnotes or metadata that make clear what you have done).'
  - name: Shankar Somayajula
    text: 'I take your point regd numeric fields and defaults like 999.9 and -1 or
      -99 etc. Normally we should just have Nulls instead of these special values.
      Median calculations should ignore such null value records.

      However, for categorical fields, i find the approach of imputing most prevalent
      value (mode) during Cleaning slightly worse than choosing sentinels (unassigned
      but valid, default value indicating missing data) as in my opinion that decision
      is not reversible (even if documented) and ought to be in the hands of the ultimate
      users of the data - The Analysts/Data Scientists etc.

      I don''t see what difference having implausible data values has for categorical
      variables (or for Viz/Stats/ML activities) when they too have been documented
      and catered for via defaults for missing as has been the case with BI typically.

      I would rather have 90 valid records with valid values and 10 records with missing
      categorized as "unassigned" letting me choose what to do with those 10 records
      than all valid values for this field across 100 records with metadata note:
      10 missing have been replaced by median value &lt;xyz&gt;.'
- name: Heeren Sharma
  text: "Hi David Mertz I was searching for a book like this for quite some time as\
    \ I realised that discussions around data quality are still somehow centered around\
    \ commercial tooling. This book is definitely a refreshing breeze. \U0001F642\
    \  As a data engineer (and on the top a consultant \U0001F648), I have come across\
    \ various discussion which centres around data cleaning, a quick blame game jump\
    \ over data quality and then somehow eureka moment style statement \u201CWe need\
    \ a data catalogue \U0001F604 \u201C. Building on the top of David Cox\u2019s\
    \ last question, do you also see data cleaning and data quality in the similar\
    \ light? And, may you provide some thoughts around data catalogues for primal\
    \ use to boost data quality. I am trying to explore to capture the knowledge \u201C\
    why you are cleaning that data\u201D into some sort of another structured and\
    \ persistent format (JSON/ YAML config file)  rather than code only."
  replies:
  - name: David Mertz
    text: 'Data catalogs are definitely valuable.  Part of metadata can and absolutely
      should include known problems... as well, of course, as version information
      on datasets that have undergone various remediations (cleaning).

      I avoided discussing closed source tools in the book.  This is both a natural
      distrust of them (who knows if it will become unavailable or lose features),
      and because they create walled gardens.  But some tools like Apache Atlas and
      Truedat do exist.'
  - name: Heeren Sharma
    text: "Many thanks for your insights! Another quick follow up question, do you\
      \ recommend a way/process in keeping data catalogues up to date? That\u2019\
      s also something that I have seen quite a bit in industry as a challenge. \U0001F642"
  - name: David Mertz
    text: I'm afraid I don't have any specific insight about that currently.
- name: Tim Becker
  text: Hi David Mertz, thank you for doing this. Does your book provide recipes for
    how to best solve different data cleaning tasks?
  replies:
  - name: David Mertz
    text: 'I very deliberately eschew "recipes."  Understanding the specific problem
      and specific dataset is crucial, and reducing a solution to a cargo-culted recipe
      is almost always going to do the wrong thing for your specific purpose.

      What I do discuss in considerable depth is how to *think about* the problem
      in hand, and likely techniques with which to approach it.'
- name: Tim Becker
  text: What are in your opinion the most important things to improve in order to
    become more efficient at data cleaning?
  replies:
  - name: David Mertz
    text: Practice and an understanding of your domain.  I mean, of course understanding
      particular tools like Pandas or R tidyverse are of huge value... but knowing
      what you *want* to do must come before simply learning APIs.
  - name: Ken Lee
    text: Been seeing APIs appearing continuously.. just wondering what exactly is
      an API? David Mertz
  - name: David Mertz
    text: Oh... Application Programming Interface.  It just means the names and arguments
      of the functions and methods that some particular software library or tool provides.
  - name: Tim Becker
    text: "thank you \U0001F642 David Mertz I guess, there is no easy way around data\
      \ cleaning and having domain knowledge."
- name: A McCauley
  text: Hi David Mertz data cleaning is quite a repetitive task, are you a fan of
    trying to automate as much of the process of data cleaning, such as stages of
    detecting areas that need cleaned etc?
  replies:
  - name: David Mertz
    text: 'Obviously automation save a whole lot of time.  I''d have a certain caution
      about some of it though.  If you really are automating cleanup/transformation
      of the SAME data source that has characteristic problems, of course it''s good
      to reuse the scripts you wrote in your first analysis.

      But applying those to very different data is likely to miss crucial issues.  Moreover,
      sometimes data coming from the same source can change character in certain ways,
      which may mean that you need to be sensitive to new kinds of cleanup issues
      that arise.'
- name: WingCode
  text: "Hi David Mertz,\nThou book shall be hailed amongst thy mortal Data Engineers!\
    \ Humor coupled with anything, I find is a fun way to learn about anything. I\
    \ would love to read your book! I had a few questions:\n1. Does one of the reasons.\
    \ that data cleaning issue stems from the fact of not having proper schema registry\
    \ or API format (OpenAPI) ? If we have proper schema registry in place everywhere,\
    \ we can track the evolution of schema and schema registry itself ensure that\
    \ missing fields, new fields, changes to schemas are handled. Using codegen coupled\
    \ with API format, we can ensure that clients don't break with data changes. \n\
    2. One of the biggest problems I have faced with respect to data cleaning is deduplication.\
    \ The same information can be represented in magnitudes of different ways. For\
    \ example: 2 Product description of the latest &amp; greatest phone. \"This is\
    \ the fastest phone from Pineapple with 256GB of RAM, 1GHz processor and available\
    \ in all color spectrum under the RGB space\" Vs \"Coupled with 256GB of RAM,\
    \ 1GHz processor and available in all colors you can dream of, this is the Pineapple\
    \ phone\". Is there any good library, frameworks which you found useful in deduplication\
    \ of data?\n3. Assume a Utopia ( that one I am dearly waiting for) every single\
    \ person &amp; organisation follows the same proper data standards (naming conventions,\
    \ schema standards, JSON response standards). Do you think we will have data cleaning\
    \ issues?"
  replies:
  - name: David Mertz
    text: 'I''ll go by parts.

      1. Having (versioned) schema registries might help a certain proportion of data
      integrity issues.  My feeling is that it''s a fairly small percentage though.

      I find that errors because of instrumentation faults, human transcription errors,
      bias in selection, recording failures, etc. are much more prevalent.  All of
      those apply just as much even when the schema is clearly understood and followed
      by all ends of the data processing.'
  - name: David Mertz
    text: '2. I think the question is about plain text descriptions that may describe
      the same thing but be worded differently. I''m not sure.  I discuss in some
      moderate detail analyzing string similarity in the book.

      That said, for something like a product description, anything mechanical will
      probably fail. Version 16 and Version 17 of the same line are likely to use
      largely the same marketing language (and hence have similar strings).  More
      sophisticated semantic concept clustering doesn''t improve that problem.  In
      fact, even a different product, in whatever version, is likely to use similar
      marketing language, especially from the same maker.

      Anything you do that says "equivalent descriptions name the same product" will
      get as many false positives as true positives.'
  - name: David Mertz
    text: 3. In your utopia, do all instruments record measurements correctly? I guess
      some religious doctrines have a notion of an afterlife of such perfection, so
      I suppose if you follow one of those, it's something to hope for.
  - name: WingCode
    text: Thank you David for your time and replies. I wish you all the best for the
      book!
- name: David Mertz
  text: 'It''s been nice having folks comment this week.  I''m happy to reply for
    however many more hours the timezone indicates, or indeed in general personally,
    to any questions.

    Can I ask participants a favor? Apparently more Amazon reviews helps convince
    them the promote my book, and Packt essentially makes itself a subsidiary of Amazon
    (not happy about that; but such is life).  So if contributors to this thread write
    reviews (and buy the book, of course), it helps me.'
  replies: []
---

It is something of a truism in data science, data analysis, or machine learning that most of
the effort needed to achieve your actual purpose lies in cleaning your data. Written in David’s
signature friendly and humorous style, this book discusses in detail the essential steps performed
in every production data science or data analysis pipeline and prepares you for data visualization
and modeling results.


The book dives into the practical application of tools and techniques needed for data ingestion,
anomaly detection, value imputation, and feature engineering. It also offers long-form
exercises at the end of each chapter to practice the skills acquired.

