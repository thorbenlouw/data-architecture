---
type: Technology
id: databricks-online-feature-store
title: Databricks Online Feature Store
description: A Lakebase-backed store that publishes feature tables for millisecond lookups by Model Serving endpoints and feature serving endpoints.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [online-feature-store]
resource: https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

New stores are created as Lakebase Autoscaling projects and do not support scale-to-zero. It replaces earlier online tables and third-party online stores. Feature serving endpoints expose features to non-Databricks applications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Online feature store](../../capabilities/machine-learning/online-feature-store.md) (Machine learning development) (primary): Serve the latest feature values to models in milliseconds.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Feature Store](../aws/aws-sagemaker-feature-store.md), [Amazon DynamoDB](../aws/aws-dynamodb.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Feature Store](../google-cloud/gcp-agent-platform-feature-store.md), [Bigtable](../google-cloud/gcp-bigtable.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Online Feature Store](../snowflake/snowflake-online-feature-store.md) (preview) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Feast](../open-source/feast.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redis Cloud](../independent/redis-cloud.md) | [Online feature store](../../capabilities/machine-learning/online-feature-store.md) |
