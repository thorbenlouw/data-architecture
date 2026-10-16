---
type: Technology
id: aws-timestream-liveanalytics
title: Amazon Timestream for LiveAnalytics
description: Serverless time-series database with memory and magnetic tiers and SQL time-series functions.
formerly: [Amazon Timestream]
platform: platform-aws
kind: managed-service
availability: deprecated
realises: [time-series-data]
resource: https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Closed to new customers since 20 June 2025; existing customers can continue. AWS points to Timestream for InfluxDB.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types) (primary): Store and query time-stamped measurements efficiently, with time-based functions and retention.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
**Product family:** Amazon Timestream  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Bigtable](../google-cloud/gcp-bigtable.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](../snowflake/snowflake-time-series-functions.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TimeSeries table engine](../clickhouse/clickhouse-timeseries.md) (preview), [ClickStack](../clickhouse/clickhouse-clickstack.md), [ClickHouse server](../clickhouse/clickhouse-server.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Database](../teradata/teradata-database.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
