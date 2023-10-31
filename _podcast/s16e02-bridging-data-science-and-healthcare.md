---
episode: 2
guests:
- elenistamatelou
ids:
  anchor: datatalksclub/episodes/Bridging-Data-Science-and-Healthcare---Eleni-Stamatelou-e2aegvc
  youtube: pDOwlulDh0c
image: images/podcast/s16e02-bridging-data-science-and-healthcare.jpg
links:
  anchor: https://podcasters.spotify.com/pod/show/datatalksclub/episodes/Bridging-Data-Science-and-Healthcare---Eleni-Stamatelou-e2aegvc
  apple: https://podcasts.apple.com/us/podcast/bridging-data-science-and-healthcare-eleni-stamatelou/id1541710331?i=1000632040444
  spotify: https://open.spotify.com/episode/5W6lfZVhjIKEmVzBuexfzE?si=0nUHr66eQa6oPVJDb3d0rw
  youtube: https://www.youtube.com/watch?v=pDOwlulDh0c
season: 16
short: Bridging Data Science and Healthcare
title: Bridging Data Science and Healthcare
transcript:
- line: This week, we'll talk about data science in healthcare. We have a special
    guest today, Elena. Elena is a machine learning researcher and educator. She's
    passionate about using data science to improve health care and save human lives.
    Her expertise includes signal processing, deep learning, and data-driven design.
    Welcome!
  sec: 44
  time: 0:44
  who: Alexey
- line: "Thank you. Also, thank you for the invitation to the podcast. I have been\
    \ following some previous podcasts that you did \u2013 some other talks. But I'm\
    \ also glad to meet you like that in life. But I'm familiar with this setting,\
    \ and also seeing you, but not in an interview. [chuckles]"
  sec: 65
  time: '1:05'
  who: Elena
- line: Thanks. [chuckles] And big thanks to Antonis, who recommended Elena. It's
    also not the first guest that he recommended, so thanks, Antonis, a lot. Also,
    the questions for today's interview were prepared by Johanna Bayer. Thanks a lot,
    Johanna, for your help. Yeah, let's start.
  sec: 86
  time: '1:26'
  who: Alexey
- header: "Elena\u2019s background"
- line: Before we go into our main topic of data science and healthcare, let's start
    with your background. Can you tell us about your career journey so far?
  sec: 105
  time: '1:45'
  who: Alexey
- line: "So, as I said, I am Greek \u2013 I was born and raised there. I went to university\
    \ there at the University of Patras. I did electrical and computer engineering,\
    \ which is a five-year Bachelor's and Master's \u2013 a joint degree. During those\
    \ studies, I did Erasmus and I did part of my thesis in Brussels \u2013 I stayed\
    \ there for one year. It was my first international experience. And then I got\
    \ excited\u2026"
  sec: 115
  time: '1:55'
  who: Elena
- line: At which University?
  sec: 148
  time: '2:28'
  who: Alexey
- line: It was VUB (Vrije Universiteit Brussel)
  sec: 150
  time: '2:30'
  who: Elena
- line: So it was a Dutch-speaking university. I studied in the French one.
  sec: 153
  time: '2:33'
  who: Alexey
- line: ULB
  sec: 161
  time: '2:41'
  who: Elena
- line: Yeah, ULB exactly.
  sec: 163
  time: '2:43'
  who: Alexey
- line: "I also did some courses there because I needed to pick up some courses. So\
    \ I also did a bit of ULB. But mainly it was VUB. Then after that, I was excited\
    \ about going abroad, and I applied for an internship at Philips Healthcare in\
    \ the Netherlands. So I moved to the Netherlands. Actually, now, I\u2019ve spent\
    \ the last seven years here and I have been doing different things. The main focus\
    \ is always healthcare. I also worked there at Philips Healthcare after some point."
  sec: 165
  time: '2:45'
  who: Elena
- line: "Then I did the two-year engineering doctorate diploma in data science. That's\
    \ the only thing that was not related to healthcare because we were involved in\
    \ multiple projects and we worked with different companies and organizations.\
    \ But then after that degree, I got back into healthcare again, and I worked for\
    \ a startup \u2013 working on developing monitoring systems for vital signs for\
    \ pediatric patients in Africa. In short, that's my journey, but if you have questions,\
    \ you can ask them and we can go into more detail."
  sec: 165
  time: '2:45'
  who: Elena
- line: How's your Dutch?
  sec: 243
  time: '4:03'
  who: Alexey
- line: It's good [chuckles]. [speaks Dutch] Around B1 level, let's say.
  sec: 245
  time: '4:05'
  who: Elena
- line: Because in the Netherlands, everyone speaks English, so I guess it's very
    difficult to actually learn and practice Dutch, right?
  sec: 254
  time: '4:14'
  who: Alexey
- line: It's true. But I find it interesting and also sometimes useful because some
    things are just written in Dutch or sometimes, I need to search for something
    in Dutch and I can find better results. So that's why I stuck with it a bit. I
    also have a personal interest in learning it.
  sec: 262
  time: '4:22'
  who: Elena
- header: "Some of Elena\u2019s past projects"
- line: "Nice. Well, I have never heard about Philips Healthcare. What I know about\
    \ Philips is that they produce lamps. I have a few smart lamps \u2013 Philips\
    \ Hue. I also know that they produce trimmers (for shaving) but that's pretty\
    \ much the extent of what I know about Philips. [chuckles] I know it's a gigantic\
    \ company and I know that their headquarters is in Eindhoven, right? What does\
    \ Philips Healthcare actually do?"
  sec: 283
  time: '4:43'
  who: Alexey
- line: "They don't make lamps anymore \u2013 they sold the company. Any lamps with\
    \ smart lighting and all those things, it's called Signify. Now Philips is focusing\
    \ on home care \u2013 shaving machines, toothbrushes, and things like that \u2013\
    \ and also health care, but broad care of health: at home, in the hospitals, they\
    \ have MRI scans, they have big machines as well. I did my internship in the C-arm,\
    \ which is like a machine used in the operation room. When I was working at Philips\
    \ Healthcare, I also worked in the pregnancy department. There were two different\
    \ projects focusing on different areas of healthcare. It's a huge company."
  sec: 320
  time: '5:20'
  who: Elena
