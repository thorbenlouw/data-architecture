---
type: Technology
id: clickhouse-materialized-views
title: ClickHouse incremental materialized views
description: Insert triggers that run a query over each newly inserted block and write the results to a target table, usually an AggregatingMergeTree or SummingMergeTree that merges partial aggregates.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [materialised-views, incremental-processing, sql-transformation]
resource: https://clickhouse.com/docs/materialized-view/incremental-materialized-view
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Views can be chained and a Null-engine source can keep only aggregates. Only the left-most table of a JOIN triggers the view and changes to joined tables are not reflected, so they are not a general streaming SQL engine. This is the standard pattern for pre-aggregation and for routing data from Kafka and S3Queue engines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute) (primary): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse materialized views

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift materialized views](../aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../aws/aws-glue-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake materialized views](../snowflake/snowflake-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md), [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [RisingWave](../open-source/risingwave.md), [Apache Doris](../open-source/apache-doris.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Materialize](../independent/materialize.md), [Tinybird](../independent/tinybird.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
