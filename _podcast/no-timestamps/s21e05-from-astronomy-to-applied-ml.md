---
episode: 5
guests:
- danielegbo
ids:
  anchor: datatalksclub/episodes/From-Astronomy-to-Applied-ML---Daniel-Egbo-e38ha20
  youtube: b92gwrsVQtg
image: images/podcast/s21e05-from-astronomy-to-applied-ml.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/From-Astronomy-to-Applied-ML---Daniel-Egbo-e38ha20
  apple: https://podcasts.apple.com/us/podcast/from-astronomy-to-applied-ml-daniel-egbo/id1541710331?i=1000728601772
  spotify: https://open.spotify.com/episode/0hV7d1zSKO7ykGDZxjXyJ8
  youtube: https://www.youtube.com/watch?v=b92gwrsVQtg
season: 21
short: From Astronomy to Applied ML
title: "Detecting Radio-Emitting Stars with MEERKAT: Building ML & Cloud Data Pipelines"
transcript:
- header: Lunar eclipse story and Daniel’s astronomy career
- line: Hi everyone, welcome to our event. This event is brought to you by Data Talks
    Club which is a community of people who love data. We have weekly events and today
    is one of such events. If you want to find out more about the events we have in
    our pipeline, click on this link. It's in the description. You will see other
    events we have in our pipeline.
  sec: 0
  time: 0:00
  who: Alexey
- line: Then do not forget to subscribe to our YouTube channel. This way you'll receive
    notifications about all future streams like the one we have today. And last but
    not least, we have an amazing Slack community where you can talk to your other
    data enthusiasts. The link is also in the description. Check it out. During the
    interview, you can ask any question you want.
  sec: 24
  time: 0:24
  who: Alexey
- line: There is a pinned link in the live chat. So ask your questions there and we
    will be covering these questions during the interview. That's the usual intro.
    I haven't done it in a while ’cause we've been on a break. But now it's back to
    school time. So now we are also back to our usual activities and right now I'm
    opening the document with the questions. So Daniel, are you ready to start?
  sec: 43
  time: 0:43
  who: Alexey
- line: Oh yes I am.
  sec: 68
  time: '1:08'
  who: Daniel
- line: Yeah. So let's start. This week we'll discuss astronomy, applied machine learning,
    and how you can move from one to another. We have a very special guest today Daniel.
    Daniel is an astrophysicist, turned machine learning engineer and AI ambassador.
    He is a PhD candidate at the University of Cape Town.
  sec: 73
  time: '1:13'
  who: Alexey
- line: He builds end-to-end systems and LM applications with a focus on reliability
    and monitoring. His recent work spans knowledge retrieval, assistance, evaluation,
    observability, applying data science to space weather and multi-wavelength astronomy.
    So this is really cool. I am really excited to talk about all these topics. So
    welcome to our event.
  sec: 93
  time: '1:33'
  who: Alexey
- line: Thank you Alexey.
  sec: 115
  time: '1:55'
  who: Daniel
- line: Usually the first thing I ask about is your career so far but recently I don't
    know if you observed this in the southern hemisphere. Recently we had a lunar
    eclipse and it was very very cool because we had this full moon but then the next
    night I see the moon is not full and I'm like okay this is strange like it's supposed
    to gradually decrease but all of a sudden it's just like a little piece of the
    moon and I'm like what's happening?
  sec: 120
  time: '2:00'
  who: Alexey
- line: But then it turns red and I'm like oh my god what's going on? So I asked GPT
    how can moon be red and then GPT says yeah it can be during moon eclipse and like
    okay when is the next lunar eclipse and it says yeah by the way it's actually
    today and I'm like wow it was so cool and now we talk about astronomy. I don't
    know anything about astronomy except this lunar eclipse thing I witnessed with
    my own eyes that the moon can turn red. This is awesome.
  sec: 156
  time: '2:36'
  who: Alexey
- line: And I've been to our planetarium in Berlin here in Berlin a few times. So
    that's my knowledge of astronomy. So I'm really excited about this talk today
    because for me this is always interesting but I don't know much about this. Pretty
    cool.
  sec: 186
  time: '3:06'
  who: Alexey
- line: Well, thank you very much. Also on my side I'm going to say thank you again
    to you because over the years you have been running this Data Talks Club and to
    be honest there's been a lot of value that I have gotten from it, especially with
    the concurrent courses that run from January to end of the year. So I sometimes
    wonder how you do that? How are you able to organize podcasts, bring people to
    talk about new software developments and all that? So kudos to you as well for
    pulling that off.
  sec: 198
  time: '3:18'
  who: Daniel
- line: Yeah. Well, it's kind of my job now. So before it wasn't so. I was a data
    scientist, but now it's my job. That's how I managed to do all that. But today
    we're talking about you Daniel. So let's start with your background. Can you tell
    us about your career journey so far?
  sec: 233
  time: '3:53'
  who: Alexey
- header: Electromagnetic spectrum and MEERKAT data explained
- line: Well, my career journey just like you said, I'm a PhD candidate at University
    of Cape Town. I only came to South Africa because of my PhD. I did my undergrad
    and masters in Nigeria and then I got a scholarship to come do my PhD here at
    the University of Cape Town also at one of the institutes here called the South
    African Astronomy Observatory. So generally my work is on leveraging what we call
    multi-strategy to find radio emitting stars.
  sec: 252
  time: '4:12'
  who: Daniel
- line: All of us know that stars are something that we see very commonly in the sky
    with our neck and eyes. But that is because stars are very good at radiating in
    the optical wavelength which our eyes can see. But if you go towards the lower
    frequency regime of the electromagnetic spectrum it becomes very difficult to
    see stars.
  sec: 289
  time: '4:49'
  who: Daniel
