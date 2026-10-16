---
type: Technology
id: oracle-fusion-data-intelligence
title: Oracle Fusion Data Intelligence
description: Packaged analytics for Oracle Fusion ERP, HCM, SCM and CX applications, with managed pipelines, a prebuilt data model in Autonomous AI Database and Oracle Analytics Cloud content.
aliases: [FDI]
formerly: [Oracle Fusion Analytics Warehouse, FAW, Fusion Analytics]
platform: platform-oracle
kind: saas
availability: ga
realises: [saas-connectors, semantic-layer, dashboards-reports, packaged-analytics, application-data-products]
resource: https://www.infotech.com/research/oracle-analyst-summit-2026-integrating-ai-data-platform-fusion-data-intelligence-and-oci-enterprise-ai
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Relevant when Fusion applications are a major source; it is increasingly linked to the AI Data Platform for extending the packaged model.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Packaged analytics content](../../capabilities/analytics-bi/packaged-analytics.md) (Analytics and BI): Use prebuilt models, metrics and dashboards for a business domain that a vendor delivers and updates.
- [Vendor-supplied application data products](../../capabilities/data-products/application-data-products.md) (Data products): Use governed, documented datasets that business application vendors publish and maintain, instead of building extraction.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Analytics

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Datastream](../google-cloud/gcp-datastream.md), [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md), [Vendor-supplied application data products](../../capabilities/data-products/application-data-products.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Data Integration](../independent/boomi-data-integration.md), [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
