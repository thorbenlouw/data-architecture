---
type: Maturity Track
id: track-metadata-catalogue
title: Metadata and catalogue
description: How completely and accurately data assets are described, findable and connected through metadata, for people and for machines.
covers:
- data-catalogue
- metadata-harvesting
- business-glossary
- usage-metadata
- ai-generated-documentation
- active-metadata
- schema-registry
- metadata-interoperability
- table-catalogue
- catalogue-federation
- ai-context-layer
related_tracks: [track-lineage, track-governance, track-analytics-bi, track-genai]
levels:
- level: 1
  name: Initial
  summary: Knowledge of what data exists lives in people's heads, spreadsheets and wiki pages.
  criteria:
  - Finding a dataset means asking colleagues or searching code.
  - Descriptions and owners, where recorded, are in spreadsheets or wiki pages that are rarely updated.
  - Each engine or tool keeps its own list of tables, and the lists disagree.
  capabilities: []
- level: 2
  name: Managed
  summary: A catalogue harvests technical metadata from the main platforms, and some teams describe their assets.
  criteria:
  - A catalogue harvests schemas, tables and columns from the main warehouse or lake on a schedule.
  - Engines share one table catalogue that records each table's schema and storage location.
  - Some datasets have owners and descriptions entered by their teams, and coverage is uneven.
  - Schemas for the main event topics are stored in a schema registry.
  capabilities: [data-catalogue, metadata-harvesting, table-catalogue, schema-registry]
- level: 3
  name: Defined
  summary: Cataloguing is a platform standard with required fields, a business glossary and usage information.
  criteria:
  - A deployment check stops a production dataset being published without an owner, description and domain in the catalogue.
  - A business glossary defines key terms with named approvers, and terms are linked to the tables and columns that hold them.
  - The catalogue shows query counts and main users for each dataset, taken from platform logs.
  - AI drafts descriptions and tags for undocumented assets, and owners approve or edit them before they are published.
  capabilities: [business-glossary, usage-metadata, ai-generated-documentation]
- level: 4
  name: Measured
  summary: Metadata coverage is measured, metadata flows between tools, and it triggers automated actions.
  criteria:
  - Harvest failures raise alerts, and catalogue entries older than their asset's last schema change are flagged as stale.
  - Tags such as personal data propagate automatically to derived tables, and owners are alerted when an upstream schema changes.
  - Metadata moves between ingestion, transformation, BI and catalogue tools through open APIs or standards, without re-keying.
  - Catalogue search returns assets from every connected catalogue and applies each user's permissions, so people see only what they may open.
  - Search success, such as the share of searches that end with an asset being opened, is measured.
  capabilities: [active-metadata, metadata-interoperability, catalogue-federation]
- level: 5
  name: Optimising
  summary: Metadata is curated from usage evidence and served as context to AI agents with measured accuracy.
  criteria:
  - AI agents receive curated definitions, metrics, verified queries and usage guidance from a context layer, and their answer accuracy is measured against reference questions.
  - Documentation gaps are prioritised by usage, so the most queried undocumented assets are described first.
  - Datasets with no use for a defined period are flagged to owners for deprecation automatically.
  - Corrections that users suggest in the catalogue are reviewed and applied within a stated time.
  capabilities: [ai-context-layer]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means anyone can find a dataset and see what it means, who owns it, whether it is trusted and how it is used, and the same metadata drives automation such as tag propagation, owner alerts and context for AI agents. The usual blockers are catalogues filled once by a project and then left to decay, descriptions that depend on volunteers, and several tools each holding partial metadata with no exchange between them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Knowledge of what data exists lives in people's heads, spreadsheets and wiki pages.

- Finding a dataset means asking colleagues or searching code.
- Descriptions and owners, where recorded, are in spreadsheets or wiki pages that are rarely updated.
- Each engine or tool keeps its own list of tables, and the lists disagree.

## Level 2: Managed

A catalogue harvests technical metadata from the main platforms, and some teams describe their assets.

- A catalogue harvests schemas, tables and columns from the main warehouse or lake on a schedule.
- Engines share one table catalogue that records each table's schema and storage location.
- Some datasets have owners and descriptions entered by their teams, and coverage is uneven.
- Schemas for the main event topics are stored in a schema registry.

**Capabilities first relied on:** [Data catalogue](../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Schema registry](../capabilities/metadata/schema-registry.md)

## Level 3: Defined

Cataloguing is a platform standard with required fields, a business glossary and usage information.

- A deployment check stops a production dataset being published without an owner, description and domain in the catalogue.
- A business glossary defines key terms with named approvers, and terms are linked to the tables and columns that hold them.
- The catalogue shows query counts and main users for each dataset, taken from platform logs.
- AI drafts descriptions and tags for undocumented assets, and owners approve or edit them before they are published.

**Capabilities first relied on:** [Business glossary](../capabilities/metadata/business-glossary.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md)

## Level 4: Measured

Metadata coverage is measured, metadata flows between tools, and it triggers automated actions.

- Harvest failures raise alerts, and catalogue entries older than their asset's last schema change are flagged as stale.
- Tags such as personal data propagate automatically to derived tables, and owners are alerted when an upstream schema changes.
- Metadata moves between ingestion, transformation, BI and catalogue tools through open APIs or standards, without re-keying.
- Catalogue search returns assets from every connected catalogue and applies each user's permissions, so people see only what they may open.
- Search success, such as the share of searches that end with an asset being opened, is measured.

**Capabilities first relied on:** [Active metadata](../capabilities/metadata/active-metadata.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md)

## Level 5: Optimising

Metadata is curated from usage evidence and served as context to AI agents with measured accuracy.

- AI agents receive curated definitions, metrics, verified queries and usage guidance from a context layer, and their answer accuracy is measured against reference questions.
- Documentation gaps are prioritised by usage, so the most queried undocumented assets are described first.
- Datasets with no use for a defined period are flagged to owners for deprecation automatically.
- Corrections that users suggest in the catalogue are reviewed and applied within a stated time.

**Capabilities first relied on:** [AI context layer](../capabilities/metadata/ai-context-layer.md)

# Capabilities in scope

[Active metadata](../capabilities/metadata/active-metadata.md), [AI context layer](../capabilities/metadata/ai-context-layer.md), [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Schema registry](../capabilities/metadata/schema-registry.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md)

# Related tracks

- [Lineage](track-lineage.md): How completely and automatically the organisation can show where data came from, how it was changed and what depends on it.
- [Governance operating model](track-governance.md): How clearly the rules, roles and controls for managing data are defined, implemented on the platform and evidenced.
- [Analytics and BI](track-analytics-bi.md): How consistently people across the organisation explore, report on and act on data using shared definitions and governed tools.
- [Generative AI](track-genai.md): How safely and reliably the organisation builds, evaluates and runs applications that use language models and agents with its own data.

Levels follow the shared [maturity scale](maturity-scale.md).
