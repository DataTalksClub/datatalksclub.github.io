---
title: "What Researchers and Engineers Can Learn from Each Other"
short: "What Researchers and Engineers Can Learn from Each Other"
guests: [mihaileric]

image: images/podcast/s05e05-researchers-vs-engineers.jpg

season: 5
episode: 5

ids:
  youtube: d9xVXqKq3sU
  anchor: What-Researchers-and-Engineers-Can-Learn-from-Each-Other---Mihail-Eric-e1854bj

links:
  youtube: https://www.youtube.com/watch?v=d9xVXqKq3sU
  anchor: https://anchor.fm/datatalksclub/episodes/What-Researchers-and-Engineers-Can-Learn-from-Each-Other---Mihail-Eric-e1854bj
  spotify: https://open.spotify.com/episode/0cJJCjK7nX5p1PdeMvGrVL
  apple: https://podcasts.apple.com/us/podcast/what-researchers-and-engineers-can-learn-from-each/id1541710331?i=1000537258362

transcript:
- line: "This week, we'll talk about machine learning researchers and machine learning\
    \ engineers. We will also talk about what they can learn from each other. We have\
    \ a special guest today, Mihail. Mihail is a double founder \u2013 he's a founder\
    \ of a machine learning consultancy company that helps with solving tough business\
    \ problems. He's also founder of Confetti.ai, which is an educational platform\
    \ for learning data science and engineering. Before that, Mihail worked as a senior\
    \ machine learning scientist at Amazon Alexa. Welcome."
  sec: 77
  time: '1:17'
  who: Alexey
- line: "Thank you. It's really great to be here. I'm a huge fan of your work Alexey,\
    \ and also DataTalks.Club. I\u2019m really happy to be here."
  sec: 112
  time: '1:52'
  who: Mihail
- header: "Mihail\u2019s background"
- line: Thanks for your kind words. Before we go into our main topic of machine learning
    researchers and machine learning engineers, let's start with your background.
    Can you tell us a few words about your career journey so far?
  sec: 120
  time: '2:00'
  who: Alexey
- line: Sure. I've been in machine learning for about close to a decade now. My entry
    point into machine learning was more from the academic standpoint. I studied neuroscience
    and AI at Stanford. In addition to just ordinary coursework that I did while I
    was there, I had the really great pleasure and fortune of working in the NLP group.
    I worked with a lot of the really big names in NLP in the world, including Chris
    Manning, Zhilin Yang, Chris Potts, and Dan Jurafsky.
  sec: 134
  time: '2:14'
  who: Mihail
- line: One of the first real entry points in the machine learning research that I
    had was actually helping to lead up projects in collaboration with Ford, the big
    car automaker, where we were investigating new methods and primarily neural network-based
    techniques to conversational systems. We were building a lot of new architectures
    and building on new data sets and resources to really tackle this problem of deep
    learning for conversational systems.
  who: Mihail
- line: After Stanford, I joined a self-driving car startup in San Francisco called
    rideOS. I was there as one of the very early employees and got to get that first
    taste of what startup life is like. The focus of the company was actually a lot
    more on building a real-time data platform for optimizing and coordinating the
    movements of fleets of vehicles on the road. It was fundamentally a problem about
    engineering and how we can do things very efficiently.
  who: Mihail
- line: "I was there for a while and when I left, I actually went to help start a\
    \ new team at Amazon Alexa, which I've often described as a bit like a Google\
    \ brain-esque effort within Alexa. It was similar in that the charter of the team\
    \ was to kind of sit at this intersection between research and engineering. We\
    \ did a lot of thinking about what research in conversational systems looks like\
    \ today and how we can contribute to the research. But we were also constantly\
    \ thinking about \u201CHow can a lot of these advances make their way into the\
    \ Alexa platform?\u201D and \u201CHow can we do that effectively so that we can\
    \ deliver customer value?\u201D So really, that was this nice hybrid of both the\
    \ engineering and the research that came together in this nice way while I was\
    \ there."
  who: Mihail
- line: "Then, along the way, as you described, I've always been interested in education\
    \ \u2013 building tools and platforms to help people learn things \u2013 Confetti\
    \ being the most recent example of that. Nowadays, I'm doing a lot of consulting\
    \ and working with a lot of companies across different verticals to help them\
    \ solve their toughest business problems using data-driven and machine learning\
    \ techniques."
  who: Mihail
- header: NLP and self-driving vehicles
- line: That's pretty cool. You worked at Stanford in the NLP group, and then you
    went to a self-driving company. I'm wondering, what does NLP have in common with
    self-driving? How did you convince them to actually hire you?
  sec: 300
  time: '5:00'
  who: Alexey
- line: "That's a question that they would maybe have to answer themselves. [laughs]\
    \ How they picked me, I don't know. But from a problem domain standpoint, I think\
    \ you're right. There doesn't seem to be as much overlap, in some ways. I would\
    \ agree that fundamentally, they're very different problems. Though, I would say\
    \ that, when you think of self-driving compared to NLP \u2013 the difficulty of\
    \ the problems \u2013 they do have very similar characteristics. They're both\
    \ very long tail problems, where a lot of the complexity comes in everything that\
    \ happens after you have achieved 80% accuracy. I think that in NLP, as in self-driving\
    \ vehicles, we can do pretty well on 80% of the phenomena. But really, the hardest\
    \ part is everything that happens at that long tail. So those characteristics\
    \ make them very similar."
  sec: 319
  time: '5:19'
  who: Mihail
- line: "But I think that for me, a lot of what drew me to going into this particular\
    \ company was that the team was just really phenomenal. It was a very high-performance\
    \ engineering team of people that had built a lot of amazing systems at Uber,\
    \ Tesla, Apple, and a lot of different companies. I'm sure we'll get into this,\
    \ but a lot of what I've been thinking about coming out of research was, \u201C\
    How do I become a better engineer?\u201D So I felt like I should just throw myself\
    \ into some really hard engineering problems and work with some really good engineers\
    \ to become a better engineer myself. That was a lot of the motivation there."
  who: Mihail
- header: Transitioning from academia to the industry
- line: Was that your biggest problem when you were transitioning from academia to
    the industry world? Was it the engineering aspects, or was it something else?
  sec: 406
  time: '6:46'
  who: Alexey
- line: "Yes, that's right. I think that when I was at Stanford, we were solving a\
    \ lot of interesting problems. We did a lot of interesting research that I'm really\
    \ happy with. But a lot of the time, when I was working on things, I felt that\
    \ my engineering chops were maybe not at the level where I felt that I was doing\
    \ things as effectively as efficiently as I could. There was an element of, you're\
    \ doing things and you're building things, but maybe at times, even as I was setting\
    \ up some infrastructure, I felt like I was kind of fumbling through it a little\
    \ bit. It's not just that the code wasn't the cleanest \u2013 research code tends\
    \ not to be the cleanest, at least it\u2019s not known to be. That's maybe not\
    \ appealing from an aesthetic standpoint."
  sec: 417
  time: '6:57'
  who: Mihail
- line: "But I think that the bigger problem for me was\u2026 I'm a very relentless\
    \ optimizer in terms of time. I like to do things very efficiently and effectively.\
    \ When I see that there are maybe deficiencies in how I\u2019m doing something,\
    \ I think, \u201COkay, I need to spend the time to really build out that foundation\
    \ and get better in those engineering aspects.\u201D And I start to ask myself\
    \ these questions, \u201COkay, how do I go from a proof of concept model to something\
    \ that can interact with tens of thousands or hundreds of thousands of people\
    \ in a scalable way?\u201D That's something that you don't really get to see in\
    \ research too often, because those aren\u2019t really the problems that researchers\
    \ think about. So making that transition from a very research-minded way of thinking\
    \ about things to \u201CHey, build something that works and is robust.\u201D That\
    \ was really one of the bigger challenges."
  who: Mihail
