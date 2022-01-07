---
title: "The Rise of MLOps"
short: "The Rise of MLOps"
guests: [theofilospapapanagiotou]

image: images/podcast/s02e04-mlops.jpg

season: 2
episode: 4

ids:
  youtube: -i0fVp0ntYA
  anchor: The-Rise-of-MLOps---Theofilos-Papapanagiotou-ept67o

links:
  youtube: https://www.youtube.com/watch?v=-i0fVp0ntYA
  anchor: https://anchor.fm/datatalksclub/episodes/The-Rise-of-MLOps---Theofilos-Papapanagiotou-ept67o
  spotify: https://open.spotify.com/episode/3YPvzGQnfxl7Mo1VKE0l1K
  apple: https://podcasts.apple.com/us/podcast/the-rise-of-mlops-theofilos-papapanagiotou/id1541710331?i=1000507907719

transcript:
- line: "Today we will talk about MLOps. We have a special guest \u2014 Theofilos\
    \ Papapanagiotou. Theo and I are colleagues. I work at OLX Group and Theo works\
    \ at the parent company of OLX \u2014 Prosus. In our company, Theo is the main\
    \ advocate of MLOps. He's usually the go-to person for everything related to machine\
    \ learning in production, model deployments, tools for serving machine learning,\
    \ Kubeflow, everything related to that. I wanted to invite somebody to talk about\
    \ MLOps and it was very difficult for me to think of anyone else better suited\
    \ for this chat than Theo. Thank you very much for coming to our event. Welcome."
  sec: 154
  time: '2:34'
  who: 'Alexey:'
- line: Thanks, Alexey. It's my pleasure to be here.
  sec: 198
  time: '3:18'
  who: 'Theo:'
- header: "Theo\u2019s background"
- line: Before we go into our main topic of MLOps, let's start with your background.
    Can you tell us a bit about your career journey so far?
  sec: 201
  time: '3:21'
  who: 'Alexey:'
- line: Sure. I'm an engineer with a background of working in telecom for the last
    20 years. I studied computer science. Then I had a Master's in data communications,
    and finally a Master's in AI. In that journey of 20 years, I've been transitioning
    from a Unix engineer to Data Ops and to ML engineering for about the last seven
    years.
  sec: 210
  time: '3:30'
  who: 'Theo:'
- line: "You actually had two Master\u2019s?"
  sec: 241
  time: '4:01'
  who: 'Alexey:'
- line: Yes. I haven't finished the last one yet, it's ongoing.
  sec: 244
  time: '4:04'
  who: 'Theo:'
- line: You're still studying?
  sec: 248
  time: '4:08'
  who: 'Alexey:'
- line: I did. I don't study anymore. I finished with the lectures a couple of years
    ago but there is still this thesis thing that I need to deliver.
  sec: 250
  time: '4:10'
  who: 'Theo:'
- line: What do you do now?
  sec: 269
  time: '4:29'
  who: 'Alexey:'
- line: Now, I'm working at Prosus and it's a company that invests in other companies.
    We are working together with some of them on some projects. This company invests
    mostly in segments like food delivery, payments, classifieds, as well as EdTech.
    We have a team called the Prosus AI team and we are helping the data science teams
    of these companies to level up their maturity in the space of machine learning
    operations.
  sec: 273
  time: '4:33'
  who: 'Theo:'
- header: DevOps and MLOps
- line: Companies like OLX, where you help us to do all these things related to MLOps.
    So, what is MLOps?
  sec: 314
  time: '5:14'
  who: 'Alexey:'
- line: It's a buzzword these days. In the TWIML conference, everyone was talking
    about MLOps. All the vendors that have a platform to sell were talking about this.
    I remember that we had the same thing and the same feeling like 10 years ago,
    when people started talking about DevOps and what DevOps is. And there are a lot
    of things. It's about the culture, it's about how people are working together,
    and how they are collaborating to solve a problem. But it's also about processes
    and technology.
  sec: 325
  time: '5:25'
  who: 'Theo:'
- line: "So, it's a set of best practices that helps people to deliver machine learning\
    \ models in production, and not only deliver but also maintain effectively. The\
    \ industry realized 10 years ago that not having some barriers between the development\
    \ department and an operational department is not helping with fast iteration\
    \ of delivering or releasing software quickly. When you want to have a product\
    \ that is changing fast, in order to deliver new features to your customers or\
    \ to fix bugs, you have to iterate fast \u2013 you have to release a lot of times."
  sec: 325
  time: '5:25'
  who: 'Theo:'
- line: "You have to minimize the amount of time that you spend from the moment that\
    \ you will write a line of code to the moment that it will reach production and\
    \ start serving customers. This is DevOps. Over time, it's been described with\
    \ different names. The skill set of people that have been working with it has\
    \ been changing. Although, to me, it's still the same \u2014 a Unix Engineer or\
    \ a system engineer that has been transitioning from different titles."
  sec: 325
  time: '5:25'
  who: 'Theo:'
- line: "\u201CCloud engineer\u201D I think also comes up pretty often nowadays."
  sec: 443
  time: '7:23'
  who: 'Alexey:'
- line: "Absolutely. However, we should also mention that there are differences on\
    \ the fundamentals \u2014 what is a software delivery workflow and what is a machine\
    \ learning workflow? In the software space, you write code, you have some requirements,\
    \ and you deliver a piece of artifact that you deploy somewhere. This is fundamentally\
    \ different from the machine learning workflow. There, a data scientist has to\
    \ do some exploratory analysis first on the data and then build the pipeline that\
    \ will build a model based on some modeling activity. But the input of the modeling\
    \ (or the training process, as we call it) is not just the code that the data\
    \ scientist is writing, but the input is also the data. The artifact that has\
    \ been produced in that case is the model and that model has a life cycle, which\
    \ is not the same as the lifecycle of a typical artifact from the software engineering\
    \ world."
  sec: 448
  time: '7:28'
  who: 'Theo:'
- line: "In the software engineering world, you have an artifact in the form of a\
    \ container or in the form of a binary file that you release or you deploy in\
    \ a server and after the tests have been executed in your in your CI process,\
    \ you have it always running, as long as there are no breaks in the connections\
    \ in the other systems. However, in the space of the machine learning workflow,\
    \ this is different. The model is not something that you will build and will work\
    \ on forever. The model degrades over time because the data are changing over\
    \ time. I have a nice example that I like to use in the company, which says that\
    \ when a new iPhone is coming out every year, if you have a classifier that identifies\
    \ the model of the iPhone, let's say \u2013 every year you will have to retrain\
    \ the model that is doing this classification, because you have a new class in\
    \ the data space. That's why for example, the model will degrade."
  sec: 448
  time: '7:28'
  who: 'Theo:'
