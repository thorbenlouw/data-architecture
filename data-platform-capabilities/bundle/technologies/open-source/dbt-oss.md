---
type: Technology
id: dbt-oss
title: dbt OSS
description: Open-source distribution of the Rust-based dbt v2 engine, which parses and compiles dbt projects much faster and checks them against a strict language specification.
formerly: [dbt Core v2]
platform: platform-open-source
kind: open-source
availability: ga
realises: [transformation-as-code, data-testing, column-lineage]
resource: https://docs.getdbt.com/blog/dbt-core-v2-is-here
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Released as an alpha in June 2026 as dbt Core v2 and renamed dbt OSS at v2 GA on 15 September 2026. It shares a runtime and language specification with the "dbt" distribution, the [dbt v2 engine](../independent/dbt-fusion-engine.md) (formerly the dbt Fusion engine). It uses ADBC and Arrow for adapters and writes artefacts as Parquet. Choose it when you need a fully open-source build.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md), [dbt platform](../independent/dbt-platform.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
