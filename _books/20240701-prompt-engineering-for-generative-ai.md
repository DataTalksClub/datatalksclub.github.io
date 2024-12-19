---
authors:
- michaeltaylor
- jamesphoenix
cover: images/books/20240701-prompt-engineering-for-generative-ai/cover.jpg
description: Book of the Week. Prompt Engineering for Generative AI by Michael Taylor
  and James Phoenix
end: 2024-07-05 23:59:59
image: images/books/20240701-prompt-engineering-for-generative-ai/preview.jpg
links:
- link: https://www.oreilly.com/library/view/prompt-engineering-for/9781098153427/
  text: Book's page
- link: https://www.amazon.com/Prompt-Engineering-Generative-AI-Future-Proof/dp/109815343X
  text: Buy on Amazon
start: 2024-07-01 00:00:00
title: Prompt Engineering for Generative AI

archive:
- name: Max
  text: 'Hi James and Mike.

    As models become more smarter, do you think prompt engineering will be as useful
    - or emphasized - as it is now? Maybe smarter models would be able to understand
    even the less curated prompts? Just like ChatGPT is able to overlook typos in
    queries...'
  replies:
  - name: James Phoenix
    text: 'Heyas Max

      More powerful models will likely require less curated prompts, however generally
      more rich context will even help these models.'
  - name: James Phoenix
    text: I still think prompt engineering will be useful in the sense of task direction
      and task execution.
  - name: James Phoenix
    text: Also, as models grow in both parameter and context window size, previously
      impossible tasks will become possible.
  - name: Mike Taylor
    text: Yes I agree with James that prompting may be less curated with larger models.
      But humans are pretty intelligent and we still need prompting in the form of
      legal, HR, management to align us towards business goals.
- name: Ruddi Rodriguez
  text: Hi James and Mike , Do you think that we will find consistent results for
    same applications across different platforms or companies based on prompts ?
  replies:
  - name: James Phoenix
    text: I would say that this is unlikely, unless they are using the same models.
      Each model has different training data with it's own nuance.
  - name: Mike Taylor
    text: 'I am seeing them diverge in personality: for example talking to Claude
      is already a really different experience from ChatGPT.'
- name: Ruddi Rodriguez
  text: Another question , what in your opinion should be the best way to test different
    prompts when is about generative ? I use another llm to verify the information
    , but sometimes can be like an infinite loop.
  replies:
  - name: James Phoenix
    text: 'Give this a read: [https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/)

      I think in-context learning is important via few shot examples.'
  - name: James Phoenix
    text: Also for when you have cyclical activities with self-reflection (i.e. checking
      the input/output) several times, you will need to have a maximum number of iterations.
  - name: James Phoenix
    text: 'Have a look at this for reflection: [https://github.com/langchain-ai/langgraph/blob/main/examples/reflection/reflection.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/reflection/reflection.ipynb)'
  - name: Mike Taylor
    text: I prefer to use an LLM that has access to the internet for verification.
      For example perplexity or Tavily
  - name: Ruddi Rodriguez
    text: In theory you can instruct gpt to search in internet , using langchain for
      example , it is possible.
  - name: Mike Taylor
    text: Yes exactly but they use one of these tools under the hood of the framework.
      I think serpapi is what they use in the tutorials unless they updated them.
- name: Ruddi Rodriguez
  text: What do you think should be the best approach for production ,in terms of
    prompt generation ? To use platforms like langchain or to build everything from
    zero . The use of platformas like langchain looks to me help to the developer
    to focus in more essential.
  replies:
  - name: James Phoenix
    text: 'I''d recommend using LangChain, because you can easily switch out the models
      very easily.

      Also I''d recommend having a look at LangGraph for stateful actors.'
  - name: Mike Taylor
    text: I prefer a simpler approach of just using the OpenAI library before you
      have product market fit. But LangChain can be a useful abstraction in production
      and is really the standard framework to use, so perhaps it's easier to hire
      other AI engineers with transferrable experience.
  - name: Ruddi Rodriguez
    text: the problem I have found with langchain is that you take into production
      a framework that you do not have control over it. You already have a model that
      you do not control , so using another framework that you do not own , can be
      problematic for production. I would said use langchain for prototype and use
      a custom home-made framework  for production?
  - name: Mike Taylor
    text: Well yes but that's true of all frameworks. You just have to take the choice
      of whether the framework adds more than it takes away. i.e. does giving up some
      control make things easier to maintain or add new features. If you're not planning
      on using LangChain in production I would argue it's too much overhead to learn
      it just for a prototype.
