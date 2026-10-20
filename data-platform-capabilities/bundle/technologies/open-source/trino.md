---
type: Technology
id: trino
title: Trino
description: Distributed SQL query engine that queries data in place across object storage, lakehouse tables and many databases through connectors.
formerly: [PrestoSQL]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- sql-query-engine
- query-federation
- engine-interoperability
- decoupled-storage-compute
- approximate-query-processing
resource: https://trino.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, governed by the non-profit Trino Software Foundation. Starburst is the main commercial vendor ([Starburst Galaxy](../independent/starburst-galaxy.md) and [Starburst Enterprise](../independent/starburst-enterprise.md)), and Amazon Athena is built on it. Forked from Presto in 2019 (formerly PrestoSQL). Supports Iceberg, Delta and Hudi connectors and fault-tolerant execution for long batch queries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute) (primary): Run analytical SQL over large datasets with parallel, optimised execution.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md), [Amazon Redshift](../aws/aws-redshift.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake virtual warehouses](../snowflake/snowflake-virtual-warehouses.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md), [Databricks SQL](../databricks/databricks-sql.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md), [IBM Db2](../ibm/ibm-db2.md) | [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md), [SAS SpeedyStore](../sas/sas-speedystore.md) | [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
