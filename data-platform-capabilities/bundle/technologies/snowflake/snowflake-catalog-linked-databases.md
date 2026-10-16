---
type: Technology
id: snowflake-catalog-linked-databases
title: Snowflake catalog-linked databases
description: Databases linked to an external Iceberg REST catalogue (for example AWS Glue, Unity Catalog, Open Catalog, BigLake or S3 Tables) that discover and sync remote namespaces and tables automatically for querying and writing.
platform: platform-snowflake
kind: feature
availability: ga
realises: [catalogue-federation, engine-interoperability]
resource: https://docs.snowflake.com/en/user-guide/tables-iceberg-catalog-linked-database
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is Snowflake's form of catalogue federation. Remote tables can be queried and written, and shared through listings. Equality deletes and UNDROP are not supported.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management) (primary): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md), [Amazon Athena](../aws/aws-athena.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks catalog federation](../databricks/databricks-catalog-federation.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Polaris](../open-source/apache-polaris.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
