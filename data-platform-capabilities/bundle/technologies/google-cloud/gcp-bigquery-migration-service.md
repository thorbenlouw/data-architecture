---
type: Technology
id: gcp-bigquery-migration-service
title: BigQuery Migration Service
description: Tooling for moving warehouses to BigQuery, covering assessment, batch and interactive SQL translation, data transfer and validation.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [platform-migration, ai-assisted-development, data-reconciliation, code-translation]
resource: https://docs.cloud.google.com/bigquery/docs/migration-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports Teradata, Redshift, Snowflake, Oracle, Netezza and Hadoop/Hive/Spark sources, with Gemini-assisted translation. It can also migrate Hive Metastore and Iceberg REST catalogue metadata into Lakehouse. The open-source data validation tool compares source and target.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations) (primary): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.
- [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) (Data quality and observability): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Transform](../aws/aws-transform.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [SnowConvert AI](../snowflake/snowflake-snowconvert-ai.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebridge](../databricks/databricks-lakebridge.md), [Databricks agentic code converter](../databricks/databricks-agentic-code-converter.md) (preview) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter Cloud Edition (PCCE)](../informatica/informatica-powercenter-cloud-edition.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
