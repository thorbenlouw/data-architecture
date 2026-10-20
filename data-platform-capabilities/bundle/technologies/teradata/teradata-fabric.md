---
type: Technology
id: teradata-fabric
title: Teradata Fabric
description: Query federation layer that joins data across Teradata systems and other engines such as Hive, Spark SQL, Oracle and BigQuery, pushing processing to where the data sits.
formerly: [Teradata QueryGrid]
platform: platform-teradata
kind: software
availability: ga
realises: [query-federation, engine-interoperability, internal-data-sharing]
resource: https://www.teradata.com/platform/fabric
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in May 2026; documentation still uses the QueryGrid name. Connectors include generic JDBC and Arrow Flight SQL. Useful for hybrid and multi-cloud estates to reduce data movement and egress.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata Autonomous Knowledge Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery federated queries](../google-cloud/gcp-bigquery-federated-queries.md), [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Hub](../sas/sas-data-hub.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Starburst Galaxy](../independent/starburst-galaxy.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
