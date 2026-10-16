---
type: Technology
id: apache-kafka
title: Apache Kafka
description: Distributed event streaming platform that stores ordered, replayable logs of events in topics for publish and subscribe at high throughput.
aliases: [Kafka]
platform: platform-open-source
kind: open-source
availability: ga
realises: [event-streaming, message-queuing, idempotent-loading]
resource: https://kafka.apache.org/community/downloads/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. Kafka 4.0 (2025) removed ZooKeeper, leaving KRaft only. The 4.3 line is current (4.3.1, June 2026). Share groups (queue semantics, KIP-932) became production-ready in 4.2, and tiered storage is GA. Loading streams into other systems is done with [Kafka Connect](../open-source/apache-kafka-connect.md) and stream processing with [Kafka Streams](../open-source/apache-kafka-streams.md). Confluent, the cloud providers and many others sell managed Kafka; Confluent Schema Registry is not part of Apache Kafka and uses the Confluent Community Licence.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) (Ingestion and integration): Distribute messages to competing consumers with per-message acknowledgement and redelivery.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../../capabilities/ingestion-integration/message-queuing.md) |
| [IBM](../../platforms/platform-ibm.md) | [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
