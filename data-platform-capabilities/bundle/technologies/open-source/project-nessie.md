---
type: Technology
id: project-nessie
title: Project Nessie
description: Transactional catalogue for Iceberg that adds Git-like branches, tags and commits across many tables at once.
aliases: [Nessie]
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-branching, table-catalogue, acid-transactions]
resource: https://projectnessie.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, led by Dremio, which SAP agreed to buy in May 2026 and which now describes itself as part of SAP. Supports the Iceberg REST API. Many of its maintainers also work on [Apache Polaris](../open-source/apache-polaris.md), so check the project's direction before choosing it for a new build.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data branching and tagging](../../capabilities/storage/data-branching.md) (Storage and table management) (primary): Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Global Branching](../palantir/palantir-global-branching.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md) |
