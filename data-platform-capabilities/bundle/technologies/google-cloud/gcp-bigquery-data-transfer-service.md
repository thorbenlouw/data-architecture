---
type: Technology
id: gcp-bigquery-data-transfer-service
title: BigQuery Data Transfer Service
description: Scheduled, managed loads into BigQuery from Google marketing products, SaaS applications, other warehouses, databases and cloud object stores.
aliases: [BigQuery DTS]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [saas-connectors, database-extraction, file-ingestion]
resource: https://docs.cloud.google.com/bigquery/docs/dts-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sources include Salesforce, ServiceNow, Google Ads, GA4, Redshift, Teradata, Snowflake (GA April 2026), Oracle, MySQL, PostgreSQL, S3 and Azure Blob; HubSpot, Stripe, Shopify, SQL Server and others are in preview. It has a remote MCP server.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
