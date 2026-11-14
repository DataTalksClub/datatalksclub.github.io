---
episode: 8
season: 25
guests:
- migueloteropedrido
ids:
  youtube: xC5lqvfSfLU
links:
  spotify: https://open.spotify.com/episode/5J8royMpnXL43xtJ9y87qA
  youtube: https://www.youtube.com/watch?v=xC5lqvfSfLU
short: Navigating the Maze of Production Machine Learning
title: Navigating the Maze of Production Machine Learning
description: 'Miguel Otero Pedrido discusses why traditional ML still matters, building recommender systems, LLMs in recommenders, AI gateways and evaluating agent traces.'
transcript:
- header: "Miguel’s path from physics to production ML"
- line: |-
    I'm interested in why we should care about production machine learning when
    everyone is talking about AI. Should we even care about it? That's one thing
    I plan to ask.

    We'll talk about interesting things related to this topic. You've probably
    seen Miguel on LinkedIn.
  sec: 10
  time: "0:10"
  who: Alexey
- line: |-
    That's how I regularly see him, always wearing headphones, including today.
    He's an ML/AI engineer who learns and teaches by building. He went from
    studying spacetime curvature and quantum field theory—it's difficult even to
    articulate, which reflects the complexity of the subject—
  sec: 32
  time: "0:32"
  who: Alexey
- line: |-
    to creating real-world ML systems, from fashion recommendation engines to
    complex agentic workflows for insurance companies. I already have a
    question: doesn't that feel like downshifting?
  sec: 57
  time: "0:57"
  who: Alexey
- line: |-
    It's different. Maybe mathematically it's a downshift, but in terms of
    contact with reality, it feels like an upgrade. I love physics; that's why I
    studied it.

    But things change when you get into research. I was researching gravitation,
    spacetime curvature and quantum field theory.
  sec: 70
  time: "1:10"
  who: Miguel
- line: |-
    They're beautiful theories if you enjoy the mathematics behind them. I
    wouldn't call this a downshift. Now I have the pleasure of building systems
    that affect thousands, tens of thousands or even millions of people at the
    companies I work for.

    That's a good feeling in a different sense. Before, I was learning,
    understanding or developing theories, but it felt different.
  sec: 112
  time: "1:52"
  who: Miguel
- line: |-
    They're very different worlds. Mathematics was helpful when I started in
    this field, but also a big disadvantage. You tend to focus on the
    mathematics behind models and algorithms and forget about solving the actual
    problem.
  sec: 148
  time: "2:28"
  who: Miguel
- line: |-
    I was guilty of that too, because the theory is interesting. I remember
    learning support vector machines; they have a beautiful foundation. Did you
    find that nobody really cares about support vector machines?
  sec: 172
  time: "2:52"
  who: Alexey
- line: |-
    Absolutely. I relate to that because it happened to me. When I started with
    random forests and XGBoost, I wanted to dive into each algorithm's
    mathematical foundations.

    Ten years ago, you wanted to find a problem where you could apply SVMs or
    neural networks. Then the numbers and evaluations told you a simple linear
    regression was enough.
  sec: 184
  time: "3:04"
  who: Miguel
- line: |-
    It was a huge disappointment, and you tried to justify using more complex
    mathematical models. I relate to that experience and feeling.
  sec: 224
  time: "3:44"
  who: Miguel
- line: |-
    You went from physics to machine learning. What do you do now, and what is
    The Neural Maze?
  sec: 235
  time: "3:55"
  who: Alexey
- line: |-
    I have two jobs. During the day I'm a machine learning engineer, but
    increasingly an AI engineer. I work for Zapier, a company focused on
    automations and workflows, which is evolving into an AI-first company.
  sec: 241
  time: "4:01"
  who: Miguel
- line: |-
    I've used Zapier for quite some time. It's very simple.
  sec: 270
  time: "4:30"
  who: Alexey
- line: |-
    That's what we try to achieve. With the AI features we're adding, we hope to
    make it even simpler. I'm on Zapier's AI platform team, behind the AI
    functionality and features appearing progressively in the product.

    That's my first job. The second is The Neural Maze, an educational brand I
    created two years ago.
  sec: 276
  time: "4:36"
  who: Miguel
- line: |-
    Through The Neural Maze, on YouTube, primarily on LinkedIn, and on Substack,
    where I have a newsletter, I teach AI. I teach production AI that tutorials,
    videos and courses often skip. I try to distill what I've learned from ten
    years deploying AI systems to production, from machine learning to agentic
    systems and many other systems.

    I want to give subscribers and the community knowledge I don't often see in
    tutorials.
  sec: 306
  time: "5:06"
  who: Miguel
