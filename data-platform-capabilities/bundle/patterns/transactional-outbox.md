---
type: Pattern
id: transactional-outbox
title: Transactional outbox
description: Write events to an outbox table in the same transaction as the business change, then publish them reliably.
aliases: [outbox pattern, outbox table]
uses:
- operational-database
- change-data-capture
- event-streaming
- message-queuing
- schema-registry
- data-contracts
- idempotent-loading
related: [cqrs-read-models, kappa-architecture, shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a service updates its database and also publishes an event, doing the two separately risks one succeeding and the other failing. With an outbox, the service writes the event to an outbox table in the same database transaction as the business change, so both commit or neither does. A separate relay then reads the outbox, publishes each event to the broker and marks it as sent. Often the relay is a change data capture connector reading the outbox table from the transaction log. The pattern is documented in Chris Richardson's catalogue of microservice patterns and is common in event-driven systems.

For data platforms, the outbox gives domain events a defined schema owned by the producing team, instead of downstream consumers reverse-engineering internal tables through change data capture. That makes it a practical way to implement a data contract at the source. Delivery is at least once, so consumers must deduplicate, and the outbox table needs regular pruning so it does not grow without limit.

# When to use

- A service must publish events that exactly reflect committed database changes, without distributed transactions.
- Downstream consumers need stable, deliberately designed events rather than raw table changes.
- You already run change data capture and can point it at an outbox table instead of internal tables.

# Watch out for

- The relay delivers at least once, so consumers need idempotent handling or deduplication.
- Ordering is only preserved per key if the relay and topic partitioning both keep it.
- Outbox tables grow quickly; schedule removal of events that have been sent.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Operational database integration](../capabilities/serving/operational-database.md): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Change data capture](../capabilities/ingestion-integration/change-data-capture.md): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Event streaming](../capabilities/ingestion-integration/event-streaming.md): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Message queuing](../capabilities/ingestion-integration/message-queuing.md): Distribute messages to competing consumers with per-message acknowledgement and redelivery.
- [Schema registry](../capabilities/metadata/schema-registry.md): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Data contracts](../capabilities/data-products/data-contracts.md): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

# Related patterns

- [Separate read models](cqrs-read-models.md)
- [Kappa architecture](kappa-architecture.md)
- [Shift-left data quality and governance](shift-left.md)

# Where it appears

- **Use cases:** [Application data publishing](../use-cases/usecase-application-data-publishing.md)
- **Personas:** [Software engineer](../personas/persona-software-engineer.md)
