---
episode: 4
guests:
- nikitakozodoi
ids:
  anchor: datatalksclub/episodes/From-GenAI-Pilots-to-Production---Nikita-Kozodoi-e3kc7uh
  youtube: 1LhvqZvDT5w
image: images/podcast/s24e04-from-genai-pilots-to-production.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/From-GenAI-Pilots-to-Production---Nikita-Kozodoi-e3kc7uh
  apple: https://podcasts.apple.com/us/podcast/from-genai-pilots-to-production-nikita-kozodoi/id1541710331?i=1000771350776
  spotify: https://open.spotify.com/episode/6PDxN20VMKvkwLyVyG5uvX?si=b75bd781f72c4098
  youtube: https://www.youtube.com/watch?v=1LhvqZvDT5w
season: 24
short: From GenAI Pilots to Production
title: From GenAI Pilots to Production
transcript:
- header: Shifting from traditional ML to generative AI
- line: Hi everyone, welcome to our event. This event is brought to you by DataTalks.Club,
    which is a community of people who love data. We have weekly events, and today
    is one of such events.
  sec: 0
  time: 0:00
  who: Alexey
- line: If you want to find out more about the events we have, there is a link in
    the description. Go check it out. Do not forget to subscribe to our YouTube channel.
    This way you will stay up to date with all the future streams that we will have.
  sec: 7
  time: 0:07
  who: Alexey
- line: Last but not least, we have an amazing Slack community where you can hang
    out with other data enthusiasts. During today's interview, you can ask any question
    you want. There is a pinned link in the live chat. Click on that link, ask your
    questions, and we will be covering these questions during the interview.
  sec: 24
  time: 0:24
  who: Alexey
- line: By the way, I think this is Grammarly. I do not remember when I took this
    screenshot, but ever since ChatGPT came out, I kind of stopped using it. It is
    an old screenshot.
  sec: 37
  time: 0:37
  who: Alexey
- line: Do you use Grammarly, Nikita?
  sec: 51
  time: 0:51
  who: Alexey
- line: Not anymore, to be honest. I share a similar impression that after all these
    GenAI tools came out, it is just easier to prompt them instead of doing it by
    yourself.
  sec: 54
  time: 0:54
  who: Nikita
- line: Today we will be talking about what it takes to move GenAI from pilots to
    production. In this episode we will speak with Nikita, PhD, senior applied data
    scientist at the AWS Generative AI Innovation Center. That is a very long name.
  sec: 67
  time: '1:07'
  who: Alexey
- line: Nikita works with companies across industries to design and build custom GenAI
    and agentic solutions for real business problems. Welcome.
  sec: 82
  time: '1:22'
  who: Alexey
- line: Thank you. Thank you, Alexey, for inviting me, and hello to everyone who is
    listening.
  sec: 92
  time: '1:32'
  who: Nikita
- line: For me, this is especially interesting because I noticed more and more people
    started having the role of AI engineer starting from January. When thinking about
    this role, Nikita, you are the first person I think about because you have been
    doing this for quite some time.
  sec: 98
  time: '1:38'
  who: Alexey
- line: I do not know whether you consider yourself an AI engineer or not, but we
    get to see each other in person quite regularly. I always think about you. Finally,
    I am very happy to have you here and talk about what you do at work, as well as
    all the things that happened in the last couple of years. I am really interested
    to learn from you here today. Welcome.
  sec: 114
  time: '1:54'
  who: Alexey
- line: I am excited to talk about it and discuss different things with you about
    AI and what we do with different companies.
  sec: 148
  time: '2:28'
  who: Nikita
- line: Let us start by talking about your background. Can you tell us about your
    career journey so far?
  sec: 157
  time: '2:37'
  who: Alexey
- line: Yes, sure. My background is actually in economics. There has been a journey
    for me transitioning towards machine learning and AI over the years. I finished
    my bachelor's and master's in economics, but my most interesting subjects, and
    the ones I was more passionate about, were actually statistics and econometrics.
  sec: 165
  time: '2:45'
  who: Nikita
- line: These subjects were related to data analysis, so I started checking out different
    platforms and found Kaggle. This is probably one of the common journey types for
    different people. Once I found it out, I was sure that this is what I want to
    do.
  sec: 188
  time: '3:08'
  who: Nikita
- line: I started gradually transitioning more and more towards data science and machine
    learning. I learned some things by myself and learned other things through the
    courses I could take at the university. My bachelor's and master's were done in
    Russia at the Higher School of Economics, and then I moved to Berlin.
  sec: 205
  time: '3:25'
  who: Nikita
- line: I think this was about 12 years ago, and I have been living in Germany since
    then. Here, I did a PhD on machine learning for financial applications. I was
    focusing on a topic around credit scoring.
  sec: 220
  time: '3:40'
  who: Nikita
- line: That is when we build models that basically predict whether a certain person
    will return the loan or whether they will not be able to do that. To build these
    models, we need to use machine learning heavily.
  sec: 238
  time: '3:58'
  who: Nikita
- line: I was mostly thinking about traditional ML models, with no GenAI yet. Things
    like gradient boosting and feature engineering were my areas of expertise back
    then. After I did my PhD, I joined Amazon about four years ago.
  sec: 254
  time: '4:14'
  who: Nikita
- line: I first joined the team called Machine Learning Solutions Lab. That team is
    a part of Amazon Web Services, and it was working with different customers. We
    worked with other enterprises, startups, and different companies and entities
    who need help implementing machine learning use cases and creating business value
    out of problems they could not solve yet.
  sec: 269
  time: '4:29'
  who: Nikita
- line: When I joined Amazon, the focus was mostly on traditional machine learning.
    For example, the first project I did when I joined was about demand forecasting.
    We were working with our customer Adidas, who basically needed our help to predict
    how much different items will be selling in different stores around the world.
  sec: 303
  time: '5:03'
  who: Nikita
- line: These were the kinds of projects we were doing. Our team basically builds
    the first prototype, the first proof of concept, to prove that machine learning
    can solve the use case. If it can, then we will talk about putting it into production.
    I was doing a couple of classic machine learning projects at Amazon, and then
    something happened. We all know what happened.
  sec: 327
  time: '5:27'
  who: Nikita
- line: When was it for you?
  sec: 352
  time: '5:52'
  who: Alexey
- line: I think it was when ChatGPT got released. I think this was three years and
    a couple of months ago when ChatGPT came out, and it was immediately clear that
    this is something big and new.
  sec: 354
  time: '5:54'
  who: Nikita
- line: It did not happen overnight, but more and more as months went by, companies
    and enterprises got interested in what GenAI can do for them. We also started
    to realize individually, but also as a team as part of AWS, that many use cases
    we previously could not even think about, or could not find a good solution to
    solve with machine learning, are now possible with the new technology.
  sec: 370
  time: '6:10'
  who: Nikita
