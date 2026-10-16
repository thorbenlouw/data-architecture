---
type: Pattern
id: elt
title: ELT
description: Extract and load raw data into the platform first, then transform it there.
aliases: [extract load transform]
uses:
- saas-connectors
- change-data-capture
- database-replication
- sql-transformation
- transformation-as-code
- incremental-processing
- data-testing
- column-masking
- workflow-orchestration
related: [etl, medallion-architecture, lakehouse]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed connectors or change data capture copy source tables into the platform largely unchanged, and transformations then run inside the platform, usually as SQL that builds cleaned and modelled tables from the raw ones. Because raw tables stay available, engineers can change or add models later without returning to the source. The approach became common in the 2010s once cloud warehouses offered elastic compute and cheap storage, and tools that treat SQL transformations as version-controlled, tested code made it manageable at scale.

ELT shortens the time from a new source to first use, and keeps transformation logic in one place where lineage and testing tools can see it. It moves cost into platform compute, so inefficient models show up directly on the bill. It also means raw and possibly sensitive data lands in the platform before anything is masked, so access control has to cover raw tables from the start. Most lakehouse and medallion designs are ELT; ETL remains for cases where data must be reshaped before it lands.

# When to use

- The target platform has elastic compute and can transform large volumes at acceptable cost.
- Requirements change often, so keeping raw data for later remodelling is valuable.
- Teams work in SQL and want transformations under version control with tests and lineage.

# Watch out for

- Sensitive raw data lands before any masking, so access controls and classification must apply to raw tables.
- Growing numbers of models and full refreshes raise compute cost; use incremental models and attribute cost to owners.
- Landing data is so easy that unused raw tables pile up; set ownership and retention for everything loaded.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [SaaS application connectors](../capabilities/ingestion-integration/saas-connectors.md): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Change data capture](../capabilities/ingestion-integration/change-data-capture.md): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database replication and mirroring](../capabilities/ingestion-integration/database-replication.md): Replicate operational databases continuously into the analytical platform without building pipelines.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Transformation as code](../capabilities/processing/transformation-as-code.md): Define transformations as version-controlled, tested, modular code whose dependencies are resolved automatically.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md): Test transformation logic and data with unit, integration and regression tests before release.
- [Column security and dynamic masking](../capabilities/security/column-masking.md): Hide or mask sensitive columns depending on who is querying.
- [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

# Related patterns

- [ETL](etl.md)
- [Medallion architecture](medallion-architecture.md)
- [Lakehouse](lakehouse.md)
- [Data lake](data-lake.md)
- [Metadata-driven pipelines](metadata-driven-pipelines.md)

# Where it appears

- **Use cases:** [Marketing audience activation](../use-cases/usecase-marketing-activation.md) · [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md)
- **Personas:** [Analytics engineer](../personas/persona-analytics-engineer.md) · [Data engineer](../personas/persona-data-engineer.md)
