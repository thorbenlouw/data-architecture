---
type: Technology
id: databricks-declarative-automation-bundles
title: Databricks Declarative Automation Bundles
description: A Databricks CLI feature that defines jobs, pipelines, dashboards, apps, serving endpoints, AI Search, Lakebase and other resources in YAML with per-target settings. The CLI then validates, plans and deploys them from CI/CD.
aliases: [DABs]
formerly: [Databricks Asset Bundles]
platform: platform-databricks
kind: software
availability: ga
realises: [ci-cd, environment-promotion, infrastructure-as-code, ephemeral-environments]
resource: https://docs.databricks.com/aws/en/dev-tools/bundles/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in March 2026. The direct deployment engine, which removes the Terraform dependency, became GA and the default for new bundles in June 2026. Custom templates can be published to workspace users for self-service.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps) (primary): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations): Define platform resources, permissions and configuration as code and apply them automatically.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CodePipeline](../aws/aws-codepipeline.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [fabric-cicd](../microsoft/fabric-cicd-library.md), [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md), [LookML](../google-cloud/gcp-lookml.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md), [Snowflake CLI](../snowflake/snowflake-cli.md), [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md), [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLFluff](../open-source/sqlfluff.md), [Flyway Community](../open-source/flyway.md), [Liquibase Community](../open-source/liquibase.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Tinybird](../independent/tinybird.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