- line: We basically just started doing more and more projects that use GenAI in one
    form or another. Since that time, our team basically changed.
  sec: 393
  time: '6:33'
  who: Nikita
- line: I became part of a new team which is not the Machine Learning Solutions Lab
    anymore, but is called the GenAI Innovation Center. This team basically helps
    AWS customers, which are mostly enterprises and other companies, to unlock new
    use cases and to productionize solutions that leverage GenAI in one way or another.
  sec: 411
  time: '6:51'
  who: Nikita
- line: I was making my personal journey along with the changing trends in the industry.
    At first, I was the kind of person who specialized in classic tabular data and
    knew everything about gradient boosting and algorithms like that. Even though
    those algorithms are still very useful in many use cases, I shifted my focus towards
    NLP and GenAI solutions.
  sec: 444
  time: '7:24'
  who: Nikita
- header: Hybrid pipelines blending classical ML and LLMs
- line: Do you still get to use any of the classical machine learning?
  sec: 469
  time: '7:49'
  who: Alexey
- line: Sometimes yes, but with the kind of solutions our team is building, it may
    happen that a classic ML model is part of the pipeline. Maybe we need to generate
    some content, but as part of generating this content, we need to make certain
    predictions with forecasting models, for example. Sometimes they become blended
    into one pipeline.
  sec: 473
  time: '7:53'
  who: Nikita
- line: If it is a pure classical ML use case at work, this is not something that
    the GenAI Innovation Center is doing. There are other teams who focus on classic
    machine learning, but from time to time, there are different projects that involve
    its usage.
  sec: 502
  time: '8:22'
  who: Nikita
- line: I do not know if you consider NLP models classical, like classification and
    entity extraction. Sometimes a GenAI model is working better, but sometimes it
    actually makes more sense to fine-tune a smaller classifier like modern BERT.
  sec: 510
  time: '8:30'
  who: Nikita
- line: I was in Porto a few weeks ago, and there was a talk about classical NLP versus
    generative NLP. By classical, they of course mean BERT and all this kind of stuff.
    I was like, wait a minute, this thing is what, five years old?
  sec: 537
  time: '8:57'
  who: Alexey
- line: Yes, exactly. I remember reading one joke on the internet, which was based
    on an actual case where someone was presenting a new paper at one of the AI conferences,
    probably NeurIPS.
  sec: 557
  time: '9:17'
  who: Nikita
- line: They realized that the audience attending the talk does not know what TF-IDF
    is because it is now considered very old. There is a whole new generation that
    does not even know what it is because it is not used anymore.
  sec: 573
  time: '9:33'
  who: Nikita
- line: It is not one of the questions that we have prepared for you, but I can't
    help but wonder. You said you use classical ML in your pipelines, so the solution
    is still GenAI, but you sometimes have ML here and there. What is the most common
    use case or the most common part of the pipeline where you see that, or is it
    too different to see a pattern?
  sec: 588
  time: '9:48'
  who: Alexey
- line: It is really different because we work with customers coming from many different
    industries. Forecasting is probably something that is not going away, and I see
    many companies using it for demand forecasting, sales forecasting, and different
    kinds of time series.
  sec: 618
  time: '10:18'
  who: Nikita
- line: In those cases, classical transformer models are working better. You do not
    need to run Claude Opus to predict what the next value of the time series is going
    to be. Forecasting is one of such popular use cases.
  sec: 636
  time: '10:36'
  who: Nikita
- line: I am thinking that you do not need to run Claude Opus on that, but also, if
    you do, I have a concern about whether the prediction will actually be good.
  sec: 650
  time: '10:50'
  who: Alexey
- line: Yes, exactly. One reoccurring topic I have seen a couple of times is when
    you use a classical ML model to make predictions, but then you can use a GenAI
    model to contextualize or explain them.
  sec: 667
  time: '11:07'
  who: Nikita
- line: You can provide some kind of explainability where you can put in a text form
    why this model predicted this, based on things like variable importance and other
    factors.
  sec: 676
  time: '11:16'
  who: Nikita
- header: Production guardrails and multi-layered system defense
- line: How about guardrails?
  sec: 685
  time: '11:25'
  who: Alexey
- line: This is a very good point. For many of the solutions we are building, guardrails
    are part of them. For guardrails, you usually use smaller classifier models.
  sec: 694
  time: '11:34'
  who: Nikita
- line: They do not need to be generative models. They can be models fine-tuned to
    detect certain things like violence, prompt attacks, or something along these
    lines. We usually use something like this as part of our pipelines to make sure
    that this small classifier filters out certain user questions before they even
    reach the generative model.
  sec: 700
  time: '11:40'
  who: Nikita
- line: Do you have some sort of framework that you use, or is it just one of the
    building blocks you reuse from your portfolio of building blocks?
  sec: 730
  time: '12:10'
  who: Alexey
- line: It is one of the building blocks on AWS. On AWS we have a service called Amazon
    Bedrock, which basically serves as a service that gives access to many foundation
    models that you can use via AWS, like Claude from Anthropic and models from OpenAI.
  sec: 739
  time: '12:19'
  who: Nikita
- line: As part of this block, we have a managed service called Bedrock Guardrails
    where you can basically just tick a couple of boxes and set up a guardrail to
    filter out certain things or hide PII data, which is personally identifiable information,
    before it reaches the model. This can be used as a managed service.
  sec: 762
  time: '12:42'
  who: Nikita
- line: What I can say from practice is that just setting up a guardrail, whether
    it is a Bedrock guardrail or something else, is usually not enough. You usually
    need to have multiple layers of defense.
  sec: 782
  time: '13:02'
  who: Nikita
- line: For example, you can add specifically allowed topics in your prompt templates.
    Then you set up a guardrail, and then potentially set up some observability to
    make sure that once things are not filtered out, you can catch that and work on
    filtering it out, because there will be a point when something is not filtered
    out.
  sec: 791
  time: '13:11'
  who: Nikita
- line: The funny thing is, as we speak about this, I see a question in the Q&A. Can
    Nikita talk more about guardrails? I will ask you one more thing about them before
    we move on.
  sec: 813
  time: '13:33'
  who: Alexey
- line: Recently, I had a workshop about guardrails and one of the participants asked
    me what the point of having these guards is if we can just include the allowed
    topics in our system prompt. Why do we need to bother?
  sec: 827
  time: '13:47'
  who: Alexey
