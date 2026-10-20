---
type: Technology
id: snowflake-interactive-tables
title: Snowflake interactive tables and interactive warehouses
description: A table type and a matching warehouse type built for sub-second, highly concurrent queries such as user-facing dashboards and data APIs.
platform: platform-snowflake
kind: feature
availability: ga
realises: [real-time-analytics, low-latency-serving, read-optimised-views]
resource: https://docs.snowflake.com/en/user-guide/interactive
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generally available since December 2025. Interactive warehouses limit queries to 5 seconds, falling back to a standard warehouse for longer ones, and have a minimum auto-suspend of 24 hours. Interactive tables need CLUSTER BY, refresh from a source table with a target lag, and accept no DML except INSERT OVERWRITE.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Read-optimised views](../../capabilities/serving/read-optimised-views.md) (Serving and activation): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md), [ClickHouse server](../clickhouse/clickhouse-server.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md), [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md) | [Read-optimised views](../../capabilities/serving/read-optimised-views.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [StarTree Cloud](../independent/startree-cloud.md), [Imply Polaris](../independent/imply-polaris.md), [Tinybird](../independent/tinybird.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
