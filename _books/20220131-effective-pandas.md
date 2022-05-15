---
title: "Effective Pandas"
description: "Book of the Week. Effective Pandas by Matt Harrison"
cover: "images/books/20220131-effective-pandas/cover.jpg"
image: "images/books/20220131-effective-pandas/preview.jpg"
start: 2022-01-31 00:00:00
end: 2022-02-04 22:59:58
authors: [mattharrison]
links:
  - text: Buy the book
    link: https://store.metasnake.com/effective-pandas-book
  - text: Announcement post
    link: https://hairysun.com/announcing-effective-pandas.html


archive:
- name: Tim
  text: 'Kindly, I would like to know:

    How this book is different from the other books that @Matt Harrison has written?'
  replies:
  - name: Matt Harrison
    text: Hi Tim, Great question. My first Pandas book, _Learning the Pandas Library,_
      was one of the first books on Pandas. After that book I had the chance to use
      Pandas even more, teaching and consulting with it. I had been planning on updating
      it after those experiences. In the meantime I was approached to do the second
      edition of the _Pandas Cookbook_. I had read the 1st edition and liked it. Though
      I added a few chapters to the cookbook, I also re-wrote almost all of the code.
      I think it is a great book. However, it is not "my" book. (edited)
- name: Dr Abdulrahman Baqais
  text: 'Thank you. Sounds an interesting book. I would like you ask few questions:

    1) What do you mean effective? Time performance, readibility, best practise among
    other choices....

    2) Some of the methods performed by Pandas can be done by other libraries such
    as : nupmy or sciket learn. For example:null impuatation or categorical varible
    conversion.  Was there a comparison ?

    3) Pandas is evolving and 1.0 already there. Do you think thaere is still a large
    room for improvement in a Pandas and in which areas?

    4) When it is advisable to use Pandas? Any guirlines on the best cases where Pandas
    are preferred over R   packages for example.

    5) Where are the neck pains of pandas.  For example transpose a dataframe is very
    slow comapring to transposing a numpy array.

    Thank you so much and your expertise surely will help us.'
  replies:
  - name: Matt Harrison
    text: "Hi Dr Abdulrahman Baqais\n1. Yes. You can read reviews. This book teaches\
      \ a Pandas style that few teach, however it will completely change your Pandas\
      \ code.\n2. No. This is not an ML book. I was tempted to do an ML chapter but\
      \ early reviewers advised against it. Perhaps in the next edition.\n3. Great\
      \ question. The Pandas API is HUGE. However, if you master a small subset, you\
      \ can be really productive. Personally (in consulting, training, and using Pandas),\
      \ I haven't found post 1.x features to be used much. What is more interesting\
      \ to me is optimization and the notion of the Pandas \"API\" being the standard\
      \ interface for interacting with data in Python. (See libraries for scaleout,\
      \ GPU, etc that all have a Pandas API).\n4. I don't use R in happiness or anger.\U0001F609\
      \ So I'm heavily biased for using Python. Use Pandas when you have \"small\"\
      \ data. Use the Pandas API after that.\n5. Great example. Numpy is excellent\
      \ for matrices of like-typed data. You can use Pandas for that but as you mention\
      \ things like transpose aren't really meant for hetergenous data types. Index\
      \ assignment is probably the biggest thing. It leads to confusion and bugs.\n\
      (edited)"
- name: "ousk\xE4"
  text: 'Hello, thank you very much for doing this. I would like to know:

    1. Who is your target audience for this book?

    2. Are there any prerequisites needed to get the most out of the book?

    3. How is it Different than the _Pandas 1.x Cookbook (with Ted_ Petrou) ?

    4. There are so many Python-based libraries out there which can be used for a
    variety of data science tasks. Where does pandas fit into this picture?

    5. What are the most challenging lessons that you have learned while working on
    this book?

    6. What advice would you have for beginners in data science/engineering? What
    things should they keep in mind while designing and developing their data science/engineering
    workflow?

    7. Are there any specific resources which we could refer to, apart from this book
    of course?

    Thank you.'
  replies:
  - name: Matt Harrison
    text: "ousk\xE4, thanks for your questions.\n1. The target audience is anyone\
      \ who wants to write better pandas code.\n2. Basic Python skills: Functions,\
      \ loops. After that, I really encourage Lambdas and Comprehension constructs,\
      \ and argument unpacking.\n3. See my answer to Tim. Cookbook is a great book,\
      \ however, it is not the book I want.\n4. If you have tabular data that fits\
      \ on your machine, Pandas should be at the top of your list. If it doesn't fit\
      \ on your machine consider the pandas \"API\" (spark, dask, modin, etc).\n5.\
      \ With respect to book authoring: books always take longer to write. (I wish\
      \ it were out a year earlier). With respect to the content: finding real-world\
      \ data to illustrate concepts is challenging. Also, the API is HUGE, considering\
      \ what percent to cover is always a tradeoff.\n6. Work on projects that interest\
      \ you and you can learn from. Learn the basics of software engineering even\
      \ if you don't want to be a \"programmer\". You are using a programming tool.\n\
      7. Watch my PyData talk for some of the big ideas from the book [https://www.youtube.com/watch?v=zgbUk90aQ6A&amp;t=4604s](https://www.youtube.com/watch?v=zgbUk90aQ6A&amp;t=4604s)"