- line: If we just have our instructions and the instructions to the agent, we can
    say these topics are allowed and these topics are not allowed. I assume with modern
    models, they will be able to detect these topics fine. Why do we need to bother
    with all these guardrails, and why would we need multiple levels of defense?
  sec: 835
  time: '13:55'
  who: Alexey
- line: This is a very good question, and this is something we think about a lot when
    building our solutions. There are multiple answers to this. First of all, including
    something like this in a prompt is very useful, and it is better than not doing
    it. I highly recommend everyone think about prompt templates and consider what
    kind of attacks or topics you care about, and set them up in the prompt so that
    the agent or the LLM knows it should not answer certain things.
  sec: 860
  time: '14:20'
  who: Nikita
- line: What we see in practice is that no matter how well you phrase that in the
    prompt, there are always ways to work around it. With the previous generations
    of models, you could just say that your grandmother is telling you a story that
    helps you fall asleep, but to tell the story, you need to do this and that, and
    then the model would work with it. With more modern models, it becomes more difficult,
    but there are still a lot of patterns of attacks.
  sec: 902
  time: '15:02'
  who: Nikita
- line: One of the patterns is when you start doing it not in the English language,
    but in some language that is not so widespread in the model's training data. Many
    of these guardrails start working much less reliably when you do it in a foreign
    language, or when you translate it to bytes or to some weird code.
  sec: 927
  time: '15:27'
  who: Nikita
- line: We have seen use cases where people left comments in code blocks, and in those
    comments, there were malicious instructions. Sometimes you can upload a file into
    your agent and say, "This is a book I want you to summarize," and as part of that
    book, there are some instructions hidden at some point. There are more and more
    elaborate ways to make the agent believe that this is not a malicious instruction,
    but a genuine thing it needs to do.
  sec: 952
  time: '15:52'
  who: Nikita
- header: Prompt bypasses, input attacks, and AI red teaming
- line: Adding guardrails in the prompt is usually not enough. What we want to do
    to just increase our layers of defense is to have a separate mechanism, like a
    separate block that is not dependent on the language model.
  sec: 975
  time: '16:15'
  who: Nikita
- line: One of the reasons we want to have it separate is because then it does not
    matter which model we are using. Maybe tomorrow there is a new open-source model
    from Qwen that actually outperforms our previous base model, so we want to switch
    to that.
  sec: 991
  time: '16:31'
  who: Nikita
- line: Maybe this new open-source model has higher chances of not following allowed
    topics, and it has completely different tuning and alignment regarding what kind
    of topics are good to talk about and what kind of topics should not be mentioned.
    That is why we want to have this block as a separate component, so that we make
    it completely independent of the model we are using.
  sec: 1006
  time: '16:46'
  who: Nikita
- line: As part of this block, one of the most common patterns I see is that we set
    up a fleet of different classifiers, usually zero-shot classifiers, that basically
    take input from the user. Let us say a user asks how to create a bomb or something
    like this. There will be certain labels that those classifiers are assigning to
    that user input.
  sec: 1029
  time: '17:09'
  who: Nikita
- line: They check whether it is a prompt attack, whether it is a violent topic, or
    whether the language is harmful. You can think about multiple dimensions, and
    they will be different for each usecase.
  sec: 1054
  time: '17:34'
  who: Nikita
- line: Sometimes it is evident that we do not want violence to be there, but if we
    are building a chatbot for company A, we probably do not want this chatbot to
    talk about company B. This will be specific to a particular usecase. We can basically
    filter it out and have a placeholder answer instead of sending this user question
    to the model.
  sec: 1070
  time: '17:50'
  who: Nikita
- line: We either send a placeholder back to the user saying this is not an allowed
    topic, or we somehow rephrase or hide certain things from the user question before
    we send it to the LLM.
  sec: 1093
  time: '18:13'
  who: Nikita
- line: Is it usually sequential? Do you run a bunch of classifiers before you send
    the request to the main model, or does it depend?
  sec: 1103
  time: '18:23'
  who: Alexey
- line: Exactly. Those classifiers can run in parallel. Maybe there are 10 classifiers
    that check 10 different things, so it takes like 100 milliseconds or 50 milliseconds,
    which is usually not a problem.
  sec: 1113
  time: '18:33'
  who: Nikita
- line: Yeah, they should be very small models that you could fine-tune on the corresponding
    data.
  sec: 1124
  time: '18:44'
  who: Alexey
- line: I think what people do now is they overload the LLM with a lot of text, and
    at a high number of tokens, it starts breaking. I do not know if it is still working
    with new models, but this is the pattern I saw maybe half a year ago.
  sec: 1182
  time: '19:42'
  who: Alexey
- line: Yes, this is popular as well. When we want to address this, we do something
    that is called red teaming. If you have not heard of red teaming, it basically
    refers to methods to stress test your system before you deploy it to production.
    You can either have a human team that tries to break your solution, or you can
    also have a team of LLM agents that try to break it, and then you can see the
    statistics.
  sec: 1199
  time: '19:59'
  who: Nikita
- line: Out of 20 different stress scenarios, maybe your system only passes five or
    six, and then it means that you need to work on these guardrails and security.
  sec: 1222
  time: '20:22'
  who: Nikita
- line: I guess for some cases, you do not even need an LLM. If you see that the user
    is sending you a huge prompt, you can just say this prompt is too huge, right?
  sec: 1235
  time: '20:35'
  who: Alexey
- line: Yes, let us ask the user to make it shorter.
  sec: 1245
  time: '20:45'
  who: Nikita
- header: Newsletter localization and translation with Zalando
- line: I see a question asking if Nikita could give a few examples of his GenAI business
    projects. I know that you did include them in the notes that we prepared, even
    though we do not have questions right now about this. I know you have a list of
    these things, and maybe it would be interesting for us now to go through this
    list. From what you can share, what kind of projects did you do? Maybe we should
    not go three years back, but we can talk about some of the projects that you find
    very interesting.
  sec: 1249
  time: '20:49'
  who: Alexey
- line: For sure. The first thing I should say is that there are some projects I can
    talk about and some projects I cannot talk about due to NDAs. I will only cover
    the projects that are referenced publicly as well.
  sec: 1284
  time: '21:24'
  who: Nikita
- line: The first one I could mention is the project that we were working on in collaboration
    with Zalando, where the topic was newsletter translation and localization. Zalando
    is a big online e-commerce retail store that basically sells a lot of fashion
    items, accessories, clothes, shoes, bags, hats, and things like that.
  sec: 1300
  time: '21:40'
  who: Nikita
- line: One of the divisions inside Zalando is Lounge by Zalando, and this is the
    kind of store where you can get your items on discount. You can go there, check
    what the current discounts are, and buy many different things.
  sec: 1325
  time: '22:05'
  who: Nikita
