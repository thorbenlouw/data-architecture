---
type: Technology
id: fabric-onelake-shortcuts
title: OneLake shortcuts
description: Virtual folders or tables in OneLake that point to data in other Fabric items or in external stores, so it can be used without copying.
aliases: [shortcuts, OneLake shortcut, Fabric shortcuts]
platform: platform-microsoft
kind: feature
availability: ga
realises: [query-federation, internal-data-sharing, engine-interoperability]
resource: https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Internal targets include lakehouses, warehouses, KQL, SQL and mirrored databases; external targets include ADLS Gen2, Blob Storage, Amazon S3 and S3-compatible stores, Google Cloud Storage, Dataverse, Iceberg tables, OneDrive and SharePoint, and on-premises stores through the data gateway. A workspace cache (1-28 days) cuts cross-cloud egress. Delegated shortcuts are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery federated queries](../google-cloud/gcp-bigquery-federated-queries.md), [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Hub](../sas/sas-data-hub.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Starburst Galaxy](../independent/starburst-galaxy.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
