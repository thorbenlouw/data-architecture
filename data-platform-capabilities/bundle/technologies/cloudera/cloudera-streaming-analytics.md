---
type: Technology
id: cloudera-streaming-analytics
title: Cloudera Streaming Analytics
description: Apache Flink distribution with SQL Stream Builder, a console for writing continuous SQL jobs and materialised views over streams.
aliases: [CSA, SQL Stream Builder, SSB]
platform: platform-cloudera
kind: software
availability: ga
realises: [stream-processing, streaming-sql, event-time-windowing]
resource: https://docs.cloudera.com/csa-operator/1.6/overview/topics/csa-op-main.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Delivered in Base, on Data Hub, and as the Cloudera Streaming Analytics Operator for Kubernetes. SQL Stream Builder can expose materialised views as REST endpoints for low-latency reads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Stream Processing

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Streams](../open-source/apache-kafka-streams.md), [Apache Flink](../open-source/apache-flink.md), [Apache Beam](../open-source/apache-beam.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
