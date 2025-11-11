---
episode: 2
guests:
- aishwaryajadhav
ids:
  anchor: datatalksclub/episodes/Lessons-from-Applied-AI-Tesla--Waymo--and-Beyond---Aishwarya-Jadhav-e39befu
  youtube: vK_SxyqIfwk
image: images/podcast/s22e02-lessons-from-applied-ai-tesla-waymo-and-beyond.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/Lessons-from-Applied-AI-Tesla--Waymo--and-Beyond---Aishwarya-Jadhav-e39befu
  apple: https://podcasts.apple.com/us/podcast/lessons-from-applied-ai-tesla-waymo-and-beyond/id1541710331?i=1000731200298
  spotify: https://open.spotify.com/episode/0h9eX7m6H2TPqOjUwb3Jw6?si=I4rKrHXpQTmS7cJBMJbUMA
  youtube: https://www.youtube.com/watch?v=vK_SxyqIfwk
season: 22
short: 'Lessons from Applied AI: Tesla, Waymo, and Beyond'
title: "Autonomous Driving AI: LiDAR vs Camera, On-Vehicle Inference & Model Compression"
transcript:
- header: Aishwarya’s career journey from finance to self-driving AI
- line: Hey everyone, welcome to our event. This event is brought to you by DataTalks.Club,
    a community of people who love data. We have weekly events, and today is one of
    them. If you want to find out more about the events we have, there is a link in
    the description. Click on that link and check it out.
  sec: 0
  time: 0:00
  who: Alexey
- line: We actually have quite a few events in our pipeline, but we need to put them
    on the website. Keep an eye on it. We will publish them soon, and you’ll see them.
    Don’t forget to subscribe to our YouTube channel. This is the most reliable way
    to get notified when our stream starts.
  sec: 19
  time: 0:19
  who: Alexey
- line: Last but not least, do not forget to join our data community where you can
    hang out with other data enthusiasts. During today's interview, you can ask any
    question you want. There is a pinned link in the live chat. Click that link, ask
    your questions, and we'll cover them during the interview.
  sec: 35
  time: 0:35
  who: Alexey
- line: That’s the usual introduction I do. I’m a bit sleepy, but I hope it goes well.
    If you’re ready, I have the questions prepared in front of me.
  sec: 61
  time: '1:01'
  who: Alexey
- line: Yeah, sounds good. Ready.
  sec: 80
  time: '1:20'
  who: Aishwarya
- line: Today on the podcast we are joined by Aishwarya. Do I pronounce your name
    correctly?
  sec: 86
  time: '1:26'
  who: Alexey
- line: Yes, that is right.
  sec: 92
  time: '1:32'
  who: Aishwarya
- line: 'Good. Aishwarya is a Machine Learning Engineer at Waymo, formerly part of
    Tesla''s Autopilot AI team and a Carnegie Mellon University alumna. She has worked
    across some of the toughest applied AI problems: financial recommendation systems
    at Morgan Stanley, multimodal research at CMU, perception and video understanding
    at Tesla, and now gesture and pedestrian semantics at Waymo. She has also contributed
    to AI for social good, including a malaria mapping project in Africa that achieved
    real-world impact at scale. Welcome to this event.'
  sec: 93
  time: '1:33'
  who: Alexey
- line: Hi, thank you for having me.
  sec: 126
  time: '2:06'
  who: Aishwarya
- line: That’s quite a nice bio. Probably what you do now and at Tesla is very challenging,
    but for me Morgan Stanley also sounds very challenging because I worked a little
    near high-frequency trading. I wasn’t actually working on the trading system,
    but we were doing analytics on top of this data. It was huge, so probably quite
    challenging. Can you tell us more about your career journey?
  sec: 132
  time: '2:12'
  who: Alexey
- line: Like you mentioned, at Morgan Stanley it was a lot of data. I was a Big Data
    Engineer there and handled huge amounts of data. I was there when Morgan Stanley
    was doing the acquisition of E*TRADE, so we had much more data coming in. My role
    was handling this data, connecting the different dots, and analyzing them together.
  sec: 171
  time: '2:51'
  who: Aishwarya
- line: From there I realized that data has so much value that we don’t need to do
    everything manually. That was back in 2018, and the AI domain hadn’t yet fully
    formed, but it was getting there. People were realizing its importance, and finance
    was one of the last fields to take on machine learning and AI. We were onboarding
    systems, and that’s when I decided to get hands-on with AI, starting with smaller
    systems like recommendation engines that were already well known in the AI domain.
  sec: 196
  time: '3:16'
  who: Aishwarya
- line: I started with that and then got more research-oriented. We tried out graph
    neural networks, which were more complex topics at the time, and I realized there
    was so much to learn and the field was vast. That’s when I decided to pursue a
    master’s and joined Carnegie Mellon University. My program was a mix of data science
    and machine learning, so I could draw upon both my experiences and interests.
  sec: 235
  time: '3:55'
  who: Aishwarya