- line: You mentioned, you were setting some infra as a researcher. I think that's
    quite uncommon for a researcher to set up infra to begin with, right?
  sec: 514
  time: '8:34'
  who: Alexey
- line: "Yeah, that's right. I mean, when I say infra, it's probably not infra in\
    \ the most robust sense. Even just standing up web services and if you're setting\
    \ up an annotation task and you have to interface with Amazon Mechanical Turk\
    \ \u2013 or you have to do any of these things. We were collecting audio data\
    \ and being able to stream audio data over the web was difficult at times. Eventually,\
    \ it got done and it worked. But it was not the cleanest and prettiest thing when\
    \ it did work. So we thought \u201CThere's got to be a better way than this.\u201D"
  sec: 525
  time: '8:45'
  who: Mihail
- line: "So you first worked as a researcher. Then you worked more as an engineer\
    \ in the self-driving startup. Then you joined Amazon to work in a more hybrid\
    \ role \u2013 your official position was ML researcher \u2013 is that right?"
  sec: 561
  time: '9:21'
  who: Alexey
- line: "Yeah, it was a scientist by title. \u2018Scientist\u2019 at Amazon can mean\
    \ a lot of things. I mean, there are scientists that really focus primarily on\
    \ engineering, and there are scientists that are literally just researchers. My\
    \ role was set up in such a way that there was a lot of flexibility in the stuff\
    \ that I was working on, especially because it was a new team. It was literally\
    \ just my manager and I when it was started. Almost by necessity, I had to do\
    \ a lot more engineering. Because when we started, there were just two of us.\
    \ By the time I left, there were maybe 20 or so people in the team. A lot of the\
    \ engineering, setting up of infrastructure, setting up the codebases, and all\
    \ these things, kind of fell on me by default. Although I liked that \u2013 I\
    \ did actually like doing those things. Because of my prior experience in engineering,\
    \ I thought, \u201CWell, this is super fun anyway. Research is fun, but this is\
    \ also fun.\u201D So fundamentally, I ended up doing a lot of both. I wrote a\
    \ lot of papers, but I also built systems that found their way into the Alexa\
    \ platform."
  sec: 576
  time: '9:36'
  who: Mihail
- line: "Yeah, that's pretty cool. So you basically managed to be in both worlds.\
    \ You saw how things are done from the researcher\u2019s point of view and how\
    \ things are done from the engineering point of view. Then at Amazon, you were\
    \ doing both. Right?"
  sec: 634
  time: '10:34'
  who: Alexey
- line: "That\u2019s right."
  sec: 651
  time: '10:51'
  who: Mihail
- header: Machine learning researchers
- line: Maybe you can tell us what machine learning researchers actually do. What
    kind of problems do they solve? What do they use for solving these problems?
  sec: 652
  time: '10:52'
  who: Alexey
- line: "Absolutely, yes. Machine learning researchers tend to focus a lot more on\
    \ open-ended problems. These are open-ended problems from a scientific standpoint.\
    \ There's a way of thinking about things where you don't really know if something\
    \ is going to work, right? Researchers tend to be very hypothesis-driven. They\
    \ will look at something and say, \u201CAlright, how can I improve this through\
    \ some modeling advancement or some architectural change or something like that?\
    \ How can I do that?\u201D And a lot of it does tend to be driven by hypothesis.\
    \ So you don't know if it's going to work upfront, but you run experiments deliberately\
    \ and methodically to try and validate those hypotheses. There's a lot of reading\
    \ of papers, seeing what other people are doing, and then writing the papers when\
    \ you maybe discover something interesting."
  sec: 661
  time: '11:01'
  who: Mihail
- line: "I think as far as tooling is concerned, a lot of the tools that researchers\
    \ in machine learning primarily use, are ones that enable really fast prototyping,\
    \ or really fast validating or invalidating hypotheses. A lot of the usual suspects\
    \ come up \u2013 things like Jupyter-hub notebooks, they come up a lot, tools\
    \ and platforms, like weights and biases \u2013 things that allow you to keep\
    \ a very detailed experimental log that allows you to invalidate or confirm your\
    \ hypotheses."
  who: Mihail
- line: Hypotheses and open-ended problems
  who: Mihail
- line: "Can you think of an example of such a hypothesis? Like what it could be \u2013\
    \ an open-ended scientific problem?"
  sec: 740
  time: '12:20'
  who: Alexey
- line: Yeah, absolutely. The nature of machine learning research today is a lot about
    benchmarks. There are benchmark datasets and things like leaderboards, in some
    cases. There are formal leader boards that come up. But really, there's some community
    agreed-upon dataset that people are trying to improve.
  sec: 747
  time: '12:27'
  who: Mihail
- line: Like ImageNet?
  sec: 769
  time: '12:49'
  who: Alexey
- line: "ImageNet is a good one for computer vision. You can also think of something\
    \ like Squad in the case of question answering for NLP. There are so many. But\
    \ that's really how machine learning research has evolved, by centering around\
    \ these different benchmarks. It's a way of standardizing and making sure that\
    \ everyone's talking in the same language in some sense. You can imagine that\
    \ when you're trying to improve the performance on these datasets, sometimes even\
    \ just by really, really small amounts, you might say, \u201COkay, this model\
    \ uses this one particular kind of architecture. What if I use a special kind\
    \ of cross-attention between maybe the encoder and the decoder of something? Does\
    \ that allow me to maybe propagate some information from the encoder to the decoder\
    \ so that downstream I have an increase in performance?\u201D So you might try\
    \ that. You might build your model in such a way that you try and capture some\
    \ of that signal and then see if it works. It's a lot of thinking-through about\
    \ these different architectures."
  sec: 770
  time: '12:50'
  who: Mihail
- line: So if it works, you publish your paper. And if it doesn't, what happens then?
  sec: 829
  time: '13:49'
  who: Alexey
- line: "Well, then when you're back to square one. Then you're back to the drawing\
    \ board for a lot of the time split. But I think that it doesn't always just have\
    \ to be squeezing out half a percentage point by getting that perfect architecture.\
    \ There are some papers that I've written in the past where we were just showing\
    \ that you can use great simple things to do comparably as well as much more difficult\
    \ architectures. There's even a line of work that's about \u201CHow do I reduce\
    \ the complexity of something without giving up on performance?\u201D That can\
    \ be reducing complexity in terms of the architecture or reducing complexity in\
    \ terms of the model size or anything like that. But yeah \u2013 fundamentally,\
    \ if you can squeeze out percentage points of improvements and you write a good\
    \ story, that ends up being a paper most of the time."
  sec: 834
  time: '13:54'
  who: Mihail
- header: Finding open-ended problems
- line: Where do these open-ended questions come from? Do you have to come up with
    them yourself? Does your professor tell you about them or you work with companies
    from the industry to find them? How do you come up with these problems?
  sec: 885
  time: '14:45'
  who: Alexey
- line: "There are different ways of doing that, I think. In the early parts of every\
    \ researcher\u2019s career, I think it's always very common to start by just serving\
    \ what's out in a field. Nowadays, a lot of researchers have done good jobs of\
    \ literally producing survey papers where they talk about the high-level problems\
    \ that a certain field is talking about. They'll include all the relevant citations.\
    \ If you read these surveys, especially early in my research career, you just\
    \ do what is effectively like depth-first search through the citation landscape,\
    \ right? Where you're like, \u201COkay, here's the paper. Here are a bunch of\
    \ links. I understand this. I don't understand this. Okay, but this links to something\
    \ else.\u201D And you just kind of go down this rabbit hole of \u201CHow are people\
    \ thinking about problems?\u201D And \u201CWhat have they thought about before?\u201D"
  sec: 904
  time: '15:04'
  who: Mihail
- line: "If you do this enough, and then you keep kind of going down this rabbit hole,\
    \ eventually you get a really good sense for \u201CWhat's the state of the art\
    \ look like today?\u201D Sometimes you'll discover that something that you're\
    \ hypothesizing or thinking about that doesn't yet exist. Or maybe you'll see\
    \ that someone sort of thought about something similar in the past, but they maybe\
    \ never fleshed out this one particular detail. So then you think, \u201CWhat\
    \ if I combine what I'm thinking of with what they're thinking of. Can there be\
    \ something new to come out of this?\u201D"
  who: Mihail
