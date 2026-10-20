---
type: Technology
id: gcp-bigquery-omni
title: BigQuery Omni
description: Runs BigQuery queries on data held in Amazon S3 or Azure Blob Storage, using BigQuery-managed compute in the corresponding AWS or Azure region.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [query-federation, deployment-options]
resource: https://docs.cloud.google.com/bigquery/docs/omni-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Available only with Enterprise edition reservations or on-demand pricing (not Standard or Enterprise Plus). Cross-cloud joins have per-subquery transfer limits; materialised view replicas and cross-cloud transfers move selected data into Google Cloud regions. The borderless Lakehouse preview addresses some of the same needs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md), [Teradata Autonomous Knowledge Platform](../teradata/teradata-autonomous-knowledge-platform.md) | [Query federation](../../capabilities/compute/query-federation.md), [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Hub](../sas/sas-data-hub.md), [SAS Viya](../sas/sas-viya.md) | [Query federation](../../capabilities/compute/query-federation.md), [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud](../dataiku/dataiku-cloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md), [Trino](../open-source/trino.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md), [Denodo Platform](../independent/denodo-platform.md), [StarTree Cloud](../independent/startree-cloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Query federation](../../capabilities/compute/query-federation.md) |
