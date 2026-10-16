---
type: Technology
id: snowflake-pg-lake
title: pg_lake
description: An open-source Postgres extension from Snowflake that reads and writes Iceberg tables and Parquet files in object storage from Postgres.
platform: platform-snowflake
kind: open-source
availability: preview
realises: [engine-interoperability, open-table-formats]
resource: https://docs.snowflake.com/en/user-guide/snowflake-postgres/postgres-pg_lake
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Open source at github.com/Snowflake-Labs/pg_lake. In Snowflake Postgres it is a preview extension. It is the mechanism behind shared Iceberg tables and [data mirroring](snowflake-postgres-data-mirroring.md) between Snowflake Postgres and Snowflake.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake Postgres

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [OneLake](../microsoft/fabric-onelake.md), [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md), [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md), [Teradata Fabric](../teradata/teradata-fabric.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Arrow](../open-source/apache-arrow.md), [Apache XTable (incubating)](../open-source/apache-xtable.md) (preview), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
