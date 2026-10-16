---
type: Technology
id: snowflake-dynamic-tables
title: Snowflake Dynamic Tables
description: Tables defined by a query and a target lag that Snowflake keeps refreshed, incrementally where possible, working out dependency order across chains of dynamic tables.
platform: platform-snowflake
kind: feature
availability: ga
realises:
- declarative-pipelines
- incremental-processing
- sql-transformation
- asset-based-orchestration
- read-optimised-views
resource: https://docs.snowflake.com/en/user-guide/dynamic-tables-about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Refresh modes are AUTO, INCREMENTAL, FULL, ADAPTIVE and CUSTOM_INCREMENTAL, the last in preview. The minimum target lag is 60 seconds, and TARGET_LAG = DOWNSTREAM refreshes intermediate tables only when a consumer needs them. Dynamic tables can be Iceberg tables, and since September 2026 they keep refreshing incrementally after failover.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation) (primary): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Read-optimised views](../../capabilities/serving/read-optimised-views.md) (Serving and activation): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines](../databricks/databricks-lakeflow-pipelines.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Read-optimised views](../../capabilities/serving/read-optimised-views.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Spark Declarative Pipelines](../open-source/apache-spark-declarative-pipelines.md), [Apache Flink](../open-source/apache-flink.md) | [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
