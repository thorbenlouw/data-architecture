---
type: Technology
id: fivetran-managed-data-lake-service
title: Fivetran Managed Data Lake Service
description: Destination option that writes replicated data as Parquet files with Iceberg metadata, and optionally Delta Lake metadata, into the customer's S3, ADLS or GCS storage, and maintains the tables.
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: feature
availability: ga
realises:
- open-table-formats
- table-catalogue
- table-maintenance
- engine-interoperability
- table-format-conversion
resource: https://fivetran.com/docs/managed-data-lake-service
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tables are registered in the Fivetran Catalog, a managed Apache Polaris (Iceberg REST) catalogue, and can also be synced to AWS Glue, OneLake, BigLake Metastore, Unity Catalog or Snowflake catalog-linked databases. It is also the default Iceberg catalogue for dbt Lake Compute.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management): Expose one copy of table data in several table formats by generating or translating metadata.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md), [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md), [Delta Lake on Databricks](../databricks/databricks-delta-lake.md), [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckLake](../open-source/ducklake.md), [Apache Hudi](../open-source/apache-hudi.md), [Apache Paimon](../open-source/apache-paimon.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
