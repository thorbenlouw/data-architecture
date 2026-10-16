---
type: Maturity Track
id: track-serving
title: Data serving
description: How well curated data reaches applications, people and operational tools at the latency, volume and reliability they need.
covers:
- serving
- read-optimised-views
- low-latency-serving
- operational-data-store
- operational-database
- data-apis
- sql-access
- change-feeds
- reverse-etl
- audience-activation
- data-export
- online-feature-store
- event-api-catalogue
- decision-management
related_tracks: [track-data-products, track-real-time, track-data-sharing, track-analytics-bi]
levels:
- level: 1
  name: Initial
  summary: Data leaves the platform through ad hoc extracts and direct connections set up on request.
  criteria:
  - Consumers receive CSV extracts by email, shared drive or manual SFTP upload.
  - Applications connect to analytical tables with shared service accounts.
  - Business tools such as CRM are updated by people uploading spreadsheets.
  capabilities: [data-export, sql-access]
- level: 2
  name: Managed
  summary: Standard connection methods and scheduled exports exist, run by one team.
  criteria:
  - Tools connect through standard drivers such as JDBC, ODBC or Arrow Flight, using individual or service identities.
  - Recurring exports are scheduled jobs with logs and failure alerts instead of manual pulls.
  - Data that is read often is precomputed into tables or views shaped for each main consumer.
  - At least one operational tool receives modelled data, such as customer segments, from a scheduled reverse ETL sync.
  capabilities: [read-optimised-views, reverse-etl]
- level: 3
  name: Defined
  summary: Serving interfaces are standard, registered and available to teams through self-service.
  criteria:
  - Teams can publish a dataset as a managed REST or GraphQL API with authentication, paging and rate limits without writing a bespoke service.
  - Consumers that need increments subscribe to row-level change feeds instead of rereading whole tables.
  - Every API, event stream, sync, export and feed is registered in a catalogue with an owner, its schema version, its consumers and the tables it exposes.
  - Operational reporting reads from an operational data store or a synchronised operational database, not from source applications.
  - Marketing and service teams build audiences from governed data and send them to channels without engineering tickets.
  capabilities:
  - data-apis
  - change-feeds
  - operational-data-store
  - operational-database
  - audience-activation
  - event-api-catalogue
- level: 4
  name: Measured
  summary: Each serving interface has measured latency, availability and freshness targets, and automated decisions are logged so they can be explained and replayed.
  criteria:
  - Each serving interface has latency, availability and freshness targets, and a dashboard shows results against them.
  - Key-based lookups for applications come from a store built for point reads and meet a target such as 20 milliseconds at the 99th percentile.
  - Reverse ETL syncs report rows sent, rejected and failed per destination, and rejections raise alerts.
  - Online feature lookups for real-time models have their own latency target and are monitored alongside other point-read endpoints.
  - Automated decisions that combine business rules and model scores run in a decision service, and each decision is logged with its inputs, rule and model versions and outcome so it can be explained and replayed.
  capabilities: [low-latency-serving, online-feature-store, decision-management]
- level: 5
  name: Optimising
  summary: Read paths and interfaces are reshaped or retired continuously from measured demand.
  criteria:
  - API and feed schemas are versioned, use of each version is tracked per consumer, and old versions are withdrawn on a published timetable.
  - A precomputed view or cache is added when usage logs show the same query served thousands of times a day.
  - Replicas and caches are placed according to measured demand by region and time of day.
  - Consumers of bulk exports are moved to change feeds or live shares when their usage shows they only need increments.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means consumers get data through supported, governed interfaces such as SQL endpoints, APIs, change feeds and syncs to business tools, instead of ad hoc extracts, and each interface has a known owner, latency and availability. Typical blockers are pressure to grant direct database access as a shortcut, files emailed to partners, and analytical systems pressed into service as low-latency stores they were not built to be.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Data leaves the platform through ad hoc extracts and direct connections set up on request.

