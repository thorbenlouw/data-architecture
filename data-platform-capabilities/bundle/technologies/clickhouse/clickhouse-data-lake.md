---
type: Technology
id: clickhouse-data-lake
title: ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)
description: Table functions and engines that query Apache Iceberg, Delta Lake, Apache Hudi and Apache Paimon tables in object storage, with Iceberg time travel and the ability to create and insert into Iceberg tables.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [query-federation, engine-interoperability, open-table-formats, time-travel, data-export]
resource: https://clickhouse.com/docs/use-cases/data-lake/support-matrix
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Iceberg reads cover partition pruning, schema evolution, position and equality deletes and v1/v2 tables, with partial v3 support (deletion-vector reads). Iceberg INSERT is beta from 26.2 and table creation, DELETE and compaction are experimental. Delta Lake INSERT is beta through the Delta Kernel, Hudi support is read-only, and Paimon support is experimental and read-only. Typical uses are querying the lakehouse in place and offloading cold or derived data to Iceberg. On-Demand Compute (Cloud, private preview September 2026) adds burst capacity for these queries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Time travel](../../capabilities/storage/time-travel.md) (Storage and table management): Query or restore a table as it was at an earlier point in time or version.
- [Data export](../../capabilities/serving/data-export.md) (Serving and activation): Unload query results or tables to files and external systems in bulk.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse table engines

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery federated queries](../google-cloud/gcp-bigquery-federated-queries.md), [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md), [pg_lake](../snowflake/snowflake-pg-lake.md) (preview) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md), [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open table formats](../../capabilities/storage/open-table-formats.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md), [Open table formats](../../capabilities/storage/open-table-formats.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Data export](../../capabilities/serving/data-export.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Trino](../open-source/trino.md), [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Starburst Galaxy](../independent/starburst-galaxy.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Query federation](../../capabilities/compute/query-federation.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
