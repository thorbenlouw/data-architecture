---
type: Technology
id: airbyte
title: Airbyte
description: Data integration platform with hundreds of prebuilt connectors for loading data from databases, APIs and SaaS applications into warehouses and lakes.
aliases: [Airbyte Core, Airbyte Open Source]
platform: platform-open-source
kind: software
availability: ga
realises:
- saas-connectors
- database-extraction
- api-ingestion
- custom-connectors
- change-data-capture
- idempotent-loading
resource: https://github.com/airbytehq/airbyte
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Source-available rather than fully open source. The platform is under the Elastic License 2.0 (ELv2), which bars offering it as a managed service; connectors and the Connector Development Kit are mostly MIT. A low-code Connector Builder supports API sources. Self-hosted and cloud editions exist.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [Datastream](../google-cloud/gcp-datastream.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) |
