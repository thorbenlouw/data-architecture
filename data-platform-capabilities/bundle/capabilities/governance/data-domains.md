---
type: Capability
id: data-domains
title: Data domains
description: Group data assets, products and owners into business domains with their own stewardship and policies.
broader: [governance]
related: [data-ownership, data-products, multi-tenancy, master-data-management, cost-attribution]
depends_on: [data-catalogue]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data domain is a business area, such as customer, finance, supply chain or HR, that groups related data assets, data products, owners and stewards. Each asset belongs to one domain, and the domain sets local standards, approves access, agrees definitions in the glossary and is measured on its own governance metrics. On the platform, domains appear as catalogue structures, workspaces or schemas, and policies can be scoped to them, for example "access to finance-domain tables needs steward approval".

Domains let governance scale by delegating decisions to the people who know the data, while a central team sets common rules. They are the organising unit of data mesh, where each domain publishes data products for others, but they also suit centralised platforms that need clear accountability. The hard choices are where boundaries fall and how to handle shared entities such as customer, which many domains use but one should own. Ownership names the people and groups who are accountable; a domain is the area they are accountable for.

# Key considerations

- Align domains with business capabilities that change slowly, not with current team or system boundaries, which change often.
- Decide which domain owns each shared entity, such as customer and product, and how other domains consume it.
- Make domains visible in platform structure, such as catalogues, workspaces and cost tags, so policy, cost and metrics can use them.
- Write down what is decided centrally and what each domain decides, or federated governance becomes inconsistent.

# Questions to ask

- How is accountability for data divided today: by business area, system or team?
- Which entities are used across many domains, and who should own them?
- Which decisions should domains make for themselves, and which must stay central?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Master and reference data](../master-data/master-data.md), [Data products](../data-products/data-products.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Data catalogue](../metadata/data-catalogue.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Master data management](../master-data/master-data-management.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Ownership and stewardship](data-ownership.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data architect](../../personas/persona-data-architect.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Governance; Data Architecture · [Data mesh principles](../../frameworks/framework-data-mesh.md): Domain-oriented decentralised data ownership and architecture · [DCAM v3](../../frameworks/framework-edm-dcam.md): 1 Data Strategy, DMS & Business Case; 3 Architecture – Business, Data & Technology; 6 Govern Data & DMP · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Fundamentals · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Fundamentals

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric domains](../../technologies/microsoft/fabric-domains.md), [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Discover](../../technologies/databricks/databricks-discover.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md), [OpenMetadata](../../technologies/open-source/openmetadata.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Atlan](../../technologies/independent/atlan.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md) |