- line: So there is a current large international project going on called the Square
    Kilometer Array. The SKA is one of those gigantic science missions to build arrays
    of radio telescopes and is going to be hosted by two countries South Africa and
    Australia. South Africa got the hosting rights to host part of the SKA. This prompted
    them to build a precursor telescope called MEERKAT which is a 64 antenna array
    sitting in the Karoo desert in the Northern Cape.
  sec: 308
  time: '5:08'
  who: Daniel
- line: After launching the telescope in 2018 there was a legacy dataset taken about
    the galactic plane. The galactic plane is that patch of the sky that is very dusty.
    If you look at the picture you'll see the Milky Way. This is the galactic plane
    and from 2018 to 2020 MEERKAT mapped this whole portion of the sky.
  sec: 350
  time: '5:50'
  who: Daniel
- line: My job is now to take the data from MEERKAT and find radio emitting stars
    from that dataset.
  sec: 379
  time: '6:19'
  who: Daniel
- line: Find what? Sorry.
  sec: 385
  time: '6:25'
  who: Alexey
- line: Find radio emitting stars.
  sec: 393
  time: '6:33'
  who: Daniel
- line: So what is it? I'm a very lay person when it comes to these things. Physics
    wasn't my favorite in school. I liked mathematics but not physics. So what does
    electromagnetic spectrum mean?
  sec: 399
  time: '6:39'
  who: Alexey
- line: The electromagnetic spectrum is basically the range by which light can emit.
    It can be low frequency, high frequency, or wavelength related. It spans from
    radio which is considered low frequency to high frequency like gamma ray.
  sec: 405
  time: '6:45'
  who: Daniel
- line: So you have x-ray and gamma ray which tells you more about the intensity or
    the energy range of the photon. Our eyes can only pick up things in the optical,
    but communication channels like radio, Wi-Fi all operate in the radio region.
    Telecommunication devices do too.
  sec: 425
  time: '7:05'
  who: Daniel
- line: Gamma ray and x-ray devices are less common. In astronomy and astrophysics,
    they build receivers for picking up these emissions at different wavelengths.
    Optical telescopes are the most common and easy to buy, even from places like
    Alibaba or Amazon.
  sec: 451
  time: '7:31'
  who: Daniel
- line: Big ones exist too like at this South African observatory. But radio telescopes
    are less common; they need to be built in quiet fields to avoid radio interference
    from electronic devices or satellites. X-ray telescopes are even more difficult
    and have to be sent to space on satellites.
  sec: 480
  time: '8:00'
  who: Daniel
- line: I'm based in Germany.
  sec: 526
  time: '8:46'
  who: Alexey
- line: Okay. There is a project ongoing, a collaboration between Russia and Germany.
    It's a space telescope that operates in x-ray.
  sec: 532
  time: '8:52'
  who: Daniel
- line: And James Webb telescope is optical?
  sec: 539
  time: '8:59'
  who: Alexey
- line: James Webb is also a space telescope. It operates in the infrared.
  sec: 547
  time: '9:07'
  who: Daniel
- line: Infrared. Okay. So many things. Infrared is something we don't see, right?
    When I go out at night in Berlin and the sky isn't very visible because of light
    pollution, but when there’s less light pollution, I look up and see stars. This
    is just usual light waves, right?
  sec: 553
  time: '9:13'
  who: Alexey
- line: Infrared sits at lower frequency compared to optical but very close to it.
  sec: 573
  time: '9:33'
  who: Daniel
- line: The electromagnetic spectrum includes devices like mobile phones, Wi-Fi routers
    but stars and other space bodies emit too?
  sec: 593
  time: '9:53'
  who: Alexey
- line: Yes, in multiple wavelengths but sometimes the strength can't reach us here.
    Usually optical light is dominant unless with x-ray for special energetic systems
    like black holes.
  sec: 599
  time: '9:59'
  who: Daniel
- line: Because black holes they don't emit light but they emit something else or
    they don't emit anything.
  sec: 621
  time: '10:21'
  who: Alexey
- line: Well, yeah, not optical light, but there's a whole lot of activity there that
    is very very energetic. So, with that, we're able to pick up even x-ray and gamma
    ray events.
  sec: 627
  time: '10:27'
  who: Daniel
- header: Data analysis and positional cross-correlation challenges
- line: Interesting. And what do you exactly do? So, you said there is this MEERKAT
    telescope, right?
  sec: 639
  time: '10:39'
  who: Alexey
- line: So what I do is that we have the MEERKAT data, the collected data of the galactic
    plane and then we identify the point source or compact source points in this object.
  sec: 646
  time: '10:46'
  who: Daniel
- line: Our job is to say given the fact that we have these data sets, we need to
    find how many of them are emissions coming from stars and not from other extragalactic
    or astrophysical subjects out there because usually in the radio you tend to pick
    up mostly extragalactic sources, AGN's, galaxies and the rest because they are
    very strong in the radio.
  sec: 664
  time: '11:04'
  who: Daniel
- line: At the same time we know there are a couple of stars too that also have emissions
    that we can pick up especially with new instruments coming up like MEERKAT or
    Australia's ASKAP or VLA.
  sec: 686
  time: '11:26'
  who: Daniel
- line: So your job if I understood so you scan the sky at least the Milky Way part,
    right?
  sec: 697
  time: '11:37'
  who: Alexey