- line: This division sends out newsletters to the end customers saying which items
    are on sale each week.
  sec: 1348
  time: '22:28'
  who: Nikita
- line: Is it personalized?
  sec: 1364
  time: '22:44'
  who: Alexey
- line: Yes, exactly. Personalization is something that we were working on here as
    well. Imagine that we have a new marketing campaign where we are selling hundreds
    of items, and there are certain newsletters and push notifications that our users
    will be getting to learn about the most relevant sales for them.
  sec: 1364
  time: '22:44'
  who: Nikita
- line: Zalando actually works in many European countries that have different languages,
    such as Germany, France, and Poland. Each of these countries has different languages,
    so you need to translate your newsletters and notifications to different languages.
  sec: 1398
  time: '23:18'
  who: Nikita
- line: It is not as easy as just translation because there are many nuances in different
    markets that you need to take care of. For example, in certain countries, Zalando
    has a different legal name that you have to use.
  sec: 1415
  time: '23:35'
  who: Nikita
- line: Did you know that in France, there is a word for "sale" that can only be used
    for specific sales during the season? I think it applies to the New Year's sale,
    the Christmas sale, and some summer sales. In the other months of the year, you
    cannot use that term anymore; you have to use a different term that means "sales."
  sec: 1431
  time: '23:51'
  who: Nikita
- line: If you just use something like Google Translate, it will not have context,
    will it? That is why we use these models.
  sec: 1456
  time: '24:16'
  who: Alexey
- line: Exactly, that is the problem. They do not know that we need to change the
    name of the Zalando legal entity. They do not know that we need to change the
    term we use for "sale." They do not know the guidelines of how we approach the
    audience in different countries.
  sec: 1464
  time: '24:24'
  who: Nikita
- line: For example, in Germany, there are different ways of saying "you." There is
    the formal "Sie" and the informal "du." In one country we may have a guideline
    stating that we should address our customers formally, and in another country
    it works better if we address our audience with informal language. What we definitely
    do not want is that every time we translate it, we get it randomly, making it
    inconsistent.
  sec: 1479
  time: '24:39'
  who: Nikita
- line: When we are talking about push notifications, we also want our text in the
    banners to be visible and compact enough, so we have a certain character limit.
    If our translation exceeds this limit, we want to squeeze it, maybe without losing
    the meaning, but by using different wording to make sure it still appears as part
    of the notification banner that pops up.
  sec: 1512
  time: '25:12'
  who: Nikita
- line: There are many nuances like this, starting from the language itself and going
    all the way back to which wording is used where, and how you write currency. Do
    you put euros at the end of the word or at the beginning of the word, and things
    like that?
  sec: 1535
  time: '25:35'
  who: Nikita
- line: A better word is not "to translate" but "to localize" because we also have
    these branding guidelines that span multiple pages and contain detailed instructions
    on how people in this particular country should be addressed.
  sec: 1551
  time: '25:51'
  who: Nikita
- line: For this, we were building a GenAI pipeline that was taking the English version
    as the base copy, and then translating it to all the European languages that Zalando
    sells items in. We ran a couple of iterations to evaluate the translation quality,
    tweak the translation, and improve things here and there. Then we made these translations
    available so that they could be sent to the audiences in different countries.
  sec: 1568
  time: '26:08'
  who: Nikita
- line: I like this project because it does not involve RAG and it does not involve
    agents, but it still solves a business problem. Sometimes when people ask me for
    project ideas that involve agents and RAG, I tell them that if you find an idea
    that solves your particular problem, it does not have to be super involved. This
    is a good example where you do not need anything fancy, but there is a very clear
    business problem that this project is solving.
  sec: 1600
  time: '26:40'
  who: Alexey
- header: Evaluation frameworks and human-in-the-loop metrics
- line: You described this, but this is not enough, is it? You need to make sure that
    the system actually works, and you probably had some sort of evaluation frameworks
    to handle that. Can you talk more about this?
  sec: 1644
  time: '27:24'
  who: Alexey
- line: Yes, of course. Evaluation is very important, and what we used here was an
    evaluation score sheet with different dimensions. I won't be able to name all
    the dimensions now, but it covers things like whether the spelling is correct,
    whether the translation is accurate, and whether the language flow is natural.
  sec: 1661
  time: '27:41'
  who: Nikita
- line: You can come up with dimensions like that and score them on different levels,
    let us say between zero and 10. While we were developing our pipeline, we had
    actual human experts who were speakers of those languages and people familiar
    with the branding and marketing guidelines score our translations. We were then
    able to count the number of issues in different dimensions and quantify them with
    a couple of metrics that tell you whether the translation is good or not.
  sec: 1685
  time: '28:05'
  who: Nikita
- line: This was super important to do because to iterate on the system, you need
    to have some metrics. This is a reoccurring topic we see in many projects. One
    of the very first things we try to do is to actually build some kind of evaluation.
    Even if your system is just producing some kind of placeholder text for now, it
    is fine.
  sec: 1721
  time: '28:41'
  who: Nikita
- line: Let us first design an evaluation because we cannot optimize something if
    we do not know the metrics. We started with human experts scoring our solution,
    and this served as a golden standard for us.
  sec: 1741
  time: '29:01'
  who: Nikita
- line: Using human experts is expensive in the sense that you cannot ask them to
    evaluate every single change you make to your prompt or to your system in general.
    That is why we also used LLM-as-a-judge evaluation.
  sec: 1756
  time: '29:16'
  who: Nikita
- line: We reused the same score sheets and guidelines, but this time we used a separate,
    independent LLM to score the translations and evaluate the quality over a batch
    of outputs in the test sample. We were then able to use those metrics to iterate
    on the solution as well.
  sec: 1772
  time: '29:32'
  who: Nikita
- line: 'This is what we do in most of the projects: we use LLM-as-a-judge for fast
    iterations, and then we use human experts for a golden evaluation of the major
    version changes in your solution.'
  sec: 1795
  time: '29:55'
  who: Nikita
- line: Do I understand correctly that when you want to start a project, even before
    you start implementing, you might have some placeholders and come up with this
    evaluation framework? Once you start working on the project, you involve human
    experts to evaluate the output, collect the data, and build this gold standard
    dataset.
  sec: 1813
  time: '30:13'
  who: Alexey
- line: Then you take this output from humans and train the LLM in such a way that
    it can repeat what humans do on scale. Is this what you do? You still do not remove
    humans from the loop completely; they are still involved in some major milestones.
  sec: 1839
  time: '30:39'
  who: Alexey
- line: Yes, they are definitely still involved because in many cases, you need subject
    matter experts. When I look at a certain translation, I would never know that
    a certain terminology needs to be used in this country. I would just double-check
    my translation with DeepL or some other online service, see that it looks legit,
    but I wouldn't know all these details.
  sec: 1861
  time: '31:01'
  who: Nikita