- line: There are other examples of models that are being retrained for example, every
    day or every time you are performing an action to label some data set in your
    doorbell from Nest or in your car with your driving models that you might have.
    So, the fundamental difference is that the model is degrading over time and that's
    why the monitoring of this deployed artifact has to be able to trigger every training
    job, not just stay there forever. You will never have this in software engineering.
  sec: 448
  time: '7:28'
  who: 'Theo:'
- line: So basically, the main difference between DevOps and MLOps is that the life
    cycle is different, because the input to machine learning service is data that
    changes over time, and it means that we need to look out and see if there are
    some changes, which is when we possibly need to trigger some things. This is not
    something that we cover in DevOps, right?
  sec: 609
  time: '10:09'
  who: 'Alexey:'
- line: "Absolutely. Of course, in DevOps, you deploy an application. This application\
    \ is following some rules. It's rule-based software that is performing some action\
    \ and based on the tests \u2013 in the unit and functional tests that you have\
    \ written \u2013 you validate that the artifact is performing exactly the activity\
    \ that you have described in your requirements. But yes, with a model, this is\
    \ different. It's not as static as the software artifact."
  sec: 635
  time: '10:35'
  who: 'Theo:'
- line: Are there other crucial differences between DevOps and MLOps in addition to
    these so-called data drifts? Is there something else?
  sec: 666
  time: '11:06'
  who: 'Alexey:'
- line: "Yes. There is another thing. If you remember, especially in the world of\
    \ SREs, this statement that \u201Cmonitoring is the foundation of the operation\
    \ of SREs\u201D that\u2019s important. Monitoring in the space of MLOps is even\
    \ more important, because you don't only need monitoring in order to have a service\
    \ that is performing as you described it, you also need monitoring in order to\
    \ trigger these actions that we have described \u2013 the retraining action. So,\
    \ the monitoring is going to another level."
  sec: 677
  time: '11:17'
  who: 'Theo:'
- line: In the typical DevOps environment or in the typical software environment,
    you will have service-related metrics and business-related metrics, like how many
    requests per second you'll receive and latency. But in the space of machine learning,
    you might want to also monitor some extra things that you are also doing during
    training time, or even that you want to only have during inference time. For example,
    fairness or anomaly detection, or I don't know, adversarial attacks on your model.
    In order to have such extended monitoring unit components in your workflow that
    are not only retrieving all these logs and metrics that you are producing from
    your inference, but also performing the action to kick off the training pipeline.
  sec: 677
  time: '11:17'
  who: 'Theo:'
- header: Tooling in ML Ops and DevOps
- line: So are these monitoring tools that we're talking about different from traditional
    DevOps tools? For example, usually what we use is like Prometheus, Grafana, and
    things like that. Are they different in the MLOps world, or are they similar?
    Are these the same tools?
  sec: 766
  time: '12:46'
  who: 'Alexey:'
- line: "In a typical software component, you are generating metrics in your Prometheus\
    \ \u2013 from your application itself \u2013 when a class has been instantiated,\
    \ you might want to increase a counter, or when you are receiving a new request\
    \ to export to a particular workflow of your application. In ML, you want separate\
    \ components that are receiving the data that you're trying to infer, and also\
    \ receiving maybe the payload of the response, and do comparisons with the rest\
    \ of the data that you have. So, you need a large infrastructure to build and\
    \ send such metrics in Prometheus."
  sec: 784
  time: '13:04'
  who: 'Theo:'
- line: "Of course, the toolset is the same. Prometheus is the standard, let\u2019\
    s say, metric system now, like Graphite was 10 years ago. At the same time, Grafana\
    \ is dominant in the space of visualization of dashboards for monitoring. But\
    \ the component or the service that is going to generate these metrics is something\
    \ new and it's something that should become something reusable that people can\
    \ utilize \u2013 you can buy it \u2013 you want to have this commoditized, you\
    \ want to buy from a vendor or from the supermarket, a component that's performing\
    \ inference monitoring on the robustness of your model."
  sec: 784
  time: '13:04'
  who: 'Theo:'
- line: And why do we want to commoditize that? I know that it's a difficult thing
    to deploy models. So, this is why we want to make it as simple as possible, right?
  sec: 871
  time: '14:31'
  who: 'Alexey:'
- line: Yes, absolutely. If we want to be able to iterate fast, we don't want to spend
    time and development effort on figuring out what the special metrics are for each
    model that we need to have. We need to be able to automatically, if possible,
    identify these and plug them into the pipeline.
  sec: 884
  time: '14:44'
  who: 'Theo:'
- header: ML engineering vs ML Ops
- line: "I often see that there is confusion between ML engineering and MLOps. Often\
    \ these terms are now used as synonyms. So, I was wondering \u2013 do you think\
    \ they are different? And if they are, what is the main difference between the\
    \ two?"
  sec: 909
  time: '15:09'
  who: 'Alexey:'
- line: "ML engineering is a relatively new topic and [Inaudible] MLOps. The same\
    \ way that you would say that a software engineer and DevOps are the same, or\
    \ something like this, I could imagine. The role is \u201Cmachine learning engineer\u201D\
    \ and MLOps is the practice of following the best practices roadmap, let's say.\
    \ It\u2019s some maturity level, or a roadmap that is available out there. So,\
    \ ML engineer is the profession or the role, and MLOps is the practice of performing\
    \ such a role with the rest of the departments \u2013 communicating with your\
    \ business and your operations."
  sec: 929
  time: '15:29'
  who: 'Theo:'
- header: The roles of ML Ops
- line: "The people who are doing MLOps, who are they? Are they ML engineers, or is\
    \ it a special person who we can call an \u201CMLOps engineer\u201D. If you want\
    \ to do MLOps, what kind of role do you want to acquire?"
  sec: 976
  time: '16:16'
  who: 'Alexey:'
- line: "Well, MLOps is the practice that three different roles in an organization\
    \ perform. There\u2019s the business need, the production operation, and the development,\
    \ all working together and following the best practices. Similar to how in DevOps,\
    \ you have a developer, you have the operator, and you have the business need.\
    \ The business need defines the metric, or the SLO or SLI. You define these metrics,\
    \ you define the error budget. Then in the space of the operator and developer,\
    \ you have someone who's producing something, and he's collaborating with someone\
    \ who is consuming something \u2013 that's the customer \u2013 the operator is\
    \ consuming the code that the developer wrote. In the space of MLOps, it's similar.\
    \ You have the ML engineer who's creating the model, creating the pipeline and\
    \ maintaining it. Then you have the operator who is monitoring, operating the\
    \ model, and making sure that the pipeline is working properly. Then the business,\
    \ or the product owner, or however you want to call him or her \u2013 the person\
    \ setting the requirements or the service level."
  sec: 997
  time: '16:37'
  who: 'Alexey:'
