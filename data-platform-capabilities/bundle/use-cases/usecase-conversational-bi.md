---
type: Use Case
id: usecase-conversational-bi
title: Conversational analytics for business users
description: Business users ask questions of governed data in plain language and get trustworthy answers.
aliases: [talk to your data, natural language BI]
requires:
- {capability: conversational-analytics, level: 3, why: Questions in plain language are turned into queries and answers within the governed environment.}
- {capability: semantic-layer, level: 3, why: 'The model must query business entities and measures, not guess joins across raw tables.'}
- {capability: metric-definitions, level: 3, why: Answers must use the same certified KPI logic as the dashboards.}
- {capability: ai-context-layer, level: 3, why: 'Synonyms, verified queries and usage notes steer the model to correct queries.'}
- {capability: business-glossary, level: 2, why: Business terms in questions must map to defined concepts.}
- {capability: foundation-model-access, level: 2, why: An approved model interprets questions and writes queries inside the security boundary.}
- {capability: identity-authentication, level: 3, why: 'Generated queries must run as the asking user, not a shared service account.'}
- {capability: row-level-security, level: 3, why: 'Users must get only the rows they are entitled to, however they phrase a question.'}
- {capability: column-masking, level: 3, why: Sensitive fields stay hidden even if a question asks for them.}
- {capability: data-certification, level: 2, why: Only certified datasets are exposed to conversational queries.}
- {capability: genai-evaluation, level: 3, why: A benchmark of real questions with known answers decides whether a domain is ready for users.}
- {capability: genai-observability, level: 2, why: Question logs and feedback show where answers fail and which context to add.}
benefits_from:
- {capability: semantic-model-interchange, why: Reuses the BI semantic model in AI tools without redefining it.}
- {capability: workload-management, why: Limits heavy generated queries.}
- {capability: ai-spend-controls, why: Caps model and query spend per user or team.}
- {capability: data-catalogue, why: Provides descriptions that help the model choose the right dataset.}
- {capability: usage-metadata, why: 'Shows which questions people actually ask, to prioritise context work.'}
- {capability: ai-guardrails, why: Blocks requests outside scope and prompt injection.}
- {capability: augmented-analytics, why: Adds automatic explanations of why a figure changed.}
- {capability: data-consumer-portal, why: Puts the assistant alongside the dashboards users already have.}
- {capability: enterprise-ai-assistant, why: Brings data answers into the assistant staff already use.}
- {capability: data-trust-indicators, why: 'Answers show whether the data behind them is current and passing checks, so users can judge them.'}
personas:
- persona-business-user
- persona-data-analyst
- persona-analytics-engineer
- persona-ai-engineer
- persona-data-steward
patterns: [dimensional-modelling, one-big-table, data-marts]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many business users never open a BI tool, and dashboards answer only the questions their designers anticipated. Conversational analytics lets users ask questions such as "how did margin in the north compare with last quarter" and get a number, chart or table back. A language model translates the question into a query over a governed semantic model, guided by curated context such as synonyms, verified example queries and metric definitions, and the query runs with the user's own permissions.

Good looks like answers that match the official dashboards, show which definition and filters were used so users can check them, and stay within curated domains where accuracy has been measured. Each new domain is opened only once it meets an accuracy target on a benchmark of real questions with known answers, and wrong answers feed back into the context.

# Non-functional requirements

- Answers return within about ten seconds for typical questions.
- Each domain meets an agreed accuracy on its benchmark before release, often 90 per cent or higher.
- Every answer shows the definition, filters and source used, and the query for those who want it.
- The same access rules apply as in BI tools.

# Risks

- Plausible but wrong numbers from a misread filter or join erode trust quickly.
- Exposing the whole warehouse instead of curated domains lowers accuracy.
- Context is written once and not maintained as definitions change.
- Expensive generated queries raise compute costs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Questions in plain language are turned into queries and answers within the governed environment. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | The model must query business entities and measures, not guess joins across raw tables. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Answers must use the same certified KPI logic as the dashboards. |
| [AI context layer](../capabilities/metadata/ai-context-layer.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Synonyms, verified queries and usage notes steer the model to correct queries. |
| [Business glossary](../capabilities/metadata/business-glossary.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Business terms in questions must map to defined concepts. |
| [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | An approved model interprets questions and writes queries inside the security boundary. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Generated queries must run as the asking user, not a shared service account. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Users must get only the rows they are entitled to, however they phrase a question. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Sensitive fields stay hidden even if a question asks for them. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Only certified datasets are exposed to conversational queries. |
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | A benchmark of real questions with known answers decides whether a domain is ready for users. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Question logs and feedback show where answers fail and which context to add. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md) | Reuses the BI semantic model in AI tools without redefining it. |
| [Workload management](../capabilities/compute/workload-management.md) | Limits heavy generated queries. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | Caps model and query spend per user or team. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | Provides descriptions that help the model choose the right dataset. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | Shows which questions people actually ask, to prioritise context work. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | Blocks requests outside scope and prompt injection. |
| [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md) | Adds automatic explanations of why a figure changed. |
| [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md) | Puts the assistant alongside the dashboards users already have. |
| [Enterprise AI assistant](../capabilities/generative-ai/enterprise-ai-assistant.md) | Brings data answers into the assistant staff already use. |
| [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) | Answers show whether the data behind them is current and passing checks, so users can judge them. |

# Personas

- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [AI engineer](../personas/persona-ai-engineer.md): Builds applications and agents on foundation models and enterprise data.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.

# Patterns

- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [One big table](../patterns/one-big-table.md)
- [Data marts](../patterns/data-marts.md)

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 9 of 12 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 12 of 12 |  |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 12 | [Data certification](../capabilities/metadata/data-certification.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 12 | [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Databricks](../platforms/platform-databricks.md) | 11 of 12 | [Business glossary](../capabilities/metadata/business-glossary.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 6 of 12 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Informatica](../platforms/platform-informatica.md) | 4 of 12 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 12 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 12 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [SAP](../platforms/platform-sap.md) | 7 of 12 | [Identity and authentication](../capabilities/security/identity-authentication.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../platforms/platform-teradata.md) | 1 of 12 (+3 in preview) | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) (preview only), [AI context layer](../capabilities/metadata/ai-context-layer.md) (preview only), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 6 of 12 | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Row-level security](../capabilities/security/row-level-security.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Palantir](../platforms/platform-palantir.md) | 7 of 12 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Data certification](../capabilities/metadata/data-certification.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 10 of 12 | [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Independent vendors](../platforms/platform-independent.md) | 11 of 12 | [Identity and authentication](../capabilities/security/identity-authentication.md) |
