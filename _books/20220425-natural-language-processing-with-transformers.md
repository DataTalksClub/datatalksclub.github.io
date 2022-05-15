---
authors:
- leandrovonwerra
- lewistunstall
- thomaswolf
cover: images/books/20220425-natural-language-processing-with-transformers/cover.jpg
description: Book of the Week. Natural Language Processing with Transformers by Leandro
  von Werra, Lewis Tunstall and Thomas Wolf
end: 2022-04-29 23:59:59
image: images/books/20220425-natural-language-processing-with-transformers/preview.jpg
links:
- link: https://www.oreilly.com/library/view/natural-language-processing/9781098103231/
  text: Book's page
- link: https://www.amazon.com/_/dp/1098103246?tag=oreilly20-20
  text: Buy on Amazon
- link: https://github.com/nlp-with-transformers
  text: GitHub repository
start: 2022-04-25 00:00:00
title: Natural Language Processing with 

archive:
- name: leandro von werra
  text: Hi everyone, looking forward to answering all of your questions!
  replies: []
- name: Lewis Tunstall
  text: "G'day everyone, it's great to be here \U0001F917 ! Looking forward to your\
    \ questions too \U0001F642"
  replies: []
- name: Igor Dal Bo
  text: "Hi guys, thanks for taking the time to answer our questions \U0001F642\n\
    - what is the knowledge level needed for this book?\n- which role do transformers\
    \ play in topic modelling?"
  replies:
  - name: Lewis Tunstall
    text: "Hi Igor, thanks for your questions!\n1. The book assumes some familiarity\
      \ with deep learning and PyTorch, so we recommend reading it after working through\
      \ e.g. the [fast.ai](http://fast.ai) course / book. \n2. Are you referring to\
      \ unsupervised topic modelling, e.g. cluster my texts into a set of topics?\
      \ For this, there's a neat library called BERTopic ([https://github.com/MaartenGr/BERTopic](https://github.com/MaartenGr/BERTopic))\
      \ that get's quite good results in my experience. The alternative is to use\
      \ `sentence-transformers` to embed your documents ([https://sbert.net/](https://sbert.net/))\
      \ and then apply clustering on the embeddings - this too gives quite good results."
  - name: Igor Dal Bo
    text: "thanks Lewis Tunstall for your answers \U0001F642\n- I had in mind taking\
      \ that course for a long while, your suggestion add another point to it \U0001F604\
      \ \n- that is exactly what I wanted to know, thanks a lot for pointing me out\
      \ to the right resources. So far what I have been working on was a supervised\
      \ approach, but defining a topic dictionary manually requires a lot of time\
      \ and knowledge.."
