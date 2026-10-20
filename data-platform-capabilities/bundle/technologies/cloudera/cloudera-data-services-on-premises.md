---
type: Technology
id: cloudera-data-services-on-premises
title: Cloudera Data Services on premises
description: Kubernetes-based deployment of the Data Engineering, Data Warehouse and Cloudera AI services on customer infrastructure, attached to a Cloudera Base cluster.
formerly: [CDP Private Cloud Data Services]
platform: platform-cloudera
kind: software
availability: ga
realises: [deployment-options, container-services, workload-isolation, self-service-provisioning]
resource: https://docs.cloudera.com/cdp-private-cloud-data-services/latest/overview/topics/cdppvc-data-services-overview.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs on Red Hat OpenShift or Cloudera's embedded container service, release line 1.5.x in 2026. It gives on-premises users the same containerised, autoscaling services as on cloud, sharing SDX with the Base cluster.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations) (primary): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Container services](../../capabilities/compute/container-services.md) (Query and compute): Run custom containerised applications and services next to the data, inside the platform's security boundary.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) (Platform operations): Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Data Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Report Server](../microsoft/powerbi-report-server.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Omni](../google-cloud/gcp-bigquery-omni.md), [AlloyDB for PostgreSQL](../google-cloud/gcp-alloydb.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake organisations](../snowflake/snowflake-organizations.md), [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Intelligent Data Management Cloud (IDMC)](../informatica/informatica-idmc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../oracle/oracle-database-multicloud.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Autonomous Knowledge Platform](../teradata/teradata-autonomous-knowledge-platform.md), [Teradata Factory](../teradata/teradata-factory.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md), [Confluent Platform](../ibm/confluent-platform.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya](../sas/sas-viya.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Cloud](../dataiku/dataiku-cloud.md), [Dataiku Cloud Stacks and Fleet Manager](../dataiku/dataiku-cloud-stacks.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Starburst Enterprise](../independent/starburst-enterprise.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) |
