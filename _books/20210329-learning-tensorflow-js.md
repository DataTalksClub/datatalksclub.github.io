---
title: "Learning Tensorflow.js"
description: "Book of the Week. Learning Tensorflow.js by Gant Laborde"
cover: "images/books/20210329-learning-tensorflow-js/cover.jpg"
image: "images/books/20210329-learning-tensorflow-js/preview.jpg"
start: 2021-03-29 00:00:00
end: 2021-04-02 22:59:58
authors: [gantlaborde]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/learning-tensorflowjs/9781492090786/
  - text: Amazon
    link: https://www.amazon.com/gp/product/1492090794
  - text: Book's GitHub repository
    link: https://github.com/GantMan/learn-tfjs

archive:
- name: Ricky McMaster
  text: Hi Gant, thanks for doing this!  At the beginning of your book you outline
    several benefits of using JavaScript for ML and I definitely understand that,
    especially the no-install aspect.  However, for companies with a substantial ML
    implementation using Python, for example, are there compelling reasons to migrate
    regardless in your view, or would it only make sense to implement Tensorflow.js
    given specific business cases or regulatory reasons (you also mention privacy)?
  replies:
  - name: Gant
    text: 'In my opinion, if your AI is not your primary business then AI on edge
      makes a lot of sense.  You''re trading freedom of your model for security as
      the model maintainer.

      Example:   Your AI does style transfer for makeup.  Then it''s amazing to run
      this on the browser on the client and get more people to click purchase for
      their makeup or even hair dye packages.

      However, if your model is proprietary and your work is to apply the makeup/hairdye
      it''s  harder to protect your model, as it must be downloaded to the client.'
  - name: Gant
    text: I believe more and more people will lean towards scalability and even depend
      on cool things like federated learning, and to do that we'll all need to have
      a JavaScript arm of our MLOps
  - name: Ricky McMaster
    text: Got it, nice example Gant.  So depending on the use case it can certainly
      make sense to have client- and server-based deployments in parallel, at least
      in the short- to medium-term.
  - name: Gant
    text: absolutely.  And you can easily convert TF to TFJS models.   Most of them
      convert just fine.
  - name: Ricky McMaster
    text: "That would have been my follow-up question \U0001F642"
  - name: Ricky McMaster
    text: Thanks a lot for your response
- name: "Mert Bozk\u0131r"
  text: "Hello Gant, I know you from Merve Noyan's podcast \U0001F642\nWelcome here.\n\
    A lot of people who aspring data scientist know python and libraries for this\
    \ area. Machine Learning and Deep learning so important of course but I think\
    \ python isn't enough for ML Engineer or Data Scientist. This titles require Back-end\
    \ of course. What do you think about back-end? there are 3 ways in back. You would\
    \ deploy your model Web server, mobile application and of course Devops(docker,kubernetes,\
    \ you can dockerize your model.)\nMy question is which one will populer in future\
    \ ?\nI want to add one more skill to myself but I don't know which one I have\
    \ to add. Actually this question is a little personal question because, You don't\
    \ know which one I will love or hate, but I wanted to ask."
  replies:
  - name: Gant
    text: 'If I understand correctly, you''re interested in my preferred backend solution
      for a web-hosted model.

      I think microservices/cloud functions are perfect for models in the backend,
      because they are very "pay as you go" with infinite scalability.

      So I would prefer setting up an AWS lambda that handles a result and reports
      back the results.'
  - name: Gant
    text: These are not limited by GPUs either.   The whole problem of dynamically
      allocating resources for your server model is handled by the service, and faster
      and more scalable than either of us could hope.
  - name: Gant
    text: The largest benefit, is that when the model is not in use, the costs are
      quite minimal.    I've got several free AWS files/services I have released in
      the wild from past conference talks.   They've never gone over $10 USD a month.
  - name: "Mert Bozk\u0131r"
    text: 'Okey, I got it. Thankss :heart:'
- name: Alexey Grigorev
  text: With TF.js, how does a training pipeline look like? Do you do training in
    python and then export the model to use in JS, or you do the entire thing in JS?
  replies:
  - name: Alexey Grigorev
    text: In Python, there are many nice libraries for data augmentation and different
      image manipulations. I'm wondering what happens when we move to the browser.
      Do we need to re-implement all this functionality in JS?
  - name: Gant
    text: 'So if you''re needing the power of python libs, I generally use Python
      to train for my advanced networks and then convert it down to JS.

      In the book, I show you object localization and detection.  Both of those I
      decided to do in Python for ease and then convert over.

      But you can definitely do it in JS, and I show how.

      In the book the Tic Tac Toe model was trained in JS, and in chapters 8, 9, 10,
      11, 12 all models are trained in JS.'
  - name: Gant
    text: I think Python wins in having a history of lots of libs.  But the speed
      of training in Node is no joke!
  - name: Alexey Grigorev
    text: What are some good image manipulation libraries in node?
  - name: Gant
    text: 'Similar to imgaug is this:  [https://github.com/piercus/image-augment](https://github.com/piercus/image-augment)'
  - name: Gant
    text: I think you'll see more and more JS level tools coming in the next 2 years
  - name: Alexey Grigorev
    text: Oh nice, thank you!
