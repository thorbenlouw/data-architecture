---
type: Technology
id: databricks-feature-store
title: Databricks Feature Store
description: A feature registry in Unity Catalog that stores features in primary-keyed Delta tables, with point-in-time training set creation, automatic lookup at inference and lineage to models.
formerly: [Feature Engineering in Unity Catalog]
platform: platform-databricks
kind: feature
availability: ga
realises: [feature-store, offline-feature-store, point-in-time-joins, feature-engineering]
resource: https://docs.databricks.com/aws/en/machine-learning/feature-store/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The legacy Workspace Feature Store is deprecated. The current docs use the name "Databricks Feature Store" for the Unity Catalog-based product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development) (primary): Manage features centrally so they are reused, documented and served consistently for training and inference.
- [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md) (Machine learning development): Store historical feature values for model training and batch scoring.
- [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) (Machine learning development): Join features as they were known at each training example's timestamp, preventing leakage of future data.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Feature Store](../snowflake/snowflake-feature-store.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Feature Store](../dataiku/dataiku-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
