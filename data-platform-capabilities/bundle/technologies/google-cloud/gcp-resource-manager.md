---
type: Technology
id: gcp-resource-manager
title: Google Cloud Resource Manager
description: Organises resources into an organisation, folders and projects, with tags and organisation policies inherited down the hierarchy.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [multi-tenancy, configuration-guardrails, data-residency]
resource: https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Projects are the unit of isolation, billing and quota for most data services, so domain-aligned project and folder design is the main tenancy decision. Organisation policy constraints restrict locations and services.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations) (primary): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) (Platform operations): Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.
- [Data residency and sovereignty](../../capabilities/governance/data-residency.md) (Governance and compliance): Keep data and its processing in approved jurisdictions and prove that you have.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspaces](../microsoft/fabric-workspaces.md), [Azure Policy](../microsoft/azure-policy.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake organisations](../snowflake/snowflake-organizations.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks compliance security profile](../databricks/databricks-compliance-security-profile.md) | [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Software Hub (Cloud Pak for Data)](../ibm/ibm-software-hub.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Kyuubi](../open-source/apache-kyuubi.md), [Apache Polaris](../open-source/apache-polaris.md) | [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
