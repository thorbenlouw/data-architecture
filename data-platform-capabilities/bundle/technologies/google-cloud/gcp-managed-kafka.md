---
type: Technology
id: gcp-managed-kafka
title: Google Cloud Managed Service for Apache Kafka
description: Runs Apache Kafka clusters, managed Kafka Connect clusters and a schema registry on Google Cloud, with Google handling brokers, scaling and patching.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [event-streaming, streaming-ingestion]
resource: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed Kafka Connect (GA October 2025) runs MirrorMaker 2, BigQuery, Cloud Storage and Pub/Sub connectors, and Debezium-based PostgreSQL sources were added in July 2026. A schema registry has been in preview since May 2025. Integrates with VPC Service Controls and has a remote MCP server (GA April 2026).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md), [Amazon Managed Streaming for Apache Kafka](../aws/aws-msk.md), [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
