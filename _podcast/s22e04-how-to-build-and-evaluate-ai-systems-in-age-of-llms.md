---
episode: 4
guests:
- hugobowneanderson
ids:
  anchor: datatalksclub/episodes/How-to-Build-and-Evaluate-AI-systems-in-the-Age-of-LLMs---Hugo-Bowne-Anderson-e39vt24
  youtube: eC3RNuI6ow0
image: images/podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/How-to-Build-and-Evaluate-AI-systems-in-the-Age-of-LLMs---Hugo-Bowne-Anderson-e39vt24
  apple: https://podcasts.apple.com/us/podcast/how-to-build-and-evaluate-ai-systems-in-the-age-of/id1541710331?i=1000733350691
  spotify: https://open.spotify.com/episode/2RD2qXaYa2ZjKjuIE7Aj6O
  youtube: https://www.youtube.com/watch?v=eC3RNuI6ow0
season: 22
short: How to Build and Evaluate AI systems in the Age of LLMs
title: How to Build and Evaluate AI systems in the Age of LLMs
transcript:
- header: Episode Introduction & Guest Bio
- line: This week we will talk about LLMs and AI like everyone else, I guess.
  sec: 0
  time: 0:00
  who: Alexey
- line: The difference between everyone else and us is that we have amazing Hugo joining
    us. You might have figured it out from our discussion that he is a returning guest
    and also a teacher. I have a video that I will read, I guess. Hugo is an independent
    data and AI consultant with extensive expertise in the tech industry. He has advised
    and taught teams building AI powered systems including engineers from Netflix,
    Meta, and the US Air Force. That is quite far from Australia, isn’t it?
  sec: 0
  time: 0:00
  who: Alexey
- line: You can still teach online these days, thank goodness. You do not need to
    go to the US to teach them.
  sec: 45
  time: 0:45
  who: Hugo
- line: That is good. He is also the host of Vanishing Radiance. I think your background
    is a hint about that and High Signal. I have no idea what High Signal is. You
    will probably tell us. It is a podcast exploring developments in data science.
    Why do you need two podcasts, by the way?
  sec: 50
  time: 0:50
  who: Alexey
- header: 'Podcasts Overview: Vanishing Gradients and High Signal'
- line: One, Vanishing Gradients, is really for builders who want to know what they
    can learn today to ship and maintain products. High Signal is a lot of conversations
    with people in leadership. We have had Michael Jordan on High Signal and Fay Lee
    and Chris Wiggins who runs data science at the New York Times. It is really intended
    for leaders who are also practitioners but thinking at a higher level.
  sec: 72
  time: '1:12'
  who: Hugo
- line: Which Michael Jordan are you talking about?
  sec: 100
  time: '1:40'
  who: Alexey
- line: The Michael Jordan of machine learning. He is from Berkeley originally but
    lives in Italy now.
  sec: 105
  time: '1:45'
  who: Hugo
- line: He has a book about machine learning, right?
  sec: 113
  time: '1:53'
  who: Alexey
- line: Yes, exactly. He has done a lot of stuff.
  sec: 115
  time: '1:55'
  who: Hugo
- line: Is it called Machine Learning or something else?
  sec: 117
  time: '1:57'
  who: Alexey
- line: I would need to fact check myself.
  sec: 118
  time: '1:58'
  who: Hugo
- header: 'Career Journey: Academia to Data science and DevRel'
- line: I remember when I was studying machine learning in 2012 or 2013. I thought,
    “Oh, Michael Jordan, interesting.” Later, after some time, I realized which one
    you meant. Tell us about your career journey so far. We remember that you were
    doing DevRel. We also talked about your teaching experience, but can you give
    us the full picture?
  sec: 124
  time: '2:04'
  who: Alexey
- line: My background is in basic research in biology, mathematics, and physics. I
    lived in Dresden, close to you, for a couple of years. There is a Max Planck Institute
    for Cell Biology and Genetics there where I did part of my postdoc over a decade
    ago.
  sec: 161
  time: '2:41'
  who: Hugo
- line: Over a decade ago. So that is how you know a bit of German, right? When I
    was eating, you said “gut” and a bit.
  sec: 172
  time: '2:52'
  who: Alexey
- line: Exactly. I realized I needed to analyze large scale data that my colleagues
    were generating, so I taught myself Python. I jumped into what were then called
    IPython notebooks, not Jupyter notebooks, and the growing PyData stack. Pandas
    and Matplotlib were key tools. At that point pandas did not even have a read CSV
    function. When it was added, it really started to super power us.
  sec: 187
  time: '3:07'
  who: Hugo
- line: Then I moved to the US and lived in New York while working at Yale University
    in New Haven. There were so many data science and machine learning meetups and
    hackathons in 2014 and 2015 in New York. It was so exciting that I decided to
    join industry. I met the DataCamp team and joined as the fifth employee to build
    out the Python curriculum. As an early employee I wore many hats including product,
    data science, curriculum, and marketing.
  sec: 207
  time: '3:27'
  who: Hugo
- header: Freelance Consulting, Advising, and Teaching Focus
- line: I started a podcast there called The DataFrame Podcast which was super fun.
    During the pandemic I worked at several PyData adjacent open source tooling companies
    leading developer relations. Then last year the space became too exciting for
    me to focus on one project. I went freelance doing consulting, advising, teaching,
    and developer relations across the board. It is an exciting time, and I get to
    collaborate and work with many wonderful people such as yourself now.
  sec: 237
  time: '3:57'
  who: Hugo
