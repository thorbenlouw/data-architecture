---
type: Capability
id: time-series-data
title: Time-series data
description: Store and query time-stamped measurements efficiently, with time-based functions and retention.
broader: [specialised-data]
related: [iot-ingestion, event-time-windowing, real-time-analytics, observability-analytics, storage-tiering]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A time series is a sequence of measurements, each with a timestamp, the identity of its source and one or more values, such as a meter reading every 15 minutes or a price every millisecond. Time-series storage organises data by source and time, compresses it heavily by exploiting regular timestamps and slowly changing values, and drops old data automatically. Typical functions group readings into time buckets, downsample, interpolate and fill gaps, compute moving averages, and perform as-of joins that match each event with the latest value recorded before it.

It is central to industrial telemetry, energy, finance, monitoring and IoT, where volumes are high, most queries look at recent windows and older data is kept at lower resolution. Options range from dedicated time-series databases to time-series functions and partitioning in a general analytical engine. A key sizing factor is cardinality, the number of distinct series: millions of sensors with many tags strain some engines. Observability analytics applies the same ideas to system metrics.

# Key considerations

- Estimate the number of distinct series and tag combinations. High cardinality is the usual scaling limit.
- Plan retention and downsampling tiers, for example raw readings for 30 days and hourly summaries for years.
- As-of joins and gap filling are missing or slow in some general engines. Test them on realistic volumes.
- Decide how late and corrected readings are handled. Devices send both often.

# Questions to ask

- How many series, at what sampling rate, and how long must raw data be kept?
- Are the main queries for the latest value, aggregates over windows, or comparisons across long histories?
- Must measurements be joined with business data such as assets, customers or prices?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Related | [Edge data processing](../processing/edge-data-processing.md), [Event-time windowing](../processing/event-time-windowing.md), [IoT and telemetry ingestion](../ingestion-integration/iot-ingestion.md), [Observability data analytics](observability-analytics.md), [Pretrained predictive models](../machine-learning/pretrained-predictive-models.md), [Real-time analytical database](../compute/real-time-analytics.md), [Storage tiering and lifecycle](../storage/storage-tiering.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 3)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 2, Managed)
- **Frameworks:** [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-210 to 8000-230 – Sensor data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Timestream for InfluxDB](../../technologies/aws/aws-timestream-influxdb.md), [AWS IoT SiteWise](../../technologies/aws/aws-iot-sitewise.md), [Amazon Timestream for LiveAnalytics](../../technologies/aws/aws-timestream-liveanalytics.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Explorer](../../technologies/microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Bigtable](../../technologies/google-cloud/gcp-bigtable.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake time-series functions (ASOF JOIN, TIME_SLICE, RESAMPLE)](../../technologies/snowflake/snowflake-time-series-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse server](../../technologies/clickhouse/clickhouse-server.md), [ClickHouse TimeSeries table engine](../../technologies/clickhouse/clickhouse-timeseries.md) (preview), [ClickStack](../../technologies/clickhouse/clickhouse-clickstack.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database](../../technologies/teradata/teradata-database.md), [Teradata in-database analytics functions](../../technologies/teradata/teradata-in-database-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Contour and Quiver](../../technologies/palantir/palantir-contour-quiver.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Druid](../../technologies/open-source/apache-druid.md) |
