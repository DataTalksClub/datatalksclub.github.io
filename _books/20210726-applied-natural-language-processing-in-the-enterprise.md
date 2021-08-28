---
title: "Applied Natural Language Processing in the Enterprise"
description: "Book of the Week. Applied Natural Language Processing in the Enterprise by Ankur A. Patel and Ajay Uppili Arasanipalai"
cover: "images/books/20210726-applied-natural-language-processing-in-the-enterprise/cover.jpg"
image: "images/books/20210726-applied-natural-language-processing-in-the-enterprise/preview.jpg"
start: 2021-07-26 00:00:00
end: 2021-07-30 22:59:58
authors: [ankurapatel, Ajay Uppili Arasanipalai]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/applied-natural-language/9781492062561/
  - text: Book on Amazon
    link: https://www.amazon.com/dp/149206257X


archive:
- name: Rimma Shafikova
  text: "\U0001F44B  NLP beginner here. When we speak about progress in NLP, is it\
    \ always limited to English? Are state-of-the-art approaches transferable to other\
    \ languages? (of interest: Russian, Mandarin)"
  replies:
  - name: Ankur Patel
    text: Yes, the beauty of the state-of-the-art approaches today is that they are
      very transferable to other languages, especially languages where large corpuses
      of text is readily available (e.g., Russian, Mandarin, etc.). Progress is more
      limited in languages where large corpuses of text are harder to come by, though
  - name: Ankur Patel
    text: Basically, to develop very good NLP models today, you need access to massive
      volumes of text (in any language of your choice), which is easy to come by
  - name: Rimma Shafikova
    text: thanks Ankur!
- name: Alex
  text: "Hi there Ankur Patel! First of all, thanks a lot for taking the time to reply\
    \ our questions \U0001F604\nSince this book is aiming to show applied NLP in companies/orgs:\
    \ Do you consider that getting the executive buy-in is difficult, given the conceived\
    \ complexity of getting effective NLP models to work in real-world/business problems?"
  replies:
  - name: Ankur Patel
    text: In general, yes getting executive buy-in is difficult, mostly because this
      is a new space, and executives may prefer the tried and tested over something
      new that they do not fully understand yet
  - name: Ankur Patel
    text: That being said, it does depend on the executive. In my experience, defining
      the deliverable narrowly and showing value in a modest way fast is a good way
      to garner the attention and interest of executives fast
  - name: Ankur Patel
    text: Once they see the return on investment, you can pitch more ambitious projects
  - name: Ankur Patel
    text: Too often, I see people promising too much, and then things take longer
      and cost more and executives become disenchanted by the space because of it
