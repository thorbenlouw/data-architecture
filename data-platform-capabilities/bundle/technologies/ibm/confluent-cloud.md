---
type: Technology
id: confluent-cloud
title: Confluent Cloud
description: Fully managed Apache Kafka service on AWS, Azure and Google Cloud, with managed connectors, Schema Registry, Stream Governance and cluster linking.
aliases: [Confluent Stream Governance]
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- event-streaming
- streaming-ingestion
- schema-registry
- change-data-capture
- cross-region-failover
- event-api-catalogue
- data-contracts
resource: https://docs.confluent.io/cloud/current/clusters/cluster-types.html
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cluster types are Basic, Standard, Enterprise (private networking), Dedicated and Freight (lower cost, higher latency). Stream Governance adds Stream Catalog, Stream Lineage and data contracts with quality rules on schemas. IBM completed its acquisition of Confluent on 17 March 2026 and positions it beside watsonx.data, IBM MQ and webMethods.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Schema registry](../../capabilities/metadata/schema-registry.md) (Metadata and discovery): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** Confluent

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Schema registry](../../capabilities/metadata/schema-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
