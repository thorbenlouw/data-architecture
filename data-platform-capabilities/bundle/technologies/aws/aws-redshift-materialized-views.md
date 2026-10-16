---
type: Technology
id: aws-redshift-materialized-views
title: Amazon Redshift materialized views
description: Precomputed query results in Redshift that refresh incrementally where possible and can be used automatically to rewrite matching queries.
platform: platform-aws
kind: feature
availability: ga
realises: [materialised-views, incremental-processing]
resource: https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Automated materialised views are created by Redshift from workload patterns. Views can be defined over local, data-shared, streaming and Iceberg sources.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute) (primary): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake materialized views](../snowflake/snowflake-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md), [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md), [ClickHouse projections](../clickhouse/clickhouse-projections.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [RisingWave](../open-source/risingwave.md), [Apache Doris](../open-source/apache-doris.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Materialize](../independent/materialize.md), [Tinybird](../independent/tinybird.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
