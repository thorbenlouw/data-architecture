---
type: Capability
id: version-control
title: Version control integration
description: Keep code and configuration in Git and work with branches from inside the platform.
aliases: [Git folders, repos]
broader: [development-lifecycle]
related: [ci-cd, data-branching, dashboards-as-code, infrastructure-as-code, transformation-as-code]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

With good integration a developer can clone a repository into a platform workspace, create a branch, edit and run code against a development environment, commit and open a pull request without leaving the platform. Deployed jobs point at a specific commit or tag, so anyone can see exactly which version is running. Some platforms also sync objects such as dashboards, pipelines and semantic models to Git as text files, so they can be reviewed like code.

Version control is the base for code review, CI/CD, environment promotion and audit. It records who changed what, when and why, and makes rollback possible. Integration quality varies widely. Strong integration works with the organisation's existing Git provider, supports branch and merge operations, gives readable diffs for every object type and runs production from Git rather than from the workspace. Weak integration means people edit objects in the platform and export them now and then, so Git and production drift apart. Data branching applies similar ideas to data rather than code.

# Key considerations

- Make Git the source of truth for production. If changes can be made directly in a workspace, the repository stops describing what actually runs.
- Check which object types can be stored as reviewable text. Visual pipelines, dashboards and notebooks often serialise poorly.
- Choose a branching model the team can sustain. Short-lived branches merged often cause fewer conflicts in shared SQL models than long-running environment branches.
- Keep secrets, data samples and notebook outputs out of repositories with ignore rules and pre-commit scanning.

# Questions to ask

- Which Git provider does the organisation use, and must the platform integrate with it directly?
- Can anything in production today be changed without a commit?
- Which artefacts beyond code, such as dashboards, pipelines and permissions, need version history?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [CI/CD](ci-cd.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data branching and tagging](../storage/data-branching.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [IDE and local development](local-development.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Notebooks](notebooks.md), [Prompt management](../generative-ai/prompt-management.md), [Transformation as code](../processing/transformation-as-code.md) |
| Needed by | [CI/CD](ci-cd.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data engineering agents](data-engineering-agents.md), [Environment promotion](environment-promotion.md), [Ephemeral development environments](ephemeral-environments.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Runtime and environment management](runtime-management.md), [Schema change management](schema-change-management.md), [Transformation as code](../processing/transformation-as-code.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 2)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 2, Managed)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 2 – CI/CD pipeline automation · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 1 – DevOps but no MLOps

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Studio](../../technologies/aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Git integration](../../technologies/microsoft/fabric-git-integration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Git integration (Git repository objects)](../../technologies/snowflake/snowflake-git-integration.md), [Snowsight Workspaces](../../technologies/snowflake/snowflake-workspaces.md) |
| [Databricks](../../platforms/platform-databricks.md) | Git folders | [Databricks Git folders](../../technologies/databricks/databricks-git-folders.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md), [Palantir Global Branching](../../technologies/palantir/palantir-global-branching.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [marimo](../../technologies/open-source/marimo.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Charts](../../technologies/independent/dbt-charts.md) (unconfirmed) |
