---
title: "Practical MLOps"
description: "Book of the Week. Practical MLOps by Noah Gift and Alfredo Deza"
cover: "images/books/20210830-practical-mlops/cover.jpg"
image: "images/books/20210830-practical-mlops/preview.jpg"
start: 2021-08-30 00:00:00
end: 2021-09-03 22:59:58
authors: [noahgift, Alfredo Deza]
links: 
  - text: Book's page
    link: https://www.oreilly.com/library/view/practical-mlops/9781098103002/
  - text: Amazon page
    link: https://www.amazon.com/Practical-MLOps-Operationalizing-Machine-Learning/dp/1098103017
  - text: Book's GitHub repository
    link: https://github.com/paiml/practical-mlops-book

archive:
- name: Alex S
  text: I wasn't sure how it's possible to read this book as it isn't published until
    October this year. Could you let us know, Alexey Grigorev?
  replies:
  - name: Alexey Grigorev
    text: "Probably you should ask Noah Gift about it \U0001F603 But you can read\
      \ it through OReilly Learning, the early release version is already available\
      \ there"
  - name: Alex S
    text: Ah ok I didn't realise that you could read the book before it was published!
  - name: Mahmoud Jalajel
    text: 'Same in Germany.

      And I _think_ my trial with O''Reilly learning expired. So I''ll have to wait
      for the book release!'
  - name: Maja
    text: Me too. I can't wait till October to by this book fromNoah Gift. His previous
      two books (Python for DevOps and Pragmatic AI) are great and have been a huge
      help for me. Also, his co author Alfredo Deza has such an inspiring life story.
  - name: Noah Gift
    text: "Yes, you can read online in rough draft form on the O\u2019Reilly website:\
      \  [https://learning.oreilly.com/library/view/practical-mlops/9781098103002/](https://learning.oreilly.com/library/view/practical-mlops/9781098103002/)"
  - name: Noah Gift
    text: It also should be in kindle form in around 30 days or so and in print soon
      after.
- name: Praveen
  text: 'Noah Gift

    Are there any generic rules behind selecting MLOps tools for a given ML task ?'
  replies:
  - name: Noah Gift
    text: A good place to start is by using the tools on the platform you are already
      on.  All major cloud platforms have an MLOps solution and this is a great place
      to start.  AWS Sagemaker, GCP Vertex AI, and Azure ML Studio
