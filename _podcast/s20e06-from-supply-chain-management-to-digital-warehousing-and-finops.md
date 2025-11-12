---
episode: 6
guests:
- eddyzulkifly
ids:
  anchor: datatalksclub/episodes/From-Supply-Chain-Management-to-Digital-Warehousing-and-FinOps---Eddy-Zulkifly-e313t7b
  youtube: 7ePp6wuxM5s
image: images/podcast/s20e06-from-supply-chain-management-to-digital-warehousing-and-finops.jpg
links:
  anchor: https://creators.spotify.com/pod/profile/datatalksclub/episodes/From-Supply-Chain-Management-to-Digital-Warehousing-and-FinOps---Eddy-Zulkifly-e313t7b
  apple: https://podcasts.apple.com/us/podcast/from-supply-chain-management-to-digital-warehousing/id1541710331?i=1000702233986
  spotify: https://open.spotify.com/episode/33YZpX7zE6YcBGbQK9Iclp
  youtube: https://www.youtube.com/watch?v=7ePp6wuxM5s
season: 20
short: From Supply Chain Management to Digital Warehousing and FinOps
title: 'FinOps for Data Engineers: Optimize Cloud Costs with dbt, BigQuery & Modern
  Data Stack'
transcript:
- header: Podcast Introduction
- line: Let’s get started. This week, we’ll discuss Digital Data Warehousing and FinOps.
    We have a special guest today, Eddy Zulkifly, a staff data engineer at Kinaxis.
    Eddy, did I pronounce it correctly?
  sec: 0
  time: 0:00
  who: Alexey
- header: 'Guest Introduction: Eddy Zulkifly, Staff Data Engineer at Kinaxis'
- line: Yes, it’s Eddy Zulkifly and Kinaxis.
  sec: 95
  time: '1:35'
  who: Eddy
- line: Okay, great. Eddy is building a robust data platform at Kinaxis and has over
    10 years of experience in the data field. He’s also a mentor and teaching assistant.
    Previously, he worked as a senior data scientist at Home Depot, specializing in
    e-commerce and supply chain analytics. Welcome to the show, Eddy!
  sec: 100
  time: '1:40'
  who: Alexey
- line: Thank you, Alexey. It’s a pleasure to be here. I’ll briefly introduce myself.
    Alexey covered a bit about my experience, but I’ll dive in further.
  sec: 117
  time: '1:57'
  who: Eddy
- line: Before we go into the main topic of Digital Data Warehousing and FinOps, let’s
    start with your background. Can you tell us about your career journey so far?
  sec: 123
  time: '2:03'
  who: Alexey
- header: 'Career Origins: Industrial Engineering, Supply Chain & Excel Macros'
- line: For sure. My journey into data wasn’t exactly linear. Initially, I was supposed
    to pursue chemical engineering, but midway through considering my options, I was
    drawn to industrial engineering, particularly the psychology side—designing systems
    for people, which is essentially user experience. Although I didn’t know it at
    the time, that focus on building systems for people shaped how I approach data
    today.
  sec: 134
  time: '2:14'
  who: Eddy
- line: My first job was in technology, deep inside supply chains, working in distribution
    centers. I focused on optimizing space in warehouses, using Excel macros to figure
    out how many containers would arrive next week or next month. This was tied to
    staffing demands.
  sec: 134
  time: '2:14'
  who: Eddy
- line: I moved through several roles—supply chain, e-commerce merchandising, and
    business intelligence. However, it wasn’t always about Python or SQL. My first
    role was in a distribution center, where I had to move out of the city and come
    into the office. While it wasn’t the typical data analyst role, it was a great
    learning experience. Looking back, it provided a solid foundation for analytics.
    Excel remains the universal language for business. No matter how nice your dashboard
    is, the main question from stakeholders will always be, “Can I have this in an
    Excel file?”
  sec: 134
  time: '2:14'
  who: Eddy
- line: My journey into data was driven by curiosity. I didn’t have access to Tableau
    at first, so I used Tableau Public, learning from YouTube and different creators.
    Eventually, my organization gained access to Alteryx, which I loved because it
    allowed quick analysis with a low-code approach. I got certified in Alteryx.
  sec: 134
  time: '2:14'
  who: Eddy
- line: At the same time, I was pursuing a master’s in analytics, which led me to
    discover Python and build modern data stacks with an ELT approach. Now, I work
    as a staff data engineer at Kinaxis, focusing on building data sets and dashboards
    for our FinOps team to optimize cloud spend and ensure the platform runs efficiently.
  sec: 134
  time: '2:14'
  who: Eddy
- line: I think of FinOps as process optimization, similar to my early work in a physical
    warehouse but now applied in a digital warehousing context. A lot of the skills
    I learned early on still apply today, from Excel all the way to Python, Git, and
    the command line.
  sec: 134
  time: '2:14'
  who: Eddy
- header: 'Career Pivot: From Business Analyst to Data Engineering'
- line: What I also noticed is that you’re currently a data engineer, but you were
    previously working in data science. How did the switch happen?
  sec: 380
  time: '6:20'
  who: Alexey
- line: I’d like to clarify that my title is senior data engineer, but I moved from
    a business analyst role to more of a data engineering role. Working as a business
    analyst, my focus was on building dashboards. That’s where I first learned Tableau
    Public and attended events like Makeover Monday, where you were given a dataset
    and had to create narratives and charts.
  sec: 393
  time: '6:33'
  who: Eddy
- line: Moving into data engineering, I realized my true passion lay in the technical
    side. I had a great manager who told me that whenever I discussed Tableau or dashboards,
    my eyes would light up. That’s when I realized I enjoyed working on the backend
    side of things. That’s why I decided to pivot my career to data engineering.
  sec: 393
  time: '6:33'
  who: Eddy
- header: Analyst Skills as a Foundation for Data Engineering
- line: This is a common question in our data engineering course. Our course is designed
    for people coming from a software engineering background, but we often get asked,
    “I’m a data analyst—can I transition to data engineering?” Does the background
    of an analyst make this transition easier?
  sec: 468
  time: '7:48'
  who: Alexey