- line: The product manager, right?
  sec: 1068
  time: '17:48'
  who: 'Alexey:'
- line: Yeah, you could say product manager, but not in the form of giving the requirements
    and not even knowing who they are working with. It's about having a common theme
    that they are working together, maybe under the same manager even, if possible.
    But they are focusing on delivering something very particular, like a set of models.
    This is a special team that is doing, let's say, the sets in the organization,
    and this is the special thing that is doing the recommendation.
  sec: 1116
  time: '18:36'
  who: 'Theo:'
- line: "Okay. It\u2019s basically a cross-functional team where everyone is working\
    \ on solving the same problem together as one team. So, it\u2019s not like the\
    \ developers do something and then they throw it over the wall to the original\
    \ team \u2013 they support it, but everyone is working together."
  sec: 1096
  time: '18:16'
  who: 'Alexey:'
- line: "That\u2019s the cultural topic of MLOps and it's quite similar, or even the\
    \ same as the culture in DevOps."
  sec: 1116
  time: '18:36'
  who: 'Theo:'
- line: So, the ML engineer is this developer role, but who has this operator role
    in the MLOps world? How can we call these people?
  sec: 1124
  time: '18:44'
  who: 'Alexey:'
- line: "Well, you might have the same people who are performing this action. If you\
    \ have a small, functionally complete team that is doing this and who is responsible\
    \ for what they are writing \u2013 that's what they wrote at the Amazon lead,\
    \ for example, with the big two [Inaudible] teams, saying that you build it and\
    \ you run it. You have a team of, let's say, five people, and the product owner\
    \ that is defining the inputs and outputs of the team, or the interfaces, the\
    \ API definitions and everything, and the developers are the same people who are\
    \ also running it. If you would say that you have separate departments, in the\
    \ past, that were producing a model and were operating the model, you would expect\
    \ that in the future, you would have one common thing \u2013 they perform this\
    \ action as a functional completed team."
  sec: 1138
  time: '18:58'
  who: 'Theo:'
- line: Is there such a thing as an MLOps engineer as a role, in the same way that
    we have site reliability engineers or DevOps engineers? I also saw this title
    pop up sometimes.
  sec: 1191
  time: '19:51'
  who: 'Alexey:'
- line: I don't think that it will become a title. Maybe people will have it because
    it's a fancy word now, like data scientist was 10 years ago. But I don't think
    this will become a role of a department. If it does, that would be a shame because
    we've also seen this in some organizations trying to create a role, or even a
    team, with the name DevOps. They are missing the whole concept of having DevOps.
    The whole concept is about having a common team that is performing this function
    rather than having different things to communicate with each other over an escalation
    path for different managers and operating silos.
  sec: 1208
  time: '20:08'
  who: 'Theo:'
- line: "Okay. So, we have a team and in the team, we have three roles: we have the\
    \ developer, the operator, and somebody from business. The developer is the machine\
    \ learning engineer, from business, we have a product owner or product manager,\
    \ and the operator can be someone like the site reliability engineer. I know that\
    \ at OLX, we have a role called site ability engineer, and then in parenthesis,\
    \ we say \u201Cmachine learning\u201D, but it means nothing else except that it\
    \ will be someone who will be working with the ML team. Did you see these things\
    \ coming up, like some sort of specialization within the SRE role?"
  sec: 1255
  time: '20:55'
  who: 'Alexey:'
- line: "That's a good question. Eventually, I think, more and more people will jump\
    \ into that role. Because maintaining a model will become more adopted in organizations\
    \ \u2013 having machine learning models will become more than just a trend, but\
    \ the fact of how organizations operate as they are switching from process-driven\
    \ to data-driven to model-driven organizations. That's the concept of democratization\
    \ of machine learning. You have your whole organization being able to utilize\
    \ models, and even to build them, if possible. Thus, more and more software engineers\
    \ will come to become machine learning engineers. More and more data scientists\
    \ will transition to that, like they have transitioned from data mining experts\
    \ or statisticians into that role. The software is the tool to achieve what you\
    \ want anyway. The model can also be the tool, in the future, to achieve what\
    \ you want as a function in the organization."
  sec: 1307
  time: '21:47'
  who: 'Theo:'
- header: Recognizing an MLOps role and MLOps maturity
- line: Let's say we want to find a place, or a company, that practices MLOps, and
    we're looking for a job right now. How do we recognize that a job posting is for
    an MLOps role? Are there some specific keywords that I need to look for?
  sec: 1376
  time: '22:56'
  who: 'Alexey:'
- line: Well, the easiest thing would be to look at the skills required. You can search
    in the requirements or the responsibilities for the role, but usually, these are
    just fancy sentences.
  sec: 1400
  time: '23:20'
  who: 'Theo:'
- line: "\u201CExperience in MLOps,\u201D go figure out what that means. [laughs]"
  sec: 1422
  time: '23:42'
  who: 'Alexey:'
- line: '[laughs] But, of course, if you''re seeing names of tools like Kubeflow in
    the skill set or ML pipelines and even special skills on components that are trending
    now in the space of monitoring of machine learning models in the space of fairness
    and detection. Then, of course, you can understand that they have reached some
    depth in the maturity of the MLOps. Maybe I can use this opportunity to say that
    there is an article written by Google, and then there was an article written by
    Microsoft, on the topic of maturity on the MLOps.'
  sec: 1427
  time: '23:47'
  who: 'Theo:'
- line: "In these articles, they have defined levels. Google defined three levels\
    \ \u2013 0, 1, 2 \u2013 and Microsoft defined five levels \u2013 0, 1, 2, 3, 4\
    \ \u2013 and they describe with some bullet points regarding what are the requirements\
    \ to achieve maturity in the adoption of MLOps. There is even an MLOps roadmap\
    \ for 2020 and 2025, which describes all the technologies that you should adopt\
    \ in order to mature in that space. We didn't have this back 10 years ago when\
    \ we were defining DevOps. We had the manifesto of what DevOps is and how we should\
    \ collaborate, but we didn't have such a nice definition of how to mature. I appreciate\
    \ that. I can post references at the end."
  sec: 1427
  time: '23:47'
  who: 'Theo:'
- line: Maybe we can just quickly go over these three levels of maturity. It was from
    Google, you said?
  sec: 1533
  time: '25:33'
  who: 'Alexey:'
- line: Yeah, there is one from Google and one from Microsoft.
  sec: 1541
  time: '25:41'
  who: 'Theo:'
- line: The one from Google has three and the one from Microsoft has five. So, the
    one from Microsoft is probably more detailed. But the one from Google, what kind
    of stages did they define?
  sec: 1544
  time: '25:44'
  who: 'Alexey:'
