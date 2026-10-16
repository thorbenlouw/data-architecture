---
type: Technology
id: databricks-lakehouse-real-time
title: Databricks Lakehouse Real-Time
description: A serverless SQL warehouse type tuned for sub-second reads of Unity Catalog tables by many concurrent users and applications.
platform: platform-databricks
kind: managed-service
availability: preview
realises: [real-time-analytics, low-latency-serving]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/june
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Beta since June 2026. It is aimed at operational analytics and user-facing dashboards without copying data into a separate real-time database.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview  
**Product family:** Databricks SQL

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md), [ClickHouse server](../clickhouse/clickhouse-server.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md), [StarRocks](../open-source/starrocks.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [StarTree Cloud](../independent/startree-cloud.md), [Imply Polaris](../independent/imply-polaris.md), [Tinybird](../independent/tinybird.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
