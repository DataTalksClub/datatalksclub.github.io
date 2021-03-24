---
title: "Reinforcement Learning"
description: "Book of the Week. Reinforcement Learning by Phil Winder"
cover: "images/books/20210111-reinforcement-learning/cover.jpg"
image: "images/books/20210111-reinforcement-learning/preview.jpg"
start: 2021-01-11 00:00:00
end: 2021-01-15 22:59:59
authors: [philwinder]
links: 
  - text: Book's page on O'Reilly
    link: https://www.oreilly.com/library/view/reinforcement-learning/9781492072386/
  - text: Book's page
    link: https://rl-book.com/

archive:
- name: Dmitry Yemelyanov
  text: 'Hello, Phil Winder! First of all, thanks for kindly agreeing to share your
    knowledge with us :muscle:

    :question: So my question is:

    Could it be possible to improve performance of RL agent doing humanoid motions
    by virtual demonstrations of a person wearing a mocap suit and what, in your opinion,
    would be TOP challenges in order to do this?'
  replies:
  - name: Phil Winder
    text: ":100: yes. This is a perfect example where Behaviour cloning/Imitation\
      \ RL will be useful. In fact, this reminds me of a paper that I read a while\
      \ ago\u2026 Here: [https://bair.berkeley.edu/blog/2020/04/03/laikago/](https://bair.berkeley.edu/blog/2020/04/03/laikago/)\n\
      Gif for example. 1) Motion capture, 2) no IRL, 3) with IRL."
- name: Alexey Grigorev
  text: Apart from multi-armed bandits, what are the other RL techniques that are
    getting wide adoption in the industry?
  replies:
  - name: Phil Winder
    text: "Good question but it\u2019s hard to obtain any real numbers on this. From\
      \ my research/reading, most people tend to follow the media. If a particular\
      \ algorithm gets media attention then it\u2019s then quite popular in the frameworks\
      \ which then leads to adpotion.\nIn general though, the tried and tested, simple\
      \ models tend to remain the most popular. From basic Q-learning based algorithms,\
      \ to simple policy gradient algorithms like SAC.\nThere\u2019s no one-size fits\
      \ all \u201Cbest algo\u201D though, like in ML, the \u201Cno free lunch\u201D\
      \ theorem. So you have to evaluate and experiment for your particular application."
- name: Phil Winder
  text: "Morning all. I\u2019ll be online all week and responding to questions in\
    \ threads. Be sure to tag me so I don\u2019t miss the message. Thanks in advance!"
  replies:
  - name: Alexey Grigorev
    text: Good morning!
- name: Sara Lane
  text: 'Good morning Phil Winder!

    Which industries do you see being most affected by advancements in reinforcement
    learning? More specifically, in which industries do you think it will prove the
    most useful and also will be open to actually implementing the necessary changes?'
  replies:
  - name: Phil Winder
    text: "Hi SL,\nFor reference, see page 5-7 of the book.\n\u201CIndustry\u201D\
      \ is a tricky word because it is broad and out-dated. It\u2019s similar to asking\
      \ what industry could make use of software. Of course, all of them could. There\
      \ are opportunities everywhere.\nWith that said, it\u2019s a valid question.\
      \ So far, robotics seems to be the number 1 use case. Simply because it\u2019\
      s hard to derive control programs for complex tasks. It\u2019s easier to learn\
      \ them.\nPricing/bidding/recommendations/advertising/etc. are largely similar\
      \ tasks and have also had a lot of press.\nThe finance industry are going to\
      \ be big users. I\u2019ve spoken to people already that are using it.\nHealthcare\
      \ and specifically personalised medicine is a perfect match, although the regulatory\
      \ requirements are likely to prevent this from taking off.\nThe Tech industry\
      \ can leverage it to much greater extents for automation. E.g. ML, auto-ML,\
      \ neural architecture search, etc. Lots of mundane automation like Alexa, email\
      \ control, etc.\nAnd lots more\u2026 :smile:"
  - name: Sara Lane
    text: 'Thanks for the clear response!

      I know that all industries could technically use this technology, but I''ve
      seen that many businesses are hesitant to take on new things. Many of them live
      by the adage, if it ain''t broke, don''t fix it. So I''m curious more where
      you see it taking off practically, not theoretically.

      What you said about healthcare is interesting, why would regulatory requirements
      prevent reinforcement learning from improving things there?

      As far as pricing/bidding/recommendation/advertising, why is reinforcement learning
      superior to other forms of machine learning for this?

      Thanks!'
  - name: Phil Winder
    text: "Healthcare == people\u2019s lives. So there\u2019s lots of rules and regulations\
      \ to prevent accidents. This means there\u2019s a very high barrier to entry.\
      \ (I\u2019m talking from a UK/EU perspective by the way :wink: - there may be\
      \ fewer regulations in, say, the US for e.g.)\nBetter depends on your application.\
      \ Testing, experimentation and evidence will prove whether it\u2019s better.\
      \ But in general, any application that involves mult-step decision making could\
      \ be improved by RL. ML makes one-shot decisions which are unlikely to be optimal\
      \ in the long run.\nSee page 5 in the book."
  - name: Sara Lane
    text: 'Phil Winder I just read pages 5-7, fascinating! As you wrote, I always
      associated RL with robotics and not much else. Thanks for clarifying and I look
      forward to reading more.

      And I believe that you''re correct, in the USA there aren''t as many regulations
      for these things and I wonder if we will indeed see RL being used in healthcare
      in the coming years.'
