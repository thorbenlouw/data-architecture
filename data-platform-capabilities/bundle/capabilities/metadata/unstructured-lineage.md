---
type: Capability
id: unstructured-lineage
title: Document and unstructured lineage
description: Track which documents and chunks fed indexes, models and AI-generated answers.
aliases: [document lineage]
broader: [data-lineage]
related: [retrieval-pipelines, genai-observability, data-subject-requests, model-lineage, unstructured-data]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This lineage records the chain from source documents to AI outputs: which file and version was parsed, which chunks were created and embedded with which model, which index holds them, which chunks were retrieved for a given answer, and which documents went into a training or fine-tuning set. For example, after a contract is found to contain a legal error, lineage shows which index chunks came from it, which assistant answers in the past month cited it and which fine-tuning dataset included it.

It is needed to remove content reliably after deletion requests or accidental sharing, to explain answers, and to show regulators which data trained a model. It is built by carrying document identifiers and versions through retrieval pipelines as chunk metadata, recording retrieved chunk identifiers in traces, and fixing the composition of each training set. It differs from table lineage because the units are files and chunks, and which chunks reach an answer is decided by search at question time, not by fixed code.

# Key considerations

- Assign stable document identifiers and versions at ingestion. Without them, chunks cannot be traced back to their source.
- Retrieval lineage lives in traces. Keep retrieved chunk identifiers even when full prompt text is not retained.
- Deletion must reach every copy: parsed text, chunks, vectors, caches and agent memories.
- Record training data composition when the model is trained. It cannot be reconstructed reliably afterwards.

# Questions to ask

- Must you be able to remove a document's influence from indexes or models on request?
- Do users or regulators need to know which sources an answer used?
- Which document collections feed AI systems today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md) |
| Related | [AI content marking and provenance](../generative-ai/ai-content-provenance.md), [Data subject requests](../governance/data-subject-requests.md), [Generative AI observability](../generative-ai/genai-observability.md), [Model lineage](model-lineage.md), [Retrieval pipelines](../generative-ai/retrieval-pipelines.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md), [Training and evaluation dataset management](../machine-learning/training-dataset-management.md), [Unstructured data ingestion](../ingestion-integration/unstructured-ingestion.md), [Unstructured data management](../specialised-data/unstructured-data.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 2) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 5, Optimising)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 53 – Obligations of general-purpose AI model providers · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): Generative AI Profile (NIST AI 600-1)

# How platforms provide it

No technology in this bundle realises this capability directly yet.