- line: During CMU, I was more inclined toward projects involving computer vision.
    I worked on a project for a navigational app for blind people called AI Guide
    Dog. It captures the world and helps navigate people without vision. From there,
    I got into Tesla because it was also in the computer vision and navigation domain,
    and that’s where my self-driving journey began. From Tesla to Waymo, it’s a similar
    domain but with different kinds of products.
  sec: 273
  time: '4:33'
  who: Aishwarya
- line: That’s where I am now at Waymo, in the self-driving domain. I started in finance
    and reached a completely different field, but it has been an interesting journey.
  sec: 334
  time: '5:34'
  who: Aishwarya
- header: Building AI guide dog for the visually impaired
- line: That’s an interesting journey. The app that you developed for blind people,
    can you tell us more about it? How does it work? Do they hold their phone and
    it tells them where to go or describes things?
  sec: 339
  time: '5:39'
  who: Alexey
- line: For this app, the goal was that people without vision should be able to navigate
    the world just as sighted people do. The app is basically their eyes. You hang
    it around your neck and walk with it, and it captures the world in front of you.
    Then, via live audio instructions, it tells you to keep walking straight, take
    a left or right, stop at a traffic signal, or notice a pedestrian crossing. It
    gives instructions via audio.
  sec: 363
  time: '6:03'
  who: Aishwarya
- line: Interesting. Was it a pet project, a company project, or an AI for social
    good project? How did you get involved?
  sec: 401
  time: '6:41'
  who: Alexey
- line: My program has something called the Capstone Project. Every year, you either
    pair up with a professor or someone from the industry who has an interesting project,
    and then you work on it. This project was from a CMU alumnus who now works at
    Pinterest. He started the project, and ours was the third iteration, where our
    team joined and continued the work.
  sec: 409
  time: '6:49'
  who: Aishwarya
- line: Was it a community AI social good project or a company project?
  sec: 446
  time: '7:26'
  who: Alexey
- line: It was more of a volunteer project. Every year, a group of CMU volunteers
    work on it, make progress, and then pass it on to the next group.
  sec: 452
  time: '7:32'
  who: Aishwarya
- line: That’s a very interesting concept.
  sec: 465
  time: '7:45'
  who: Alexey
- line: Yes. Before me, two batches had worked on it, and they were mentors to us.
    When I finished, I mentored the next batch. It’s now in its fifth iteration, with
    two more batches after me making more progress on it.
  sec: 471
  time: '7:51'
  who: Aishwarya
- line: That’s a really nice idea. At DataTalks.Club, we have courses, and I immediately
    started thinking how we could implement something similar. It sounds amazing because
    it allows people from previous iterations to mentor those currently taking courses.
    Having a project like that helps them sharpen their skills.
  sec: 492
  time: '8:12'
  who: Alexey
- line: 'And it doesn’t need to be done all at once. It’s a big project with many
    moving parts, so it can’t be built in one year or even six months. You pick small
    pieces: the first team worked on data, the second built baseline models, and the
    third improved evaluation. It’s iterative. It’s a good idea.'
  sec: 518
  time: '8:38'
  who: Aishwarya
- line: Do you know if this app is accessible in the App Store?
  sec: 547
  time: '9:07'
  who: Alexey
- line: Not yet. The next community of students will be working on the app. We have
    the model, but it’s still in the beta phase. We are doing a lot of testing because
    it’s a sensitive use case.
  sec: 554
  time: '9:14'
  who: Aishwarya
- line: I can imagine. I recently participated in a marathon. People who know me would
    roll their eyes because I wouldn’t stop talking about it. I had been preparing
    for so long.
  sec: 566
  time: '9:26'
  who: Alexey
- line: During the marathon, blind people and those with vision problems also took
    part. They were running with guides who held their hands and ran together. I thought
    it was amazing to include them because they also want to be part of these events.
  sec: 578
  time: '9:38'
  who: Alexey
- line: Since they cannot see, it’s difficult, but the organizers allowed guides to
    join and lead them. It was wonderful. Maybe with this app they wouldn’t yet be
    able to run a race, but it’s one step closer to that.
  sec: 604
  time: '10:04'
  who: Alexey
- line: Yes, that’s the hope. They won’t need to rely on someone else. They can have
    their app as their guide for the world.
  sec: 633
  time: '10:33'
  who: Aishwarya
- line: Also, with VR glasses, you probably heard that Meta and other companies have
    them. You put them on, and they have cameras that provide a broader view than
    mobile phones. Maybe this is something future alumni can work on.
  sec: 645
  time: '10:45'
  who: Alexey
- line: Yes, those are the things we’re trying to work around. It needs to be cost-efficient,
    and we can’t afford to use expensive hardware like LiDAR. Since everyone already
    has a mobile phone, we’re trying to make it work with what people already have.
  sec: 682
  time: '11:22'
  who: Aishwarya
- line: How expensive is LiDAR?
  sec: 702
  time: '11:42'
  who: Alexey
- line: It depends on the quality. You can find some that are really cheap and others
    that are extremely high-end.
  sec: 710
  time: '11:50'
  who: Aishwarya
- header: Exploring LiDAR, radar, and Tesla’s camera-based approach
- line: How do you pronounce it? LiDAR?
  sec: 718
  time: '11:58'
  who: Alexey
