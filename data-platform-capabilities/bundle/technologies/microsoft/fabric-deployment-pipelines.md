---
type: Technology
id: fabric-deployment-pipelines
title: Fabric deployment pipelines
description: Promote workspace content through two to ten stages such as development, test and production, with item pairing and deployment rules.
platform: platform-microsoft
kind: feature
availability: ga
realises: [environment-promotion, ci-cd]
resource: https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Deployment plans for explicit ordering and pre/post actions are preview. Item support varies; many Power BI items are listed as preview. Teams with mature CI/CD often use Git plus fabric-cicd instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps) (primary): Promote the same artefacts through development, test and production with environment-specific configuration.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CodePipeline](../aws/aws-codepipeline.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Global Branching](../palantir/palantir-global-branching.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md), [SQLFluff](../open-source/sqlfluff.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Dagster+](../independent/dagster-plus.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