- line: The operation of MEERKAT was to scan the Milky Way part and then get this
    data. My job is also to take this data derived from MEERKAT and do cross correlation
    with other multi-wavelength data sets.
  sec: 710
  time: '11:50'
  who: Daniel
- line: Okay. And the task for this particular project if I understood correctly.
    So you have this scan of the sky with the Milky Way and there are many sources
    of waves of radio?
  sec: 721
  time: '12:01'
  who: Alexey
- line: Many detections of sources.
  sec: 739
  time: '12:19'
  who: Daniel
- line: So then you need to understand if this wave is coming from a star or something
    else?
  sec: 744
  time: '12:24'
  who: Alexey
- line: Yeah. Exactly.
  sec: 749
  time: '12:29'
  who: Daniel
- line: And you use machine learning for that?
  sec: 752
  time: '12:32'
  who: Alexey
- line: Oh well, not necessarily. We didn't use machine learning for this. We used
    cross matching method which is more like the nearest neighbor concept. Because
    you have to also take into account positions in the sky.
  sec: 756
  time: '12:36'
  who: Daniel
- line: The same way in geography we know positions on earth using longitude. We also
    have it for the sky. Even though you observe a different epoch you need to enter
    the correct position.
  sec: 764
  time: '12:44'
  who: Daniel
- line: Given the position that we have with MEERKAT, we go to other instruments like
    the European Space Agency space telescope which has its own mission called Gaia
    which stopped operation this year.
  sec: 781
  time: '13:01'
  who: Daniel
- line: Why do we need to look in the electromagnetic spectrum? Why is light not enough?
  sec: 809
  time: '13:29'
  who: Alexey
- line: We're looking for stars and stars are very weak in the radio but have lots
    of stars in the optical. Cross correlation helps link emissions from the same
    object.
  sec: 815
  time: '13:35'
  who: Daniel
- line: If you match the positions and see the emissions are from the same position
    it raises the probability that it's from the same source but that is not enough.
    Because it's 2D space not 3D. So you don't have distance information.
  sec: 832
  time: '13:52'
  who: Daniel
- line: There is also the possibility of background and foreground objects overlapping.
    Like when you look at a pen in front of a paper. The pen is closer but the paper
    appears behind.
  sec: 851
  time: '14:11'
  who: Daniel
- line: Yeah. For listeners, you were showing a pen and a piece of paper behind it.
  sec: 871
  time: '14:31'
  who: Alexey
- line: Yes. You might assume the pen and paper are in the same position because they
    are seen aligned from afar but they are not.
  sec: 889
  time: '14:49'
  who: Daniel
- line: So when you observe only light, the radio tells us they could be distant objects
    just overlapping.
  sec: 908
  time: '15:08'
  who: Alexey
- line: Right, one covers the other.
  sec: 920
  time: '15:20'
  who: Daniel
- header: Physics behind radio star detection and observation limits
- line: In the Milky Way, it's a common problem because of the many stars.
  sec: 925
  time: '15:25'
  who: Alexey
- line: Yes, many stars so you have to take that into account. So just finding things
    in the same position isn't enough but you need to consider physics. What are known
    properties of the source?
  sec: 930
  time: '15:30'
  who: Daniel
- line: Previous observations help tie that the radio emission is from the source,
    not from background.
  sec: 941
  time: '15:41'
  who: Daniel
- line: Yeah, okay I understand now. When I visited the planetarium in Berlin, they
    showed the Milky Way but because it's so dense, we can't receive light from other
    galaxies behind it so our map is limited to outside the Milky Way.
  sec: 946
  time: '15:46'
  who: Alexey
- header: Radio astronomy’s advantage and machine learning potential
- line: That's from looking in optical wavelengths. In radio it's different. Stars
    are dark in radio. If you point to stars seen in optical, in radio you might not
    see them because the emission is faint or non-existent.
  sec: 995
  time: '16:35'
  who: Daniel
- line: Potentially with your research, we can extend the map to include galaxies
    behind the Milky Way?
  sec: 1021
  time: '17:01'
  who: Alexey
- line: Yes, some people look at non-galactic sources behind the galactic plane. My
    job is to find galactic sources or radio stars.
  sec: 1035
  time: '17:15'
  who: Daniel
- line: Very interesting. How do you use machine learning in your work?
  sec: 1061
  time: '17:41'
  who: Alexey
- line: Not yet. We are building a dataset that could be useful for machine learning
    in the future. Currently, it's more observational data and physics modeling is
    needed first.
  sec: 1074
  time: '17:54'
  who: Daniel
- line: So it's more modeling now using physics formulae?
  sec: 1087
  time: '18:07'
  who: Alexey
- line: Yes. Physics gives interpretations and ensures reliable data to find reliable
    signals.
  sec: 1106
  time: '18:26'
  who: Daniel
- line: As an example, Gaia mission mapped over 1.8 billion stars optically. Infrared
    data picks up close to billions as well.
  sec: 1120
  time: '18:40'
  who: Daniel
- line: But in radio, only thousands of stars are detectable due to complexity of
    radio infrastructure compared to optical.
  sec: 1162
  time: '19:22'
  who: Daniel
- line: Recently, investments are building sensitive telescopes to detect faint radio
    stars. This helps astronomers resolve candidates possibly emitting radio signals.
  sec: 1192
  time: '19:52'
  who: Daniel
- line: Old SKA pathfinder telescopes like MEERKAT, ASKAP, and VLA are contributing
    to this research.
  sec: 1232
  time: '20:32'
  who: Daniel
- header: Radio astronomy progress and Daniel’s ML journey
- line: Okay. So right now it's a few thousand of stars only but with the investment
    in the hardware and technology we should be able to observe more and more stars
    with this radio stars.
  sec: 1237
  time: '20:37'
  who: Alexey
