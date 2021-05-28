---
title: "Grokking Deep Reinforcement Learning"
description: "Book of the Week. Grokking Deep Reinforcement Learning by Miguel Morales"
cover: "images/books/20210517-grokking-deep-reinforcement-learning/cover.jpg"
image: "images/books/20210517-grokking-deep-reinforcement-learning/preview.jpg"
start: 2021-05-17 00:00:00
end: 2021-05-21 22:59:58
authors: [miguelmorales]
links: 
  - text: Book's page
    link: https://www.manning.com/books/grokking-deep-reinforcement-learning
  - text: Book's GitHub repository
    link: https://github.com/mimoralea/gdrl

archive:
- name: Tino
  text: Miguel Morales Thanks for taking the time! Where do you expect to have RL
    the biggest impact in industry in the next few years? And is there any specific
    use case for finance where you think this could be a game changer (keeping regulations,
    explainability, etc. in mind)?
  replies:
  - name: Miguel Morales
    text: Hi, Tino. Thanks for the question. I think RL will continue to have an impact
      on several industries in the next few years. I'm not too familiar with finance,
      but I know there are lots of R&amp;D investments that involve RL (and AI in
      general). I'm more familiar with the military industry, and my guess is other
      industries see AI/ML/RL as critical technologies of the future, along with 5G
      and Quantum.
- name: Wendy Mak
  text: hi Miguel Morales do you think there are ML problems where we are currently
    using supervised learning that could potentially be solved better using reinforcement
    learning?
  replies:
  - name: Miguel Morales
    text: 'Hi, Wendy Mak. Thank you for the questions. I think, in general, supervised
      learning is commonly used to make better decisions. That''s true for classification
      and regression. Are you working on models that classify traffic signs? Are you
      working on models that predict stock prices? Usually, the real need behind those
      is better decision making--self-driving cars, automatic trading, etc.

      The question is whether RL is ready to take over the decisions of those models.
      And, the answer to this is, it depends. It depends on whether you can create
      a simulation for the AIs to learn, it depends on the number of people working
      on the project, and whether you''ll be able to work on techniques such as transfer
      learning, it depends.

      The way I see it, many ML problems can be transformed into RL problems to let
      the decision model learn features used for decision making directly, as opposed
      to having the model learn features for prediction of a proxy objective, which
      will be the classification/regression objective in a decision-making problem,
      which may bias the model.'
  - name: Grzegorz Sajko
    text: 'Kind of follow up:

      Are there tools for "RL production ready" at this moment? to enable this trasformation
      from ML to RL?'
  - name: Miguel Morales
    text: Hi, Grzegorz Sajko. Thanks for the question. I think RLlib is a pretty good
      starting point. But, I don't think there are any tools to convert an ML problem
      into RL smoothly.
- name: Wendy Mak
  text: Also, do you have any tips on how to tune/select decent hyperparameters for
    RL algorithms?
  replies:
  - name: Miguel Morales
    text: 'Yeah, I think using Grid search first to find approximately good hyperparameters
      and then Random search to fine-tune the best set is an excellent practical strategy
      for tuning RL algorithms. Also, there are more advanced methods and can be helpful:
      population-based training is a good one, for instance.'
- name: Saulius Lukauskas
  text: "Hi Miguel Morales - a bit of a semi-serious and philosophical question to\
    \ you, but when I think about deep RL I always think about this xkcd comic [https://xkcd.com/720/](https://xkcd.com/720/)\
    \ in which humans are providing feedback to RL algorithm about the recipes it\
    \ is generating. In the comic the data scientist announces that in a few hundred\
    \ more iterations, the food might actually start tasting good. I think this is\
    \ a fun  analogy to reinforcement learning. But this comic is quite old - with\
    \ the recent advances in methods, data, and the Moore\u2019s law, do you think\
    \ this comic is still accurate ? what would teaching computers to \u201Ccook\u201D\
    \ with reinforcement learning look like today? Would we still need hundreds of\
    \ iterations before something is edible ?"
  replies:
  - name: Miguel Morales
    text: 'Hi, Saulius Lukauskas. Thanks for the question. Funny one! Yes, unfortunately,
      RL still looks like this if you think of training from scratch, but there are
      several strategies for reducing sample complexity, too. It all begins with the
      type of RL methods that you select. For instance, a technique called "deep neuroevolution,"
      related to genetic algorithms, has very high sample complexity. While those
      techniques are okay to use, if you have a simulation and lots of computing,
      I wouldn''t train it in the real world. On the other side of the spectrum of
      sample complexity, we have the family of model-based RL methods. These methods
      are commonly used to train robots in the real world. These methods need fewer
      samples to come up with a solution. But of course, everything has pros and cons,
      and with these methods, wall-clock time may be affected.

      But, then, you get into techniques such as transfer learning, multi-task learning,
      and even a more recent, causal RL. I think researchers are aware of the problem
      the xkcd illustrates and have been prioritizing it.'