- line: Absolutely, I think a data analyst background makes the transition to data
    engineering easier. The foundational knowledge is already there, especially in
    understanding how data flows and what the needs of the business are. The skills
    in analysis and creating reports, dashboards, and interpreting data directly translate.
    The main difference will be shifting from more front-end roles, like working with
    Tableau or Power BI, to focusing on back-end processes, such as data pipelines,
    databases, and automating workflows.
  sec: 480
  time: '8:00'
  who: Eddy
- header: 'Docker & Terraform: Learning Curve for Data Practitioners'
- line: It’s great to hear that. A lot of people are curious about this shift. One
    challenge often mentioned in data engineering is working with the command line,
    Docker, and Terraform. How was your experience transitioning to these tools?
  sec: 486
  time: '8:06'
  who: Alexey
- line: Yes, I agree. When I started learning Docker and Terraform, it felt overwhelming
    because as a data person, we’re often used to working with UI tools. I came from
    an Alteryx background, which has a low-code approach. Moving to the command line
    was a big change. But once I started getting used to it, it all clicked.
  sec: 497
  time: '8:17'
  who: Eddy
- line: Now, working in data engineering, Docker and Terraform are critical tools
    for building infrastructure and managing environments. I realized that once you
    get comfortable with one language or tool, it’s easier to pick up others. It’s
    about building a mindset where you can apply the concepts across different technologies.
    It’s not as daunting as it seems at first.
  sec: 497
  time: '8:17'
  who: Eddy
- header: 'Tools & Low-Code Beginnings: Excel, Alteryx, Tableau'
- line: That’s interesting. Funny enough, when we were building the course for Data
    Engineering, we assumed that everyone would already be familiar with Docker. We
    thought it would just be a brief warm-up session for those who were unfamiliar.
    However, it turned out to be one of the most challenging weeks for participants.
  sec: 522
  time: '8:42'
  who: Alexey
- line: I have a similar experience. When I first encountered Docker, I was introduced
    to development containers. I had some colleagues in Toronto who were explaining
    development containers using a JSON file. When I tried explaining it to data folks,
    they found it difficult to grasp because it wasn’t a standard approach like other
    tools we use. It’s not really DevOps; it’s more about configuring a file, but
    it’s a whole different way of working. It takes time to get used to, especially
    for those who are more familiar with GUI-based tools.
  sec: 543
  time: '9:03'
  who: Eddy
- line: It’s great that you brought that up. I can see how that shift would be a challenge.
    But now that you’re more comfortable with Docker and Terraform, do you think it’s
    easier to learn new tools?
  sec: 568
  time: '9:28'
  who: Alexey
- line: Definitely. The key is the mindset of understanding the fundamentals and getting
    comfortable with one tool first. From there, it’s much easier to pick up new tools
    because the concepts tend to overlap. Whether you’re working with Python, Terraform,
    or any other tool, they all serve a similar purpose—they help automate processes
    and manage infrastructure efficiently. The more you work with these tools, the
    more it feels natural.
  sec: 584
  time: '9:44'
  who: Eddy
- line: I will definitely shout out to you what you have done. Through my connections
    at Home Depot, some folks in the US told me about the Data Talks Club. That’s
    how I heard about the Data Engineering Zoom Camp. I remember it was interesting
    because the first thing you taught was Docker and Terraform. For most data folks,
    it was new and overwhelming. We’re used to working with a UI, but moving to a
    command-line interface felt strange.
  sec: 498
  time: '8:18'
  who: Eddy
- line: I came from an Alteryx background, where everything was low-code. But after
    getting used to it, I found that Docker and Terraform, as well as other languages,
    become easier to understand. Once you get comfortable with one language, many
    of the concepts carry over to the others.
  sec: 498
  time: '8:18'
  who: Eddy
- line: It’s funny with Docker because we expected that everyone signing up knew it.
    When we built the course, we assumed Docker was something everyone was familiar
    with, so we included a warm-up week for those who didn’t know it. The idea was
    that they would pick it up during that time and then the actual content would
    begin. But it turned out to be the most difficult week, and we definitely didn’t
    expect that.
  sec: 569
  time: '9:29'
  who: Alexey
- line: I have a similar story. In the Docker space, I had colleagues in Toronto talking
    about dev containers. I went to a couple of meetups where they would give you
    a dev container JSON file for tutorials. It’s an abstraction of Docker, but even
    then, when I tried explaining it to data folks, they felt confused because they
    had never worked with it before. They’d say, “I’m not in DevOps,” but it’s not
    exactly DevOps—it’s just configuring a file. Working with Docker and development
    containers requires some getting used to.
  sec: 600
  time: '10:00'
  who: Eddy
- line: If all you did before was business analytics, and now you suddenly need to
    work with Docker, everything related to this feels overwhelming. It might seem
    like devops, something complicated. But once you dive into it, you realize it's
    not devops; it's something different, something you can learn.
  sec: 649
  time: '10:49'
  who: Alexey
- header: 'Retail & Warehousing Experience: Forecasting, Preload Optimization'
- line: You worked at Home Depot, and for me, Home Depot was notable for hosting a
    Kaggle competition. I think it was one of the first Kaggle competitions I participated
    in. Was it about forecasting? I can’t quite recall, but I remember it being an
    awesome experience. Can you tell us more about your work there? Were you still
    focused on physical warehouses, or were you already transitioning to digital warehouses?
  sec: 673
  time: '11:13'
  who: Alexey
- line: My time at Home Depot was a discovery process where I explored different aspects
    of my degree. Part of my degree focused on logistics and optimization, so I had
    periods where I worked in the warehouse. To give context, think of the equivalent
    of Home Depot in Europe as something like an Obi or Bauhaus. In Southeast Asia,
    where I'm from, it could be something like Mr. DIY or Daiso. These are stores
    that sell products like screws, hammers, and outdoor furniture.
  sec: 714
  time: '11:54'
  who: Eddy
