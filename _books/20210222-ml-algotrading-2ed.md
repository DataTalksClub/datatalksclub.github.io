---
title: "Machine Learning for Algorithmic Trading"
description: "Book of the Week. Machine Learning for Algorithmic Trading (2nd edition) by Stefan Jansen"
cover: "images/books/20210222-ml-algotrading-2ed/cover.jpg"
image: "images/books/20210222-ml-algotrading-2ed/preview.jpg"
start: 2021-02-22 00:00:00
end: 2021-02-26 22:59:59
authors: [stefanjansen]
links: 
  - text: Book's page on Packt
    link: https://www.packtpub.com/product/machine-learning-for-algorithmic-trading-second-edition/9781839217715
  - text: Book's page
    link: https://ml4trading.io/
  - text: Book on Amazon
    link: https://www.amazon.com/gp/product/1839217715/
  - text: Book's GitHub repository
    link: https://github.com/stefan-jansen/machine-learning-for-trading
  - text: ML4Trading Community
    list: https://exchange.ml4trading.io/

archive:

- name: Doink
  text: How good are the strategies mentioned in the book good enough to make decent
    money in real time? Vladimir Finkelshtein basically completed my question, absolutely
    valid points with the whole Gamestock Saga and BTC price pump with just one tweet
    and investment by Musk.
  replies: []
- name: Vladimir Finkelshtein
  text: 'One of the most successful trading strategies is market manipulation. How
    can one make sure that ML does not learn to do it? (because it will, since it
    tries to optimize the profits)

    From the other side, how can one identify that the market is being manipulated?
    Nowadays, a single tweet can wreak havoc in the markets.'
  replies: []
- name: Aleix
  text: "Hi, Stefan Jansen! Nice to meet you.\nIt's actually a great timing for me,\
    \ since I am actually very interested in this topic and was thinking of developing\
    \ my bachelor thesis around an algotrading system \U0001F604\nMy question is:\
    \ how would you describe the use of ML in the algotrading scenario? Has it been\
    \ a game-changer and everyone uses it now? Or just another tool that sometimes\
    \ works and sometiems don't?\nThanks a lot!"
  replies: []
- name: Hong-Ngoc Emily Tran
  text: Who should read the book? Can a normal banker with somewhat knowledge in Data
    Analytics use this book to understand what IT people are doing?
  replies: []
- name: Rica
  text: Hi Stefan, thanks for doing this. What type of securities does machine learning
    for algorithmic trading cover?
  replies: []
- name: Rica
  text: Can you share some success stories in using machine learning for algorithmic
    trading?
  replies: []
- name: Rica
  text: "Last question: can machine learning for algorithmic trading detect or prevent\
    \ what happened to Gamestop? Thank you for your time \U0001F642"
  replies: []
- name: Denis Lepchev
  text: 'Hi Stefan, thanks for writing the book!

    What in your opinion are most common pitfalls in backtesting and how to avoid
    them? To extend the previous question, what do you think about usage of synthetic
    data for backtesting - how reliable it is?Thank you.'
  replies:
  - name: Oliver Wilkins
    text: Hi Stefan, it'd be great to see your thoughts on this!
- name: Wendy Mak
  text: 'Hi Stefan, my question is:

    Does algorithmic trading (tbh all the ''fancy'' financial instruments in general)
    serve any positive purpose beyond making a bunch of investment bankers very rich?
    ;)) -- sorry it''s only distantly related to the main content in your book, but
    I''ve never really got the point of the fancier things you can do on the stock/commodities/etc
    markets...'
  replies: []
- name: Vladimir Finkelshtein
  text: I imagine if one trains trading algorithms with neural networks, they will
    learn many spurious correlations. Is there some regularization for this?
  replies: []
- name: Vladimir Finkelshtein
  text: 'Once in a while there is an article about some academic algorithm that beats
    the market. But these algorithms always work only on the past data. Are there
    examples of ML algorithms that actually generalize to the future?

    Is this question even meaningful? Since most of the trading today is algorithmic,
    maybe beating the market just means beating other algorithms?'
  replies:
  - name: Vladimir Finkelshtein
    text: "My statement about \u201Cmost of the trading is algorithmic\u201D refers\
      \ to forex market (in which wiki says algo trading is 90%). You can disregard\
      \ it, since it is probably not true for more volatile markets."