- line: "Like this \u2018future work section\u2019?"
  sec: 984
  time: '16:24'
  who: Alexey
- line: "Exactly. Future work section \u2013 a lot of the time. I think that's one\
    \ fantastic aspect of research. If you go right down to the end of a paper, typically,\
    \ they'll have the conclusion and they'll have like three or four open questions.\
    \ They'll just say something like, \u201CHey, we did really awesome work. But\
    \ there are a few things we're not so sure about. So maybe you guys can think\
    \ about this in the future.\u201D That's actually a good place to find motivation\
    \ as well. But then, also, depending on how the researchers that you're working\
    \ with are \u2013 they can also just give you ideas. Especially early in researchers\u2019\
    \ careers, a lot of professors will have their own agendas and kind of a broad\
    \ class of things that they're thinking about. So they're happy to share that.\
    \ Because that's why they hired you, right? In some sense, it was to pursue a\
    \ lot of their own research questions."
  sec: 986
  time: '16:26'
  who: Mihail
- line: "So, you're there on your own. Maybe there are some tips coming from your\
    \ supervisor \u2013 from the professor \u2013 but you're doing this breadth-first\
    \ search yourself, right? You're reading these papers. You're trying to have a\
    \ picture in your mind, \u201CWhat is the state of the art?\u201D It's all on\
    \ you, so you have a lot of independence there."
  sec: 1030
  time: '17:10'
  who: Alexey
- line: "It\u2019s a blessing and a curse, for sure."
  sec: 1052
  time: '17:32'
  who: Mihail
- header: Machine learning engineers
- line: You did this for some time, and then you joined this self-driving startup
    and you worked as an engineer. What do machine learning engineers do? What kind
    of problems do they solve and what do they use to do that?
  sec: 1055
  time: '17:35'
  who: Alexey
- line: "Unlike the sort of open-ended questions that researchers tend to think about,\
    \ machine learning engineers tend to be more focused on the full machine learning\
    \ lifecycle. Whereas a researcher might train a model, and their work is done.\
    \ They might say, \u201COkay, I have my pickle file. I have my binary whatever.\
    \ That's it.\u201D And maybe \u201CI've confirmed and validated a hypothesis.\u201D\
    \ An engineer is really responsible for going to the next step and saying, \u201C\
    Okay, now that I have the model, how do I handle all the other aspects of making\
    \ a fully-fledged system that uses machine learning?\u201D"
  sec: 1073
  time: '17:53'
  who: Mihail
- line: "That systematic aspect has a lot of things that fall under the curve, including\
    \ deployments, \u201CHow do I scalably deploy something? How do I make sure that\
    \ there's uptime? How do I monitor that something is working all the time?\u201D\
    \ A lot of it really does have to do with those engineering aspects. With a machine\
    \ learning engineer, of course, there's engineering that's involved in that. But\
    \ I think that in some sense, the way the field has progressed, the machine learning\
    \ aspect of it has actually become an even smaller part of the role. Nowadays,\
    \ you might only have to use 20% of your time on machine learning, if even that,\
    \ and really 80% of the heavy lifting is the engineering."
  who: Mihail
- line: "So when I think about tooling that falls into an ML engineer\u2019s toolkit,\
    \ there are some of the usual suspects around modeling. You're almost certainly\
    \ going to be using PyTorch or TensorFlow, or some high level modeling library.\
    \ But a lot of your toolkit is also going to involve these more traditional engineering\
    \ tools like Docker to help with reproducibility. Or you have to be very comfortable\
    \ with the cloud provider in order to deal with cloud infrastructure, whether\
    \ that's AWS or GCP, or Azure, or whatever. Then you also have to be very comfortable\
    \ with a web framework \u2013 something like FastAPI or Flask, depending on the\
    \ language that you use for your backend services. So it's really this combination\
    \ of some machine learning. Maybe not as much now as it was before, but then a\
    \ lot of engineering."
  who: Mihail
- line: "Okay. So researchers ask themselves open-ended questions. They come up with\
    \ hypotheses, they test them, and then maybe if it works out, they come up with\
    \ a better architecture. They have this pickle model file, or PyTorch model file,\
    \ or whatever file. I don't know about University, but if it happens in a company,\
    \ they can go to their fellow machine learning engineers \u2013 their colleagues\
    \ \u2013 and say, \u201COkay, we have this file, now let\u2019s figure out how\
    \ to actually deploy this.\u201D Is that right?"
  sec: 1191
  time: '19:51'
  who: Alexey
- line: Yeah, that's right.
  sec: 1223
  time: '20:23'
  who: Mihail
- header: Is data science more engineering or research?
- line: What about data science? What is it? Is it more engineering or is it more
    research?
  sec: 1225
  time: '20:25'
  who: Alexey
- line: "Yeah, that's a really good question. I think data science has changed a lot\
    \ in the last, maybe 8-10 years, maybe 5-10 years. I think that at a high level,\
    \ data science has really gone through different phases. When data science really\
    \ began as a field, I think it was this huge umbrella term. It still is an umbrella\
    \ term, but especially back then. It\u2019s what I think of as \u2018Data Science\
    \ 1.0,\u2019 which is when, all of a sudden, companies and different groups realized\
    \ that there was a lot of data that was coming in that had to be processed in\
    \ some way. That was being combined with the fact that there would be modeling\
    \ advancements, where now people were trying to see \u201CHow can I extract some\
    \ insight from those new data sources that we now have?\u201D But what ended up\
    \ happening, I think, is that people just went on hiring splurges. They just hired\
    \ a bunch of data scientists to \u2018do data\u2019 \u2013 whatever that meant.\
    \ There wasn't really a clear strategy about \u201CWhat does it mean to extract\
    \ insight from data?\u201D And \u201CHow do you do that in a way that actually\
    \ helps a company?\u201D as an example."
  sec: 1231
  time: '20:31'
  who: Mihail
- line: "So that was data science at one point. I think that now we're living through\
    \ what I consider \u2018Data Science 2.0,\u2019 which is where we are starting\
    \ to realize and develop systems for going from extracting the data insights to\
    \ something that's commercially viable and that can deliver value to people. Building\
    \ out that pipeline and building that system is something that we're really refining\
    \ nowadays. A lot of the time it is really more engineering than it is science.\
    \ That's not to say that science isn't there \u2013 there absolutely is science\
    \ there. But it's something where the tools have become so good on the scientific\
    \ standpoint, that now there's really just a lot more of an emphasis on improving\
    \ the tooling on the engineering standpoint \u2013 to make that transition from\
    \ science to engineering more seamless \u2013 and really just setting yourself\
    \ up for success to do that."
  who: Mihail
- line: "I also think in data science, like in research, you often don't know if your\
    \ idea is going to work. So you still have this experimentation aspect. You still\
    \ need to come up with a hypothesis, and then you need to prove that this hypothesis\
    \ works. Maybe come up with a POC and then deploy it. Then you also have the engineering\
    \ part there to show that, \u201COkay, this hypothesis works. Now let's throw\
    \ it out to all the users.\u201D So it's kind of a combination of both worlds."
  sec: 1339
  time: '22:19'
  who: Alexey
- line: "Yeah. I don't think there is single data science or machine learning team\
    \ out there \u2013 even if they're doing something that doesn't seem like it's\
    \ very novel from a research standpoint \u2013 that doesn't have some experimentation.\
    \ Just the nature of doing data-driven machine learning work is such that, even\
    \ if you're just reproducing a paper, you have to run experiments. You're going\
    \ to have to deal with issues of reproducibility, building proof of concepts,\
    \ you know, \u201COh, they say one thing on the paper. I'm not seeing the same\
    \ results here.\u201D There's always this disconnect that happens there. So, you're\
    \ absolutely right. I think that data science just anywhere, regardless of the\
    \ level of sophistication and organization, will involve some level of science."
  sec: 1373
  time: '22:53'
  who: Mihail
