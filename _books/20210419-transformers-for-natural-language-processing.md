---
title: "Transformers for Natural Language Processing"
description: "Book of the Week. Transformers for Natural Language Processing by Denis Rothman"
cover: "images/books/20210419-transformers-for-natural-language-processing/cover.jpg"
image: "images/books/20210419-transformers-for-natural-language-processing/preview.jpg"
start: 2021-04-19 00:00:00
end: 2021-04-23 22:59:58
authors: [denisrothman]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/transformers-for-natural-language-processing/9781800565791
  - text: Amazon
    link: https://www.amazon.com/Transformers-Natural-Language-Processing-architectures-ebook/dp/B08S977X8K

archive:
- name: Krzysztof Ograbek
  text: 'Denis Rothman thank you for doing this!! Maybe I''ll start with this question:
    Do transformers outperform RNNs in any kind of NLP tasks? What makes transformers
    so great?'
  replies: []
- name: Rodney Silva
  text: Denis Rothman Hi! How should a beginner implement Transformers? Using Hugging
    Face,Google Trax,MS Azure or implement from scratch to control maintenance?
  replies: []
- name: "Mert Bozk\u0131r"
  text: Denis Rothman What do you think about  future of Natural Language Processing?
    What will the location of the Transformers in future ?
  replies: []
- name: Lalit Pagaria
  text: Denis Rothman Isn't Transformers constraints by compute resources? What is
    way forward for startups with less resources?
  replies: []
- name: Vladimir Finkelshtein
  text: When do you think we will see transformers for non-NLP tasks? There seem to
    be papers and attempts with transformers for vision, but no breakthrough, or at
    least no mainstream adoption of it.
  replies: []
- name: Denis Rothman
  text: I'm live so you can ask any question you wish.
  replies: []
- name: Denis Rothman
  text: 'Krzysztof Ograbek There are to reasons transformers outperform RNNs:'
  replies: []
- name: Denis Rothman
  text: "Krzysztof Ograbek I mean there are \"two\" \U0001F642 main reasons: 1.optimal\
    \ transport= RNNs carry all of the information from word(or token) to word and\
    \ pile the information up in a big backback. 2/ The architecture of RNNs is obsolete\
    \ with variable sized layers. Transformers have fixed sized industrialized layers.\
    \ I explain this in chapter 1 of my book but also in this video:"
  replies: []
