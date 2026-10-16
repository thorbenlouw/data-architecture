---
type: Technology
id: fabric-materialized-lake-views
title: Fabric materialized lake views
description: Declarative Spark SQL views persisted as Delta tables, refreshed incrementally in dependency order, with optional data quality constraints.
platform: platform-microsoft
kind: feature
availability: ga
realises:
- declarative-pipelines
- materialised-views
- incremental-processing
- data-quality-rules
- table-lineage
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/materialized-lake-views/overview-materialized-lake-view
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA from March 2026; PySpark authoring is preview and full-refresh only. Incremental refresh needs Delta change data feed on sources. Constraints can drop or fail on violating rows; lineage view shows dependencies and violation counts. The Fabric answer to Databricks Lakeflow Declarative Pipelines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation) (primary): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Engineering

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift materialized views](../aws/aws-redshift-materialized-views.md), [AWS Glue Data Catalog materialized views](../aws/aws-glue-materialized-views.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md), [BigQuery materialized views](../google-cloud/gcp-bigquery-materialized-views.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [Apache Flink](../open-source/apache-flink.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