- line: The most interesting time for me was during the holiday seasons, particularly
    September and December. That’s when Home Depot sold a lot of Halloween products,
    like skeletons and dinosaurs. A typical workflow for me during that period involved
    forecasting based on orders. We had to figure out how many containers of goods
    were arriving, how they were packaged, and what products they contained.
  sec: 751
  time: '12:31'
  who: Eddy
- line: Once we figured out the size of the boxes, we had to estimate how much space
    they would occupy in the warehouse. After that, we calculated how much labor was
    required to store them. Later, when we needed to send the products to stores,
    we’d figure out how many people were needed to pick, package, and ship the items.
    There were many questions to consider, and we used various tools, like Excel macros,
    to determine the best configuration to store these products.
  sec: 776
  time: '12:56'
  who: Eddy
- line: At the time, we also did something called preload optimization, which involved
    engineers and warehouse staff figuring out how to maximize trailer space when
    shipping products to stores. We manually solved problems like the knapsack problem
    using Excel, which was quite manual. Looking back, I realize that today software
    from companies like Kanexis automates a lot of this work, making it much easier.
  sec: 818
  time: '13:38'
  who: Eddy
- line: Interesting! You must be an expert with Excel macros.
  sec: 879
  time: '14:39'
  who: Alexey
- line: I had to pick up a lot of skills. That was my introduction to programming.
    I remember using the "record" function in Excel to create macros by performing
    actions like selecting cells, then seeing the code. It was a great starting point.
    Over time, I learned how to define objects and refine the macros to make them
    more efficient.
  sec: 884
  time: '14:44'
  who: Eddy
- line: I even created a website once. I had a database of music bootlegs—concert
    videos that fans film themselves. I exchanged DVDs of these recordings with people
    from all over the world. Using Excel, I created a website. It had a macro that
    published an HTML page and then uploaded it via FTP. At the time, it was mind-blowing
    to me.
  sec: 910
  time: '15:10'
  who: Alexey
- line: That’s interesting! I have a similar story, but we can talk about that later.
  sec: 966
  time: '16:06'
  who: Eddy
- line: Excel is surprisingly powerful. There’s so much you can do with it. You could
    even play games like Space Invaders or Doom in Excel if you wanted.
  sec: 973
  time: '16:13'
  who: Alexey
- line: I’ve seen people create art in Excel, and there are even Excel competitions.
    In those competitions, participants have to create complex models to solve specific
    problems. If you can do it faster, there are people willing to pay for those skills.
  sec: 986
  time: '16:26'
  who: Eddy
- line: I just checked the competition, and it was Home Depot Product Search. It was
    about predicting the relevance of search results on Home Depot’s website. People
    would type a search, and the task was to predict the relevance of the products
    that came up. It was one of my first exposures to these kinds of problems.
  sec: 1003
  time: '16:43'
  who: Alexey
- line: That sounds like it was related to cosine similarity.
  sec: 1042
  time: '17:22'
  who: Eddy
- line: I didn’t realize that Home Depot had physical stores. I thought it was just
    an online store because I participated in that competition and knew the name.
    They have a big team, and I thought it was just an online store for screws. But
    it turns out they have a lot of physical stores too.
  sec: 1047
  time: '17:27'
  who: Alexey
- line: Yes, Home Depot has a lot of stores in Canada, the US, and Mexico. It’s a
    pretty big operation.
  sec: 1071
  time: '17:51'
  who: Eddy
- line: It’s a huge operation, and you need a huge warehouse to manage all that inventory.
    You were working on optimizing those warehouses, right?
  sec: 1079
  time: '17:59'
  who: Alexey
- line: Yes, I was involved in the backend processes. We had distribution centers
    for larger products, which were shipped to stores. On the merchandising side,
    we had planograms, which are configurations that show where products should be
    placed in the store. There’s a whole science behind this.
  sec: 1092
  time: '18:12'
  who: Eddy
- line: We had heat maps that showed where sales were coming from, and a dedicated
    team worked on optimizing store layouts to maximize revenue. Certain products
    were placed closer to the exits, while others were at the back to get customers
    to walk around more. It’s similar to how grocery stores place milk at the back
    to get people to walk through the aisles.
  sec: 1109
  time: '18:29'
  who: Eddy
- line: Did you use Excel for that as well?
  sec: 1127
  time: '18:47'
  who: Alexey
- line: For merchandising, the team used tools like Alteryx and Tableau. We also had
    in-house software that mapped sales data to store layouts and planograms.
  sec: 1157
  time: '19:17'
  who: Eddy
- line: Is this part of merchandising an art or a science?
  sec: 1180
  time: '19:40'
  who: Alexey
- line: It’s called assortment planning. Each store has a slightly different plan
    based on the region and customer preferences. We would tweak the planograms based
    on sales data to match local buying habits.
  sec: 1186
  time: '19:46'
  who: Eddy
- line: Did you ever work in a physical warehouse, like actually handling the products?
  sec: 1208
  time: '20:08'
  who: Alexey
- line: Yes, my first job at Home Depot was at a distribution center. I was involved
    in loading products onto racks. Later, I worked more on the corporate side, focusing
    on planograms and data analytics.
  sec: 1214
  time: '20:14'
  who: Eddy
- line: Did you use robots from Amazon Robotics?
  sec: 1240
  time: '20:40'
  who: Alexey
- line: I’m not sure. At the time, I don’t think we were using Amazon Robotics, but
    it’s possible we were testing some automation.
  sec: 1247
  time: '20:47'
  who: Eddy
- line: Amazon Robotics, previously Kiva Systems, uses robots to move products around
    in warehouses. I worked at Kiva as a Java developer. I think Home Depot was one
    of their customers, but maybe that didn’t go anywhere after Amazon acquired them.
  sec: 1264
  time: '21:04'
  who: Alexey
