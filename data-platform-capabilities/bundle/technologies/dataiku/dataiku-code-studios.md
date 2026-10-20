---
type: Technology
id: dataiku-code-studios
title: Dataiku Code Studios
description: Browser-based development environments such as VS Code, JupyterLab and RStudio that run in containers next to a project, with coding agents such as Claude Code, OpenAI Codex and GitHub Copilot.
platform: platform-dataiku
kind: feature
availability: ga
realises: [local-development, ai-assisted-development]
resource: https://doc.dataiku.com/dss/latest/code-studios/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Administrators define Code Studio templates with the tools and code environments allowed. Streamlit, Dash and similar apps built in a Code Studio can be published as Dataiku webapps. Needs Elastic AI computation on Kubernetes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps) (primary): Develop in your own editor and run against the platform, with debugging and local tests.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Kiro](../aws/aws-kiro.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview), [Snowflake CLI](../snowflake/snowflake-cli.md), [Snowsight Workspaces](../snowflake/snowflake-workspaces.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md), [clickhouse-local](../clickhouse/clickhouse-local.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS 9.4 and SAS Enterprise Guide](../sas/sas-9.md), [SAS Viya Copilot](../sas/sas-viya-copilot.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt v2 engine](../independent/dbt-fusion-engine.md) | [IDE and local development](../../capabilities/development-lifecycle/local-development.md) |
