---
type: Technology
id: sap-bdc-connect
title: SAP Business Data Cloud Connect
description: Bidirectional, zero-copy sharing of data and metadata between BDC and a customer's existing Databricks, Google BigQuery or Snowflake environment.
aliases: [BDC Connect, SAP BDC Connect]
platform: platform-sap
kind: feature
availability: ga
realises: [engine-interoperability, metadata-interoperability, open-protocol-sharing]
resource: https://news.sap.com/2025/11/sap-snowflake-new-data-fabric-innovations-sap-bdc-sap-hana-cloud/
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP BDC Connect for Databricks and for Google BigQuery came first; SAP BDC Connect for Snowflake was announced in November 2025 for the first half of 2026. It differs from SAP Databricks and SAP Snowflake, which SAP sells and runs inside BDC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute) (primary): Let several engines read and write the same tables through open formats and shared catalogues.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md), [Power BI Direct Lake](../microsoft/powerbi-direct-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Snowflake Open Data Sharing](../snowflake/snowflake-open-data-sharing.md) (preview), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md), [Databricks catalog federation](../databricks/databricks-catalog-federation.md), [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Arrow](../open-source/apache-arrow.md), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Apache XTable (incubating)](../open-source/apache-xtable.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
