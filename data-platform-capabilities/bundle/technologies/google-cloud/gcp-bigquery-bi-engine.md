---
type: Technology
id: gcp-bigquery-bi-engine
title: BigQuery BI Engine
description: In-memory cache in front of BigQuery that speeds up dashboard-style SQL queries, sized as a regional memory reservation.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [query-acceleration, result-caching]
resource: https://docs.cloud.google.com/bigquery/docs/bi-engine-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works transparently for Looker, Data Studio, Tableau, Power BI and API clients. It does not accelerate queries with row-level security, external tables, JSON columns, vector search or many joins.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute) (primary): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute): Return results of repeated queries from a cache without recomputing them.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Query Acceleration Service](../snowflake/snowflake-query-acceleration-service.md), [Snowflake persisted query results (result cache)](../snowflake/snowflake-result-cache.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md), [Result caching](../../capabilities/compute/result-caching.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse projections](../clickhouse/clickhouse-projections.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md), [ClickHouse query cache](../clickhouse/clickhouse-query-cache.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md), [Result caching](../../capabilities/compute/result-caching.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [Denodo Platform](../independent/denodo-platform.md), [Cube Cloud](../independent/cube-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
