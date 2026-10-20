---
type: Technology
id: apache-druid
title: Apache Druid
description: Real-time analytical database that ingests streams and batches and answers aggregation queries over high-cardinality event data in under a second.
aliases: [Druid]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- real-time-analytics
- streaming-ingestion
- time-series-data
- read-optimised-views
- approximate-query-processing
- idempotent-loading
- data-enrichment
resource: https://druid.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0; Imply is the main commercial vendor. Ingests directly from Kafka and Kinesis with roll-up at ingestion time. Strong for user-facing dashboards; joins are more limited than in general warehouses.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Read-optimised views](../../capabilities/serving/read-optimised-views.md) (Serving and activation): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Read-optimised views](../../capabilities/serving/read-optimised-views.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
