---
type: Capability
id: saas-connectors
title: SaaS application connectors
description: Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
aliases: [managed connectors, ELT connectors]
broader: [batch-ingestion]
related: [api-ingestion, custom-connectors, application-data-products, reverse-etl]
depends_on: [secrets-management]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A SaaS connector is prebuilt code that knows how to authenticate to one business application, which objects it exposes, how to page through them and how to read only what changed. Pointed at a CRM, a connector lists accounts, contacts and opportunities, maps custom fields to columns and syncs changes into the platform every hour. The connector's maintainer, a vendor or an open-source community, updates it when the application's API changes.

Most organisations run dozens of SaaS applications, and writing and maintaining extraction code for each is poor use of engineering time. Connectors are bought as a managed service or run from an open-source catalogue, and are often priced by rows synced. Quality varies widely: some handle incremental sync, deletes and custom objects, others only full reloads of standard objects. Where an application vendor publishes governed datasets directly, vendor-supplied data products can remove the need for extraction.

# Key considerations

- Check each connector for incremental sync, delete handling, custom fields and history. Coverage of standard objects alone is often not enough.
- Usage-based pricing rises sharply on objects that change often. Estimate monthly changed rows before choosing.
- SaaS API quotas are shared with other integrations. Agree a budget with application owners so analytics syncs do not block operational ones.
- Connector output schemas change when the application changes. Plan how downstream models absorb renamed or added fields.

# Questions to ask

- Which applications hold data needed for analytics, and which objects and custom fields matter?
- Do prebuilt connectors exist for each, and do they support incremental sync and deletes?
- Who owns the credentials and API quotas for each application?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Batch ingestion](batch-ingestion.md) |
| Related | [API ingestion](api-ingestion.md), [Custom connector development](custom-connectors.md), [Packaged analytics content](../analytics-bi/packaged-analytics.md), [Reverse ETL](../serving/reverse-etl.md), [Vendor-supplied application data products](../data-products/application-data-products.md) |
| Depends on | [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Use cases:** [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from)
- **Patterns:** [ELT](../../patterns/elt.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon AppFlow](../../technologies/aws/aws-appflow.md), [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md), [AWS zero-ETL integrations](../../technologies/aws/aws-zero-etl-integrations.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Azure Logic Apps](../../technologies/microsoft/azure-logic-apps.md), [Fabric Dataflow Gen2](../../technologies/microsoft/fabric-dataflow-gen2.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Data Transfer Service](../../technologies/google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../../technologies/google-cloud/gcp-data-fusion.md), [Datastream](../../technologies/google-cloud/gcp-datastream.md), [Google Cloud Application Integration](../../technologies/google-cloud/gcp-application-integration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../../technologies/snowflake/snowflake-native-connectors.md), [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakeflow Connect managed connectors | [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Application Ingestion and Replication](../../technologies/informatica/informatica-application-ingestion-and-replication.md), [Informatica Cloud Data Integration (CDI)](../../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Data 360 Connector and Scanner](../../technologies/informatica/informatica-data-360-connector-and-scanner.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Fusion Data Intelligence](../../technologies/oracle/oracle-fusion-data-intelligence.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data products](../../technologies/sap/sap-bdc-data-products.md), [SAP BW/4HANA](../../technologies/sap/sap-bw4hana.md), [SAP Datasphere replication flows](../../technologies/sap/sap-datasphere-replication-flows.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku connections](../../technologies/dataiku/dataiku-connections.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Agents](../../technologies/independent/airbyte-agents.md) (unconfirmed), [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Boomi Data Integration](../../technologies/independent/boomi-data-integration.md), [Domo](../../technologies/independent/domo.md), [Estuary](../../technologies/independent/estuary.md), [Fivetran](../../technologies/independent/fivetran.md), [Matillion Maia Foundation](../../technologies/independent/matillion-maia-foundation.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md) |
