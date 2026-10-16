---
type: Technology
id: aws-kinesis-data-streams
title: Amazon Kinesis Data Streams
description: Serverless, sharded event stream that stores ordered records for up to 365 days and lets many consumers read them independently.
aliases: [KDS]
platform: platform-aws
kind: managed-service
availability: ga
realises: [event-streaming, streaming-ingestion, backfill-replay, reserved-capacity]
resource: https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Capacity modes are On-demand Standard, On-demand Advantage (an account-level commitment of at least 25 MiB/s with lower unit prices and warm throughput) and Provisioned shards. Enhanced fan-out gives each consumer dedicated read throughput.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) (Ingestion and integration) (primary): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Hubs](../microsoft/azure-event-hubs.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Google Cloud Pub/Sub](../google-cloud/gcp-pubsub.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Streams Messaging](../cloudera/cloudera-streams-messaging.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud](../ibm/confluent-cloud.md), [WarpStream](../ibm/warpstream.md), [Confluent Platform](../ibm/confluent-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview), [Apache Kafka](../open-source/apache-kafka.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Redpanda Cloud](../independent/redpanda-cloud.md), [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Event streaming](../../capabilities/ingestion-integration/event-streaming.md) |
