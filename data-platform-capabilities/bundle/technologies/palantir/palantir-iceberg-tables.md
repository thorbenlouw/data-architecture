---
type: Technology
id: palantir-iceberg-tables
title: Iceberg tables in Palantir Foundry
description: Apache Iceberg as an alternative Foundry table type, with an Iceberg REST catalogue that lets external clients such as Snowflake and Jupyter read Foundry-governed tables.
platform: platform-palantir
kind: feature
availability: preview
realises:
- open-table-formats
- table-catalogue
- engine-interoperability
- incremental-processing
- open-protocol-sharing
resource: https://www.palantir.com/docs/foundry/iceberg/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Labelled beta in the documentation. Supports incremental and CDC-style processing on [Apache Iceberg](../open-source/apache-iceberg.md) tables. A Lakehouse Iceberg REST catalogue connector also reads external Iceberg catalogues.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** preview  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed Iceberg tables](../databricks/databricks-managed-iceberg-tables.md), [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md), [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckLake](../open-source/ducklake.md), [Apache Hudi](../open-source/apache-hudi.md), [Apache Iceberg](../open-source/apache-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