- line: That is really cool. Your journey from academia to developer relations is
    exciting. For me, doing developer relations sounds cool because you get to teach
    people and receive good money for it. I am originally from Russia, and being a
    teacher there is not always the best paid profession. It is cool that there is
    an opportunity for people to educate and also receive good pay from the IT sector.
  sec: 278
  time: '4:38'
  who: Alexey
- line: Since then you switched focus to consulting. How did that happen? It has been
    a few years, right? About a year and a half? You were at Outerbounds doing developer
    relations. That is the orchestrator platform, right?
  sec: 327
  time: '5:27'
  who: Alexey
- line: Metaflow.
  sec: 345
  time: '5:45'
  who: Hugo
- line: Metaflow, yes. I remember it was something with “flow.”
  sec: 350
  time: '5:50'
  who: Alexey
- line: There are too many flows.
  sec: 352
  time: '5:52'
  who: Hugo
- line: Exactly. I was thinking which one it was. It was Metaflow. You did developer
    relations there. What happened after that? Did you decide you wanted to consult?
  sec: 353
  time: '5:53'
  who: Alexey
- line: Exactly. I wanted to consult, do a lot of podcasting and education, and help
    people ship and build products in a variety of ways. In my consulting I also do
    a lot of internal training, both on the technical side and the executive side.
    I teach people how to leverage AI to build software and also advise executives.
    It is a wild time and there is more work than I can do myself, so it is definitely
    exciting.
  sec: 368
  time: '6:08'
  who: Hugo
- line: What kind of work do you do?
  sec: 398
  time: '6:38'
  who: Alexey
- line: Everything from consulting to advising and teaching, as well as developer
    relations.
  sec: 404
  time: '6:44'
  who: Hugo
- line: Consulting, teaching, I am just taking notes to ask you later. Consulting,
    teaching, developer relations. What was the last thing?
  sec: 415
  time: '6:55'
  who: Alexey
- line: Advisory work as well.
  sec: 423
  time: '7:03'
  who: Hugo
- line: What is the difference between advisory and consulting?
  sec: 429
  time: '7:09'
  who: Alexey
- header: 'Consulting vs Advisory: Hands-on Work and Organizational Advice'
- line: In my consulting work I really help people ship products and build.
  sec: 431
  time: '7:11'
  who: Hugo
- line: So you basically open your VS Code and do OpenAI work. You actually code.
    Consulting is hands on, and advisory is more like, “This is how you do it, now
    you go do it,” right?
  sec: 435
  time: '7:15'
  who: Alexey
- line: Exactly, and even advising nontechnical people about how to restructure their
    organizations around AI tools and similar topics.
  sec: 447
  time: '7:27'
  who: Hugo
- line: Can you give an example? Why would they need to restructure? For example,
    to have data engineers helping machine learning people?
  sec: 455
  time: '7:35'
  who: Alexey
- line: For example, take a nontechnical marketing team. You have three individuals
    using ChatGPT, each writing their own prompts, and there are no synergistic effects.
    Even something basic like having a Slack channel where they can share prompts
    or a version controlled system for sharing prompts that work best can make a difference.
    Thinking about small technological tools that allow teams to work together with
    AI systems is key.
  sec: 466
  time: '7:46'
  who: Hugo
- header: 'Incentivizing AI Adoption: Loss Aversion and Dedicated Experimentation
    Time'
- line: There is interesting research on loss aversion. If you frame not using AI
    as a potential loss rather than using it as a gain, it can incentivize people
    more. Another thing that is important is that the most successful organizations
    adopting AI carve out time and space for people to use it. Instead of expecting
    efficiency gains on top of full time work, they dedicate half a day a week for
    employees to experiment with AI. It brings short term loss but medium and long
    term gains.
  sec: 504
  time: '8:24'
  who: Hugo
- line: Are there people who still have not tried it?
  sec: 560
  time: '9:20'
  who: Alexey
- line: A handful, not many.
  sec: 568
  time: '9:28'
  who: Hugo
- line: Everyone is talking about this. Two years ago someone on our Slack channel
    shared a screenshot of ChatGPT writing a poem about our machine learning engineering
    course. It was like, “Wow, a poem about the course, how cool is that.” Now everyone
    uses it. My mom uses it, though she is pretty advanced, but everyone does.
  sec: 568
  time: '9:28'
  who: Alexey
- line: My mom uses it, my dad has not. He knows about it and has seen screenshots.
    Many people who use it think it is just for conversations. They do not realize
    they can use it for transcript summarization, translation, content generation,
    idea generation, or filtering ideas. You can upload a document and have it summarized,
    although sometimes it pretends to summarize without really doing it.
  sec: 604
  time: '10:04'
  who: Hugo
- line: That is how I use it now, not necessarily for summarization, but for simple
    data processing with Excel or CSV files. I just upload and ask ChatGPT to do this
    or that for me and plot a graph. I can do it myself, but it saves so much time.
    I do not even need to write code anymore for these simple things. That is cool.
  sec: 646
  time: '10:46'
  who: Alexey
- header: 'Practical Prompting Use Cases: Summaries, CSVs, and Role-Based Prompts'
- line: Exactly. Many people do not realize you can generate CSV files or PDFs with
    it. Helping people understand how to prompt is also key. If you give it a role
    and an objective, like “You are a chief marketing officer writing this campaign,”
    and add examples and heuristics, it becomes incredibly useful.
  sec: 671
  time: '11:11'
  who: Hugo
