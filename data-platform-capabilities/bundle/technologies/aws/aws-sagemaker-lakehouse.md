---
type: Technology
id: aws-sagemaker-lakehouse
title: Lakehouse architecture of Amazon SageMaker
description: Logical layer that organises S3, S3 Tables and Redshift Managed Storage into catalogues, and mounts other sources as federated catalogues, all queryable through Iceberg-compatible engines.
formerly: [Amazon SageMaker Lakehouse]
platform: platform-aws
kind: feature
availability: ga
realises: [engine-interoperability, decoupled-storage-compute, query-federation, catalogue-federation]
resource: https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on the Glue Data Catalog and Lake Formation rather than being a separate store. Managed catalogues can keep data in Redshift Managed Storage yet expose it to Spark and other Iceberg clients; federated catalogues mount Redshift, DynamoDB and Snowflake. It is the target for most zero-ETL integrations.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md), [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake catalog-linked databases](../snowflake/snowflake-catalog-linked-databases.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks catalog federation](../databricks/databricks-catalog-federation.md), [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [Apache Arrow](../open-source/apache-arrow.md), [Apache Polaris](../open-source/apache-polaris.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [Catalogue federation](../../capabilities/storage/catalogue-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md), [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
