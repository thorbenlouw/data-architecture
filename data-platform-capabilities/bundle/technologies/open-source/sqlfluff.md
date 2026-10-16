---
type: Technology
id: sqlfluff
title: SQLFluff
description: Linter and auto-formatter for SQL that supports many dialects and dbt or Jinja templating.
platform: platform-open-source
kind: open-source
availability: ga
realises: [ci-cd]
resource: https://docs.sqlfluff.com/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence, community-maintained. Commonly run in pre-commit hooks and CI to enforce SQL style in dbt and SQLMesh projects. It checks code style, not data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps) (primary): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CodePipeline](../aws/aws-codepipeline.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [fabric-cicd](../microsoft/fabric-cicd-library.md), [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md), [LookML](../google-cloud/gcp-lookml.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Git integration (Git repository objects)](../snowflake/snowflake-git-integration.md), [Snowflake CLI](../snowflake/snowflake-cli.md), [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md), [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tinybird](../independent/tinybird.md), [dbt platform](../independent/dbt-platform.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
