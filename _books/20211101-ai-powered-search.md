---
title: "AI-Powered Search"
description: "Book of the Week. AI-Powered Search by Trey Grainger, Doug Turnbull and Max Irwin"
cover: "images/books/20211101-ai-powered-search/cover.jpg"
image: "images/books/20211101-ai-powered-search/preview.jpg"
start: 2021-11-01 00:00:00
end: 2021-11-05 22:59:58
authors: [Trey Grainger, dougturnbull, Max Irwin]
links: 
  - text: Book's page
    link: https://www.manning.com/books/ai-powered-search
  - text: Book's GitHub repository
    link: https://github.com/treygrainger/ai-powered-search

archive:
- name: Matthew Emerick
  text: 'Hey, Doug Turnbull! Thanks for doing this!

    The main thing I remember from my AI courses a couple decades ago is the A* algorithm.
    Has that been unseated as the "ultimate" search algorithm? Will it ever be?'
  replies:
  - name: Doug Turnbull
    text: "oh ha! A* is about graph search, no? This book is about natural language\
      \ search \U0001F642 Of which I doubt there ever will be an ultimate algorithm\
      \ given how diverse the space and domains are"
- name: Doug Turnbull
  text: "Hi all, I\u2019m excited to be here. Hopefully I can drag fellow authors\
    \ here a swell!"
  replies: []
- name: WingCode
  text: "Hi Doug Turnbull , good to have you here again \U0001F642\n1. What are the\
    \ commonly used \"dials and knobs\" used in search engine to fine-tune its behaviour?\
    \ example: Synonym groups to handle domain level business jargons. Who usually\
    \ controls these \"dials and knobs\"? Is it the data scientists, business team\
    \ or someone else?"
  replies:
  - name: Doug Turnbull
    text: "Hey WingCode -\n- Basically anything that defines the structure of the\
      \ index and how it\u2019s queried is open game. Maybe some major groupings?\n\
      \    \u25E6 Stages of ranking from first pass retrieval and later reranking\
      \ against different criteria / loss functions \n    \u25E6 Synonyms, stemming,\
      \ lematization, any kind of NLP between the content and the index (or query\
      \ and querying the index)\n    \u25E6 Any kind of statistic that might indicate\
      \ quality (page rank, sales, clicks, etc)\n    \u25E6 Really the limit is your\
      \ imagination!\n- I find its best if the domain expert manages direct synonyms,\
      \ but the relevance/data team has to decide exactly how they interface into\
      \ the main algorithm"
- name: WingCode
  text: '2. What are the characteristics of your dream search engine? example: For
    me personally, it is not using any of the facets or "sort by" options. The search
    engine knows my favorite color is red and usually I look out for the cheapest
    product out there.'
  replies:
  - name: Doug Turnbull
    text: "If by search engine you mean the underlying search index technology programmable\
      \ to build a search solution, I want\n- A math-oriented, not text-match-oriented,\
      \ API (see Vespa\u2019s ranking steps)\n- An ability mix traditional sparse\
      \ and dense vector indices for hybrid retrieval \n- Doing all those things at\
      \ high speed\n- Declarative configuration, not programmatic configuration, so\
      \ we can iterate on the search solution independent of the end application\n\
      - Built in ability to execute arbitrary python code at query and index time\
      \ with the classic data science toolkit"
  - name: xnot
    text: "Since you mentioned vespa, I\u2019m curious if you would advise picking\
      \ it over ES as a base search stack ? \U0001F642"
  - name: Doug Turnbull
    text: "Probably yes these days, but I usually don\u2019t recommend people go through\
      \ extensive search rewrites just for the sake of the underlying index\u2026"
  - name: WingCode
    text: Thank you Doug for the detailed answers
- name: xnot
  text: When is a good time to start thinking about investing in LTR capabilities
    in your search stack?
  replies:
  - name: Doug Turnbull
    text: "I think you should always think about it, because the limiting factor is\
      \ training data, and you would want good training data for a non-LTR solution\
      \ anyway. Once you figure out the training data side the LTR optimization becomes\
      \ \u201Ceasy\u201D"
  - name: xnot
    text: Great, does the book cover the event analytics side of gathering relevant
      training data?
  - name: Doug Turnbull
    text: Yes! Very much so
  - name: xnot
    text: Awesome
- name: xnot
  text: What are the low hanging fruits in AI powered search - stuff with the highest
    ROI in short amount of time
  replies:
  - name: Doug Turnbull
    text: Anything around query understanding. Can you classify queries into categories?
      Types of intents, etc based on simple click statistics?
  - name: xnot
    text: "Thanks! I\u2019m looking forward to this part in the book. I have struggled\
      \ with query understanding because of lack of click data. Simple methods like\
      \ string matching lead to a lot of weird edge cases"
  - name: xnot
    text: That and spelling correction. I have tried the standard stuff like edit
      distance and metaphone based algos, but they still fall short of expectations
