---
type: Technology
id: apache-spark-declarative-pipelines
title: Spark Declarative Pipelines
description: Spark framework in which you declare datasets and the queries that produce them, and Spark works out execution order, parallelism, checkpoints and retries.
aliases: [Apache Spark Declarative Pipelines, SDP]
platform: platform-open-source
kind: open-source
availability: ga
realises: [declarative-pipelines, incremental-processing, materialised-views]
resource: https://www.databricks.com/blog/introducing-apache-sparkr-41
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Added in Apache Spark 4.1 (December 2025) after Databricks contributed the core of what it now calls [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) (formerly Delta Live Tables). Pipelines are written in Python or SQL and run from a CLI or over Spark Connect. Expect the Databricks managed version to have more features than the open-source one.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation) (primary): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift materialized views](../aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../aws/aws-glue-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md), [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
