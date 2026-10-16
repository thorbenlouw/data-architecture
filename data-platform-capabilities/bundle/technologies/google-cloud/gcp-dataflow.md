---
type: Technology
id: gcp-dataflow
title: Google Cloud Dataflow
description: Serverless runner for Apache Beam batch and streaming pipelines with autoscaling, exactly-once processing and event-time windowing.
formerly: [Cloud Dataflow]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- stream-processing
- event-time-windowing
- distributed-processing
- streaming-ingestion
- serverless-compute
- data-enrichment
- interruptible-compute
resource: https://docs.cloud.google.com/dataflow/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pipelines are written with the open-source Apache Beam SDKs (Java, Python, Go, YAML) and use Streaming Engine and Managed I/O connectors. Flexible Resource Scheduling (FlexRS) runs delay-tolerant batch jobs on a mix of preemptible and standard VMs at a lower price. In 2026 Dataflow became the engine for importing Parquet, Delta Lake and external Iceberg data into Lakehouse, with CDC from Delta and Iceberg in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Event-time windowing](../../capabilities/processing/event-time-windowing.md) (Processing and transformation): Group events into time windows by when they happened, handling late and out-of-order data.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.
- [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) (Query and compute): Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Dataflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Apache Flink](../open-source/apache-flink.md), [Spark Structured Streaming](../open-source/apache-spark-structured-streaming.md) | [Data enrichment](../../capabilities/processing/data-enrichment.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Event-time windowing](../../capabilities/processing/event-time-windowing.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
