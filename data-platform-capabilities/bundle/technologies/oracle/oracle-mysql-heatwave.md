---
type: Technology
id: oracle-mysql-heatwave
title: MySQL HeatWave
description: Managed MySQL service with an in-memory, scale-out query accelerator for analytics on transactional data, and HeatWave Lakehouse for querying files in object storage.
aliases: [HeatWave, HeatWave MySQL, HeatWave Lakehouse]
formerly: [MySQL Database Service]
platform: platform-oracle
kind: managed-service
availability: ga
realises: [real-time-analytics, operational-database, query-federation, columnar-storage]
resource: https://dev.mysql.com/doc/mysql-analytics/en/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs OLTP and analytics in one MySQL service without ETL to a separate warehouse. HeatWave Lakehouse reads CSV, Parquet and JSON from object storage. Available on OCI, AWS and Azure.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Operational database integration](../../capabilities/serving/operational-database.md) (Serving and activation): Run transactional databases as part of the platform, with data flowing to and from analytical storage without separate pipelines.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** HeatWave

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md), [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Operational database integration](../../capabilities/serving/operational-database.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Operational database integration](../../capabilities/serving/operational-database.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md), [StarRocks](../open-source/starrocks.md) | [Query federation](../../capabilities/compute/query-federation.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [StarTree Cloud](../independent/startree-cloud.md), [Imply Polaris](../independent/imply-polaris.md), [Tinybird](../independent/tinybird.md) | [Query federation](../../capabilities/compute/query-federation.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
