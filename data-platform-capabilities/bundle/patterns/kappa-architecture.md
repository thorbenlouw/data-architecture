---
type: Pattern
id: kappa-architecture
title: Kappa architecture
description: Treat all data as streams and rebuild state by replaying the log, using a single processing path.
uses:
- event-streaming
- stream-processing
- streaming-sql
- event-time-windowing
- backfill-replay
- idempotent-loading
- schema-registry
- stream-to-table
related: [lambda-architecture, cqrs-read-models, transactional-outbox]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Every input is appended to a durable, ordered log, such as an Apache Kafka topic with long retention. A single stream processing job reads the log and maintains the output tables or views. To change the logic or fix a bug, you start a new version of the job reading from the start of the log, let it catch up, switch consumers to its output and retire the old version. Jay Kreps, one of Kafka's creators, proposed this in 2014 as a simpler alternative to the Lambda architecture.

The pattern removes duplicated batch and streaming code by making replay the batch mechanism. It suits systems where data naturally arrives as events and results must stay fresh. It relies on stream processors that keep exactly-once state and handle late events correctly, and on retaining enough history in the log, or in tiered storage behind it, to rebuild state. Replaying years of events can be slow and costly, so many teams combine the pattern with periodic snapshots or by materialising the log as tables.

# When to use

- Data arrives as events and consumers need continuously fresh results.
- You want one code path for both live processing and reprocessing.
- The event log can keep, or tier to cheap storage, enough history to rebuild state.

# Watch out for

- Full replays of long histories take time and compute; plan capacity and use snapshots to shorten them.
- Correct results depend on event-time handling, idempotent sinks and exactly-once state in the stream processor.
- Exploring history directly against a log is awkward, so analysts still need tables.
- Years of retained events must stay readable as schemas change, which needs a schema registry and compatibility rules.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Event streaming](../capabilities/ingestion-integration/event-streaming.md): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Stream processing](../capabilities/processing/stream-processing.md): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Streaming SQL](../capabilities/processing/streaming-sql.md): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Event-time windowing](../capabilities/processing/event-time-windowing.md): Group events into time windows by when they happened, handling late and out-of-order data.
- [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
- [Schema registry](../capabilities/metadata/schema-registry.md): Store and version schemas for events and messages, and enforce compatibility between producers and consumers.
- [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.

# Related patterns

- [Lambda architecture](lambda-architecture.md)
- [Separate read models](cqrs-read-models.md)
- [Transactional outbox](transactional-outbox.md)

# Where it appears

- **Use cases:** [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md) · [Real-time fraud detection](../use-cases/usecase-fraud-detection.md) · [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) · [Operational reporting](../use-cases/usecase-operational-reporting.md) · [Personalised recommendations](../use-cases/usecase-recommendations.md) · [Security and log analytics](../use-cases/usecase-security-log-analytics.md)
- **Personas:** [Data engineer](../personas/persona-data-engineer.md) · [Software engineer](../personas/persona-software-engineer.md)
