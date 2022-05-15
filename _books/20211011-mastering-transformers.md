---
title: "Mastering Transformers"
description: "Book of the Week. Mastering Transformers by Savaş Yıldırım and Meysam Asgari-Chenaghlu"
cover: "images/books/20211011-mastering-transformers/cover.jpg"
image: "images/books/20211011-mastering-transformers/preview.jpg"
start: 2021-10-11 00:00:00
end: 2021-10-15 22:59:58
authors: [savasyildirim, meysamasgarichenaghlu]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/mastering-transformers/9781801077651
  - text: Amazon
    link: https://www.amazon.com/Mastering-Transformers-advanced-processing-techniques/dp/1801077657/
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Mastering-Transformers

archive:
- name: Matthew Emerick
  text: "Hello, Savas Y\u0131ld\u0131r\u0131m and Meysam Asgari-chenaghlu for doing\
    \ this. \nHow long until you see transformers replaced with a new architecture\
    \ or technique?"
  replies:
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: Hi Matthew Emerick
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: "Two really tough questions \U0001F642 . Thanks a lot. I think we will continue\
      \ with transformer architectures for 2-3 years. However, alternatives are being\
      \ developed for many of its sub-parts. For example, the attention layer is the\
      \ layer that creates the most complexity, and some sparsification is being employed\
      \ for this memory and computational burden. It will sound like an advertisement,\
      \ but we discussed them clearly in CH 08: The Efficient Transformer (pruning,\
      \ quantization etc.) section.\nIn some studies, while the tokenization part\
      \ is completely removed (see ByT5), in some studies they try to remove or change\
      \ the attention part (FNet: Mixing Tokens with Fourier Transforms). It is said\
      \ that only FF Neural Net will remain in the final stage. But it's too early\
      \ to say that they will be successful and will be used in the industry at scale.\n\
      I think I answered two problems in one shot :)"
- name: Matthew Emerick
  text: Do you foresee a method to reduce the costs of using transformers?
  replies: []
- name: David Cox
  text: "Very excited to see this book come through! Savas Y\u0131ld\u0131r\u0131\
    m and Meysam Asgari-chenaghlu, I think it\u2019s fun to explore everything transformers\
    \ are doing so well at and the novel ways they are being applied. I\u2019m always\
    \ curious about the boundary conditions of various approaches. What are some things\
    \ that transformers are not great at yet and alternative methods are recommended?"
  replies:
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: Thanks David Cox for the questions.
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: 'Let me try to say the first answer that comes to my mind. Maybe Meysam
      Asgari-chenaghlu will add something.

      Attention can only work with fixed-length text strings, which is a really important
      limitation whereas we can cope with it with other traditional RNN like models
      and they are still in use. Well,  the texts are needed to be split so that they
      can be a proper input in size for the Transformer. Likewise The document segmentation
      is the second issue, such as splitting a sentence from the middle, then we suddenly
      lost a significant amount of context. Even though Transformer XL-like model
      can handle it, we face such problems in the field.'
  - name: David Cox
    text: "Thank you Savas Y\u0131ld\u0131r\u0131m!! I really appreciate this answer."
- name: xnot
  text: "Hello Savas Y\u0131ld\u0131r\u0131m, Meysam Asgari-chenaghlu. What level\
    \ of proficiency in ML / Engg is expected from the reader here?"
  replies: []
- name: xnot
  text: What are some of the most creative uses of Transformers you've seen?
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: Hi xnot, thank you for the questions. Our expectation from the reader is that
    they should have at least experience in machine learning &amp; AI and its culture
    and that they should have a good programming background.
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: It has many effective aspects. What surprises me the most and comes to my
    mind first is that it successfully processes two sentences, which is hardly handled
    with traditional approaches, at the same time and can even encode cross-sentence
    anaphoric (reference) relationships thanks to contextual word embedding, which
    in turn can solve many tough NLP problems with stunning quality. xnot
  replies: []
