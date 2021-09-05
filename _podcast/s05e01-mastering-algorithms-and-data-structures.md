---
title: "Mastering Algorithms and Data Structures"
short: "Mastering Algorithms and Data Structures"
guests: [marcellolarocca]

image: images/podcast/s05e01-mastering-algorithms-and-data-structures.jpg

season: 5
episode: 1

ids:
  youtube: RiQa-9LguW8
  anchor: Mastering-Algorithms-and-Data-Structures---Marcello-La-Rocca-e16s7lf

links:
  youtube: https://www.youtube.com/watch?v=RiQa-9LguW8
  anchor: https://anchor.fm/datatalksclub/episodes/Mastering-Algorithms-and-Data-Structures---Marcello-La-Rocca-e16s7lf
  spotify: https://open.spotify.com/episode/5IM2Des1sjVIwrvB3dGoJN
  apple: https://podcasts.apple.com/us/podcast/mastering-algorithms-and-data-structures-marcello-la/id1541710331?i=1000534241523

transcript:
- line: "This week, we'll talk about algorithms. We have a special guest, Marcello.\
    \ Marcello is a senior software engineer at Tundra. And he is the author of \"\
    Advanced Algorithms and Data Structures\". I think it was released recently, right?\
    \ It's out of MEAP now. Congratulations. It\u2019s a book about algorithms. Marcello\
    \ works with graphs, optimization, algorithms, genetic algorithms, machine learning,\
    \ and quantum computing. Welcome."
  sec: 111
  time: '1:51'
  who: Alexey
- line: Hi. Thanks a lot for inviting me. It's a pleasure.
  sec: 172
  time: '2:52'
  who: Marcello
- header: "Marcello\u2019s background"
- line: My pleasure as well. Before we go into our main topic of algorithms, let's
    start with your background. Can you tell us about your career journey so far?
  sec: 179
  time: '2:59'
  who: Alexey
- line: "I've worked as a web developer and on data infrastructure. I started with\
    \ web development. Then, I worked for five years in a government-owned company\
    \ in Italy. Then I started working remotely with startups and then moved to Ireland\
    \ to join Twitter. Then I worked for Microsoft, Apple. And last year, I joined\
    \ Tundra \u2014 an online shop."
  sec: 191
  time: '3:11'
  who: Marcello
- line: Does Tundra have anything to do with forests in Russia?
  sec: 246
  time: '4:06'
  who: Alexey
- line: No, I don't know. Nobody knows where the name exactly comes from. But it's
    a nice company.
  sec: 252
  time: '4:12'
  who: Marcello
- header: Learning algorithms and data structures
- line: How should people approach learning algorithms?
  sec: 291
  time: '4:51'
  who: Alexey
- line: "It can be learned at a very different level, depending on how much in-depth\
    \ you need to learn. When I started my studies, I was suggested that it's important\
    \ not to focus on details. You need to learn that there is such an algorithm,\
    \ when to use it \u2014 in which situations, and what problems it can solve. Also\
    \ perhaps, how efficient it is. By knowing that there is such an algorithm, that\
    \ it solves a certain problem, you can find it when you need it at work \u2014\
    \ when you should apply it. If you don't remember the algorithm by heart, that's\
    \ fine. Nobody can remember all the algorithms. But if you know where to look\
    \ for it, it's perfect."
  sec: 319
  time: '5:19'
  who: Marcello
- line: "I didn't have algorithms during my studies, so I was learning them outside\
    \ of the university, by myself. Many courses I took focused on derivations and\
    \ on mathematical proofs. It seemed like that is an important thing \u2014 to\
    \ really understand how the algorithm works and to prove that it's O(N log N)\
    \ using some difficult mathematical stuff. So this is not something we should\
    \ focus on, we should focus more on applications, right?"
  sec: 407
  time: '6:47'
  who: Alexey
- line: Yes. There is also a funny story about this. Google was created by Page and
    Brin. When they started their studies, they talked to an Italian researcher about
    this idea of an intelligent crawler. It did the searching in a different way than
    just indexing like Yahoo or Altavista. This guy went to his Italian University
    and proposed this idea. They told him that, it would never have a future because
    you couldn't prove that it was right. So focusing on the mathematical proof can
    be tricky and dangerous. It's important, of course, if you are working on a paper
    to prove that the algorithm works. But it doesn't mean that if you don't know
    how it works, or don't work out the math, it will be useless.
  sec: 450
  time: '7:30'
  who: Marcello
