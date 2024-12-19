---
authors:
- sebastianraschka
cover: images/books/20241017-build-large-language-model-from-scratch/cover.jpg
description: Book of the Week. Build a Large Language Model (From Scratch) by Sebastian
  Raschka
end: 2024-10-20 23:59:59
image: images/books/20241017-build-large-language-model-from-scratch/preview.jpg
links:
- link: https://www.manning.com/books/build-a-large-language-model-from-scratch
  text: Book's page
- link: https://www.amazon.com/gp/product/1633437167
  text: Buy on Amazon
- link: https://github.com/rasbt/LLMs-from-scratch
  text: GitHub repository
start: 2024-10-14 00:00:00
title: Build a Large Language Model (From Scratch)

archive:
- name: Malik Hebbat
  text: Is the book feasible for every stage of experience also for experts? And has
    it code examples included that can also be used as templates (in specific cases)
    to modify? Thanks in advance! Malik
  replies:
  - name: Sebastian Raschka
    text: "I hope so \U0001F60A. And if they are not challenging enough, I do also\
      \ have plenty of bonus material in the GitHub repo here: [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)\n\
      This may also answer the question regarding the templates to modify \U0001F60A\
      . Actually, when I first started writing the book I wanted to move some of the\
      \ codes that are reused throughout the chapters into a Python package that readers\
      \ can pip-install and import from, but then I decided against it and made the\
      \ code in each folder self-contained so it\u2019s easier to just go in and edit,\
      \ which is nice for tinkering."
  - name: Malik Hebbat
    text: Thank you so much Sebastian. Sounds very good to me.
- name: Avinash More
  text: hi Sebastian Raschka What skills would you recommend acquiring to efficiently
    leverage large language models (LLMs) for solving real-world problems? I believe
    that while the number of experts building LLMs will be smaller and highly specialized,
    there will be a large number of developers using these models. What key skills
    should developers focus on to make the most effective use of LLMs?
  replies:
  - name: Sebastian Raschka
    text: "You are absolutely correct, I think there will only be a few experts truly\
      \ training LLMs from the ground up. However, I think it\u2019s important to\
      \ understand the process on a general level and have good understanding of how\
      \ the architectures look like. Because this helps making decisions which LLMs\
      \ to use in practice since there are more and more options out there.\nJust\
      \ as an example, Gemma-2 has a 2x larger vocabulary than Llama 3.2. This is\
      \ nice because this way you can fit more tokens into the context window, but\
      \ the trade-off is that the output projection layer will require more GPU memory.\
      \ And there are lots of these insights or understandings that come from a solid\
      \ understanding of how LLMs work. But for that, you don\u2019t need to be an\
      \ expert in building LLMs on a daily basis though."
- name: Low Kim Hoe
  text: Sebastian Raschka Nice to meet you! thanks for the great effort here to reply
    all of us question. Do you think it's necessary to understand deeply the architecture
    of LLM for the people using the LLM?
  replies:
  - name: Sebastian Raschka
    text: "Hi Low Kim Hoe! This is an absolutely warranted question, because it\u2019\
      s a bit of a time investment. However, I think it will pay off! I answered a\
      \ related question, and I think the answer would maybe apply here as well:\n\
      &gt;  However, I think it\u2019s important to understand the process on a general\
      \ level and have good understanding of how the architectures look like. Because\
      \ this helps making decisions which LLMs to use in practice since there are\
      \ more and more options out there.\n&gt; \n&gt; Just as an example, Gemma-2\
      \ has a 2x larger vocabulary than Llama 3.2. This is nice because this way you\
      \ can fit more tokens into the context window, but the trade-off is that the\
      \ output projection layer will require more GPU memory. And there are lots of\
      \ these insights or understandings that come from a solid understanding of how\
      \ LLMs work. But for that, you don\u2019t need to be an expert in building LLMs\
      \ on a daily basis though.\nPlease let me know in case you have any follow-up\
      \ questions!"
- name: Chintan Gotecha
  text: Sebastian Raschka -- The book's github repo is actively growing super fast;
    please let know any kind of help is required there.
  replies:
  - name: Sebastian Raschka
    text: "Thanks for asking! Actually, there\u2019s currently no help required; I\
      \ am mainly typing up some of notes in a nicer formats and sometimes also address\
      \ reader questions with those. I have a list of some more that I plan to add\
      \ over the next few months. Thanks!"
- name: Tim Becker
  text: 'Hi Sebastian Raschka, thank you very much for taking the time to answer our
    questions. There have already been a lot of good questions. I hope you still have
    some time to look at mine. I would appreciate it a lot.

    - In your opinion, what are the most promising trends in LLM development? Beyond
    simply increasing model size, what new directions do you see for LLM research?
    Are there specific areas, like interpretability or reasoning, or domain-specific
    enhancements that excite you?

    - What do you consider the biggest challenges to further improving LLMs? Are there
    intrinsic limitations that we may never be able to overcome with this technology?
    For instance, could there be a point where scaling up no longer yields significant
    gains?

    - Do you think LLMs could replace software engineers and data scientists in the
    near future? Alternatively, could they significantly augment our capabilities,
    potentially leading to fewer jobs? What role do you see LLMs playing in enabling
    non-technical roles, like product managers, to handle technical aspects of product
    development without developer support?

    - In your view, are there specific application areas where LLMs are unsuitable
    or even potentially harmful? For example, would you recommend against their use
    in certain high-stakes domains, such as medical or legal advising, due to accuracy
    or ethical concerns?'
  replies:
  - name: Sebastian Raschka
    text: "&gt;  In your opinion, what are the most promising trends in LLM development?\
      \ Beyond simply increasing model size, what new directions do you see for LLM\
      \ research? Are there specific areas, like interpretability or reasoning, or\
      \ domain-specific enhancements that excite you?\nThe architecture changes of\
      \ the state-of-the-art LLMs are actually relatively minor. Most of the progress\
      \ seems to come from improving the training recipes. I wrote more about it here\
      \ ([https://magazine.sebastianraschka.com/p/new-llm-pre-training-and-post-training](https://magazine.sebastianraschka.com/p/new-llm-pre-training-and-post-training))\
      \ if you are interested.\n&gt;  What do you consider the biggest challenges\
      \ to further improving LLMs? Are there intrinsic limitations that we may never\
      \ be able to overcome with this technology? For instance, could there be a point\
      \ where scaling up no longer yields significant gains?\nGood question. Actually,\
      \ I think we already stopped scaling up. E.g., after the release of GPT-4 I\
      \ don\u2019t think OpenAI (or others) released a bigger more scaled up model\
      \ (haha, I may be proven wrong if/when GPT-5 is released one day). Instead,\
      \ the focus was/is more on making models smaller and cheaper. That being said,\
      \ there are interesting new approaches to get more out of the model (E.g,. see\
      \ the GPT o1 model).\n&gt;  Do you think LLMs could replace software engineers\
      \ and data scientists in the near future? Alternatively, could they significantly\
      \ augment our capabilities, potentially leading to fewer jobs? What role do\
      \ you see LLMs playing in enabling non-technical roles, like product managers,\
      \ to handle technical aspects of product development without developer support?\n\
      Unfortunately, I can\u2019t really comment on that. I think it is likely going\
      \ to be similar to the introduction of computers or the internet back then.\
      \ Some jobs will be more automated, some jobs will go away, and some jobs will\
      \ be created, and some jobs will be unaffected.\n&gt;  In your view, are there\
      \ specific application areas where LLMs are unsuitable or even potentially harmful?\
      \ For example, would you recommend against their use in certain high-stakes\
      \ domains, such as medical or legal advising, due to accuracy or ethical concerns?\n\
      That\u2019s another tricky question \U0001F605. I think it all comes down to\
      \ using the technology responsibly. You mentioned medical domains. Fully automating\
      \ a medical diagnosis with LLMs is probably irresponsible (right now). However,\
      \ I don\u2019t think that LLMs are necessarily harmful here\u2026it all depends\
      \ on the user and usecase.\nImagine you are a doctor and have a patient where\
      \ you are not exactly sure what the patient\u2019s health issue is. Given the\
      \ symptoms, you could ask an LLM to suggest potential diagnoses. Then, as a\
      \ doctor, you can carefully examine those, check the literature, and maybe come\
      \ up with a diagnosis you otherwise wouldn\u2019t have thought of. I.e., the\
      \ LLM could be used here to see things that you otherwise would miss."
  - name: Tim Becker
    text: "Sebastian Raschka thank you for your answers \U0001F642 I will definitely\
      \ have a look! Let's see what the future brings!"
