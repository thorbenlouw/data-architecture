---
type: Capability
id: single-node-processing
title: Single-node processing
description: Process small to medium datasets quickly on one machine using in-process engines.
aliases: [small data, DuckDB, Polars, pandas]
broader: [processing]
related:
- distributed-processing
- dataframe-apis
- credential-vending
- engine-interoperability
- local-development
depends_on: [file-formats]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The whole job runs in one process on one machine, often embedded in a Python program, notebook or application. In-process engines such as DuckDB and Polars use columnar, vectorised execution across all of a machine's cores, and can read Parquet files and open table formats straight from object storage. An aggregation over 50 GB that once needed a cluster can now run in seconds on a laptop or a single cloud virtual machine.

Most analytical datasets are small enough for this, and skipping the cluster removes start-up delay, coordination overhead and much of the cost. It suits development and testing, small and medium pipelines, data applications, and tasks running inside orchestrator workers or serverless functions. The limits are one machine's memory and disk, and no built-in recovery: if the process dies, the job starts again. Many teams combine it with distributed processing and keep clusters for the few jobs that need one.

# Key considerations

- Engines spill to disk when data exceeds memory, but run much slower. Know the largest working set before choosing.
- Many single-node processes writing to the same table need an open table format with transactions, or their writes collide.
- An embedded engine reading files directly can bypass catalogue permissions. Give it governed access, for example through vended credentials.
- Keep SQL and DataFrame code portable so a job can move to a distributed engine if it outgrows one machine.

# Questions to ask

- What share of your pipelines process less than a few hundred gigabytes per run?
- Where would single-node jobs run: laptops, orchestrator workers, containers or serverless functions?
- How will these engines get governed access to tables in the lake?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Compute provisioning options](../compute/compute-options.md), [DataFrame APIs](dataframe-apis.md), [Distributed processing](distributed-processing.md), [IDE and local development](../development-lifecycle/local-development.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [SQL query engine](../compute/sql-query-engine.md), [Storage credential vending](../storage/credential-vending.md) |
| Depends on | [Open file formats](../storage/file-formats.md) |

# Where it appears

- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric notebooks](../../technologies/microsoft/fabric-notebooks.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [pandas on Snowflake](../../technologies/snowflake/snowflake-pandas-on-snowflake.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | clickhouse-local, chDB | [chDB](../../technologies/clickhouse/clickhouse-chdb.md), [clickhouse-local](../../technologies/clickhouse/clickhouse-local.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md) |
| [SAS](../../platforms/platform-sas.md) | SAS Compute Server | [SAS 9.4 and SAS Enterprise Guide](../../technologies/sas/sas-9.md), [SAS Compute Server](../../technologies/sas/sas-compute-server.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache DataFusion](../../technologies/open-source/apache-datafusion.md), [DuckDB](../../technologies/open-source/duckdb.md), [pandas](../../technologies/open-source/pandas.md), [Polars](../../technologies/open-source/polars.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Lake Compute](../../technologies/independent/dbt-lake-compute.md) (preview), [MotherDuck](../../technologies/independent/motherduck.md) |