- line: |-
    I found your YouTube channel and shared it in the live chat. I also linked
    it in the title. If you're interested, please subscribe.

    As a fellow educator and teacher, I really like this path.
  sec: 350
  time: "5:50"
  who: Alexey
- line: |-
    You do something during the day, then share everything you learn with
    people. How do you find time for it?
  sec: 379
  time: "6:19"
  who: Alexey
- line: |-
    It's been a rough two years, honestly. I guess at some point I'll need to
    make a final decision.
  sec: 394
  time: "6:34"
  who: Miguel
- line: |-
    I did that three and a half years ago. I think it’s more now.
  sec: 401
  time: "6:41"
  who: Alexey
- line: |-
    Even with AI, agents and the promise of productivity, a personal brand still
    needs a human being. That’s why I can’t multiply myself yet.
  sec: 405
  time: "6:45"
  who: Miguel
- line: |-
    That's the problem with time. I work a lot, and I hope in the coming years I
    can reduce the workload a little.
  sec: 420
  time: "7:00"
  who: Miguel
- header: "Why traditional machine learning still matters"
- line: |-
    Agents are certainly helpful. My first question about production ML systems
    is: why should we care about ML when everything is generative AI? You throw
    a problem at AI and it figures it out.

    Why care about machine learning these days?
  sec: 445
  time: "7:25"
  who: Alexey
- line: |-
    Sometimes, when we learn a new tool or technique, we overestimate its
    capabilities. AI and agents are amazing tools that solve many use cases. But
    many problems could be solved by traditional machine learning algorithms at
    a lower cost.

    Recommender systems are a good example.
  sec: 461
  time: "7:41"
  who: Miguel
- line: |-
    I've worked on recommender systems for five or six years. Some teams default
    to agents or give recommendations to an LLM system. But when you compare
    benchmarks, simple matrix factorization or a learning-to-rank algorithm
    using gradient-boosted trees can outperform LLMs.

    You also get determinism that you don't get with agents and LLMs, although
    models such as Jev can now achieve something similar.
  sec: 495
  time: "8:15"
  who: Miguel
- line: |-
    Sometimes I think Jev is amazing because it provides zero hallucinations and
    probabilities for each category. But we also got that from logistic
    regression or random forests.
  sec: 547
  time: "9:07"
  who: Miguel
- line: |-
    I was surprised by the attention Jev got. I thought, 'Wait, it's just a
    classifier.'
  sec: 566
  time: "9:26"
  who: Alexey
- line: |-
    That's my point too. It's amazing they're getting this through a new
    reinforcement-learning approach. People are amazed you can use Jev as a
    router instead of an LLM.

    You could do the same with a random forest or another classifier. It's funny
    how we rediscover these things.
  sec: 573
  time: "9:33"
  who: Miguel
- line: |-
    Exactly.
  sec: 601
  time: "10:01"
  who: Alexey
- line: |-
    Sometimes we default to the tools we know. Machine learning still offers
    techniques that might be the best default solution. You may later discover
    that a complex agentic system solves your use case.

    But I'd start with machine learning systems.
  sec: 607
  time: "10:07"
  who: Miguel
- line: |-
    A chatbot isn't that kind of machine learning use case. But for a
    classifier, recommender or credit-default system, I wouldn't default to an
    LLM. There are libraries and implemented algorithms we know work and give
    good results in companies.

    I'd start with a machine learning algorithm, even if only as a benchmark.
  sec: 631
  time: "10:31"
  who: Miguel
- line: |-
    If it's not enough, move to something more complex. People sometimes start
    with the most complex idea; I take the opposite approach. Maybe it's the
    physicist's mind, starting with spherical cows instead of a real cow.

    I like starting with the simplest solution, even a heuristic. If it solves
    the use case, use it rather than jumping to a multi-agent system with
    context engineering.
  sec: 669
  time: "11:09"
  who: Miguel
- line: |-
    Did you read Netflix's article about moving its recommender system to an
    LLM? I was surprised. Recommenders seemed like an area where using an LLM
    didn't make sense, but it looks like it does.
  sec: 706
  time: "11:46"
  who: Alexey
- line: |-
    That's a good example. They've created a foundation-model approach, which
    might suit Netflix because of its huge data volumes. Starting a recommender
    from scratch, it's difficult to find these approaches outperforming matrix
    factorization.

    Running it in a Jupyter notebook is also very different from production. In
    the lab, an LLM approach might outperform matrix factorization, but
    deploying it will probably be much more expensive.
  sec: 726
  time: "12:06"
  who: Miguel