- header: Resources for learning algorithms and data structures
- line: So when we learn algorithms we should focus more on applications than proofs.
    Do you know any good references for basic algorithms, like sorting?
  sec: 540
  time: '9:00'
  who: Alexey
- line: "There are a lot of resources online \u2014 courses and websites. There is\
    \ a series of videos from MIT, it's very good. There is Tim Roughgarden's course\
    \ on Coursera. It explains things clearly and it's as simple as it gets. If you\
    \ prefer books, I can suggest Grokking Algorithms published by Manning, which\
    \ also is a general introduction to basic algorithms and data structures."
  sec: 563
  time: '9:23'
  who: Marcello
- header: Most important data structures
- line: In your opinion, what are the most important algorithms and data structures
    that we should know? By "we", I mean developers, data engineers, and data scientists.
    So, for anyone who programs, what kind of algorithms data structures they should
    know?
  sec: 608
  time: '10:08'
  who: Alexey
- line: "Importance is relative. It depends on your field and what you're actually\
    \ doing. The basic data structures can be the most important. They are the ones\
    \ that can make a greater impact. Misusing an array or a list can hurt the performance\
    \ of your application a lot. And it\u2019s very common that you are using these\
    \ data structures, so they are the most important ones."
  sec: 634
  time: '10:34'
  who: Marcello
- line: So you need to know array, list, when to use them, when to use set, when to
    use a dictionary, right?
  sec: 680
  time: '11:20'
  who: Alexey
- line: "For example, knowing when you should use an array, or when you should use\
    \ a list, depending on what you have to do. If you need random access, array is\
    \ the best choice. But if you are always adding elements in front, array is complicated\
    \ \u2014 you will have to do a lot of copying and moving of memory. It becomes\
    \ a mess. Besides arrays and lists, the bare minimum for me would be stacks, queues,\
    \ these kinds of structures."
  sec: 690
  time: '11:30'
  who: Marcello
- line: And sets as well?
  sec: 729
  time: '12:09'
  who: Alexey
- line: Sets, yes, of course.
  sec: 732
  time: '12:12'
  who: Marcello
- header: Learning the abstractions
- line: "Let's say if we use Python, it comes with a set of different data structures.\
    \ So knowing \u2014 at least having some idea \u2014 how they are implemented\
    \ internally is useful. Like, if you want to add something, how does it work inside?\
    \ If you want to check if something is in a list or is in a set, how does it work?\
    \ And things like this."
  sec: 737
  time: '12:17'
  who: Alexey
- line: "Yes, absolutely. With algorithms, you have to distinguish the implementation\
    \ and the abstract data structures. The first step would be understanding what's\
    \ the abstraction behind it. And then you can implement it in many ways. For example,\
    \ you could implement a dictionary with anything \u2014 with a list or an array,\
    \ or a tree, or a hash table. All these implementations have pros and cons. They\
    \ do well on some operations and perform poorly on other operations."
  sec: 774
  time: '12:54'
  who: Marcello
- line: If you use a language like Python, you are more interested in understanding
    the abstraction behind it. What's the API of the dictionary, what are the operations
    that you do? Then if you delve into the language, if you're performing time-critical
    operations or memory-critical operations, then you might want to dive into the
    implementations. Understand how we can leverage those or if they can present any
    problem or any bottleneck.
  sec: 816
  time: '13:36'
  who: Marcello
- line: So you can take all the data structures that you should use, from Python or
    any other language, and you learn their APIs. What are the possible methods? And
    then try to understand how they work internally, right?
  sec: 853
  time: '14:13'
  who: Alexey
- line: "Yes. For example, you mentioned the set. It's important to know that what's\
    \ the contracts that the client has with a data structure like a set \u2014 you\
    \ can add elements, you can remove elements, but there will be no duplicates.\
    \ You can expect that insertions and checks are reasonably fast compared to an\
    \ array. Although this also depends on the implementation."
  sec: 873
  time: '14:33'
  who: Marcello
- header: "Learning algorithms if they aren\u2019t needed at work"
- line: "You mentioned that you worked as a web developer at some point. I heard this\
    \ from many web developers, and also from data scientists as well. Let's talk\
    \ about web developers. These days, they do simple things \u2014 they create simple\
    \ web applications. They say, \"I don't actually need algorithms for that. All\
    \ I need is this library React. It works, and I don't need to use algorithms.\""
  sec: 909
  time: '15:09'
  who: Alexey
- line: So how do I learn algorithms if I don't need them at work? It's not unique
    to web developers.
  sec: 945
  time: '15:45'
  who: Alexey
