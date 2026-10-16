---
type: Technology
id: dbt-platform
title: dbt platform
description: Hosted service for developing, testing, scheduling and deploying dbt transformation projects, with a browser IDE, a visual editor, job scheduling, CI on pull requests and environments.
formerly: [dbt Cloud]
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: saas
availability: ga
realises:
- transformation-as-code
- workflow-orchestration
- ci-cd
- environment-promotion
- data-contracts
- ephemeral-environments
resource: https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Components include the Studio IDE, Canvas (drag-and-drop model building), the dbt CLI, the job scheduler, Mesh (cross-project references, model contracts and versions), Insights (exploratory SQL) and Cost Insights (beta). dbt State, in preview, is a caching layer that rebuilds only models whose inputs changed.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Transformation as code](../../capabilities/processing/transformation-as-code.md) (Processing and transformation) (primary): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric dbt job](../microsoft/fabric-dbt-job.md) (preview) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataform](../google-cloud/gcp-dataform.md) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [dbt-clickhouse adapter](../clickhouse/clickhouse-dbt.md) (preview) | [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md), [dbt OSS](../open-source/dbt-oss.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Transformation as code](../../capabilities/processing/transformation-as-code.md) |
