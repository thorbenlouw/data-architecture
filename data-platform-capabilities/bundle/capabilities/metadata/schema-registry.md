---
type: Capability
id: schema-registry
title: Schema registry
description: Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
broader: [metadata]
related:
- data-contracts
- schema-evolution
- stream-to-table
- behavioural-event-collection
- schema-change-management
depends_on: [event-streaming]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A schema registry stores the schemas of messages on event streams, in formats such as Avro, Protobuf or JSON Schema, with a version history for each topic or subject. Producers register the schema they write, each message carries a short schema identifier, and consumers fetch the schema to decode it. Compatibility rules decide which changes are allowed. Adding an optional field passes; removing a required one is rejected. For example, a team tries to rename `amount` to `value` in the payments event, and the registry rejects the new version because existing consumers expect `amount`.

Streams decouple producers from consumers, so without a registry a producer change can break consumers silently, often far away in the organisation. Compatibility modes include backward, forward and full, each optionally checked against all earlier versions rather than just the last. A data contract usually includes the schema plus meaning and service levels; table schema evolution does the same job for tables. Registries increasingly feed the data catalogue and stream-to-table materialisation.

# Key considerations

- Choose a compatibility mode per topic deliberately. Backward compatibility is the common default but does not protect consumers that lag behind.
- Enforce registration in producer clients or the broker, not by convention.
- A change of meaning with the same type passes compatibility checks. Review such changes through data contracts.
- Producers and consumers depend on the registry. Run it with high availability and let clients cache schemas.

# Questions to ask

- How many teams produce and consume events, and how often do schemas change?
- Have producer changes broken consumers before?
- Which serialisation formats are in use?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md) |
| Related | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Data contracts](../data-products/data-contracts.md), [Event and API catalogue](event-api-catalogue.md), [Event streaming](../ingestion-integration/event-streaming.md), [Open file formats](../storage/file-formats.md), [Schema change management](../development-lifecycle/schema-change-management.md), [Schema enforcement and evolution](../storage/schema-evolution.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md), [Streaming SQL](../processing/streaming-sql.md) |
| Depends on | [Event streaming](../ingestion-integration/event-streaming.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 3)
- **Patterns:** [Kappa architecture](../../patterns/kappa-architecture.md) · [Shift-left data quality and governance](../../patterns/shift-left.md) · [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 2, Managed) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue Schema Registry](../../technologies/aws/aws-glue-schema-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Schema Registry in Event Hubs](../../technologies/microsoft/azure-event-hubs-schema-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Pub/Sub](../../technologies/google-cloud/gcp-pubsub.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Streams Messaging](../../technologies/cloudera/cloudera-streams-messaging.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md), [Confluent Platform](../../technologies/ibm/confluent-platform.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apicurio Registry](../../technologies/open-source/apicurio-registry.md) |
