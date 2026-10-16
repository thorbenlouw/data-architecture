---
type: Technology
id: clickhouse-projections
title: ClickHouse projections
description: Hidden, automatically maintained copies of a table with a different sort order or pre-aggregation that the optimiser picks when they reduce the data read.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [query-acceleration, data-skipping-indexes, materialised-views]
resource: https://clickhouse.com/docs/data-modeling/projections
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Unlike materialised views they are queried through the base table and stay consistent with it. Since 25.5 a projection can store only the sorting key and _part_offset, acting as a secondary index. They cannot be chained, use joins or filters, and limit lightweight updates and deletes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute) (primary): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md) (Query and compute): Use indexes, statistics and filters to avoid scanning data that cannot match a query.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Query Acceleration Service](../snowflake/snowflake-query-acceleration-service.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Indexes and data skipping](../../capabilities/compute/data-skipping-indexes.md), [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [Denodo Platform](../independent/denodo-platform.md), [Cube Cloud](../independent/cube-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