- name: Plinio Zanini
  text: In what type of problems would a few-shot classification model using LLM be
    able to obtain good performance compared to traditional ML methods?
  replies:
  - name: James Phoenix
    text: Wherever there is good pre-training data within the model. So sentiment
      analysis would likely be good.
  - name: James Phoenix
    text: 'Your mileage may vary depending upon the use case, so I''d recommend doing
      this workflow:

      0 shot --&gt; Few shot --&gt; LLM fine tuning --&gt; More traditional classification
      model'
  - name: Mike Taylor
    text: Yes agreed my approach is to be lazy and use a few shot prompt first, then
      optimize for cost later when I have enough data to build a traditional ML classifier.
- name: Plinio Zanini
  text: How does the prompting change when using different models? Should a prompt
    change significantly from a simpler smaller model than ca be run locally vs the
    GPT4, for example?
  replies:
  - name: James Phoenix
    text: For less capable models, you will need to tweak/iterate the prompt and provide
      much better K-shot few learning examples.
  - name: Mike Taylor
    text: Usually you need many more examples for smaller models, and more optimized
      instructions.
- name: Plinio Zanini
  text: How to figure out when a model is simply not good enough for prompt engineering
    to do the trick and fine tunning or a more capable model (potentially bigger)
    should be used?
  replies:
  - name: James Phoenix
    text: You should use evaluations, i.e. programmatic or LLM based.
  - name: James Phoenix
    text: '[https://python.langchain.com/v0.2/docs/concepts/#evaluation](https://python.langchain.com/v0.2/docs/concepts/#evaluation)'
  - name: Mike Taylor
    text: For me I tend to see few shot prompting comfortably boost performance 10
      to 20 pergectage points and a further 5-10 from optimizing instructions. So
      if you're currently getting 50% accuracy and you need to get to 80% accuracy
      on a task that gap is realistic to close just by prompting.
- name: Marcin Mazur
  text: Hi, can you recommend any reliable methods of structure enforcement that are
    not simple masking of logits? If answer is yes, have you seen any of them used
    in prod?
  replies:
  - name: Marcin Mazur
    text: "When I say \"reliable\" I mean methods that are on a par with masking \U0001F609"
  - name: James Phoenix
    text: 'I don''t think there is a predictable way apart from enforcing the logits
      to a specific structure.

      My advice would be to use a more powerful model if the schema is complex, and
      have a re-try + fix mechanism.'
  - name: James Phoenix
    text: Also always remember to use JSON mode.
  - name: Ruddi Rodriguez
    text: What do you mean with json mode ? Function call ?
  - name: James Phoenix
    text: '[https://platform.openai.com/docs/guides/text-generation/json-mode](https://platform.openai.com/docs/guides/text-generation/json-mode)'
  - name: Mike Taylor
    text: There's also the concept of Grammars in open source models (introduced by
      llama.cpp I believe) which enforce specific tokens.
- name: Prashant
  text: What is the best way to capture all the variants of a prompt with their result
    to make a decision later? Any suggested tools or approach to make this efficient?
  replies:
  - name: Mike Taylor
    text: I personally use LangSmith or I manually log them to a spreadsheet. Others
      use weights and biases, or similar logging tools. There are tonnes and I don't
      think it's clear yet who will be market leader so try a few and use whichever
      you like best.