- line: "First, I'd like to challenge the assumption that you don't need algorithms\
    \ for that. If you as a web developer, or a data analyst, or a data scientist,\
    \ you use algorithms more than you think. Even the basic one that we mentioned\
    \ earlier \u2014 I cannot believe that you are not using arrays or lists. That\
    \ can make a big difference. As a web developer, you may have time-constraint\
    \ or resource-constraint. Or you may have to handle large data sets as a data\
    \ scientist. Web developers can be in a situation where using the right data structure\
    \ makes a difference. For example, if you have to provide some spell checker functionality.\
    \ If you know what Bloom filters or tries are, then you're in a better position.\
    \ Otherwise, you might end up reinventing the wheel or providing a suboptimal\
    \ solution, whether or not you use a third-party library."
  sec: 957
  time: '15:57'
  who: Marcello
- line: To go back to your question, how do you master algorithms if you don't have
    the chance to work every day on this in your job?
  sec: 1060
  time: '17:40'
  who: Marcello
- line: Yeah, I don't implement spell checkers every day. How do I learn how to use
    Bloom filters?
  sec: 1071
  time: '17:51'
  who: Alexey
- line: "There are a few things. If you're interested in the topic, there are a lot\
    \ of resources. You can do some learning on your own, you can set goals. But if\
    \ you're looking for extra motivation, joining some competition like Google Code\
    \ Jam or something like that, can be a good push for you. You can get motivated\
    \ to learn more. And more than that, it gives anyone the chance to learn in the\
    \ field and have some practical experience with these algorithms \u2014 not just\
    \ knowing the theory but actually learning to use them and to take advantage of\
    \ these data structures."
  sec: 1081
  time: '18:01'
  who: Marcello
- line: So if you cannot do this at work, try to do this outside of work.
  sec: 1147
  time: '19:07'
  who: Alexey
- line: "Well, it's not common that at work you need to implement these algorithms\
    \ from scratch. But you can learn how to use them at work. One thing you can do\
    \ \u2014 if you see that there is a bottleneck or see some room for improvement\
    \ when profiling your application, you can try to learn which algorithms can help\
    \ in similar situations and try to apply them. Especially if you use a mainstream\
    \ programming language at work, it's easy to find libraries that implement common\
    \ and advanced algorithms. Then you will see how they can make a difference."
  sec: 1154
  time: '19:14'
  who: Marcello
- header: Common mistakes when using wrong data structures
- line: One mistake I often notice in code is people accidentally use a list for checking
    for containment instead of using a set. Simple things like that are very common
    for web developers and for data scientists. This is a very common operation. You
    have something that comes in, and you want to check if this is something that
    you already know or not. For that, you check if this X is in a collection of seen
    things. If we just replace a list with a set, then we see an order of magnitude
    improvement in speed.
  sec: 1214
  time: '20:14'
  who: Alexey
- line: Exactly. Similarly, I have seen that for keeping track of elements, for adding
    elements to a list, people add it to the wrong end of the list. For example, in
    Scala, or in Haskell, adding it to the wrong end of the list can cause this simple
    operation to become slow and time out your server.
  sec: 1258
  time: '20:58'
  who: Marcello
- header: Importance of data structures for data scientists
- line: Coming back to the question, "How important are these data structures for
    data scientists?" I think we just mentioned this particular use case like checking
    for containment. And as a data scientist, I do this operation very often. In your
    opinion, are there other cases where it's very important to know data structures
    for data scientists?
  sec: 1298
  time: '21:38'
  who: Alexey
- line: "Whenever you are working on huge data sets, even the slightest improvement\
    \ can make a difference in time. And if you have an order of magnitude improvement,\
    \ that makes a tremendous difference. It can be speeding up searches \u2014 using\
    \ Bloom filters instead of dictionaries to keep track of what you have already\
    \ seen. It can be the nearest neighbour search to search in this huge multi-dimensional\
    \ data sets. I think they are even more important for data scientists."
  sec: 1332
  time: '22:12'
  who: Marcello
- header: "Marcello\u2019s book - Advanced Algorithms and Data Structures"
- line: You mentioned bloom filters and approximate neighbour search. This is actually
    something I wanted to talk to you about. You cover them in your book. So maybe
    let's talk a bit about your book. First of all, what is there in your book? Can
    you tell us a bit about that?
  sec: 1390
  time: '23:10'
  who: Alexey
