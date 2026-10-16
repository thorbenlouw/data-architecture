---
type: Capability
id: event-streaming
title: Event streaming
description: Publish and subscribe to durable, ordered and replayable streams of events between systems.
aliases: [message broker, event bus, Kafka, pub/sub]
broader: [ingestion-integration]
related:
- streaming-ingestion
- stream-processing
- schema-registry
- change-data-capture
- application-integration
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An event streaming platform stores events in append-only logs called topics, split into partitions so many machines can write and read in parallel. Producers append events; each consumer tracks its own position, or offset, and reads at its own pace, so a fraud service and an analytics loader can read the same payments topic independently. Events are kept for a set retention period, or indefinitely with compaction to the latest value per key, so a new consumer can replay history from the start. The Apache Kafka protocol is the common reference point.

Streaming decouples systems: producers need not know who consumes, and consumers can be added without changing producers. Order is guaranteed only within a partition, so all events for one key, such as one account, must go to the same partition. Message queuing differs because messages are removed once acknowledged. Streaming is the transport; streaming ingestion and stream processing are what read from it.

# Key considerations

- Choose partition keys for both ordering and even load. A hot key can overwhelm one partition while others sit idle.
- Use a schema registry with compatibility rules from the start. Unmanaged event formats are hard to fix once many consumers depend on them.
- Decide delivery guarantees per use. At-least-once is normal; exactly-once needs transactional producers and consumers and reduces throughput.
- Retention drives storage cost. Tiered storage that moves older segments to object storage makes long retention affordable.

# Questions to ask

- Which systems produce events today, and how many consumers need each stream?
- How long must events be kept for replay or for new consumers?
- What ordering and delivery guarantees do consumers need?
- What peak throughput and message sizes must be supported?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Application integration](application-integration.md), [Backfill and reprocessing](../orchestration/backfill-replay.md), [Change data capture](change-data-capture.md), [Change feeds](../serving/change-feeds.md), [Event and API catalogue](../metadata/event-api-catalogue.md), [Inference logging](../mlops/inference-logging.md), [IoT and telemetry ingestion](iot-ingestion.md), [Schema registry](../metadata/schema-registry.md), [Stream processing](../processing/stream-processing.md), [Streaming inference](../mlops/streaming-inference.md), [Streaming ingestion](streaming-ingestion.md) |
| Needed by | [Schema registry](../metadata/schema-registry.md), [Stream processing](../processing/stream-processing.md), [Stream-to-table materialisation](stream-to-table.md), [Streaming SQL](../processing/streaming-sql.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [Kappa architecture](../../patterns/kappa-architecture.md) · [Lambda architecture](../../patterns/lambda-architecture.md) · [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Kinesis Data Streams](../../technologies/aws/aws-kinesis-data-streams.md), [Amazon Managed Streaming for Apache Kafka](../../technologies/aws/aws-msk.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Eventstream; Event Hubs | [Azure Event Hubs](../../technologies/microsoft/azure-event-hubs.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Pub/Sub | [Google Cloud Managed Service for Apache Kafka](../../technologies/google-cloud/gcp-managed-kafka.md), [Google Cloud Pub/Sub](../../technologies/google-cloud/gcp-pubsub.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Streams Messaging](../../technologies/cloudera/cloudera-streams-messaging.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Streaming with Apache Kafka](../../technologies/oracle/oracle-oci-streaming-kafka.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md), [Confluent Platform](../../technologies/ibm/confluent-platform.md), [WarpStream](../../technologies/ibm/warpstream.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Fluss (incubating)](../../technologies/open-source/apache-fluss.md) (preview), [Apache Kafka](../../technologies/open-source/apache-kafka.md), [Apache Pulsar](../../technologies/open-source/apache-pulsar.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [Redpanda Cloud](../../technologies/independent/redpanda-cloud.md) |