- line: It’s LiDAR.
  sec: 723
  time: '12:03'
  who: Aishwarya
- line: LiDAR. I know radar emits radio frequencies and waits for the waves to return
    to estimate objects and their movement. Bats do this with sound. LiDAR is similar,
    but instead of radio waves, it uses light, right?
  sec: 728
  time: '12:08'
  who: Alexey
- line: Yes, that’s right. It uses light rays. That’s why it’s called LiDAR.
  sec: 770
  time: '12:50'
  who: Aishwarya
- line: I thought it was based on lasers.
  sec: 781
  time: '13:01'
  who: Alexey
- line: It’s similar. I think it’s one of the light frequencies.
  sec: 783
  time: '13:03'
  who: Aishwarya
- line: I don’t know if you can talk about your work, but these systems are often
    used in cars, right?
  sec: 788
  time: '13:08'
  who: Alexey
- line: Yes, for self-driving. It depends on the company’s stack. Some use LiDAR for
    fully self-driving systems where there’s no driver at all, while others like Tesla
    rely solely on cameras.
  sec: 801
  time: '13:21'
  who: Aishwarya
- line: I’ve taken a few rides in Teslas as taxis, and it was fun to watch the screen
    showing cars and people around. It was interesting to see when it made mistakes
    or didn’t. It made the ride more entertaining than a normal car because I could
    watch the screen.
  sec: 826
  time: '13:46'
  who: Alexey
- line: This system works with cameras, right? Sorry, I think I caught the flu this
    evening. I have a cold.
  sec: 860
  time: '14:20'
  who: Alexey
- line: I hope you recover quickly.
  sec: 880
  time: '14:40'
  who: Aishwarya
- line: Thank you. Could you please repeat how the Tesla visualization system works?
    Does it only use video cameras?
  sec: 885
  time: '14:45'
  who: Alexey
- line: Yes, that’s the unique part of Tesla’s system. Since LiDAR is expensive, they
    focus on scalability and rely on cameras. But it’s not just one camera. There
    are cameras all around the car providing a 360-degree view.
  sec: 905
  time: '15:05'
  who: Aishwarya
- line: The models process these different views to understand the surroundings and
    see all around the car. The car has a more holistic view of the world than a human
    driver, who cannot see behind or to the sides at the same time.
  sec: 928
  time: '15:28'
  who: Aishwarya
- line: Yes, that makes sense. The goal of self-driving is to make driving safer once
    the AI reaches that level.
  sec: 954
  time: '15:54'
  who: Alexey
- header: Trust, regulation, and challenges in self-driving adoption
- line: But what is this screen for? The self-driving system is there, but in the
    taxis I took, the drivers were still driving. So what’s the point of the screen?
  sec: 966
  time: '16:06'
  who: Alexey
- line: At this point, it serves two purposes. On long drives or in stop-and-go traffic,
    you can use autopilot mode and don’t need to stay constantly alert. The car assists
    you.
  sec: 984
  time: '16:24'
  who: Aishwarya
- line: I remember two years ago, I took a trip to Las Vegas, a 13-hour drive each
    way. The car handled about 95% of the driving, and I was just there monitoring.
    It made the trip so much easier because driving that long alone would have been
    exhausting.
  sec: 1004
  time: '16:44'
  who: Aishwarya
- line: It’s like an assistant system. Some people still prefer to drive because they
    don’t fully trust it yet. It’s also about building that trust factor.
  sec: 1025
  time: '17:05'
  who: Aishwarya
- line: I wonder if there are statistics about that.
  sec: 1038
  time: '17:18'
  who: Alexey
- line: Yes, there are statistics about failure rates and performance.
  sec: 1046
  time: '17:26'
  who: Aishwarya
- line: People often say, “It’s better if I drive than AI,” but the question is who
    actually drives better. Some people might be overconfident in their driving skills.
  sec: 1050
  time: '17:30'
  who: Alexey
- line: For long straight routes, like your trip to Vegas, maybe the AI handles it
    better. Was it mostly a straight highway?
  sec: 1067
  time: '17:47'
  who: Alexey
- line: Yes, it was a highway, so there weren’t many traffic lights or turns. You
    just go straight for miles. There’s a stretch that’s about 150 miles of straight
    road, and a normal person would be bored out of their mind driving that long.
  sec: 1072
  time: '17:52'
  who: Aishwarya
- line: I think it’s a highway, so there isn’t much traffic or many lights. You just
    go straight along the route. There’s a patch about 150 miles long that’s completely
    straight, and a normal person would get bored driving that much.
  sec: 1072
  time: '17:52'
  who: Aishwarya
- line: In Berlin, it’s probably more difficult because there are many bikes. The
    streets are narrow, and cyclists can appear suddenly. I guess that’s why they
    don’t use self-driving cars here.
  sec: 1090
  time: '18:10'
  who: Alexey
- line: I think Tesla is trying to enter the European markets with its autopilot.
    When I was there, I worked on recognizing European road signs, such as speed-limit
    signs.
  sec: 1112
  time: '18:32'
  who: Aishwarya
- line: But it’s also regulated, right? So maybe they can’t use self-driving yet.
  sec: 1125
  time: '18:45'
  who: Alexey