- name: Tim
  text: 'Matt Harrison Thank you very much for your response. Well noted. Second question
    if you don''t mind.

    - There have been some errors that occur due to the latest version of pandas.
    Is there a section in your book handling this? eg performance warning, Future
    warning ''your data frame is defragmented'''
  replies:
  - name: Matt Harrison
    text: I intentionally write (and teach) Pandas in a way to avoid errors/warnings.
  - name: Matt Harrison
    text: I do have some content on date and timezone conversion issues.
  - name: Tim
    text: What is the pricing? Does it come on paperback only or there is a kindle
      version?
  - name: Matt Harrison
    text: Paperback is on Amazon. Digital version at [https://store.metasnake.com](https://store.metasnake.com)
  - name: Tim
    text: 'Okay. Thank you very much Matt. I appreciate the time you took to answer
      my questions. It was nice chatting with you. I certainly hope I can get my hands
      on this book.

      Good luck and stay safe.'
- name: "Philip Die\xDFner"
  text: 'Hi Matt Harrison, thanks for being with us!

    1. What is your favorite functionality in Pandas that you would never want to
    miss? (If it is chaining, I also would be interested in #2 )

    2. What do you think are the most common anti-patterns, which might trap people
    with experience in Python and starting with Pandas?

    3. What part of the API are you using now very often that you picked up on far
    too late?'
  replies:
  - name: Matt Harrison
    text: "1. Great question. I would probably say the ease of grouping and aggregating\
      \ or visualization.\n2. inplace, index assignment, .apply, reading bad advice\
      \ on the internet. \U0001F609\n3. Chaining. Not really an API, but a game-changer."
  - name: Alexey Grigorev
    text: can you show an example of chaining?
  - name: Matt Harrison
    text: See the get_sales function in attached image
  - name: Alexey Grigorev
    text: looks nice, thanks!
  - name: Michael Harty
    text: "inplace did seem like such a great idea when I first heard about it \U0001F605\
      \nIn reference to Alexey's comment below about dplyr, I have barely used it,\
      \ but many of my teammates use it, and they have shown me the basics. Not too\
      \ long ago I thought. Wouldn't it be nice if we could do this piping in pandas.\n\
      Turns out you can and it's called method chaining. My python code has started\
      \ to look a lot more similar to the dplyr pipes (and a lot better too) once\
      \ I started learning how method chaining works"
  - name: "Philip Die\xDFner"
    text: Matt Harrison Thanks for your answers! Regarding 2., as I have experienced
      the others but not this, could you explain the index assignment a bit or give
      an example?
  - name: Matt Harrison
    text: Using index assignment makes it hard to chain because assignment doesn't
      return a pandas object to chain on. Also, it exposes you to potential bugs because
      you might be working a view or a copy.
  - name: Michael Harty
    text: What exactly do you mean by index assignment?
  - name: Matt Harrison
    text: 'Updating a column by doing something like this. `df[col] = new_col`

      You should be doing this instead`df.assign(col=new_col)`'
- name: Alexey Grigorev
  text: What do you think about the convergence to this pandas API? Wouldn't the world
    be better off if instead everyone used something similar to [dplyr](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html)?
  replies:
  - name: Matt Harrison
    text: 'The Python world (which is arguable 10-100X bigger than the R world) has
      converged on the Pandas API. I personally don''t think Pandas is the perfect
      API (certainly there are tough spots for beginners), but it is where we are
      at today.

      I think it is a good thing in that an investment in learning pandas turns out
      to be a super-power when you need to move to Spark or Dask.'
- name: Evren Unal
  text: "Hi Matt Harrison \nI would like to learn a tool which i can use to manipulate\
    \ ndim array easly\nIs Series enough for this job, or do i need to learn data\
    \ Frames as well?"
  replies:
  - name: Matt Harrison
    text: 'For n-dimensional arrays of the same type use numpy.

      WRT pandas, +80% of the interface of Series and DataFrame is the same (one is
      applied to 1-dimension, the other 2-dimension)'
  - name: Evren Unal
    text: "Thank you \U0001F44D"
- name: Varun Nayyar
  text: "Hey Matt Harrison welcome and congratulations on your latest Book.\nIt would\
    \ be great if you could answer a few questions I have.\n1. How superior is it\
    \ to your Pandas cookbook from Packt?\n2. Is the book for beginners or for people\
    \ with some prior experience in pandas? Or indifferent to all levels?\n3. How\
    \ easy would it be for someone after this book to transition to PySpark for big\
    \ data manipulation? \n4. Why do you think pandas is a better choice for data\
    \ manipulation when compared with other Libraries in python? \n5. Would you say\
    \ that this book is a reference book or does it require thorough reading to get\
    \ the best out of it?\n6. Is there some content dedicated to what after pandas?\
    \ For example preprocessing and feature engineering for ML models?\nForgive me\
    \ if there's any overlap in the questions which you previously answered.\nAll\
    \ the best for your book.\nHoping to grab a copy\u2728"
  replies:
  - name: Matt Harrison
    text: "1. Much superior \U0001F609 (See other threads)\n2. Anyone who wants to\
      \ improve their Pandas. I have reviews from beginners and experience alike that\
      \ this is changing how they think about Pandas.\n3. PySpark recently merged\
      \ the \"Pandas API\" \U0001F609\n4. It is better for \"structured\" or \"tabular\"\
      \ data. Because it is built for that use case but also leverages NumPy so it\
      \ is speedy and memory efficient.\n5. There is a reference section at the end\
      \ of each chapter. However, you can pick chapters that might be relevant to\
      \ you.\n6. It is focused on Pandas. There is an example of ML in the book, but\
      \ it is not the focus.\nCheers!"
- name: Bhaskar Sarma
  text: 'Hi Matt Harrison congratulations and thank you for deciding to answer our
    questions on this community.

    I would like to ask three questions:

    1. What is the presentation style in the book? Do you present through independent
    small examples through the whole book or, you start with small examples and then
    build up to a big project towards the end?

    2. In one of the previous answers, you have told that "Use Pandas when you have
    small data. Use the Pandas API after that". Where do you draw the line between
    small and big data (if you want to call it) ?

    3. What is the difference between Pandas and Pandas API ? Asking as a beginner
    in Data Science and Pandas.

    Thank you'
  replies:
  - name: Matt Harrison
    text: '1. There are "projects" scattered throughout the book. However, in contrast
      to many Pandas resources, I try to use real-world data throughout. So my code
      may be a little more complicated because it is not using canned data.

      2. Small data (IMO) is data that will fit on a single* machine.

      3. Pandas implements the Pandas API. So does Dask and Spark and about a dozen
      other projects.

      `* - Small varies as a single machine might have a few gigs to 100+gigs these
      days.'
- name: William Jamir
  text: "Congratulations on your book!\nI would like to know more about your opinion\
    \ on \u201Cinplace\u201D operations, do you think there are valid cases to use\
    \ it? (like memory consumption perhaps)\nAlso, does your book address best practices\
    \ around inplace oprerations, or does it \u201Ccompletely\u201D ban its use?"
  replies:
  - name: Matt Harrison
    text: 'I recommend disregarding "inplace". Don''t use it. In general it doesn''t
      do what you think it does and it prohibits chaining. There is a dialog among
      pandas devs to remove it completely.

      Yes, my book has best practices which include "don''t use inplace". Check out
      the reviews at [https://store.metasnake.com/effective-pandas-book](https://store.metasnake.com/effective-pandas-book)
      to see how people are changing their code after going through the book.'
- name: Michael Harty
  text: One of first things I noticed when trying your style of method chaining is
    that black code formatting does not agree with it. Have you found any formatters
    that work? Or in your opinion, is it best to not use one for pandas code?
  replies:
  - name: Matt Harrison
    text: "I've thought about making \"black panda\"... (not enough time in the day).\n\
      Yes, black is horrible for properly chained pandas code. Right now I just format\
      \ it manually. \U0001F622"
  - name: Michael Harty
    text: "oh yeah, \u201Cblack panda\u201D would be great"
- name: A
  text: 'Hello Matt!

    In a world where currently either most Data Scientists either strive for more
    core modelling skills or core engineering skills (mainly with respect to being
    more MLOps aware), how would you place skills like writing effective pandas code?

    Also, what do you think is the biggest reason why people fail to write effective
    pandas code? Do you think is it because pandas is mainly used for exploratory
    work and thus, Data Scientists do not see much upside in learning it effectively
    or is this lack of awareness about what exactly is effective pandas?

    Good luck with your book!'
  replies:
  - name: Matt Harrison
    text: 'Pandas is useful for both exploring and creating pipelines. Generally the
      former is done in a very loose manner. The latter is done by software engineers.
      Many "scientists" claim they don''t want to be programmers and ignore best-practices.

      Most of the examples of pandas code on blogs, videos, books, or otherwise push
      learners to use poor coding practices. I think that is because we are pretty
      early on with the library and crossovers from science to programming. Take heart,
      best practices are emerging though!'
- name: Michael Harty
  text: "I\u2019m curious in your experience teaching pandas do you take a different\
    \ approach based on your specific audience\u2019s background? Im thinking there\
    \ might be a different approach to a team of analysts that work largely in excel\
    \ (like many of the engineers I work with) versus analysts who are more familiar\
    \ with SQL but not Python and pandas. Thanks \U0001F64F\U0001F3FB"
  replies:
  - name: Matt Harrison
    text: 'In my live courses I generally try to cater the content to the experience
      level of the attendees. Certainly I''ve seen that Excel experts prefer .pivot_table
      while database gurus like .groupby. :woman-shrugging:'
- name: Tim Becker
  text: Hi Matt Harrison, thanks for this interesting book! I would like to know what
    are the biggest anti-patterns in terms of computational speed. For example, if
    I remember correctly, iterrows seems to be very slow. Is there a situation in
    which you would recommend iterrow?
  replies:
  - name: Matt Harrison
    text: 'You want to stay in the "fast path" in pandas for numeric operations. Using
      .apply and .iterrows are generally bad for numeric performance. However, they
      are fine for string operations (though you may want to consider conversion to
      categoricals) as strings are already on the "slow path".

      I generally only find myself using .iterrows when I''m tweaking labels on a
      plot.

      HTH'
- name: Beau Waldrop
  text: Hi Matt Harrison, what's something in pandas that is super useful that you
    feel doesn't get used enough by a lot of people working in data?
  replies:
  - name: Matt Harrison
    text: 'Great question.

      Many people don''t realize how easy it can be to visualize with pandas. Especially
      with an aggregation.'
- name: Aruna Sri
  text: 'Hi Matt Harrison,

    Congratulations on the release of the book,  I am sure it will cover many techniques
    to help the ML community. Could you share your insights in reducing latency time
    with Pandas operations for real time ML applications especially computer vision.

    Thanks'
  replies:
  - name: Matt Harrison
    text: Hi Aruna, You want to stay in the "fast path" for numeric operations. Avoid
      .apply, .iterrows, etc. Use vectorized operations where possible.
- name: William Jamir
  text: "For a team that doesn\u2019t have much experience with pandas, what is your\
    \ suggestion to better educate the team to write \u201Cidiomatic\u201D pandas\
    \ code (besides reading your book \U0001F913) ? Do you know any tools/linters\
    \ that can help with this task?"
  replies:
  - name: Matt Harrison
    text: "Hi William, I'm not aware of linters for pandas, however I am very opinionated\
      \ regarding best ways to educate a team.\U0001F609\nIn fact, I wrote a post\
      \ about it ... [https://www.metasnake.com/blog/learn-python-2021.html](https://www.metasnake.com/blog/learn-python-2021.html)"
- name: Roy Jafari
  text: 'Hi Matt! I just ordered the book and looking forward to reading and improving
    my pandas'' coding and knowledge.

    Obviously, you have a great depth of experience and expertise with programming
    and pandas and I am thankful that you are sharing that with us through this book.
    My question is exactly about this experience and expertise. How would you describe
    it? How many years and what type of experiences has led you to this exciting book?'
  replies:
  - name: Matt Harrison
    text: Hi Roy, these days anyone can write a book. You just need to want to. I
      will say that many of the practices in the book came after years of using Pandas
      and deriving strong opinions.

---

Best practices for manipulating data with Pandas. This book will arm you with years of knowledge and experience that are condensed into an easy to follow format. Rather than taking months reading blogs and websites and searching mailing lists and groups, this book will teach you how to write good Pandas code.