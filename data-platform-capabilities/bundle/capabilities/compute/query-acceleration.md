---
type: Capability
id: query-acceleration
title: Query acceleration
description: Speed up repeated or selective queries using caches, precomputed results and indexes.
broader: [compute]
related:
- query-performance-analysis
- partitioning-clustering
- read-optimised-views
- semantic-layer
- real-time-analytics
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These techniques let an engine do less work per query. Some avoid recomputing: result caches return a stored answer to a repeated query, and materialised views keep precomputed joins and aggregates up to date. Some avoid reading: indexes, statistics, partition pruning and bloom filters skip data that cannot match. Others make the work cheaper: approximate algorithms trade a little accuracy for speed, and vectorised native execution processes data in batches in compiled code. A dashboard that aggregates a billion rows on every load might instead read a small precomputed aggregate, or skip most files thanks to clustering statistics.

Acceleration matters most where many users repeat similar queries, as with dashboards and embedded analytics, and where latency targets are tight. Each technique costs something, whether storage, refresh compute or staleness, and helps only within its scope. Features that pick views or indexes automatically from query history save tuning effort but can make cost and behaviour harder to predict.

# Key considerations

- Find the expensive, repeated queries in query history first, then choose the technique that fits each one, rather than switching everything on.
- Count the upkeep. Materialised views and indexes use compute every time their source data changes.
- Know how fresh accelerated answers are. Caches and views can return data older than the base tables.
- Most acceleration structures belong to one engine. They do nothing for other engines reading the same tables.

# Questions to ask

- Which queries or dashboards are slow or costly, and how often do they run?
- What latency do users expect, and how fresh must the answers be?
- How often does the underlying data change?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Narrower | [Approximate query processing](approximate-query-processing.md), [Indexes and data skipping](data-skipping-indexes.md), [Materialised views](materialised-views.md), [Result caching](result-caching.md), [Vectorised native execution](native-execution-acceleration.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Partitioning and clustering](../storage/partitioning-clustering.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Read-optimised views](../serving/read-optimised-views.md), [Real-time analytical database](real-time-analytics.md), [Semantic layer](../analytics-bi/semantic-layer.md) |

# Where it appears

- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 6 – Adaptability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI Direct Lake](../../technologies/microsoft/powerbi-direct-lake.md), [Power BI semantic models](../../technologies/microsoft/powerbi-semantic-models.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery BI Engine](../../technologies/google-cloud/gcp-bigquery-bi-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Query Acceleration Service](../../technologies/snowflake/snowflake-query-acceleration-service.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse dictionaries](../../technologies/clickhouse/clickhouse-dictionaries.md), [ClickHouse projections](../../technologies/clickhouse/clickhouse-projections.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Exadata](../../technologies/oracle/oracle-exadata.md) |
| [SAP](../../platforms/platform-sap.md) |  | [Dremio Cloud](../../technologies/sap/dremio-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Cube Core](../../technologies/open-source/cube-core.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [AtScale](../../technologies/independent/atscale.md), [Cube Cloud](../../technologies/independent/cube-cloud.md), [Denodo Platform](../../technologies/independent/denodo-platform.md) |

Narrower capabilities are realised by a further 52 technologies; see their pages.
