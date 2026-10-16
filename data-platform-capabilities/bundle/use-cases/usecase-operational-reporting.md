---
type: Use Case
id: usecase-operational-reporting
title: Operational reporting
description: Report on current operations within minutes of events happening.
requires:
- capability: change-data-capture
  level: 3
  why: Inserts, updates and deletes must leave operational databases within seconds, without heavy queries on production.
- {capability: streaming-ingestion, level: 2, why: 'Events from applications and devices must land continuously, not in nightly batches.'}
- {capability: incremental-processing, level: 3, why: Only changed rows can be processed each cycle if reports are to stay minutes behind the source.}
- {capability: row-level-updates, level: 3, why: Captured updates and deletes have to be merged into reporting tables efficiently.}
- {capability: idempotent-loading, level: 3, why: Replayed or duplicated change events must not double-count orders or calls.}
- {capability: sql-query-engine, level: 2, why: Dashboards query fresh data continuously throughout the shift.}
- {capability: dashboards-reports, level: 2, why: Supervisors watch auto-refreshing views of current activity.}
- {capability: data-alerting, level: 2, why: 'Staff are told when a queue, backlog or target crosses a threshold, without watching a screen.'}
- {capability: freshness-monitoring, level: 3, why: A real-time view that has silently stopped updating is worse than none.}
- {capability: pipeline-monitoring, level: 3, why: Failures in always-on pipelines must reach on-call staff within minutes.}
- {capability: workload-isolation, level: 2, why: Continuous loading and dashboard queries must not slow each other down.}
- {capability: row-level-security, level: 2, why: Each site or team manager sees only their own operation.}
benefits_from:
- {capability: real-time-analytics, why: 'Gives sub-second queries over very fresh, high-volume data when many users watch at once.'}
- {capability: materialised-views, why: Keeps common aggregates up to date automatically.}
- {capability: streaming-sql, why: Lets analysts define continuous aggregations without stream-processing code.}
- {capability: event-time-windowing, why: 'Counts events in the period they happened, even when they arrive late.'}
- {capability: database-replication, why: Mirrors operational databases into the platform without building pipelines.}
- {capability: operational-data-store, why: Gives an integrated current view across several operational systems.}
- {capability: embedded-analytics, why: Puts the figures inside the operational application staff already use.}
- {capability: data-contracts, why: Source application teams agree to announce or version schema changes that would break change capture.}
personas:
- persona-business-user
- persona-data-analyst
- persona-data-engineer
- persona-software-engineer
- persona-platform-engineer
patterns: [cqrs-read-models, kappa-architecture, lambda-architecture, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Operations teams such as contact centres, warehouses, store networks, logistics and clinical services need to see what is happening now: queue lengths, orders not yet picked, today's sales against target. Traditional overnight warehouse loads are too slow for this. Changes are captured from operational databases as they happen, or events are taken straight from applications, then applied incrementally to reporting tables that dashboards and alerts read within minutes.

Good looks like dashboards that are a few minutes behind reality and say so when they fall further behind, figures that agree with the operational system once in-flight changes settle, and no noticeable extra load on production databases. People act on what they see during the shift, not the next morning.

# Non-functional requirements

- End-to-end latency from source change to dashboard of 1 to 15 minutes, agreed per report.
- Available for the full operating day, including weekends and seasonal peaks.
- Change capture adds only marginal load to source databases and is agreed with their owners.
- Late or stalled data is visibly flagged on the report itself.

# Risks

- Change capture breaks when source log retention is too short or the source schema changes.
- Out-of-order or replayed changes produce totals that do not match the source.
- Always-on compute costs far more than the overnight batch it replaced.
- Teams start treating the reporting copy as the system of record.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Inserts, updates and deletes must leave operational databases within seconds, without heavy queries on production. |
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Events from applications and devices must land continuously, not in nightly batches. |
| [Incremental processing](../capabilities/processing/incremental-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | Only changed rows can be processed each cycle if reports are to stay minutes behind the source. |
| [Row-level updates and deletes](../capabilities/storage/row-level-updates.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Captured updates and deletes have to be merged into reporting tables efficiently. |
| [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Replayed or duplicated change events must not double-count orders or calls. |
| [SQL query engine](../capabilities/compute/sql-query-engine.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Dashboards query fresh data continuously throughout the shift. |
| [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Supervisors watch auto-refreshing views of current activity. |
| [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Staff are told when a queue, backlog or target crosses a threshold, without watching a screen. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | A real-time view that has silently stopped updating is worse than none. |
| [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Failures in always-on pipelines must reach on-call staff within minutes. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Continuous loading and dashboard queries must not slow each other down. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Each site or team manager sees only their own operation. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Real-time analytical database](../capabilities/compute/real-time-analytics.md) | Gives sub-second queries over very fresh, high-volume data when many users watch at once. |
| [Materialised views](../capabilities/compute/materialised-views.md) | Keeps common aggregates up to date automatically. |
| [Streaming SQL](../capabilities/processing/streaming-sql.md) | Lets analysts define continuous aggregations without stream-processing code. |
| [Event-time windowing](../capabilities/processing/event-time-windowing.md) | Counts events in the period they happened, even when they arrive late. |
| [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md) | Mirrors operational databases into the platform without building pipelines. |
| [Operational data store](../capabilities/serving/operational-data-store.md) | Gives an integrated current view across several operational systems. |
| [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md) | Puts the figures inside the operational application staff already use. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | Source application teams agree to announce or version schema changes that would break change capture. |

# Personas

- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.

# Patterns

- [Separate read models](../patterns/cqrs-read-models.md)
- [Kappa architecture](../patterns/kappa-architecture.md)
- [Lambda architecture](../patterns/lambda-architecture.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 11 of 12 | [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 11 of 12 | [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 12 | [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 12 of 12 |  |
| [Databricks](../platforms/platform-databricks.md) | 11 of 12 | [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 10 of 12 | [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [Informatica](../platforms/platform-informatica.md) | 5 of 12 | [Incremental processing](../capabilities/processing/incremental-processing.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 7 of 12 | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Oracle](../platforms/platform-oracle.md) | 5 of 12 | [Incremental processing](../capabilities/processing/incremental-processing.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 12 | [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Teradata](../platforms/platform-teradata.md) | 3 of 12 | [Change data capture](../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| [IBM](../platforms/platform-ibm.md) | 5 of 12 | [Incremental processing](../capabilities/processing/incremental-processing.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Row-level security](../capabilities/security/row-level-security.md) |
| [Palantir](../platforms/platform-palantir.md) | 8 of 12 | [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 11 of 12 | [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) |
| [Independent vendors](../platforms/platform-independent.md) | 11 of 12 | [Row-level updates and deletes](../capabilities/storage/row-level-updates.md) |
