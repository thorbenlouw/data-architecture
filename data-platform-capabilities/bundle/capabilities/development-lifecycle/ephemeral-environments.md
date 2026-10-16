---
type: Capability
id: ephemeral-environments
title: Ephemeral development environments
description: Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.
aliases:
- branch deployments
- virtual data environments
- per-PR environments
- preview environments
- deferral
- slim CI
broader: [development-lifecycle]
related: [environment-promotion, zero-copy-cloning, data-branching, ci-cd, self-service-provisioning]
depends_on: [version-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a developer opens a pull request, the platform creates an environment for that change alone: a schema, catalogue branch or workspace named after the branch, with its own jobs and service identity. Only the changed models and their dependants are built there. Everything upstream is read from production, directly or through zero-copy clones or table branches, so a change to one model in a project of two thousand builds in minutes on full-size data. Reviewers query the results, comparison tests run, and the environment is deleted after merge.

Shared, fixed test environments drift from production and rarely hold realistic data, so tests there prove little. Per-change environments give each developer and CI run an isolated, current view without the storage cost of full copies. Implementations range from transformation tools that defer unchanged models to production, to orchestrators with branch deployments, to catalogue-level data branches. Environment promotion is the permanent route to production; these are the temporary places where changes are built and checked first.

# Key considerations

- Reading production data from a development environment needs explicit read-only grants and masking of sensitive columns. A per-change environment must never be able to write to production tables.
- Set expiry and automatic clean-up. Abandoned branches, clones and schemas keep accumulating storage and compute cost.
- Building only what changed depends on accurate state from the last production run. Stale state either skips models that changed or rebuilds everything.
- Run comparison tests between the change and production output inside the environment, so reviewers see the effect on data and not only the code diff.

# Questions to ask

- How long does it take today to test a change against realistic data, and how many people share each test environment?
- May development environments read production data, and under which masking rules?
- How large is the transformation project, and how long does a full build take?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [CI/CD](ci-cd.md), [Data branching and tagging](../storage/data-branching.md), [Environment promotion](environment-promotion.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Version control integration](version-control.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Git integration](../../technologies/microsoft/fabric-git-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [dbt Projects on Snowflake](../../technologies/snowflake/snowflake-dbt-projects.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Declarative Automation Bundles](../../technologies/databricks/databricks-declarative-automation-bundles.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Global Branching](../../technologies/palantir/palantir-global-branching.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [lakeFS](../../technologies/open-source/lakefs.md), [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dagster+](../../technologies/independent/dagster-plus.md), [dbt platform](../../technologies/independent/dbt-platform.md) |