- name: Gonzalo Ancochea Blanco
  text: "Hi!! Thanks Leandro, Lewis and Thomas for sharing some of your time! \nThrough\
    \ your QA chapter I became very interested in Haystack. Retrieval+extraction/generation\
    \ is very relevant for our team's needs and I've seen they have more nodes but\
    \ we also need flexibility to add any other NLP components to the pipeline (e.g.\
    \ NER, topic modelling, sentiment...)\nDo you have any experience with building\
    \ custom Haystack nodes and using the framework to implement full pipelines, and\
    \ if so what is your take on it? Any alternatives? Thanks again \U0001F604"
  replies:
  - name: Lewis Tunstall
    text: 'Hi Gonzalo, thanks for your question!

      I believe that `haystack` did a major overhaul of their `Pipeline` abstraction
      in v1 (which unfortunately came out after our book was in production), and my
      understanding is that it now supports several NLP tasks like summarization (i.e.
      summarize the retrieved docs): [https://haystack.deepset.ai/reference/pipelines#searchsummarizationpipeline](https://haystack.deepset.ai/reference/pipelines#searchsummarizationpipeline)

      For a completely custom pipeline, I''d suggest joining their Slack group: [https://haystack.deepset.ai/community/join](https://haystack.deepset.ai/community/join)

      They''re really responsive and helpful for these kind of questions!'
  - name: Gonzalo Ancochea Blanco
    text: Thanks a ton Lewis Tunstall I will check out the source code of Pipeline
      and definitely join the Slack group!
- name: Alexander Seifert
  text: "So awesome, good to have you guys here! My first question would be: Being\
    \ both NLP practitioner _and_ book publisher I know that (1) you often can\u2019\
    t include everything you want into a book, and (2) the field of NLP moves faster\
    \ than the printing presses. Were there things you had to cut that you would have\
    \ liked to include, and what advances in the field that came about since you handed\
    \ off the manuscript make you excited to have included in the next edition of\
    \ the book if there was one?"
  replies:
  - name: leandro von werra
    text: "When we started working on the book multi-modality was not really a thing,\
      \ yet. Since than CV, Audio, Tabular applications etc. were also conquered by\
      \ transformers. We were able to give a brief overview of what exists in the\
      \ last chapter but obviously it would have been nice to include them in more\
      \ detail and show how to train them. Maybe v2 of the book needs to be renamed\
      \ to `Machine Learning with Transformers` \U0001F642\nIt helped a lot to work\
      \ closely with the maintainers of `transformers` and `datasets` to plan a bit\
      \ around upcoming features or features that would soon be deprecated. E.g the\
      \ streaming API used in the `Training transformers from scratch` chapter was\
      \ finalized at the same time as we wrote the chapter."
- name: Alexander Seifert
  text: "I heard that you wrote the entire manuscript inside Jupyter notebooks. How\
    \ was your experience with that toolchain for writing a whole book, and what did\
    \ O\u2019Reilly think about that? I imagine it\u2019s still somewhat unusual."
  replies:
  - name: Lewis Tunstall
    text: "We used the fastdoc library ([https://github.com/fastai/fastdoc](https://github.com/fastai/fastdoc))\
      \ to handle all the conversion from notebooks to Asciidoc (which is O'Reilly's\
      \ preferred format).\nOverall we found the experience was rather smooth, and\
      \ we were lucky that O'Reilly already had experience from the fastai book \U0001F642\
      \nWe heard from the production editors that they're getting more submissions\
      \ in this format, so I think notebooks might become the norm for these kind\
      \ of publications - it really makes writing a breeze when everything is in one\
      \ place!"
  - name: leandro von werra
    text: "One point to addd here is that the O\u2019Reilly team was happy to keep\
      \ the notebook -&gt; asciidoc conversion pipeline in place until the very last\
      \ reviewing process which kept the notebooks in sync with the formatting/copy-editing\
      \ changes.\nSo it was really nice of them production team to adapt to this new\
      \ workflow. As a nice side effect the whole book is nicely git version controlled\
      \ \U0001F642"
- name: Max Payne
  text: 'Hi, great project and book indeed,

    I have a question regarding explainability, which is gaining a lot of attention.
    With such a large model/training data, is it possible for these APIs to ''explain''
    their decision?'
  replies:
  - name: Lewis Tunstall
    text: 'Hi Max, thanks for the question! As far as I know, explainability of transformers
      is still an open research problem and one that we didn''t have space to cover
      in the book.

      One of the best examples I know of is Jay Alammar''s `ecco` library ([https://github.com/jalammar/ecco](https://github.com/jalammar/ecco))
      which uses various visualisation techniques to understand which factors lead
      to a specific prediction. It doesn''t give you an explanation "for free", since
      you have to do some work to interpret these results, but I think it might be
      interesting to you'
  - name: Max Payne
    text: Thanks alot
- name: Max Payne
  text: Also, regarding explainability, don't you think that the paper 'Pretrained
    Transformers as Universal Computation Engines' sort of makes it even harder, since
    it claims something like there is something special in the architecture that makes
    it generalizable and hence making it more difficult to justify the outputs?
  replies: []
- name: Alexander Seifert
  text: "I am working on a human-in-the-loop NER system, where I\u2019d like to use\
    \ the prediction scores as a proxy for correctness. As far as I understand, this\
    \ is called \u201Cuncertainty estimation\u201D and it is not something that transformer\
    \ models are providing out-of-the-box. Is there content on this problem in the\
    \ book, and if not, are there any good resources you would recommend?"
  replies:
  - name: leandro von werra
    text: "So if by prediction scores you mean the model\u2019s output probabilities\
      \ then yu can actually get them fairly easy from the `transformer` models: For\
      \ each token the model will return the logits and by applying a SoftMax function\
      \ you\u2019ll get each classes probability.\nIn the book we show how to get\
      \ the logits from the model for NER so the only thing that\u2019s missing to\
      \ get probabilities is applying SoftMax. Hope that helps!"
  - name: Alexander Seifert
    text: 'the problem is that the softmax will indeed squish the logits into a probability
      distribution (formally), but this distribution is unfortunately poorly calibrated
      to the correctness likelihood: [https://arxiv.org/abs/1706.04599](https://arxiv.org/abs/1706.04599)'
- name: Hugo
  text: 'Thanks for this wonderful book! I am looking forward to reading it.  Writing
    a book is a very time consuming task so I have two general questions: 1) how long
    did it take you to do it? 2) what was the most challenging section of the book
    to write?'
  replies:
  - name: leandro von werra
    text: "1. It took as roughly 1.5 years to write the book. Since we did it in our\
      \ spare time this means that we mostly worked on it on weekends \U0001F642 \n\
      2. For me working on the few labels and pretraining from scratch were the most\
      \ challenging. The few labels chapter required a lot of experimentation and\
      \ research to first figure out what works well. The pretraining chapter was\
      \ one of my first contacts with distributed training and in addition we used\
      \ a lot of features of the hugging face ecosystem that were brand new.\nMaybe\
      \ the others have other chapters they found challenging \U0001F642"
- name: Adisorn
  text: Hi, I am a beginner in this field.  I heard from the above comment that you
    use Jupyter notebooks to write your code.  Can I follow your code step by step
    if I use Collab?
  replies:
  - name: leandro von werra
    text: "Yes you can! See the table with Colab links in the book\u2019s repository:\n\
      [https://github.com/nlp-with-transformers/notebooks](https://github.com/nlp-with-transformers/notebooks)"
- name: Adisorn
  text: In case my interesting NLP task is the Text summarization. Is there a connected
    issue to this topic?
  replies:
  - name: leandro von werra
    text: "You could look at chapter 6 where we show how to train a transformer model\
      \ on text summarization. All the book\u2019s code is freely available in the\
      \ repository (but without the text from the book, so no explanations)."
- name: Amruta Ranade
  text: Hi leandro von werra, the concept of transformers is new to me and am learning
    about their architectures and functions currently. I was interested in knowing
    how transfer learning can be adopted with the transformers and are there any specific
    applications that you have covered in this book?
  replies:
  - name: leandro von werra
    text: Hi Amruta Ranade, yes transfer learning can be applied to transformers and
      is in fact the driving force behind their success. Except for the last chapter
      where we train a model from scratch all chapters show how to apply transfer
      learning to tune a pretrained model on a specific task such as classification,
      NER, QA, or summarization.
  - name: Amruta Ranade
    text: "Thankyou for the information ! Sounds interesting to me. I am definitely\
      \ going to buy your book! \U0001F60A"
- name: Sitao Zhang
  text: "Congrats HF team! !\nThis is Sitao from the J&amp;J team, really glad to\
    \ see you guys published this wonderful book and been awarded as the <#C01H403LKG8|book-of-the-week>.\U0001F44F\
    \U0001F389\nJust a glance of the book description, I\u2019m curious about:\n1.\
    \ Whats the major difference between this book and the HF documentations online?\n\
    2. Since I have been leveraging the transformer for a while, which part/parts\
    \ of the book do you mostly recommend for people who have some experience?\n3.\
    \ Not sure whether the HF BigScience will be cover here? I know the BigScience\
    \ is super recent, maybe the similar concepts will be discussed in the book?\n\
    Thank you guys!\U0001F44D"
  replies:
  - name: leandro von werra
    text: "Hi Siato, thanks for being here!\n1. What we try in the book is to be much\
      \ more practical than the documentation, which is why each chapter aims to solve\
      \ a realistic use-case. So it involves more steps like preparing your data or\
      \ doing some error analysis of your model.\n2. In general the later chapters\
      \ in the book are mode advanced (e.g. making transformers efficient for prod,\
      \ few labels or pretraining from scratch). Almost every chapter also tackles\
      \ a different task (classification, ner, qa, summarization etc.). So you could\
      \ also pick a task that you haven\u2019t encountered before.\n3. Unfortunately,\
      \ we don\u2019t go into detail of BigScience. The very last chapter looks a\
      \ bit ahead especially at the scaling trend of transformers and multimodal transformers."
- name: Lalit Pagaria
  text: 'Thanks team for conducting this QnA.

    Have following query -

    HF being a leader in practical deployment of transformers model and super heading
    collaborative research  initiative like Big Science. What are practical pipelines
    (pre-processing) must before giving input to transformers (production setup)?'
  replies:
  - name: leandro von werra
    text: "So I think this can be divided into two categories:\n- data cleaning: before\
      \ you train your model you want to make sure that the data is as clean as possible.\
      \ for BigScience we spent a lot of time cleaning and filtering the data. this\
      \ includes: removing duplicates, deleting html code from websites and so on.\
      \ whatever you do to your training data here you should also do to the inputs\
      \ in production. always clean your data \U0001F642 \n- tokenization: there are\
      \ a few steps that besides splitting the string into tokens that the tokenizer\
      \ takes care of such as unicode normalization or lower casing all strings. as\
      \ long as you use the same tokenizer in prod as you used during training you\
      \ should be fine. \nhope that answers your question! \U0001F917"
  - name: Lalit Pagaria
    text: "Yes it answers partially. But I was looking for a deeper answer. \U0001F642\
      \nMore of practical example"
  - name: leandro von werra
    text: "I guess the deeper answer depends on your use-case \U0001F642 To work as\
      \ well in production as on your local test set the most important thing is to\
      \ make sure the data preprocessing steps are the same and the test set reflects\
      \ the production data.\nThe second aspect is the performance on the test set:\
      \ data cleaning is usually very important here but again which particular steps\
      \ are necessary depends on your use-case and dataset."
- name: Lalit Pagaria
  text: In low resource setup. Is multi-head single transformers deployment is more
    suited or serially connecting multiple specific transformers? For example if we
    need translation + classification + summarization on same given input.
  replies:
  - name: leandro von werra
    text: "I experimented in the past with creating a single model for three classification\
      \ tasks and thus creating a model with three heads. the motivation was more\
      \ to have just one large model in production instead of three and we didn\u2019\
      t see a significant performance improvement. Also this was the same task type\
      \ just three different classification criteria.\nA model that works well on\
      \ a wide range of tasks at the same time is T5. Maybe you can tune it for the\
      \ tasks you are trying to cover.\nAlternatively one thing that can work well\
      \ in low resource setting is to use models that are already trained on a e.g.\
      \ summarization task instead of the raw pretrained models. We do this in the\
      \ QA chapter: we use a model that has been trained on SQuAD and train it a bit\
      \ more on the Amazon dataset which gives better results.\nWhich (if any) of\
      \ these suggestion works depends a lot on what you are actual use-case looks\
      \ like. My general advice is to build a good evaluation set that captures your\
      \ use-case and lets you easily evaluate your models. Start creating a few simple\
      \ baselines and then iterate quickly on different ideas. Without the evaluation\
      \ pipeline the iterations will be slow."
  - name: Lalit Pagaria
    text: "Thank you leandro von werra \nYes trial and error is the way forward"
- name: A
  text: "Huggingface has done a tremendous job in making transformer based models\
    \ accessible to a lot of people. As a result, trying these SOTA models is no longer\
    \ difficult and has enabled organisations of all scales make use of them\n1. How\
    \ do you feel about the widespread applicability of these models? Are there any\
    \ cool use-cases in maybe some obscure domain where transformers are working there\
    \ magic and which you\u2019d like to share?\n2. The popularity and ease of use\
    \ of Huggingface means even non-DS background folks also are able to use the power\
    \ of BERT. Most of the times this leads to models which are not built taking into\
    \ bias and other components of responsible-ai into consideration. What do you\
    \ think can be done to tackle this (if it needs to be tackled) ?\nThanks for the\
    \ book! Definitely need to read this."
  replies:
  - name: leandro von werra
    text: "Hi A, thanks for being here!\n1. I am personally very excited about ML\
      \ in science. I think any tool that enables iterate faster in science will have\
      \ a huge impact. One of my favourite application here is [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2)\
      \ from DeepMind. Predicting how proteins fold is a critical task in chemistry\
      \ and biology to make progress and until AlphaFold the only way to get good\
      \ predictions was through very expensive and long experiments that could take\
      \ weeks or month. With AlphaFold the same researchers can now iterate through\
      \ 100s of molecules in a day which changes the game completely. \n2. I would\
      \ even argue that most biased models that make headlines these days were deployed\
      \ by DS folks \U0001F642  I am not an expert here and maybe Thomas Wolf has\
      \ more to share. My two cents are that thinking about and investigation bias\
      \ and impact of a deployed model should become a core task of DS lifecycle.\
      \ This requires documenting on what exactly and how the model was trained and\
      \ rigorous testing of how it performs in different situations. There is a lot\
      \ of work going on in [BigScience](https://bigscience.huggingface.co) for example\
      \ where people work on showing how a large language model can be built and released\
      \ responsibly."
- name: Mischa Ungermann
  text: 'Hi guys, thanks for taking the time for this Q&amp;A!

    I was working with mostly CV topics for the last years and now I am curious to
    get an insight into this world of NLP everyone is talking about. For this I was
    wondering what resources you would recommend as an entry point to the field? I
    could imagine a certain book will be high on the list, and probably also the Hugging
    Face course, but maybe you know of more gems?'
  replies:
  - name: leandro von werra
    text: "Indeed our book is NLP beginner friendly and the main requirement are the\
      \ core ML concepts (what\u2019s a train test split, how to build and train a\
      \ neural network, standard metrics etc). So if your are familiar with CV that\
      \ won\u2019t be an issue \U0001F642\nI know a lot of people got into NLP with\
      \ Chris Mannings excellent lecture series: [https://web.stanford.edu/class/cs224n/](https://web.stanford.edu/class/cs224n/).\
      \ Also the popular fastai course covers some NLP: [https://course.fast.ai/videos/?lesson=8](https://course.fast.ai/videos/?lesson=8)"
- name: leandro von werra
  text: "So many great questions so far! Thank you and keep them coming! \U0001F917"
  replies: []
- name: Max Payne
  text: It's the first time I have seen a book (predominantly targeting a specific
    API) and also addressing the topic of 'Text Generation' (i.e. beam search, greedy
    decoding etc.). How does HuggingFace deal with these methods - I mean do we as
    a user have a choice in selecting the method? or the model has a default setting?
    (Sorry if this question is answered in the book)
  replies:
  - name: leandro von werra
    text: 'Yes, we go into that in more detail, but to give you the short summary
      here:

      Every model in the `transformers` library that is able to do text generation
      has a `.generate()` method. This method is loaded with options to do all sorts
      of generation strategies: greedy, beam search, sampling (with top-k or nucleus),
      repetition penalties etc. You can also define your own stopping criteria or
      processors to be applied.

      [see here](https://huggingface.co/docs/transformers/v4.18.0/en/main_classes/text_generation#transformers.generation_utils.GenerationMixin.generate)

      Patrick von Platen wrote a great article about that function and how to use
      it:

      [https://huggingface.co/blog/how-to-generate](https://huggingface.co/blog/how-to-generate)'
  - name: Max Payne
    text: Awesome. Thank you!
- name: Marcello La Rocca
  text: 'Hi! Congrats on the book, it looks awesome!

    Question: where would you say it''s the main advantage in using Huggingface''s
    tranformers vs say GPT-3? What could be a disadvantage?'
  replies:
  - name: leandro von werra
    text: 'There are a number of advantages:

      - you can host the modals on your own infrastructure - for many companies sending
      data to an outside API can be complicated, especially if the data is sensitive

      - you have a lot more flexibility to train the models and iterate through different
      training setups. you can also customize your architecture to your use-case

      - dopending on your setup hosting your own models can be much cheaper, especially
      if you have heavy workloads. Nils Reimers wrote a thread about this: [https://twitter.com/nils_reimers/status/1487014195568775173](https://twitter.com/nils_reimers/status/1487014195568775173)'
  - name: Marcello La Rocca
    text: "Thanks Leandro! Indeed, that totally makes sense.\nAlso thanks for the\
      \ link! \U0001F64F"
- name: Marcello La Rocca
  text: '2nd question (partially related, but also more about the book content): what''s
    the hardest challenge in scaling transformers?'
  replies:
  - name: leandro von werra
    text: "oh there are many, hard to pinpoint a single hardest \U0001F643 just to\
      \ list a few:\n- engineering: training such models requires a large distributed\
      \ infrastructure with <tel:100-1000|100-1000>s of GPUs. you need some resilience\
      \ when some of them crash and you need to make sure they are optimally used.\
      \ also at that scale you can be haunted by many numerical instabilities. in\
      \ BigScience we are training such a model in the open and you can read the chronicles\
      \ of the experiments: [https://github.com/bigscience-workshop/bigscience](https://github.com/bigscience-workshop/bigscience)\n\
      - dataset: training these beadts requires a lot of data (~TBs of text). at the\
      \ same time you need to make sure that the data is clean which gets harder at\
      \ that scale. you can\u2018t just look at it\n- release: how can one responsibly\
      \ release such models. there is a lot of work going on about for example licensing.\
      \ \nmaybe Thomas Wolf has some more insights here :)"
  - name: Marcello La Rocca
    text: "Ah, interesting! How can you deal with the numerical instabilities? I imagine\
      \ they also propagate and get larger and larger \U0001F914\nI'm looking forward\
      \ to reading more in your book \U0001F642"
  - name: Marcello La Rocca
    text: Also what do you think about "sparsity-aware inference engines"?
- name: Marcello La Rocca
  text: '3rd one: Do you think that transformers will be possibly applied beyond text/vision/speech?
    Maybe reasoning?'
  replies:
  - name: leandro von werra
    text: 'Currently it seems that transformers are penetrating almost every field
      in ML. on the topic of reasoning you might find this recent paper by Google
      interesting: [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)'
  - name: Marcello La Rocca
    text: 'Wow, that''s impressive!!! Thanks a lot for the link

      58.1% on GSM8K is impressive (though also a reminder of long path ahead!)'
- name: Marcello La Rocca
  text: (thanks a lot!!!)
  replies: []
- name: Evren Unal
  text: 'Hi.

    Thank you participating this event.

    I would like to build a language translator some time in the future.

    Q1) Can i use transformer technology to built it?

    Q2) if so, did you give enough information in your book to build it?'
  replies:
  - name: leandro von werra
    text: "1. definitley. there are for example ~1000 translation models already on\
      \ the huggingface hub! see: [https://huggingface.co/models?pipeline_tag=translation&amp;sort=downloads](https://huggingface.co/models?pipeline_tag=translation&amp;sort=downloads).\
      \ you can either use them out of the box or further tune them on your specific\
      \ data!\n2. we don\u2018t go into details on translation specifically, but we\
      \ show summarization in more detail. conceptually the task is very similar (one\
      \ input text and an output text) and we also show and explain BLEU which is\
      \ often used in translation."
  - name: Evren Unal
    text: "thank you very much  \U0001F44D"
- name: armin zirak
  text: 'Hi all!

    Thanks for the great book!

    Q: If I want to use transformers for numeric data instead of text, how can I do
    that? Do you think feeding the numbers as text does the job in the best way or
    is there any specific solution?'
  replies:
  - name: Lewis Tunstall
    text: 'Hi Armin, thanks for your question! There do exist transformers like SAINT
      for numerical features like the ones you would find in tabular data.

      However, it seems that gradient boosting remains the state-of-the-art and it
      might be a while before transfer learning is truly cracked for tabular data
      (see plot).

      There''s a very nice survey of these models here: [https://arxiv.org/abs/2110.01889](https://arxiv.org/abs/2110.01889)'
- name: Allan
  text: 'Hi, thanks for taking the time to answer questions here!  Looking forward
    to the book!

    Does the book address issues related to deploying and using transformers in production
    settings?'
  replies:
  - name: Lewis Tunstall
    text: "Hi Allan, yes Chapter 8 covers various techniques related to optimisation\
      \ including:\n- Knowledge distillation\n- Quantization\n- Graph optimization\
      \ with ONNX Runtime\n- Pruning (although at the time of writing it wasn't easy\
      \ to prune transformers effectively)\nThe end result is figure like this which\
      \ shows how you can reduce the latency of a BERT model by ~7x \U0001F642"
  - name: Allan
    text: Thanks!
- name: Shantanu Ladhwe
  text: "Hey, thanks for the amazing book. I am yet reading, and really liked the\
    \ explanation of transformers there.\nQuestion: How different would be Google\u2019\
    s next AI Architecture- Pathways from the Transformer architecture?"
  replies:
  - name: leandro von werra
    text: "Hi Shantanu Ladhwe, not an expert on Pathways but as far as I understand\
      \ it is mainly a vision towards multi-tasking, multi-modality, and maybe a switch\
      \ to sparsity (see Jeff Dean\u2019s article [here](https://blog.google/technology/ai/introducing-pathways-next-generation-ai-architecture/)).\
      \ This vision could be (and will likely be) realized with a Transformer architecture.\
      \ There are already multi-tasking (e.g. T0pp), multi-modality (e.g. CLIP, Perceiver),\
      \ and sparse (e.g. SwitchTransformer) transformer models out there.\nThe Pathways\
      \ Language Model ([PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html))\
      \ uses a classical transformer decoder architecture and the main innovation\
      \ is around infrastructure to train the model efficiently on 6000 TPUs."
- name: Max Payne
  text: I wish I could use a Transformer here to generate questions (and hence increase
    my chances of getting the book) :-)
  replies: []

---

Since their introduction in 2017, transformers have quickly become the dominant architecture for achieving state-of-the-art results on a variety of natural language processing tasks. If you're a data scientist or coder, this practical book shows you how to train and scale these large models using Hugging Face Transformers, a Python-based deep learning library.

Transformers have been used to write realistic news stories, improve Google Search queries, and even create chatbots that tell corny jokes. In this guide, authors Lewis Tunstall, Leandro von Werra, and Thomas Wolf, among the creators of Hugging Face Transformers, use a hands-on approach to teach you how transformers work and how to integrate them in your applications. You'll quickly learn a variety of tasks they can help you solve.

- Build, debug, and optimize transformer models for core NLP tasks, such as text classification, named entity recognition, and question answering
- Learn how transformers can be used for cross-lingual transfer learning
- Apply transformers in real-world scenarios where labeled data is scarce
- Make transformer models efficient for deployment using techniques such as distillation, pruning, and quantization
- Train transformers from scratch and learn how to scale to multiple GPUs and distributed environments