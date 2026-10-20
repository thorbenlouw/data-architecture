---
type: Technology
id: fabric-git-integration
title: Fabric Git integration
description: Connects a workspace to a branch in Azure DevOps, GitHub or GitHub Enterprise so item definitions can be committed, branched and updated.
platform: platform-microsoft
kind: feature
availability: ga
realises: [version-control, ephemeral-environments]
resource: https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works at workspace level; unsupported items are ignored. Branched workspaces, selective branching and file-level commits are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps) (primary): Keep code and configuration in Git and work with branches from inside the platform.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [LookML](../google-cloud/gcp-lookml.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Git integration (Git repository objects)](../snowflake/snowflake-git-integration.md), [Snowsight Workspaces](../snowflake/snowflake-workspaces.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Git folders](../databricks/databricks-git-folders.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Global Branching](../palantir/palantir-global-branching.md), [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [marimo](../open-source/marimo.md) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Charts](../independent/dbt-charts.md) (unconfirmed) | [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
