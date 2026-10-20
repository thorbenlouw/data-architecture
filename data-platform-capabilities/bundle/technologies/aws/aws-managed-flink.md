---
type: Technology
id: aws-managed-flink
title: Amazon Managed Service for Apache Flink
description: Managed runtime for Apache Flink applications in Java, Scala, Python or SQL, with checkpoints, scaling and a notebook-based Studio for interactive streaming SQL.
formerly: [Amazon Kinesis Data Analytics for Apache Flink]
platform: platform-aws
kind: managed-service
availability: ga
realises: [stream-processing, event-time-windowing, streaming-sql, streaming-inference]
resource: https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The separate Kinesis Data Analytics for SQL Applications was retired on 27 January 2026; its applications had to be rebuilt on Flink. Managed Service for Apache Flink Studio suits exploration; long-running jobs belong in versioned application code.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Kafka Streams](../open-source/apache-kafka-streams.md), [Spark Structured Streaming](../open-source/apache-spark-structured-streaming.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
