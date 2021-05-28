---
title: "Street Coder"
description: "Book of the Week. Street Coder by Sedat Kapanoglu"
cover: "images/books/20210322-street-coder/cover.jpg"
image: "images/books/20210322-street-coder/preview.jpg"
start: 2021-03-22 00:00:00
end: 2021-03-26 22:59:58
authors: [sedatkapanoglu]
links: 
  - text: Book's page
    link: https://www.manning.com/books/street-coder
  - text: Book's GitHub repository
    link: https://github.com/ssg/streetcoder

archive:
- name: Alexey Grigorev
  text: 'Hi Sedat Kapanoglu, thanks a lot for finding time to take our questions!

    I prepared a few, so let me start with the first one.

    I know there are some "rules" in software development. Like you need to have X%
    test coverage, your code needs to follow the SOLID principles, etc. So what are
    these rules? Do you have a list of them?'
  replies:
  - name: Sedat Kapanoglu
    text: "Thanks Alexey Grigorev for the opportunity! The rules in software development\
      \ are mostly folkloric tales that come from curriculum, code reviews, or HackerNews.\
      \ Because of their viral nature, it's hard to come up with a complete list.\
      \ But, the common narrative among those rules are that they are treated like\
      \ immutable laws that can't be questioned. For example, when talking about SOLID,\
      \ you should follow SOLID all the way without questioning the reasoning behind\
      \ them. That kind of approach usually makes you spend too much time on stuff\
      \ that doesn't really matter in a professional setting where I call \"the streets\"\
      \ in the book. In the streets, the rules are vague, priorities are fluid. Similarly\
      \ with X% test coverage, you might spend a disproportionate time developing\
      \ the last 1% because you might feel the urge to at least achieve X%, rather\
      \ than X-1%. So, I go over some of these rules and either explain the nonsense\
      \ behind the rule, or explain the actual justification behind it so, the next\
      \ time it comes up in code review, you can defend yourself. \U0001F642"
  - name: Alexey Grigorev
    text: 'Thanks! Are these other similar rules and best practices that we usually
      try to follow - and they are sold as silver bullets?

      Like pair programming, following TDD and these sorts of things'
  - name: Sedat Kapanoglu
    text: 'Alexey Grigorev Exactly. I''m all for silver bullets, but like literal
      silver bullets, they are rare and they work worse than described in the books.
      They usually create more problems than they solve when treated as immutable
      laws. Since you mentioned it, I have a section in the book called "Don''t use
      TDD". Unit testing is invaluable, but TDD itself is unnecessarily constraining.
      I think rapid prototyping and retrofitting tests to an existing code is a much
      faster and practical approach. In "the streets", requirements change all the
      time and TDD assumes a spec is ready beforehand and won''t be updated a lot.
      I find it disconnected from the reality.

      I don''t go into pair programming in the book, (perhaps I should). Pair programming
      is very effective in getting the code quality up, adding to the productivity
      of the developer. The problem is that pair programming achieves this with the
      expense of another developer, completely blocking their work. It''s inefficient
      in that sense. I find code reviews a fair compromise.'
- name: Alper Demirel
  text: "Hi Sedat Kapanoglu,\n- What are the most important gains we will achieve\
    \ when the book is finished? \n- Also, what is your motivation to write the book?\n\
    I'm a big follower on Twitter, thank you this opportunity \U0001F44B"
  replies:
  - name: Sedat Kapanoglu
    text: "Hi Alper Demirel! I think the one key takeaway would be that the rules\
      \ and paradigms have some reasoning, some logic behind them, and knowing their\
      \ logic would help you decide to make better decisions in a constrained setting,\
      \ usually the case with professional career. I usually try to explain the details\
      \ of certain concepts (like how a class is laid out in memory), so you exactly\
      \ know when a class or a struct would be preferable, and why, rather than \"\
      hey stick to classes and you're fine\". When you internalize the reasoning behind\
      \ these concepts, your decision making process in a professional setting becomes\
      \ both fast and accurate. More importantly, you don't dig yourself into a hole\
      \ \U0001F642\nAbout motivation, I started to keep notes years ago for a potential\
      \ book that might help the software developers I work with, so I don't have\
      \ to repeat myself on every topic. A new developer is usually idealistic and\
      \ dogmatic as neither have they an understanding of the inner workings of the\
      \ rule set they're working with, nor they have been in a professional setting\
      \ enough to prioritize the problems. I wanted to fill in the knowledge gap from\
      \ a perspective of a self-taught developer like me, and infuse the habit of\
      \ questioning. We're getting bombarded with best practices, the newest greatest\
      \ framework every day, and I wanted to create a book that would give a clean\
      \ perspective on approaching those."
  - name: Alper Demirel
    text: Thank you very much for your detailed answer. I hope I read your book and
      benefit from your experience as a new developer.
