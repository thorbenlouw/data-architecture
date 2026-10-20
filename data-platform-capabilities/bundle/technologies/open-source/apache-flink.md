---
type: Technology
id: apache-flink
title: Apache Flink
description: Distributed stream processing engine with exactly-once state, event-time semantics and a unified batch and streaming SQL and Table API.
aliases: [Flink, Flink SQL]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- stream-processing
- event-time-windowing
- streaming-sql
- distributed-processing
- declarative-pipelines
- idempotent-loading
- data-enrichment
resource: https://flink.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. Flink 2.3 is the current stable line and 1.20 is the long-term support release. The 2.x line adds disaggregated (remote) state storage; Materialized Tables (from 1.20) are declared in SQL with a freshness target and refreshed by Flink. Flink Agents (event-driven AI agents on Flink, version 0.3) is a separate, early-stage subproject. Commercial offerings come from Ververica, Confluent and the cloud providers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md), [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
