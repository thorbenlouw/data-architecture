---
type: Pattern
id: dimensional-modelling
title: Dimensional modelling
description: Model data as fact tables of measurements surrounded by dimension tables of context.
aliases: [Kimball, star schema, snowflake schema, fact and dimension tables, dimensional model]
uses:
- data-modelling
- sql-transformation
- transformation-as-code
- columnar-storage
- semantic-layer
- metric-definitions
- master-data-management
- hierarchy-management
related: [slowly-changing-dimensions, data-marts, data-warehouse, one-big-table]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each business process, such as sales, shipments or claims, gets a fact table of numeric measurements at a declared grain, for example one row per order line. Around it sit dimension tables describing who, what, where and when: customer, product, store, date. Drawn out, the layout looks like a star, hence the name star schema; normalising the dimensions further gives a snowflake schema. Ralph Kimball set out the method in The Data Warehouse Toolkit in 1996, with conformed dimensions shared across fact tables so that measures from different processes can be compared.

Dimensional models are easy for business users and BI tools to understand, and columnar engines answer star joins quickly. They remain the most common shape for a presentation or gold layer, and semantic layers usually sit on top of them. They are built for analysis rather than for integrating many changing sources, which is why they often sit on a normalised or Data Vault layer. A one big table design trades the separate dimensions for a single wide table.

# When to use

- Users query through BI tools and need understandable tables with consistent measures.
- Several business processes must be analysed against shared dimensions such as customer, product and date.
- You need a presentation layer whose structure changes less often than its sources.

# Watch out for

- Getting the grain wrong, or mixing grains in one fact table, leads to double counting.
- Conformed dimensions need agreement across departments; without it each mart builds its own version of customer or product.
- History in dimensions must be designed deliberately, usually with slowly changing dimension techniques.
- Many-to-many relationships and uneven hierarchies need bridge tables, which users find hard to query correctly.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Transformation as code](../capabilities/processing/transformation-as-code.md): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Columnar storage](../capabilities/storage/columnar-storage.md): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Semantic layer](../capabilities/analytics-bi/semantic-layer.md): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md): Define, certify and version key business metrics with owners and calculation logic.
- [Master data management](../capabilities/master-data/master-data-management.md): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Hierarchy management](../capabilities/master-data/hierarchy-management.md): Maintain hierarchies and relationships such as corporate structures, product taxonomies and organisation charts.

# Related patterns

- [Slowly changing dimensions](slowly-changing-dimensions.md)
- [Data marts](data-marts.md)
- [Data warehouse](data-warehouse.md)
- [One big table](one-big-table.md)
- [Data Vault](data-vault.md)

# Where it appears

- **Use cases:** [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md) · [Demand forecasting](../use-cases/usecase-demand-forecasting.md) · [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) · [Self-service BI](../use-cases/usecase-self-service-bi.md)
- **Personas:** [Analytics engineer](../personas/persona-analytics-engineer.md) · [Data analyst](../personas/persona-data-analyst.md) · [Data architect](../personas/persona-data-architect.md)
