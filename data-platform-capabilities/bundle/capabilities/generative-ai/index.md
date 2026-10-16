# Generative AI

* [Generative AI](generative-ai.md) - Build applications that use large language models and other generative models with enterprise data.
  * [AI agents](ai-agents.md) - Build systems in which models plan, call tools and act over several steps to complete a task.
    * [Agent and tool registry](agent-registry.md) - Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled.
    * [Agent hosting and runtime](agent-runtime.md) - Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
    * [Agent identity and authorisation](agent-identity.md) - Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.
    * [Agent memory](agent-memory.md) - Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
    * [Agent tool and data access](agent-tool-access.md) - Give agents governed access to data and actions through tools and protocols such as MCP.
    * [Agent-to-agent interoperability](agent-interoperability.md) - Let agents built on different platforms discover, delegate to and call each other through open protocols.
  * [AI content marking and provenance](ai-content-provenance.md) - Mark AI-generated content in machine-readable form and detect such marks so synthetic content can be identified.
  * [AI guardrails](ai-guardrails.md) - Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
  * [Enterprise AI assistant](enterprise-ai-assistant.md) - Give staff a governed, ready-made assistant that answers questions and completes tasks across structured and unstructured enterprise data.
  * [Foundation model access](foundation-model-access.md) - Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
    * [AI gateway](ai-gateway.md) - Route, secure, rate-limit and track model calls across providers from one place.
  * [Generative AI evaluation](genai-evaluation.md) - Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
    * [AI red teaming](ai-red-teaming.md) - Probe models and agents adversarially for prompt injection, jailbreaks and unsafe behaviour before and after release.
  * [Generative AI observability](genai-observability.md) - Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
  * [Model customisation](model-customisation.md) - Adapt foundation models to a domain through fine-tuning, distillation or further training.
  * [Prompt management](prompt-management.md) - Version, test and reuse prompts and model configurations.
  * [Retrieval-augmented generation](retrieval-augmented-generation.md) - Ground model answers in your own content by retrieving relevant passages at query time.
    * [Permission-aware retrieval](permission-aware-retrieval.md) - Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.
    * [Retrieval pipelines](retrieval-pipelines.md) - Parse, chunk, embed and index content, and keep indexes in step as sources change.
  * [Vector search](vector-search.md) - Store embeddings and find the most similar items quickly.
    * [Embedding generation](embedding-generation.md) - Turn text, images or other content into vector embeddings for search and retrieval.

# Also part of this domain

* [AI context layer](../metadata/ai-context-layer.md) (main home: Metadata and discovery) - Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
* [AI functions in SQL](../processing/ai-functions.md) (main home: Processing and transformation) - Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
* [AI usage and spend controls](../platform-operations/ai-spend-controls.md) (main home: Platform operations) - Limit, prioritise and attribute model and agent consumption per user, team or application.
* [Conversational analytics](../analytics-bi/conversational-analytics.md) (main home: Analytics and BI) - Ask questions of data in natural language and get answers, charts or SQL back.
* [Data engineering agents](../development-lifecycle/data-engineering-agents.md) (main home: Development and DataOps) - Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
* [Generative model serving](../mlops/generative-model-serving.md) (main home: ML operations) - Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
* [Human oversight of AI](../governance/human-oversight.md) (main home: Governance and compliance) - Route model and agent decisions to people for review, approval or override, and let them pause or stop a system.
* [Model release strategies](../mlops/model-release-strategies.md) (main home: ML operations) - Reduce release risk by exposing new models, prompts or agent versions gradually, or running them in parallel with the current version.
