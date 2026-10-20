---
type: Technology
id: apache-beam
title: Apache Beam
description: Portable programming model and SDKs for batch and streaming pipelines that run on several engines, such as Flink, Spark and Google Cloud Dataflow.
aliases: [Beam, Beam YAML]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- stream-processing
- distributed-processing
- event-time-windowing
- streaming-inference
- data-enrichment
resource: https://beam.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0, driven mainly by Google. Portability is the selling point, but in practice most production Beam runs on Dataflow. Beam YAML allows pipelines to be declared without code, and the RunInference transform applies ML models within pipelines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