- line: Yeah, radio stars because again these things do also other science projects
    not just for stars. They dominate the radio galactic field like even galaxies,
    extended objects, remnants and the rest of them just things outside of our galaxy.
  sec: 1255
  time: '20:55'
  who: Daniel
- line: Yeah. But how did you actually so you said what you use right now at work
    is more like statistics, correlation, uh, than also physics, more like traditional
    modeling. At what point and how did you come across machine learning and decide
    to use it?
  sec: 1274
  time: '21:14'
  who: Alexey
- line: 'Well, so coming across machine learning was a thing that happened sometime,
    like say, I''ll say probably during my masters or so. So I will say this: I have
    a friend who is an engineer. We also grew up together in Nigeria and then he left
    for Canada sometime and was able to build an AI startup called Way back in like
    2015/16.'
  sec: 1291
  time: '21:31'
  who: Daniel
- line: It was an AI project analyzing the infant cries of babies to predict if an
    infant has a certain condition. It became a motivating factor but at the time
    it wasn't necessarily my thing. But getting into doing this program I realized
    I needed to work on a lot of data. I had a lot of data and this data is actually
    very huge, tens of gigabytes.
  sec: 1331
  time: '22:11'
  who: Daniel
- line: So you can't process it on your PC; you need a cloud, a cluster to process
    the data. So that is where the whole data science concept came in. When I started
    my program, there was an announcement for a program called Black and Brilliant
    AI program organized by some people in the US and collaboration with Codecademy
    because I was also struggling to learn how to code in Python and do data analysis.
  sec: 1376
  time: '22:56'
  who: Daniel
- line: Because I was going to deal with a lot of data and you need hands on in all
    of this. So I applied for that program and got accepted. In about three months
    we had this whole coding phase with Codecademy as the platform and also provided
    me with a couple of mentors. There were conversations around machine learning
    because many of them are practitioners in the tech industry.
  sec: 1410
  time: '23:30'
  who: Daniel
- line: One of my mentors, who was also in machine learning, motivated me about data
    science's impact in my field, but he also tried to explain I should not look at
    it just from the prism of astronomy but also from the prism of the fact I could
    understand data analysis and use programming tools.
  sec: 1439
  time: '23:59'
  who: Daniel
- line: Because if I do this in my academic field I can also do it in the industry.
    That became a motivator and I started getting my hands dirty. Instead of using
    some software to do the cross-matching or cross-correlation, I started using Astropy,
    a Python package which is very robust.
  sec: 1473
  time: '24:33'
  who: Daniel
- line: Astropy incorporates things from NumPy, SciPy and other libraries. It's the
    go package for astronomy in Python. So I started combining my data with Astropy
    because the data was very huge. Even pandas wouldn't work well but Astropy allowed
    the flexibility to deal with big data.
  sec: 1523
  time: '25:23'
  who: Daniel
- line: So that's where I saw the beauty of this and I was also glad I didn't have
    to run everything on my PC. I had access to free cloud service where I ran on
    JupyterHub and kept running daily.
  sec: 1547
  time: '25:47'
  who: Daniel
- header: Python tools and experience with ZoomCamps
- line: And then in 2022, I saw one of the mentors reshared your post about MLOps,
    which was data engineering actually.
  sec: 1560
  time: '26:00'
  who: Daniel
- line: It was the first one, the first.
  sec: 1582
  time: '26:22'
  who: Alexey
- line: Yeah. I signed up for data engineering but I was traveling and couldn't do
    it all because I was just starting Python and learning a lot, cloud stuff like
    Terraform, and I was also studying my PhD so had to skip it.
  sec: 1587
  time: '26:27'
  who: Daniel
- line: Later that year I took the ML ZoomCamp which was the eye opener about machine
    learning. When I finished the course which was about eight to ten weeks, I had
    to share my learnings online.
  sec: 1618
  time: '26:58'
  who: Daniel
- line: Sharing helped me connect with mentors and other learners on LinkedIn who
    encouraged me and gave feedback.
  sec: 1645
  time: '27:25'
  who: Daniel
- line: That's how the whole team started encouraging me. People told me I was doing
    a good job which motivated me. So that's when machine learning fully kicked in.
  sec: 1679
  time: '27:59'
  who: Daniel
- line: So you took it in 2022, the ML ZoomCamp?
  sec: 1684
  time: '28:04'
  who: Alexey
- line: Yes.
  sec: 1692
  time: '28:12'
  who: Daniel
- line: Cool. It was the second edition then. Did it help your work even though you
    don’t use ML regularly now?
  sec: 1700
  time: '28:20'
  who: Alexey
- line: Yes, it helped. Aside from machine learning, it was a paradigm shift in coding.
    I learned to write reusable Python scripts rather than just doing everything in
    Jupyter notebooks.
  sec: 1720
  time: '28:40'
  who: Daniel
- line: Many scientists just do basic analysis and plotting in notebooks, but don't
    write reusable code. The course helped me think about developing projects, implementing
    models used in the industry.
  sec: 1759
  time: '29:19'
  who: Daniel
- line: It also introduced cloud computing, setting up virtual environments, and Terraform
    which were new to me. Although familiar with Linux and bash scripting, writing
    reusable Python scripts was new.
  sec: 1818
  time: '30:18'
  who: Daniel
- header: Intel internship and exploring LLMs
- line: In 2023, with OpenAI's chat introduction, a mentor recognized my progress
    and offered me an internship testing Intel's deployment on edge devices.
  sec: 1886
  time: '31:26'
  who: Daniel