- name: Sebastian Raschka
  text: "Hi all, it\u2019s crazy timing but I woke up with a fever today. I appreciate\
    \ the interest and questions and promise I will get to them when I am feeling\
    \ a bit better. Please don\u2019t worry and keep the questions coming"
  replies:
  - name: Daniel Kleine
    text: "Get well soon! \U0001F340"
  - name: Abm Adnan Azmee
    text: Hope you get well soon!
  - name: Vivien S.
    text: hope you feel better soon!
  - name: Rileen Sinha
    text: Gute Besserung!
  - name: Moaaz Khokhar
    text: "Get well soon \U0001F33F"
- name: Rileen Sinha
  text: Sebastian Raschka - I'm looking forward to diving into your book, which teaches
    us how to build a GPT-2 like LLM from scratch. Are there any books you'd recommend
    for the next stages, i.e. working with the best LLMs of today and tomorrow? Also,
    are there any books on ML-DL (besides the 4th edition of your own) that you'd
    recommend? Thanks so much!
  replies:
  - name: Sebastian Raschka
    text: "Thanks for your interest in my book. Actually, I am not super aware of\
      \ a good follow-up book at the moment (I\u2019ve been in the zone writing the\
      \ book and haven\u2019t had much time to read anything besides research papers\
      \ for the last couple of months).\nThat being said. for the next stages, I have\
      \ a GPT-2 to Llama 3.2 guide here that could be a good follow-up: [https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/07_gpt_to_llama](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/07_gpt_to_llama)\n\
      Another thing that may be interesting to study is LitGPT, a open-source library\
      \ I help developing: [https://github.com/Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)\n\
      I am mentioning it because it implements a variety of LLMs, but the code base\
      \ is kept relatively readable. I think there you could get a good understanding\
      \ of how the different LLM architectures (Phi, Llama, Gemini, Mistral) etc compare.\
      \  Of course, it\u2019s not a tutorial, but maybe it\u2019s useful!"
  - name: Rileen Sinha
    text: Thanks, I'll definitely check those two out. I'm also planning to look at
      Jay Alammar's new book - looks promising. Hope you're feeling much better now!
  - name: Sebastian Raschka
    text: "Thanks, Rileen! I actually just got an ebook copy of the book and it looks\
      \ super interesting. It\u2019s more of a survey book but I think it would work\
      \ in both ways:\n1. Reading it before the Build an LLM from Scratch book for\
      \ a top-down-view to see what types of LLMs and applications are down there,\
      \ then diving into \u201CBuild an LLM from Scratch\u201D to understand how LLMs\
      \ work.\n2. Reading it after Build an LLM from Scratch, after getting a good\
      \ understanding of how LLMs work, and then reading gaining an understanding\
      \ of what other applications and usecases are out there"
  - name: Rileen Sinha
    text: Thanks! I'm inclined to go for option 2, so that I can potentially add a
      few projects to the ones I did while doing the "LLM Zoomcamp" course with Alexey,
      and then get under the hood with your book. Looking forward to both!
- name: Abm Adnan Azmee
  text: Hi Sebastian Raschka, Since LLM technology is advancing rapidly, what is the
    best approach for a beginner to get started in this field?
  replies:
  - name: Sebastian Raschka
    text: "You are absolutely right, keeping up with the latest developments can be\
      \ a fulltime job itself.\nFortunately, there are active online communities (lots\
      \ of blogs, newsletters, and others such as the LocalLlama subreddit) where\
      \ interesting new developments are shared. Once you understand the basics, you\u2019\
      ll see that most of these are just extensions.\nI recorded a short video a few\
      \ weeks ago to discuss/show how most is still based on the original GPT architecture:\
      \ [https://www.youtube.com/watch?v=itIab9ZTAqk](https://www.youtube.com/watch?v=itIab9ZTAqk)"
- name: Harshit Lamba
  text: Hi Sebastian Raschka, hope you are feeling good! I have an application based
    question - in a corporate setting, we usually do the pilot runs using LLMs to
    get the clients onboarded and then don't know where to go from there. In traditional
    and advanced machine learning (for instance, spam detection problem), we still
    get some pointers regarding the things to try, such as improved pre-processing,
    n-grams, tuning sequence models etc. But when we use LLMs there is a little scope
    of tuning the model and clearly we can't think of pre-processing as the model
    is already that advanced. So what next should we take?
  replies:
  - name: Sebastian Raschka
    text: "Thanks, I am slowly getting better \U0001F60A.\nI think that\u2019s a good\
      \ question, and it depends a bit on the use case. There\u2019s always something\
      \ you can improve.\nFinetuning on custom data is usually always an option if\
      \ the domain and application benefits from custom data. Here, the same rules\
      \ apply as in classic ML: the dataset quality and format matters. This includes\
      \ many factors:\n- inclusion of synthetic data\n- dataset ratio/mixing\n- quantity\
      \ and quality\n- formatting\n- etc.\nBut let\u2019s assume you are not interested\
      \ in finetuning. Still there are lots of ways to improve the model. In this\
      \ case, the most substantial one would probably be prompt engineering."
- name: RAVI SHEKHAR TIWARI
  text: Hi Sebastian Raschka  llm are very good at representation of the features
    by considering global and local features. It this possible we can implement the
    concept of fine granularity and course granularity inside llm to represent features
    and then used multi headed attention based on the use case without specifying
    explicitly
  replies:
  - name: Sebastian Raschka
    text: "Thanks for the question! I am not sure if I am understanding it correctly,\
      \ but let me give it a try! I think that accessing the features explicitly is\
      \ tricky. As a general rule of thumb the earlier layers access more of the fine-grained\
      \ feature information and the later layers capture more of the coarse-grained\
      \ features. Then the different heads in multi-head attention access different\
      \ aspects of these features. Beyond that, I am not not aware of any approach\
      \ that codes things more explicitly, except maybe Alphafold 2, which coded geometric\
      \ constraints (it\u2019s not an LLM per-se but LLM-adjacent); however, even\
      \ they found that this is not necessary and dropped that in their recent AlphaFold\
      \ model."
- name: Ruslan Nuriev
  text: Hello, I couldn't make it to the QA session because of my classes. Is there
    going to be any event with Sebastian Raschka in the near future?
  replies:
  - name: Alexey Grigorev
    text: Hopefully!
- name: Sebastian Raschka
  text: "Hey everyone!\nThank you all so much for participating! The questions were\
    \ fantastic \U0001F60A, and I really appreciated the interest! Unfortunately,\
    \ I came down with a fever this week, but I did my best to respond to almost everyone.\
    \ (There are a few questions I haven\u2019t responded to yet, but I will do so\
    \ in the next few days as I get better.)\nAlso, big thanks to the organizers Alexey\
    \ Grigorev and Anj for making this happen! \U0001F64C\nAnd, of course, congratulations\
    \ to the winners! I hope the book will be a valuable resource for your work and\
    \ career \U0001F38A. Looking under the hood of an LLM and implementing one from\
    \ the ground up is a time investment (versus just taking a shortcut and using\
    \ a third-party service or library).\nHowever, I think that it\u2019s similar\
    \ to learning math fundamentals if you are a data scientist, for example. Sure,\
    \ we are not going to implement our own code functions to implement matrix multiplication,\
    \ hypothesis text, and so forth in our everyday work. But I think that doing it\
    \ by hand and (/coding it up) once as an exercise can be super useful to really\
    \ understand how these things work.\nWishing you all a great weekend!"
  replies:
  - name: Alexey Grigorev
    text: Thank you Sebastian! It was a big pleasure hosting  you!
  - name: Malik Hebbat
    text: As a reader and questioner I also wanted to thank all the Organizers and
      Sebastian himself for the whole thread. Very useful, also in future. Hope you
      are better and healthy now Sebastian. All the best for you.
  - name: Sebastian Raschka
    text: Thanks, Malik Hebbat!
  - name: Chintan Gotecha
    text: Just ordered my copy; turns out Amazon India takes 1 month to deliver!
  - name: Chintan Gotecha
    text: Received my copy today Sebastian Raschka, thank you and best wishes from
      India.