- line: |-
    The uplift in your metrics may not even justify it. That's something I
    consider when making these decisions.
  sec: 789
  time: "13:09"
  who: Miguel
- header: "Starting a recommender system without data"
- line: |-
    Suppose we open an online shoe store and need a recommender system. What do
    we do?
  sec: 808
  time: "13:28"
  who: Alexey
- line: |-
    First, you need data. Without any data, I'd probably start with heuristics
    such as bestsellers.
  sec: 813
  time: "13:33"
  who: Miguel
- line: |-
    It's a brand-new store; we've just opened.
  sec: 824
  time: "13:44"
  who: Alexey
- line: |-
    Then I'd probably start with a content-based approach. It's better for the
    cold-start problem when you have no data. You get information from users,
    such as gender, age or color preferences, and assign similar attributes to
    items.

    Then you match user attributes with item attributes. That's a content-based
    algorithm.
  sec: 829
  time: "13:49"
  who: Miguel
- line: |-
    Does it work that well? Isn't it basically using search?
  sec: 862
  time: "14:22"
  who: Alexey
- line: |-
    That's it. It works well for cold starts when you have no information. As
    traffic grows, users interact with items.

    You can start collaborative filtering, of which matrix factorization is one
    example. You use the collaborative information from different users'
    interactions with items.
  sec: 869
  time: "14:29"
  who: Miguel
- line: |-
    You represent each user and item in the same embedding or vector space and
    find which users are closest to which items. Users and items become
    embeddings representing preferences as vectors. I'd begin with content-based
    recommendations, then move to a collaborative approach, probably simple
    matrix factorization with implicit feedback.
  sec: 902
  time: "15:02"
  who: Miguel
- line: |-
    If I had to choose, I'd probably use reinforcement learning with contextual
    bandits. It works well for recommender systems, because you can add
    randomness. One problem is the echo chamber: you send recommendations, the
    user clicks them, and the model takes those clicks as the actual preference
    when it retrains.
  sec: 943
  time: "15:43"
  who: Miguel
- line: |-
    You influence the behavior.
  sec: 984
  time: "16:24"
  who: Alexey
- line: |-
    You influence it, and it starts deteriorating. You never show the user
    anything serendipitous or new; you put them in an echo chamber. Contextual
    bandits are useful because you can add randomness.

    Even if one bandit recommends based on preferences, randomness can surprise
    users with new items.
  sec: 992
  time: "16:32"
  who: Miguel
- line: |-
    You explore the space. It's the exploration-versus-exploitation tradeoff.
    That's what you achieve with these systems.
  sec: 1027
  time: "17:07"
  who: Miguel
- header: "Contextual bandits and feedback"
- line: |-
    Could you explain contextual bandits a little more? Maybe start with
    ordinary bandits, then contextual ones, so we know what to look up to learn
    about them.
  sec: 1037
  time: "17:17"
  who: Alexey
- line: |-
    I'd start with basic reinforcement learning. You don't need advanced
    techniques. You could start with Thompson sampling, which I typically use.

    You're balancing exploration and exploitation. Contextual bandits don't
    select items randomly without context.
  sec: 1058
  time: "17:38"
  who: Miguel
- line: |-
    They have context—that's the name. The context includes features of the user
    and items, plus the user's recent search history. You put that information
    into the contextual bandit and recommend based on it.
  sec: 1096
  time: "18:16"
  who: Miguel
- line: |-
    Then there's another bandit that's completely random. Imagine two boxes. To
    generate a recommendation, one box might be a random forest that ranks
    items, while another contains a random model.

    There's a probability of the recommendation going through either box.
  sec: 1133
  time: "18:53"
  who: Miguel
- line: |-
    If it goes through the first box, the recommendation comes from the random
    forest using the user's features. Through the other, it's random. You could
    create as many boxes as you want: one based on recent activity, another on
    bestsellers for a particular gender.

    You can combine them.
  sec: 1156
  time: "19:16"
  who: Miguel
- line: |-
    Contextual bandits learn the probability of sending each user's
    recommendation through these different bandits. You get that in real time,
    which is cool.
  sec: 1188
  time: "19:48"
  who: Miguel
- line: |-
    I was recently a victim of this on Twitter. Suddenly I saw Manchester United
    tweets, although I'm not interested in football. You mentioned context:
    perhaps it assumed that because I'm male, and football is popular, there was
    a chance I'd be interested.
  sec: 1207
  time: "20:07"
  who: Alexey
- line: |-
    Twitter started showing those tweets to see how I'd react.
  sec: 1232
  time: "20:32"
  who: Alexey
