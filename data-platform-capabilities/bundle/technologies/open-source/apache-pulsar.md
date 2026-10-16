---
type: Technology
id: apache-pulsar
title: Apache Pulsar
description: Distributed messaging and event streaming platform with built-in multi-tenancy, geo-replication, tiered storage and both stream and queue subscriptions.
aliases: [Pulsar]
platform: platform-open-source
kind: open-source
availability: ga
realises: [event-streaming, streaming-ingestion, cross-region-failover, message-queuing, idempotent-loading]
resource: https://pulsar.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0; StreamNative is the main commercial vendor. Separates brokers from storage (Apache BookKeeper). Less widely adopted than Kafka, and it offers a Kafka-compatible protocol layer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) (Ingestion and integration): Distribute messages to competing consumers with per-message acknowledgement and redelivery.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md) | [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
