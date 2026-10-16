---
type: Technology
id: snowflake-openflow
title: Snowflake Openflow
description: A managed integration service, built on Apache NiFi, that runs prebuilt and custom connectors for databases, SaaS, streams and unstructured content in batch or streaming mode.
platform: platform-snowflake
kind: managed-service
availability: ga
realises:
- change-data-capture
- saas-connectors
- unstructured-ingestion
- streaming-ingestion
- custom-connectors
- hybrid-data-plane
resource: https://docs.snowflake.com/en/user-guide/data-integration/openflow/about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Comes from the Datavolo acquisition (2024). It runs either as a Snowflake deployment on Snowpark Container Services or as a BYOC data plane in your own cloud. Second-generation deployments became GA in September 2026, and gen 1 creation is retired. Gen 2 connector configuration is still in preview. Connectors include CDC for Oracle, SQL Server, PostgreSQL, MySQL and MongoDB, plus Salesforce, Workday, Jira, Kafka, Kinesis, SharePoint and Google Drive. There is also an outbound Snowflake-to-Kafka connector.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Copy job](../microsoft/fabric-copy-job.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md), [IBM StreamSets](../ibm/ibm-streamsets.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md), [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md), [Airbyte Cloud](../independent/airbyte-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
