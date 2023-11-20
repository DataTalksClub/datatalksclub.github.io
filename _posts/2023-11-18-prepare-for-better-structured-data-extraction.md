---
authors:
- amberroberts
description: Structured Data Extraction with OpenAI Function Calling
image: images/posts/2023-11-18-prepare-for-better-structured-data-extraction/cover.jpg
layout: post
subtitle: Structured Data Extraction with OpenAI Function Calling
tags:
- arize
- monitoring
- llm
title: Prepare for (Better) Structured Data Extraction
---

<figure>
<img src="/images/posts/2023-11-18-prepare-for-better-structured-data-extraction/image3.jpg"  />
<figcaption></figcaption>
</figure>

<em>Authored in collaboration with Aman Khan</em>

Extracting structured information from unstructured data (i.e. audio, images, text) to make it easier to analyze and use is a common and often-critical task where machine learning is used in a larger software system.

This blog covers some of the differences between traditional and large language model (LLM) structured data extraction, then walks through an example of how to implement a structured data extraction application leveraging OpenAI function calling and [Phoenix](https://github.com/Arize-ai/phoenix){:target="_blank"}, an open source AI observability tool.

### Extracting Data from Unstructured Sources

The costs and intricacies involved in deciphering and analyzing unstructured data can be immense. While research is still ongoing on exactly where LLMs are more cost efficient for data extraction tasks compared to traditional NLP methods, it is clear that [many teams](https://arize.com/blog/llm-survey/){:target="_blank"} are beginning to implement LLM apps because they excel at intuitively grasping the intricacies of language, particularly on extracting structured data from unstructured text.

#### Traditional Unstructured Techniques

The exact methods and tools used for extracting structured information from unstructured data today depend on the use case in question, as well as exactly what data you are working with. For example, the most common strategy for extracting keywords from text data is Regular Expressions (Regex). It is rather baffling how fast we all went from using Regex to LLMs! In addition to Regex for text data extraction, natural language processing (NLP) techniques like Named Entity Recognition (NER) and Latent Dirichlet Allocation (LDA) have also been used to extract entities and determine the main topics via Topic Modeling respectively.

While there are many different methods for extracting text from images (object detection, image segmentation, optical character recognition) and audio (speech-to-text, Mel spectrograms, to name a few), this post only covers structured data extraction from written language to demonstrate the role of LLMs.

#### LLMs for Structured Data Extraction

While traditional text extraction methods are still used frequently, these approaches are starting to lose favor to LLMs due to their efficient and scalable approach to distill relevant data from unstructured text. While research is ongoing on whether or not LLMs are more [cost efficient for data extraction tasks](https://indatalabs.com/blog/large-language-model-benefits){:target="_blank"} (such as scraping text from documents and pulling keywords from queries), it is clear that LLMs are built with comprehensive extraction capabilities. LLMs excel at intuitively grasping the intricacies of language, particularly on extracting structured data from unstructured text.

<figure>
<img src="/images/posts/2023-11-18-prepare-for-better-structured-data-extraction/image4.jpg"  />
<figcaption><p>Structured data extraction using an LLM. Here, an LLM receives unstructured input together with a schema and outputs a structured representation of the information.</p></figcaption>
</figure>

The example above shows how LLMs can efficiently convert unstructured text data into structured information. These extracted attributes can then be used to construct a structured query to find options that might be relevant to the user or enrich company databases for future model training.

### Implementing a Structured Extraction Application with Arize Phoenix OSS

The [OpenAI API](https://arize.com/blog-course/mastering-openai-api-tips-and-tricks/){:target="_blank"} is great for developers looking to build LLM applications with few lines of code. However, it was still difficult for developers to work with unstructured data (mostly strings) without either regular expressions (RegEx) or prompt engineering to extract the information from the text string. OpenAI recently released new OpenAI's function calling capabilities for GPT-3.5 and GPT-4 models to take user-defined functions as input and generate structure output. [With this](https://www.datacamp.com/tutorial/open-ai-function-calling-tutorial){:target="_blank"}, you don't need to write RegEx or perform prompt engineering.

Arize Phoenix comes in as a way to instruct your OpenAI client to record trace data in OpenInference tracing format, inspect the traces and spans of your application to visualize your trace data, and export your trace data to run an evaluation on the quality of your structured extractions. Now, let’s see how to use OpenAI's function calling feature to perform structured data extraction: the task of transforming unstructured input (e.g., user requests in natural language) into structured format (e.g., tabular format).

Structured extraction is a place where it’s simplest to work directly with the OpenAI function calling API. OpenAI functions for structured data extraction recommends providing the following JSON schema object in the form of parameters_schema (the desired fields for structured data output).


```python
parameters_schema = {
    "type": "object",
    "properties": {
        "location": {
            "type": "string",
            "description": 'The desired destination location. Use city, state, and country format when possible. If no destination is provided, return "unstated".',
        },
        "budget_level": {
            "type": "string",
            "enum": ["low", "medium", "high", "not_stated"],
            "description": 'The desired budget level. If no budget level is provided, return "not_stated".',
        },
        "purpose": {
            "type": "string",
            "enum": ["business", "pleasure", "other", "non_stated"],
            "description": 'The purpose of the trip. If no purpose is provided, return "not_stated".',
        },
    },
    "required": ["location", "budget_level", "purpose"],
}
function_schema = {
    "name": "record_travel_request_attributes",
    "description": "Records the attributes of a travel request",
    "parameters": parameters_schema,
}
system_message = (
    "You are an assistant that parses and records the attributes of a user's travel request."
)
```

The ChatCompletion call to Open AI would look like:

```python
response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": travel_request},
    ],
    functions=[function_schema],
    # By default, the LLM will choose whether or not to call a function given the conversation context.
    # The line below forces the LLM to call the function so that the output conforms to the schema.
    function_call={"name": function_schema["name"]},
)
```

One powerful feature of the OpenAI chat completions API is function calling, wherein a user describes the signature and arguments of one or more functions to the OpenAI API via a JSON schema and natural language descriptions, and the LLM decides when to call each function and provides argument values depending on the context of the conversation. In addition to its primary purpose of integrating function inputs and outputs into a sequence of chat messages, function calling is also useful for structured data extraction, since you can specify a "function" that describes the desired format of your structured output. Structured data extraction is useful for a variety of purposes, including ETL or as input to another machine learning model such as a recommender system.

While it's possible to produce structured output without using function calling via careful prompting, function calling is more reliable at producing output that conforms to a particular format. For more details on OpenAI's function calling API, see the [OpenAI documentation](https://platform.openai.com/docs/introduction){:target="_blank"}.

### Tracing Structured Data Extraction with LLMs in Phoenix

Now let’s go through a colab notebook: *Tracing and Evaluating a Structured Data Extraction Application with OpenAI Function Calling* ([colab](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/tracing/openai_tracing_tutorial.ipynb){:target="_blank"} \| [github](https://github.com/Arize-ai/phoenix/blob/main/tutorials/tracing/openai_tracing_tutorial.ipynb){:target="_blank"}).

You can use Phoenix spans and traces to inspect the invocation parameters of the function to verify:

1.  The inputs to the model in form of the the user message
2.  Your request to OpenAI
3.  The corresponding generated outputs from the model match what's expected from the schema and are correct

<figure>
<img src="/images/posts/2023-11-18-prepare-for-better-structured-data-extraction/image5.png"  />
<figcaption><p>Viewing a batch of traces within Phoenix</p></figcaption>
</figure>

The full tutorial covers how to:

-   Use OpenAI's [function calling feature](https://openai.com/blog/function-calling-and-other-api-updates){:target="_blank"} to perform structured data extraction: the task of transforming unstructured input (e.g., user requests in natural language) into structured format (e.g., tabular format),
-   Instrument your OpenAI client to record trace data in [OpenInference tracing](https://github.com/Arize-ai/open-inference-spec/blob/main/trace/spec/traces.md){:target="_blank"} format,
-   Inspect the traces and spans of your application to visualize your trace data,
-   Export your trace data to run an evaluation on the quality of your structured extractions.



Topics include:

-   OpenAI
-   Structured data extraction
-   Function calling
-   Note: This notebook requires an OpenAI API key.



### Additional Evaluations for Structured Extraction with LLMs

When working with unstructured data, it's important to have a clear understanding of the desired outcome, as the methods and tools you choose will depend on the specific task at hand. It's also crucial to continuously evaluate and refine the extraction processes to ensure accuracy and relevancy.

Evals help you continuously understand your system’s performance after deployment. Evaluating LLM applications needs to take place across three environments: pre-production when you’re doing the benchmarking, pre-production when you’re testing your application and production when it’s deployed. Life is messy. Data drifts, users drift, models drift, all in unpredictable ways. Just because your system worked well once doesn’t mean it will do so on Tuesday at 7 p.m.

<figure>
<img src="/images/posts/2023-11-18-prepare-for-better-structured-data-extraction/image2.jpg"  />
<figcaption><p><em>LLM evals need to work in several different environments: pre-production (benchmarking, testing) and production to understand a system’s performance.</em></p></figcaption>
</figure>

Remember that verifying correctness of extraction at scale or in a batch pipeline can be challenging and expensive. It is a best practice not to do [LLM evals](https://arize.com/blog-course/llm-evaluation-the-definitive-guide/){:target="_blank"} with one-off code but rather a library that has built-in prompt templates. This increases reproducibility and allows for more flexible evaluation where you can swap out different pieces.

<figure>
<img src="/images/posts/2023-11-18-prepare-for-better-structured-data-extraction/image1.png"  />
<figcaption><p><em>Workflow for evaluating an LLM retrieval span using Phoenix</em></p></figcaption>
</figure>

Evaluating data extraction tasks performed by LLMs is challenging with these models being non-determinism and often not having “ground truths” for their language tasks; However, with careful monitoring and LLM observability using LLMs for structured data extraction can scale faster and perform better than any previously used methods.

Ready to dive deeper? Get certified in key areas like [Traces and Spans](https://courses.arize.com/p/llm-observability-traces-spans?dl_cd=eyJrdiI6IktWX2VjOGE0OTI2YTE5MGVhNzBiZTMyMWUzMWFlZDM2YWEwIiwiaXNQcmV2aWV3IjpmYWxzZX0%3D){:target="_blank"} or [Agents, Tools, and Chains](https://courses.arize.com/p/agents-tools-and-chains?dl_cd=eyJrdiI6IktWX2VjOGE0OTI2YTE5MGVhNzBiZTMyMWUzMWFlZDM2YWEwIiwiaXNQcmV2aWV3IjpmYWxzZX0%3D){:target="_blank"} or ask questions on the [Arize community](https://arize.com/community/){:target="_blank"}.

<em>This post is sponsored by [Arize](https://arize.com/model-monitoring/){:target="_blank"}.
We thank the [Arize](https://arize.com/model-monitoring/) team for their ongoing support of the community.</em>
