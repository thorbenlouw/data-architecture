---
type: Capability
id: real-time-analytics
title: Real-time analytical database
description: Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
aliases: [real-time OLAP, user-facing analytics]
broader: [compute, serving]
related:
- embedded-analytics
- streaming-ingestion
- low-latency-serving
- observability-analytics
- stream-processing
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Real-time analytical databases take in events continuously, often hundreds of thousands per second from a stream, and make them queryable within seconds. They answer aggregations over billions of rows in tens of milliseconds and serve thousands of concurrent queries. They do this with columnar storage, often on local disks, heavy indexing, pre-aggregation as data arrives, data sorted by time and key, and engines tuned for short queries rather than large joins. A delivery app that shows each restaurant its orders and ratings for the last hour on every page load is a typical case. Apache Druid, Apache Pinot and ClickHouse are well-known open-source examples.

They are needed when analytics face customers or operations, as in in-product dashboards, monitoring, fraud views and personalisation, where a warehouse's latency and concurrency fall short. They give up flexibility in return: large joins, frequent updates and ad hoc modelling are weaker, and data often has to be shaped for known queries. Low-latency serving returns individual records; these databases return aggregates over many records.

# Key considerations

- Design tables around the queries. Sort keys, pre-aggregation and rollups decide performance, and changing them later can mean reloading the data.
- Updates and deletes are often limited or expensive. Check how corrections, late events and privacy deletions are handled.
- Joins are usually weaker than in a warehouse. Denormalise as data arrives, or keep joined dimensions small.
- Another storage engine adds operations, security and cost. Confirm that the latency and concurrency targets really need it.

# Questions to ask

- What query latency and concurrency do users need, and are they internal or external?
- How fresh must results be, measured from event to answer?
- How much do the queries vary, and can they be known in advance?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md), [Serving and activation](../serving/serving.md) |
| Related | [Approximate query processing](approximate-query-processing.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Low-latency serving](../serving/low-latency-serving.md), [Observability data analytics](../specialised-data/observability-analytics.md), [Query acceleration](query-acceleration.md), [Stream processing](../processing/stream-processing.md), [Streaming ingestion](../ingestion-integration/streaming-ingestion.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 4, Measured) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon OpenSearch Service](../../technologies/aws/aws-opensearch-service.md), [Amazon Timestream for InfluxDB](../../technologies/aws/aws-timestream-influxdb.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Eventhouse / KQL database | [Azure Data Explorer](../../technologies/microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../../technologies/microsoft/fabric-real-time-dashboards.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | interactive tables and interactive warehouses | [Snowflake interactive tables and interactive warehouses](../../technologies/snowflake/snowflake-interactive-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakehouse Real-Time | [Databricks Lakehouse Real-Time](../../technologies/databricks/databricks-lakehouse-real-time.md) (preview) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickHouse (real-time analytical database) | [ClickHouse Cloud](../../technologies/clickhouse/clickhouse-cloud.md), [ClickHouse server](../../technologies/clickhouse/clickhouse-server.md) |
| [Oracle](../../platforms/platform-oracle.md) | HeatWave | [MySQL HeatWave](../../technologies/oracle/oracle-mysql-heatwave.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Doris](../../technologies/open-source/apache-doris.md), [Apache Druid](../../technologies/open-source/apache-druid.md), [Apache Fluss (incubating)](../../technologies/open-source/apache-fluss.md) (preview), [Apache Pinot](../../technologies/open-source/apache-pinot.md), [StarRocks](../../technologies/open-source/starrocks.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Imply Polaris](../../technologies/independent/imply-polaris.md), [StarTree Cloud](../../technologies/independent/startree-cloud.md), [Tinybird](../../technologies/independent/tinybird.md) |
