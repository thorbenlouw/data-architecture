---
type: Pattern
id: cqrs-read-models
title: Separate read models
description: Separate the models used to write data from models shaped for reading, and keep the read models in sync.
aliases: [CQRS, command query responsibility segregation, CQRS read models]
uses:
- change-data-capture
- change-feeds
- event-streaming
- read-optimised-views
- materialised-views
- low-latency-serving
- operational-data-store
- full-text-search
- backfill-replay
related: [kappa-architecture, transactional-outbox, lambda-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An application writes through a model designed for correct updates, usually a normalised transactional database or an event log. Read models, each shaped for one access pattern, are derived from it: a search index, a denormalised document for a product page, an aggregate table for a dashboard. A projection process listens to changes, often through change data capture or events, and updates each read model. Greg Young named the pattern command query responsibility segregation (CQRS) around 2010, building on Bertrand Meyer's earlier principle of separating commands from queries.

In data platforms the same idea appears whenever reads are kept off the system of record: an analytical copy fed by change data capture, a cache behind an API, or a real-time table for a customer-facing dashboard. Each read model can use the store best suited to it and scale on its own. The price is eventual consistency, because reads lag writes by the projection delay, and the need to rebuild read models when their shape changes.

# When to use

- Read and write workloads differ sharply in volume, shape or latency, and one model cannot serve both well.
- Several consumers need the same data in different shapes, such as search, APIs and dashboards.
- The system of record must be protected from heavy analytical or high-volume read traffic.

# Watch out for

- Read models lag writes; consumers must tolerate that, or read from the source when they cannot.
- Every read model is another store to monitor, secure and rebuild when the projection logic changes.
- Applying the pattern to simple create-read-update-delete systems adds moving parts with little benefit.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Change data capture](../capabilities/ingestion-integration/change-data-capture.md): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Change feeds](../capabilities/serving/change-feeds.md): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Event streaming](../capabilities/ingestion-integration/event-streaming.md): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Read-optimised views](../capabilities/serving/read-optimised-views.md): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
- [Materialised views](../capabilities/compute/materialised-views.md): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Low-latency serving](../capabilities/serving/low-latency-serving.md): Serve individual records or small result sets to applications in milliseconds.
- [Operational data store](../capabilities/serving/operational-data-store.md): Hold a current, integrated view of data from several operational systems for operational reporting and lookups.
- [Full-text search](../capabilities/specialised-data/full-text-search.md): Index text for full-text search, relevance ranking and fast filtering.
- [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md): Rerun pipelines over historical periods or replay events to correct or rebuild data.

# Related patterns

- [Kappa architecture](kappa-architecture.md)
- [Transactional outbox](transactional-outbox.md)
- [Lambda architecture](lambda-architecture.md)

# Where it appears

- **Use cases:** [Customer 360](../use-cases/usecase-customer-360.md) · [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md) · [Operational reporting](../use-cases/usecase-operational-reporting.md)
- **Personas:** [Data architect](../personas/persona-data-architect.md) · [Software engineer](../personas/persona-software-engineer.md)