- line: Not yet.
  sec: 1133
  time: '18:53'
  who: Aishwarya
- line: That makes sense. I’m originally from Russia, and I know that in Moscow some
    cars already drive without drivers. I guess in San Francisco too, right?
  sec: 1139
  time: '18:59'
  who: Alexey
- line: Yes. San Francisco also has Waymo, which has no driver at all. People find
    it very interesting.
  sec: 1149
  time: '19:09'
  who: Aishwarya
- line: So you get something like Uber, and then a car comes with no driver, right?
  sec: 1156
  time: '19:16'
  who: Alexey
- line: Yes, there’s no one there. If you visit San Francisco, be sure to take a Waymo.
    It’s quite the tourist attraction right now.
  sec: 1162
  time: '19:22'
  who: Aishwarya
- line: Okay. That’s where you work, right?
  sec: 1174
  time: '19:34'
  who: Alexey
- line: Yes.
  sec: 1179
  time: '19:39'
  who: Aishwarya
- header: Waymo, ride-hailing, and gesture recognition for traffic control
- line: Is there an app called Waymo?
  sec: 1181
  time: '19:41'
  who: Alexey
- line: Yes, there’s a Waymo app you can use to hail a ride. In some cities, they’ve
    also partnered with Uber and Lyft so you can call a Waymo through those apps as
    well.
  sec: 1186
  time: '19:46'
  who: Aishwarya
- line: How much about your current position can you talk about? You mentioned you
    work on gesture recognition. Can you tell us more about that?
  sec: 1197
  time: '19:57'
  who: Alexey
- line: I can give a high-level picture. It’s about trying to understand gestures
    from people such as police officers or construction workers who guide traffic,
    for example when there’s a big event or roadwork.
  sec: 1217
  time: '20:17'
  who: Aishwarya
- line: So there is a police officer who tells you to slow down?
  sec: 1229
  time: '20:29'
  who: Alexey
- line: They tell you to stop or to go. Humans slow down when there is a police officer.
    The car tries to follow traffic rules. I try to understand what they want to communicate
    and modify the car's route or behavior accordingly.
  sec: 1235
  time: '20:35'
  who: Aishwarya
- line: In the case of my mom, if a ride-hailing car comes without a driver and there
    is suddenly an event with a lot of people, what should the car do? In training
    data, it is less common to have such cases, like a traffic light breaking or a
    police officer controlling traffic.
  sec: 1265
  time: '21:05'
  who: Alexey
- line: I think all of these cases are covered. Waymo has been in business for around
    15 years and they have worked to cover many of the cases we see. Broken traffic
    lights and large crowds are handled well. There are sometimes events and game
    nights where it performs very well. During those cases police officers direct
    traffic and my job is to make Waymo better at understanding them.
  sec: 1296
  time: '21:36'
  who: Aishwarya
- line: How much can you talk about this project? What kind of technology do you use,
    and how fast does it need to be to make decisions in real time?
  sec: 1337
  time: '22:17'
  who: Alexey
- line: There are in-house models that use cameras, LiDAR, and other sensor information
    from the car. Waymo does not publish the exact models it uses. The internal models
    are optimized to run on the car and to run very fast. They are not necessarily
    the same networks used during training. We use techniques so they can detect multiple
    times per second and understand what is happening in the world in real time.
  sec: 1363
  time: '22:43'
  who: Aishwarya
- line: What is this process called when you take a big model and make it smaller
    and faster?
  sec: 1408
  time: '23:28'
  who: Alexey
- line: There are many ways. One publicly known method is quantization. Quantization
    makes the model smaller and faster. There are many similar techniques and additional
    internal optimizations.
  sec: 1415
  time: '23:35'
  who: Aishwarya
- header: Malaria mapping in Africa and AI for social good
- line: I do not want to put you in an uncomfortable position by asking too many details.
    One project I find interesting is the malaria mapping project in Africa. Can you
    tell us more about that?
  sec: 1445
  time: '24:05'
  who: Alexey
- line: This was when I was at Morgan Stanley and I found the domain really interesting.
    I joined Omdena, which runs AI for good projects. They pair nonprofits with volunteer
    ML engineers who form teams of thirty to forty people. One nonprofit, Zap Malaria,
    led fumigation efforts in Africa and wanted to make fumigation more efficient
    by targeting areas with high mosquito probability.
  sec: 1471
  time: '24:31'
  who: Aishwarya
- line: Initially, they would just go to places and fumigate to prevent breeding and
    spread. They wanted to target only regions with high probability of mosquitoes
    instead of everywhere. We thought satellite images or knowledge of marshy lands
    and stagnant water could identify breeding grounds.
  sec: 1518
  time: '25:18'
  who: Aishwarya
- line: That approach would let fumigation teams focus efforts and save manpower and
    cost, which is crucial for nonprofits. Our team split into groups; one used satellite
    images to detect stagnant water bodies. My model used topographic information
    from Google to identify low-lying areas likely to collect water.
  sec: 1549
  time: '25:49'
  who: Aishwarya
