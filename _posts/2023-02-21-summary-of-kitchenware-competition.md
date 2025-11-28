---
authors:
- angelicaloduca
description: A deep dive into the Kaggle Competition on Kitchenware Classification,
  focusing on the winning approach.
image: images/posts/2023-02-21-summary-of-kitchenware-competition/cover.jpg
layout: post
subtitle: A deep dive into the Kaggle Competition on Kitchenware Classification, focusing
  on the winning approach.
tags:
- competition
- kaggle
title: 'A Summary Of The Kaggle Kitchenware Classification Competition: Find Out Who
  Won!'
datepublished: '2023-02-21'
date: '2023-02-21'
---

<figure>
<img src="/images/posts/2023-02-21-summary-of-kitchenware-competition/image1.png"  />
<figcaption><p>An overview of the Kitchenware Classification competition on Kaggle</p></figcaption>
</figure>

The Kaggle competition with the theme: Kitchenware Classification has just ended. Below is a summary of how it unfolded, some statistics, and the approach followed by the winners.

What we’ll cover

-   Overview of the competition
-   How the dataset was built
-   The starter notebooks
-   The solution of the winner
-   Making the solutions production-ready



## Overview of the Kitchenware Classification Competition

A Kaggle competition is an online competition where teams compete to develop the most accurate model based on certain data. Teams usually comprise data scientists, statisticians, and machine learning engineers who work together to develop a model that can accurately predict and classify data. The team with the best model wins the competition.

The Kaggle competition on Kitchenware Classification started on December 5th, 2022, and ended on February 1st, 2023. Participants were tasked with correctly identifying the type of kitchenware in a given image. There were six categories: cups, glasses, plates, spoons, forks, and knives.

### How the dataset was built

The dataset contains 9337 images. The following figure shows some sample images:

<figure>
<img src="/images/posts/2023-02-21-summary-of-kitchenware-competition/image3.png"  />
<figcaption><p>Some sample images were extracted from the dataset provided by the competition.</p></figcaption>
</figure>

