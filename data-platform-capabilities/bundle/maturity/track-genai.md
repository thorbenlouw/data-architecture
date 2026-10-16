---
type: Maturity Track
id: track-genai
title: Generative AI
description: How safely and reliably the organisation builds, evaluates and runs applications that use language models and agents with its own data.
covers:
- generative-ai
- foundation-model-access
- ai-gateway
- vector-search
- embedding-generation
- retrieval-augmented-generation
- retrieval-pipelines
- permission-aware-retrieval
- ai-agents
- agent-tool-access
- agent-runtime
- agent-memory
- agent-registry
- agent-identity
- agent-interoperability
- human-oversight
- model-customisation
- prompt-management
- genai-evaluation
- ai-red-teaming
- genai-observability
- ai-guardrails
- enterprise-ai-assistant
- ai-content-provenance
- ai-functions
- conversational-analytics
- data-engineering-agents
- model-release-strategies
- generative-model-serving
related_tracks: [track-ai-governance, track-mlops, track-metadata-catalogue, track-specialised-data]
levels:
- level: 1
  name: Initial
  summary: Staff experiment with public or personal AI tools and prototypes outside the platform.
  criteria:
  - Teams call model APIs with personal or project keys, and nobody holds a list of which applications use which models.
  - Company documents are pasted or uploaded into tools that have no data processing agreement.
  - Prototype chatbots answer from a one-off copy of documents that is never refreshed.
  - Prompt text sits in application code and changes without review.
  capabilities: []
- level: 2
  name: Managed
  summary: Approved models are reached through managed access, and a few teams run retrieval-based applications.
  criteria:
  - Model calls go to approved endpoints under the organisation's cloud or contract terms, with keys held in a secrets store.
  - At least one application indexes internal content as embeddings in a vector store and cites its sources in answers.
  - Prompts and model settings are versioned alongside application code.
  - Each application logs prompts, responses, latency and token use.
  - Staff have a sanctioned enterprise assistant, and policy restricts the use of unsanctioned tools.
  capabilities:
  - foundation-model-access
  - vector-search
  - embedding-generation
  - retrieval-augmented-generation
  - prompt-management
  - genai-observability
  - enterprise-ai-assistant
- level: 3
  name: Defined
  summary: Applications are built on shared platform components with standard access, retrieval, guardrails and evaluation.
  criteria:
  - All model calls, including those from SQL functions and natural-language query tools, pass through a gateway that enforces authentication, rate limits, routing and logging.
  - Retrieval indexes update when source content changes and filter results by each user's permissions in the source system.
  - Input and output guardrails for prompt injection, sensitive data and harmful content are on by default for every application.
  - Every application has an evaluation set, and a release is blocked if accuracy, groundedness or safety scores fall below agreed thresholds.
  - Agents reach data and actions only through tools and MCP servers listed in a registry with owners and permissions, never through embedded credentials.
  capabilities:
  - ai-gateway
  - retrieval-pipelines
  - permission-aware-retrieval
  - ai-guardrails
  - genai-evaluation
  - ai-agents
  - agent-tool-access
  - agent-registry
  - ai-functions
  - conversational-analytics
- level: 4
  name: Measured
  summary: Agents run with their own identities on managed infrastructure, new versions are released gradually, and quality, safety and cost are measured against targets.
  criteria:
  - Each agent has its own identity and acts for a named user with scoped, short-lived permissions checked at request time.
  - Agents run on a managed runtime with durable state, sandboxed code execution and retention rules for stored memory.
  - Quality, groundedness and safety scores from sampled production traffic, and user feedback, are tracked against targets, and new model, prompt and agent versions reach a share of traffic first and roll back automatically on evaluator or feedback thresholds.
  - Red-team tests for prompt injection and jailbreaks run before release and on a schedule, with findings tracked to closure.
  - High-impact agent actions wait in a review queue for human approval, operators can pause any agent, and image, audio and video generators mark outputs with an open provenance standard such as C2PA.
  capabilities:
  - agent-identity
  - agent-runtime
  - agent-memory
  - ai-red-teaming
  - human-oversight
  - ai-content-provenance
  - model-release-strategies
