---
type: Technology
id: aws-sagemaker-feature-store
title: Amazon SageMaker Feature Store
description: Feature repository with an online store holding the latest values for low-latency lookup and an append-only offline store in S3 for training.
platform: platform-aws
kind: feature
availability: ga
realises: [feature-store, online-feature-store, offline-feature-store, point-in-time-joins]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Offline data is queryable with Athena and can use the Iceberg table format; the SDK builds point-in-time-correct training sets. Ingests from streams with PutRecord or in batch.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development) (primary): Manage features centrally so they are reused, documented and served consistently for training and inference.
- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development): Serve the latest feature values to models in milliseconds.
- [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md) (Machine learning development): Store historical feature values for model training and batch scoring.
- [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) (Machine learning development): Join features as they were known at each training example's timestamp, preventing leakage of future data.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Feature Store](../snowflake/snowflake-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Feature Store](../databricks/databricks-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
