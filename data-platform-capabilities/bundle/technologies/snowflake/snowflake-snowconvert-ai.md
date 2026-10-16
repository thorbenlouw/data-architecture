---
type: Technology
id: snowflake-snowconvert-ai
title: SnowConvert AI
description: A migration tool that assesses and converts SQL code and objects from Teradata, Oracle, SQL Server, Redshift, Synapse, BigQuery, Databricks SQL and other platforms to Snowflake.
formerly: [SnowConvert]
platform: platform-snowflake
kind: software
availability: ga
realises: [code-translation, ai-assisted-development]
resource: https://docs.snowflake.com/migrations/snowconvert-docs/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowflake now recommends the Snowflake AIM Agent for Data Warehouses for migration projects. SAS migration through that agent, and SSIS-to-dbt ETL migration in SnowConvert AI, are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations) (primary): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md), [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview), [Lakebridge](../databricks/databricks-lakebridge.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter Cloud Edition (PCCE)](../informatica/informatica-powercenter-cloud-edition.md), [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [SQLMesh](../open-source/sqlmesh.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