- name: Neal Lathia
  text: ':question: Phil Winder What are your top tips for debugging RL algos?'
  replies:
  - name: Phil Winder
    text: "Great question. Check out chapter 11 for more detail on this.\nHere\u2019\
      s some random thoughts off the top of my head:\n1. Visualise what is going on\
      \ (like any data-related task)\n2. If you are given the environment, start with\
      \ the simplest algorithm and work up (e.g. random/CEM).\n3. If you have control\
      \ over the environment/simulation, make that as simple as possible and solve\
      \ that first. Then make the environment/simulation more complex.\n4. Split the\
      \ tech. If you\u2019re working with deep models, attempt to decouple the training\
      \ of the deep NN from the RL. Not always optimal, but makes development much\
      \ easier. For example, use autoencoders, train the autoencoder first and verify\
      \ it works. Then pass the much lower-dimensional state into the RL algo. It\
      \ will train much faster (possibly less optimally) and it will be easier to\
      \ figure out issues.\n5. Split the problem. Try and halve the problem. Halve\
      \ it again. Solve each quarter independently.\n6. Consider hierarchical policies\
      \ (similar to 5). If you can manually design the hierarchy, even better for\
      \ understanding/explainability. But you can automate that process too.\n7. Good\
      \ old debugging techniques. print\u2019s are your friend.\n8. Assert expected\
      \ array sizes\n9. Don\u2019t overcomplicate the reward function.\nAnd more and\
      \ more\u2026"
  - name: Dmitry Yemelyanov
    text: 'Great answer! :thumbsup:'
- name: Jayesh Garg
  text: Are there customers already live with RL algorithms?
  replies:
  - name: Phil Winder
    text: "Hi Jayesh. Oh if only my sales team had access to that information. :smile:\n\
      So, there\u2019s a variety of things that I\u2019ve heard. Some public, some\
      \ not. Let me try and recall some:\n- [Covariant AI](https://covariant.ai/)\
      \ demoed a super cool RL-driven pick and place robot.\n- I\u2019ve spoken to\
      \ engineers that have used RL to improve their recommendations.\n- I\u2019ve\
      \ spoken to leaders that have deployed RL as part of a continuous-learning strategy\
      \ for their ML models.\n- I spoke to another leader that managed to reduce the\
      \ size of the ML team running their core recommendations algorithm by using\
      \ RL.\nAnd there\u2019s loads of use cases reported in the papers. But of course,\
      \ whether you call that production or not depends on what they are doing. Many\
      \ are pure research. But lots are for research on current production systems.\
      \ For example, this one from the [YouTube team](https://rl-book.com/applications/2019_reinforcement_learning_for_slatebased_recommender_systems_a_tractable_decomposition_and_practical_methodology/),\n\
      More on [https://rl-book.com/applications/](https://rl-book.com/applications/)\
      \ and in the book.\nOf course if you know anyone that wants to develop production\
      \ RL algorithms, let me know. :wink:"
- name: Vladimir Finkelshtein
  text: What would be an example of environment with which one can experiment at home?
    I have neither robotic hand at home nor trading partners willing to make biding
    wars. The card/text/video games are covered in much detail in the books. It will
    be more interesting to play with something resembling a commercial use case.
  replies:
  - name: Phil Winder
    text: "Hi Vladimir,\nThe world really is your oyster here. You can create your\
      \ own in a domain that you want more experience in (that\u2019s a great way\
      \ to gain experience). Or you can search through the thousands of gyms other\
      \ people have created.\nFor example:\n- [https://github.com/topics/openai-gym](https://github.com/topics/openai-gym)\n\
      - [https://rlenv.directory/](https://rlenv.directory/)"
