---
type: Technology
id: confluent-cloud-flink
title: Confluent Cloud for Apache Flink
description: Serverless Apache Flink service for continuous SQL and Table API processing over Kafka topics, with autoscaling and built-in functions.
platform: platform-ibm
kind: managed-service
availability: ga
realises: [stream-processing, streaming-sql, event-time-windowing, serverless-compute, user-defined-functions]
resource: https://docs.confluent.io/cloud/current/flink/overview.html
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Flink SQL and the Java Table API are GA, and the Python Table API is in preview. Built-in functions cover anomaly detection, forecasting, embeddings and calls to remote models. It is the runtime for Streaming Agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** Confluent

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Streams](../open-source/apache-kafka-streams.md), [Apache Flink](../open-source/apache-flink.md), [Apache Beam](../open-source/apache-beam.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