- line: That’s interesting. I worked with the Canadian branch of Home Depot, so the
    situation may have been a bit different here.
  sec: 1278
  time: '21:18'
  who: Eddy
- line: You worked later in your career to optimize distribution centers, which are
    essentially warehouses, right?
  sec: 1303
  time: '21:43'
  who: Alexey
- line: Yes, that’s correct. It’s very much like working in a warehouse.
  sec: 1309
  time: '21:49'
  who: Eddy
- header: 'Digital Data Warehousing: Data as Inventory and Pipelines'
- line: We also wanted to talk about digital warehousing. What exactly is that, and
    how does it work? Let's start with physical warehouses first. A warehouse is a
    space with tracks where products are stored. There are processes for people, robots,
    or machines to move the products and deliver them to the appropriate location.
    For example, getting products from racks and loading them into cars for distribution.
    That's a physical warehouse.
  sec: 1317
  time: '21:57'
  who: Alexey
- header: 'Modern Data Stack: ELT, dbt, BigQuery and Orchestration'
- line: In this case, I'd like to thank you for that context. I’ve worked at Home
    Depot for a long time, and I recall working in a physical warehouse. But when
    I became a senior data engineer, I realized I was still working in a warehouse—just
    a digital one. In this case, think of moving data like moving products. You're
    ingesting data, similar to trucks delivering goods into a warehouse. We use Google
    Cloud and BigQuery to store the data. Inside the warehouse, you have internal
    processes. We used orchestrators to run SQL queries, which helped transform and
    process the data. Once the data is ready, it is sent to a consumption layer, like
    a BI tool, such as Tableau or Looker.
  sec: 1356
  time: '22:36'
  who: Eddy
- line: Data engineers build pipelines or write Python scripts to move data from the
    source into the warehouse. Inside the warehouse, we use transformation tools like
    data build tools to clean and organize the data. The data is then put into tables
    or racks to be easily accessible. Once it’s organized, you have a service account
    or process to send the data to tools like Looker or PowerBI. Finally, dashboards
    are created for the end users to generate insights. The process of working in
    a digital warehouse is quite similar to a physical one.
  sec: 1418
  time: '23:38'
  who: Eddy
- header: 'Operational Differences: Change Velocity, Monitoring, and Tests'
- line: I just realized that the term "data warehouse" includes the word "warehouse,"
    which is really a distribution center. The goal of a physical warehouse is to
    receive products in large trucks and then store them in racks. The products are
    organized in a way that makes them easy to access. Once the products are organized,
    they can be moved to smaller trucks for delivery to stores. In the same way, data
    in a digital warehouse is organized to make it easy to access.
  sec: 1474
  time: '24:34'
  who: Alexey
- line: One major difference between digital and physical warehouses is the speed
    of changes. In my first role in process improvement, we focused on understanding
    processes and managing change. In a physical warehouse, changes often take a long
    time because you need approval from various teams. For example, if you need more
    space or racks, it can cost millions of dollars and require construction.
  sec: 1532
  time: '25:32'
  who: Eddy
- line: In a digital warehouse, changes are much quicker. If you need a new data requirement,
    you can create a new table and optimize it immediately. The feedback loop is much
    faster, too. You can create a model, send it out, receive feedback, and make adjustments
    quickly. Another difference is that, in a physical warehouse, you might rely on
    internal systems or human observation to track products. In a digital warehouse,
    since everything is in the cloud, you need monitoring systems and tests to ensure
    everything is working properly.
  sec: 1587
  time: '26:27'
  who: Eddy
- header: 'Metric Trees & Data Specs: Translating Business Requirements for FinOps'
- line: That's interesting. Can you tell us more about your role as a staff data engineer
    at Kanexis?
  sec: 1670
  time: '27:50'
  who: Alexey
- line: My day-to-day work involves both business and technical tasks. One key thing
    I've learned is the importance of understanding business requirements. In the
    analytics space, we focus on building metric trees to understand which metrics
    the business cares about and what factors affect them. We recently worked on a
    metric tree for the FinOps team to understand the cost factors inside the data
    warehouse and cloud platform.
  sec: 1677
  time: '27:57'
  who: Eddy
- line: Building a metric tree helps everyone gain a better understanding of data
    and how to build datasets that answer important business questions. Another important
    task is using a data spec, which I learned from Zack Wilson’s course. Business
    requirements can be vague, so it's important to translate them into clear technical
    data requirements. This way, you can ensure the data pipeline meets business needs,
    define metric definitions, set pipeline frequencies, and identify any assumptions
    or unknowns.
  sec: 1701
  time: '28:21'
  who: Eddy
- line: Once you have everything outlined, you can communicate with the business and
    get alignment. This alignment is crucial because it gives everyone a clear understanding
    of the direction. I believe this step is one of the most important tasks for data
    engineers. Once the requirements are clear, it's easier to move forward with building
    the necessary systems.
  sec: 1756
  time: '29:16'
  who: Eddy
- header: 'Building a Digital Warehouse: Stack Choices and Open-Source Tools'
- line: Another part of my role involves standing up a digital warehouse by setting
    up our stack. We use cloud platforms and a mix of open-source tools to maximize
    business value while ensuring the system is easy to maintain for engineers and
    analysts within the team
  sec: 1796
  time: '29:56'
  who: Eddy
- line: Kanexis offers a platform for supply chain management, covering all aspects
    of the supply chain, including transportation and orders. The platform handles
    a wide range of use cases, all aimed at optimizing supply chain operations.
  sec: 1895
  time: '31:35'
  who: Eddy
- header: 'FinOps Overview: Cloud Cost Optimization for SaaS Platforms'
- line: Can you tell us more about what exactly you mean by optimizing costs? Let's
    say I work at, I don't know, something similar to Home Depot—just as an example,
    a large chain that needs a solution for supply chain planning. We have warehouses,
    stores, and clients, and we need to optimize that. Now, if we wanted to use something
    like InkaNexis, how do we optimize costs? What does it mean in this particular
    case?
  sec: 1900
  time: '31:40'
  who: Alexey