- name: Dr Abdulrahman Baqais
  text: "Thank you Ankur Patel for the book.\nFew questions:\n1) Most NLP advances\
    \ now is based on huge preteained model,  what about the classical ML models (Logistic\
    \ Regression, Bayes naive, LSTM..etc). \nDo you feel that Today's NLP practitioners\
    \ should jump directly to transformers and preteained models."
  replies:
  - name: Ankur Patel
    text: I think the older approaches (regex and classical ML models) still have
      a place even with transformers
  - name: Ankur Patel
    text: It really depends on the task. For example, if you are trying to process
      invoices (OCR + text classification), using transformers is the way to go
  - name: Ankur Patel
    text: If you are performing entity resolution or linking, then a simpler approach
      based on cosine similarity or regex or Elasticsearch may be better
  - name: Ankur Patel
    text: I think having awareness of all the different potential approaches to the
      problem will help you pick the right tool for the given job at hand
  - name: Doink
    text: how to know which to use when? Is there a mindmap especially for those who
      don't have much NLP domain
  - name: Ankur Patel
    text: 'Here is a good approach.

      1. If your task is the same or similar to one of the core NLP tasks here, use
      a Transformer-based model. [https://huggingface.co/transformers/task_summary.html](https://huggingface.co/transformers/task_summary.html)

      2. If your task is for a small dataset or relatively simple or requires interpretability,
      start with the older yet simpler approaches such as rules-based NLP (e.g., regex)
      or classical ML.

      3. If your task is for a large dataset and is more complex in nature, skip the
      rules-based NLP or classical ML and research some of the state of the art NLP
      approaches to solving the problem. Implement one of these approaches.'
- name: Dr Abdulrahman Baqais
  text: "2) NLP domain seems daunting with many subdomains: NER, summarization, translation..etc.\
    \ many tools, many libraries and packages. Yet running  a blacbox preteained model\
    \ can get very high accuracy if it was run by a junior DS who has no clue what\
    \ is going on.\n\n What kind of skills NLP practitioners should equip themselves\
    \ in order to be able to digest all these information and still be in demand in\
    \ industrial market."
  replies:
  - name: Ankur Patel
    text: I think spending 20% of your time learning what is new and effective (in
      an applied setting) is a must. It is true that some of the latest methods are
      so good that they may leap frog existing approaches even without too much tuning
  - name: Ankur Patel
    text: For example, we write about spaCy, Hugging Face, and fastai in our book.
      These are must haves today if you are doing NLP in enterprise
  - name: Ankur Patel
    text: Older libraries such as StanfordNLP and NLTK are much more dated and less
      effective
- name: Dr Abdulrahman Baqais
  text: "3) NLP is taught at an advanced level at separate track in many DS bootcamps\
    \ assuming a solid DS knowledge. \nCan we teach NLP to non-DS to create a citizen\
    \ NLP practitioners?"
  replies:
  - name: Ankur Patel
    text: "It\u2019s possible now, but it wasn\u2019t really possible a few years\
      \ ago. Now there are more easy to use libraries available, but we still have\
      \ a long way to go"
  - name: Ankur Patel
    text: I would say that you need some Python and DS knowledge to begin the NLP
      journey today, but NLP is not necessarily a crazy advanced field
  - name: Ankur Patel
    text: Our book assumes that the reader has some basic Python experience but not
      much more than that
- name: Matthew Emerick
  text: "Hey, Ankur Patel! Thanks for doing this! \nWhat is the singular biggest challenge\
    \ for putting NLP into production?"
  replies:
  - name: Ankur Patel
    text: I find that most NLP specialists struggle with the engineering aspects such
      as refactoring code, developing Docker containers, writing unit and integration
      tests, deploying the model as a service on AWS / Azure / GCP
- name: Matthew Emerick
  text: How important is the study of linguistics to NLP developers?
  replies:
  - name: Ankur Patel
    text: Nope, not necessary today. It helps but it is not required by any means
- name: Matthew Emerick
  text: What do you see as the next big step in NLU?
  replies:
  - name: Ankur Patel
    text: "We need better representations to achieve \u201Clonger-term memory.\u201D\
      \ Without this, NLU is very hard. Attention mechanisms and transformers have\
      \ helped on this front, but we need machines to hold memory over very long spans\
      \ (chapters and chapters of a book), and this is really hard today"
  - name: Matthew Emerick
    text: Would you think symbolic AI mixed with today's statistical methods might
      help?
  - name: Ankur Patel
    text: "I think so. I haven\u2019t studied symbolic AI enough and it hasn\u2019\
      t been in vogue recently, but I think using just statistical based methods may\
      \ be limiting. I\u2019m hoping more research is done in this and other areas\
      \ soon (to complement the statistical approaches)"
- name: David Cox
  text: "I appreciate you taking the time to respond to questions, Ankur Patel! I\
    \ second Matthew\u2019s questions about with respect to getting NLP products into\
    \ production.  Also, many database systems (e.g., AWS) are offering out-of-the-box\
    \ NLP solutions. I\u2019m wondering if you have any thoughts or recommendations\
    \ on cloud computing systems that do simple NLP solutions well and also allow\
    \ individuals with training in NLP to engage in more advanced analytics?"
  replies:
  - name: Ankur Patel
    text: I think the major cloud providers have done a great job lowering the barrier
      of entry to perform NLP
  - name: Ankur Patel
    text: I find Google best in this regard today, followed closely by Amazon. Today,
      you can perform some of the core NLP tasks with just basic Python knowledge
      without knowing ML or DL
  - name: Ankur Patel
    text: I think we will see this trend continue quite a bit. Easy to use NLP APIs
      tailored to the developer community at large instead of to just data scientists
- name: ASHISH SONI
  text: 'Hey Ankur Patel! Really curious about the content your book!

    What kind of business problems/examples have you covered in the book?'
  replies:
  - name: Ankur Patel
    text: We cover a lot of the more popular NLP tasks in enterprise today such as
      named entity recognition, text classification, sentiment analysis, and summarization
  - name: Ankur Patel
    text: "We don\u2019t focus on any one vertical because a lot of these tasks are\
      \ appropriate across verticals"
  - name: ASHISH SONI
    text: "Thank you Ankur! \U0001F64F"
  - name: Ajay Arasanipalai
    text: 'To add on: there''s been lots of evidence recently that backs up what Ankur
      Patel says here about the same techniques working across verticals.'
  - name: Ajay Arasanipalai
    text: The real beauty of neural nets and deep learning is that they actually do
      live up to the promise of generalize across many different datasets. For example
      - GitHub copilot and AI dungeon, two very successful and popular real world,
      actually deployed, commercial products who's domains are quite different (software
      engineering vs. entertainment), use nearly identical models.
