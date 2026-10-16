---
type: Technology
id: clickhouse-clickpipes-cdc
title: ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)
description: ClickPipes connectors that take an initial snapshot of source tables and then replicate inserts, updates and deletes from Postgres, MySQL or MongoDB logs into ClickHouse, plus a BigQuery connector for bulk and incremental loads.
aliases: [PeerDB]
platform: platform-clickhouse
kind: feature
availability: ga
realises: [change-data-capture, database-replication, database-extraction]
resource: https://clickhouse.com/docs/integrations/clickpipes/postgres
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Postgres CDC (GA May 2025) and MySQL CDC (GA September 2026) are stable; MongoDB CDC is in public beta (January 2026) and BigQuery in private preview (February 2026). The CDC engine is PeerDB, acquired by ClickHouse in 2024, whose open-source project can still be self-hosted. Targets are usually ReplacingMergeTree tables with version and deleted-flag columns, so deduplication happens at merge or query time. The older MaterializedPostgreSQL engine is experimental and not supported in Cloud.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud, ClickPipes

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Copy job](../microsoft/fabric-copy-job.md), [Fabric Eventstream](../microsoft/fabric-eventstream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md), [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Qlik Replicate](../independent/qlik-replicate.md), [Striim Cloud](../independent/striim-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
