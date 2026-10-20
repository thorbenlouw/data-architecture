---
type: Technology
id: clickhouse-chdb
title: chDB
description: In-process OLAP engine built on ClickHouse that runs inside Python, Go, Rust, Node.js or C/C++ programs, with a pandas-compatible DataStore API.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [single-node-processing, dataframe-apis, local-development]
resource: https://clickhouse.com/docs/chdb
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0 and maintained under ClickHouse. Comparable to DuckDB for notebooks and embedded analytics; it can query files, DataFrames and remote ClickHouse services. The DataStore API is new.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation) (primary): Process small to medium datasets quickly on one machine using in-process engines.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS 9.4 and SAS Enterprise Guide](../sas/sas-9.md), [SAS Compute Server](../sas/sas-compute-server.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Polars](../open-source/polars.md), [Apache DataFusion](../open-source/apache-datafusion.md), [pandas](../open-source/pandas.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
