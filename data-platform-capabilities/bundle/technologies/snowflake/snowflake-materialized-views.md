---
type: Technology
id: snowflake-materialized-views
title: Snowflake materialized views
description: Stores the results of a single-table query and keeps them up to date automatically in the background, so queries read precomputed results.
platform: platform-snowflake
kind: feature
availability: ga
realises: [materialised-views]
resource: https://docs.snowflake.com/en/user-guide/views-materialized
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition. Materialised views are limited to one table, with no joins. Use Dynamic Tables for multi-table or pipeline-style precomputation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute) (primary): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift materialized views](../aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../aws/aws-glue-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md), [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md), [ClickHouse projections](../clickhouse/clickhouse-projections.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [RisingWave](../open-source/risingwave.md), [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [Apache Doris](../open-source/apache-doris.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Materialize](../independent/materialize.md), [Tinybird](../independent/tinybird.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
