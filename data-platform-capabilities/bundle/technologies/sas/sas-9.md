---
type: Technology
id: sas-9
title: SAS 9.4 and SAS Enterprise Guide
description: Earlier SAS platform of Base SAS, SAS/STAT and other products running on Windows and Linux servers, with the SAS Enterprise Guide desktop client for code and point-and-click tasks.
aliases: [SAS 9, SAS9, Base SAS, SAS Enterprise Guide, SAS EG, SAS Grid Manager]
platform: platform-sas
kind: software
availability: ga
realises: [single-node-processing, local-development]
resource: https://support.sas.com/en/software/base-sas-support.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

SAS 9.4M9 was released in June 2025, with standard support until 1 July 2030, and SAS has said a further maintenance release is planned. SAS Grid Manager handles workload management for SAS 9. From version 8.4, Enterprise Guide also connects to SAS Viya 4.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation) (primary): Process small to medium datasets quickly on one machine using in-process engines.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache DataFusion](../open-source/apache-datafusion.md), [DuckDB](../open-source/duckdb.md), [Polars](../open-source/polars.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md) | [Single-node processing](../../capabilities/processing/single-node-processing.md) |
