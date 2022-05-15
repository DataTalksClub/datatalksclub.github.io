---
title: "Generative AI with Python and TensorFlow 2"
description: "Book of the Week. Generative AI with Python and TensorFlow 2 by Joseph Babcock and Raghav Bali"
cover: "images/books/20211108-generative-ai-with-python-and-tensorflow-2/cover.jpg"
image: "images/books/20211108-generative-ai-with-python-and-tensorflow-2/preview.jpg"
start: 2021-11-08 00:00:00
end: 2021-11-12 22:59:58
authors: [Joseph Babcock, raghavbali]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/generative-ai-with-python-and-tensorflow-2/9781800200883
  - text: Amazon
    link: https://www.amazon.com/Generative-AI-Python-TensorFlow-Transformer/dp/1800200889
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/Hands-On-Generative-AI-with-Python-and-TensorFlow-2

archive:
- name: Kshitiz
  text: 'Hi Raghav Bali and Joseph. Thanks for doing this. I am curious to know -

    1. What problems Generative models can solve right now?

    2. What are some latest developments in the field of Generative models?

    3. With deepfakes being a think now, do you think the world has enough artillery
    to deal with it?'
  replies:
  - name: Raghav Bali
    text: 'Hey Kshitiz, interesting and important questions... Here''s my take:

      1. Generative models are being leveraged for a numbers applications currently.
      Some popular examples are: Painting/Art Generation (a number of neural artists
      are all the rage nowadays), FaceGeneration(check [thispersondoesnotexist.com](http://thispersondoesnotexist.com))
      for stock photos, music generation for high quality background scores (free from
      copyright issues), style transfer for fun usecases (Snapchat/Instagram filters)
      , dataset augmentation (for classification usecases) and a number of other domains.

      2. Recent Developments in the field of Generative Models: well this is quite a
      broad question but a number of amazing works are focusing on improving the output
      quality with far lesser infra and training time. GANs are being improved to be
      more stable , lean yet generate extremely high quality outputs. See the likes
      of StyleGAN3 from folks at NVIDIA. We cover quite a few of these recent architectures
      in our book as well.

      3. Well, with any powerful technology, there is always a danger of it being used
      improperly. Researchers ans practitioners like us have a huge task at our hands
      to make people aware of stuff like deepfake. Apart from awareness, a number of
      research labs are focusing on ways of identification of fake(deep fake) content
      (though there is a long way to go for this). In short, tldr; we are not there
      but efforts are being made nonetheless'
  - name: Kshitiz
    text: Raghav Bali  Thanks for the responses!
- name: Cam Buchanan
  text: "Hi Raghav and Joseph, interesting stuff thanks for taking the time. I\u2019\
    m curious when making content in the creative field based on generative models,\
    \ are there any methods you use to avoid \u201Ctraps\u201D like copyright infringement?"
  replies:
  - name: Raghav Bali
    text: 'Hey Cam Buchanan

      Apologies, looks like I somehow missed answering this very interesting and pertinent
      question.

      Copyright infringement (and other aspects of law are quite varied and dependent
      on interpretation). But keeping the nuances aside, the following are some rules
      of thumb to keep in mind when generating content using models:

      1. Generative Models are searching the training space at a very abstract level.
      There is a very highly chance the output would be derivative of the training
      space. Even solutions like Github''s autopilot and the likes have raised similar
      questions

      2. Make use of available tools for a quick check. For instance, uploading content
      on soundcloud, youtube, etc, you should pay attention to the inbuilt copyright
      checks. If your content is getting flagged, go back to drawing board. But again,
      these tools are not always foolproof

      3. Always mention a caveat or a disclaimer on how you generated this content
      and if someone claims their copyright, best to oblige or collaborate (if it
      is indeed the case)'
- name: WingCode
  text: "Hi Raghav Bali, Good to have you here again \U0001F642\nI was wondering whether\
    \ Generative AI can help in video summarisation within each frame of context.\
    \ ex: In YouTube videos it is called video chapters ([https://techcrunch.com/2020/05/28/youtube-introduces-video-chapters-to-make-it-easier-to-navigate-through-longer-videos/](https://techcrunch.com/2020/05/28/youtube-introduces-video-chapters-to-make-it-easier-to-navigate-through-longer-videos/))\
    \  where we have to manually create the window with it's relevant text summary.\
    \ This would be helpful for DTC since we do it manually \U0001F604\nDoes it have\
    \ a specific name in ML research where you generate a super short 2-5 words summary\
    \ for long piece of video, text or audio?"
  replies:
  - name: Raghav Bali
    text: 'Glad to have you back in this discussion WingCode. Excellent question n
      I can shamelessly admit that it took me down a rabbit hole. I am still looking
      to find more details on this (haven''t got too far yet), but here''s my take:

      1. Video segmentation sounds like an apt name for it but fortunately or unfortunately
      it refers to segmenting objects within a given video frame, so we might have
      to get creative here. Let''s brain-storm till we find some papers detailing
      this?'
  - name: Raghav Bali
    text: '2. contrary to your mention, it seems youtube started creating video chapters
      automatically using "ML". The support pages do not detail much about it though.
      See here: [https://support.google.com/youtube/answer/9884579](https://support.google.com/youtube/answer/9884579)

      Seems like the manual stuff for DTC can be managed through this feature? The
      documentation says that the service does the segmentation based on different
      text in the video to generate titles etc but I am pretty sure there is more
      here than meets the eye'
  - name: Raghav Bali
    text: '3. Creating summary from a video frame sounds similar to the task of image
      captioning. There are a number of works which do this quite nicely, starting
      points are: [https://arxiv.org/abs/1411.4555](https://arxiv.org/abs/1411.4555)
      , [https://arxiv.org/abs/1601.03896](https://arxiv.org/abs/1601.03896)'
  - name: WingCode
    text: "Thank you Raghav Bali for digging up all the resource and the elaborate\
      \ answers as usual \U0001F642"
- name: Alexey Grigorev
  text: What's the easiest way to generate an intro tune for a podcast? Asking for
    a friend
  replies:
  - name: Raghav Bali
    text: 'Well, Generative Models are to the rescue here (RNNs in particular). <#C01F53D373M|shameless-promotion>
      and plug, refer to my article here: [https://towardsdatascience.com/lstms-for-music-generation-8b65c9671d35](https://towardsdatascience.com/lstms-for-music-generation-8b65c9671d35)

      The article also points to a few samples generated using the said architectures.
      The book explores it to a greater depth'
- name: Lavanya M K
  text: "Hi Raghav Bali asking this totally out of curiosity. Is it possible to create\
    \ a sort of reverse subtitling from Generative AI?.  Ex. Given text \"a beautiful\
    \ place\", the model has to generate a picture/video/art of a scenic place, something\
    \ similar to how our mind generates.\n If so, how are these models trained?"
  replies:
  - name: Wendy Mak
    text: you might want to look at what openai has been doing with dall-e/clip etc
      (one blog post with runnalbe code [https://minimaxir.com/2021/08/vqgan-clip/](https://minimaxir.com/2021/08/vqgan-clip/)
      )
  - name: Raghav Bali
    text: Thanks for your question Lavanya M K and kudos to Wendy Mak for the perfectly
      crisp answer. DALL-E and CLIP are state of the art works and generate some really
      wonderful works of art.
  - name: Raghav Bali
    text: "Lavanya M K found something interesting on the lines of your question.\
      \ I know its well past the AMA but who cares \U0001F609\n[https://blogs.nvidia.com/blog/2021/11/22/gaugan2-ai-art-demo/](https://blogs.nvidia.com/blog/2021/11/22/gaugan2-ai-art-demo/)"
  - name: Lavanya M K
    text: This looks super exciting. Thanks Raghav Bali for sharing.
  - name: Lavanya M K
    text: Really interested to know how training is done for such models
- name: Raghav Bali
  text: 'Not answering to a question but Generative Models are becoming more and more
    common and creative nowadays. This recent art gallery exhibition by Emil Wallner
    (leading AI researcher with Google) takes Style Transfer to the next level, see
    here: [https://twitter.com/EmilWallner/status/1453050980438843397](https://twitter.com/EmilWallner/status/1453050980438843397)'
  replies:
  - name: Raghav Bali
    text: 'Another interesting take on Generative AI

      [https://twitter.com/_joelsimon/status/1458507647515254785?t=rrN80ZIEweAX0ITBvmV7VQ&amp;s=19](https://twitter.com/_joelsimon/status/1458507647515254785?t=rrN80ZIEweAX0ITBvmV7VQ&amp;s=19)'
- name: Tim Becker
  text: Hi Raghav Bali, thanks for being here again!
  replies:
  - name: Raghav Bali
    text: "Hey Tim Becker nice to meet you \U0001F642"
  - name: Tim Becker
    text: "Thank you for answering my questions \U0001F642"
- name: Tim Becker
  text: '- In your book, are you talking about data augmentation with generative AI?
    I am particularly interested in when this technique is useful and when not? And
    how beneficial is it? I guess, there are certain limits to this approach?'
  replies:
  - name: Raghav Bali
    text: 'Unfortunately no. Data Augmentation using generative models is definitely
      a topic worth exploring but given that there weren''t many books introducing
      generative models and different nuances associated. Hence, we decided to focus
      the book on different types of generative models along with their different
      applications.

      But yeah, outside the book using generative model for data augmentation is certainly
      gathering some steam. There are works by folks like Antoniou et. al. spearheading
      this space (important paper: [https://arxiv.org/abs/1711.04340](https://arxiv.org/abs/1711.04340))

      My two cents on the topic (though I am pretty new to this aspect itself):

      1. Highly beneficial if you have a training data space which is not so expansive/diverse
      (for the lack of better word) . This would help you generate samples for a robust
      model

      2. Limits: certainly risky if you do not have a metric to understand the quality
      of your samples. For instance, I am working in the healthcare space and imagine
      a scenario where we would want to generate sample X-Rays for lung cancer. We
      would need very tough quality check to ensure that generated samples indeed
      make sense'
- name: Tim Becker
  text: '- Could you give an example of an adversarial learning paradigm?'
  replies:
  - name: Raghav Bali
    text: 'This is something I want to explore for quite some time but haven''t been
      able to. Really interested to read and understand the poisoning strategies.
      Maybe we can catchup sometime soon to discuss more.

      *Ask to the larger community here: any pointers/materials to get started?*'
  - name: Maja
    text: This is a very interesting research and [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9483649)
      about CryoGAN for me.
- name: Tim Becker
  text: '- For you personally what is the most exciting topic in generative AI?'
  replies:
  - name: Raghav Bali
    text: 'On a broader level, the whole concept of GAN is very exciting to me. Every
      new architecture and the ideas behind them simply amaze me.

      From an application standpoint, I believe Music Generation and DeepFakes (though
      notorious) have great potential'
- name: WingCode
  text: 'Hi Raghav Bali,

    Have you come across any work on unsupervised labelled interpretable controls
    for GANs ? [https://www.youtube.com/watch?v=jdTICDa_eAI](https://www.youtube.com/watch?v=jdTICDa_eAI)
    In this video, they manually play around on each component to understand the changes
    it brings about but then it is manual and requires a human annotator to label
    each component.'
  replies:
  - name: WingCode
    text: "Digging up on the above paper, found reference to this paper [https://arxiv.org/abs/2002.03754](https://arxiv.org/abs/2002.03754)\
      \ which finds these manipulation axises unsupervised but I am not sure whether\
      \ it generates a labeled text for that specific axis \U0001F642"
- name: Raghav Bali
  text: 'Awesome week and equally Awesome set of questions. Thank you to all the participants
    and congratulations to all the winners. It''s been fun interacting and discussing
    stuff with you all.

    Thanks Alexey Grigorev again for this wonderful platform. Would love to keep this
    discussion on going.

    Cheers and keep exploring guys n girls'
  replies: []

---

In this book, you’ll explore the evolution of generative models, from restricted Boltzmann
machines and deep belief networks to VAEs and GANs. You’ll learn how to implement models
yourself in TensorFlow and get to grips with the latest research on deep neural networks.