- name: Alexey Grigorev
  text: 'There''s this saying (from Picasso I think) - "Learn the rules like a pro,
    so you can break them".

    Which software engineering rules, in your opinion, we should learn before we can
    break them? Do we need to know SOLID by heart before we can say "Okay I don''t
    care about O here, but I have to make sure D is there"?

    Which rules would fall into this category?'
  replies:
  - name: Sedat Kapanoglu
    text: 'I think many letters in SOLID are there just to make it look like a cool
      word. I''m not saying they don''t matter, but they don''t matter equally. If
      I had written my own SOLID, it would just be called "S", because I find "God
      class" problem the most prevalent and causing the most problems in a professional
      setting.

      I think new developers should incorporate the process of understanding the reasoning
      behind a rule before accepting it by heart, and make this a habit. That can
      be hard in a class setting because students can feel pressured to keep going
      at a certain tempo and you don''t want to anger other fellow students by insisting
      on these seemingly pedantic questions. But, you can make it a pastime to retroactively
      work on these concepts and find exactly why they are useful. I say, don''t internalize
      a rule before making sure it''s useful. Don''t start applying a rule before
      being convinced of its benefits.

      Embracing immutable data structures, or at least avoiding mutating state after
      creating a class can help you prevent a whole set of bugs from surfacing entirely.
      I go into details of that topic in the book.'
- name: Alexey Grigorev
  text: "I'm also curious how did you come up with the name? Did you come up with\
    \ it or the folks from Manning's marketing? \U0001F642"
  replies:
  - name: Sedat Kapanoglu
    text: "I'm a self-taught programmer, and I had to learn everything taught in software\
      \ engineering by myself, \"in the streets\" if you will. \U0001F642 I came up\
      \ with the name Street Coder as I see myself as one. You don't learn some of\
      \ these stuff at school, and you don't know value of some topics you learn at\
      \ school before you experience them in the streets first hand. For example,\
      \ the notion of algorithmic complexity can just be a boring lesson at the university,\
      \ but it's a mandatory tool to have on your toolbelt in a professional setting.\
      \ I explain Big-O notation and algorithmic complexity in the book in simple\
      \ and practical terms and show scenarios where such knowledge can make a significant\
      \ difference."
- name: Evren Unal
  text: "Sedat Kapanoglu   i think the name of the book suits the book very well.\
    \ \U0001F44D"
  replies: []
- name: Sedat Kapanoglu
  text: "Thanks! I'm glad to hear that \U0001F642"
  replies: []
