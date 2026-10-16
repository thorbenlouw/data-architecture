---
type: Technology
id: databricks-agentic-code-converter
title: Databricks agentic code converter
description: A Genie Code-based migration project that converts T-SQL, Snowflake, Redshift, Oracle, BigQuery and Teradata SQL into Databricks SQL or DataFrame notebooks.
platform: platform-databricks
kind: feature
availability: preview
realises: [code-translation, ai-assisted-development]
resource: https://docs.databricks.com/aws/en/migration/agentic-code-converter
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Beta since July 2026, and a workspace admin must enable it. Each batch is limited to 300 files and Teradata BTEQ is not supported.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations) (primary): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md), [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter Cloud Edition (PCCE)](../informatica/informatica-powercenter-cloud-edition.md), [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
