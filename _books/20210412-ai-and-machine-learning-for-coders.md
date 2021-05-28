---
title: "AI and Machine Learning for Coders"
description: "Book of the Week. AI and Machine Learning for Coders by Laurence Moroney"
cover: "images/books/20210412-ai-and-machine-learning-for-coders/cover.jpg"
image: "images/books/20210412-ai-and-machine-learning-for-coders/preview.jpg"
start: 2021-04-12 00:00:00
end: 2021-04-16 22:59:58
authors: [laurencemoroney]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/ai-and-machine/9781492078180/

archive:
- name: Krzysztof Ograbek
  text: Laurence Moroney Is this a book for all coders, regardless of their years
    of experience or programming languages they use?
  replies: []
- name: Darya Petrashka
  text: 'Hi, Laurence Moroney thanks a lot for this wonderful opportunity! My question
    is: after studying properly the NLP section would it be possible to create a meaning-extract
    NLP algorithm that accepts a natural language phrase like "Show me sales by the
    company N" and ''translates'' it to a query for the database?'
  replies: []
- name: Matthew Emerick
  text: 'Hey, Laurence Moroney!  Thanks for doing this.

    Question: how much math do you go into in your book?  How much math do you expect
    your audience to know before reading it?'
  replies: []
- name: Matthew Emerick
  text: How much theory do you cover in your book?
  replies: []
- name: Matthew Emerick
  text: What resources do you recommend after reading your book to go deeper into
    AI and ML?
  replies: []
- name: Matthew Emerick
  text: Are there any supplemental books you recommend that go well with your writings?
  replies: []
- name: David Cox
  text: "Laurence Moroney Looks like a fun read! In particular, I\u2019d be curious\
    \ to hear more about how/why you chose the deployment options you did later in\
    \ the book?"
  replies: []
- name: Laurence Moroney
  text: Krzysztof Ograbek -- The first half of the book is about learning how to train
    models, and it will require you to know a bit of python. Not expert-level by any
    means, but it would be helpful. The second half of the book deals with deploying
    models to Android (Kotlin), iOS (Swift) and the browser (JavaScript), so will
    need you to understand a little of them.
  replies: []
- name: Laurence Moroney
  text: Darya Petrashka -- The NLP section is primarily focussed on the underlying
    basics of NLP, leading to two outcomes -- classifying text for sentiment, and
    generating new text, so not NLP-&gt;SQL type querying, sorry. I think there are
    a number of *products* that can do that, but I teach generally the underlying
    principles in ML
  replies: []
- name: Laurence Moroney
  text: 'Matthew Emerick -- Almost no math! The point of the book is so that the usual
    math/calculus barrier that prevents people from learning ML is removed.

    How much theory? -- Only enough to help you get to the point of being able to
    code. For example, I''ll teach (lightly) what a convolutional filter is, but from
    a code perspective (i.e. multiply these values by these) and not a math perspective
    (no greek letters!)

    Resources to go deeper: Aurelien Geron''s book and/or Andrew Ng''s Coursera courses

    Supplemental books: Anything that will help you with the language parts (basic
    Python, basic Android/Kotlin, basic iOS/Swift etc)'
  replies: []
- name: Laurence Moroney
  text: David Cox -- Deployment is what generally differentiates TF from other ML
    frameworks. It's ecosystem allows you to deploy optimized ML to servers (via TF-Serving),
    iOS/Android (via TF-Lite), Browser/Node (via TF.js) and microcontrollers (via
    TF-Lite Micro). The goal was to give the developer a broad understanding and a
    grounding in what they need to know to get their models deployed to these runtimes.
  replies: []
- name: Laurence Moroney
  text: David Cox -- I ended up not being able to put TF-Lite Micro into the book
    for microcontrollers, as that would have required many chapters to cover properly,
    and Pete Warden / Daniel Situnayake's book covers that brilliantly
  replies: []
- name: David Cox
  text: Got it! This was very helpful. The know-how to deploy ML models is often a
    critical skill I see many data science students lacking when they join our team.
    Excited to see you talking about that in this book and to check out your implementation!
  replies: []
- name: "Laura Uzc\xE1tegui"
  text: "Welcome Laurence Moroney, \U0001F44B"
  replies: []
