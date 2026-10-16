---
type: Technology
id: clickhouse-timeseries
title: ClickHouse TimeSeries table engine
description: Experimental engine that stores Prometheus-style metrics as samples, tags and metric tables and accepts Prometheus remote-write and remote-read traffic.
platform: platform-clickhouse
kind: feature
availability: preview
realises: [time-series-data, observability-analytics]
resource: https://clickhouse.com/docs/engines/table-engines/special/time_series
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Experimental in open source, where it must be enabled with the allow_experimental_time_series_table setting. The engine documentation still lists it as not supported in ClickHouse Cloud, but in September 2026 ClickHouse opened a waitlisted private preview of the TimeSeries engine with PromQL querying in Cloud. Most time-series workloads use ordinary MergeTree tables with time-based sorting keys, TTL and time-series aggregate functions instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types) (primary): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [AWS IoT SiteWise](../aws/aws-iot-sitewise.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Bigtable](../google-cloud/gcp-bigtable.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](../snowflake/snowflake-time-series-functions.md), [Observe by Snowflake](../snowflake/snowflake-observe.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Database](../teradata/teradata-database.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Druid](../open-source/apache-druid.md) | [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