- line: We trained models to detect those regions and combined satellite and topographic
    approaches into an ensemble. They integrated this system and reported very good
    results. It was a volunteer-based, AI-for-good project.
  sec: 1584
  time: '26:24'
  who: Aishwarya
- line: That sounds interesting. How accurate was this approach? Did they share feedback
    from the ground?
  sec: 1623
  time: '27:03'
  who: Alexey
- line: They did. They reported the model performed well and allowed them to focus
    on critical areas. They shared that it helped them save time and improve effectiveness.
    It was fulfilling because it had a clear social impact.
  sec: 1637
  time: '27:17'
  who: Aishwarya
- line: That must have felt rewarding. Working on projects that create real-world
    benefits is always motivating.
  sec: 1667
  time: '27:47'
  who: Alexey
- line: Absolutely. It showed how machine learning can help with problems outside
    the corporate world. It also gave me the confidence to work on complex challenges
    in different domains.
  sec: 1677
  time: '27:57'
  who: Aishwarya
- line: How did you end up at Waymo after that? The transition from finance to self-driving
    cars sounds big.
  sec: 1699
  time: '28:19'
  who: Alexey
- line: It happened step by step. I worked in finance, then healthcare, and finally
    moved to autonomous vehicles. Each step helped me build different technical and
    domain skills. I wanted to work on something that combines AI with real-world
    physical systems, and Waymo was perfect for that.
  sec: 1711
  time: '28:31'
  who: Aishwarya
- line: What does your day-to-day work look like at Waymo?
  sec: 1745
  time: '29:05'
  who: Alexey
- line: I work mostly on perception models, helping the car understand the world around
    it. That includes identifying pedestrians, vehicles, traffic lights, and understanding
    dynamic situations. I also work on improving accuracy and speed. The models must
    process information very quickly while maintaining reliability.
  sec: 1751
  time: '29:11'
  who: Aishwarya
- header: Deployment, safety, and testing in self-driving systems
- line: How do you test those systems before putting them on the road?
  sec: 1785
  time: '29:45'
  who: Alexey
- line: There are multiple stages. First, we test everything in simulation, where
    we recreate millions of real-world scenarios. Then we move to closed tracks with
    controlled conditions. Finally, we do on-road testing with safety drivers. Only
    after extensive testing do we deploy updates to cars operating without drivers.
  sec: 1791
  time: '29:51'
  who: Aishwarya
- line: That makes sense. The safety requirements must be very strict.
  sec: 1829
  time: '30:29'
  who: Alexey
- line: Yes, extremely strict. Safety is the top priority in every decision. Each
    change goes through rigorous validation and approval. There are layers of redundancy
    to ensure that even if one system fails, others keep the car safe.
  sec: 1835
  time: '30:35'
  who: Aishwarya
- line: What kind of data do you collect from the cars?
  sec: 1862
  time: '31:02'
  who: Alexey
- line: We collect sensor data like camera images, LiDAR scans, radar, and GPS. We
    also gather metadata about driving conditions and system responses. The data is
    anonymized and used only for improving performance and safety.
  sec: 1867
  time: '31:07'
  who: Aishwarya
- line: That must be a huge amount of data.
  sec: 1897
  time: '31:37'
  who: Alexey
- line: It is massive. Waymo has been operating for years, so the scale of data is
    huge. Managing and labeling it is a major challenge. We rely heavily on internal
    tooling and automation.
  sec: 1902
  time: '31:42'
  who: Aishwarya
- line: Do you use human labelers or automatic labeling for that data?
  sec: 1929
  time: '32:09'
  who: Alexey
- line: Both. Human labelers handle complex cases, while automatic systems take care
    of repetitive tasks. The combination improves both speed and accuracy. We constantly
    refine labeling quality to ensure the models learn from the best data possible.
  sec: 1934
  time: '32:14'
  who: Aishwarya
- line: How often do you update the models in the cars?
  sec: 1963
  time: '32:43'
  who: Alexey
- line: Updates depend on project cycles and validation results. Some improvements
    roll out every few weeks, while major updates take longer. Every release goes
    through multiple safety checks and real-world validation before deployment.
  sec: 1968
  time: '32:48'
  who: Aishwarya
- line: How large is the team you work with?
  sec: 1999
  time: '33:19'
  who: Alexey
- line: Waymo has many specialized teams. I work closely with perception, data, and
    simulation engineers. Collaboration is key because every component affects others.
    Even a small change can influence performance across the system.
  sec: 2004
  time: '33:24'
  who: Aishwarya
- line: It sounds like a huge operation.
  sec: 2036
  time: '33:56'
  who: Alexey
- line: It is. Building autonomous driving technology requires expertise in software,
    hardware, sensors, and safety. Each team contributes to a different layer, and
    together they make the system work smoothly.
  sec: 2040
  time: '34:00'
  who: Aishwarya
- line: What do you enjoy most about your work?
  sec: 2069
  time: '34:29'
  who: Alexey
- line: I enjoy solving real-world problems with tangible impact. Seeing a car drive
    safely using models we built is very satisfying. It feels like working on the
    future of mobility.
  sec: 2073
  time: '34:33'
  who: Aishwarya