- line: There are examples where everything looks great to me, but when I show it
    to a subject matter expert, they point out specific corrections. For that, you
    need human experts to evaluate and judge your system.
  sec: 1885
  time: '31:25'
  who: Nikita
- line: Is it the case that we can have 100% alignment, where our judges repeat what
    humans do?
  sec: 1902
  time: '31:42'
  who: Alexey
- line: Sorry, I think I had a small break. Could you please repeat the question?
  sec: 1930
  time: '32:10'
  who: Nikita
- line: I am sorry, the internet in my entire house is bad and we are waiting for
    a technician. I hope the technician comes soon. I will try to repeat the question.
  sec: 1937
  time: '32:17'
  who: Alexey
- line: Humans generate evaluation data, and then we take an LLM and try to repeat
    what humans did with a judge. We call this alignment because we want to align
    the output of the LLM with the output that humans produce. Is it possible to achieve
    100% alignment so that the judges can fully mimic what humans can do, or is it
    not possible to achieve 100%, and maybe we do not even need that?
  sec: 1946
  time: '32:26'
  who: Alexey
- header: Aligning LLM-as-a-judge with few-shot prompts
- line: I think 100% is never possible. You will always have deviations because there
    are so many edge cases that you cannot think of upfront. You can do a great deal
    of aligning and move towards this 100%.
  sec: 1987
  time: '33:07'
  who: Nikita
- line: When we build LLM systems, we usually find that including few-shot examples
    is something that always helps us. It is the same with the LLM judges.
  sec: 2003
  time: '33:23'
  who: Nikita
- line: When we build LLM-as-a-judge frameworks, one of the best ways to make these
    judges more in line with what we expect is to include a few-shot examples of human
    judges judging the output. Depending on the volume of the data, we can also think
    about fine-tuning a specific model.
  sec: 2016
  time: '33:36'
  who: Nikita
- line: In many cases, we can just work on the prompting and examples to make sure
    that what we want the judge to do is reflected in the actual judge behavior. In
    one of the recent engagements, I remember that my LLM-as-a-judge model had almost
    50 examples showing how different human judges judge the output.
  sec: 2039
  time: '33:59'
  who: Nikita
- line: You can include this as part of the system prompt that is cached, so you do
    not need to pay too much for it when you repeatedly run this LLM-as-a-judge. This
    highlights that in order to align the judge with what you expect to see as a human,
    you may need a lot of examples.
  sec: 2068
  time: '34:28'
  who: Nikita
- header: Fine-tuning small language models versus prompting
- line: You mentioned fine-tuning a small model. How often do you need to do this?
    How often is fine-tuning involved, whether for judges, guardrails, or the main
    model?
  sec: 2089
  time: '34:49'
  who: Alexey
- line: This is definitely something that we see frequently, but in many cases in
    practice, setting up the agent, the prompt, and the few-shot examples will get
    you to the accuracy level you need without fine-tuning. To get an additional boost
    on top of that, you sometimes need to consider fine-tuning as well.
  sec: 2107
  time: '35:07'
  who: Nikita
- line: 'There are two main reasons for fine-tuning: either to push your accuracy
    even more to get even higher, or you want to fine-tune when the cost and latency
    considerations are such that it is better to have a small model that you can deploy
    yourself. You can fine-tune and try to replace a bigger model with a smaller model
    that is doing well specifically in the dimension that you need it for.'
  sec: 2129
  time: '35:29'
  who: Nikita
- line: Usually, this would not be the case for things like chatbots because you need
    generic behavior for them. Maybe you are fine-tuning a model for something specific,
    like entity extraction from a certain document, and if you know your documents
    are coming from the same kind of domain, it makes a lot of sense to fine-tune.
  sec: 2167
  time: '36:07'
  who: Nikita
- line: In some engagements, we basically take different models. Sometimes it can
    be our own models developed by Amazon, such as the Amazon Nova family of foundation
    models, or sometimes we work with open-source models like Qwen, Llama, or some
    of the others that can be fine-tuned for a specific task.
  sec: 2192
  time: '36:32'
  who: Nikita
- line: The main requirement with fine-tuning is data availability because you need
    a lot of data if you really want to get good accuracy with fine-tuning. The biggest
    problem to solve if you want to try fine-tuning is how to get good quality data.
  sec: 2215
  time: '36:55'
  who: Nikita
- line: How much data are we talking about? It is different based on the usecase,
    but let us consider entity recognition in English.
  sec: 2234
  time: '37:14'
  who: Alexey
- line: Most models can do English and entity recognition out of the box quite well,
    but when you start fine-tuning it, let us say we are talking about a couple of
    thousand examples to take the accuracy to the next level.
  sec: 2242
  time: '37:22'
  who: Nikita
- line: A couple of thousand does not seem like a lot. You can even take a frontier
    model to generate these examples and then review them, can you?
  sec: 2258
  time: '37:38'
  who: Alexey
- line: Yes, and there is a lot of work on synthetic data generation, but sometimes
    what you get with synthetic data is generic, so it does not really help with fine-tuning.
    What if our task is entity extraction from contracts in German?
  sec: 2271
  time: '37:51'
  who: Nikita
- line: Let us say we are taking rental contracts and we are extracting things like
    the expiration date, the rent amount, the times of the day when we can make noise,
    and whether we can barbecue on our balcony or not. Probably half of those things
    will be extracted automatically just fine by any of the recent models.
  sec: 2287
  time: '38:07'
  who: Nikita
- line: It may start having problems with specific nuances that are typical for German
    rental contracts. If you just go to ChatGPT or Claude and ask them to generate
    German contracts, they may not be specific enough. If you generate 10,000 of these
    contracts and fine-tune your model on them, you might not get a boost.
  sec: 2316
  time: '38:36'
  who: Nikita
- line: If you have real-world contracts, getting a couple of thousand contracts might
    be a challenge because you do not only need the contracts, you also need actual
    labels. Someone must have already extracted those entities from those contracts
    and completed this exercise.
  sec: 2338
  time: '38:58'
  who: Nikita
- line: Still, I thought the number would be one or two orders of magnitude higher,
    like 10,000 instead of 1,000. This is what I thought.
  sec: 2357
  time: '39:17'
  who: Alexey
- line: The more, the better. If you tell me that you only have hundreds, then I personally
    will have doubts that fine-tuning will work. If you have a couple of thousands,
    then it is a good starting point. When you have real data, generating synthetic
    data on top of the real data becomes much easier because you can use this real
    data as seeds to guide your data generator.
  sec: 2365
  time: '39:25'
  who: Nikita