- name: Rishabh Bhargava
  text: Phil Winder what are the most common use cases in industry where problems
    are framed as supervised learning (or ranking) problems, but you would reframe
    them as RL problems? what would be the evidence you would give such teams?
  replies:
  - name: Phil Winder
    text: "Hi Rishabh. Really great question and one that deserves a much more comprehensive\
      \ and evidence-based answer.\nBut, if I had to try and fit it in a chat window\u2026\
      .\nI\u2019d summarise the dilemma by reminding you of the Markov Decision Process\
      \ (MDP - page 35 of the book).\nIf you have an environment that has state that\
      \ can be mutated, if it can be observed, if you can alter the state through\
      \ your agent\u2019s actions, and if you have a business problem that where it\
      \ pays to move the environment into a certain state, then by definition you\
      \ have an RL problem.\nTo the first part of your question, common use cases\
      \ masquerading as supervised ML\u2026\nAny recommendations task. I think that\u2019\
      s broad enough for you! I would suggest that the vast majority of cases where\
      \ people use recommendations are optimising for the wrong thing. The goal is\
      \ to help the user find things as easily as possible so that they value the\
      \ functionality and keep coming back/buying unnecessary plastic stuff.\nA standard\
      \ solution (I\u2019m grossly simplifying here) would build a model, in a supervised\
      \ manner, that maps user intent to products, quantified by click through rate\
      \ or something.\nThat\u2019s entirely the wrong metric. You could use RL and\
      \ train over full customer lifecycles. You could train on raw profit. Or the\
      \ amount of time individual users spend on the site. Or whatever is most applicable\
      \ for your problem.\nSo the action is the recommendation (lots of research available\
      \ on this). The environment is user and possibly the business/products. The\
      \ observation is the product catalogue, user demographics, past history, information,\
      \ the weather, etc. The reward is customer lifetime value or whatever.\nLook\
      \ up any of the RL recommendations papers for an academic argument as to why\
      \ RL is better suited."
  - name: Rishabh Bhargava
    text: 'Thanks for the great answer.

      On the topic of recommender systems: if the metric that is being optimized might
      be off, do you think this is more down to Product Managers not setting the metrics
      correctly or ML engineers choosing to solve for the simpler problem (even though
      it might not be the right formulation)? Given that this is such a technical
      domain, who should be pushing for RL adoption?'
  - name: Phil Winder
    text: "Like most things in life, I suspect there\u2019s no easy or right answer.\
      \ I\u2019m no expert in management, but I think POs or PMs should be steering\
      \ product development, but decisions should be agreed/discussed as a team. Ideas,\
      \ solutions, metrics, everything, have to be defined by \u201Cthe team\u201D\
      \ because no one person can know everything and get everything right.\nI have\
      \ the same argument with people that have the word \u201Carchitect\u201D in\
      \ their title. :wink:"
- name: Ashutosh Sanzgiri
  text: Hi Phil Winder - I am curious as to why RL techniques are not widely used
    as a means to improve on supervised learning problems - by this I mean both in
    model training (hyperparameter optimization, architecture search, ensembling models
    etc.) and in model deployment (measuring model drift, correcting for it etc.)
  replies:
  - name: Phil Winder
    text: "&gt;  why RL techniques are not widely used as a means to improve on supervised\
      \ learning problems\nWhy? I guess it\u2019s some complex combination of attention,\
      \ media, ease of use, advice, reading, media and something with the word OpenAI\
      \ or Google in the name. :smile:\nI mean, it\u2019s there, it\u2019s possible.\
      \ Maybe it\u2019s just waiting for someone to wrap it or market it better than\
      \ the last person? Hint hint, nudge nudge. If you have a spare 6 months on your\
      \ hands. :slightly_smiling_face:\nTo be fair there are things out there already.\
      \ For example I\u2019ve used Optuna for hyperparameter optimisation, which has\
      \ an RL solution in there.\nBut they\u2019re not selling the fact that it\u2019\
      s using RL. They\u2019re selling the fact that it automatically does hyperparameter\
      \ tuning for you.\nSame with Kubeflow\u2019s Katib. That has an RL mode too.\n\
      That\u2019s the thing about engineering in general. People don\u2019t care how\
      \ the sausage is made. It\u2019s the product that counts. And it\u2019s why\
      \ UI engineers take all the glory!"