- line: In this case, we enter the realm of Software as a Service (SaaS). Many solutions
    we build eventually run on servers or in data centers. Every component requires
    some kind of virtual machine with specific requirements for RAM and storage. Additionally,
    when storing data in different regions, especially with global clients, we must
    comply with local data regulations, so data has to be stored in certain places.
    There's also the issue of securing and backing up the data, which involves internal
    processes to ensure the customers' data is safe and protected. The goal is to
    figure out how to do all this in the most cost-efficient way possible.
  sec: 1926
  time: '32:06'
  who: Eddy
- line: So, the cost optimization is for you, not for the clients?
  sec: 2013
  time: '33:33'
  who: Alexey
- line: Yes, in this case, it's about optimizing costs on our side as well.
  sec: 2021
  time: '33:41'
  who: Eddy
- line: I see. My impression was that you offer a bunch of solutions, and then the
    customer comes and says, "I want your solution." Then you work with them to figure
    out the best setup for them.
  sec: 2031
  time: '33:51'
  who: Alexey
- line: We also do that. When a client signs on, there’s an engagement process where
    we work with the customer to integrate their systems into our platform. We have
    a team dedicated to maintaining that and ensuring it runs smoothly.
  sec: 2037
  time: '33:57'
  who: Eddy
- line: This is probably related to FinOps, right? Optimizing costs?
  sec: 2050
  time: '34:10'
  who: Alexey
- header: Vendor Negotiations & Reservation Instances for Cost Savings
- line: Yes, exactly. In a previous company I worked for, the procurement department
    was responsible for tools that cost money. For example, if I needed something
    like Klaviyo or Google Workspace, I would go through them to figure out how to
    purchase these tools. For AWS, we could negotiate special contracts based on how
    many instances we wanted in advance, which made them cheaper. This is a form of
    cost optimization. So, when you deal with AWS, you negotiate based on the amount
    of money you want to spend and the services you need. That’s part of what FinOps
    involves.
  sec: 2055
  time: '34:15'
  who: Eddy
- line: Yes, exactly. Our team uses the data we generate to understand the costs and
    usage of our systems. From there, we figure out how to negotiate with cloud vendors
    to optimize the costs. Typically, we have an idea of how long our servers will
    run, and we can negotiate discounts for longer-term commitments.
  sec: 2128
  time: '35:28'
  who: Eddy
- line: So, it’s pretty similar to what I just described?
  sec: 2157
  time: '35:57'
  who: Alexey
- line: Yes, exactly. Reservation instances are part of the FinOps process as well.
  sec: 2165
  time: '36:05'
  who: Eddy
- header: 'Cloud Cost Modeling: VM Sizing, Storage Tiers and Multi-Cloud Comparison'
- line: Can you tell us more about the problems you solve and what kind of solutions
    you use to address them?
  sec: 2171
  time: '36:11'
  who: Alexey
- line: When addressing cost and usage, it’s important to understand both the business
    requirements and what’s expected in the coming months. For example, forecasting
    usage helps in understanding costs. Virtual machines generate significant costs,
    so knowing when and how long to run them is crucial. Configuring virtual machines
    requires knowing the required RAM and storage, as these are cost factors. Additionally,
    depending on the operating system—whether Linux or Windows—there may be licensing
    considerations, and cloud platforms may offer discounts or bundle licenses.
  sec: 2178
  time: '36:18'
  who: Eddy
- line: The cloud pricing model is complex, with different factors like RAM, storage,
    and licensing that contribute to costs. To manage this, we run models across different
    cloud providers to compare which offers the best value.
  sec: 2273
  time: '37:53'
  who: Eddy
- line: So, you evaluate multiple clouds, right? You know the requirements for virtual
    machines, and then you compare the deals you can get from Google Cloud, AWS, Azure,
    and so on. Based on that, you can make a decision on which provider to go with?
  sec: 2312
  time: '38:32'
  who: Alexey
- line: That’s correct.
  sec: 2333
  time: '38:53'
  who: Eddy
- header: 'Demand Forecasting Analogy: Inventory Planning Applied to Cloud Capacity'
- line: Interesting. When it comes to tools or solutions to these problems, it sounds
    a lot like demand forecasting to me.
  sec: 2343
  time: '39:03'
  who: Alexey
- line: Right. There’s demand forecasting, inventory planning, and other features.
    We also do a form of what-if analysis, similar to Excel, where you input different
    variables to see the potential outcomes. We use a more advanced version internally
    that looks at parameters and adjusts them to optimize revenue or profits.
  sec: 2349
  time: '39:09'
  who: Eddy
- line: So, inventory planning and demand forecasting in the cloud is similar to physical
    operations, right? It sounds like we’re talking about distribution centers and
    similar physical optimizations.
  sec: 2387
  time: '39:47'
  who: Alexey
- line: Yes, absolutely. My experience from that part of my career has been very helpful
    here.
  sec: 2398
  time: '39:58'
  who: Eddy
- header: FinOps Foundation, Cost Tagging & Accountability Best Practices
- line: Where can we learn more about FinOps?
  sec: 2418
  time: '40:18'
  who: Alexey
- line: There's a FinOps foundation, and they are considered the de facto player in
    the FinOps space. They offer training courses online to help people upskill in
    FinOps. Right now, I’m also working towards certification as a FinOps practitioner
    to fully understand the various aspects of FinOps. The foundation provides a nice
    framework document that details what FinOps teams do, with shared principles.
  sec: 2422
  time: '40:22'
  who: Eddy
- line: For example, when dealing with cloud costs, you need to ensure that the teams
    using the cloud are accountable for their costs. This is where tagging systems
    come in, making sure that each virtual machine is tied to a specific department.
    There’s also a process of regularly reviewing costs. On the data side, you want
    to make sure access to data is timely. This means ensuring that your data is fresh
    daily and available for monthly or weekly reporting, depending on requirements.
  sec: 2422
  time: '40:22'
  who: Eddy
