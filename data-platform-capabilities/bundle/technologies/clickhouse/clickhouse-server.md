---
type: Technology
id: clickhouse-server
title: ClickHouse server
description: Open-source column-oriented SQL database that runs analytical queries over very large tables with vectorised, parallel execution on single servers or sharded and replicated clusters.
aliases: [ClickHouse OSS, open-source ClickHouse]
platform: platform-clickhouse
kind: open-source
availability: ga
realises:
- real-time-analytics
- sql-query-engine
- distributed-processing
- time-series-data
- approximate-query-processing
resource: https://clickhouse.com/docs
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0 licence; the same binary also provides clickhouse-client, clickhouse-local and ClickHouse Keeper. Self-managed clusters scale with shards plus ReplicatedMergeTree replicas, and parallel replicas can split one query across replicas. Time-series work relies on date/time functions, window functions, ASOF JOIN and WITH FILL rather than a separate engine.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [StarRocks](../open-source/starrocks.md), [Apache Druid](../open-source/apache-druid.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
