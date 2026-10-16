---
type: Maturity Track
id: track-master-data
title: Master and reference data
description: How consistently core business entities and shared code lists are identified, matched and maintained across systems.
covers:
- master-data
- master-data-management
- entity-resolution
- survivorship
- hierarchy-management
- reference-data-management
- product-information-management
related_tracks: [track-data-quality, track-analytics-bi]
levels:
- level: 1
  name: Initial
  summary: Each system keeps its own version of core entities and code lists.
  criteria:
  - Customer and product records are joined across systems by name or by fuzzy matching written separately in each report.
  - Code lists such as country or product category are copied into spreadsheets and pipelines and drift apart.
  - Duplicates are cleaned up in one-off projects that are not repeated.
  capabilities: []
- level: 2
  name: Managed
  summary: One domain has a matching process and shared identifier, and code lists have a single maintained source.
  criteria:
  - One domain, usually customer or product, links records from its main sources to a shared identifier through a matching process.
  - Shared code lists are held in one maintained table with an owner, and pipelines read from it.
  - Rules for which source wins for key attributes are written down for that domain.
  capabilities: [master-data-management, entity-resolution, reference-data-management]
- level: 3
  name: Defined
  summary: Golden records, hierarchies and reference data follow documented rules, stewardship and versioning.
  criteria:
  - Golden records are built by documented match and survivorship rules, and each attribute records the source it came from.
  - Stewards work uncertain matches from a queue with agreed turnaround times.
  - Reference data changes go through versioned approval, and consumers can retrieve any past version.
  - Corporate, product and organisation hierarchies are versioned with effective dates.
  - Master records and identifiers are published to consuming systems through one standard table or interface.
  capabilities: [survivorship, hierarchy-management]
- level: 4
  name: Measured
  summary: Match quality, duplicate rates and propagation times are measured against targets.
  criteria:
  - Duplicate rate, match precision on a reviewed sample and steward queue age are measured against targets.
  - Consuming systems are checked automatically for unknown or retired identifiers.
  - Product attributes and content have completeness scores per sales channel, and incomplete products are blocked from publication.
  - Changes to golden records reach subscribing systems within a measured time.
  capabilities: [product-information-management]
- level: 5
  name: Optimising
  summary: Matching improves from steward decisions, and errors are prevented at the point of entry.
  criteria:
  - Matching rules or models are retuned from steward decisions, and the share of matches needing review falls.
  - Operational applications validate new entries against master data when they are captured.
  - New domains are added to master data management based on the measured cost of duplicates and reconciliation effort.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means a customer, product or supplier has one identifier and one trusted set of attributes that every system and report uses, and code lists such as countries or product categories change in one place under version control. The implementation style (registry, consolidation, coexistence or centralised authoring) is a design choice, not a level. Typical blockers are disagreement over which system owns which attribute, matching rules that nobody can explain, and stewards without the time or tools to resolve conflicts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Each system keeps its own version of core entities and code lists.

- Customer and product records are joined across systems by name or by fuzzy matching written separately in each report.
- Code lists such as country or product category are copied into spreadsheets and pipelines and drift apart.
- Duplicates are cleaned up in one-off projects that are not repeated.

## Level 2: Managed

One domain has a matching process and shared identifier, and code lists have a single maintained source.

- One domain, usually customer or product, links records from its main sources to a shared identifier through a matching process.
- Shared code lists are held in one maintained table with an owner, and pipelines read from it.
- Rules for which source wins for key attributes are written down for that domain.

**Capabilities first relied on:** [Master data management](../capabilities/master-data/master-data-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Reference data management](../capabilities/master-data/reference-data-management.md)

## Level 3: Defined

Golden records, hierarchies and reference data follow documented rules, stewardship and versioning.

- Golden records are built by documented match and survivorship rules, and each attribute records the source it came from.
- Stewards work uncertain matches from a queue with agreed turnaround times.
- Reference data changes go through versioned approval, and consumers can retrieve any past version.
- Corporate, product and organisation hierarchies are versioned with effective dates.
- Master records and identifiers are published to consuming systems through one standard table or interface.

**Capabilities first relied on:** [Merge and survivorship](../capabilities/master-data/survivorship.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md)

## Level 4: Measured

Match quality, duplicate rates and propagation times are measured against targets.

- Duplicate rate, match precision on a reviewed sample and steward queue age are measured against targets.
- Consuming systems are checked automatically for unknown or retired identifiers.
- Product attributes and content have completeness scores per sales channel, and incomplete products are blocked from publication.
- Changes to golden records reach subscribing systems within a measured time.

**Capabilities first relied on:** [Product information management](../capabilities/master-data/product-information-management.md)

## Level 5: Optimising

Matching improves from steward decisions, and errors are prevented at the point of entry.

- Matching rules or models are retuned from steward decisions, and the share of matches needing review falls.
- Operational applications validate new entries against master data when they are captured.
- New domains are added to master data management based on the measured cost of duplicates and reconciliation effort.

# Capabilities in scope

[Master and reference data](../capabilities/master-data/master-data.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Master data management](../capabilities/master-data/master-data-management.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Product information management](../capabilities/master-data/product-information-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md)

# Related tracks

- [Data quality and observability](track-data-quality.md): How systematically the organisation defines, measures, monitors and fixes the fitness of data for its intended uses.
- [Analytics and BI](track-analytics-bi.md): How consistently people across the organisation explore, report on and act on data using shared definitions and governed tools.

Levels follow the shared [maturity scale](maturity-scale.md).