- line: 'The idea for writing this book was to provide a bridge between theoretical
    knowledge on algorithms in textbooks and more practical knowledge from hands-on
    books. My book covers both the theory and more practical aspects of how to use
    the algorithms. For each data structure or algorithm in the book, the focus was
    coming up with a real-life use case where you can make a difference by using the
    right algorithm. The problem can also be the opposite: you can make a negative
    difference by using the wrong data structure in the wrong place. If you learn
    to avoid that, that''s already great and you can improve the performance of your
    applications.'
  sec: 1419
  time: '23:39'
  who: Marcello
- line: "There are 18 chapters and 3 parts. The first part and the appendices cover\
    \ the basic data structures \u2014 they cover the ground. Then we go into more\
    \ complicated algorithms. In the second part, we cover nearest neighbour search,\
    \ machine learning clustering, explain the MapReduce programming model. In the\
    \ third part, we cover graphs, evolutionary algorithms, and optimization in general\
    \ \u2014 different options for permutation problems from random algorithms and\
    \ random sampling to gradient descent, simulated annealing, and genetic algorithms."
  sec: 1504
  time: '25:04'
  who: Marcello
- line: It's called "advanced algorithms". Does it require some knowledge of algorithms
    already?
  sec: 1579
  time: '26:19'
  who: Alexey
- line: We try to cover the basics in the appendices in the first few chapters. You
    shouldn't need anything more. Of course, if you had "Algorithms 101", or if you
    have previous experience with the topic, you're in better shape.
  sec: 1591
  time: '26:31'
  who: Marcello
- line: I guess if somebody watches this MIT course that you recommended, or the Coursera
    course by Tim Roughgarden, then these will give enough foundation to continue
    with your book. But even if they don't do these courses, you cover everything
    in the appendices as well as the first chapters, right?
  sec: 1628
  time: '27:08'
  who: Alexey
- line: Yes, we cover everything you need to start. You don't need complex math, knowledge
    of linear algebra, and you need initial knowledge of programming. We don't use
    a single programming language, we use pseudocode, so anyone with any background
    can understand how the algorithms work. The only thing that will help is knowing
    what a for loop or conditional is.
  sec: 1658
  time: '27:38'
  who: Marcello
- line: I know that you also have a GitHub repo, where all these algorithms are implemented
    in every possible language.
  sec: 1717
  time: '28:37'
  who: Alexey
- line: Not every possible, but my goal is to have them in as many languages as possible.
    For now, most of them are implemented in Java, JavaScript, and Python. Soon, in
    Scala, and I was hoping to add C++ and Rust later.
  sec: 1729
  time: '28:49'
  who: Marcello
- line: So you also had a lot of fun implementing it in all these different languages.
  sec: 1751
  time: '29:11'
  who: Alexey
- line: Yes. It's fun.
  sec: 1757
  time: '29:17'
  who: Marcello
- line: Do you plan to cover Go as well after you cover these ones?
  sec: 1760
  time: '29:20'
  who: Alexey
- line: Yeah, why not? I love Go.
  sec: 1767
  time: '29:27'
  who: Marcello
- header: Bloom filters
- line: When I look at the table of contents, I got interested in Bloom filters and
    approximate nearest neighbours, and coincidentally, this is what we already talked
    about previously. I thought maybe we could cover a bit these data structures a
    bit?
  sec: 1783
  time: '29:43'
  who: Alexey
- line: Let's start with Bloom filters. So what problem do they solve? And why do
    we need them?
  sec: 1809
  time: '30:09'
  who: Alexey
- line: "It's not a coincidence, they're very useful for data science. Bloom filter\
    \ is quite an interesting data structure. Surprisingly, it's not as widespread\
    \ as I would expect. Bloom filters solve the traditional dictionary problem. The\
    \ dictionary is a container. You can save entries there and retrieve them quite\
    \ fast. There are many different ways you can implement it. For example, you can\
    \ implement it as a tree \u2014 as a fully balanced tree or a binary search tree.\
    \ Then you can get good performance for almost all applications. But what people\
    \ usually associate with dictionaries are hash tables \u2014  they are synonyms\
    \ in many languages."
  sec: 1817
  time: '30:17'
  who: Marcello
- line: "Bloom filters work similarly to hash tables \u2014 they leverage hash functions.\
    \ But they follow a different approach compared to hash tables, which allows them\
    \ to use limited memory. If you have a large data set, you might not have enough\
    \ memory or disk space to use a hash table. This happens especially when you store\
    \ variable-size data such as strings in your containers. In that case, you can\
    \ store each entry in a Bloom filter regardless of how much space they require.\
    \ You can store them with the same amount of space. And we need a fixed number\
    \ of lookups to find those elements."
  sec: 1902
  time: '31:42'
  who: Marcello