- line: Was that computer vision?
  sec: 1947
  time: '32:27'
  who: Alexey
- line: Yes. Testing models packaged for deployment on Intel hardware with GPUs and
    CPUs was my task. I tested latency and infrastructure suitability.
  sec: 1954
  time: '32:34'
  who: Daniel
- line: Then LangChain and AI LLM models appeared and I started exploring open source
    models like Hugging Face, and prototyping AI applications like retrieval augmented
    generation and vector DBs.
  sec: 2018
  time: '33:38'
  who: Daniel
- line: Testing new products and frameworks for clients through a consulting company
    was challenging but fun. Trust was given despite my still-growing technical knowledge.
  sec: 2081
  time: '34:41'
  who: Daniel
- line: Eventually Intel had internal problems delaying projects, so I refocused on
    my PhD and publishing academic papers.
  sec: 2111
  time: '35:11'
  who: Daniel
- line: So they reached out to you because you shared your progress on LinkedIn in
    May 2023?
  sec: 2165
  time: '36:05'
  who: Alexey
- line: Yes. I knew the mentor already, and sharing progress helped gain encouragement
    and feedback.
  sec: 2170
  time: '36:10'
  who: Daniel
- line: That's great. We encourage sharing but many don’t.
  sec: 2221
  time: '37:01'
  who: Alexey
- line: I often tell people to share regardless of level because feedback can be praises
    or suggestions from others. I’ve seen beginners helped by it.
  sec: 2256
  time: '37:36'
  who: Daniel
- line: I recommend ML ZoomCamp for learning best practices and the full end-to-end
    process, which many other places don’t cover.
  sec: 2306
  time: '38:26'
  who: Daniel
- line: That’s why we focused on ML engineering and deployment, because many get stuck
    deploying projects after courses.
  sec: 2392
  time: '39:52'
  who: Alexey
- line: I also took the recent MLOps course but only on weekends. I focused on projects
    but didn’t share everything for personal reasons.
  sec: 2424
  time: '40:24'
  who: Daniel
- header: Sharing progress and course projects with orchestration tools
- line: So uh there are sometimes cases when you don't want to share your rolling
    in public, right?
  sec: 2464
  time: '41:04'
  who: Alexey
- line: Well, yeah, of course. Especially if you are you are uh yeah I recommend majority
    of the time you should but like in my case the reason why I didn't share it then
    was that I I was in between a couple of projects and you don't want to feel like
    you have a divided attention but again desired I need to actually do that course
    and get the certificate so that's lingered for months 2023 when I got the ML zoom
    I bought the next certificate I was like no I have to do this I I actually registered
    the in the data engineering zoom camp at the beginning of the year.
  sec: 2470
  time: '41:10'
  who: Daniel
- line: I actually went through it end to end. The only problem was that I didn't
    put I didn't submit I didn't submit the project like I didn't even though I did
    project because uh beginning of the year too was like I usually like have this
    activities a lot of activities like volunteer engagement and all that at the beginning
    of the year even observation time sometimes we like sometime which is also what
    like you know you have to use the telescope sometimes like do observation run
    for like weeks so you you're walk during the day and you need to pay attention
    to observation. So those times are not usually convenient for me to do any other
    things.
  sec: 2508
  time: '41:48'
  who: Daniel
- line: Well, if you'll have a bit of free time, you can just submit your project
    in the next the next iteration, not do any course, just focus on—
  sec: 2543
  time: '42:23'
  who: Alexey
- line: Oh, yeah. Okay. I actually just did another one this time using a flow. Um
    okay. Yeah. The whole thing all integrated.
  sec: 2555
  time: '42:35'
  who: Daniel
- line: Can you tell us about uh any of the projects you did for the courses? Maybe
    like for example this one um it's I don't know if it's for a course or not but
    the one you mentioned right now airflow and minio uh is so yeah.
  sec: 2568
  time: '42:48'
  who: Alexey
- line: It is recently yeah so I so I because I usually just sit down sometimes I
    say what are the unfinished project that I did and what is more relevant. So during
    the editor engineering zoom camp the one at the beginning of the year. remember
    the orchestration was Kestra and I did use Kestra and I did the whole thing of
    running the whole process from using Terraform to create your compost your big
    query because we use Google right and then um setting things up and make sure
    they are running and also um querying data doing the ELC transformation and putting
    them in Google query uh bigquery and I use Kestra for
  sec: 2585
  time: '43:05'
  who: Daniel
- line: But then I was speaking to somebody like I said sometimes I like to like consult
    with people in the industry to figure out what's actually the major trend. So
    it was like was telling me no um a flow is still the number one orchestrator for
    for you know running this thing. I was like if you can try I'm like okay
  sec: 2630
  time: '43:50'
  who: Daniel
- line: I think I've tried a flow for once but I didn't sure I'm not sure I did I
    understood what was happening. So I just sit down um last weekend. You won't believe
    it. And then I like okay setting up a flow 3.0. And to be honest, thanks to there
    was a pres thanks to there was one of the uh presenters in the in one of your
    show. I don't know if it's what's called again who talk about a flow 3.0.
  sec: 2648
  time: '44:08'
  who: Daniel
- line: Mhm. Yeah. Yeah. So that's that's one of the resources I used. You believe
    it to just set up the the Aflow 3.0 zero on a da
  sec: 2675
  time: '44:35'
  who: Daniel
- line: right this is the command line you use this command line utility from astronomer
    for setting up
  sec: 2684
  time: '44:44'
  who: Alexey
