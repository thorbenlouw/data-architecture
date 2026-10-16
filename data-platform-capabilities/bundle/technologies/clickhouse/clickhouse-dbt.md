---
type: Technology
id: clickhouse-dbt
title: dbt-clickhouse adapter
description: ClickHouse-supported dbt adapter that builds views, tables, incremental and microbatch models, materialised views and dictionaries in ClickHouse.
platform: platform-clickhouse
kind: open-source
availability: preview
realises: [transformation-as-code, data-testing]
resource: https://clickhouse.com/docs/integrations/dbt
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The docs state the integration is not yet production-ready; distributed and materialised-view materialisations are experimental. An adapter for the Rust-based dbt v2 engine entered public beta and a dbt Platform connection private beta in September 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dbt OSS](../open-source/dbt-oss.md), [dbt Core (v1.x)](../open-source/dbt-core.md), [SQLMesh](../open-source/sqlmesh.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md), [dbt platform](../independent/dbt-platform.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
