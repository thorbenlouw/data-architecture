---
type: Technology
id: ibm-netezza
title: IBM Netezza Performance Server
description: MPP data warehouse, now offered as a cloud service and on appliances, that can also read and write Iceberg tables shared with watsonx.data.
aliases: [Netezza, Netezza as a Service]
formerly: [IBM PureData System for Analytics]
platform: platform-ibm
kind: software
availability: ga
realises: [sql-query-engine, provisioned-compute, open-table-formats]
resource: https://www.ibm.com/products/netezza
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still met as legacy appliances; IBM positions migration to Netezza as a Service or watsonx.data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md), [Amazon Athena](../aws/aws-athena.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Presto](../open-source/presto.md), [Trino](../open-source/trino.md), [Apache DataFusion](../open-source/apache-datafusion.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