- line: Let us say I want to create timestamps for YouTube. I guess you also do this.
    What is the most effective prompt for that? I have a transcript, we edit it slightly,
    and YouTube generates subtitles. I copy them to ChatGPT and say, “Give me YouTube
    time codes.” I specify the format, time code and chapter name, and that is it.
    How can I improve this process?
  sec: 705
  time: '11:45'
  who: Alexey
- header: Timestamp Generation Tools & Workflows (Gemini, Descript)
- line: I use Gemini because I do it programmatically as well. Gemini can get data
    directly from YouTube, and ChatGPT cannot because Google has blocked it from transcribing.
  sec: 742
  time: '12:22'
  who: Hugo
- line: That is why I copy and paste things.
  sec: 762
  time: '12:42'
  who: Alexey
- line: Gemini takes it straight in. Tell it not to hallucinate timestamps and to
    double check its work. If it is long, ask it to chunk the content. For videos
    I avoid all that. I use Descript. It generates excellent timestamps for me. If
    it is not broken, do not fix it.
  sec: 765
  time: '12:45'
  who: Hugo
- line: I use Loom for recording videos, and the prompt they have for timestamps needs
    improvement. If you were consulting a company like Loom, where they need to create
    timestamps, how would you suggest they approach it?
  sec: 794
  time: '13:14'
  who: Alexey
- line: We would look at the prompt and iterate on it several times. For this kind
    of prompting you would say, “Have an eye for detail.” You would also want timestamps
    relevant to your audience. For this podcast, maybe data science people, machine
    learning engineers, and AI engineers. The timestamps need to attract them.
  sec: 813
  time: '13:33'
  who: Hugo
- header: 'Quality Control Pattern: Evaluator–Optimizer for Generated Outputs'
- line: You would also want a subject matter expert in the loop to evaluate the results.
    Whoever used to write timestamps should be involved. Another effective approach
    is the evaluator optimizer pattern. You can have one model generate timestamps
    and another evaluate them, scoring the output and sending it back if it fails.
  sec: 836
  time: '13:56'
  who: Hugo
- line: How does it work? You have two models or agents, one evaluator and one optimizer.
    The evaluator looks at the output and gives it a score from zero to ten.
  sec: 889
  time: '14:49'
  who: Alexey
- line: You can just give it zero or one, pass or fail, and feedback.
  sec: 910
  time: '15:10'
  who: Hugo
- line: So the evaluator should have multiple criteria, right? Say ten criteria, each
    pass or fail.
  sec: 917
  time: '15:17'
  who: Alexey
- line: In the end you just want pass or fail, because either it goes to production
    or not.
  sec: 922
  time: '15:22'
  who: Hugo
- line: I see. With timestamps it is tricky because there are many correct answers.
    There are so many ways to split videos into chapters. How do you know which one
    is better?
  sec: 932
  time: '15:32'
  who: Alexey
- line: You want it aligned with your judgment, when Alexey sees it and says, “I like
    that.” You can give it examples and heuristics. For example, Alexey may dislike
    timestamps ten seconds apart. I would hate that. You can give it a heuristic,
    like if it is an hour long there should be only ten to fifteen timestamps.
  sec: 958
  time: '15:58'
  who: Hugo
- line: That is why prompt iteration, or prompt engineering, is important. It tries
    something, you review, then adjust. Maybe it starts using emojis, then you add
    “Do not use emojis.” After fifteen or twenty prompts you will have something that
    looks good for most videos.
  sec: 996
  time: '16:36'
  who: Hugo
- line: That is how I do it. I open ChatGPT, copy the transcript, play with the prompt
    until I like the result, and hopefully save the prompt, though usually I forget
    and start again next time. I check the output, copy the chapters to YouTube, and
    my job is done.
  sec: 1022
  time: '17:02'
  who: Alexey
- header: 'Scaling Transcript Work: Automation and GitHub Actions'
- line: If we have hundreds of transcripts, optimizing for one may worsen others,
    and I cannot check all one hundred. That is why we need an evaluator. I want correct
    transcripts and timestamps at least five minutes apart.
  sec: 1058
  time: '17:38'
  who: Alexey
- line: This is amazing because we are hitting on what it is like to build and iterate
    on AI powered software. First, you look at your data and see what works and what
    does not, then iterate. You are iterating on a prompt. If you are building retrieval
    augmented generation, maybe you iterate on chunking or embeddings.
  sec: 1090
  time: '18:10'
  who: Hugo
- line: If you are building agentic systems, maybe you iterate on tool call descriptions.
    You look at the data to see what happens next. The way you describe it, you iterate
    and then throw the prompt away and start again. You also mentioned wanting it
    to work across one hundred things.
  sec: 1130
  time: '18:50'
  who: Hugo
- line: If I build a product, one thing is doing it once and throwing it away. Another
    is keeping the prompt, reusing it, and giving it to my assistant so she can use
    it. That way I can be sure the transcript quality stays good because we have tested
    it.
  sec: 1152
  time: '19:12'
  who: Alexey
- line: Exactly. You do not want to overfit to the transcripts you have already tested.
    If your new transcript is similar, like another machine learning podcast, it will
    likely perform well. If it is something different, like carpentry, maybe adjust.
    But if you iterate enough and it performs well across a diverse set, it will generalize
    and save time.
  sec: 1180
  time: '19:40'
  who: Hugo
- line: We are building a pipeline that takes in transcripts and uses GitHub Actions
    to generate timestamps and other outputs, automating what I used to do by hand.
  sec: 1242
  time: '20:42'
  who: Hugo
