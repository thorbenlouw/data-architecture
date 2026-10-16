---
type: Technology
id: gcp-dataflow-ml
title: Dataflow ML
description: Beam transforms such as RunInference and MLTransform that run model inference and feature preprocessing, including embeddings, inside batch and streaming Dataflow pipelines.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [streaming-inference, batch-inference, feature-engineering]
resource: https://docs.cloud.google.com/dataflow/docs/machine-learning
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports GPUs on workers and calling Agent Platform endpoints or Gemini models from the pipeline.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations) (primary): Apply models to events as they flow through a stream.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Dataflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Batch inference](../../capabilities/mlops/batch-inference.md), [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md) | [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Intelligence](../ibm/confluent-intelligence.md) (preview) | [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Spark Structured Streaming](../open-source/apache-spark-structured-streaming.md) | [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
