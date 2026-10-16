---
type: Technology
id: aws-codepipeline
title: AWS CodePipeline
description: Continuous delivery service that builds, tests and deploys code and infrastructure through staged pipelines with approvals.
platform: platform-aws
kind: managed-service
availability: ga
realises: [ci-cd, environment-promotion]
resource: https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Often paired with CodeBuild and CloudFormation, or replaced by GitHub Actions or GitLab using IAM OIDC federation. SageMaker Projects templates generate pipelines for ML.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps) (primary): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [fabric-cicd](../microsoft/fabric-cicd-library.md), [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md), [Fabric variable library](../microsoft/fabric-variable-library.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md), [LookML](../google-cloud/gcp-lookml.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md), [Snowflake Git integration (Git repository objects)](../snowflake/snowflake-git-integration.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Apollo](../palantir/palantir-apollo.md), [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLFluff](../open-source/sqlfluff.md), [Flyway Community](../open-source/flyway.md), [Liquibase Community](../open-source/liquibase.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Tinybird](../independent/tinybird.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
