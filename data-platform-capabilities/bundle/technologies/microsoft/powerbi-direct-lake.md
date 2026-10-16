---
type: Technology
id: powerbi-direct-lake
title: Power BI Direct Lake
description: A semantic model storage mode that loads Delta tables from OneLake into memory on demand, avoiding scheduled import refreshes and DirectQuery latency.
aliases: [Direct Lake on OneLake, Direct Lake on SQL endpoints]
platform: platform-microsoft
kind: feature
availability: ga
realises: [query-acceleration, engine-interoperability]
resource: https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Two variants. Direct Lake on SQL endpoints can fall back to DirectQuery; Direct Lake on OneLake can span several items and mix with Import tables but has no fallback. Guardrails depend on capacity size, so table maintenance and V-Order matter.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute) (primary): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Query Acceleration Service](../snowflake/snowflake-query-acceleration-service.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse projections](../clickhouse/clickhouse-projections.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [Denodo Platform](../independent/denodo-platform.md), [Cube Cloud](../independent/cube-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
