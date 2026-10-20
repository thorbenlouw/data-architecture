---
type: Technology
id: starburst-galaxy
title: Starburst Galaxy
description: Managed Trino-based query service that queries lake tables and federated sources in place, with Iceberg lake management, streaming ingest into live tables and built-in governance.
platform: platform-independent
vendor: Starburst
kind: managed-service
availability: ga
realises:
- sql-query-engine
- query-federation
- engine-interoperability
- data-product-specification
- attribute-based-access
- stream-to-table
resource: https://docs.starburst.io/starburst-galaxy/index.html
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on [Trino](../open-source/trino.md). Built-in governance provides universal search, RBAC, attribute tags and policies. Icehouse LakeOps handles table maintenance. Warp Speed adds indexing and caching. Starburst AI includes an AI Data Assistant, SQL AI functions, an MCP endpoint and guardrails.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) (Ingestion and integration): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md), [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM Db2](../ibm/ibm-db2.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [Presto](../open-source/presto.md), [DuckDB](../open-source/duckdb.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
