---
type: Technology
id: dbt-copilot
title: dbt Copilot
description: AI assistant in the dbt platform that drafts models, tests, documentation, semantic models and SQL from natural language.
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: feature
availability: ga
realises: [ai-assisted-development, ai-generated-documentation, data-engineering-agents]
resource: https://docs.getdbt.com/docs/dbt-ai/copilot-overview
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

dbt Wizard, a beta agent announced with the merger, adds multi-step authoring, refactoring and debugging with full project context. Both are limited to selected plans.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Kiro](../aws/aws-kiro.md), [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Copilot in Power BI](../microsoft/powerbi-copilot.md), [Fabric MCP server](../microsoft/fabric-mcp-server.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake CoCo](../snowflake/snowflake-coco.md), [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md), [Snowflake Extension for Visual Studio Code](../snowflake/snowflake-vscode-extension.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