- line: Of course, you have to pay a price for this. The price can be performance,
    because each time you look it up or store it, you have to hash the same entry
    many times. The other big disadvantage is that you can have false positives with
    Bloom filters. If you look up for an entry, the Bloom filter can tell you that
    it was stored although it actually wasn't. This is caused by the way that works
    internally. I explain these in chapter eight. I don't know if we have time to
    explain it.
  sec: 1992
  time: '33:12'
  who: Marcello
- line: "Probably not. I just wanted to ask, what are they used for? To summarise\
    \ you said: we need to use this data structure when we have a limited amount of\
    \ memory. It uses hashes to look things up. We use it to check if something is\
    \ in our Bloom filter or not \u2014 for containment. But the way it works, sometimes\
    \ it gives us false positives. It can say \"this item is there\", but actually\
    \ it's not true."
  sec: 2043
  time: '34:03'
  who: Alexey
- header: Where Bloom filters are useful
- line: "Sometimes it's not a big deal. Bloom filters are used in many, many places.\
    \ For example, in crawlers to check if a page was already visited \u2014 by looking\
    \ at the URL, or even at the content of the page. They were used in spell checkers,\
    \ but now they are placed by tries. But for a long time, they were used for that.\
    \ They are used a lot in routing tables to check if an IP address was already\
    \ visited or not. In all these cases, if you have a false positive, it's not a\
    \ big deal. In a crawler, you will process the page again. With Bloom filters,\
    \ you can balance the amount of memory you use with the false-positive ratio.\
    \ You can control how often false positives happen and how often you pay this\
    \ penalty."
  sec: 2083
  time: '34:43'
  who: Marcello
- line: "Maybe I can also tell about a use case I had a couple of years ago at the\
    \ previous company. The company is adtech company. They're doing advertisements.\
    \ They're selling advertisements on mobile devices \u2014 all these annoying ads\
    \ that you see when playing games, we contributed to that."
  sec: 2159
  time: '35:59'
  who: Alexey
- line: "Every phone has some ID \u2014 the device ID. Let's say I am a returning\
    \ user of an app. I have used the app already, and the owners of the app want\
    \ to bring me back. For example, I played 10 levels and stopped. They want to\
    \ show me an ad saying, \"Hey, come back, finish your game\". So they have the\
    \ device IDs of everyone who played the game, but stopped \u2014 and there are\
    \ hundreds of thousands of device IDs if a game is popular."
  sec: 2185
  time: '36:25'
  who: Alexey
- line: "When I open a different app, it's sending a request... There is an auction\
    \ happening under the hood, but it doesn't matter now. But we want to check if\
    \ we know this person or not \u2014 is it a returning user or not? Imagine that\
    \ for everyone in the world who's holding a phone right now, we want to show an\
    \ ad. We only want a subset of those people \u2014 only the returning users. For\
    \ that, we use a Bloom filter to check if we know this user or not. Because it's\
    \ impossible to store everything in memory. If it turns out that we actually don't\
    \ know this user, even though we think we do, it's not a big deal. We just show\
    \ that person an ad. We lose a fraction of a cent, but the world doesn't stop\
    \ because of this."
  sec: 2245
  time: '37:25'
  who: Alexey
- line: It's used a lot in industries like marketing. Every time you want to bring
    back a user, you need to store all these users. This is when I learned why Bloom
    filters exist and why we actually need them. Before that, I had no idea. Previously,
    I just watched this course on Coursera by Tim Roughgarden. It looked complex and
    I had no idea why this thing is actually needed.
  sec: 2312
  time: '38:32'
  who: Alexey
- line: It is a perfect use case.
  sec: 2344
  time: '39:04'
  who: Marcello
- header: Approximate nearest neighbours
- line: What about search trees? You have another part of your book where you talk
    about approximate nearest neighbours. Maybe we can talk about this use case as
    well. Why do we need approximate search trees for approximate nearest neighbours?
  sec: 2350
  time: '39:10'
  who: Alexey
- line: "We need nearest neightbors search in many fields, especially in data science\
    \ \u2014 when we need to search in multi-dimensional data. Binary search tree\
    \ is a fast way to search in a static or slowly changing set. You can also use\
    \ automatically balanced search trees like red-black trees to tackle more dynamic\
    \ sets. But they work for one-dimensional datasets, and we often have to deal\
    \ with multi-dimensional data. Even geographical data with geolocations. And there\
    \ are also other data sets with hundreds of features."
  sec: 2373
  time: '39:33'
  who: Marcello
