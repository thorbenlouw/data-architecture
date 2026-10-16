---
type: Technology
id: snowflake-coco
title: Snowflake CoCo
description: An AI coding agent, available in Snowsight, as a CLI, as a desktop app and in VS Code, that uses Snowflake skills and MCP tools to explore data, write SQL, and build pipelines, dbt projects and apps.
formerly: [Cortex Code]
platform: platform-snowflake
kind: feature
availability: ga
realises: [ai-assisted-development, data-engineering-agents]
resource: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed from Cortex Code in June 2026. It is replacing [Snowflake Copilot](snowflake-copilot.md). Restricted Session Scope limits what it can do, and usage appears in SNOWFLAKE_COCO_USAGE_HISTORY. [Intent-Driven Governance](snowflake-intent-driven-governance.md) is built on it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps) (primary): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Data Agent](../aws/aws-sagemaker-data-agent.md), [Kiro](../aws/aws-kiro.md), [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview), [Fabric MCP server](../microsoft/fabric-mcp-server.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md), [Data Agent Kit](../google-cloud/gcp-data-agent-kit.md) (preview), [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Code](../databricks/databricks-genie-code.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../clickhouse/clickhouse-sql-console.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md), [CLAIRE GPT](../informatica/informatica-claire-gpt.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir MCP and Ontology MCP](../palantir/palantir-mcp.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Hex](../independent/hex.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) |
