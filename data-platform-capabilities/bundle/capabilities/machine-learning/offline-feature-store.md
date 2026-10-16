---
type: Capability
id: offline-feature-store
title: Offline feature store
description: Store historical feature values for model training and batch scoring.
broader: [feature-store]
related: [time-travel, open-table-formats, table-catalogue, batch-inference]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The offline store keeps the full history of feature values, each row carrying an entity key and a timestamp for when that value became true or known. It usually lives as tables in the lake or warehouse, often in an open table format, so years of data can be held cheaply. Training sets are built by joining labelled examples, such as customers and whether they churned, to these tables at each example's timestamp. Batch scoring jobs read the same tables to score a whole population.

Training needs history and correctness more than speed. Keeping every value over time, rather than overwriting it, is what makes point-in-time joins and reproducible training sets possible. Some designs store one row per change; others store periodic snapshots, which are simpler to query but use more storage and miss changes between snapshots. The offline store is also the usual source for loading the online store, so both are built from the same computed values.

# Key considerations

- Keep both the time an event happened and the time it was recorded. The gap between them decides what a model could really have known.
- Retention drives cost. Decide how much history models need and whether older values can move to cheaper storage tiers.
- Use the same tables and catalogue as the rest of the platform where possible, so existing access control and lineage apply.

# Questions to ask

- How many years of feature history do models need for training?
- Must you be able to rebuild the exact training set used for a model released last year?
- Will batch scoring read features from these tables or compute them separately?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Feature store](feature-store.md) |
| Related | [Batch inference](../mlops/batch-inference.md), [Open table formats](../storage/open-table-formats.md), [Table catalogue](../storage/table-catalogue.md), [Time travel](../storage/time-travel.md) |
| Needed by | [Point-in-time correct joins](point-in-time-joins.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Feature store

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Feature Store](../../technologies/aws/aws-sagemaker-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning managed feature store](../../technologies/microsoft/azure-ml-managed-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Feature Store](../../technologies/google-cloud/gcp-agent-platform-feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Feature Store](../../technologies/snowflake/snowflake-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Feature Store](../../technologies/databricks/databricks-feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Feast](../../technologies/open-source/feast.md) |
