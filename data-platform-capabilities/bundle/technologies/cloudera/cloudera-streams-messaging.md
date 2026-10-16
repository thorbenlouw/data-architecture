---
type: Technology
id: cloudera-streams-messaging
title: Cloudera Streams Messaging
description: Cloudera's Apache Kafka distribution with Schema Registry, Streams Messaging Manager, Streams Replication Manager and Cruise Control.
aliases: [Streams Messaging Manager, Streams Replication Manager]
platform: platform-cloudera
kind: software
availability: ga
realises: [event-streaming, schema-registry, cross-region-failover]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Available in Base on premises, as Data Hub templates on cloud, and as a Kubernetes operator. Streams Replication Manager (MirrorMaker 2) replicates topics between clusters for disaster recovery.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Stream Processing

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [Confluent Platform](../ibm/confluent-platform.md), [WarpStream](../ibm/warpstream.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
