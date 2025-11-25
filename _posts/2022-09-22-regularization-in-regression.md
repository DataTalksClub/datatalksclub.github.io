---
authors:
- ksenialegostay
description: Remedy for numerical instability
image: images/posts/2022-09-22-regularization-in-regression/cover.jpg
layout: post
subtitle: Remedy for numerical instability
tags:
- regression
- regularization
title: Regularization in Regression
math: true
datepublished: '2022-09-22'
date: '2022-09-22'
---

There are a lot of methods of how you can improve your ML model accuracy. They include feature engineering, missing value imputation, improvements in data quality, etc.

One of the effective approaches is regularization. It is a popular concept that helps to control coefficients under the numerical instability in computation taste such as model training.

In this article, we will take a closer look at why you might want to regularize your model. As an example, we will apply a basic regularization technique to a simple linear regression model and learn how it influences the model.


### Linear Regression

Linear regression is a supervised machine learning model, which can be expressed in a matrix form as follows:

$$g(X) \approx y$$

$X$ is a matrix where the features of observations are rows of the matrix and $y$ is a vector with the values we want to predict. Function $g(X)$ can be represented as a matrix-vector multiplication of feature matrix $X$ and some weight vector $w$:

$$Xw = y$$

After some transformations described in [Training Linear Regression: Normal Equation](https://www.youtube.com/watch?v=hx6nak-Y11g&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=18){:target="_blank"} lecture of [Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code#machine-learning-zoomcamp){:target="_blank"}, weight vector $w$ can be represented as:

$$w = (X^T X)^{-1}  X^T y$$

where

- $X^T$ is the [transpose](https://en.wikipedia.org/wiki/Transpose){:target="_blank"} of $X$,
- $X^T X$ is a [Gram matrix](https://en.wikipedia.org/wiki/Gram_matrix){:target="_blank"},
- $(X^T X)^{-1}$ is the [inverse](https://en.wikipedia.org/wiki/Invertible_matrix){:target="_blank"} of Gram matrix.

A matrix inversion should be considered with caution. If a matrix contains a column that is a linear combination of its other columns the matrix is singular, which means the inverse matrix does not exist.

### Why do we need regularization in Linear Regression

Linear dependent columns in a matrix is not a typical case in real-world problems, even though due to noise in the data, characteristics of your machine, OS, or NumPy version there might be some similar vectors in the above sense. When it happens, the weight vector $w$ can result in very large values (both positive and negative) and the overall model predictions won't be useful.

To overcome this numerical instability problem we can refer to regularization. Regularization in linear regression guarantees the existence of inverse matrix $(X^T X)^{-1}$

One of the regularization techniques is adding a factor to the diagonal of matrix $X^T X$ like this:

$$w = (X^T X + \alpha I)^{-1}  X^T y$$

where

- $I$ is an [Identity matrix](https://en.wikipedia.org/wiki/Identity_matrix){:target="_blank"} and
- $\alpha$ is a (typically small) factor.

This modification of the linear regression is commonly called [Ridge Regression](https://en.wikipedia.org/wiki/Ridge_regression){:target="_blank"}.


### How regularization can fix your Regression

Let’s demonstrate the effect of regularization through an example and see that the more regularization we add (factor $\alpha$), the smaller the weights $w$ become.

We will build a Linear Regression model for predicting car prices based on a dataset from Kaggle - [Car Prices Dataset](https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv){:target="_blank"}.

*The full code is in the notebook [here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/02-regression/notebook.ipynb){:target="_blank"}.*

For the sake of simplicity we won’t use any specific ML packages, instead we train a simple linear regression model in a vector form:

```python
# define feature matrix X of size 6x3 with nearly same second and third column 
X = np.array([[4, 4, 4],
             [3, 5, 5],
             [5, 1, 1],
             [5, 4, 4],
             [7, 5, 5],
             [4, 5, 5.00000001]])
# define vector y of size 1x6
y= np.array([1, 2, 3, 1, 2, 3])
# calculate Gram matrix for X
XTX = X.T.dot(X)
XTX

array([[140.        , 111.        , 111.00000004],
       [111.        , 108.        , 108.00000005],
       [111.00000004, 108.00000005, 108.0000001 ]])
 
# take inverse matrix of Gram matrix
XTX_inv = np.linalg.inv(XTX)
XTX_inv

array([[ 3.86409478e-02, -1.26839821e+05,  1.26839770e+05],
       [-1.26839767e+05,  2.88638033e+14, -2.88638033e+14],
       [ 1.26839727e+05, -2.88638033e+14,  2.88638033e+14]])

# calculate a weights vector w:
w = XTX_inv.dot(X.T).dot(y)
W

array([-1.93908875e-01, -3.61854375e+06,  3.61854643e+06])

```

As you can see the second and the third values of the weights vector $w$ are huge. It comes from the fact that initial feature matrix $X$ contains almost the same columns: 2 and 3.

Let’s introduce a regularisation term and see how the vector $w$ changes:

```python
# add regularization factor 0.01 to the main diagonal of Gram matrix
XTX = XTX + 0.01 * np.eye(3)

# take inverse matrix of Gram matrix
XTX_inv = np.linalg.inv(XTX)
XTX_inv

array([[ 3.85624712e-02, -1.98159300e-02, -1.98158861e-02],
       [-1.98159300e-02,  5.00124975e+01, -4.99875026e+01],
       [-1.98158861e-02, -4.99875026e+01,  5.00124974e+01]])


# calculate a weights vector w:
w = XTX_inv.dot(X.T).dot(y)
W

array([0.33643484, 0.04007035, 0.04007161])
```


The weights in vector $w$ now are reasonable and suitable for prediction.

The example of applying regularization in Linear Regression for car price prediction can be found in this [notebook](https://github.com/Ksyula/ML_Engineering/blob/master/02-regression/Regularization%20in%20Linear%20Regression.ipynb){:target="_blank"}.


### Summary

The main purpose of regularization techniques is to control the weights vector $w$ and not let it grow too large in magnitude. A regularized regression considered in this article is called Ridge Regression and you can typically find it in various ML packages (e.g. [scikit-learn](https://scikit-learn.org/){:target="_blank"}).

Regularization is capable of finding a solution when there are correlated columns, reduce overfitting and improve your model performance in many cases.