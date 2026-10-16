---
type: Maturity Track
id: track-real-time
title: Real-time and streaming
description: How well the organisation moves, processes and queries data continuously, with predictable latency and correct results, instead of in scheduled batches.
covers:
- event-streaming
- streaming-ingestion
- change-data-capture
- stream-processing
- streaming-sql
- event-time-windowing
- stream-to-table
- real-time-analytics
- change-feeds
- schema-registry
- event-api-catalogue
related_tracks: [track-ingestion, track-transformation, track-serving, track-specialised-data]
levels:
- level: 1
  name: Initial
  summary: Fresh-data needs are met by running batch jobs more often or by point-to-point integrations.
  criteria:
  - Near-real-time tables are produced by batch jobs every few minutes, and runs overlap when one is slow.
  - Applications poll each other's databases or call each other directly to pass events.
  - No event broker is in shared use, or one runs for a single project with no agreed topic naming or retention.
  - Events produced while a consumer is down are lost or replayed by hand.
  capabilities: []
- level: 2
  name: Managed
  summary: One team runs an event broker and a few streaming pipelines with known owners.
  criteria:
  - A broker holds durable topics with defined retention, and consumers keep their own offsets so they resume after an outage.
  - At least one source database feeds the platform through log-based change data capture rather than polling queries.
  - Streaming jobs restart automatically from checkpoints after failure.
  - Topic owners and consumers are listed, even if only on a wiki page.
  capabilities: [event-streaming, change-data-capture, streaming-ingestion]
- level: 3
  name: Defined
  summary: Streaming is a supported platform pattern with registered schemas, explicit time semantics and self-service setup.
  criteria:
  - Every production topic has a registered schema with a compatibility rule that the broker or client enforces, and is listed in an event catalogue with its owner, versions and consumers.
  - The standard job template makes each streaming job declare event-time fields, watermarks and how late events are handled.
  - Teams create topics, change capture feeds and streaming jobs from templates, with access control and quotas applied automatically.
  - Topics can be landed as open-format tables registered in the catalogue without writing a custom sink.
  - Continuous transformations can be written in SQL as well as in code.
  capabilities:
  - schema-registry
  - stream-processing
  - event-time-windowing
  - streaming-sql
  - stream-to-table
  - event-api-catalogue
- level: 4
  name: Measured
  summary: End-to-end latency and correctness are measured per pipeline against stated targets.
  criteria:
  - Latency from source commit to queryable result is measured per pipeline against a target, such as 10 seconds at the 95th percentile.
  - Consumer lag, checkpoint duration and late-event counts have dashboards and alert thresholds.
  - Stream outputs are reconciled with source totals on a schedule to show that no events were lost or counted twice.
  - User-facing queries over data less than a minute old return within a target, such as 200 milliseconds, at measured peak concurrency.
  - Change feeds from platform tables carry each row's change type and commit version, and consumers resume from their last processed version after an outage.
  capabilities: [real-time-analytics, change-feeds]
- level: 5
  name: Optimising
  summary: Streaming capacity, cost and freshness are tuned continuously against business need.
  criteria:
  - Partitions and workers scale from observed and forecast load, and expected peaks are rehearsed with load tests.
  - Each pipeline's latency is reviewed against the business need, and pipelines that do not need seconds-level freshness move to cheaper micro-batch or batch.
  - Replaying a window of any topic into a test environment is routine and used to check changes before release.
  - Schema changes are checked against every registered consumer and rolled out without a coordinated outage.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up lets operational decisions, customer-facing features and monitoring use data that is seconds old rather than hours old, without giving up correctness. Typical blockers are treating streaming as faster batch with no plan for late or duplicate events, event schemas that change without notice, the cost of always-on clusters, and too few people who can run brokers and stateful stream processors.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Fresh-data needs are met by running batch jobs more often or by point-to-point integrations.

- Near-real-time tables are produced by batch jobs every few minutes, and runs overlap when one is slow.
- Applications poll each other's databases or call each other directly to pass events.
- No event broker is in shared use, or one runs for a single project with no agreed topic naming or retention.
- Events produced while a consumer is down are lost or replayed by hand.

## Level 2: Managed

One team runs an event broker and a few streaming pipelines with known owners.

- A broker holds durable topics with defined retention, and consumers keep their own offsets so they resume after an outage.
- At least one source database feeds the platform through log-based change data capture rather than polling queries.
- Streaming jobs restart automatically from checkpoints after failure.
- Topic owners and consumers are listed, even if only on a wiki page.

**Capabilities first relied on:** [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md)

## Level 3: Defined

Streaming is a supported platform pattern with registered schemas, explicit time semantics and self-service setup.

- Every production topic has a registered schema with a compatibility rule that the broker or client enforces, and is listed in an event catalogue with its owner, versions and consumers.
- The standard job template makes each streaming job declare event-time fields, watermarks and how late events are handled.
- Teams create topics, change capture feeds and streaming jobs from templates, with access control and quotas applied automatically.
- Topics can be landed as open-format tables registered in the catalogue without writing a custom sink.
- Continuous transformations can be written in SQL as well as in code.

**Capabilities first relied on:** [Schema registry](../capabilities/metadata/schema-registry.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md)

## Level 4: Measured

End-to-end latency and correctness are measured per pipeline against stated targets.

- Latency from source commit to queryable result is measured per pipeline against a target, such as 10 seconds at the 95th percentile.
- Consumer lag, checkpoint duration and late-event counts have dashboards and alert thresholds.
- Stream outputs are reconciled with source totals on a schedule to show that no events were lost or counted twice.
- User-facing queries over data less than a minute old return within a target, such as 200 milliseconds, at measured peak concurrency.
- Change feeds from platform tables carry each row's change type and commit version, and consumers resume from their last processed version after an outage.

**Capabilities first relied on:** [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Change feeds](../capabilities/serving/change-feeds.md)

## Level 5: Optimising

Streaming capacity, cost and freshness are tuned continuously against business need.

- Partitions and workers scale from observed and forecast load, and expected peaks are rehearsed with load tests.
- Each pipeline's latency is reviewed against the business need, and pipelines that do not need seconds-level freshness move to cheaper micro-batch or batch.
- Replaying a window of any topic into a test environment is routine and used to check changes before release.
- Schema changes are checked against every registered consumer and rolled out without a coordinated outage.

# Capabilities in scope

[Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Change feeds](../capabilities/serving/change-feeds.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Stream processing](../capabilities/processing/stream-processing.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Streaming SQL](../capabilities/processing/streaming-sql.md)

# Related tracks

- [Ingestion and integration](track-ingestion.md): How reliably, quickly and safely the organisation brings data from source systems into the platform and keeps it in step with them.
- [Transformation engineering](track-transformation.md): How consistently transformation logic is written, tested, reused and run efficiently, from raw data to tables ready for use.
- [Data serving](track-serving.md): How well curated data reaches applications, people and operational tools at the latency, volume and reliability they need.
- [Specialised data](track-specialised-data.md): How well the organisation stores, governs and analyses data that needs specialised types, indexes or engines, such as time series, location, graphs, searchable text, media, logs and bitemporal history.

Levels follow the shared [maturity scale](maturity-scale.md).
