---
type: Technology
id: dbt-core
title: dbt Core (v1.x)
description: Python framework for SQL and Python transformations as version-controlled models, with dependency resolution, tests, documentation and lineage.
aliases: [dbt Core]
platform: platform-open-source
kind: open-source
availability: ga
realises: [transformation-as-code, data-testing, table-lineage, incremental-processing]
resource: https://www.getdbt.com/licenses-faq
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. dbt Labs merged with Fivetran on 1 June 2026. dbt Core 1.13 is the final 1.x minor release and will get security and installation patches for an expected 3-5 years. From dbt v2 (GA 15 September 2026) the "dbt Core" name no longer applies: the open-source v2 build is [dbt OSS](../open-source/dbt-oss.md), and the default distribution is the [dbt v2 engine](../independent/dbt-fusion-engine.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md), [dbt platform](../independent/dbt-platform.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
