---
type: Technology
id: databricks-genie-code
title: Genie Code
description: An AI coding and data agent in notebooks, the SQL editor, the pipelines editor, dashboards and MLflow. It plans, writes and runs code, fixes errors and builds pipelines and dashboards, using Unity Catalog context and the user's permissions.
formerly: [Databricks Assistant]
platform: platform-databricks
kind: feature
availability: ga
realises: [ai-assisted-development, data-engineering-agents]
resource: https://docs.databricks.com/aws/en/genie-code/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in March 2026. It runs only in agent mode, with an approval classifier that auto-approves actions unless you require manual approval. It supports custom skills, instructions and MCP servers. Scheduled tasks are GA and a terminal CLI is in Beta. Agentic features need partner-powered AI to be enabled, and usage has been billed pay-as-you-go since July 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Genie

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Kiro](../aws/aws-kiro.md), [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md), [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md), [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya Copilot](../sas/sas-viya-copilot.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Code Studios](../dataiku/dataiku-code-studios.md), [Dataiku Cobuild](../dataiku/dataiku-cobuild.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Hex](../independent/hex.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
