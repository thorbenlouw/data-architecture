---
type: Pattern
id: data-vault
title: Data Vault
description: Model integrated history with hubs, links and satellites so new sources can be added without rework.
aliases: [Data Vault 2.0, raw vault, business vault, 'hubs, links and satellites']
uses:
- data-modelling
- sql-transformation
- transformation-as-code
- incremental-processing
- idempotent-loading
- temporal-data
- master-data-management
- data-lineage
related: [dimensional-modelling, data-warehouse, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The model splits data into three kinds of table. Hubs hold the unique business keys of core entities, such as a customer number. Links record relationships between hubs, such as a customer placing an order. Satellites hold descriptive attributes and their change history, each attached to a hub or link and usually one per source system. Tables are insert-only and carry load timestamps and record sources, so the model keeps a full, auditable history of what each source said. Dan Linstedt developed the method in the 1990s and published it around 2000; Data Vault 2.0 later added hash keys, loading patterns and a delivery methodology.

Because a new source usually means new satellites or links rather than changes to existing tables, the model grows without rework and loads can run in parallel. It suits integrating many sources under audit requirements, for example in banking and insurance. It is not designed for direct querying: most teams publish dimensional marts or wide tables on top, and use code generation to manage the large number of tables.

# When to use

- Many source systems feed the same entities and new sources are added often.
- Auditors or regulators need the full history of what each source supplied and when it was loaded.
- You want to separate integration, in the vault, from presentation, in marts built on top.

# Watch out for

- The number of tables and joins is large; without automation and code generation the model is slow to build and maintain.
- Raw vault tables are hard for analysts to query, so a presentation layer is still needed.
- Poorly chosen business keys undermine the whole model, so key analysis must come before building hubs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Transformation as code](../capabilities/processing/transformation-as-code.md): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
- [Bitemporal data](../capabilities/specialised-data/temporal-data.md): Store and query data as it was true in the real world and as it was recorded in the system.
- [Master data management](../capabilities/master-data/master-data-management.md): Create a single trusted record for entities such as customer, product or supplier from many sources.
- [Data lineage](../capabilities/metadata/data-lineage.md): Track where data comes from, how it is transformed and where it goes.

# Related patterns

- [Dimensional modelling](dimensional-modelling.md)
- [Data warehouse](data-warehouse.md)
- [Medallion architecture](medallion-architecture.md)
- [Slowly changing dimensions](slowly-changing-dimensions.md)

# Where it appears

- **Use cases:** [Customer 360](../use-cases/usecase-customer-360.md) · [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md)
