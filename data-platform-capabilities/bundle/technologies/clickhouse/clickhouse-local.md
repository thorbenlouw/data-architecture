---
type: Technology
id: clickhouse-local
title: clickhouse-local
description: Mode of the ClickHouse binary that runs SQL over local or remote files and piped data without starting a server.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [single-node-processing, local-development, file-formats]
resource: https://clickhouse.com/docs/operations/utilities/clickhouse-local
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Useful for format conversion, ad hoc file analysis and testing SQL before deployment; not intended for serving applications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation) (primary): Process small to medium datasets quickly on one machine using in-process engines.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.
- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache DataFusion](../open-source/apache-datafusion.md), [DuckDB](../open-source/duckdb.md), [Polars](../open-source/polars.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