- name: Dr Abdulrahman Baqais
  text: "Hi Savas Y\u0131ld\u0131r\u0131m and Meysam Asgari-chenaghlu.\n1) Transformer\
    \ was a breakthrough. Then a Reformer is proposed. What is ahead?\n2) Transformer\
    \ was adopted for computer vision. Do you think it will have the same success\
    \ as in NLP."
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: 'Hi Dr Abdulrahman Baqais. Thank you for your challenging questions.

    1) There are some ideas to radically change the attention mechanism and tokenization
    mechanism. I have seen many articles in this direction. But it will take time
    to reflect on the industry.  Nowadays we see different models in addition to Reformer,
    which is mostly called efficient transformers, to name a few  BigBird, Reformer,
    Performer, linformer, longformer, and so on... They mostly concern computation
    and memory efficiency of the architecture.

    2)

    It has been mentioned in a few articles that the transformer surpasses other architectures
    (CNN-based) in image processing and signal processing , but again, this may change
    over time.

    There are models published for audio processing and CV on the HuggingFace Hub
    and they seem to be very successful. Please check!'
  replies: []
- name: State Of The Art
  text: "Hi Savas Y\u0131ld\u0131r\u0131m and Meysam Asgari-chenaghlu. i have few\
    \ questions for you guys \U0001F642\n1. What library is being used in the book?\
    \ pytorch or tensorflow?\n2. Do you think learning about transformers is enough\
    \ like don't we need knowledge about vectorizers, embeddings? like i see people\
    \ not learning about languages or machine learning and they directly jump to advanced\
    \ stuffs like applying Sota models or learning about sota models."
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: Hi State Of The Art
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: Thanks for the question
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: 1. Transformer models discussed in the book can based on both libraries (framework)
    thanks to HuggingFace transformers library. In addition to these libraries, many
    other important ones have been utilized whenever needed, such as sentence-transformers,
    flairs, Bertviz etc.
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: "2. It's not enough \U0001F642  We are proceeding by putting the basic building\
    \ blocks on top of each other. To develop a good model, it is necessary to know\
    \ all the building blocks.\nWe need to be familiar  (or even more) with deep learning\
    \ approaches from a single Perceptron to GPT (175B parameters). Otherwise, We\
    \ cannot produce new models and build effective SOTA models without understanding\
    \ the transformation that AI has gone through.\nBut still, a lot of work can be\
    \ done without knowing them in detail. However, there can be a blockage in creative\
    \ and challenging problems."
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: Meanwhile,  we have become able to solve hard problems that were called unsolvable
    in the past, with 2-3 lines of python code.
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: "\U0001F642"
  replies: []
- name: State Of The Art
  text: "Thank you for the amazing reply. \U0001F642"
  replies: []
