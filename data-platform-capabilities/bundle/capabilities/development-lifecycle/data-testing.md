---
type: Capability
id: data-testing
title: Data pipeline testing
description: Test transformation logic and data with unit, integration and regression tests before release.
aliases: [unit tests for SQL, data unit tests, regression testing, data diff, pipeline tests]
broader: [development-lifecycle]
related: [data-quality-rules, data-reconciliation, transformation-as-code, ci-cd, data-contracts]
depends_on: [test-data-management]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data pipelines need two kinds of test. Logic tests check transformation code on small, fixed inputs: given these three order rows, the model must return this one aggregated row. Data tests check assertions on real or representative output: `customer_id` is never null, every order joins to a customer, daily totals match the source within a tolerance. Integration tests run several steps end to end. Regression tests compare the changed pipeline's output with current production output, by rows or summary statistics, to show exactly what a change alters.

Testing catches errors before they reach reports and models, where they are costly to find and fix. It differs from data quality monitoring in timing: pipeline tests run before release on known inputs, while observability watches production data that keeps changing. The two overlap, since many teams run the same assertions in CI and on every production run. Regression comparisons matter most for refactoring and migration, where the aim is to change code without changing results.

# Key considerations

- Unit testing SQL is awkward in many engines. Check whether tooling supports mocked inputs or whether tests can only run against real tables.
- Keep test fixtures small and in version control so tests are fast and give the same result every time.
- Comparing large tables row by row is expensive. Compare keys, counts and aggregates first, then sample rows.
- Agree what a failure means. Tests that only warn are soon ignored; tests that block need clear owners to fix them.

# Questions to ask

- How do you know today that a pipeline change did not alter its results unexpectedly?
- Which datasets matter enough that a wrong number would cause regulatory, financial or customer harm?
- Do tests run automatically on every change, or only when someone remembers?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [Processing and transformation](../processing/processing.md), [Data quality and observability](../data-quality/data-quality.md), [AI-assisted development](ai-assisted-development.md), [CI/CD](ci-cd.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Code and SQL translation](../platform-operations/code-translation.md), [Custom connector development](../ingestion-integration/custom-connectors.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data branching and tagging](../storage/data-branching.md), [Data contracts](../data-products/data-contracts.md), [Data engineering agents](data-engineering-agents.md), [Data quality rules](../data-quality/data-quality-rules.md), [Data reconciliation](../data-quality/data-reconciliation.md), [DataFrame APIs](../processing/dataframe-apis.md), [IDE and local development](local-development.md), [Platform migration](../platform-operations/platform-migration.md), [Runtime and environment management](runtime-management.md), [Transformation as code](../processing/transformation-as-code.md) |
| Depends on | [Test data management](test-data-management.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Patterns:** [ELT](../../patterns/elt.md) · [Shift-left data quality and governance](../../patterns/shift-left.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 2 – CI/CD pipeline automation; Data validation · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 3 – Automated model deployment

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric dbt job](../../technologies/microsoft/fabric-dbt-job.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Dataform](../../technologies/google-cloud/gcp-dataform.md), [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [dbt Projects on Snowflake](../../technologies/snowflake/snowflake-dbt-projects.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [dbt-clickhouse adapter](../../technologies/clickhouse/clickhouse-dbt.md) (preview) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Data Validation](../../technologies/informatica/informatica-data-validation.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku scenarios](../../technologies/dataiku/dataiku-scenarios.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Data Contract CLI](../../technologies/open-source/data-contract-cli.md), [dbt Core (v1.x)](../../technologies/open-source/dbt-core.md), [dbt OSS](../../technologies/open-source/dbt-oss.md), [GX Core (Great Expectations)](../../technologies/open-source/great-expectations.md), [Soda Core](../../technologies/open-source/soda-core.md), [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [GX Cloud](../../technologies/independent/gx-cloud.md) |
