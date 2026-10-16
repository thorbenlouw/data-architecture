---
type: Pattern
id: etl
title: ETL
description: Extract data, transform it in a separate engine, then load the result into the target.
aliases: [extract transform load]
uses:
- batch-ingestion
- database-extraction
- low-code-transformation
- distributed-processing
- data-cleansing
- deidentification
- data-reconciliation
- workflow-orchestration
related: [elt, data-warehouse]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The transformation happens in transit. A dedicated integration server or a processing cluster reads from the sources, applies type conversions, lookups, deduplication, joins and business rules, and writes only the cleaned, conformed result to the warehouse or application. The approach has been used since the 1970s and dominated data warehousing while warehouse compute was scarce and expensive, because transforming before loading kept the target small and fast. Much ETL is built with graphical tools that generate the underlying jobs.

ETL remains the right choice when raw data must not reach the target, for example when personal data has to be masked or removed first, when the target cannot transform data at scale, or when data moves between operational systems rather than into an analytical store. Its weakness is that raw data is not kept where analysts work, so a new question can mean a new extract. ELT reverses the last two steps; the differences are where the compute runs and whether raw data stays in the platform.

# When to use

- Sensitive or unneeded data must be filtered, masked or tokenised before it reaches the target.
- The target has limited compute, or is an operational system rather than an analytical platform.
- Transformations need specialised processing that the target engine cannot run.

# Watch out for

- Logic held in a separate tool's jobs is hard to version, test and trace through lineage unless that tool supports it.
- The transformation engine is another system to size, secure, patch and monitor.
- Fixing a logic error usually means re-extracting from sources, which may no longer hold the history.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Database extraction](../capabilities/ingestion-integration/database-extraction.md): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Low-code transformation](../capabilities/processing/low-code-transformation.md): Build transformation logic visually from configurable components rather than writing code.
- [Distributed processing](../capabilities/processing/distributed-processing.md): Process large datasets in parallel across a cluster of machines.
- [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md): Correct and standardise data values such as addresses, names, dates and codes.
- [De-identification](../capabilities/governance/deidentification.md): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Data reconciliation](../capabilities/data-quality/data-reconciliation.md): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

# Related patterns

- [ELT](elt.md)
- [Data warehouse](data-warehouse.md)
- [Metadata-driven pipelines](metadata-driven-pipelines.md)