- name: Tim Becker
  text: "Hi Savas Y\u0131ld\u0131r\u0131m, I am a total NLP and transformer newb.\
    \ I hope you do not mind my simple questions."
  replies:
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: Hi Tim Becker  thank you for your interest.
  - name: "Savas Y\u0131ld\u0131r\u0131m"
    text: '1)To put it simply, This architecture effectively represents a sentence
      using contextual word embedding in a Feed-Forward Neural Net, and also allows
      transfer learning, allowing us to solve many NLP problems even with very little
      labeled dataset.

      2) In transformers, we use self-attention mechanism when representing a word
      and sentence. In NLP  we use the neighboring words around a word to represent
      both in traditional and deep learning framework. But, the attention mechanism
      selectively uses some surrounding words (using weights), not all neighboring
      words. We repeat this for each word and finally, create contextual word embedding
      and eventually sentence embedding.

      3)

      To start simply you can use pipeline module as follows:

      `from transformers import pipeline`

      summarization = pipeline("summarization")

      summarization(yourtext)

      If you want to get your hands dirty and have a labeled sentiment dataset in
      any domain, you can repeat our code with your project (fine-tuning phase) in
      GitHub

      [https://github.com/PacktPublishing/Mastering-Transformers/blob/main/CH05/CH05a_BERT_fine-tuning.ipynb](https://github.com/PacktPublishing/Mastering-Transformers/blob/main/CH05/CH05a_BERT_fine-tuning.ipynb)'
- name: Tim Becker
  text: "- Could you explain the concept of what a transformer actually is? \U0001F605"
  replies: []
- name: Tim Becker
  text: '- What is the attention mechanism?'
  replies: []
- name: Tim Becker
  text: '- Do you have a toy project in mind that would be good to get started with
    transformers?'
  replies: []
- name: Max Payne
  text: "Hi Savas Y\u0131ld\u0131r\u0131m,\nCould you please elaborate on your sentence\
    \ in Chapter 1 (Transformers section), where you were referring to tokenization\
    \ schemes?\n`universal text-compression scheme to prevent unseen tokens on the\
    \ input side`\nI mean what does tokenization have to do with compression here?"
  replies:
  - name: Meysam Asgari-chenaghlu
    text: "Hi Max Payne,\nActually it means that most of the tokenization schemes\
      \ (white space and related ones) can not deal with OoV problem. But instead\
      \ the BPE and related ones can deal with it. The main idea behind using subwords\
      \ or byte-pairs comes from text compression. Finding the most common byte-pairs\
      \ in huge data and then mapping them to smaller representations such as a single\
      \ byte makes the compression more effective. The same idea is used in transformers\
      \ tokenizers to make the tokenization more robust. I have seen some other articles\
      \ that use similar method variations.\nRefs:\nPhilip Gage, A New Algorithm for\
      \ Data Compression. \u201CDr Dobbs Journal\u201D\nSennrich, R., Haddow, B.,\
      \ &amp; Birch, A. (2015). Neural machine translation of rare words with subword\
      \ units. arXiv preprint arXiv:1508.07909."
  - name: Max Payne
    text: Thanks. I was going through the book and found it a great read.
- name: Max Payne
  text: 'Please correct me if I am wrong.

    In - say e.g. CNN -  when we use Transfer Learning, like VGG16 on a cat-dog problem,
    we generally remove then add (or modify) the last layer *AND FREEZE ALL THE PREVIOUS
    LAYERS*. But while training transformers, on notebooks that I came across, I haven''t
    seen people freeze all but the last layers. In fact, they just train all the layers.
    Is there any wisdom behind this or is it technically incorrect (since the HF model
    has already been pre-trained on a corpus)? What would you recommend?'
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: Hi Max Payne, Transformers are trained in an end-to-end fashion contrary to
    CNN architecture. We mostly add a task-specific thin layer on top of Transformers.
    Freezing would deteriorate the system's performance. You can simply try by saying
    bert_model.trainble=false or some specific layers 0..12. However please keep in
    mind that,  each layer has its own characteristic. While some layers encode semantic
    information (mostly further ones), some layers (mostly initial layers) encode
    syntactic information. For example, some are experts in reference relations (he-&gt;John)
    . Therefore, you can determine the layers you will freeze according to the down
    task problem. Once again, freezing is not used much in regular transformer model
    training. It is worth discussing why.
  replies: []
- name: Timur Kamaliev
  text: "Hi Savas Y\u0131ld\u0131r\u0131m and Meysam Asgari-chenaghlu! Thanks for\
    \ your replies for the questions. And I also have one.\nAs I know today all State-of-the-Art\
    \ language models based on transformers (like GPT, Megatron etc) are trying to\
    \ improve their performance by increasing the number of parameters and the related\
    \ with it computational powers. Do you think this trend will remain? Or maybe\
    \ some other ways is have already developed?\nMany thanks!\n[https://developer.nvidia.com/blog/using-deepspeed-and-megatron-to-train-megatron-turing[\u2026\
    ]orlds-largest-and-most-powerful-generative-language-model/](https://developer.nvidia.com/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/)"
  replies: []
- name: "Savas Y\u0131ld\u0131r\u0131m"
  text: 'Hi Timur Kamaliev Thank you for your question. The contribution of such large
    models to the system in terms of success is around 2% at most. However, it is
    important for us that the models should be lighter and more accurate. It is very
    vital especially to use them on edge devices and other sorts of limited devices.
    Therefore, models such as efficient transformers are more focused on the speed
    and memory efficieny of the model.

    Another important problem in Transformers is the input size (e.g. 512 tokens).
    Increasing it is more vital than increasing the parameters at the moment. So what
    we are looking for is to be able to work with longer inputs and produce lighter
    but successful models. That is, sounds like a parameter show to me.'
  replies: []

---

The book gives you an introduction to Transformers by showing you how to write your first hello-world program.
You'll then learn how a tokenizer works and how to train your own tokenizer. As you advance, you'll explore
the architecture of autoencoding models, such as BERT, and autoregressive models, such as GPT. You'll see
how to train and fine-tune models for a variety of natural language understanding (NLU) and natural language
generation (NLG) problems, including text classification, token classification, and text representation.
Furthermore, this book helps you to learn efficient models for challenging problems, such as long-context
NLP tasks with limited computational capacity. You'll also work with multilingual and cross-lingual problems,
optimize models by monitoring their performance, and discover how to deconstruct these models for interpretability
and explainability. Finally, you'll be able to deploy your transformer models in a production environment.