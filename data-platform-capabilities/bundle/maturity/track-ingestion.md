---
type: Maturity Track
id: track-ingestion
title: Ingestion and integration
description: How reliably, quickly and safely the organisation brings data from source systems into the platform and keeps it in step with them.
covers:
- ingestion-integration
- batch-ingestion
- file-ingestion
- database-extraction
- saas-connectors
- api-ingestion
- bulk-data-transfer
- change-data-capture
- event-streaming
- message-queuing
- streaming-ingestion
- iot-ingestion
- behavioural-event-collection
- stream-to-table
- database-replication
- unstructured-ingestion
- managed-file-transfer
- application-integration
- custom-connectors
- b2b-edi-integration
- mainframe-integration
- idempotent-loading
- edge-data-processing
related_tracks: [track-real-time, track-orchestration, track-transformation, track-platform-migration]
levels:
- level: 1
  name: Initial
  summary: Sources are loaded by exports and scripts that individuals write and run.
  criteria:
  - Data arrives through hand-run exports, spreadsheet uploads or scripts on individual laptops or servers.
  - Each source is reloaded in full because no high-water mark or change log is tracked.
  - Source credentials are written into scripts or belong to personal accounts.
  - Nobody can produce a list of which sources feed the platform and how often.
  capabilities: [batch-ingestion, file-ingestion, database-extraction, api-ingestion]
- level: 2
  name: Managed
  summary: A team runs scheduled, incremental loads on a chosen tool and knows when they fail.
  criteria:
  - Ingestion jobs run on a scheduler or managed connector service that keeps run history, not from personal machines.
  - High-volume tables load incrementally using a watermark column or log-based change data capture.
  - A failed load alerts the owning team and can be restarted from the last successful batch.
  - A register lists each source with its owner, load method, schedule and the partner or file transfer route where one applies.
  capabilities:
  - saas-connectors
  - change-data-capture
  - managed-file-transfer
  - bulk-data-transfer
  - b2b-edi-integration
- level: 3
  name: Defined
  summary: A documented set of ingestion patterns is offered as self-service templates, and every load is safe to replay.
  criteria:
  - Each supported pattern (file drop, database replication, SaaS connector, API, event stream, document store) has a template that teams configure without the platform team writing code.
  - Replaying a file or batch produces no duplicate rows, and a pipeline test proves it.
  - Landed data carries source, load time and batch identifier columns and is registered in the catalogue on arrival.
  - Source schema changes are detected before loading, and the owning team is alerted to apply or block each one.
  - Sources without a prebuilt connector, including mainframe files, are built on a shared connector framework rather than one-off scripts.
  capabilities:
  - idempotent-loading
  - custom-connectors
  - database-replication
  - event-streaming
  - message-queuing
  - streaming-ingestion
  - stream-to-table
  - unstructured-ingestion
  - mainframe-integration
- level: 4
  name: Measured
  summary: Every source has freshness and completeness targets, and results against them are reported.
  criteria:
  - Each source has a freshness and completeness target, and a dashboard shows breaches by source and owner.
  - Connector failures, API throttling, replication lag and errors in application integration flows are monitored against alert thresholds.
  - Events from web and mobile apps are validated against a schema or tracking plan at collection, with rejection rates reported per producer.
  - Device and gateway telemetry arrives over authenticated connections, and dropped or delayed messages are counted per device fleet.
  - The time to onboard a new source is recorded and compared with a target, such as five working days.
  capabilities: [behavioural-event-collection, iot-ingestion, application-integration]