- name: Max
  text: Which library/tool do you recommend that does a systematic evaluation of different
    prompting techniques? I see one by Microsoft called 'Prompt Engine'
  replies:
  - name: Mike Taylor
    text: Can you elaborate by what you mean by a systematic evaluation? I typically
      have custom evaluation metrics and manually a/b test prompts in a jupyter notebook.
      I haven't found any one tool to be that useful.
  - name: Max
    text: '&gt; Can you elaborate by what you mean by a systematic evaluation?

      You have a dataset (of QnA) and you prompt with different techniques and see
      which prompt gets you the best result. e.g. while testing Meditron - a healthcare
      LM - the developers found that SC-CoT was the best prompt. So they must have
      run different prompts for the same queries to see which one yields the best
      result.

      &gt; I haven''t found any one tool to be that useful.

      I saw one:  ''Prompt Engine'' by Microsoft; I just found that it was difficult
      to extend.'
  - name: Mike Taylor
    text: Ah yes for this I just do custom evaluation metrics and apply them to a
      pandas data frame. Also haven't found a library that's any good.
  - name: Max
    text: Thanks.
- name: Kathryn Armitstead
  text: 'We hear alot about AI research and developments, but in practice it seems
    that most companies do not have Gen AI in production - particularly small to medium
    size companies. Assuming you agree with this perspective, how do you see it changing
    over the next few years and what will enable smaller companies to take advantage
    of the new capabilities?

    thanks (it looks a great book from the reviews!)'
  replies:
  - name: Mike Taylor
    text: Almost every company has gen AI projects but very few of them are in production.
      That'll change fairly rapidly over the next year in my opinion as people get
      better at testing and evaluation. Also when we see a GPT-4 level open source
      model more small businesses and startups will form, just like we saw with stable
      diffusion. Too risky to build your business entirely on OpenAI in my opinion
      though some people have been successful with it.
  - name: Ruddi Rodriguez
    text: My company has several products in productions that use GenAi and we are
      developing more and the strategy in the long term is to use lees OpenAi. However
      until now it still cheaper and more efficiently to use OpenAi than created the
      infrastructure to run  powerful models locally. Now that is the bottle neck
      not even the model quality itself.