- line: "From what I understood, it's mostly about different devices that doctors\
    \ use for different things like MRI scans or support integration rooms or things\
    \ like that. [Elena agrees] At your current company, what do you do? You mentioned\
    \ helping people in Africa \u2013 maybe you can tell us more about that."
  sec: 380
  time: '6:20'
  who: Alexey
- line: "I actually left my current company in July. I'm actually now on sabbatical.\
    \ I worked for them for almost two years, focusing more on designing things like,\
    \ \u201CWhat is the future of data science in the company and how can we develop\
    \ data science into the vital sign monitoring system that we were working on?\u201D\
    \ That was actually a system that recorded vital signs, like heart rate, respiration\
    \ rate, etc of pediatric patients\u2026 [cross-talk]"
  sec: 408
  time: '6:48'
  who: Elena
- line: Devices like this? [Alexey points at a wearable health tracker] Wearables?
    Or something more precise?
  sec: 449
  time: '7:29'
  who: Alexey
- line: "It was actually a system for the intensive care unit. But then the difference\
    \ was that we were working on a design for low-resource settings and also a more\
    \ simplified design because sometimes, healthcare professionals there might find\
    \ it more convenient if the device is simpler for them. Actually, a lot of hospitals\u2026\
    \ We were working with Malawi, and a lot of hospitals there don't have monitoring\
    \ systems. I was mainly working on the design because we were involved in a data\
    \ collection process \u2013 we were collecting data and there was this big question,\
    \ \u201CWhat are we going to do with this data and how can we use it to predict\
    \ vital signs for patients and to associate lab tests we were getting to identify\
    \ specific clinical outcomes?\u201D Things like that. But one of my learnings\
    \ there was that it's a very long process, starting from the research part that\
    \ I was mainly focusing on, into really integrating those algorithms into the\
    \ real setting and making it usable for people."
  sec: 454
  time: '7:34'
  who: Elena
- line: "As I understood, the devices are already there \u2013 all the things that\
    \ collect data from patients (all these vitals) are already there and what you\
    \ were doing was thinking, \u201COkay, we have all this data \u2013 how can we\
    \ use it?\u201D"
  sec: 545
  time: '9:05'
  who: Alexey
- line: The devices were also there because we were part of a bigger research project.
    They were installed there for the purpose of the research.
  sec: 560
  time: '9:20'
  who: Elena
- header: Why Elena chose to go into healthcare
- line: Okay. That's quite interesting. You spent a couple of years there, right?
    [Elena agrees] So you started in Philips Healthcare and then you worked in this
    company. Why did you decide to go into healthcare? Why did you decide to choose
    this field?
  sec: 574
  time: '9:34'
  who: Alexey
- line: Before choosing and going into engineering, I had this big question whether
    to go into studying to be a doctor or to go into engineering. I went with engineering
    because I was into math. When the time came to decide on what kind of thesis I
    wanted to do, the only topics that I found most interesting were topics related
    to healthcare because I found that there is a greater direct impact on people.
    I still remember, for example, that there were some projects on developing games,
    and I found that, for me, personally, it was not impactful. So I choose to do
    that. Indeed, it was true that I felt that my work went into something that could
    impact people's lives.
  sec: 598
  time: '9:58'
  who: Elena
- line: What was your thesis topic?
  sec: 659
  time: '10:59'
  who: Alexey
- line: "I worked together with IMEC, which is a Belgian Research Institute. There,\
    \ we were working on\u2026 I had images from white blood cells and I was analyzing\
    \ those images with basic, conventional image processing methods. The main goal\
    \ was to classify those images into subcategories of white blood cells. That was\
    \ part of a bigger project because they were working on the development of a cell\
    \ sorter machine. With this machine, they wanted to filter people\u2019s blood\
    \ and classify the blood cells into \u201Cgood cells\u201D and cancerous cells.\
    \ They wanted to filter out the cancerous cells. I was just working on a small\
    \ part of this project \u2013 on the white blood cells."
  sec: 663
  time: '11:03'
  who: Elena
- line: "I was going to ask, \u201CWhy exactly do you need to categorize cells?\u201D\
    \ But you answered that \u2013 if the cell is cancerous, you don\u2019t want to\
    \ have it there."
  sec: 732
  time: '12:12'
  who: Alexey
- line: Yes. They wanted to prevent the metastasis of cancer into other tissues.
  sec: 744
  time: '12:24'
  who: Elena
- line: "Yeah, that does sound very impactful. For you, as a student working on I\
    \ think like that\u2026 I can see why it was very interesting. You worked on this\
    \ Master\u2019s thesis and then the company\u2026 You did some models, and then\
    \ the company integrated this into their sorting mechanism, right? [Elena agrees]\
    \ That's pretty cool. So you really liked this topic and then you started researching,\
    \ \u201COkay, where can I go next?\u201D And then you found Philips Healthcare.\
    \ Is that right?"
  sec: 753
  time: '12:33'
  who: Alexey
- line: Yeah. And there, I worked on a topic that was not really related to data science.
    They have this C-arm, which is in the shape of a C, like that [Elena shows the
    shape of the letter C with her hand] and on the top of this arm, there are four
    cameras. Here [points to thumb] it's the bed of the patient. Those four cameras
    take [photos of the patient from] different perspectives and different angles.
    My task there was to take those four images, calculate the geometry, and create
    the 3D object representation of the patient.
  sec: 793
  time: '13:13'
  who: Elena
- line: Well, it still sounds very mathematically heavy, right?
  sec: 837
  time: '13:57'
  who: Alexey
- line: Yes! [chuckles] It was very mathematically heavy. Not like machine learning
    and those things, but it was, yes.
  sec: 841
  time: '14:01'
  who: Elena
- line: Do you know if this problem is being solved these days with machine learning
    (with neural nets)?
  sec: 848
  time: '14:08'
  who: Alexey
