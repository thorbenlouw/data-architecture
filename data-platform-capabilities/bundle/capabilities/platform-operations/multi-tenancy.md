---
type: Capability
id: multi-tenancy
title: Multi-tenancy and workspace isolation
description: Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
broader: [platform-operations]
related:
- workload-isolation
- data-domains
- internal-data-sharing
- cost-attribution
- self-service-provisioning
depends_on: [access-control, identity-authentication]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

One platform is divided among many teams, domains or customers. Each tenant usually gets its own workspace or project, its own catalogue or schemas, compute, administrators and budget, and identities that see only what has been granted, while the underlying accounts, storage, catalogue service and contracts are shared. For example, the finance and marketing domains each have a workspace with their own clusters and cost tags, and both read certified customer data from a shared catalogue through explicit grants.

This lets a central team run one platform rather than many, while giving domains the independence that data mesh and federated operating models expect. The key choice is the isolation boundary. Separate cloud accounts or subscriptions give the strongest separation of blast radius, quotas and billing. Workspaces in one account are easier to share between. Schemas in one workspace are cheapest but rely entirely on permissions. Workload isolation deals with compute contention; multi-tenancy covers the wider separation of administration, data, cost and access.

# Key considerations

- Choose the tenant boundary deliberately. Moving data and permissions between accounts or workspaces later is slow and risky.
- Platform limits often apply per account or workspace, such as the number of workspaces, concurrent jobs or API calls. Check them against the number of tenants you expect.
- Plan how tenants share data with each other. Too much isolation leads to copies; too little makes isolation meaningless.
- Decide what tenant administrators may change and what stays central, such as network rules, encryption keys and audit settings.

# Questions to ask

- How many teams or domains need their own space, and do any need strict separation for legal or regulatory reasons?
- Must costs be reported and charged per tenant?
- Will external customers or partners be tenants, or only internal teams?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Related | [Security and access](../security/security.md), [Cost attribution and chargeback](cost-attribution.md), [Customer-hosted data plane](hybrid-data-plane.md), [Data domains](../governance/data-domains.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Row-level security](../security/row-level-security.md), [Self-service provisioning](self-service-provisioning.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [Access control](../security/access-control.md), [Identity and authentication](../security/identity-authentication.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Domain-oriented decentralised data ownership and architecture; Self-serve data platform

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker Unified Studio domains and projects | [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Workspaces and domains | [Fabric workspaces](../../technologies/microsoft/fabric-workspaces.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | resource hierarchy (organisation, folders, projects) | [Google Cloud Resource Manager](../../technologies/google-cloud/gcp-resource-manager.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | organisations and accounts | [Snowflake organisations](../../technologies/snowflake/snowflake-organizations.md) |
| [Informatica](../../platforms/platform-informatica.md) | sub-organisations | [IDMC Administrator](../../technologies/informatica/informatica-administrator.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Environments | [Cloudera on cloud](../../technologies/cloudera/cloudera-on-cloud.md) |
| [SAP](../../platforms/platform-sap.md) | Spaces | [SAP Datasphere](../../technologies/sap/sap-datasphere.md) |
| [IBM](../../platforms/platform-ibm.md) | Projects and spaces (Software Hub) | [IBM Software Hub (Cloud Pak for Data)](../../technologies/ibm/ibm-software-hub.md) |
| [Palantir](../../platforms/platform-palantir.md) | Organizations and Spaces | [Palantir Foundry](../../technologies/palantir/palantir-foundry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Kyuubi](../../technologies/open-source/apache-kyuubi.md), [Apache Polaris](../../technologies/open-source/apache-polaris.md) |
