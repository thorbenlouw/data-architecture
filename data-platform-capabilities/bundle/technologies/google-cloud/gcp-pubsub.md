---
type: Technology
id: gcp-pubsub
title: Google Cloud Pub/Sub
description: Global publish-subscribe messaging service with push, pull and export subscriptions that write directly to BigQuery, Cloud Storage and Bigtable.
formerly: [Cloud Pub/Sub]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [event-streaming, streaming-ingestion, schema-registry, streaming-inference, message-queuing]
resource: https://docs.cloud.google.com/pubsub/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Import topics ingest from Amazon Kinesis, Amazon MSK, Confluent Cloud, Azure Event Hubs and Cloud Storage. Single message transforms run JavaScript UDFs, and an AI Inference transform (GA April 2026) calls Agent Platform models per message. Topic schemas use Avro or Protocol Buffers. Pub/Sub Lite is deprecated and shuts down on 31 January 2027; Google recommends Pub/Sub or Managed Kafka instead. Bigtable subscriptions are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.
- [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) (Ingestion and integration): Distribute messages to competing consumers with per-message acknowledgement and redelivery.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md), [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [Confluent Platform](../ibm/confluent-platform.md), [WarpStream](../ibm/warpstream.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Kafka](../open-source/apache-kafka.md), [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
