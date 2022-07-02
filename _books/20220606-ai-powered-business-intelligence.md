---
authors:
- tobiaszwingmann
cover: images/books/20220606-ai-powered-business-intelligence/cover.jpg
description: Book of the Week. AI-Powered Business Intelligence by Tobias Zwingmann
end: 2022-06-10 23:59:59
image: images/books/20220606-ai-powered-business-intelligence/preview.jpg
links:
- link: https://www.oreilly.com/library/view/ai-powered-business-intelligence/9781098111465/
  text: Book's page
- link: https://www.amazon.com/AI-Powered-Business-Intelligence-Improving-Forecasts/dp/1098111478
  text: Buy on Amazon
start: 2022-06-06 00:00:00
title: AI-Powered Business Intelligence

archive:
- name: Tobias Zwingmann
  text: Hello everyone! Happy to join this discussion and excited for your questions!
  replies: []
- name: Ruddi Rodriguez
  text: Hello my name is Ruddi Rodriguez  .  I would like to ask you  about security
    issues in platform like H2O for autoML , and in general all cloud service like
    plotly for Dashoboards , or for example prefect for workflow control . How do
    you think that could be the best wait to introduce these tools in a company that
    use customer data ? Thanks
  replies:
  - name: Tobias Zwingmann
    text: Hey Ruddi Rodriguez ! Thanks for your question. Enterprise ML platforms
      like AzureAuto ML, Sagemaker, Vertex AI, Datarobot, H2O etc. generally have
      a high security level compared to most of your own custom solutions. GDPR is
      still a roadblock for many companies in the the EU. I like to use these platforms
      for rapid prototyping because 99% of the more traditional businesses don't have
      the resources to build and maintain their own custom ML stack. They need to
      focus on use cases and execution instead.
  - name: Ruddi Rodriguez
    text: Hi Tobias , thank you for the answer , I have in mind that  perhaps scaling
      and encoder , numerical and categorical data locally before to use a service
      in the cloud can be  an option . Then the data that si exchange with the cloud
      does  not contains data that can be tracked back.
  - name: Tobias Zwingmann
    text: Good approach to anonymize data first before you send it to the cloud!
- name: Ognen
  text: Is the purpose of the book to teach non-data scientists how to use black box
    solutions by pointing and clicking?
  replies:
  - name: Tobias Zwingmann
    text: Haha Ognen! No, it's for people who are well versed with business intelligence
      (including the underlying data) and who want to improve their reports and dashboards
      with the help of some data science techniques. Nocode tools help them to use
      these toys and build fist prototypes without the need of looping in a data scientist
      or turning into a data scientist themselves.
- name: JaimeRV
  text: 'Hi Tobias, one question regarding organizations that are not data driven
    and do not necessarily see how AI-Powered BI could help them. How could they decide
    if it makes sense for them to spend time/resources in learning about AI-Powered
    BI?

    I am thinking about bigger organizations who could intuitively see some value
    on some dashboards but might be skeptic to invest AI/ML'
  replies:
  - name: Tobias Zwingmann
    text: Hi JaimeRV - great question! Prototyping is the way to go. In my experience,
      building a quick PoC in a small team (3-5 people) helps a lot as it demonstrates
      value even to non-technical management and get buy-in. It definitely helps if
      the management follows some top-level data or digitalization strategy as you
      can potentially link your prototypes/pocs to that which makes everything much
      easier.
  - name: JaimeRV
    text: Thanks for the answer Tobias Zwingmann!
- name: Ruddi Rodriguez
  text: 'Hi Tobias I have another question actually several  , why Azure and not AWS
    for the book? a second one: with tools like H2o where you can train for free your
    model and from my point of view with a simpler interface  ,  do you think that
    the future will go in the direction of platforms like H2o?'
  replies:
  - name: Tobias Zwingmann
    text: Hi Ruddi Rodriguez, I chose Azure because I find it easier to use than AWS.
      Also, many companies build on the Microsoft stack for their BI (eg PowerBI)
      so I found Azure more natural for them. H2O is also a great platform. But even
      here, once you move to their enterprise MLOps platform you have to pay. Most
      non-tech companies are much better off taking an MLOps platform from the shelf
      and using it instead of trying to build with open source tools and reinvent
      the wheel imho.
  - name: Ruddi Rodriguez
    text: Thanks for the answer, I see  Power BI gives to Azure an advantage in many
      cases. So, if I understood well if I use AWS it lacks a tool integrated like
      power BI, sorry for the naive question I have zero experience using these tools
      I do everything locally mainly because of security restrictions. We are not
      even allowed to use power BI.
  - name: Ruddi Rodriguez
    text: well "we"  , I am the only one
  - name: Tobias Zwingmann
    text: "AWS doesn't have a native BI tool as far as I know. But it's very easy\
      \ to build a model with eg Sagemaker, deploy it as an HTTP endpoint and query\
      \ this endpoint from within PowerBI / PowerQuery. That's why I have not focused\
      \ on the \u201Cnative\u201D integration between Azure and PowerBI in the book,\
      \ but explained how to bring those tools together with a little scripting in\
      \ Python or R."