- line: Do I understand correctly that FinOps is... let me take a step back. Initially,
    when we started talking about FinOps, my impression was that it’s about general
    cost optimization. But the more we talk, the more I realize it specifically focuses
    on the cloud, right?
  sec: 2497
  time: '41:37'
  who: Alexey
- line: Yes, that's correct. FinOps is all about using the cloud in the most cost-effective
    way.
  sec: 2515
  time: '41:55'
  who: Eddy
- line: It opens up opportunities where, if you're working with physical infrastructure,
    you'd need experience to build a rack from raw materials. But in the cloud, you
    can focus on understanding cloud architecture and data to figure out how to make
    your processes more efficient. For instance, instead of relying on traditional
    servers, you could opt for a serverless architecture or deploy containers. This
    way, you only pay for what you use, rather than paying for fixed assets.
  sec: 2526
  time: '42:06'
  who: Eddy
- line: In cloud platforms, there are services like cloud functions or Lambda functions
    that run as needed. I find this really interesting, as with enough knowledge of
    the cloud, you can work with your team to figure out cost optimization strategies.
    A key area of focus is storage—how to minimize costs by switching between different
    types of storage. For example, Azure offers hot and cold storage, and GCP has
    similar definitions. Understanding these storage options and optimizing them can
    result in significant savings.
  sec: 2526
  time: '42:06'
  who: Eddy
- line: 43:32Alexey
  sec: 2526
  time: '42:06'
  who: Eddy
- line: Another thing I was thinking about is the evolution of DevOps. Later, we had
    MLOps and DataOps—MLOps is machine learning operations, which is essentially DevOps
    for ML, and DataOps is data engineering operations, essentially DevOps for data
    engineering.
  sec: 2526
  time: '42:06'
  who: Eddy
- line: My understanding is that FinOps is somewhat parallel to this, though it’s
    not directly related to DevOps. The name is just somewhat similar, right?
  sec: 2526
  time: '42:06'
  who: Eddy
- line: Yes, the name is similar, but the more specific term is Cloud Cost Management.
    It’s more of a business-type role, but you can definitely spin it into something
    technical if you want. The interesting part about FinOps is that it can be either
    business-focused or technical, depending on how you approach it.
  sec: 2645
  time: '44:05'
  who: Eddy
- line: When it comes to the technical focus, what tools and technologies does one
    need to know in order to say they are proficient in FinOps?
  sec: 2667
  time: '44:27'
  who: Alexey
- header: OUCS & Standardizing Cloud Cost Reporting Across AWS/GCP/Azure
- line: Knowing FinOps involves understanding various processes related to it. This
    includes using open-source tagging software to implement tags in cloud infrastructure.
    Once tagging is done, the focus shifts to data processing approaches such as data
    warehousing, setting up ingestion systems, performing transformations, and creating
    visualizations. The visualization aspect is often tied to FinOps use cases. A
    great initiative by the FinOps Foundation is the development of Open Usage Cost
    Specifications (OUCS), aimed at standardizing how major cloud platforms—AWS, Azure,
    and Google Cloud—report costs. This effort addresses inconsistencies in terminology
    and calculations across platforms, enabling organizations to merge data seamlessly
    for consistent reporting. At our organization, we’re exploring how to implement
    these standards to streamline cost reporting further.
  sec: 2681
  time: '44:41'
  who: Eddy
- header: 'FinOps Processes: Parallels with DevOps, DataOps and CI/CD'
- line: While you were explaining, I realized that even though FinOps isn’t directly
    related to DevOps, there are similarities. In DevOps, the focus is not just on
    tools but also on processes—ensuring software is reliable, testable, and delivered
    efficiently. FinOps appears to have a similar focus on processes, streamlining
    cost optimization efforts, and leveraging tools to achieve this. Would you say
    that’s accurate?
  sec: 2777
  time: '46:17'
  who: Alexey
- line: Yes, exactly. You hit the nail on the head. The processes in FinOps mirror
    some of the DataOps practices as well. For example, using CI/CD pipelines to validate
    datasets or check how new data impacts downstream dashboards employs similar methodologies.
  sec: 2829
  time: '47:09'
  who: Eddy
- line: When I previously asked about your role as a Staff Data Engineer, you mentioned
    business and technical aspects. Could we revisit that discussion now that we’ve
    talked about FinOps?
  sec: 2861
  time: '47:41'
  who: Alexey
- header: 'Staff Data Engineer Responsibilities: Technical & Strategic FinOps Work'
- line: Sure! As a Staff Data Engineer, my role is multifaceted. On the technical
    side, I work on deploying pipelines, fixing bugs, and maintaining data quality
    through DataOps processes. On the strategic side, I focus on defining business
    metrics like unit economics, which help optimize costs and performance. This dual
    focus allows us to build a robust data platform for FinOps.
  sec: 2881
  time: '48:01'
  who: Eddy
- line: So, if I understand correctly, you’re building a data platform specifically
    for FinOps, enabling cost optimization and better decision-making?
  sec: 2931
  time: '48:51'
  who: Alexey
- line: That’s right. We manage data from cloud platforms, apply business logic and
    metric definitions, and generate unit economics to evaluate cloud performance.
  sec: 2944
  time: '49:04'
  who: Eddy
- line: Does Kinaxis have a dedicated FinOps team? How do data engineers collaborate
    with them?
  sec: 2969
  time: '49:29'
  who: Alexey
- line: We work closely with various business users, including engineers, product
    owners, and infrastructure teams. These stakeholders play a role in managing and
    optimizing cloud spending, ensuring efficient collaboration across the board.
  sec: 2977
  time: '49:37'
  who: Eddy
- line: Alexey
  sec: 2977
  time: '49:37'
  who: Eddy
- header: 'Continuous Learning: Georgia Tech Master’s, dbt, Python and Applied Analytics'
- line: I'm almost done with my master's, hopefully by the end of this year. I'm doing
    a program called the Master’s in Analytics from Georgia Tech. So far, in terms
    of my learnings, it’s been pretty cool because it’s more of an applied analytics
    degree. Since I work in data quite a bit, you get exposed to different approaches
    in analytics.
  sec: 3025
  time: '50:25'
  who: Eddy
