---
type: Technology
id: snowflake-online-feature-store
title: Snowflake Online Feature Store
description: Syncs feature views to a low-latency online store and serves them by key through a REST API, with stream and real-time feature views for sub-minute freshness.
platform: platform-snowflake
kind: feature
availability: preview
realises: [online-feature-store]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/online-feature-store
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Postgres-backed store with REST serving (around 10 ms p50) has been in public preview since July 2026. The older hybrid-table-backed online serving is GA but has fewer capabilities.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development) (primary): Serve the latest feature values to models in milliseconds.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md), [Bigtable](../google-cloud/gcp-bigtable.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Online Feature Store](../databricks/databricks-online-feature-store.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