- header: What can engineers and researchers learn from one another?
- line: What do you think machine learning engineers and researchers can learn from
    each other?
  sec: 1412
  time: '23:32'
  who: Alexey
- line: "Hey, that's the core of the talk! I think it's a very interesting question,\
    \ honestly. I've worn a lot of different hats in my career, and depending on the\
    \ room that I'm in and that I've been in, you deal with people that think very,\
    \ very differently. There is actually this pretty big disconnect between how scientists\
    \ and researchers think about things and how engineers tend to think about things.\
    \ I think some of the actual problems that I've seen \u2013 sometimes these two\
    \ roles don't really appreciate each other, or what one contributes to the other.\
    \ But I really do believe that in the best of all possible worlds, and the best\
    \ of all possible organizations, they see that the best things happen when they\
    \ work together and collaborate very closely. That's where I've seen the best\
    \ work and the fastest work being done."
  sec: 1418
  time: '23:38'
  who: Mihail
- line: "Concretely speaking, when I look at a researcher \u2013 what does a researcher\
    \ have to learn from an engineer? Engineers tend to think about things in terms\
    \ of very deterministic systems. They build systems that are very robust, and\
    \ that have this very kind of expected predictable path through. There's a lot\
    \ of rigor in how engineers build systems. That's not something that we typically\
    \ think of when we think of researchers. Researchers are sort of more exploratory.\
    \ They think about these ad hoc problems, or they think about, \u201CHey, what\
    \ happens if I do this?\u201D They maybe don't have the same level of structure\
    \ that an engineer will have."
  who: Mihail
- line: "But I think that if you adopt some of the practices around engineering, even\
    \ just the low-level programmatic aspects \u2013 how you code something \u2013\
    \ that involves testing more thoroughly, using things that static typing. I think\
    \ that will make you much more effective. But then I think that engineers are\
    \ also really good at having a very scrappy way of doing things. When engineers\
    \ face a problem, they are very good about saying something like, \u201CAlright.\
    \ Roll up your sleeves. Let's dive into any part of the stack we need to in order\
    \ to solve the problem.\u201D So they really are comfortable going across the\
    \ full stack."
  who: Mihail
- line: "Whereas researchers \u2013 at least a lot of researchers that I've worked\
    \ with in the past \u2013 they sometimes have this mentality of \u201CWell, certain\
    \ problems are beneath me.\u201D And then maybe, like, \u201CI really just think\
    \ about science. I just think about research. I don't really want to think about\
    \ how to spin up an EC2 instance.\u201D Or something along those lines. That's\
    \ just not something they concern themselves with, or even want to concern themselves\
    \ with. But I think that's a pretty destructive mindset, honestly. Because if\
    \ you don't think about these things, and you aren\u2019t comfortable with some\
    \ of these engineering aspects, then you're gonna introduce dependencies in your\
    \ own work. If you're a researcher and you want to do something, you're gonna\
    \ have to use a cloud provider. So if you don't know how to use that, then you're\
    \ gonna have to depend on someone else just to do even the most basic things.\
    \ That'll slow you down. I don't think it's the best way to do things. I think\
    \ adopting some of that scrappiness is really useful for researchers."
  who: Mihail
- line: "On the counter side, I think that researchers have a lot of things they can\
    \ offer engineers as well. Researchers are really good at dealing with situations\
    \ of uncertainty. This is something that happens in machine learning all the time,\
    \ right? We talked about uncertainty in hypothesis-driven research. But even for\
    \ any company that's doing any machine learning, there's a whole lot of uncertainty\
    \ that building machine learning models introduce. \u201CWill it even work? Will\
    \ it work as well as I think it will? I don't know. It's hard to say.\u201D"
  who: Mihail
- line: "But a researcher is incredibly comfortable with that way of thinking about\
    \ things because that's all they do. They think about things in probabilities,\
    \ right? \u201CThere's some chance that\u2019ll work and some chance that it doesn't\
    \ work.\u201D But engineers, especially ones that are classically trained, are\
    \ maybe not super comfortable with that level of uncertainty in their work. They\
    \ really want that kind of strict \u2018if/then\u2019 relationship. It makes sense,\
    \ right? If you deal with engineering systems, you've never asked yourself, \u201C\
    Will I be able to query my database?\u201D Or \u201CWill I be able to write to\
    \ my database?\u201D You just expect that these things will happen. So I think\
    \ engineers can adopt some of that uncertainty-driven way of thinking."
  who: Mihail
- line: "I also think that researchers tend to be better at running experiments than\
    \ engineers. I've definitely worked with engineers in the past where they'll build\
    \ something and they'll sort of run some experiments. Or maybe they'll conclude\
    \ that a model maybe isn't as good as they think it is. They're coming to those\
    \ conclusions because they haven't maybe been as deliberate about hyperparameter\
    \ tuning or refining some aspects of the model, which is something that researchers\
    \ are super good at doing. They maintain very clear experimental logs. They'll\
    \ make sure that when I say \u201CThis hypothesis doesn't work.\u201D You can\
    \ be pretty certain that there are confidence intervals; calculated p-values \u2013\
    \ all these things. So researchers are just really good about being rigorous in\
    \ those aspects of machine learning work."
  who: Mihail
- line: "I remember when I was going from being a software engineer to being a data\
    \ scientist, I really struggled with maintaining this experimentation work. I\
    \ had such a mess and it was just too difficult to find out what's going on. You\
    \ said that \u201CWhat researchers can learn from engineers is structuring your\
    \ projects\u201D which also includes coding \u2013 having some structure there\
    \ will help you have less of a mess in your code. Then you mentioned \u201CBe\
    \ comfortable with stepping outside of your comfort zone.\u201D In other words,\
    \ being able to say \u201CI don't know how to do this.\u201D You can just try\
    \ different things. This way, you don't depend on others. You don't wait till\
    \ somebody comes to you and helps you to press this \u2018create instance\u2019\
    \ button on AWS. That's two things that they can learn."
  sec: 1730
  time: '28:50'
  who: Alexey
- line: "Then what engineers can learn from researchers is: how to handle uncertainty\
    \ and how to be comfortable with uncertainty. It's not always \u2018if/then,\u2019\
    \ right? It's not always a set of strict rules \u2013 sometimes there is uncertainty.\
    \ They can also learn how to be good with experiments \u2013 how to maintain this\
    \ experimentation work. Did I miss anything?"
  who: Alexey
- line: "I think that\u2019s good."
  sec: 1815
  time: '30:15'
  who: Mihail
- header: Bridging the disconnect between researchers and engineers
- line: "You also said that there is a lot of disconnect between researchers and engineers.\
    \ I imagine that, especially if you're at university, you don't always have industry\
    \ partners. You're working independently. You have 100 papers. You're doing this\
    \ breadth-first search there. You kind of start living in your own bubble, right?\
    \ You don't necessarily have this connection with the real world \u2013 how things\
    \ are done in the industry."
  sec: 1816
  time: '30:16'
  who: Alexey
- line: Then when it comes to engineers, they also don't always work with data scientists.
    You also said that either side doesn't necessarily appreciate what the other is
    doing. And that great things happen when you put them in one room. Right?
  who: Alexey
- line: Maybe we can talk about that a bit? So, how can we put them together in one
    room? How can businesses and organizations achieve the best results from their
    efforts?
  who: Alexey
- line: "Yeah. I think it's a hard problem. And it's not one that I think any organization\
    \ has really solved completely. Because part of the work in doing that comes from\
    \ a cultural aspect, right? If you imagine that researchers are accustomed to\
    \ being with other researchers in the same room, or maybe by themselves in their\
    \ own room, and then you have engineers that are so accustomed to working with\
    \ other engineers, \u2013 they really just have fundamentally different ways of\
    \ thinking about things. I do think that there's a certain aspect where leaders\
    \ that oversee these kinds of hybrid organizations do have to make an effort to\
    \ encourage this cross-pollination and make sure that people understand that there\
    \ is value that comes from each of the other organizations."
  sec: 1885
  time: '31:25'
  who: Mihail
