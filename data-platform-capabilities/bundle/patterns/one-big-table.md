---
type: Pattern
id: one-big-table
title: One big table
description: Denormalise data into wide tables to simplify and speed up analytical queries.
aliases: [OBT, wide tables]
uses:
- columnar-storage
- semi-structured-data
- sql-transformation
- incremental-processing
- read-optimised-views
- materialised-views
- partitioning-clustering
related: [dimensional-modelling, data-marts]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of joining facts to dimensions at query time, the joins are done once in the pipeline and stored as a single wide table, with customer, product and date attributes repeated on every row. Nested types such as arrays and structs can keep related detail, for example an order and its lines, in one row. The approach became practical with columnar storage: queries read only the columns they use, and compression keeps repeated values cheap to store. It has no single originator and spread with cloud warehouses and BI tools that work best on one table.

Wide tables are fast and simple to query. They suit analysts, feature extraction for data science and AI tools that generate SQL, because there are no joins to get wrong. The cost is in maintenance: when a descriptive attribute changes, many rows must be rewritten, and separately built tables may disagree on the same attribute. Many teams keep a dimensional model as the source of truth and generate wide tables from it for specific uses.

# When to use

- Query speed and simplicity matter more than storage, and users struggle with joins.
- One use case reads the same joined view repeatedly, such as a dashboard, a feature set or AI-generated SQL.
- The engine is columnar and handles wide tables and nested types well.

# Watch out for

- Changes to descriptive attributes mean rewriting many rows, which is slow and costly on large tables.
- Wide tables built independently drift apart on shared attributes such as customer segment.
- A wide table hides its grain; aggregating repeated or nested values can double count.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Columnar storage](../capabilities/storage/columnar-storage.md): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Semi-structured data](../capabilities/storage/semi-structured-data.md): Store and query nested data such as JSON without flattening it first.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [Read-optimised views](../capabilities/serving/read-optimised-views.md): Precompute tables in the shape consumers read them, such as pre-joined or pre-aggregated tables, and keep them current with pipelines so reads are fast and cheap.
- [Materialised views](../capabilities/compute/materialised-views.md): Have the query engine store a query's result, refresh it as sources change and optionally use it to answer other queries.
- [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md): Organise table data by key columns so queries can skip data they do not need.

# Related patterns

- [Dimensional modelling](dimensional-modelling.md)
- [Data marts](data-marts.md)

# Where it appears

- **Use cases:** [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md) · [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md) · [Self-service BI](../use-cases/usecase-self-service-bi.md)
- **Personas:** [Analytics engineer](../personas/persona-analytics-engineer.md) · [Data analyst](../personas/persona-data-analyst.md)
