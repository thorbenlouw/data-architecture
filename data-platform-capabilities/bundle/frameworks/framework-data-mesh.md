---
type: Framework
id: framework-data-mesh
title: Data mesh principles
description: Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
aliases: [data mesh, four principles of data mesh]
kind: principles
publisher: Zhamak Dehghani
resource: https://martinfowler.com/articles/data-mesh-principles.html
related: [framework-bitol-odps, framework-bitol-odcs]
applies_to:
- data-mesh
- usecase-domain-onboarding
- usecase-application-data-publishing
- persona-data-product-owner
- persona-platform-engineer
- persona-data-architect
mappings:
- ref: Domain-oriented decentralised data ownership and architecture
  summary: Business domains own, build and serve their analytical data and can release it independently.
  capabilities: [data-domains, data-ownership, multi-tenancy, internal-data-sharing]
- ref: Data as a product
  summary: Each domain publishes data as products that are discoverable, understandable, trustworthy and secure, with owners accountable for quality and consumer satisfaction.
  capabilities:
  - data-product-specification
  - data-contracts
  - data-slas
  - data-catalogue
  - data-product-lifecycle
  - data-trust-indicators
- ref: Self-serve data platform
  summary: A shared platform lets domain teams build and run data products without specialist infrastructure skills.
  capabilities: [self-service-provisioning, infrastructure-as-code, multi-tenancy]
- ref: Self-serve platform – infrastructure provisioning plane
  summary: Provides storage, compute, access control, orchestration and query engines on demand.
  capabilities: [self-service-provisioning, infrastructure-as-code, access-control, workflow-orchestration]
- ref: Self-serve platform – data product developer experience plane
  summary: Gives declarative tooling to build, test, deploy and version data products with standards applied automatically.
  capabilities: [declarative-pipelines, ci-cd, data-product-lifecycle, transformation-as-code]
- ref: Self-serve platform – mesh supervision plane
  summary: Provides mesh-wide discovery, lineage and querying across data products.
  capabilities: [data-catalogue, cross-system-lineage, query-federation, data-marketplace]
- ref: Federated computational governance
  summary: Domain and platform representatives agree global standards, such as shared identifiers and policies, and the platform enforces them automatically.
  capabilities:
  - data-policy-management
  - attribute-based-access
  - active-metadata
  - data-classification
  - data-contracts
  - master-data-management
  - governance-metrics
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Zhamak Dehghani described data mesh in articles on martinfowler.com (the principles article dates from December 2020) and in her 2022 O'Reilly book. It rests on four principles: domain ownership, data as a product, a self-serve data platform and federated computational governance. The platform principle is the one that most directly defines capabilities: it describes an infrastructure provisioning plane, a data product developer experience plane and a mesh supervision plane. Data mesh is an operating model rather than a product, and Bitol's ODPS and ODCS are commonly used to describe its products and contracts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Domain-oriented decentralised data ownership and architecture | Business domains own, build and serve their analytical data and can release it independently. | [Data domains](../capabilities/governance/data-domains.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) |
| Data as a product | Each domain publishes data as products that are discoverable, understandable, trustworthy and secure, with owners accountable for quality and consumer satisfaction. | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| Self-serve data platform | A shared platform lets domain teams build and run data products without specialist infrastructure skills. | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| Self-serve platform – infrastructure provisioning plane | Provides storage, compute, access control, orchestration and query engines on demand. | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Access control](../capabilities/security/access-control.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) |
| Self-serve platform – data product developer experience plane | Gives declarative tooling to build, test, deploy and version data products with standards applied automatically. | [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) |
| Self-serve platform – mesh supervision plane | Provides mesh-wide discovery, lineage and querying across data products. | [Data catalogue](../capabilities/metadata/data-catalogue.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Query federation](../capabilities/compute/query-federation.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md) |
| Federated computational governance | Domain and platform representatives agree global standards, such as shared identifiers and policies, and the platform enforces them automatically. | [Policy management](../capabilities/governance/data-policy-management.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Active metadata](../capabilities/metadata/active-metadata.md), [Data classification](../capabilities/governance/data-classification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Master data management](../capabilities/master-data/master-data-management.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) |

# Related frameworks

- [Open Data Product Standard (ODPS)](framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.
- [Open Data Contract Standard (ODCS)](framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.

# Applies to

- [Data mesh](../patterns/data-mesh.md) (pattern): Decentralise data ownership to business domains that publish data products on a shared self-service platform under federated governance.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md) (use case): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Application data publishing](../use-cases/usecase-application-data-publishing.md) (use case): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Data product owner](../personas/persona-data-product-owner.md) (persona): Owns the value, roadmap and consumers of one or more data products.
- [Data platform engineer](../personas/persona-platform-engineer.md) (persona): Builds and runs the shared data platform and its self-service tooling.
- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
