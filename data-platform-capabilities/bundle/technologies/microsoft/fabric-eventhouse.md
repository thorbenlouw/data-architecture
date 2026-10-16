---
type: Technology
id: fabric-eventhouse
title: Eventhouse and KQL database
description: A Kusto-engine store for high-volume time-based and log data, queried with KQL or T-SQL in seconds, with optional copies of data in OneLake.
aliases: [Fabric Eventhouse, KQL database]
platform: platform-microsoft
kind: feature
availability: ga
realises:
- real-time-analytics
- time-series-data
- streaming-ingestion
- semi-structured-data
- observability-analytics
- approximate-query-processing
resource: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhouse
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The same engine as Azure Data Explorer and the migration target for Synapse Data Explorer. OneLake availability exposes tables as Delta for other engines. Includes native anomaly detection (preview) and a remote MCP server (preview).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Fabric Real-Time Intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon OpenSearch Service](../aws/aws-opensearch-service.md), [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md), [Apache Pinot](../open-source/apache-pinot.md), [Apache Doris](../open-source/apache-doris.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
