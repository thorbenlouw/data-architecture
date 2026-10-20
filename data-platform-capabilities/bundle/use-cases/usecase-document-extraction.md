---
type: Use Case
id: usecase-document-extraction
title: Document data extraction
description: Extract fields and tables from invoices, claims, contracts and forms into business systems, with people reviewing uncertain results.
requires:
- capability: unstructured-ingestion
  level: 3
  why: Documents arrive from mailboxes, portals, scanners and repositories and must be captured once each, with their metadata.
- {capability: document-processing, level: 3, why: 'Layout, tables, stamps and handwriting must be read accurately from scans and PDFs.'}
- {capability: foundation-model-access, level: 3, why: Approved multimodal models extract fields into a fixed schema inside the security boundary.}
- capability: genai-evaluation
  level: 3
  why: Field-level accuracy is measured per document type on labelled examples before release and after every model or prompt change.
- {capability: data-labelling, level: 2, why: 'Labelled documents per type are needed for evaluation, and reviewer corrections become new labels.'}
- {capability: human-oversight, level: 3, why: 'Low-confidence or high-value fields wait in a review queue, and every correction is recorded.'}
- {capability: data-quality-rules, level: 3, why: 'Extracted values are checked: line items sum to the total, dates are valid and the supplier or policy exists.'}
- {capability: application-integration, level: 2, why: Validated results are posted to finance or claims systems to be acted on.}
- capability: unstructured-lineage
  level: 2
  why: Each extracted value links to its document, page and region, and to the model and prompt version that produced it.
- {capability: ai-guardrails, level: 2, why: Instructions hidden in a document must not change the extraction or trigger actions.}
- {capability: genai-observability, level: 2, why: 'Per-document traces show confidence, latency and cost, and where failures occur.'}
benefits_from:
- {capability: ai-functions, why: Runs extraction as SQL or DataFrame functions over document tables in bulk.}
- {capability: model-customisation, why: A small tuned or distilled model cuts cost per page at high volume.}
- {capability: shadow-deployment, why: Runs a new model version on live documents and compares its fields with the current one before switching.}
- {capability: training-dataset-management, why: Keeps the labelled evaluation set for each document type versioned and owned.}
- {capability: entity-resolution, why: Matches extracted supplier or customer names to existing records.}
- {capability: event-driven-triggering, why: Processes each document as soon as it arrives.}
- {capability: deidentification, why: Masks personal data before it reaches reviewers or external models where policy requires.}
- {capability: ai-spend-controls, why: Caps model cost per document and per month.}
personas: [persona-ai-engineer, persona-data-engineer, persona-business-user, persona-software-engineer]
patterns: [medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Invoices, claims, delivery notes, contracts and application forms still arrive as PDFs, scans and email attachments, and staff retype their contents into business systems. Document extraction reads each document, identifies its type and pulls out the fields and tables a process needs, such as supplier, invoice number, line items and total, into a fixed schema. Layout-aware parsing and multimodal language models do most of the work, validation rules check the results, and fields the system is unsure about go to a person before anything is posted to the finance or claims system.

Good looks like most documents processed without anyone touching them, accuracy measured per field and per document type against labelled examples, every extracted value traceable to the page and region it came from, and reviewer corrections fed back as labels. New layouts and model version changes are caught by evaluation before they reach payments, and the cost per page is known.

# Non-functional requirements

- Accuracy targets are set per field and document type, for example 99 per cent for amounts and dates.
- Most documents are processed within minutes of arrival, including at month-end peaks.
- Items in the review queue are handled within an agreed time so payment and claim deadlines are met.
- Every extracted value can be traced to its source page and region.
- Cost per page is measured and kept within budget.

# Risks

- Plausible but wrong amounts or dates pass validation and reach payments.
- A supplier changes its invoice layout and accuracy falls without anyone noticing.
- Instructions hidden in a document alter the extraction.
- Reviewers accept suggestions without checking, so errors are recorded as correct labels.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Documents arrive from mailboxes, portals, scanners and repositories and must be captured once each, with their metadata. |
| [Document processing](../capabilities/processing/document-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | Layout, tables, stamps and handwriting must be read accurately from scans and PDFs. |
| [Foundation model access](../capabilities/generative-ai/foundation-model-access.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Approved multimodal models extract fields into a fixed schema inside the security boundary. |
| [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 3 (Defined) | Field-level accuracy is measured per document type on labelled examples before release and after every model or prompt change. |
| [Data labelling](../capabilities/machine-learning/data-labelling.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Labelled documents per type are needed for evaluation, and reviewer corrections become new labels. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Low-confidence or high-value fields wait in a review queue, and every correction is recorded. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Extracted values are checked: line items sum to the total, dates are valid and the supplier or policy exists. |
| [Application integration](../capabilities/ingestion-integration/application-integration.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Validated results are posted to finance or claims systems to be acted on. |
| [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Each extracted value links to its document, page and region, and to the model and prompt version that produced it. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Instructions hidden in a document must not change the extraction or trigger actions. |
| [Generative AI observability](../capabilities/generative-ai/genai-observability.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Per-document traces show confidence, latency and cost, and where failures occur. |

# Capabilities that help

| Capability | Why |
|---|---|
| [AI functions in SQL](../capabilities/processing/ai-functions.md) | Runs extraction as SQL or DataFrame functions over document tables in bulk. |
| [Model customisation](../capabilities/generative-ai/model-customisation.md) | A small tuned or distilled model cuts cost per page at high volume. |
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | Runs a new model version on live documents and compares its fields with the current one before switching. |
| [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) | Keeps the labelled evaluation set for each document type versioned and owned. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | Matches extracted supplier or customer names to existing records. |
| [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md) | Processes each document as soon as it arrives. |
| [De-identification](../capabilities/governance/deidentification.md) | Masks personal data before it reaches reviewers or external models where policy requires. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | Caps model cost per document and per month. |

# Personas

- [AI engineer](../personas/persona-ai-engineer.md): Builds applications and agents on foundation models and enterprise data.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.

# Patterns

- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 8 of 11 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 9 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 9 of 11 | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 8 of 11 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 11 | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 2 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) |
| [Informatica](../platforms/platform-informatica.md) | 2 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 1 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Oracle](../platforms/platform-oracle.md) | 2 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [SAP](../platforms/platform-sap.md) | 5 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../platforms/platform-teradata.md) | 0 of 11 (+3 in preview) | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Document processing](../capabilities/processing/document-processing.md), [Foundation model access](../capabilities/generative-ai/foundation-model-access.md), [Generative AI evaluation](../capabilities/generative-ai/genai-evaluation.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) (preview only), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) (preview only), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 7 of 11 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Palantir](../platforms/platform-palantir.md) | 6 of 11 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [SAS](../platforms/platform-sas.md) | 3 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [AI guardrails](../capabilities/generative-ai/ai-guardrails.md), [Generative AI observability](../capabilities/generative-ai/genai-observability.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 8 of 11 | [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 8 of 11 | [Data labelling](../capabilities/machine-learning/data-labelling.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
| [Independent vendors](../platforms/platform-independent.md) | 10 of 11 | [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) |
