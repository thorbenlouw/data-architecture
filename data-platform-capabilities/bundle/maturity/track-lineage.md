---
type: Maturity Track
id: track-lineage
title: Lineage
description: How completely and automatically the organisation can show where data came from, how it was changed and what depends on it.
covers:
- data-lineage
- table-lineage
- column-lineage
- cross-system-lineage
- unstructured-lineage
- model-lineage
- impact-analysis
related_tracks: [track-metadata-catalogue, track-governance, track-data-quality]
levels:
- level: 1
  name: Initial
  summary: Lineage is reconstructed by hand when someone needs it.
  criteria:
  - Lineage, where it exists, is drawn by hand in diagrams that go out of date.
  - Questions about what feeds a report are answered by reading code or asking the original developer.
  - Changes to source tables break reports that nobody knew depended on them.
  capabilities: []
- level: 2
  name: Managed
  summary: Table-level lineage is captured automatically inside the main platform.
  criteria:
  - The main warehouse or transformation tool records which tables each job reads and writes, and the graph can be browsed.
  - Engineers check the lineage view for downstream tables before changing a model.
  - Lineage covers scheduled jobs but not notebooks, ad hoc scripts or BI tools.
  capabilities: [table-lineage]
- level: 3
  name: Defined
  summary: Lineage is collected across tools in a common format, at column level for critical data.
  criteria:
  - Ingestion, transformation, orchestration and BI tools emit lineage events in a common format such as OpenLineage into one store.
  - Column-level lineage exists for critical data elements and regulatory reports, including logic inside views and MERGE statements.
  - Change reviews for schema changes include an impact list of affected tables, dashboards and owners taken from lineage.
  - Lineage from source system to report can be shown for every authoritative source and key report.
  capabilities: [cross-system-lineage, column-lineage, impact-analysis]
- level: 4
  name: Measured
  summary: Lineage coverage is measured, and lineage is used automatically in releases, incidents and models.
  criteria:
  - The share of production jobs and reports with captured lineage is measured against a target.
  - CI flags pipeline changes that would break downstream consumers, using the lineage graph.
  - Model lineage sits in the same graph as data lineage, so a defective source table lists the models trained on it.
  - During data incidents, owners of affected downstream assets are notified automatically from lineage.
  capabilities: [model-lineage]
- level: 5
  name: Optimising
  summary: Lineage reaches unstructured content and AI answers, and gaps are closed systematically.
  criteria:
  - AI answers and indexes trace back to the documents and chunks that produced them, and removing a source document removes it from dependent indexes.
  - Lineage gaps found in incidents or audits are logged and closed, and their number is falling.
  - Lineage is captured for notebooks and ad hoc scripts as well as scheduled jobs, and the share of production tables with no recorded upstream is kept below a set threshold, such as 1 per cent.
  capabilities: [unstructured-lineage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means impact analysis before a change takes minutes rather than days of asking around, incidents are traced to their source quickly, and auditors can be shown how a reported figure was derived. CDMC key control 13 expects lineage for sensitive data from source to consumption, and banks commonly rely on lineage to meet the accuracy and integrity principle of BCBS 239; that corresponds roughly to level 3 here, with level 4 adding measured coverage and automated use. The usual blockers are tools that do not emit lineage, dynamic SQL and stored procedures that parsers cannot follow, and lineage that stops at the warehouse boundary.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Lineage is reconstructed by hand when someone needs it.

- Lineage, where it exists, is drawn by hand in diagrams that go out of date.
- Questions about what feeds a report are answered by reading code or asking the original developer.
- Changes to source tables break reports that nobody knew depended on them.

## Level 2: Managed

Table-level lineage is captured automatically inside the main platform.

- The main warehouse or transformation tool records which tables each job reads and writes, and the graph can be browsed.
- Engineers check the lineage view for downstream tables before changing a model.
- Lineage covers scheduled jobs but not notebooks, ad hoc scripts or BI tools.

**Capabilities first relied on:** [Table-level lineage](../capabilities/metadata/table-lineage.md)

## Level 3: Defined

Lineage is collected across tools in a common format, at column level for critical data.

- Ingestion, transformation, orchestration and BI tools emit lineage events in a common format such as OpenLineage into one store.
- Column-level lineage exists for critical data elements and regulatory reports, including logic inside views and MERGE statements.
- Change reviews for schema changes include an impact list of affected tables, dashboards and owners taken from lineage.
- Lineage from source system to report can be shown for every authoritative source and key report.

**Capabilities first relied on:** [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md)

## Level 4: Measured

Lineage coverage is measured, and lineage is used automatically in releases, incidents and models.

- The share of production jobs and reports with captured lineage is measured against a target.
- CI flags pipeline changes that would break downstream consumers, using the lineage graph.
- Model lineage sits in the same graph as data lineage, so a defective source table lists the models trained on it.
- During data incidents, owners of affected downstream assets are notified automatically from lineage.

**Capabilities first relied on:** [Model lineage](../capabilities/metadata/model-lineage.md)

## Level 5: Optimising

Lineage reaches unstructured content and AI answers, and gaps are closed systematically.

- AI answers and indexes trace back to the documents and chunks that produced them, and removing a source document removes it from dependent indexes.
- Lineage gaps found in incidents or audits are logged and closed, and their number is falling.
- Lineage is captured for notebooks and ad hoc scripts as well as scheduled jobs, and the share of production tables with no recorded upstream is kept below a set threshold, such as 1 per cent.

**Capabilities first relied on:** [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md)

# Capabilities in scope

[Column-level lineage](../capabilities/metadata/column-lineage.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md)

# Related tracks

- [Metadata and catalogue](track-metadata-catalogue.md): How completely and accurately data assets are described, findable and connected through metadata, for people and for machines.
- [Governance operating model](track-governance.md): How clearly the rules, roles and controls for managing data are defined, implemented on the platform and evidenced.
- [Data quality and observability](track-data-quality.md): How systematically the organisation defines, measures, monitors and fixes the fitness of data for its intended uses.

Levels follow the shared [maturity scale](maturity-scale.md).