- line: Binary search trees don't generalise well to multi-dimensional sets. It's
    possible to use it, it's still faster than going through all the data points,
    but for multi-dimensional sets, it may become costly even to compare a single
    data point with the rest of the data.
  sec: 2459
  time: '40:59'
  who: Marcello
- line: "The way we can solve this is to use the nearest neighbour search. There are\
    \ different data structures for that. The first one that was invented to deal\
    \ with this particular problem was the KD trees. It's 40-50 years old, and for\
    \ a long time, that was the best solution for this. However, now, there are even\
    \ better structures \u2014 KD trees have some problems. They work well up to a\
    \ certain dimensionality of the data, and they don't work well with high dimensional\
    \ data sets. And they also have a problem with dynamic sets."
  sec: 2497
  time: '41:37'
  who: Marcello
- line: "In the book, we go through a credit risk example to whet the appetite, to\
    \ explain the basics and explain why nearest neighbour search is important. Then\
    \ we go through a real case of using geolocation for a delivery system of an online\
    \ shop \u2014 to handle millions of orders and for each of them, find the closest\
    \ warehouse from where the goods can be shipped. We then go through R-trees and\
    \ SS-trees (similarity search trees), which handle high-dimensional spaces better,\
    \ and allow this \"approximate nearest neighbour\" search."
  sec: 2564
  time: '42:44'
  who: Marcello
- line: Sometimes we don't need the actual best possible results, we can be good with
    close-to-the-optimal results. For example, if two warehouses are approximately
    10 km away from the destination, it doesn't matter if one is 100 meters closer.
    If we can perform this search faster, and find the sub-optimal solution which
    is only 1% and 0.1% further away than the best possible solution then, in many,
    many areas, for many, many problems, it's pretty much the same.
  sec: 2624
  time: '43:44'
  who: Marcello
- header: Searching for most similar vectors
- line: "I have an example in my mind, but I'm not sure if this is a great example\
    \ for search trees. I work at OLX. OLX is an online marketplace and we have a\
    \ recommender system there. In the recommender system, we want to recommend to\
    \ a person things that they might be interested in. Think of Amazon as well \u2014\
    \ based on what you saw previously, we want to recommend something that the user\
    \ might be interested in. For that, we represent each item with a 16-dimensional\
    \ vector \u2014 an array with 16 numbers. Then we do a similar thing with the\
    \ users \u2014 we represent each user as a 16-dimensional array. You have an array\
    \ for a user, and you have an array for each item. Then, for each user, we want\
    \ to find the closest possibly item array to the user array. We look at all the\
    \ items, and we try to find the closest one. Often, we don't need the closest\
    \ one. We just need something that is close enough. Is it a good use case for\
    \ that?"
  sec: 2686
  time: '44:46'
  who: Alexey
- line: "Yes, it's a perfect use case. This, or finding similar images, if the images\
    \ are translated to feature vectors. For example, we may want to find similar\
    \ images to a product that the user \u2014 or similar users \u2014 already saw.\
    \ Even finding not just the closest one, but the five closest profiles to some\
    \ users or five closest images. It's a perfect use case."
  sec: 2776
  time: '46:16'
  who: Marcello
- line: We use a library for that. It's called "faiss", it's from Facebook. To be
    honest, I don't know what it actually uses inside. I just know that it works faster
    than brute force search. It probably users one of those data structures inside.
  sec: 2810
  time: '46:50'
  who: Alexey
- line: It's possible. These data structures are used a lot in machine learning. For
    example, in clustering, K-means or other clustering algorithms can use this nearest
    neighbour search to speed up the algorithm.
  sec: 2831
  time: '47:11'
  who: Marcello
- header: Knowing frameworks vs knowing internals of data structures
- line: "We have a question that may be quite related to the point I just brought\
    \ up \u2014 about using a library and not necessarily knowing what is inside.\
    \ It's a question from WingCode. Is it necessary to know data structures? Or knowing\
    \ how to use a framework is more important? For example, we can just take an off-the-shelf\
    \ implementation of Bloom filters. Do we need to know how these things work inside?"
  sec: 2867
  time: '47:47'
  who: Alexey
