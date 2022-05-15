---
title: "Transfer Learning in Action"
description: "Book of the Week. Transfer Learning in Action by Raghav Bali"
cover: "images/books/20211004-transfer-learning-in-action/cover.jpg"
image: "images/books/20211004-transfer-learning-in-action/preview.jpg"
start: 2021-10-04 00:00:00
end: 2021-10-08 22:59:58
authors: [Dipanjan Sarkar, raghavbali]
links: 
  - text: Book's page
    link: https://www.manning.com/books/transfer-learning-in-action
  - text: Book's GitHub repository
    link: https://github.com/dipanjanS/transfer-learning-in-action


archive:
- name: Kshitiz
  text: 'Hi Raghav Bali and Dipanjan,

    Glad to have you here for answering our questions.

    I have few questions to ask here -

    1. Are there any prerequisites for applying transfer learning to get better performance?
    (For e.g. if the data is highly domain specific, I believe, it might not generate
    good results)

    2. Has transfer learning in NLP reached the same performance compared to computer
    vision?'
  replies:
  - name: Raghav Bali
    text: "Kshitiz Full points for the first set of questions. Let me try and answer\
      \ them:\n1. The short answer is yes. Before you plan out for leveraging Transfer\
      \ Learning, you need to keep a few things in mind, such as, how closely related\
      \ are your source and target domains, how many labels/data samples do you have\
      \ from the target domain, etc. These and a few other considerations play an\
      \ important role to determine whether you should use TL or would there be any\
      \ possibility of improved performance. Checkout chapter 1 from the livebook\
      \ for a detailed discussion\n2. Oh yes, this is my personal favourite. Computer\
      \ Vision might have brought ML/DL into the limelight but it is the recent research\
      \ and success of large scale NLP models that have had an even larger impact.\
      \ Most importantly, the concepts of attention, self attention and the Transformer\
      \ architectures have a very important role. These key concepts have not only\
      \ improved the NLP domain but also provided a solid foundation for transfer\
      \ learning. Even more importantly, these concepts though initially were applied\
      \ only to NLP domain, are not being cross pollinated to Computer Vision, Audio\
      \ etc as well.\nThanks for your questions again. Hope my response points you\
      \ in the right direction \U0001F603"
- name: Alexey Grigorev
  text: "Hi Dipanjan Sarkar, welcome \U0001F44B"
  replies: []
- name: Alexey Grigorev
  text: I have a question for Dipanjan Sarkar. Do you describe in your book how to
    make a userpic like yours?
  replies:
  - name: Alexey Grigorev
    text: Does style transfer have anything to do with transfer learning?
