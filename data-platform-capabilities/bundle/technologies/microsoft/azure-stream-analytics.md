---
type: Technology
id: azure-stream-analytics
title: Azure Stream Analytics
description: Serverless stream processing with a SQL-like language, event-time windows, reference data joins and calls to machine learning models.
aliases: [ASA]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [stream-processing, streaming-sql, event-time-windowing, streaming-inference, data-enrichment]
resource: https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still current; for Fabric-centred designs Eventstream covers simpler cases.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Data enrichment](../../capabilities/processing/data-enrichment.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Apache Flink](../open-source/apache-flink.md), [Kafka Streams](../open-source/apache-kafka-streams.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