- name: Neal Lathia
  text: "&gt; seasoned AI veterans and web developers alike can help propel the future\
    \ of AI-driven websites\nWhich type of folks do you find using `Tensorflow.js`\
    \ more - seasoned AI veterans, or web developers? (Am assuming that the intersection\
    \ of these two camps may be somewhat smaller that the union \U0001F642 )"
  replies:
  - name: Gant
    text: 'using more: web developers are playing with all kinds of amazing tech and
      will continue to grow.  I think in quantity the current winner is web devs.

      However, in quality, I think the best projects are coming from seasoned AI veterans
      who are leveraging AI in web.  The most profitable and impressive projects are
      people who know how to make this new avenue of AI sing.'
- name: Alexey Grigorev
  text: Let's say I'm a python developer who wants to learn Tensorflow.js to use in
    my projects. How would you suggest to get started? Would your book will be enough
    or I already need to know some JS?
  replies:
  - name: Gant
    text: I expect a basic level of JavaScript skills.  But all the code is available.   If
      you've been programming for a while, you can probably learn a lot about JavaScript
      using the book.   You might need to take a moment to go look up a function,
      but if you know Python you'll probably be just fine.
  - name: Alexey Grigorev
    text: Is there a good learn-JS-in-15-minutes tutorial for those who already know
      how to program?
  - name: Wendy Mak
    text: I think if you just read/tinker with some js you can pick it up in 15mins
      (just remember those curly brackets ;)) (and also async stuff can trip you up
      if you're not careful)
  - name: Gant
    text: 'Glancing through this, here''s a 1hr jumpstart that seems decent

      [https://www.youtube.com/watch?v=IEf1KAcK6A8](https://www.youtube.com/watch?v=IEf1KAcK6A8)'
- name: Dmitry Yemelyanov
  text: Hello, Gant! I have tried porting some my TensorFlow2.0 models to TF.js and
    have been quite disappointed by the fact that lots of cool new features are poorly
    supported (for example, feature columns). Would you agree with my opinion that
    feature-wise TensorFlow.js is cursed to always lag behind TensorFlow? Or maybe
    one day it will take the lead?
  replies:
  - name: Gant
    text: 'Yes.  TFJS will always lag behind.   However, in a few ways it is ahead.  TFJS
      1.0 was using TF 2 syntax before TF 2 was released.

      I think you''ll continue to see TFJS parity be a priority, but yes, lagging
      behind.'
  - name: Dmitry Yemelyanov
    text: Thanks for your answer. I hope this project will get more attention thus
      voluntary contribution from the open source community.
- name: Gant
  text: Would you crazy kids be interested in seeing some internal graphics and process
    stuff?
  replies:
  - name: Amr Alaa
    text: That will be awesome for sure
  - name: Alexey Grigorev
    text: Yes!
  - name: Gant
    text: I had to do my own graphics.  I did OK
  - name: Gant
    text: Some of my examples were just plain silly
  - name: Gant
    text: The editors were  AMAZING though, they loved everything I had
  - name: Gant
    text: I'm quite proud of this diagram... but I know what they make will be better
      for print
  - name: Gant
    text: Also, I used coworkers in examples.  This will let me know if they actually
      read the book
  - name: Gant
    text: I was worried if some of my graphics would work in B&amp;W, but they gave
      them the thumbs up!!!!
  - name: Amr Alaa
    text: Wow, looks interesting already
- name: Amr Alaa
  text: 'Hey Gant

    Thanks for your time with us here, waiting forbthe interanl graphics..

    Here''s my question

    does TensorFlow.js have access to the file system in the browser host environment?

    if it does not, that means available data resources are limited and can put restrictions
    on file sizes needed for training and verifying, right?'
  replies:
  - name: Gant
    text: "TensorFlow.js can run on client or server.\nSo if you\u2019re running your\
      \ training on a machine using Node.js you have direct access to the filesystem\
      \ via Node.js.   Then you\u2019re just managing stream and RAM.\nIf you\u2019\
      re running on the browser, you are sandboxed.  This means you cannot access\
      \ the filesystem and you\u2019ll need to load your data via compatible URIs.\
      \  Browsers have DBs in local storage, RAM, cookies, and all kinds of fun places\
      \ you can gather data.\nBecause of the sandbox, I would recommend only minor\
      \ amounts of training to happen in the browser if you have a significant data\
      \ source.   The browser is much better at utilizing trained models rather than\
      \ training models.\nThis does break down when you want customization for your\
      \ client, however.   So if you\u2019re going to do transfer learning or federated\
      \ learning, you can get real benefits from training in the browser, but yes,\
      \ it\u2019s constrained.\nMy suggestion, do base training in Node.js, then ship\
      \ the model.   Do transfer/federated learning in the browser as needed."
  - name: Amr Alaa
    text: Super, looks clearer now
- name: Alexey Grigorev
  text: Which chapter did you enjoy the most? And which one was the most challenging
    for you?
  replies:
  - name: Gant
    text: 'That''s a tough one!!!

      I guess the capstone project was pretty hard for me.  Bc I had to come up with
      something that tied all the lessons from the book together into a cohesive unit.  It
      was a fantastic end for the book though!  But tough!

      Second hardest chapter is chapter 1... I rewrote that damn thing 10xs

      My favorite chapter was probably Chapter 10, which was simple image training.  It
      felt fun and rewarding.

      Chapter 6 was a secondmost favorite, because we hook a model up to a webcam!'
  - name: Alexey Grigorev
    text: Sounds like a lot of fun!
- name: Alexey Grigorev
  text: Also, as an author myself, I'm really impressed by how fast you finished your
    book. Can you tell us a bit about your process, and how you organized your time
    to work on the book?
  replies:
  - name: Gant
    text: 'I have to say the pandemic helped.   I was able to get into a writing frenzy.   My
      editor told me, "Ride that wave!" and so I did.  The more I wrote the easier
      it became and I hit a traction point where I realized I was running out of chapters.   At
      that point, I had to assess what makes it in the book and what didn''t.

      After that strange hiccup, the finish line was in sight and I used the rest
      of my frenzy to finish the book.

      Since I finished the book, I''ve done a whole lot of nothing!   I think I''m
      recovering.  I don''t even read cool projects right now, I binge watched a whole
      season of a Netflix show.'
  - name: Alexey Grigorev
    text: How did get into this flow mode? Or it just happened itself?
  - name: Gant
    text: To be honest, I didn't get into it at first.   I had so much trouble writing
      chapter 1.   However, like gradient decent, each time I took a step that felt
      right, I leaned into it.   Next thing I knew I was running.
  - name: Gant
    text: One thing that reallllly helped, was having people review chapters.   That
      helped me see large leaps of logic I made, and when I went back to fill in the
      missing gaps, my mindset carried me to how they should see the next thing and
      the next.   Sort of like reading the book from an outside perspective, I had
      a conversation with a hypothetical audience.
- name: Daniel Wexler
  text: "Hi Gant can you compare the back-end features of tfjs-node against Python?\
    \ What\u2019s missing from tfjs-node that would encourage more use of JS on the\
    \ back-end? Does tfjs-node have any advantages over Python on the back-end?"
  replies:
  - name: Gant
    text: 'I feel like web frameworks that use Python are generally treated as second-class
      in the web world.   Node for cloud etc is easy.

      Node has even outperformed Python in quite a few benchmarks.

      IMO, if you''re using backend, it needs to match the team maintaining it.  Focus
      on dev preference.'
  - name: Gant
    text: The big advantage is that the code is portable to client, and IoT
  - name: Daniel Wexler
    text: Similar to portability, you can provide the same computations in the client,
      on customer hardware, and at scale on the server.
  - name: Daniel Wexler
    text: "I\u2019m just trying to understand why I don\u2019t see more discussion\
      \ of TFJS on the backend? I don\u2019t have stats, but I see much more traffic\
      \ about TF+Python than TFJS in Node. Like you said, I\u2019d expect the web\
      \ backend work to be more JS/Java, but I just don\u2019t see much about that\
      \ in the wild."
  - name: Daniel Wexler
    text: "Wendy Mak\u2019s comment about async/await makes me think that Data Scientists\
      \ might just be more comfortable with Python\u2019s less asynchronous nature?"
  - name: Gant
    text: 'In my opinion it''s a momentum thing.   Same reason JavaScript is everywhere.

      Python was the spoken language for primary data culture, so it will take time
      for new solutions to root.'
- name: Wendy Mak
  text: hi Gant do you find the async nature of javascript a bit annoying to work
    with when you are building models/training? Also, do you use tfjs node with the
    GPU? the browser can obviously make use of webgl but this is less clear for node?
    there's [https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-nodegl](https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-nodegl)
    but the doc says it's under heavy development
  replies:
  - name: Daniel Wexler
    text: FYI, tfjs-node-gpu works just fine in node and uses GPUs when available
      using the main TF Cuda backend. Interesting question about async JS. Perhaps
      many folks feel more comfortable with the more traditional Python TF binding?
  - name: Gant
    text: 'I''m find with async await.  It''s common in JS, so it feels natural.

      As for the second part, tfjs-node-gpu works great for accesing the GPU on node.

      The browser uses WebGL, and they have an experiment with WebGPU which is promising.

      Lastly, they are doing some amazing stuff in WASM with threads!   I know this
      is a bit off-topic, but it''s cool.

      CUDA now has JavaScript API, so I imagine tfjs-node-gpu will just keep getting
      better and better.  It worked great for me.'
  - name: Wendy Mak
    text: "&gt; I'm find with async await. It's common in JS, so it feels natural.\n\
      ah, cool, although, I think I like synchronus better lol --  the async things\
      \ gave me no end of headaches when I was a js dev \U0001F602 (well, I was also\
      \ trying to munge together something that takes about 10 steps each of which\
      \ has a callback...)"
  - name: Daniel Wexler
    text: Thanks for the GPU.js tip!
  - name: Gant
    text: 'Oh, GPU.js is a different library.  Brain.js uses GPU.js

      WebGL and WebGPU are being supported as backends for TFJS'
  - name: Gant
    text: "we need more acronyms ^ \U0001F602"
  - name: Daniel Wexler
    text: "I know! I hadn\u2019t heard there was a (limited) JS Cuda binding until\
      \ you mentioned it."
- name: Hironori Sakai
  text: "Hi, Gant Thanks for participating book of the week.\nI have a question about\
    \ TF.js and federated learning. My question can be stupid, because I do not understand\
    \ federated learning much. But if I understand correctly, then\n- Federated learning\
    \ proposes a model training on a distributed system without collecting the data\
    \ in one place. \n- 3rd-party cookie will be replaced with FLoC (federated learning\
    \ of cohorts). \nBecause FL(oC) involves a distributed system, especially web\
    \ clients/browsers for FLoC, it is natural to use TF.js to implement FL so that\
    \ FLoC is one of the use cases. So my question is: Do you think TF.js can be mainstream\
    \ of FL(oC)?\n(Recently Google released a new version of chrome on which FLoC\
    \ works, but I do not know its implementation.)"
  replies:
  - name: Gant
    text: 'Federated learning is pretty complicated, and there''s the idea and implementation
      details.

      The idea (at least in my head).

      1. Create a model

      2. Send copies to people

      3. Use transfer learning to personalize and improve the model

      4. Send back the improved models (NOT the user''s data)

      5. Improve the core model that is distributed.

      I''m unaware of the FL(oC) specifics, but I significantly believe Google has
      a lot of benefit in getting federated learning going.   I think you can expect
      TFJS to be a core contributor to this.

      I know Google is seeking lots of adjustments to W3C standards based on TFJS,
      but it''s hard to know which pieces are prioritized and why.'
  - name: Hironori Sakai
    text: Thanks for your valuable answer. When I googled FL with TF.js quickly, I
      could find only one TF.js project and it is not maintained. But I found it quite
      strange, because JavaScript is the default option if lots of different browsers
      are/must be involved. This was the motivation of my question. I am wishing that
      a good FL(oC) Framework on TF.js will appear soon.
  - name: Gant
    text: I have no doubt that this will emerge.  I think there's a lot of green opportunities
      in TFJS for sure.


---

Combining the demand for AI with the ubiquity of JavaScript was inevitable. With Google's TensorFlow.js
framework, seasoned AI veterans and web developers alike can help propel the future of AI-driven websites.
In this guide, author Gant Laborde--Google Developer Expert in machine learning and the web--provides a
hands-on, end-to-end approach to TensorFlow.js fundamentals for a broad technical audience that includes
data scientists, engineers, web developers, students, and researchers.

You'll begin by working through some basic examples in TensorFlow.js before diving deeper into neural
network architectures, DataFrames, TensorFlow Hub, model conversion, transfer learning, and more. Once
you finish this book, you'll know how to build and deploy production-ready deep learning systems with
TensorFlow.js.