- line: |-
    That's it. It's difficult to learn human reactions because, if we don't like
    something, we usually scroll past rather than explicitly give thumbs-up or
    thumbs-down feedback. That's important for people building recommenders.

    You mostly get implicit feedback, such as scrolling past or clicking and
    going back.
  sec: 1240
  time: "20:40"
  who: Miguel
- line: |-
    Implicit feedback can be hard to measure, but there's much more of it than
    explicit feedback. I don't usually click thumbs down. If I like something, I
    click thumbs up.
  sec: 1265
  time: "21:05"
  who: Miguel
- line: |-
    In my case, there were too many Manchester United tweets. I wondered what
    was happening because I didn't want them. First I scrolled past, then
    decided it was enough and used 'don't show more.'
  sec: 1286
  time: "21:26"
  who: Alexey
- line: |-
    Absolutely. YouTube does this too, mixing new things into the feed. Twitter
    recently released its algorithm.

    I think it also uses an LLM to rank the feed.
  sec: 1311
  time: "21:51"
  who: Miguel
- line: |-
    It uses one for ranking the feed?
  sec: 1329
  time: "22:09"
  who: Alexey
- header: "The four-stage recommender architecture"
- line: |-
    Yes, for ranking. It's not a bad decision. Production recommender systems
    typically follow a four-stage design.

    First is candidate generation, with algorithms such as matrix factorization
    or word2vec.
  sec: 1335
  time: "22:15"
  who: Miguel
- line: |-
    NLP models can also work well. If you're following a user's session and
    predicting the next item, they work well. These cheap algorithms generate
    candidates.

    You don't expect highly accurate recommendations at that stage; you might
    want ten candidates from each model and a hundred candidates overall.
  sec: 1371
  time: "22:51"
  who: Miguel
- line: |-
    That's candidate generation. Next is filtering. There may be duplicates, so
    you remove them.

    If we're recommending movies to a teenager, some contain violence and need
    removing. You filter the candidates.
  sec: 1407
  time: "23:27"
  who: Miguel
- line: |-
    Filtered candidates go to the ranking step, connecting to what you said
    about Twitter. The ranker needs to be slower than candidate generation but
    much better in results. It sorts the candidates into an accurate list to
    show the user.

    That's where LLMs might fit. In my experiments, gradient-boosted trees often
    work better for learning to rank.
  sec: 1437
  time: "23:57"
  who: Miguel
- line: |-
    This isn't regression or classification; it's a learning-to-rank task with a
    different objective function. A traditional neural network or LLM
    transformer might be legitimate here. The ranking stage's objective is the
    most accurate ranking.
  sec: 1499
  time: "24:59"
  who: Miguel
- line: |-
    The fourth stage is the business layer. The business may want to put certain
    items at the top because they're on promotion. That final layer can change
    the ordering the ranking model produced.
  sec: 1536
  time: "25:36"
  who: Miguel
- header: "Where LLMs help recommender systems"
- line: |-
    Back to the new shoe store. You suggested a questionnaire for the cold-start
    problem: users fill it in, and we show recommendations. Would using an LLM
    there make sense?
  sec: 1564
  time: "26:04"
  who: Alexey
- line: |-
    When I ask for points of interest, LLMs can be good at recommendations. In
    Shanghai, for example, they know places from general knowledge. Could that
    general knowledge be enough?

    Is it too slow or expensive? How do we decide whether to take that route?
  sec: 1588
  time: "26:28"
  who: Alexey
- line: |-
    That relates to Zapier's recommender. The homepage recommends workflows
    based on your history, using a traditional recommender model. We considered
    cheap LLMs, such as the new Qwen family, with useful features and local
    hosting.

    In that case, we wouldn't have the same issues around customer data or PII.
  sec: 1622
  time: "27:02"
  who: Miguel
- line: |-
    It could fit, but cost remains a problem, and the output isn't guaranteed.
    Even with RAG or fine-tuning, you can't guarantee the output is in the
    catalog. You need many checks and tests.

    I think LLMs are useful for two things in recommenders. The first is
    synthetic data.
  sec: 1658
  time: "27:38"
  who: Miguel
- line: |-
    The second is natural-language explanations of recommendations. That's how
    we use them, and I like that LLM or agent layer. It can recommend shoes and
    explain that you liked similar shoes two weeks ago or looked at related
    boots.
  sec: 1691
  time: "28:11"
  who: Miguel
- line: |-
    With collaborative filtering, we get a vector without knowing what's in it.
    The LLM can look at the history and make sense of it.
  sec: 1730
  time: "28:50"
  who: Alexey