- name: Kshitiz
  text: 'Noah Gift and Alfredo Deza - First of all thanks for doing this. I want to
    discuss couple of things here -

    1. Should MLOps be applied to all data science/ML projects or should people be
    looking at some sort of maturity in the project? To put it simply - Should there
    be any minimum requirements in terms of size of data, number of users if it''s
    used in an application, how long in a problem do people have to wait to get the
    results validated etc. ?

    2. In what sort of problems/use cases are feature stores useful? How is feature
    store different than a database?'
  replies:
  - name: Noah Gift
    text: '1. I do think the process of MLOps should be applied to all projects because
      it is an extension of DevOps.  All software projects should have CI/CD and you
      can even do this with notebooks:  [https://github.com/noahgift/myrepo](https://github.com/noahgift/myrepo)

      2.  For feature stores they have raw materials in a form easily consumed by
      a ML pipeline.  I.E. Containers package the runtime with the code, Feature stores
      package the raw ingredients for ML into a metadata system.  A database is too
      low level by itself to be a feature store.'
- name: Eunice
  text: Noah Gift What are the common skills between an MLOps and a Data Engineer
    ?  And what skills are specific to MLOps ?
  replies:
  - name: Noah Gift
    text: There is a strong overlap between Data Engineer and MLOps with perhaps as
      little as a 5% overlap.  The key 5% is that a MLOps practitioner also knows
      a bit about ML and can train models, diagnose their output and knows about ML
      Platforms like AWS Sagemaker, MLflow, etc.
- name: Denis Volk
  text: Larger companies are using in-house MLOps platforms, while for smaller teams,
    it is hard to dedicate lots of development time to set up similar machinery. On
    the other hand, some level of MLOps is just necessary to keep an ML project useful
    to business users. How to determine the right amount of MLOps for a project?
  replies:
  - name: Noah Gift
    text: "I would start with whatever platform is available and use their offerings:\
      \  i.e. Google, AWS, Azure.  Let\u2019s take AWS for example, if you have gigantic\
      \ data and gigantic teams, say over 250 people in your company then a \u201C\
      big\u201D platform like Sagemaker probably makes sense because of how much it\
      \ offers.\nIf you use AWS but have a 3 person team, Sagemaker may or may not\
      \ be the best easy win.  Perhaps AWS App Runner with open source MLOps tools\
      \ might be a better fit."
  - name: Alexey Grigorev
    text: Which open source tools can you recommend?
- name: Jon Exume
  text: Can you talk about the specific careers that MLOps plays a big role in?
  replies:
  - name: Noah Gift
    text: Autonomous driving is a good example.  I went to Tesla AI Day last week
      and 90% of the people I spoke with did MLOps, i.e. tools/infra around computer
      vision.
  - name: Jon Exume
    text: Thanks
- name: David Cox
  text: I appreciate your taking the time to answer questions, Noah Gift! From your
    experience, what is the background of the primary people you see getting into
    MLOps?
  replies:
  - name: Noah Gift
    text: "People with a strong DevOps/Infrastructure skill set can easily make the\
      \ transition to MLOps.  They just need to pick up a bit of ML training.  One\
      \ way to do this is to read the book I wrote and also to get AWS ML Certification\
      \ certified (or similar).  Note, I helped create the AWS ML certificaiton\u2026\
      ."
  - name: David Cox
    text: Thanks, Noah!
- name: David Cox
  text: A follow-up question to the one above. Sometimes "new" jobs in technology
    are just the same skills from past positions but combined in a new way or centering
    around a new tool. What do you think distinguishes MLOps from past, similar areas?
    And, what similarities does it share with other areas/processes?
  replies:
  - name: Noah Gift
    text: I think MLOps is essentially an evolved DevOps but with the addition of
      ML.
- name: Duverger PETGA
  text: 'Hi Noah Gift  I really appreciate your work but I have one question : between
    "Cloud Computing for Data Analysis" and your actual book "Practical MLOps" or
    "Python for Devops", in what order we have to read your books ? For a beginner
    in MLOps ?'
  replies:
  - name: Noah Gift
    text: You can read in any order.  Since both Python for DevOps and Cloud Computing
      are start with either then move on to Practical MLOps.  They all have a similar
      theme with more depth on cloud, devops or mlops depending on the book
- name: Doink
  text: How to decide which tools to choose? Should one choose for an open source
    alternative or choose a tool by a cloud service provider?
  replies:
  - name: Noah Gift
    text: "How to decide which tools to choose?\nwhatever is simple to get started\
      \ with an improves automation and quality.\n\nShould one choose for an open\
      \ source alternative or choose a tool by a cloud service provider?\nI personally\
      \ prefer to pay a vendor, so I would start with a cloud offering.\n\n[10:03\
      \ AM] There are a plethora of tools coming out, how do you make a framework\
      \ on choosing which tool to choose and how to choose?\nIf you are on a cloud\
      \ platform start with what they offer and go from there.\n\n[10:04 AM] How to\
      \ practically navigate through the MLOps cycle? Some nuggets of wisdom like\
      \ MLOps isn\u2019t a tech problem but a people problem etc\nMake sure you have\
      \ CI/CD working and iterate from there.\n\n[10:04 AM] Do small startups really\
      \ need MLOps or is it over engineering?\nMLOps is a behavior/methodology that\
      \ focuses on Kaizen (continuous improvement).  So it applies to anything small\
      \ or big.\nA.  Automate everything\nB.  Make it better quality daily"
- name: Doink
  text: There are a plethora of tools coming out, how do you make a framework on choosing
    which tool to choose and how to choose?
  replies: []
- name: Doink
  text: How to practically navigate through the MLOps cycle? Some nuggets of wisdom
    like MLOps isn't a tech problem but a people problem etc
  replies: []
- name: Doink
  text: Do small startups really need MLOps or is it over engineering?
  replies: []
- name: WingCode
  text: "Hi Noah Gift,\nWhy did you choose the cheetah as the book cover? How is it\
    \ related to MLOps? Does it portray the advantages given by MLOps ? \U0001F642"
  replies:
  - name: xnot
    text: "Looks like a \U0001F415, probably dalmation"
  - name: Noah Gift
    text: "We don\u2019t have control of the animals."
- name: Alper Demirel
  text: 'Hi Noah Gift, thanks for being with us.

    What should be the starting point for our current project for MLOps? And what
    are the biggest disadvantages that MLOps bring?'
  replies:
  - name: Noah Gift
    text: "To start with I would make sure you have CI/CD, i.e. the foundation of\
      \ modern software engineering.  This is the first step.\n\nI don\u2019t believe\
      \ there are any disadvantages to MLOps.  In a nutshell it just means \u201C\
      Kazien\u201D, i.e. continuous improvement.  Make everything better and more\
      \ automated."
- name: Lalit Pagaria
  text: 'Thanks Noah Gift for this session. I have following queries

    What are good observability tools are there in MLOps space? (Specially open source
    tools)

    What is most important MLOps checklist for business critical model serve pipeline?

    Do you believe current set of lowcode/nocode MLOps solutions are good enough to
    be used for mission critical usecase?'
  replies:
  - name: Noah Gift
    text: 'I would start with traditional monitoring/instrumentation for you platform
      using whatever tools are already in place.  Then add additional business logic
      for ML.

      Additionally if you use Cloud Platforms they have default monitoring like for
      example Azure ML Studio which does model versioning and experiment versioning.'
  - name: Noah Gift
    text: "\u201CWhat is most important MLOps checklist for business critical model\
      \ serve pipeline?\u201D\nStart with CI/CD, if you don\u2019t have this you cannot\
      \ do MLOps"
  - name: Noah Gift
    text: "\u201CDo you believe current set of lowcode/nocode MLOps solutions are\
      \ good enough to be used for mission critical usecase?\u201D\n\nYes, in many\
      \ cases you don\u2019t need to write code.  A good example is Azure ML Studio\
      \ AutoML."
- name: Eunice
  text: Hi Noah Gift, Alfredo Deza thanks for the quick answers. When a team starts
    using the Agile framework, they may need a Scrum Master to facilitate and help
    to implement Agile. Do you think an MLOps specialist may be necessary for big
    organizations used to other frameworks to start using MLOps? Or hire an ML Engineer
    and have a Lead Data and Project Manager aware of the subject may be sufficient?
  replies:
  - name: Noah Gift
    text: 'I think it may help to have someone who has some form of MLOps certification.  One
      good example of this is course I just created on Coursera:  [https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)'
- name: Noah Gift
  text: 'Btw, you can also help promote a lot of my content and contribute to charity
    with this humble bundle, including PSF and women who code:  [https://www.linkedin.com/posts/noahgift_humble-software-bundle-python-2021-activity-6838263509390807040-zJ98](https://www.linkedin.com/posts/noahgift_humble-software-bundle-python-2021-activity-6838263509390807040-zJ98)&gt;.
    Help spread the word.'
  replies: []
- name: Kamran Ali
  text: Noah Gift Is this book covers any specific Cloud Platform (e.g. AWS ) or any
    specific tool (e.g. MLFlow) etc
  replies:
  - name: Noah Gift
    text: We cover AWS/Azure/GCP very heavily
  - name: Kamran Ali
    text: "Thanks for the response ! \U0001F642"
- name: Alexey Grigorev
  text: By the way, we have another celebrity appearance - Alfredo Deza himself! Welcome
    Alfredo!
  replies: []
- name: Maja
  text: Hello Alfredo Deza ! Thank you so much for joining us. I am so happy to have
    this opportunity to e-meet you and to ask questions. From your inspiring life
    story we can learn that anything is possible and that geat tihngs do happen. You
    just have to love what you are doing and to do it in the best way you can. From
    your book "_Python for DevOps_" we have learned how to do DevOps in Python. But,
    I have to ask you considering that ML pipeline is more complex, what are things
    we shouldn't ever do - bad practices that happen due to the lack of knowledge,
    or experience?
  replies:
  - name: Alfredo Deza
    text: 'Hi Maja! Thanks for the super kind words. This is a great question! I think
      that there are a few things from seeing the opposites of the core pillars of
      operations (DevOps/MLOps in general) like automation, monitoring, testing, and
      CI/CD. For example: no (or little) automation, doing things manually, no pipelines,
      no monitoring.

      Aside from those, you have other red-flags like over-engineering. Fast, iterative
      processes are far better than waiting 3 months to design the perfect thing'
  - name: Alfredo Deza
    text: "There is always room for improvement. I keep hearing people say \u201C\
      what if everything is already automated?\u201D - well\u2026 there is always\
      \ stuff to automate and improve. You are asking a critical question here, and\
      \ not asking critical questions (see critical thinking section at the beginning\
      \ of the book) is a tremendous problem."
  - name: Maja
    text: I will read it as soon as I get the book. Thank you Alfredo Deza so much
      for your guidance!
- name: Livsha Klingman
  text: 'Alfredo Deza Noah Gift I''m a REAL beginner, but majorly interested and so
    far got a good repertoire of success in a few beginning projects (maybe beginners''
    luck)!

    Your books are all touching on my work topics and what I am facing daily and now
    you have exposed them for me to read up on!

    As I develop, slowly, my knowledge and experience, I am discovering how much breaking
    into the ''big'' world is an upward struggle between big enterprises and the well-experienced.
    (As in any professional field!).

    What is the correct priority considering  the limited manpower for startups and
    small businesses - veer towards automation or not? Develop pipelines or CI/CD?
    or using a service tool and focusing on the ML?

    Do you have any advice for ''us'' small businesses to ''make a dent'' in the big
    world and gain the skills and experience to be aware of and make the educated
    decision of tools, methodology and topology, correctly balancing labor, to successfully
    develop MLOps?'
  replies:
  - name: Alfredo Deza
    text: 'Automation is not a one time thing that takes months to achieve and is
      super expensive. Noah Gift taught me the right path years ago: pick *any one
      thing* you do manually and automate it by the end of the week. Rinse and repeat,
      and suddenly a few months later you have several things automated. It is now
      CHEAPER to run operations because of it and the team can concentrate in even
      better automation'
  - name: Alfredo Deza
    text: '*Always* automate'
  - name: Alfredo Deza
    text: "Leveraging the cloud for automation (CI/CD or pipelines doesn\u2019t matter)\
      \ is good. Leveraging anything that is already solved that is not a core competency\
      \ of your business is crucial"
- name: Livsha Klingman
  text: Alfredo Deza Thanks for your response! Taking this opportunity further...
    How do you suggest trying to circumvent issues in MLOps, with compounding model
    decays through either data discrepancy between CI and CD or training and pipeline
    data, or models based on a initial wrong hypothesis - collecting biased data,
    which then exacerbates over time growing in bias?
  replies:
  - name: Alfredo Deza
    text: "This is a difficult question to get a straight answer. I don\u2019t think\
      \ there is a one-size-fits-all problem solver here. If you have biased data,\
      \ but you have automation, tests, pipelines, etc\u2026 you still have a biased\
      \ model in the end. MLOps can\u2019t solve biased data. There is always the\
      \ human element in all of this, and critical thinking (see critical thinking\
      \ section at the beginning of the book) is essential"
  - name: Livsha Klingman
    text: Alfredo Deza Thank you for your advice.. Can't wait to read your book and
      thanks for all your valuable time!
- name: Shankar Somayajula
  text: 'Alfredo Deza Thanks for taking questions. I like the focus on Automation
    in your book and answers to questions here.

    Can the process of Automation involve an abstraction of the data structures as
    a data model (schema/objects) so that the artifacts of automation are reusable
    from one project to another.. facilitating more reuse, making the process of automation
    more of a Product/Platform service instead of a Project/Task output? How does
    one facilitate reuse (otherwise) - publishing an API?'
  replies:
  - name: Alfredo Deza
    text: Reusability is the gold standard. Not entirely sure how to abstract data
      structures, but sharing/reusing artifacts sounds great to me. As to _how_ to
      do this, well it depends! Perhaps an S3 bucket would suffice if everything is
      behind AWS. If you need external access, it sounds like an HTTP API is the way
      to go
- name: Tony Gunawan
  text: Hi, Noah Gift and Alfredo Deza. Thank you for being here to answer the questions.
    I am newbie in the MLOps field as I am a data engineer right now on financial
    institutional field with previous experience as ETL developer and hope my questions
    is not out of context. Is it possible to fully automate all the process of ML
    end to end, especially in model evaluation? So many data with unpredictable behavior
    (like in the financial case) that make a model that has been deployed obsolete
    like during the start of the pandemic, behavior of the people who need to borrow
    the money from banks or other institutional lenders have gradually changed and
    need to do some remodeling with new set of data behavior if I would say. In this
    case, what kind of things that MLOps need to consider when facing this kind of
    unpredictable phenomena that will happen in the future? Thank you.
  replies:
  - name: Alfredo Deza
    text: "There is no silver bullet here where everything can be fully automated.\
      \ You\u2019ve mentioned one of the caveats which is unpredictable behavior.\
      \ Human interaction+evaluation has to be possible. Pipelines have to be flexible.\
      \ Any automation/workflow has to easily allow for changes and updates. When\
      \ automating, you _must_ think about the pitfalls and how to address them. For\
      \ example, you have a pipeline that normalizes data in small amounts, what can\
      \ you do _today_ that will allow batching the normalizing if the data is gigantic?"
  - name: Alfredo Deza
    text: alfredinsky
- name: Tim Becker
  text: Hi Noah Gift and Alfredo Deza, thank you for answering all our questions!
    What would you say are the most useful MLOps skills for a data scientist? For
    example, if I as a data scientist want to increase the collaboration with a MLOps
    specialist or if I am working for a small company that does not have a dedicated
    MLOps person and I as a data scientist have to cover the topic as well as possible.
  replies:
  - name: Alfredo Deza
    text: if you are starting out then I would pick automation. Anything you can do
      to start automation is going to be super useful and empowering
- name: Tim Becker
  text: Do you have a good idea for a toy project that I could work on to learn more
    about MLOps? Do you use an example project in your book?
  replies:
  - name: Alfredo Deza
    text: 'The book uses a public Github repository that you can use to see examples
      [GitHub - paiml/practical-mlops-book: [Book-2021] Practical MLOps O''Reilly
      Book](https://github.com/paiml/practical-mlops-book)'
  - name: Noah Gift
    text: cookbook in particular is a good recipe
  - name: Tim Becker
    text: "thank you guys \U0001F642"
- name: Luke Garcia
  text: Hi Noah Gift Alfredo Deza, I'm new to DS and MLOps. Does the book mention
    Kedro? What role (if any) does Kedro have in MLOps?
  replies:
  - name: Alfredo Deza
    text: "We don\u2019t have anything related to Kedro (sorry, not sure what that\
      \ is)"
  - name: Luke Garcia
    text: thank you
- name: Noah Gift
  text: 'If you want a deep dive on the book and how to MLOPs from Zero, watch this
    2.5 hour video:  [https://www.youtube.com/watch?v=OMv3lkB5W20](https://www.youtube.com/watch?v=OMv3lkB5W20)'
  replies: []

---

Getting your models into production is the fundamental challenge of machine learning.
MLOps offers a set of proven principles aimed at solving this problem in a reliable and automated way.
This insightful guide takes you through what MLOps is (and how it differs from DevOps) and shows you
how to put it into practice to operationalize your machine learning models.

Current and aspiring machine learning engineers--or anyone familiar with data science and Python -- will
build a foundation in MLOps tools and methods (along with AutoML and monitoring and logging), then learn
how to implement them in AWS, Microsoft Azure, and Google Cloud. The faster you deliver a machine learning
system that works, the faster you can focus on the business problems you're trying to crack.
This book gives you a head start.