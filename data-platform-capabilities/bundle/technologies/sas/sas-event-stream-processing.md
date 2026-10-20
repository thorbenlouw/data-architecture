---
type: Technology
id: sas-event-stream-processing
title: SAS Event Stream Processing
description: Streaming engine that filters, aggregates, joins and scores events in continuous queries, running from edge devices to Kubernetes clusters, with a low-code designer.
aliases: [SAS ESP, ESP, SAS Event Stream Processing Studio, SAS Event Stream Manager]
platform: platform-sas
kind: software
availability: ga
realises: [stream-processing, streaming-inference, edge-data-processing, iot-ingestion]
resource: https://www.sas.com/en_us/software/event-stream-processing.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Included in SAS Viya Enterprise and also deployable without SAS Viya. Prebuilt connectors and adapters read from and write to message brokers, databases and devices; custom windows can be written in Python. SAS Event Stream Manager deploys and manages projects across many sites.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation) (primary): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.
- [Edge data processing](../../capabilities/processing/edge-data-processing.md) (Processing and transformation): Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.
- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration): Collect high-volume telemetry securely from devices and edge gateways.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Service for Apache Flink](../aws/aws-managed-flink.md), [AWS IoT SiteWise](../aws/aws-iot-sitewise.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md), [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Azure Stream Analytics](../microsoft/azure-stream-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery continuous queries](../google-cloud/gcp-bigquery-continuous-queries.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streaming Analytics](../cloudera/cloudera-streaming-analytics.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md), [Confluent Platform](../ibm/confluent-platform.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Beam](../open-source/apache-beam.md), [Spark Structured Streaming](../open-source/apache-spark-structured-streaming.md), [Kafka Streams](../open-source/apache-kafka-streams.md) | [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming inference](../../capabilities/mlops/streaming-inference.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md) | [Stream processing](../../capabilities/processing/stream-processing.md) |