- name: Tino
  text: "Hey Stefan! \U0001F44B Thanks for sharing your knowledge!  \U0001F9E0 How\
    \ do you include the natural uncertainty when modelling stocks, trading, etc!\
    \ Often individuals (Elon Musk, etc.) can have an unpredictable impact. Is there\
    \ kind of a general approach to include this?"
  replies: []
- name: Arni Westh
  text: Have you launched any algo trading systems trading live autonomously with
    real assets on the line? Imo, until this stage, all of these discussions tends
    to be rather academic - it's when you go live you learn about all details you
    didn't think about in simulation/backtesting...
  replies: []
- name: Stefan Jansen
  text: "Alright, so here are a few points on your questions:\n1. On Aleix question\
    \ of how I would describe the use of ML for trading in the industry:\n- Finance,\
    \ of course, has  very long history of using quantitative tools. This includes\
    \ basic ML algos like good old linear regression. \n- Just as elsewhere, more\
    \ data drives more demand for better techniques to apply to the data. More specifically,\
    \ together with the emergence of 'alternative data' ([https://alternativedata.org/](https://alternativedata.org/)),\
    \ there has been a lot if interest (and more need) to use data science / ML to\
    \ extract value. \n- This takes different forms depending on the time horizon:\
    \ \n    \u25E6 On one end of the spectrum, it includes more traditional investors\
    \ that have started to use ML to forecast fundamentals (see e.g. interview with\
    \ Michael Recce, now CDS at Neuberberger Berman who previously introduced this\
    \ at Point 72: [https://www.investmentmagazine.com.au/2019/10/michael-recce-the-goldilocks-approach-to-neuroscience-ai-and-investing/](https://www.investmentmagazine.com.au/2019/10/michael-recce-the-goldilocks-approach-to-neuroscience-ai-and-investing/)).\n\
    \    \u25E6 On the other end, high-frequency trading also offers applications\
    \ from optimal trade execution to alpha (see, e.g. survey of use cases: [https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf](https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf)).\n\
    - The basic argument in favor of using ML is that most investors are already trying\
    \ to project market trends in the short or long run from all sorts of data. It's\
    \ not unreasonable to assume that ML can add value to this process. Machines naturally\
    \ have more of an edge for shorter horizons, whereas humans may be (still) better\
    \ positioned to process the complex information involved in analyzing longer-term\
    \ trends.\n- It is important to keep in mind that financial markets are highly\
    \ competitive and packed with sophisticated institutions operating at substantial\
    \ scale. Clearly it takes a bit more than downloading some data from yahoo finance\
    \ and installing scikit-learn to predict Apple's (or Tesla's..) stock price. Some\
    \ healthy skepticism is certainly warranted and several funds have closed down\
    \ their ML efforts. \n- At the same time, you may have heard of Renaissance Technology\
    \ (RenTek). I'd highly recommend 'The man who solve the market' about Jim Simons\
    \ ([https://www.amazon.com/Man-Who-Solved-Market-Revolution/dp/073521798X](https://www.amazon.com/Man-Who-Solved-Market-Revolution/dp/073521798X))\
    \ who started the - by far! - most successful hedge fund, achieving 50%+ per year\
    \ since the late 80s on their (now only internal) Medallion Fund. Earlier and\
    \ more focused than most, Rentek has built a highly-secretive quantitative fund\
    \ run largely by scientists who have started collecting huge datasets before anybody\
    \ else was doing this, and apply all sorts of proprietary algorithms to identify\
    \ patterns. While nobody knows what they are actually doing, much would probably\
    \ be broadly classified as ML that operates in a largerly autonomous fashion.\
    \ \n- Two Sigma, started by DE Shaw alums who also hired several ML &amp; Python\
    \ specialists (Anaconda provides consultancy, lead Pandas maintainer is VP). These\
    \ are very substantial success stories, and have attracted numerous attempts to\
    \ imitate with mixed results.\n- However, financial markets are very large and\
    \ diverse, extending way beyond the (recently) popular sensations surrounding\
    \ Gamestop, Tesla or Bitcoin. There are many niches in less actively traded areas\
    \ where even smaller players can do well."
  replies:
  - name: Rica
    text: "I\u2019m curious has Rentek ever publish about its models?"
  - name: nate8020
    text: What a high-quality response Stefan. This alone has made me infinitely curious
      about your work.
  - name: Aleix
    text: man, that's what I call a response! thanks a lot for the huge details and
      clarity, really appreaciated!
  - name: Stefan Jansen
    text: Rica nothing, nada, niente. airtight NDAs. the book is really fun to read,
      you'll see. the folks who work there are as good as it gets.
  - name: Doink
    text: why is alternativedata giving their datasets for free?