- line: "I've definitely been in teams and worked with teams where there really is\
    \ an almost \u2013 I wouldn't say strong resentment \u2013 but there is a resentment\
    \ where an engineer is talking about a data scientist or a data scientist is talking\
    \ about an engineer, and they're just like, \u201COh. What are they even doing?\
    \ They don't really know what they're talking about. They don't even write good\
    \ code.\u201D There are really those types of attitudes sometimes. They're not\
    \ always that toxic, but maybe at a lower level. Sometimes they\u2019re just \u201C\
    Yeah, I don't really get what they do and I don't know how they do it.\u201D"
  who: Mihail
- line: "So I think part of it is cultural. I think that you have to encourage cross-pollination\
    \ within the organization, where you put people in situations where they have\
    \ to work together. I think that different organizations have tried over the last\
    \ 5-10 years of progression of data science and machine learning. They've tried\
    \ different models for how to integrate machine learning into an engineering organization.\
    \ I've seen a number of different models in the places where I've worked. A few\
    \ models that I haven't seen work really well are those where you just silo off\
    \ the researchers from the engineers. They literally create these almost separate\
    \ units. You kind of think, \u201CAlright. Well, maybe they're doing this because\
    \ a lot of places have these strict lines that make it clear what the responsibilities\
    \ are.\u201D And that's great."
  who: Mihail
- line: "But I think that in practice, what ends up happening is you get this, \u2018\
    throw the model over the wall\u2019 kind of approach. You have a researcher that\
    \ builds something, and they're like, \u201CHey, engineer, go handle this.\u201D\
    \ The engineer gets the model, they write some inference code on top of the model.\
    \ They deploy it. The model isn't doing well. Someone starts yelling at the engineer.\
    \ The engineer says, \u201COh, well. I don't know what's going on here. I don\u2019\
    t even know what the model is doing.\u201D It goes back to the researcher. The\
    \ researcher says \u201CWell, your inference code is wrong,\u201D or \u201CDid\
    \ I even give you the right pickle file?\u201D So there are all kinds of latency\
    \ issues and just bad stuff that happens when you really separate these two roles."
  who: Mihail
- line: "And what's worse \u2013 let's say that the researchers wrote the code in\
    \ R, they want to rewrite it in Java. And when you rewrite the code from R to\
    \ Java, things break. Then it's in production, and then the researcher says, \u201C\
    Okay. Well, you know what? This piece of R code is actually \u2013 I have no idea\
    \ what your Java code is doing, but it seems like maybe this part is not correct.\u201D\
    \ Then the engineers think, like, \u201CWhat even is this? Why do you use this\
    \ funny language?\u201D [laughs]"
  sec: 2060
  time: '34:20'
  who: Alexey
- line: "All true. I've seen these things happen. Honestly, some of the funny stuff\
    \ I've seen \u2013 I remember being in a debugging session where we were hashing\
    \ model files to make sure that we were passing the right model files from one\
    \ place to the next. So you're literally looking at the byte representations of\
    \ something to make sure that somebody hadn\u2019t maybe used an earlier version\
    \ of a model or something like that. You know, even funnier stuff like that."
  sec: 2094
  time: '34:54'
  who: Mihail
- line: "But yes, I think that this siloed-off approach is really bad. It reinforces\
    \ the exact disconnects that tend to happen. I think that the far better approach\
    \ that I've seen in organizations, especially from a business standpoint, is when\
    \ the two are just embedded right next to each other \u2013 where you have engineers\
    \ and researchers working together hand-in-hand. This is typically in the context\
    \ of a product. You'll have a scientist and a researcher literally in the same\
    \ room, or in the same office space, working on things. You can imagine that that\
    \ introduces a lot of speed \u2013 there's not as much communication latency.\
    \ There's also a lot more diffusion of knowledge. All of a sudden, researchers\
    \ are seeing answers to things like, \u201CWhat does it mean to actually put something\
    \ into production? What are the things that engineers are doing?\u201D And vice\
    \ versa. The engineers are saying, \u201COh. They're getting more insight into\
    \ what the model is doing.\u201D So really, this hand-in-hand kind of collaboration\
    \ is great."
  who: Mihail
- line: "In the extreme case, I've even seen organizations where even the researchers\
    \ have on-call rotations. On-call being something that engineers hate. I mean,\
    \ no one really likes it, in some sense. But you can imagine a researcher, who's\
    \ so accustomed to working on papers, getting a call at three in the morning because\
    \ the service is down. They\u2019re probably developing a good appreciation for\
    \ what engineers have to go through, if they're sleepy-eyed trying to debug a\
    \ model that is now down. Someone's complaining in a blah-blah part of the world.\
    \ That's a little extreme, but I've seen it happen. And it's maybe not the craziest\
    \ thing in the world."
  who: Mihail
- header: Breaking down silos
- line: "I do agree that the approach with different teams works a lot worse than\
    \ the embedded approach, where it\u2019s one team. What I also saw is, if you\
    \ have an embedded team, you still have tasks that are done by researchers and\
    \ tasks that are done by the engineers. They still form these little silos in\
    \ the team. Does that happen usually? How do you actually make them work together?"
  sec: 2217
  time: '36:57'
  who: Alexey
- line: "Yeah. I think it can happen. And I think sometimes it's a function of the\
    \ leadership as well. The people that are either the product managers or the technical\
    \ managers \u2013 how much are they making sure that there is active collaboration\
    \ going on? People will always default to the thing they're comfortable with.\
    \ I think that's just a human characteristic. People like to do things they're\
    \ comfortable with. But a lot of the time, if you have good leaders, they might\
    \ step in and say, \u201CAll right, something is getting too siloed off. I\u2019\
    ll make sure that there is a very active flow of communication all the time, and\
    \ that there are updates happening.\u201D If you're fostering that collaboration\
    \ as much as you can, then that's where things are most productive. I think it\
    \ can be done well. I've seen the embedded model work incredibly well and incredibly\
    \ high performance teams have come out of the embedded model that I've been involved\
    \ with. It does require deliberate effort on the part of whoever oversees the\
    \ team."
  sec: 2248
  time: '37:28'
  who: Mihail
- line: "Yeah, I imagine that if a team is working in sprints \u2013 let's say a sprint\
    \ is two weeks. \u201COkay, for the next two weeks, the entire team is working\
    \ on checking a hypothesis.\u201D Then the engineers say, \u201COkay, now I have\
    \ to open this Jupyter that I don't like, and experiment with the other side.\u201D\
    \ Then a week later, \u201COkay, now that we have this pickle file, let's \u2013\
    \ everyone together \u2013 deploy.\u201D And then the data scientists say \u201C\
    Whoops. What is this Terraform thing?\u201D Is that right?"
  sec: 2317
  time: '38:37'
  who: Alexey
- header: Fluid roles
- line: "Yeah. [laughs] We joke about it, but I think that's absolutely right. It's\
    \ funny, because there are organizations that don't even specify the roles. Like\
    \ DoorDash \u2013 apparently they don\u2019t specify the exact roles that each\
    \ of their scientists do. They don't specifically pigeonhole people into roles.\
    \ They really just encourage fluidity and the kind of responsibilities that people\
    \ have. You can imagine, in that situation, people end up working on things they\
    \ like to work on, but they are also forced to learn a lot of new things.  Like\
    \ the data scientist who has to learn Terraform or the researcher that has to\
    \ open up a Jupyter hub notebook."
  sec: 2348
  time: '39:08'
  who: Mihail
- line: "Yeah, interesting. In the case of DoorDash, what do they call their employees?\
    \ So they just call everyone engineers? Or do they call them \u2018staff\u2019\
    , or\u2026?"
  sec: 2382
  time: '39:42'
  who: Alexey