- line: How expensive is it to take a small model and fine-tune it?
  sec: 2396
  time: '39:56'
  who: Alexey
- line: Usually it is not. It depends on the kind of model, but if we are talking
    about models below 9 billion parameters, they usually fit on a single GPU, like
    Qwen 9B.
  sec: 2401
  time: '40:01'
  who: Nikita
- line: You can fit it on a single machine, such as a G6.xlarge or G5.xlarge on AWS,
    depending on which generation you want to use. I think the cost of it is below
    $2 per hour.
  sec: 2417
  time: '40:17'
  who: Nikita
- line: For the fine-tuning itself, we usually do not do a full fine-tuning or a full-weight
    fine-tuning, but rather one of the parameter-efficient variants like LoRA and
    QLoRA. It will probably take a couple of hours. Basically, for 10 bucks, you can
    probably fine-tune one or two model variants.
  sec: 2432
  time: '40:32'
  who: Nikita
- line: That is reasonable because I remember there were times when it was actually
    not that cheap to do this kind of stuff.
  sec: 2456
  time: '40:56'
  who: Alexey
- line: A couple of years ago, smaller models were much less capable, and now the
    gap between small and big models is still there, but small models have become
    much better.
  sec: 2464
  time: '41:04'
  who: Nikita
- header: Complementary mechanics of RAG and fine-tuning
- line: What is your opinion on RAG versus fine-tuning? Now that it is cheaper and
    more available, do we still need to fine-tune, or is RAG still the way?
  sec: 2478
  time: '41:18'
  who: Alexey
- line: In my mind, it is not a competition. They are two complementary workflows,
    and sometimes you need both.
  sec: 2491
  time: '41:31'
  who: Nikita
- line: If you think about fine-tuning for the purposes of answering questions about
    company-specific knowledge, the big problem is that every time you have a new
    document with new information, you have to run your fine-tuning again because
    this new information will not make it into the training data.
  sec: 2500
  time: '41:40'
  who: Nikita
- line: You can fine-tune the model to make it more expert in a specific domain, such
    as the finance domain, by fine-tuning it on a big corpus of data. We still need
    RAG to be able to check the most recent documents and double-check all the information
    from the actual relevant data sources.
  sec: 2523
  time: '42:03'
  who: Nikita
- line: I always think about fine-tuning as a student passing an exam. If I work on
    fine-tuning, it basically means that I memorized more things when I was preparing
    for the exam. If the professor says that I can still take a sneak peek into my
    textbook when answering the question, I will probably still do that in many cases
    because even though I memorized many things, I want to know the exact thing from
    a particular portion of the book.
  sec: 2546
  time: '42:26'
  who: Nikita
- header: Agentic web search tools for anomaly explanation
- line: I like this analogy. We were talking about the projects you worked on, and
    I interrupted you to ask some other things, but we can continue and you can mention
    a few other projects. I also see that we do not have a lot of time, only 15 minutes
    left, and we have some other questions. You can briefly talk about these projects,
    and if something is interesting, we can do a little deep dive into them.
  sec: 2580
  time: '43:00'
  who: Alexey
- line: I can just mention a couple. One of the other projects we were doing was with
    a company called Windward, which focuses on maritime data analytics. Maritime
    means everything connected to the world's seas and oceans, which is a very relevant
    topic these days.
  sec: 2606
  time: '43:26'
  who: Nikita
- line: They look at vessel movements in different areas of the sea and track data
    to notice different anomalies. For example, in this area of the world, there is
    an unusual spike in the number of ships doing something or moving in a certain
    direction.
  sec: 2628
  time: '43:48'
  who: Nikita
- line: In the previous version, they were able to notice these anomalies, but what
    was missing was the explanation of why. We suddenly see more than 20 boats standing
    next to a certain strait in the sea, so why is it happening?
  sec: 2653
  time: '44:13'
  who: Nikita
- line: We were working together on building a solution that performs a web search
    over different sources, connects to a couple of APIs to download different assets,
    downloads weather forecasts, and downloads news and different materials describing
    events in different areas of the world to try to contextualize and explain why
    a certain event is happening.
  sec: 2669
  time: '44:29'
  who: Nikita
- line: Maybe a certain country is doing military exercises, so this path is blocked
    for two days, and this is why there are many ships doing this. Maybe there is
    shadow activity by oil tankers happening in a particular part of the world when
    a new round of sanctions is imposed, and things like that.
  sec: 2695
  time: '44:55'
  who: Nikita
- line: I assume this is an agentic solution. You do not just dump a bunch of data
    at the LLM for it to figure it out, but it needs to actively explore things.
  sec: 2722
  time: '45:22'
  who: Alexey
- line: Yes. Your solution needs to have connections to a couple of tools where it
    can get information from, and you need to give it the flexibility to query a different
    set of tools before it is satisfied with the amount of information and can formulate
    the explanation summary.
  sec: 2733
  time: '45:33'
  who: Nikita
- line: That is really cool. When you mentioned that you needed to analyze vessel
    movement, I wondered why you would use an LLM, and now I understand. There is
    some other anomaly detection system that flags an anomaly saying, "Look, in this
    area there are many ships, let us figure out why." This is another good example
    of merging classical ML that detects the anomaly and generative AI that explains
    the anomaly.
  sec: 2751
  time: '45:51'
  who: Alexey
- line: Yes, and you need this solution because, depending on what is happening, many
    companies have businesses that depend on it. Maybe my boats will be carrying certain
    shipments in this area, and they need to know if this is just a one-day thing
    or if this is something I should plan around.
  sec: 2784
  time: '46:24'
  who: Nikita
- line: Maybe I sell fuel to the transport companies, so if I see that there are many
    ships here and I know they will be here for a while, maybe I will move my fuel
    closer so that they can buy fuel from me in that area.
  sec: 2800
  time: '46:40'
  who: Nikita
- header: Automated text generation from real-time sports sensors
- line: Any other interesting projects?
  sec: 2821
  time: '47:01'
  who: Alexey
- line: One of the cool projects was when we were building an AI live ticker for football
    games. Imagine that you are following a football game on your phone or on your
    tablet because you cannot actually watch the match.
  sec: 2825
  time: '47:05'
  who: Nikita
- line: You probably saw those tickers where they say Lewandowski makes a shot and
    the score is now 1-0, or there is a free kick, or there is a yellow card. Usually,
    it is either automated without much emotion and context, presenting just a list
    of events, or you need to have people who actually watch the game and write rich
    messages about what is happening on the field.
  sec: 2842
  time: '47:22'
  who: Nikita
- line: You need humans to stay there, watch the game, and print this live in the
    chat. What we were working on together with our partner company is building a
    solution that takes the sensor data from the game.
  sec: 2874
  time: '47:54'
  who: Nikita
