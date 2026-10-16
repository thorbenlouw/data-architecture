---
type: Technology
id: apache-kafka-streams
title: Kafka Streams
description: Java library for building stateful stream processing applications that read from and write to Kafka.
aliases: [Apache Kafka Streams, KStreams]
platform: platform-open-source
kind: open-source
availability: ga
realises: [stream-processing, event-time-windowing]
resource: https://kafka.apache.org/documentation/streams/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Apache Kafka; runs inside your application rather than on a separate cluster. Kafka 4.2 made the server-side rebalance protocol GA (with a limited feature set) and added dead-letter queue support in exception handlers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