- line: "That I don't know. I actually don't know what the titles are. But I do know\
    \ that they are very flexible about their responsibilities. For example, what\
    \ a data scientist works on and what an engineer works on. As I said, they don't\
    \ pigeonhole people into responsibilities. They really just say, \u201CYeah, you\u2019\
    re the data scientist and you want to touch on some production code \u2013 go\
    \ ahead.\u201D I mean, you're gonna feel more motivated when doing it. And you\
    \ probably should take a look at it, because it'll help you. I think that when\
    \ you do that, you get much more diverse and well-balanced ML practitioners as\
    \ a result."
  sec: 2392
  time: '39:52'
  who: Mihail
- header: Full-stack data scientists
- line: We already have a question from Roa about full-stack data scientists. I think
    this is something that I actually also wanted to cover. Maybe we can talk a bit
    about that. What are your thoughts about full-stack data scientists? What are
    they? What do they do?
  sec: 2433
  time: '40:33'
  who: Alexey
- line: "It's an interesting term. I subscribe to it a lot, but I think that in some\
    \ ways, a full-stack data scientist is similar to an ML engineer. I think the\
    \ responsibilities can be very similar. For young machine learning organizations\
    \ \u2013 ones that are really just getting their machine learning efforts started\
    \ \u2013 I think it's important to have someone who can really span the full stack\
    \ of responsibilities. Teams that I've worked with and collaborated with, sometimes\
    \ they'll say, \u201CHey, we're looking to get into data science, so we should\
    \ just hire data scientists.\u201D And I always say, \u201CWell, yes. You should\
    \ have a data scientist. But be careful with the kind of person that you're picking.\u201D"
  sec: 2452
  time: '40:52'
  who: Mihail
- line: "Because you don't want someone who\u2019s just going to say, \u201CHey, here's\
    \ some data. Go deal with some data.\u201D In that \u2018data science point\u2019\
    \ way of thinking about things. You really want someone who feels comfortable\
    \ going from the data science work \u2013 the actual analyzing and building the\
    \ models \u2013 to then ultimately, either doing the deployment and the engineering\
    \ themselves, or is very comfortable interfacing with engineers. My friend, and\
    \ I think he's been on this podcast as well, Eugene, wrote about the full-stack\
    \ data scientist. I very much subscribe to that way of thinking about things."
  who: Mihail
- line: "A lot of the best people I've known are ones that are kind of \u2018jack\
    \ of all trades\u2019 in some sense. That obviously has its pros and cons, but\
    \ being able to make that full transition from one to the other, I think it makes\
    \ you way better-versed in all the problems that come up in deploying a fully-fledged\
    \ data product. So I think the \u2018full-stack data scientist,\u2019 this relatively\
    \ new role \u2013 it's been a few years now \u2013 but somebody who can just handle\
    \ all those tasks from the deployment, as well as those pure machine learning\
    \ aspects [is necessary]."
  who: Mihail
- line: "So are they more engineers because they can just go ahead and do whatever\
    \ it takes to deploy or to test something? But they're also still data scientists\
    \ \u2013 they still need to experiment with different things and maybe be able\
    \ to train a model, whether it\u2019s a regression model, classification model\
    \ \u2013 image classification or visual classification. They can do that as well.\
    \ Maybe they won\u2019t train an NLP model as good as an NLP researcher will,\
    \ but they might have a model that is 80% accurate and then spend the time deploying\
    \ it."
  sec: 2565
  time: '42:45'
  who: Alexey
- line: "You mentioned these NLP \u2018long tail\u2019 kinds of problems and that\
    \ you don't spend a lot of time to get it to 80% of accuracy. Then you spent an\
    \ immense amount of time covering the remaining 20. For the first 80%, you need\
    \ a full-stack data scientist, right?"
  who: Alexey
- line: "Honestly, I think there's a lot of business problems where you maybe don't\
    \ even need the full 100%. A lot of products that I've seen people work on are\
    \ ones where they build assistive data science technology. Ones, where they anticipate\
    \ that they\u2019re never gonna, get 100%. So if they can at least handle 90%\
    \ really well, then they can always find some smart way of doing a \u2018human\
    \ in the loop\u2019 type of thing, where they can defer the stuff that they're\
    \ not as confident about. So you're absolutely right, I would go as far as to\
    \ say that for a lot of business use cases, we don't even need 99.9% exact state\
    \ of the art \u2013 we need maybe 90%, but then something robust around it to\
    \ make it better. That really does take you most of the way there."
  sec: 2630
  time: '43:50'
  who: Mihail
- header: Advice to machine learning researchers
- line: Right. So if machine learning researchers are listening to this conversation,
    would you give them any advice to improve their engineering skills?
  sec: 2676
  time: '44:36'
  who: Alexey
- line: "Absolutely. I always encourage diffusion. I've gone from one to the other\
    \ and back. In some sense, I've gone both directions. I've always felt that when\
    \ I came back, I was just so much more confident in a lot of things. As I said,\
    \ when I came back to Amazon and was in more of this machine learning engineer\
    \ role, I just felt so much more productive at what I was doing \u2013 so much\
    \ faster about iterating on ideas, even from a research standpoint."
  sec: 2692
  time: '44:52'
  who: Mihail
- line: "So I do think that researchers should be deliberate about learning to engineer\
    \ systems well. I think they should take the time to build out those engineering\
    \ fundamentals. That means doing so from an exercise standpoint, even if you just\
    \ do it for yourself \u2013 it doesn't have to be in the business context. It's\
    \ great if it\u2019s in the business context. But even if you're just trying to\
    \ learn on your own \u2013 going through that full pipeline yourself will be very\
    \ informative. So don't just train that model in Jupyter hub. Go to the next step.\
    \ Actually, try and put it onto AWS or whatever cloud provider you\u2019re using.\
    \ Really go through those steps. That's one thing you can do \u2013 just force\
    \ yourself to come to appreciate a lot of those aspects."
  who: Mihail
- line: "Then I think the other thing that I found incredibly useful in different\
    \ contexts, if you're a researcher, get an engineer or someone else to do code\
    \ reviews on your code. I think that's one of the fastest ways to learn a lot\
    \ about how to engineer systems. When you have someone, especially someone that's\
    \ more experienced than you, looking at the stuff that you're writing and telling\
    \ you, \u201CHey, this isn\u2019t great. You can do this a little bit better.\u201D\
    \ Or something like that. The ratio of the time to how much you learn is immense.\
    \ I've gone through so many horrible code reviews in my time and each time I just\
    \ felt like I was getting so much better, like, \u201COh, wow, I didn't even think\
    \ about how to do that!\u201D A lot of engineering lessons were learned that way."
  who: Mihail
- line: "So \u2013 ask somebody to sit down with you and together go through the code\
    \ line by line. Not just \u201CCheck my pull request.\u201D and getting a \u2018\
    looks good to me\u2019 in response. Right?"
  sec: 2817
  time: '46:57'
  who: Alexey
- line: "Yeah, not like when you just want to merge something into master and you\
    \ say, \u201CHey, can you just\u2026?\u201D \u201COkay, fine.\u201D No. Literally\
    \ someone who will \u2018destroy\u2019 your code in some sense. Not literally\
    \ destroy, but I'm saying someone who will constructively help you to build it\
    \ out."
  sec: 2831
  time: '47:11'
  who: Mihail
- line: "Okay. So first, you said \u201CBe deliberate about learning engineering.\u201D\
    \ Don't treat it as an afterthought. \u201COkay, let me first do this hacky thing,\
    \ and then let's see if I ever need engineering.\u201D Then the second thing is,\
    \ \u201CGet somebody to sit with you and review your code.\u201D"
  sec: 2850
  time: '47:30'
  who: Alexey
- line: "That\u2019s right."
  sec: 2870
  time: '47:50'
  who: Mihail
