---
type: Technology
id: snowflake-dcm-projects
title: Snowflake DCM Projects
description: Database Change Management projects that declare the desired state of databases, schemas, tables, dynamic tables, views, warehouses, roles, grants and data quality checks in SQL DEFINE files, then plan and deploy the changes.
aliases: [Database Change Management, Snowflake DCM]
platform: platform-snowflake
kind: feature
availability: ga
realises: [schema-change-management, infrastructure-as-code, environment-promotion, ci-cd]
resource: https://docs.snowflake.com/en/user-guide/dcm-projects/dcm-projects-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA since 7 August 2026. Jinja templating supports per-environment configuration, and each environment has its own project object. Some object types and attachments (for example ATTACH MASKING POLICY) are still in preview. CREATE OR ALTER statements are a lighter, imperative alternative.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Schema change management](../../capabilities/development-lifecycle/schema-change-management.md) (Development and DataOps) (primary): Version and apply database schema changes through controlled migrations.
- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations): Define platform resources, permissions and configuration as code and apply them automatically.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudFormation](../aws/aws-cloudformation.md), [AWS CodePipeline](../aws/aws-codepipeline.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md), [fabric-cicd](../microsoft/fabric-cicd-library.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Flyway Community](../open-source/flyway.md), [Liquibase Community](../open-source/liquibase.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Schema change management](../../capabilities/development-lifecycle/schema-change-management.md) |
