---
type: Technology
id: aws-dms
title: AWS Database Migration Service
description: Service that copies data between databases with a full load followed by ongoing change capture from transaction logs, and converts schemas between engines.
aliases: [AWS DMS, DMS Serverless, DMS Schema Conversion]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- change-data-capture
- database-extraction
- data-reconciliation
- database-migration
- code-translation
resource: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Offers provisioned replication instances and DMS Serverless, data validation between source and target, and DMS Schema Conversion (with AWS SCT as a desktop alternative). End of support was announced for DMS Fleet Advisor in May 2025. Also powers zero-ETL from self-managed databases.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) (Data quality and observability): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Database migration](../../capabilities/platform-operations/database-migration.md) (Platform operations): Move databases to new engines or platforms, converting schemas and keeping data in sync until cut-over.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Copy job](../microsoft/fabric-copy-job.md), [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Eventstream](../microsoft/fabric-eventstream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Datastream](../google-cloud/gcp-datastream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Database migration](../../capabilities/platform-operations/database-migration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md), [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database migration](../../capabilities/platform-operations/database-migration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md), [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Qlik Replicate](../independent/qlik-replicate.md), [Striim Cloud](../independent/striim-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