- line: "The most important thing is to know how they work on the outside. What you\
    \ can expect? What is the contract that you have with this structure? What are\
    \ the guarantees that you have from them? Most of the time you can be fine not\
    \ knowing the internals. You need that only if you have to improve your performance\
    \ or if you run into problems. The other case where you might want to know how\
    \ things work is when you have to do customization \u2014 when you cannot use\
    \ something off-the-shelf and you have to write your own. Another possible case\
    \ is when you're using a new programming language for which there is no such library\
    \ yet. So you have to write your own. You have to be the first one. But it's more\
    \ common that you have to implement a customised solution yourself."
  sec: 2903
  time: '48:23'
  who: Marcello
- header: Serializing Bloom filters
- line: "I was talking about this use case of an adtech company. We ended up implementing\
    \ Bloom filters ourselves. We needed to have exactly the same implementation for\
    \ multiple languages \u2014 for Go, for Java, and for JavaScript. And for Python\
    \ as well \u2014 because we are data scientists, and the data scientists work\
    \ in Python. If we create a Bloom filter, we need to make sure that this Bloom\
    \ filter can be used by whatever other language we were running. We ended up implementing\
    \ Bloom filters ourselves. I did that. I remember that I took the implementation\
    \ from somewhere and just re-implemented it. I cannot claim I actually know how\
    \ it works. But it seems to work."
  sec: 2992
  time: '49:52'
  who: Alexey
- line: "In Bloom filters, you have false positives. So, you need to know at least\
    \ a little bit about the internals of bloom filters \u2014 to understand that\
    \ you can control false positives based on the size of your set and based on the\
    \ false positive error rate you want. How can you make sure that you can minimise\
    \ this error rate? You need to know a little bit about that to use Bloom filters.\
    \ But maybe for the first use case, you can just go ahead and use something like\
    \ Google Guava. It's a library in Java, they use a pretty good preset configuration.\
    \ You don't need to care about what is inside. It just gives you an okay Bloom\
    \ filter. Then, if performance is not good, you can try to understand what's going\
    \ on inside and tune it."
  sec: 3044
  time: '50:44'
  who: Alexey
- line: Yes. This use case is an ideal example. You needed a serialisation of this
    Bloom filter and you needed to have the same seeds for the hash functions. That's
    another case where you might want to have control of these things.
  sec: 3116
  time: '51:56'
  who: Marcello
- line: "We were producing Bloom filters in a Python job \u2014 we're data scientists,\
    \ that's the only language we know. But then it was used by production systems\
    \ written in Java, Go, and, for some reason, JavaScript. But we needed to read\
    \ these boom filters. It was fun. I liked doing that."
  sec: 3143
  time: '52:23'
  who: Alexey
- header: Algorithmic problems in job interviews
- line: What do you think about job interviews? In job interviews, companies seem
    to be really obsessed with algorithms. You worked at Twitter, at Microsoft as
    well. I have an impression that if you want to get into these companies, you really
    need to know all the "Algorithms 101", and you also need to know more advanced
    algorithms. You need to know trees, graphs, and so on. What do you think about
    this? Is it reasonable that these companies expect everyone to know these things?
  sec: 3175
  time: '52:55'
  who: Alexey
- line: 'These companies have a lot of experience interviewing people. It''s hard
    for me to say. When I was at Twitter, we worked actively on changing the way interviews
    were done. When you focus only on challenges and algorithms, you are not interviewing
    the candidates with the right knowledge and the right skills. Maybe they will
    use them. Certainly, it''s good to know if a candidate knows about performance
    bottlenecks and how they can screw everything by misusing an array. But it''s
    not the only part of the job. There is much more. I''ve seen candidates who did
    a stellar job on the algorithms interview and then they could not use Git. They
    had to catch up a lot on their first month on the job. I think it''s too much.
    It''s good to have some questions on these, but it''s also good to test a different
    set of skills in the interview. I like mixing different kinds of interviews: doing
    some pair programming, or even some debugging in the interviews. You can see how
    is it actually working with this person, and what they can do on the job.'
  sec: 3227
  time: '53:47'
  who: Marcello
- line: Like debugging Bloom filters?
  sec: 3337
  time: '55:37'
  who: Alexey
- line: That's maybe a tough one.
  sec: 3342
  time: '55:42'
  who: Marcello
- line: Could be. I remember I had an interview with Facebook. I don't remember the
    exact questions. But you need to solve two problems in 35 minutes. Two, not just
    one. If you spent 30 minutes solving one, then you have just five minutes for
    solving the second one. It's too cruel.
  sec: 3345
  time: '55:45'
  who: Alexey
- line: When you have limited time, maybe you don't have the right idea immediately.
    Also because of the pressure.
  sec: 3380
  time: '56:20'
  who: Marcello