- name: Stefan Jansen
  text: 'On market manipulation: it''s hard to know. Manipulation is illegal and regulators
    are watching. Not sure predicting returns better than by chance which is already
    useful would count as or be confounded with market manipulation. I would also
    distinguish between the famous Elon Musk etc examples and the much larger volume
    that trades in less spectacular environments. Since I''m not sure that the bulk
    of trading activity is related to market manipulation, I''m not sure ML would
    automatically ''learn how to do it''. Also, manipulation typically requires some
    influence - either the ML would first have to figure out how to attract as many
    twitter followers and general real world success as Elon Musk, or how to rally
    a bunch of reddit users (plus the HF that also played along). Tricky..'
  replies: []
- name: Stefan Jansen
  text: 'Hong-Ngoc Emily Tran - who should read the book: it''s useful if you''re
    an analyst who wants to go beyond spreadsheet, a PM who wants to use ML, either
    to run things herself or by directing specialists. The book is fairly hands-on
    with 150+ notebooks; you should be pretty familiar with Python and the standard
    data science/ML libraries so you can focus on the domain-specific aspects.'
  replies: []
- name: Stefan Jansen
  text: Rica the book mostly uses equities simply because the data is most easily
    available. Free data is rare, but we do have examples that use minute-data (somewhat
    'high-frequency') as well as intl equities and pairs trading with ETF. I would
    say though, that the most important part is demonstrating how the ML algorithms
    can be used to inform a strategy and then backtest/evaluate the strategy. I think
    if you're proficient with these applications you're in a very good position to
    come up with your own ideas for other markets if you prefer.
  replies:
  - name: Rica
    text: "Thanks for your response Stefan Jansen, I will explore and learn from your\
      \ models \U0001F642"