- name: David Cox
  text: "Ankur Patel Based on the trends you\u2019ve watched over the past decade\
    \ and that led into your book, what do you think are the next areas for major\
    \ advancement in NLP? And, what are some lingering challenges that we don\u2019\
    t seem to be close to?"
  replies:
  - name: Ankur Patel
    text: "Let\u2019s start with the next major (applied) advancement in NLP. Combining\
      \ computer vision with NLP to process documents is and will become a very large\
      \ area of investment (from the applied / enterprise community)."
  - name: Ankur Patel
    text: For example, think of all the paper heavy industries today that require
      visual and textual cues to interpret properly (e.g., invoices, health statements,
      receipts, legal documents, financial documents, etc.). These areas are ripe
      for automation using not just NLP but also computer vision (jointly).
  - name: Ankur Patel
    text: The most hyped area is NLG (natural language generation), largely off of
      GPT-2 and GPT-3 from OpenAI. But, we are still quite a bit away from having
      human-like generation
  - name: Ankur Patel
    text: "That\u2019s one of the biggest challenges, but GPT-3 has caught the attention\
      \ of many people, both in academia and in industry, so I expect a lot more innovation\
      \ here in the coming decade"
  - name: David Cox
    text: Very interesting! Especially tin thinking about businesses that are paper
      heavy. Do you know, offhand, if anyone has looked at the carbon offsets between
      creating and using paper as compared to the resources needed to build the models
      specific to the different business cases and the resulting data storage/use?
  - name: David Cox
    text: I wonder a lot about the getting to language that is similar to human. In
      particular because of the known contextual factors that go into human language
      outside of simply looking at the structure of what was said prior to the generated
      statement. It seems this will require combining other datasets to get to that
      structural piece as well as advances in NLP generally.
- name: Wendy Mak
  text: Hi Ankur, what business problems do you think would benefit a lot from modern
    NLP methods but is commonly overlooked in research as too boring or from the businesses
    not being aware it is possible?
  replies:
  - name: Ankur Patel
    text: "A few problems come to mind, but one of the biggest areas is information\
      \ retrieval. Researchers find it \u201Cboring\u201D at least compared to NLU\
      \ and NLG tasks, but informational retrieval (think Google on domain-specific\
      \ private documents such as legal and finance and healthcare) is incredibly\
      \ valuable to businesses."
  - name: Ankur Patel
    text: "Businesses are using CTRL-F and manual organization and tagging of data\
      \ to find what they need but NLP could really unlock a lot of value here. It\u2019\
      s not a Google scale problem so it often gets overlooked by the tech giants.\
      \ Curious what you think about this (and others)."
  - name: Wendy Mak
    text: yeah, I agree-- I think it's really relevant but you don't see a lot of
      papers about document tagging etc in e.g. Neurips... In the last company I worked
      for there's a lot of legal documentation that could really benefit from automatic
      tagging (unfortunately that project got parked when the biz people decided it
      was low priority...)
  - name: Ankur Patel
    text: "Part of the challenge here is that the effort to build a model to do this\
      \ well isn\u2019t worth it for any given organization, so software companies\
      \ will need to provide this service to many clients to make the investment worthwhile.\
      \ I think we are starting to see more of this now"
