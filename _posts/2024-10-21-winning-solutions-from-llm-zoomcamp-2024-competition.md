---
authors:
- valeriiakuka
description: Solving High School Mathematics Problems with LLMs
image: images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/cover.jpg
layout: post
subtitle: Solving High School Mathematics Problems with LLMs
tags:
- competition
- llm
title: Winning Solutions from the LLM Zoomcamp 2024 Competition
---

In October 2024, we announced the winners of the [LLM Zoomcamp 2024 Competition](https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/overview){:target="_blank"}, where participants tackled high school math problems using large language models (LLMs). This challenge was part of our [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp){:target="_blank"}, a free course focused on real-world LLM applications.

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image1.png"  />
<figcaption>LLM Zoomcamp 2024 Competition <a href="https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/overview">(source)</a>.</figcaption>
</figure>

In this article, we’ll share insights from the competition and spotlight some of the top solutions. Here’s what we’ll cover:

-   [Overview of the LLM Zoomcamp 2024 Competition](#overview-of-the-llm-zoomcamp-2024-competition)
-   [Dataset Description](#dataset-description)
-   [Artur G's Solution: Combining Code Generation with Chain-of-Thought Reasoning](#artur-gs-solution-combining-code-generation-with-chain-of-thought-reasoning)
-   [Blaqadonis' Solution: Agent-based Approach Leveraging LangGraph](#blaqadonis-solution-agent-based-approach-leveraging-langgraph)
-   [Vladyslav Khaitov’s Hybrid Model Approach](#vladyslav-khaitovs-hybrid-model-approach)
-   [Slava Shen's Solution: Blending Results with Data-Driven Logic](#slava-shens-solution-blending-results-with-data-driven-logic)



### Overview of the LLM Zoomcamp 2024 Competition

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image6.png"  />
<figcaption>A sample Russian ЕГЭ exam answer sheet <a href="https://en.wikipedia.org/wiki/Unified_State_Exam">(source)</a>.</figcaption>
</figure>

The competition tasked participants with solving high school-level math problems from the [Russian ЕГЭ exam](https://en.wikipedia.org/wiki/Unified_State_Exam){:target="_blank"} using LLMs. The ЕГЭ exam is a standardized test required for admission to Russian universities and professional colleges.

We provided participants with the original problem statements in Russian and their English translations, generated by GPT-4. The goal was to solve these problems using LLMs without manual intervention.

### Dataset Description

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image7.jpg"  />
<figcaption>A screenshot of the train data, source: train.csv</figcaption>
</figure>

The dataset for the competition consisted of several CSV files containing training and test data. Key components of the dataset included:

-   Training Data: Contained problem statements in English and Russian, answers, and hints. The data also included unchecked entries that might contain errors.
-   Test Data: Required participants to predict the correct answers based on the problem statements in both languages.
-   Sample Submission File: Offered guidance on the expected format for final submissions.



Now, let’s take a closer look at the winning solutions and the approaches behind them.

### Artur G's Solution: Combining Code Generation with Chain-of-Thought Reasoning

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image2.png"  />
<figcaption>LLM Zoomcamp leaderboard <a href="https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/leaderboard">(source)</a>.</figcaption>
</figure>

Artur G’s [solution](https://github.com/ArturGR3/LLM-kaggle-competition){:target="_blank"} used Claude-3.5 Sonnet’s natural language understanding and Python code generation capabilities. He applied the Zero-shot Chain-of-Thought technique to prompt Claude-3.5 Sonnet to reason through problems and created two solutions:

-   Solution 1: Reasoning without code.
-   Solution 2: Reasoning supported by Python code execution.



To select the final solution, Artur compared the results from both approaches. If they matched, the answer was considered correct. If they didn’t, an additional reasoning step was performed to refine the answer.

Artur’s solution also included several safeguards:

-   **[Instructor](https://github.com/jxnl/instructor){:target="_blank"} validation** to ensure the Python code was executable.
-   A **timeout mechanism** to prevent infinite loops.
-   **Error handling** that allowed for retries in case of code failures.



Here are Artur’s key takeaway from this competition:

> One might wonder if LLMs are useful to solve math problems. My answer is yes; the techniques I used, such as structured outputs, chain of thought reasoning, multithreading, and error handling with retry mechanisms, can elevate most LLM-based applications to the next level.

### Blaqadonis' Solution: Agent-based Approach Leveraging LangGraph

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image4.png"  />
<figcaption>A screenshot of a notebook with Blaqadonis' solution <a href="https://colab.research.google.com/drive/1EtEePcBQUQ731c4QARKcJuVyGERbxGAI?usp=sharing">(source)</a>.</figcaption>
</figure>

Blaqadonis's [solution](https://colab.research.google.com/drive/1EtEePcBQUQ731c4QARKcJuVyGERbxGAI?usp=sharing){:target="_blank"} used an agent-based approach, coordinating two models: OpenAI’s GPT-4 Omni and Meta’s Llama 3.1 70B through LangGraph, a low-level framework for building stateful AI applications. His solution achieved high accuracy at a cost of less than $3 per test run.

Blaqadonis used the Groq API to handle rate limits and avoid throttling. With a leaderboard score of 96.25%, his solution showcased the scalability and cost-effectiveness of agentic systems in solving complex problems. He also noted some challenges in the reliability of such systems.

Reflecting on his experience, Blaqadonis said:

> What impressed me most was the leap in reasoning capabilities from GPT-3.5 Turbo to the current models. This improvement was reflected in the leaderboard scores: from 90% to 96.25% using agents. Among the latest models, there was a significant gap between the GPT-4o-mini and the original GPT-4o.

### Vladyslav Khaitov’s Hybrid Model Approach

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image5.png"  />
<figcaption>A screenshot of Vladyslav Khaitov's description of their solution. <a href="https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/discussion/540578">(source)</a>.</figcaption>
</figure>

Vladyslav Khaitov's [solution](https://www.kaggle.com/competitions/llm-zoomcamp-2024-competition/discussion/540578){:target="_blank"} combined open-source [NuminaMath-7B-TIR-GPTQ](https://huggingface.co/AI-MO/NuminaMath-7B-TIR-GPTQ){:target="_blank"} with GPT-4 Omni to balance cost and performance. His hybrid approach used different models for different tasks, achieving high accuracy and cost efficiency.

Vladyslav initially adapted a [solution](https://www.kaggle.com/code/lewtun/numina-1st-place-solution/notebook){:target="_blank"} from the [AI Mathematical Olympiad competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-prize){:target="_blank"}, which used the [NuminaMath-7B-TIR-GPTQ](https://huggingface.co/AI-MO/NuminaMath-7B-TIR-GPTQ){:target="_blank"} math LLM and Python REPL. Then, for certain task types where this solution performed poorly, Vladyslav used OpenAI’s GPT-4o to handle those specific cases.

Key aspects of Vladyslav’s solution included:

-   **Majority voting**: Running models multiple times and selecting the most common solution, a form of ensembling for LLMs. Vladyslav noted that while this required many runs, it significantly improved results.
-   **Extensive post-processing**: Much of the post-processing came from the Numina solution, but Vladyslav added more to accommodate differences in data and task types.
-   **Prompt experimentation**: Minimal prompts worked best for Numina, while structured prompts like "Please reason step by step, and put your final answer within `\\boxed{}`" improved results for GPT-4o.



Vladyslav shared his conclusions from the competition:

> Many open-source models (without tool use, like Mathstral) didn’t perform well enough. Even OpenAI GPT-4o-mini fell short. The difference between GPT-4o-mini and GPT-4o was significant.

### Slava Shen's Solution: Blending Results with Data-driven Logic

<figure>
<img src="/images/posts/2024-10-21-winning-solutions-from-llm-zoomcamp-2024-competition/image3.png"  />
<figcaption>A screenshot of Slava Shen’s submissions.</figcaption>
</figure>

Slava Shen provided multiple [solutions](https://docs.google.com/document/d/1zAFJEvP3hdquuR6emN55qYnzHUC1mLY68JrxM8mD63Q/edit?usp=sharing){:target="_blank"}, all based on GPT-4o-mini:

-   Solution 1: Combined solutions 2 and 3, with mismatches resolved through randomized selection based on a hyperparameter.
-   Solution 2: A refined version of an initial [Kaggle notebook](https://www.kaggle.com/code/vyacheslavshen/double-check-with-llms){:target="_blank"} with adjustments to prompts and temperature settings.
-   Solution 3: The most complex approach, which involved dynamically constructing few-shot prompts using Elastic Search and running Python code extracted from the model's output.


Slava’s solutions demonstrated flexibility and robustness, combining different models and methodologies, resulting in a final score of 95%.

### Conclusion

The LLM Zoomcamp 2024 Competition was a great opportunity to test the limits of LLMs in solving structured mathematical problems. Participants explored diverse approaches, from blending open-source and closed-source models to using agentic systems and advanced prompt engineering techniques.