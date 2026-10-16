---
type: Capability
id: query-federation
title: Query federation
description: Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
aliases:
- data virtualisation
- data virtualization
- federated query
- external tables
- shortcuts
- zero-copy access
broader: [compute]
related:
- catalogue-federation
- database-replication
- data-residency
- ad-hoc-analysis
- engine-interoperability
depends_on: [sql-query-engine]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A query federation engine reads data in place instead of loading it first, in two ways. Connector federation sends parts of a query to another database, warehouse or SaaS API, pushing down filters and column selection, and finishes joins itself: an analyst joins last year's orders in the lakehouse with today's open orders in PostgreSQL in one statement. Virtual references, often called external tables or shortcuts, register files or tables held in other storage accounts or clouds so the engine scans them directly as if they were local.

It suits exploration, data that may not be copied for legal reasons and the period before a pipeline is worth building. It fits heavy, repeated analytics poorly: speed depends on the source and the network, and each query adds load or egress cost. Catalogue federation differs in exposing another catalogue's metadata and permissions; replication differs in copying the data.

# Key considerations

- Check pushdown support for each connector. Without it, the engine pulls whole tables across the network just to filter them.
- Federated queries load the source. Agree limits with owners of operational databases, or point queries at read replicas.
- Security must hold end to end: which credentials the connector uses, and whether the user's own permissions in the source apply.
- Repeated federated queries on the same data are a sign that it should be replicated or cached instead.

# Questions to ask

- Which data cannot be copied into the platform, and why?
- How often would federated queries run, and how much data would they move?
- Can the source systems take extra query load, and at what times?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Catalogue federation](../storage/catalogue-federation.md), [Data residency and sovereignty](../governance/data-residency.md), [Database replication and mirroring](../ingestion-integration/database-replication.md), [Multi-engine interoperability](engine-interoperability.md) |
| Depends on | [SQL query engine](sql-query-engine.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability · [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – mesh supervision plane

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Athena federated query and federated catalogues | [Amazon Athena](../../technologies/aws/aws-athena.md), [Amazon Redshift federated query](../../technologies/aws/aws-redshift-federated-query.md), [Amazon Redshift Spectrum](../../technologies/aws/aws-redshift-spectrum.md), [Lakehouse architecture of Amazon SageMaker](../../technologies/aws/aws-sagemaker-lakehouse.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Shortcuts and metadata mirroring | [Azure Synapse Analytics](../../technologies/microsoft/azure-synapse-analytics.md), [OneLake shortcuts](../../technologies/microsoft/fabric-onelake-shortcuts.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery external tables and load jobs](../../technologies/google-cloud/gcp-bigquery-external-tables.md), [BigQuery federated queries](../../technologies/google-cloud/gcp-bigquery-federated-queries.md), [BigQuery Omni](../../technologies/google-cloud/gcp-bigquery-omni.md), [Google Cloud Lakehouse](../../technologies/google-cloud/gcp-lakehouse.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | catalog-linked databases and external tables | [Snowflake external tables](../../technologies/snowflake/snowflake-external-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakehouse Federation | [Lakehouse Federation (query federation)](../../technologies/databricks/databricks-lakehouse-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Table functions and integration table engines | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../../technologies/clickhouse/clickhouse-data-lake.md), [ClickHouse dictionaries](../../technologies/clickhouse/clickhouse-dictionaries.md), [ClickHouse integration table engines and table functions](../../technologies/clickhouse/clickhouse-integration-engines.md), [ClickHouse Managed Postgres](../../technologies/clickhouse/clickhouse-managed-postgres.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [MySQL HeatWave](../../technologies/oracle/oracle-mysql-heatwave.md), [Oracle Autonomous AI Lakehouse](../../technologies/oracle/oracle-autonomous-ai-lakehouse.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere](../../technologies/sap/sap-datasphere.md), [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) | Teradata Fabric (QueryGrid) | [Teradata Fabric](../../technologies/teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../../technologies/teradata/teradata-open-table-format.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Presto (C++) engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-presto.md) |
| [Palantir](../../platforms/platform-palantir.md) | Virtual tables | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Doris](../../technologies/open-source/apache-doris.md), [DuckDB](../../technologies/open-source/duckdb.md), [Presto](../../technologies/open-source/presto.md), [Trino](../../technologies/open-source/trino.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Denodo Platform](../../technologies/independent/denodo-platform.md), [Starburst Enterprise](../../technologies/independent/starburst-enterprise.md), [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md), [StarTree Cloud](../../technologies/independent/startree-cloud.md) |
