---
type: Technology
id: databricks-managed-iceberg-tables
title: Unity Catalog managed Iceberg tables
description: Apache Iceberg tables (v1 to v3) that Unity Catalog manages, with compaction, snapshot expiry and liquid clustering. Databricks and external engines can read and write them through the Iceberg REST catalogue.
platform: platform-databricks
kind: feature
availability: ga
realises: [open-table-formats, engine-interoperability, table-maintenance]
resource: https://docs.databricks.com/aws/en/iceberg/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed and foreign Iceberg tables and Iceberg v3 features became GA in May 2026. Creating managed Iceberg tables requires predictive optimisation. Iceberg v2 position and equality deletes are not supported.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management) (primary): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md), [OneLake](../microsoft/fabric-onelake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery tables for Apache Iceberg](../google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pg_lake](../snowflake/snowflake-pg-lake.md) (preview), [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Apache Iceberg in Cloudera](../cloudera/cloudera-lakehouse-iceberg.md) | [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hudi](../open-source/apache-hudi.md), [Apache Iceberg](../open-source/apache-iceberg.md), [DuckLake](../open-source/ducklake.md) | [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
