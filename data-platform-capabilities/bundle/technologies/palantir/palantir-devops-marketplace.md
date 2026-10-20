---
type: Technology
id: palantir-devops-marketplace
title: Palantir DevOps and Marketplace
description: Packaging of pipelines, Ontology, models and applications into versioned products with release channels, and a storefront for installing and upgrading them across spaces and organisations.
aliases: [Foundry DevOps, Foundry Marketplace]
platform: platform-palantir
kind: feature
availability: ga
realises: [environment-promotion, data-marketplace, ci-cd, data-product-lifecycle, application-sharing]
resource: https://www.palantir.com/docs/foundry/devops/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used to promote from development to production installations, to roll out the same product to many partners with their own inputs, and to share products internally.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps) (primary): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) (Data products): Version, publish, deprecate and retire data products with notice to their consumers.
- [Data application distribution](../../capabilities/data-sharing/application-sharing.md) (Data sharing and collaboration): Package code, models, interfaces and data as installable applications that run in the consumer's environment.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CodePipeline](../aws/aws-codepipeline.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md), [fabric-cicd](../microsoft/fabric-cicd-library.md), [Fabric variable library](../microsoft/fabric-variable-library.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md), [Databricks Marketplace](../databricks/databricks-marketplace.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Data application distribution](../../capabilities/data-sharing/application-sharing.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Dagster+](../independent/dagster-plus.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
