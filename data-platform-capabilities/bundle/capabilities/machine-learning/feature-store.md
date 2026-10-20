---
type: Capability
id: feature-store
title: Feature store
description: Manage features centrally so they are reused, documented and served consistently for training and inference.
broader: [machine-learning]
related: [data-catalogue, low-latency-serving, model-lineage, data-classification]
depends_on: [feature-engineering]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A feature store holds feature definitions, the pipelines that compute them and the computed values, organised by entity such as customer, device or product. A data scientist browses existing features, builds a training set by naming the features needed and supplying entity keys with timestamps, and deploys a model that fetches the same features by name at prediction time. Most designs have two layers: an offline store with history for training and an online store with the latest values for fast lookup.

The benefits are consistency between training and serving, reuse across models, and training sets that are correct in time. It matters most when several models share features or when models score in real time; for a few batch models, documented feature tables in the warehouse may be enough. Some products compute features themselves, while others only register and serve features computed elsewhere. Unlike a general data catalogue, a feature store understands entities, timestamps and serving, not just metadata.

# Key considerations

- Decide whether the store computes features or only registers and serves them. Computing inside it is quicker to start but ties transformation logic to that product.
- Copying values from offline to online storage adds cost and delay. Publish online only the features that real-time models read.
- Features derived from personal data inherit its classification and access rules, and need lineage back to their sources.
- Reuse depends on documentation and search. A store full of undocumented near-duplicates offers little over plain tables.

# Questions to ask

- How many models share features, and how many of them score in real time?
- Have production problems been traced to features computed differently in training and serving?
- Who will own shared features and keep their pipelines running?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Narrower | [Offline feature store](offline-feature-store.md), [Online feature store](online-feature-store.md), [Point-in-time correct joins](point-in-time-joins.md) |
| Related | [Data catalogue](../metadata/data-catalogue.md), [Data classification](../governance/data-classification.md), [Low-latency serving](../serving/low-latency-serving.md), [Model lineage](../metadata/model-lineage.md) |
| Depends on | [Feature engineering](feature-engineering.md) |

# Where it appears

- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Feature store

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Feature Store](../../technologies/aws/aws-sagemaker-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning managed feature store](../../technologies/microsoft/azure-ml-managed-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Agent Platform Feature Store | [Agent Platform Feature Store](../../technologies/google-cloud/gcp-agent-platform-feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Feature Store](../../technologies/snowflake/snowflake-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Feature Store](../../technologies/databricks/databricks-feature-store.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Feature Store](../../technologies/dataiku/dataiku-feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Feast](../../technologies/open-source/feast.md) |

Narrower capabilities are realised by a further 12 technologies; see their pages.