- Consumers receive CSV extracts by email, shared drive or manual SFTP upload.
- Applications connect to analytical tables with shared service accounts.
- Business tools such as CRM are updated by people uploading spreadsheets.

**Capabilities first relied on:** [Data export](../capabilities/serving/data-export.md), [SQL and programmatic access](../capabilities/serving/sql-access.md)

## Level 2: Managed

Standard connection methods and scheduled exports exist, run by one team.

- Tools connect through standard drivers such as JDBC, ODBC or Arrow Flight, using individual or service identities.
- Recurring exports are scheduled jobs with logs and failure alerts instead of manual pulls.
- Data that is read often is precomputed into tables or views shaped for each main consumer.
- At least one operational tool receives modelled data, such as customer segments, from a scheduled reverse ETL sync.

**Capabilities first relied on:** [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Reverse ETL](../capabilities/serving/reverse-etl.md)

## Level 3: Defined

Serving interfaces are standard, registered and available to teams through self-service.

- Teams can publish a dataset as a managed REST or GraphQL API with authentication, paging and rate limits without writing a bespoke service.
- Consumers that need increments subscribe to row-level change feeds instead of rereading whole tables.
- Every API, event stream, sync, export and feed is registered in a catalogue with an owner, its schema version, its consumers and the tables it exposes.
- Operational reporting reads from an operational data store or a synchronised operational database, not from source applications.
- Marketing and service teams build audiences from governed data and send them to channels without engineering tickets.

**Capabilities first relied on:** [Data APIs](../capabilities/serving/data-apis.md), [Change feeds](../capabilities/serving/change-feeds.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Operational database integration](../capabilities/serving/operational-database.md), [Audience building and activation](../capabilities/serving/audience-activation.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md)

## Level 4: Measured

Each serving interface has measured latency, availability and freshness targets, and automated decisions are logged so they can be explained and replayed.

- Each serving interface has latency, availability and freshness targets, and a dashboard shows results against them.
- Key-based lookups for applications come from a store built for point reads and meet a target such as 20 milliseconds at the 99th percentile.
- Reverse ETL syncs report rows sent, rejected and failed per destination, and rejections raise alerts.
- Online feature lookups for real-time models have their own latency target and are monitored alongside other point-read endpoints.
- Automated decisions that combine business rules and model scores run in a decision service, and each decision is logged with its inputs, rule and model versions and outcome so it can be explained and replayed.

**Capabilities first relied on:** [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Decision management](../capabilities/serving/decision-management.md)

## Level 5: Optimising

Read paths and interfaces are reshaped or retired continuously from measured demand.

- API and feed schemas are versioned, use of each version is tracked per consumer, and old versions are withdrawn on a published timetable.
- A precomputed view or cache is added when usage logs show the same query served thousands of times a day.
- Replicas and caches are placed according to measured demand by region and time of day.
- Consumers of bulk exports are moved to change feeds or live shares when their usage shows they only need increments.

# Capabilities in scope

[Serving and activation](../capabilities/serving/serving.md), [Audience building and activation](../capabilities/serving/audience-activation.md), [Change feeds](../capabilities/serving/change-feeds.md), [Data APIs](../capabilities/serving/data-apis.md), [Data export](../capabilities/serving/data-export.md), [Decision management](../capabilities/serving/decision-management.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Operational data store](../capabilities/serving/operational-data-store.md), [Operational database integration](../capabilities/serving/operational-database.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [SQL and programmatic access](../capabilities/serving/sql-access.md)

# Related tracks

- [Data products](track-data-products.md): How far data is managed as products with accountable owners, known consumers, explicit contracts and service levels.
- [Real-time and streaming](track-real-time.md): How well the organisation moves, processes and queries data continuously, with predictable latency and correct results, instead of in scheduled batches.
- [Data sharing](track-data-sharing.md): How safely and efficiently data is shared between teams and with external parties without unnecessary copies.
- [Analytics and BI](track-analytics-bi.md): How consistently people across the organisation explore, report on and act on data using shared definitions and governed tools.

Levels follow the shared [maturity scale](maturity-scale.md).
