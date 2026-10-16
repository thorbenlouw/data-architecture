---
type: Technology
id: estuary
title: Estuary
description: Data movement platform that combines CDC, streaming and batch pipelines, backfilling history and then capturing changes into collections stored in the customer's bucket.
formerly: [Estuary Flow]
platform: platform-independent
vendor: Estuary
kind: saas
availability: ga
realises:
- change-data-capture
- streaming-ingestion
- saas-connectors
- stream-processing
- hybrid-data-plane
- idempotent-loading
resource: https://estuary.dev/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Derivations transform records in flight using SQL, Python or TypeScript. Materialisations write to destinations at intervals from real time to hourly. It can run on Estuary's shared infrastructure, a private data plane or BYOC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Copy job](../microsoft/fabric-copy-job.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md), [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Stream processing](../../capabilities/processing/stream-processing.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md), [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