- name: Tino
  text: Hello Dipanjan Sarkar, I know that transfer learning is a common concept in
    deep learning but I see it less in traditional algorithms. Some libraries offer
    convenient ways of using it e.g. for a logistic regression. What use cases do
    you know where something like this could be useful? And what do you think about
    using this for boosted trees as the transfer learning here is not well documented
    (from my experience).
  replies:
  - name: Raghav Bali
    text: 'Hi Tino

      Interesting question and something we both are also exploring as well. The iterative
      nature and capacity of deep neural networks make them right candidates for leveraging
      transfer learning (see weight matrices).

      Traditional learning algorithms have been studied for application of transfer
      learning as well (we share some further pointers to this as well, see: [https://arxiv.org/pdf/1812.11806.pdf](https://arxiv.org/pdf/1812.11806.pdf),
      [https://people.csail.mit.edu/lpk/papers/MarxRosensteinKaelblingDietterich-final.pdf](https://people.csail.mit.edu/lpk/papers/MarxRosensteinKaelblingDietterich-final.pdf))

      You are correct, boosted trees such as XGBoost, CatBoost and the likes provide
      APIs to make use of warm start which enables online learning and transfer learning.

      Dipanjan Sarkar, would you want to share more?'
- name: WingCode
  text: 'Hi Raghav Bali &amp; Dipanjan Sarkar ,

    Could you suggest some popular pre-trained models and their use-cases for:

    1. Video

    2. Audio

    3. Timeseries data

    4. Recommendation systems

    Example: NLP - GPT; Q&amp;A answering, text generation, text similarity'
  replies:
  - name: Raghav Bali
    text: "Thanks WingCode, here's my take (pretrained models for specific domains\
      \ but there could be more as well):\n1. Video:\n    a. Classification: movinet,\
      \ tweening_conv3d\n2. Audio:\n    a. Audio Transcription: wave2vec, deepSpeech(2,3,etc),\
      \ Conformer\n    b. Audio Classification: YamNet, TRILL, \n    c. Speech to\
      \ Text: silero-stt (different languages)\n3. NLP: BERT, XLNet, GPT-3, etc for\
      \ a number of tasks such as classification, NER, etc"
  - name: WingCode
    text: "Thank you Raghav for the answer \U0001F642"
- name: ramreddy yasa
  text: "Hi Raghav Bali and Dipanjan Sarkar\nI have few questions:\n1. Does transfer\
    \ learning help if we have a dataset with images that are not similar to ImageNet\
    \ datasets as most of the CNN models are trained on ImageNet datasets? \n2. What\
    \ is the best way to fine-tune the transfer learning model?\n3. How do we initialize\
    \ the weights? If we use the random weights, after proper training do we reach\
    \ similar local minima when compared with model trained using pretrained weights?"
  replies:
  - name: Raghav Bali
    text: "Hey ramreddy yasa, thanks for your questions. Let me try and answer these\
      \ briefly:\n1. This is a really good question. You need to be careful about\
      \ the characteristics between source and target datasets. If they are completely\
      \ different, it is highly likely that transfer learning will have a negative\
      \ impact\n2. Best way to fine tune: well, this is a tricky and subjective question\
      \ i believe. could you share some more details on what is the ask about? Typically\
      \ we freeze till the penultimate layer and update the last layer itself\n3.\
      \ I am not sure if I understand the question but I suppose you are asking with\
      \ respect to ResNet. The typical options are to either initialize the weights\
      \ as:\n    a. random\n    b. pretrained weights file path\n    c. imagenet weights,\
      \ typically bundled with frameworks such as TF, PT, etc"
  - name: ramreddy yasa
    text: "Hi Raghav Bali\nThank you for answering the questions.\nI have updated\
      \ the 3rd question above and in 2nd question I just want to know\n- how many\
      \ epochs do we have to typically train a model by freezing it\u2019s layers\
      \ before training all its layers? \n- Ex: If we train the network by freezing\
      \ the layers for just 5-10 epochs then train whole network for <tel:100-1000|100-1000>\
      \ epoch, will this approach give good results or should I train 1000 epochs\
      \ by freezing the layers itself then train the whole network for another 1000\
      \ epochs?\nIn couple of articles I also saw people freezing till penultimate\
      \ layer and train the network, later train the whole network.  After few epochs,\
      \ If there is no improvement in validation loss, now they freeze the bottom\
      \ layers and train only the top layers. Does this really help?"
- name: Doink
  text: Raghav Bali and Dipanjan Sarkar How to productionize models using Transfer
    learning to deal with milli-second throughput latencies?
  replies:
  - name: Raghav Bali
    text: 'Doink production related questions are very much environment dependent
      (by environment I am referring to budget constraints, infrastructure limitations,
      business SLAs, etc.). For milli-second throughput latencies,  I would recommend
      checking quantization of models or making use of pre-trained models from TF_Hub
      and the likes.

      I know this is a very high level response. Let us discuss more if you have specific
      details around this one'
  - name: Doink
    text: Raghav Bali If you would like to share any experiences which you had on
      the above would love to hear some war like stories if there where any, especially
      when it came to post deployments.
- name: Evren Unal
  text: "Hi Dipanjan Sarkar \nHi Raghav Bali \nAre there any use case of using transfer\
    \ learning for speech generation from text?"
  replies:
  - name: Raghav Bali
    text: "Evren Unal Good question. TTS or speech generation from text is an active\
      \ area of study. Some of the popular models in this field for transfer learning\
      \ are Tacotron, wave2vec (and its variants), deep voice, FastSpeech etc. We\
      \ will be covering a few of these in the later parts of the book as well. Stay\
      \ tuned \U0001F642"
  - name: Evren Unal
    text: "It would be very nice.\nBecouse in that field, there is not much book or\
      \ tutorial for beginner level \nPeople who want to generate their own speach\
      \ engine need some reference about the topic."
- name: Yasser
  text: 'How can we handle transfer learning models which trained  on images data
    with various data types such as text, signal, voice, etc.?

    Can we use this concept to train data with data pre-trained with the same type
    of data?'
  replies:
  - name: Raghav Bali
    text: Yasser are you referring to Multi-Modal architectures which can ingest inputs
      of different data types? I am afraid I would need more details to answer this
      one
  - name: Yasser
    text: "Thanks a lot Raghav Bali for writing this great book and I will wait your\
      \ answer \U0001F642."
- name: Tim Becker
  text: Hello Raghav Bali and Dipanjan Sarkar, awesome topic for a book! It seems
    extremely practical and relevant.
  replies: []
- name: Tim Becker
  text: '- How would you approach selecting the best pre-trained model from, e.g.
    Tensorflow hub, for a specific modeling task. There are so many potential models
    to choose from. Would you test several and compare results?'
  replies:
  - name: Raghav Bali
    text: 'That''s actually a very valid question and challenge. There a few rules
      of thumb I typically follow:

      1. Check the datasets on which the hub/pretrained model is trained upon. The
      higher the similarity/relevance to your problem, the higher the impact of transfer
      learning

      2. The infrastructure requirements of the pretrained model. Unless you have
      access to on demand capacity and budget, there are tradeoffs to be made

      3. The input dimensionality of the pretrained model. If your input is too large
      or too small for the pretrained model, it would be counter productive in most
      cases'
- name: Tim Becker
  text: '- How would you approach the problem of counting specific objects or object
    tracking? I imagine that it should be quite easy to select a pre-trained model
    to recognise certain object, but how to continue?'
  replies:
  - name: Raghav Bali
    text: 'I am not quite sure I understood the question here. There are a number
      of pretrained object detection models to choose from, depending upon your requirements.

      Counting and tracking are downstream tasks, once you are able to detect the
      required object(s) , counting or tracking them is fairly straightforward'
- name: Tim Becker
  text: '- Are there cases in which it is a bad idea to use transfer learning?'
  replies:
  - name: Raghav Bali
    text: Yes, there are cases where transfer learning can have a negative effect.
      For instance (over simplified) image a model trained on fish species and you
      try to use this pretrained model for dog breed classification. More details
      in chapter 1 of our book. Checkout on MEAP
- name: Tim Becker
  text: '- I haven''t heart anything concerning transfer learning for timeseries data
    or simple numeric data. Do you think it is promising?'
  replies:
  - name: Raghav Bali
    text: 'That''s right, there are some works/research labs focusing on the time
      series class of problems from a transfer learning perspective but I haven''t
      personally seen a lot of breakthroughs over there. Off late there have been
      some papers in this space, especially in Time Series Classification space though
      I am yet to go through them in detail to comment.

      Do share your experience on this. I will also circle back if I get anything'
- name: Dr Abdulrahman Baqais
  text: 'Hi Raghav Bali :. Thank you for being here. Few questions:

    1) Transfer learning are extensively in text and image kind of problems. Do you
    think transfer learning can work in other traditional or future domains: for example
    speech.

    2) When it is advisable to start with transfer learning and when it is better
    to build your own solutions from scratch directly.

    3) in a ModelOps era , do you see transfer learning has an advantage over traditional
    solutions?.


    Thank you.'
  replies:
  - name: Raghav Bali
    text: "Hi Dr Abdulrahman Baqais \nThank you for your questions and patience.\n\
      1. Oh yes definitely. Transfer Learning is playing a huge role in the domains\
      \ such as speech, video, Generative modeling etc. Some of the latest speech\
      \ related models are enabling amazing use cases like edge device voice/speaker\
      \ detection etc, all thanks to transfer learning\n2. If you have a pretrained\
      \ model trained on a similar dataset as yours, go ahead and use it. Building\
      \ your own from scratch is typically motivated by scenarios where you have enough\
      \ data, compute and time along with a very nieche domain where you wouldn't\
      \ find a pretrained model.\n3. Absolutely, in the modelOps era, TL is not only\
      \ helping you iterate faster but also achieve better results with lesser effort"
- name: Timur Kamaliev
  text: 'Hi Raghav Bali and Dipanjan Sarkar. Thanks for doing that.

    Just a couple of questions.

    - Can transfer learning give satisfactory results on small datasets? And how the
    training process will be differ in this case? Could you please share some best
    practices from your background?

    - And what often do you use - Pytorch or TF? :)

    Many thanks!'
  replies:
  - name: Raghav Bali
    text: "Hi Timur Kamaliev \n1. Yes, actually TL is highly impactful if your target\
      \ dataset is relatively small. The training process isn't different, you may\
      \ try the pretrained model as a feature extractor with your own shallow classification\
      \ head to achieve the desired results. See chapters 1 and 2 of the book or the\
      \ repo for some easy to understand examples : [https://github.com/raghavbali/transfer-learning-in-action](https://github.com/raghavbali/transfer-learning-in-action)\n\
      2. Depending upon the setup, either is good though I myself prefer TF more than\
      \ PT"
---

Transfer Learning in Action shows you how using pre-trained models can massively improve the accuracy and performance of your machine learning projects. Focused on the real-world applications of transfer learning, you’ll explore how to enhance everything from computer vision to natural language processing and beyond. Master hands-on techniques taken from the latest research, and discover how you can customize open source models for your specific needs.