- name: David Cox
  text: "Very excited to see this book come through the book-of-the-week channel!!\
    \ I have a bit of a framing question. Let\u2019s say we\u2019re not interested\
    \ in identifying the optimal solution a system should take in a situation. Rather,\
    \ we\u2019re interested in training an artificial agent to imitate/mimic/behave\
    \ like a biological system (who often behave suboptimally). Let\u2019s say we\
    \ have a bunch of data on the environment, the response options, the choice the\
    \ biological organism makes, and what environmental changes happen as a result\
    \ of their choice. How would you setup the RL system to learn to imitate that\
    \ biological organism?"
  replies:
  - name: Miguel Morales
    text: Hi, David Cox. Thanks for the question! This question is interesting and
      related to behavioral cloning, inverse RL, and imitation learning. The critical
      distinction is that many of these methods assume optimal behavior, which may
      be a limitation. However, that's not the case for other algorithms, such as
      DAgger (Dataset Aggregation), in which the goal is the clone the behavior of
      another agent, whether it is optimal or not. Overall, behavioral cloning is
      related to RL in some contexts, but more so to supervised learning. You are
      trying to predict the action given a data set of behavior. Yet, it is not supervised
      learning directly because the data is not i.i.d. (independent and identically
      distributed), so many of the assumptions of the optimization algorithms no longer
      hold, and we need different methods to solve the problem. The field you are
      looking for, though, is imitation learning. I would start there!
  - name: David Cox
    text: Thanks, Miguel Morales! This is extremely helpful!! Any offhand recommendations
      on researchers or authors who are particularly good in this area?
  - name: Miguel Morales
    text: Yeah, I like the work of Sergey Levine, Chelsea Finn, Pieter Abbeel, and
      Andrew Ng. Of course, they do a lot more than just imitation learning. But they
      have also done lots of good work in imitation learning and inverse RL.
  - name: David Cox
    text: Great! Thank you!!
- name: Matthew Emerick
  text: 'Thanks, Miguel Morales, for doing this!

    What prerequisites do we need before reading your book?'
  replies:
  - name: Miguel Morales
    text: Hi, Matthew Emerick. Thank you for the questions. I think a background in
      supervised learning methods is sufficient. Have you trained a couple of NN just
      following the TensorFlow, or PyTorch tutorial? Then, that's sufficient. If not,
      it should take an hour or so to review. After that, I'm not assuming any RL
      background. So everything moves from the perspective of RL, then to DeepRL.
- name: Vladimir Finkelshtein
  text: 'We always hear about successes of reinforcement learning: chess, go, robo-dogs,
    robotic arms solving rubic cubes and so on. What are some examples of tasks which
    intuitively RL should tackle, but it fails to do so?'
  replies:
  - name: Miguel Morales
    text: 'Hi, Vladimir Finkelshtein. Thanks for the question. Hard to answer because
      you use the word "intuitively," and that can make it subjective. If you understand
      what RL does, it becomes intuitive to use it and what to expect. Surprisingly,
      some folks don''t think so. For instance, when RL methods mine rewards in a
      loop, instead of playing a game the way a human plays. Why would the human expect
      the agent to learn to play like a human if the objective is not that?! But,
      interestingly, many folks argue that''s a problem with RL.

      Now, to answer something related to your question (removing the word "intuitively"),
      RL should work better at learning a hierarchy of policies. So, that one policy
      learns to fly an airplane, another learns the tactics of a dogfight, another
      learns to command multiple platforms, another one an entire campaign. RL should
      be better at understanding the causal relationships in data; although that is
      a problem with machine learning overall, RL methods would benefit from it. Also,
      the fact that an agent trained to perform at a superhuman level in Breakout
      (Atari) doesn''t do well at all in Pong (Atari) is a clear issue. You would
      have to train a new model from scratch with Pong. So, multi-task learning is
      another area where RL methods should be better.'