- line: I'm not aware of this.
  sec: 857
  time: '14:17'
  who: Elena
- header: 3D imaging and healthcare metric tracking
- line: "Because I saw\u2026 It's not related to health care at all, but I saw some\
    \ demos where people were going around Berlin (or other different cities) taking\
    \ pictures. Then there is a model or something that just takes all these images\
    \ and creates a 3D model of these things. It looked really impressive \u2013 what\
    \ they could do with just a few images."
  sec: 859
  time: '14:19'
  who: Alexey
- line: "I'm sure that machine learning can probably help with the challenges of these\
    \ computational methods. For example, sometimes we had occlusions, which means\
    \ that\u2026 When there was no object between the cameras, it was easy to reconstruct\
    \ a 3D object, but when we had a surgical object, it was harder to create the\
    \ shape of the 3D model. This computational method was not really tackling this\
    \ challenge. But machine learning can probably create a better graphical model.\
    \ [Alexey agrees]"
  sec: 886
  time: '14:46'
  who: Elena
- line: Okay. But it was still quite mathematically heavy and then, eventually, after
    working on this 3D reconstruction, you probably continued work in these data science
    areas, right? Also in Philips?
  sec: 928
  time: '15:28'
  who: Alexey
- line: "Yeah, I worked as a data analyst afterward, on a project that was a research\
    \ project. Again, because I mainly worked in research all those years. We were\
    \ actually collecting data from pregnant women. That project was directed\u2026\
    \ The users were midwives. They wanted to see how pregnant women are doing at\
    \ home. So it was homecare \u2013 and the pregnant women were weighing themselves\
    \ every day, they were wearing a smartwatch that calculated their heart rate.\
    \ This was important information for the midwives because it's also very important\
    \ during the pregnancy \u2013 to see how much weight the pregnant woman is gaining\
    \ because it needs to be within certain limits. I was working as a data analyst\
    \ there on developing a dashboard, visualizing this information for the midwives\
    \ in a user-friendly way. We were calculating this because we were getting a lot\
    \ of feedback from them on what is useful for them to see and what is not. It\
    \ was quite interesting. I really liked that I was getting feedback from them,\
    \ and we were creating it together."
  sec: 943
  time: '15:43'
  who: Elena
- line: "I'm trying to look at what we discussed so far. First, your thesis was about\
    \ cell classification for a cell sorter. Then you worked with this 3D reconstruction.\
    \ Then [there was] the thing you just described \u2013 it was more not for the\
    \ operation room (not for a hospital) but something you wear at home, for pregnant\
    \ women. I\u2019m wondering\u2026 These areas appear quite different from one\
    \ another. They're different. I'm wondering if there is any area of healthcare\
    \ that you're more interested in or if they're all equally interesting to you."
  sec: 1035
  time: '17:15'
  who: Alexey
- line: As you said, they're quite different from one another. Also, if you consider
    the projects I work on later, they're also quite different. But they have a common
    theme in that the things that you're looking at when you're working are healthcare
    data. But personally, what I find interesting is to work on the research side
    of healthcare, because I like the novelty of creating new ideas. Another common
    thing that I find interesting is to work on projects that also have the potential
    for clinical application, or that they're already tested in a real-world setting.
  sec: 1085
  time: '18:05'
  who: Elena
- header: Making an impact and signal processing
- line: "So, there is no specific area \u2013 you focused more on \u201CCan I make\
    \ an impact now? Can I publish a paper?\u201D Or \u201CWill they think I work\
    \ on go and affect lives after I finish?\u201D It must be really cool to see things\
    \ that you work on in action, right?"
  sec: 1140
  time: '19:00'
  who: Alexey
- line: Yes. It's quite rewarding.
  sec: 1157
  time: '19:17'
  who: Elena
- line: You published a few research papers, right? What were these papers about?
  sec: 1162
  time: '19:22'
  who: Alexey
- line: "During the period when I was working for this company where we were working\
    \ on vital sign monitoring systems in Africa, I was working on\u2026 It is called\
    \ ballistography signal data. It's a novel signal\u2026 I'm thinking of how to\
    \ explain it to make it easier for people. This signal is meant to replace the\
    \ electrocardiography signal. In simple terms, if a patient is in the intensive\
    \ care unit, they just put the electrodes on the patient, and they need to have\
    \ the electrodes there for many hours, which could be tiring for the patient since\
    \ the patient cannot move around. Meanwhile, this sensor is actually a mat that\
    \ goes below the patient's bed, which records the signal of the movement, including\
    \ the movement that comes from the respiration rate and the heart rate. I was\
    \ working on that \u2013 I was using the ballistography signal and the electrocardiography\
    \ signal as a reference, and I was trying to remove the noise from the ballistography\
    \ signal and extract the vitals from there. So that was a novel application."
  sec: 1168
  time: '19:28'
  who: Elena
- line: "So if I understood correctly, there is a method that is more\u2026 not intrusive,\
    \ but annoying \u2013 and inconvenient method \u2013 when the patient is covered\
    \ with all these electrodes. It's not convenient. Then there is a less annoying\
    \ method, which is just placing a mat under the patient. What you were doing was\
    \ trying to use machine learning to go from the signal noisier signal to a more\
    \ accurate signal. Right? [Elena agrees] That\u2019s awesome."
  sec: 1276
  time: '21:16'
  who: Alexey
- line: Yes. You have the estimation of the heart rate and respiration rate. For the
    respiration rate, I used more conventional signal processing approaches, because
    it's simpler to estimate the respiration rate since you get a much stronger signal.
    But then for the heart rate, it was much more challenging and that's why we went
    into deep learning. Also, I have the approach that if we can solve a problem with
    basic signal processing, then it's much better to do it like that. And if we need
    to use something more advanced, then we can go into deep learning machine learning
    techniques.
  sec: 1309
  time: '21:49'
  who: Elena
- line: What is basic signal processing? Is this like the Fourier method? Something
    like that?
  sec: 1349
  time: '22:29'
  who: Alexey