The dataset was generated using [Toloka](https://toloka.ai/){:target="_blank"}, a scalable AI and Machine Learning development platform. Toloka covers the entire Machine Learning life cycle, starting from data collection and ending with model monitoring.

Toloka’s offerings include a crowdsourcing platform that enables companies to collect and label data using human insight. The annotators, called Tolokers,will complete simple tasks for money, such as labeling images or transcribing audio.

The Kitchenware dataset defined the following rules for image collection in Toloka:

-   The picture should be yours. It's best to use your phone and take pictures of your own kitchenware.
-   It's strictly not allowed to download pictures from the internet. It cannot be images from websites like Ikea or similar.
-   There should be only one item on the picture, not multiple
-   The item should be placed in the center of the picture
-   The item should be visible
-   If you have a set with many similar items (e.g., 6 forks, 6 spoons, etc.), don't take pictures of all six. Just take a picture of one spoon, fork, and so on.
-   Don't upload duplicates of your previous pictures. Each picture you submit should be unique
-   Don't upload multiple pictures of the same item. One is enough
-   Screenshots are not allowed. It has to be your picture



Checkthe related [documentation](https://docs.google.com/document/d/e/2PACX-1vRK9pEAbmrNm0kD-u09no2l8KP6gwZdBF87fB_RoF7duVDNi8NrVq4XqUYISOdZ6n1H33iEVoW9wBLZ/pub){:target="_blank"} and [workshop](https://www.youtube.com/watch?v=POGiLFWxQWQ){:target="_blank"} for more details on how the dataset was collected.

### The Starter Notebooks

The competition provided the competitors with two basic notebooks. The [first notebook](https://github.com/DataTalksClub/kitchenware-competition-starter/blob/main/keras-starter.ipynb){:target="_blank"} trains an xception model, and the [second](https://www.kaggle.com/code/harpdeci/supergradients-starter-notebook){:target="_blank"}, developed by Harpreet Sahota, uses SuperGradients. Competitors were asked to start from one of these two notebooks and then improve it to achieve a higher score.

Both notebooks are available in Saturn Cloud, an enterprise-level cloud computing platform enabling users to manage workloads, process data, and run applications in the cloud. Check [this repo](https://github.com/DataTalksClub/kitchenware-competition-starter){:target="_blank"} for instructions on running the notebooks in Saturn Cloud.

### Statistics

The following table resumes some statistics on the Kitchenware Competition:

| **Statistic**                     | **Value**                                    |
|-----------------------------------|----------------------------------------------|
| Number of participants            | 115 teams                                    |
| Average number of people per team | Most people did the competition individually |
| Lowest score                      | 0.05445                                      |
| Highest score                     | 0.99145                                      |

### The Prize

The winner of the Kitchenware Competition won the NVIDIA GeForce RTX 3080 Ti shown below:

<figure>
<img src="/images/posts/2023-02-21-summary-of-kitchenware-competition/image2.jpg"  />
<figcaption><p>The NVIDIA GeForce RTX 3080 Ti given as a prize to the winner.</p></figcaption>
</figure>

The competition also gave other prizes, including $3000 in AWS credits.

## The Winner 

The competition's winner is Olufemi Victor Tolulope with the [Kitchenware Classification 3rd Place Notebook](https://www.kaggle.com/code/victorolufemi/kitchenware-classification-3rd-place-notebook){:target="_blank"}. Olufemi Victor improved the [solution](https://www.kaggle.com/code/miwojc/starter-notebook-with-fastai){:target="_blank"} proposed by MIWOJC, who used the [fastai](https://docs.fast.ai/){:target="_blank"} Python library to train the model.

### The MIWOJC’s Solution

MIWOJC executed the following steps to solve the kitchenware classification problem:

1.  Import load data as ImageDataLoaders

2.  Create the learner model. Use the vision_learner() function provided by fastai. This line of code creates a vision learner object using fastai. MIWOJC used a convnext_nano model, which is an efficient and accurate model.

3.  Use the lr_find() method to find the best learning rate

4.  Use the fine_tune() method to fine-tune the model. The method takes two arguments: the number of training epochs and the learning rate.

### The Winner’s Solution

Olufemi Victor Tolulope started from the MIWOJC’s solution and improved it by modifying the following elements:

1.  Augment the dataset size using the [albumentations](https://albumentations.ai/){:target="_blank"} library. This library provides you with various augmentations, including geometrical transformations, color adjustments, and various other augmentations.

2.  Use the convnext_xlarge_384_in22ft1k model instead of convnext_nano. While the first model is an advanced convolutional neural network designed for larger image datasets, the second one is designed for small datasets. The convnext_xlarge_384_in22ft1k model is, therefore more powerful but requires more resources and computing power, while the convnext_nano model is lightweight and quick to train.

3.  Set the training floating point precision to 16 through the to_fp16() method. This setting provides a more accurate result by allowing the model to make calculations with higher precision. This is especially important when dealing with large datasets or complex models with many layers, as it can help to reduce numerical errors and improve the overall accuracy of the results.

4.  Use test time augmentation (TTA) to improve the model accuracy through the tta() method.

The winner also provided a solution ready for production by saving the export() method.

## Making it Production-Ready

Building a well-performing model is only the first step of a project life cycle. When the model is ready, you should move it to production, that is, making the model usable for predictions in a real environment. To make the competitors aware of this challenge, the Kitchenware Competition did not conclude with building a model. There was a second part of the competition, named [make it production ready](https://www.kaggle.com/competitions/kitchenware-classification/overview/make-it-production-ready){:target="_blank"}, which invited the competitors to build a GitHub repository for the project and, optionally, a blog post.

### Evaluation

A jury composed of two experts decided on the winner in the following categories:

-   The most production-ready ML solution (the overall winner of the contest).
-   The best GitHub repo with a solution.
-   The smallest model size (measured by the size of the models used in the final solution).



#### The Winners

The proposed solutions included some modern practices and frameworks for production: Docker containerization, serverless inference, optimized inference engines, package managers, and additional UI like Streamlit and Telegram.

The winning solution was proposed by **Martin Uribe**, who also got the nomination for “The best GitHub repo with a solution”. Martin’s solution: [https://github.com/clamytoe/kitchenware_classifier](https://github.com/clamytoe/kitchenware_classifier){:target="_blank"}.

**Bhaskar Sarma** won the prize for the smallest model size. Bhaskar’s solution: [https://github.com/bhasarma/kitchenware-classification-project](https://github.com/bhasarma/kitchenware-classification-project){:target="_blank"}.

## Acknowledgments

We thank our sponsors, [Toloka](https://toloka.ai/){:target="_blank"}, [SaturnCloud](https://saturncloud.io/){:target="_blank"}, and [NVIDIA](https://www.nvidia.com/){:target="_blank"}. We couldn't have done it without their support, and we're grateful for their help in making education more accessible and fun for our community.

We also want to thank [Rustem Feyzkhanov](https://www.linkedin.com/in/ryfeus/){:target="_blank"} for donating $2000 in AWS Credits.

And, most importantly, we thank our amazing community of participants. This competition would not have been the same without you. Your passion and dedication are truly inspiring.

Thank you all for making this competition a success!

## Summary

The Kaggle Competition on Kitchenware Classification was a great learning experience for many data scientists and computer vision enthusiasts. It provided an opportunity to apply the latest state-of-the-art algorithms, learn from others’ approaches and gain valuable insights into kitchenware classification problems.

Congratulations are due to all participants who worked hard throughout the competition and congratulations in particular to the winner of this amazing event!