- header: Setting up Airflow 3.0 and building data pipelines
- line: oh yeah yeah so actually I tried using it but unfortunately uh I didn't succeed
    because I was trying to connect spark okay the other things to um I don't know
    I think like I said I was in a hurry but I figured out how to like do all of those
    things with um just to compose without using but I think the CLI is very very
    nice to set things up And yeah, but yeah, finally if you get everything worked
    right night last
  sec: 2689
  time: '44:49'
  who: Daniel
- line: night, the whole end to end my SQL. So I did the whole thing of think about
    quing the data from a source, right? And putting it in your data warehouse. So
    in this case uh I didn't want to connect to a cloud service although I know how
    to do that but I had to use M IO to um simulate the the data link sorry. Yeah.
    So take data using um my SQL put it into min.io
  sec: 2715
  time: '45:15'
  who: Daniel
- line: and then also do um ispark transformation and then also save it mio and then
    take the data from min.io transform data to pos like where you have like analytics.
    Yeah. So what I still have to do now is to employ dbt.
  sec: 2741
  time: '45:41'
  who: Daniel
- line: Okay. Yeah. You're almost done. and then you can just submit this uh when
    we start the course and then you'll get your certificate.
  sec: 2760
  time: '46:00'
  who: Alexey
- line: Oh yeah yeah yeah I'm actually thinking of doing writing a maybe probably
    think of writing my first medium article because I haven't I've not written medium
    article I know I've written something on them then because to be honest the the
    whole integration right now is not out there like you know um incapassing 3.0
    zero.
  sec: 2766
  time: '46:06'
  who: Daniel
- line: Yeah, I imagine that it wasn't super straightforward.
  sec: 2788
  time: '46:28'
  who: Alexey
- line: Yeah, I was searching on YouTube. I I couldn't figure out I couldn't find
    so I had to struggle but n I figured out how to work. So I think this is going
    to be one of those things that
  sec: 2795
  time: '46:35'
  who: Daniel
- line: Yeah, please do. You'll save time to many people. But this is also kind of
    the essence of of the data engineer job because you have some things you need
    to figure out how they work together and sometimes you spend a lot of time doing
    that.
  sec: 2801
  time: '46:41'
  who: Alexey
- line: So it was a combination of looking at many mostly people using airflow 2.0
    and then um because that's where you see a lot of them use by spark but then the
    3.0 there's a whole lot of glitching so I had to take my time to figure that out.
    Yeah writing the ta compose also setting environmental variables and parameters
    inflow web server to make sure things work.
  sec: 2812
  time: '46:52'
  who: Daniel
- line: Yeah. So it's just one of those you know learning phases that we um we just
    do especially when I feel like not like I have time but when I feel like I have
    my free time I just hop in. Then other things that I do I think and is also there
    something I probably recommend is especially now that we have this whole AI thing.
  sec: 2839
  time: '47:19'
  who: Daniel
- header: AI startups, training resources, and NVIDIA courses
- line: There's a lot of startups coming up especially those building um you know
    um conventional frameworks like you know lang chain lama index mon have even you
    know many of these things they also have their own academy
  sec: 2859
  time: '47:39'
  who: Daniel
- line: I think sometimes you have this sort of best practices where they kind of
    like you know offer tailored trainings know you know that fits in with how to
    use their tools effectively so I also saw this um an guy who I saw for the data
    data talk post this morning about um um learning a flow 3.0 which I signed up
    for.
  sec: 2879
  time: '47:59'
  who: Daniel
- line: I believe those who are interested in data engineering should take that kind
    of course. Those who are interested in AI should look out for um AI related courses.
    Um especially from especially if you want to be a developer from a developer perspective,
    look out for the academy like Arise AI.
  sec: 2904
  time: '48:24'
  who: Daniel
- line: They do have their own academy for those who want to learn how to do um obser
    um observability within the LLM space. Yeah. Or take the lang chain um academy.
    They do have um I think about two courses now around agents land graph rest of
    them. So I think it's it's more like um for me that's more like the best bet.
  sec: 2918
  time: '48:38'
  who: Daniel
- line: And then there a couple of resources too that are out there. Uh one of the
    things that have helped me is um you know NVIDIA deep learning institute. Mhm.
    Yeah. So um they do offer um you know courses around um so thinking about especially
    around leveraging NVIDIA hardway. So they try to like their courses around you
    thinking about the hard way thinking about best practices
  sec: 2939
  time: '48:59'
  who: Daniel
- line: and also deploying. So I was lucky enough so one of the mentors that I have
    just was able to offset that for me um getting me a coupon for one of their courses.
    Some of the courses are also free. Yeah. Some of the are free. Yeah. So they also
    like that essential
  sec: 2971
  time: '49:31'
  who: Daniel
- line: with Nvidia. I remember they often uh give coupons for free. So I remember
    partnering with them uh for they do this conference. I don't remember how it's
    called. They do it once or twice per year. BTC PTC. Exactly. And they usually
    want to promote the conference. That's why they contact people on LinkedIn with
    some number of followers. They contacted me too and say okay like here are coupons
    you can share them with your followers. So I was doing that.
  sec: 2983
  time: '49:43'
  who: Alexey
- line: So some yeah just watch out maybe check social from time to time.
  sec: 3014
  time: '50:14'
  who: Alexey
- header: Student access to education, NVIDIA experience, and beginner astronomy programs
- line: Yeah social they have this website for higher institutions. So they have this
    some of their courses um especially those special ones. Um they usually do it
    at certain times of the year. So you always you see the trainings that they have
    and you can sign up free as a student. just use your student email. So that has
    helped me a lot to take a number of their courses like the recent one I did was
    the conversational AI building conversational AI application deploying it using
    the Nvidia name infrastructure deploying on um on the on Nvidia GPU hardware be
    it a 100 or H100
  sec: 3020
  time: '50:20'
  who: Daniel
