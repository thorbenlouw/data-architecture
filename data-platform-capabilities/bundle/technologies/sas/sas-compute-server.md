---
type: Technology
id: sas-compute-server
title: SAS Compute Server
description: Single-machine server in SAS Viya that runs traditional SAS programs, such as DATA step and procedures, and Python code in sessions started for each user or job.
aliases: [SAS Programming Runtime Environment, SPRE, compute service]
platform: platform-sas
kind: feature
availability: ga
realises: [single-node-processing]
resource: https://developer.sas.com/rest-apis/compute/docs/overview
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Compute sessions take the place of the SAS 9 Workspace Server and Stored Process Server, and compute contexts correspond to SAS 9 application servers. Python runs through PROC PYTHON in a subprocess of the session; work that needs a cluster runs in [CAS](sas-cloud-analytic-services.md). SAS/ACCESS engines connect it to external data, including one for DuckDB, added in release 2025.07, that reads Parquet files and Iceberg tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation) (primary): Process small to medium datasets quickly on one machine using in-process engines.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Polars](../open-source/polars.md), [Apache DataFusion](../open-source/apache-datafusion.md), [DuckDB](../open-source/duckdb.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
