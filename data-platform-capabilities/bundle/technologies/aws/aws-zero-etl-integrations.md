---
type: Technology
id: aws-zero-etl-integrations
title: AWS zero-ETL integrations
description: Managed replication that keeps tables from AWS databases, self-managed databases and SaaS applications continuously in step in Amazon Redshift or the SageMaker lakehouse.
platform: platform-aws
kind: feature
availability: ga
realises: [database-replication, change-data-capture, saas-connectors]
resource: https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sources include Aurora MySQL and PostgreSQL, RDS for MySQL, PostgreSQL and Oracle, DynamoDB, Oracle Database@AWS, self-managed MySQL, PostgreSQL, SQL Server and Oracle (via DMS, Redshift provisioned target only), and SaaS such as Salesforce, SAP OData, ServiceNow, Zendesk, Zoho CRM and Meta ads. Targets are Redshift, S3, S3 Tables or Redshift Managed Storage. Configured through Glue or Redshift.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration) (primary): Replicate operational databases continuously into the analytical platform without building pipelines.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric open mirroring](../microsoft/fabric-open-mirroring.md), [SQL database in Microsoft Fabric](../microsoft/fabric-sql-database.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md), [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../snowflake/snowflake-native-connectors.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md), [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Qlik Replicate](../independent/qlik-replicate.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
