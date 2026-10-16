---
type: Capability
id: online-feature-store
title: Online feature store
description: Serve the latest feature values to models in milliseconds.
broader: [feature-store, low-latency-serving]
related: [real-time-inference, stream-processing, operational-database, streaming-inference]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An online feature store keeps the latest value of each feature per entity in a key-value database or in-memory cache. A model serving a request can fetch, say, 20 features for one customer by id in a few milliseconds. Values arrive from the offline store on a schedule, from streaming pipelines that write them directly, or both. A fraud check might combine a customer risk profile refreshed nightly with a count of card transactions in the last five minutes kept current from a stream.

It is needed when a model predicts inside an interactive request and cannot wait for a warehouse query. Teams that first read features straight from the analytical warehouse often find that tail latency and concurrency miss a 50-millisecond budget. The main design choices are freshness, read latency under load, and how values are loaded. Unlike general low-latency serving of records, the online store must stay consistent with the offline history used for training, which is why the two are usually managed together.

# Key considerations

- Measure latency at the 99th percentile under realistic concurrency, not as an average. The whole prediction usually has a tight budget.
- Set a time-to-live or staleness check per feature, so models do not keep using values that have stopped updating.
- Online storage costs far more per gigabyte than offline. Publish only the features and entities real-time models read.
- Plan for serving in several regions if the calling applications run in several regions.

# Questions to ask

- What end-to-end latency must predictions meet, and how much of it can feature lookup use?
- How many lookups per second are expected at peak?
- How stale may each feature be: seconds, minutes or a day?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Feature store](feature-store.md), [Low-latency serving](../serving/low-latency-serving.md) |
| Related | [Decision management](../serving/decision-management.md), [Operational database integration](../serving/operational-database.md), [Real-time inference](../mlops/real-time-inference.md), [Stream processing](../processing/stream-processing.md), [Streaming inference](../mlops/streaming-inference.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 4, Measured) · [ML development](../../maturity/track-ml-development.md) (from level 4, Measured)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Feature store

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon DynamoDB](../../technologies/aws/aws-dynamodb.md), [Amazon SageMaker Feature Store](../../technologies/aws/aws-sagemaker-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning managed feature store](../../technologies/microsoft/azure-ml-managed-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Feature Store](../../technologies/google-cloud/gcp-agent-platform-feature-store.md), [Bigtable](../../technologies/google-cloud/gcp-bigtable.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Online Feature Store](../../technologies/snowflake/snowflake-online-feature-store.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Online Feature Store](../../technologies/databricks/databricks-online-feature-store.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Feast](../../technologies/open-source/feast.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Redis Cloud](../../technologies/independent/redis-cloud.md) |
