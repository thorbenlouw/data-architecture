---
type: Capability
id: streaming-inference
title: Streaming inference
description: Apply models to events as they flow through a stream.
aliases: [stream scoring, event-driven inference, near-real-time scoring]
broader: [model-deployment]
related: [event-streaming, event-time-windowing, online-feature-store, real-time-inference]
depends_on: [stream-processing]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A stream processor reading machine sensor readings computes rolling averages over the last minute, passes them to an anomaly model, and publishes alerts to another topic within seconds. The model can be embedded in the stream processing job itself, or the job can call a real-time endpoint for each event or small group of events.

It fits event-driven processes where no user waits for a reply but results are needed within seconds: monitoring equipment, flagging transactions for review, updating recommendations after each click. It brings stream concerns into model serving, including event ordering, late events, exactly-once output and state for window features. Embedding the model gives the lowest latency and no extra network hop, but ties model releases to stream job deployments. Calling an endpoint keeps the two release cycles separate, at the cost of a network call per event and another service to run.

# Key considerations

- Choose between embedding the model and calling an endpoint early. It decides how model releases and job releases interact.
- Window features computed on the stream must match how training data computed them, including the handling of late events.
- Plan for replay. Reprocessing a topic after an outage should not send duplicate alerts or trigger actions twice.
- Monitor consumer lag. A slow model makes the stream fall behind rather than fail visibly.

# Questions to ask

- How soon after an event must the prediction exist, and who or what acts on it?
- Is there already a stream processing platform the model can run in?
- What should happen to predictions when events arrive late or out of order?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model deployment](model-deployment.md) |
| Related | [Edge data processing](../processing/edge-data-processing.md), [Edge inference](edge-inference.md), [Event streaming](../ingestion-integration/event-streaming.md), [Event-time windowing](../processing/event-time-windowing.md), [Online feature store](../machine-learning/online-feature-store.md), [Real-time inference](real-time-inference.md), [Stream processing](../processing/stream-processing.md) |
| Depends on | [Stream processing](../processing/stream-processing.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Managed Service for Apache Flink](../../technologies/aws/aws-managed-flink.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Stream Analytics](../../technologies/microsoft/azure-stream-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery continuous queries](../../technologies/google-cloud/gcp-bigquery-continuous-queries.md), [Dataflow ML](../../technologies/google-cloud/gcp-dataflow-ml.md), [Google Cloud Pub/Sub](../../technologies/google-cloud/gcp-pubsub.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow pipelines](../../technologies/databricks/databricks-lakeflow-pipelines.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Intelligence](../../technologies/ibm/confluent-intelligence.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Beam](../../technologies/open-source/apache-beam.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md) |