- header: Advice to machine learning engineers
- line: "Likewise \u2013 if there is an engineer listening to this podcast right now,\
    \ what advice would you give to them to improve themselves and be more research-minded?"
  sec: 2871
  time: '47:51'
  who: Alexey
- line: "Yeah. I think that part of building empathy between the two also comes down\
    \ to understanding how researchers think. For engineers, you can take the time\
    \ to even just read some papers and start to see how researchers think about problems.\
    \ You'll immediately start seeing what a researcher\u2019s responsibilities will\
    \ involve and how researchers think about problems. \u201CHow do they think about\
    \ approaches to problems?\u201D Even if you just try to understand the structure\
    \ of a paper, you can see why experiments are done in certain ways and what it\
    \ means to very deliberately and methodically run experiments to validate a hypothesis.\
    \ That's something that engineers that have never read a paper don't really understand,\
    \ like, \u201CWhat does it even mean to really do research?\u201D I think papers\
    \ are a fantastic way to do that."
  sec: 2884
  time: '48:04'
  who: Mihail
- line: "If you really want to go the next step, to really understand how to run,\
    \ how to build, how to do good research, and how to be more research-minded \u2013\
    \ go through the exercise of trying to improve on the state of the art of something.\
    \ Even if it\u2019s unsuccessful \u2013 if you take a state-of-the-art model,\
    \ and you say, \u201CWell, I'm going to try to improve this a little bit.\u201D\
    \ Go through that exercise of trying to add something new to the architecture\
    \ or trying an X, Y or Z thing. It's not just about adding the modeling aspect,\
    \ but going through the process of setting up your system so you can run experiments\
    \ and then keeping track of those experiments. Then going back and saying \u201C\
    Well, maybe this didn't work. How can I add something else?\u201D I think going\
    \ through that exercise, in the same way, that for researchers doing the engineering\
    \ exercise will teach them a lot, going through the research exercise will also\
    \ teach you a lot about uncertainty in work and how you can do things in a way\
    \ where you keep track of things very well and iterating on things constructively."
  who: Mihail
- line: By improving state-of-the-art, I don't think you mean going there and beating
    the first position in ImageNet? You mean something like improving accuracy and
    things like that, right?
  sec: 2992
  time: '49:52'
  who: Alexey
- line: "I mean, that would be great. If you can do that, then more power to you.\
    \ I think just trying to get to the point where you're even just taking a state-of-the-art\
    \ system and fiddling with it a little bit to see, \u201CWhat does it mean?\u201D\
    \ Like \u201CHow hard is it really if I took something off of the transformers\
    \ library?\u201D Which is supposed to be state of the art.\u201D At first \u201C\
    Can I reproduce the state of the art?\u201D and then, \u201CWhat happens if I\
    \ start like adding a thing here and there?\u201D I mean, great \u2013 if you\
    \ can build it and you can train state-of-the-art systems \u2013 that's fantastic.\
    \ Then you may have another job waiting for you somewhere else at DeepMind or\
    \ whatever. But even just trying to pull it and seeing what it means to have a\
    \ state-of-the-art system is also informative."
  sec: 3002
  time: '50:02'
  who: Mihail
- line: "It probably doesn't have to be state-of-the-art worldwide \u2013 it can be\
    \ just within your company. Maybe there is a model, like a recommender system\
    \ or some classification system. You can try to figure out what's going on there\
    \ and how these things work. Maybe you'll notice some things that could be improved\
    \ and then you can come up with a suggestion, and then try to improve it. This\
    \ way, of course, you need to track everything \u2013 track your experiments \u2013\
    \ and then be able to show later to others \u201COkay, I actually tried this and\
    \ it works. Here's the experiment. Let's now integrate this into our system. Let's\
    \ improve it.\u201D Right?"
  sec: 3042
  time: '50:42'
  who: Alexey
- line: "Exactly. That\u2019s absolutely right."
  sec: 3087
  time: '51:27'
  who: Mihail
- header: Reading papers
- line: "Your first point was about reading papers. I remember for me, I was a Java\
    \ developer, and then I got into my Master\u2019s degree \u2013 I was doing my\
    \ Master Thesis \u2013 and then I needed to read papers. I opened this paper,\
    \ and there was a lot of math. The language is so boring and it puts me to sleep.\
    \ That was my impression, I don't know if it's true for everyone. But sometimes\
    \ they are written in a language that makes it sound more complex than it should\
    \ be. Right? So how do you actually go about reading these papers when you don't\
    \ understand half of the symbols in them? Maybe you recognize sigma for sum, but\
    \ for others\u2026? How do you do that?"
  sec: 3088
  time: '51:28'
  who: Alexey
- line: "That's right. Yeah, researchers are definitely guilty of that. Not even from\
    \ a joke standpoint, that's actually very true. This is a whole separate topic\
    \ of conversation around \u201CHow do you get accepted into a conference?\u201D\
    \ And \u201CHow do you maybe inflate something so that it sounds cooler?\u201D\
    \ You add the math to make it seem cooler and more sophisticated than it actually\
    \ is. That's a whole separate topic of discussion."
  sec: 3139
  time: '52:19'
  who: Mihail
- line: "But you're right. I think that, especially if you don't come from that world,\
    \ these papers can be very dense and very difficult to read. There are alternatives,\
    \ though. One really good thing that has happened because of how popular machine\
    \ learning has become, is that people have gotten really good at summarizing and\
    \ trying to create their own understandings of papers. Thus, you have a lot of\
    \ great tutorials \u2013 some of them are interactive tutorials that people have\
    \ written for a lot of models and papers about models. So if something is too\
    \ dense for you in its raw form in the primary source, then there are certainly\
    \ secondary sources that people have done well and explained well."
  who: Mihail
- line: "Then there\u2019s another thing that I think can help. If you're committed\
    \ to going through that exercise, then I would collaborate with a researcher.\
    \ I would pull in a researcher if something doesn't make sense and say \u201C\
    What does this mean? Like, I get the sigma, but can you explain what this is doing?\u201D\
    \ Adding that layer of collaboration will also just be good for team building.\
    \ That's what a researcher is supposed to be good at. They should be able to give\
    \ you insights. As far as the boredom is concerned, that aspect is a bit harder\
    \ to sell [laughs] whether or not you find it boring."
  who: Mihail
- line: "Basically, it\u2019s the same advice for researchers \u2013 pull in machine\
    \ learning engineers, or engineers, to do code review. You can actually apply\
    \ it here the other way. Just get a researcher, try to read the paper together\
    \ and ask them to translate this thing for you. Ask questions. Okay, cool."
  sec: 3247
  time: '54:07'
  who: Alexey
- line: "Also, I think nowadays many papers actually have code, either from the authors\
    \ or somebody who tried to reproduce the results and put the code somewhere there.\
    \ I think that could also be helpful for engineers. Maybe engineers understand\
    \ code better. Although I'm not sure if this code is written by researchers or\
    \ not. If that\u2019s the case, it could be difficult to understand. Probably\
    \ going through the code could be even easier."
  who: Alexey
- line: "If you find a good code base \u2013 absolutely. But a big caveat to the people\
    \ that are listening \u2013 and this is something I've seen in my career and I\
    \ always try to get them out of this mindset whenever I work with researchers\
    \ \u2013 research code is not the best in the world. It can be stale and not updated\
    \ very frequently. So yeah. Good luck. It's almost like if it doesn't work from\
    \ the first go, good luck diving into it and trying to understand what the matrices\
    \ are doing and what each one represents. The translation is a whole separate\
    \ issue."
  sec: 3300
  time: '55:00'
  who: Mihail
- header: "Choosing between engineering or research if you\u2019re just starting"
- line: "Right. Let's say somebody is listening to this podcast, and they're maybe\
    \ doing their Bachelor\u2019s, and they are thinking, \u201COkay, should I go\
    \ to industry and work as an engineer? Or should they go to get a Master\u2019\
    s and then do a PhD and do research?\u201D Do you have any advice for people who\
    \ need to decide what they like more? How should they choose?"
  sec: 3331
  time: '55:31'
  who: Alexey