- name: Neal Lathia
  text: "\u2754 what is the biggest dogmatic principle in coding that you\u2019ve\
    \ come across &amp; that you want the world to be rid of?"
  replies:
  - name: Sedat Kapanoglu
    text: 'That''s a great question Neal. I think I''d choose TDD as one of the top
      contenders. It impedes a rapid prototyping cycle (aka not fun and unrewarding),
      and it constrains you from making changes too early in the development. I love
      unit tests, but TDD is like converting such a fun activity like writing tests
      into a military drill.

      Inheritance as a code reusability model comes probably the second. Usually,
      any problem with inheritance can be solved with composition, and in return you
      get great decoupling. It''s usually easier to start with inheritance at the
      beginning in some languages, so I''m not completely against it, but I suggest
      anyone who''s getting slightly complicated class hierarchies to move onto composition.
      Languages like Rust and Go have better default reusability models based on traits/interfaces.'
  - name: Alexey Grigorev
    text: "I really like that you put TDD here as the number one thing. I sooo feel\
      \ the same way.\nI once tweeted about it and many people unfollowed me \U0001F605"
  - name: Neal Lathia
    text: "Thanks! Great answer. Am a big fan of Go too \U0001F642"
  - name: Anton Helm
    text: "I think I fully agree with Sedat Kapanoglu. However, I think TDD and inheritance\
      \ have their use-cases, and I think you should never use a principle purely.\
      \ I think you should try to understand the idea behind each principle and ask\
      \ yourself if it applies to my use-case or my project. (Same applies for programming\
      \ languages but not for editors - VIM always wins!!! \U0001F642 ). I would say\
      \ if someone applies a coding principle dogmatically, they should remove it.\
      \ But automatic and repeatable tests in the codebase are required. Moreover,\
      \ the code should be formatted consistently and have \u201Csome guidelines.\u201D"
- name: Heeren Sharma
  text: "Sedat Kapanoglu Thank you for providing such elaborate answers. I wanted\
    \ to ask your POV or argument that I often hear for \u201CStreet Coders\u201D\
    \ that they can\u2019t thrive in larger codebases as they don\u2019t embrace certain\
    \ concepts fully but some parts here and some parts there. I remember a personal\
    \ experience, 7-8 years back, I interviewed for a company and interviewer asked\
    \ me if I do TDD. And my answer was something similar as explained in your \u201C\
    dogmatic principle\u201D answer. And at the end, I didn\u2019t get the job and\
    \ interviewers really defended the fort by saying that without this, one will\
    \ not go far in professional setting. Since then, I have seen two world of software\
    \ developers. First is quite strict on coding principles while others is go with\
    \ the problem statement, come up with working elegant solution without caring\
    \ too much about strictness of certain practices (e.g. taking S from SOLID). But\
    \ later one if I may say are also referred as \u201CCode Hustlers\u201D \U0001F604\
    \ and I have an inherent feeling that they are looked down upon. I am interested\
    \ if you had similar experiences and How did you answer that \u201CLearning like\
    \ a Street Coder is equally if not less powerful approach\u201D?"
  replies:
  - name: Sedat Kapanoglu
    text: 'Hi Heeren! Cargo cult is a real thing and I think it was a fortunate outcome
      that you weren''t hired. You wouldn''t be happy there. It''s also possible that
      the company was using strict workflows in software development that a spec would
      be set in stone first and the code would be written later. In that case, TDD
      can be a beneficial practice, similar to how PostgreSQL team writes documentation
      for a feature first, and develops the feature after. But generally, such strict
      development processes are never fully applied, and design is usually subject
      to change even during the development process. TDD even contradicts Agile principle
      of embracing evolving requirements in that aspect.

      It''s natural that companies would want to hire people fitting to their own
      culture. I''ve also known my share of people who''d look down upon certain stereotypes,
      be it a "code hustlers", "college dropouts", "youngsters", or even "new graduates".
      Such people actually put themselves at a disadvantage by depriving themselves
      of great talent. Microsoft hired me as a software engineer to Windows team as
      a high school graduate because they optimized their hiring process to vacuum
      as many talents as possible regardless of stereotypes. I think the sector will
      eventually evolve to a point that hiring practices would be optimized to identify
      talent objectively. Anything else would be inefficient.'
  - name: Heeren Sharma
    text: Thank you so much for your answers.
