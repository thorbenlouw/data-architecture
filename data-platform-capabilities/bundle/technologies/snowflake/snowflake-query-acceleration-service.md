---
type: Technology
id: snowflake-query-acceleration-service
title: Snowflake Query Acceleration Service
description: Offloads parts of large scans and filters in eligible queries to shared serverless compute, so outlier queries finish faster without enlarging the warehouse.
aliases: [QAS]
platform: platform-snowflake
kind: feature
availability: ga
realises: [query-acceleration, elastic-scaling]
resource: https://docs.snowflake.com/en/user-guide/query-acceleration-service
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Turned on per warehouse with a maximum scale factor, and billed as serverless credits. It is on by default for new Gen2 warehouses. Adaptive warehouses manage it themselves.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute) (primary): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery BI Engine](../google-cloud/gcp-bigquery-bi-engine.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse projections](../clickhouse/clickhouse-projections.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [Denodo Platform](../independent/denodo-platform.md), [Cube Cloud](../independent/cube-cloud.md) | [Query acceleration](../../capabilities/compute/query-acceleration.md) |
