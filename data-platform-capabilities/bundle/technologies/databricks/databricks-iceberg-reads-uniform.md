---
type: Technology
id: databricks-iceberg-reads-uniform
title: Databricks Iceberg reads (UniForm)
description: Generates Iceberg metadata asynchronously for Delta tables so that Iceberg clients can read them without copying the data.
formerly: [Delta Lake Universal Format (UniForm)]
platform: platform-databricks
kind: feature
availability: ga
realises: [engine-interoperability, table-format-conversion]
resource: https://docs.databricks.com/aws/en/delta/uniform
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Iceberg clients can only read these tables, and reads can lag the latest Delta commit. Enabling it changes Parquet compression to Zstandard and cannot be reversed. External access to pipeline-managed tables through IcebergCompatV3 is in Public Preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management): Expose one copy of table data in several table formats by generating or translating metadata.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Delta Lake on Databricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md), [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
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
