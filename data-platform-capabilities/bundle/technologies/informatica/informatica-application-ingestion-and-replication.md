---
type: Technology
id: informatica-application-ingestion-and-replication
title: Informatica Application Ingestion and Replication
description: Replicates objects from SaaS and on-premises applications such as Salesforce, SAP and Workday to warehouses, lakes and streaming targets, as a snapshot or continuous change propagation.
formerly: [Cloud Mass Ingestion Applications, Mass Ingestion Applications]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [saas-connectors, change-data-capture]
resource: https://onlinehelp.informatica.com/IICS/prod/CDI/en/cc-cloud-dbi_intro/Introducing_Data_Ingestion_and_Replication.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Use it for no-code bulk replication of application objects with schema drift handling. Use Data Integration when you need transformation on the way in.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Data Ingestion and Replication

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [Amazon AppFlow](../aws/aws-appflow.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Data Integration](../independent/boomi-data-integration.md), [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
