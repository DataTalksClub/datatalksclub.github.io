---
authors:
- nielsenaileen
cover: images/books/20220523-practical-fairness/cover.jpg
description: Book of the Week. Practical Fairness by Nielsen Aileen
end: 2022-05-27 23:59:59
image: images/books/20220523-practical-fairness/preview.jpg
links:
- link: https://www.oreilly.com/library/view/practical-fairness/9781492075721/
  text: Book's page
- link: https://www.amazon.com/Practical-Fairness-Achieving-Secure-Models/dp/1492075736
  text: Buy on Amazon
- link: https://github.com/PracticalFairness/BookRepo
  text: GitHub repository
start: 2022-05-23 00:00:00
title: Practical Fairness

archive:
- name: Matthew Emerick
  text: Is 100% fairness even possible? If not, what is an acceptable metric?
  replies:
  - name: Aileen Nielsen
    text: 100% fairness is not possible by any definition of 100% fairness. You're
      not going to have a metric that 100% of people find fair. You're not going to
      have a model that will be guaranteed fair in 100% of the cases. This is for
      a few reasons, but a big one is that there are many plausible and even compelling
      definitions of fairness. In many realistic scenarios, it's not possible to satisfy
      all such cases.
  - name: Aileen Nielsen
    text: 'Re: acceptable metric. This will depend on a host of factors, including
      which kinds of mistakes are most worrying, whether the stakes are high or low,
      whether there are historical reasons to not just go for formal equality but
      to even favor equality-enhancing measures, and so on. So for example, I would
      say that in the case of a life-saving medical application (high stakes), the
      right fairness metric might not be the same as the case of legal price discrimination
      (that is where retailers might price goods differently based on their belief
      that some customers are willing to pay more for the same good).'
- name: Matthew Emerick
  text: Is 100% secure data possible (on the technical side)?
  replies:
  - name: Aileen Nielsen
    text: This is also a no. I am not a data security expert, but based on what I
      do know, there are lots of "known unknowns" (such as the extent of joinable
      data already out in the world, or the extent of vulnerability of a given ML
      model to certain adversarial attacks). There are also presumably unknown unknowns.
      So yeah, no computer security expert is going to promise 100% data security.
      This is especially true because humans ultimately have some form of access at
      some point. For example, even in end-to-end encrypted applications, there are
      easy data leaks, such as a friend screenshotting and sharing pictures of conversations.
- name: Matthew Emerick
  text: Is there any trade off between fairness and security?
  replies:
  - name: Aileen Nielsen
    text: This is an interesting one. I am going to assume that when people ask about
      fairness, they are largely referring to the specific fairness concerns of equality
      and anti-discrimination. In such a case, empirically trade offs have been observed.
      For example, I have seen papers (not difficult to find if you look) where training
      models to be more robust to adversarial attacks tends to enhance unfairness
      as indicated by a variety of fairness metrics (such as differential error rates
      between groups).
  - name: Aileen Nielsen
    text: In general, with most technical systems, it's safe to assume there are trade-offs
      almost always (unless proven otherwise). *However* these trade-offs can sometimes
      be minuscule and not of true concern even if they do exist.
- name: Dinara Kanarina
  text: "Hello Aileen Nielsen! \nThank you for your time! The topic your book covers\
    \ is definetely in demand. \nMay I ask some questions that are not only technical:\n\
    - What is your view on changing the existing language in order to shift systematical\
    \ thinking towards more acceptable and fair? (For example, in some languages that\
    \ have gender distinctiveness, people try to add new endings specific ending to\
    \ female professionals etc.)\n- Do we always try to identify bias and create models\
    \ by excluding it or sometimes it's important to keep it? When then?"
  replies:
  - name: Aileen Nielsen
    text: In answer to your first question, I am all for making language more inclusive
      (and precise). So I find the idea of modernizing language use, grammar, etc,
      to be more inclusive to be a great idea. I also think it's good to call out
      language that has long been accepted but that actually perpetuates inequality.
      For example, it's still common for people to say things like "so easy your grandma
      could do it" or "how would you explain this to your grandma?". "Grandma" (but
      not grandpa) tends to be the stand-in for a presumed doddering old person. This
      is both sexist and ageist, so I try to call this out.
  - name: Aileen Nielsen
    text: On the other hand, I'm not sure it's always productive to be the "thought
      police" and if people don't feel that they can speak freely without getting
      attacked, that can lead to its own problems. So yes, in general I am all for
      more inclusive language, but I am also for a welcoming environment for all and
      taking care not to become the "thought police"
  - name: Aileen Nielsen
    text: "But these are my own personal opinions and not related to the topic of\
      \ coding for fairness so don't take these as anything more than my own thoughts\
      \ \U0001F642"
  - name: Aileen Nielsen
    text: Regarding your second question, whether bias should always be identified
      and removed, in theory I would say yes. A perfect world would be one where we
      can get rid of all bias. However, in practice, I think for the moment it's best
      to focus on high stakes applications where the real costs to humans of bias
      are quite high. So I am far more worried about bias potentially baked in to
      ML models built for policing or healthcare or education than I am about ML models
      built for retail or gaming. (Also see my earlier question that what constitutes
      fairness or bias has many definitions, so that it won't always be possible for
      everyone to agree on whether bias has been removed).