- line: "Yes. They break it down into people, processes, and technology \u2013 traditional\
    \ maturity models from their organization. Then they describe with bullet points\
    \ \u201CWhat are the important things to have?\u201D They show that at maturity\
    \ level zero, that\u2019s when you don't have MLOps, which means that you have\
    \ manual processes to train a model, and you have manual processes to deploy a\
    \ model. You also have someone who is monitoring the model and maybe makes a decision\
    \ after comparing it with some data that they receive from a data store to perform\
    \ a training activity."
  sec: 1554
  time: '25:54'
  who: 'Theo:'
- line: "By \u201Cmanual\u201D, you mean running it in a Jupyter Notebook? Or something\
    \ fancier? For training, specifically."
  sec: 1592
  time: '26:32'
  who: 'Alexey:'
- line: Manual monitoring or manual deployment?
  sec: 1601
  time: '26:41'
  who: 'Theo:'
- line: No, model training. Because I know for a fact that even we at OLX sometimes
    do that with a model and then what we do to train it is just run a Jupyter Notebook,
    and then you know, run, run, run. At the end you have a model.
  sec: 1603
  time: '26:43'
  who: 'Alexey:'
- line: Even if you're not doing it in your laptop, and you're doing it in the cloud,
    such as in Sage Maker, it's still a manual process. If you have to start a notebook,
    and clickety click, run the cells and produce your artifact, and produce your
    model. This is a manual process, this is the maturity level is zero, where you
    don't have ML Ops. You might have DevOps and you might have CI there, and you
    might have it where the model is being picked up by S3 and it's being deployed
    in Sage Maker endpoint and it's been made available. But you definitely don't
    have MLOps.
  sec: 1621
  time: '27:01'
  who: 'Theo:'
- line: "Of course, there are other things. You might have integration with an application\
    \ that you might want to introduce and this is also not something that you have\
    \ automated in the MLOps space \u2013 MLOps level zero. Then they describe the\
    \ level one of maturity. That\u2019s when you are starting to introduce some automation.\
    \ You're building a pipeline, and then you have the components of the pipeline\
    \ that are doing the data validation that you're receiving in a nice way that\
    \ the TensorFlow extended paper defined about four years ago. You have components\
    \ that are validating the data that you have received or the features, whether\
    \ they are according to the schema of the data that you are expecting and performing\
    \ the training, having the evaluation component of the evaluation module that\
    \ is setting the criteria that you have set in order to promote it or to label\
    \ it as a \u2018golden model\u2019 that you will promote in production or that\
    \ will go for more testing in order to release it."
  sec: 1621
  time: '27:01'
  who: 'Theo:'
- line: "When you have a pipeline, this is an automation task, and the level goes\
    \ up to maturity level one, because you spend less time on this, there\u2019s\
    \ less friction between teams. The teams are working together and you have the\
    \ data engineer who's producing the features, working together with a machine\
    \ learning engineer who is maintaining the training job, and who maybe wakes up\
    \ during the night to fix a broken model. Because that's also the role of the\
    \ operator, which the machine learning engineer should have, if we want to have\
    \ this combined MLOps role."
  sec: 1621
  time: '27:01'
  who: 'Theo:'
- line: "So basically, when we train our model in Jupyter by clicking \u2018run, run,\
    \ run\u2019, this is automation level zero. Once we move this from a notebook\
    \ to a script, then there is a certain level of automation (when we don't do this\
    \ manually). But instead, there is some training pipeline that we can easily run.\
    \ We change some parameters, hit enter and then it just transfers them \u2013\
    \ this is level one. Right?"
  sec: 1762
  time: '29:22'
  who: 'Alexey:'
- line: Yes, and more things as well. You are producing metrics that you are observing
    and you make a decision to hit the button in your CI to do retraining.
  sec: 1793
  time: '29:53'
  who: 'Theo:'
- line: Well, this is still manual, right?
  sec: 1805
  time: '30:05'
  who: 'Alexey:'
- line: "Yes, it\u2019s manual. But maybe it automatically adds your new features\
    \ from your feature store, or if you have some data versioning system, and etc.\
    \ So, that's the maturity level one. Then there is the visual \u2013 the ultimate\
    \ goal that we should target. That's maturity level two in terms of Google, level\
    \ four in terms of Microsoft, which says that we have an automated retraining\
    \ process. The model is being monitored with all the metrics that we have mentioned\
    \ in the past. Not only the service-level metrics, like the latency and the number\
    \ of requests, but all these quality metrics about the fairness and the robustness,\
    \ and maybe even explainability topics that you want to have."
  sec: 1808
  time: '30:08'
  who: 'Theo:'
- line: "To detect whether your model is degrading, this is a difficult problem. So,\
    \ it\u2019s having all these metrics in your Prometheus that are setting data\
    \ drift and model\u2019s concept drift, and all these sensors that you have around\
    \ your ecosystem are triggering. So, you have triggers, and these are triggering\
    \ an execution of a pipeline. This is maturity level two. Triggering the execution\
    \ of a pipeline is a whole another discussion. What we have been seeing in the\
    \ last 10 years of big data was the scheduler \u2013 that was the ultimate component\
    \ that was periodically performing an action, maybe daily training a model or\
    \ maybe nightly creating the new features from your orders \u2013 from your data\
    \ set. That was typically a time-driven execution, time-driven scheduling. But\
    \ now, the modern machine learning pipelines, which are different from data pipelines,\
    \ should be data-driven. They should be able to be triggered by your metrics,\
    \ your threshold."
  sec: 1808
  time: '30:08'
  who: 'Theo:'
- line: So, you define thresholds for the metrics that you have set, or even the threshold
    is something static, even the threshold should be something that you can even
    create a model for in order to identify when we should trigger the retraining.
    Imagine having this being trained when you don't want it. So, when you are setting
    up a data-driven execution, you need special tooling for that pipeline. But then
    you're having such quality problems that you're facing as an organization, that
    you are maturing on how the model is performing. That's why I think that this
    maturity model will help organizations get deeper and better into onboarding ML
    models.
  sec: 1808
  time: '30:08'
  who: 'Theo:'
- header: Changing the mindset to MLOps
- line: "So basically, to help not just directly jump on monitoring drift and having\
    \ faith in the model that it will retrain itself and everything will be fine.\
    \ Instead, it\u2019s just gradually moving from one step to another and changing\
    \ the mindset in the meantime, right?"
  sec: 1991
  time: '33:11'
  who: 'Alexey:'
- line: "Yes, and of course, the foundation is monitoring. I\u2019m vocal about this\
    \ \u2013 we should take care of our models in production and not only take care\
    \ of them, but create new data out of how they are performing. Because the monitoring\
    \ is generating data, it\u2019s not only the payload loading where you get the\
    \ inference request and the inference responds with class names, let's say. You\
    \ also want all the peripheral explainability metrics \u2013 fairness, etc."
  sec: 2007
  time: '33:27'
  who: 'Theo:'
