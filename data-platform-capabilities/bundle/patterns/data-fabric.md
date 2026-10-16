---
type: Pattern
id: data-fabric
title: Data fabric
description: Integrate distributed data through a metadata-driven layer that automates discovery, integration and governance across sources.
uses:
- metadata-harvesting
- active-metadata
- data-catalogue
- knowledge-graphs
- metadata-interoperability
- cross-system-lineage
- query-federation
- data-classification
- data-policy-management
- attribute-based-access
related: [data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A metadata layer spans databases, lakes, warehouses and applications and records what data exists, what it means, how it relates and who uses it. The fabric uses that metadata to automate work: suggesting joins and mappings, generating integration jobs, deciding whether to query data in place or copy it, and applying classification and access policies wherever the data lives. A knowledge graph often holds the relationships, and machine learning ranks the recommendations. Analyst firms, first Forrester and later Gartner, popularised the term; it names a design approach rather than a single product.

A fabric suits organisations whose data is spread across many platforms that cannot or will not be consolidated, and that want consistent discovery and governance across all of it. Its value depends on the coverage and accuracy of metadata, which is where most efforts stall. Compared with data mesh, a fabric is technology-led and usually run centrally. The two can coexist, with the fabric providing the discovery and policy layer that mesh domains publish into.

# When to use

- Data is spread across several clouds, on-premises systems and applications, and consolidation is not realistic.
- You need consistent discovery, classification and access policy across different kinds of store.
- Integration demand outstrips engineering capacity, and automation driven by metadata could absorb routine work.

# Watch out for

- Automation depends on complete, accurate metadata; partial harvesting gives poor recommendations and gaps in policy.
- Queries federated across many sources can be slow and can put load on operational systems.
- Vendors use the term loosely; agree which capabilities you mean before buying anything labelled as a fabric.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Active metadata](../capabilities/metadata/active-metadata.md): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.
- [Data catalogue](../capabilities/metadata/data-catalogue.md): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
- [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md): Exchange metadata between tools through open APIs and standards.
- [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Query federation](../capabilities/compute/query-federation.md): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Data classification](../capabilities/governance/data-classification.md): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Policy management](../capabilities/governance/data-policy-management.md): Define data policies centrally and apply them consistently across platforms and tools.
- [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md): Grant or deny access based on attributes of the user and tags on the data.

# Related patterns

- [Data mesh](data-mesh.md)
- [Metadata-driven pipelines](metadata-driven-pipelines.md)

# Where it appears

- **Use cases:** [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md)
- **Personas:** [Chief data officer](../personas/persona-cdo.md)
