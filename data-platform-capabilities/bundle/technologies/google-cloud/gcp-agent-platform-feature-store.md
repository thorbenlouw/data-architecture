---
type: Technology
id: gcp-agent-platform-feature-store
title: Agent Platform Feature Store
description: Feature management that uses BigQuery tables as the offline store and syncs selected features to online stores for low-latency serving.
formerly: [Vertex AI Feature Store]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [feature-store, offline-feature-store, online-feature-store, point-in-time-joins]
resource: https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Online serving runs on Bigtable or an optimised serving tier that also supports embedding similarity search. Historical feature values are served from BigQuery by timestamp. The earlier "legacy" Feature Store has its own separate API.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development) (primary): Manage features centrally so they are reused, documented and served consistently for training and inference.
- [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md) (Machine learning development): Store historical feature values for model training and batch scoring.
- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development): Serve the latest feature values to models in milliseconds.
- [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) (Machine learning development): Join features as they were known at each training example's timestamp, preventing leakage of future data.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Feature Store](../snowflake/snowflake-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Feature Store](../databricks/databricks-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Feature Store](../dataiku/dataiku-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Feature store](../../capabilities/machine-learning/feature-store.md), [Offline feature store](../../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
