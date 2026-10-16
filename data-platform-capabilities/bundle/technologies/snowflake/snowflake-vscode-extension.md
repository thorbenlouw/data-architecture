---
type: Technology
id: snowflake-vscode-extension
title: Snowflake Extension for Visual Studio Code
description: An IDE extension for connecting to Snowflake, running SQL and Snowpark code, and using CoCo from a local editor.
platform: platform-snowflake
kind: software
availability: preview
realises: [local-development, ai-assisted-development]
resource: https://docs.snowflake.com/en/user-guide/vscode-ext
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The extension is a preview feature, although CoCo inside it has been GA since August 2026. Remote development is also in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps) (primary): Develop in your own editor and run against the platform, with debugging and local tests.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Kiro](../aws/aws-kiro.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
