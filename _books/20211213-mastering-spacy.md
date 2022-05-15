---
title: "Mastering spaCy"
description: "Book of the Week. Mastering spaCy by Duygu Altinok"
cover: "images/books/20211213-mastering-spacy/cover.jpg"
image: "images/books/20211213-mastering-spacy/preview.jpg"
start: 2021-12-13 00:00:00
end: 2021-12-17 22:59:58
authors: [duygualtinok]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/mastering-spacy/9781800563353
  - text: Amazon
    link: https://www.amazon.com/Mastering-spaCy-end-end-implementing/dp/1800563353

archive:
- name: Krzysztof Ograbek
  text: "Wow, how great!! Thanks Duygu Altinok for doing this \U0001F642"
  replies: []
- name: Krzysztof Ograbek
  text: 'My first question: What can you perform with spaCy but cannot with other
    NLP libraries (nltk, gensim, textblob, ...)? Which features are unique?'
  replies:
  - name: Duygu Altinok
    text: 'Thanks for the question!

      First of all we want offer the users complete pipelines per each supported languages.
      In this aspect, NLTK and textblob are similar but gensim is different.

      We include the following components:

      - Sentence segmenter

      - Tokenizer

      - Lemmatizer

      - Morphologizer

      - NER

      - dependency parser

      - POS tagger

      - Rule based matcher

      - Entity linker

      - Vectors &amp; semantic similarity

      - Tetxcat

      - Spancat'
  - name: Duygu Altinok
    text: "Problem with NLTK it's not really suitable for industry-level usage. Some\
      \ pretrained models are ancient but the main problem is the speed. I'd say it's\
      \ good for academical use, but not really suitable for production level NP.\n\
      Coming to unique components that you cannot find anywhere else I'd say:\n- Morphologizer:\
      \ This is a trainable component, calculate morphological features by looking\
      \ at the word. one example:  `hermosa-&gt; singular, feminine` \n- Rule based\
      \ matchers are definitely unique and very useful components for extracting information\
      \ based on patterns. \n- Tok2vec: This component is really unique allows dependency\
      \ parser, named entity recognizer and pos tagger to share a common NN. Also\
      \ this layer generates word vectors for `oov` words, hence feature calculations\
      \ of oov words don't fail \U0001F609 That's a disadvantage in many libraries,\
      \ misspelled words and some words that are not in the models vocab sometimes\
      \ fails, sometimes work with the statistical models. We wanted to handle oovs\
      \ in a proper way.\n- Entity linker: This component disambiguates textual mentions\
      \ (tagged as named entities) to unique identifiers, grounding the named entities\
      \ into the real world via a KnowledgeBase\n- Spancat: This is an uniquq and\
      \ very useful component too, it can classify word spans. I'll post an example\
      \ project link."
  - name: Duygu Altinok
    text: "So each component is modifiable by your own training data, easy to use\
      \ and  really blazing fast.\nFinal remark is that we also have transformer-based\
      \ pipelines. I consider it pretty uniquq as well \U0001F642"
  - name: Krzysztof Ograbek
    text: "Oh yes! Rule-based matchers are awesome \U0001F642"
  - name: Duygu Altinok
    text: "I really like playing with Matcher too, I enjoyed writing the Matcher chapter\
      \ quite a lot. Also as Explosion we'll soon publish some videos and I plan to\
      \ make a Matcher video \U0001F642"
- name: Doink
  text: what tasks can be done with Spacy more efficiently than a transformer?
  replies:
  - name: Duygu Altinok
    text: "Thanks for the question:woman-raising-hand:\nHere, paradigms are bit different.\
      \ Transformers provide a state-of-art way of calculating context dependent word\
      \ vectors and sentence representations. Hence if you feed your sentence to a\
      \ transformer, you get a word vector for each token and a dense representation\
      \ of your sentence.\nIf you want to do text classification, POS tagging or other\
      \ downstream tasks with a Transformer\n- You need to find an annotated corpus\n\
      - You need to train the Transformer by adding more layers on top (which should\
      \ suit your task, seq2seq for NER, POS tagger or just softmax for text classification).\n\
      spaCy's paradigm is different, we want to provide users with `pretrained` pipelines\
      \ that can be usable immediately. This way you don't worry about the training\
      \ phase, directly start creating NLP applications. Here's an example:\n```&gt;&gt;&gt;\
      \ import spacy\n&gt;&gt;&gt; nlp   = spacy.load(\"en_core_web_md\") #Load our\
      \ pretrained model\n&gt;&gt;&gt; doc = nlp(\"I went there fast\")\n&gt;&gt;&gt;\
      \ for token in doc:\n...   token, token.pos_\n... \n(I, 'PRON')\n(went, 'VERB')\n\
      (there, 'ADV')\n(fast, 'ADV')  \n# Then do your stuff with the pos tags```"
  - name: Duygu Altinok
    text: "Our pipelines are either based on word vectors or on Transformers. So we\
      \ use Transformers for our downstream tasks too \U0001F609"
