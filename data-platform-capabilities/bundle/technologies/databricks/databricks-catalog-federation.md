---
type: Technology
id: databricks-catalog-federation
title: Databricks catalog federation
description: Mounts external catalogues such as Hive metastore, AWS Glue, Snowflake Horizon and Salesforce Data 360 as foreign catalogs, read from object storage under Unity Catalog governance.
platform: platform-databricks
kind: feature
availability: ga
realises: [catalogue-federation, engine-interoperability, metadata-interoperability]
resource: https://docs.databricks.com/aws/en/query-federation/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Foreign tables are read-only. It is commonly used to migrate from the Hive metastore one step at a time or to run a lasting hybrid with Glue or Snowflake. Some sources may still be in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management) (primary): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [Amazon Athena](../aws/aws-athena.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake catalog-linked databases](../snowflake/snowflake-catalog-linked-databases.md), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Polaris](../open-source/apache-polaris.md), [Apache Gravitino](../open-source/apache-gravitino.md), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