- line: Yeah, that is what we do too. But this GitHub Actions is only for processing
    transcripts. Still, it is cool because it is free, right?
  sec: 1261
  time: '21:01'
  who: Alexey
- line: Yeah. Exactly.
  sec: 1274
  time: '21:14'
  who: Hugo
- line: How do you iterate 500 times on a prompt? You said some people iterate a few
    times, some a few hundred, and some a few thousand. For me, the way I come up
    with prompts is that I first type them myself. Then I add more and more details,
    and at some point, I ask ChatGPT, “Hey, this is the prompt I have. It cannot do
    this or that,” and I describe the cases it cannot handle.
  sec: 1275
  time: '21:15'
  who: Alexey
- line: The GPT5 version of the model is pretty good at creating very specific prompts
    that usually solve my problems. Then I have this prompt, and it kind of works.
    Maybe I do ten or fifteen iterations at most. But how do I go from that to 500?
    Is it humanly possible?
  sec: 1307
  time: '21:47'
  who: Alexey
- line: Yeah. It can take weeks. But this is iterating on prompts that ship SaaS software
    to tens or hundreds of thousands of people. I also use LLMs to write prompts.
    Prompts usually perform better when written or at least edited by humans.
  sec: 1326
  time: '22:06'
  who: Hugo
- line: As I said, LLMs will insert emojis into prompts all the time. There is no
    reason for that.
  sec: 1351
  time: '22:31'
  who: Hugo
- line: I hate formatting when it adds random stuff. It just increases the cost of
    my prompts.
  sec: 1364
  time: '22:44'
  who: Alexey
- line: Exactly. Maybe that is why they are doing it. Who knows? Demand generation.
  sec: 1369
  time: '22:49'
  who: Hugo
- header: 'Gold Test Sets: Size, Cost, and Representativeness for Evaluation'
- line: If you want to iterate 500 times on a prompt, you need to have a proper evaluation
    set, right?
  sec: 1380
  time: '23:00'
  who: Alexey
- line: That is a good question. Not necessarily at the beginning, but in the end,
    yes, especially when shipping reliable and consistent software. A lot of the time,
    you can just vibe check it. They call it vibe checking when you look at the result
    and think, the date format is not correct, so I will tell the prompt or use structured
    outputs to fix it.
  sec: 1385
  time: '23:05'
  who: Hugo
- line: A lot of things you can eyeball. In the end, though, you definitely want some
    kind of gold test set. Just as in machine learning, we have a hold out set and
    a test set. The premise is the same. The practice is a bit different because of
    rich natural language and tool calls.
  sec: 1415
  time: '23:35'
  who: Hugo
- line: How large should the evaluation data set or gold test set be? The problem
    is that unlike traditional machine learning, it might take a lot longer to evaluate.
    Even with deep learning, maybe it takes half a minute, but with prompt evaluation,
    it takes much longer. How large should the data set be?
  sec: 1436
  time: '23:56'
  who: Alexey
- line: We want the data set to be large, but if it is too large, it costs money and
    takes time. So we want it to be as small as possible but not too small. Otherwise,
    we might overfit to just a few examples.
  sec: 1458
  time: '24:18'
  who: Alexey
- line: It really depends on what you are working on. You want it to be representative
    of what user interactions will be like. About the cost, I totally agree, but you
    do not need to use an LLM judge for everything. An LLM judge is just another prompt
    you use to judge one.
  sec: 1479
  time: '24:39'
  who: Hugo
- line: You can test whether it produces structured output or use regular expressions
    or string matching, depending on your use case. You can lower costs by using cheaper
    models or flash models instead of the most powerful ones. The key is that the
    test set should be representative.
  sec: 1499
  time: '24:59'
  who: Hugo
- line: When you start looking at your data in spreadsheets, you start to see patterns
    emerge. You can see failure modes and get a sense of how much you need to collect
    and how big the test set should be.
  sec: 1525
  time: '25:25'
  who: Hugo
- line: The reason I am trying to pull as much information from you as possible is
    because for my course that I am doing now, it is the evaluations week. I am thinking
    about what else I should include there. I already included the usual testing like
    format adherence and whether references are included.
  sec: 1557
  time: '25:57'
  who: Alexey
- line: There are also integration tests where we run a set of data and see the output.
    Then there is the performance test, like out of 100 questions, 90 percent got
    relevant responses.
  sec: 1585
  time: '26:25'
  who: Alexey
- header: 'Failure Analysis: Categorizing Errors and Prioritizing Retrieval Fixes'
- line: You use this process to guide your development as well. This is something
    I teach a lot in my work and courses. You should do failure analysis and rank
    order your failures. Formatting issues might be more obvious but if they are only
    10 percent of the issues, and most are retrieval errors, focus on retrieval.
  sec: 1603
  time: '26:43'
  who: Hugo
- line: Doing some failure analysis, categorizing errors in a spreadsheet, then doing
    a pivot table to rank order them will help. You will see that most errors come
    from retrieval, and that is where you should focus, not on the generative part.
  sec: 1640
  time: '27:20'
  who: Hugo
- line: Makes sense. Do you use any software tools for evaluation and monitoring?
  sec: 1650
  time: '27:30'
  who: Alexey
- header: 'Monitoring & Vibe Coding: Logging, Traces, and Debuggable MVPs'
- line: We have many monitoring and evaluation tools to help with this process. I
    output things to pandas, copy them to Google Sheets, and analyze there. But there
    are special tools. Have you tried any of them? Do you like any?
  sec: 1658
  time: '27:38'
  who: Alexey