- line: designing the whole kubernetes um that's yami templates and the rest of them
    and then deploying so these are very very essential especially for students to
    have an email address. Your student email address can get you a lot of stuff.
  sec: 3057
  time: '50:57'
  who: Daniel
- line: There are a few questions. The first question I see is when to can we register
    for 2026 batch.
  sec: 3074
  time: '51:14'
  who: Alexey
- line: The question is about data engineering course. I shared the link. it does
    say 2025 simply because I did not update the date. So you just sign up for 2025
    link and it's fine. Um yeah. Um but then we also have a questions to you Daniel.
    So the question is for a data beginner what works in the field and how to approach
    um how to even approach doing projects there and I guess you were there a couple
    of years ago. Um so how did you approach being a beginner and starting to actually
    um get things done?
  sec: 3080
  time: '51:20'
  who: Alexey
- line: Okay. So, yeah, that's a good question, but I'm going to answer it this way.
    Um, I borrowed your templates, um, Alexy. so like I said, a lot of people in astronomy,
    especially for some of us coming from developing countries, don't even know how
    to code. So, if you want to do a postgraduate program, that's the whole coding
    thing now because scripts automatically need it, but then you don't have enough
    time to learn the skills because remember you're already in the middle of your
    program.
  sec: 3121
  time: '52:01'
  who: Daniel
- line: So people that I work with here I reached out to the bricks astronomy team
    here. So because astronomy we have the bricks astronomy for the bricks countries
    so they have the office. So I reached out to the league and then I proposed that
    don't you think we need to organize some sort of um learning um event for young
    people who are interested in astronomy and he was like okay what do you want?
    I say yes I know uh there's a lot of summer schools but most times the summer
    schools always center on physics itself.
  sec: 3154
  time: '52:34'
  who: Daniel
- line: Even when they do Python, especially for developed countries like America
    or Europe they usually have the notion that you're already very good at programming
    right so um we started this whole thing I made the first proposal last year I
    think around October or so and was like okay this is a good idea we're going to
    discuss it and then around January they would finalize it and say okay a lot of
    people came in.
  sec: 3192
  time: '53:12'
  who: Daniel
- line: We have the institute called idea. They provide a cloud service for astronomy
    and then the bricks astronomy group and then other people from India, an institute
    in India. So we have two professors from there who teach computational astronomy
    physics. So they were like oh this is a good idea for beginners in astronomy to
    say so we called it data based astronomy data analytics program.
  sec: 3222
  time: '53:42'
  who: Daniel
- line: It was an 8x program that is designed for those who are like who have no background
    in programming. So it's a pure analytics studio. Come in you learn the process
    you learn the coding process from beginner level Python and then at the end of
    the day we also incorporated assignments.
  sec: 3240
  time: '54:00'
  who: Daniel
- line: Like I said I borrowed your template making sure every week there's always
    a lecture and presentation hands-on that people need to do and then at the end
    of the course there was a project at the beginning of the whole thing we also
    mentioned that people should share their resources online.
  sec: 3263
  time: '54:23'
  who: Daniel
- line: To be honest, my LinkedIn, that's why I say I don't know how you do this.
    My LinkedIn has been because we had more than 900 people sign up for this program
    and then in the course of this whole thing the video is also there on YouTube
    because I was the lead facilitator training people.
  sec: 3280
  time: '54:40'
  who: Daniel
- line: We also have to do it two times, morning and evening to just make sure we
    accommodate people either in the eastern part of the world or the western part
    of the world so it was very very successful.
  sec: 3298
  time: '54:58'
  who: Daniel
- line: They did a project like you know what you're just a beginner yes maybe I encourage
    the second one even if you just do it in a Jupyter notebook for now in a collab
    that is sharable I emphasize that they should make sure that they put the whole
    things in collab because with collab you can share the link people can see exactly
    what do you even see the result.
  sec: 3312
  time: '55:12'
  who: Daniel
- line: They did that and they were able to also tell the story taking astronomy data
    for those who have astronomy background or if you have so because there were a
    lot of people who were not amateur astronomers who wanted to use the opportunity
    to see what is happening there.
  sec: 3333
  time: '55:33'
  who: Daniel
- line: So we had more than 190 submissions of project that we had done and a whole
    lot of them got their certificates at the same time they shared their learning
    things on this program finished in July first around first second week of July.
  sec: 3349
  time: '55:49'
  who: Daniel
- line: About two three people have reached out to say they are so happy about this
    that it has helped them to even improve especially those applying for postgraduate
    opportunities because they want to also show a form of projects that you've done
    to demonstrate that you know how to code, think about solving problems, taking
    a dataset, doing analysis and generating results.
  sec: 3363
  time: '56:03'
  who: Daniel
- line: Some of them did very things that were like I was surprised like how did you
    guys come up with these whole ideas so the thing is irrespective of where you
    are if you're just starting make sure you learn the basics but while you are learning
    the basics think about the problems that basics can solve.
  sec: 3408
  time: '56:48'
  who: Daniel
- line: If your background is finance or economics and you just learn how to maybe
    use pandas to read a dataset and do basic statistical analysis the next thing
    should be to find economic data. Use your background to do the same thing and
    share the results, explain what you have done.
  sec: 3432
  time: '57:12'
  who: Daniel
