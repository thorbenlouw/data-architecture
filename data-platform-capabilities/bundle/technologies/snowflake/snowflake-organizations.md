---
type: Technology
id: snowflake-organizations
title: Snowflake organisations
description: Group multiple Snowflake accounts across regions and clouds under one organisation for account creation, organisation-wide usage views, organisation users and organisational listings.
aliases: [Snowflake organizations]
platform: platform-snowflake
kind: feature
availability: ga
realises: [multi-tenancy, self-service-provisioning, deployment-options]
resource: https://docs.snowflake.com/en/user-guide/organizations
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Separate accounts per domain or environment is the main isolation pattern on Snowflake, alongside databases and roles within an account.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations) (primary): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) (Platform operations): Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspaces](../microsoft/fabric-workspaces.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Resource Manager](../google-cloud/gcp-resource-manager.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md), [Cloudera Anywhere Cloud](../cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Kyuubi](../open-source/apache-kyuubi.md), [Apache Polaris](../open-source/apache-polaris.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