- level: 5
  name: Optimising
  summary: Onboarding is generated from requests or contracts, and extraction methods and windows are tuned from load and trend data.
  criteria:
  - A new source is onboarded from a request or contract, with its pipeline, catalogue entry and quality checks generated automatically.
  - The load that extraction puts on each source system is measured, and full extracts that exceed an agreed share of source capacity are moved to log-based capture or a replica.
  - Source application teams are told automatically, from their own release pipelines, when a planned change would break an ingestion feed.
  - Load windows and capacity are forecast from source volume trends, and alerts fire before a window is missed.
  - Filtering and buffering on devices or sites is managed centrally, with versioned logic deployed remotely.
  capabilities: [edge-data-processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means new sources are onboarded in days from a set of supported patterns instead of weeks of bespoke scripting, loads can be rerun without double counting, and source changes are caught before they break anything downstream. Progress is usually blocked by a long tail of one-off scripts owned by individuals, sources that offer no change-tracking column or log access, and no agreement with source owners about schema changes and load windows.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Sources are loaded by exports and scripts that individuals write and run.

- Data arrives through hand-run exports, spreadsheet uploads or scripts on individual laptops or servers.
- Each source is reloaded in full because no high-water mark or change log is tracked.
- Source credentials are written into scripts or belong to personal accounts.
- Nobody can produce a list of which sources feed the platform and how often.

**Capabilities first relied on:** [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md), [Database extraction](../capabilities/ingestion-integration/database-extraction.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md)

## Level 2: Managed

A team runs scheduled, incremental loads on a chosen tool and knows when they fail.

- Ingestion jobs run on a scheduler or managed connector service that keeps run history, not from personal machines.
- High-volume tables load incrementally using a watermark column or log-based change data capture.
- A failed load alerts the owning team and can be restarted from the last successful batch.
- A register lists each source with its owner, load method, schedule and the partner or file transfer route where one applies.

**Capabilities first relied on:** [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md)

## Level 3: Defined

A documented set of ingestion patterns is offered as self-service templates, and every load is safe to replay.

- Each supported pattern (file drop, database replication, SaaS connector, API, event stream, document store) has a template that teams configure without the platform team writing code.
- Replaying a file or batch produces no duplicate rows, and a pipeline test proves it.
- Landed data carries source, load time and batch identifier columns and is registered in the catalogue on arrival.
- Source schema changes are detected before loading, and the owning team is alerted to apply or block each one.
- Sources without a prebuilt connector, including mainframe files, are built on a shared connector framework rather than one-off scripts.

**Capabilities first relied on:** [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md)

## Level 4: Measured

Every source has freshness and completeness targets, and results against them are reported.

- Each source has a freshness and completeness target, and a dashboard shows breaches by source and owner.
- Connector failures, API throttling, replication lag and errors in application integration flows are monitored against alert thresholds.
- Events from web and mobile apps are validated against a schema or tracking plan at collection, with rejection rates reported per producer.
- Device and gateway telemetry arrives over authenticated connections, and dropped or delayed messages are counted per device fleet.
- The time to onboard a new source is recorded and compared with a target, such as five working days.

**Capabilities first relied on:** [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Application integration](../capabilities/ingestion-integration/application-integration.md)

## Level 5: Optimising

Onboarding is generated from requests or contracts, and extraction methods and windows are tuned from load and trend data.

- A new source is onboarded from a request or contract, with its pipeline, catalogue entry and quality checks generated automatically.
- The load that extraction puts on each source system is measured, and full extracts that exceed an agreed share of source capacity are moved to log-based capture or a replica.
- Source application teams are told automatically, from their own release pipelines, when a planned change would break an ingestion feed.
- Load windows and capacity are forecast from source volume trends, and alerts fire before a window is missed.
- Filtering and buffering on devices or sites is managed centrally, with versioned logic deployed remotely.

**Capabilities first relied on:** [Edge data processing](../capabilities/processing/edge-data-processing.md)

# Capabilities in scope

[Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md), [API ingestion](../capabilities/ingestion-integration/api-ingestion.md), [Application integration](../capabilities/ingestion-integration/application-integration.md), [B2B and EDI integration](../capabilities/ingestion-integration/b2b-edi-integration.md), [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Bulk and offline transfer](../capabilities/ingestion-integration/bulk-data-transfer.md), [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [File ingestion](../capabilities/ingestion-integration/file-ingestion.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Mainframe data integration](../capabilities/ingestion-integration/mainframe-integration.md), [Managed file transfer](../capabilities/ingestion-integration/managed-file-transfer.md), [Message queuing](../capabilities/ingestion-integration/message-queuing.md), [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md), [Stream-to-table materialisation](../capabilities/ingestion-integration/stream-to-table.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Unstructured data ingestion](../capabilities/ingestion-integration/unstructured-ingestion.md)

# Related tracks

- [Real-time and streaming](track-real-time.md): How well the organisation moves, processes and queries data continuously, with predictable latency and correct results, instead of in scheduled batches.
- [Orchestration](track-orchestration.md): How dependably the organisation schedules, sequences and recovers the jobs that move and transform data.
- [Transformation engineering](track-transformation.md): How consistently transformation logic is written, tested, reused and run efficiently, from raw data to tables ready for use.
- [Platform migration and portability](track-platform-migration.md): How safely and predictably the organisation moves workloads, code and data to new platforms, and how freely it can choose where the platform runs.

Levels follow the shared [maturity scale](maturity-scale.md).
