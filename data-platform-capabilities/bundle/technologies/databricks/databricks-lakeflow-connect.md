---
type: Technology
id: databricks-lakeflow-connect
title: Lakeflow Connect
description: Managed connectors that ingest data incrementally from SaaS applications, databases (including change data capture), file sources and message buses into Unity Catalog tables, running on serverless Lakeflow pipelines.
platform: platform-databricks
kind: managed-service
availability: ga
realises:
- saas-connectors
- change-data-capture
- database-extraction
- unstructured-ingestion
- custom-connectors
- database-replication
resource: https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Connectors have their own release stages. Salesforce, Workday, ServiceNow, SharePoint, Google Drive, NetSuite, HubSpot, SQL Server, MySQL and PostgreSQL CDC are among them, and many newer connectors (audit-log and security sources added through 2026) are in Beta. Query-based connectors (GA May 2026) read databases without setting up CDC. Open-source community connectors (Beta, May 2026) and PySpark custom data sources cover other sources and generic APIs. Connectors bill under Lakeflow Connect.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [Amazon AppFlow](../aws/aws-appflow.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
