---
type: Technology
id: snowflake-git-integration
title: Snowflake Git integration (Git repository objects)
description: Syncs remote Git repositories into Snowflake as repository clones, so code can be run with EXECUTE IMMEDIATE FROM and Workspaces, notebooks and Streamlit apps can commit and push.
platform: platform-snowflake
kind: feature
availability: ga
realises: [version-control, ci-cd]
resource: https://docs.snowflake.com/en/developer-guide/git/git-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works with GitHub, GitLab, Bitbucket, Azure DevOps and AWS CodeCommit, including self-hosted instances.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps) (primary): Keep code and configuration in Git and work with branches from inside the platform.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Git integration](../microsoft/fabric-git-integration.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Git folders](../databricks/databricks-git-folders.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md), [Palantir Global Branching](../palantir/palantir-global-branching.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [marimo](../open-source/marimo.md), [SQLFluff](../open-source/sqlfluff.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Charts](../independent/dbt-charts.md) (unconfirmed) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
