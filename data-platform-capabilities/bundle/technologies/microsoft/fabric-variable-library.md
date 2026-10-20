---
type: Technology
id: fabric-variable-library
title: Fabric variable library
description: A workspace item holding variables with value sets per stage, consumed by pipelines, notebooks, shortcuts, dataflows and other items.
platform: platform-microsoft
kind: feature
availability: ga
realises: [environment-promotion]
resource: https://learn.microsoft.com/en-us/fabric/cicd/variable-library/variable-library-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps) (primary): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudFormation](../aws/aws-cloudformation.md), [AWS CodePipeline](../aws/aws-codepipeline.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Build](../google-cloud/gcp-cloud-build.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md), [Palantir Global Branching](../palantir/palantir-global-branching.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Deployer and API nodes](../dataiku/dataiku-deployer.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt platform](../independent/dbt-platform.md), [Dagster+](../independent/dagster-plus.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
