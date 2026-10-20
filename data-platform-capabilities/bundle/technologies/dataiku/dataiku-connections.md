---
type: Technology
id: dataiku-connections
title: Dataiku connections
description: Connectors that read and write data in SQL databases, cloud warehouses, object storage, Iceberg tables, NoSQL stores and business applications, and let recipes run inside the connected engine.
platform: platform-dataiku
kind: feature
availability: ga
realises: [database-extraction, saas-connectors, engine-interoperability, custom-connectors]
resource: https://doc.dataiku.com/dss/latest/connecting/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Has dedicated connectors for Snowflake, Databricks, BigQuery, Redshift, Azure Synapse and Microsoft Fabric Warehouse, and Apache Iceberg support, including REST catalogues, since version 14.4. Dataset plugins add connectors for other sources. Datasets usually stay in the source system; visual and SQL recipes on in-database connections are pushed down to that engine instead of moving data into Dataiku.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration) (primary): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [Amazon AppFlow](../aws/aws-appflow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Fabric Copy job](../microsoft/fabric-copy-job.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Hub](../sas/sas-data-hub.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Airbyte](../open-source/airbyte.md), [dlt (data load tool)](../open-source/dlt.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