- name: xnot
  text: On a similar note, what are the things which will take a long time to give
    results, but in the end will be worth all the effort?
  replies:
  - name: Doug Turnbull
    text: "This question is really hard as its so domain specific, IMO you really\
      \ gotta work to spike ideas with an experiment before digging too deep. I\u2019\
      ve seen teams really invest heavily upfront, but not see payoff at the end.\
      \ That\u2019s a big thing to avoid"
- name: xnot
  text: Quite a few of AI capabilities in search require decent amount of data. How
    do you deal with this if you are starting from scratch?
  replies:
  - name: Doug Turnbull
    text: "Data as in clickstream data?\nWell earlier I mentioned query understanding\
      \ as an obvious win. But this classification can also be done through manual\
      \ labelers (given a sufficiently well formulated task). Of course it breaks\
      \ down as queries grow in complexity or domain specificity, but that\u2019s\
      \ a good start."
  - name: xnot
    text: Ah yes, does the book cover a the proper ways to approach manual labelling?
      That space also seems to have exploded (so many tools!)
  - name: Doug Turnbull
    text: "Sadly we don\u2019t cover this that much, but its a great topic!"
- name: Adhi
  text: Hey Doug Turnbull. any thoughts on assessing and tackling position bias through
    empirical methods like Randpair vs theoretical methods built into LTR models?
  replies:
  - name: Adhi
    text: we found that the position biases calculated using [methods like EM](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46485.pdf)
      didnt line up with what what we found with randpair - so wanted to know whats
      more typical in industry. thanks!
  - name: Doug Turnbull
    text: "I haven\u2019t. messed with these, interesting!\nUsually my approach is\
      \ to debias the training data itself using a click model, so I\u2019m not overly\
      \ coupled to the LTR model itself and these sorts of assumptions\u2026"
  - name: Doug Turnbull
    text: Because then you can take that training data and study it independent of
      any model, and decide whether it reflects reality
- name: Carsten Schnober
  text: In practice, search relevancy can be highly subjective, which makes results
    hard to evaluate and optimise for actual users. Do you think that "AI-powered
    search" is affected by this more/equally/less than "traditional" (keyword-based)
    search?
  replies:
  - name: Doug Turnbull
    text: "yes it can be highly subjective. I think it means that you have to know,\
      \ given a keyword, the many possible intents it could have and instead of ranking\
      \ to one of those intents, you give them a mixture of them. Then as your confidence\
      \ grows in their intent (through personalization? or just better knowledge about\
      \ queries), you zero-in on one of the intents\u2026\nI wrote an articel about\
      \ that! [https://opensourceconnections.com/blog/2019/09/05/diversity-vs-relevance/](https://opensourceconnections.com/blog/2019/09/05/diversity-vs-relevance/)"
- name: Alexey Grigorev
  text: Speaking of labels, what do you think about clickstream data vs manual assessment
    (via platforms like mturk and similar)? What are the pros and cons for each? And
    how can we combine the two?
  replies:
  - name: Doug Turnbull
    text: "clickstream data will be like implicit data, where users tell you what\
      \ they wouldn\u2019t say outloud - whether because they don\u2019t want to say\
      \ it out loud, or because they\u2019re not conscious of it!\nMechanical turk\
      \ is great to overcome cold start problems. But might not reflect the reality\
      \ of your usecase/app. Especially if your app is domain specific\n\u201CCombining\u201D\
      \ is tough, rather I use them as different perspectives on the problem."
- name: Alexey Grigorev
  text: How do we know it's time to add ML to our search pipeline?
  replies: []
- name: Alexey Grigorev
  text: And finally, what's the easiest way of adding ML to our search pipeline? let's
    say we already have search on our platform, and use solr or elasticsearch for
    indexing all the documents
  replies:
  - name: Doug Turnbull
    text: "This is really tough, and depends so much on the org. Some teams become\
      \ Lucene experts and get into the nitty gritty of modifying the guts of the\
      \ search engine. These teams tend to be very engineering heavy and don\u2019\
      t mind doing this kind of work. This solution is nice because it turns your\
      \ search engine into a \u201Cone stop shop\u201D, without needing extra services,\
      \ to solve your search problems.\nBut of course, if you\u2019re more data scientist\
      \ heavy, you\u2019d prefer to work in python as much as possible \U0001F642\
      \ Such teams tend to build search services that front the search system. The\
      \ nice thing about this is its not a single point of failure, you can fallover\
      \ to Solr or Elasticsearch if the service becomes unavailable.\nOf course, my\
      \ dream solution would be a search service that lets me host and run the python\
      \ stack as the query side, exposing to my python code the underlying data structures.\
      \ Or something that lets me deploy tensorflow or other models into the engine.\
      \ The closest things out there are Vespa or Jina from what I\u2019ve seen\u2026"