- line: I see that as a change in mindset. We need to care about all these things
    before we can implement them. But I assume that it also requires some special
    tooling. What are these tools? What can we use to actually help MLOps and have
    all these things? Are there even tools for this at all?
  sec: 2041
  time: '34:01'
  who: 'Alexey:'
- line: "Yes, of course. What I was fascinated about in the MLCon, in this and last\
    \ week, was that there are so many vendors jumping on this train and using the\
    \ buzzword \u2018MLOps\u2019 to promote their solution. And good vendors that\
    \ are focusing on the right direction and focusing on how to build systems that\
    \ are triggering jobs, how to build monitoring tools, and how to produce SDKs\
    \ that are helping you build monitoring tools."
  sec: 2065
  time: '34:25'
  who: 'Theo:'
- line: Not only vendors, of course, there is plenty of open-source software and the
    whole ecosystem of Kubeflow is a collection of such tools. The fact of that is
    that it should be Kubernetes-based. That's the new Linux for me. Linux dominated
    the world 20 years ago, and we still have it in like 90-something percent in our
    data centers. Kubernetes is the de facto way to manage workloads. The way that
    we are doing machine learning on Kubernetes is today, Kubeflow is the leading
    tool.
  sec: 2065
  time: '34:25'
  who: 'Theo:'
- header: Kubeflow
- line: So, Kubeflow is the tool we should have if we want to start implementing MLOps
    in our organization. Let's say, if we don't want to go to a vendor, we want to
    go with open source, then Kubeflow is the tool we want in order to help us. Right?
  sec: 2137
  time: '35:37'
  who: 'Alexey:'
- line: Absolutely. But also vendors. The leading vendor right now in the Kubeflow
    community is AWS and Microsoft, together with Google and other great developers
    who are constantly delivering new functionality. The business has identified that
    by sharing the capabilities of the ecosystem, they also promote the product. So,
    as they are delivering cloud services, they want to deliver cloud services that
    are based on products that other people know. When you are using Sage Maker, maybe
    you're invoking a pipeline that, in the back, is a Kubeflow pipeline. When you
    are deploying a model, an inference service, in Google Cloud, it might be KF serving
    inference service. When you are running Jupyter in Azure, it might be running
    as a Kubernetes pod following the Kubeflow definition.
  sec: 2151
  time: '35:51'
  who: 'Theo:'
- line: Maybe let's take a step back and talk about Kubeflow. What is it and what
    kind of components do we have in Kubeflow?
  sec: 2218
  time: '36:58'
  who: 'Alexey:'
- line: For me, Kubeflow is an ecosystem that delivers an ML platform. If you jump
    on it, you will start figuring out that there are components that you were not
    aware of and you might want to start using them in your workflow. For example,
    when we deployed some models last year in the company, we just focused on having
    a model that is servable, one that we can use to send inference requests and get
    the responses. But then we have seen that with KF serving, which is the Kubeflow
    serving subcomponent, we have peripheral tools like the explainer and the transformer,
    and then the drift detector and the outlier detector.
  sec: 2226
  time: '37:06'
  who: 'Theo:'
- line: "Now we have more and more components. By utilizing them, we started building\
    \ metrics. So, Kubeflow is a superset of components. For me, the component I love\
    \ the most is KF serving, because I'm so into the things that are in production.\
    \ But, of course, it's touching areas before the serving \u2013 it\u2019s touching\
    \ areas before the deployment. The big component of Kubeflow is also the Kubeflow\
    \ pipelines, which are based on different schedulers. You can have it with two\
    \ different data-driven schedulers. One is Argo CD from Intuit, and the other\
    \ is the Tekton from K-native. These pipelines are an implementation of the TFX,\
    \ and implementation of the TensorFlow extended. So, the paper that was given\
    \ to the public four years ago from Google that says we should have component-based\
    \ and data-driven execution between the components with a Pop/Sub type of relationship,\
    \ led the way to have such an implementation, the Kubeflow pipelines. Then more\
    \ and more tools are assembling in this popular feature store called Feast from\
    \ Gojek is now also part of the community \u2013 it has joined the ecosystem.\
    \ I wouldn't be surprised if this will be donated to a foundation any moment soon.\
    \ Did I answer your question about KubeFlow?"
  sec: 2226
  time: '37:06'
  who: 'Theo:'
- line: From what I understood, Kubeflow will have this KF serving component that,
    in addition to just serving models, also has nice features of detecting outliers
    and detecting drift. In addition to that, there is another component called Kubeflow
    pipelines, which we use for building our training pipelines. Then there is the
    third component, which is Feast, which is not yet part of Kubeflow as I understood.
    But it's a feature store that we can use when building our training pipelines.
  sec: 2376
  time: '39:36'
  who: 'Alexey:'
- line: "Yes, and other components as well. There is this nice tool for hyperparameter\
    \ optimization and neural architecture effect, which is called Katib. It was a\
    \ Google Visio (or something) product that evolved to Katib. Katib is image describing\
    \ in a YAML that you want to set that space to define an optimization objective\
    \ \u2013 as a data scientist, you want to train the model and receive 99% accuracy.\
    \ So, that's your optimization objective. Then you define the ranges of your hyperparameters,\
    \ the same way that you're doing grid search and you say, \u201CI want my learning\
    \ rate, to search values between 001 and 002 with a step of this amount.\u201D\
    \ Then it splits all these different executions of the search into components\
    \ or into pods, or into containers, if you like, in the space of Docker and Kubernetes,\
    \ that are performing this training job with these parameters and then they are\
    \ producing a result \u2013 it's been reduced \u2013 and then comparing all the\
    \ results in a nice visual view to decide which model to promote."
  sec: 2412
  time: '40:12'
  who: 'Theo:'
- line: "The nice thing about it is that these components can be installed as standalone\
    \ components in your cluster without having to have full blown Kubeflow. However,\
    \ the beauty of it is that you can also have it full blown. They have tight integration.\
    \ There is this company called Arrikto that has built this tool called K, which\
    \ gives you the ability to transform your notebook cells into containers. So,\
    \ you build the whole pipeline in a notebook and then, when you click \u2018play\u2019\
    , it builds containers of your cells to perform this activity. Then you split\
    \ it and send it to Katib for the hyperparameter search, let's say, and then deploy\
    \ the best model. Beautiful stuff."
  sec: 2412
  time: '40:12'
  who: 'Theo:'
- line: You mentioned TFX (TensorFlow Extended) a couple of times. Did I understand
    correctly that Kubeflow is an implementation of that paper?
  sec: 2539
  time: '42:19'
  who: 'Alexey:'
