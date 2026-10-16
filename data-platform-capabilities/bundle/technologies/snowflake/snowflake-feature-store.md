---
type: Technology
id: snowflake-feature-store
title: Snowflake Feature Store
description: Python APIs and objects for defining entities and feature views (as Dynamic Tables or views), generating point-in-time correct training sets and retrieving features for batch inference.
platform: platform-snowflake
kind: feature
availability: ga
realises:
- feature-store
- offline-feature-store
- point-in-time-joins
- feature-engineering
- training-dataset-management
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Training sets can be saved as Snowflake Datasets: versioned, immutable schema-level snapshots (GA since March 2025) that ML lineage links to the feature views and models that use them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development) (primary): Manage features centrally so they are reused, documented and served consistently for training and inference.
- [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md) (Machine learning development): Store historical feature values for model training and batch scoring.
- [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) (Machine learning development): Join features as they were known at each training example's timestamp, preventing leakage of future data.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Feature Store](../databricks/databricks-feature-store.md), [Databricks Feature Views](../databricks/databricks-feature-views.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
