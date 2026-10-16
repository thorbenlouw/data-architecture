---
type: Technology
id: fabric-workspaces
title: Fabric workspaces
description: Containers for Fabric items with their own roles, capacity assignment, Git connection and network settings.
platform: platform-microsoft
kind: feature
availability: ga
realises: [multi-tenancy, role-based-access, analytical-sandboxes]
resource: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The unit of security, deployment and isolation in Fabric; workspace roles (Admin, Member, Contributor, Viewer) are coarse, so item permissions and OneLake security refine them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations) (primary): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.
- [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md) (Analytics and BI): Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md), [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Resource Manager](../google-cloud/gcp-resource-manager.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Polaris](../open-source/apache-polaris.md), [Apache Kyuubi](../open-source/apache-kyuubi.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
