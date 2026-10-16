---
type: Capability
id: training-dataset-management
title: Training and evaluation dataset management
description: Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.
aliases: [ML datasets, evaluation datasets, golden datasets, datasheets for datasets, data cards]
broader: [machine-learning]
related: [data-labelling, genai-evaluation, data-usage-rights, model-lineage, unstructured-lineage]
depends_on: [data-versioning]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A training or evaluation dataset is kept as a named, versioned object rather than a query someone reruns. Each version records its sources and their table versions, the time window and filters, the label version, the split into training, validation and test data, and a short datasheet stating purpose, known gaps and permitted uses. For example, a credit model's development sample is frozen as version 3: applications from 2022 to 2024, bureau data as at each application date, exclusions listed and a test set nobody trains on. A generative AI evaluation set works the same way, with owned questions and reference answers.

It matters wherever results must be reproduced or defended. Validators rebuild a model from the exact sample, regulators ask how training and test data were chosen and checked for bias, and licence or consent limits must follow data into each model. Data versioning supplies the snapshots underneath; this capability adds composition, documentation and links to the models trained or evaluated on each version.

# Key considerations

- Freeze test sets and control who can read them. Test data that leaks into training or into prompt examples makes every later evaluation look better than it is.
- Store composition as metadata linked to lineage, not only as files. Questions such as which models used a licensed source should be answerable by a query.
- Check consent, licence and classification when the dataset is assembled, and attach the restrictions to the dataset so they reach every model trained on it.
- Evaluation sets go stale as products and questions change. Give each one an owner and a refresh rule, and add production failures to it.
- Plan for erasure. If a person's data must be removed, you need to know which dataset versions and models it reached.

# Questions to ask

- Could you reproduce the exact training and test data for a model released last year?
- Do regulators, validators or customers ask how training data was selected and checked for bias?
- Who owns the evaluation set for each generative AI application, and when was it last refreshed?
- Can you list every model trained on a given source dataset?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Data labelling](data-labelling.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Model lineage](../metadata/model-lineage.md) |
| Depends on | [Data versioning](../storage/data-versioning.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (benefits from) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance; Article 11 and Annex IV – Technical documentation; Article 17 – Quality management system; Article 53 – Obligations of general-purpose AI model providers · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): ML metadata management · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO/CD TR 8000-320 – AI training data quality (in development) · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.4 – Resources for AI systems; Annex A.7 – Data for AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MEASURE 1 – Methods and metrics

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Feature Store](../../technologies/snowflake/snowflake-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../../technologies/databricks/databricks-agent-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [Langfuse](../../technologies/clickhouse/clickhouse-langfuse.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DVC (Data Version Control)](../../technologies/open-source/dvc.md), [MLflow](../../technologies/open-source/mlflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Braintrust](../../technologies/independent/braintrust.md), [Labelbox](../../technologies/independent/labelbox.md), [LangSmith](../../technologies/independent/langsmith.md), [Scale Data Engine](../../technologies/independent/scale-data-engine.md), [Snorkel AI](../../technologies/independent/snorkel-ai.md), [Weights & Biases](../../technologies/independent/weights-and-biases.md) |
