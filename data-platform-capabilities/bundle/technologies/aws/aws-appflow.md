---
type: Technology
id: aws-appflow
title: Amazon AppFlow
description: No-code service that moves data on demand, on schedule or on event between SaaS applications and AWS services.
platform: platform-aws
kind: managed-service
availability: ga
realises: [saas-connectors, reverse-etl, custom-connectors]
resource: https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Can write back to some SaaS applications such as Salesforce, which covers simple reverse ETL. A custom connector SDK (Python or Java) covers other APIs. Glue native SaaS connectors and zero-ETL integrations now cover many of the same sources for analytical ingestion.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [Datastream](../google-cloud/gcp-datastream.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Data Integration](../independent/boomi-data-integration.md), [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) |
