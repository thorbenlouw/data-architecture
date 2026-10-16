---
type: Pattern
id: write-audit-publish
title: Write-audit-publish
description: Write new data to an isolated location, check it, and only then publish it to consumers.
aliases: [WAP, blue-green data deployment]
uses:
- data-branching
- zero-copy-cloning
- open-table-formats
- acid-transactions
- data-quality-rules
- data-reconciliation
- data-testing
- freshness-monitoring
- workflow-orchestration
related: [shift-left, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The isolated location can be a staging table, a branch of the table or an uncommitted snapshot. Automated checks run against it: row counts, uniqueness, null rates, reconciliation with the source and comparison with the previous version. Only if the checks pass is the data published, typically by an atomic swap, a branch merge or a snapshot commit, so consumers move from the old version to the new one in a single step. If checks fail, the data stays staged for investigation and consumers keep the last good version. Engineers at Netflix described the pattern publicly around 2017.

The pattern stops bad data reaching dashboards and models, rather than detecting it afterwards. Open table formats and data branching make it cheap, because staging and publishing are metadata operations rather than copies. It is the data equivalent of a blue-green release. It differs from bad-data quarantine: write-audit-publish holds back a whole batch, while quarantine diverts individual failing records and lets the rest through.

# When to use

- Consumers such as executive dashboards, regulatory reports or production models must never see a partial or incorrect batch.
- Tables are loaded or rebuilt in batches that should succeed or fail as a whole.
- The table format or platform supports branches, staged snapshots or atomic table swaps.

# Watch out for

- Audits add time and compute to every run; keep the checks to what matters for consumers.
- Withholding a batch leaves data stale, so freshness alerts and an agreed override process are needed.
- Checks are only as good as their rules; untested assumptions pass straight through.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Data branching and tagging](../capabilities/storage/data-branching.md): Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
- [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md): Create an instant copy of a table, schema or database that shares storage with the original until either changes.
- [Open table formats](../capabilities/storage/open-table-formats.md): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [ACID transactions](../capabilities/storage/acid-transactions.md): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Data quality rules](../capabilities/data-quality/data-quality-rules.md): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data reconciliation](../capabilities/data-quality/data-reconciliation.md): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md): Test transformation logic and data with unit, integration and regression tests before release.
- [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md): Detect when data arrives later than expected or misses its freshness target.
- [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

# Related patterns

- [Shift-left data quality and governance](shift-left.md)
- [Medallion architecture](medallion-architecture.md)

# Where it appears

- **Use cases:** [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md)
- **Personas:** [Data engineer](../personas/persona-data-engineer.md)