- name: A McCauley
  text: "Hi Phil Winder , congratulations on the book! I have a question on the topic.\
    \ \nIs reinforcement learning considered a crucial approach in robotics (or do\
    \ you have an opinion on its use for this)?\nWith a robot learning behaviours\
    \ through \u2018trial and error\u2019 of their interactions. It seems like RL\
    \ would have many advantages which ML just couldn\u2019t solve in this case -\
    \ becoming useful with dynamically changing constrains, or environments, they\
    \ would experience. "
  replies:
  - name: Phil Winder
    text: "Hi A,\nCrucial. Hmmm. Depends on how you define the word. I wouldn\u2019\
      t say it\u2019s CRUCIAL, in capital letters, no. You can create perfectly adaquate\
      \ solutions using simple stuff like PID controllers and inverse kinematics.\n\
      The threshold is complexity. Once you need to do something remotely complex,\
      \ like more complex than just \u201Cmove to coordinates x,y\u201D or as soon\
      \ as it involves a non-trivial number of interacting components, then yes, RL\
      \ is probably necessary.\nBut I think that\u2019s missing the point slightly.\
      \ The great thing about RL is the interface. The MDP. It\u2019s a way of defining\
      \ problems, not solutions. And it can be applied to any project, simple or complex.\
      \ If the interface is the same then you can use the same processes, the same\
      \ techniques to solve a wide variety of problems. It scales from simple to mind-bendingly\
      \ complex, very few ML techniques and say the same.\nFor example, if you worked\
      \ for a robotics company and you sold a bomb-disposal robot and a floor-cleaning\
      \ robot, you\u2019d have to develop completely different architectures, systems,\
      \ code, solutions, etc. But if you\u2019re using RL, it\u2019s the same. Define\
      \ the environment, define what you\u2019re trying to do, try lots of actions\
      \ and learn which ones maximise the reward.\nSorry, rambling a bit. But yes,\
      \ I think we\u2019re on the same page!"
- name: Alexey Grigorev
  text: 'Phil Winder you mentioned in a thread that RL was used for "reducing the
    size of the ML team running their core recommendations algorithm".

    I''m curious to learn more about it. If it''s possible, can you give more details
    about this case? How did they actually do it?

    And another question - when RL will replace all the data scientists? :sweat_smile:'
  replies:
  - name: Phil Winder
    text: "Haha. Thanks Alexey. I knew someone would pick up on that.\nThis is not\
      \ another clickbait \u201Cwe all won\u2019t have jobs next year\u201D. :smile:\n\
      No I can\u2019t I\u2019m afraid, it\u2019s not public knowledge.\nTo summarise,\
      \ consider:\na) a team of 10+ highly educated, very expensive smart people tweaking\
      \ neural network architectures and running massive expensive experiments (for\
      \ example). This is what large tech companies do to solve heavily used, data-intensive\
      \ systems.\nvs.\nb) an RL algorithm, with a decent reward function, that trains\
      \ itself over the long term, to solve the actual business metric that the business\
      \ is keen on improving.\nRL can easily match and with effort surpass the performance\
      \ of that team quite quickly.\nTo be clear, the engineering challenge doesn\u2019\
      t go away, it shifts. Now these people are curators. Guardians of the RL algorithm\
      \ that is actually doing the number crunching. There\u2019s still a lot of engineering\
      \ work that goes into building a system like that, but it\u2019s not pure data\
      \ science any more.\nI\u2019m being intentionally vague and speculative here,\
      \ but you can see it happening.\nedited for clarity."
  - name: Alexey Grigorev
    text: Makes sense. I like the "guardian" metaphor! Thank you
- name: Alexey Grigorev
  text: "Good morning!\nPhil Winder you mentioned that \"the engineering challenge\
    \ doesn\u2019t go away, it shifts\".\nI'm curious to learn about these engineering\
    \ challenges that come with training and deploying RL algorithms. How are they\
    \ different from \"classical\" ML and DL models? What are the typical tools for\
    \ training and deploying?"
  replies:
  - name: Phil Winder
    text: "Morning Alexey.\nFirst, bear in mind that there isn\u2019t much industrial\
      \ experience of running RL in production, yet. It\u2019s not like ML, where\
      \ there\u2019s now years worth or experience to leverage. But I can speculate.\n\
      One of the key issues with RL is state. By definition the MDP loop is constantly\
      \ evolving. New observations, new models, new actions. In particular, if you\u2019\
      re running an algorithm which is actively learning (most, but not all implementations),\
      \ which means that the underlying state of the model (the trained parameters)\
      \ are changing ALL the time.\nOne of the definitions of \u201Cmodern\u201D software\
      \ is immutability and software that is free of side effects. By definition,\
      \ an actively learning RL algorithm is mutable and most definitely has side\
      \ effects!\nSo over the next few years I predict that there is going to be industrial\
      \ research (i.e. new frameworks/blog posts/presentations/etc.) into how to run\
      \ mutable RL algorithms in a robust way. I imagine that under the hood there\
      \ will be a strategy to do some kind of checkpointing to make it pseudo-immutable.\n\
      On the training side, there\u2019s loads. I can\u2019t keep up. I did a review\
      \ a long time ago and I\u2019ve been meaning to update it (here: [https://rl-book.com/rl-frameworks/](https://rl-book.com/rl-frameworks/)).\
      \ Take your pick.\nOn the deployment side, less so. Many of the frameworks above\
      \ have some kind of serving mode, but I get the impression that most people\
      \ have to roll their own serving infrastructure and tooling."
  - name: Alexey Grigorev
    text: Thank you! Looking forward to seeing how this field develops
