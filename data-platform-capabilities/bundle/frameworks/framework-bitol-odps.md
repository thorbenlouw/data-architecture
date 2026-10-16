---
type: Framework
id: framework-bitol-odps
title: Open Data Product Standard (ODPS)
description: An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.
aliases: [ODPS, Bitol ODPS]
kind: standard
publisher: Bitol (Linux Foundation AI & Data)
resource: https://bitol-io.github.io/open-data-product-standard/latest/
related: [framework-bitol-odcs, framework-data-mesh]
applies_to:
- data-mesh
- usecase-domain-onboarding
- usecase-data-monetisation
- persona-data-product-owner
- persona-data-architect
mappings:
- ref: Fundamentals
  summary: Identifies the product, its domain, tenant, type (such as source-aligned or consumer-aligned), version, status and purpose.
  capabilities: [data-product-specification, data-product-lifecycle, data-domains]
- ref: Product Information (input and output ports)
  summary: Lists the contracts the product consumes and the output ports it exposes, each tied to a contract version.
  capabilities: [data-product-specification, data-contracts, data-lineage]
- ref: Context
  summary: Tells AI agents and semantic tools which port answers which questions and what they must not do with the product.
  capabilities: [ai-context-layer, agent-tool-access, data-product-specification]
- ref: Management Ports
  summary: Exposes REST or topic endpoints for discovering, observing and controlling the product.
  capabilities: [data-catalogue, data-observability, active-metadata, data-trust-indicators]
- ref: Support and Communication Channels
  summary: Lists where consumers get help and announcements about the product.
  capabilities: [data-ownership, data-product-lifecycle]
- ref: Team
  summary: Names the people who own and run the product.
  capabilities: [data-ownership]
- ref: Custom & Other Properties
  summary: Lets organisations add their own fields.
  capabilities: [metadata-interoperability]
- ref: Authoritative Definitions
  summary: Links the product to definitive sources of meaning or policy.
  capabilities: [business-glossary, data-certification]
- ref: Synonyms
  summary: Records other business names for the product and its ports so they are easier to find.
  capabilities: [business-glossary, data-catalogue]
- ref: Deprecated
  summary: Marks products and ports that should not be used for new work.
  capabilities: [data-product-lifecycle]
- ref: Variables
  summary: Lets values be resolved at run time so one document works across environments.
  capabilities: [environment-promotion, secrets-management]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ODPS is Bitol's companion to ODCS: where a contract describes one dataset's promises, a data product document describes the product as a whole, including the contracts it consumes and the output ports it offers. Version 1.0.0 was released in September 2025 and v1.1.0 in September 2026, which added AI context, synonyms, deprecation flags and variables. Each port points to an ODCS contract by id and version, so the two standards together give a machine-readable description of a data mesh. Product status runs from proposed and draft through active to deprecated and retired, which supports lifecycle management.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Fundamentals | Identifies the product, its domain, tenant, type (such as source-aligned or consumer-aligned), version, status and purpose. | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data domains](../capabilities/governance/data-domains.md) |
| Product Information (input and output ports) | Lists the contracts the product consumes and the output ports it exposes, each tied to a contract version. | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data lineage](../capabilities/metadata/data-lineage.md) |
| Context | Tells AI agents and semantic tools which port answers which questions and what they must not do with the product. | [AI context layer](../capabilities/metadata/ai-context-layer.md), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md), [Data product specification](../capabilities/data-products/data-product-specification.md) |
| Management Ports | Exposes REST or topic endpoints for discovering, observing and controlling the product. | [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data observability](../capabilities/data-quality/data-observability.md), [Active metadata](../capabilities/metadata/active-metadata.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| Support and Communication Channels | Lists where consumers get help and announcements about the product. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| Team | Names the people who own and run the product. | [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| Custom & Other Properties | Lets organisations add their own fields. | [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md) |
| Authoritative Definitions | Links the product to definitive sources of meaning or policy. | [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md) |
| Synonyms | Records other business names for the product and its ports so they are easier to find. | [Business glossary](../capabilities/metadata/business-glossary.md), [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Deprecated | Marks products and ports that should not be used for new work. | [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| Variables | Lets values be resolved at run time so one document works across environments. | [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Secrets management](../capabilities/security/secrets-management.md) |

# Related frameworks

- [Open Data Contract Standard (ODCS)](framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
- [Data mesh principles](framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.

# Applies to

- [Data mesh](../patterns/data-mesh.md) (pattern): Decentralise data ownership to business domains that publish data products on a shared self-service platform under federated governance.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md) (use case): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md) (use case): Share or sell data products to partners and customers under agreed terms.
- [Data product owner](../personas/persona-data-product-owner.md) (persona): Owns the value, roadmap and consumers of one or more data products.
- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