- name: Denis Rothman
  text: Krzysztof Ograbek This is the link to the video [https://youtu.be/tQTpCvZ1-0w](https://youtu.be/tQTpCvZ1-0w)
  replies: []
- name: Denis Rothman
  text: 'Krzysztof Ograbek Proof? Transformers have wiped RNNs off the top ranks of
    the SuperGlue Leaderboard:'
  replies: []
- name: Denis Rothman
  text: Krzysztof Ograbek Here is the link to SuperGlue:[https://super.gluebenchmark.com/leaderboard/](https://super.gluebenchmark.com/leaderboard/)
  replies: []
- name: Denis Rothman
  text: Rodney Silva A beginner should begin by understanding the original Transfomer
    model explained in Chapter 1 of my book. Even with a piece of paper and a pencil!
    Or a spreadsheet!
  replies: []
- name: Denis Rothman
  text: Rodney Silva Implementing in a real-life project is something else entirely.
    If it's a low level non-strategic project and isn't really necessary and the project
    has only a small budget because of that, you can implement almost anything you
    find since the interest of the solution will be limited! Now if you are implementing
    Transformers in a critical project, that's something else...
  replies: []
- name: Denis Rothman
  text: Rodney Silva The first question is what is the goal of the project. To really
    understand it. Then to go hunting for the right data with standard software approaches.
    This can take anywhere from 1 month to 6 months, a year, and maybe two years!
    In the meantime, you need to find a reason for your customer or employer to keep
    you on the project so it stays alive! If you understand the project, you can begin
    with a useful user interface that enables the users to visualize, understand their
    data and run short but productive tasks. ...
  replies: []
- name: Denis Rothman
  text: Rodney Silva If you can get your project in cruise mode as described above
    then you have plenty of time to build a transformer prototype of the project with
    the model you find best suited for the project in terms of SLA (Service Level
    Agreement) with the customer. SLA is standard IT practice that is well documented
    and contractual.
  replies: []
- name: Denis Rothman
  text: "Mert Bozk\u0131r Your question : What do you think about future of Natural\
    \ Language Processing? What will the location of the Transformers in future ?\
    \ My answer: I see transformer-driven NLP (until a new model comes up) on Cloud\
    \ platforms such as AWS, Googe Cloud or IBM Cloud or another giant such as Microsoft\
    \ Azure. Why? They have reliable scalable servers! I doubt anybody can match without\
    \ the power to back up the sales. The smaller solutions will survive but not be\
    \ critical unless they are partners of the tech giants. NLP will spread out to\
    \ every area of human activity."
  replies: []
- name: Denis Rothman
  text: 'Vladimir Finkelshtein Your question: When do you think we will see transformers
    for non-NLP tasks? including vision. My answers: First of all,l let''s take vision
    out of the picture because there are more legends than actual reality here. Computer
    Vision (CV) relies heavily on massive non-AI algorithms. Then the CNNs do a pretty
    good job. Transformers are kicking in for image captioning. Ok that''s for vision
    because vision is ok right now. There are a lot of solid AI and non-AI tools.
    Now in non NLP, you have transformer driven-Recommenders! They can be applied
    to e-commerce behavior prediction and also can be used in manufacturing. See my
    video here:[https://www.youtube.com/watch?v=tQTpCvZ1-0w&amp;list=PL9uLp9IOO56Gv0YEnRWdrIZOPKwRBHnJe&amp;index=10&amp;t=1s](https://www.youtube.com/watch?v=tQTpCvZ1-0w&amp;list=PL9uLp9IOO56Gv0YEnRWdrIZOPKwRBHnJe&amp;index=10&amp;t=1s)'
  replies:
  - name: Vladimir Finkelshtein
    text: "Denis Rothman Thanks, awesome examples. If I understand correctly, the\
      \ tasks are just naturally reframed as NLP tasks (e.g. in recommendation systems:\
      \ sentences = list of products that one likes, recommendation = fill the mask).\n\
      As for the optimal transport solution, it wasn\u2019t quite clear how the rewards\
      \ are used. Do you just pick a threshold, for which you keep a sequence of actions\
      \ if its reward is above the threshold, and throw away bad sequences? Also,\
      \ I didn\u2019t quite understand how initial and final distributions are encoded,\
      \ but I guess there are more details in the book\u2026"
  - name: Vladimir Finkelshtein
    text: As for vision, for example this paper ([https://arxiv.org/abs/2010.11929](https://arxiv.org/abs/2010.11929))
      claims that transformers achieve almost SOTA or SOTA performance with significantly
      reduced training resources. So perhaps scalability can play a role in adopting
      transformers there.
- name: Denis Rothman
  text: Vladimir Finkelshtein Now, let's take your question a bit further for non-NLP
    transformers. I see powerful solutions being kept secret by tech giants. For example,
    in terms of recommenders, China has access to far more data in terms of volumes
    and information than anybody in the world. They are advancing toward a digital
    society and are many years ahead of the West. For example, they have a national
    digital currency that is expanding with information (like VISA with its tens of
    thousands of transactions per minute but China is more like 300 000 transactions
    per minute). You can easily perceive the patterns you can draw from that with
    sequences of customer behavior.
  replies: []
- name: Denis Rothman
  text: 'Lalit Pagaria Your question:Isn''t Transformers constraints by compute resources?
    What is way forward for startups with less resources? My answer: Let''s go beyond
    the hype and into the real topic! If you use a nice simple robust model BUT have
    excellent datasets you will even beat GPT-3 which used a supercomputer!!! Proof?
    The Pattern-Extracting Training (PET) method I describe in the introduction of
    Chapter 6 of my book. I describe an average sized transformer model that trained
    on an optimized tiny dataset and...beat GPT-3 on the SuperGlue Leaderboard!!!
    More proof? Look at line 13 of the SuperGLue Leaderboard today and you will see
    PET (Tom Schick) with a nice and good accessible computer and then look down at
    line 16. What do you see today? GPT-3 is 3 ranks behind! Conclusion: Humans that
    have imagination can beat super-rich humans and machines any time!'
  replies:
  - name: Lalit Pagaria
    text: "Thank you Denis Rothman for clarification \U0001F64F"
  - name: Denis Rothman
    text: "You are more than welcome! \U0001F60A\U0001F44D\U0001F64F"
- name: Rodney Silva
  text: Denis Rothman Do I need to build a Transformer from scratch to fully understand
    it?
  replies:
  - name: Denis Rothman
    text: Rodney Silva No. But you do need to understand the architecture of the Original
      Transformer described in Chapter 1. You can have a look at the chapter and ask
      me questions this week in our thread.
- name: Vladimir Finkelshtein
  text: What is your position on positional encodings? They seem like an afterthought
    and it is not so clear when to use them. I saw suggestions in the forums to try
    to train models with and without them, because a priori it is not clear in which
    type of problems they are helpful.
  replies:
  - name: Denis Rothman
    text: "Vladimir Finkelshtein Positional encoding is a fundamental part of the\
      \ architecture of the Original Transformer. RNNs contained a separate cumbersome\
      \ positional vector.\nTransformers ADD positional encoding to word(token) embedding.\
      \ This is a powerful feature : the word's \"meaning\" will take its position\
      \ into account which is critical for grammatical and semantic structures.\n\
      That being said \xE0 deBERT model trains positional encoding separately.\nIn\
      \ any case, positional encoding is a very effective tool."
- name: Vladimir Finkelshtein
  text: 'Are there other metrics outside of the GLUE benchmarks on which NLP models
    are compared? For example, if I compared regression with decision trees, I could
    compare sensitivity to outliers, tendency to overfit, reduction of performance
    due to imbalanced data, robustness, explainability (I guess this one is model
    agnostic now) etc.

    Could we compare which NLP model is more susceptible to biases, because they are
    overrepresented in the data?'
  replies:
  - name: Denis Rothman
    text: "Vladimir Finkelshtein Interesting question.\nFirst, some context. SuperGLUE\
      \ was mostly created because the recent arrival of transformers blew the GLUE\
      \ human baselines out of the sky! So SuperGlue was a solution. Now transformers\
      \ are again exceeding the human baselines of SuperGlue.\nIf you use decision\
      \ trees or any other ML/DL algorithm just:\n1.Download the SuperGLUE datasets\
      \ and train them with any algorithm you wish to explore and see what happens.\
      \ You might even end up in the leaderboard. Who knows? \U0001F914"
- name: Zhi Men Lau
  text: Hi Denis Rothman what is your take on interpretability of Transformer?  There
    is a lot of buzz around explainable ML and interpretability, how does Transformer
    address these issues compare to other technologies.
  replies:
  - name: Denis Rothman
    text: 'Zhi Men Lau The best Explainable (Interpretable) AI methods are MODEL AGNOSTIC.
      This means they use the input data to explain very precisely why a result was
      obtained.

      I explain this in my book on [Hands-On Explainable Artificial Intelligence(XAI)](https://www.amazon.com/Hands-Explainable-XAI-Python-trustworthy/dp/1800208138/ref=mp_s_a_1_3?dchild=1&amp;keywords=Denis+Rothman&amp;qid=1618930655&amp;sr=8-3)

      For example, for an input such as "the coach(bus or sports coach?) was unhappy",'
  - name: Denis Rothman
    text: If you have any questions please feel free to ask me.
  - name: Zhi Men Lau
    text: Thanks Denis, didn't know about your other book on XAI.  Going to check
      it out.
- name: Rodney Silva
  text: Denis Rothman Can you guess  what will be the evolution of transformers in
    the next years? Less complexity,efficency,less training time,etc...
  replies:
  - name: Denis Rothman
    text: 'Rodney Silva Transformers will expand to every single field involving sequences
      including recommenders.

      Then a new model, one day, will take over. Mastering transformers will make
      the transition to the future much faster for developers and designers.'
- name: Krzysztof Ograbek
  text: 'Denis Rothman Thank you for yesterday''s answers. Correct me if I''m wrong,
    but I believe that training transformers doesn''t require any knowledge about
    the language itself. I mean to train a transformer we just need a pre-trained
    word embedding, feed it to the transformer and wait for the results. So the question
    here. Nowadays, what is the point of learning things like: Linguistic syntax,
    dependency parser, Part-of-Speech, Named Entities, etc? How does this "language
    knowledge" make one a better NLP Specialist?'
  replies:
  - name: Denis Rothman
    text: "Krzysztof Ograbek Good question! In real life implementations the models\
      \ take weeks if not months to train. Mastering the  Linguistics of the Superglue\
      \ tasks, e.g.,and translations will save you an incredible amount of time! Otherwise,\
      \ understanding errors and correcting them can take exponentially longer.\n\U0001F609"
- name: RH
  text: 'Denis Rothman: If someone is starting their journey into NLP, what is the
    pathway you would recommend them to take? What knowledge/skills makes a strong
    industry ready NLP practitioner?'
  replies:
  - name: Denis Rothman
    text: 'I recommend two axes:

      1. Mastering basic calculus, matrix and vector multiplications and good basic
      statistics.

      2. Linguistics. Knowing what a lexical field is, what semantics is about, phonology(intonation,
      for example)

      Then everything in NLP becomes easy to understand!'
- name: Doink
  text: Denis Rothman Is learning about Bag of words, tf-idf, w2vec, rnn and lstm
    a waste of time? How much do we need to know in NLP it's an ever growing field.
  replies:
  - name: Denis Rothman
    text: "Nothing you learn is a waste of time. Learn everything you can and spend\
      \ all the time you have. \nYou will then quickly discover two fantastic things\
      \ about yourself :\n1.The more you learn the faster you learn something new.\
      \ It's exponential!\n2.The more you know, the faster you will implement NLP\
      \ projects. On top of that, you will be able to explain your work much better\
      \ to others in a team. \U0001F44D"
  - name: Doink
    text: what is the proof of 1. ?
- name: VK
  text: Denis Rothman  What type of research was implemented for writing this book?
  replies:
  - name: Denis Rothman
    text: "1.First my background helped: mathematics and linguistics. You can find\
      \ out more in [this article](https://www.amazon.com/Hands-Explainable-XAI-Python-trustworthy/dp/1800208138/ref=mp_s_a_1_3?dchild=1&amp;keywords=Denis+Rothman&amp;qid=1618930655&amp;sr=8-3)\n\
      2.My previous research, corporate experience and writing books. You can find\
      \ out more [here](https://www.amazon.com/Denis-Rothman/e/B07DFRCJG8/ref=dp_byline_cont_book_1)\n\
      3.Reading hundreds of pages of papers on Transformers and exploring all of the\
      \ source code available in 24/7 mode. It was quite a fantastic experience! \U0001F60E\
      \U0001F61C\U0001F600"
  - name: VK
    text: Thank you Denis Rothman
- name: Akshat
  text: Denis Rothman Hi Denis, can these transformer models be used in predicting
    physical quantities in car crash simulations or other numerical simulations?
  replies:
  - name: Denis Rothman
    text: 'Let''s be careful here! Transformers are excellent in predicting sequences.
      They  can be used to predict if a car crash is probable.

      However, for precise numerical series, I would rely more on standard math.'
  - name: Akshat
    text: "Thanks Denis Rothman! \U0001F642"
- name: Rodney Silva
  text: Denis Rothman What's the most common difficulty for people trying to learn
    the architecture of Transformers?
  replies:
  - name: Denis Rothman
    text: The most common thing I have seen is a lack of patience and underestimating
      the work it takes to understand the Original Transformer as described in Chapter
      1 of my book. If someone takes the time to understand this chapter, then the
      rest becomes easier if not easy with some basic knowledge of Linguistics that
      really helps.
- name: Lalit Pagaria
  text: "Denis Rothman this not a question but appreciation message. Tomorrow I received\
    \ your book still in first chapter. So far so good. Really nice book. \U0001F64F"
  replies:
  - name: Denis Rothman
    text: "Thank you very much for your encouraging message! Please ask me any questions\
      \ you may have. \U0001F60A\U0001F64F"
  - name: Lalit Pagaria
    text: "Thank you Denis \U0001F64F"
  - name: Denis Rothman
    text: "Your more than welcome. \U0001F60A"
- name: Rodney Silva
  text: Denis Rothman  How much time did it take to write this book, from the research
    till the final version?
  replies:
  - name: Denis Rothman
    text: "The time it took requires context :\n1.I have been doing AI research for\
      \ the past 35+ years on a daily basis from expert systems to ML/DL. In that\
      \ same period I implemented my research on key corporate sites.\nFor more you\
      \ can peek into my LinkedIn profile starting here.\n2.I studied linguistics\
      \ in college and at the time taught computer science as well. I've been studying\
      \ cognitive sciences all my life.\n3.I'm used to writing papers and books on\
      \ AI.\nThat being clarified \U0001F60A, I did the research, (papers and source\
      \ code), tested code/wrote code, and wrote the book in 10 weeks.\nOne last point.\
      \ I'm a workaholic when I write. I 'm in 24/7 mode, can get up at any of the\
      \ night because something just popped up, develop at the dinner table or anywhere.\n\
      As long as the book isn't finished, I just keep on pounding on the laptop!\U0001F60A"
  - name: Denis Rothman
    text: 'P. S. Here is the link mentioned in the message :

      My 1982 Word2vector-Word Piece model patent led to an AI NLP Cognitive Chabot
      and a Turing-APS model used in Major Corporations to this day!

      [https://www.linkedin.com/pulse/did-you-miss-ai-parsing-train-denis-rothman](https://www.linkedin.com/pulse/did-you-miss-ai-parsing-train-denis-rothman)'
  - name: Alexey Grigorev
    text: 10 weeks! Wow! That's super impressive!
  - name: Krzysztof Ograbek
    text: Alexey Grigorev, agreed. Denis Rothman, this is just amazing. Your background
      also
  - name: Denis Rothman
    text: "Thanks. It's hard work. \U0001F60A"
- name: Krzysztof Ograbek
  text: Denis Rothman I don't know how to properly phrase my question, but I hope
    you'll know what I mean. How to take advantage of speaking multiple languages?
    How to use it in NLP field?
  replies:
  - name: Denis Rothman
    text: 'Mastering more than one language is naturally an asset in NLP. First, it
      develops better knowledge of language structures and meaning.

      When testing translation models, it''s a good asset.

      However, we cannot master all of the language s we will face, so there is a
      limit to that asset!'
- name: Krzysztof Ograbek
  text: Denis Rothman Could you recommend some good resources for learning linguistic,
    that can be useful in NLP?
  replies:
  - name: Denis Rothman
    text: "A good place to start with linguistics is a good elementary or high school\
      \ book of grammar!\nThen an easy book on semantics and phonology /phonetics.\n\
      In short, the easier the better to build a solid approach.\nThen once that is\
      \ done, look for a nice book or course you like. \U0001F60A"
  - name: Krzysztof Ograbek
    text: "Denis Rothman, thank you again. I found [this tutorial](https://www.youtube.com/playlist?list=PLoROMvodv4rOFZnDyrlW3-nI7tMLtmiJZ) on YT, it has 100\
      \ videos.\
      \ Would you be so kind to skim through the titles and say if the content makes\
      \ sense for beginners? I already learned plenty from this. I just wonder if\
      \ the direction is right \U0001F642"
  - name: Denis Rothman
    text: 'I see that these videos were designed by Stanford professors. If you find
      them interesting, then of course you can follow them.

      Just keep transformers in mind as well.'
- name: Rodney Silva
  text: Denis Rothman  What was your reaction the first time you realised how transformers
    worked? Do you think that you could have invented Transformers?
  replies:
  - name: Denis Rothman
    text: "When I first explored the Original Transformer model, I was in awe. The\
      \ small Google team that was working on this new model were experimenting all\
      \ sorts of ways to solve the limitations of RNNs.\n It was low level trial and\
      \ error. Then they decided to drop the 30+year old concept of recurrence and\
      \ replaced it with attention!\nThey also industrialized the layers that are\
      \ all the same size, spilt the layers into parallel processing, and went on\
      \ like that for everything in it.\nThey surprised themselves by outrank ing\
      \ everybody on the NLP leaderboards.\nI was admirative of this little team within\
      \ a large corporation. \U0001F60A"
  - name: Rodney Silva
    text: And how about the second question? Denis Rothman
  - name: Denis Rothman
    text: "Right. Could I have invented transformers?\nNo. Why?\nI don't think of\
      \ NLP only in terms of statistics. I think transformers are a fantastic evolution\
      \ but will also, like RNNs, be prehistory as IoT sensors develop and concepts\
      \ are added. \nIn my book in AI by Example, I teach a CNN how to learn concepts\
      \ in Chapter 10 CRL. In chapter 6 on translations, I introduce symbols in the\
      \ Google translate API:\n[link](https://www.amazon.com/Artificial-Intelligence-Example-advanced-learning/dp/1839211539/ref=mp_s_a_1_3?dchild=1&amp;keywords=Denis+Rothman&amp;qid=1619109365&amp;sr=8-3)\n\
      Now why do I think this?\nI often use the simple word \"hello\". \nThere are\
      \ billions of interpretations of that word. \nLet me give you some. \n1. Person\
      \ A is sitting in an office working. Person B comes in and says \"hello\" in\
      \ a neutral tone. \n      Context : B has never said hello in 10 years to A,\
      \ even when in the same elevator. \nInterpretation by A: Am I going to be fired?\
      \ What's going on?etc. \n2.B walks in and mumbles a gloomy hello. \nContext\
      \ : B is always chirpy, smiling and happy. \nInterpretation by A: Did I do something\
      \ wrong? Is something wrong with B? What's Going on. \n3.B comes in and gets\
      \ very very close to A and says \"helloooo\" like a hungry wolf. \nInterpretation\
      \ by A: This happens every day. Oops! Is this some kind of harassment? What\
      \ should I do. \n4 to infinity! \nNow add more words, situations and body language,\
      \ cultural habits and emotions! \nHumans are very complex machines faced with\
      \ an infinity of complex situations. \nStatistics can help. But more is to come!"
- name: Rodney Silva
  text: 'Denis Rothman What do you think is the most brilliant thing in Transformers:
    multi head attention or sinusoidal positional encoding?'
  replies:
  - name: Denis Rothman
    text: 'Using attention with simple matmul operations was baffling. Then adding
      cos/sin positional encoding to the vectors/matrices instead of adding more vectors
      was brilliant. I enjoy trigonometry so I liked that.

      Both ideas are beautiful. Some recent models have separately trained positional
      encoding(deBERT, for example).

      Everything is brilliant. It''s like building a new motor engine in your garage
      at home. That''s how they did it.'
- name: Lalit Pagaria
  text: Denis Rothman what is faster ways to test which encoding would be great for
    a task instead of going into whole train - test life cycle. At least any fast
    intuitive way to try first in order to get fast feedback.
  replies:
  - name: Denis Rothman
    text: 'The fastest way to choose a model in production is to have learned transformers
      from A to Z in general. And during that process select the one you like the
      best.

      Once that is done, there are many ways to train and fine-tune models. Have a
      look at the PET approach, for example, in the beginning of chapter 6 of the
      book.

      PET is pattern-extracting training which processes the data BEFORE training
      a model. It like a good teacher that well prepares a course instead of throwing
      raw information at the students!'

---

The transformer architecture has proved to be revolutionary in outperforming the classical RNN
and CNN models in use today. With an apply-as-you-learn approach, Transformers for Natural
Language Processing investigates in vast detail the deep learning for machine translations,
speech-to-text, text-to-speech, language modeling, question answering, and many more NLP domains with transformers.

The book takes you through NLP with Python and examines various eminent models and datasets
within the transformer architecture created by pioneers such as Google, Facebook, Microsoft,
OpenAI, and Hugging Face.