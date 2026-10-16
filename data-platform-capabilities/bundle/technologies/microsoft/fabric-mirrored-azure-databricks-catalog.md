---
type: Technology
id: fabric-mirrored-azure-databricks-catalog
title: Mirrored Azure Databricks Catalog
description: Synchronises Unity Catalog metadata into Fabric and exposes the tables through shortcuts, without copying data.
platform: platform-microsoft
kind: feature
availability: ga
realises: [catalogue-federation, engine-interoperability]
resource: https://learn.microsoft.com/en-us/fabric/mirroring/azure-databricks
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A form of metadata mirroring; Snowflake, Dremio (preview) and other catalogues are also supported this way. The main integration point between Azure Databricks and Fabric/Power BI. Not supported in CMK-enabled workspaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management) (primary): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Databases

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md), [Amazon Athena](../aws/aws-athena.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake catalog-linked databases](../snowflake/snowflake-catalog-linked-databases.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks catalog federation](../databricks/databricks-catalog-federation.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse DataLakeCatalog database engine](../clickhouse/clickhouse-datalakecatalog.md) (preview) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Polaris](../open-source/apache-polaris.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
