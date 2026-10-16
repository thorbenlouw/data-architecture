---
type: Persona
id: persona-data-architect
title: Data architect
description: Designs the data platform and how data flows, is modelled and is governed across the organisation.
cares_about:
- data-modelling
- open-table-formats
- table-catalogue
- engine-interoperability
- data-lineage
- impact-analysis
- data-contracts
- semantic-layer
- metadata-interoperability
- master-data-management
- data-domains
- data-classification
- access-control
- decoupled-storage-compute
- change-data-capture
- event-streaming
- query-federation
- data-product-specification
- catalogue-federation
- schema-evolution
- data-residency
- deployment-options
- platform-migration
patterns: [lakehouse, medallion-architecture, data-mesh, dimensional-modelling, cqrs-read-models]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data architects usually sit in an enterprise architecture function or a central data team, and work across delivery teams, security, governance and procurement. Their output is target-state designs, reference patterns, standards, decision records and reviews of other teams' designs, rather than running code. They translate a business use case into the capabilities, data models and products needed to deliver it.

Success is a platform on which new use cases need little bespoke work: shared patterns for ingestion, modelling, serving and AI, consistent identifiers and definitions across domains, and technology choices that still make sense in three years. Failure looks like duplicated pipelines, several platforms doing the same job and integration problems found late.

# Goals

- Define a target architecture and reference patterns that delivery teams actually follow.
- Keep data models, identifiers and business definitions consistent across domains.
- Choose capabilities and products that fit the requirements and avoid lock-in that has no payback.
- Design security, privacy and governance in from the start rather than adding them after go-live.
- Reduce duplicated pipelines, copies of data and overlapping platforms.

# Jobs

- Turn a new use case into a list of required capabilities, target maturity levels and a solution design.
- Run architecture reviews and record decisions with their trade-offs.
- Assess vendors and products against capability requirements and existing standards.
- Maintain conceptual and logical models of core entities and their mapping to physical tables.
- Set standards for table formats, catalogues, naming, layering and data contracts.
- Assess current maturity against the target and plan the roadmap that closes the gap.

# Pain points

- Teams choose tools independently and the estate fragments into overlapping platforms.
- Vendor marketing blurs what products actually do, so like-for-like comparison is slow.
- Models and documentation drift away from what is deployed.
- Latency, freshness, retention and recovery requirements surface late in delivery.
- Lineage and metadata are too patchy to show what a proposed change will break.

# Questions they ask

- Which capabilities does this use case need, at what maturity, and which can we reuse from existing work?
- Should this data be modelled once centrally, or owned and published by the domain that produces it?
- Do our table format and catalogue choices let several engines share one copy of the data?
- What latency, freshness and retention do consumers really need, and what does each step up cost?
- Where are the single points of failure and the hardest-to-reverse dependencies in the current design?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Design and document conceptual, logical and physical data models, and keep them in step with what is deployed. |
| [Open table formats](../capabilities/storage/open-table-formats.md) | [Storage and table management](../capabilities/storage/storage.md) | Manage collections of files as transactional tables with a defined schema, history and metadata. |
| [Table catalogue](../capabilities/storage/table-catalogue.md) | [Storage and table management](../capabilities/storage/storage.md) | Register tables, their schemas and storage locations so engines can find, govern and share them. |
| [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md) | [Query and compute](../capabilities/compute/compute.md) | Let several engines read and write the same tables through open formats and shared catalogues. |
| [Data lineage](../capabilities/metadata/data-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track where data comes from, how it is transformed and where it goes. |
| [Impact analysis](../capabilities/metadata/impact-analysis.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Use lineage to find everything affected by a proposed change or a data incident. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define business entities, measures and relationships once so every tool calculates them the same way. |
| [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Exchange metadata between tools through open APIs and standards. |
| [Master data management](../capabilities/master-data/master-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | Create a single trusted record for entities such as customer, product or supplier from many sources. |
| [Data domains](../capabilities/governance/data-domains.md) | [Governance and compliance](../capabilities/governance/governance.md) | Group data assets, products and owners into business domains with their own stewardship and policies. |
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically. |
| [Access control](../capabilities/security/access-control.md) | [Security and access](../capabilities/security/security.md) | Decide who can see and change which data, at every level from account down to individual values. |
| [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Scale storage and compute independently and let several compute clusters work on the same data. |
| [Change data capture](../capabilities/ingestion-integration/change-data-capture.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency. |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | Publish and subscribe to durable, ordered and replayable streams of events between systems. |
| [Query federation](../capabilities/compute/query-federation.md) | [Query and compute](../capabilities/compute/compute.md) | Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first. |
| [Data product specification](../capabilities/data-products/data-product-specification.md) | [Data products](../capabilities/data-products/data-products.md) | Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form. |
| [Catalogue federation](../capabilities/storage/catalogue-federation.md) | [Storage and table management](../capabilities/storage/storage.md) | Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand. |
| [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md) | [Storage and table management](../capabilities/storage/storage.md) | Reject data that does not match a table's schema, and change schemas safely over time. |
| [Data residency and sovereignty](../capabilities/governance/data-residency.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep data and its processing in approved jurisdictions and prove that you have. |
| [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Run the platform across clouds, regions or on-premises, or inside your own cloud account. |
| [Platform migration](../capabilities/platform-operations/platform-migration.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation. |

# Patterns

- [Lakehouse](../patterns/lakehouse.md)
- [Medallion architecture](../patterns/medallion-architecture.md)
- [Data mesh](../patterns/data-mesh.md)
- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [Separate read models](../patterns/cqrs-read-models.md)

# Use cases they take part in

- [Application data publishing](../use-cases/usecase-application-data-publishing.md): Application teams publish their data to the platform through versioned events and change capture under agreed contracts, so downstream consumers do not break when applications change.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DAMA-DMBOK 2](../frameworks/framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [Data mesh principles](../frameworks/framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [Open Data Product Standard (ODPS)](../frameworks/framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.