- line: "Yes. Filters, Fourier methods \u2013 yes. I focused on the frequencies of\
    \ the respiration rate that we were interested in. Of course, there were some\
    \ challenges because we had to deal with pediatric patients, which meant weaker\
    \ signals and more movement. We also had the challenge that sometimes the frequencies\
    \ of the respiration rate and the heart rate can overlap and then it's hard to\
    \ make out what is what. But yeah, it's very interesting research, I think."
  sec: 1355
  time: '22:35'
  who: Elena
- line: "I see that you shared a link to one of your publications, which is \u201C\
    A U - Net Deep Learning Model for Infant Heart Rate Estimation from Ballistography\u201D\
    . That's the paper you're talking about?"
  sec: 1395
  time: '23:15'
  who: Alexey
- line: Yeah. This is the paper where we were estimating the heart rate. We used this
    U net, which is actually used for object segmentation in images, but in this case,
    we used it for the signal because, in the ballistography signal, there is a very
    distinct pattern for the heart rate. Our focus was to identify this distinct pattern
    in the signal.
  sec: 1411
  time: '23:31'
  who: Elena
- line: "Quite interesting. I'm looking at the paper \u2013 well, not at the actual\
    \ paper but more at the Research Gate website. we will definitely put the link\
    \ in the description so people can check it out. There are a lot of words I don't\
    \ understand, like \u201CBSG waveform\u201D. It's quite an interesting read. Okay,\
    \ thanks. You probably wanted to talk about some other papers or some other research\
    \ before we move on, right?"
  sec: 1446
  time: '24:06'
  who: Alexey
- line: "This is my first publication. But then I also published a poster that is\
    \ not available online. It was about calculating a patient\u2019s score based\
    \ on the vitals of the patient. The main idea behind this was to have an overall\
    \ assessment of the health status of the patient so that healthcare professionals\
    \ can have an idea of how critical the patient is."
  sec: 1483
  time: '24:43'
  who: Elena
- header: The challenges of working in healthcare
- line: I already see quite a few questions, and this is actually one of the questions
    we also have for this interview. It is about the challenges of working in healthcare.
    It's quite a regulated field, right? I guess there are a lot of privacy concerns
    and things like that. So what are the typical challenges of working there?
  sec: 1523
  time: '25:23'
  who: Alexey
- line: Yes, one is getting regulatory approval, including algorithms, and machine
    learning algorithms in the devices. The reason behind that is that it's like a
    black box. Of course, it's sometimes hard to understand why a machine learning
    model predicts a specific outcome. There, a lot of work needs to be done in the
    Explainable AI part, how we can give an explanation of why the algorithm predicts
    a specific outcome. This field of AI is still in a very early stage. I think the
    more this field is developed, the more trust there will be from the side of the
    healthcare professionals, and also from the people who approve the devices to
    be used in hospitals.
  sec: 1553
  time: '25:53'
  who: Elena
- line: "Another challenge is a lack of data sometimes or a lack of consistent data.\
    \ In real datasets, a lot of the time, we see that there are many data gaps. This\
    \ makes it hard for algorithms to take the inputs properly. Sometimes we need\
    \ to make assumptions on what kind of data we would expect for that patient. But\
    \ then, still, this is also not always the way to go. So that's a problem. Another\
    \ big problem is that oftentimes the data is being collected without having in\
    \ mind what kind of a use this organization wants to perform with this. For example,\
    \ one common problem is a lack of annotations \u2013 they say we want to do a\
    \ predictive algorithm for a specific clinical outcome, but then the proper data\
    \ annotations for this outcome are not there."
  sec: 1553
  time: '25:53'
  who: Elena
- line: "What kind of outcomes? Is it like whether a patient is going to have a stroke\
    \ \u2013 things like that?"
  sec: 1687
  time: '28:07'
  who: Alexey
- line: "Yeah. In my previous research, I was working on estimating sepsis, let\u2019\
    s say, based on the vital signs of the patient, and also the clinical data."
  sec: 1692
  time: '28:12'
  who: Elena
- line: "I don't know if I want to Google what sepsis is. Ah, \u201CSepsis is the\
    \ body's extreme response to an infection. It is a life-threatening medical emergency.\u201D\
    \ So I guess you want to predict that this thing is about to happen \u2013 you\
    \ want to act as fast as possible, right?"
  sec: 1706
  time: '28:26'
  who: Alexey
- line: Yes, because the faster you act on that, the more chances you have to treat
    it.
  sec: 1728
  time: '28:48'
  who: Elena
- line: "I guess that's why Explainable AI is very important, because if the algorithm\
    \ predicts, \u201CHey, this patient is going to have sepsis.\u201D And the doctor\
    \ looks at the patient and thinks, \u201COkay, they look normal.\u201D They need\
    \ to understand why exactly the algorithm (this model) thinks that there is a\
    \ problem. Maybe if the doctor understands that, they can think, \u201COkay, yeah.\
    \ Now it makes sense. Let's perform a few checks.\u201D Right?"
  sec: 1736
  time: '28:56'
  who: Alexey
- line: "What I think about this topic is the approach that should be taken for the\
    \ algorithms \u2013 it needs to be used as a tool for decision-making. The algorithms\
    \ are now not on a level to do the decision-making. That's why we need to be careful\
    \ with that. It's just a tool to help the doctors assess a situation. What I've\
    \ seen is that people tend to really go far ahead and say, \u201CWe want to predict\
    \ what the patients have. We want to give advice on what the doctor should do.\u201D\
    \ However, I think a more data-driven approach needs to be integrated slowly into\
    \ the hospital setting by just, in the beginning, giving some recommendations\
    \ or even saying, \u201CThere's a 60% chance that this patient might have this\
    \ kind of disease.\u201D To make the doctors aware that this is not a certainty\
    \ \u2013 they just need to look more at that."
  sec: 1765
  time: '29:25'
  who: Elena
- line: "So it's more to gain trust from the doctors (from the medical personnel)\
    \ that they see, \u201COkay, this model is actually making our lives simpler.\
    \ Now we trust it.\u201D Then it could be integrated into their workflow more\
    \ and more. Right?"
  sec: 1825
  time: '30:25'
  who: Alexey
