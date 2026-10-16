---
type: Technology
id: dbt-fusion-engine
title: dbt v2 engine
description: Rust-based dbt v2 engine, distributed as "dbt", that parses and understands SQL across warehouse dialects, so it can catch errors and resolve dependencies before anything runs in the warehouse.
formerly: [dbt Fusion engine, dbt Fusion]
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: software
availability: ga
realises: [transformation-as-code, local-development, incremental-processing, column-lineage]
resource: https://docs.getdbt.com/docs/fusion/about-fusion
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Called the dbt Fusion engine until dbt v2 reached GA on 15 September 2026, when it became the default "dbt" distribution. It shares its runtime and language specification with [dbt OSS](../open-source/dbt-oss.md), the Apache 2.0 build; this distribution adds features that need a free dbt platform sign-in under a separate licence. The Python-based v1 line ([dbt Core](../open-source/dbt-core.md)) is still maintained.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dbt OSS](../open-source/dbt-oss.md), [SQLMesh](../open-source/sqlmesh.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