- name: Doug Turnbull
  text: "I\u2019ll ask a question! What does your search, discovery, or recommendations\
    \ platform look like at a high level? What do you like, dislike about it? (For\
    \ example, do you just use Elasticsearch, or do you use Vespa fronted by a Java\
    \ service? etc etc)"
  replies:
  - name: Alexey Grigorev
    text: "Is it a question for you Doug Turnbull or for us? \U0001F606"
  - name: Doug Turnbull
    text: "Oh for all of you sorry \U0001F61B"
  - name: Alexey Grigorev
    text: Maybe Cristian Javier Martinez can say a few words about OLX =)
  - name: xnot
    text: The one I'm working on right now is pretty simple at a high level. LB-&gt;
      Gateway -&gt; Reco/Search Backend -&gt; ES/Redis
  - name: xnot
    text: Backend is written in Go. Using official lib of es to connect to it. Redis
      is used for caching of user historical features / recently watched items which
      we then use for reco
  - name: xnot
    text: Don't use any vector search engine right now. Content size is small enough
      that we got away with in memory ann index which gets built on service startup
      (this is used to serve reco)
  - name: xnot
    text: What I don't like - quality of query understanding + spelling correction
      components, lack of good quality labelled data so to build good classifiers,
      ES's json based DSL is a pain, want to eventually decouple ANN from this system
- name: Rishabh Bhargava
  text: "Doug Turnbull thanks for doing this! \nI\u2019m curious to understand how\
    \ the best teams measure and understand performance of their search systems on\
    \ an ongoing basis. What are the dashboards and alerts they\u2019ll set up, and\
    \ how do they use those to make incremental improvements to their search models?"
  replies:
  - name: Doug Turnbull
    text: "good question! It takes a lot of different effort and a deep appreciation\
      \ of the pros and cons of different metrics:\n- Human ratings, including judgments\
      \ (evaluation of relevance of each result) and whole SERP evaluation (how \u2018\
      good\u2019 does this search results page look)\n- General search conversion\
      \ rates over time (though these can be influenced by factors like checkout or\
      \ product page design)\n- Search CTR (understanding this is a combination of\
      \ relevance, UX, perf). Another flaw here is users won\u2019t click if they\
      \ get their answer from the Search UX itself\n- Roundtrip latency to the user\
      \ and other performance metrics, like p90 latency, etc. Super critical and highly\
      \ correlated with performance\n- Best and worst performing queries -&gt; a great\
      \ product person can analyze to see what patterns you do well / do poorly with\n\
      - Typeahead success: after users clickthrough to a typeahead query suggestion,\
      \ do they take a follow on action or was the click in the end perhaps not so\
      \ great\n- Content performance: what content does well / poorly in the search\
      \ system? Are there areas where the content itself needs to be tuned to be more\
      \ findable\nProbably a ton others, but the really great teams, work really really\
      \ hard here. It takes a lot of great data work to make use of these metrics!"
  - name: Rishabh Bhargava
    text: 'This is super interesting. Quick follow-up: how do teams quantify best
      and worst performing queries?'
- name: Tim Becker
  text: Hi Doug Turnbull, interesting book! I have some basic questions for you.
  replies: []
- name: Tim Becker
  text: '- Could you please explain what a search engine actually is?'
  replies:
  - name: Doug Turnbull
    text: 'omg I have no idea. Some people use the term to mean just the technology
      that serves results from sparse (classic inverted) or dense vector (approximate
      nearest neighbor) indices. This is a piece of infrastructure

      Other people use the term to refer to a full search solution that solves a specific
      problem. In the latter case lots of pieces of infra can be involved, not just
      the index-serving part but query understanding and rerannkig layers'
- name: Tim Becker
  text: '- What kind of ML models are usually applied to search problems?'
  replies:
  - name: Doug Turnbull
    text: Classically GBDT (Gradient Boosted Decision Trees) have worked well and
      fast for ranking, as these play well with existing technologies. But increasingly,
      the problem can be distilled to similarity function modeled in a nearest-neighbor
      index. This similarity might be the result of an embedding generated from a
      deep learning or other model
- name: Tim Becker
  text: '- What was the most exiting AI powered search problem you have been working
    on?'
  replies:
  - name: Doug Turnbull
    text: "Aside from Shopify, I got to work on the Elasticsearch Learning to Rank\
      \ plugin that helps power Wikipedia search. Exciting from a tech, data, and\
      \ impact perspective \U0001F642 Also very high scale!"
  - name: Tim Becker
    text: "cool! Thank you for your answers \U0001F642"
- name: Adhi
  text: Doug Turnbull any thoughts on the right way to combine filtering and nearest
    neighbor search? do we do the former first and then the latter or the other way
    around? is there a way to do both reliably?
  replies:
  - name: Doug Turnbull
    text: "I actually don\u2019t know \U0001F605\nWith a faster NN index, I\u2019\
      d like to do the NN part first as it helps improve recall. Then filter out candidates.\
      \ But I think combining the two is still an art, and very much an open area\
      \ of research"

---

Great search is all about delivering the right results. Today’s search engines are expected to be smart,
understanding the nuances of natural language queries, as well as each user’s preferences and context.
AI-Powered Search teaches you the latest machine learning techniques to create search engines
that continuously learn from your users and your content, to drive more domain-aware and intelligent search.

This book empowers you to create and deploy search engines that take advantage of user interactions and
the hidden semantic relationships in your content to constantly get smarter and automatically deliver
better, more relevant search experiences.
