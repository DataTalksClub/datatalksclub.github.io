---
authors:
- luisoliveira
description: How this has several impacts
image: images/posts/2022-10-21-important-sql-fact-that-everyone-should-know/cover.jpg
layout: post
subtitle: How this has several impacts
tags:
- sql
- data-engineering
title: Important SQL Fact That Everyone Should Know
---

<figure>
<img src="/images/posts/2022-10-21-important-sql-fact-that-everyone-should-know/image1.png"  />
<figcaption><p>SQL is the primary programming language used in databases (picture <a href="https://pixabay.com/users/earvine95-2534314/"><u>fromearvine95</u></a> in <a href="https://pixabay.com/"><u>Pixabay</u></a>)</p></figcaption>
</figure>

A database-management system (DBMS) is a group of linked data and a collection of software tools for accessing that data. The database, a collection of data, often contains information important to an organization. A DBMS's main objective is to offer a simple and effective method for storing and retrieving database data.

SQL (also called SeQueL or Structured Query Language) has been designed to make it easier for programmers to interact with databases. SQL provides a variety of language constructs for database queries, such as the SELECT, FROM, and WHERE clauses but also mechanisms to rename both attributes and relations, and to order query results by sorting on specific attributes.

According to the book “[Database System Concepts](https://www.mheducation.com/highered/product/database-system-concepts-silberschatz-korth/M9780078022159.html){:target="_blank"}” from McGraw-Hill Education (7th Edition) the history around SQL is as follows:

*“IBM developed the original version of SQL, originally called Sequel, as part of the System R project in the early 1970s. The Sequel language has evolved since then, and its name has changed to SQL (Structured Query Language).*

*In 1986, the American National Standards Institute (ANSI) and the International Organization for Standardization (ISO) published an SQL standard, called SQL-86. ANSI published an extended standard for SQL, SQL-89, in 1989. The next version of the standard was SQL-92 standard, followed by SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011, and most recently SQL:2016.”*

One important fact about SQL is the way the SQL syntax is read by the SQL processor (also called SQL engine).

In this article, we are going to talk about how the real order of the SQL syntax affects:

-   The final result of the query;
-   The performance of the query;
-   Readability of the query using an alias;



### How does the processor read the SQL statement?

SQL is considered by some authors as a programming language of the fourth level because it is very similar to a speaking language (in this case, similar to English), i.e. If you know how to write in English then you will quickly learn the basics of SQL. However, the real order of the statement is a little different.

Below I present to you the genuine order of the SQL statement.

| **Order** | **Clause** | **Description**                                                                         |
|-----------|------------|-----------------------------------------------------------------------------------------|
| 1st       | FROM       | Gets all the needed tables for the query - it includes all the JOIN clauses (Mandatory) |
| 2nd       | WHERE      | Filters the rows.                                                                       |
| 3th       | GROUP BY   | Aggregates the data according to common information.                                    |
| 4th       | HAVING     | Filters the groups created before.                                                      |
| **5th**   | **SELECT** | **Select the attributes(columns) that you need. (Mandatory)**                           |
| 6th       | ORDER BY   | Orders the result based on one attribute.                                               |
| 7th       | LIMIT      | Limit the number of rows represented.                                                   |

As you saw above the first clause to be read is the **FROM** with all the respective joins clauses (in case of existence), after that, we will filter the tables with the **WHERE** clause, then we create groups with **GROUP BY** followed by the group filtering using the **HAVING**.

Only after all these clauses, are we going to run the **SELECT** clause.

In case of need the clause **ORDER BY** is going to be read and then the **LIMIT** clause.

In a very general point of view, the SQL processor goes "from big to small" (by [Michael Shoemaker](https://medium.com/@dataslinger){:target="_blank"}) to get the wanted result, and then it will "think" in the way of presenting the result by ordering and limiting.

The real order of the SQL statement has implications on the query if you don't know this important SQL fact.

I created three tables running [PostgreSQL](https://www.postgresql.org/){:target="_blank"} locally using [Docker](https://www.docker.com/){:target="_blank"} containers, then I inserted some rows in these tables (clients, invoice, and client_invoice) that were used for the purpose of this article.

<figure>
<img src="/images/posts/2022-10-21-important-sql-fact-that-everyone-should-know/image2.jpg"  />
<figcaption><p><a href="https://medium.com/p/c388483712e9"><u>Learn how to run PostgreSQL locally</u> <u>on</u> <u>Docker</u></a> (picture created using the official PostgreSQL and Docker logos)</p></figcaption>
</figure>

### The impact of the SQL statement order

#### 2.1. The final result of the query

The obvious consequence of this order is the query's final result. You may be filtering a query in the FROM clauses (the first clause to run) when you have to filter with the **WHERE** clause.

One classic example is when you want to know the data present in one table and not another table. A simple way of analyzing this information is by doing a **LEFT JOIN** between the tables and then checking if there is no corresponding to the second table using a IS NULL filter (see query below). For this query I got as a final result 42 k rows, meaning that there are 42 k clients that are not in the client_invoice table.

```sql
SELECT COUNT(c.nickname) as number_nickname
FROM clients c
LEFT join client_invoice ci
ON c.id=ci.user_id
WHERE ci.id IS NULL
```

However if you run the query like this below you will get a warning saying that *““ci.id IS NULL” is always false”* and the total result we get is 172k rows. This query is obviously incorrect because we are trying to filter during the **JOIN** clause.

```sql
SELECT COUNT(c.nickname) as number_nickname
FROM clients c
LEFT join client_invoice ci
ON c.id=ci.user_id AND ci.id IS NULL
```

Another important piece of information regarding the SQL statement's real order is the awareness of the difference between the **WHERE** clause and the **HAVING** clause.

Since the SQL processor is running the **WHERE** clause in the second it will always filter the rows based on that clause, while the **HAVING** clause always needs the **GROUP BY** clause because the filter will be made according to the groups.

Knowing the difference between these two clauses is very important if you want to get a correct final result.

#### 2.2. The performance of the query 

Another effect of the order is the performance of the query. Since the **FROM** clause is the first to run if we have a join between two very large tables the performance can decrease. Sometimes it can be a good idea to filter one table before joining with another.

For this article, I made two simple queries and analyzed the time of each one:

-   For the first query, I did a simple join using the three tables and then filtering at the end.


```sql
SELECT nickname, SUM(value) as total_to_pay
FROM client_invoice ci
INNER JOIN clients cl
on cl.id=ci.user_id
INNER JOIN invoice i
on i.id=ci.invoice_id
WHERE nickname NOT ILIKE 'The Singer%'
GROUP BY nickname
HAVING sum(value) > 200000
ORDER BY total_to_pay
```

-   In the second query I filtered one table in a CTE before joining with the others.

```sql
WITH CTE_not_singer AS (SELECT id, nickname
			        FROM clients
			        WHERE nickname NOT ILIKE 'The Singer%')

SELECT nickname, SUM(value) as total_to_pay
FROM client_invoice ci
INNER JOIN CTE_not_singer cl
on cl.id=ci.user_id
INNER JOIN invoice i
on i.id=ci.invoice_id
GROUP BY nickname
HAVING sum(value) > 200000
ORDER BY total_to_pay
```

I made several iterations and got the final time results as you may see in the next table.

| **Iterations** | **Query 1**          | **Query 2**          |
|----------------|----------------------|----------------------|
| 1              | 09 sec 017 ms        | 09 sec 921 ms        |
| 2              | 09 sec 470 ms        | 08 sec 252 ms        |
| 3              | 08 sec 485 ms        | 07 sec 660 ms        |
| 4              | 07 sec 622 ms        | 07 sec 275 ms        |
| 5              | 07 sec 711 ms        | 07 sec 591 ms        |
| 6              | 09 sec 185 ms        | 07 sec 477 ms        |
| Average | 08 sec 582 ms | 08 sec 029 ms |

As you can see from the table above the second query had slightly better performance, not much but in a larger scale, you can imagine the possible effects (my tables have around 100 k rows so we can’t mention them as “big data” tables).

Of course, today's SQL processors feature one or more SQL planners, which will "improve" query performance (using indexes, choosing the most important attributes, etc.). However, if we are utilizing vast data or the database is continually updating (for example, daily UPDATES), these improvements will take some time. As a result, staying on top of our queries' performance is always a wise habit.

#### 2.3. Readability of the query using an alias

One golden rule while working with data is “If the solution is “nasty” then is wrong” (see all the Golden Rules [here](https://medium.com/@lgsoliveira/do-you-know-the-golden-rules-while-working-with-data-110385bc9b25){:target="_blank"}). This means that your code should be as “beautiful” as possible, for example, a query should have good readability.

Knowing the real order of the query you can apply several alias and therefore your SQL statement is easier to understand (for other developers or for “future you”).

The most common use of the alias is to give one to a table and then you can use it everywhere. Perhaps you didn’t know before why was that possible but now you know… the **FROM** clause is the first one to be read.

Since the clause **ORDER BY** only runs after the **SELECT** clause you also can use the alias like the example below.

```sql
SELECT c.nickname, count( distinct ci.invoice_id) total_invoice_id
FROM clients c
INNER JOIN client_invoice ci
ON c.id=ci.user_id
GROUP BY 1
ORDER BY total_invoice_id DESC	
```


But be aware that the **WHERE** clause is the second to be read and the **SELECT** clause is only the fifth. So if you try to run the query below you will get the error - “ \[42703\] ERROR: column "number_invoice_id" does not exist”

```sql
SELECT c.nickname, ci.invoice_id number_invoice_id
FROM clients c
INNER JOIN client_invoice ci
ON c.id=ci.user_id
WHERE number_invoice_id > 1000
```

Use alias to get beautiful queries but always remember the real order.

### Summary

SQL is a simple programming language to master the fundamentals of, but it does include several "secrets" and information that you must be aware of if you want to become a SQL expert.

One important fact that you should know is that the SQL statement order is not totally as it looks. The first clause to be read is the **FROM**, followed by the **WHERE** clause, then the **GROUP BY** and the HAVING clauses, followed by the **SELECT** clause, and at the end the **ORDER BY** and the **LIMIT** clause.

This information is significant since it can influence the query's final result, performance, and internal code quality.

I would like some feedback from your side 🙂

-   Did you know this was the real order of the statement?
-   Do you have any important information you know and could share with me?
-   Did you know the **SELECT** was almost the last to be… selected? 😁



Did you like this article? Follow me for more articles on [Medium](https://medium.com/@lgsoliveira){:target="_blank"}.