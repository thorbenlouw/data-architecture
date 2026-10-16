---
type: Technology
id: apache-fluss
title: Apache Fluss (incubating)
description: Streaming storage for real-time analytics that holds fresh data in primary-key and columnar log tables and tiers it into lakehouse formats.
aliases: [Fluss]
platform: platform-open-source
kind: open-source
availability: preview
realises: [event-streaming, real-time-analytics, stream-to-table]
resource: https://fluss.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, donated by Alibaba to the ASF Incubator in 2025. Tiers data to Paimon, Iceberg, Hudi or Lance, and supports union reads across hot and lake data. Mainly used with Flink; early-stage compared with Kafka.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) (Ingestion and integration): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [IBM](../../platforms/platform-ibm.md) | [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
