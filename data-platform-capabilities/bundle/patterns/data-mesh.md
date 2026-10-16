---
type: Pattern
id: data-mesh
title: Data mesh
description: Decentralise data ownership to business domains that publish data products on a shared self-service platform under federated governance.
uses:
- data-domains
- data-ownership
- data-product-specification
- data-contracts
- data-slas
- data-product-lifecycle
- self-service-provisioning
- multi-tenancy
- data-catalogue
- data-policy-management
- internal-data-sharing
related: [data-fabric, shift-left, data-marts]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of a central team ingesting and modelling everything, each business domain, such as payments or logistics, owns the analytical data it knows best and publishes it as data products: datasets with an owner, documentation, quality targets and a stable interface. A platform team provides self-service tooling so domains do not each build their own infrastructure. Governance is federated: domain and platform representatives agree a small set of global standards, such as identifiers, classification and interoperability rules, and the platform enforces them automatically. Zhamak Dehghani described the approach at Thoughtworks in 2019 and set out its four principles in 2020: domain ownership, data as a product, a self-serve platform and federated computational governance.

Data mesh is an operating model, not a technology. It tackles the bottleneck of a central team that cannot understand every domain's data or keep up with demand. It suits large organisations with many capable domain teams; smaller ones rarely have the people to staff it. It is often compared with data fabric, but a fabric centralises integration through metadata and automation, while a mesh decentralises ownership.

# When to use

- A central data team is a bottleneck and lacks the domain knowledge to model every area well.
- Several business domains have engineering capacity and are willing to own their data.
- Data is consumed across domains and needs clear owners, contracts and service levels.

# Watch out for

- Without a strong self-service platform, each domain rebuilds pipelines and tooling, raising cost and divergence.
- Federated governance fails if global standards are not automated; written policies alone are ignored.
- Relabelling existing tables as data products without owners, contracts or service levels changes nothing.
- Entities that cross domains, such as customer, still need master data and shared identifiers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data domains](../capabilities/governance/data-domains.md): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Ownership and stewardship](../capabilities/governance/data-ownership.md): Assign accountable owners and stewards to data and record their responsibilities.
- [Data product specification](../capabilities/data-products/data-product-specification.md): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Data contracts](../capabilities/data-products/data-contracts.md): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data service levels](../capabilities/data-products/data-slas.md): Set and track service levels for data products, such as freshness, availability and quality.
- [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md): Version, publish, deprecate and retire data products with notice to their consumers.
- [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md): Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.
- [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Data catalogue](../capabilities/metadata/data-catalogue.md): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Policy management](../capabilities/governance/data-policy-management.md): Define data policies centrally and apply them consistently across platforms and tools.
- [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md): Share live data between teams, accounts and workspaces without copying it.

# Related patterns

- [Data fabric](data-fabric.md)
- [Shift-left data quality and governance](shift-left.md)
- [Data marts](data-marts.md)

# Where it appears

- **Use cases:** [Application data publishing](../use-cases/usecase-application-data-publishing.md) · [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md) · [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md)
- **Personas:** [Chief data officer](../personas/persona-cdo.md) · [Data architect](../personas/persona-data-architect.md) · [Data product owner](../personas/persona-data-product-owner.md) · [Data steward](../personas/persona-data-steward.md) · [Data platform engineer](../personas/persona-platform-engineer.md)
