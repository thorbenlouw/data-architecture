---
type: Technology
id: databricks-predictive-optimization
title: Databricks predictive optimization
description: Runs OPTIMIZE, VACUUM and ANALYZE automatically on Unity Catalog managed tables and chooses liquid clustering keys, based on how each table is used.
platform: platform-databricks
kind: feature
availability: ga
realises: [table-maintenance, cost-optimisation]
resource: https://docs.databricks.com/aws/en/optimizations/predictive-optimization
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Enabled by default for accounts created since November 2024, with existing accounts rolled out by August 2026. It does not run on external tables. It is billed as serverless usage and logged in a system table.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management) (primary): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Delta Lake on Databricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Delta table optimization and V-Order](../microsoft/fabric-delta-optimisation-v-order.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake clustering keys and Automatic Clustering](../snowflake/snowflake-clustering-keys.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md), [MergeTree table engine family](../clickhouse/clickhouse-mergetree.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration FinOps](../informatica/informatica-cdi-finops.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Lakehouse Optimizer](../cloudera/cloudera-lakehouse-optimizer.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Tableflow](../ibm/confluent-tableflow.md), [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md) | [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
