---
title: "Engineering MLOps"
description: "Book of the Week. Engineering MLOps by Emmanuel Raj"
cover: "images/books/20210705-engineering-mlops/cover.jpg"
image: "images/books/20210705-engineering-mlops/preview.jpg"
start: 2021-07-05 00:00:00
end: 2021-07-09 22:59:58
authors: [emmanuelraj]
links: 
  - text: Book's page
    link: https://www.packtpub.com/product/engineering-mlops/9781800562882
  - text: Amazon
    link: https://www.amazon.com/dp/1800562888
  - text: Book's GitHub repository
    link: https://github.com/PacktPublishing/EngineeringMLOps

archive:
- name: Tino
  text: "Hello Emmanuel Raj \U0001F642 Thanks for taking the time! As it feels like\
    \ MLOps is currently on the rise when do you think it is really needed for a company\
    \ to focus on MLOps? I often feel it is important to get something out there to\
    \ see the impact but the operational part is often only the 3. or 4. steps whereas\
    \ model drift, ect. can cause a negative business impact right away. Would you\
    \ recommend to set up a good MLOpy framework before going live?"
  replies:
  - name: Emmanuel Raj
    text: Hello Tino,good question! For any tech company focusing on making intelligent
      products (or data powered) setting up MLOps is recommended (to save time, money
      and energy). It saves a lot of time for data scientists and SE team from mundane
      tasks (deployments, manual tests, repetitive data engineering tasks, manual
      debugging etc) and enables them to focus on what truly matters (making best
      models and learning in realtime from data) by taking benefits of automation
      via CI-CD pipeline to avoid mundane jobs. Yes, before implementing in live/production
      it is recommended to test the pipeline and monitoring features (model, data,
      feature drifts etc) in DEV and QA environments to validate if the MLOps pipeline
      provides business value or not (measure with business KPI's), only then go live/to
      production.
  - name: Tino
    text: "Okay cool \U0001F642 Got it \U0001F642 Thanks!!"
- name: Emmanuel Raj
  text: "Hello everyone! I am glad to answer you questions \U0001F642 looking forward\
    \ to hearing your thoughts!"
  replies: []
- name: Agrita Ga
  text: Do you believe there should be a difference between implementing MLOps in
    a smaller organization (let's say startup focusing on ML solutions) and bigger
    organization?
  replies:
  - name: Emmanuel Raj
    text: "Yes, there will be some differences b/w MLOps pipelines for smaller vs\
      \ big organisations based on their business needs, teams and data processing\
      \ abilities. Check out chapter 2: *Characterizing Your Machine Learning Problem*\
      \  in the book. It explains on this on detail \U0001F642 (screenshot from chapter\
      \ 2, figure 2.9)"
  - name: Agrita Ga
    text: I'll expand this question a bit, - does best practices (or some tips&amp;tricks,
      or even tech stack?) differ for small vs big teams?
  - name: Emmanuel Raj
    text: "Yes, they differ case by case (company by company) especially the tools.\
      \ But some of the the principles remain same on high level (MLOps pipeline to\
      \ build, deploy and monitor ML models). For small companies, most likely they\
      \ need to build the MLOps platform with limited, budget both in money and time\
      \ and their operations might be small on scale. Big companies have high volume\
      \ of data, operations and teams so the setup of MLOps pipelines/platform will\
      \ differ in most cases \U0001F642"
  - name: Agrita Ga
    text: "Thanks for your input! Appreciate a lot! \U0001F64C"
- name: Diego
  text: Hi Emmanuel Raj, thanks for this opportunity of q&amp;a. to  Do you think
    that MLOps is definitely a skill that every data scientist needs to have if he/she
    wants to keep relevant in the job market or, on the other hand, data scientists
    should just focus on data/statistics/algorithms because otherwise they are 'biting
    off more than they can chew'?
  replies:
  - name: Emmanuel Raj
    text: "Good question Diego! Knowing how to setup MLOps pipeline/platform (infra\
      \ and architecture) is a bit too much for data scientists. However it is recommended\
      \ for data scientist to know how to work with features of MLOPs pipelines/platform\
      \ (once they are setup) such as registering datasets, models and packaging them\
      \ on the MLOps platform. This way DS's can take the benefits of MLOps and focus\
      \ on what they are good at 'data/Stats/algorithms'. I hope this answers your\
      \ question  \U0001F642"
- name: Chetna
  text: "Hi Emmanuel Raj, what\u2019s your take on the importance of cloud technologies\
    \ certifications? do they make a resume more relevant for MLOps role?"
  replies:
  - name: Emmanuel Raj
    text: "Hello Chetna Cloud certifications are worth it, they give a 360 degree\
      \ view on what cloud has to offer so you may pick and choose best services to\
      \ solve your business problems (optimisation). They surely make the resume standout\
      \ for MLOps role, companies are looking for ML engineers who know data engineering\
      \ and infrastructure setup well (certified is better) \U0001F642"
  - name: Chetna
    text: "thanks \U0001F642"
- name: Lalit Pagaria
  text: 'What is importance of choosing right Cloud Provider in implementation of
    MLOps?

    What things to take care of while implementing MLOps?

    In your experience, which providers do you suggest for small and medium startups?'
  replies:
  - name: Emmanuel Raj
    text: "Lalit Pagaria Choosing right tools for the business problem is most important\
      \ (not the other way around). Any cloud which has capabilites to serve your\
      \ needs will do (these days most of them are good enough). Down side of cloud\
      \ though is vendor lock, to avoid that we can use cloud agnostic/open source\
      \ MLOps tools e.g. MLFlow and Valohai which can work with most of the clouds.\
      \ So choosing right cloud/tools depends on the business problem at hand \U0001F642"
- name: Matthew Emerick
  text: 'Hey, Emmanuel Raj!  Thanks for doing this!

    In an open world where both the data and the environment itself are constantly
    changing, how does MLOps keep up?'
  replies:
  - name: Emmanuel Raj
    text: "Good question Matthew Emerick! MLOps addresses that constantly changing\
      \ environment by adapting to the changing data/environment, optimising performance\
      \ for changes, auto scaling and being relevant for the changing environment\
      \ \U0001F642"
- name: Neal Lathia
  text: "\u2754 How uniform do you think MLOps workflows is across companies?"
  replies:
  - name: Emmanuel Raj
    text: "Hard to generalize at this point as different companies are at different\
      \ stages in their ML adoption \U0001F642"
- name: Mansi Parikh
  text: 'Thank you, Emmanuel, for sharing your thoughts!

    Should MLOps be a concern during early stages of an organization or only when
    it becomes necessary? (More specifically, at what stage of growth of a data department
    does this become top of mind?)'
  replies:
  - name: Emmanuel Raj
    text: "Nice question Mansi Parikh! If the company/organisation is sure of having\
      \ ML models in their workflow then the sooner the better it is to think of implementing\
      \ MLOps. Otherwise, When data pipelines are set up and the organisation has\
      \ the needed data setup in place. The sooner the better it is \U0001F642"
  - name: Mansi Parikh
    text: "thank you so much, Emmanuel! this is great. I appreciate the thoughtful\
      \ response. \U0001F642"
- name: Rushanthi
  text: "Hi Emmanuel Raj thanks a lot for the golden opportunity on QnA. \nWhat\u2019\
    s your point of view on MLOps when it comes to job market? To be more elaborative,\
    \ there are number of roles when it comes to data science which involves a data\
    \ Analyst, data scientist and as well as a machine learning engineer, when taking\
    \ these roles into consideration which job role requires experience on MLOps?\
    \ \nBut then again there arises another question where we are headed towards an\
    \ automated ML what would be the outcome of MLOps with relevance to the job roles\
    \ in the market?"
  replies:
  - name: Emmanuel Raj
    text: Rushanthi It's good for an ML Engineer to have experience in MLOPs (especially
      data engineering and platform setup). Data Scientist is the user of MLOPs platform,
      so it helps if they have some exp using MLOPs platforms to build and deploy
      models. Data analysts can do without it. Good question on where are we headed
      with automation - Time will say but probably MLOPs will impact every Data science/Engineering
      job roles (let's hope positively) e.g. more efficiency, less time and resources.
  - name: Rushanthi
    text: "Thanks a lot for the enlightenment Emmanuel. Appreciate it a lot for clearing\
      \ up my puzzle \U0001F64C"
- name: Oleg Polivin
  text: 'Hi Emmanuel Raj, thanks a lot for this opportunity! I would like to ask you
    two questions that are a bit related.

    1. In your opinion, what is the main added value that an MLOps person brings to
    a company?

    2. Is it easy to replace an MLOps engineer?

    A brief thought that was the reason to ask the questions is in the thread.'
  replies:
  - name: Oleg Polivin
    text: "When I was working on projects that needed something I would call MLOps:\
      \ creating a docker application, deploying on a google k8s cluster, making a\
      \ pipeline using gitlab ci, I realized that I do not understand how it is working\
      \ under the hood, but just looking for \u201Crecipes\u201D, keywords and using\
      \ tutorials or to a lesser extent documentation (written in a form of a \u201C\
      recipe\u201D as well). Like: put this into `gitlab-ci.yaml` file, click on this,\
      \ that and that in google cloud. Sure, it took a long time to make all the parts\
      \ work together.\nHowever, it makes me think that:\n- there is no special knowledge\
      \ involved into MLOps vs. ,say, data science where one is expected to know math\
      \ or statistics.\n- Therefore, it makes be a bit \u201Cafraid\u201D that MLOps\
      \ engineer will be either replaced by some automatic deployment solutions or\
      \ \n- simpler, young people who tend to grasp many new tools that appear.\n\
      Thank you!"
  - name: Doink
    text: '+1'
  - name: Emmanuel Raj
    text: "Good question Oleg Polivin! MLOps person brings added value to a Data science\
      \ team mainly in terms of infra setup/maintenance, monitoring ML Models/systems\
      \ and maintaining pipelines. Sure it can be done/learned by others and MLOps\
      \ engineers can may as well be replace (e.g. with SRE engineers, DEVOps engineers\
      \ etc). For now it looks like data scientists are more on the verge of replacement\
      \ (with AutoML) \U0001F603 it's not as easy to replace MLOps engineer though\
      \ but maybe with time and more automation tools we might get there where MLOps\
      \ engineers can be easily replaced."
- name: Lamjed Debbich
  text: Hi Emmanuel Raj, thank you for this nice book, it covers one of the subjects
    that interests me a lot. As you know, there are many methods of MLOPS on the market,
    the new user can get confused for which method should we use? Do you have any
    tips for getting started?
  replies:
  - name: Doink
    text: '+1'
  - name: Emmanuel Raj
    text: "Hi Lamjed Debbich Thank you! To begin with I suggest to get a good theoretical\
      \ understanding of MLOps workflow, learn how to build ML microservices using\
      \ docker and deploy them on various deployment targets (Engineering MLOps book\
      \ will give a great headstart on this). After that decide on MLOPs tools (cloud\
      \ or opensource, e.g. Azure, MLFLow etc) you would like implement and then find\
      \ resources that teach you implementation. Learning by doing is the best way\
      \ to learn MLOps \U0001F642"
- name: Alexey Grigorev
  text: What do you think about the role "MLOps engineer"? Does it make sense? Should
    it exist?
  replies:
  - name: Alexey Grigorev
    text: I see that it's often synonymous to ML engineer, which I don't agree with.
      What's your opinion about it?
  - name: Chi
    text: "From my understanding, there are (at least) 2 types of MLE defined by most\
      \ of the companies. Some MLEs focus on the ML models algorithms, other MLEs\
      \ focus on designing \u201Cdata intensive application\u201D or wee can call\
      \ it MLOps? Again, ML in production is not just the ML algorithms \u2014 Andrew\
      \ Ng."
  - name: Emmanuel Raj
    text: "Depends. If a person is needed for team to setup and monitor infra and\
      \ operations it's a good idea, otherwise Devops (or SRE) engineers with some\
      \ knowledge of ML can enable MLOps \U0001F642"
- name: Alexey Grigorev
  text: Also, what's your opinion about the new course from Andrew Ng? I'm taking
    about MLEPs
  replies:
  - name: Emmanuel Raj
    text: "Haven't looked at the content, can't say much but for the look of it, looks\
      \ like it's more focused on ML Engineering/DS problems (e.g optimisation, robustness,\
      \ efficient modelling etc) and not much on MLOps \U0001F642"
- name: Doink
  text: I see different MLOps course one from Made with ML, another on Udemy which
    is quite popular then we have Andrew Ng and then there is full stack deep learning
    course covering stuff. Which course or path do you recommend for a noob?
  replies:
  - name: Emmanuel Raj
    text: "Made with ML looks good (recommended), not sure of Udemy course or Andrew\
      \ NG's courses (haven't looked at the content) \U0001F642"
- name: Tino
  text: Hey Emmanuel Raj Would you rather suggest to build an MLOps system on your
    own or buy it from an external provider? I saw that Fiddler has an amazing solution
  replies:
  - name: Emmanuel Raj
    text: "Hey Tino, it's hard to generalize for all cases but depends on the use\
      \ case we work on.  For some cases data is too sensitive and can't be worked\
      \ using external tools. For those cases it is better to build on your own but\
      \ otherwise plug and play solutions like fiddler, mlflow, valohai etc are awesome,\
      \ using them will save a lot of time and energy \U0001F642"
---

MLOps is a systematic approach to building, deploying, and monitoring machine learning (ML) solutions. It is an engineering discipline that can be applied to various industries and use cases. This book presents comprehensive insights into MLOps coupled with real-world examples to help you to write programs, train robust and scalable ML models, and build ML pipelines to train and deploy models securely in production.

The book begins by familiarizing you with the MLOps workflow so you can start writing programs to train ML models. Then you’ll then move on to explore options for serializing and packaging ML models post-training to deploy them to facilitate machine learning inference, model interoperability, and end-to-end model traceability. You’ll understand how to build ML pipelines, continuous integration and continuous delivery (CI/CD) pipelines, and monitoring pipelines to systematically build, deploy, monitor, and govern ML solutions for businesses and industries. Finally, you’ll apply the knowledge you’ve gained to build real-world projects.

By the end of this ML book, you'll have a 360-degree view of MLOps and be ready to implement MLOps in your organization.