- name: "Mert Bozk\u0131r"
  text: "Welcome Sedat Kapanoglu, I am really happy to see you in here. \nHere is\
    \ my question:\nI am freshman student in university and I am trying to improve\
    \ myself in Machine Learning Engineer or Data Science areas (don't focus title).\
    \ I was following courses in platforms such as Coursera, edx, cognitiveclass.\
    \ But I realized that if I follow the courses I am stuck with theoretical concepts\
    \ and I was assumed if I want to learn C, I need to learn A and B too. \nThis\
    \ is difficult situation and everything coming to your face. My question is how\
    \ I need to change my learning style. I know theory is  so important but I require\
    \ focus practice, doing something even basic concepts. \nWhat is your suggestions\
    \ to Freshman or Sophomore students to practice ? How we approach this working\
    \ style as students?(Your style \U0001F609)"
  replies:
  - name: Sedat Kapanoglu
    text: "Hi Mert! Great question. If we were in the early 2000's I would say \"\
      hey why don't you develop a new project?\". I can't say that now because the\
      \ list of requirements to bring a software project to life can get really long\
      \ (frontend, backend, multiple platforms, multiple programming languages, frameworks,\
      \ libraries) .\nInstead, I can recommend contributing to open source projects.\
      \ Project owners have already handled the hard part of creating it. You just\
      \ need to read the code, understand it, and write small bugfixes, tests, and\
      \ even features to it. Not only would this count as a practice, you can also\
      \ expand your social network with new developers this way.  Developing good\
      \ relationships is very critical in the streets, and doing that early would\
      \ be the second bird you'd hit with that one stone. \U0001F642 You can proudly\
      \ list the open source projects you've contributed to in your resume too.\n\
      You can also practice your coding skills with sites like Leetcode, Project Euler,\
      \ Codekata, and those would prepare you for interviews too as the problems asked\
      \ would be similar, but it wouldn't be as fulfilling as contributing to a real\
      \ project."