- name: Ritobrata Ghosh
  text: Phil Winder, can this book be treated as a primary textbook of Reinforcement
    Learning or a reference book for studying Reinforcement Learning?
  replies:
  - name: Phil Winder
    text: "Hi Ritobrata,\nSorry I don\u2019t quite understand your question. Can you\
      \ explain what you are looking for?\nI wrote this book from an industrial perspective.\
      \ It contains more \u201Cadvice\u201D that you would expect from an academic\
      \ reference. It also contains less mathematics than you would expect from academia.\n\
      My goal was to try and be a bridge between the industrial, software-driven world\
      \ and academic research."
  - name: Samuel O. Alfred
    text: Phil Winder  I actually like this question. I have read the popular reinforcement
      learning book by Bartto and Sutton. I don't have access to your book. So, is
      your book an extension or looking at things from a different perspective with
      the same underlying principles?
  - name: Phil Winder
    text: "Yes, the underlying principals are the same. We\u2019re both talking about\
      \ RL in the context of the MDP and build up from there.\nMy book is far more\
      \ focussed towards industry. I cover more modern algorithms and talk a LOT more\
      \ about how to do RL in industry. Sutton/Barto\u2019s book is more formal, has\
      \ a lot more maths, talks less about industrial concerns. In short, Sutton/Barto\u2019\
      s is a textbook. Mine is an O\u2019Reilly book. :slightly_smiling_face:"
  - name: Phil Winder
    text: "Sutton/Barto\u2019s book is excellent for what it is, by the way. I recommend\
      \ getting both. :smile:"
  - name: Phil Winder
    text: 'You can find more info on the main page of the website: [https://rl-book.com/](https://rl-book.com/)

      I might add some pages from the preface there too, to answer this question outright.

      Thanks!'
  - name: Ritobrata Ghosh
    text: Phil Winder, thanks for the reply. Appreciate it.  Look forward to reading
      your book. I suggest Sutton and Barto's book to everyone who asks me. Many came
      back to me looking for an alternative. While not a substitute, Thomas Simonini's
      tutorials do offer a different attempt in learning RL. So I was asking you if
      learners could read your book to gain a fair level of knowledge in RL before
      eventually graduating towards Sutton and Barto.
  - name: Phil Winder
    text: "Yeah I\u2019d agree with that. Most engineers in industry are probably\
      \ going struggle a bit with sutton\u2019s because it\u2019s too academic. So\
      \ yes, I\u2019d definitely recommend reading mine first. :blush:"
  - name: Ritobrata Ghosh
    text: Phil Winder Yes, you are right. Even with my background in Physics, I found
      Deep Learning textbooks such as Goodfellow's to be easier to read than Sutton,
      Barto's book. I have my answer, thanks. Look forward to reading this book!
- name: Leonid Kholkine
  text: 'Hello Phil Winder!

    Happy to see a book more focused on the industry. I know that more and more companies
    are exploring the application of RL, but, at least in Portugal, it is still in
    a very embryonary stage. I''m wondering how do you see the adaption of RL by the
    industry?'
  replies:
  - name: Phil Winder
    text: "Hi Leonid,\nLike you said, nascent at this point. But it is moving. I don\u2019\
      t think it will be anywhere as big as the generic ML/analytics industry, which\
      \ in turn isn\u2019t as big as the software industry.\nBut as you probably know\
      \ already, these are just tools in your tool belt. The trick is to pick the\
      \ right tool for the job.\nIn terms of adoption, I think it\u2019s being adopted\
      \ already. It\u2019s just a matter of size. I think it will cascade as more\
      \ \u201Cnormal\u201D use cases come into popular industrial culture. And as\
      \ frameworks/libraries start to offer easy to use and robust RL serving, natively.\n\
      In short, we\u2019re fighting against low-hanging fruit here. Quite often something\
      \ very simple is good enough and/or better than nothing. It takes quite a lot\
      \ to jump up through the hoops of full ML to full RL.\nThis probably means that\
      \ it\u2019s going to be larger companies that adopt first. Smaller ones (at\
      \ least in the non-tech industry) will probably have to wait."
  - name: Phil Winder
    text: Yeah, to be clear, I see RL taking a slice of the ML industry. So RL depends
      on the underlying size of the ML and software industries.
  - name: Leonid Kholkine
    text: 'That leads me to another thought, will there be then more out of the box
      tools as it happens now more and more with ML?

      I think that also might shorten this gap'
