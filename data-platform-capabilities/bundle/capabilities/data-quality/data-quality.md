---
type: Capability
id: data-quality
title: Data quality and observability
description: Measure, monitor and improve whether data is fit for its intended use.
broader: []
related: [data-contracts, critical-data-elements, pipeline-monitoring, data-testing, master-data-management]
depends_on: [data-ownership]
order: 12
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data quality is judged against a use: the same customer table can be good enough for a marketing campaign and not good enough for a regulatory return. Quality is usually broken into dimensions such as completeness, validity, accuracy, consistency, uniqueness and timeliness, each measured by specific checks.

The capabilities form a loop. Profiling discovers what the data actually looks like. Rules state what it must look like and run as checks in pipelines. Observability watches production data for late arrivals, volume drops, schema changes and odd distributions, including failures nobody wrote a rule for. When checks fail, records can be quarantined, systems reconciled, values cleansed, and incidents tracked to resolution. Scorecards report results over time so owners can see trends. Unstructured data quality applies similar ideas to documents used for search and AI.

Checks are useless without someone who responds to them, so quality depends on ownership. It overlaps with data contracts, which publish quality promises, and with pipeline monitoring, which watches jobs rather than data.

# Key considerations

- Check data where errors enter. Checks at ingestion and at producer boundaries are cheaper than fixing reports later.
- Decide per check whether failure stops the pipeline, quarantines records or only warns. Stopping everything for minor issues teaches people to switch checks off.
- Combine explicit rules for known requirements with learned monitoring for unknown failures. Neither covers both.
- Prioritise by impact. Start with critical data elements and the products behind key decisions, not blanket coverage.
- Store check results as data, so they can feed scorecards, catalogues and incident tracking.

# Questions to ask

- Which decisions or reports have been wrong because of bad data, and what did it cost?
- Who is accountable for fixing data problems at the source?
- Which datasets carry regulatory or contractual quality obligations?
- How are data problems found today: by checks, or by consumers?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Bad-data quarantine](bad-data-quarantine.md), [Data cleansing and standardisation](data-cleansing.md), [Data issue management](data-issue-management.md), [Data observability](data-observability.md), [Data profiling](data-profiling.md), [Data quality rules](data-quality-rules.md), [Data quality scorecards](data-quality-scorecards.md), [Data reconciliation](data-reconciliation.md), [Unstructured data quality](unstructured-data-quality.md) |
| Related | [Metadata and discovery](../metadata/metadata.md), [Governance and compliance](../governance/governance.md), [Critical data elements](../governance/critical-data-elements.md), [Data contracts](../data-products/data-contracts.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Master data management](../master-data/master-data-management.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 52 technologies; see their pages.