- name: WingCode
  text: 'Hi Duygu Altinok,

    Does this book cover putting spacy into production?'
  replies:
  - name: Duygu Altinok
    text: "Moins, thanks for the question. There's no dedicated section in my book.\
      \ However, we aim our pipelines to be easily usable, hence integrating spaCy\
      \ and pretrained models into your porject is not difficult at all. You can just\
      \ add 2 lines to your project's `requirements.txt` then you're ready to go \U0001F642\
      Here's an example of what you can add:\n```spacy&gt;=3.0.0\n[https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz#egg=en_core_web_sm-2.2.0](https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz#egg=en_core_web_sm-2.2.0)```"
  - name: Duygu Altinok
    text: "This is quite pain free, usually with pretrained models\n- DevOps guys\
      \ need to download the model, store it on somewhere(usually) AWS\n- Then put\
      \ some S3 checkout lines to download the model to the project scripts\n- and\
      \ more work\nCompared to that spaCy way is really painless\U0001F601"
  - name: WingCode
    text: "Thank you Duygu Altinok for the answer \U0001F642\nFollow up question,\
      \ is there any aspects of spacy pipelines which makes it better than other framework\
      \ pipelines (sklearn-pipeline, transformers pipeline etc) ?"
- name: "\xC1lvaro Budr\xEDa"
  text: "Hi Duygu, for students like me and people in academia, would you recommend\
    \ spaCy over other alternatives such as Nltk? Thanks! \U0001F642"
  replies:
  - name: Duygu Altinok
    text: "Yes \U0001F642\nPlease refer to this previous answer:  [https://datatalks-club.slack.com/archives/C01H403LKG8/p1639390846197000?thread_ts=1639386552.194400&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1639390846197000?thread_ts=1639386552.194400&amp;cid=C01H403LKG8)"
  - name: "\xC1lvaro Budr\xEDa"
    text: Oh I didn't see that answer, thanks!
- name: Matthew Emerick
  text: 'Hey, Duygu Altinok. Thanks for doing this!

    I have applied for many AI roles in the past year and read many NLP descriptions.
    I can barely recall just a few times when spaCy is mentioned. Why do you think
    the library is hardly mentioned when so many NLP applications are based on it?'
  replies:
  - name: Duygu Altinok
    text: 'Many thanks for this interesting question:woman-raising-hand:

      This is a point that is really curious to me, too. I know few companies where
      the whole application depends on spaCy but still no mention in the job add.  Even
      if I see spaCy in the add, I see sth quite generic sth like this:

      - familiarity with NLP libraries such as gensim, nltk, spacy'
  - name: Duygu Altinok
    text: "I think the reason is copy-paste mania among HR. In the -3th company I\
      \ worked for, HR was preparing the job adds and then show to us for corrections.\
      \ Here's one example of what he wrote down:\n- terabytes of data (not true at\
      \ all)\n- state of art deep learning models (no DL, just some logistic regression)\
      \ \n- experience with spark (not used at all)\nSo, I asked him how he prepared\
      \ this job add and I found out how most HRs prepare job adds: Look for some\
      \ NLP job adds online and made a mix-n-match of those adds. This process converges\
      \ to a very generic NLP job add at the end\U0001F9E0"
  - name: "\xC1lvaro Budr\xEDa"
    text: Seems that technical people should get more involved in the hiring process!
- name: Matthew Emerick
  text: Is this book best for beginners, intermediate practitioners, or almost experts?
    Would college students interested in AI find this book useful?
  replies:
  - name: Duygu Altinok
    text: "I included explanations of concepts along with examples, so this is a book\
      \ I %100 recommend for beginners and intermediate level colleagues. Each chapter\
      \ starts with explanations, include lots of code and ends with example applications.\n\
      For expert colleagues, I think they can find the all-hands-on chapters. Especially\
      \ building a chatbot chapter would be interest to all NLP lovers. Rest of the\
      \ book of course has teaching material as well, so I leave this decision to\
      \ NLP experts themselves \U0001F642"
