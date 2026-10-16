---
type: Technology
id: databricks-iceberg-rest-catalog
title: Unity Catalog Iceberg REST Catalog API
description: An Iceberg REST catalogue endpoint with credential vending. Spark, Flink, Trino, Snowflake and other engines can use it to read and write Unity Catalog tables.
platform: platform-databricks
kind: feature
availability: ga
realises: [engine-interoperability, metadata-interoperability, credential-vending]
resource: https://docs.databricks.com/aws/en/iceberg/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Unity REST API serves Delta clients, and external access to views through it became GA in October 2026. External engines cannot read Unity Catalog views through the Iceberg endpoint. Credential vending is not available on default-storage workspaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md), [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Snowflake catalog-linked databases](../snowflake/snowflake-catalog-linked-databases.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Apache Arrow](../open-source/apache-arrow.md), [Unity Catalog (open source)](../open-source/unity-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
