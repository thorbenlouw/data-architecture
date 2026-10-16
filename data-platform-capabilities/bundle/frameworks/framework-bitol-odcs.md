---
type: Framework
id: framework-bitol-odcs
title: Open Data Contract Standard (ODCS)
description: An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
aliases: [ODCS, Bitol ODCS, ODCS v3]
kind: standard
publisher: Bitol (Linux Foundation AI & Data)
resource: https://bitol-io.github.io/open-data-contract-standard/latest/
related: [framework-bitol-odps, framework-data-mesh]
applies_to:
- usecase-application-data-publishing
- usecase-data-monetisation
- shift-left
- data-mesh
- persona-data-product-owner
- persona-data-engineer
- persona-software-engineer
mappings:
- ref: Fundamentals
  summary: Identifies the contract, its version, status, domain and purpose.
  capabilities: [data-contracts, data-product-lifecycle, data-domains]
- ref: Schema
  summary: Describes datasets and their properties, including types, keys and classification.
  capabilities: [data-contracts, schema-evolution, data-modelling, data-classification]
- ref: Context
  summary: Gives AI agents and other consumers guidance on how to use the data and what they must not do.
  capabilities: [ai-context-layer, agent-tool-access, semantic-layer]
- ref: References
  summary: Defines relationships such as foreign keys within a contract and to elements in other contracts.
  capabilities: [data-modelling, data-contracts]
- ref: Data Quality
  summary: States quality rules and metrics, with schedules for running them.
  capabilities: [data-quality-rules, data-contracts, data-observability]
- ref: Support & Communication Channels
  summary: Lists where consumers get help and hear about changes.
  capabilities: [data-ownership, data-product-lifecycle]
- ref: Pricing
  summary: States the price of using the data, for internal chargeback or commercial sale.
  capabilities: [data-product-metering, cost-attribution, data-marketplace, external-data-sharing]
- ref: Team
  summary: Names the people responsible for the data and their roles.
  capabilities: [data-ownership]
- ref: Roles
  summary: Lists the access roles consumers can request, the access each grants and who approves it.
  capabilities: [access-requests, role-based-access, stewardship-workflows]
- ref: Service-Level Agreement
  summary: Sets measurable commitments such as availability, latency, frequency, retention and time to detect, notify and repair.
  capabilities: [data-slas, freshness-monitoring, data-retention, data-issue-management]
- ref: Infrastructures & Servers
  summary: Describes the platforms, topics and endpoints where the data can be reached.
  capabilities: [sql-access, table-catalogue, engine-interoperability, event-api-catalogue]
- ref: Custom & Other Properties
  summary: Lets organisations and tools add their own fields without breaking the standard.
  capabilities: [metadata-interoperability]
- ref: Authoritative Definitions
  summary: Links elements to the definitive sources of their meaning, such as glossary terms or policies.
  capabilities: [business-glossary, data-certification]
- ref: Tags
  summary: Labels the contract and its elements for search and classification.
  capabilities: [data-classification, data-catalogue]
- ref: Variables
  summary: Lets one contract be used across development, test and production without storing secrets in it.
  capabilities: [environment-promotion, secrets-management]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ODCS is an open, Apache-licensed specification maintained by the Bitol project under the Linux Foundation AI & Data, used by data contract tools and platforms to describe what a producer promises to consumers. The latest release is v3.2.0 (September 2026, released together with ODPS v1.1.0); v3.1.0 split the specification into smaller documents and added relationships, and v3.2.0 added AI context, synonyms, variables for multiple environments and more server types. A contract is a YAML document with fifteen top-level sections, so it maps cleanly onto contract enforcement, quality, service level, access and catalogue capabilities. ODPS data products refer to ODCS contracts from their ports.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Fundamentals | Identifies the contract, its version, status, domain and purpose. | [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data domains](../capabilities/governance/data-domains.md) |
| Schema | Describes datasets and their properties, including types, keys and classification. | [Data contracts](../capabilities/data-products/data-contracts.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data classification](../capabilities/governance/data-classification.md) |
| Context | Gives AI agents and other consumers guidance on how to use the data and what they must not do. | [AI context layer](../capabilities/metadata/ai-context-layer.md), [Agent tool and data access](../capabilities/generative-ai/agent-tool-access.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) |
| References | Defines relationships such as foreign keys within a contract and to elements in other contracts. | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data contracts](../capabilities/data-products/data-contracts.md) |
| Data Quality | States quality rules and metrics, with schedules for running them. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data observability](../capabilities/data-quality/data-observability.md) |
| Support & Communication Channels | Lists where consumers get help and hear about changes. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| Pricing | States the price of using the data, for internal chargeback or commercial sale. | [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md) |
| Team | Names the people responsible for the data and their roles. | [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| Roles | Lists the access roles consumers can request, the access each grants and who approves it. | [Access requests and reviews](../capabilities/security/access-requests.md), [Role-based access control](../capabilities/security/role-based-access.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md) |
| Service-Level Agreement | Sets measurable commitments such as availability, latency, frequency, retention and time to detect, notify and repair. | [Data service levels](../capabilities/data-products/data-slas.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Data issue management](../capabilities/data-quality/data-issue-management.md) |
| Infrastructures & Servers | Describes the platforms, topics and endpoints where the data can be reached. | [SQL and programmatic access](../capabilities/serving/sql-access.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Event and API catalogue](../capabilities/metadata/event-api-catalogue.md) |
| Custom & Other Properties | Lets organisations and tools add their own fields without breaking the standard. | [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md) |
| Authoritative Definitions | Links elements to the definitive sources of their meaning, such as glossary terms or policies. | [Business glossary](../capabilities/metadata/business-glossary.md), [Data certification](../capabilities/metadata/data-certification.md) |
| Tags | Labels the contract and its elements for search and classification. | [Data classification](../capabilities/governance/data-classification.md), [Data catalogue](../capabilities/metadata/data-catalogue.md) |
| Variables | Lets one contract be used across development, test and production without storing secrets in it. | [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Secrets management](../capabilities/security/secrets-management.md) |

# Related frameworks

- [Open Data Product Standard (ODPS)](framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.
- [Data mesh principles](framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [EU Data Act](framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.

# Applies to

- [Application data publishing](../use-cases/usecase-application-data-publishing.md) (use case): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md) (use case): Share or sell data products to partners and customers under agreed terms.
- [Shift-left data quality and governance](../patterns/shift-left.md) (pattern): Move quality checks, contracts and governance controls upstream to where data is produced.
- [Data mesh](../patterns/data-mesh.md) (pattern): Decentralise data ownership to business domains that publish data products on a shared self-service platform under federated governance.
- [Data product owner](../personas/persona-data-product-owner.md) (persona): Owns the value, roadmap and consumers of one or more data products.
- [Data engineer](../personas/persona-data-engineer.md) (persona): Builds and operates the pipelines that ingest, transform and deliver data.
- [Software engineer](../personas/persona-software-engineer.md) (persona): Builds applications that produce data for the platform or consume data from it.