- name: CJ
  text: I have spent an inordinate amount of my life explaining to people how to get
    information from text. Do you recommend starting with the easier bag of words,
    tf-idf models, or jump right into more complicated embeddings?
  replies:
  - name: Duygu Altinok
    text: "I started from really the scratch because when I started (around 13 years\
      \ ago) there was only tf-idf and bag of words \U0001F642 When word vectors came,\
      \ I %100 understood the problem they wanted to solve and innovation they introduced.\
      \ After that transformers came and the same, I appreciated the solutions that\
      \ word vectors couldn't offer.\nI definitely saw the benefit of building up,\
      \ when I'm vectorizing text I always know\n- good sides and down sides of my\
      \ approach\n- shape of the vectors I generated, also the size they'll take\n\
      - what sort of information my vectors encode\n- why would my approach work\n\
      - for which cases my approach wouldn't work and what can I do about it\nSo,\
      \ I definitely recommend starting from scratch, also some tf-idf computations\
      \ make students to warm up to the vector computations any way. However, young\
      \ people are quite impatient and want to build cool stuff asap. I'm not %100sure\
      \ they have the patience to practice from scratch \U0001F642 I'd say if this\
      \ is a college class, I'd go ahead and teach it. If it's a professional course\
      \ for junior colleagues, I'd  go over basics in 1 hr with some examples and\
      \ then assign some reading material."