- line: "Also, what I think is that sometimes even just data visualizations of historical\
    \ data \u2013 what happened to similar patients in the past \u2013 can already\
    \ be helpful, without any predictions. Then this is more data science and not\
    \ machine learning \u2013 just making doctors more aware of what happened in the\
    \ past."
  sec: 1843
  time: '30:43'
  who: Elena
- header: Jumping over hurdles, gaining trust, and collecting feedback
- line: "You spoke about these regulatory approvals, and I imagine that these things\
    \ make it very difficult to\u2026 Let's say you\u2019re working on a thesis or\
    \ you're working on a model and the time comes to actually \u201Cship this model\
    \ to production\u201D \u2013 this process of actually bringing this model and\
    \ algorithm from research to production could be quite challenging, right? There\
    \ is also a question from David about this, \u201CHow difficult is it to come\
    \ up with a solution that is actually used in the field?\u201D There are some\
    \ political barriers that might appear along the way. How difficult is it and\
    \ how do you usually solve these problems?"
  sec: 1870
  time: '31:10'
  who: Alexey
- line: "What we were doing was getting a lot of feedback from the healthcare professionals\
    \ on what they needed \u2013 from the doctors, from the nurses \u2013 because\
    \ they were also using the vital sign monitoring system. But indeed, the regulatory\
    \ approval part is a very big challenge. There are also other people involved\
    \ that are experts on that. Asking those people what the way to go is can be helpful\
    \ for bringing those things into production. Oftentimes we have the application,\
    \ but it gets stuck \u2013 it might take five years to be used in a hospital.\
    \ [cross-talk]"
  sec: 1922
  time: '32:02'
  who: Elena
- line: "I guess, in this case, what you want is doctors to also actively advocate\
    \ on your behalf, saying, \u201CLook, this thing is really useful. We want to\
    \ have it.\u201D Like you said, you want to get feedback from these healthcare\
    \ professionals. Because if the feedback is positive, and they clearly see the\
    \ value in this thing, they help you \u2013 right?"
  sec: 1976
  time: '32:56'
  who: Alexey
- line: "Then they also trust it more. There is also a lack of trust sometimes. There\
    \ is also this approach that people have, where they don't want to try something\
    \ new. They say, \u201COh, no. We already work with this.\u201D And they don't\
    \ want to change to something else."
  sec: 2000
  time: '33:20'
  who: Elena
- line: So you need to find doctors (or healthcare professionals) who are a little
    more open-minded than others, right? [Elena agrees] That can be difficult. [Elena
    agrees]
  sec: 2018
  time: '33:38'
  who: Alexey
- header: Convincing professionals to try new things
- line: "I see that there is a comment from Sylvia. \u201CThanks, Eleni, for sharing\
    \ your experience. How advanced and trusted is data science in healthcare compared\
    \ to other sectors?\u201D For example, I worked in e-commerce, and I think in\
    \ e-commerce, people already know that they have to have a recommender system.\
    \ That\u2019s the default, so it is automatically trusted. \u201CWe know that\
    \ machine learning and data science will help e-commerce, so let's use it.\u201D\
    \ There are usually no questions asked. But in healthcare, as you said, people\
    \ are not willing to try new things, it's not always clear what exactly it brings,\
    \ and there are also the regulatory approvals, which might be difficult. I imagine\
    \ that maybe the data science there is less advanced than in other fields. Is\
    \ it the correct assumption?"
  sec: 2034
  time: '33:54'
  who: Alexey
- line: "It\u2019s true. There's also something. Like you said, you worked in e-commerce,\
    \ and everything is digital there. You can have a lot of data \u2013 you can track\
    \ what customers are doing. In the hospitals, it's not like this. Sometimes you\
    \ have data, but you don't have the timestamp of when this happened, or you have\
    \ a timestamp that might be wrong, so then you need to assume that \u201CThis\
    \ happened around this time.\u201D There are a lot of things that happen offline,\
    \ which makes the data less accurate. From the beginning, that's already a difficulty.\
    \ Of course, the second thing is that the impact of a prediction can be much bigger\
    \ \u2013 if an e-commerce client gets a wrong recommendation, what's the worst\
    \ thing that can happen?"
  sec: 2088
  time: '34:48'
  who: Elena
- header: How data science will evolve in the healthcare field
- line: Exactly. They just would not buy the things and continue living their life.
    Meanwhile, in healthcare, it can sometimes actually be a matter of life and death.
    How do you think this will evolve? Do you think it will get more trust in the
    future? Are there successful use cases, studies?
  sec: 2145
  time: '35:45'
  who: Alexey
- line: "There is a lot of research and investment in that. I think that already means\
    \ that they are going to become better. There is also a reason why there is no\
    \ trust \u2013 it's not that this field is not really evolved and the predictions\
    \ are not always to be trusted. There is a lot of research. Also, that means that\
    \ we have data from different populations \u2013 because that's also a problem.\
    \ What also I noticed during my previous work experience is that we were collecting\
    \ data from Africa, but there is not a lot of data for Africa. We cannot use an\
    \ algorithm that we developed in Europe (with European patients) for African patients.\
    \ I think, with time, we will have data from different populations and then the\
    \ algorithms will become better in that. So I see there is a lot of potential,\
    \ that's why I'm also motivated to contribute to that. But I think, even if AI\
    \ or generative AI is really advanced \u2013 AI is not really advanced in all\
    \ the fields in society. There are still fields that need a lot of work to be\
    \ done."
  sec: 2172
  time: '36:12'
  who: Elena
- line: "One of the points you mentioned is that you can\u2019t just easily take data\
    \ collected in Europe and use it for Africa, which makes sense, but also not exactly\
    \ intuitive when I first think about this. On one hand, people are people \u2013\
    \ everywhere \u2013 but then there are probably things like the living conditions\
    \ that are different, the climate is different, etc. So why can't we just take\
    \ data from Europe and use it for Africa? What are the reasons?"
  sec: 2260
  time: '37:40'
  who: Alexey
