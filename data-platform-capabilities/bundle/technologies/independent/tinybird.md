---
type: Technology
id: tinybird
title: Tinybird
description: Managed ClickHouse platform that ingests events and files, transforms them with SQL pipes and incremental materialised views, and publishes the results as authenticated HTTP API endpoints.
platform: platform-independent
vendor: Tinybird
kind: saas
availability: ga
realises: [real-time-analytics, data-apis, streaming-ingestion, materialised-views, ci-cd]
resource: https://www.tinybird.co/docs
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tinybird Forward is the current product, and Tinybird Classic is the legacy one. Resources are defined as code and deployed through the CLI or CI/CD, with Tinybird Local and cloud branches for testing. Enterprise plans get a dedicated cluster, and self-managed regions are possible.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon OpenSearch Service](../aws/aws-opensearch-service.md), [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md), [ClickHouse server](../clickhouse/clickhouse-server.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md), [StarRocks](../open-source/starrocks.md) | [Materialised views](../../capabilities/compute/materialised-views.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
