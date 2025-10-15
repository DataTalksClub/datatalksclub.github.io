---
authors:
- valeriiakuka
description: "2024 LLM Survey Results: 200+ professionals reveal OpenAI dominance (73%), self-hosting trends, fine-tuning practices, and production deployment strategies. Key insights on managed services, cloud infrastructure, and integration frameworks."
image: images/posts/2025-04-11-how-do-professionals-use-llm-tools-and-frameworks/cover.jpg
layout: post
subtitle: Results of our DataTalks.Club Survey
tags:
- survey
- ai
- '2024'
title: How Do Professionals Use LLM Tools and Frameworks?
charts: true
---

We [surveyed](https://docs.google.com/forms/d/e/1FAIpQLScdx1FAIp2GDGgiMf7xu-I1PfhsQBJDvFstGmWmWbpP4S69Zg/viewform){:target="_blank"} over 200 professionals working with large language models (LLMs) to capture insights on adopting managed services, self-hosting options, customization practices, infrastructure choices, and integration strategies.

In this article, we present key findings on managed LLM services, customization, fine-tuning practices, infrastructure choices, and current use cases among technical professionals.

Let's explore the data.

## Managed LLM Services

Respondents primarily rely on managed LLM services, with OpenAI clearly in the lead:

-   **OpenAI** - Used by 73.4% of respondents
-   **Anthropic** - Adopted by 24.5%
-   **AWS Bedrock** - Selected by 10.8%
-   **Groq** - Used by 12.4%
-   **No managed service** - 20.7% indicated they do not use any managed LLM services
-   **Other Providers** - Platforms such as Google, Azure, and IBM Watsonx have only limited adoption, indicating a high level of concentration around a few key players

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which managed LLM services or cloud-based providers do you use?"
          data-labels='["OpenAI", "Anthropic", "I don’t use any managed LLM services"]'
          data-values='[73.1, 24.4, 21.1]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>OpenAI dominates the managed LLM services space.</figcaption>
</figure>

The dominance of OpenAI suggests that its offerings are considered reliable and well-suited to a broad set of applications. The concentrated market share may also indicate the trust and maturity these services have built over time.

## Self-Hosting Open-Source LLMs

Regarding self-hosting, the majority (74.1%) do not run open-source LLMs on their own infrastructure.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Do you use any solutions for self-hosting open-source LLMs?"
          data-labels='["We don't self-host LLMs", "vLLM", "Self-written (custom inference solutions)"]'
          data-values='[74.1, 9.4, 8.5]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Majority do not self-host open-source LLMs.</figcaption>
</figure>


Among those who do:

-   **vLLM:** Used by 9.4%.
-   **Custom solutions:** About 8.5% have developed their own inference setups.
-   Other tools like TGI, Ollama, and cortex.cpp have smaller adoption rates.

Managed services clearly dominate due to their ease of use and reduced maintenance overhead. However, the minority pursuing self-hosted solutions typically do so for greater control over the models, potentially lower costs, or to customize the system for specific needs.

This suggests that while the majority prioritize convenience, a dedicated subset is willing to invest in infrastructure to tailor performance more closely to their requirements.

## Customization and Fine-Tuning

Fifty percent of respondents customize their LLMs, while the other half use them as provided.

The equal split in customization practices suggests that many professionals see value in tailoring models to specific applications.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="If you do any fine-tuning of LLMs, which of the following applies?"
          data-labels='["No, I don't fine-tune", "Yes, for self-hosted", "Yes, for managed LLM"]'
          data-values='[72.6, 15.6, 11.8]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Fine-tuning is uncommon &ndash; most don't do it.</figcaption>
</figure>


Regarding fine-tuning:

-   **Fine-tuning managed services** - 11.9% engage in fine-tuning
-   **Fine-tuning self-hosted models** - 15.7% do so
-   **No fine-tuning** - 72.5% do not fine-tune their LLMs

However, the relatively low rates of fine-tuning indicate that significant model modification remains niche, either due to the technical complexity involved or because the out-of-the-box performance is sufficient for many tasks. Over time, we might see an increase in fine-tuning as organizations look to optimize performance for specialized use cases.

## Infrastructure for LLMs

Over half (54.7%) of respondents find GPU provisioning not applicable, likely because they do not run extensive training or fine-tuning workloads in-house.

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="How do you access or provision GPUs for training/fine-tuning or running LLMs?"
          data-labels='["Cloud (AWS)", "Cloud (Azure)", "Cloud (GCP)", "Cloud (Other)", "On-premise / Private"]'
          data-values='[39.0, 22.9, 16.2, 2.9, 12.4]'
          data-height="300px"
          data-width="500px">
  </canvas>
  <figcaption>Most rely on cloud GPUs, especially AWS and Azure.</figcaption>
</figure>

For those who use GPUs:

-   **Cloud-based GPUs:** Providers like AWS (39%), GCP (16.2%), Azure (22.9%), and other cloud services are used.
-   **On-premise/Private Data Centers:** 12% reported using dedicated hardware.



The preference for cloud-based GPU solutions underscores a trend toward scalable, on-demand computing. This avoids the substantial capital expenditures associated with owning and maintaining physical hardware while meeting performance needs. The relatively small number of organizations using on-premise solutions may indicate either cost barriers or the complexity of managing dedicated hardware.

## Integration and Observability Tools

While dedicated vector databases such as Chroma and Pinecone have gained traction, the majority of respondents either rely on more traditional systems or have yet to integrate these specialized tools. This may reflect a transitional phase where organizations are still exploring the best methods for handling vectorized data in LLM-powered applications.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Do you use any of the following vector databases for LLM-powered applications?"
          data-labels='["No vector databases", "Elasticsearch", "Chroma", "Pinecone"]'
          data-values='[58.9, 21.0, 15.6, 11.6]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Elasticsearch and Chroma lead among vector DBs used.</figcaption>
</figure>


**Usage Statistics:**

-   **Do Not Use:** 58.9%
-   **Elasticsearch:** 21%
-   **Chroma:** 15.6%
-   **Pinecone:** 11.6%
-   **Pgvector:** 8%
-   **Quadrant:** 6.3%
-   **Weaviate:** 2.7%
-   **Milvus:** 1.3%



## Integration Frameworks

More than half of respondents (58%) do not use dedicated frameworks to integrate LLM applications.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Which frameworks or libraries do you use to integrate or orchestrate LLM applications?"
          data-labels='["We don't use LLM integration frameworks", "LangChain", "LlamaIndex"]'
          data-values='[58.1, 33.9, 16.7]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>LangChain is the most common LLM integration tool.</figcaption>
</figure>


Among those who do:

-   **LangChain:** The most popular integration library (34.1%).
-   **LlamaIndex:** Used by 16.8%.
-   Smaller communities use AutoGen, Haystack, or alternatives.



The data indicates that while frameworks like LangChain are becoming popular, many organizations still rely on ad hoc or custom-built solutions to integrate LLM capabilities into their workflows. The evolution of standardized integration tools could simplify deployment and maintenance, facilitating broader adoption.

#### Observability Tools

73.5% of respondents do not track performance with dedicated observability solutions.

<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="Do you use any tools to monitor and observe LLM usage, performance, or quality?"
          data-labels='["No observability/monitoring", "Weights & Biases (W&B)", "LangSmith", "Evidently AI"]'
          data-values='[73.6, 12.0, 9.7, 5.6]'
          data-height="300px"
          data-width="600px">
  </canvas>
  <figcaption>Most do not currently use observability tools for LLMs.</figcaption>
</figure>

Among those who do, use the following tools: 

-   **Weights & Biases:** 12.1%
-   **LangSmith:** 9.8%


The low usage of observability tools suggests that performance monitoring for LLMs is still in its early stages. As these models become more critical to operational processes, improved monitoring and analytics will likely be essential to ensure reliability and optimize system performance.


### Primary Use Cases for LLMs

Respondents employ LLMs across a range of applications. The most common use cases include:

-   Question-answering on internal knowledge bases: 58.1%
-   Code generation: 62.1%
-   Document summarization/extraction: 55.1%
-   Customer support automation (e.g., chatbots): 25.6%
-   Data annotation: 17.2%
-   Agentic interactions (e.g., API connections): 12.8%
-   Autonomous agents for task completion: 14.3%
-   Content moderation/quality control: 9.9%
-   Content generation (articles, blogs, social media): 31.5%


<figure>
  <canvas class="ai-chart"
          data-type="bar"
          data-orientation="horizontal"
          data-title="For which use cases do you currently employ LLMs?"
          data-labels='["Code generation", "Question-answering on internal knowledge", "Document summarization / classification", "Content generation", "Customer support automation", "Data annotation", "Autonomous agents", "Agentic interactions", "Content moderation / quality control"]'
          data-values='[62.1, 58.1, 55.2, 31.5, 25.6, 17.2, 14.3, 12.8, 9.9]'
          data-height="450px"
          data-width="700px">
  </canvas>
  <figcaption>Code generation and Q&A are top LLM use cases.</figcaption>
</figure>


The most common applications, such as code generation, question-answering, and document summarization, highlight the focus on internal process efficiency and productivity. Although customer-facing applications like chatbots and content generation have lower adoption rates, these areas present significant growth opportunities as organizations refine their LLM implementations.

## Production Deployment and Organizational Focus

<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="How many LLM-based systems do you currently have in production?"
          data-labels='["0", "1", "2–5", "5+"]'
          data-values='[54.3, 27.4, 16.1, 2.2]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Most respondents currently have no LLM systems in production.</figcaption>
</figure>


When asked about production systems:

-   54.3% have no LLM-based systems live.
-   27.4% report one live system.
-   16.1% have between 2-5 live systems, with very few exceeding this range.



<figure>
  <canvas class="ai-chart"
          data-type="pie"
          data-title="Do you have a dedicated GenAI/LLM team in your organization?"
          data-labels='["No", "Yes"]'
          data-values='[75.7, 24.3]'
          data-height="300px"
          data-width="400px">
  </canvas>
  <figcaption>Most organizations do not yet have a dedicated GenAI team.</figcaption>
</figure>

We also asked whether organizations have dedicated GenAI/LLM teams.

-   75.7% reported they do not have a dedicated team
-   Only 24.3% have a special team

These results indicate that while experimentation with LLMs is widespread, a majority of organizations have not yet transitioned to full-scale production deployments. The limited presence of dedicated teams suggests that LLM initiatives are still integrated into broader technology projects rather than being standalone strategic units. This points to an opportunity for organizations to develop specialized expertise as LLM applications become more central to their operations.

## Challenges and Future Opportunities

- **Integration and interoperability:** The varied landscape of managed and self-hosted solutions makes seamless integration a challenge. There is an opportunity for vendors to offer more unified and user-friendly platforms that can easily connect with existing systems.
- **Customization and quality assurance:** While many organizations engage in some form of model customization, extensive fine-tuning is still rare. As LLMs play a larger role in mission-critical applications, ensuring consistent performance and quality through more advanced fine-tuning techniques will become increasingly important.
- **Production readiness:** The high proportion of organizations with no live production systems reflects the current experimental phase of LLM adoption. As organizations gain confidence in these systems, the focus is expected to shift toward scalable, production-ready deployments and robust monitoring.

## Conclusion

The survey reveals a clear dominance of managed LLM services and highlights a growing interest in self-hosted, open-source options.

Key conclusions include:

1. **Dominance of managed services:** With over 70% reliance on platforms like OpenAI, managed services are currently the go-to solution for many organizations, likely due to their ease of integration and proven reliability.
2. **Exploration beyond convenience:** Although managed services prevail, a significant minority is experimenting with self-hosted solutions to obtain greater control and potentially reduce costs.
3. **Customization without extensive fine-tuning:** While half of the respondents customize their models, extensive fine-tuning remains relatively niche. This suggests that for many, the balance between convenience and the need for optimal configurations is still being evaluated.
4. **Cloud-centric infrastructure:** The preference for cloud-based GPUs over dedicated hardware underlines the trend toward scalable, cost-effective computing solutions.
5. **Emerging integration and monitoring tools:** With considerable room for improvement in integration frameworks and observability tools, future developments in these areas could simplify the transition from experimental setups to robust production systems.