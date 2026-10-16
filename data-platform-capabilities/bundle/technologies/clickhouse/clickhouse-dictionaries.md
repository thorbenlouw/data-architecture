---
type: Technology
id: clickhouse-dictionaries
title: ClickHouse dictionaries
description: In-memory key-value lookups loaded from ClickHouse tables, external databases, HTTP or files, refreshed on a set lifetime and queried with dictGet functions or as tables.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [query-acceleration, query-federation, low-latency-serving, data-enrichment]
resource: https://clickhouse.com/docs/sql-reference/dictionaries
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used to enrich facts with reference attributes faster than a JOIN, including IP-range and polygon lookups. In Cloud they must be created with DDL rather than configuration files.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute) (primary): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Query Acceleration Service](../snowflake/snowflake-query-acceleration-service.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [AtScale](../independent/atscale.md), [Cube Cloud](../independent/cube-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md), [Query federation](../../capabilities/compute/query-federation.md) |