- name: Lamjed Debbich
  text: Laurence Moroney, thank you for presenting your book. I wonder what is the
    specificity of this book compared to the number of books currently on the market,
    and is it intended for people with previous data science practice or new learner?
    Thank you for clarification.
  replies: []
- name: Laurence Moroney
  text: Lamjed Debbich -- Hi! The goal of this book was primarily to bring ML into
    the hands of the traditional software developer. As such half of it is an introduction
    to building common types of models for general, vision, nlp and sequence, and
    the other half is in getting those models into people's hands with different deployment
    technologies. So, someone who previously has data science might find it useful.
  replies: []
- name: Laurence Moroney
  text: I think it's really useful for new learners -- as it assumes no prior knowledge,
    particularly of data science.
  replies: []
- name: Amr Alaa
  text: 'Hey Laurence Moroney

    Thanks for your time with us here

    First question is about the title itself

    "coders"

    What do you mean by coders exactly?

    How is it differ than developers?'
  replies: []
- name: Rohan
  text: "Hello Laurence Moroney, \nI had a question about fit_generator method in\
    \ Tensorflow. What does steps_per_epoch argument do?  \nI have tried to look about\
    \ it online but couldn't understand them. \nAnd secondly, are we only supposed\
    \ to ask questions about the book ?"
  replies: []
- name: Laurence Moroney
  text: "Amr Alaa -- Haha , good question! I don't think there's a deeper meaning\
    \ in it, other than I know many people who are dabbling in code, but don't have\
    \ a job title calling them a 'developer' yet, so I wanted to focus on the book\
    \ being for people who code, as opposed to somebody with a particular job title\
    \ \U0001F642"
  replies: []
- name: Laurence Moroney
  text: Rohan - I'm not sure if that argument is fully used any more, I should check.
    But the idea behind it was to specify the number of steps to take in an epoch
    based on the data size and the batch size. So, for, example, if you have 60,000
    training records, and a batch size of 1,000, then you'd have 60 steps in each
    epoch to get through the whole data. AFAIK it's automatically counted now, (and
    fit_generator has been deprecated in favor of just fit)
  replies:
  - name: Rohan
    text: "Ah! Got it. \nThank you for the clarification. \U0001F604"
- name: Laurence Moroney
  text: "Rohan -- Feel free to AMA. I may not be able to answer *everything*, but\
    \ I'll try \U0001F642"
  replies:
  - name: Rohan
    text: "Thanks a lot! \U0001F604"
- name: Seed Badran
  text: Hi Laurence Moroney. Thank you for this great opportunity. I got certified
    as a *Tensorflow Developer* few months ago and I wonder where would you put your
    book (knowledge dependency) in comparison to your "Tensorflow Developer Professional
    Certificate" specialization on Coursera? Which one would you recommend going through
    first?
  replies: []
- name: Laurence Moroney
  text: Seed Badran -- They are complementary, and both the book and teh course were
    developed from the same material.
  replies:
  - name: Seed Badran
    text: Thanks. If the book is following the same great approach as in the Specialization
      (and expect it to be) I would definitely enjoy reading such book. Thanks for
      answering.
- name: Seed Badran
  text: I am always looking for resources where I can practice building an End-to-end
    Machine Learning project(s), does the book cover such scope?
  replies: []
- name: "Ca\xEDque Coelho"
  text: 'Laurence Moroney is an honor to have this conversation directly with you!
    My million-dollar question is: is this book a good way for those looking to get
    their first job as data science? What are the fundamental points to be learned
    in the book to help me search for my first job in data science? I am currently
    looking for a migration from the software testing area to data science'
  replies: []
- name: Bayram Kapti
  text: Laurence Moroney since you mentioned the book focuses on Android, IOS and
    web deployments for ML algorithms, does this mean only Client Side ML Deployment
    is included in your book vs Server Side ML?
  replies: []
- name: Laurence Moroney
  text: Seed Badran -- I guess it depends on the project, but in general, yes.
  replies: []
- name: Laurence Moroney
  text: "Ca\xEDque Coelho - It really depends on the requirements for the job. If\
    \ the job requires hands-on coding of models, as well as the usual data science\
    \ stuff, then I think this book would be useful, but in and of itself, it's probably\
    \ not enough. A survey of employers looking for ML Programmers had many wanting\
    \ people who knew Computer Vision and/or NLP, and this book digs into those."
  replies: []
