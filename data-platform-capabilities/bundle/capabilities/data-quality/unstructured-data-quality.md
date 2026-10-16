---
type: Capability
id: unstructured-data-quality
title: Unstructured data quality
description: Assess document collections for duplication, staleness, sensitive content and fitness for retrieval or training.
aliases: [AI data readiness]
broader: [data-quality, unstructured-data]
related: [retrieval-pipelines, data-classification, unstructured-lineage, genai-evaluation]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical checks find exact and near-duplicate documents, superseded versions that contradict current ones, content past its review date, failed text extraction such as scanned pages with no text, the wrong language, missing owners or metadata, and personal or confidential content that should not be indexed. A policy library might hold five versions of the same travel policy; an assistant that retrieves the oldest gives a wrong answer with confidence.

It matters because AI answers can only be as current and consistent as the content behind them, and document collections rarely have the owners and rules that tables do. Techniques include hashing and embedding similarity to find duplicates, metadata checks, classifiers for sensitive content, and scoring of extraction and readability. Unlike structured data, documents have no fixed schema, so many checks are statistical or model-based rather than exact rules.

# Key considerations

- Clean a collection before indexing it. Removing duplicates and stale versions often improves retrieval more than tuning models.
- Scan for sensitive content before it reaches an index, since retrieval can expose it to anyone who can use the assistant.
- Track document owners and review dates. Without owners, staleness can only be detected, not fixed.
- Model-based checks such as classification and similarity make mistakes. Review a sample before acting on results in bulk.

# Questions to ask

- Which document collections feed AI assistants, search or model training?
- Who owns each collection and keeps it current?
- Have AI answers been wrong because of outdated or duplicate content?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md), [Unstructured data management](../specialised-data/unstructured-data.md) |
| Related | [Data classification](../governance/data-classification.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md) |

# Where it appears

- **Use cases:** [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Unstructured Data Governance](../../technologies/informatica/informatica-unstructured-data-governance.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md) |