- name: Leonid Kholkine
  text: 'And a more interesting question for me, it''s how do you see RL being applied
    besides the classical cases such as recommender systems, Auto ML, finances, robotics,
    etc... :slightly_smiling_face:'
  replies:
  - name: Phil Winder
    text: "Hi again Leonid,\nI\u2019m afraid I\u2019m going to have to resort to:\
      \ `${insert any use case here}`. :smile:\nSorry, I couldn\u2019t help it. :stuck_out_tongue:\
      \  It has a very broad applicability. In fact, you could technically use it\
      \ anywhere you currently use ML. Although it may not technically be more performance.\
      \ But it many cases it could be.\nI\u2019ve been trying to collate use cases\
      \ here ([https://rl-book.com/applications/](https://rl-book.com/applications/)).\
      \ There\u2019s lots already, but I\u2019m already well out of date.\nCheck out\
      \ some of the other answers here too: [https://rl-book.com/learn/faq/frequently_asked_questions/](https://rl-book.com/learn/faq/frequently_asked_questions/)\n\
      Apologies for the generic answer but the real answer is really broad."
  - name: Leonid Kholkine
    text: 'That''s a perfect answer, I did miss those use cases :slightly_smiling_face:'
- name: Alexey Grigorev
  text: 'Good morning!

    Phil Winder I know you also have a lot of interest in MLOps. Is there any connection
    between it and RL in your work?'
  replies:
  - name: Phil Winder
    text: "Great question.\nYou\u2019re right. I am very interested and we\u2019ve\
      \ gained a lot of experience delivering MLOps projects.\nThe connection to RL\
      \ is the operational part. RLOps, if you will. Just like in ML, data scientists\
      \ probably aren\u2019t that interested in spending massive amounts of time messing\
      \ about with infra/tooling. They\u2019re job and responsibility is extracting\
      \ value from data, not building supporting infra.\nThe same is true in RL too.\
      \ The value is delivering the algorithm that optimises the business metric.\
      \ The Ops part is irrelevant. The business doesn\u2019t care how it happens,\
      \ just that it does.\nBut the business certainly does care how long it takes\
      \ and whether it is operationally viable. They\u2019d be the first to complain\
      \ if it breaks.\nSo there is value in the supporting tech/infra, but it\u2019\
      s not directly tied to the business objective. The value is \u201Cmaking it\
      \ easier for other people to do their job\u201D.\nSince RL is hard to do well,\
      \ and very difficult to operationalise/productionise, RLOps certianly has a\
      \ very important role to play."
  - name: Alexey Grigorev
    text: Great, thank you! Excited to see how "RLOps" is going to develop
- name: Alexey Grigorev
  text: 'I was checking the book on Amazon and noticed this:

    Best Sellers Rank:

    - #136 in Machine Theory (Books)

    - #155 in Minecraft Guides

    - #165 in Artificial Intelligence (Books)

    The second category is quite an interesting one. I''m curious how it ended up
    there? :slightly_smiling_face:

    Do you use Minecraft as one of the examples?'
  replies:
  - name: Phil Winder
    text: "Haha. Yeah I saw that too. Hilarious.\nThe US metrics are more stable,\
      \ because there\u2019s been more sales there.\nBut yeah, Minecraft. Someone\
      \ needs to do some NLP consulting to Amazon to fix their broken catagorisation\
      \ algorithm!"
  - name: Phil Winder
    text: "I\u2019ve just grepped the book and I never mention the word minecraft.\
      \ So I can only assume that there is some overlap in embedding-space between\
      \ my content and other minecraft books."
  - name: Ritobrata Ghosh
    text: 'No, Amazon should never fix it. Think about it. You get to brag about writing
      a bestselling book about Minecraft! :wink:'
  - name: Phil Winder
    text: "Hahaha. Yay!  :joy:  Can you imagine\u2026\nMedia person: \u201C\u2026\
      \ and here to talk about minecraft is bestselling author\u2026\u201D\nMe: \u201C\
      errrm\u2026. blocks and stuff?\u201D"
  - name: Ritobrata Ghosh
    text: Just bragging rights to teenagers! Don't go deep into it, or you'd be caught!