- line: For me, they had two such interviews in a row. So, two times like that. That
    was too much.
  sec: 3392
  time: '56:32'
  who: Alexey
- header: Important data structures for data scientists and data engineers
- line: I didn't notice one interesting question. There are quite a lot of algorithms
    and data structures. For data engineers, data scientists, and everyone else who
    works with machine learning, what are the most needed ones? We talked about arrays
    and sets. Is there anything else that every data scientist and data engineer should
    keep in mind?
  sec: 3403
  time: '56:43'
  who: Alexey
- line: "For sure, the basics. At least knowing what binary search is \u2014 it's\
    \ a must."
  sec: 3440
  time: '57:20'
  who: Marcello
- line: Especially if you want to get to Facebook.
  sec: 3453
  time: '57:33'
  who: Alexey
- line: "If you're going to interview for these companies, I have to share that I\
    \ had similar experiences as you. You need to know all the basics and graphs as\
    \ well \u2014 like DFS, BFS, even Dijkstra. But probably not much more than that.\
    \ Sometimes I got questions that could be solved with interval trees or more exotic\
    \ ones."
  sec: 3460
  time: '57:40'
  who: Marcello
- line: There are programming contests. You need to use some very smart data structures
    to solve problems there, like interval trees. These people will have no problems
    getting into Facebook.
  sec: 3497
  time: '58:17'
  who: Alexey
- line: Actually, I once was interviewed by one of the former champions.
  sec: 3514
  time: '58:34'
  who: Marcello
- header: Learning by doing
- line: "Maybe the last one. Can you suggest good resources for building projects\
    \ to learn data structures and algorithms? To learn them by doing \u2014 by using\
    \ them? I think already you suggested taking part in online competitions, like\
    \ topcoder, are there are many of them. But maybe we can build our own pet project\
    \ to learn data structures and algorithms?"
  sec: 3533
  time: '58:53'
  who: Alexey
- line: There are sites like leetcode. You have problems there and you can try to
    solve them. You can also see other people's solutions. You can learn new techniques
    to solve the same problems. Another suggestion is working on an open-source project.
    You can join one or start your own. You can also get feedback, especially if you
    join an existing project. If you start yours, you'll need to put yourself out
    there to get some feedback.
  sec: 3584
  time: '59:44'
  who: Marcello
- header: Importance of compiled languages for data scientists
- line: Thank you. Another question popped up. Do you recommend to data scientists,
    interested in data structures and algorithms, to go into compiled languages like
    C++ or Java, rather than use Python? Is there any advantage going this way?
  sec: 3639
  time: '1:00:39'
  who: Alexey
- line: I think Python is perfect for data scientists. It has the best libraries for
    data. It's like Esperanto for data science. But you might need to implement the
    production model, then you might need C++ more than Java. It will allow you to
    write more performant code, with multi-threading and greater control on the low-level
    details. Maybe sometimes it's the difference between data scientists and data
    engineers. Data engineers could be more on the C++ side than data scientists.
    It can be useful. But I wouldn't suggest switching one for the other. But maybe
    learn about it.
  sec: 3669
  time: '1:01:09'
  who: Marcello
- line: "And there is a thing called \u201CCython\u201D. You don't need to ditch Python\
    \ completely, you can use Cython \u2014 it's almost C. You can have quite performant\
    \ and typed code for number crunching. You can still stay within the Python realm,\
    \ but you also get the benefits of writing in native code."
  sec: 3745
  time: '1:02:25'
  who: Alexey
- header: Wrapping up
- line: I guess that's all for today. How can people find you?
  sec: 3781
  time: '1:03:01'
  who: Alexey
- line: On Twitter and also on Slack.
  sec: 3787
  time: '1:03:07'
  who: Marcello
- line: Thanks for the chat. Thanks for joining us today, for sharing your experience
    with us. It was nice chatting with you.
  sec: 3812
  time: '1:03:32'
  who: Alexey
- line: Thank you. Thank you again for having me.
  sec: 3821
  time: '1:03:41'
  who: Marcello
- line: I aslo wanted to thank everyone for joining us today and asking questions.
    That's it. Have a great weekend.
  sec: 3822
  time: '1:03:42'
  who: Alexey

---


Links:

- Marcello's book: [Advanced Algorithms and Data Structures](http://mng.bz/eP79){:target="_blank"} (promo code for 35% discount: poddatatalks21)
- [MIT, Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/){:target="_blank"}
- [Algorithms specialization by Tim Roughgarden](https://www.coursera.org/specializations/algorithms){:target="_blank"}