- line: Do you sometimes ride in Waymo cars yourself?
  sec: 2099
  time: '34:59'
  who: Alexey
- line: Yes, I have. It is an amazing experience. The first time feels a bit strange
    because there is no driver, but after a few minutes you realize how smoothly it
    drives. It follows all rules and handles complex scenarios confidently.
  sec: 2104
  time: '35:04'
  who: Aishwarya
- line: That must be surreal. How does it handle unexpected events like pedestrians
    suddenly crossing?
  sec: 2134
  time: '35:34'
  who: Alexey
- line: The car constantly monitors surroundings with multiple sensors. It predicts
    motion paths and can react within milliseconds. It prioritizes safety and will
    slow down or stop immediately when needed.
  sec: 2143
  time: '35:43'
  who: Aishwarya
- line: How much of this technology is transferable to other domains?
  sec: 2172
  time: '36:12'
  who: Alexey
- line: Quite a lot. Perception, prediction, and planning models have applications
    beyond autonomous driving. Similar approaches can be used in robotics, drones,
    or industrial automation.
  sec: 2177
  time: '36:17'
  who: Aishwarya
- line: Do you collaborate with research teams or external partners?
  sec: 2204
  time: '36:44'
  who: Alexey
- line: Yes. We collaborate with academic and research groups to advance the field.
    Waymo also contributes to open-source tools and publishes papers to share learnings
    with the broader community.
  sec: 2209
  time: '36:49'
  who: Aishwarya
- header: Transition from NLP to computer vision and deep learning
- line: That’s great. What’s one thing you learned from working at Waymo that surprised
    you?
  sec: 2238
  time: '37:18'
  who: Alexey
- line: How complex real-world driving is. Even simple-looking actions involve multiple
    models and systems working together. It made me appreciate how much coordination
    and testing is required to make everything reliable.
  sec: 2245
  time: '37:25'
  who: Aishwarya
- line: What advice would you give to someone who wants to work in self-driving technology?
  sec: 2277
  time: '37:57'
  who: Alexey
- line: Start by building a strong foundation in machine learning and computer vision.
    Get hands-on experience with data and simulation. Learn about safety-critical
    systems because reliability is key in this field.
  sec: 2283
  time: '38:03'
  who: Aishwarya
- line: Do you think it’s a good time to enter the industry?
  sec: 2313
  time: '38:33'
  who: Alexey
- line: Yes. The field is evolving quickly, and there’s still so much to explore.
    Many challenges remain, especially around edge cases and scaling. It’s a great
    time for engineers who like solving complex problems.
  sec: 2318
  time: '38:38'
  who: Aishwarya
- line: What skills are most valuable for someone entering this space?
  sec: 2349
  time: '39:09'
  who: Alexey
- line: Strong programming skills, understanding of ML fundamentals, and experience
    with large-scale systems. Knowing data pipelines and simulation helps too. Curiosity
    and persistence matter a lot because the work can be challenging.
  sec: 2355
  time: '39:15'
  who: Aishwarya
- line: Do you think the industry is close to full self-driving adoption?
  sec: 2389
  time: '39:49'
  who: Alexey
- line: We are getting closer. Fully autonomous driving in all conditions is still
    hard, but progress is steady. It will likely start with limited areas and then
    expand gradually as technology matures.
  sec: 2394
  time: '39:54'
  who: Aishwarya
- line: Do you see Waymo expanding internationally?
  sec: 2429
  time: '40:29'
  who: Alexey
- line: Potentially, yes. Each country has different regulations and infrastructure,
    so it takes time. Waymo is focused on perfecting safety and scalability first
    before expanding widely.
  sec: 2434
  time: '40:34'
  who: Aishwarya
- line: What kind of challenges do regulations create?
  sec: 2463
  time: '41:03'
  who: Alexey
- line: Regulations vary by region. Some areas allow testing with safety drivers,
    while others permit fully driverless operations. We work closely with local authorities
    to ensure compliance and transparency.
  sec: 2468
  time: '41:08'
  who: Aishwarya
- line: How does public perception affect your work?
  sec: 2500
  time: '41:40'
  who: Alexey
- line: Public trust is essential. We focus on transparency, safety, and consistent
    communication. People need to feel comfortable sharing the road with autonomous
    cars. Every successful ride helps build that confidence.
  sec: 2505
  time: '41:45'
  who: Aishwarya
- line: If you could apply your skills to another big problem in the world, what would
    it be?
  sec: 2538
  time: '42:18'
  who: Alexey
- line: Probably climate change. Machine learning can help optimize energy usage,
    improve transportation efficiency, and support sustainability efforts. Applying
    technology to make a positive global impact is very motivating.
  sec: 2544
  time: '42:24'
  who: Aishwarya
- line: That’s inspiring. Thank you for sharing your experience and insights. It was
    great learning about your work and the impact of AI in the real world.
  sec: 2576
  time: '42:56'
  who: Alexey
- line: Thank you. It was a pleasure talking with you.
  sec: 2587
  time: '43:07'
  who: Aishwarya
