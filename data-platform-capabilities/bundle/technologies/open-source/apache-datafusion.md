---
type: Technology
id: apache-datafusion
title: Apache DataFusion
description: Extensible query engine library in Rust, built on Apache Arrow, that projects embed to get SQL and DataFrame execution.
aliases: [DataFusion, DataFusion Comet, Ballista]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- single-node-processing
- sql-query-engine
- dataframe-apis
- user-defined-functions
- native-execution-acceleration
resource: https://datafusion.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Graduated from Arrow subproject to ASF top-level project in 2024. Subprojects include Comet (a native accelerator for Spark) and Ballista (distributed execution). Many newer engines and databases are built on it, so architects meet it inside other products more often than on its own.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation) (primary): Process small to medium datasets quickly on one machine using in-process engines.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
- [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) (Query and compute): Speed up engines by running operators in native, vectorised code without changing user code.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Compute Server](../sas/sas-compute-server.md), [SAS 9.4 and SAS Enterprise Guide](../sas/sas-9.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