- line: I like most of them, but my favorite tool besides spreadsheets is vibe coding.
    Let’s say I have an email assistant I am building. Then I can vibe code what it
    looks like to interact with the email assistant and look at all the traces and
    function calls there.
  sec: 1682
  time: '28:02'
  who: Hugo
- line: That can be incredibly useful. Of course, use tools that make your job easier,
    whether it be Logfire, Braintrust, or Phoenix Arise. These are all wonderful tools.
    Generative AI is one of the most civilization changing technologies, bigger than
    the internet in many ways.
  sec: 1719
  time: '28:39'
  who: Hugo
- line: It will take years for us to see the full effect. It is a horizontal technology
    with people building application layers on top of it in healthcare, finance, and
    education. People are also building tools to help others use it, but they cannot
    satisfy everyone.
  sec: 1743
  time: '29:03'
  who: Hugo
- line: Think about it. React came out more than ten years after the internet. The
    tools that will really help builders in the future may not even exist yet. The
    current tools are fantastic, but for the entire application layer we still need
    more.
  sec: 1762
  time: '29:22'
  who: Hugo
- line: When you vibe code these things, you said you include traces and function
    calls. So basically you create a React app or Streamlit app that looks like the
    end product but add debugging tools to see what the function calls are, right?
  sec: 1795
  time: '29:55'
  who: Alexey
- line: That is exactly it. Whenever you build an MVP, build logging into it immediately.
    Log everything and then you can vibe code.
  sec: 1812
  time: '30:12'
  who: Hugo
- line: When vibe coding, chat with it first before building. Give it your database
    schema and as much information as possible. AI assistants are like very bright
    interns who sometimes forget things you want them to do.
  sec: 1824
  time: '30:24'
  who: Hugo
- line: My friend John Barryman, who worked on Copilot at GitHub, always says to have
    empathy for your AI assistant. Understand its strengths and weaknesses. Have a
    conversation with it first, develop a short requirement document, and remind it
    of the database schema.
  sec: 1850
  time: '30:50'
  who: Hugo
- line: Yeah. Sometimes it is stubborn or refuses to do things. I ask it to edit a
    file and it refuses, so I do it myself, and then it works. Sometimes it is amazing.
    I ask it to edit a file and it turns a Jupyter notebook into a clean markdown
    file.
  sec: 1882
  time: '31:22'
  who: Alexey
- line: Totally. We talk about hallucinations a lot, but not enough about forgetting.
    State of the art tool calling by an LLM as an agent is about 90 percent accurate.
    If you have six or seven tool calls in a row, it will only work about half of
    the time. You just need to understand what you are working with.
  sec: 1916
  time: '31:56'
  who: Hugo
- line: What kind of assistants do you use? My current favorite is GitHub Copilot.
    I have tried many tools. I use it because I have an open source license, so it
    is free for me.
  sec: 1933
  time: '32:13'
  who: Alexey
- line: I do not need to pay twenty dollars for Cursor. But I am curious what your
    favorite one is right now. I know it might change in a week.
  sec: 1952
  time: '32:32'
  who: Alexey
- line: I use Cursor and have for some time. I have used Claude Code, Copilot, Windsurf,
    and played with AMP. Cursor does everything I need and does it well.
  sec: 1958
  time: '32:38'
  who: Hugo
- line: It is mostly inertia that keeps me from switching. I am doing so many things
    that I have no strong reason to change now. But I should make time to experiment
    with new tools.
  sec: 1983
  time: '33:03'
  who: Hugo
- header: 'Embedded Agents and IDE Integrations: Cursor, Copilot, and Slack Workflows'
- line: I am also excited about having these tools in normal interfaces. Some people
    use Cursor and Devon in Slack. You can be in Slack and say, “This documentation
    is wrong, update it.”
  sec: 1994
  time: '33:14'
  who: Hugo
- line: Bringing agentic systems into our normal environments will become common.
    Manis has an email assistant where you can tag it in an email to update documentation
    or perform tasks. Having these assistants around more often will become normal.
  sec: 2015
  time: '33:35'
  who: Hugo
- line: Slack.
  sec: 2039
  time: '33:59'
  who: Alexey
- line: What is that?
  sec: 2040
  time: '34:00'
  who: Hugo
- line: How can you use Cursor from Slack?
  sec: 2041
  time: '34:01'
  who: Alexey
- line: I think there is a Slack integration. I would need to check, but I am pretty
    sure.
  sec: 2042
  time: '34:02'
  who: Hugo
- line: It is like a Visual Studio clone, right? They have a CLI application. That
    is what I like about GitHub Copilot.
  sec: 2046
  time: '34:06'
  who: Alexey
- line: They have strong GitHub integration. I can create an issue, assign it to GitHub
    Copilot, and in half an hour have a working result. With Cursor, I cannot do that
    or do not know how.
  sec: 2058
  time: '34:18'
  who: Alexey
- line: But now you say there is Slack integration, which means I can write, “Hey
    Cursor, can you fix issue number 124?” and it will pull the issue and solve it,
    right?
  sec: 2076
  time: '34:36'
  who: Alexey
- line: Exactly. That is cool. I think they do have it. I have not used it much. It
    might not be as advanced as Claude Code yet.
  sec: 2093
  time: '34:53'
  who: Hugo
