---
type: Technology
id: confluent-platform
title: Confluent Platform
description: Self-managed Kafka distribution for on-premises and private cloud, with connectors, Schema Registry, Flink and management tooling.
platform: platform-ibm
kind: software
availability: ga
realises: [event-streaming, deployment-options, schema-registry, stream-processing]
resource: https://www.confluent.io/product/confluent-platform/
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Version 8.3 is current. Confluent for Kubernetes (CFK) runs it on Kubernetes, and Confluent Platform for Apache Flink adds self-managed stream processing. Unified Stream Manager monitors self-managed clusters from Confluent Cloud.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation): Transform, join and aggregate events continuously as they arrive, keeping state across events.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** Confluent

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md), [Apache Pulsar](../open-source/apache-pulsar.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