- line: |-
    Exactly. It could look at the vectors, with metadata, and explain why
    something was recommended. Recommendations are useful, but understanding
    them improves the service.

    People want to know why.
  sec: 1742
  time: "29:02"
  who: Miguel
- line: |-
    Back to the shoe example: suppose I'm not technical and ask Claude to build
    a recommender. Would it know enough to follow your approach? Have you
    experimented with that?
  sec: 1768
  time: "29:28"
  who: Alexey
- line: |-
    I think it would do a good job. It gives sensible results and
    approximations, and I think it would help you see that you need to start
    simpler. If you explain that you have no data, it's aware of cold starts,
    content-based approaches, collaborative-filtering tradeoffs and the
    four-stage design.
  sec: 1800
  time: "30:00"
  who: Miguel
- line: |-
    For deployment and services talking to one another, I'm not sure it would do
    it perfectly. But for the actual plan, you'd get decent results.
  sec: 1840
  time: "30:40"
  who: Miguel
- header: "System design, foundations and comprehension debt"
- line: |-
    Does that mean we don't need ML engineers anymore?
  sec: 1855
  time: "30:55"
  who: Alexey
- line: |-
    We still need them for design. The strength of a machine learning engineer
    isn't implementing scikit-learn or PyTorch anymore. It's similar for AI
    engineers: ask Claude for a RAG system, and it can create one from scratch.

    For both roles, the strength is system design.
  sec: 1862
  time: "31:02"
  who: Miguel
- line: |-
    Even with a four-stage blueprint, you need to decide where to deploy it, how
    to use candidate generation and reranking, and whether it should be
    streaming or batch. Those decisions still belong to the ML engineer. Whether
    to use agent memory, RAG or an LLM wiki belongs to the AI engineer designing
    the system.

    My response would have been different three years ago.
  sec: 1897
  time: "31:37"
  who: Miguel
- line: |-
    Maybe even six months ago. Even with Opus or Astra, their choices can be
    questionable. Sometimes they make very suboptimal decisions because they
    lack the big picture.

    Using a PyTorch model doesn't make sense if a heuristic is enough.
  sec: 1950
  time: "32:30"
  who: Alexey
- line: |-
    Absolutely. Sometimes it's our fault because we didn't provide the context.
    I like 'questionable,' because that's the value of AI system-design
    engineers: they design systems their agents implement.

    It's more important than ever to know system design and question what new
    models output.
  sec: 1998
  time: "33:18"
  who: Miguel
- line: |-
    You need to question it and request another implementation. If you passively
    accept everything an LLM produces, then ML engineers aren't needed anymore.
  sec: 2051
  time: "34:11"
  who: Miguel
- line: |-
    We teach ML Zoomcamp, an introduction to machine learning engineering. It's
    the sixth cohort, and I haven't fundamentally changed the content since the
    first. Scikit-learn from five years ago is still scikit-learn today;
    Kubernetes is still Kubernetes.

    People remain interested in the course and learning the theory.
  sec: 2069
  time: "34:29"
  who: Alexey
- line: |-
    Is it still relevant? Do I still need to understand logistic regression or
    tree-based models? Is learning these things important for ML engineers?
  sec: 2099
  time: "34:59"
  who: Alexey
- line: |-
    For me, foundations matter. AI is good at getting from A to B much faster,
    but not at defining A and B. I tell it what those points are and how I want
    to get there.

    It implements that efficiently, perhaps in an hour rather than two weeks.
  sec: 2120
  time: "35:20"
  who: Miguel
- line: |-
    My decisions depend on solid foundations in those things. I know when
    logistic regression is needed and when it's enough, so I don't need a random
    forest. I could ask Claude, but there's comprehension debt: how much
    decision-making are you willing to delegate to an agent rather than
    understand yourself?
  sec: 2167
  time: "36:07"
  who: Miguel
- line: |-
    The system works, but I have no idea how.
  sec: 2212
  time: "36:52"
  who: Alexey
- line: |-
    Exactly. If it fails, you could ask the model what to do. But you lose the
    big picture and overfit to the system by asking Claude for changes.

    You keep evolving a system you didn't understand initially, and
    comprehension debt grows. People may say an agent will fix it, but
    eventually it will explode.
  sec: 2218
  time: "36:58"
  who: Miguel
- line: |-
    You built a crazy neural network with custom losses because Claude told you
    to, although a simple scikit-learn logistic-regression import could achieve
    the same. I think your cohort is useful, and I understand why people want
    these courses.
  sec: 2252
  time: "37:32"
  who: Miguel
- line: |-
    An example outside ML: I get an AWS bill that's twice last month's. Agents
    decided on a large Postgres instance when serverless DynamoDB was enough.
    Now I'm paying three hundred a month.

    Sometimes it's useful to let them explore the direction I want,
  sec: 2283
  time: "38:03"
  who: Alexey