- name: Laurence Moroney
  text: Bayram Kapti They're not really the "focus" of the book. The first half of
    the book is on building models. The second half is on deployments, including Android,
    iOS and Browser. It also has a chapter on how to use TF-Serving for server side
    models accessible via REST or GPRC
  replies: []
- name: Bayram Kapti
  text: "Got it! Thank you! \nA follow up question on deployment, what would be your\
    \ recommendation for a startup to try ML algorithms for the first time for some\
    \ optimization purposes? \nClient Side or Server Side? I think I\u2019m more interested\
    \ in the ease of deployment and maintainance for now."
  replies: []
- name: Laurence Moroney
  text: Bayram Kapti -- I think client side for sure, just because of the install
    base, and because it's easier to wrap an interface around a model in Android/iOS/JavaScript
    than dealing with the REST/GRPC interface.
  replies:
  - name: Bayram Kapti
    text: Amazing! thank you Laurence Moroney ! I think your book will be an amazing
      resource for me.
  - name: Laurence Moroney
    text: "\U0001F642 Thanks!"
- name: Gant
  text: "Hey hey Laurence Moroney!!!   You know I already have a copy of the book\
    \ \U0001F642   However, I'm interested in what was your favorite dataset from\
    \ the book, and why?"
  replies: []
- name: Laurence Moroney
  text: "Gant -- Hey hey! We'll have to have you do an AMA too! \U0001F642 I think\
    \ my favorite dataset, being completely biased, is my horse-or-human one. It's\
    \ a *really* tough one to build a good model from, but when it works it's really\
    \ cool. The images are all CGI, I synthesised them myself, and they greatly prove\
    \ the concept of feature detection in CNNs because the computer can use features\
    \ learned from a CGI image (like a horse's ear or a human hand) to classify real,\
    \ non-synthesised images!"
  replies: []
- name: Kenny
  text: Laurence Moroney For a developer who wants to get into machine learning and
    AI, what change in mindset is required to do well?  Is there a different fundamental
    approach to solving problems?  Thanks!
  replies: []
- name: Eric Sims
  text: "Laurence Moroney Your book looks very interesting! I'm particularly interested\
    \ in learning how to convert Python models to JavaScript. I want to get back to\
    \ JavaScript. I tried learning it a few years ago before I knew any other languages,\
    \ and it was just too over my head. I think I could handle it much better now.\n\
    The other thing I'm keen to understand is federated learning. How would you recommend\
    \ even starting with it? Could I use a couple of local devices to create a tiny\
    \ \"federation\" and experiment at my kitchen table? Or am I totally misunderstanding\
    \ what I have read on Wikipedia and elsewhere? \U0001F605"
  replies: []
- name: Laurence Moroney
  text: Kenny -- I think so -- It's as much about good data selection to train a model,
    as good code selection for definining one. It's definitely a new mindset, but
    IMHO, a good one!
  replies: []
- name: Laurence Moroney
  text: "Eric Sims Thanks! I do have a couple of chapters on TensorFlow.js in my book,\
    \ but all of Gant's book is about JS! \U0001F642 Right now TF-Federated is a bit\
    \ difficult to get started with as it is very experimental and doesn't yet have\
    \ a mobile runtime (you simulate the devices using Python)"
  replies: []
- name: Rohan
  text: "Hello again, Laurence Moroney \nWhile working with Natural Language Processing\
    \ problems with Tensorflow, I have been getting stuck at choosing the correct\
    \ model architecture for the project. \nI have used, \nBidirectional LSTM layer\
    \ ,\nOr  A GRU layer, \nOr a Convolution network,\nBut none of them have reached\
    \ a good accuracy. \nAm I missing out something? \nIn your perspective what model\
    \ architecture would you go with ?"
  replies: []
- name: Ricky McMaster
  text: 'Hi Laurence Moroney, thanks for doing this!

    I''m definitely in favour of making this subject more explicable to a wider audience
    - however, I wonder if you could comment on potential risks.  I work in data,
    and have often encountered legacy problems that originated from someone having
    insufficient understanding of creating/maintaining databases.  Do you think there
    are similar dangers with AI/ML, and if so do you have any advice on safeguards/preventative
    measures, other than (obviously) a strong organisational culture?'
  replies: []