- name: Jeff Herman
  text: Hi Ankur.  Thanks again for taking some time to give your great insights on
    our questions! With transformers how easy is it to really understand how the model
    is making the predictions that it is?  For example if we have a text classification
    using a transformer, can we see which words were of most importance for a prediction?
  replies:
  - name: Ankur Patel
    text: Initially, this was hard to do, but since 2018 there has been some good
      progress on introducing interpretability to the Transformer models
  - name: Ankur Patel
    text: "You can now see which word(s) the model paid most \u201Cattention\u201D\
      \ to as it was making a prediction"
  - name: Ankur Patel
    text: "It\u2019s still difficult to truly understand the black box at scale though\
      \ (across many predictions) but for one off predictions, this is possible today"
  - name: Ajay Arasanipalai
    text: 'To add on: I know it wasn''t originally your question, but let me also
      mention that I don''t think trying to kind "keywords" is necessarily a great
      idea for interpretability. As Ankur Patel mentioned, I don''t think this approach
      scales well in practice - when you have thousands of users querying your model
      with many gigabytes of text, what insight do you hope to get by finding the
      most "attentive" words?'
  - name: Ajay Arasanipalai
    text: In the case of text classification, it might be smarter to just use basic
      word/subword counting post-classification (i.e. what are the most common words
      among novels that have been classified as horror).
  - name: Jeff Herman
    text: Hi Ajay Arasanipalai.  Appreciate your insight!  Originally, I was thinking
      of how to audit the model.  For example, if we are looking at novels and we
      predict a novel as horror when it is actually historical I wanted to know the
      most important words for why the model predicted it to be horror.  I like your
      approach, I could compare most common words in that novel vs the most common
      words in the different novel genres
- name: Krzysztof Ograbek
  text: 'Hi Ankur Patel, thank you for doing this.

    How will NLP be different in 3 years from how it is today? Are there any tasks
    that will explode on popularity?'
  replies:
  - name: Ankur Patel
    text: I think we have seen NLP in good use in consumer applications today (for
      example, with social apps), but the next 3 years will focus on getting NLP into
      the workplace, automating tasks that white collar workers are doing today
  - name: Ankur Patel
    text: For example, analyzing and processing invoices, bank statements, legal memos,
      health care statements, financial documents, etc.
  - name: Ankur Patel
    text: The barrier to entry to use NLP will also come down, just like it did for
      computer vision since 2012
  - name: Ankur Patel
    text: Another trend that intersects well with NLP is the no-code movement in software
      development and machine learning. We should be able to load documents, highlight
      text, and have NLP models perform an array of valuable tasks such as document
      classification, sentiment analysis, summarization, etc. We are not quite there
      yet
  - name: Krzysztof Ograbek
    text: I love the answers. Thank you!
- name: Krzysztof Ograbek
  text: Is your book for everyone, regardless the level of NLP experience?
  replies:
  - name: Ankur Patel
    text: Yes, it is. In fact, it is positioned best for newcomers and intermediate
      users
  - name: Ankur Patel
    text: You will need to know Python and have some awareness of data science and
      ML though
  - name: Ajay Arasanipalai
    text: "To clarify: we don\u2019t really require any NLP experience, but it\u2019\
      s definitely. If you\u2019re a complete beginner, you can definitely pick up\
      \ the book and get started - we have a bunch of external resources (which I\
      \ think is actually one of the more valuable parts) to help. But it definitely\
      \ won\u2019t be enough on it\u2019s own if you don\u2019t have any experience\
      \ with Python, PyTorch, or basic deep learning."
  - name: Ajay Arasanipalai
    text: One thing we realized early on is that there are a lot of resources that
      help you get started, but less so that dive into the details of how to go from
      copy-pasting SciKit Learn snippets to implementing and deploying state of the
      models in production.