- line: |-
    but their route isn't necessarily a straight line. You can fly from Berlin
    to Munich, which is fast but expensive and involves waiting. Or take a train
    with less hassle and lower cost, even if it takes thirty minutes longer.
  sec: 2326
  time: "38:46"
  who: Alexey
- line: |-
    I fully agree.
  sec: 2362
  time: "39:22"
  who: Miguel
- header: "The changing ML and AI engineering roles"
- line: |-
    I don't think these cohorts are going away. Sponsors aren't interested in ML
    engineering because it isn't a hot AI topic. They won't sponsor the course,
    but I keep it because it's close to my heart.

    Looking at what the market wants, VC money is driving the current interest
    in AI. You also work as an AI engineer.
  sec: 2371
  time: "39:31"
  who: Alexey
- line: |-
    How was that transition? Did you wake up one day and realize you were an AI
    engineer?
  sec: 2431
  time: "40:31"
  who: Alexey
- line: |-
    It was gradual and incremental. I never thought 'AI engineer' was a very
    good term. What's the difference from a machine learning engineer?

    People typically say AI engineers build applications on pretrained
    foundation models, while ML engineers focus on feature pipelines and
    training models.
  sec: 2445
  time: "40:45"
  who: Miguel
- line: |-
    That's the distinction I make too.
  sec: 2492
  time: "41:32"
  who: Alexey
- line: |-
    Once an ML engineer deploys a model, the role becomes similar to AI
    engineering. I could fine-tune an LLM and deploy it through an inference
    server. My transition was easy because I didn't encounter something
    fundamentally different.

    AI engineers tend to be software engineers entering the AI ecosystem by
    using AI tools. If you don't know about training and fine-tuning models, I
    wouldn't call you an AI engineer.
  sec: 2498
  time: "41:38"
  who: Miguel
- line: |-
    You're a software engineer with some AI sparkles. That's what I teach
    through The Neural Maze newsletter. Eventually AI will become a commodity,
    like DynamoDB or Postgres.

    We don't understand all the algorithms Postgres uses underneath. Eventually
    developers won't understand how Pinecone works underneath either.
  sec: 2540
  time: "42:20"
  who: Miguel
- line: |-
    If you don't know how to fine-tune models today, I'm not sure that qualifies
    as AI engineering. To me, it's software engineering with new tools.
  sec: 2602
  time: "43:22"
  who: Miguel
- line: |-
    I have some data points. Every month I scrape AI-engineer job descriptions
    across the US, UK, Netherlands, Germany and India. I have nine months of
    data and see a downward trend in PyTorch requirements.

    Early in the year, forty percent or more of companies required it; now it's
    below thirty percent. The market seems to be moving toward the
    software-engineering definition, rather than ML engineers who train models.
  sec: 2620
  time: "43:40"
  who: Alexey
- line: |-
    You're probably right. Two years ago I was more in the ML-engineering role;
    now I'm more in AI engineering. At Zapier we're fine-tuning models and
    creating a semantic router.

    I think that's AI engineering, even though fine-tuning is also ML
    engineering.
  sec: 2683
  time: "44:43"
  who: Miguel
- line: |-
    For me, AI engineering is having a model, making requests and handling
    everything around it, such as evaluation and monitoring. That's what you
    call software engineering in AI.
  sec: 2718
  time: "45:18"
  who: Alexey
- line: |-
    I think that definition is right. But there are discrepancies. Chip Huyen's
    AI Engineering book includes fine-tuning and RAG in the discipline.

    It's difficult for me to distinguish the two now.
  sec: 2733
  time: "45:33"
  who: Miguel
- line: |-
    We'll see how it evolves when the dust settles in a year.
  sec: 2765
  time: "46:05"
  who: Alexey
- line: |-
    When people ask why my title is ML/AI engineer, I say deploying logistic
    regression or a fine-tuned LLM to production isn't different for me. I'm
    deploying AI systems, whether they're classification models or LLMs. That's
    how I see myself.
  sec: 2777
  time: "46:17"
  who: Miguel
- header: "Trace redaction and the AI gateway at Zapier"
- line: |-
    What AI engineering work do you do? You mentioned fine-tuning and semantic
    routing. Could you describe your day-to-day work?
  sec: 2818
  time: "46:58"
  who: Alexey