- line: It helps a lot. People will see that you have the technical knowhow in your
    background and scientific knowledge of your field and you also have the technical
    knowhow of tools to derive results. So whichever field you are in, make sure you're
    doing that.
  sec: 3461
  time: '57:41'
  who: Daniel
- header: Skills, projects, and career advice for beginners
- line: So basically how to what works in the field and your answer if I may summarize
    it is first face focus on basic basics for machine learning this uh would be Python
    programming and then do projects.
  sec: 3479
  time: '57:59'
  who: Alexey
- line: And for projects what helps is having some sort of structure so for example
    this is what we did in our courses so say okay this is what is expected this is
    the criteria we use for evaluating now for you it's simpler to go ahead and implement
    the project.
  sec: 3491
  time: '58:11'
  who: Alexey
- line: Oh yes, of course. Because this is a system where students are applying for
    like PhD opportunities. People are always applying and want to show strong motivation
    that they have skills in their area of interest.
  sec: 3525
  time: '58:45'
  who: Daniel
- line: They’ve done something like taking data from somewhere and doing physical
    analysis that shows background knowledge. It’s a plus as seeing is believing.
    Communicating astronomy is beautiful as well.
  sec: 3548
  time: '59:08'
  who: Daniel
- header: Starting with data science or engineering
- line: And then uh the same question actually has two questions the other part is
    should I focus on data engineering or data science/machine learning what do you
    think.
  sec: 3559
  time: '59:19'
  who: Alexey
- line: I’ll just say start with data science first. Data engineering is a bit technical
    because you need to understand data itself before moving on, since data engineering
    is more like managing data provisioning and warehousing.
  sec: 3566
  time: '59:26'
  who: Daniel
- line: But also it depends where you start. If you start as a software engineer maybe
    data engineering will be easier than machine learning.
  sec: 3582
  time: '59:42'
  who: Alexey
- line: Yeah, I'm just answering from maybe four years ago when I was in your place.
  sec: 3599
  time: '59:59'
  who: Daniel
- header: Course sponsorship, data tools, and learning resources
- line: Okay. Uh there’s also a question about my T-shirt actually installing DT that's
    a data load tool. DT is one of our sponsors.
  sec: 3607
  time: '1:00:07'
  who: Alexey
- line: They support the Data Talks Club and with them we did quite a few things already.
    You can check our YouTube channel.
  sec: 3621
  time: '1:00:21'
  who: Alexey
- line: It’s a data engineering tool. Let’s say you have things on S3 and you want
    to move them to BigQuery. You can easily use the Data Load Tool for that, also
    for some transformation.
  sec: 3634
  time: '1:00:34'
  who: Alexey
- line: It’s a very convenient way to build pipelines and because they sponsor our
    community and they are Berlin based, they gave me this T-shirt which I like, so
    I wore it for today’s stream. Sometimes I do that.
  sec: 3649
  time: '1:00:49'
  who: Alexey
- line: But yeah, it’s a very convenient shirt. Give them a go.
  sec: 3664
  time: '1:01:04'
  who: Alexey
- line: 'With that, we should be wrapping up. Maybe Daniel, last question to you:
    If anyone wants to learn more about astronomy and data science in astronomy, you
    mentioned Astropy. Is there any resource for learning Astropy?'
  sec: 3669
  time: '1:01:09'
  who: Alexey
- line: Oh yes, just Google Astrop Astropy Len.
  sec: 3689
  time: '1:01:29'
  who: Daniel
- line: Astropy what?
  sec: 3695
  time: '1:01:35'
  who: Alexey
- line: Len Astropy Len. Yeah. There’re a couple of tutorials on it. You will see
    how to get started.
  sec: 3701
  time: '1:01:41'
  who: Daniel
- line: I cannot quickly find it. Maybe YouTube?
  sec: 3706
  time: '1:01:46'
  who: Alexey
- line: I’ll share the link in the chat.
  sec: 3729
  time: '1:02:09'
  who: Alexey
- line: Okay. Thanks a lot for joining us today, for sharing your story. I’m sure
    it motivated and will motivate many people.
  sec: 3742
  time: '1:02:22'
  who: Alexey
- line: I want to use your story as an example why students should share their learnings
    publicly. So thanks a lot for joining us and for talking about astronomy, machine
    learning, and our courses.
  sec: 3762
  time: '1:02:42'
  who: Alexey
- line: Yeah, sure. Thank you too, Alex. Like I said pulling those courses for free
    is not easy.
  sec: 3775
  time: '1:02:55'
  who: Daniel
- line: I hope you get sponsors for the next MLOps camp because that course is very
    essential especially for anyone wanting to do AI LLM related stuff.
  sec: 3781
  time: '1:03:01'
  who: Daniel
- line: MLOps is sad because I can’t find sponsors. Many companies are focusing on
    AI products where investor money goes.
  sec: 3798
  time: '1:03:18'
  who: Alexey
- line: I get it. LLM ops is to catch people up.
  sec: 3824
  time: '1:03:44'
  who: Daniel
- line: Maybe things will change. I will continue reaching out to sponsors even though
    I said it might be the last. If some sponsor says yes we will run it again and
    update.
  sec: 3830
  time: '1:03:50'
  who: Alexey
- line: Final word, the resources are freely available on YouTube. Even if there is
    no next live course, just go there and bookmark it. Resources are not outdated.
  sec: 3850
  time: '1:04:10'
  who: Daniel
- line: Yeah, we will not remove content. The course will stay on GitHub. All content
    is available to watch anytime.
  sec: 3875
  time: '1:04:35'
  who: Alexey
---

Links:

* [Linkedin](https://www.linkedin.com/in/egbodaniel/){:target="_blank"}