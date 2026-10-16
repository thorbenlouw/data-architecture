---
type: Technology
id: clickhouse-refreshable-materialized-views
title: ClickHouse refreshable materialized views
description: Views that rerun a full query on a schedule and replace or append to a target table, with optional dependencies between views.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [materialised-views, sql-transformation, workflow-orchestration]
resource: https://clickhouse.com/docs/materialized-view/refreshable-materialized-view
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Suited to complex joins and batch denormalisation that are hard to maintain incrementally; dependencies (DEPENDS ON) give a simple DAG that can replace a small scheduler. In Cloud they only run on read-write services; refresh coordination across restarts relies on Keeper.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute) (primary): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse materialized views

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift materialized views](../aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../aws/aws-glue-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake materialized views](../snowflake/snowflake-materialized-views.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md), [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [RisingWave](../open-source/risingwave.md), [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [Apache Doris](../open-source/apache-doris.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Materialize](../independent/materialize.md), [Tinybird](../independent/tinybird.md) | [Materialised views](../../capabilities/compute/materialised-views.md) |
