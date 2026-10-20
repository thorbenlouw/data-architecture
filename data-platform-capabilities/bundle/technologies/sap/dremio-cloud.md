---
type: Technology
id: dremio-cloud
title: Dremio Cloud
description: Managed lakehouse query service built on Apache Iceberg, with an Iceberg catalogue, automatic query acceleration and an AI semantic layer.
platform: platform-sap
vendor: Dremio (SAP)
kind: managed-service
availability: ga
realises:
- sql-query-engine
- query-acceleration
- table-catalogue
- semantic-layer
- conversational-analytics
- ai-context-layer
- credential-vending
resource: https://www.dremio.com/platform/
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP announced on 4 May 2026 that it would acquire Dremio, and Dremio now describes itself as part of SAP, so confirm the roadmap for Dremio Cloud as a standalone service. Open Catalog is built on [Apache Polaris](../open-source/apache-polaris.md). Autonomous Reflections create and maintain precomputed accelerations without user action. An AI agent and an MCP server let users and external agents generate and run SQL. Dremio Enterprise is the self-managed edition. Dremio also leads [Project Nessie](../open-source/project-nessie.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Db2](../ibm/ibm-db2.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [Apache DataFusion](../open-source/apache-datafusion.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md), [Cube Cloud](../independent/cube-cloud.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Query acceleration](../../capabilities/compute/query-acceleration.md) |