- line: A year or two ago, we were copying and pasting between ChatGPT and our IDE.
    Then we got code completion. Now we have agents in IDEs and terminals.
  sec: 2113
  time: '35:13'
  who: Hugo
- line: Coding was also not very good then. GPT 3.5 was not great at coding.
  sec: 2119
  time: '35:19'
  who: Alexey
- line: Yeah. And it did not even know its own API. Then we got code completion. Now
    we have agents in IDEs and proactive AI doing code reviews and continuous integration.
  sec: 2127
  time: '35:27'
  who: Hugo
- line: We are seeing more background agents working quietly. I am excited about proactive
    AI that tells you when something happens in production or organizes your work
    schedule.
  sec: 2145
  time: '35:45'
  who: Hugo
- line: So we are at the background agents level now, right? I can create an issue
    in GitHub, assign it to Copilot, and half an hour later there is a pull request
    ready. But what if Copilot emailed me saying, “Hey, you could add this feature.
    Do you want me to work on that?” That would be amazing.
  sec: 2184
  time: '36:24'
  who: Alexey
- line: Proactive agents and multiplayer agents are the next step. When multiple people
    ping the same one, it gets confused. We might need to fine tune models for multiplayer
    conversations.
  sec: 2233
  time: '37:13'
  who: Hugo
- line: You could imagine several people talking to an agent in Slack, and it acting
    as a team member. Once we solve that, having agents as embedded team members will
    be normal. Proactive and multiplayer agents will be a big part of the future.
  sec: 2263
  time: '37:43'
  who: Hugo
- line: If things changed this much in three years, I am curious to see what will
    happen in the next three. It might slow down over time, but still be exciting.
  sec: 2289
  time: '38:09'
  who: Hugo
- line: Look at the evolution of the internet. It grew fast, then slowed down. Then
    companies like Google and YouTube emerged, connecting and indexing the internet.
    Similar products will emerge for AI.
  sec: 2308
  time: '38:28'
  who: Hugo
- line: There is this browser from Perplexity. You have heard of it, right?
  sec: 2343
  time: '39:03'
  who: Alexey
- line: Yeah. Comet.
  sec: 2350
  time: '39:10'
  who: Hugo
- line: Sometimes I get an email from my tax advisor saying I need to prepare some
    documents. When it comes to taxes, I am such a procrastinator. You can probably
    relate.
  sec: 2356
  time: '39:16'
  who: Alexey
- line: I cannot even talk about it right now.
  sec: 2372
  time: '39:32'
  who: Hugo
- line: 'Exactly. She sent the email a month ago and I know I need to do it, but it
    takes time. It is manual work: downloading documents, saving them in folders,
    and sending them back. I would love to wake up one day and have an agent do that
    for me.'
  sec: 2372
  time: '39:32'
  who: Alexey
- line: Absolutely.
  sec: 2406
  time: '40:06'
  who: Hugo
- line: That would be amazing because I think Comet is one step toward that.
  sec: 2407
  time: '40:07'
  who: Alexey
- header: 'Agentic Value Beyond Chat: Actions, Documents, and Automation'
- line: Definitely a provocative statement, but I do not think the future of AI happens
    in chat. We will still chat and do that kind of stuff, but the amount of value
    a conversation can generate is limited by human time, and human time is scarce.
    The real value comes from generating documents, taking actions, sending emails,
    and other agentic capabilities. That is where over ninety-nine percent of the
    economic value will be delivered.
  sec: 2412
  time: '40:12'
  who: Hugo
- line: Let’s see. So what else do you consult about? What kind of applications do
    you build or help your customers build?
  sec: 2447
  time: '40:47'
  who: Alexey
- line: The main focus is retrieval, though some agentic work as well. It often comes
    down to setting expectations. Let me share an example that combines several clients.
    Many teams get stuck in what I call “proof of concept purgatory.” That is where
    great ideas exist but they do not solve any real problems.
  sec: 2458
  time: '40:58'
  who: Hugo
- line: For example, an edtech company wanted to build an all-purpose AI tutor that
    could teach anyone anything. It sounded great, but we realized that while models
    can appear to do that, they cannot do it consistently or reliably.
  sec: 2489
  time: '41:29'
  who: Hugo
- line: I have used it to learn many things.
  sec: 2522
  time: '42:02'
  who: Alexey
- line: Yes, and you are right. For topics it has been trained on, it usually performs
    well.
  sec: 2530
  time: '42:10'
  who: Hugo
- line: Right. But of course if I go beyond common human knowledge or into research-level
    topics, it struggles. I learned basics of chemistry, electronics, and even German
    using ChatGPT. But at a PhD or advanced research level, it cannot yet do original
    work or independent research.
  sec: 2535
  time: '42:15'
  who: Alexey
- line: They can search the internet using tools, but not always reliably. Sometimes
    they say they searched when they actually did not. Even at a college level, for
    subjects like algebraic representation theory, they can hallucinate. They also
    make mistakes with basic geometry like Platonic solids, sometimes inventing new
    shapes that do not exist. So I do not think ChatGPT is ready to be an all-purpose
    tutor yet.
  sec: 2561
  time: '42:41'
  who: Hugo
- line: So you mean it struggles with visual or structured reasoning tasks, right?
  sec: 2619
  time: '43:39'
  who: Alexey
- line: Yes, and even arithmetic. There are many failure modes. That is why I would
    not trust it as a general tutor.
  sec: 2626
  time: '43:46'
  who: Hugo
