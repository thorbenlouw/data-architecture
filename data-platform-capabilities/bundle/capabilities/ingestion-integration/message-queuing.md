---
type: Capability
id: message-queuing
title: Message queuing
description: Distribute messages to competing consumers with per-message acknowledgement and redelivery.
aliases: [queues, work queues, share groups]
broader: [ingestion-integration]
related: [application-integration, event-driven-triggering, idempotent-loading]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A message queue holds each message until a consumer takes it and acknowledges it. Several consumers share the work: each message goes to one of them, and if that consumer fails before acknowledging, the message becomes visible again for another to take. After repeated failures it moves to a dead-letter queue for inspection. A queue of invoice-generation jobs, for example, can be worked by ten processes in parallel, with failed jobs retried automatically. AMQP and JMS are common standards.

Queues suit work distribution and commands, where each message must be handled once and then forgotten. Event streams suit broadcast and replay, where many consumers read the same history. Queues rarely guarantee order across consumers and do not keep messages after acknowledgement, so they cannot be replayed to rebuild a dataset. In data platforms they mostly appear as job dispatch, as triggers for file processing and at the boundary with application integration.

# Key considerations

- Make handlers idempotent. Redelivery after a timeout means some messages will be processed twice.
- Set visibility timeouts longer than the slowest normal processing time, or messages are redelivered while still being worked on.
- Give dead-letter queues owners and alerts. Unwatched dead-letter queues are where data quietly goes missing.
- Do not treat a queue as storage. Acknowledged messages are gone, so anything needed later must be written elsewhere.

# Questions to ask

- Must each message be handled by one worker, or read by many independent consumers?
- Is ordering required, and at what scope?
- What is the business effect if a message is delayed or processed twice?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Application integration](application-integration.md), [Bad-data quarantine](../data-quality/bad-data-quarantine.md), [Deduplication and idempotent loading](idempotent-loading.md), [Event-driven triggering](../orchestration/event-driven-triggering.md) |

# Where it appears

- **Patterns:** [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Pub/Sub](../../technologies/google-cloud/gcp-pubsub.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Kafka](../../technologies/open-source/apache-kafka.md), [Apache Pulsar](../../technologies/open-source/apache-pulsar.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md) |