- name: Stefan Jansen
  text: 'Denis Lepchev backtesting is tricky as you''ve probably hear. I''m sure you''ve
    come across Marcos Lopez de Prado who is one of the leading practitioners in the
    field and has discussed this in great detail (now runs quant at Abu Dhabi''s SWF,
    before at Guggenheim and AQR [https://www.quantresearch.org/](https://www.quantresearch.org/)).
    My book summarizes his points which are conceptually simple: given limited historical
    data, if you just try long enough you''re bound to find something that looks really
    good in hindsight. Just like ML model overfitting. There are ways to protect against
    this, being aware of the risk being the first and most important step.

    Synthetic data would be (part of ) a solution and and there are certainly promising
    early research results. In the book, I reproduce the TimeGAN paper presented recentat
    NeurIPS [https://proceedings.neurips.cc/paper/2019/file/c9efe5f26cd17ba6216bbe2a7d26d490-Paper.pdf](https://proceedings.neurips.cc/paper/2019/file/c9efe5f26cd17ba6216bbe2a7d26d490-Paper.pdf).
    I haven''t had the time to experiment with this at scale but I''m sure most of
    the larger funds are exploring this as an option. It may take a few years until
    we know if this can produce sufficiently useful data; GANs have the mode collapse
    problem that delivers very realistic but not very diverse results, which is one
    of the issues that still needs to be overcome.'
  replies:
  - name: nate8020
    text: Marco's work is high-caliber, this fragment of his book (Advances in Financial
      Machine Learning / Marcos Lopez de Prado) really grabbed my attention when his
      book came out.
- name: Stefan Jansen
  text: Wendy Mak good and fair question. I would agree that the financial sector
    has overall taken on proportions as  a % of GDP that is quite a bit larger than
    its contribution to overall welfare. There are some economic arguments how sophisticated
    investors make markets more efficient because they help 'discover the right prices'
    that are signals for other activity, but I'm not sure that justifies the outsized
    gains by some. Applies to other areas as well, though; I'm not sure the winner-take-all
    results in some industries are the best outcome overall.
  replies: []
- name: Stefan Jansen
  text: Vladimir Finkelshtein right, financial data is very noisy, precisely because
    markets are a competitive arena to the extent that quite a few say it should be
    next to impossible to predict anything about price movements at all. The best
    way out is of course access to (at least somewhat) exclusive data. Even then,
    and even more so if you rely mostly on market data, denoising via feature engineering
    (we cover e.g. Kalman filter etc) and regularlzation are key. In fact, complex
    models like deep NN are often at a disadvantage since they cannot benefit from
    the abundance of data that we have in other domains where they excel. In other
    words, success is unlikely going to rely on the biggest model but rather on a
    good overall setup from good data to robust risk and transaction cost management.
  replies: []
- name: Stefan Jansen
  text: Tino ML models perform best when there's a systematic relationship between
    the input data and the target. They are least likely to do well when things fundamentally
    change. Fortunately, the Gamestop &amp; Musk stories are not what dominates markets,
    just the news. So there's plenty of room for models to add value (I think..).
  replies: []
- name: Stefan Jansen
  text: Arni Westh fair point, the book on Simons/Rentek in fact has some of the key
    figures of the fund on record that the one thing that never worked was trying
    to replicate academic papers. I work with clients and there are some examples
    in the wild that are working. It's often based on a strategy that uses some specific
    data and has been developed manually before (and already created profits). ML
    is very useful to then automate and scale such a strategy. There are many use
    cases, just as there are many profitable traders that operate at limited scale,
    'under the radar'.
  replies: []
- name: nate8020
  text: Stefan Jansen in your view, where is the greatest opportunity at the intersection
    of ML and Algo-Trading right now?
  replies: []
- name: Vinoth Kumar
  text: "Hi Stefan Jansen . \n1. From your experience in developing ML systems for\
    \ trading, what are the characteristics of a simple system and when does it become\
    \ too complex. And do simple systems do Better than complex systems. \n2. Retail\
    \ investors have certain advantages over institutional investors in terms of size.\
    \ How can retailers develop systems that play to their advantage over the big\
    \ funds houses. \n3. trading Systems also need to be aligned with the over market-\
    \ bull, bear and side ways market. How can investors predict the future state\
    \ of market or when they should fine tune their allocation to various systems.\n\
    4. What are some of the features that retailers usually miss in their trading\
    \ systems design."
  replies: []
- name: Amr Alaa
  text: 'Hey Stefan Jansen, thanks for your answers here,

    Can python developer or machine learning engineer benefit from your awesome book,
    or donwe need to review some of the basics first?'
  replies: []
- name: Amr Alaa
  text: '2nd question

    Why it is so hard to get excellent results with ML in trading systems

    We can develop reinforcement learning to deal with the market using paper money
    for 6 months, it will had most of the parameters needed to do good profitting
    trades after using real accounts, right?

    I know it looks pretty silly, but why it is not working like this using modern
    learning techniques?'
  replies: []
- name: Tino
  text: 'Hey Stefan Jansen :) thanks for the great answer :)

    A follow-up question: depending on volatility and risk which varies from market
    to market, how would you rate the options for risk distribution over ones portfolio
    by using ML? And is this e.g. a more suitable/accurate use case?'
  replies: []
- name: Vladimir Finkelshtein
  text: From your answers it sounds like that the industry prefers to rely on the
    advanced features engineered by domain experts and to apply less complex and reliable
    algorithms. Is there a hope that ML can find insights unknown to the experts?
    It seems like there are many regulatory and trust-related problems to use the
    latent features that ML offers in other domains.
  replies: []
- name: Stefan Jansen
  text: Vladimir Finkelshtein when it comes to financial data, esp market data (prices,
    volumes, returns), there is a lot of noise and complex models tend to overfit
    plus some domain expertise has developed over the last decades when this was the
    only data (plus fundamentals). What's new is that now much more data is available
    - from new to credit card payments, mobile phone location or supplier activity.
    In this sense, finance is catching up to other industries and the evaluation of
    what works and what doesn't is still underway. Clearly there are regulatory issues
    around privacy and also fair competition, which are also still playing out.
  replies: []
- name: Stefan Jansen
  text: "nate8020 not sure there is one single greatest opportunity. There are several\
    \ that range from -\n- coming up with ingenuous use cases of novel datasets to\
    \ \n- NLP applications (given advances in the area and the limited use of text\
    \ data thus far) and\n- using ML/DL in low-latency context"
  replies: []
- name: Stefan Jansen
  text: "Vinoth Kumar\n- The system should match the kind of data and scale you're\
    \ operating at. If you properly test your models you should notice pretty quickly\
    \ when they over- or underfit. I don't think there's a general rule, it really\
    \ depends on what you are trying you accomplish. \n- Clearly, the most profitable\
    \ hedge funds that use ML also operate at scale in terms of AUM, staff, data and\
    \ range of different strategies. Your best chance as a retail investor is to find\
    \ a niche that you know or are learning something about that has not attracted\
    \ too many sophisticated players yet. I'm not sure it's 'the system' as more the\
    \ area you choose to play.\n- Overall market trends is a macro prediction that\
    \ retail investors can do as well (or poorly) as anyone else. It's hard! But gotta\
    \ keep trying \U0001F642\n- Retail investors may want neglect to have a nimble\
    \ system that permits them to constantly come up with new ideas and migrate them\
    \ from backtest to paper- and then livetrading, while closely monitoring the latter.\
    \ It's always evolving."
  replies: []
- name: Stefan Jansen
  text: 'Tino there are attempts to use hiearchical clustering and others to handle
    asset/risk allocation, see Lopez de Prado 2016: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678)

    Some results are promising, others not so much. Certainly some research in this
    direction.'
  replies:
  - name: Tino
    text: Stefan Jansen thanks for the answer :)
