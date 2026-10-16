---
type: Capability
id: access-requests
title: Access requests and reviews
description: Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
aliases:
- access governance
- entitlement reviews
- access recertification
- access reviews
- user access reviews
- access packages
broader: [access-control]
related: [data-ownership, data-catalogue, data-marketplace, usage-metadata, role-based-access]
depends_on: [data-ownership, role-based-access]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

People find a dataset in the catalogue or marketplace and request access, stating a purpose and duration. The request goes to the owner or steward, and approval adds the requester to the right group or role automatically, with an expiry date, recording who approved it and why. Periodic reviews then ask owners to confirm or revoke existing access. For example, an analyst requests 90 days of access to a claims dataset for a fraud study; the claims steward approves, and the grant lapses on schedule.

Without a workflow, access is granted by ticket and by hand, takes days, is rarely removed and leaves little evidence of who approved what. The delay pushes people to share extracts and credentials instead. A good workflow makes least privilege practical: quick approval for low-risk data, several approvers for sensitive data, time limits by default and a record for auditors. Access control enforces permissions; this capability manages how they are requested, approved and reviewed.

# Key considerations

- Grant access by adding users to groups or data-product subscriptions, not by direct object grants, so revocation is clean.
- Set expiry by default for sensitive data and make renewal easy, otherwise people ask for permanent access.
- Route approvals automatically to the owners and stewards recorded in the catalogue. Requests sent to a central queue wait.
- Show usage data in access reviews so reviewers can see which grants are actually used.
- Consider standing access for low-risk data, such as everyone in a domain, so the workflow is kept for decisions that matter.

# Questions to ask

- How long does it take to get access to a typical dataset today?
- Who approves access, and how is the approval recorded?
- When were existing grants last reviewed, and how many were removed?
- Should access to some classes of data expire automatically?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Data catalogue](../metadata/data-catalogue.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data marketplace](../data-sharing/data-marketplace.md), [Ownership and stewardship](../governance/data-ownership.md), [Privileged access management](privileged-access.md), [Role-based access control](role-based-access.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md), [Stewardship workflows](../governance/stewardship-workflows.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md), [Role-based access control](role-based-access.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data scientist](../../personas/persona-data-scientist.md) · [Data steward](../../personas/persona-data-steward.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 7 Entitlements and Access for Sensitive Data (Accessibility and usage); 8 Data Consumption Purpose (Accessibility and usage) · [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Roles

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker Catalog subscription requests | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Data product access policies (Purview) | [Data products in Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-data-products.md), [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | data product access groups and governance workflows | [Knowledge Catalog data products](../../technologies/google-cloud/gcp-knowledge-catalog-data-products.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Internal Marketplace (organisational listings)](../../technologies/snowflake/snowflake-internal-marketplace.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Marketplace (CDMP)](../../technologies/informatica/informatica-cloud-data-marketplace.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Data Product Hub](../../technologies/ibm/ibm-data-product-hub.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Access](../../technologies/independent/collibra-data-access.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [Immuta Data Authorization Platform](../../technologies/independent/immuta-data-authorization-platform.md), [Secoda](../../technologies/independent/secoda.md) |
