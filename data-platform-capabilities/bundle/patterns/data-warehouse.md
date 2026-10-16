---
type: Pattern
id: data-warehouse
title: Data warehouse
description: A central store of integrated, historical data, modelled for analysis and reporting.
aliases: [EDW, enterprise data warehouse, DWH, Inmon]
uses:
- sql-query-engine
- sql-transformation
- data-modelling
- columnar-storage
- batch-ingestion
- workload-isolation
- semantic-layer
- data-quality-rules
- managed-storage
related: [dimensional-modelling, data-vault, data-marts, lakehouse]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data from operational systems is extracted, cleaned and conformed to shared definitions, then stored with its history so analysts can compare periods and follow trends. Bill Inmon described it in the early 1990s as subject-oriented, integrated, time-variant and non-volatile: organised around business subjects such as customer or product, consistent across sources, keeping history, and not overwritten by day-to-day transactions. The schema is defined before data is loaded, so every consumer reads the same structure.

Warehouses suit recurring reporting where numbers must agree across departments and over time. Two schools shaped their design: Inmon's normalised enterprise warehouse feeding departmental marts, and Kimball's dimensional models built as conformed star schemas. Data Vault later added a history-first integration layer. Modern cloud warehouses separate storage from compute and increasingly read open table formats, which blurs the line with the lakehouse. The main difference from a data lake is that data is modelled and validated on the way in rather than when it is read.

# When to use

- Finance, management and regulatory reporting where figures must reconcile and be reproducible.
- Many sources describe the same business entities and need conforming into one consistent view.
- Most consumers use SQL and BI tools rather than raw files or ML frameworks.

# Watch out for

- Up-front modelling makes new sources slow to add, and a central team can become a bottleneck.
- Proprietary storage can tie data to one engine; check whether other tools can read it without an export.
- Semi-structured and unstructured data and ML workloads often fit poorly and end up in a separate lake, with copies between the two.
- Mixed workloads compete for the same compute unless reporting, loading and exploration are isolated.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [SQL query engine](../capabilities/compute/sql-query-engine.md): Run analytical SQL over large datasets with parallel, optimised execution.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
- [Columnar storage](../capabilities/storage/columnar-storage.md): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Workload isolation](../capabilities/compute/workload-isolation.md): Run different workloads on separate compute so one cannot slow or starve another.
- [Semantic layer](../capabilities/analytics-bi/semantic-layer.md): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Data quality rules](../capabilities/data-quality/data-quality-rules.md): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Platform-managed storage](../capabilities/storage/managed-storage.md): Let the platform manage table storage layout, compression and durability internally.

# Related patterns

- [Dimensional modelling](dimensional-modelling.md)
- [Data Vault](data-vault.md)
- [Data marts](data-marts.md)
- [Lakehouse](lakehouse.md)
- [Data lake](data-lake.md)
- [ETL](etl.md)

# Where it appears

- **Use cases:** [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) · [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) · [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md)