- name: Giuditta Parolini
  text: Why are chatbots so frustrating for the user, when NLP-based translation tools
    (I am thinking about DeepL for instance) can do a very good job?
  replies:
  - name: Ankur Patel
    text: "Part of this has to do with NLU. Chatbots today don\u2019t do a great job\
      \ of holding relevant context across questions. You can see this firsthand if\
      \ you try to ask Google Assistant or Siri or Alexa a series of related questions"
  - name: Ankur Patel
    text: Another part has to do with conversational language that many of us use
      in chatbots (for example, the use of casual language or idioms, both of which
      are very hard for NLP models today)
  - name: Ankur Patel
    text: "I think both of these items will have to get solved before chatbots appear\
      \ \u201Cintelligent\u201D"
  - name: Ajay Arasanipalai
    text: The other thing to consider that most chatbots deployed today probably aren't
      using the very best of modern deep learning techniques. While the GPT-3 demos
      certainly look convincing, keep in mind that they require 22 GPUs for inference...
  - name: Ajay Arasanipalai
    text: Especially for those not utilizing the latest tools (like Hugging face's
      transformers library), the engineering effort and compute resources required
      to run a medium-sized model like BERT for a simple chatbot that really only
      needs to cancel orders every once in a while may be prohibitively expensive.
  - name: Giuditta Parolini
    text: Thanks for your answers. At this point one can only say that, most of the
      time, chatbots are the fancy equivalent of switchboards with intolerably long
      recorded instructions. Both chatbots and switchboards do not give the user what
      (s)he needs,  but they gain time when companies do not have enough customer
      service staff. I will try not to be too upset next time a chatbot wastes my
      time.
- name: Ajay Arasanipalai
  text: "Hi everyone, I\u2019m Ajay, Ankur Patel\u2019s coauthor for \u201CApplied\
    \ Natural Language Processing in the Enterprise.\u201D Thanks for setting this\
    \ up, and I\u2019m happy to stick around and answer any questions you all may\
    \ have."
  replies: []
- name: Ajay Arasanipalai
  text: 'Quick comment: while no-one specifically asked this question, it seems like
    many of you here are asking about something along on the lines of what NLP applications
    are going to be hot in the next few years. Note that this isn''t _just_ about
    completely new products and services, but things that we''ve all been using for
    a while from established companies may also start getting better as they incorporate
    transformer models.'
  replies: []