- name: Tim Becker
  text: 'Hi Tobias Zwingmann, thanks for being here and for answering our questions!

    - Could you give us some example of where AI-powered analytics had a great business
    impact?

    - What is an AI-powered analytics dashboard?'
  replies:
  - name: Tobias Zwingmann
    text: 'Hi Tim Becker - glad to be here and thanks for your questions!

      1- I had an aha moment once when I realized how dashboard users where using
      natural language queries very intuitively to get the metrics they wanted from
      a dashboard. It works really well. The technology has become mature enough and
      user have been trained to this kind of data retrieval over years because it
      works similar like a google search. I think key is when you really start with
      the basics and thus empower the masses. I have seen computer vision applications
      for turning unstructured data into structured data also deliver great results
      (eg document analysis)'
  - name: Tobias Zwingmann
    text: 2- An AI-powered analytics dashboard for me is when you use AI to improve
      your analytics/reporting experience throughout multiple stages (descriptive,
      diagnostic, predictive and prescriptive analytics)
  - name: Tim Becker
    text: "thank you \U0001F642"
  - name: Tim Becker
    text: Concerning question 1, do I understand correctly that the user would for
      example type "monthly sales" or "daily imports November" into a field and then
      get figures with corresponding data?
  - name: Tobias Zwingmann
    text: "exactly! Even more complex queries work pretty well meanwhile thanks to\
      \ the advancements in NLP. eg \u201Csales in the US over time\u201D or \u201C\
      daily active users january vs february as bar chart\u201D"
  - name: Tobias Zwingmann
    text: you can combine that with a custom business glossary so the tool speaks
      the language of your analysts which really makes it a powerful technology
  - name: Ruddi Rodriguez
    text: The first example indeed is very powerful. But I think not many companies
      use are not using such tools in their daily tasks. Many companies are tight
      to Excel or even worst to delivering reports. Do you have any thoughts on why
      too many companies, including big banks, are still far behind in terms of AI?
      And why are they still struggling to change from power BI to tableau to excel
      and back without a good strategy to develop or adopt solutions as you mentioned?
  - name: Tobias Zwingmann
    text: "Technology adoption always happens in phases. \nWhy did people still use\
      \ typewriters when the could use computers?\nWhy did people still send letters\
      \ when they could send an email?\nWhy do people still use email if they could\
      \ use slack?\nSooner or later, new technologies will replace old, but it's hard\
      \ to predict which and when. We humans are crazy creatures \U0001F603"
  - name: Tobias Zwingmann
    text: "But some general principles for enterprise AI adoption: \n- must be triggered\
      \ from top to bottom. No leadership buy-in, means no AI strategy\n- you have\
      \ to come up with a use case roadmap and tie that into a vision\n- you need\
      \ to sell that vision to the employees \n- you have to acknowledge that culture\
      \ eats strategy for breakfast"
  - name: Ruddi Rodriguez
    text: "\U0001F44D"
- name: Allan
  text: Hi Tobias Zwingmann , would this book be appropriate for who has a background
    in data science and ML, but not necessarily BI?
  replies:
  - name: Tobias Zwingmann
    text: "Hi Allan, they won't probably find it as valuable as the other way around.\
      \ But if you\u2019re looking for use case inspiration to apply your data science\
      \ skills to BI (and especially PowerBI) it might still be useful for you."
  - name: Allan
    text: Thanks Tobias, appreciate your taking the time to answer questions here!

---

Use business intelligence to power corporate growth, increase efficiency, and improve corporate decision-making. With this practical book, you'll explore the most relevant AI use cases for BI, including improved forecasting, automated classification, and AI-powered recommendations. And you'll learn how to draw insights from unstructured data sources like text, image, and voice audio files.

Author Tobias Zwingmann, senior data scientist and cofounder of Germany-based AI startup RAPYD.AI, helps BI, business, and data analysts understand high-impact areas of predictive and prescriptive analytics. You'll learn how to leverage popular AI-as-a-service and AutoML platforms to ship enterprise-grade proof of concepts without the help of software engineers or data scientists.

- Learn how AI can generate business impact in BI environments
- Use AutoML for automated classification and improved forecasting
- Implement recommendation services to support decision-making
- Draw insights from text data at scale with NLP services
- Extract information from documents and images with computer vision services
- Make voice audio files accessible for reporting with AI transcription services
- Build interactive user frontends for AI-powered dashboard prototypes
- Implement an end-to-end case study for building an AI-powered customer analytics dashboard