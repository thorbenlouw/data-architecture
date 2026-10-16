---
type: Technology
id: aws-sagemaker-data-agent
title: Amazon SageMaker Data Agent
description: AI assistant in SageMaker Unified Studio notebooks and the query editor that writes SQL and code from natural language, explains its plan and fixes failed queries.
platform: platform-aws
kind: feature
availability: ga
realises: [ai-assisted-development, conversational-analytics, data-engineering-agents]
resource: https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-sagemaker-data-agent-query-editor
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generates SQL for Redshift and Athena and Python for notebooks; added to the query editor in March 2026 and to IAM Identity Center domains in April 2026. Aimed at engineers and analysts rather than business users, who are served by Amazon Quick.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Copilot in Power BI](../microsoft/powerbi-copilot.md), [Fabric MCP server](../microsoft/fabric-mcp-server.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md), [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md), [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE GPT](../informatica/informatica-claire-gpt.md), [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Hex](../independent/hex.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
