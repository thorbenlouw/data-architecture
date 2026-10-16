---
type: Technology
id: aws-timestream-influxdb
title: Amazon Timestream for InfluxDB
description: Managed InfluxDB instances for storing and querying time-stamped measurements with Multi-AZ failover.
platform: platform-aws
kind: managed-service
availability: ga
realises: [time-series-data, real-time-analytics]
resource: https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Offers InfluxDB 2.x instances and, since October 2025, InfluxDB 3 Core and Enterprise. It is AWS's recommended home for new time-series workloads now that Timestream for LiveAnalytics is closed to new customers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types) (primary): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Timestream

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Bigtable](../google-cloud/gcp-bigtable.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](../snowflake/snowflake-time-series-functions.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TimeSeries table engine](../clickhouse/clickhouse-timeseries.md) (preview), [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Database](../teradata/teradata-database.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
