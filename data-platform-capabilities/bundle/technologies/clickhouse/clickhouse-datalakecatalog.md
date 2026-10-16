---
type: Technology
id: clickhouse-datalakecatalog
title: ClickHouse DataLakeCatalog database engine
description: Database engine that connects to an external lakehouse catalogue and exposes its tables as ClickHouse tables for querying and joining.
platform: platform-clickhouse
kind: feature
availability: preview
realises: [catalogue-federation, engine-interoperability]
resource: https://clickhouse.com/docs/engines/database-engines/datalakecatalog
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports AWS Glue, Databricks Unity Catalog, Iceberg REST catalogues, BigLake Metastore, Lakekeeper, Microsoft OneLake (beta) and Project Nessie and Hive Metastore (experimental). All need beta or experimental settings; only Unity Catalog and OneLake allow creating and inserting into tables. Cloud added these integrations through 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management) (primary): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** preview  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md), [Amazon Athena](../aws/aws-athena.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirrored Azure Databricks Catalog](../microsoft/fabric-mirrored-azure-databricks-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake catalog-linked databases](../snowflake/snowflake-catalog-linked-databases.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks catalog federation](../databricks/databricks-catalog-federation.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Polaris](../open-source/apache-polaris.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
