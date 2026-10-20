---
type: Capability
id: environment-promotion
title: Environment promotion
description: Promote the same artefacts through development, test and production with environment-specific configuration.
aliases: [deployment pipelines, release promotion]
broader: [development-lifecycle]
related: [ci-cd, infrastructure-as-code, multi-tenancy, test-data-management, model-registry]
depends_on: [version-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

One built artefact, such as a package of SQL models and job definitions, a container image or a model version, moves through a sequence of environments, typically development, test and production. Only configuration changes between them: catalogue and schema names, connection endpoints, compute sizes, schedules and service identities. A pipeline bundle might read `catalogue: dev_sales` in development and `catalogue: sales` in production while the code inside is identical. Each promotion is gated, for example by passing tests and, for production, a recorded approval.

Promoting the same artefact means that what was tested is what runs, which removes errors caused by rebuilding for each environment. Environments can be separate accounts or workspaces, separate catalogues in one account, or separate schemas. Stronger separation limits accidents but costs more to run and keep consistent. Data is not promoted: each environment has its own, so promotion design must also cover how test environments get representative data. CI/CD automates the model that environment promotion defines.

# Key considerations

- Parameterise every environment-specific value. Hard-coded schema names or endpoints are the usual cause of test jobs writing to production.
- Choose the separation boundary. Separate accounts or workspaces isolate most strongly; schemas in one account are cheaper but depend entirely on correct permissions.
- Keep environments structurally identical through infrastructure as code, so a promotion does not fail on a missing grant or table.
- Use only as many environments as you need. Each extra one adds cost, data refresh work and delay.

# Questions to ask

- How many environments exist today, and how is each one's data populated?
- Is production built again from source, or is the tested artefact deployed unchanged?
- Who approves promotion to production, and is that approval recorded?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [CI/CD](ci-cd.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data branching and tagging](../storage/data-branching.md), [Data product lifecycle management](../data-products/data-product-lifecycle.md), [Ephemeral development environments](ephemeral-environments.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Model deployment](../mlops/model-deployment.md), [Model registry](../machine-learning/model-registry.md), [Model release strategies](../mlops/model-release-strategies.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Prompt management](../generative-ai/prompt-management.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md), [Test data management](test-data-management.md), [Transformation as code](../processing/transformation-as-code.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Version control integration](version-control.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 2 – CI/CD pipeline automation · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 3 – Automated model deployment · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Variables · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Variables

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS CloudFormation](../../technologies/aws/aws-cloudformation.md), [AWS CodePipeline](../../technologies/aws/aws-codepipeline.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Deployment pipelines | [Fabric deployment pipelines](../../technologies/microsoft/fabric-deployment-pipelines.md), [Fabric variable library](../../technologies/microsoft/fabric-variable-library.md), [fabric-cicd](../../technologies/microsoft/fabric-cicd-library.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Build](../../technologies/google-cloud/gcp-cloud-build.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake CLI](../../technologies/snowflake/snowflake-cli.md), [Snowflake DCM Projects](../../technologies/snowflake/snowflake-dcm-projects.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Declarative Automation Bundles](../../technologies/databricks/databricks-declarative-automation-bundles.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Terraform provider](../../technologies/clickhouse/clickhouse-terraform.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir DevOps and Marketplace](../../technologies/palantir/palantir-devops-marketplace.md), [Palantir Global Branching](../../technologies/palantir/palantir-global-branching.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Bundles and Project Deployer | [Dataiku Deployer and API nodes](../../technologies/dataiku/dataiku-deployer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dagster+](../../technologies/independent/dagster-plus.md), [dbt platform](../../technologies/independent/dbt-platform.md) |