- line: "Yes. They don't call it that. Since the beginning, they were saying that\
    \ they don't see something as an extended externalization of Google ML platform,\
    \ but this is what this to me. [laughs] If you look at TFX, it\u2019s how to do\
    \ production with TensorFlow, that\u2019s saying that you can also do it with\
    \ Airflow. Because Airflow is also a scheduler. You have your data, you have your\
    \ components, you are producing an artifact from each component and it's being\
    \ used maybe for the input of the next task. Similarly, you can also do it with\
    \ Apache Beam, which is another software that is abstracting your Spark or your\
    \ Pandas or whatever framework you're using for your data processing to perform\
    \ certain such tasks. But for me, the production-, or the enterprise-level system\
    \ is Kubeflow."
  sec: 2548
  time: '42:28'
  who: 'Theo:'
- header: How to learn Kubeflow
- line: If I want to learn Kubeflow, how can I do that?
  sec: 2603
  time: '43:23'
  who: 'Alexey:'
- line: "As a nice, open-source tool, it has a beautiful community. I would advise\
    \ to start from the website of Kubeflow. They have excellent documentation. It\u2019\
    s still being built. The documentation itself is open source, so you can extend\
    \ it if you find the problem. You can also join as a contributor to the project\
    \ if you have an idea of how to improve something. The organization of Kubeflow\
    \ has around 20 repositories of 20 different components and you can onboard and\
    \ read the GitHub issues. If you have a problem, search the code and figure out\
    \ what the problem you are having is \u2013 if you want to resolve the problem.\
    \ Because it's becoming a more and more complex system, you will have more and\
    \ more problems, as you can imagine. But it also has easy ways to start."
  sec: 2608
  time: '43:28'
  who: 'Theo:'
- line: "There are two books already published about this from O'Reilly. There are\
    \ YouTube videos where you can find how to get started for each individual component.\
    \ There are workshops delivered from each vendor. AWS, for example, has a workshop\
    \ on Kubeflow. There is a special website for that. IBM created the Kubeflow Dojo,\
    \ which is a set of training, a two-day workshop that specifies how to perform\
    \ certain different implementations. Not only to install it but also to use it\
    \ \u2013 to get the TFX example with the taxi driver, for example, if you remember.\
    \ It was published two years ago. And build it in Tekton pipelines in Kubeflow."
  sec: 2608
  time: '43:28'
  who: 'Theo:'
- line: I remember going through this myself. We used AWS and there is a nice article
    in Kubeflow recommendation, (end-to-end setup on AWS or something like that) and
    you just can follow this article, and you have a full blown Kubeflow your cluster.
    Right?
  sec: 2712
  time: '45:12'
  who: 'Alexey:'
- line: Yeah.
  sec: 2793
  time: '46:33'
  who: Theo
- line: Do you maybe have something in mind, maybe an easy getting started project
    one can do? Let's say by following this tutorial, they set up a Kubeflow in their
    AWS or Google Cloud or whatever, and they just want to learn this. Is there an
    easy getting started project, like Iris in machine learning?
  sec: 2796
  time: '46:36'
  who: 'Alexey:'
- line: Sure. The easiest way is to start Sage Maker, build the pipeline, and fit
    some features from the feature store and deploy them in the endpoint. It gives
    you the Sage Maker studio that is doing all these things nicely. The same way
    with Google Cloud, which is also Kubeflow-based, so AI platform is, when you are
    creating a model, you're creating an inference service. When you are creating
    a pipeline, you are creating a Kubeflow pipeline. So, that's the easiest way.
    You'll consume it as a service from a cloud provider. But if you want to get deeper
    as a machine learning engineer and maintain your own implementation from the open-source
    tool, rather than paying a vendor for that, you can install it, as you described,
    from this nice document.
  sec: 2761
  time: '46:01'
  who: 'Theo:'
- header: Data versioning and DataOps
- line: We also have a question about data versioning. How important data is versioning
    in MLOps?
  sec: 2807
  time: '46:47'
  who: 'Alexey:'
- line: It is important. The data is the raw source of what you need in order to produce
    a model. You cannot produce a model without data. As we discussed cast, there
    is the concept of data drift. So, you want to retrain your model with the new
    data. But when you have new versions of the model, then we are introducing the
    concept of model versions, next to your code version, and next to your data versioning.
    You want to have some type of synchronization or record of which version of the
    model was used, which version of data with which version of code. Because, as
    you will start automating and to have automated retraining, you want to be able
    to review all these things. You want to be able to go back.
  sec: 2818
  time: '46:58'
  who: 'Theo:'
- line: "Maybe due to privacy or GDPR issues, you would like to go back in time and\
    \ figure out why this model gave this inference. \u201CWhy did this model say\
    \ that this customer should not get a loan from the bank?\u201D So, you need to\
    \ go back to the model version that gave this prediction, you need to have the\
    \ payload, of course, you need to go back from this model to map it to the data\
    \ that you have used in order to train it, to see which feature was important,\
    \ and for example, see that customer had another loan. So, that was another feature\
    \ and because of that, the importance of these features, the model should infer\
    \ that the customer should not get a loan. So tracking of the versions of the\
    \ data, of the code, and the model usually is done in a system called the metadata,\
    \ or machine learning metadata store."
  sec: 2818
  time: '46:58'
  who: 'Theo:'
- line: "There is good news, the TensorFlow team decided to work together with the\
    \ Kubeflow team and combine this project into one and build the MLMD system, which\
    \ is nothing more than an SQL database with an API that is receiving metadata\
    \ records when the model is being generated, or a data set has been created, or\
    \ a feature has been updated, and keeps a record for reference. Imagine having\
    \ your model degradation metrics in your Prometheus that are annotated with that\
    \ model version. You can see how it degrades, its version, and even if you're\
    \ doing A/B testing between different model versions, or I don't know, blue-green\
    \ deployment, you want to be able to see how different model versions are behaving.\
    \ Having the ability to track back into the data that were used to produce this\
    \ is important. It\u2019s crucial, but not part of the responsibility of the machine\
    \ learning platform. The data versioning is the responsibility of the data platform\
    \ and this is different."
  sec: 2818
  time: '46:58'
  who: 'Theo:'
- line: This is Data Ops, right?
  sec: 3035
  time: '50:35'
  who: 'Alexey:'
- line: "Yeah, why not. We have been using the data already to build data-driven organizations\
    \ for 15 years, 10 years, build nice visuals, dashboards, and justify decisions\
    \ based on data or even use data to make decisions \u2013 even better. We have\
    \ a lot of development and a lot of progress in the space of data processing.\
    \ So, all these data scientists and data analysts have been using the data platforms\
    \ with data engineers have been doing this thing called \u2018Data Ops\u2019,\
    \ which was brilliant. We are moving on to the next step, let's say, to MLOps\
    \ \u2013 as they are onboarding machine learning models now."
  sec: 3035
  time: '50:35'
  who: Theo
