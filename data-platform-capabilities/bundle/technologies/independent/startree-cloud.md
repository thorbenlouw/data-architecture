---
type: Technology
id: startree-cloud
title: StarTree Cloud
description: Managed Apache Pinot service for low-latency, high-concurrency analytics on fresh event data, including user-facing and agent-facing applications.
platform: platform-independent
vendor: StarTree
kind: managed-service
availability: ga
realises:
- real-time-analytics
- low-latency-serving
- query-federation
- hybrid-data-plane
- approximate-query-processing
resource: https://startree.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Offered as SaaS with isolated data planes, as BYOC, or as BYOK (customer Kubernetes). Can query Iceberg and Delta Lake data in place. ThirdEye is the vendor's anomaly detection product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Low-latency serving](../../capabilities/serving/low-latency-serving.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md), [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Query federation](../../capabilities/compute/query-federation.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS SpeedyStore](../sas/sas-speedystore.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md), [StarRocks](../open-source/starrocks.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
