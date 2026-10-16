---
type: Technology
id: denodo-platform
title: Denodo Platform
description: Logical data management and virtualisation platform that presents many sources as one governed semantic model and pushes queries down to them.
aliases: [Denodo]
platform: platform-independent
vendor: Denodo
kind: software
availability: ga
realises: [query-federation, semantic-layer, query-acceleration, data-marketplace, sql-access]
resource: https://www.denodo.com/en/denodo-platform/overview
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Denodo Agora is the fully managed cloud edition, and Denodo Express is free. The Denodo AI SDK supports building RAG and natural-language query applications over the virtual layer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute) (primary): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Query acceleration](../../capabilities/compute/query-acceleration.md) (Query and compute): Speed up repeated or selective queries using caches, precomputed results and indexes.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.
- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation): Connect tools and code to the platform through standard drivers and protocols.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../aws/aws-sagemaker-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery federated queries](../google-cloud/gcp-bigquery-federated-queries.md), [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md), [ClickHouse dictionaries](../clickhouse/clickhouse-dictionaries.md) | [Query federation](../../capabilities/compute/query-federation.md), [Query acceleration](../../capabilities/compute/query-acceleration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Warehouse](../cloudera/cloudera-data-warehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md), [Oracle Autonomous AI Lakehouse](../oracle/oracle-autonomous-ai-lakehouse.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md), [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Query federation](../../capabilities/compute/query-federation.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../teradata/teradata-open-table-format.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Query federation](../../capabilities/compute/query-federation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DuckDB](../open-source/duckdb.md), [Presto](../open-source/presto.md), [Trino](../open-source/trino.md) | [Query federation](../../capabilities/compute/query-federation.md) |