- name: Amr Alaa
  text: "Laurence Moroney  I really liked your decision to make the book easy to be\
    \ read by coders from different backgrounds, including me I think \U0001F914\n\
    Here's my second question\nIn your book I see from the content table, i see that\
    \ there are 4 chapters for TensorFlow.js and 3 for TensorFlow lite\nWhich one\
    \ do you think will dominate the next phase of developing satisfying needs of\
    \ rapid development and growth?"
  replies: []
- name: Rohan
  text: "Laurence Moroney I wonder if the book covers contents from your course on\
    \ Coursera \" TensorFlow Advanced Techniques\". \U0001F914\nAnd does it also covers\
    \ topics such as TensorFlow serving?"
  replies: []
- name: Ramit Surana
  text: Laurence Moroney Does the book explore any ideas on building large scale NLP
    models like GPT3 using Tensorflow? What's your take on it? Is it possible for
    small scale companies/groups to build and serve models with billions of parameters
    by scraping the internet for data in future. Thanks.
  replies: []
- name: Chirag Aggarwal
  text: "Laurence Moroney I wonder if book covers the deployment of DL model over\
    \ a web based tool developed using tensorflow-python and tensorflow.js both. So\
    \ that someone can better understand stand how to use them in production environment\
    \ and when to use which one. \nThanks\nChirag"
  replies: []
- name: A McCauley
  text: "Hi Laurence Moroney  - what are your favourite types of projects to work\
    \ on with AI? E.g. such as working with images/ video etc . Which do you have\
    \ the most fun with or feel most passionate about? \U0001F60A"
  replies: []
- name: Laurence Moroney
  text: A McCauley -- I can't say I have a particular favorite data type with AI projects,
    to me I'm more excited about particular difficult projects to solve, like medical
    diagnosis (be it based on image or NLP), but recently I've been exploring more
    about how models come up with their decisions, with a view to turning the black
    box into a glass box, and stuff around images here is fascinating. For example,
    when doing a 'Class Activation Map' for the famous Cats v Dogs dataset, I found
    the main thing my model was making a decision on was the eyes. I had hundreds
    (maybe thousands) of feature extractor filters, but in the end, the eyes have
    it (sic!), and being able to show and prove that was awesome.
  replies: []
- name: Laurence Moroney
  text: Chirag Aggarwal - Yes. There's a chapter on TF-Serving with a basic scenario
    of putting a model on a server and using TF-Serving to wrap it in a REST/gRPC
    interface. There are several chapters on JavaScript, making models, using models,
    and transfer learning with models.
  replies: []
- name: Laurence Moroney
  text: "Ramit Surana -- No, I don't focus on large scale NLP models, more on the\
    \ fundamentals of how NLP works, using smaller datasets for classification. I\
    \ do a text generation algorithm though, trained on Traditional Irish songs, so\
    \ you can write your own! \U0001F642"
  replies: []
- name: Laurence Moroney
  text: Rohan -- It predates 'Advanced Techniqes', so it doesn't cover that. There
    is a chapter on TF-Serving though
  replies: []
- name: Laurence Moroney
  text: Amr Alaa The 3 on TFLite are -- 1 on the tech, 1 on an Android scenario, 1
    on an iOS scenario. For TFJS, I needed some extra time to discuss it, because
    we don't just do inference in JS, we also do training, and there are some special
    considerations you need to take into account when training in the browser. I think
    both can be huge for the future, but only time will tell.
  replies: []
- name: Laurence Moroney
  text: Ricky McMaster -- In some ways AI/ML doesn't really change the ethics of responsibility
    with data and/or with how the work we create is used. I think the fact that AI
    can lead to more powerful solutions has brought the conversation to the forefront,
    and that's a good thing, but issues with ethics, bias, responsibility etc have
    always been with us. Now's the time to double down on them and take them more
    seriously.
  replies:
  - name: Ricky McMaster
    text: Good to know.  That's kind of reassuring, in a way - the need for oversight,
      actively maintained by responsible management, is enduring.
- name: Laurence Moroney
  text: "Rohan -- For NLP layers, it really depends. I did find, however, that for\
    \ NLP solutions, good vocabulary management, good, clean, datasets etc had much\
    \ more of an impact on my final results than a neural architecture search for\
    \ the best layer types and hyperparameters. That's one of the things I discuss\
    \ in the book. \U0001F642"
  replies: []