- name: Dmitriy Shvadskiy
  text: Hi Duygu Altinok Does the book cover training/finetuning Transformer as part
    of Spacy pipeline? If not what resources would you recommend on the topic. I was
    trying to integrate Spacy NER  with Transformer few months back and it is not
    really obvious task
  replies:
  - name: Duygu Altinok
    text: 'OK, I covered the code of how to fine tune some components including NER
      and textcat.

      If you want to fine tune a component, it''s no so difficult ; one just needs
      to provide some examples with labels. For your case, you can download a transformer-based
      model and then fine tune NER. You can see the example of how to provide examples
      from my book''s code: [https://github.com/PacktPublishing/Mastering-spaCy/blob/main/Chapter07/train_on_cord19.py](https://github.com/PacktPublishing/Mastering-spaCy/blob/main/Chapter07/train_on_cord19.py)

      If you want to fine tune the transformer itself, it''s not an easy task because
      you need huge amounts of data. Transformers are giants, even with a huge corpus
      I noticed I only fined tuned maybe last 2 layers. If you want to go down this
      road then you need a spaCy project:  [https://github.com/explosion/projects/tree/v3/pipelines/ner_wikiner](https://github.com/explosion/projects/tree/v3/pipelines/ner_wikiner)'
- name: WingCode
  text: 'Duygu Altinok

    I see that spacy supports distributed training via ray. Is the text-preprocessing
    &amp; inference pipelines also distributed?'
  replies:
  - name: Duygu Altinok
    text: No, not supported due to Cython reasons.
- name: Krzysztof Ograbek
  text: Duygu Altinok Is it possible to perform stemming using spaCy? If yes, how?
    If not, why? I know there is lemmatization but I couldn't find stemming
  replies:
  - name: Duygu Altinok
    text: 'Thanks for the question!

      No, we don''t have a stemming component.

      You can hunt down the `root` of a word either by lemmatization or stemming.
      Lemmas are more useful in general, so we prefer using lemmas.'
  - name: Evren Unal
    text: "Duygu Altinok  this question may be out of context.\nI want to build an\
      \ \"arabic to turkish\" dictionary.\n I surmise that i need to use a stemmer\
      \ for it.\nWould you suggest a tool for arabic word stemming?"
  - name: Duygu Altinok
    text: 'Hey ho!

      For this task, you need a lemmatizer, stemmer won''t be much of help.

      I know two good Arabic lemmatizers, Farasa [https://farasa.qcri.org/lemmatization/](https://farasa.qcri.org/lemmatization/)
      and Madamira [https://camel.abudhabi.nyu.edu/madamira/](https://camel.abudhabi.nyu.edu/madamira/)

      If you need further help you can always open an issue at spaCy discussions :woman-raising-hand:'
  - name: Evren Unal
    text: "Thank you very much\U0001F642"
- name: Noa Tamir
  text: "Hi Duygu Altinok and thanks for joining us for the Q&amp;A this week!\nI've\
    \ been using spaCy a bit recently to detect sentences in legal text. I was really\
    \ impressed with the documentation and how easy it was to get started. \nFor now,\
    \ I'm particularly interested in the more advanced chapters, as I can see myself\
    \ needing to tweak the model to achieve better results and haven't gotten into\
    \ that yet. \nWould you say the learning curve for the advanced chapters is as\
    \ quick as getting started or does it get steeper as you progress? What other\
    \ domains / resources would be useful to speed up mastery of the advanced chapters?"
  replies:
  - name: Duygu Altinok
    text: "I'd say no, you need spend more energy on advanced chapters \U0001F642\
      \ Advanced chapters uses information from previous chapters, so one needs to\
      \ really melt  what they learnt so far into one pot  to digest the content.\
      \ Still, putting knowledge together and at the end how code ends up is fun \U0001F609"
- name: Tim Becker
  text: 'Hi Duygu Altinok thanks for being here and answering our questions. I would
    like to ask:'
  replies:
  - name: Duygu Altinok
    text: Thanks for the questions!
- name: Tim Becker
  text: '- What project would you recommend to do if you want to get started with
    spaCy?'
  replies:
  - name: Duygu Altinok
    text: "Universe has a number of projects: [https://spacy.io/universe](https://spacy.io/universe)\n\
      All of the resources are great. I can recommend negspaCy, EpiTator  and Rule-based\
      \ Matcher Explorer for new comers \U0001F609"
- name: Tim Becker
  text: '- Are there drawbacks of using spaCy in comparison to other tools?'
  replies:
  - name: Duygu Altinok
    text: "I don't know any \U0001F642"
- name: Tim Becker
  text: '- What is new in spaCy 3.0? Do you cover the new features in your book?'
  replies:
  - name: Duygu Altinok
    text: "That's a long list \U0001F642 I can recommend Ines's video ([https://www.youtube.com/watch?v=BWhh3r6W-qE](https://www.youtube.com/watch?v=BWhh3r6W-qE))\
      \ and this great page: Rule-based Matcher Explorer\nMy book is spaCy 3.x compatible.\
      \ I focused on how to create applications withspaCy rather than spaCy inetrnals."
  - name: Tim Becker
    text: thank you Duygu Altinok
- name: Allan
  text: 'Hello Duygu Altinok, appreciate your taking the time this week to answer
    questions!

    For someone getting started in NLP, would learning it using Spacy be appropriate?
    Or is there too much performed automatically by the  library/framework that one
    would miss out on some basics?'
  replies:
  - name: Duygu Altinok
    text: Thanks for the question!
  - name: Duygu Altinok
    text: "I'd say it's a good start because one needs to understand the linguistic\
      \ concepts to grasp the spaCy concepts.\nIf I was a starter I'd do the following:\n\
      - Get started with Keras\n- Read Jurafsky's chapters 1-7\n- Get started with\
      \ spaCy\n- Read Jurafsky chapters 12-14\n- Become more accustomed to working\
      \ with  Keras, work on some easy/mid-level text classification projects\n- Advance\
      \ with spaCy\n- Do some seq2seq models with Keras\n- Read rest of Jurafsky\n\
      More advanced NLP colleagues (including me \U0001F642 ) designs and uses different\
      \ types of seq2seq archtiectures for different tasks. At the very end while\
      \ coding you should always have a clear mind, almost all text based models based\
      \ on a linguistic concept. Without grasping the linguistic concepts, it's easy\
      \ to get lost. This is why I offer learning spaCy, while using the library you\
      \ get a chance to work with different concepts of linguistics. Hope it works\
      \ \U0001F642"
  - name: Duygu Altinok
    text: 'Forgot to give the Jurafsky book: [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)'
  - name: Allan
    text: Thanks Duygu Altinok !
- name: Allan
  text: "Another question\u2026 how robust are the pre-trained pipelines?  In what\
    \ scenarios would one need to (re)train their own model as opposed to just using\
    \ the pre-trained ones."
  replies:
  - name: Duygu Altinok
    text: "Pretrained pipelines are quite good and usable (at least for German, English,\
      \ French, Spanish and Portuguese I tried those ones myself \U0001F601 )\nSome\
      \ of the projects you need your own NER definitely, but some of the projects\
      \ you don't need to if your design includes general entities such as location,\
      \ person, time-date, money entities. Here's a some example code for  parsing\
      \ restaurant reservation utterances (extracting ents and intent) : [https://github.com/PacktPublishing/Mastering-spaCy/tree/main/Chapter10](https://github.com/PacktPublishing/Mastering-spaCy/tree/main/Chapter10)"

---

Build end-to-end industrial-strength NLP models using advanced morphological and
syntactic features in spaCy to create real-world applications with ease.

spaCy is an industrial-grade, efficient NLP Python library. It offers various pre-trained
models and ready-to-use features. Mastering spaCy provides you with end-to-end coverage
of spaCy's features and real-world applications.

By the end of this book, you'll be able to confidently use spaCy, including its linguistic
features, word vectors, and classifiers, to create your own NLP apps.