- name: ankush khanna
  text: "Hi Sedat Kapanoglu, love your comment on TDD and honestly I would have benefited\
    \ a lot from such a perspective early in my career (100s of hour wasted in fixing\
    \ TDDs).\nWhat are your thoughts around tech debt? When is the right time to tackle\
    \ it and how can we as developers take actions on it, rather than waiting for\
    \ the PM or PO to prioritise it?\n(Considering the tech debt is huge and cannot\
    \ be sneaked into a improvement ticket \U0001F642 )"
  replies:
  - name: Sedat Kapanoglu
    text: 'Hi Ankush! There is a section in the book titled "Leave no debt behind".
      What I argue in the book is that the constantly changing code is more adaptable
      to change than untouched code for a long time. That sounds unintuitive because
      any code change is a source of potential regressions. But, I find benefits of
      activities like refactoring, dependency upgrades, small code improvements, paying
      technical debts overwhelm the risks in most projects, especially at the initial
      stages of a project. You will experience breaks, but those breaks will teach
      you where your code is weak, and you''ll strengthen that part. The code will
      remain malleable, easily modifiable. Otherwise it turns into "`// DON''T TOUCH
      - NOBODY KNOWS HOW THIS WORKS`". Dealing with such changes keeps you involved
      with the code, your knowledge stays up to date. And, I even claim in the book
      that after making all those changes, you can throw the new code you just wrote
      in the trash if you find it too significant or too risky. You get to retain
      the value of practice, experience, and even motivation. It heightens the sense
      of code ownership in team members too.

      I think addressing tech debt should be a day to day practice like formatting
      code, as long as it''s aligned with business goals. I also talk about techniques
      to how to make it part of your daily work in the book.'
  - name: ankush khanna
    text: "Thank you for the great explanation, I believe I never looked at it that\
      \ way, although following it on many micro-services. Definitely helpful \U0001F642"
- name: Eric Sims
  text: 'Sedat Kapanoglu - Your book is very engaging! I love your intro and story
    about doing your project in Pascal.

    Figure 3.8 caught my eye because I am constantly battling with high quality variable
    and function naming. Your rule of thumb about avoiding needing to use "and" or
    "or" is great!'
  replies: []
- name: Eric Sims
  text: "Okay, I'm back. Chapter 3.9 \"Don't write code comments\" is so helpful!\
    \ I am definitely guilty of obvious commenting. `df = pd.read_csv()  # read CSV`\
    \ \U0001F605  Also, the comparison between Listing 3.18 and 3.19 is so helpful\
    \ for seeing how to pull small bits of code into functions.\nWhich brings me to\
    \ a question...\nI have a project I am working on right now that is essentially\
    \ one giant function. The client is not super technical, so the function basically\
    \ uses loops and returns a single final output. I am worried that if I put things\
    \ into functions it will make the code harder for them to read/troubleshoot. Do\
    \ you think it is better to leave the code in a more \"linear\" format for legibility,\
    \ or is there something I am missing that would make it more legible by putting\
    \ things into smaller functions?"
  replies:
  - name: mucio
    text: 'What I got from a senior colleague years ago was: a function should do
      a single thing. Keep the function shorts and with meaningful names (so people
      will remember what that function does - no need to check again and again what
      it does).

      I prefer to keep thing simple and use the power of the language.

      For example if you want to log before and after every method you call (I saw
      that recently), use a decorator for that :)'
  - name: Sedat Kapanoglu
    text: "Hi Eric! I'm so glad to hear that you liked the book! About your question,\
      \ I think you're already on the right track to address the problem. If you think\
      \ what you end up with is less readable, then you shouldn't be doing it. It\
      \ might be the case where you are extracting too much logic from the function\
      \ into other functions that the function itself fails to convey what it's doing.\
      \ Try to focus on extracting details irrelevant at the function's scope.\nFor\
      \ example, a function like `computeCsvAverage(filename, column)` could be opening\
      \ a CSV file, parse its contents and compute average on a given column based\
      \ on the parsed contents and return the result. since the main promise of this\
      \ function seems to be \"computing average\", the CSV parts can be abstracted\
      \ away and the function can look like this:\n```float computeAverage(string\
      \ filename, string columnName) {\n  var csv = readCsv(filename);\n  var numbers\
      \ = parseColumn(csv, columnName);\n  return numbers.Average();\n}```\nThis tells\
      \ what the function does without hiding any logic at the scope of the function\
      \ itself. Bringing in any of the logic in one of those functions doesn't help\
      \ explaining what the function does. It might even hurt readability as it clutters\
      \ the function body. If you follow a similar principle, readability shouldn't\
      \ be hurt.\n(By the way, you can compute while reading the CSV without needing\
      \ to read everything in memory beforehand, but this one was just for the sake\
      \ of the example :))\nThat was a great question! I'll consider adding a note\
      \ about this detail in the book."
  - name: Eric Sims
    text: 'Thanks for the helpful and detailed response! I''ll definitely take a look
      at my "giganto-function" and see where I can create useful functions without
      obscuring logic. I originally wrote the code in chunks in a notebook, so it''s
      fairly modular, but then I stuck it all together so I could have it in a single
      script file for deploying in a web app.

      I am still learning how to properly use global and local scope, so this should
      be a good learning experience!'
