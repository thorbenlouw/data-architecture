---
type: Technology
id: sqlmesh
title: SQLMesh
description: Transformation framework that understands SQL semantically, plans changes before applying them and uses virtual data environments to test and promote models without rebuilding tables.
platform: platform-open-source
kind: open-source
availability: ga
realises:
- transformation-as-code
- environment-promotion
- data-testing
- column-lineage
- incremental-processing
- code-translation
- ephemeral-environments
resource: https://www.linuxfoundation.org/press/linux-foundation-welcomes-sqlmesh-project
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Created by Tobiko Data, which Fivetran acquired in 2025. Fivetran contributed SQLMesh to the Linux Foundation in March 2026 for vendor-neutral governance. It can run existing dbt projects and uses SQLGlot to parse and transpile SQL between dialects.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md), [dbt platform](../independent/dbt-platform.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