- line: "One thing is that in Africa, there are more malaria patients, for example,\
    \ than in Europe. What I want to say is that there are also sometimes different\
    \ diseases in people based on the location where they live. That's why it's important\
    \ to take those things into account. Also, in different settings \u2013 maybe\
    \ in Europe, it's easier to collect data for every single metric of the patient,\
    \ but in Africa, this is not possible. You have limited data collected, and you\
    \ need to make a decision based on that as well."
  sec: 2288
  time: '38:08'
  who: Elena
- line: I imagine that an average person who lives in Norway is probably very different
    from an average person living in Nigeria.
  sec: 2327
  time: '38:47'
  who: Alexey
- line: Yeah, they have different lifestyles, different [inaudible].
  sec: 2345
  time: '39:05'
  who: Elena
- line: Interesting. But still, is this European data not useful at all?
  sec: 2349
  time: '39:09'
  who: Alexey
- line: "Mmm\u2026 We need to be careful when we do these kinds of things. But it\
    \ can also be useful maybe for drawing some conclusions for us \u2013 but not\
    \ really for developing an algorithm to apply in low-resource settings."
  sec: 2358
  time: '39:18'
  who: Elena
- header: The issue of automating away human jobs
- line: "Okay. So you need to think \u201COkay, for this specific feature or dataset,\
    \ are there any problems that might occur? Is there something that makes the way\
    \ the data was collected in Europe different from the data that was collected\
    \ in Africa? Can we actually use it?\u201D For each specific case, you need to\
    \ think about that, right? [Elena agrees] While we were talking about integrating\
    \ the solutions (the algorithms) \u2013 bringing them from research to production\
    \ \u2013 there is some pushback from people who don't want to try new things.\
    \ I remember, even in e-commerce settings, as I was working with moderation teams\
    \ in the past, there were some moderators that were thinking, \u201CNow these\
    \ data scientists come, create machine learning models, this AI will automate\
    \ our jobs and will become redundant. So, let's not help them.\u201D I'm not saying\
    \ that people were explicitly saying that there, but I sensed this sentiment."
  sec: 2377
  time: '39:37'
  who: Alexey
- line: "My job as a data scientist was also to educate them and say, \u201CHey, we\
    \ are not going to make you redundant. We are not going to fire you. We actually\
    \ want to help you be more effective.\u201D I wonder, is there something similar\
    \ that you see in healthcare? Maybe there is this lack of trust that comes from\
    \ these healthcare professionals because they think, \u201COkay, now my job will\
    \ be automated. There will be these sensors that monitor the patient's condition.\
    \ So why am I needed there? I won\u2019t be needed anymore, so I will not try\
    \ to help you. Why would I help you make myself redundant?\u201D"
  sec: 2377
  time: '39:37'
  who: Alexey
- line: I have not seen it because they still have a lot of impact in decision-making.
    Those algorithms are not too far ahead. For now, I think they probably don't feel
    that their job is at risk. Maybe in the further, further future, but for now,
    I have not seen anything like that. What I personally believe is that, by the
    time that AI will become more developed, this is an actual risk. It already happens
    with some jobs.
  sec: 2488
  time: '41:28'
  who: Elena
- line: For example, in the Netherlands, there are many supermarkets that have automatic
    cashier machines. Before, people were working there, and now just one person observes
    if everything is going right. This is simple automation, but in the future, more
    complex decision-making processes can replace humans. Okay, I know the viewpoints
    on this topic are controversial sometimes. [chuckles]
  sec: 2488
  time: '41:28'
  who: Elena
- line: I mean, maybe the cashiers who worked and were replaced by machines can now
    do something else in the same store. They don't need to do this monotonous work
    every day. Maybe it's actually a good thing. But we don't know what happened with
    the cashiers, right? [chuckles]
  sec: 2562
  time: '42:42'
  who: Alexey
- line: Yeah. But let's see. I'm also curious how this thing is going to be developed.
  sec: 2581
  time: '43:01'
  who: Elena
- header: The challenge of data collection and storage in healthcare
- line: "I see that there is a comment about India, \u201CIn smaller cities, data\
    \ is not created properly, especially in healthcare.\u201D Even in Germany \u2013\
    \ it's such a mess, to be honest. [chuckles] Germany is a pretty advanced country,\
    \ but when it comes to healthcare, it's so decentralized \u2013 all the different\
    \ doctors\u2019 offices have their own methods of collecting data. It's quite\
    \ messy."
  sec: 2590
  time: '43:10'
  who: Alexey
- line: "Yes, this is true. [chuckles] But I think there is a lot of work that is\
    \ being done on organizing the systems. Also, I think the healthcare system in\
    \ the Netherlands\u2026 When I came to the Netherlands, it was much less organized.\
    \ Now, they have patient files, and they can just send your electronic file to\
    \ another hospital. When I initially came, those things were less automatic and\
    \ less connected. So, yes, there are people that are working on standardizing\
    \ the systems that the data is going through and saved on. That's also another\
    \ thing \u2013 sometimes data is not properly saved in secured places."
  sec: 2626
  time: '43:46'
  who: Elena
- line: "I think, in general, the Netherlands is a pretty advanced country in many\
    \ aspects, not just healthcare, and the way data is collected. In Germany, people\
    \ still send faxes. I recently did an MRI examination, and all I got was a compact\
    \ disc. I don't know\u2026 I don't even have places where I can put a compact\
    \ disc anymore. [laughs] Well, at least it wasn't a diskette or whatever. [chuckles]\
    \ It could have been a diskette, too. Right?"
  sec: 2679
  time: '44:39'
  who: Alexey
- line: Maybe I also see big differences because I see that healthcare in Greece,
    for example, is also different from the Netherlands. They don't have the digitalization
    that they have here. They also give compact discs sometimes. [chuckles]
  sec: 2715
  time: '45:15'
  who: Elena