- line: The sensor data tells you that player ID 173 had the ball, and then it was
    moved to player ID 325 in an area of the field specified by XY coordinates. It
    is a statistics-heavy kind of language coming from these sensors.
  sec: 2889
  time: '48:09'
  who: Nikita
- line: We were using LLMs to create an actual description of what is happening out
    of it because we can map the players to the IDs, and we can understand what part
    of the pitch it is. Is it far from the goal, or is it not far from the goal? Then
    we can put additional emotion on that in the context of what the score is and
    what is happening in the game.
  sec: 2913
  time: '48:33'
  who: Nikita
- line: Each ball used in football is actually sensored, so there is a sensor in the
    ball?
  sec: 2941
  time: '49:01'
  who: Alexey
- line: It depends on the league, but most leagues have comprehensive solutions for
    collecting the data.
  sec: 2945
  time: '49:05'
  who: Nikita
- line: If I am watching a match, I need to know that it is not a simple football
    there, is it? It is probably augmented.
  sec: 2951
  time: '49:11'
  who: Alexey
- line: Especially if you watch the German Bundesliga, AWS has a partnership with
    them, so there are a lot of smart statistics being calculated in the backend.
  sec: 2962
  time: '49:22'
  who: Nikita
- header: AWS project scoping and proof of concept timelines
- line: Is this project already deployed, and do people already use it?
  sec: 2998
  time: '49:58'
  who: Alexey
- line: Somewhere on my laptop, I have a big document that lists all the projects
    I worked on, and it is dozens after four years at Amazon. Usually, when we do
    a project, it lasts between one and three months, depending on the complexity,
    because we usually work on it during the first proof of concept stage.
  sec: 3014
  time: '50:14'
  who: Nikita
- line: That means we need to demonstrate that it works on the customer data and in
    the customer environment, but we are not counting the further integration work
    that happens after the first proof of concept.
  sec: 3043
  time: '50:43'
  who: Nikita
- line: In my day-to-day job, there are cases where we have multiple projects at the
    same time, but they can be at different stages. We can be scoping one project,
    meaning that we are just figuring out the usecase and trying to understand what
    we will be working on, while another project involves hands-on active work that
    I am doing at the moment. You usually do not have too many of them in parallel.
  sec: 3059
  time: '50:59'
  who: Nikita
- line: After scoping, how often does it happen that you conclude that an LLM is not
    the right solution, and you think either a different team should take it or the
    customer should think about a different problem?
  sec: 3081
  time: '51:21'
  who: Alexey
- line: I wouldn't be able to tell you the exact ratio, but this happens quite frequently,
    and this is actually good. We usually start from the business usecase; we do not
    think about whether an LLM, AI, or ML will solve this.
  sec: 3106
  time: '51:46'
  who: Nikita
- line: We start asking the customer about their main pain points, and they list problem
    X, problem Y, and problem Z. Then we start looking at those problems and trying
    to understand if we can approach them with ML or with GenAI.
  sec: 3122
  time: '52:02'
  who: Nikita
- line: My personal opinion is that you should always pick the simplest tool possible
    to address a usecase before you proceed with building a multi-agent solution that
    does something that could be solved with logistic regression or even with a business
    heuristic. This was previously a problem with traditional ML, where many people
    were jumping to ML before trying very simple versions, like always predicting
    the average, which will get you halfway there.
  sec: 3139
  time: '52:19'
  who: Nikita
- line: Is it from the Rules of Machine Learning from Google? Do you remember this
    document?
  sec: 3171
  time: '52:51'
  who: Alexey
- line: I think so, yes. I do remember it.
  sec: 3174
  time: '52:54'
  who: Nikita
- line: The first rule is to start without machine learning, or something like that.
  sec: 3177
  time: '52:57'
  who: Alexey
- line: Yes, exactly. Nowadays, it is even more tempting to build an agentic solution
    that tries to solve a multi-agent problem.
  sec: 3180
  time: '53:00'
  who: Nikita
- line: There are also a couple of good blog posts from Anthropic about this. I can
    look them up later and we can add them to the video. It is about agents where
    they say you do not need agents, you need a workflow. Is that the one you are
    talking about?
  sec: 3191
  time: '53:11'
  who: Alexey
- line: Yes, this one.
  sec: 3206
  time: '53:26'
  who: Nikita
- line: For you, the motivation to scope it properly is that you want your POC to
    actually be deployed and put into production, not parked. That is why you suggest
    what they should do instead, so after you hand it over, they find it very useful
    and actually deploy it. Then they continue paying AWS for their infrastructure,
    don't they?
  sec: 3209
  time: '53:29'
  who: Alexey
- line: Yes. Making sure that the project ends up in production is our main goal,
    because if we build something, we want it to be useful and to actually solve the
    problem that our customers have. We are very interested in scoping out a usecase
    very specifically, and we have a whole team whose main job is to scope these usecases
    and understand the business value behind them.
  sec: 3238
  time: '53:58'
  who: Nikita
- line: Do you also take part in these meetings?
  sec: 3263
  time: '54:23'
  who: Alexey
- line: I take part in these meetings, but we have dedicated roles in our team for
    people who mostly do the scoping and people who mostly do the hands-on work, like
    product manager-oriented roles. We call them AI strategists, so that is what you
    would look for if anyone watching is looking for job positions. An AI strategist
    in the GenAI Innovation Center is the person who is mainly responsible for scoping
    and talking to customers.
  sec: 3263
  time: '54:23'
  who: Nikita
- header: Interview requirements and career skills for AWS roles
- line: Since you mentioned your job openings, are you hiring right now?
  sec: 3298
  time: '54:58'
  who: Alexey
- line: If somebody is really interested in what you do, and in a couple of months
    there is an open position and they apply, what kind of background and skills should
    they have to confidently say, "I want to apply and I know I will pass"? What exactly
    do you look for in people?
  sec: 3316
  time: '55:16'
  who: Alexey
- line: In our team, we mainly look for people who first of all have good breadth
    because we have different kinds of usecases. Sometimes we are building chatbots,
    sometimes we are fine-tuning models, and sometimes we are developing an agentic
    system, so you have to have a good breadth of experience with different GenAI
    applications.
  sec: 3340
  time: '55:40'
  who: Nikita
- line: The second thing is that you should have experience with customer communication.
    One of the big distinctions with our team compared to some other science teams
    you may face is that we talk directly to customers.
  sec: 3364
  time: '56:04'
  who: Nikita
- line: Every week I have multiple customer meetings where I have to talk to technical
    but also non-technical people. Some usually want to see the business side of things,
    and others want to see the technical side.
  sec: 3378
  time: '56:18'
  who: Nikita
