---
type: Technology
id: ibm-watsonx-data
title: IBM watsonx.data
description: Open lakehouse service that runs Presto, Spark, OpenSearch and Cassandra engines over Iceberg, Delta and Hive tables in object storage with shared catalogues and access policies.
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- engine-interoperability
- open-table-formats
- decoupled-storage-compute
- hybrid-data-plane
- table-catalogue
resource: https://www.ibm.com/products/watsonx-data
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Delivered as SaaS on IBM Cloud and AWS, as self-managed software on IBM Software Hub, or in the customer's own cloud account. SQL runs on the [Presto engine](ibm-watsonx-data-presto.md) and data engineering on the [Spark engine](ibm-watsonx-data-spark.md); OpenSearch serves search and retrieval, and Astra DB is the operational NoSQL engine. GPU-accelerated Presto is in technical preview. Often used to offload work from a costly warehouse while keeping data in open formats.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx, IBM watsonx.data

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake](../microsoft/fabric-onelake.md), [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md), [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md), [Teradata Fabric](../teradata/teradata-fabric.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Arrow](../open-source/apache-arrow.md), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Trino](../open-source/trino.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
