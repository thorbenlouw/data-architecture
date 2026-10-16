---
type: Technology
id: cloudera-on-cloud
title: Cloudera on cloud
description: Cloudera's platform running in the customer's AWS, Azure or Google Cloud account, with a Cloudera-hosted Management Console that creates environments, data lakes and Data Hub clusters.
aliases: [Cloudera Data Hub]
formerly: [CDP Public Cloud, Cloudera Data Platform Public Cloud]
platform: platform-cloudera
kind: managed-service
availability: ga
realises: [multi-tenancy, provisioned-compute, decoupled-storage-compute, hybrid-data-plane]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each environment has an SDX data lake (Ranger, Atlas, Hive Metastore) shared by its data services. Data Hub gives classic, user-sized clusters from templates for workloads that the containerised data services do not cover. Compute runs in the customer's cloud account, so cloud costs are billed separately from Cloudera credits.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations) (primary): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) (Query and compute): Scale storage and compute independently and let several compute clusters work on the same data.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Data Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspaces](../microsoft/fabric-workspaces.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Resource Manager](../google-cloud/gcp-resource-manager.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md), [WarpStream](../ibm/warpstream.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Decoupled storage and compute](../../capabilities/compute/decoupled-storage-compute.md), [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Kyuubi](../open-source/apache-kyuubi.md), [Apache Polaris](../open-source/apache-polaris.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