- line: Anyway, that edtech company wanted a flashy AI tutor, but when we looked into
    their customer support tickets, we found that twenty percent were simply questions
    like “Which class is this lesson in?” or “Where can I learn about this?”
  sec: 2637
  time: '43:57'
  who: Hugo
- header: 'Prioritizing RAG for Business Impact: Quick Wins over Moonshots'
- line: So instead of building a moonshot tutor, if they just built a simple RAG bot
    with good chunking, embeddings, and a nice interface, they could solve one in
    five support tickets immediately. It is less flashy, but delivers real business
    value fast. Helping people see that is important.
  sec: 2666
  time: '44:26'
  who: Hugo
- line: Is chunking a solved problem, or do we still not know how to do it properly?
  sec: 2696
  time: '44:56'
  who: Alexey
- line: Generally, you can do it relatively well, but it depends on the data. For
    example, with a transcript like this one, you could chunk by question and answer
    pairs or by speaker turns. If there were five people talking, you might chunk
    by topic instead. It depends entirely on the structure of the content.
  sec: 2701
  time: '45:01'
  who: Hugo
- line: So there is no one-size-fits-all. For a podcast, it makes sense to chunk by
    Q&A pairs, but for a book like Game of Thrones you would use a different approach.
  sec: 2749
  time: '45:49'
  who: Alexey
- line: Exactly. Also look at the data you get. Zoom, for example, gives you two transcripts
    closed captions without names, and a full transcript with speaker names. The second
    one is much richer and more useful for chunking.
  sec: 2768
  time: '46:08'
  who: Hugo
- line: Funny enough, ChatGPT can often infer who is speaking even without names.
  sec: 2792
  time: '46:32'
  who: Alexey
- line: True. But sometimes you do not even need to chunk. Context windows are getting
    large, though that comes with context rot. Jeff Huber and his team at Chroma wrote
    a great essay about context rot how giving too much context can reduce precision
    and relevance.
  sec: 2799
  time: '46:39'
  who: Hugo
- line: Yes, I notice that with long transcripts. At the start it reformats things
    nicely, but by the end it gets sloppy.
  sec: 2830
  time: '47:10'
  who: Alexey
- line: Exactly. In prompt engineering, if something is really important, say it at
    the start of your prompt and repeat it at the end. You will often get better results.
  sec: 2846
  time: '47:26'
  who: Hugo
- line: Yes, when I ask it to improve my prompt, it often repeats my intent at the
    end. That seems to help it follow instructions better.
  sec: 2860
  time: '47:40'
  who: Alexey
- line: So when it comes to chunking, which approach did you use for that tutor?
  sec: 2887
  time: '48:07'
  who: Alexey
- line: 'That project was a mix of several experiences. But the main rule is: study
    your data. If you have 30-minute instructional videos, maybe chunk every five
    minutes or wherever topics shift.'
  sec: 2900
  time: '48:20'
  who: Hugo
- line: Would you still use character-based chunking or rely on section splits?
  sec: 2930
  time: '48:50'
  who: Alexey
- line: I would start with fixed character-length chunks and refine from there.
  sec: 2937
  time: '48:57'
  who: Hugo
- line: It seems to work well with a sliding window approach. More complex methods
    often overcomplicate things. I wonder what the industry consensus is.
  sec: 2942
  time: '49:02'
  who: Alexey
- header: 'Chunking Strategies and Context Rot: Sliding Windows and Summarizers'
- line: You are right. Also, RAG struggles with certain questions like “What is this
    whole video about?” because it looks for individual chunks. That is where agents
    and tool calls can help. For example, a summarization tool can answer broad questions
    that a RAG system cannot.
  sec: 2961
  time: '49:21'
  who: Hugo
- line: Even a few simple sub-agents can make it much more powerful and natural for
    the kinds of questions humans ask.
  sec: 2995
  time: '49:55'
  who: Hugo
- header: 'Adding Tooling vs. Simplicity: When to Move from RAG to Agents'
- line: But the moment we go from RAG to agents, system complexity increases a lot.
    We must define tool calls carefully, repeat instructions to ensure correct use,
    and handle more errors. While RAG follows a fixed path and is predictable. So
    when should someone actually consider using agents?
  sec: 3019
  time: '50:19'
  who: Alexey
- line: If your system works well, there is no need to add complexity. But if users
    start asking questions like “Tell me about the entire corpus,” then you might
    add a summarization tool. Tool calls increase complexity but also power and scope.
    Introduce them mindfully and always evaluate them using tools like Braintrust,
    Arise, or Logfire.
  sec: 3070
  time: '51:10'
  who: Hugo
- line: You can also vibe code some things to see what is really happening before
    making things too complex.
  sec: 3126
  time: '52:06'
  who: Hugo
- line: Braintrust? I have not heard about that one.
  sec: 3137
  time: '52:17'
  who: Alexey
- line: Yes, it is braintrust.dev. There are two with similar names, so look for “Braintrust
    LLM.”
  sec: 3143
  time: '52:23'
  who: Hugo
- line: Got it. I am checking now. It is not open source, right?
  sec: 3150
  time: '52:30'
  who: Alexey
- line: They do have a GitHub, actually.
  sec: 3158
  time: '52:38'
  who: Hugo
- line: Okay, I will check it out. These tools appear faster than mushrooms in Germany
    in October—it is hard to keep track.
  sec: 3164
  time: '52:44'
  who: Alexey
- line: Yes, and many of them combine open source and commercial parts.
  sec: 3181
  time: '53:01'
  who: Hugo
