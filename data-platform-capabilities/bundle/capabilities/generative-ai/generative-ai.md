---
type: Capability
id: generative-ai
title: Generative AI
description: Build applications that use large language models and other generative models with enterprise data.
aliases: [GenAI, AI engineering, LLMOps]
broader: []
related: [ai-governance, unstructured-data, knowledge-graphs]
depends_on: [access-control]
order: 10
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generative AI on a data platform means connecting models that produce text, code, images or structured output to the organisation's own data and systems. Three groups of capability do most of the work. Model access, through managed endpoints and an AI gateway, decides which models can be called and under what terms. Retrieval (embeddings, vector search, retrieval pipelines and permission-aware filtering) supplies the right content at the moment a question is asked. Agents add tools, a runtime, memory, identity and human oversight so models can take several steps and act.

Around these sits the engineering lifecycle that makes outputs dependable: prompt management, model customisation when prompting is not enough, evaluation and red teaming before release, observability and guardrails in production, and content marking where synthetic output must be identifiable.

Packaged forms such as an enterprise assistant, AI functions in SQL and conversational analytics reuse the same parts. The domain leans heavily on others. Most quality problems are really data problems: finding current content, describing tables so models use them correctly, keeping source permissions intact and attributing cost. That is why metadata, the AI context layer, access control and AI governance matter as much as the choice of model.

# Key considerations

- Most poor answers come from missing or wrong context, not from the model. Invest in content quality, metadata and evaluation before switching models.
- Keep model choice replaceable. Models, prices and terms change every few months, so call them through a gateway or a thin abstraction.
- Agree data-handling terms with each model provider: retention, use for training, abuse monitoring and the region where processing happens.
- Treat prompts, retrieval settings and agent tools as versioned code with tests and releases, not as configuration edited in place.
- Cost grows with tokens and agent steps, not with the number of users. Set budgets and attribution from the first production use case.

# Questions to ask

- Which use cases are in scope: answering questions over documents, analysing data, generating content, or agents that change records?
- What data may be sent to which models, under which contractual and regional terms?
- How will you decide that answers are good enough, and who makes that call?
- Which regulations, such as the EU AI Act or sector rules, apply to the intended uses?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [AI agents](ai-agents.md), [AI content marking and provenance](ai-content-provenance.md), [AI context layer](../metadata/ai-context-layer.md), [AI functions in SQL](../processing/ai-functions.md), [AI guardrails](ai-guardrails.md), [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Enterprise AI assistant](enterprise-ai-assistant.md), [Foundation model access](foundation-model-access.md), [Generative AI evaluation](genai-evaluation.md), [Generative AI observability](genai-observability.md), [Model customisation](model-customisation.md), [Model release strategies](../mlops/model-release-strategies.md), [Prompt management](prompt-management.md), [Retrieval-augmented generation](retrieval-augmented-generation.md), [Vector search](vector-search.md) |
| Related | [Specialised data types](../specialised-data/specialised-data.md), [AI governance](../governance/ai-governance.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Unstructured data management](../specialised-data/unstructured-data.md) |
| Depends on | [Access control](../security/access-control.md) |

# Where it appears

- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 260 technologies; see their pages.