- name: Rohan
  text: "Laurence Moroney I think that building a model and working with data is an\
    \ art. But data is present in different format and working with them can be very\
    \ daunting sometimes. Transforming the given data into an insightful information\
    \ is not everyones cup of tea. \nWhat would you suggest if a person has difficulties\
    \ working on a dataset?  \U0001F605\n(The person cannot leave this field. \U0001F602\
    )"
  replies: []
- name: Ricky McMaster
  text: Hi again Laurence Moroney, on the subject of text generation... the stuff
    I've read from GPT-3 is fun, and impressive in its own way, but do you foresee
    a point where it could be used in a genuinely creative context?  At least one
    use might be in literary works with elements of pastiche, but are there other
    contexts you can think of, or are aware of?
  replies: []
- name: Laurence Moroney
  text: Rohan -- I think as tooling evolves, where one can see how tuning input data
    affects output performance, that this part of the job will get a bit easier. Often
    there's a lot of burden now where you'll have a thesis that a particular format,
    slice, function, on data can impact a model positively, but then you still have
    to go through the process of building the model, adjusting the architecture to
    how the data is formatted, training, testing etc, before you can get any results
    to prove/disprove your thesis. As that process gets faster and easier, and then
    becomes automated and scriptable (think AutoML for data management too), then
    I think that part of the process will get much easier to do, and you can focus
    more on solutions and less on massaging data.
  replies: []
- name: Laurence Moroney
  text: Ricky McMaster -- I'll say 'never say never', but when you do text generation,
    or indeed any type of generation, it rapidly descends into gibberish, when you
    realize that it's a prediction on a prediction on a prediction on a prediction
    etc. That's a hard problem to solve for it to be really useful. Large scale models
    like the one you mention attempt to solve that by being trained on more data,
    but I think there's a ceiling to what's possible with that approach. That being
    said, I'm sure somebody will someday have a breakthrough that makes text (or any
    other type) generation more realistic.
  replies:
  - name: Ricky McMaster
    text: Thanks Laurence Moroney, that's interesting to hear.  Of course it's debatable
      whether it's worth the effort... in music production (so for example, mastering
      algorithms) I am definitely aware of creative or practical uses for AI, but
      with large-scale text generation, I guess the entire thrust of a narrative or
      argument could be upset by a single word.
  - name: Laurence Moroney
    text: Music is a great point...and there are often repeating rhythms in music
      so that a long piece of information is repeated sections of smaller pieces.
      Text is harder because that's not usually the case.
  - name: Ricky McMaster
    text: 'That''s exactly it!  Especially with electronic music, but even with more
      complex forms there are always repetitive elements, and whilst the creative
      uses might be more limited you can still train a model to take care of mastering.

      Whereas text (or more particularly literature) is an endless series of forking
      paths...'
- name: Rohan
  text: "Laurence Moroney often while training a model, we encounter a case of stalling.\
    \ The network stops learning at all. We do use early stopping technique to stop\
    \ the training but, what do you think the person should keep in mind while building\
    \ the model? \nWhat are your observations while tweaking those hyper- parameters\
    \ \U0001F913"
  replies: []
- name: Laurence Moroney
  text: Rohan -- Stalls can be a result of too small a learning rate, so maybe it's
    good to adjust that. Or, it could be because of sparse or too little data. Have
    you tried Keras Tuner to do a hyperparamter search?
  replies: []
- name: Krzysztof Ograbek
  text: Laurence Moroney you used Python to train models but other languages to deploy
    them. Why don't you use Python to deploy? Is it because of performance? Are there
    more reasons?
  replies: []
- name: Krzysztof Ograbek
  text: Laurence Moroney I'm just curious about your predictions, what's the next
    3-5 years will look like. Is there any language that may soon take over training
    models from Python? Is Python going anywhere or its position is strong enough?
  replies: []
- name: Laurence Moroney
  text: Krzysztof Ograbek -- Because of *where* they are deployed. For example. the
    primary languages to build Android apps are Java and Kotlin. Or for iOS it's Objective-C
    or Swift. Thus models, created with TF in Python need to be executed elsewhere,
    and we need to be able to interface with them.
  replies: []
- name: Laurence Moroney
  text: Krzysztof Ograbek -- I think Python will be the primary one, but keep an eye
    on languages like Go or Kotlin.
  replies:
  - name: Krzysztof Ograbek
    text: Thank you so much for answering my questions, Laurence Moroney. And thank
      you for doing this AMA. I never used any of those 2 languages