- name: Ritobrata Ghosh
  text: Phil Winder, in your opinion, what factors have prevented the wide adoption
    of Reinforcement Learning in the industry as opposed to Machine Learning and to
    some extent, Deep Learning as academic fields widely adopted in the industry?
  replies:
  - name: Phil Winder
    text: "Hi Ritobrata,\nGood question. Probably just a combination of time, media\
      \ exposure, market size, processing power, low-hanging fruit.\nYou say\n&gt;\
      \ ML widely adopted in the industry.\nBut statistics, and therefore ML, has\
      \ existed forever. Only recently (i.e. a decade, maybe) has ML \u201Ctaken off\u201D\
      . So you could argue that it took 200 years for ML to be adopted.\nRL originated\
      \ around the 90's, so wait until 2290, then ask your question again. :smile:\n\
      So the real answer is market size and perception. It goes like this:\nIT -&gt;\
      \ Software -&gt; ML -&gt; DL -&gt; RL.\nBecause they are applied by/for:\nEveryone\
      \ -&gt; Companies -&gt; One-shot decisions -&gt; Complex decisions -&gt; Strategic/long-term\
      \ decisions.\nEach time you\u2019re reducing the market size. And when you do\
      \ that you are reducing media exposure. So it might seem like ML has been adopted\
      \ and RL hasn\u2019t, but in fact the market is just smaller. When normalised\
      \ the perceived adoption is the same.\nWith that said, I do think you\u2019\
      re right, it\u2019s not been adopted yet. Mainly because there\u2019s a lack\
      \ of books like mine and well defined use cases. We\u2019ll get there\u2026"
  - name: Ritobrata Ghosh
    text: 'Thanks for the detailed answer. :slightly_smiling_face:'
- name: Leonid Kholkine
  text: Phil Winder A bit more of a generic question, but how do you see the field
    of RL fold out in the next 3-5 years?
  replies:
  - name: Phil Winder
    text: "The correct answer to this is probably more boring than you were hoping\
      \ for.\nIt will expand, it will get used more. It will become easier to use\
      \ and will become more obvious where to use it (because you can use off the\
      \ shelf open-source solutions).\nThen RLOps will become a thing.\nThen people\
      \ will perceive it as being \u201Cadopted\u201D.\nThen something else will take\
      \ the limelight.\nIf I put my marketing hat on it would sound similar except\
      \ with more hyperbole! :smile:"
- name: Timothy Wolodzko
  text: Phil Winder RL is still niche of ML, there's much less books &amp; courses
    on it as compared to general ML. Besides your book, what would you suggest for
    someone interested in learning it? Where to start? What on focus first? Moreover,
    I have a feeling that online you can find either trivial examples, or the very
    complicated applications like AlphaGo, with not much intermediate ones. So any
    suggestions for planning the learning journey further?
  replies:
  - name: Phil Winder
    text: "It\u2019s the same as anything technical IMO. There is stuff to be learnt,\
      \ and you can do that by reading. Read all the books and papers you can.\nBut\
      \ the real learning experience is\u2026 experience. Do it for real. Do it in\
      \ your company. Do it at work. Then and only then do you learn what you need\
      \ to learn to do your job.\nYeah, that\u2019s the point. Doing your job is nothing\
      \ like anybody else\u2019s job. I could tell you to do certain projects but\
      \ it wouldn\u2019t make sense for your unique situation. Your first challenge\
      \ is finding a problem that is valuable and makes sense for RL. Then work on\
      \ that. Start simple. Start with software, then ML, then RL. Work your way up.\n\
      What you need is a RL driven learning curriculum that delivers training that\
      \ suits your unique needs. :smile:"
  - name: Alexey Grigorev
    text: Can one use RL to come up with the best curriculum to study it?
  - name: Alexey Grigorev
    text: 'Sounds like a good project :sweat_smile:'
  - name: Ritobrata Ghosh
    text: Timothy Wolodzko, the author has answered. I would like to add a few things.
      You could try University of Alberta's RL Specialization in Coursera, and definitely
      read the Sutton, Barto's book. I highly recommend David Silver's Lectures. There
      are other lectures from DeepMind as well. There's Spinning Up from OpenAI. You
      could also read Thomas Simonini's indroductory RL blogs. There's plethora of
      beginners' and intermediate stuff out there for RL, not as much as DL and ML,
      but enough for an individual to learn.
  - name: Timothy Wolodzko
    text: Ritobrata Ghosh &amp; Phil Winder thanks! I already have some of those books
      etc, just wanted to learn if there's anything more I should look for.
  - name: Vladimir Finkelshtein
    text: "I think one obstacle for learning is the lack of plug and play libraries\
      \ like for more classical ML. Even with openai.gym, some of the recent books\
      \ have code that doesn\u2019t compile, because the libraries are still being\
      \ developed and change too often. It is certainly an obstacle for people who\
      \ are less experienced in programming."
  - name: Phil Winder
    text: "Hi Vladimir Finkelshtein,\nAlthough I have seen people/companies try to\
      \ do data science without software experience/capabilities, I would recommend\
      \ that gaining software engineering experience is as important as ML/RL experience.\n\
      Software is the language of applications, so if you want to build useable ML/RL,\
      \ you need software. Of course this doesn\u2019t apply to everything. E.g. you\
      \ can just about get by with hosted tools for an analytics project and larger\
      \ companies can hire multiple people with different skils (this is the general\
      \ solution, by the way). But sooner or later you\u2019ll need to code :slightly_smiling_face:\n\
      I have sympathy for your despair, however. I think the main issue is the complexity.\
      \ Any complex system has a million ways to fail and it sounds like you\u2019\
      ve found most of them. :slightly_smiling_face:"
