---
authors:
- igordemidov
description: Why df is a bad name for a dataframe
image: images/posts/2022-10-02-naming-variables-in-machine-learning/cover.jpg
layout: post
subtitle: Why df is a bad name for a dataframe
tags:
- machine-learning
- python
- clean-code
title: Naming Variables in Machine Learning
---

For a long time there has been a significant discrepancy in coding style between software engineers and data scientists. The first have been following established practice of good code writing, and the last… have just been writing some code. It worked well for us, data scientists, for quite some time. But then our projects became more complex, the code grew larger. Eventually, we faced the same complications in understanding our own code, as software engineers faced a long time ago.

Did you think that strict code writing conventions are for software engineers, not data scientists? Just like I did. It’s time to use our colleagues’ experience and adopt those good code practices one by one.

Starting from the very beginning. Can you tell what each variable in your project contains at any moment of time? Do you know its type? And most importantly, are you sure the variable contains what you expect it to contain?

If your answer is “ehm”, then read on - let’s reinvent the wheel.

<figure>
<img src="/images/posts/2022-10-02-naming-variables-in-machine-learning/image1.png"  />
<figcaption><p>Even in Python names are important</p></figcaption>
</figure>

## Clean Code

If you read Robert Martin’s “Clean Code” book, most of the points described here will be familiar to you. If you didn’t… just read it right after you finish this article and press the clap button. The book really provides a life changing experience. It describes a huge amount of techniques to make your code structurally better. The main idea that I took out of the book is that your code should strive to be reader-friendly as well as flexible for modification.

You may argue that it is the case for big “real” software applications, on which many engineers are working. If you are a machine learning specialist, most probably you work on your code alone. So why bother about readability? You know every corner of the code, right? Of course you are. Now imagine you get back to your code several months after. To fix something or to take one of its parts to a recent project. And this is where you face the “s” variable in the middle of a huge function named “func”. And now you need a huge cup of coffee, as you know you will need to spend time trying to remember what’s going on here.

“Okay, I’m convinced”, - I hope you say. If so, follow me.

## Naming Tips

### Intention-revealing names

This one is simple. Variable and function names should reveal intentions.

```python
if e > 10:
    break
```

If you look at this code abstractedly, can you guess what’s happening here? Probably not.

With a tiny tweak like this:

```python
if epoch > 10:
    break
```

it makes perfect sense: it’s definitely a part of a neural network training procedure, specifically, a training loop termination condition.

You say *epoch* is a standard name for data science? You are perfectly right! And this is the example of a meaningful name. You don’t need neither a comment nor additional guessing to understand what this part of the code is about.

What about bad names? I’d probably incur the wrath of the data science community, but “data” and “df” are poor names.

Let’s look at an example. Common data scientific code could look like this:

```python
def process_data(df):
    df = df.fillna()
    df['column_name'] = df['another_column'] * 5
    df = df.groupby('major_column').sum()
    df = pandas.concat([df.iloc[0:100], df.iloc[200:300])
    return df
```

Can you tell right away, what this code does? Probably you’d need some time to dig into it. And it could be much more complicated.

To solve this, it could be a good idea to detach operations of one purpose into a separated function with a meaningful name. There you’d know what happens inside, what comes in and out. Then organise everything into a data pipeline, which would eliminate the need to reassign all results into one variable (this we will discuss in one of the following articles).

### Comments to explain variables

Another hint is a comment. If you need it to explain what the variable means, then there probably might be a better name for it.

Compare two code examples, which do exactly the same. The first one is brute and straightforward:

```python
p = numpy.percentile(df.groupby('user')['sales'].mean(), 0.95)
x = df.groupby('user')['date'].min().max()
df = df[(df['sales'] >= p) & (df['date'] > x]
u = df['user'].unique()
```

The second one provides more readable solution:

```python
user_mean_sale = sales.groupby('user')['sales'].mean()
mean_sales_percentile = numpy.percentile(user_mean_sale, 0.95)

user_first_sale_date = sales.groupby('user')['date'].min()
latest_first_sale_date = user_first_sale_date.max()

recent_high_value_sales = sales[
                           (sales['sales'] >= mean_sales_percentile) & 
                           (sales['date'] > latest_first_sale_date)]
unique_hv_users = recent_high_value_sales['user'].unique()
```

You would probably need to add comments into the first code block to explain what each variable means in order to save you thinking efforts. Does the second part need a comment to describe intentions? Probably not. I can agree it looks more bulky, but look me in the eye and say you don’t understand what the second code example does. I won’t believe you. Now when you return to your code in several months or years, it doesn’t matter, you will be right on board with the code.

### Meaningful distinctions

<figure>
<img src="/images/posts/2022-10-02-naming-variables-in-machine-learning/image2.jpg"  />
<figcaption><p>The distinction should be really meaningful</p></figcaption>
</figure>

Sometimes you need to create several objects with similar content. It is important to make names, which express the difference between the objects. The most obvious example here might be variables *df* and *data.* What’s in *data* and what’s in *df*? How do they differ? Impossible to understand without a detective investigation about origins of both objects.

Similarly, naming objects like *df1* and *df2* does not help to understand the code.

Try to check your naming by answering the question if this specific word in the name helps to understand. For example, if you name a variable the_user_data, do all the words work for the purpose? The first word in the name (*the)* is definitely not important. If you omit it, the name’s meaning won’t change at all. The second one (*user)* – definitely is, extract it and you lose a vast share of information. *The third on (data)* – probably, as adding data type to naming isn’t considered a good practice, but still it can be useful to distinguish such important objects in machine learning projects as dataframes.

### Searchable names

This one seems quite self-explanatory. Imagine you want to rename a variable in your class or a notebook. Let’s say you want to change it from *train* to *test*. If you did the naming right, all you’ll need to do is to find and replace all the names. If not – you will have a hard time understanding if the current *train* is *the train* you want to change or if it’s meant for something else.

If you name your variable *sum*. How many false search results will you filter in order to find your variable.

Another use case is when you decide to get rid of some function and you want to make sure that variables generated by this function do not affect any other piece of code.

Finally, when you try to understand why your predicted validation data frame missing columns, it’s quite useful to run a search on a validation set variable to look through all the places where it’s involved.

### Class and method names

Perfect code can be read like a book. And this tip is one of the most elegant ways to get closer to it. Here is the idea: you name your classes in nouns, because a class is some service, providing you with specific processing; and functions are named in verbs, because a function executes one specific task. A function’s arguments are nouns as well, as they are mostly some data structures or primitive data types. As a result you can get a really smooth notation, like this:

```python
train_data = DataLoader().load_data(path)
```

or

```python
encoded_train = Encoder().encode_country(train_data)
```

You don’t really need any comments about these functions, do you? Proper naming tells the story by itself. Actually, you regularly meet such examples when using some properly designed libraries.

```python
RandomForestClassifier().train(train_data, train_target)
```

```python
pandas.DataFrame().corrwith(another_df)
```

Looks pretty and quite easy to read.

## Conclusion

Well written code will not make your model work faster or better. In some cases it can make your code shorter, but pretty often it will on the contrary enlarge the program. It may seem that for machine learning projects it’s redundant and only requires additional time and space. Of course it’s neither mandatory nor demanded as a must. Moreover, if you adopt this practice, you’d probably have numerous disputes with colleagues about whether this is a good or a bad thing. I can’t promise it will work for you, but it surely worked for me, and I hope I can put your mind to another helpful habit in writing code. As it will surely enhance your code readability and facilitate its support for the next reader, even if the next reader is the future you.