- line: For me, I think it would be two weeks. If I needed to get into any modern
    papers like this, I don’t know if I would go to Arxiv and take any paper about
    NLP or computer vision. Yeah, good that we have ChatGPT now, so I can ask it to
    explain things.
  sec: 2596
  time: '43:16'
  who: Alexey
- header: Reinforcement learning, robotics, and self-driving constraints
- line: That is so good now. It wasn’t there back when we were in school and college
    doing assignments. Where was ChatGPT then?
  sec: 2618
  time: '43:38'
  who: Aishwarya
- line: Interesting that you mentioned you didn’t have any prior experience with reinforcement
    learning because I thought reinforcement learning is something used quite often
    for driving too. For me, before this whole LLM space appeared, AI meant machine
    learning, which was a part of AI. But reinforcement learning can get an agent
    to do things in an environment and learn.
  sec: 2624
  time: '43:44'
  who: Alexey
- line: There were companies I interviewed with that were creating environments for
    self-driving cars to test in. They had environments with streets and everything
    looking very realistic. It was in Germany, so I guess companies like BMW and Audi
    that work on self-driving could use it to test their cars. They used reinforcement
    learning frameworks where the car could go wild and learn that hitting a pedestrian
    results in a penalty, so it learns not to do that.
  sec: 2660
  time: '44:20'
  who: Alexey
- line: It was interesting, but it didn’t work out, so I didn’t join the company.
    It was funny—it was a company with four people in a basement and a lot of GPUs.
    They thought they needed one more person.
  sec: 2707
  time: '45:07'
  who: Alexey
- line: That doesn’t sound very stable. Wow, okay. But it was a good thing. Reinforcement
    learning is interesting.
  sec: 2724
  time: '45:24'
  who: Aishwarya
- line: My first interaction with reinforcement learning was with robots. In college,
    we had Robo Wars where you build your robot, go to a tech festival, and compete
    against others. Reinforcement learning is still a big part of robotics.
  sec: 2737
  time: '45:37'
  who: Aishwarya
- line: 'So far, my career has been in computer vision and robotics, mostly on the
    perception side understanding the world. Reinforcement learning comes in when
    teaching an agent how to behave in the world. These are two parts of the stack:
    perception and behavior.'
  sec: 2755
  time: '45:55'
  who: Aishwarya
- line: I work on perception making the agent understand the world while reinforcement
    learning is for behavior. Even though I’m in the self-driving industry, I’ve never
    worked on that part. I skipped reinforcement learning courses in college because
    I found them hard.
  sec: 2791
  time: '46:31'
  who: Aishwarya
- line: But I imagine you would not let a car go wild and learn how to interact with
    pedestrians outside in real life. That would not be fun. That’s for sure it’s
    karma gone wrong.
  sec: 2810
  time: '46:50'
  who: Alexey
- line: Honestly, I don’t know if we use reinforcement learning. I’ve never tried
    to find out because it looks more like a fun project to do in an emulator.
  sec: 2827
  time: '47:07'
  who: Aishwarya
- line: 'Yeah, but in real life, you still need some rules. There’s actually a question
    from Ole. He’s asking about self-driving: is it full AI or a mix of rules and
    AI? I assume he means self-driving because full AI would be reinforcement learning
    when the car learns to drive by itself. But we still need to add rules. What’s
    the current state of self-driving AI?'
  sec: 2839
  time: '47:19'
  who: Alexey
- line: I think all environments, even in reinforcement learning or other training
    methods, have constraints. You impose the rules of the world, like not driving
    against traffic. It’s not completely free to learn however it wants.
  sec: 2876
  time: '47:56'
  who: Aishwarya
- line: It’s definitely constrained by many rules. As you expand into different countries
    or continents, new rules appear. Even within a country, different cities have
    different driving patterns. Some are aggressive, and some follow rules more closely.
    It needs to adapt and remain constrained.
  sec: 2910
  time: '48:30'
  who: Aishwarya
- line: In Italy and Germany, driving is very different. In Berlin, people drive slowly,
    and it’s easy to cross the street. But in southern Italy, good luck—you just have
    to walk across, and then they stop. Otherwise, they keep going.
  sec: 2939
  time: '48:59'
  who: Alexey
- line: It still needs to learn all these patterns. That’s why it’s such a hard problem.
    Everything changes so much across geographies.
  sec: 2964
  time: '49:24'
  who: Aishwarya
- line: I was thinking about chess. In chess and Go, reinforcement learning was used
    to build state-of-the-art models. They let the AI explore the game freely instead
    of learning from past games. Because of that, it could play better than humans.
  sec: 2970
  time: '49:30'
  who: Alexey
- line: With self-driving, it’s different. You still need to obey rules. In chess,
    you also have rules like how a knight or bishop moves, but they are fixed and
    limited.
  sec: 3015
  time: '50:15'
  who: Alexey
- line: The difference is that in chess, the rules are fixed every piece has a clear
    purpose, and that’s it. You can explore within those limits. But in self-driving,
    the rules are constantly evolving.
  sec: 3029
  time: '50:29'
  who: Aishwarya
- line: You have an infinite number of rules, so it’s hard to teach the model in such
    a changing environment. I honestly don’t know if we use reinforcement learning,
    but constraints definitely play a role in any model we use.
  sec: 3062
  time: '51:02'
  who: Aishwarya
