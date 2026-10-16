---
type: Capability
id: ci-cd
title: CI/CD
description: Build, test and deploy pipelines, models and infrastructure automatically on every change.
aliases: [continuous integration, continuous delivery]
broader: [development-lifecycle]
related:
- data-testing
- infrastructure-as-code
- zero-copy-cloning
- schema-change-management
- transformation-as-code
depends_on: [version-control, secrets-management]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Continuous integration builds and tests every change automatically, usually when a pull request is opened. Continuous delivery then packages the tested change and deploys it to the next environment with few or no manual steps. For a data project, one pipeline run might lint SQL, run unit tests, build only the changed models and their dependants in a temporary schema against cloned or sampled data, run data tests, then deploy the bundle of job definitions to test and, after approval, to production.

CI/CD replaces hand deployments with a repeatable, logged process. That cuts release errors and produces the change record auditors ask for. Data CI has its own cost problem: building against realistic data takes time and compute, so teams use selective builds, references to production state and zero-copy clones. The same practice covers infrastructure, transformation code, orchestration definitions and machine learning, where model validation and registry steps are added. Environment promotion describes where artefacts go; CI/CD is the automation that moves them.

# Key considerations

- Run pipelines under a dedicated service identity with only the permissions needed in each environment. A pipeline that can write anywhere is a valuable target for attackers.
- Keep CI fast by building only what changed and its dependants and caching dependencies, or developers will find ways round it.
- Decide which checks block a release, such as failed tests, breaking schema changes or policy violations, and which only warn.
- Clean up the temporary schemas, clones and compute that CI runs create, or they accumulate cost.
- Plan stateful changes separately. Dropping or rebuilding a large table cannot be undone the way redeploying code can.

# Questions to ask

- How are changes deployed to production today, and how many steps are manual?
- What evidence of testing and approval do auditors or change boards require?
- How long may a CI run take before developers stop waiting for it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Narrower | [CI/CD for machine learning](../mlops/ml-cicd.md) |
| Related | [Orchestration](../orchestration/orchestration.md), [ML operations](../mlops/mlops.md), [Custom connector development](../ingestion-integration/custom-connectors.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data branching and tagging](../storage/data-branching.md), [Data engineering agents](data-engineering-agents.md), [Data pipeline testing](data-testing.md), [Data versioning](../storage/data-versioning.md), [Environment promotion](environment-promotion.md), [Ephemeral development environments](ephemeral-environments.md), [Impact analysis](../metadata/impact-analysis.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Runtime and environment management](runtime-management.md), [Schema change management](schema-change-management.md), [Secrets management](../security/secrets-management.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md), [Transformation as code](../processing/transformation-as-code.md), [Version control integration](version-control.md), [Workflow orchestration](../orchestration/workflow-orchestration.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Version control integration](version-control.md), [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 3) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Patterns:** [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md) · [Shift-left data quality and governance](../../patterns/shift-left.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Data platform engineer](../../personas/persona-platform-engineer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – data product developer experience plane · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 1 – DevOps but no MLOps

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS CodePipeline](../../technologies/aws/aws-codepipeline.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric deployment pipelines](../../technologies/microsoft/fabric-deployment-pipelines.md), [fabric-cicd](../../technologies/microsoft/fabric-cicd-library.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Build](../../technologies/google-cloud/gcp-cloud-build.md), [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [dbt Projects on Snowflake](../../technologies/snowflake/snowflake-dbt-projects.md), [Snowflake CLI](../../technologies/snowflake/snowflake-cli.md), [Snowflake DCM Projects](../../technologies/snowflake/snowflake-dcm-projects.md), [Snowflake Git integration (Git repository objects)](../../technologies/snowflake/snowflake-git-integration.md) |
| [Databricks](../../platforms/platform-databricks.md) | Declarative Automation Bundles | [Databricks Declarative Automation Bundles](../../technologies/databricks/databricks-declarative-automation-bundles.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Apollo](../../technologies/palantir/palantir-apollo.md), [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md), [Palantir DevOps and Marketplace](../../technologies/palantir/palantir-devops-marketplace.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Data Contract CLI](../../technologies/open-source/data-contract-cli.md), [Flyway Community](../../technologies/open-source/flyway.md), [Liquibase Community](../../technologies/open-source/liquibase.md), [SQLFluff](../../technologies/open-source/sqlfluff.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt platform](../../technologies/independent/dbt-platform.md), [Tinybird](../../technologies/independent/tinybird.md) |

Narrower capabilities are realised by a further 4 technologies; see their pages.
