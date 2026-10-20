---
type: Technology
id: boomi-data-integration
title: Boomi Data Integration
description: Managed ELT service with no-code connectors, CDC replication, Python steps, pipeline orchestration and reverse ETL to operational applications.
formerly: [Rivery]
platform: platform-independent
vendor: Boomi
kind: saas
availability: ga
realises: [saas-connectors, change-data-capture, workflow-orchestration, reverse-etl]
resource: https://boomi.com/platform/data-integration/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This is the former Rivery product, bought by Boomi. Trial sign-up still goes to rivery.io.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration) (primary): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon AppFlow](../aws/aws-appflow.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Glue ETL](../aws/aws-glue-etl.md) | [Reverse ETL](../../capabilities/serving/reverse-etl.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Azure Logic Apps](../microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Google Cloud Application Integration](../google-cloud/gcp-application-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Reverse ETL](../../capabilities/serving/reverse-etl.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
