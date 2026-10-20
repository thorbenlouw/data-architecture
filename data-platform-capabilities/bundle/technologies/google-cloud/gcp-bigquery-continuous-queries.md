---
type: Technology
id: gcp-bigquery-continuous-queries
title: BigQuery continuous queries
description: Long-running SQL statements that process rows as they arrive in a table and write results to BigQuery or Iceberg tables, Pub/Sub, Bigtable or Spanner.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [stream-processing, streaming-sql, reverse-etl, streaming-inference]
resource: https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Needs an Enterprise or Enterprise Plus reservation with a CONTINUOUS assignment. Stateless processing is GA; joins, aggregations and windowing (stateful continuous queries) are in preview. AI.GENERATE can be called in the stream.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Spark Structured Streaming](../open-source/apache-spark-structured-streaming.md), [Apache Flink](../open-source/apache-flink.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