- line: We explore descriptive, prescriptive, and predictive analytics, figuring out
    how to implement data to solve business problems in this context.
  sec: 3025
  time: '50:25'
  who: Eddy
- line: Since you're based in Toronto and this is Georgia Tech, I assume it's...
  sec: 3032
  time: '50:32'
  who: Alexey
- line: '...in Atlanta, in the United States. It’s interesting because my organization,
    Home Depot, is also based in Atlanta. While taking the program, I met a lot of
    Home Depot colleagues from the U.S. who were also enrolled.'
  sec: 3071
  time: '51:11'
  who: Eddy
- line: That’s how I learned about cool open-source technologies like dbt (data build
    tool), picked up Python, explored the cloud, and a range of other tools. These
    experiences helped me transition from being more of a business user to a software
    and data engineer.
  sec: 3071
  time: '51:11'
  who: Eddy
- line: When I was doing my master’s in business intelligence, it was almost 10 years
    ago. This year marks the 10th anniversary since I graduated.
  sec: 3105
  time: '51:45'
  who: Alexey
- line: Back then, I was working as a freelancer. It was more of a part-time job.
    I’d take a contract, complete it, and then move on to the next one, spending around
    20 hours per week. You, however, work full-time as a staff data engineer. It must
    be challenging to manage both at the same time, right?
  sec: 3105
  time: '51:45'
  who: Alexey
- line: Yeah, exactly. One of the things that interested me about the Georgia Tech
    program was its analytical rigor. Based on reviews, they expect you to pick up
    on the math and learn Python as required.
  sec: 3145
  time: '52:25'
  who: Eddy
- line: In one of the courses, we had to learn D3, a JavaScript library, which was
    pretty intense. I don’t think many people use D3 now, but it was a great opportunity
    to learn something new and apply it.
  sec: 3145
  time: '52:25'
  who: Eddy
- line: Pursuing my master’s while working full-time has been about managing my time
    and responsibilities carefully. I try not to overwork myself, usually taking one
    course per semester. I also choose topics related to my job so I can apply what
    I’m learning directly at work.
  sec: 3145
  time: '52:25'
  who: Eddy
- line: This approach has added value because I can immediately apply my university
    learnings to my job in analytics. It helps reinforce my understanding and makes
    the knowledge more practical.
  sec: 3145
  time: '52:25'
  who: Eddy
- line: This is something we talked about. You also run—you’re into running and were
    running marathons. This year, you’re slowly returning to that. Preparing for a
    marathon takes a lot of time, and then you’re also doing a master’s, working,
    and probably want to do something else apart from these things, right?
  sec: 3235
  time: '53:55'
  who: Alexey
- line: Absolutely. The secret is to take one course per semester.
  sec: 3256
  time: '54:16'
  who: Eddy
- line: When I was preparing for a marathon, I think I took a lighter course. One
    thing I’ll say about the analytics community at Georgia Tech is that it’s a really
    great online community. They have a Google Sheet where they collect course reviews
    and calculate the estimated workload for each course.
  sec: 3262
  time: '54:22'
  who: Eddy
- line: My rule is to do the math—if I want to double up, my max is 20 hours. If a
    course is around 10, 8, or 12 hours, I’ll likely just take one at a time. It’s
    interesting that people in the community spend time building tools like this to
    help manage workloads. I found that really helpful as well.
  sec: 3262
  time: '54:22'
  who: Eddy
- line: That makes sense. The program is about analytics, so there should be analytical
    ways to support decision-making in this case, right?
  sec: 3314
  time: '55:14'
  who: Alexey
- line: Exactly!
  sec: 3323
  time: '55:23'
  who: Eddy
- line: I can see your cat.
  sec: 3331
  time: '55:31'
  who: Alexey
- line: Maybe one last question, and then we’ll call it a day. You mentioned you’re
    either recently preparing for or have already earned a certificate in some field.
    You seem to have quite a few certificates. Are you actively investing your time
    in extra learning, in addition to your master’s? How do you manage that, given
    we only have 24 hours in a day?
  sec: 3337
  time: '55:37'
  who: Alexey
- header: 'Career Advice: Certifications, Mentorship, Community and Time Management'
- line: Exactly, and I think this applies to everyone. Nowadays, when I talk to folks
    interested in breaking into data, I encourage them to focus on certifications
    that align with their interests and passions.
  sec: 3365
  time: '56:05'
  who: Eddy
- line: As a data engineer, you develop the skill of learning as you go. This has
    helped me become more efficient in learning and strategic in acquiring the knowledge
    I need to get the job done.
  sec: 3365
  time: '56:05'
  who: Eddy
- line: Pursuing my master’s and picking up certificates has taught me to build habits
    around learning. Finding your community is essential. Toronto, for example, is
    a big tech hub for data and analytics. Attending meetups and learning from others
    in the city has helped me build relationships and understand market trends.
  sec: 3365
  time: '56:05'
  who: Eddy
- line: Another thing I’ve found valuable is applying what I learn. At my organization,
    there’s openness to building and applying skills from school. Shoutout to my team
    at Home Depot for creating a great environment for learning and growth.
  sec: 3421
  time: '57:01'
  who: Eddy
- line: Lastly, having an accountability partner helps. I have monthly calls with
    a friend where we discuss our goals. They’re not even in data, but it helps to
    have someone to keep you on track.
  sec: 3421
  time: '57:01'
  who: Eddy
- line: Finally, I believe in giving back to the community. Platforms like Data Talks
    Club are great because they teach others for free. Last year, I joined ADP List
    as a mentor to share what I’ve learned.
  sec: 3527
  time: '58:47'
  who: Eddy