- name: Ajay Arasanipalai
  text: You might have noticed that Gmail's autocomplete and predictive keyboards
    have been getting better over the years. I think this trend will continue, and
    we'll start to see even more autosuggestions and prompts popping up across different
    applications/domains. A great example of this is GitHub Copilot - [https://copilot.github.com/](https://copilot.github.com/)
  replies: []
- name: Alexey Grigorev
  text: Which NLP papers are your favourite? Why?
  replies:
  - name: Ankur Patel
    text: 'I personally love this paper: [https://arxiv.org/abs/2012.14740v1](https://arxiv.org/abs/2012.14740v1)'
  - name: Ankur Patel
    text: "I\u2019m working on document understanding problems, and this is an excellent\
      \ paper on the topic"
- name: Krzysztof Ograbek
  text: What are the characteristics of a great NLP Engineer? Can you tell someone
    has a potential despite lack of experience?
  replies:
  - name: Ankur Patel
    text: Most of the time it comes down to practical, hands-on experience for me
  - name: Ankur Patel
    text: "I love to see Github repos and projects, even if the work experience isn\u2019\
      t quite there"
  - name: Ankur Patel
    text: Any indication that the individual is learning new materials and experimenting
      with them is a huge positive
  - name: Ankur Patel
    text: Thirst for the space is big
- name: Mansi Parikh
  text: 'Hi, Ankur and Ajay. Thanks for interacting with the community! We appreciate
    your time and enthusiasm.

    At what point does it become crucial for an organization to adopt an NLP-focused
    analytics strategy? Is it only when you''ve exhausted all other analytical opportunities
    for non-text data that you need to dive into this and developing new capabilities
    to continue to add incremental value to your business? Is it based on the actions
    of competitors in the market? Basically, how do you know when to seriously introduce
    this to an organization?'
  replies:
  - name: Ankur Patel
    text: I would frame it a bit differently. If your organization uses text or documents
      today at reasonably high volume, then it is time to invest in NLP.
  - name: Ankur Patel
    text: If your organization does not have high text or audio needs, there is no
      need to dabble in NLP
  - name: Mansi Parikh
    text: Thank you!! I just wasn't sure if NLP was essentially a right step forward
      for even organizations that may not have this type of data yet but now are realizing
      that they have to collect it and if NLP techniques could eventually be valuable
      to them. I was considering it like that, but maybe the business should just
      focus where it's meant to focus.
  - name: Ankur Patel
    text: Yes exactly. Let the business need drive the technology instead of the other
      way around
- name: Mansi Parikh
  text: 'One more, please, for both of you.

    How can you estimate the value of an NLP undertaking to a business? Given its
    popularity, it might not take much to convince leadership that this is a promising
    route forward, but as there are usually many options for ways an organization
    can proceed in the future, you may still need to justify building expertise around
    this subject compared to alternatives and that can be done by estimating potential
    (or expected) business value, I suppose.'
  replies:
  - name: Ankur Patel
    text: I would start by framing the problem in terms of savings to the organization
      if you could introduce x% automation
  - name: Ankur Patel
    text: "By itself, applying new tech for the sake of using new tech isn\u2019t\
      \ going to be too convincing, no matter how hot the new tech is"
  - name: Ankur Patel
    text: If you could deliver some value fast, that will also help with buy in
  - name: Mansi Parikh
    text: Great! That sounds reasonable to do and provide. Sometimees fast POCs are
      difficult, but necessary to win over the decision-makers. Thanks again, Ankur.
- name: Ricky McMaster
  text: "Hi Ajay Arasanipalai/Ankur Patel, thanks for doing this!  Just following\
    \ from the point Ajay makes above about improvements in autocomplete/predictive\
    \ text, which is something I\u2019ve been thinking about anyway recently.\nAs\
    \ we as users become more reliant on such features, how do NLP models account\
    \ for their training data potentially becoming more and more machine-generated\
    \ (or at least machine-influenced), whilst humans might lose more of their standards\
    \ in grammar or general literacy?\nIs there a risk that it makes it more difficult\
    \ for models to keep up with developing linguistic trends whilst remaining grammatically\
    \ \u2018correct\u2019?"
  replies:
  - name: Ajay Arasanipalai
    text: Good question. I think this is still an unsolved problem, but there are
      a few things that we might be able to do short-term as a quick fix. The most
      obvious solution is flagging the data your model generates, and avoid training
      on that. High quality testing and validation sets also help a lot here. You
      could also measure user satisfaction with the prompts and use that as a metric.
  - name: Ajay Arasanipalai
    text: "As for humans loosing grammar standards, I suppose that\u2019s more of\
      \ a social problem. The same could be said of self-driving cars, but we work\
      \ on that anyway. I think worrying about polluting the training set with bad\
      \ grammar due to mass normalization of autocorrect is a fairly out-there long\
      \ term concern."
  - name: Ricky McMaster
    text: Thanks, appreciate the response.
- name: Laia
  text: 'Hi Ajay Arasanipalai and Ankur Patel very interesting topic!

    NLP products have become better and better, but what are the current NLP frontiers?'
  replies:
  - name: Ankur Patel
    text: The two frontiers that I see are NLU and NLG, both of which are sub-areas
      in NLP more broadly. Here is [a good post on it](https://www.ibm.com/blogs/watson/2020/11/nlp-vs-nlu-vs-nlg-the-differences-between-three-natural-language-processing-concepts/)
  - name: Ankur Patel
    text: NLP is much more mature today, and it is being used to process and structure
      all sorts of text and audio data (e.g., invoice processing).
  - name: Ankur Patel
    text: "NLU and NLG are more open areas of research that aren\u2019t ripe enough\
      \ for broad industry application just yet, partly because of the inference costs\
      \ as Ajay Arasanipalai mentioned yesterday and partly because the tech isn\u2019\
      t quite good enough yet to be applied to broad settings (above and beyond autocomplete,\
      \ for example)."
  - name: Ankur Patel
    text: "NLU can unlock a lot of value because, once it has matured, we will see\
      \ more context-aware conversational bots that handle queries much more like\
      \ humans would, instead of the fairly \u201Cdumb\u201D question and answer bots\
      \ today"
  - name: Ankur Patel
    text: NLG will help us generate more open-ended text and audio, perhaps even assist
      in the creative fields such as novel writing
  - name: Ankur Patel
    text: We have a ways to go before we get to that point though
  - name: Laia
    text: Thanks for your answer!
- name: WingCode
  text: 'Thank you Ankur Patel &amp; Ajay Arasanipalai for the great Q&amp;A.

    Do you think the future will be ruled by compute intensive models (example: Transformers,
    GPT-3) ?

    Will there be more efforts put into less compute intensive techniques (example:
    distillation) thereby making the state of the art accessible to all?'
  replies:
  - name: Ajay Arasanipalai
    text: "I\u2019m conflicted on this. Note that the other way you can get accessibility\
      \ is by making compute cheaper. We\u2019re started to see many accelerator and\
      \ deep learning hardware startups that promise huge gains in efficiency and\
      \ affordability. Even Nvdia, who has an undisputed monopoly on this market,\
      \ continues to make better GPUs year over year. It\u2019s entirely possible\
      \ that what we consider \u201Ccompute intensive\u201D today will be very easy\
      \ for the average practitioner to run 5-10 years from now."
  - name: Ajay Arasanipalai
    text: "The reason we\u2019re seeing an interest in larger language models is that\
      \ at the moment is because they are continuing to scale nicely and it\u2019\
      s a relatively \u201Csafe\u201D bet to improve your model\u2019s performance.\
      \ Would you rather hire a team researchers to work on distillation for a year\
      \ who may or may not be able to produce a ~20% improvement, or just change a\
      \ parameter in your initializer that doubles the number of layers?"
  - name: Ajay Arasanipalai
    text: "But even then, the only company I know of that regularly scales language\
      \ models is OpenAI. I think most others have settled on BERT and it\u2019s variants\
      \ for practical use. I think it will be similar to the story in vision today\
      \ - ResNet50 and YOLO are the standard, but there are better alternatives if\
      \ you\u2019re willing to invest the time, energy, and compute."
  - name: WingCode
    text: "Thank you for the answer Ajay \U0001F642 Interesting take.\nFollowup question.\
      \ Do you think the future of GPU hardware for DL will be dominated by NVIDIA\
      \ GPUs because of the wide adoption of their CUDA language? Do you think any\
      \ other player can pull an \"Apple\" (with their ARM transition) and we get\
      \ a new open source API interface?"
  - name: Ajay Arasanipalai
    text: "I think the lesson we\u2019ve learned from Nvidia is that programmability\
      \ &gt; raw performance. If developers don\u2019t like using your platform, it\
      \ won\u2019t work."
  - name: Ajay Arasanipalai
    text: "Whether or not these hardware startups end up providing a competitive products\
      \ remains to be seen (and is probably 10+ years away, so is hard to predict).\
      \ But I think the most promising thing to look for short-term is software/compiler\
      \ improvements to Google\u2019s TPUs. The really big issue there is that Google\
      \ doesn\u2019t want to sell their TPUs though."
  - name: Ajay Arasanipalai
    text: "As for an open source CUDA alternative, I don\u2019t think we\u2019ll see\
      \ anything promising within the next 1/2 years unfortunately. But that\u2019\
      s just my guess."
  - name: WingCode
    text: Thank you again for the answers Ajay
- name: Ankur Patel
  text: Thanks everyone! And big shoutout to Alexey Grigorev for inviting us and organizing
    this. If you want to follow me personally on trends in the AI/ML and NLP space,
    please feel free to [subscribe here](https://www.ankursnewsletter.com).
    Hope to see you all again soon
  replies: []

---

NLP has exploded in popularity over the last few years. But while Google, Facebook, OpenAI,
and others continue to release larger language models, many teams still struggle with building
NLP applications that live up to the hype. This hands-on guide helps you get up to speed on the
latest and most promising trends in NLP.

With a basic understanding of machine learning and some Python experience, you'll learn how to
build, train, and deploy models for real-world applications in your organization. Authors Ankur
Patel and Ajay Uppili Arasanipalai guide you through the process using code and examples that
highlight the best practices in modern NLP.