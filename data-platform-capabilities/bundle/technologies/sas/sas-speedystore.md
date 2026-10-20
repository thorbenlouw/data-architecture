---
type: Technology
id: sas-speedystore
title: SAS SpeedyStore
description: SingleStore database embedded in SAS Viya, so that transactional and analytical workloads and SAS analytics run against one copy of the data.
formerly: [SAS Viya with SingleStore Premium]
platform: platform-sas
kind: software
availability: ga
realises: [real-time-analytics, operational-database, sql-query-engine]
resource: https://www.sas.com/en_us/software/viya/singlestore.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

It is queried with ANSI SQL, compresses stored data, and runs on premises or in public or hybrid clouds. SAS analytics are co-located with the database to reduce data movement.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [StarRocks](../open-source/starrocks.md), [Apache Pinot](../open-source/apache-pinot.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