- header: Testing processes, evaluations, and staged rollouts for autonomous driving
- line: 'There’s a question from Adonis: how does testing work for sensitive cases
    like autonomous driving? Do developers inherit tests, or are there stages? How
    is testing organized?'
  sec: 3088
  time: '51:28'
  who: Alexey
- line: It depends on what change you’re making. I work on pedestrians and gestures,
    so we have evaluations around cases with pedestrians or past events. We rerun
    new models on those cases as the first stage.
  sec: 3116
  time: '51:56'
  who: Aishwarya
- line: Then we evaluate a broader set of real-world scenarios involving pedestrians.
    Like the question mentioned, there are stages where you start small, then move
    to larger evaluation sets. Finally, you roll it out slowly to drivers and expand.
  sec: 3136
  time: '52:16'
  who: Aishwarya
- header: Can multimodal LLMs be applied to self-driving?
- line: Another question about LLMs. We already talked about how they can do computer
    vision, but they are slow. Can they be applied to self-driving? Does it make sense
    to use generative models for that?
  sec: 3173
  time: '52:53'
  who: Alexey
- line: There have been many attempts. The latest research and some companies like
    Wave are using multimodal LLMs for end-to-end self-driving. There’s room for it
    because LLMs are pretrained on massive data, so they have world knowledge.
  sec: 3200
  time: '53:20'
  who: Aishwarya
- line: The challenge is making them fast enough. Tradeoffs and techniques are needed,
    but it’s actively explored in research and by companies. Some systems already
    use LLMs for self-driving.
  sec: 3237
  time: '53:57'
  who: Aishwarya
- line: We talked about patterns in different countries, like Italy versus Germany.
    LLMs might already know these differences from their training data. Maybe that
    makes it easier for them to adapt.
  sec: 3257
  time: '54:17'
  who: Alexey
- line: That’s the hope, that they have some knowledge about various things that curated
    datasets might miss. LLMs have broad world knowledge, so they can help tune systems
    for global use.
  sec: 3293
  time: '54:53'
  who: Aishwarya
- header: How to get started in self-driving AI careers
- line: Okay, maybe last question. If I want to work on self-driving cars, what should
    I do? What should I study? How can I get into this industry?
  sec: 3325
  time: '55:25'
  who: Alexey
- line: It starts with deep learning. I was good at deep learning and got into the
    AI Guard Dog project, which used vision and navigation. That led me to Tesla.
    It’s about knowing fundamentals and doing relevant projects.
  sec: 3345
  time: '55:45'
  who: Aishwarya
- line: If you do computer vision projects, that’s a great start. It helps your resume
    stand out so companies know you’re familiar with the space, and you can get interviews
    and improve from there.
  sec: 3372
  time: '56:12'
  who: Aishwarya
- line: So, a good pet project could be building an app that uses your camera to describe
    objects in your room. It could say there’s a bed, a clock, and so on.
  sec: 3384
  time: '56:24'
  who: Alexey
- line: Yes, and with LLMs, it’s even easier. If you prompt an LLM correctly, you
    don’t need to train anything; it just tells you what’s in the room.
  sec: 3412
  time: '56:52'
  who: Aishwarya
- line: You can even ask ChatGPT to write the app and then learn from how it did it.
  sec: 3425
  time: '57:05'
  who: Alexey
- line: That’s two stages, you don’t even write the app yourself; the AI does it.
  sec: 3432
  time: '57:12'
  who: Aishwarya
- line: I recently used a tool like Cursor, a coding agent. I asked it to implement
    a multi-agent system for evaluating GitHub projects, and half an hour later, it
    worked.
  sec: 3441
  time: '57:21'
  who: Alexey
- line: I tweaked it a bit with prompts, and it was running. Then I studied the code
    to understand how it was implemented, and I thought, okay, now I know how to do
    it.
  sec: 3460
  time: '57:40'
  who: Alexey
- line: It’s fascinating. These projects used to take weeks in college, but now they’re
    done so quickly. Still, sometimes it gets stuck on weird bugs.
  sec: 3471
  time: '57:51'
  who: Aishwarya
- line: Then you have to intervene and learn what the AI built before fixing the bug.
    You have to understand the entire codebase.
  sec: 3485
  time: '58:05'
  who: Alexey
- line: It’s great for setting up frameworks when starting new projects from scratch.
    But for details, you still need to know what you’re doing.
  sec: 3503
  time: '58:23'
  who: Aishwarya
- line: Okay, it was amazing talking to you. Thanks a lot. I’m glad we made it work.
    Sorry you were sick. I hope you recover quickly. It’s late for you, so you should
    rest, and I’ll go have breakfast.
  sec: 3515
  time: '58:35'
  who: Alexey
- line: All right, have a good day.
  sec: 3535
  time: '58:55'
  who: Aishwarya
- line: You too. Thanks, everyone, for joining us today.
  sec: 3541
  time: '59:01'
  who: Alexey
---

Links:

* [Linkedin](https://www.linkedin.com/in/aishwaryajadhav8/){:target="_blank"}