- line: "Yeah. I think that's where one of the most important things is to be introspective.\
    \ You really have to ask yourself, \u201CWhat parts of these problems am I most\
    \ interested in?\u201D If you understand what each of the roles does \u2013 if\
    \ you understand that, as a machine learning engineer, you'll be handling a lot\
    \ more engineering nowadays. Or if you\u2019re doing a full-stack data scientist\
    \ role, likely, it's gonna be a lot of engineering. If you're aware of those responsibilities,\
    \ then that's important when you choose. But you first have to understand what\
    \ you are getting yourself into in either situation."
  sec: 3356
  time: '55:56'
  who: Mihail
- line: "In one, you're going to be on deployment, monitoring, handling all these\
    \ engineering aspects, maybe a little bit of modeling, but not really as much\
    \ nowadays. Then on the science aspect, you're typically just going to be working\
    \ on open-ended problems, a lot of experiments, the tooling might be a little\
    \ bit different. If you understand that base level, \u201CHere's what each role\
    \ entails.\u201D Then you can ask yourself, \u201CWell, okay. Does one field pull\
    \ me more than the other?\u201D I think in the ideal situation if you're really\
    \ early on in your career, I suggest going and trying and do a little bit of both.\
    \ If you can, that is."
  who: Mihail
- line: "I think that one of the really great things about being at the early part\
    \ of your career is that you have the flexibility to work on internships where\
    \ you can do things that maybe you will never do further on in your career. But\
    \ at least you can see what it's like to do those things. I remember very early\
    \ in my career, I did nanofabrication work in an electrical engineering lab, where\
    \ I was wearing like a Breaking Bad bunny suit, literally growing carbon nanotubes.\
    \ I spent a good four or five months doing that and I was like, \u201CThis is\
    \ cool, but it's not something that I can see myself doing long term.\u201D So\
    \ giving yourself the opportunity to try that, even just for a little bit, it's\
    \ a pretty low-risk way to see if something really resonates with you. And then\
    \ if you can see yourself doing that farther along in your career."
  who: Mihail
- line: "I don't know if this is good advice, but what worked for me was \u2013 I\
    \ did a Master\u2019s, and in Germany Master\u2019s degrees are free. I know that\
    \ in the States that\u2019s not the case. But I needed to write my Master thesis.\
    \ For that, I needed to read a lot of papers, and I needed to experiment a lot.\
    \ By doing this for half a year, I realized that maybe this is not the thing I\
    \ enjoy doing the most. So it could be a way of checking as well. Just go and\
    \ do something. You don't have to do a Master's for that, especially if it costs\
    \ an arm and a leg."
  sec: 3473
  time: '57:53'
  who: Alexey
- line: "Yeah, if you're in an institution that has research labs, I always recommend\
    \ for undergrads to do research, even if it\u2019s just to try it. Most places\
    \ have really good research professors. If you're working with a PhD student,\
    \ they're always happy to have someone help. So if you just go and knock on a\
    \ PhD student\u2019s door and say, \u201CHey, I can code pretty well. Can I just\
    \ do some research with you?\u201D I've rarely seen someone saying no."
  sec: 3511
  time: '58:31'
  who: Mihail
- header: Confetti.ai
- line: "Okay. I know we should be wrapping up, but I have one more question that\
    \ you will probably like. I wanted to ask you a few words about your project \u2013\
    \ Confetti. What is it? What is it for? And what is there?"
  sec: 3536
  time: '58:56'
  who: Alexey
- line: "Yeah. It\u2019s a project that a friend of mine and I started about a year\
    \ and a half ago \u2013 it was born over a dinner conversation once in the Bay\
    \ Area. Really, we came to this conclusion that we have been doing so much interviewing\
    \ and we've gone through so many different parts of our career thinking about\
    \ machine learning and the \u2018right\u2019 machine learning role and data science.\
    \ We found ourselves sort of recreating and reinventing ways of doing things and\
    \ ways of preparing for these things. Between the two of us, we've done hundreds\
    \ of interviews, and every time we found ourselves kind of patching together different\
    \ resources to understand \u201CHow do I prepare for this? What are the kinds\
    \ of questions that are going to be asked?\u201D When it comes to data science\
    \ machine learning rules, there's really not a standardized process for preparing\
    \ for these roles. And that\u2019s not just from the interview standpoint \u2013\
    \ I think the interview sampling is really important and there aren\u2019t a lot\
    \ of good tools to do that. But even just from your career standpoint."
  sec: 3552
  time: '59:12'
  who: Mihail
- line: "Earlier in the conversation, we talked about \u2018Data Science 1.0\u2019\
    \ and \u2018Data Science 2.0\u2019. I saw that transition, of course, in my career\
    \ \u2013 how the role evolved. So Confetti was really like a tool that we built\
    \ to really scratch our own itch and say, \u201CIf I were starting today, what\
    \ would I want someone to tell me about not only \u2018how I get a job in these\
    \ fields?\u2019 but what should I be thinking about going into a career in this\
    \ field?\u201D And \u201CHow do I dispel and share that knowledge with other people,\
    \ so that others can learn from my mistakes?\u201D Which I've made more than my\
    \ fair share of. Confetti was really this platform that we built to try and codify\
    \ a lot of these best practices that we have learned over the course of our time,\
    \ based around \u201CHow do I prepare to be a machine learning engineer? How do\
    \ I prepare to be a data engineer? What are the kinds of things I should be thinking\
    \ about? What are the resources I should be thinking about and using to learn?\u201D"
  who: Mihail
- line: "So far, the reception has been very warm. People have found it very useful\
    \ and people have gotten jobs using this platform, which we're really happy to\
    \ see. But a lot of it is really just about getting people to learn from some\
    \ of the stuff that we've learned. We wanted people to start ahead of us, in some\
    \ sense \u2013 ahead of the point that we were at when we were just bumbling through\
    \ in the early days."
  who: Mihail
- header: Finding Mihail online
- line: That's pretty nice of you to put this together and make it available for others.
    Thanks. So, how can people find you?
  sec: 3700
  time: '1:01:40'
  who: Alexey
- line: Me, personally?
  sec: 3710
  time: '1:01:50'
  who: Mihail
- line: "Yeah, if they want to ask a question or a follow-up question \u2013 stuff\
    \ like that."
  sec: 3711
  time: '1:01:51'
  who: Alexey
- line: "I'm pretty active on Twitter. So by all means \u2013 direct message me on\
    \ Twitter. I\u2019m relatively active on LinkedIn. But, yeah, those are two big\
    \ platforms that come to mind. I have a personal site where I think it's relatively\
    \ easy to get in touch with me. I'm always happy to help people. I really am very\
    \ deliberate about when I get emails or messages \u2013 I will try to answer all\
    \ of them. I do believe in paying things forward. So much of where I\u2019m at\
    \ in my career is just because of the generosity of people's time and the things\
    \ that people have taught me. So, I'm always happy to talk to people that are\
    \ just getting started, want to bounce ideas off of, have questions about how\
    \ to do something \u2013 I'm always happy to talk."
  sec: 3714
  time: '1:01:54'
  who: Mihail
- line: "Thanks a lot. Thanks for coming today. Thanks for sharing your experience.\
    \ That was really great. And thanks, everyone, for joining us today \u2013 for\
    \ watching, for asking questions. I think that's all for today."
  sec: 3756
  time: '1:02:36'
  who: Alexey
- line: Thank you, Alexey. I really appreciate being here. It was a great conversation.
  sec: 3770
  time: '1:02:50'
  who: Mihail
- line: I guess that's it then. Goodbye. Have a great rest of the day and have a great
    weekend.
  sec: 3773
  time: '1:02:53'
  who: Alexey

---

Links:

- [Mihail's Twitter](https://twitter.com/mihail_eric){:target="_blank"}
- <http://confetti.ai/>{:target="_blank"}
