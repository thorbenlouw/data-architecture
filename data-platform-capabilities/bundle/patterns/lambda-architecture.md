---
type: Pattern
id: lambda-architecture
title: Lambda architecture
description: Run a batch layer and a speed layer in parallel and merge their results for serving.
aliases: [batch and speed layers]
uses:
- batch-ingestion
- streaming-ingestion
- event-streaming
- distributed-processing
- stream-processing
- workflow-orchestration
- read-optimised-views
- low-latency-serving
related: [kappa-architecture, cqrs-read-models]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Incoming data is written to an immutable master dataset and processed twice. The batch layer periodically recomputes complete, accurate views from all history. The speed layer processes only recent events as they arrive and produces incremental views that cover the gap since the last batch run. A serving layer merges the two, so queries see results that are exact up to the last batch and fresh since then. Nathan Marz, creator of Apache Storm, described the design in 2011, and later set it out in the book Big Data with James Warren.

The pattern arose when stream processors could not guarantee correct results, so the batch layer acted as the correction. It still appears where an exact nightly recomputation must sit alongside a fast but rougher live view. Its main cost is keeping the same logic in two code bases that must agree. Engines that run one program in both batch and streaming modes, and table formats with incremental reads, have made the Kappa architecture or a single unified pipeline the more common choice.

# When to use

- You need a fast live view now and an exact, fully recomputed view later, and the stream processor cannot guarantee correctness on its own.
- Recomputing history is cheap compared with the cost of errors persisting in live results.
- Trusted batch pipelines exist and a real-time view must be added without replacing them.

# Watch out for

- The same business logic is written and tested twice, and small differences make the layers disagree.
- Merging batch and speed views at query time adds logic and failure points to the serving layer.
- Running two processing stacks doubles monitoring, on-call and upgrade effort.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Event streaming](../capabilities/ingestion-integration/event-streaming.md): Publish and subscribe to durable, ordered and replayable streams of events between systems.
- [Distributed processing](../capabilities/processing/distributed-processing.md): Process large datasets in parallel across a cluster of machines.
- [Stream processing](../capabilities/processing/stream-processing.md): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Read-optimised views](../capabilities/serving/read-optimised-views.md): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
- [Low-latency serving](../capabilities/serving/low-latency-serving.md): Serve individual records or small result sets to applications in milliseconds.

# Related patterns

- [Kappa architecture](kappa-architecture.md)
- [Separate read models](cqrs-read-models.md)

# Where it appears

- **Use cases:** [Real-time fraud detection](../use-cases/usecase-fraud-detection.md) · [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) · [Operational reporting](../use-cases/usecase-operational-reporting.md) · [Personalised recommendations](../use-cases/usecase-recommendations.md)
