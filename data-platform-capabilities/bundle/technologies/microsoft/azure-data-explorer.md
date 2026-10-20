---
type: Technology
id: azure-data-explorer
title: Azure Data Explorer
description: A managed Kusto cluster for fast analytical queries over large volumes of log, telemetry and time-series data using KQL.
aliases: [ADX, Kusto]
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- real-time-analytics
- time-series-data
- semi-structured-data
- observability-analytics
- approximate-query-processing
resource: https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Same engine as Fabric Eventhouse, Azure Monitor Logs and Microsoft Defender hunting. Choose ADX when you need dedicated clusters in your subscription, Eventhouse when on Fabric capacity.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md), [ClickHouse TimeSeries table engine](../clickhouse/clickhouse-timeseries.md) (preview) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md), [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