- name: shaolang
  text: 'hi, Aileen Nielsen

    As biasness are often detected in production (and usually with material impact):

    - Are there ways to catch them before that?

    - Would the model(s) need to be explainable?

    Also, are models that use online learning susceptible to biasness and even insecurity
    over time?

    One last question: is fairness and security equally applicable to unsupervised
    learning? If so, how?

    Thanks!'
  replies:
  - name: Aileen Nielsen
    text: 'Re: q1: In my opinion, bias is detected in production models for two reasons.
      (1) No work has been done to debias/audit that particular model (surprisingly
      common) and (2) Some work has been done, but the people identifying the bias
      may have a different definition of bias or a different threshold for establishing
      bias.

      But yes there are absolutely ways to audit a model for bias before it is rolled
      out into production. There are in fact many ways to do so (and more than one
      way can be used). For starters, you can preprocess the data to remove bias you
      identify in the data, you can in process by adding fairness awareness to your
      training process, or you can post process to modify model outputs to make them
      more conformant to a fairness definition. You don''t have to do just one of
      these things....you can do them all.'
  - name: Aileen Nielsen
    text: 'Re: question of explainability. Do models need to be explainable? This
      is a hot topic, and I certainly think that explanation can be appropriate and
      even necessary in many domains. On the other hand, I sometimes think explainability
      is overemphasized in some discussions. For example, we should also recognize
      that in human decision making there is a lot that goes unexplained (or where
      explanations can be pretextual rather than true). Therefore I am a big believer
      in explainability generally but I do not see this as necessary or even desirable
      in all cases. In fact, sometimes explanations can be more confusing than helpful.'
  - name: Aileen Nielsen
    text: 'Regarding your questions about online learning and unsupervised learning.
      Yes, there are absolutely security and fairness concerns here as well. These
      elements of ML are less used in industry, so that''s one reason I focus on them
      less. Also there way to make such practices more fair and robust are also even
      less clear than in the case of supervised ML. However, a good example of a real
      world scenario where such a model existed and rapidly went bad is of course
      Microsoft''s Tay chatbot: [https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist](https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist)'
  - name: shaolang
    text: Woah, thanks for such thoughtful responses! Sorry for such late reply, 'cos
      I had some urgent family matters to attend to.