- header: 'Practical Project Example: Building an Email Assistant'
- line: Like Arise with Phoenix, right? Okay, we should wrap up. Maybe share some
    advice for people starting with agents. What should they focus on first?
  sec: 3189
  time: '53:09'
  who: Alexey
- line: A few things. First, build something meaningful to you. For example, if you
    are overwhelmed by emails, connect to the Gmail API and start clustering or classifying
    emails by priority. Use some basic machine learning and iterate.
  sec: 3214
  time: '53:34'
  who: Hugo
- line: You connected it to Gmail through the API?
  sec: 3243
  time: '54:03'
  who: Alexey
- line: Yes, absolutely. Cluster and classify your emails, then maybe build a model
    that prioritizes them. You could even connect another LLM to draft suggested responses
    for you to review and send.
  sec: 3243
  time: '54:03'
  who: Hugo
- line: That is exactly what I want. A system that looks at unread emails and suggests
    two or three replies.
  sec: 3271
  time: '54:31'
  who: Alexey
- line: Fantastic. You should build that.
  sec: 3277
  time: '54:37'
  who: Hugo
- line: Yes, because I procrastinate on so many emails especially when I read them
    on my phone. If a system generated responses I could just approve, I would probably
    reply to half of them immediately.
  sec: 3284
  time: '54:44'
  who: Alexey
- line: Exactly.
  sec: 3308
  time: '55:08'
  who: Hugo
- line: If anyone is building this, please reach out to me.
  sec: 3309
  time: '55:09'
  who: Alexey
- line: Totally. And to your point, start building things that solve your own problems
    or your company’s problems. That is the best way to learn.
  sec: 3314
  time: '55:14'
  who: Hugo
- header: Four-Step Framework for Building Agents (Problem, Start Small, Data, Evaluation)
- line: 'In short, four steps:'
  sec: 3381
  time: '56:21'
  who: Hugo
- line: First, find a meaningful problem, like your email example.
  sec: 3381
  time: '56:21'
  who: Hugo
- line: Second, start small use an LLM and add tools or memory only as needed.
  sec: 3381
  time: '56:21'
  who: Hugo
- line: Third, look at your data carefully.
  sec: 3381
  time: '56:21'
  who: Hugo
- line: Fourth, build a basic evaluation set to guide iteration.
  sec: 3381
  time: '56:21'
  who: Hugo
- line: Often the issues are not embeddings or chunking but OCR or data ingestion.
    Also, if you want to go deeper, I teach a course on building AI applications for
    data scientists and engineers. I can offer your community a 20% discount.
  sec: 3413
  time: '56:53'
  who: Hugo
- line: Great. One quick last question when you mentioned adding memory, how do people
    usually do that? I have only used retrieval-based approaches so far.
  sec: 3438
  time: '57:18'
  who: Alexey
- header: 'Memory Design: Multi-Turn Conversation Memory vs. Retrieval-Based Memory'
- line: Good question. Many people handle memory poorly. GPT-5 itself has changed
    how it handles memory; long conversations now work differently. You should first
    ask if you even need memory. Many systems are single-turn and do not require it
    at all.
  sec: 3461
  time: '57:41'
  who: Hugo
- line: Memory becomes important once you need multi-turn conversations.
  sec: 3539
  time: '58:59'
  who: Hugo
- line: Right, like in the email assistant idea it would need to remember how I responded
    before. That could be retrieval-based, though.
  sec: 3545
  time: '59:05'
  who: Alexey
- line: Exactly. In that case, retrieval is your memory. But when I say memory, I
    mean within an active conversation like when you tell a travel assistant “Find
    me a hotel,” and later ask, “Which is the cheapest?” It should remember that context.
  sec: 3568
  time: '59:28'
  who: Hugo
- line: I see. I was thinking of memories across conversations.
  sec: 3597
  time: '59:57'
  who: Alexey
- line: That is another challenge entirely. For short conversations, you can just
    include the entire chat history as input. For longer ones, you might use a sliding
    window or a separate agent to manage memory. It decides what information is relevant
    to keep. Evaluating multi-turn conversations is also tricky, so define the desired
    conversation length early on.
  sec: 3599
  time: '59:59'
  who: Hugo
- header: Episode Wrap-Up and Next Steps
- line: Yes, it makes sense. I still have many questions, but we should wrap up.
  sec: 3655
  time: '1:00:55'
  who: Alexey
- line: We should chat again soon. Maybe we can run a workshop or teach something
    together. That would be fun.
  sec: 3661
  time: '1:01:01'
  who: Hugo
- line: That could be. My son wants attention now.
  sec: 3673
  time: '1:01:13'
  who: Alexey
- line: Then you should definitely go.
  sec: 3676
  time: '1:01:16'
  who: Hugo
- line: Thanks a lot, Hugo. Let’s catch up again soon, no need to wait another three
    years.
  sec: 3679
  time: '1:01:19'
  who: Alexey
- line: Exactly. Thanks everyone for watching and listening, and thanks Alexey and
    everyone at DataTalks as well.
  sec: 3685
  time: '1:01:25'
  who: Hugo
- line: All right. Ciao.
  sec: 3690
  time: '1:01:30'
  who: Alexey
---
Links:

* [Twitter](https://x.com/hugobowne){:target="_blank"}
* [Linkedin](https://www.linkedin.com/in/hugo-bowne-anderson-045939a5/){:target="_blank"}
* [Github](https://github.com/hugobowne){:target="_blank"}
* [Website](https://hugobowne.github.io/){:target="_blank"}