---
type: Technology
id: snowflake-dbt-projects
title: dbt Projects on Snowflake
description: Deploys, runs, schedules and monitors dbt projects as Snowflake objects on a dbt Core or dbt Fusion runtime that Snowflake manages, developed in Workspaces or from Git.
platform: platform-snowflake
kind: feature
availability: ga
realises: [transformation-as-code, data-testing, ci-cd, ephemeral-environments]
resource: https://docs.snowflake.com/en/user-guide/data-engineering/dbt-projects-on-snowflake
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs are scheduled with Snowflake tasks or called from Airflow. Since September 2026, dbt artefacts can drive Slim CI and defer-to-production, so a CI run builds only the changed models and reads unchanged ones from production. This is an alternative to dbt Cloud, not a replacement for it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dbt OSS](../open-source/dbt-oss.md), [SQLMesh](../open-source/sqlmesh.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [dbt v2 engine](../independent/dbt-fusion-engine.md), [Coalesce Transform](../independent/coalesce-transform.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
