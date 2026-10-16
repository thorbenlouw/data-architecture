---
type: Technology
id: databricks-connect
title: Databricks Connect
description: A client library built on Spark Connect. Python, Scala and R DataFrame code written in an IDE or application runs on remote Databricks compute, including serverless.
platform: platform-databricks
kind: software
availability: ga
realises: [local-development, dataframe-apis]
resource: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Databricks extension for Visual Studio Code uses it for debugging, and it also works with PyCharm and IntelliJ. The Databricks CLI became GA in May 2026. Spark Connect itself is Apache Spark open source.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps) (primary): Develop in your own editor and run against the platform, with debugging and local tests.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Kiro](../aws/aws-kiro.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Fabric semantic link (SemPy)](../microsoft/fabric-semantic-link.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview), [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowsight Workspaces](../snowflake/snowflake-workspaces.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