- name: Krzysztof Ograbek
  text: "Laurence Moroney I have a few more questions that are out of the scope of\
    \ your book. It would be awesome if you share your thoughts \U0001F609\nHow do\
    \ you explain to people that are completely non technical, what AI is?\nCan Software\
    \ Developer's job be automated by AI? Are Developers gonna be replaced with AI?\
    \ What are the skills that Developers should improve in order to future proof\
    \ their careers?"
  replies: []
- name: Rohan
  text: "Laurence Moroney hadn't heard about Keras Tuner. Will try it out!  The problem\
    \ which I often face is of Vanishing Gradient. I tried SGD with momentum to tackle\
    \ this. But that too didn't have much of an effect. \nThe second thing which I\
    \ wanted to know was, how do you decide the dimensions of a picture while feeding\
    \ it into the network, given that the dataset has pictures of different dimensions\
    \ which are very high!"
  replies: []
- name: Laurence Moroney
  text: "Krzysztof Ograbek -- I generally like to explain that AI is the result of\
    \ using programming techniques that have computers act on data the way the people\
    \ would. For example, Computer Vision, a person would look at a picture of a cat\
    \ and say it's a cat. When a computer can do the same, you have the beginnings\
    \ of AI. Are developers going to be replaced by AI -- absolutely not, in the same\
    \ way as developers weren't replaced by compilers, IDEs, intellisense, emulators\
    \ etc. \U0001F642 Skills that they should improve on: ML, Data Science, Python\
    \ etc."
  replies:
  - name: Krzysztof Ograbek
    text: Just a quick follow up question here, Laurence Moroney. By improving ML
      here, do you mean learn also math behind it or simply learn how to train models?
  - name: Laurence Moroney
    text: Ideally both, but if you're a developer, it's best to start with the code.
- name: Laurence Moroney
  text: "Rohan -- Definitely give it a try. KT might be able to help find a model\
    \ that doesn't have VG. For deciding dimensions of a picture, there's a lot of\
    \ trial and error of training time against accuracy...or, I'd do something like\
    \ a Class Activation Model to determine what the features are that determine classificaiton\
    \ of the image. For example, with the classic Cats v Dogs model, a good classifier,\
    \ when passed through a CAM ended up showing me that the eyes were the single\
    \ most important feature to distinguish...and if that was the case, maybe the\
    \ eyes could have sufficient fidelity in tiny images so as not to make a difference,\
    \ so why train on larger ones? \U0001F642"
  replies: []
- name: Laurence Moroney
  text: "By the way, small factoid for everybody reading -- one of the best things\
    \ you can do for any book, to support it, is to give a review on amazon. A star\
    \ rating is good, but a review is best. I've had books where sales were boosted\
    \ even after a poor review! There's clearly something in their ranking/recommendation\
    \ engine that values written reviews. So, while I'm not asking for you to review\
    \ mine (although I would love it), I would ask you to remember this to support\
    \ authors. Margins on books are razor thin, and many writers simply give up because\
    \ it's not financially worth it -- I've observed an almost inverse Moore's law,\
    \ where royalties halve every 18 months. I didn't write this book for profit (all\
    \ proceeds go to charity per Google employment agreement), but there are authors\
    \ out there who need the income, so please remember this for any books you buy\
    \ and/or read! Thanks \U0001F642"
  replies: []
- name: Krzysztof Ograbek
  text: Laurence Moroney When doing an ML Project, how do you know, which algorithm
    to use? What are the factors? Is Deep Learning always a better choice than the
    traditional ML algorithms?
  replies: []
- name: Laurence Moroney
  text: Krzysztof Ograbek -- Not always...it really depends on the problem. Things
    like CNNs for images (mostly), LSTM/RNN/GRU for text etc. Generally, I would need
    to see what the problem I'm trying to solve is, and explore solutions for similar
    ones to use as a starting point.
  replies: []
- name: Saurav Maheshkar
  text: "Laurence Moroney it\u2019s amazing to have the opportunity to talk to you.\
    \ I have taken all of your courses with [deeplearning.ai](http://deeplearning.ai)\
    \ and I love the way you taught and broke down the API into small chunks.\nMy\
    \ question is: What according to you is the ideal \u201C*Full-Stack*\u201D pipeline\
    \ for building deep learning models ? How do we incorporate methodologies like\
    \ _CI/CD_, _Testing_ and _Deployment_ with the Tensorflow Ecosystem. Does Post-Training\
    \ Optimization methods such as _Pruning_ and _Quantisation_ come under \u201C\
    *Full-Stack*\u201D and what according to you is the future of the `tfmot` package\
    \ ?"
  replies: []