- name: Ashutosh Sanzgiri
  text: Phil Winder Do you think that the field needs a new name or branding? Maybe
    the word "reinforcement" is not catchy enough or does not have the right connotations?
    Also when do you think we will start seeing "self-help" apps (weight loss etc.)
    that claim to be powered by RL?
  replies:
  - name: Phil Winder
    text: "Not necessarily a new name, no. But I would like to see RL become more\
      \ mainstream in the ML toolbox.\nI\u2019d like to be at the point where people\
      \ say (at the most general level) \u201Cwe\u2019re working on a data project\
      \ and we might need to dip into our toolbox, rummage around, and we might need\
      \ to pick RL for the job\u201D."
  - name: Phil Winder
    text: "And the term RL represents quite a small spectrum of techniques. You could\
      \ use the words for all the sub-techniques too if you want to be more specific\
      \ (e.g. imitation RL, inverse RL, curriculum RL, etc. etc.).\n\u201CClaims\u201D\
      \ are powered by marketing/advertising. So that\u2019s entirely powered by marketing.\n\
      I\u2019d suspect at some point someone in marketing will hear the term, go \u201C\
      oh that\u2019s cool, is that like AI?\u201D and then they\u2019ll run with it.\
      \ \u201CThe first app to use RL\u2026\u201D\nThen there will be a domino effect,\
      \ then users will get confused annoyed, and then people will stop using it again\
      \ and move on to the next thing.\nThis is why I tend to try to avoid predicting\
      \ marketing hype cycles. They are so fickle. The core technologies and concepts\
      \ are useful in certain applications and that is why it will stick around for\
      \ a long time."
- name: George Melvin
  text: "Phil Winder Hi Phil, Pavlov\u2019s famous experiments (:bell:) are a great\
    \ example of reinforcement learning for non-machines. I\u2019m interested to know:\
    \ do you foresee any interplay between reinforcement learning for biological/machine\
    \ entities in the future? e.g. do you expect to see research insights from (machine)\
    \ reinforcement learning having application in psychology, and vice-versa?"
  replies:
  - name: Phil Winder
    text: "Great question. I think the answer depends on how deep you want to go.\n\
      At a superficial level, yes, definitely, health apps in particular. RL driven,\
      \ personalised nudges to help you loose weight, get fit, learn a new subjects,\
      \ etc. are an obvious use case.\nAt a slightly deeper level, the introduction\
      \ of RL in core front-line healthcare, like personalised medicine, shows strong\
      \ signs.\nBut at the full-on I\u2019ve-had-too-many-beers-deep level, you could\
      \ imagine RL providing \u201Clife\u201D strategies. Like a personalised, optimal\
      \ route to getting a job that you want. Or \u201Cautomated relationships\u201D\
      .\nHaha. I need that. Imagine not having to remember anniversaries, the perfect\
      \ present automatically ordered."
  - name: Phil Winder
    text: "And in pshychological wellness. Yes, definitely.\n\u201CHi Dave, you look\
      \ sad Dave.\u201D"
  - name: Phil Winder
    text: '[https://media.giphy.com/media/11wzSz5pm4WktW/giphy.gif](https://media.giphy.com/media/11wzSz5pm4WktW/giphy.gif)'
  - name: Phil Winder
    text: "TIL there\u2019s a poor selection of Red Dwarf gifs available on the internet\u2026"
---

Reinforcement learning (RL) will deliver one of the biggest breakthroughs in AI over the next decade,
enabling algorithms to learn from their environment to achieve arbitrary goals. This exciting development
avoids constraints found in traditional machine learning (ML) algorithms. This practical book shows data
science and AI professionals how to learn by reinforcement and enable a machine to learn by itself.


