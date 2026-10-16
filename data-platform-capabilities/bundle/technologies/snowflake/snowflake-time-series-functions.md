---
type: Technology
id: snowflake-time-series-functions
title: Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)
description: SQL constructs for aligning, bucketing and joining time-stamped data, including ASOF JOIN and gap filling.
platform: platform-snowflake
kind: feature
availability: ga
realises: [time-series-data]
resource: https://docs.snowflake.com/en/user-guide/querying-time-series-data
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Gap-filling (RESAMPLE) is in preview. There is no dedicated time-series storage engine.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types) (primary): Store and query time-stamped measurements efficiently, with time-based functions and retention.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [AWS IoT SiteWise](../aws/aws-iot-sitewise.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Bigtable](../google-cloud/gcp-bigtable.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TimeSeries table engine](../clickhouse/clickhouse-timeseries.md) (preview), [ClickStack](../clickhouse/clickhouse-clickstack.md), [ClickHouse server](../clickhouse/clickhouse-server.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Database](../teradata/teradata-database.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