- name: Rohan
  text: "Laurence Moroney I have asked several technical questions. But I was curious\
    \ about journey in this field of AI. What excites you the most? \nYou are an inspiration\
    \ to students like us. Any suggestions you can provide to people starting their\
    \ career in the vast universe of AI. \nThank you. \U0001F604"
  replies: []
- name: Krzysztof Ograbek
  text: Laurence Moroney thanks again for this amazing opportunity. I didn't know
    you don't get any profit for your book. This leaves me speechless
  replies: []
- name: Laurence Moroney
  text: 'Rohan -- My inspiration. I guess there''s a number of places. First -- I
    graduated college in 1991, in the UK, in the middle of the biggest economic recession
    since WW2, and matched only by the current one, I think. I was unemployed, and
    it was really hard to find work. I spent some time as a clerk for London Underground
    (and got laid off on Christmas Eve, very Dickensian), and doing odd-jobs here
    and there. I remember working in a recycling plant, being the guy that collects
    the tin cans that people come in off the street to hand us, expecting payment,
    weighing them, and seeing people''s disappointment at the few pennies they got.
    Then, the UK government started a scheme where they wanted to find 20 people,
    who are currently unemployed, to train them in AI to be a cohort of future consultants
    in industry. It was 1992 at this point, and I had been out of work for about a
    year, and really struggling. I went to the testing center, along with thousands
    of others, and was the first person selected to enter the program, with the highest
    scores. It was a massive boost to my flagging confidence! Unfortunately the program
    failed miserably after about 3 months, but the contract I had signed had entitled
    me to 2 years of education, so it got parlayed into a Masters degree, fully paid,
    which I graduated from in 1993, as the economy was emerging, and my career got
    on track. Then...Fast forward to 2017, I''m now at Google, and we had an initiative
    to train all engineers in ML and AI. I remember sitting in a conference room in
    Kirkland (near Seattle), with a few hundred other folks, excited as anything....and....after
    3 hours of calculus, and most of the room bored out of their minds, I realized
    something was wrong with how we teach ML as an industry. I approached the TF team
    showing how a code-first approach would work better, and how the material is aimed
    at the 300K current AI practitioners globally (measured by academic publications)
    instead of the 30M+ software developers.

    So they hired me, and asked me to fix it.

    And here I am :)'
  replies:
  - name: Rohan
    text: "Wow! \nIt's amazing. A true example of never giving up no matter what!\
      \ \U0001F603"
  - name: Seed Badran
    text: "I can relate to this. It helps to know (for real) how others overcome their\
      \ life challenges... Thanks for sharing \U0001F64F"
- name: Laurence Moroney
  text: "Saurav Maheshkar -- Thanks! \U0001F642 As for 'Full Stack' -- I don't think\
    \ it's well defined yet, but I will take a stab at definining it similarly to\
    \ how we define full stack web developers -- and that is someone who is involved,\
    \ at least in part, in every part of the overall stack to solve a problem. A full\
    \ stack web developer, for example, is involved in coding the part of the solution\
    \ that lives on the server, but they're not necessarily an expert in infosec.\
    \ They'll interface with the people who are. They'll also be involved in coding\
    \ the front end, and the UX, but they're not necessarily a designer or a UXE.\
    \ So, similarly, when it comes to ML, if you explore the life cycle from data-&gt;feature\
    \ engineering-&gt;model training-&gt;deployment-&gt;management, I think a full\
    \ stack ML Engineer will be involved in all of them to some extent, but the closer\
    \ you get to the center of that chart, the more they do."
  replies: []

---

If you’re looking to make a career move from programmer to AI specialist, this is the ideal place
to start. Based on Laurence Moroney's extremely successful AI courses, this introductory book provides
a hands-on, code-first approach to help you build confidence while you learn key topics.

You’ll understand how to implement the most common scenarios in machine learning, such as computer
vision, natural language processing (NLP), and sequence modeling for web, mobile, cloud, and embedded
runtimes. Most books on machine learning begin with a daunting amount of advanced math. This guide
is built on practical lessons that let you work directly with the code.