- name: Stefan Jansen
  text: 'Amr Alaa if you''re familiar with python &amp; ML using pandas/sklearn/tensorflow
    you should be fine and off to the races.

    - It''s hard because markets are very competitive. See previous answers.

    - Think about how trading works - for me to make money, someone else tends to
    lose some. There''s a lot of smart people at works because there''s a lot of money
    to be made. That''s why it''s hard. Market players adapt very quickly to changes
    in the market, news etc.'
  replies: []
- name: Wendy Mak
  text: Hi Stefan, if I am not particularly interested in apply the algos to real
    trading, do you think the concepts introduced in your book still quite useful
    for other ML applications? e.g. I think you said there are some interesting timeseries
    algos you introduced in the book?
  replies:
  - name: Amr Alaa
    text: Great question by the way
- name: Stefan Jansen
  text: Wendy Mak I try to give a fairly broad overview of ML with plenty of background
    on how things work. Some have found it useful as a more general reference but
    really depends on your interests and background. Check out the website [https://www.ml4trading.io/](https://www.ml4trading.io/)
    and the repo [https://github.com/stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading)
    where you can see in detail what to expect.
  replies: []
- name: nate8020
  text: Stefan Jansen Say you set aside $100 (of real USD) of budget to build your
    own trading bot, what would be a good resource to put together such home-built
    service (APIs)?
  replies: []
- name: Stefan Jansen
  text: nate8020 not sure I understand, what would you spend the $100 on? Data, services,
    investment capital, learning reources?
  replies:
  - name: nate8020
    text: "Say I want to create my own trading bot with real money ($100). Is there\
      \ a public API I can use to actually execute trades and pull balances? You know,\
      \ like the pros \U0001F642"
  - name: nate8020
    text: 'Stefan Jansen this is what I was looking for: [https://algotrading101.com/learn/robinhood-api-guide/](https://algotrading101.com/learn/robinhood-api-guide/)'
  - name: Stefan Jansen
    text: "Oh sorry didn\u2019t see your clarification. There\u2019s also Alpaca;\
      \ IB also has a popular API."
  - name: Stefan Jansen
    text: The plan for the 3rd edition is to include the trading/execution part. If
      time permits..
  - name: nate8020
    text: "You've got your first sale ready!  \U0001F601"
- name: Dan
  text: "As someone who has read Stefan Jansen\u2019s book thoroughly ([https://www.linkedin.com/feed/update/urn:li:activity:6712046823361536000/](https://www.linkedin.com/feed/update/urn:li:activity:6712046823361536000/))\
    \ I can tell you that this book is fantastic.\nNot only for trading and finance\
    \ but ML and data science in general. It went brilliantly in tandem with my MS\
    \ in Financial Math. It's brilliant how it explains really complicated concept\
    \ in easy to grasp chunks.\nPeople like to compare this book to Marcos Lopez de\
    \ Prado's book but they're not really a competition, I'd say they work in tandem.\
    \ Furthermore this is the more technical one and with better applications.\nMLDP's\
    \ is more general concepts and most of the code examples are from python 2. Not\
    \ taking anything away from his books, they're brilliant, but Stefan Jansen\u2019\
    s is definitely more up-to-date\nCould not possibly recommend this book enough."
  replies: []
- name: Vladimir Finkelshtein
  text: What is the current hype in algorithmic trading and is it justified or not
    in your opinion? I heard people got excited about LSTMs but that was a while ago.
  replies: []
- name: Stefan Jansen
  text: Thanks Dan! Absolutely, I would not in my dreams attempt to compete with Marcos
    Lopez de Prado; I think we have very different goals. Adv. in Fin ML is a collection
    of research and practical advice from a leading practitioner and first and foremost
    delivers some very pointed insights straight from the frontier. I'm trying to
    provide a much broader introduction and think it is best read as a domain-specific
    intro to ML. I've done both trading and data science for while and when I was
    teaching DS in NYC I noticed that there was a lot of interest from folks in investment
    but hardly any specific material available. Personally I think it's helpful to
    have a good grasp of how algos work I have included quite a bit of background
    and that's possibly why I've heard a few times that folks have got something out
    of it about using ML more generally, esp in a time series context.
  replies: []
- name: Stefan Jansen
  text: Vladimir Finkelshtein I guess hype is almost by definition not justified?
    I think it's a case of overestimated in the short run, underestimated in the long
    run. It takes time to figure out how to incorporate ML into trading processes
    since it's not about switching over from human to machine in most cases; finding
    the right balance is a bit of work that takes many years. I'm sure in 10 years
    ML and the use of a very broad range of data is going to be common place. May
    look different than we imagine today but I think it's hard to see that crunching
    excel is going to grow and python &amp; co will disappear instead.
  replies: []
- name: tony hung
  text: "Hey Stefan Jansen Im currently working on a forecasting model and I\u2019\
    m curious if the book goes into detail about ARIMA and othe r deep Learning models.\
    \ I don\u2019t know much about finance ,and more on the deep Learning side. Is\
    \ the book geared towards finance people or ml people? I\u2019m hoping both"
  replies: []
- name: Stefan Jansen
  text: hey tony hung the book tries to sort of bridge the gap. there's a chapter
    on arima, arch/garch and cointegration, and another one on RNN. and of course
    much more, check out the website and repo linked a bit above that should give
    you an idea
  replies:
  - name: tony hung
    text: "Thanks, I\u2019m going through the site now"
  - name: Stefan Jansen
    text: Great, pls let me know what you think!
- name: Vladimir Finkelshtein
  text: What are some other use cases of ML in algorithmic trading beyond traders
    making profit? (I am thinking of regulators here, but maybe something else?)
  replies: []
- name: Doink
  text: Stefan Jansen how to detect pump and dump characteristics in a stock? And
    to spot parties which create FUD? Do you think Renaissance Finance or Two Sigma
    handle this? I had seen a kaggle competition of 2 sigma where they tried to do
    sentiment analysis of stocks via news but they removed that data.
  replies: []
- name: Roman G
  text: "I've heard a story about a system which detects insider trading at NASDAQ,\
    \ which tries to estimate via ML how lucky you are. If you are too lucky, then\
    \ a person in SEC takes a detailed look on your trading activity \U0001F642"
  replies:
  - name: Doink
    text: Interesting stuff but how can you build such a system?
  - name: Vladimir Finkelshtein
    text: 'That almost sounds like rule based approach: if you are making higher margins
      than others (in some metric), you will be looked at closely.'
  - name: nate8020
    text: Roman G Vladimir Finkelshtein do you know of an API in which I can place
      but/sell trades? I wanna play with the algos of the book with an actual (tiny)
      budget
  - name: Vladimir Finkelshtein
    text: Not really.
  - name: Roman G
    text: 'it depends on your scale. HFT traders usually use FIX apis to directly
      inject orders into broker system, but these are usually quite pricey: expect
      somewhere around 1-2k$/month + comissions.'
  - name: Roman G
    text: 'a low-cost solution can be using brokers public apis like this: [https://www.interactivebrokers.com/en/index.php?f=5041](https://www.interactivebrokers.com/en/index.php?f=5041)'
  - name: Roman G
    text: these APIs won't give you ultra-low-latency, but it's cheap enough to play
      with it.
  - name: Roman G
    text: main pro of FIX is that you're not tied to a specific broker and migrate
      freely. main con is that it's quite complicated (market data tier2 stream for
      NASDAQ has so huge data rate so it's non-trivial even to receive it)
- name: Chris Chia
  text: Hi Stefan, thanks for writing the book! Are there any recent papers or new
    ML/DL techniques that are still emerging, but you think could be particularly
    promising towards algorithmic trading?
  replies: []
- name: Stefan Jansen
  text: 'Vladimir Finkelshtein regulators would be interested in market manipulation
    through collusion, cornering or things like insider trading . methods like anomaly
    detection come to mind. here''s the SEC on the topic: [https://www.sec.gov/news/speech/bauguess-big-data-ai](https://www.sec.gov/news/speech/bauguess-big-data-ai)'
  replies: []
- name: Stefan Jansen
  text: Doink for traders, detecting such schemes would be useful if they can profit
    from it. as such they would be looking for profitable momentum situations based
    on volume velocity and who is participating. regulators might be more interested
    in detecting such a scheme as and end to itself rather than a means to profit.
    they are certainly trying.
  replies: []
- name: Stefan Jansen
  text: Roman G see above - not familiar with this story but clearly if your trades
    turn a profit too many times you'll raise flags just like in a casino.
  replies: []
- name: Stefan Jansen
  text: Chris Chia the book has tons of references, many of a recent nature. look
    up bryan kelly at yale/aqr, for instance who has been pretty active, and the work
    he and co-authors cite.
  replies: []
- name: Tino
  text: Stefan Jansen Is explainabilty a Big topic in trading? In credit risk for
    e.g. it is super important due to reportings for the regulator. Is it similar
    in trading?
  replies: []
- name: Stefan Jansen
  text: Tino the datasets themselves are certainly subjects to compliance re privacy
    etc. On the modeling side, I think explainability is more of an issue because
    decision makers (depending on the organization) want to understand if a model
    aligns with their priors than for the reasons you mention for credit decisions,
    for instance. It's certainly a hot topic, but getting the models to work well
    is probably a higher priority.
  replies: []


---

The explosive growth of digital data has boosted the demand for expertise in trading strategies
that use machine learning (ML). This thoroughly revised and expanded second edition enables you
to build and evaluate sophisticated supervised, unsupervised, and reinforcement learning models.

This edition introduces end-to-end machine learning for the trading workflow, from the idea and
feature engineering to model optimization, strategy design, and backtesting. It illustrates this
workflow using examples that range from linear models and tree-based ensembles to deep-learning
techniques from the cutting edge of the research frontier.