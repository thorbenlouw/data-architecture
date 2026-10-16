---
type: Pattern
id: metadata-driven-pipelines
title: Metadata-driven pipelines
description: Run one generic ingestion or transformation pipeline driven by control tables that list hundreds of sources and how to load each.
aliases:
- metadata-driven ingestion
- metadata-driven ETL
- configuration-driven pipelines
- control-table pipelines
- parameterised pipelines
- generic ingestion framework
uses:
- workflow-orchestration
- database-extraction
- file-ingestion
- incremental-processing
- idempotent-loading
- schema-evolution
- data-quality-rules
- pipeline-monitoring
- table-lineage
- ci-cd
related: [elt, etl, medallion-architecture, data-fabric]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of one pipeline per source, the team builds one parameterised pipeline and a set of control tables that describe each source: connection, object name, full or incremental load, watermark column, target table, keys, schedule and quality checks. An orchestrator reads the active rows, runs the same steps for each, often in parallel, and writes the new watermark and run status back to the control tables. Onboarding the 301st table becomes a reviewed configuration change rather than new pipeline code.

The pattern suits estates with hundreds of similar sources, such as tables from many instances of one ERP system or files from many partners. Logging, error handling and quality checks live in one place, so a fix applies everywhere. Its weakness is the exception: sources that do not fit the template collect flags and special cases until the generic pipeline is harder to follow than separate ones. The control tables become critical metadata and need version control, testing and access control of their own.

# When to use

- Many sources share the same load shape, such as tables on the same database engines or files with known layouts.
- New sources arrive often and should be onboarded by adding configuration rather than writing code.
- Consistent logging, naming, quality checks and error handling across every load matter more than tuning each one.

# Watch out for

- Special cases piling into the generic code. Give sources that do not fit the template their own pipelines.
- Control tables edited by hand in production. Keep them in version control and deploy them through CI like code.
- One faulty change breaking every source at once. Test changes to the framework against a representative set of sources before release.
- Lineage and monitoring that see only one generic job. Emit run status and lineage for each source and target.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Database extraction](../capabilities/ingestion-integration/database-extraction.md): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [File ingestion](../capabilities/ingestion-integration/file-ingestion.md): Detect and load files arriving in landing storage, processing each file exactly once.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [Deduplication and idempotent loading](../capabilities/ingestion-integration/idempotent-loading.md): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.
- [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md): Reject data that does not match a table's schema, and change schemas safely over time.
- [Data quality rules](../capabilities/data-quality/data-quality-rules.md): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md): Track pipeline runs, failures and durations, and alert the right people.
- [Table-level lineage](../capabilities/metadata/table-lineage.md): Track dependencies between datasets, tables and views.
- [CI/CD](../capabilities/development-lifecycle/ci-cd.md): Build, test and deploy pipelines, models and infrastructure automatically on every change.

# Related patterns

- [ELT](elt.md)
- [ETL](etl.md)
- [Medallion architecture](medallion-architecture.md)
- [Data fabric](data-fabric.md)
