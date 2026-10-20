---
type: Use Case
id: usecase-rag-assistant
title: Knowledge assistant
description: A generative AI assistant that answers questions from internal documents, with citations.
aliases: [RAG assistant, enterprise search assistant, document Q&A]
requires:
- {capability: unstructured-ingestion, level: 3, why: Documents must be brought in from many repositories with their metadata and access lists.}
- {capability: document-processing, level: 3, why: 'PDFs, scans, slides and tables must be parsed into clean text, or retrieval quality suffers.'}
- {capability: retrieval-pipelines, level: 3, why: 'Indexes must follow source changes, including edits, deletions and permission changes.'}
- {capability: embedding-generation, level: 2, why: Passages and questions are turned into embeddings for semantic matching.}
- {capability: vector-search, level: 3, why: The most relevant passages must be found quickly across millions of chunks.}
- {capability: permission-aware-retrieval, level: 3, why: Answers must never include content the user could not open in the source system.}
- {capability: identity-authentication, level: 3, why: The assistant must know exactly who is asking to apply that person's permissions.}
- {capability: foundation-model-access, level: 3, why: Answers are written by approved models inside the organisation's security boundary.}
- {capability: unstructured-lineage, level: 2, why: 'Each answer must cite the documents and passages it used, and removed documents must leave the index.'}
- {capability: prompt-management, level: 2, why: Prompts change often and must be versioned and tested like code.}
- {capability: genai-evaluation, level: 3, why: 'Accuracy, grounding and citation quality are measured on a test set before each release.'}
- {capability: genai-observability, level: 2, why: Traces and user feedback show which questions fail and why.}
- {capability: ai-guardrails, level: 3, why: 'Inputs and outputs are filtered for prompt injection, sensitive data and harmful content.'}
- {capability: ai-governance, level: 2, why: 'The assistant is registered with an owner, purpose and risk rating, and users are told they are dealing with AI.'}
benefits_from:
- {capability: full-text-search, why: Keyword search alongside vector search finds exact terms such as product codes and clause numbers.}
- {capability: unstructured-data-quality, why: Removing duplicates and stale versions stops the assistant citing outdated policies.}
- {capability: data-classification, why: Keeps restricted document types out of the index entirely.}
- {capability: ai-gateway, why: 'Routes, rate-limits and tracks model calls across providers.'}
- {capability: ai-red-teaming, why: Finds injection and leakage weaknesses before attackers do.}
- {capability: ai-spend-controls, why: Keeps cost per question within budget as use grows.}
- {capability: knowledge-graphs, why: Adds entity relationships to retrieval for questions that span documents.}
- {capability: enterprise-ai-assistant, why: A ready-made assistant may meet the need without building one.}
- {capability: audio-video-processing, why: Brings recorded meetings and training videos into the content.}
- {capability: model-release-strategies, why: 'Compares a new model, prompt or retrieval setting with the current one on live questions before full rollout.'}
- {capability: training-dataset-management, why: 'Keeps the evaluation set versioned, owned and refreshed from real questions and failures.'}
personas:
- persona-ai-engineer
- persona-business-user
- persona-security-officer
- persona-data-steward
- persona-platform-engineer
- persona-data-engineer
patterns: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Staff spend a lot of time searching policies, procedures, product documentation, contracts and past cases spread across many repositories. A knowledge assistant answers questions in plain language from that content and cites the passages it used. Documents are pulled from their sources with their metadata and permissions, parsed, split into passages, turned into embeddings and indexed. At question time the system retrieves the passages most relevant to the question that the user is allowed to see, and a language model writes an answer grounded in them.

Good looks like answers that are correct, cite real and current sources, never reveal content the user could not open in the source system, and say so when the content does not hold the answer. Quality is measured on a maintained test set before every change, and answers improve because poor ones are traced back to the retrieval, parsing or prompt that caused them.

# Non-functional requirements

- First words of the answer appear within about two seconds and the full answer within about ten.
- Document edits reach the index within hours, and permission revocations within an agreed shorter time.
- Every factual answer cites at least one source the user can open.
- Prompts and responses are logged with retention that matches policy and privacy rules.
- Cost per question is measured and kept within budget.

# Risks

- Stale, duplicated or conflicting documents produce confident wrong answers.
- The index falls behind source permissions and reveals restricted content.
- Instructions hidden in documents manipulate the model.
- Adoption fades because answers on real questions are not reliable enough.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Documents must be brought in from many repositories with their metadata and access lists. |
| [Document processing](../capabilities/processing/document-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | PDFs, scans, slides and tables must be parsed into clean text, or retrieval quality suffers. |
| [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Indexes must follow source changes, including edits, deletions and permission changes. |
| [Embedding generation](../capabilities/generative-ai/embedding-generation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Passages and questions are turned into embeddings for semantic matching. |
| [Vector search](../capabilities/generative-ai/vector-search.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | The most relevant passages must be found quickly across millions of chunks. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Answers must never include content the user could not open in the source system. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | The assistant must know exactly who is asking to apply that person's permissions. |
| [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Answers are written by approved models inside the organisation's security boundary. |
| [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Each answer must cite the documents and passages it used, and removed documents must leave the index. |
| [Prompt management](../capabilities/generative-ai/prompt-management.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Prompts change often and must be versioned and tested like code. |
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Accuracy, grounding and citation quality are measured on a test set before each release. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Traces and user feedback show which questions fail and why. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Inputs and outputs are filtered for prompt injection, sensitive data and harmful content. |
| [AI governance](../capabilities/governance/ai-governance.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | The assistant is registered with an owner, purpose and risk rating, and users are told they are dealing with AI. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Full-text search](../capabilities/specialised-data/full-text-search.md) | Keyword search alongside vector search finds exact terms such as product codes and clause numbers. |
| [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md) | Removing duplicates and stale versions stops the assistant citing outdated policies. |
| [Data classification](../capabilities/governance/data-classification.md) | Keeps restricted document types out of the index entirely. |
| [AI gateway](../capabilities/generative-ai/ai-gateway.md) | Routes, rate-limits and tracks model calls across providers. |
| [AI red teaming](../capabilities/generative-ai/ai-red-teaming.md) | Finds injection and leakage weaknesses before attackers do. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | Keeps cost per question within budget as use grows. |
| [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md) | Adds entity relationships to retrieval for questions that span documents. |
| [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md) | A ready-made assistant may meet the need without building one. |
| [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md) | Brings recorded meetings and training videos into the content. |
| [Model release strategies](../capabilities/mlops/model-release-strategies.md) | Compares a new model, prompt or retrieval setting with the current one on live questions before full rollout. |
| [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) | Keeps the evaluation set versioned, owned and refreshed from real questions and failures. |

# Personas

- [AI engineer](../personas/persona-ai-engineer.md): Builds applications and agents on foundation models and enterprise data.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.

# Frameworks that apply

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 13 of 14 | [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 11 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Prompt management](../capabilities/generative-ai/prompt-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 13 of 14 | [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 14 (+1 in preview) | [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI governance](../capabilities/governance/ai-governance.md), [Prompt management](../capabilities/generative-ai/prompt-management.md) (preview only) |
| [Databricks](../platforms/platform-databricks.md) | 12 of 14 | [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 5 of 14 (+1 in preview) | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [AI governance](../capabilities/governance/ai-governance.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md) (preview only) |
| [Informatica](../platforms/platform-informatica.md) | 2 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 1 of 14 (+1 in preview) | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [AI governance](../capabilities/governance/ai-governance.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md) (preview only) |
| [Oracle](../platforms/platform-oracle.md) | 4 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI governance](../capabilities/governance/ai-governance.md) |
| [SAP](../platforms/platform-sap.md) | 6 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../platforms/platform-teradata.md) | 3 of 14 (+3 in preview) | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Prompt management](../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) (preview only), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) (preview only), [AI governance](../capabilities/governance/ai-governance.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 10 of 14 (+1 in preview) | [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md) (preview only) |
| [Palantir](../platforms/platform-palantir.md) | 7 of 14 | [Retrieval pipelines](../capabilities/generative-ai/retrieval-pipelines.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| [SAS](../platforms/platform-sas.md) | 8 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 10 of 14 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 11 of 14 | [Embedding generation](../capabilities/generative-ai/embedding-generation.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Independent vendors](../platforms/platform-independent.md) | 12 of 14 | [Identity and authentication](../capabilities/security/identity-authentication.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
