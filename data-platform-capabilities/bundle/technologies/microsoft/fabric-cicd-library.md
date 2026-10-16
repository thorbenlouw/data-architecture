---
type: Technology
id: fabric-cicd-library
title: fabric-cicd
description: A Microsoft-maintained Python library for deploying Fabric item definitions from a Git repository to target workspaces with environment-specific parameters.
platform: platform-microsoft
kind: open-source
availability: ga
realises: [ci-cd, environment-promotion]
resource: https://microsoft.github.io/fabric-cicd/
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Code-first alternative to deployment pipelines, typically run from Azure DevOps or GitHub Actions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps) (primary): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CodePipeline](../aws/aws-codepipeline.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md), [LookML](../google-cloud/gcp-lookml.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md), [Snowflake Git integration (Git repository objects)](../snowflake/snowflake-git-integration.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Apollo](../palantir/palantir-apollo.md), [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLFluff](../open-source/sqlfluff.md), [Flyway Community](../open-source/flyway.md), [Liquibase Community](../open-source/liquibase.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Tinybird](../independent/tinybird.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
