---
type: Capability
id: transformation-as-code
title: Transformation as code
description: Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
aliases: [dbt, models as code, SQL frameworks]
broader: [sql-transformation]
related: [data-testing, ci-cd, table-lineage, environment-promotion, declarative-pipelines]
depends_on: [version-control]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Transformations are organised as a project of small, named models held in Git. Each model is usually a SELECT statement or a short Python function. Models refer to each other through a function rather than hard-coded table names, so the tool can build a dependency graph and run them in the right order. The same project holds tests (for example, `order_id` is unique and never null), documentation, and settings for how each model is stored: as a view, a table or an incrementally updated table. The open-source dbt popularised the approach and other frameworks follow similar ideas.

It applies software practice to analytics: code review, builds in isolated schemas on every change, separate environments, and lineage and documentation generated from the code. It is the usual home of analytics engineering. Compared with loose SQL scripts it adds modularity and automatic ordering. Compared with declarative pipelines, it usually relies on an external scheduler and leaves incremental logic to the author rather than the engine.

# Key considerations

- Projects with thousands of models need conventions for layers, naming and ownership, or the graph becomes too tangled to change safely.
- Incremental models must handle late data and schema changes. Keep a full-rebuild path that still works.
- In CI, build only changed models and their dependants against cloned or deferred production data, to keep build time and cost down.
- Tests help only if they run on every deployment and a failure blocks the release.
- Decide whether the transformation tool or the orchestrator owns scheduling, so jobs are not triggered twice.

# Questions to ask

- How many people contribute transformations, and do they already work in Git?
- Is there a CI process that builds and tests changes before they reach production?
- Do you want lineage and documentation generated from the code, or is a separate catalogue enough?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [SQL transformation](sql-transformation.md) |
| Related | [Orchestration](../orchestration/orchestration.md), [Development and DataOps](../development-lifecycle/development-lifecycle.md), [AI-generated documentation](../metadata/ai-generated-documentation.md), [CI/CD](../development-lifecycle/ci-cd.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data quality rules](../data-quality/data-quality-rules.md), [Declarative pipelines](declarative-pipelines.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Feature engineering](../machine-learning/feature-engineering.md), [Table-level lineage](../metadata/table-lineage.md), [Version control integration](../development-lifecycle/version-control.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Version control integration](../development-lifecycle/version-control.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md) · [ELT](../../patterns/elt.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 2, Managed)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – data product developer experience plane

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric dbt job](../../technologies/microsoft/fabric-dbt-job.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Dataform (SQLX) | [Dataform](../../technologies/google-cloud/gcp-dataform.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [dbt Projects on Snowflake](../../technologies/snowflake/snowflake-dbt-projects.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [dbt-clickhouse adapter](../../technologies/clickhouse/clickhouse-dbt.md) (preview) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [dbt Core (v1.x)](../../technologies/open-source/dbt-core.md), [dbt OSS](../../technologies/open-source/dbt-oss.md), [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Coalesce Transform](../../technologies/independent/coalesce-transform.md), [dbt platform](../../technologies/independent/dbt-platform.md), [dbt v2 engine](../../technologies/independent/dbt-fusion-engine.md) |
