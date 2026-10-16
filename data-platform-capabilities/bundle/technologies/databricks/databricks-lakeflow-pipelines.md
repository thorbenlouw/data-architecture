---
type: Technology
id: databricks-lakeflow-pipelines
title: Lakeflow pipelines
description: A declarative framework in which you define streaming tables, materialised views and flows in SQL or Python. The platform then works out dependencies, incremental refresh, retries and infrastructure.
aliases: [DLT]
formerly: [Delta Live Tables, Lakeflow Declarative Pipelines, Lakeflow Spark Declarative Pipelines]
platform: platform-databricks
kind: managed-service
availability: ga
realises:
- declarative-pipelines
- incremental-processing
- materialised-views
- streaming-sql
- streaming-inference
- read-optimised-views
resource: https://docs.databricks.com/aws/en/ldp/where-is-dlt
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on and compatible with open-source [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md) (Spark 4.1 and later). The product was called Delta Live Tables until June 2025, then Lakeflow Declarative Pipelines and, from November 2025, Lakeflow Spark Declarative Pipelines; classic SKUs and event-log schemas still say "DLT". AUTO CDC flows apply SCD type 1 and 2 changes. Materialised views and streaming tables created from Databricks SQL run as serverless standalone pipelines. Parameters (GA October 2026), the Lakeflow Pipelines Editor (GA May 2026), unit testing (Beta) and Structured Streaming real-time mode (Public Preview) are also available.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation) (primary): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Materialised views](../../capabilities/compute/materialised-views.md) (Query and compute): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Streaming inference](../../capabilities/mlops/streaming-inference.md) (ML operations): Apply models to events as they flow through a stream.
- [Read-optimised views](../../capabilities/serving/read-optimised-views.md) (Serving and activation): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Read-optimised views](../../capabilities/serving/read-optimised-views.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [Apache Flink](../open-source/apache-flink.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Materialised views](../../capabilities/compute/materialised-views.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md) |
