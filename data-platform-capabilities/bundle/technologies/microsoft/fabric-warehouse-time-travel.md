---
type: Technology
id: fabric-warehouse-time-travel
title: Time travel in Fabric Data Warehouse
description: Queries warehouse tables as they were at an earlier timestamp within a retention window, with read-only warehouse snapshots for stable reporting.
platform: platform-microsoft
kind: feature
availability: ga
realises: [time-travel]
resource: https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Retention defaults to 30 days and is configurable from 1 to 120 days (configurable retention is preview). Warehouse snapshots give a fixed point-in-time copy for consumers during ETL. Time travel on lakehouse SQL analytics endpoints is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management) (primary): Query or restore a table as it was at an earlier point in time or version.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Warehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery time travel](../google-cloud/gcp-bigquery-time-travel.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Time Travel](../snowflake/snowflake-time-travel.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Time travel](../../capabilities/storage/time-travel.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md), [DuckLake](../open-source/ducklake.md), [Delta Lake](../open-source/delta-lake.md) | [Time travel](../../capabilities/storage/time-travel.md) |
