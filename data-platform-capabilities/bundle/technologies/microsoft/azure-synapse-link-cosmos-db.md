---
type: Technology
id: azure-synapse-link-cosmos-db
title: Azure Synapse Link for Azure Cosmos DB
description: Replicates Cosmos DB containers to an analytical column store queryable from Synapse without ETL.
platform: platform-microsoft
kind: feature
availability: deprecated
realises: [database-replication]
resource: https://learn.microsoft.com/en-us/azure/cosmos-db/synapse-link
tags: [microsoft]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

New accounts cannot enable it from 31 March 2026; existing use is supported until 31 March 2029. Replacement is Fabric mirroring for Cosmos DB.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration) (primary): Replicate operational databases continuously into the analytical platform without building pipelines.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md), [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Qlik Replicate](../independent/qlik-replicate.md), [Striim Cloud](../independent/striim-cloud.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
