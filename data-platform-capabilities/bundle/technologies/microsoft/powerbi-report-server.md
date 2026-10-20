---
type: Technology
id: powerbi-report-server
title: Power BI Report Server
description: An on-premises server for publishing Power BI and paginated reports where cloud services cannot be used.
platform: platform-microsoft
kind: software
availability: ga
realises: [deployment-options, dashboards-reports, paginated-reports]
resource: https://learn.microsoft.com/en-us/power-bi/report-server/get-started
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Licensed through Power BI Premium or SQL Server Enterprise with Software Assurance; lags the cloud service in features.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations) (primary): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) (Analytics and BI): Produce formatted, printable reports with precise layout for operational and regulatory use.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Intelligent Data Management Cloud (IDMC)](../informatica/informatica-idmc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Autonomous Knowledge Platform](../teradata/teradata-autonomous-knowledge-platform.md), [Teradata Factory](../teradata/teradata-factory.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md), [Confluent Platform](../ibm/confluent-platform.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya](../sas/sas-viya.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud](../dataiku/dataiku-cloud.md), [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
