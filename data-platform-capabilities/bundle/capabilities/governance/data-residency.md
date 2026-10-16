---
type: Capability
id: data-residency
title: Data residency and sovereignty
description: Keep data and its processing in approved jurisdictions and prove that you have.
broader: [governance]
related:
- cross-region-sharing
- cross-region-failover
- deployment-options
- hybrid-data-plane
- customer-managed-keys
depends_on: [data-classification]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Residency rules say where data may be stored and processed, usually by country or region. Sovereignty goes further and asks which legal jurisdiction can compel access to the data, which depends on who operates the service as well as where the servers are. The platform supports both by pinning storage and compute to approved regions, blocking replication, sharing or queries that would move data elsewhere, and recording where each dataset lives. For example, a bank keeps customer data in EU regions and replicates only aggregated figures to a global reporting region.

Requirements come from privacy-law transfer rules, sector regulation, public-sector contracts and customer agreements. Residency is often broken quietly outside the main data store: in catalogue metadata, logs, backups, disaster recovery replicas, support access by staff in other countries and AI model endpoints in another region. Approaches range from single-region deployments, to region-aware policies on a global platform, to sovereign or customer-hosted deployments run by an operator under local jurisdiction.

# Key considerations

- Check where metadata, logs, telemetry, backups and model inference are processed, not only where tables are stored.
- Disaster recovery regions and cross-region sharing must stay within approved jurisdictions, which can limit failover options.
- Tag datasets with their residency constraints and enforce them in sharing, replication and export, so one misconfigured job cannot move data.
- Support access, managed services and AI features operated from other countries may count as a transfer. Review the operator's terms, not only region settings.

# Questions to ask

- Which datasets have residency or sovereignty requirements, and where do the requirements come from?
- Does the requirement cover only storage, or also processing, metadata, support access and backups?
- Do the AI and model services used by the platform run in approved regions?
- How would you prove to a regulator or customer where a dataset has been stored and processed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Cross-region and cross-cloud sharing](../data-sharing/cross-region-sharing.md), [Cross-region replication and failover](../platform-operations/cross-region-failover.md), [Customer-hosted data plane](../platform-operations/hybrid-data-plane.md), [Customer-managed keys](../security/customer-managed-keys.md), [Edge data processing](../processing/edge-data-processing.md), [Encryption](../security/encryption.md), [Foundation model access](../generative-ai/foundation-model-access.md), [Hybrid and multi-cloud deployment](../platform-operations/deployment-options.md), [Network security](../security/network-security.md), [Object storage](../storage/object-storage.md), [Query federation](../compute/query-federation.md), [Sustainability and carbon management](../platform-operations/sustainability-reporting.md) |
| Depends on | [Data classification](data-classification.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 14 – Home/host cooperation · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 4 Data Sovereignty and Cross-Border Movement (Governance and accountability) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VII – Unlawful international governmental access · [GDPR](../../frameworks/framework-gdpr.md): Articles 44 to 49 – Transfers to third countries

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Outposts](../../technologies/aws/aws-outposts.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Policy](../../technologies/microsoft/azure-policy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Assured Workloads](../../technologies/google-cloud/gcp-assured-workloads.md), [Google Cloud Resource Manager](../../technologies/google-cloud/gcp-resource-manager.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks compliance security profile](../../technologies/databricks/databricks-compliance-security-profile.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse BYOC (Bring Your Own Cloud)](../../technologies/clickhouse/clickhouse-byoc.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Intelligent Data Management Cloud (IDMC)](../../technologies/informatica/informatica-idmc.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Skyflow Data Privacy Vault](../../technologies/independent/skyflow-data-privacy-vault.md) |
