---
type: Capability
id: data-ownership
title: Ownership and stewardship
description: Assign accountable owners and stewards to data and record their responsibilities.
aliases: [stewardship, data stewardship, data custodians, data accountability, RACI]
broader: [governance]
related: [data-domains, access-requests, data-issue-management, data-catalogue, data-product-specification]
depends_on: [data-catalogue]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each dataset, data product or domain gets a named owner who is accountable for it, and usually one or more stewards who do the day-to-day work. The owner decides who may use the data, approves changes to its meaning and accepts the risk if it is wrong. Stewards maintain definitions, triage quality issues and answer questions. For example, the head of credit risk owns the `loan_exposure` tables, while a steward in the risk data team keeps their documentation current and approves access requests. The assignment is recorded in the catalogue against the asset, ideally as a group or role rather than one person.

Without a recorded owner, access requests, quality incidents and change requests have nowhere to go, and nobody can decide whether a dataset can be retired. Many organisations separate the business owner, who answers for meaning and use, from the technical custodian, who runs the pipelines and storage. Data domains group assets; ownership names the people who answer for them.

# Key considerations

- Assign ownership to roles or groups and keep it in step with the HR or identity system, so it survives reorganisations and people leaving.
- Ownership without time and authority is nominal. Agree what stewards are expected to do and how much of their week it takes.
- Inherit ownership from domain or schema level by default and override it for individual assets, rather than assigning thousands of tables by hand.
- Flag orphaned assets automatically when an owner leaves or a group is emptied, and route them to the domain lead.

# Questions to ask

- Who approves access to, and changes in, the most sensitive datasets today?
- Are owners expected to be business people, technical teams or both?
- What happens to an asset's ownership when its owner changes role or leaves?
- How many assets currently have no named owner?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Access requests and reviews](../security/access-requests.md), [Data catalogue](../metadata/data-catalogue.md), [Data domains](data-domains.md), [Data issue management](../data-quality/data-issue-management.md), [Data product specification](../data-products/data-product-specification.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Merge and survivorship](../master-data/survivorship.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md) |
| Needed by | [Data quality and observability](../data-quality/data-quality.md), [Master and reference data](../master-data/master-data.md), [Data products](../data-products/data-products.md), [Access requests and reviews](../security/access-requests.md), [Business glossary](../metadata/business-glossary.md), [Data certification](../metadata/data-certification.md), [Data issue management](../data-quality/data-issue-management.md), [Master data management](../master-data/master-data-management.md), [Stewardship workflows](stewardship-workflows.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 2) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 2)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md) · [Shift-left data quality and governance](../../patterns/shift-left.md)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data steward](../../personas/persona-data-steward.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 1 – Governance; Principle 2 – Data architecture and IT infrastructure · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 2 Ownership Field (Governance and accountability) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Governance · [Data mesh principles](../../frameworks/framework-data-mesh.md): Domain-oriented decentralised data ownership and architecture · [DCAM v3](../../frameworks/framework-edm-dcam.md): 2 Data Management Program & Funding; 6 Govern Data & DMP · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-150 – Roles and responsibilities · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.3 – Internal organisation · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 2 – Accountability structures · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Support & Communication Channels; Team · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Support and Communication Channels; Team

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric domains](../../technologies/microsoft/fabric-domains.md), [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md), [OneLake catalog](../../technologies/microsoft/fabric-onelake-catalog.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data products](../../technologies/google-cloud/gcp-knowledge-catalog-data-products.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Data Product Standard (ODPS)](../../technologies/open-source/open-data-product-standard.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [Solidatus](../../technologies/independent/solidatus.md) |
