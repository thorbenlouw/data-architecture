---
type: Technology
id: snowflake-native-connectors
title: Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)
description: Connectors packaged as Snowflake Native Apps that ingest and refresh data from SaaS applications and databases incrementally, some using a customer-run agent for change data capture.
platform: platform-snowflake
kind: feature
availability: ga
realises: [saas-connectors, database-replication, custom-connectors]
resource: https://docs.snowflake.com/en/connectors/servicenow/v2/about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is the older connector family. ServiceNow V2 is GA. The PostgreSQL, MySQL, SharePoint and Google Analytics connectors, and the Native SDK for Connectors used to build more, are still in preview. Snowflake is building most new connectors in Openflow, so prefer Openflow CDC connectors, or data mirroring for Snowflake Postgres, for new work.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Fabric open mirroring](../microsoft/fabric-open-mirroring.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