- line: "Yeah, okay. [chuckles] Well, from what I heard about the Netherlands, it\
    \ is doing a really amazing job when it comes to all this digitalization of things.\
    \ Coming back to this trust topic, I imagine that most of these healthcare problems,\
    \ like cell classification and, I don't know\u2026 The thing you were talking\
    \ about \u2013 quick signal predicting, what the patient\u2019s vitals are \u2013\
    \ since we know that machine learning is not always accurate, I imagine that in\
    \ many cases, it's not a 100% accurate prediction. It can be 80%, 70%. Does it\
    \ make it more difficult? Do we have to have really accurate systems to use them?\
    \ Or if it's 60% accurate, that's already good enough?"
  sec: 2732
  time: '45:32'
  who: Alexey
- header: The importance of gradual and cyclical change
- line: "I think in the case where it's not very accurate, we need to give more information\
    \ to the people so that they can make decisions. As I said before, it can say,\
    \ \u201CWe have 60% accuracy.\u201D Then the person knows that this is just an\
    \ estimation and it's not really what the reality is. They need to check by themselves,\
    \ or they need to see that and say, \u201COkay, we will do this extra lab test\
    \ because of that.\u201D In the end, it's not a tool that says what happens in\
    \ reality, but it's more like a notification, \u201CMaybe this patient has this.\u201D\
    \ Or even if we want to make systems that don't say, \u201CThis patient has this\
    \ critical outcome,\u201D it can be that you say, \u201CThis patient has a high\
    \ risk factor,\u201D which is more generic. There are different things and different\
    \ ways you can phrase things and you can give estimations about the situation\
    \ of the patient."
  sec: 2792
  time: '46:32'
  who: Elena
- line: "What I think is that we need to build this thing gradually. Maybe at first,\
    \ we just give a description of the data of the patient in a better visualization\
    \ \u2013 data visualization is also a part of this \u2013 so that the healthcare\
    \ professional can understand the current status. Then, if you develop a mathematical\
    \ model, you can say, \u201CThis patient has a big higher risk. Just look at this\
    \ place.\u201D Maybe, with time, those algorithms, as I said, will be developed\
    \ more and they will be more accurate. Plus, I think, for the algorithm to be\
    \ developed and to be more accurate, we need feedback from the healthcare professionals.\
    \ If there is a prediction, then they can say, \u201CThis was a good prediction.\
    \ This was a bad prediction.\u201D And give the reasons. Then the algorithm can\
    \ take this feedback and improve."
  sec: 2792
  time: '46:32'
  who: Elena
- line: 'So it all comes back to two things that we already talked about: getting
    feedback from healthcare professionals and investing in better data collection
    processes.'
  sec: 2919
  time: '48:39'
  who: Alexey
- line: "More feedback on the prediction. You have the prediction and then they respond\
    \ to that. But what I see, this is kind of a cyclical process. So it's not that,\
    \ \u201CI have the algorithms and they will be ready and they will be used in\
    \ a linear way.\u201D It's more about cyclically making more and more accurate\
    \ predictions. I think, for me, it's important to be as transparent as possible\
    \ and to give information to the people \u2013 and not make big claims about things."
  sec: 2930
  time: '48:50'
  who: Elena
- line: "[chuckles] Okay. It\u2019s not like, \u201CThis patient definitely has sepsis.\u201D\
    \ Instead, it\u2019s, \u201CThis is a high-risk patient, please check them.\u201D\
    \ Then the doctor makes an examination and says, \u201COkay, indeed. This was\
    \ a high-risk case.\u201D Then you get this feedback and you try to incorporate\
    \ this feedback \u2013 collect this and add this to your data. Right?"
  sec: 2969
  time: '49:29'
  who: Alexey
- line: Yeah.
  sec: 2995
  time: '49:55'
  who: Elena
- header: Data engineering in healthcare
- line: "There is a question from Avinash about data engineering and data science,\
    \ which made me think, \u201COkay, we talked about the data science part.\u201D\
    \ But there is also\u2026 For example, (I'm, again, thinking about the e-commerce\
    \ setting). Say there is a data scientist who develops a machine learning algorithm\
    \ (a model) and then there is typically a machine learning engineer who takes\
    \ this model and takes care of all the engineering around the model. Is there\
    \ something like that? How exactly do you go about deploying this thing, provided\
    \ that all these bureaucratic things are solved? I imagine that it's not like\
    \ you just take this pickle file and put it on the device \u2013 there is a process\
    \ and there is a lot of engineering involved there as well, right?"
  sec: 2996
  time: '49:56'
  who: Alexey
- line: "This is indeed, for the data engineer to just take the model that the data\
    \ scientists create, and then deploy that on the machine so that it also works\
    \ and aligns with the rest of the software there. Also, they take into account\
    \ the restrictions of that. For example, in the low-resource setting, for example,\
    \ you sometimes cannot have the model on the cloud \u2013 it's not a good idea,\
    \ because there is no internet and there is not a lot of constant connectivity.\
    \ Then you need to deploy the model on the device itself. So you need to take\
    \ into account the specific use case where you deploy the model."
  sec: 3050
  time: '50:50'
  who: Elena
- line: For this U Net that we talked about, was it on the device or in the cloud?
  sec: 3103
  time: '51:43'
  who: Alexey
- line: "U Net was more in the research phase. We wanted to validate it further. It\
    \ was in that phase. [chuckles] Things don\u2019t go very fast. We need to keep\
    \ at it."
  sec: 3110
  time: '51:50'
  who: Elena
- line: "It was more about, \u201COkay, we have this data. We're applying the model.\
    \ The research looks promising. Let's continue.\u201D Rather than, \u201COkay,\
    \ we already deployed it and it\u2019s working everywhere.\u201D"
  sec: 3127
  time: '52:07'
  who: Alexey
- line: "And the continuation is also the validation of this. Before deploying it,\
    \ we validate it with new data, check whether it works or not, and what the accuracy\
    \ of it is. There are many steps to it. And regulatory approval \u2013 it's also\
    \ a big one. It takes more time to deploy."
  sec: 3137
  time: '52:17'
  who: Elena
- line: You mentioned that you're having a sabbatical at the moment. Are you working
    on some personal projects that are related to healthcare as well?
  sec: 3165
  time: '52:45'
  who: Alexey
