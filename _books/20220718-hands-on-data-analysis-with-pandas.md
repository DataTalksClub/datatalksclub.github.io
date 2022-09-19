---
authors:
- stefaniemolin
cover: images/books/20220718-hands-on-data-analysis-with-pandas/cover.jpg
description: Book of the Week. Hands-On Data Analysis with Pandas - Second Edition
  by Stefanie Molin
end: 2022-07-22 23:59:59
image: images/books/20220718-hands-on-data-analysis-with-pandas/preview.jpg
links:
- link: https://www.packtpub.com/product/hands-on-data-analysis-with-pandas-second-edition/9781800563452
  text: Book's page
- link: https://www.amazon.com/Hands-Data-Analysis-Pandas-visualization-ebook/dp/B08R67H7F5
  text: Buy on Amazon
- link: https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas-2nd-edition
  text: GitHub repository
start: 2022-07-18 00:00:00
title: Hands-On Data Analysis with Pandas - Second Edition

archive:
- name: Alexey Grigorev
  text: Hi Stefanie! Which datasets did you use in the book? And do you know some
    good datasets that you wanted to use in the book but at the end didn't?
  replies:
  - name: Stefanie Molin
    text: "Hi Alexey \u2013 there are many datasets in the book: earthquakes, weather,\
      \ stock prices, planets, and wine. For some of these datasets, I also cover\
      \ how to use APIs to collect the data."
  - name: Stefanie Molin
    text: The UCI Machine Learning Repository ([https://archive.ics.uci.edu/ml/datasets.php](https://archive.ics.uci.edu/ml/datasets.php))
      is a great spot to find public datasets, as are government websites (I provide
      lots of sources in chapter 12). Narrowing it down ultimately came down to what
      would be interesting to write about that would also make for good examples.
  - name: Stefanie Molin
    text: When I designed my workshops ([https://github.com/stefmolin?tab=repositories&amp;q=workshop&amp;type=source&amp;language=&amp;sort=](https://github.com/stefmolin?tab=repositories&amp;q=workshop&amp;type=source&amp;language=&amp;sort=)),
      I wanted to use different datasets (e.g., taxi rides and meteorites), so people
      would have new examples.
- name: "Jos\xE9 Mar\xEDa Vargas Mendoza"
  text: Hello, Stefanie! In your experience, what methods have proven to be effective
    in spear-heading the transition from the "ol' reliable" Excel to Python for analytics?
    A lot of small to medium businesses (specially those who are already established
    in the market for some time) tend to rely on Excel a lot, and the analysts who
    try to introduce Pandas, Dask, or other tools available to the process, usually
    get blocked by the stakeholders.
  replies:
  - name: Stefanie Molin
    text: "Automation, automation, automation. In my experience, framing the move\
      \ from Excel (or similar tools)  to coding as freeing up time for new analyses\
      \ is key. Are there frequent requests for stakeholders that can be automated?\
      \ Automate those and work on something that you wouldn't have had time for if\
      \ you needed to use Excel \u2013 the stakeholders will see the additional value\
      \ being provided."
  - name: "Jos\xE9 Mar\xEDa Vargas Mendoza"
    text: Thanks for your answer! Indeed, there are quite a number of processes that
      have the potential for being automated in the classic "analytics with Excel"
      workflow. Hopefully, as more and more analysts adopt Python and other tools
      as their go-to for day-to-day analytics, businesses of all sizes start implementing
      changes to accommodate these newer, more efficient workflows in their operations.
- name: Sergio Rozada
  text: Hi Stefanie!! Thanks for being here. Can you share some insights in the key
    Pandas aspects that we have to look closely when deploying anything involving
    Pandas in pro?
  replies:
  - name: Stefanie Molin
    text: "Hi Sergio \u2013 The first thing to consider is whether you actually need\
      \ pandas in what you are deploying. While pandas makes it very easy to explore\
      \ your data and figure out what kind of processing you need, it has some overhead,\
      \ which can be mitigated by converting your logic into standard Python objects\
      \ once you have thoroughly explored and identified what needs to be done.\n\
      Secondly, if you must use pandas in production, it's important to consider how\
      \ you are using it. Are you immediately removing columns/rows once they are\
      \ no longer of use? Are you converting strings to categories? Are you performing\
      \ operations in place, where possible? Are you using chaining? If not, you are\
      \ probably making multiple copies of that data in memory for each operation,\
      \ which is going to be costly."
- name: serdar
  text: Hi. Excuse my ignorance i am new to ML but dont you think we might really
    need to work big data when it comes to real world problems? Feel like we really
    need to use pyspark iso pandas for better performance.
  replies:
  - name: Stefanie Molin
    text: "I'm a firm believer that you need to use the best tool for the job. Sometimes\
      \ that's pandas and sometimes it isn't. You will encounter numerous datasets\
      \ that aren't big data, on which you can comfortably use pandas without the\
      \ need for PySpark \u2013 it's important not to prematurely optimize. \nAlso,\
      \ keep in mind that ML is not exclusive to big data by any means. Consider a\
      \ linear regression to find the relationship between price and number of goods\
      \ sold: do you need millions of points to calculate that? Definitely not \u2013\
      \ you could get an answer much quicker and just as accurate with significantly\
      \ fewer data points."
  - name: serdar
    text: Thank you very much for the clarification.
- name: Ashish Lalchandani
  text: Hi Stefanie! Thanks for being here! I always struggle with EDA whenever working
    on a dataset. I see many people posting their code on kaggle, and everyone  performs
    EDA in different manner.  My question is, is there any standard way to perform
    EDA, like step 1 -&gt; do this, step 2 -&gt; do that, etc.?
  replies:
  - name: Stefanie Molin
    text: "Hi Ashish. Unfortunately not. People will approach this differently. Different\
      \ datasets may require you to approach things differently, as well. The emphasis\
      \ is really on the \"exploratory\" part \u2013 you will move around between\
      \ cleaning, wrangling, and visualizing the data as you explore, but you are\
      \ free to explore how you see fit."
  - name: Ashish Lalchandani
    text: Okay so cleaning, wrangling and visualizing is a must, and other than that
      we are free to play with data however we like. Got it, thanks!
- name: Tyrone Li
  text: 'Hi Stefanie! It was great meeting you at ODSC East this year! I''m fairly
    new to Python so I''m curious: what were some of the key methods that helped you
    to transition from learning how to use Python to eventually becoming an expert
    with a textbook of your own? For instance, do you make a habit of perusing other
    textbooks? Or perhaps you spend a good bit of time interacting with other practitioners
    in the field and their githubs? Many people learn how to code but writing your
    own book is absolutely next level, so I''m curious how that happened.'
  replies:
  - name: Stefanie Molin
    text: "Hi Tyrone \u2013 nice to see you here! While learning how to use Python,\
      \ I did a lot of LeetCode (and similar sites) and practice projects. I perused\
      \ some books to get started with the Python data science stack, but the biggest\
      \ help was using the libraries for projects both at work and at home. Going\
      \ through the docs and trying out what's there on datasets I was working on\
      \ helped me more than looking at the examples in the docs. For me a big part\
      \ is having a use case or project, identifying a tool, and then learning how\
      \ to make it work. \nAs far as the book, Packt (my publisher) reached out to\
      \ me about writing it. From the books and documentation I had read while learning,\
      \ I had lots of ideas of how I would approach it differently, and I knew writing\
      \ it would make me even more knowledgeable on the topic. Teaching is one of\
      \ the best ways to learn since it forces you to fill in the gaps in your knowledge\
      \ \u2013 the things that you know how to use but can't explain  the how/why\
      \ behind them. The same goes for my workshops: I learned plenty of things while\
      \ creating them as well. For me, it's important to always be learning something."
- name: Carlos Orjuela
  text: Hi Stefanie Molin , thanks for taking the time to answer our questions....
    Does the book deal with working through Pandas error messages or do you have any
    suggestions on this? I'm not expert and I've found sometimes a bit difficult to
    try to understand what's going on
  replies:
  - name: Stefanie Molin
    text: "Hi Carlos - Beyond a specific error related to not using loc/iloc, it does\
      \ not. However, this is a skill that isn't exclusive to pandas code, so it's\
      \ definitely important to hone it. Python 3.11 is going to have better error\
      \ messages that should make this easier, but we will still need to have this\
      \ skill. \nWhat I do when I'm faced with an error message is first look at the\
      \ type of error, the error message, and also the stack trace to find the line\
      \ where the exception was triggered. With that information, I work on debugging\
      \ the code: what does the data look like just before the code that raised the\
      \ exception was called? Understanding the format that different functions expect\
      \ their parameters will help you narrow down where the issue could be, so if\
      \ you aren't too familiar with that code, check out the docs. Googling the error\
      \ is also helpful if you can't see why it is happening. Another useful strategy\
      \ is to break down everything into simple operations so instead of chaining\
      \ multiple calls, run each one separately to see exactly where it is failing."
- name: Tim Becker
  text: Hi Stefanie Molin, thanks for being here. I am wondering what is new in the
    second edition? Also, in your opinion, what are the most useful pandas features
    that are rarely used?
  replies:
  - name: Stefanie Molin
    text: "Hi Tim \u2013 for the second edition, all code examples have been updated\
      \ for newer versions of the libraries used. The second edition also features\
      \ new/revised examples highlighting new features. For pandas in particular,\
      \ the first edition uses a much older version than what is currently available\
      \ (pre 1.0), and this edition brings the content up to date with the latest\
      \ version (1.x). You can look through the pandas release notes to get an idea\
      \ of all the changes that have happened since the version of pandas used in\
      \ the first edition (0.23.4). In addition, there are significant changes to\
      \ the content of some chapters, while others have new and improved examples\
      \ and/or datasets."
  - name: Stefanie Molin
    text: As for your second question, I've often seen casual users not using assign()
      or not being aware that pandas has plotting functionality. Many people also
      don't realize that you can resample by month but use the start date of the month
      instead of the end date just by changing the frequency to MS instead of just
      S (always check the docs before trying to hack something together). Another
      would be crosstabs, which are a very powerful feature that people seem to forget
      about.
  - name: Tim Becker
    text: "Thank you! \U0001F642"

---

Data analysis has become an essential skill in a variety of domains where knowing how to work with data and extract insights can generate significant value. Hands-On Data Analysis with Pandas will show you how to analyze your data, get started with machine learning, and work effectively with the Python libraries often used for data science, such as pandas, NumPy, matplotlib, seaborn, and scikit-learn.

Using real-world datasets, you will learn how to use the pandas library to perform data wrangling to reshape, clean, and aggregate your data. Then, you will learn how to conduct exploratory data analysis by calculating summary statistics and visualizing the data to find patterns. In the concluding chapters, you will explore some applications of anomaly detection, regression, clustering, and classification using scikit-learn to make predictions based on past data.

This updated edition will equip you with the skills you need to use pandas 1.x to efficiently perform various data manipulation tasks, reliably reproduce analyses, and visualize your data for effective decision making—valuable knowledge that can be applied across multiple domains.