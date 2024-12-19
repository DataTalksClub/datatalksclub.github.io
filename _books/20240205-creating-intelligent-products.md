---
authors:
- jannalipenkova
cover: images/books/20240205-creating-intelligent-products/cover.jpg
description: Book of the Week. Creating Intelligent Products by Janna Lipenkova
end: 2024-02-09 23:59:59
image: images/books/20240205-creating-intelligent-products/preview.jpg
links:
- link: https://www.manning.com/books/creating-intelligent-products
  text: Book's page
start: 2024-02-05 00:00:00
title: Creating Intelligent Products

archive:
- name: David Odimegwu
  text: Hi. Lately, I have been researching an AI chatbot that is embeddable on a
    website and can connect to Bard or chat along with my data or documentation for
    customer service and sales. I really don't know if you can recommend a budget-friendly
    product for me. I just started a small company in Lagos, Nigeria and wanted to
    use this service to help retailers and small businesses in my country. Thanks.
    BTW, I looked through the chapter contents on your book on the Manning site and
    love it. It's now in my cart. I look forward to an answer to my question.
  replies:
  - name: Simas Janusas
    text: 'Hi David Odimegwu it sounds like you need a RAG solution.

      Are you looking for a no/low-code solution or something that requires technical
      knowledge to build?

      Any specific reason for using Bard? Alternatives possible (e.g. OpenAI?)

      A few resources that comes on my mind to take a look into it:

      - [Watson Chatbot embedding into website](https://developer.ibm.com/tutorials/embed-watson-assistant-in-website/)

      - [OpenAI Integeration discussion in COmmunity](https://community.openai.com/t/any-app-to-embed-a-assistant-onto-a-website-or-can-i-embed-it-myself/491783/2)

      - [Create a Generative Chat App with Vertex AI Conversation](https://codelabs.developers.google.com/codelabs/vertex-ai-conversation)
      (technical tutorial by Google. what I like in this to enable voice calls)'
  - name: David Odimegwu
    text: I don't mind something that requires programming knowledge especially if
      it's python which is now ubiquitous. I was thinking of bard because open ai
      charges for API calls and the dollar-naira exchange rate in my country would
      make the solution infeasible for the small businesses I have in mind. Thanks
  - name: Janna Lipenkova
    text: Hello David, thanks for your question! Cost is one of the important trade-offs
      to manage when selecting LLMs. If you are highly constrained in terms of budget
      but can put good programming expertise on the table, you can even try using
      an open-source model such as Mistral and integrate it into a RAG pipeline. Basically,
      in your case, you want to source the knowledge from your own documentation,
      but you also want to benefit from the linguistic capabilities of LLMs in order
      to get fluent responses.
  - name: Janna Lipenkova
    text: 'Here is a tutorial on implementing RAG with Mistral: [https://medium.com/@thakermadhav/build-your-own-rag-with-mistral-7b-and-langchain-97d0c92fa146](https://medium.com/@thakermadhav/build-your-own-rag-with-mistral-7b-and-langchain-97d0c92fa146)'
- name: Antonis Stellas
  text: Hello! Considering the added uncertainty that AI brings to product's performance,
    what strategies do you suggest for continuously improving AI performance? Also,
    how do you efficiently communicate this uncertainty to stakeholders?
  replies:
  - name: Janna Lipenkova
    text: 'Hello Antonis, thanks a lot for your question! I think it is a very important
      question for the UX and the safety of AI products. The UX we are used to is
      deterministic, but AI is not, and we need to attack this problem from both ends
      - by improving the AI, but also by educating users and other stakeholders.

      To continuously improve the performance of the AI, you need to monitor the predictions
      and evaluate them. The evaluation can either be done by the developing team,
      or by users of the product. The latter option is more involved (users will not
      always be willing to give feedback, and the data is more noisy), but if you
      manage to implement good feedback mechanisms in your UX I believe it is one
      of the most valuable sources for information. Then, you do problem analysis
      and see which of your components (data, model weights, prompt, UX, etc.) you
      need to tweak to address the problems.

      In terms of communication with users and other stakeholders, I believe it is
      very important to provide them with a basic understanding of what a model can
      and cannot do. For example, an LLM can be highly multi-functional - it can summarize,
      edit, converse, create content, etc., but all of this functionality is hidden
      behind one single prompt input! This is very different from the graphical interfaces
      we are used to.

      Then, for specific generations, we can use additional mechanisms, such as confidence
      scores, to signal to the user how confident a model is about its own output.
      We can also set thresholds for confidence below which the UX will show an alert
      or red flag, and encourage the user to get into the loop and check the output.'
  - name: Antonis Stellas
    text: Thanks! I would love to hear more about examples of such mechanisms in real
      products. It's very interesting.
  - name: Janna Lipenkova
    text: Absolutely. My book will contain a separate chapter on AI UX, and dealing
      with uncertainty and AI failures is one of the big topics there!
- name: Nishrin Kachwala
  text: 'Hi Janna Lipenkova

    I would like to understand the key criteria you recommend for evaluating AI technologies
    for integration into existing products? How do you balance the trade-offs between
    cutting-edge AI capabilities and the practicality of implementation?'
  replies:
  - name: Janna Lipenkova
    text: "Hello Nishrin Kachwala,\nI believe there are three key criteria for evaluating\
      \ AI tech in a specific product scenario:\n- The technical cost (API calls,\
      \ GPUs and other infrastructure, etc.)\n- The development effort and the technical\
      \ skills available in your company\n- The value and role of AI in your product;\
      \ is it an add-on to an existing product, the central component and differentiator\
      \ of a new product, or an internal \u201Cenabler\u201D that helps you optimize\
      \ your product?\nBased on these criteria, you can determine a rough direction.\
      \ For example, if you are building an AI product from scratch and have a bunch\
      \ of hard-core ML engineers that are hungry for technical challenges, you probably\
      \ want to switch to your own infrastructure and open-source models instead of\
      \ using OpenAI ASAP. Thie will allow you to capitalize on your tech skills,\
      \ and avoid the running costs of API calls.\nBeyond this, there is a range of\
      \ additional criteria which I call \u201Cnon-functional\u201D requirements.\
      \ Is high accuracy more important than speed, for example if you are dealing\
      \ with high-stake decisions but the AI jobs can be run in batches overnight?\
      \ Is privacy a central consideration, so you need to give up on the training\
      \ data you could potentially collect from production use? etc."
  - name: Janna Lipenkova
    text: A, and beyond that, the availability of proprietary data in your company
      can also influence your choices. Data is one of the moats you can build around
      your AI product. If you have valuable data that is already available, you can
      select AI technologies and approaches that will allow you to leverage it - for
      example, by choosing and fine-tuning open-source models rather than commercial
      APIs.
- name: Francisco Delca
  text: 'Hi Janna Lipenkova,

    I hope this message finds you well. First, I would like to express my gratitude
    for this book; I believe it significantly aids professionals working as product
    owners/managers in understanding how AI can enhance traditional software value
    for users. Recently, I''ve embarked on a course on becoming an AI PM, and my questions
    align with the insights gained from it as well. With that in mind, I would like
    to inquire:

    1. How can we assess the actual value of an AI feature for the customer before
    implementation, and what metrics or methods do you recommend for measuring its
    impact on user experience?

    2. While AI products offer adaptability to new environments, the absence of effective
    feedback loops can result in a loss of insight into the outcomes of AI features.
    What specific feedback loop mechanisms do you recommend to monitor and control
    the performance and outcomes of AI models over time?

    3. In the scenario where an AI feature becomes deprecated and requires retraining
    while users continue to interact with the product, what contingency plans or strategies
    do you propose to ensure a seamless experience for users, providing them with
    similar outcomes during the transition period?'
  replies:
  - name: Janna Lipenkova
    text: "Hello Francisco Delca, thanks for your questions! Re 1:\n1. Formulate value\
      \ hypotheses; AI features can add value in different ways, and the related KPIs\
      \ are different. For example:\n\t- Making sense of large data -> quantity of\
      \ data covered\n\t- Efficiency -> time and cost savings\n\t- Personalization\
      \ -> time savings, adoption, CSAT\n\t- Convenience -> CSAT\n\t- Fun -> CSAT\n\
      2. Test your hypotheses, starting with low-impact tests: mockups/clickable prototypes\
      \ -> \u201Chard-coding\u201D a simple version of the feature, without any ML\
      \ behind -> training simple ML models or using out-of-the-box LLMs"
  - name: Janna Lipenkova
    text: "Re 2: There are three main sources of evaluation: using LLMs as judges,\
      \ collecting user feedback, and evaluating the AI outputs yourself. Since your\
      \ question seems to be related to \u201Cproduction\u201D use, let\u2019s focus\
      \ on the latter two:\n- Collect explicit user feedback; this can be as simple\
      \ as thumbs up/down, or via more involved feedback forms if you manage to incentivize\
      \ your users.\n- To incentivize your users, educate them about the data flywheel!\
      \ The more feedback they provide, the better their user experience and the accuracy\
      \ of the predictions will get.\n- Observe user behavior, such as click-through\
      \ rates for recommendations and search.\n- Inspect samples of the data in your\
      \ team. You will have a different, but also very valuable perspective on the\
      \ data internally.\nThe main goal is to complete your training and evaluation\
      \ datasets with novel, difficult, and otherwise interesting examples. Eventually,\
      \ this will allow you to use your data as a moat."
  - name: Janna Lipenkova
    text: 're 3: I think there is no magic bullet here. If a feature is becoming deprecated,
      remove it from the product. If the model that drives the feature is becoming
      deprecated, work on two key factors:

      - Transparency. Make your users aware of the fact that they are using a deprecated
      feature, and potentially highlight AI outputs as low-confidence, asking them
      to scrutinize and review them.

      - MLOps. Having a solid MLOps pipeline can turn retraining, fine-tuning, and
      continuous updates into a natural and seamless process. In most cases, high-frequency
      updates can be performed via continued fine-tuning without retraining the full
      model. However, at some point, the model can accumulate too much outdated knowledge
      which will pollute its predictions. In this case, retraining is needed and should
      be performed on a schedule that allows to seamlessly integrate the new model.'
  - name: Francisco Delca
    text: "Thank you for your insights, Janna Lipenkova. I'm glad to know that my\
      \ thinking aligns with yours, and your responses have certainly helped organize\
      \ my thoughts on how to proceed. The key takeaways for me are:\n- Starting with\
      \ a simple solution complemented by the right feedback loops can serve as a\
      \ PoC for implementing more complex AI systems;\n- It's crucial to understand\
      \ what KPIs to measure and how, whether through direct feedback or a user experience\
      \ tracking dashboard; (also important for PoC);\n- Always collaborate with your\
      \ team. It's crucial to incorporate perspectives from different departments,\
      \ as they may identify unique values in the data. Discuss -&gt; Refine the Ideas\
      \ -&gt; Improve\n- Be transparent / Educating users is essential; helping them\
      \ understand that while no solution is perfect, the right feedback can optimize\
      \ the system to meet their needs (educate them about the data flywheel);\n-\
      \ While MLOps is significant, a simple product may not require a robust MLOps\
      \ framework. However, as models become more complex, navigating the nuances\
      \ of MLOps becomes indispensable. (Thanks to DataTalks we have this resources\
      \ available, so its a matter of doing it \U0001F605)"
- name: Ella
  text: 'Hello. How do you suggest we instill the sense in our  AI product users that
    our AI-apps is still in infancy stage? To take our suggestions but still need
    to verify the info it gives?

    I have this worry that the product consumers have such confidence and faith in
    AI-products like web searches, that they take 100% suggestions 100% of the time.

    Also because, most people don''t read long texts anymore (let alone fine print).

    Because I still need to balance the need to market my AI-app to more users right?
    and yet ensure that the safety, ethical and fairness concerns is still covered?

    I see some great answers already from your reply to Antonis. I guess, it is like
    in gaming where games are released in "early access" and is understood as bug-prone
    and incomplete.

    Do we have something similar in AI-products?'
  replies:
  - name: Janna Lipenkova
    text: "Hello Ella, I love your question! It picks up on my favorite topic of the\
      \ \u201Chuman-AI partnership\u201D. I believe we have a long-term challenge\
      \ of educating humans about how they can work alongside AI without expecting\
      \ (trusting) it to be 100% correct all the time. On the other hand, the UX should\
      \ reflect the uncertain and non-deterministic character of AI applications.\n\
      So, one challenge is educational. We should teach humans to use AI in an optimal\
      \ way, alleviate their \u201Cfears\u201D when it comes to AI, and also prepare\
      \ them for a future where AI will be carrying out most of our daily tasks.\n\
      The other challenge is the UX. Here are some mechanisms I have considered so\
      \ far for AI UX design:\n- Content architecture: Be super thoughtful about how\
      \ you design instructions, prompt suggestions/placeholders, etc., and live-test\
      \ each of these elements.\n- Provide transparency and explainability: explain\
      \ how you calculate values, how generations are made, provide sample datapoints,\
      \ etc.\n- Disclaimers and confidence scores: Emphasize the potential shortcomings\
      \ and issues of the AI.\n- Feedback collection: By collecting feedback, you\
      \ support a feeling of uncertainty and alertness on the user side. Additionally,\
      \ you also communicate to them that they are a \u201Cco-creator\u201D of your\
      \ product and the AI models, thus reinforcing the partnership idea.\n- Rethink\
      \ traditional UX issues like friction and latency. In AI products, you can use\
      \ them to your advantage. For example, you can insert additional dialogue windows\
      \ to force the user into the loop, asking them to confirm or modify AI outputs.\
      \ You can use latency times to educate them about what is going on behind the\
      \ curtain, etc.\nHope this helps! I believe there is a lot to do in AI UX and\
      \ psychology. Two resources I can recommend are:\n- XAI for designers: [https://www.uxai.design/](https://www.uxai.design/)\n\
      - Articles and other materials by the Nielsen Norman group: [https://www.nngroup.com/topic/ai/](https://www.nngroup.com/topic/ai/),\
      \ as well as Don Norman\u2019s book The Design of Future Things"
  - name: Ella
    text: 'Thank you for the resources, and the insights!

      I still have lots of research and thinking to do!'
  - name: Ella
    text: 'I love the thought of making them a part of the creation process! A co-creator!
      Get them engaged in the process and remain invested.

      Lovely idea.'
  - name: Janna Lipenkova
    text: "Yes, exactly \U0001F642 Humans should be rational and competent in cooperating\
      \ with AI. No fears, no inflated expectations. It is also important to understand\
      \ how AI actually works (the basic principles and intuitions, not the mathematical\
      \ details) in order to get the maximum benefit out of it."
  - name: David Odimegwu
    text: 'Good morning. Please, is UXAI related to conversational AI? When I read
      this advice: "Content architecture: Be super thoughtful about how you design
      instructions, prompt suggestions/placeholders, etc., and live-test each of these
      elements." it made me think so.

      Also where do they diverge and which is better to learn, UXAI or conversational
      AI to help humans understand AI speak.'
  - name: Janna Lipenkova
    text: Hi David Odimegwu, I am not sure what you mean by UXAI. There is UX of AI
      products (I abbreviate it as AI UX ;)), and the conversational UX is a subcategory
      of it.
  - name: Janna Lipenkova
    text: "Content architecture is very important for conversational products, which\
      \ can, but don\u2019t need to be chatbots - it can also be a question-answering\
      \ platform with a simple prompt window. But what we see from experience is that\
      \ content architecture is also crucial for analytical products, dashboards etc.,\
      \ where users need guidance to read, interpret, and explore the data."
- name: Dr Abdulrahman Baqais
  text: 'Hello Janna Lipenkova Thank you for the book.

    1. Do AI products follow versioning like software products. I do not see this
    adopted in enterprices. It seems they rely more on retraining only.

    2.  Unlike software where there is SIT and UAT, how to ensure that AI products
    pass the testing? What do you suggest as a testing pipeline for AI products?

    3. Many stakeholddrs focus on ROI only for AI products but not the same for IT.

    How to convince them of other advantages that AI-powewd bring rather than monetary
    value.

    thank you'
  replies:
  - name: Janna Lipenkova
    text: Hello Dr Abdulrahman Baqais, thanks for your questions!
  - name: Janna Lipenkova
    text: '1. AI products do follow versioning just as regular products do. And AI/ML
      models also follow versioning - in fact, I think versioning is one of the main
      components of MLOps. Beyond retraining a model (with other input data or configs),
      you can also load an existing model and continue its training (or fine-tuning)
      with new data, thus creating a new version.

      2. Again, I suspect you are talking about AI models. In our own practice, we
      are defining a test suite of predictions or generations that they should be
      able to make successfully. These contain happy-path examples but also edge cases.
      For example, recently, I was involved in multiple projects on Text2SQL ([https://medium.com/towards-data-science/enabling-the-data-driven-organisation-with-text2sql-f8e07089dd0c](https://medium.com/towards-data-science/enabling-the-data-driven-organisation-with-text2sql-f8e07089dd0c)).
      We defined test examples for each class of queries we were expecting, like AGG,
      JOIN, WHERE, GROUP BY, etc.

      3. Please refer to this answer: [https://datatalks-club.slack.com/archives/C01H403LKG8/p1707316895985859?thread_ts=1707216148.527289&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1707316895985859?thread_ts=1707216148.527289&amp;cid=C01H403LKG8)'
- name: Xiaomei Song
  text: "Yuan Tang I hope all is well. As I navigate my journey in AI, focusing on\
    \ ethics and safety, I\u2019m considering two projects for next semester, each\
    \ aligning with different AI facets. Your expertise would be invaluable in helping\
    \ me choose.\nProject 1 is about enhancing AI safety and fairness, aiming to reduce\
    \ societal biases in LLMs through techniques like ROME and RepE. This aligns with\
    \ my commitment to ethical AI, focusing on making LLMs more equitable. I\u2019\
    ll collaborate with a Statistic PhD student and a senior Computer Science student\
    \ at UCB.\nProject 2 focuses on improving a student-facing LLM\u2019s reliability\
    \ and safety, incorporating features to prevent misinformation and ensure content\
    \ accuracy. This project is crucial for educational AI applications. My team will\
    \ include two master\u2019s students and one doctoral student from EECS at UCB.\n\
    Both projects promise meaningful contributions to AI, yet I\u2019m unsure which\
    \ best suits my career goals and offers the most enriching experience. Could you\
    \ offer your insights on which project might have a more significant impact and\
    \ growth potential in AI safety and fairness? Any additional advice for decision-making\
    \ in this field would be greatly appreciated.\nThank you for your time and wisdom.\n\
    Warm regards, Xiaomei"
  replies: []
- name: Nishrin Kachwala
  text: 'Hi Janna Lipenkova

    1. With the increasing scrutiny on AI ethics and governance, what best practices
    do you recommend for companies to manage these risks proactively? Can you discuss
    a case where a company effectively navigated these challenges?

    2. AI projects can be expensive. Can you share insights or case studies on how
    to manage and optimize costs during the development and deployment of AI-powered
    products?

    3.  Once AI has been integrated into a product, how should success be measured?
    Are there specific metrics or KPIs that you find most indicative of an AI project''s
    value to the business?'
  replies: []
- name: Janna Lipenkova
  text: Thanks a lot for your questions!! Was a fun week and I think I crystallized
    some new information needs which I will elaborate on in the book!
  replies: []

---

Creating Intelligent Products: Generative AI, advanced analytics, smart automation teaches you how to successfully integrate AI into your software products. Written for product managers, team leads, and anyone responsible for the success of a software product or service, this practical book introduces Generative AI, AI-assisted data analytics, intelligent process automation, and more. You’ll love the examples from across many industries that illustrate the power and versatility of AI-powered solutions.

Inside Creating Intelligent Products: Generative AI, advanced analytics, smart automation you will learn vital skills for the effective use of AI, including:

- Identifying market and business opportunities for AI
- Evaluating AI technologies for products and features
- Effectively communicating with data scientists and ML engineers
- Designing user-friendly AI interfaces
- Best practices in AI ethics, governance, and risk management

AI-powered software introduces new opportunities and challenges for product managers. This one-of-a-kind book guides you from initial design conversations through development, deployment, and day-to-day management with techniques to make the process efficient, secure, and cost effective. You’ll learn to capitalize on AI’s full potential for your business with strategies that set you on the path to market leadership in your industry.