- line: "I'm working on some personal projects and I'm also doing some traveling.\
    \ I also have some plans for the next [several] months. I'm actually reflecting\
    \ on what I'm going to do next. I\u2019m taking a break to rejuvenate."
  sec: 3177
  time: '52:57'
  who: Elena
- line: Is there something you can already tell us or will we need to wait till the
    next interview?
  sec: 3197
  time: '53:17'
  who: Alexey
- line: You will need to wait. [chuckles]
  sec: 3203
  time: '53:23'
  who: Elena
- line: Okay, okay. [chuckles] We will keep an eye on your LinkedIn profile.
  sec: 3205
  time: '53:25'
  who: Alexey
- header: Getting into healthcare as a data scientist
- line: If somebody wants to get into healthcare (somebody as a data scientist) how
    would you recommend they do that? Let's say I'm a data scientist, I have this
    typical e-commerce experience, but I got so motivated after listening to you right
    now that I think I want to do something [in healthcare]. How can I get started?
    How can I start using my skills for that?
  sec: 3211
  time: '53:31'
  who: Alexey
- line: "First, I think it's more about getting a general idea on, \u201CDo you want\
    \ to focus on research? Do you want to apply for a company where they already\
    \ have people working on regulatory approval, so that you can quickly work on\
    \ deploying those models in actual devices that are being sold?\u201D It depends.\
    \ It starts with you and what you want. But from my experience, because I had\
    \ a technical background and I was working on different healthcare projects, when\
    \ I started the project, I learned a lot of clinical information. In the beginning,\
    \ because the healthcare field is different, I had a lot of unknown conditions\
    \ and unknown words (like sepsis was new for me, as it was for you). It was unknown,\
    \ but then after a while, it became just another word in my vocabulary. If you\
    \ have the technical knowledge, then you also get the context by spending two\
    \ months in the setting."
  sec: 3241
  time: '54:01'
  who: Elena
- line: "What you said is \u2013 it's about you and what you want. But is it enough\
    \ for me to just want to work in healthcare? Or do I also need to get some prior\
    \ knowledge to be able to do that? For a typical data scientist who has experience\
    \ working at an internet company, they have no idea what sepsis means (just as\
    \ I don\u2019t). Can they just start applying because the skills they have are\
    \ already enough? Or should there be some preparation before that?"
  sec: 3310
  time: '55:10'
  who: Alexey
- line: "I think the skills are already enough. Maybe they will get a more technical\
    \ job in the beginning in a healthcare company, and then they can receive more\
    \ [medical-related work] if they want. That's what I saw, for example, in Philips\
    \ Healthcare \u2013 people entered the company, and they found their way."
  sec: 3346
  time: '55:46'
  who: Elena
- line: "Okay, so the important thing is, as you said, what you want. If you already\
    \ have the skills, then you can just apply and learn along the way. [Elena agrees]\
    \ In general\u2026 I imagine that there are many\u2026 It's not the easiest job\
    \ to have because of all the problems or the difficulties we discussed. What I\u2019\
    m trying to ask is \u2013 is there a lack of people who want to work in health\
    \ care? Or is there usually a lot of interest from candidates (from data scientists)?"
  sec: 3369
  time: '56:09'
  who: Alexey
- line: "I think there is a lot of interest, but they also ask for a lot of people\
    \ in general, in the field of data science. So that's what I have seen. It also\
    \ depends on the country, but still. For example, in the Netherlands, there are\
    \ plenty of options. But indeed, there are plenty of data scientists as well.\
    \ What I have noticed with many people is that they shift to that domain \u2013\
    \ there is a trend."
  sec: 3410
  time: '56:50'
  who: Elena
- line: "Well, it's great that there is funding. There are companies who can pay money\
    \ and there are data scientists who are interested in working on this so they\
    \ can find each other and actually make something \u2013 work on something meaningful\
    \ while not starving (while making enough money to live). That's really good."
  sec: 3446
  time: '57:26'
  who: Alexey
- line: Especially in the healthcare domain, there are still a lot of fields that
    haven't included a lot of data science yet. They use statistics, they use linear
    regression models. Yes, there is already funding, so they need a lot of people
    to work on that.
  sec: 3469
  time: '57:49'
  who: Elena
- line: "Why I mention starving \u2013 I remember talking to somebody a few years\
    \ ago and they said that sometimes these projects are not really well-funded.\
    \ So there are people who want to make a change but they have to be very enthusiastic\
    \ about this, compared to working in an internet company that sometimes pays less.\
    \ People need to be really willing to do this work. I hope this has changed."
  sec: 3489
  time: '58:09'
  who: Alexey
- line: I have not seen this. [chuckles] But maybe it also depends on the country.
    In different countries, there are different funds as well.
  sec: 3531
  time: '58:51'
  who: Elena
- line: "So the Netherlands is pretty advanced, as we discussed. So hopefully, it's\
    \ not an issue there. Okay, this is all we have time for today. Thanks a lot,\
    \ Elana, for joining us today \u2013 for sharing your experience with us. It was\
    \ really interesting to listen to your stories and everything you said. And thanks,\
    \ everyone else, for joining us today, and listening in, and asking questions."
  sec: 3539
  time: '58:59'
  who: Alexey
- line: Thanks, as well, for inviting me. It was nice to talk to you.
  sec: 3564
  time: '59:24'
  who: Elena
- line: "Likewise, and thanks again, Antonis, for introducing Elena and me. Looking\
    \ forward to seeing what happens after your sabbatical. I\u2019ll keep an eye\
    \ out. Good luck with everything."
  sec: 3569
  time: '59:29'
  who: Alexey
- line: Thank you.
  sec: 3584
  time: '59:44'
  who: Elena
- line: Okay. Bye and have a great week!
  sec: 3585
  time: '59:45'
  who: Alexey
---

Links:

* [LinkedIn](https://www.linkedin.com/in/elenistamatelou/){:target="_blank"}
* [Github](https://github.com/stamatelou){:target="_blank"}
