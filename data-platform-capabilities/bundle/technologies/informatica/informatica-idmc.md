---
type: Technology
id: informatica-idmc
title: Informatica Intelligent Data Management Cloud (IDMC)
description: Multi-cloud SaaS platform that hosts all of Informatica's cloud data management services behind one control plane, with jobs run either on customer-hosted Secure Agents or on Informatica-managed serverless runtimes.
aliases: [IDMC]
formerly: [Informatica Intelligent Cloud Services (IICS), Informatica Cloud]
platform: platform-informatica
kind: saas
availability: ga
realises: [deployment-options, data-residency, hybrid-data-plane]
resource: https://onlinehelp.informatica.com/IICS/prod/mde/en/zz-cloud-helpoverview/Help_for_Other_Services.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Organisations are provisioned on regional points of delivery (PODs) on AWS, Azure and Google Cloud. The Secure Agent, a lightweight runtime installed on Linux or Windows inside the customer network, keeps data processing on premises or in the customer's VPC while metadata and design live in IDMC. The IICS name still appears in documentation URLs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations) (primary): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Data residency and sovereignty](../../capabilities/governance/data-residency.md) (Governance and compliance): Keep data and its processing in approved jurisdictions and prove that you have.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Report Server](../microsoft/powerbi-report-server.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Autonomous Knowledge Platform](../teradata/teradata-autonomous-knowledge-platform.md), [Teradata Factory](../teradata/teradata-factory.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md), [Confluent Platform](../ibm/confluent-platform.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya](../sas/sas-viya.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud](../dataiku/dataiku-cloud.md), [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