- name: Alexey Grigorev
  text: 'Hi Sedat Kapanoglu!

    I''m a fan of the "make it work, make it right, make it fast" approach - do a
    quick-and-dirty PoC, prove value and then iterate. However, I often get a lot
    of resistance from people who want to get it right from the start.

    What do you think about it? If you also agree with this approach, how would you
    convince others that it''s okay to cut corners sometimes?'
  replies:
  - name: Sedat Kapanoglu
    text: "Silicon Valley was built upon that principle. \U0001F642 I still think\
      \ having even the barebones of a design or a roadmap helps a lot in setting\
      \ the course for the development team. Some key technical decisions can be important\
      \ for the initial launch too. But, I agree that pedantry should be left to post-launch.\n\
      My greatest example for that (after Facebook having been written in PHP) is\
      \ Eksi Sozluk, which is now one of the most popular Turkish web sites in the\
      \ world. I created Eksi back in 1999 over the course of three hours without\
      \ knowing anything about web development. I even used a single plain text file\
      \ as a database, probably the worst possible choice, just to get the product\
      \ up and running as soon as possible. Today, it runs on a small server farm\
      \ with multiple web, cache, load balancer and DB servers, handling almost 40\
      \ million unique visitors per month. Remnants of the original code can be seen\
      \ here: [https://github.com/ssg/sozluk-cgi](https://github.com/ssg/sozluk-cgi)\n\
      Having a tangible, working product at hand that you can later shape like clay\
      \ today can be more productive than working on a fictional idea with no results\
      \ for weeks or even months. It affects developer psychology positively; it sets\
      \ the tempo for rapid iteration, and user feedback starts flowing immediately.\
      \ Good user feedback can easily be the most critical asset of a successful project.\n\
      Besides, you'll encounter cases in the streets where you'll need a product in\
      \ such a short timeline that you don't even have time for any planning or elegant\
      \ design and you just have to get something up and running. It's at least good\
      \ to get yourself acquainted in the practice.\nThat said, remember that the\
      \ idea of code is way easier to refactor than the code itself."
  - name: Alexey Grigorev
    text: "Well said, thank you!\nWhat about the cases when you can a POC, it works,\
      \ but inside it's ugly and super not optimal. But management is excited and\
      \ wants to start adding more features instead of \"making it right\"? \nHow\
      \ would you handle their expectations?"
  - name: silverstone
    text: "it's really nice to see ssg in a data driven community. who knows maybe\
      \ one day we can find an official api for eksisozluk  \U0001F92D"
  - name: Alexey Grigorev
    text: I'm checking the source code - wow, it's been a while since I saw Delphi
      code!
  - name: Ricky McMaster
    text: '```I even used a single plain text file as a database, probably the worst
      possible choice, just to get the product up and running as soon as possible.
      Today, it runs on a small server farm with multiple web, cache, load balancer
      and DB servers```

      Hi Sedat Kapanoglu - I''m really interested in this particular topic, and the
      evolution of standards in a company as it matures regarding data.  A problem
      I come across again and again is where start-ups initially operate on the ''move
      fast and break things'' mentality, and backend developers hurriedly throw together
      a database without worrying too much about data governance and maintenance.  Technical/data
      debt accrues, and fast forward 5-10 years later to the point where it is difficult
      to confirm basic, strategic information e.g. historical product pricing information
      (I could mention many other examples).

      I am not talking so much here about granular customer event-based data that
      a company _receives_, but rather how it organises and structures its _own_ product/operational
      standards (like pricing, product descriptions and taxonomies, campaign naming
      conventions etc.), particularly when this requires input and maintenance from
      business stakeholders in marketing, sales and finance, to name but three.

      Do you have any words of advice here?  Would you say there is still plenty of
      value in an ERP system, or do you see promise in a fresher approach such as
      the so-called postmodern ERP?  Or do you favour in-house solutions?'
  - name: Sedat Kapanoglu
    text: "Alexey Grigorev That's a good question. First, even when writing your dirtiest\
      \ code, never write code that you can't bear to get stuck with. \U0001F642 Second,\
      \ it's usually hard to argue about fictional future costs to management, so\
      \ usually, you can't really bargain about this with them. But, you can improve\
      \ code quality over the course of development with small steps of refactors.\
      \ As I explain it in the book, there are multiple benefits of improving the\
      \ code continuously. You don't usually need to write everything from scratch.\
      \ Sometimes, a minor change can improve the quality of life in orders of magnitude."
  - name: Sedat Kapanoglu
    text: Ricky McMaster I haven't had the chance to work on ERP systems, but you're
      right in the sense that technical debt eventually becomes business debt. It
      can reach to a certain point where it cannot be ignored, and it actively hurts
      business. With a data sensitive area like ERP, it must be doubly so. Eksi Sozluk
      today suffers from technical decisions from two decades ago like using VARCHAR
      for text fields, which doesn't allow features like emojis or other Unicode characters
      today, and switching to a new charset can be very expensive, it would at least
      require a long downtime for the upgrades and would increase the demand for storage
      and I/O. But, I'd say that any technical debt that can survive for at least
      a decade is a good tradeoff decision. I can't really comment on which ERP solution
      would be ideal though as I'm a stranger to the subject.
  - name: Ricky McMaster
    text: Thanks a lot for your response Sedat Kapanoglu
- name: Alexey Grigorev
  text: Which chapter are you working on right now? What's the main idea of this chapter?
  replies:
  - name: Sedat Kapanoglu
    text: "I'm currently working on the chapter about scalability, which is the penultimate\
      \ chapter of the book. I'll be clarifying how scalability differs from performance,\
      \ and how we can be way more productive with monolith architectures than microservices.\
      \ I'll also be expanding upon asynchronous I/O concepts that can be instrumental\
      \ in scalability scenarios, which were introduced in the previous chapter about\
      \ optimization.\nI'm really excited to be getting close to the end of the book,\
      \ but I still have too many notes from the feedback from readers. I really love\
      \ Manning's MEAP process for that; it's the rapid iteration cycle for books.\
      \ The book will be v1.6 or so when it's done. \U0001F642"
  - name: Alexey Grigorev
    text: Hehe, prototyping and iterating =) yes, MEAP is great!
  - name: Alexey Grigorev
    text: In your opinion, what are the most important  concepts in scalability?
  - name: Alexey Grigorev
    text: Is it architecture, autoscaling, possibility to work on codebase by multiple
      people? What else could be there?
  - name: Sedat Kapanoglu
    text: I think the dependency graph of a project is the most important aspect in
      scalability, be it the code itself or even in the database. For example, foreign
      keys are great for ensuring data integrity, yet they can be obstacles when you
      try to split up the database in multiple shards. They can even become performance
      bottlenecks. I'll be focusing on "poor man's scalability" in the chapter that
      will let you get as much scalability from your code on a single piece of hardware.
      That can be thought of as a performance-oriented chapter but there are ways
      to make code more scalable without improving the performance too.
  - name: Alexey Grigorev
    text: Clear, thank you!
- name: Alexey Grigorev
  text: '&gt; Street coders get the job done by prioritizing tasks, making quick decisions,
    and knowing which rules to break.

    We already talked about which rules to break - but what about task prioritization
    and making quick decisions? If you were to give tweet-sized advice about each
    of these topics, what that would be?'
  replies:
  - name: Sedat Kapanoglu
    text: 'I use two distinct concepts for prioritization: priority and severity.
      Priority is the business-related urgency of the matter while severity is the
      level of technical screw-up, aka developer''s urgency to fix it. A web page
      crashing can be very severe in the eyes of the developer, but if it''s a page
      that only 0.1% of users visit, it may not get a higher priority. Similarly,
      using wrong logo on the homepage isn''t technically severe at all, and the developer
      may not care much, yet it can have the highest priority due to business goals.
      So, sort your tasks on priority first, severity second.

      About making quick decisions: Knowledge can be a curse in the decision-making
      process because you know all the possibilities of how something can go wrong,
      and that can cause disproportional delays. Budgetize your decision-making process
      itself and go with the best option at the end of your time budget. If you''re
      still undecided at the end of your time budget, you might as well roll a dice,
      because none of the options have stood out enough for you to have a decision
      anyway.'
  - name: Alexey Grigorev
    text: How do we determine the priority? By talking to the stakeholders? Or maybe
      there's a way to develop this "sense of priority" in ourselves?

---

Software development isn't an "ivory tower" exercise. Street coders get the job done by
prioritizing tasks, making quick decisions, and knowing which rules to break.

Street Coder: Rules to break and how to break them is a programmer's survival guide,
full of tips, tricks, and hacks that will make you a more efficient programmer. This book's
rebel mindset challenges status quo thinking and exposes the important skills you need on the
job. You'll learn the crucial importance of algorithms and data structures, turn programming
chores into programming pleasures, and shatter dogmatic principles keeping you from your full potential.