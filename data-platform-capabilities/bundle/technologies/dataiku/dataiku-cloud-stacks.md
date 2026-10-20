---
type: Technology
id: dataiku-cloud-stacks
title: Dataiku Cloud Stacks and Fleet Manager
description: Self-managed deployment of Dataiku in the customer's AWS, Azure or Google Cloud account, where Fleet Manager creates, upgrades, backs up and configures the Dataiku instances.
aliases: [Fleet Manager, Dataiku Cloud Stacks]
platform: platform-dataiku
kind: software
availability: ga
realises: [deployment-options, backup-restore]
resource: https://doc.dataiku.com/dss/latest/installation/cloudstacks-aws/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Fleet Manager is itself deployed from a template supplied by Dataiku, such as an AWS CloudFormation template, and each Dataiku node (design, automation or deployer) runs on its own virtual machine. Everything runs in the customer's tenant, so Dataiku has no access to the data. Dataiku can also be installed by hand on Linux servers on premises.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations) (primary): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Report Server](../microsoft/powerbi-report-server.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake organisations](../snowflake/snowflake-organizations.md), [Snowflake Fail-safe](../snowflake/snowflake-fail-safe.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud backups and BACKUP/RESTORE](../clickhouse/clickhouse-backups.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Intelligent Data Management Cloud (IDMC)](../informatica/informatica-idmc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Autonomous Knowledge Platform](../teradata/teradata-autonomous-knowledge-platform.md), [Teradata Factory](../teradata/teradata-factory.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md), [Confluent Platform](../ibm/confluent-platform.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya](../sas/sas-viya.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