- line: |-
    I've spent a month on AI-evaluation strategy and observability. One big
    observability challenge isn't collecting traces with OpenTelemetry. We spent
    time defining how to collect traces from different services.

    Once they land in Databricks, you need PII redaction before treating them
    and fine-tuning models. You have to ensure they're redacted and contain no
    customer data.
  sec: 2860
  time: "47:40"
  who: Miguel
- line: |-
    I assume Zapier has a lot of that.
  sec: 2893
  time: "48:13"
  who: Alexey
- line: |-
    It's a challenging but beautiful problem. We create a model, not an LLM, to
    process and redact traces almost in real time. Zapier users generate around
    twenty million trace spans per day.

    For a month, I've been creating a pipeline to fetch raw traces containing
    customer PII and redact it into a schema engineers can use safely.
  sec: 2902
  time: "48:22"
  who: Miguel
- line: |-
    I've also worked on the AI gateway. Zapier uses many LLMs, so we need a
    common layer for semantic routing. The gateway sends requests to different
    models through the same interface.

    We have an abstract representation of Opus, with fallbacks to Azure, Amazon,
    GCP or Vertex. It's similar to LiteLLM, with an AI gateway and semantic
    routing.
  sec: 2954
  time: "49:14"
  who: Miguel
- line: |-
    Semantic routing matters for cost. You can use BERT or another light model
    to classify requests and send them to the most suitable model. People think
    every question deserves a heavy LLM, but that's not true.

    Routing decides whether a smaller model can handle it. It's a challenging,
    interesting project we're doing.
  sec: 2999
  time: "49:59"
  who: Miguel
- line: |-
    The main projects are the AI gateway with semantic routing, and AI
    observability for evaluations. We'll use an approach similar to Hamel
    Husain's error analysis.
  sec: 3048
  time: "50:48"
  who: Miguel
- header: "Error analysis and evaluation of agent traces"
- line: |-
    Could you walk through that error-analysis approach?
  sec: 3079
  time: "51:19"
  who: Alexey
- line: |-
    It's simple. Hamel called it 'the revenge of the data scientist,' because
    you apply a data scientist's mindset to traces. They're not just data you
    collect; you can analyze and cluster them to extract information and
    evaluate the system.

    You manually or automatically annotate traces to check how the agent
    performed.
  sec: 3084
  time: "51:24"
  who: Miguel
- line: |-
    Did it fail or hallucinate? Then you cluster traces into error groups with
    common patterns that make the agent fail.
  sec: 3136
  time: "52:16"
  who: Miguel
- line: |-
    Do you ask an LLM to cluster them, or is there a specific approach? We want
    a concise evaluation data set because each row costs money to evaluate.
    Rather than including every error, we want a representative sample.

    Is the idea to take one representative example from each cluster?
  sec: 3157
  time: "52:37"
  who: Alexey
- line: |-
    Basically, yes. You have a paradigmatic example representing the cluster. If
    the cluster is represented by vectors, it would be the average of those
    vectors.
  sec: 3199
  time: "53:19"
  who: Miguel
- line: |-
    Do we use something like k-means?
  sec: 3217
  time: "53:37"
  who: Alexey
- line: |-
    You could use k-means with numeric metrics, such as hallucination scores or
    counts of failed tool calls. Represent traces as numeric vectors and create
    a cluster center. Then decide which clusters to address.
  sec: 3222
  time: "53:42"
  who: Miguel
- line: |-
    For each trace, you run evaluations and get data. You're clustering the
    judge's results, rather than the traces themselves?
  sec: 3248
  time: "54:08"
  who: Alexey
- line: |-
    Exactly. You've annotated a representative sample; you can't annotate
    millions of traces. You run clustering based on those annotations.
  sec: 3262
  time: "54:22"
  who: Miguel
- line: |-
    This 'revenge of the data scientist' uses techniques we've known for years.
    They've become useful in AI-engineering work.
  sec: 3280
  time: "54:40"
  who: Alexey
- line: |-
    Absolutely. It needs critical thinking about agent performance. With
    traditional ML, it wasn't easy to fool the engineer building it: poor
    linear-regression metrics were easy to spot.

    Agentic systems give plausible responses and try to cheat you.
  sec: 3291
  time: "54:51"
  who: Miguel
- line: |-
    They give something that looks nearly right but isn't. We need to spend most
    of our time understanding and applying evaluations. That's where the effort
    belongs.
  sec: 3334
  time: "55:34"
  who: Miguel
- line: |-
    Krishna asks if we could categorize traces using a decision model. I'd
    rephrase that as: have you tried something like Jev?
  sec: 3361
  time: "56:01"
  who: Alexey
- line: |-
    I haven't, but it's not a bad idea.
  sec: 3377
  time: "56:17"
  who: Miguel
