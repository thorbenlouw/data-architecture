---
type: Capability
id: data-branching
title: Data branching and tagging
description: Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
aliases: [table branches, lakeFS, Nessie]
broader: [data-versioning]
related: [data-testing, ci-cd, data-quality-rules, environment-promotion, zero-copy-cloning]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data branching applies Git ideas to tables. A branch is a named, isolated line of change on a table or a whole catalogue, created from main at a point in time without copying data. A team can load and transform a day's data on a branch, run quality checks there, and merge it into main in one atomic step, or throw it away if the checks fail. Tags name specific versions, such as `month-end-2026-09`, and keep them beyond normal retention. Iceberg supports branches and tags per table; tools such as Project Nessie (at catalogue level) and lakeFS (at object storage level) branch many tables together.

Branching supports the write-audit-publish pattern, in which consumers never see data that has not passed checks, and gives each developer or CI run an isolated environment on real data. Unlike cloning, it tracks how branches relate and offers merges. Multi-table branches matter because related tables must change together; per-table branches cannot publish a consistent set of changes.

# Key considerations

- Merging data is not like merging code. When two branches changed the same rows, the fix is usually to rerun the transformation, not a line-by-line merge.
- Choose the scope. Per-table branches are simple; catalogue-level branches keep related tables consistent but need a catalogue that supports them.
- Engines and tools must understand branch references. Check support in the BI, transformation and orchestration tools that will use branches.
- Long-lived branches drift from main and hold extra storage. Keep branches short and remove abandoned ones.

# Questions to ask

- Must consumers be shielded from new data until it has passed quality checks?
- Do several tables need to be updated and published together as a consistent set?
- Would developers test transformations on production-scale data if it were safe and cheap?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Data versioning](data-versioning.md) |
| Related | [Backfill and reprocessing](../orchestration/backfill-replay.md), [CI/CD](../development-lifecycle/ci-cd.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data quality rules](../data-quality/data-quality-rules.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Ephemeral development environments](../development-lifecycle/ephemeral-environments.md), [Version control integration](../development-lifecycle/version-control.md), [Zero-copy cloning](zero-copy-cloning.md) |

# Where it appears

- **Patterns:** [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakebase](../../technologies/databricks/databricks-lakebase.md) |
| [Palantir](../../platforms/platform-palantir.md) | Global Branching | [Palantir Global Branching](../../technologies/palantir/palantir-global-branching.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [lakeFS](../../technologies/open-source/lakefs.md), [Project Nessie](../../technologies/open-source/project-nessie.md) |
