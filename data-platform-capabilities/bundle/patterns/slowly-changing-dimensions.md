---
type: Pattern
id: slowly-changing-dimensions
title: Slowly changing dimensions
description: Track changes to descriptive attributes over time, for example by overwriting values or versioning rows.
aliases: [SCD, SCD type 2, SCD2, SCD type 1]
uses:
- data-modelling
- change-data-capture
- row-level-updates
- incremental-processing
- sql-transformation
- transformation-as-code
- temporal-data
- time-travel
related: [dimensional-modelling, data-vault]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a customer moves region or a product changes category, the dimension must decide what history to keep. Ralph Kimball named and numbered the techniques. Type 1 overwrites the old value, so reports always show the current state. Type 2 closes the current row and inserts a new version with valid-from and valid-to dates and a current-row flag, so each fact joins to the attributes that were true when it happened. Type 3 keeps the previous value in an extra column. Higher-numbered types add to or combine these, for example holding type 2 history with the current value alongside.

The choice is made per attribute and is a business decision: should last year's sales appear under the customer's old region or the new one? Type 2 is the most common for audit and point-in-time analysis, and is usually built with MERGE statements or snapshot tools that compare incoming records with current ones. It differs from bitemporal modelling, which also records when the system learnt about a change, not only when the change was true.

# When to use

- Reports must show facts against the attribute values that applied at the time.
- Analysts or auditors need to see how a customer, product or account changed over time.
- Some attributes need history and others do not, and you want to decide per attribute.

# Watch out for

- Type 2 tables grow quickly if volatile attributes are tracked; move fast-changing attributes to a separate dimension.
- Late-arriving or corrected source records can break valid-date ranges unless loads handle them explicitly.
- Fact loads must look up the surrogate key that was current at the event time, or history is lost.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.
- [Change data capture](../capabilities/ingestion-integration/change-data-capture.md): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Row-level updates and deletes](../capabilities/storage/row-level-updates.md): Update, delete and merge individual rows in large tables efficiently.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Transformation as code](../capabilities/processing/transformation-as-code.md): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Bitemporal data](../capabilities/specialised-data/temporal-data.md): Store and query data as it was true in the real world and as it was recorded in the system.
- [Time travel](../capabilities/storage/time-travel.md): Query or restore a table as it was at an earlier point in time or version.

# Related patterns

- [Dimensional modelling](dimensional-modelling.md)
- [Data Vault](data-vault.md)

# Where it appears

- **Use cases:** [Customer 360](../use-cases/usecase-customer-360.md) · [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) · [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md)
- **Personas:** [Analytics engineer](../personas/persona-analytics-engineer.md)