- line: Okay. So, MLOps in a way, is a continuation of Data Ops, which is also, in
    a way, a continuation of DevOps that we had 10 years ago.
  sec: 3035
  time: '50:35'
  who: 'Alexey:'
- line: Or different branches.
  sec: 3045
  time: '50:45'
  who: 'Theo:'
- line: Yes, different branches. Exactly. Because we have data engineers and we have
    ML engineers and each has their own specific set of things they do to become more
    efficient. Right?
  sec: 3046
  time: '50:46'
  who: 'Alexey:'
- line: But I wouldn't be surprised if all of these would merge under one title. We've
    seen the data scientist role becoming the one deity to cover everything.
  sec: 3060
  time: '51:00'
  who: 'Theo:'
- line: Yes, exactly. Well, let's see what happens with the data scientist data, which
    probably will stop existing and at some point, right?
  sec: 3070
  time: '51:10'
  who: 'Alexey:'
- line: Yeah.
  sec: 3080
  time: '51:20'
  who: Theo
- header: Kubeflow in mobile
- line: "There is a question about a demo, but we will not do a demo. This is a podcast,\
    \ which will be released without video, eventually. So, there will be no demo,\
    \ sorry. Philippa is asking. \u201CDo you have any experience in deploying models\
    \ on mobile apps offline? And does it make sense to use Kubeflow in this case?\
    \ If not, what kind of tool exists for this case?"
  sec: 3070
  time: '51:10'
  who: 'Alexey:'
- line: "As far as I'm aware, most of the deployments of these models in the UPS are\
    \ manual processes. However, the good news is that the vendors have realized that\
    \ with the adoption of 5g, mobile devices will become just EDGE devices \u2013\
    \ like a CDN node that's delivering video. So, they are extending Kubernetes into\
    \ EDGE, so a mobile device can be a Kubernetes node that is performing, that is\
    \ running containers. So, we have a data science center in the mobile. [laughs]\
    \ Imagine that."
  sec: 3104
  time: '51:44'
  who: 'Theo:'
- line: "Microsoft, for example, has this Leaf as it\u2019s called, or I don't remember,\
    \ but mobile devices receiving containers. So the scheduler is also considering\
    \ the mobile device to receive a new version of the application or a new version\
    \ of the model. Here we are, as this will become faster and faster, the phone\
    \ line and the phone capability, in terms of processing, will be able to handle\
    \ loads in such a way to serve models, individually. In that, the retraining will\
    \ be even more important, because you will have personalized \u2013 we already\
    \ have personalized models."
  sec: 3104
  time: '51:44'
  who: 'Theo:'
- line: The doorbell model I have for my Nest is personalized, according to the people
    who are coming to my house, and I'm tagging them with their faces. Every time
    I'm tagging the face of someone that's my friend, then the model is detecting
    human needs saying that your friend is at the door and it's telling me his name.
    This model has been retrained so often.
  sec: 3104
  time: '51:44'
  who: 'Theo:'
- line: So, this is something you have in your home, you have this model?
  sec: 3201
  time: '53:21'
  who: 'Alexey:'
- line: "Well, I don't even know how this model works but that\u2019s what I assume.\
    \ It's a ML detection model that is getting an image of someone who's ringing\
    \ my doorbell and it\u2019s saying, \u201COh, this is your wife\u201D, or \u201C\
    This is your kid, Latki.\u201D Every time there is a new face, I have in my list\
    \ of faces, an option to tag them in order to improve the model, or to create\
    \ a new class of a new person that is a new friend of mine, and the doorbell has\
    \ never seen them before. So, if I have this, imagine how this will become more\
    \ and more democratized."
  sec: 3208
  time: '53:28'
  who: 'Theo:'
- line: "That\u2019s interesting. We have a question from Howard. It's not related\
    \ to your doorbell model, but it's also interesting. \u201CDo you think we'll\
    \ see an MLOps manifesto anytime soon?\u201D"
  sec: 3246
  time: '54:06'
  who: 'Alexey:'
- line: "We briefly talked about this. There was a DevOps manifesto and I think the\
    \ equivalent of the DevOps manifesto these days is the two articles of Microsoft\
    \ and Google on the MLOps maturity level or MLOps maturity model. Of course, there\u2019\
    s nice work from the continuous delivery foundation from CNCF, from Williams foundation,\
    \ on the MLOps Roadmap for 2025. So, for the next five years, what an organization\
    \ should do in order to reach the maturity level that is described in the paper\
    \ with details \u201CThis is how you should track fairness, and this is how you\
    \ should retrain the model.\u201D Et cetera."
  sec: 3258
  time: '54:18'
  who: 'Theo:'
- header: The importance of Kubeflow
- line: "Yeah. We will ask you to share the links later, so our listeners can read.\
    \ There is an interesting question that caught my attention. \u201CWould you recommend\
    \ learning Kubeflow?\u201D"
  sec: 3301
  time: '55:01'
  who: 'Alexey:'
- line: "Absolutely. Even for the data scientist, even for the machine learning engineer.\
    \ It's not just using it \u2013 it's about extending it. We've seen so many people\
    \ getting interested in this popular GitHub project called TensorFlow and everyone\
    \ contributed to the implementation of the paper in TensorFlow and PyTorch over\
    \ the last 10 years and especially over the last five years. Why shouldn't we\
    \ see the same in the space of engineering and the same way that we had Airflow\
    \ become so successful in the space of data orchestration, we should have the\
    \ same for ML orchestration. We should have a good representation of engineers\
    \ contributing to the Kubeflow project. So, a welcoming community, 10 meetings\
    \ every week about its different components, and everyone is welcome to join."
  sec: 3313
  time: '55:13'
  who: 'Theo:'
- line: There is also a Slack, right?
  sec: 3372
  time: '56:12'
  who: 'Alexey:'
- line: Yes, of course.
  sec: 3374
  time: '56:14'
  who: 'Theo:'
- line: I think it's quite a large community. I'm also in that Slack. It's almost
    like 5000 people. It's pretty large.
  sec: 3376
  time: '56:16'
  who: 'Alexey:'
- line: Not as large as the Kubernetes community, right? If you go, it's like 6 digits
    already.
  sec: 3387
  time: '56:27'
  who: 'Theo:'
- line: Still. Probably in a couple of years, it will get there.
  sec: 3394
  time: '56:34'
  who: 'Alexey:'
- line: "\u201CWhat do you think makes MLOps easier?\u201D Probably the question is\
    \ like \u201CHow does MLOps help make things easier?\u201D Why should we even\
    \ adopt that and what should we do? Does it make it easier to monitor things,\
    \ to debug? What are the benefits?"
  sec: 3402
  time: '56:42'
  who: 'Alexey:'