- name: Ruddi Rodriguez
  text: 'Hi James and Mike

    Thank you for taking your time to answer so far, I have another question . I am
    working in a problem where based in a list of questions-answer that characterized  a
    persona attributes, I generated descriptions of different aspect of the personality.
    I realized that the model uses a selection of the questions-answer instead of
    based the description in all of them. Eventually if you run the same profile several
    times , you will find that some questions are use more than others , with a huge
    amount of runs it will use at least once all the questions , but the frequency
    distribution is like exponential with some questions used more frequently and
    others much less. I assumed this is a way for the model to optimize the token
    it use.

    Giving this I see 3 different ways to approach this

    1- To do nothing and let the model to be free selecting questions-answers .

    2- After several experiments to use the most frequent questions. However, I do
    think that can be a case where one of the lees frequent  question will be relevant
    .

    3- Reshape the prompt to force the model to use all the information.

    In your opinion what could be a good approach ? of course this need to be tested
    , but in a first sight , thanksss'
  replies:
  - name: James Phoenix
    text: 'I suggest 3. Reshape the prompt to force the model to use all the information.

      Because as long as you know the right questions, you can base your application
      code/logic, knowing that at least the same questions will be answered.'
  - name: James Phoenix
    text: Unless the aim of the application is to provide maximum personalization
      for the user, then I would favour free form of any question.
  - name: James Phoenix
    text: But even then, I would have a `score` or `engagement_score` field, for ordering/ranking
      free-form questions.
  - name: Mike Taylor
    text: 'If you''re doing character personas character AI has a really great guide
      that gives you some tricks for giving personality to characters: [https://book.character.ai/character-book/advanced-creation/setting-a-scene](https://book.character.ai/character-book/advanced-creation/setting-a-scene)'
  - name: Ruddi Rodriguez
    text: thankssss for the answers , Indeed I am developing a pipeline top assign
      personality to a Ai persona, i did not know the character ai resource , thanks
      again. My major challenge so far have been to get the most real personality
      , since ChatGPT like I said in one of my questions above , has the tendency
      to create histories biased to a the most positive side. I do think is related
      to 2 factors , one that the internet corpus is full of happy end  histories
      people has the tendency to share those histories,  and probably all the checkpoints
      introduce in the model after the first version to avoid the model go crazy and
      misbehave.
  - name: Mike Taylor
    text: I find anthropic Claude has a better personality, and there are fine tuned
      versions of llama which have had some of the political correctness training
      removed
- name: Ruddi Rodriguez
  text: "Hi James thanks for all you answers , we recently found that when using a\
    \ nested json for a function call , sometimes some of the fields can be missed\
    \ , and it get worst with the deep of the json. It is possible to achieve same\
    \ result using prompt with indentation : `\"\"\"Your task is to parse an unstructured\
    \ request for a market research solution and turn it into a JSON containing the\
    \ most important information. The request can describe one or more designs for\
    \ different countries. The JSON should consist of the following information:`\n\
    `- Study (field name: \"study\", field type: str)`\n`- A list of markets (field\
    \ name: \"markets\", field type: array), where each market consists of:`\n  `-\
    \ The country name (field name: \"country\", field type: str)`\n  `- The city\
    \ name (field name: \"city\", field type: str, can be left empty if not mentioned)`\n\
    \  `- Additional information (field name: \"additional_information\", field type:\
    \ array) containing:` and declaring the type and examples of expected field. since\
    \ it is supposed that function call is one step ahead , the question is: would\
    \  be better to try to improve the json of the function call ? or coming back\
    \ the raw prompt with indentation as above is a good practice? Considering also\
    \ that a model like llama does not support function calls"
  replies:
  - name: James Phoenix
    text: If the JSON is very large, try breaking it down into separate requests,
      then combining that later on.
  - name: James Phoenix
    text: Alternatively you can tell the LLM that the fields are required.
  - name: Mike Taylor
    text: You can also add a step that tries to parse and check the Json and sends
      errors back to another LLM call that attempts to correct the Json result. I
      think lang chain lets you do that natively with output parsers but James Phoenix
      you know more about that.
  - name: Marcin Mazur
    text: "if u are interested in forcing types, structure I recommend you try this,\
      \ you can specify json schema too and lib will make sure to force appropriate\
      \ logits (worked pretty well in my last project \U0001F642)\n[https://github.com/outlines-dev/outlines](https://github.com/outlines-dev/outlines)"
  - name: Mike Taylor
    text: Yes this is great. I also like instructor [https://python.useinstructor.com/](https://python.useinstructor.com/)
- name: Ruddi Rodriguez
  text: Another question in your experience , how we can make the generated text more
    real and human, I am  working in a project to generated the  personality profile
    of a persona based on basic information of the persona and to be honest, it si
    hard to make the model to generate profiles without a history of resilience or
    avoid to use words like vibrant and others adjectives . I have instructed the
    prompt to use spartan vocabulary plain english , etc etc but it still hard.
  replies:
  - name: James Phoenix
    text: '- Increased temperature

      - Tell it to avoid common words that ChatGPT uses, i.e. imagine, delve

      - Also try Claude, I''ve heard it''s more natural than ChatGPT.'
  - name: Mike Taylor
    text: I found giving it multiple positive examples words better than telling it
      not to do something.
  - name: Mike Taylor
    text: But yes plus 1 on using Claude, it sounds way better and less like AI.
- name: Dr Abdulrahman Baqais
  text: 'Hello James:

    Do you think we need promptvengineering techniques for non-latin languages? Or
    just translating it to English is sufficent?'
  replies:
  - name: Mike Taylor
    text: I personally find it follows instructions better in English. Then you can
      add a translation step. But it is a messy conversion sometimes particularly
      for rarer languages.
- name: Dr Abdulrahman Baqais
  text: "A second question is: \nHow do you see the future of prompt engineering aftet\
    \ the release of DSPy?"
  replies:
  - name: Mike Taylor
    text: Using DSPy IS prompt engineering! The hard part has always been defining
      inputs/outputs for each step in the chain and settling on a good set of eval
      metrics, not trying different combinations of words to see what works. That
      part of prompt engineering will go away anyway in a few years with better models
      and changing words won't make as much difference (we saw this already with the
      shift to GPT-4 from GPT-3). In the meantime I'm using DSPy a fair bit for my
      work and it does quite well once you've done the hard work of designing the
      program and building a list of examples, and defining eval metrics. Highly recommend.
- name: Roman Zabolotin
  text: 'Hi James and Mike.

    I''ve had a look through your book and was very interested in the topics you cover.

    There is an opinion that the capabilities of LLMs grow with the size of their
    memory, and have now reached a threshold where only big players like OpenAI and
    Anthropic can train next-generation models. It seems that even Meta is not planning
    to make their next models publicly available. How do you see the future of the
    LLM market? Is there room for open-source solutions?'
  replies:
  - name: James Phoenix
    text: 'I think open source generally lags behind about 1 - 2 years.

      So as long as you are willing to wait open source is catching up.'
  - name: Mike Taylor
    text: Agreed although soon open source models will be too big to run on your computer.
      So you'll mostly use them through the cloud providers.
- name: Roman Zabolotin
  text: Fine-tuning is available for open-source models and some proprietary ones,
    while prompt engineering is universally applicable. In your experience, which
    approach tends to be more effective, and under what circumstances?
  replies:
  - name: James Phoenix
    text: 'Follow this workflow:

      1. No few shot examples (just a single prompt)

      2. Add few shot examples

      3. Optimize the prompt with few shot examples

      4. Fine tuning an LLM model

      5. Building a more traditional model i.e. a classifier with sci-kit learn /
      Keras / PyTorch.'
  - name: James Phoenix
    text: The important thing is that if you can solve the problem with less technology,
      then there is no need for fine tuning.
  - name: James Phoenix
    text: Fine tuning is better for when the LLM has not seen a lot of those tokens
      within the pre-training data.
  - name: Mike Taylor
    text: There was a paper we referenced in the book that showed prompting beat fine
      tuning all the way up to 2,000 examples of the task. The main issue is the best
      models don't allow fine tuning yet so GPT-4 few shot tends to beat gpt-3.5 fine
      tuned.
- name: Roman Zabolotin
  text: Additionally, I've noticed that prompts can sometimes become quite large,
    reaching 2000-3000 tokens per request, often due to numerous few-shot examples.
    Is this considered a normal practice in the industry? What are the trade-offs
    of using such large prompts compared to other methods like fine-tuning or more
    concise prompting strategies?
  replies:
  - name: James Phoenix
    text: You do get cost saving benefits with fine tuning because you no longer need
      to add in the few-shot learning examples, however if you don't have enough examples,
      then you can get degraded performance on a fine tuning model vs a standard model.
  - name: James Phoenix
    text: It really does matter how many samples you have fine tuned on.
  - name: Mike Taylor
    text: Yes the OpenAI system prompt for ChatGPT is 7k tokens!
- name: Ella
  text: 'Hi James and Mike.

    Been trying to grasp all the vocab and terms to understand content about LLMs
    and Generative AI.

    Do you have recommendations what core-concept and what methodologies we have to
    really really grasp like the back of our hand, as

    - models become smarter

    - tokens get faster and cheaper

    - context windows getting bigger and bigger?

    So that we can swap out the new models that seem to keep coming out each and every
    week?'
  replies:
  - name: James Phoenix
    text: '- Few shot learning will always be important (adding examples for direction)

      - Fine tuning is an important concept.

      - Breaking down complex tasks into multiple sub-problems will still be important
      until the model size is much larger.

      - I''d also recommend checking out LangChain for being able to easily switch
      out models in a single line of code.'
  - name: Mike Taylor
    text: Agree with this list but I'd just add RAG. Retrieval Augmented Generation.


---

Large language models (LLMs) and diffusion models such as ChatGPT and Stable Diffusion have unprecedented potential. Because they have been trained on all the public text and images on the internet, they can make useful contributions to a wide variety of tasks. And with the barrier to entry greatly reduced today, practically any developer can harness LLMs and diffusion models to tackle problems previously unsuitable for automation.

With this book, you'll gain a solid foundation in generative AI, including how to apply these models in practice. When first integrating LLMs and diffusion models into their workflows, most developers struggle to coax reliable enough results from them to use in automated systems. Authors James Phoenix and Mike Taylor show you how a set of principles called prompt engineering can enable you to work effectively with AI.

Learn how to empower AI to work for you. This book explains:

- The structure of the interaction chain of your program's AI model and the fine-grained steps in between
- How AI model requests arise from transforming the application problem into a document completion problem in the model training domain
- The influence of LLM and diffusion model architecture—and how to best interact with it
- How these principles apply in practice in the domains of natural language processing, text and image generation, and code