- line: |-
    It's fast. With multiple judges, I'd need a separate LLM call for each, but
    Jev lets me put everything in one place. Instead of five calls, I have one,
    which is faster and cheaper.

    The results align perfectly.
  sec: 3384
  time: "56:24"
  who: Alexey
- line: |-
    That's cool. I need to try it.
  sec: 3413
  time: "56:53"
  who: Miguel
- header: "Semantic routing and model-cost tradeoffs"
- line: |-
    You mentioned BERT for semantic routing in the AI gateway. On Zapier's page,
    the copilot says to enter an idea. There's no model selector.

    Is your system choosing the model underneath based on the problem?
  sec: 3418
  time: "56:58"
  who: Alexey
- line: |-
    Copilot is one product. I'm talking about a new product we're releasing,
    Sidekick. That's where semantic routing will be applied, although it could
    apply here too.

    As you type, it'll check the message and, with very low latency, identify
    which model to route the question to.
  sec: 3450
  time: "57:30"
  who: Miguel
- line: |-
    Does BERT still make sense for this, rather than a decision model? Is taking
    a fast, open-source decision model easier than training BERT yourself?
  sec: 3480
  time: "58:00"
  who: Alexey
- line: |-
    If you want to reach production quickly, decision models are a good example
    and justified here. But with millions of requests, a specialized BERT model
    optimized in a Rust framework such as Candle can cut costs heavily. For a
    transformer tasked just with detecting a category, I'd take that approach to
    reduce cost.
  sec: 3513
  time: "58:33"
  who: Miguel
- line: |-
    vLLM released vLLM Router. I believe its first version used BERT as a
    classifier with Candle. In the long term, I'd probably use that kind of
    custom deployment because it reduces costs, even compared with cheap
    decision models.
  sec: 3588
  time: "59:48"
  who: Miguel
- line: |-
    At the beginning, you could use Laya, a Jev alternative you can self-host,
    although it needs bigger hardware and a larger GPU and will be slower. Once
    deployed, collect the logs and train a new BERT model on those predictions.
    Then it's a hundred times faster and cheaper.
  sec: 3605
  time: "1:00:05"
  who: Alexey
- line: |-
    I like that approach; it's what I typically do. Foundation models can
    provide answers that previously needed manual annotation. From day one, we
    can give customers a solution that works reasonably well, then distill that
    knowledge into our own model.
  sec: 3644
  time: "1:00:44"
  who: Miguel
- line: |-
    Let's wrap up. I checked your Substack at theneuralmaze.com, linked your
    YouTube channel and shared it in the live chat. Where else can people find
    you?

    Are you on X?
  sec: 3688
  time: "1:01:28"
  who: Alexey
- line: |-
    I'm on X as Miguel. LinkedIn is the best place to reach me. Send a message,
    and I'll reply.
  sec: 3721
  time: "1:02:01"
  who: Miguel
- line: |-
    Are those the same headphones as in your LinkedIn picture?
  sec: 3739
  time: "1:02:19"
  who: Alexey
- line: |-
    Yes. I'm attached to them. Other creators joke that I might not have ears
    because they've never seen me without headphones.
  sec: 3744
  time: "1:02:24"
  who: Miguel
- line: |-
    Can you show us your ears?
  sec: 3766
  time: "1:02:46"
  who: Alexey
- line: |-
    I can.
  sec: 3766
  time: "1:02:46"
  who: Miguel
- line: |-
    Thanks for joining us and sharing your experience and knowledge, Miguel. I
    enjoyed this episode. Thanks to everyone for joining and asking questions.

    It was a lovely discussion, and I had fun.
  sec: 3772
  time: "1:02:52"
  who: Alexey
- line: |-
    Me too.
  sec: 3789
  time: "1:03:09"
  who: Miguel
- line: |-
    Have a great week, Miguel and everyone watching. See you around. Goodbye.
  sec: 3795
  time: "1:03:15"
  who: Alexey
---

Miguel Otero Pedrido, an ML and AI engineer and author of The Neural Maze, joins Alexey Grigorev to talk about production machine learning. They cover his path from theoretical physics to ML engineering, why traditional machine learning still matters, how to start a recommender system without data, contextual bandits, where LLMs help recommender systems, the changing ML and AI engineering roles, trace redaction with an AI gateway, error analysis of agent traces, and semantic routing.

Links:

* [The Neural Maze](https://theneuralmaze.substack.com/){:target="_blank"}
* [Miguel on LinkedIn](https://www.linkedin.com/in/migueloteropedrido/){:target="_blank"}
* [Miguel on GitHub](https://github.com/MichaelisTrofficus){:target="_blank"}
