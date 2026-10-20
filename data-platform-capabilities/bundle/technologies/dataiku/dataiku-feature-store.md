---
type: Technology
id: dataiku-feature-store
title: Dataiku Feature Store
description: Registry of curated feature groups, shared datasets that other projects join in batch or look up from API services in real time.
platform: platform-dataiku
kind: feature
availability: ga
realises: [feature-store]
resource: https://doc.dataiku.com/dss/latest/mlops/feature-store/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Feature groups are ordinary shared datasets on existing connections rather than a dedicated store. Batch use is through Join recipes and online use through dataset lookups in API node services; neither point-in-time joins nor a low-latency online store are described.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development) (primary): Manage features centrally so they are reused, documented and served consistently for training and inference.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Feature Store](../snowflake/snowflake-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Feature Store](../databricks/databricks-feature-store.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Feature store](../../capabilities/machine-learning/feature-store.md) |