- name: Standing-Appa
  text: Hi Sebastian Raschka I hope you are feeling better soon. I wanted to ask what
    you think about Mamba (Jamba) and State-Space Models. Do you think they will scale
    well and what are their advantages (e.g. Genetic Data) compared to Transformers?
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s an excellent question. I think they are very interesting and\
      \ refreshing, actually! I do think these approaches are currently still limited.\n\
      There hasn\u2019t been a competitive state space model-based LLM as far as I\
      \ know. With competitive, I mean GPT-4 or Llama 3.2 quality.\nI often wonder\
      \ whether it\u2019s\na) state space models are too limited (actually, this is\
      \ partly true, which is why Jamba and Samba are now transformer-hybrids)\nb)\
      \ researchers who are working on it don\u2019t have the budget to scale it more\n\
      c) there hasn\u2019t been that much interest yet\nMaybe all of the 3 are a bit\
      \ true. In any case, I think they are interesting and academic benchmarks in\
      \ the respective papers don\u2019t look too bad. But as far as I recall the\
      \ benchmarks are mostly multiple-choice based, like MMLU. I am haven\u2019t\
      \ seen any state space model in a conversational benchmark to test the text\
      \ writing/response quality (but maybe I missed that).\nMaybe for genetic data\
      \ these models can be quite useful though because they don\u2019t need to conversational\
      \ chatbots. And they scale very well. I think one of the first state space models\
      \ was actually used in that context ([https://arxiv.org/abs/2306.15794](https://arxiv.org/abs/2306.15794))"
  - name: Standing-Appa
    text: 'Thank you very much for your answer.

      There was something from Nivida, but it was taken down, where they trained a
      chatbot based on Mamba:

      - [https://developer.nvidia.com/blog/performance-efficient-mamba-chat-from-nvidia-ai-foundation-models/](https://developer.nvidia.com/blog/performance-efficient-mamba-chat-from-nvidia-ai-foundation-models/)

      For genetics they did it in this research:

      - [https://arxiv.org/abs/2403.03234](https://arxiv.org/abs/2403.03234)

      I was just wondering from your intution how these models work (especially Transformers)
      if you could see if they acutally could work. Because I actually tried to rap
      my head the state space models but wasn''t really convinced that they actually
      have a attention that could be as powerful as the one from Transformers.'
- name: Standing-Appa
  text: 'And since you are an expert and maybe a bit out of the scope of just the
    book:

    What is the best embedding model for text, particularly for downstream classification
    tasks? I''ve often heard that Transformer embeddings might not be ideal for such
    tasks, since "they don''t mean that much". What are your thoughts on the LLM2Vec
    approach?

    My goal is to embed long clinical texts for classification, but my dataset is
    relatively small. Would it be more effective to use a pre-trained model and fine-tune
    it, or is training a Transformer from scratch a viable option? Additionally, would
    a bidirectional encoder be more suitable (even given the smaller context size)
    than a decoder-only model for this purpose (and which layer is the most informative
    and how to some the layers), or is there a different approach that might work
    better?'
  replies:
  - name: Sebastian Raschka
    text: "Another great question!\nWith \u201CTransformer\u201D,\n1. do you mean\
      \ literally the original transformer architecture (encoder-decoder) \n2. or\
      \ do you mean just transformer-based LLMs like BERT, Llama, GPT in general?\
      \ \n(Just asking because your previous question was about state space models.)\n\
      In case you mean 1, then I would say then that actually both encoder- and decoder-style\
      \ models can work well. (There was a related question here: [https://datatalks-club.slack.com/archives/C01H403LKG8/p1729084855205539?thread_ts=1728923923.942779&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1729084855205539?thread_ts=1728923923.942779&amp;cid=C01H403LKG8))\n\
      In fact, in chapter 6 we trained a decoder-style GPT model for classification\
      \ (attaching a linear layer to the output embeddings) and get like 97% spam\
      \ classification accuracy on balanced dataset. Or 92% classification accuracy\
      \ on the balanced 50k IMDB movie review dataset (the 3x larger RoBERTa model\
      \ was only 1% better)."
  - name: Standing-Appa
    text: "I mean transformers in general. I will also probably compare with a State\
      \ Space Model or Hybrid form and then see what works best and compare them.\
      \ It is often claimed that the State Space Models would work as good even when\
      \ they have less parameters.\nFor the project, a pretrained decoder-Style model,\
      \ finetuned on the task, will probably work the best, since also the language\
      \ shouldn't be too far out of distribution.\nFor the Encoder-Style model like\
      \ Bert I think they are better for Sentence embeddings and downstream classifications\
      \ (but I am not sure, just what I read so far) but I am scared that their window\
      \ will be too small (if for example I am using a Sentence-BERT-Model) for my\
      \ long clinical texts.\nAnd maybe to point you to this again since I have no\
      \ intuition on that:\nWhat do you think about the LLM2Vec approach? Is there\
      \ something special to it than just taking the embedding and putting a linear\
      \ layer at the end?  [https://arxiv.org/abs/2404.05961](https://arxiv.org/abs/2404.05961)\n\
      And thank you very much for your answers to my two posts and the thoughts you\
      \ putted into them \U0001F642"
- name: Pastor Soto
  text: Hi. When you wrote this book do you have some profile in mind that you want
    it to explain the concepts (or did you write thinking about some general practitioners
    of LLMs)? Also, did you have concepts that were particularly tricky to simplify
    without losing essential depth?
  replies:
  - name: Sebastian Raschka
    text: "I think the book is for everyone who wants to understand how an LLM works,\
      \ not conceptually, but really how the mechanisms look like and how it functions.\n\
      A good target audience is also someone who is using a third party LLM library\
      \ like Hugging Face transformers and so forth, where LLMs are more of a black\
      \ box.\nIt\u2019s like people who want to understand how a motor in their car\
      \ works. You don\u2019t learn it by driving the car but by building your own\
      \ motor. Of course, if you build your own motor this won\u2019t be as fast as\
      \ a Ferrari or as reliable Honda. You probably won\u2019t use this motor in\
      \ your daily car. But building it and getting it to work will teach you a lot\
      \ about motors, way more than driving a car or looking at pictures of motors."
- name: Muneeb Khan
  text: '[https://datatalks-club.slack.com/archives/C01H403LKG8/p1729128841955499?thread_ts=1728975403.241789&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1729128841955499?thread_ts=1728975403.241789&amp;cid=C01H403LKG8)

    Hi, Sebastian Raschka. Thank you so much for your response. I hope you''re feeling
    much better now.

    The list is in fact open-ended, and as you mentioned, multi-label classification
    wouldn''t necessarily be appropriate since we may encounter new types of messages
    in the future. Essentially, my goal is to enable the small LLM to match the performance
    of the big LLM in summarizing the customer messages into a list of only *the _important_
    keywords*. So, the reference keywords  I use are just to enable the small LLM
    to learn to identify the important keywords. I want to be able to use a small
    LLM in a production setting for doing this task for future customer messages.'
  replies:
  - name: Sebastian Raschka
    text: In case you want to add new labels later on without having to retrain, then
      yes, I would probably not do the multi-label approach. Your approach could work,
      but you will need a relatively large dataset to finetune a model to do well
      here. Maybe 10k to 50k examples would be good. You could use a proprietary model
      to help with the dataset generation.
  - name: Muneeb Khan
    text: Thank you again for your response! I really appreciate it.
- name: Howard Ting
  text: 'Hi, Sebastian Raschka, hope you''re doing well! I have two questions:

    1. Do you think reinforcement learning will play a critical role in training LLMs
    in the future?

    2. Do you think there could be significant breakthroughs in learning theory in
    the coming years that would allow LLMs to require far less training data while
    developing reasoning abilities closer to human cognition?'
  replies:
  - name: Sebastian Raschka
    text: "1. Yes, I think RL will remain important. The first model that served in\
      \ ChatGPT (a variant of GPT-3 / InstructGPT) used RLHF+PPO (reinforcement learning\
      \ with human feedback based on proximal policy optimization). Then, researchers\
      \ and practitioners use a simpler variant called DPO, short for direct preference\
      \ optimization (e.g. Llama 3 and others). Neither RLHF nor DPO are like traditional\
      \ RL, but the concept of learning a policy that optimizes for user preferences\
      \ will remain important. Also, the recent OpenAI o1 model likely uses RL for\
      \ the chain of thought optimization.\n2. That\u2019s the billion dollar question.\
      \ I am not sure. I think everyone in deep learning is hoping for it, but no\
      \ one knows how it could work."
- name: Anj
  text: 'Hi everyone,

    As we wrap up this Book of the Week event, we want to thank you all for your insightful
    questions.

    A big thanks also goes to Sebastian Raschka for sharing their time and answering
    our queries.

    We appreciate your participation and look forward to seeing you again at the next
    event!'
  replies: []
- name: Prajwal Srinivas
  text: "Sebastian Raschka Hello!\n- What are you the most excited for, in the field\
    \ of LLMs?\n- How do you keep up and prioritise all the new stuff happening with\
    \ ML and LLMs?\n-  Any suggestions on what has worked the best for you for parsing\
    \ graphic and table heavy pdfs?\n- Any general tips/tricks would be appreciated\
    \ as well\nThank you \U0001F642"
  replies:
  - name: Sebastian Raschka
    text: "Hi there! There are good questions, and phew, non-technical questions are\
      \ actually hard to answer, haha! But let me give it a try!\n1. I am actually\
      \ quite excited that we recently got \u201Csmaller\u201D LLMs. I.e., the Llama\
      \ 3.2 1B and 3B models in particular are super interesting to me, because they\
      \ can be more conveniently used and finetuned on less expensive hardware. That\u2019\
      s super cool for tinkering and research. I am hoping to see more of this!\n\
      2. I tend to bookmark maybe 20-30 papers each month but nowadays only read 1-2\
      \ papers per week (usually one that is closely related to what I am currently\
      \ working on and one that is not super related to widen my horizon). When I\
      \ see an exciting paper I try not to read it immediately but add it to my bookmark\
      \ list instead. And then when I have time for reading, I go through all the\
      \ bookmarks and pick the most interesting/relevant one at that moment. This\
      \ helps me to not get too distracted. But yeah, ideally I would like to read\
      \ more papers.\n3. If you mean with LLMs, then I think ColPali is pretty good:\
      \ [https://arxiv.org/abs/2407.01449](https://arxiv.org/abs/2407.01449) , [https://github.com/illuin-tech/colpali](https://github.com/illuin-tech/colpali));\
      \ otherwise, if you mean as a human reader, then I don\u2019t really have a\
      \ secret, I just read or skim them \U0001F605"
  - name: Prajwal Srinivas
    text: Thank you very much!
- name: Vivien S.
  text: 'Question for Sebastian Raschka:

    - What is the thought process which leads to making a decision that one should
    build an LLM instead of using an existing LLM + RAG or fine-tuning?

    - What are the overheads that one should consider before start building an LLM
    from scratch?

    - How do one evaluate the built LLM? Would you suggest to consider existing benchmarks
    for evaluation?'
  replies:
  - name: Sebastian Raschka
    text: "Building and training an LLM from scratch can be crazy expensive. It an\
      \ literally be a (multi)million $$$ question \U0001F605. (No worries, the LLM\
      \ training in the book is kept small so it runs in reasonable time on a standard\
      \ laptop; we also load pretrained weights from OpenAI into that model later,\
      \ so there is no need to train from scratch.)\nThat being said, there are multiple\
      \ reasons for building a model from scratch:\n-  Educational purposes: It\u2019\
      s the best and most thorough way to learn LLMs. Maybe the only way where you\u2019\
      d really understand each detail. It\u2019s great for understanding the limitations\
      \ also.\n-  Research purpose: If you want to develop new and better (or just\
      \ different) architectures, you\u2019d have to know how to implement them\n\
      -  Customization & privacy: by knowing how LLMs work, it will be easier to adopt\
      \ various LLM models out there like Llama and finetune them for your needs.\
      \ In addition, you can run these models locally if you have sensitive data that\
      \ you can\u2019t share with any of the LLM providers like OpenAI, Google, or\
      \ Anthropic\nRegarding the overheads:\n-  You\u2019d likely need a couple of\
      \ GPUs if you are serious about training LLMs; but for finetuning, one GPU can\
      \ already be enough\nRegarding the evaluation:\n-  The public benchmarks are\
      \ useful for quick sanity checks but they are also very limited. For example,\
      \ MMLU and other public benchmarks are just multiple-choice tests, but a real-world\
      \ application of an LLM is probably not going to be just multiple-choice question\
      \ answering.\n-  In my opinion, one of the best ways to evaluate an LLM is to\
      \ use a test set that you set aside similar to regular machine learning (this\
      \ is done as an example in chapter 7) and then use a capable LLM like Llama\
      \ 3 or GPT-4 to compare the written solutions to the correct test set solutions\
      \ and assign scores, etc."
- name: raki
  text: '*How do you approach evaluating the performance of the LLM built in your
    book? What metrics or methods do you find most useful for understanding its strengths
    and limitations?*'
  replies:
  - name: Sebastian Raschka
    text: 'Good question! I just responded to another question here ([https://datatalks-club.slack.com/archives/C01H403LKG8/p1728900925747959](https://datatalks-club.slack.com/archives/C01H403LKG8/p1728900925747959))
      which was a bit related.

      In the book, I use the training and validation losses for the pretraining chapter
      (chapter 5) along with human evaluation.

      In chapter 6, which is about spam classification, we can calculate the training,
      validation, and test accuracy like in classic machine learning (based on whether
      the text is correctly labeled as spam or not spam).

      Then for instruction-finetuning  (chapter 7) it gets a bit trickier. Here, we
      set aside a test set with correct responses and then use another model (Llama
      3 and optionally GPT-4) to compare the model response to the correct response.
      Below is a screenshot to illustrate what I mean:'
  - name: Sebastian Raschka
    text: "The limitation of MMLU and other public benchmarks is that it\u2019s just\
      \ multiple choice question answering:"
  - name: Sebastian Raschka
    text: A currently popular way is the *LMSYS ChatBot Arena,* where humans can see
      responses of 2 models and then choose which one they like better. And based
      on the response they create a leaderboard ranking. Overall, this is a pretty
      good way to compare LLMs, but the shortcoming is that it strongly favors style
      over correctness.
  - name: Sebastian Raschka
    text: 'So in short, there is no perfect way to evaluate LLMs. But using all the
      different ways mentioned above together can be informative:

      - MMLU etc for testing knowledge

      - Instruction-response evaluation with a closed test set to test how well it
      can actually answer free-form questions

      - LMSYS ChatBot arena as an additional test to rank LLMs by preference'
- name: raki
  text: What datasets are recommended for the pretraining and fine-tuning tasks, and
    how does dataset selection impact the performance?
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s a great question, actually. It sounds like it should be simple\
      \ to answer, but unfortunately there are no comparisons of the same architecture\
      \ pretrained on different datasets. This is probably (and understandably) because\
      \ pretraining is so expensive! Actually, pretraining sets range also a lot in\
      \ size. There\u2019s a trend towards training sets becoming larger (but there\
      \ are also LLMs that focus more on smaller high-quality data like Microsoft\u2019\
      s Phi models)\nNow, regarding instruction-finetuning, there are fortunately\
      \ more comparisons. Here, specifically, quality is more  important than quantity\
      \ (e.g., one paper that demonstrates that nicely is LIMA, where the researchers\
      \ found that their 1000 example dataset beats the 50,000-example Alpaca dataset,\
      \ [https://arxiv.org/abs/2305.11206](https://arxiv.org/abs/2305.11206))\nWhen\
      \ it comes to recommendations, I would say the Olmo paper is actually a good\
      \ start as it shares the training data (other LLMs don\u2019t do that): [https://arxiv.org/abs/2402.00838](https://arxiv.org/abs/2402.00838)"
- name: Evren Unal
  text: 'Which machine do I need to train your LLM?

    Can i train it on my local machine?'
  replies:
  - name: Sebastian Raschka
    text: Yes!! I made sure that everything works and runs in reasonable time on a
      local machine. (I actually tested all the code on my MacBook Air).
- name: "Rafa\u0142 Szu"
  text: For readers who are not very familiar with deep learning, how steep is the
    learning curve when following the steps in your book?
  replies:
  - name: Sebastian Raschka
    text: "Actually, I think may not need a very comprehensive deep learning background.\
      \ Sure, LLMs are neural networks, but they are also their own thing in a way.\n\
      In addition, I wrote a ~40-page Introduction to PyTorch (Appendix A) where I\
      \ tried to get someone started with deep learning in PyTorch effectively. It\
      \ doesn\u2019t replace a full deep learning course, but I hope it covers the\
      \ prerequisites for the book."
- name: "Rafa\u0142 Szu"
  text: In the book, you guide readers step by step. Which stage do you think is the
    most critical for understanding how LLMs work?
  replies:
  - name: Sebastian Raschka
    text: "I think they are all important and build on each other, so it\u2019s hard\
      \ to pick one over the other \U0001F605. But I would say how the embedding vectors\
      \ that come out of an LLM are converted into tokens is probably the most important\
      \ aspect."
- name: "Rafa\u0142 Szu"
  text: When coding a language model from scratch, what is the most common mistake
    people make, and how can it be avoided?
  replies:
  - name: Sebastian Raschka
    text: I think most common mistake or trickiest part is to get the weight reshaping
      and transposing in the multihead attention mechanism wrong. Here, I recommend
      starting with the simplest implementation first and then gradually morphing
      it into a more efficient version while making sure that the results numerically
      still match.
- name: Till
  text: How to best organize data (getting and storing) for finetuning?
  replies:
  - name: Sebastian Raschka
    text: "For finetuning it\u2019s actually quite easy because the finetuning dataset\
      \ are usually quite small and can be held in memory. E.g., just to give an example,\
      \ the Alpaca dataset with 50-000 instruction-answer pairs is just 21.7 Mb large.\
      \ Even if the dataset is 2x the size, it\u2019s still convenient to just store\
      \ it as a JSON file."
- name: Aninda Goswamy
  text: "Hi Sebastian Raschka \nCan you please tell us what criteria or factors to\
    \ consider for choosing an encoder model like BERT or more recent decoder based\
    \ LLM architectures during a text classification or other related tasks"
  replies:
  - name: Sebastian Raschka
    text: 'Encoder-based models like BERT have been specifically developed for classification
      tasks (along some other tasks), so they are a more natural choice here. But
      that being said, you can actually get really good performance with decoder-style
      models. E.g., in chapter 6, we finetune a GPT classifier for spam classification.
      Or take the IMDB movie review dataset for sentiment analysis, in the bonus materials
      I compared a 124 M parameter GPT model to a 3x larger RoBERTa, and the accuracy
      of RoBERTa was only 1% higher.

      The problem with BERT models is that they are really old, and the training (data)
      has not been as sophisticated as the one of more recent decoder-style models.
      As a practical tip, I would recommend using RoBERTa or DistilBERT as a baseline
      and then compare it to a recent classification finetuned decoder-style model.'
- name: Ranga Hande
  text: 'Questions for Sebastian Raschka:'
  replies: []
- name: Ranga Hande
  text: 1. Does LLM tuning section in the book covers RAG, Graph RAG, agents etc?
  replies:
  - name: Sebastian Raschka
    text: Unfortunately, no. The book is more focused on coding the LLM, and a RAG
      system is more of an application surrounding LLMs. But putting the LLM trained
      in the book into a RAG system could be an interesting bonus material that I
      may add.
- name: Ranga Hande
  text: 2. What are the system requirements to try code from the book? Any free options
    that beginners can use while learning?
  replies:
  - name: Sebastian Raschka
    text: "Good question\u2026 Actually, I made sure that all code works fine on a\
      \ conventional laptop (I tested everything on my MacBook Air). However, some\
      \ chapters benefit from GPUs. I have some recommendations here: [https://github.com/rasbt/LLMs-from-scratch/tree/main/setup#cloud-resources](https://github.com/rasbt/LLMs-from-scratch/tree/main/setup#cloud-resources)"
  - name: Ranga Hande
    text: Thank you for answering and providing link to recommendations!
- name: Ravi Natukula
  text: Is there a start date for the 'Build a Large Language Model (From Scratch)'
    session? Also, is there a specific structure or process we follow for this? I'm
    new and trying to understand how the book of the week event works.
  replies:
  - name: Sebastian Raschka
    text: I am also new to this, so please take this with a grain of salt. But as
      far as I know it runs from Monday (today) to Fri. And you could post questions
      here that I then answer asynchronously.
- name: Juliana Machado
  text: Sebastian Raschka following the book, will we build a LLM or a SLM since the
    computational requirements for SLM is considerable smaller?
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s a good question. The term SLM (small language model) is really\
      \ fluid and keeps changing. E.g, an LLM today may be called an SLM tomorrow.\
      \ That being said, the book uses models with 124 M parameters in most chapters\
      \ to make it work on most hardware. But  it also includes the configuration\
      \ for 1.5B parameters that can be used by changing only one line of code."
- name: Juliana Machado
  text: Sebastian Raschka In your experience, when adapting large language models
    for specialized domains what architectural or training strategies have you found
    most effective in enhancing the model's domain-specific accuracy while still retaining
    its broader language understanding? Are there specific techniques you've found
    helpful in balancing the trade-off between specialization and generalization?
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s a good question, and this is usually a big problem and challenge\
      \ in LLM training, The most widely applied strategy is to include ~5% of the\
      \ original training data in the domain-specific data mix. (e.g., [https://arxiv.org/abs/2403.08763](https://arxiv.org/abs/2403.08763))"
- name: Juliana Machado
  text: Sebastian Raschka Do you think a domain-specific small language model could
    reach performance levels similar to a general-purpose LLM if the input data were
    transformed into structured, deterministic features rather than relying on conversational
    or unstructured text aligning it with desired outcomes ?
  replies:
  - name: Sebastian Raschka
    text: Yes, I think so. One example of this is classification finetuning where
      you can match the performance of a huge general-purpose LLM by finetuning just
      on one target task
- name: Antje
  text: "Sebastian Raschka I have some questions regarding yourself instead of your\
    \ book \U0001F642 How did you come up with the idea to write a book? Are you a\
    \ full-time writer, how much do you write each day, and how long does it take\
    \ you to finish such a book?"
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s actually a refreshing question! I\u2019ve worked with LLMs\
      \ for several years, and in my older books from 2021, I only had a single chapter\
      \ on LLMs. But readers enjoyed it so much that I decided to turn it into a standalone\
      \ book. (Plus, I am actually super excited about LLMs myself and work on them\
      \ daily.)\nI\u2019m not a full-time writer; it\u2019s more of a (very intensive)\
      \ side project. Unfortunately, I don\u2019t think it\u2019s feasible to make\
      \ a living as a tech book author. It\u2019s more of a labor of love.\nI\u2019\
      d say I spent about 2 hours a day over 1.5 to 2 years on this particular book.\
      \ It was a lot of work! (I\u2019m definitely taking a long break before starting\
      \ another book\u2026 if I even write another one, haha.)"
- name: Antje
  text: Sebastian Raschka What are main differences between your book and Andrej Karpathys
    "GPT from scratch" videos? Are the approaches comparable (both building an LLM
    from scratch), or are there fundamental differences in concepts?
  replies:
  - name: Sebastian Raschka
    text: As far as I know they are complimentary resources. I started watching the
      videos recently and they seem really good. But yeah, the differences are that
      the material is presented very differently, and the book goes into finetuning,
      like classification and instruction-finetuning. Also, in the book I am covering
      a conventional GPT-style model (plus Llama models in the bonus material) whereas
      the Karpathy videos are focused on character-level models (as far as I know).
      In either case, I would recommend checking out both the videos and the book
      to get a more complete picture.
- name: Juliana Machado
  text: Sebastian Raschka Are there specific strategies or techniques you've found
    to be particularly effective to mitigate potential biases or harmful outputs from
    LLMs?
  replies:
  - name: Sebastian Raschka
    text: I am not an expert in this area, but based on my knowledge alignment and
      preference tuning are the most commonly used approaches (although they are far
      from perfect).
  - name: Sebastian Raschka
    text: 'In addition to altering the LLM  itself, other (or additional) solutions
      include putting guardrails around the LLM. One of the popular examples is the
      NeMO-guardrails framework: [https://github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)'
- name: Mari
  text: Sebastian Raschka are there also suggestions/approaches for LLM performance
    evaluation?
  replies:
  - name: Sebastian Raschka
    text: "Good question. I answered a similar question here that may already address\
      \ your question, but please don\u2019t hesitate to reach out if you have a follow-up\
      \ question: [https://datatalks-club.slack.com/archives/C01H403LKG8/p1728901113313779](https://datatalks-club.slack.com/archives/C01H403LKG8/p1728901113313779)"
- name: Chintan Gotecha
  text: "\U0001F44B Hello, team!\nExcited to be part of the effort, look forward to\
    \ some amazing collaborations!"
  replies: []
- name: Chintan Gotecha
  text: Sebastian Raschka --Please help me with a quick one;  what techniques the
    book recommend for optimizing inference speed and reducing the computational cost
    of running the trained model?
  replies:
  - name: Sebastian Raschka
    text: 'The book is not focused on inference optimizations, but general techniques
      would include KV-caching, quantization, low-precision formats, graph compilation,
      etc. We implement many of these techniques in LitGPT, an open source library
      I help developing (the LitGPT code base is actually a good follow-up for the
      book): [https://github.com/Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)'
  - name: Chintan Gotecha
    text: Thanks Sebastian Raschka -- this helps.
- name: Sebastian Raschka
  text: "Hey all,\nI just wanted to say THANKS for all these interesting questions\
    \ so far! When I was asked to join the book-of-the-week [DataTalk.club](http://DataTalk.club),\
    \ it sounded interesting of course, but I didn\u2019t expect so many super relevant\
    \ questions to be honest!\nAnd no worries, I will get to them one by one!"
  replies: []
- name: Moaaz Khokhar
  text: "Sebastian Raschka Thanks for taking the time out to answer our questions.\
    \ I have a lot of questions and I would really appreciate if you could be kind\
    \ to answer some of these. You might find them redundant or vague, I apologize\
    \ in advance, but since your book has been released I have been trying to acquire\
    \ it and very excited to learn from it ASAP and did not want to waste the opportunity\
    \ to get answers from you. \U0001F642\nHow can I improve protein language models\
    \ for specific tasks or design new models effectively?"
  replies: []
- name: Moaaz Khokhar
  text: Sebastian Raschka What role can RAG, agents, or prompt engineering play in
    enhancing protein modeling in computational biology?
  replies:
  - name: Sebastian Raschka
    text: "I wish I could say more here, but I don\u2019t have any specific experience\
      \  in this intersection. That being said, protein amino acid sequences are essentially\
      \ text, so I can see LLMs being useful for certain pattern-recognition related\
      \ tasks here."
- name: Moaaz Khokhar
  text: Sebastian Raschka Are there specific resources you'd recommend for learning
    about building large language models from scratch?
  replies:
  - name: Sebastian Raschka
    text: "That\u2019s essentially what I try to address in the book \U0001F60A"
- name: Moaaz Khokhar
  text: Sebastian Raschka For low-resource languages like Turkish in specialized domains
    like law, how can we build or improve language models?
  replies:
  - name: Sebastian Raschka
    text: "I think it\u2019s important to start with / select a tokenizer that is\
      \ aware of the languages. The GPT-4 tokenizer (used by Meta AI\u2019s Llama\
      \ 3 models and many others) should be a good fit. Then, you\u2019d pretrain\
      \ the model on a dataset that contains a lot of Turkish texts (but pretraining\
      \ is expensive, so you may want to pick a model that has already been pretrained).\n\
      Regarding the pretrained, I think Llama 3.1 and 3.2 are capable of Turkish (I\
      \ have a conversion from the book\u2019s model to Llama 3, 3.1, and 3.2 here:\
      \ [https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/converting-llama2-to-llama3.ipynb](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/converting-llama2-to-llama3.ipynb)).\
      \ After using a basemodel such as those, you could consider further finetuning\
      \ on Turkish texts. I just did a quick search and there seem to be a bunch of\
      \ datasets for this out there: [https://huggingface.co/collections/umarigan/turkish-llm-fine-tune-datasets-66290b6cce62e36cd325fa88](https://huggingface.co/collections/umarigan/turkish-llm-fine-tune-datasets-66290b6cce62e36cd325fa88)"
- name: Moaaz Khokhar
  text: Sebastian Raschka Can models like LLaMA (pretrained on English language) serve
    as a backbone for developing Turkish language models, and what should be considered?
  replies:
  - name: Sebastian Raschka
    text: "Good question. Yes, they can! I think my previous answer above may already\
      \ address this \U0001F60A"
- name: Moaaz Khokhar
  text: Sebastian Raschka What initial steps do you recommend when starting to solve
    a problem in the language modeling domain?
  replies:
  - name: Sebastian Raschka
    text: I would always start with a baseline, e.g., an existing model that tries
      to accomplish something similar. This can be a related method or a classical
      method. E.g., if you work on an LLM to classify texts, also consider a simple
      baseline like a logistic regression classifier with bag-of-words
- name: Moaaz Khokhar
  text: Sebastian Raschka How might I collaborate with experts like you on projects
    related to language models?
  replies:
  - name: Sebastian Raschka
    text: 'Good question. There are lots of active online communities like the LocalLlama
      subreddit where it might be possible to find and partner up with people who
      are interested in specific topics: [https://www.reddit.com/r/LocalLLaMA/](https://www.reddit.com/r/LocalLLaMA/)'
- name: Moaaz Khokhar
  text: Sebastian Raschka In modeling non-natural languages like protein sequences,
    what indicators are crucial for interpretation?
  replies:
  - name: Sebastian Raschka
    text: "Fair question. And I wish I could say something useful here, but I haven\u2019\
      t worked or read anything about protein sequences in years and don\u2019t want\
      \ to give any outdated or misleading information \U0001F605"
- name: Moaaz Khokhar
  text: Sebastian Raschka With so many LLM resources available, how can we stay up-to-date
    (it's like a jungle and information overflow) and where should we begin when tackling
    new problems?
  replies:
  - name: Sebastian Raschka
    text: "Yes, keeping up with everything can be overwhelming and would be a full-time\
      \ job itself. I think here the crucial thing is to work towards something, like\
      \ an applied project, and then try to be a bit selective. It\u2019s good to\
      \ be aware of what\u2019s generally going on (e.g., via following newsletters\
      \ or checking the posts on communities like LocalLlama). But at the end of the\
      \ day you can\u2019t be an expert in every LLM subtopic, so I would select those\
      \ that are most relevant to the problem you are currently working towards."
- name: Moaaz Khokhar
  text: "Sebastian Raschka As a beginner familiar with terms like RAG and prompt engineering,\
    \ how can I quickly become proficient in formulating and solving AI problems?\n\
    Thank you so much again, in advance. \U0001F642"
  replies:
  - name: Sebastian Raschka
    text: "I wish I could tell you a secret here but I think it mostly comes automatically\
      \ after some experience with applied projects &amp; problems. If you work towards\
      \ a particular project and goal and remain curious, you\u2019ll want to check\
      \ out different solutions to solve similar problems, and things will follow\
      \ automatically.\nSuppose you are interested in retrieving information from\
      \ documents. You may start with a RAG. Then you read about long context LLMs\
      \ and wonder if they could replace your RAG. After doing some reading, you implement\
      \ the long-context LLM and notice that you can\u2019t run it on your hardware,\
      \ and you look for techniques to lower memory requirements, and so on\u2026\
      \ I think while working on applied projects, you will automatically learn and\
      \ encounter many different caveats and workarounds that will naturally lead\
      \ to building your expertise \U0001F60A"
- name: onyeka okonji
  text: "Hi Sebastian Raschka thanks for writing this book. i was fortunate to read\
    \ a few chapters in the beginning and it helped with accurate understanding of\
    \ the building blocks of LLMs and it helped me when working in my MSc dissertation.\
    \ I have a few questions: \n1. Does the book cover all techniques of parameters\
    \ efficient fine-tuning other than LoRA and in your opinion, which of these techniques\
    \ is the best to use especially when working with very small datasets, particularly\
    \ medical datasets. \n2. does the book cover grouped attention, if it doesn\u2019\
    t, do you have any tutorials on the topic? i subscribe to your substack but i\u2019\
    m not sure i\u2019ve seen anything on that from you."
  replies:
  - name: Sebastian Raschka
    text: "I am glad to hear that the book has been helpful for your dissertation!\n\
      1. I only focus on LoRA. That\u2019s because implementing techniques from scratch\
      \ takes a lot of space (/pages), and a book can only be so long \U0001F605.\
      \ The focus here is also mainly on understanding the most important techniques\
      \ well (versus writing a survey). That being said, LoRA is the one technique\
      \ that stood the test of time so far (and it\u2019s also what Apple uses in\
      \ their Apple Intelligence models). I think once you understand LoRA, it\u2019\
      s relatively easy to modify it and experiment with other variants like MoRA\
      \ and DoRA, etc.\n2. The book itself doesn\u2019t use grouped attention because\
      \ it\u2019s not used in the GPT architecture implemented in the book. But I\
      \ implement it here in the book\u2019s bonus materials when converting the GPT\
      \ architecture to Llama: [https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/converting-llama2-to-llama3.ipynb](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/converting-llama2-to-llama3.ipynb)"
  - name: onyeka okonji
    text: thank you very much Sebastian.
- name: Pastor Soto
  text: Hi, does the book discuss the benefit of building a LLMs from scratch instead
    of using a pre-existing solution? I mean, customers might understand that you
    want to finetune a pre-trained model but I am expecting having troubles to communicate
    why building something from scratch might be needed. What's your experience in
    this regard?
  replies:
  - name: Sebastian Raschka
    text: "I think that building an LLM from scratch is the best (and maybe only)\
      \ way to really understand how LLMs work, what the limitations are, etc.\nBut\
      \ yes, in practice you want to finetune pretrained models and not create models\
      \ from scratch. I do think that in order to finetune models effectively, it\u2019\
      s crucial to have some understanding of how finetuning is implemented (vs just\
      \ using a 3rd party library that feels like a black box)"
- name: Nancy Wei
  text: "Hi Sebastian Raschka!  I have been reading all your books since 2017.  Your\
    \ new book is excellent (and I like how it's not 500+ pages)!\nMy question: if\
    \ there are limitations to accessing the data (for example, there is personally\
    \ identifiable information, PII, in the data), would it be better to build an\
    \ LLM from scratch or use a foundation model and then tune from there?  \nThank\
    \ you!!"
  replies:
  - name: Sebastian Raschka
    text: "Thanks so much for the kind words (and the kind support!!).\nAnd this is\
      \ a good question. The building from scratch part is mainly to understand how\
      \ an LLM is structured and how it works (how it processes data, and so forth).\
      \ I think it really helps with understanding the finetuning process.\nBut like\
      \ you said, in practice you can finetune a pretrained model instead of building\
      \ and training it from scratch.\nWhen you say PII, do you mean (1) you are worried\
      \ that a user can access to PII that has been included in the pretraining dataset\
      \ when the pretrained model was created, or (2) do you worry about using the\
      \ foundation model when prompts may contain PII?\nFor (1) I remember reading\
      \ in the Llama papers that the researchers took specific care to exclude PII,\
      \ but of course this will never be perfect. If you train your own model from\
      \ scratch, your model may actually also have similar problems if you are not\
      \ careful with your training dataset. And since pretraining requires such huge\
      \ datasets, it would be very hard to ensure that the foundation model is 100%\
      \ PII-free. So, in short, this is a given risk in either case.\nRe (2): That\u2019\
      s a valid concern since we don\u2019t know how our data is used by OpenAI, Google,\
      \ Anthropic, etc. For this reason, for example, we are not allowed to use these\
      \ LLMs for many work-related tasks and use LLMs that run locally instead."
- name: Nishrin Kachwala
  text: 'hi Sebastian Raschka my questions, apologies if you have covered them before.

    1. *What are the ethical considerations of training an LLM from scratch, especially
    when considering potential biases in the training data?*

    2. *What are the challenges and opportunities associated with using human feedback
    to ensure an LLM follows instructions and aligns with human values?*'
  replies:
  - name: Sebastian Raschka
    text: "These are good and challenging questions.\n1. I am not an expert in AI\
      \ ethics and unfortunately can\u2019t give an elaborate answer here. A lot depends\
      \ on the intended use case of the LLM, too. In the book, training the model\
      \ from scratch is mainly for educational purposes, and we use only public domain\
      \ data. After building a solid understanding of how the process works, you may\
      \ consider available LLMs with pretrained LLMs where researchers applied some\
      \ mitigation techniques to reduce potential issues (it\u2019s never perfect\
      \ though). For example, the recent Llama 3 paper had a really good section on\
      \ safety: [https://arxiv.org/abs/2407.21783](https://arxiv.org/abs/2407.21783)\n\
      2. RLHF and DPO are in my experience very tricky. Compared to instruction-finetuning,\
      \ it\u2019s really hard to get them to work well. Also, the dataset is hard\
      \ to come by. However, they can definitely make a significant difference (although\
      \ they are not perfect). E.g. from the Llama 2 paper (screenshot below. [https://arxiv.org/abs/2307.09288](https://arxiv.org/abs/2307.09288))\
      \ you can see that with more RLHF, the harmlessness and helpfulness definitely\
      \ improve"
- name: Roman Zabolotin
  text: "Hello Sebastian Raschka \U0001F44B, thank you for your book and time for\
    \ answering questions.\nDo you cover the Reinforcement Learning from Human Feedback\
    \ (RLHF) method for model fine-tuning in your book? How would you assess the complexity\
    \ of implementing this approach for readers following your book's materials?"
  replies:
  - name: Sebastian Raschka
    text: "Good question! Actually, I only include it via the bonus materials. It\u2019\
      s a tricky topic and doesn\u2019t always work so well. Actually, instead of\
      \ RLHF+PPO I implement DPO, which is nowadays a bit more popular and widely\
      \ used (e.g. most recent models, including Llama 3.2 use it): [https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb)\n\
      I would say the complexity is higher than the complexity of instruction-finetuning,\
      \ but after understanding instruction-finetuning, I think it\u2019s a gradual\
      \ step and shouldn\u2019t be too complex"
  - name: Roman Zabolotin
    text: Oh, thank you very much. I'll read it
- name: Till
  text: Sebastian Raschka How to make a LLM multimodal (video, audio, images)?
  replies:
  - name: Sebastian Raschka
    text: "Good question. There are various different methods. The simpler (and now\
      \ more popular ones) \u201Csimply\u201D encode images as tokens similar how\
      \ text is encoded as tokens. E.g., two recent examples are the Emu3 paper: [https://arxiv.org/abs/2409.18869](https://arxiv.org/abs/2409.18869)\
      \ and Molmo &amp; Pixmo: [https://www.arxiv.org/abs/2409.17146](https://www.arxiv.org/abs/2409.17146)\n\
      Stay tuned for more details \U0001F60A. I started writing an article about that\
      \ a few weeks ago and plan to polish it up by the end of the month/early next\
      \ month. (I\u2019ll share it on my blog here: [https://magazine.sebastianraschka.com](https://magazine.sebastianraschka.com))"
  - name: Till
    text: "Great, thanks for the sneak preview \U0001F44D\U0001F3FC"
- name: Omkar Gurav
  text: 'Hello Sebastian Raschka || hope u answer this.,  I''ll not complicate things,
    just give a clear understanding  who should read this book...?, and how one can
    approach this book.. for Begineers..

    Question:  also what are you working on currently...? We would love to have some
    learning insight''s on it....


    Question: What are the key trade-offs between training a model from scratch versus
    fine-tuning an existing model?'
  replies:
  - name: Sebastian Raschka
    text: "I would say that the book is for people who would like to understand how\
      \ LLMs (really) work, versus just using the ChatGPT API or LLM libraries as\
      \ an opaque system.\nThe prerequisite is to be familiar with Python. I think\
      \ a strong machine learning background is not required (but of course it would\
      \ not hurt). I included a ~40 page introduction to PyTorch in Appendix A that\
      \ covers the basics that are necessary for the book. If it is your first time\
      \ working with PyTorch, it may be a steeper learning curve, but I think it\u2019\
      s going to be fine.\n&gt;  Question: also what are you working on currently...?\
      \ We would love to have some learning insight\u2019s on it....\nI used to be\
      \ a professor at University of Wisconsin-Madison, but my day to day work consists\
      \ of developing LLM-related tools at our company ([https://lightning.ai](https://lightning.ai))\
      \ that I joined about 2.5 years ago. I do like coding a lot actually, which\
      \ is why I made this shift. A lot of this is related on internal research, solving\
      \ problems for customers, and developing open-source libraries, for example\
      \ LitGPT ([https://github.com/Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)).\
      \ But of course, when time permits, I also like to work on educational materials\
      \ when time (and family) permits\u2026Now that the book is finished, I have\
      \ some more time for some exploration again, working on a finetuning related\
      \ research project and some other fun stuff!\n&gt;  What are the key trade-offs\
      \ between training a model from scratch versus fine-tuning an existing model?\n\
      Pretraining from scratch is almost never advisable unless you are a big company\
      \ and can spend millions of dollars to develop your own state-of-the-art LLM.\
      \ (No worries, in the book we only use a small dataset for that; the point is\
      \ more to code and understand the process; but we then load pretrained weights).\
      \ That being said, both pretraining and finetuning are part of the LLM development\
      \ cycle. So finetuning usually comes after the pretraining (and instead of pretraining\
      \ the model yourself, you can start with pretrained weights)"
- name: Antje
  text: 'Hi Sebastian Raschka thanks for answering my questions. One more: Which chapters/parts
    of your book would you recommend for a one-semester graduate student project (or
    several smaller implementation projects)? I am currently using three of Karpathy''s
    ''Zero to hero''/''GPT from scratch'' videos as basis for this course, but this
    lacks a textbook, so I am looking for an alternative. Any suggestions?'
  replies:
  - name: Sebastian Raschka
    text: "I think there\u2019s a lot of interesting work that could be designed around\
      \ each of the chapters. You could consider\n- Chapter 4: exploring different\
      \ architectural variations and see how they affect model performance\n- Chapter\
      \ 5: different tokenizers and training on low-resource languages\n- Chapter\
      \ 6: implementing the classification approach with different models such as\
      \ Gemma, Llama , Phi etc as a comparative study\n- Chapter 7: exploring parameter-efficient\
      \ finetuning techniques\nI hope this helps!"
- name: Muneeb Khan
  text: "Hi Sebastian Raschka, I'm relatively new to LLM fine-tuning. I'm working\
    \ on a project where I have a dataset of customer messages. My goal is to fine-tune\
    \ a small LLM, say Mistral 7B or even the  Llama 3.2 1B/3B, to summarize the customer\
    \ messages into a set of keywords that best describe the issues raised or the\
    \ requests. Let's say I also have a set of reference keywords that I've obtained\
    \ from a bigger model \u2014 I want this to serve as my ground truth. I'm following\
    \ the below approach for fine-tuning:\n- Prepare an instruction format dataset\
    \ by including the prompt with each message, along with the reference keywords.\
    \  The prompt template is structured somehow like this:\n    \u25E6 prompt_template\
    \ = \n```### System: You are an expert at extracting keywords from customer messages.\
    \ Your task is to identify and list the most relevant key terms that summarize\
    \ the main issues or topics in the given message. Return the key terms as a comma-separated\
    \ list. Do not include any additional information.\n### User:\n{}\n### Assistant:\n\
    Extracted Keywords: {}```\n    \u25E6 I do this for the training and the validation\
    \ sets, but exclude the reference keywords for the test set.\nQ) Is the data preparation\
    \ approach I follow correct for the fine-tuning process?\nQ) Would it be better\
    \ to exclude the reference keywords from the instruction-prepared validation set\
    \ as well to get a better idea of how the model will perform in the wild?\nQ)\
    \ What would be the best evaluation strategy for my use case? Currently, I'm using\
    \ precision, recall and f1 score between the reference keywords and the keywords\
    \ generated by the fine-tuned model.\nThank you so much for your time and I'm\
    \ quite excited to get started with your amazing book to getter better insights\
    \ into working with LLMs from the ground-up."
  replies:
  - name: Sebastian Raschka
    text: "I think your approach is totally reasonable. Instead of instruction-finetuning,\
      \ you could also consider classification finetuning though (chapter 6), because\
      \ you don\u2019t need the model to generate a response text but just a few labels.\
      \ This may be cheaper and more accurate. (In this case, this would be a multi-label\
      \ classification problem, so you\u2019d have to make some slight modifications.)\n\
      The evaluation metrics you mentioned seem good; if you have a set of true labels\
      \ then this is easy to calculate.\n&gt;  Q) Would it be better to exclude the\
      \ reference keywords from the instruction-prepared validation set as well to\
      \ get a better idea of how the model will perform in the wild?\nOh wait, maybe\
      \ I am misunderstanding; if this is an open-ended list, then the multi-label\
      \ classification approach I mentioned above may not be feasible because you\
      \ may have labels that weren\u2019t known to you beforehand.\nIn this case,\
      \ I do think the model will also be challenged in this instruction setting though."
- name: bryan bai
  text: 'Question: what is the difference between a LLM like gpt-4o and embedding
    model like ada002 ?'
  replies:
  - name: Sebastian Raschka
    text: "Hi there! That\u2019s a tricky one actually because OpenAI doesn\u2019\
      t share the architectural details of their models anymore. The GPT-4o model\
      \ is likely very similar to the original GPT architectures though and decoder-style\
      \ model. For the embedding model, this could be either a similar model (where\
      \ they don\u2019t convert the outputs into tokens but return the vector representations)\
      \ or it could be a BERT-style model.\nI think ada002 is likely a smaller GPT-model\
      \ where they simply don\u2019t convert the outputs back into tokens. Using a\
      \ figure from the book, it is likely similar to this where it returns the output\
      \ embedding vectors before converting them back into tokens"
- name: bryan bai
  text: 'Question: for RAG workload , I feel finetune an embedding model will have
    more benefit than finetune a generation model. How should I finetune an embedding
    model ?'
  replies:
  - name: Sebastian Raschka
    text: Finetuning the embedding model for a RAG system is somewhat similar to classic
      self-supervised examples in computer vision with a triplet loss or other contrastive
      loss. Basically you have triplets of (1) the text of interest, (2) an unrelated
      text snippet, (3) a related text snippet. Then, the goal (which is achieved
      by minimizing the loss) is to make the distance between the (1) and (2) large
      and the distance between (1) and (3) small.

---

In Build a Large Language Model (From Scratch), you'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. In this book, I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples.

The method described in this book for training and developing your own small-but-functional model for educational purposes mirrors the approach used in creating large-scale foundational models such as those behind ChatGPT. In addition, this book includes code for loading the weights of larger pretrained models for finetuning.