- line: I wish someone had guided me 10 years ago when I started my career as a data
    engineer. Engineers are often too busy fixing things to mentor others. I hope
    to inspire others to pursue this path and succeed.
  sec: 3527
  time: '58:47'
  who: Eddy
- header: Closing Remarks & Key Takeaways
- line: Thank you, Eddy. It was amazing talking to you. Thanks a lot for joining us
    today and sharing your experience.
  sec: 3572
  time: '59:32'
  who: Alexey
- line: I took a lot of notes—it was a very productive discussion. Now I know what
    FOPS is; I had no idea this even existed. Thanks for taking the time. It was truly
    amazing.
  sec: 3572
  time: '59:32'
  who: Alexey
- line: Thank you so much, Alexey. It was great to be part of the talk today.
  sec: 3594
  time: '59:54'
  who: Eddy
description: Master FinOps for data engineers—optimize BigQuery costs with dbt, cloud
  cost modeling, tagging and forecasting to cut spend and boost pipeline efficiency.
intro: How can data teams optimize cloud costs for analytics without slowing down
  delivery? In this episode Eddy Zulkifly, Staff Data Engineer at Kinaxis, walks through
  practical FinOps strategies for data engineers working with the modern data stack.
  Eddy brings a decade of experience across Google Cloud, Azure, and AWS, plus prior
  roles at Home Depot and ongoing graduate studies at Georgia Tech, and explains how
  his background in supply chain and analytics shapes cost-aware engineering. <br><br>
  We cover building a digital data warehouse using ELT, dbt, BigQuery and orchestration;
  operational differences like change velocity, monitoring, and tests; and translating
  business needs into metric trees and data specs for FinOps. Eddy breaks down cloud
  cost modeling—VM sizing, storage tiers, reservation instances, and multi-cloud comparisons—alongside
  cost-tagging, OUCS and standardized reporting across AWS/GCP/Azure. He also shares
  vendor negotiation tactics, demand-forecasting analogies for capacity planning,
  and the strategic responsibilities of senior data engineers. <br><br> Listen to
  learn actionable approaches to cloud cost optimization, practical dbt and BigQuery
  patterns, and how to embed FinOps practices into your data platform and team workflows.
dateadded: '2025-04-30'
duration: PT00H59M54S
quotableClips:
- name: Podcast Introduction
  startOffset: 0
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=0
  endOffset: 95
- name: 'Guest Introduction: Eddy Zulkifly, Staff Data Engineer at Kinaxis'
  startOffset: 95
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=95
  endOffset: 134
- name: 'Career Origins: Industrial Engineering, Supply Chain & Excel Macros'
  startOffset: 134
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=134
  endOffset: 380
- name: 'Career Pivot: From Business Analyst to Data Engineering'
  startOffset: 380
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=380
  endOffset: 468
- name: Analyst Skills as a Foundation for Data Engineering
  startOffset: 468
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=468
  endOffset: 486
- name: 'Docker & Terraform: Learning Curve for Data Practitioners'
  startOffset: 486
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=486
  endOffset: 498
- name: 'Tools & Low-Code Beginnings: Excel, Alteryx, Tableau'
  startOffset: 498
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=498
  endOffset: 673
- name: 'Retail & Warehousing Experience: Forecasting, Preload Optimization'
  startOffset: 673
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=673
  endOffset: 1317
- name: 'Digital Data Warehousing: Data as Inventory and Pipelines'
  startOffset: 1317
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1317
  endOffset: 1356
- name: 'Modern Data Stack: ELT, dbt, BigQuery and Orchestration'
  startOffset: 1356
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1356
  endOffset: 1474
- name: 'Operational Differences: Change Velocity, Monitoring, and Tests'
  startOffset: 1474
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1474
  endOffset: 1670
- name: 'Metric Trees & Data Specs: Translating Business Requirements for FinOps'
  startOffset: 1670
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1670
  endOffset: 1796
- name: 'Building a Digital Warehouse: Stack Choices and Open-Source Tools'
  startOffset: 1796
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1796
  endOffset: 1900
- name: 'FinOps Overview: Cloud Cost Optimization for SaaS Platforms'
  startOffset: 1900
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=1900
  endOffset: 2055
- name: Vendor Negotiations & Reservation Instances for Cost Savings
  startOffset: 2055
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2055
  endOffset: 2171
- name: 'Cloud Cost Modeling: VM Sizing, Storage Tiers and Multi-Cloud Comparison'
  startOffset: 2171
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2171
  endOffset: 2343
- name: 'Demand Forecasting Analogy: Inventory Planning Applied to Cloud Capacity'
  startOffset: 2343
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2343
  endOffset: 2418
- name: FinOps Foundation, Cost Tagging & Accountability Best Practices
  startOffset: 2418
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2418
  endOffset: 2681
- name: OUCS & Standardizing Cloud Cost Reporting Across AWS/GCP/Azure
  startOffset: 2681
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2681
  endOffset: 2777
- name: 'FinOps Processes: Parallels with DevOps, DataOps and CI/CD'
  startOffset: 2777
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2777
  endOffset: 2881
- name: 'Staff Data Engineer Responsibilities: Technical & Strategic FinOps Work'
  startOffset: 2881
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=2881
  endOffset: 3025
- name: 'Continuous Learning: Georgia Tech Master’s, dbt, Python and Applied Analytics'
  startOffset: 3025
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=3025
  endOffset: 3365
- name: 'Career Advice: Certifications, Mentorship, Community and Time Management'
  startOffset: 3365
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=3365
  endOffset: 3572
- name: Closing Remarks & Key Takeaways
  startOffset: 3572
  url: https://www.youtube.com/watch?v=7ePp6wuxM5s&t=3572
  endOffset: 3594
---

Links:

* [Twitter](https://x.com/eddarief){:target="_blank"}
* [Linkedin](https://www.linkedin.com/in/eddyzulkifly/){:target="_blank"}
* [Github](https://github.com/eyzyly/eyzyly){:target="_blank"}
* [ADPList](https://adplist.org/mentors/eddy-zulkifly){:target="_blank"}