- level: 5
  name: Optimising
  summary: Model choice, evaluation sets and agent behaviour improve continuously from production evidence.
  criteria:
  - Model choice per task is reviewed from evaluation and cost data, and traffic moves to smaller, fine-tuned or self-hosted open-weight models where they score the same, with their token throughput, latency and cost per request measured.
  - Failed or poorly rated production interactions are added to evaluation sets automatically.
  - Agents on different platforms delegate to each other through open protocols, with calls traced end to end.
  - Failed and refused agent tool calls, including those from data engineering agents that build pipelines, are analysed weekly, and tool descriptions, permissions or prompts are changed as a result.
  capabilities: [model-customisation, agent-interoperability, data-engineering-agents, generative-model-serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up takes generative AI from scattered prototypes calling public APIs with copied documents to governed applications that retrieve only what each user may see, are evaluated before every release, and are traced and costed in production. No external maturity model for generative AI applications is as widely cited as the MLOps models, so the levels use the shared scale, and the evaluation, guardrail and observability criteria draw on the risks listed in NIST's Generative AI Profile (NIST AI 600-1). Typical blockers are unclear rules on which data may go to which model, no evaluation sets to show whether a change helped, and agents given broad service credentials because per-user authorisation is hard to build.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Staff experiment with public or personal AI tools and prototypes outside the platform.

- Teams call model APIs with personal or project keys, and nobody holds a list of which applications use which models.
- Company documents are pasted or uploaded into tools that have no data processing agreement.
- Prototype chatbots answer from a one-off copy of documents that is never refreshed.
- Prompt text sits in application code and changes without review.

## Level 2: Managed

Approved models are reached through managed access, and a few teams run retrieval-based applications.

- Model calls go to approved endpoints under the organisation's cloud or contract terms, with keys held in a secrets store.
- At least one application indexes internal content as embeddings in a vector store and cites its sources in answers.
- Prompts and model settings are versioned alongside application code.
- Each application logs prompts, responses, latency and token use.
- Staff have a sanctioned enterprise assistant, and policy restricts the use of unsanctioned tools.

**Capabilities first relied on:** [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md)

## Level 3: Defined

Applications are built on shared platform components with standard access, retrieval, guardrails and evaluation.

- All model calls, including those from SQL functions and natural-language query tools, pass through a gateway that enforces authentication, rate limits, routing and logging.
- Retrieval indexes update when source content changes and filter results by each user's permissions in the source system.
- Input and output guardrails for prompt injection, sensitive data and harmful content are on by default for every application.
- Every application has an evaluation set, and a release is blocked if accuracy, groundedness or safety scores fall below agreed thresholds.
- Agents reach data and actions only through tools and MCP servers listed in a registry with owners and permissions, never through embedded credentials.

**Capabilities first relied on:** [AI gateway](../capabilities/generative-ai/ai-gateway.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [AI agents](../capabilities/generative-ai/ai-agents.md), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [AI functions in SQL](../capabilities/processing/ai-functions.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md)

## Level 4: Measured

Agents run with their own identities on managed infrastructure, new versions are released gradually, and quality, safety and cost are measured against targets.

- Each agent has its own identity and acts for a named user with scoped, short-lived permissions checked at request time.
- Agents run on a managed runtime with durable state, sandboxed code execution and retention rules for stored memory.
- Quality, groundedness and safety scores from sampled production traffic, and user feedback, are tracked against targets, and new model, prompt and agent versions reach a share of traffic first and roll back automatically on evaluator or feedback thresholds.
- Red-team tests for prompt injection and jailbreaks run before release and on a schedule, with findings tracked to closure.
- High-impact agent actions wait in a review queue for human approval, operators can pause any agent, and image, audio and video generators mark outputs with an open provenance standard such as C2PA.

**Capabilities first relied on:** [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md)

## Level 5: Optimising

Model choice, evaluation sets and agent behaviour improve continuously from production evidence.

- Model choice per task is reviewed from evaluation and cost data, and traffic moves to smaller, fine-tuned or self-hosted open-weight models where they score the same, with their token throughput, latency and cost per request measured.
- Failed or poorly rated production interactions are added to evaluation sets automatically.
- Agents on different platforms delegate to each other through open protocols, with calls traced end to end.
- Failed and refused agent tool calls, including those from data engineering agents that build pipelines, are analysed weekly, and tool descriptions, permissions or prompts are changed as a result.

**Capabilities first relied on:** [Model customisation](../capabilities/generative-ai/model-customisation.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md)

# Capabilities in scope

[Generative AI](../capabilities/generative-ai/generative-ai.md), [Agent and tool registry](../capabilities/generative-ai/agent-registry.md), [Agent hosting and runtime](../capabilities/generative-ai/agent-runtime.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Agent memory](../capabilities/generative-ai/agent-memory.md), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md), [Agent-to-agent interoperability](../capabilities/generative-ai/agent-interoperability.md), [AI agents](../capabilities/generative-ai/ai-agents.md), [AI content marking and provenance](../capabilities/generative-ai/ai-content-provenance.md), [AI functions in SQL](../capabilities/processing/ai-functions.md), [AI gateway](../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Data engineering agents](../capabilities/development-lifecycle/data-engineering-agents.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [Generative model serving](../capabilities/mlops/generative-model-serving.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model customisation](../capabilities/generative-ai/model-customisation.md), [Model release strategies](../capabilities/mlops/model-release-strategies.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../capabilities/generative-ai/retrieval-augmented-generation.md), [Vector search](../capabilities/generative-ai/vector-search.md)

# Related tracks

- [AI and model governance](track-ai-governance.md): How well the organisation knows its AI systems, assesses their risks and impacts, controls their behaviour and evidences this to regulators and customers.
- [MLOps](track-mlops.md): How automatically and safely models are released, run, monitored and improved in production.
- [Metadata and catalogue](track-metadata-catalogue.md): How completely and accurately data assets are described, findable and connected through metadata, for people and for machines.
- [Specialised data](track-specialised-data.md): How well the organisation stores, governs and analyses data that needs specialised types, indexes or engines, such as time series, location, graphs, searchable text, media, logs and bitemporal history.

Levels follow the shared [maturity scale](maturity-scale.md).