- name: Prateek Joshi
  text: "Aileen Nielsen: Thank you for being here. Fairness of AI systems is an important\
    \ topic. What metrics can be used to measure the fairness level of an AI system?\
    \ What needs to be standardized between two AI systems before we can compare their\
    \ fairness levels (so that it\u2019s apples-to-apples comparison)? And what levers\
    \ are available to influence the fairness level of an AI system?"
  replies:
  - name: Aileen Nielsen
    text: 'Good questions. Regarding metrics, there are SO many fairness metrics.
      A good starting point to get a sense of some commonly used metrics but also
      to understand some of the nuances and social influences is Arvind Narayanan''s
      tutorial on this topic: [https://fairmlbook.org/tutorial2.html](https://fairmlbook.org/tutorial2.html)
      (_21 fairness definitions and their politics)_'
  - name: Aileen Nielsen
    text: Also I think your second question about apples to apples comparisons is
      super interesting. I would say that models trained for different purposes are
      not comparable. For example, is there any sense in which I can say that a particular
      medical AI application is fairer than some ML credit scoring algorithm? I think
      not. For example, the consequences of making a mistake are quite different (e.g.
      death from wrong treatment versus not getting a loan won't kill you). Also the
      historical considerations may be different (for example, there is evidence that
      minorities continue to be discriminated against in the case of credit....but
      I think this is less problematic for women. On the other hand in the case of
      medicine there is substantial evidence that minorities but also women face substantial
      discrimination in the quality of medical care they receive).
  - name: Aileen Nielsen
    text: So I think it's an interesting question but I'm not sure any simple apples
      to apples comparison is achievable.
  - name: Prateek Joshi
    text: Aileen Nielsen Thank you for the answers.
- name: Aileen Nielsen
  text: Hi everyone! Thanks a lot for your questions. I'll be answering in individual
    threads to the original poster of each question.
  replies: []
- name: Tim Becker
  text: "Hi Aileen Nielsen, thanks for your time.\n- In your opinion, what are the\
    \ biggest security risks a data scientist should be aware of? \n- Is there a general\
    \ procedure on how to test if my models are discriminating?"
  replies:
  - name: Aileen Nielsen
    text: 'Re q1: I think a lack of precautions regarding protecting identifying information
      is the biggest problem I have seen in my experiences in a variety of organizations.
      This presents itself in a variety of ways. Sometimes identifying information
      is gratuitously made available when people are modeling even though it is in
      no way necessary. Relatedly, information is not segmented to minimize what is
      available to any given user (privacy by design). Finally, most data scientists
      I have worked with do not seem to be aware or take seriously the danger of reidentification
      even when identifying information has been putatively removed.'
  - name: Aileen Nielsen
    text: 'Re q2: There are many general procedures but there is no one single procedure.
      Two good resources to get you started are two toolkits. (1) [http://aequitas.dssg.io](http://aequitas.dssg.io)
      and (2) [https://aif360.mybluemix.net](https://aif360.mybluemix.net)'
  - name: Aileen Nielsen
    text: I discuss both of these toolkits in my book, but you can also easily learn
      them through the many tutorial examples they give.
  - name: Tim Becker
    text: thank you :)
- name: Bengsoon
  text: 'Hi Aileen Nielsen  thanks so much for writing this book and for your time
    here. I''m quite new to AI fairness and I still find it hard to wrap my head around
    its framework / toolkits.

    In particular, I notice the topic of AI fairness is mostly wrapped around data/models
    that involve users/groups of people etc. Personally, I work mostly around data
    from machinery sensors and engineering data in the energy sector, a lot of which
    do not have direct implications to any particular groups of people. Will AI fairness
    still be applicable to my data and models, or am I amiss in even asking such question?
    In general, how do I know if AI fairness applicable to my work / domain?'
  replies:
  - name: Aileen Nielsen
    text: Absolutely! sensor data is actually incredibly sensitive from a privacy
      perspective, and I'm a firm believer that privacy is a core pillar of algorithmic
      fairness
  - name: Aileen Nielsen
    text: 'Consider for example this law review article that describes why energy
      usage is in fact quite sensitive and should be protected: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3667125](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3667125)'
  - name: Aileen Nielsen
    text: Also to the extent that you view fairness through an equality lens, I can
      imagine many ways in which sensor data in the energy sector may have unequal
      impacts. For example are communities of color disproportionately subjected to
      highly granular data collection of energy?
  - name: Bengsoon
    text: awesome thank you so much for your input. A lot to chew on for sure, but
      nevertheless a very essential and much needed topic for a time such as this!
- name: Bengsoon
  text: 'Also apologize for creating another thread, but I have a different question:
    for all the AI fairness metrics that are available out there, what is the ground
    basis for fairness? How does one define "fairness"?'
  replies:
  - name: Aileen Nielsen
    text: There is no single definition of "fairness". In fact, this is something
      you'll find varies between cultures and between individuals
  - name: Aileen Nielsen
    text: Given my legal training, I tend to focus on the most fundamental definitions
      of fairness, which tend to relate to antidiscrimination (equality) and to fundamental
      rights (fair process). In these cases, there are decades of legal guidance,
      and so I tend to think a good start is to - at the least - make sure that algorithmic
      fairness in domains regulated by law is at least meeting the same standards
      that have been in place for decades
  - name: Aileen Nielsen
    text: but more generally the question of what is fair is not a question anyone
      can answer definitively
  - name: Aileen Nielsen
    text: therefore for productive ML work I think the best is to consider the fairness
      considerations of a particular domain and then to think about what fairness
      metric makes sense for that domain
  - name: Bengsoon
    text: okay that's pretty clear - sounds like one needs to evaluate the context
      of the region and cultures etc.
---

Fairness is becoming a paramount consideration for data scientists. Mounting evidence indicates that the widespread deployment of machine learning and AI in business and government is reproducing the same biases we're trying to fight in the real world. But what does fairness mean when it comes to code? This practical book covers basic concerns related to data security and privacy to help data and AI professionals use code that's fair and free of bias.

Many realistic best practices are emerging at all steps along the data pipeline today, from data selection and preprocessing to closed model audits. Author Aileen Nielsen guides you through technical, legal, and ethical aspects of making code fair and secure, while highlighting up-to-date academic research and ongoing legal developments related to fairness and algorithms.

- Identify potential bias and discrimination in data science models
- Use preventive measures to minimize bias when developing data modeling pipelines
- Understand what data pipeline components implicate security and privacy concerns
- Write data processing and modeling code that implements best practices for fairness
- Recognize the complex interrelationships between fairness, privacy, and data security created by the use of machine learning models
- Apply normative and legal concepts relevant to evaluating the fairness of machine learning models.