- line: I need to be able to communicate with different kinds of audiences and communicate
    what we improved in our system this week, why this is important, how we measure
    this, and what it will lead to in business terms. Those two things, customer communication
    and breadth of GenAI usecases and applications, are crucial for our team.
  sec: 3395
  time: '56:35'
  who: Nikita
- line: Apart from that, if you start looking online for Amazon interview processes,
    you will find many materials about behavioral interviews and coding interviews
    that are standard across many Amazon teams.
  sec: 3426
  time: '57:06'
  who: Nikita
- line: If somebody applies for an applied scientist position, what is the title?
    Is it applied scientist or data scientist?
  sec: 3442
  time: '57:22'
  who: Alexey
- line: We have both applied scientists and data scientists.
  sec: 3448
  time: '57:28'
  who: Nikita
- line: You still need to do these LeetCode kind of problems, right?
  sec: 3452
  time: '57:32'
  who: Alexey
- line: Of course, there are still coding capabilities that we need to assess.
  sec: 3458
  time: '57:38'
  who: Nikita
- line: Do you allow people to use AI?
  sec: 3466
  time: '57:46'
  who: Alexey
- line: At the moment, it is more traditional, so we will see how you will be coding
    without AI.
  sec: 3466
  time: '57:46'
  who: Nikita
- line: Do you have a few more minutes?
  sec: 3474
  time: '57:54'
  who: Alexey
- line: Of course, yes, no problem.
  sec: 3474
  time: '57:54'
  who: Nikita
- header: Enterprise architecture patterns and system observability
- line: There is a very interesting question, and I thought maybe we can cover this
    before we stop. What kind of architectural patterns do you see repeatedly across
    successful AI deployments?
  sec: 3479
  time: '57:59'
  who: Alexey
- line: That is an interesting question. The main point is that usually GenAI is a
    very small part of the architecture, but there are many things around it.
  sec: 3493
  time: '58:13'
  who: Nikita
- line: If this is a document-based solution, you need to think about where you store
    your documents, so you need a vector store. For example, at AWS, you use things
    like OpenSearch or Knowledge Bases.
  sec: 3499
  time: '58:19'
  who: Nikita
- line: If you are thinking about chatbot solutions, you need to have a frontend and
    a couple of services that basically serve your frontend, allow you to connect
    your business logic, and deliver to the actual user. The recurrent thing that
    I see is that there is a GenAI component as a Lego block as part of the architecture,
    but then there are many things around it for frontend serving, backend serving,
    and making sure that you can observe and monitor the logs from the system.
  sec: 3515
  time: '58:35'
  who: Nikita
- line: One of the most important things to talk about when we build GenAI architectures
    is observability and logs. How do you monitor? Especially if you have agentic
    solutions that run different tools, where do you deploy these tools?
  sec: 3555
  time: '59:15'
  who: Nikita
- line: If you work with AWS, you would deploy them somewhere like Lambda functions,
    so you need to have logs over the Lambda functions. If the tool is a calculator,
    how does it do the calculations, and are there any errors?
  sec: 3570
  time: '59:30'
  who: Nikita
- line: Monitoring and observability is something that you need to take care of, and
    you need to make sure that every step in your agentic pipeline has a certain service
    attached to it for logging. The second thing is how do you retry and fix things
    if you have an error somewhere on the execution path?
  sec: 3587
  time: '59:47'
  who: Nikita
- line: Yes, exactly. When you invoke LLMs, you may have throttling errors because
    all the servers are busy, so you need to have a certain logic to do retries and
    exponential backoff, for example, to send your question again. If your pipeline
    fails somewhere in the middle, such as after the sixth question from the user,
    you need to be able to retrieve the memory of the session and basically continue
    from where you left off. For this, you can use different components in the architecture.
  sec: 3604
  time: '1:00:04'
  who: Alexey
- header: Reusable infrastructure blocks on Amazon Bedrock
- line: How reusable are the components that you use, or are there always things that
    you have to adjust for every customer?
  sec: 3642
  time: '1:00:42'
  who: Alexey
- line: There are always things you have to adjust. I have not seen a single engagement
    where you can just take an out-of-the-box solution and make it work without any
    customization.
  sec: 3651
  time: '1:00:51'
  who: Nikita
- line: At AWS, we have a good set of building blocks on Amazon Bedrock Agent, which
    is a service you can check out. It provides components like memory and agent runtime,
    and it basically provides the opportunity to deploy the agent, versionize the
    agent, and handle similar tasks that can solve many of the problems when you are
    building a large architecture. Still, there is a lot of customization involved.
  sec: 3659
  time: '1:00:59'
  who: Nikita
- line: You have these building Lego blocks, but they do not necessarily fit together
    out of the box, so you need something to connect them. This is the custom work
    that is required for the customers.
  sec: 3692
  time: '1:01:32'
  who: Alexey
- line: Yes, and this field is developing very quickly. A year ago, there was much
    more chaos and fewer structured components. I think now the field is getting more
    mature, so you get more solutions that abstract away the logic on a higher level.
  sec: 3706
  time: '1:01:46'
  who: Nikita
- line: You do not need to write every individual LLM call anymore when you are building
    an agentic system. You can initialize an agent, deploy it to a certain runtime,
    and then monitor it.
  sec: 3722
  time: '1:02:02'
  who: Nikita
- line: This is getting more mature, and this also looks more secure and scalable
    compared to the first months of GenAI, where you would just take LangChain, which
    was updating probably every couple of days or even more frequently, and just have
    a bunch of custom Python code connecting things together.
  sec: 3737
  time: '1:02:17'
  who: Nikita
- line: Nikita, I think that is all we have time for today. Thanks a lot for sticking
    around for a little longer and for all your answers. They were really insightful,
    and I really enjoyed this discussion. Thanks for joining us today, and I also
    want to thank everyone who joined us, listened, or contributed questions. It was
    really cool. Thanks.
  sec: 3760
  time: '1:02:40'
  who: Alexey
- line: Thanks a lot for the invitation. I had a great hour and I am wishing everyone
    a great day, evening, afternoon, or morning, wherever you are based.
  sec: 3783
  time: '1:03:03'
  who: Nikita
- line: I hope to see you soon again because our previous session where you talked
    about RAG was really good, and I really enjoyed this one too. I hope to see you
    soon.
  sec: 3792
  time: '1:03:12'
  who: Alexey
---

Links:

* [Linkedin](https://www.linkedin.com/in/kozodoi/){:target="_blank"}
* [Github](https://github.com/kozodoi){:target="_blank"}
* [Website and blog](https://www.kozodoi.me/){:target="_blank"}