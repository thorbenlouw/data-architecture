---
type: Technology
id: snowflake-cli
title: Snowflake CLI
description: An open-source command-line tool for running SQL and for building, testing and deploying Snowflake apps, Snowpark code, Streamlit apps, dbt and DCM projects from local machines and CI pipelines.
aliases: [snow CLI]
platform: platform-snowflake
kind: software
availability: ga
realises: [local-development, ci-cd, environment-promotion]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-cli/introduction/introduction
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowflake CLI (snow) supersedes SnowSQL for developer and CI/CD use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps) (primary): Develop in your own editor and run against the platform, with debugging and local tests.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Kiro](../aws/aws-kiro.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [AWS CodePipeline](../aws/aws-codepipeline.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Fabric deployment pipelines](../microsoft/fabric-deployment-pipelines.md), [fabric-cicd](../microsoft/fabric-cicd-library.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [Google Cloud Build](../google-cloud/gcp-cloud-build.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS 9.4 and SAS Enterprise Guide](../sas/sas-9.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Code Studios](../dataiku/dataiku-code-studios.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
