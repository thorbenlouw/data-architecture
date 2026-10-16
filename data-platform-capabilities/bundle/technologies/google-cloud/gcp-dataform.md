---
type: Technology
id: gcp-dataform
title: Dataform
description: Develops, tests, version-controls and runs SQL transformation workflows in BigQuery, defined in SQLX with dependencies resolved automatically.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [transformation-as-code, declarative-pipelines, data-testing, incremental-processing]
resource: https://docs.cloud.google.com/dataform/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Free apart from BigQuery compute. Supports assertions, unit tests (GA September 2026), incremental tables, release and workflow configurations, Git providers through Developer Connect, and a remote MCP server. Strict act-as mode with custom service accounts was enforced in 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Declarative pipelines](../../capabilities/processing/declarative-pipelines.md) (Processing and transformation): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dbt Core (v1.x)](../open-source/dbt-core.md), [dbt OSS](../open-source/dbt-oss.md), [SQLMesh](../open-source/sqlmesh.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md), [dbt platform](../independent/dbt-platform.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
