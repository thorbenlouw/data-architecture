---
type: Technology
id: redpanda-cloud
title: Redpanda Cloud
description: Managed Kafka-compatible streaming service on a C++ engine with no external dependencies, offered as Serverless, Dedicated or BYOC clusters.
aliases: [Redpanda]
platform: platform-independent
vendor: Redpanda Data
kind: managed-service
availability: ga
realises: [event-streaming, open-table-formats, stream-to-table, hybrid-data-plane]
resource: https://docs.redpanda.com/redpanda-cloud/get-started/cloud-overview/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Iceberg Topics write topic data as Iceberg v2 tables to object storage and register them with an Iceberg REST catalogue (BYOC and BYOVPC only). Redpanda Connect (formerly Benthos) provides more than 300 declarative YAML connectors. Redpanda SQL, a new PostgreSQL-compatible engine built on the Oxla acquisition, queries live and historical data. Serverless on GCP is in beta. Self-Managed is the on-premises edition.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) (Ingestion and integration): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

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
| [IBM](../../platforms/platform-ibm.md) | [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md), [Apache Pulsar](../open-source/apache-pulsar.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
