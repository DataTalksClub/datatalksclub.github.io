---
authors:
- luisoliveira
description: With these, you will be a great professional
image: images/posts/2022-09-29-do-you-know-golden-rules-while-working-with-data/cover.jpg
layout: post
subtitle: With these, you will be a great professional
tags:
- data-engineering
- data-science
- best-practices
title: Do You Know the Golden Rules While Working With Data?
---

<figure>
<img src="/images/posts/2022-09-29-do-you-know-golden-rules-while-working-with-data/image1.png"  />
<figcaption><p>Following the rules will help you to be a great data professional (Photo by <a href="https://pixabay.com/users/loggawiggler-15/"><u>LoggaWiggler</u></a> on <a href="https://pixabay.com/"><u>Pixabay</u></a>)</p></figcaption>
</figure>

Data is an asset that can be captured, stored, analyzed, and retrieved whenever necessary. However, to have data is not enough to be so useful for businesses, rather, it is how we use data that makes all the difference.

Working with data isn’t as simple as "just" receiving information from a source and storing it in a designated location. Rather, it requires skillful manipulation to extract only what you need and no more, and the best possible way while being very efficient.

While working as a data engineer I always try to follow some rules. Some rules were given to me by my own Data Master: ["Data Mr. Myagi"](https://www.linkedin.com/in/guillermo-franco-garcia/){:target="_blank"} ("[Wash in, Wash out, Daniel-San](https://www.imdb.com/title/tt0087538/){:target="_blank"}" 🥋 ), and some I compose on my own.

The following five golden rules (see “Golden Rule” definition in [Cambridge Dictionary definition](https://dictionary.cambridge.org/dictionary/english/golden-rule){:target="_blank"}) will help you work efficiently with data:

-   Automate repetitive tasks;
-   Always work with data as a “defensive driver”;
-   If the solution is “nasty” then is wrong;
-   Do an extra effort to develop correctly from the start;
-   Data sources aren’t always right.



### 1. Automate repetitive tasks

One of the most important principles when working with data is to automate processes whenever possible. This will allow you to work efficiently, make fewer mistakes, and potentially save money.

<figure>
<img src="/images/posts/2022-09-29-do-you-know-golden-rules-while-working-with-data/image2.jpg"  />
<figcaption><p>Automate repetitive tasks to be a “Data Jedi” (Photo by <a href="https://www.flickr.com/photos/danandkir/"><u>Dan Pupek</u></a> from <a href="https://www.flickr.com/"><u>Flickr</u></a>)</p></figcaption>
</figure>

Automation can include a number of things, including integrating data from one system with another or using software to replace certain manual tasks. You cannot automate everything, but you should be able to identify areas where automation would be beneficial.

Likewise, you can automate processes in your personal life. A simple example is to set recurrent monthly payments (eg. water bill) by the direct debit transaction (where the bank extracts the amount for that bill on the same day every month).

### 2. Always work with data as a “defensive driver”

Once I heard the best definition for being a “defensive driver”:

-   To drive defensively is not about following the road rules but assuming that the other drivers will NOT follow these rules.



And this is what I want you to do, to work with data assuming that the data and/or the users that work with data will get wrong one day.

If you are going to work with data, you need to think about the future and what might happen in that future. Having data is good, but only if you can use it to make informed decisions not only today but also in the future. Therefore, you need to know what you may expect in future years.

To be more clear I will use examples:

1) If we are doing a SQL query based on dates this below is wrong because it will fail in January when the result will be 0 and, of course, there is no month 0.

```sql
SELECT MONTH(current_date) - 1 AS previous_month
FROM table
```

2) If you use hard-coded in your programming code sooner or later it will fail because the user can change the way he writes the information. In this example, the user can write the city in French, “Lisbonne”, and it will fail.

```python
if City_Name == 'Lisboa' OR City_Name == 'Lisbon':
    Country = 'Portugal'
```

### 3. If the solution is “nasty” then is wrong

For your ETL pipeline, Machine Learning model, or structure for visualization, you can have more than one solution but I can assure you that one will be the wrong solution: The “Nasty” Solution (by definition, the [bad or very unpleasant](https://dictionary.cambridge.org/dictionary/english/nasty#:~:text=bad%20or%20very%20unpleasant%3A){:target="_blank"} solution).

When you are developing your code or process you should:

-   Keep it as simple as possible (Do you know the KISS principle? - see definition [Wikipedia](https://en.wikipedia.org/wiki/KISS_principle){:target="_blank"});
-   Avoid redundancies. For example, enter a filter and then remove it later;
-   Guarantee each function or sub-process only performs one task;
-   Not create multiple nested codes or queries. More than three nested queries means something is wrong;
-   Document your code.



This golden rule takes into consideration internal quality code and the table below shows some properties the code must have to have good internal quality.

| **Code Properties** | **Definition**                                                  |
|---------------------|-----------------------------------------------------------------|
| Concision           | Code does not suffer from duplication                           |
| Cohesion            | Each \[module\|class\|routine\] does one thing and does it well |
| Low coupling        | Minimal interdependencies and interrelation between objects.    |
| Simplicity          | The quality or condition of being easy to understand or do.     |
| Generality          | The problem domain bounds are known and stated                  |
| Clarity             | The code enjoys a good auto-documentation level                 |

Internal quality code proprieties and its definitions (adaptation of [Good Code](https://wiki.c2.com/?GoodCode){:target="_blank"} information)

With this advice, I assure you that it will have a “beautiful” and readable code, and will allow future needed changes because internal quality code will affect external quality code.

And the golden rule is simple:

- If the code is “ugly” then it is wrong. 🙂

### 4. Do an extra effort to develop correctly from the start

This is a rule that can be seen as almost impossible to follow but it is very important because it will save you lots of time.

When developing your process you can follow two approaches:

1\) Write all the code/process to just give results and then, in the end, get the exact result proposed, correct some errors and write documentation, or

2\) Develop everything from the start.

I am a big fan of number 2) due several reasons:

-   If you correct the errors and write documentation while you are developing you will have a “fresh idea” of each sub-process and it will be easier for you;
-   If you take more time on each sub-process you will reflect more on it allowing you to “think on the future” and be a data “defensive driver”. (see golden rule number 2.)
-   Developing everything from the start will help you to reach a cleaner code (see golden rule number 3.);



Of course, this is a difficult golden rule to follow because it means to do an extra effort on each sub-process but I assure you it will compensate.

### 5. Data sources aren’t always right

While you should trust data, you shouldn’t trust it too much. For example, if you are working with survey data and have found some interesting statistics, you should be careful about drawing too many conclusions from it. You need to understand the source of the data and, if possible, try to replicate the results so that you know they are accurate.

There are three main reasons why you should be careful about trusting the data:

-   Data can be wrong: Data can be wrong for a number of reasons. It may have been collected incorrectly, the sample size may have been too small, or the data may have been entered incorrectly;
-   Data can be biased: Even if the data is collected and entered correctly, it can still be biased. For example, if you are using online surveys, people who are visiting that site may be different than the rest of your customer base;
-   Data can be outdated: Data can also be outdated. For example, if you are looking at sales data from last year, this data may not be applicable to this year.



Of course, it is impossible to always be “on top” of the data source quality but if you are doing a process, an analysis, a model, or visualization you have to have a critical vision of the data.


### **Summary**

Data is an important asset for businesses, but it is how you work with the data that makes all the difference.

These five golden rules mentioned in the article will help you work efficiently to be a better data professional. Just remember that:

1.  If you have repetitive tasks then they should be automated;

2.  While working with data you have to be a “chess player”, always thinking about the next moves;

3.  Confusing solutions are always wrong and will affect your process;

4.  Make additional efforts to develop properly from the beginning;

5.  Don’t always trust the data source quality.

Do you think these golden rules are possible to follow and will improve your work?

Do you have personal data guiding principles?

Did you like this article? Follow me for more articles on [Medium](https://medium.com/@lgsoliveira){:target="_blank"}.