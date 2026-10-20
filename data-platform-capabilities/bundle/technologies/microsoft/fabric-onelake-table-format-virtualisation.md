---
type: Technology
id: fabric-onelake-table-format-virtualisation
title: OneLake table format virtualization (Delta Lake and Apache Iceberg)
description: Generates Iceberg metadata for Delta tables and Delta metadata for Iceberg tables in OneLake, so readers of either format can use the same Parquet files.
aliases: [OneLake metadata virtualization, OneLake Iceberg tables]
platform: platform-microsoft
kind: feature
availability: unconfirmed
realises: [engine-interoperability, table-format-conversion]
resource: https://learn.microsoft.com/en-us/fabric/onelake/onelake-iceberg-tables
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works on Parquet data files only, and source tables must have fewer than 5,000 commits, so transaction logs and manifests need regular compaction. Not supported in tenants or workspaces with private links enabled, and not yet available in every region. Used for interoperability with Snowflake, which can write Iceberg tables to OneLake for Fabric engines to read.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management): Expose one copy of table data in several table formats by generating or translating metadata.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** unconfirmed  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md), [Databricks catalog federation](../databricks/databricks-catalog-federation.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache XTable (incubating)](../open-source/apache-xtable.md) (preview), [Apache Arrow](../open-source/apache-arrow.md), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
