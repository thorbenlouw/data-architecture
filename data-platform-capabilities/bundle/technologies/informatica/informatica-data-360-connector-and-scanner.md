---
type: Technology
id: informatica-data-360-connector-and-scanner
title: Informatica Data 360 Connector and Scanner
description: Native connector for two-way batch and real-time data exchange with Salesforce Data 360, plus a catalogue scanner that brings Data 360 and Agentforce Marketing objects into CDGC lineage.
platform: platform-informatica
kind: feature
availability: ga
realises: [saas-connectors, reverse-etl, metadata-harvesting, cross-system-lineage]
resource: https://www.informatica.com/blogs/activate-enterprise-data-with-trusted-context-new-capabilities-in-idmcs-spring-2026-release.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA in Spring 2026. Salesforce Data 360 was formerly Salesforce Data Cloud. The MDM integration with Data 360 was announced for Q3 2026, and Policy Pushdown for Tableau is GA. These are the main product links since the Salesforce acquisition.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Datastream](../google-cloud/gcp-datastream.md), [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Data Integration](../independent/boomi-data-integration.md), [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
