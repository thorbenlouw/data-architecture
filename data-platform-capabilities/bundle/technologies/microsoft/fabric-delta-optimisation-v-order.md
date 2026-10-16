---
type: Technology
id: fabric-delta-optimisation-v-order
title: Fabric Delta table optimization and V-Order
description: Write-time sorting and compression (V-Order) plus compaction and vacuum operations that keep Fabric Delta tables fast to read.
aliases: [V-Order]
platform: platform-microsoft
kind: feature
availability: ga
realises: [table-maintenance, columnar-storage]
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/delta-optimization-and-v-order
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

V-Order output is standard Parquet, readable by any engine, and particularly helps Direct Lake. Table maintenance can run from the lakehouse UI, APIs or a pipeline activity (preview).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management) (primary): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Engineering

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake clustering keys and Automatic Clustering](../snowflake/snowflake-clustering-keys.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks predictive optimization](../databricks/databricks-predictive-optimization.md), [Unity Catalog managed tables](../databricks/databricks-unity-catalog-managed-tables.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [MergeTree table engine family](../clickhouse/clickhouse-mergetree.md), [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Lakehouse Optimizer](../cloudera/cloudera-lakehouse-optimizer.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Tableflow](../ibm/confluent-tableflow.md), [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
