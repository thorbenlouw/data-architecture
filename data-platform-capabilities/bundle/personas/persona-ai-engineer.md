---
type: Persona
id: persona-ai-engineer
title: AI engineer
description: Builds applications and agents on foundation models and enterprise data.
cares_about:
- retrieval-augmented-generation
- genai-evaluation
- retrieval-pipelines
- permission-aware-retrieval
- foundation-model-access
- vector-search
- genai-observability
- ai-guardrails
- agent-tool-access
- agent-identity
- ai-gateway
- prompt-management
- agent-runtime
- ai-context-layer
- document-processing
- embedding-generation
- model-release-strategies
- training-dataset-management
- unstructured-lineage
- ai-red-teaming
- human-oversight
- agent-registry
- agent-memory
- ai-spend-controls
- unstructured-data-quality
- model-customisation
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI engineers are often software engineers who have moved into building with foundation models. They build knowledge assistants, document extraction, conversational analytics and agents that act in business systems. Their time goes on retrieval, prompts, tool integrations, evaluation and guardrails rather than on training models, and they work closely with security, data and platform teams because their applications touch all three.

Success is an assistant or agent whose answers are accurate and grounded in the right sources, that respects each user's permissions, costs a predictable amount per request, and can be changed without regressions because an evaluation suite stands behind it.

# Goals

- Ground answers in current enterprise content and data that the user is allowed to see.
- Measure quality and safety before and after every change.
- Keep latency and cost per request within budget.
- Give agents only the access they need, with a trace of everything they did.

# Jobs

- Build and maintain retrieval pipelines that parse, chunk, embed and index content.
- Write and version prompts and agent tool definitions.
- Connect agents to data and business systems through tools and MCP servers.
- Build evaluation sets, run evaluations and review traces of failures.
- Add guardrails against prompt injection, data leakage and harmful output.
- Choose and route between models on quality, latency and cost.
- Release new prompts, models and agent versions gradually, comparing them with the current version on live traffic.
- Move applications to new model versions before providers retire the old ones, rerunning evaluations and adjusting prompts.
- Register agents, tools and MCP servers and keep their owners, scopes and approvals current.

# Pain points

- Answer quality degrades without warning as documents, prompts or models change.
- Source system permissions are hard to carry into a retrieval index.
- Policy on which models and which data may be used is unclear or slow to obtain.
- Costs and provider rate limits are hard to predict.
- Agents need access to systems that were never designed for machine callers.
- Provider model retirements force rework on the provider's timetable.
- Evaluation sets go stale because nobody owns them.

# Questions they ask

- Which data and documents may the assistant use, and how do we honour the permissions on them?
- How do agents authenticate and act on behalf of a named user?
- How much evaluation is enough before we release, and who signs it off?
- Which model providers are approved, and through which gateway must calls go?
- How do we give agents correct business definitions for structured data?
- How do we roll out a new model or prompt to a share of users and roll it back if quality drops?
- Which documents fed this answer, and how do we remove a document from every index, cache and memory?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Ground model answers in your own content by retrieving relevant passages at query time. |
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges. |
| [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Parse, chunk, embed and index content, and keep indexes in step as sources change. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open. |
| [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Use hosted large language and multimodal models through managed APIs inside the platform's security boundary. |
| [Vector search](../capabilities/generative-ai/vector-search.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Store embeddings and find the most similar items quickly. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Trace model and agent calls with their prompts, responses, latency, cost and user feedback. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions. |
| [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Give agents governed access to data and actions through tools and protocols such as MCP. |
| [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time. |
| [AI gateway](../capabilities/generative-ai/ai-gateway.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Route, secure, rate-limit and track model calls across providers from one place. |
| [Prompt management](../capabilities/generative-ai/prompt-management.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Version, test and reuse prompts and model configurations. |
| [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly. |
| [Document processing](../capabilities/processing/document-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | Extract text, tables and fields from documents such as PDFs, scans and images. |
| [Embedding generation](../capabilities/generative-ai/embedding-generation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Turn text, images or other content into vector embeddings for search and retrieval. |
| [Model release strategies](../capabilities/mlops/model-release-strategies.md) | [ML operations](../capabilities/mlops/mlops.md) | Reduce release risk by exposing new models, prompts or agent versions gradually, or running them in parallel with the current version. |
| [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI. |
| [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track which documents and chunks fed indexes, models and AI-generated answers. |
| [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Probe models and agents adversarially for prompt injection, jailbreaks and unsafe behaviour before and after release. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | Route model and agent decisions to people for review, approval or override, and let them pause or stop a system. |
| [Agent and tool registry](../capabilities/generative-ai/agent-registry.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Keep a governed inventory of agents, tools and MCP servers with owners and permissions so they can be found, approved and controlled. |
| [Agent memory](../capabilities/generative-ai/agent-memory.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Store and recall conversation state and long-term facts for agents across sessions, with retention controls. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Limit, prioritise and attribute model and agent consumption per user, team or application. |
| [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Assess document collections for duplication, staleness, sensitive content and fitness for retrieval or training. |
| [Model customisation](../capabilities/generative-ai/model-customisation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Adapt foundation models to a domain through fine-tuning, distillation or further training. |

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md): Business users ask questions of governed data in plain language and get trustworthy answers.
- [Document data extraction](../use-cases/usecase-document-extraction.md): Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.

# Frameworks they work with

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.