- line: I think I briefly mentioned that the technology is still the enabler for progress.
    As we have learned about explainability and anomaly detection, because we have
    tried the serving, that's how we got experienced into other components that we
    were not looking for. When you get exposure to a new tool that is not only giving
    you what you want, but also the other things that you don't know yet. This is
    how you get progress, especially with new tools. This is what makes a technology
    an enabler. MLOps is something you need to adopt as an organization because it
    will help you become a model-driven organization. It will help you replace functions
    that are done manually with automation, or even improve, or even build products
    based on models. There are so many businesses already having model-based products.
  sec: 3424
  time: '57:04'
  who: 'Theo:'
- header: AutoML
- line: "And to have a somewhat related question about that. You also mentioned Katib,\
    \ which is an AutoML tool from Kubeflow. \u201CWill AutoML kill the data science\
    \ role? Is there any risk of that?\u201D"
  sec: 3489
  time: '58:09'
  who: 'Alexey:'
- line: "Well, not \u201Ckill\u201D but \u201Ccommoditize\u201D. Why should we have\
    \ a PhD level expert to tune all these parameters? That\u2019s what we had in\
    \ the past, right? One of the tasks of the data scientist, who was also a PhD-level\
    \ employee, had to search in the space of hyperparameters what the optimal combination\
    \ is that gives him the best results for his model. This has already been replaced\
    \ by the search capability. That didn't send them away from the job. That kept\
    \ them the job and made them more productive. So, data scientists will become\
    \ more productive with AutoML, they will become more productive with ML platforms\
    \ and they will have to worry about more mature problems, like \u201CWhich other\
    \ metrics should I introduce in my fairness detection? Should I also worry about\
    \ how the model is going to perform to data we haven't seen yet?\u201D And things\
    \ like that."
  sec: 3505
  time: '58:25'
  who: 'Theo:'
- line: So, the role of a data scientist is not at risk, unless the only thing that
    the data scientist does is tune in models, right?
  sec: 3576
  time: '59:36'
  who: 'Alexey:'
- line: "In the space of Katib. Remember, we also spent a lot of time in OLX and in\
    \ other companies on deploying. See how easy it is now with KF serving? You just\
    \ say \u201CThis is my S3 location of my model and that's the name of a model.\u201D\
    \ And then bam, you have an API endpoint which you can start consuming."
  sec: 3589
  time: '59:49'
  who: 'Theo:'
- line: "A couple of years ago, we would need to spend at least a week to actually\
    \ build all this \u2013 web service, put the model there, create deployment in\
    \ Kubernetes, create service, secure it, add metrics, then add auto-scaling, and\
    \ then have and SRE sitting there tuning the auto scaling and all that. Now it's\
    \ indeed a lot simpler."
  sec: 3611
  time: '1:00:11'
  who: 'Alexey:'
- line: "And 20 years ago, we needed to order some servers, drag them, and put in\
    \ the cables. I\u2019ve done this, that's why I'm saying it, because I see this\
    \ progress. And that's good to abstract more and more from the work that we have\
    \ been doing in the past and evolve into more high-level tasks."
  sec: 3642
  time: '1:00:42'
  who: 'Theo:'
- header: Team sizes and siloing in companies
- line: "We still have two more questions. Do you have time to answer them? One question\
    \ is, \u201CHow can a small team build fully automated MLOps operations? It seems\
    \ to me like only big teams can do that.\u201D Is this true in your opinion?"
  sec: 3666
  time: '1:01:06'
  who: 'Alexey:'
- line: We have experienced to share about this. Remember? It was a couple of people
    or maybe three people in our organization and your company. We have worked together
    to put like 5-10 models in the KF serving and release it. It took us two hours
    to install it and the deployment was also a few minutes. Just using one part of
    the component is simple and if you want also a full blown, then it depends. It
    will give you the ability to spend more time on it, because it will also give
    you the ability to do more stuff with it. So, if a small team of three people
    is only spending time to build a model and release it and spend time on monitoring,
    imagine how more productive this team would be if they would have all these functions
    already available in the form of services and they would worry about how to speak
    to the business to ask how to improve the model and make it better?
  sec: 3684
  time: '1:01:24'
  who: 'Theo:'
- line: "This is also related to teams \u2013 I see what it's like when teams are\
    \ siloed, or isolated, by different languages, different use cases, manual experiment\
    \ tracking, how would you recommend these teams to start moving in the ML Ops\
    \ direction?"
  sec: 3753
  time: '1:02:33'
  who: 'Alexey:'
- line: "Well, the good news is that these things are language-agnostic. Of course,\
    \ there shouldn't be silos in the organization, especially based on language.\
    \ At least the development departments should be working together. But the tooling\
    \ is already helping with that. It\u2019s another topic. It's the cultural topic\
    \ of MLOps or even DevOps, \u201CHow do you make an organization that is not based\
    \ on silos?\u201D But you will always have the force moving towards that direction\
    \ with silos, because politics play a role and it\u2019s a normal thing for human\
    \ beings to build silos around to protect the area around their territory. But\
    \ the technology is helping here because it's also agnostic to the language."
  sec: 3776
  time: '1:02:56'
  who: 'Theo:'
- line: "For example, the Tekton pipelines or even the pipelines in general, it\u2019\
    s an SDK that is helping you build a YAML definition of the components. That's\
    \ also the difference with Airflow for example. In Airflow, you normally have\
    \ Python, and your tasks should be Python-base and all the tasks should be Python-based.\
    \ In a pipeline that is done just invoking containers, imagine that each container\
    \ can be in a separate language. So, the container that does the data validation\
    \ and built by the data department can be written in Scala and the container that\
    \ is doing the training can be written in Python with PyTorch."
  sec: 3776
  time: '1:02:56'
  who: 'Theo:'
- line: So, this pipeline is invoking those different components, is getting the artifacts
    that are produced from the previous and whatever is subscribed to that is pulling
    it to move to the next step. So, the technology is also helping. If you have a
    siloed organization, as you said in the question, in the form of using different
    languages, that's not a barrier anymore. You don't have to onboard everyone to
    learn Scala or Python.
  sec: 3776
  time: '1:02:56'
  who: 'Theo:'
- line: That's a good thing. We don't have any more questions. So, thank you very
    much for coming today. Do you have any last words?
  sec: 3888
  time: '1:04:48'
  who: 'Alexey:'
- line: No, it's been my as you're talking to Alexey and the audience. I will send
    the links to the maturity models and the roadmap in the chats.
  sec: 3899
  time: '1:04:59'
  who: 'Theo:'
- line: We can share them in Slack and then I'll also put them in the comments in
    YouTube and podcasts. Thanks a lot for coming, for sharing your knowledge, your
    experience with us and thanks, everyone for attending this talk today.
  sec: 3908
  time: '1:05:08'
  who: 'Alexey:'
- line: Thanks, Alexey.
  sec: 3922
  time: '1:05:22'
  who: 'Theo:'

---