- name: Matthew Emerick
  text: What resources do you recommend to follow up after your book to go even deeper?
  replies:
  - name: Miguel Morales
    text: Oh, I have too many, but to focus, I think Berkeley's course is great. [http://rail.eecs.berkeley.edu/deeprlcourse/](http://rail.eecs.berkeley.edu/deeprlcourse/)
  - name: DevJac
    text: I think Grokking Deep RL is the best first book, best I've found. It does
      a good job at introducing the notation common in reinforcement learning. [http://incompleteideas.net/book/the-book.html](http://incompleteideas.net/book/the-book.html)
      is a famous book in the RL field, and it's much less intimidating after having
      read Miguel's book, so perhaps that is a good second book on the subject, or
      at least skim through it.
- name: Matthew Emerick
  text: Where do you see reinforcement learning going in the next five to ten yers?
  replies:
  - name: Miguel Morales
    text: I think Causal RL is something to keep an eye on. Also, the use of RL with
      other methods, such as Unsupervised Learning methods and auxiliary tasks. Meta-learning
      is another area with a lot of potential, though I see that more long-term, but
      we'll see!
- name: Bayram Kapti
  text: Hi Miguel Morales, what are some critical advantages and disadvantages of
    applying Deep RL vs just a sampling algorithm such as Thompson Sampling for RL
    purposes?
  replies:
  - name: Miguel Morales
    text: Hi, Bayram Kapti. Thanks for the question. I think the main different is
      the sequential nature of RL. Thompson Sampling is commonly use for selecting
      actions under an environment with a single state (often called multi-armed bandits).
      That's a single state and multiple actions (arms). RL and DRL is about learning
      in environments with multiple, even infinite states. However, some of the same
      action-selection techniques of Thompson Sampling can be ported and use in a
      RL context. So, I would say it is not this or that, it could be this and that.
  - name: Bayram Kapti
    text: 'Thank you for the answer Miguel Morales !

      Does your book cover both or does it focuses on DRL?'
  - name: Miguel Morales
    text: Of course! It covers Thompson Sampling on a small section of the chapter
      related to multi-armed bandits and the exploration vs. exploitation tradeoff.
      But the book covers many other things related to DeepRL, and it doesn't go too
      deep on Thompson Sampling.
  - name: Bayram Kapti
    text: Got it thanks!
- name: Glenn
  text: Hi Miguel, congrats on your book! Can you tell us anything about the exercises
    in the book and how you came up with them?
  replies:
  - name: Miguel Morales
    text: Hi, Glenn. Thanks! And, thanks for the question. Yes. It wasn't that difficult.
      I've been teaching a reinforcement learning course at Georgia Tech for a few
      years now, and some of these are ideas that I think would help folks 'grok'
      deep RL. Lots of the students I've had over the years have had related questions,
      so as I was reviewing a chapter, I would write the exercises. Some of the exercises
      are related to "gotchas" in the practical sense (when implementing an algorithm).
      I think they are not as important, given algorithms come and go, and frameworks
      change almost daily, but exciting things may help folks get a complete picture.
- name: Bayram Kapti
  text: "Miguel Morales , I saw you mentioned that you\u2019re more familiar with\
    \ Military applications of RL. I\u2019ve watched the AI win the dogfights against\
    \ a USAF fighter pilot. Do you have any participation in the development of those\
    \ AI systems?"
  replies:
  - name: Miguel Morales
    text: I've worked with that LM team, and I've also worked with the winning team
      (Heron Systems). However, I did not participate in that release of the project.
      My involvement began after those results were published.
  - name: Bayram Kapti
    text: "That\u2019s so cool. I used to fly with USAF. That was so interesting for\
      \ me. A little bit sad though. I wanted the human beat the AI :) a little biased\
      \ :)"
  - name: Miguel Morales
    text: Oh cool! Haha, well have in mind the AI had perfect knowledge of the environment.
      I think without that the results would have been different. The human only has
      a "perspective," and it needs to look around and find the bandit, so it was
      a bit unfair. But, there is work being done to improve those results.
  - name: Bayram Kapti
    text: "Haha, That\u2019s absolutely true :) Overall, so much fun for me, both\
      \ aviation and AI fan!"
- name: DevJac
  text: 'Miguel Morales I read your book some time ago and really enjoyed it. I joined
    the group to ask this question: I''ve noticed that in PPO and a few other actor-critic
    algorithms (or, what I would call "actor-critic-ish", having a policy function
    and a value function) that the critic / value function is trained after the policy.
    For example, see: [https://spinningup.openai.com/en/latest/algorithms/ppo.html#pseudocode](https://spinningup.openai.com/en/latest/algorithms/ppo.html#pseudocode)
    -- Do you know why this is? By my own non-scientific observations, I think things
    sometimes do better when training the critic before the policy. Do you have any
    thoughts on what order is best? Do you know why the literature often shows the
    critic trained after the policy?'
  replies:
  - name: Miguel Morales
    text: 'Hey, DevJac. Thanks for the question--a fascinating observation you make!

      I''m not sure 100%, but I think it has to do with on-policy vs. off-policy learning,
      and of course, the implementation. In on-policy learning, the critic evaluates
      the policy, assuming that policy will continue to run in the environment. The
      policy generating the data and the policy being trained are the same. In off-policy
      learning, the critic is evaluating the policy, assuming optimal behavior after
      that. And, because we don''t have an optimal policy, those are different policies.
      So, you can train off-policy actor-critic methods the other way (first the critic,
      then the policy).

      Papers, in general, follow this pattern. If you see A3C, PPO, PPG, they all
      have policy phases first, then critic phases. If you check DDPG, TD3, SAC, they
      all train the critic first.

      Again, I''m not 100% certain, but that is my first guess. Excellent observation,
      BTW! Let me know if you find more info.'
- name: Rona Ainslie
  text: Hi, I'm going to preface with the fact that I don't know a lot about RL. I
    have been hearing and reading a lot recently about the need for explainability
    and trust in AI and machine learning- how does RL fit in to this? Is it possible
    to understand how the decisions are made, and how does that affect the ways you
    think its best to use RL?
  replies:
  - name: Miguel Morales
    text: 'Hi, Rona Ainslie. Thank you for the question. There is a field called Explainable
      Reinforcement Learning that is focused on making Reinforcement Learning more
      explainable. What that means is we (all humans: users, developers, researchers,
      and stakeholders) need to be able to understand the decision made by an algorithm.
      We also need to trust the decision-making system, and in RL (and ML/AI in general),
      currently, a slight change of a training seed may yield significant discrepancies
      in training results. We''re far, and there''s lots of work to be done here.

      To answer your question more directly, RL also needs explainability. The main
      difference when you hear "Explainable AI" vs. "Explainable RL" is the former
      subsumes the latter. In "Explainable AI," as introduced by DARPA, there are
      two tracks, a "Data Analytics" (Supervised Learning for the most part) and an
      "Autonomy" (Reinforcement Learning for the most part). Folks who focus on that
      second track, the Autonomy track, are studying "Explainable RL."

      At the moment, there are ways to understand how decisions are made, but I would
      argue that those are not yet user-friendly. I think lots of researchers continue
      to work on their narrow RL problems, hoping that researchers working in Explainable
      RL can come up with solutions to those problems. Later in the future, we can
      merge paths to deploy explainable solutions. I think having explainable models
      is a blocking issue before we can release AI to several industries, including
      mine, of course.'
  - name: Rona Ainslie
    text: Thank you Miguel Morales Lots of interesting points (and I'm off to google
      DARPA explainable AI)! Do you think that explainable RL is a field that is being
      taken seriously? That is, in your experience is there enough money going in
      to the research yet?
  - name: Miguel Morales
    text: 'It obviously depends on the field, but if you think about it, DARPA, being
      a government institution, cares about explainability. Why is explainability
      important to the government and the military? Are those reasons likely to continue
      there?

      I think money is going to continue to flow into it for sure.'
  - name: Rona Ainslie
    text: Thank you!
- name: John Savage
  text: 'In applied machine learning it''s recommended to incrementally add complexity
    to your system until you reach good enough performance e.g. heuristics -&gt; logistic
    regression -&gt; xgboost -&gt; e2e deep learning. This allows you to understand
    your problem domain better and prevents wasted engineering/science effort.

    Are there similar pathways for RL where we can get the majority of the benefit
    out of e.g. a very simple optimisation or bandits before having to go full deep
    RL. What are the tools/methodologies you''d recommend getting projects started
    with?'
  replies:
  - name: Miguel Morales
    text: 'Hey, John Savage. This is an excellent question. I think the same idea
      applies, but a bit differently. In RL, there is an environment and an agent.
      Usually, the environment is given, and researchers concentrate on the agent.
      However, in an engineering sense, you likely don''t care about Atari games.
      You care about your problem. So, one of the main challenges in RL is finding
      an environment to train your agent, or better yet, creating one yourself. What
      simulation engine are you using? Will you use the real world for training? Will
      the agent be able to collect enough data? Will you use a sample efficient algorithm
      for training? Etc.

      My recommendation here is to spend time implementing an environment, use off-the-shelf
      algorithms first, and make your environment look like the environment those
      algorithms are tune for solving. Once you iterate a few times over your environment,
      then start changing the agents, models, and training schemes, then go back to
      the environment and polish once again. Lots of folks want to solve everything
      at once and trust me, RL is challenging. So, isolating the problem is the way
      to go.'
  - name: John Savage
    text: That's a great insight, thanks a lot, makes a bunch of sense.
- name: Tim Becker
  text: 'Hi Miguel,

    I started looking into RL and your books looks like a great asset! I would like
    to ask you couple of questions concerning the book and the general topic:

    - Do you have any recommendations for projects to work on alongside your book?
    I implemented some algorithms for the cart-pole environment from the OpenAIGym
    package and everything seemed to work, but when I moved to more complex environments
    my agents did not perform. I was wondering if you have recommendations that are
    more complex than the cart-pole problem, but still do-able for starters.

    - In the introductory chapter of your book, you mention that the book focuses
    on algorithms and not on environments or modeling problems. In my attempts, I
    found it very difficult to find a good description of the current state and to
    assign useful rewards. I assume this is part of the modeling problem. Do you have
    any recommendation on how to best do this?

    - To compare different policies, would you compare estimates of the value function?

    - In your experience, where and how would you start to debug if your model is
    not learning anything?

    - I read in another book that DRL is currently sill very hard, especially to get
    consistent high-quality results and that you usually have to tune the hyperparameters
    quite a lot and often you also need a little bit of luck. Would you agree to this
    statement?'
  replies:
  - name: Miguel Morales
    text: 'Hi, Tim Becker. Thanks for the questions!

      - Yeah. The LunarLander environment is a bit more complex (8 variables for observation,
      4 for action). You also have a Lunar Lander continuous with continuous variables
      for the action space. I recommend staying away from image-based environments
      until you have solved a couple of other environments with the same implementation.
      The problem with image-based environments is the feature extraction process
      can take quite a bit of time without the proper equipment (and even with the
      right equipment, it takes much longer than non-image-based environments.)

      - Unfortunately, this is a challenging problem, usually left out because it
      is not as "researchy" but more of an engineering problem. However, for most
      folks, this is really where the money goes. You may not be able to invent a
      new RL algorithm, and maybe you''re not even interested in that. Instead, you
      may want to use one of the available algorithms and train them to solve your
      problem. Modeling problems (as you say: "assigning useful rewards") is essential,
      and someone should spend some time creating a book or some content that explains
      how to do that. Sadly, I don''t have any recommendations at the moment, only
      to study how MDPs work (chapter 2) and try to replicate, add complexity. Feel
      free to explore how others do it. Look for `gym &lt;search term&gt; environment`
      and dig into codebases (e.g. atari-py, mujuco-py, hfo-py, etc.)

      - To compare policies in practice, you would evaluate them in environments under
      similar conditions with several random seeds. Capture the mean total return
      (sum of rewards from the initial state to the end of the episode, averaged x
      times, over n seeds), and go from there. You can monitor the accuracy of a value
      function by comparing the estimates to the actual returns. But on a policy-to-policy
      comparison, I commonly use the sum of rewards.

      - This is sooo challenging. What I always try to do is to simplify the problem.
      As opposed to debugging a complex system, simplify the solution. Train against
      a simpler environment. Use standard hyperparameters for the type of environment
      that you''re using. RL is very challenging to debug because a single typo can
      break things. And, what is probably worse in my opining, an implementation with
      a bug can "work" under certain conditions. That''s cruel, let me tell ya! :)

      - I somewhat agree. Many folks attribute their incompetence to RL and use the
      phrase: "RL is hard" to excuse themselves. Yes, I believe RL is challenging,
      but more often than not, it is not working due to user error. When you look
      at implementations available online many out there are flat-out wrong (including
      in books, BTW--sadly). But, if you start small and build up, then it is not
      that bad. You need tenacity and focus, but you''ll have so much fun! Hyperparameter
      tuning is not that bad once you learn what parameters work for certain kinds
      of environments. I recommend using a hyperparameter tuning framework and trying
      a random search. RLlib and tune are excellent starting points.

      Thanks for the great questions. I didn''t do justice to them, but it hopefully
      helps!'
  - name: Tim Becker
    text: "Thank you Miguel! This helps a lot! As you expected, I was looking at image-based\
      \ environments that gave me headaches. The LunarLander sound like fun \U0001F642\
      \ I will give it a try."

---

We all learn through trial and error. We avoid the things that cause us to experience
pain and failure. We embrace and build on the things that give us reward and success.
This common pattern is the foundation of deep reinforcement learning: building machine
learning systems that explore and learn based on the responses of the environment.

Grokking Deep Reinforcement Learning introduces this powerful machine learning approach,
using examples, illustrations, exercises, and crystal-clear teaching. You'll love the
perfectly paced teaching and the clever, engaging writing style as you dig into this
awesome exploration of reinforcement learning fundamentals, effective deep learning
techniques, and practical applications in this emerging field.