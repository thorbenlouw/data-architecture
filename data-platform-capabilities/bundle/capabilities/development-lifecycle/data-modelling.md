---
type: Capability
id: data-modelling
title: Data modelling and design
description: Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
aliases: [data modeling, ER modelling, data model design]
broader: [development-lifecycle]
related:
- business-glossary
- semantic-layer
- schema-change-management
- master-data-management
- partitioning-clustering
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Modelling decides which entities a domain contains, how they relate and how they are stored. A conceptual model names business entities and relationships, such as "customer places order". A logical model adds attributes, keys and rules without committing to a technology. A physical model sets tables, types, partitioning and clustering for a specific engine. Modelling tools let you draw and version these models, generate DDL from them and reverse-engineer models from existing databases, so the documented design can be compared with the deployed tables.

Good models make data consistent across teams and easier to query, and settle questions of meaning once in a recorded design. Common analytical approaches are dimensional models (facts and dimensions), Data Vault (hubs, links and satellites for auditable integration of many sources) and wide denormalised tables for specific uses. Modelling overlaps with the semantic layer, which defines business measures over physical tables, and with the business glossary, which defines terms. The physical model is what both of those sit on.

# Key considerations

- Pick one main modelling approach per layer and document it. Mixing dimensional, Data Vault and ad hoc designs in one layer confuses consumers.
- Keep models in version control and generate or check DDL against them, or diagrams go out of date within months.
- Design physical models for the engine you use. Partitioning, clustering and denormalisation choices that suit one engine can hurt another.
- Link entities and attributes to glossary terms and classifications so meaning and sensitivity travel with the design.

# Questions to ask

- Do different teams define core entities such as customer or product differently?
- Is there a documented model of the current platform, and does it match what is deployed?
- Which modelling approach do your engineers and consumers already know?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [Processing and transformation](../processing/processing.md), [Master and reference data](../master-data/master-data.md), [Bitemporal data](../specialised-data/temporal-data.md), [Business glossary](../metadata/business-glossary.md), [Master data management](../master-data/master-data-management.md), [Partitioning and clustering](../storage/partitioning-clustering.md), [Read-optimised views](../serving/read-optimised-views.md), [Schema change management](schema-change-management.md), [Semantic layer](../analytics-bi/semantic-layer.md), [SQL transformation](../processing/sql-transformation.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Data Vault](../../patterns/data-vault.md) · [Data warehouse](../../patterns/data-warehouse.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Architecture; Data Modelling and Design · [DCAM v3](../../frameworks/framework-edm-dcam.md): 3 Architecture – Business, Data & Technology · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Schema; References

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere](../../technologies/sap/sap-datasphere.md) |
