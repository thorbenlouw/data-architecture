---
type: Capability
id: critical-data-elements
title: Critical data elements
description: Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them.
aliases: [CDEs, key data elements, KDEs, critical data]
broader: [governance]
related: [column-lineage, data-quality-scorecards, business-glossary, data-reconciliation, impact-analysis]
depends_on: [column-lineage, data-quality-rules]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A critical data element (CDE) is a data item whose errors would materially affect regulatory reports, risk measures, financial statements or key decisions, such as exposure at default, counterparty identifier or booked revenue. Organisations name a limited set of CDEs, define each precisely, assign an owner, trace lineage from source to report and apply stricter controls: more quality rules, tighter thresholds, reconciliation at each hop and formal change approval. Each CDE is flagged in the catalogue so tools and people treat it differently.

This concentrates governance effort where errors cost most. It is common in banking, where supervisors assessing BCBS 239, the Basel Committee's principles for risk data aggregation and risk reporting, look for evidence that risk data is accurate, complete and timely, and CDEs are a usual way to scope that work. Similar ideas appear in insurance and financial reporting controls. CDEs connect several capabilities: the glossary defines them, lineage traces them, scorecards measure them and compliance evidence reports on them.

# Key considerations

- Keep the list short and justify each entry by its use in specific reports. A list that grows to thousands of elements loses its purpose.
- A CDE is defined by business meaning, but controls attach to its physical copies in many tables. Map each one to its physical columns through lineage.
- Lineage for CDEs must reach the report or model that uses them, including spreadsheets and manual adjustments where they exist.
- Require impact analysis and owner approval for changes to any pipeline that feeds a CDE.

# Questions to ask

- Which reports or regulatory submissions would be wrong if a single field were wrong?
- Is there an agreed list of CDEs, and is each one mapped to physical columns?
- Can you show lineage and quality results for each CDE from source to report?
- Who approves changes to the logic behind a CDE?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Narrower | [Approved manual adjustments](../analytics-bi/manual-adjustments.md) |
| Related | [Data quality and observability](../data-quality/data-quality.md), [Master and reference data](../master-data/master-data.md), [Bitemporal data](../specialised-data/temporal-data.md), [Business glossary](../metadata/business-glossary.md), [Column-level lineage](../metadata/column-lineage.md), [Compliance controls and evidence](compliance-evidence.md), [Data lineage](../metadata/data-lineage.md), [Data quality rules](../data-quality/data-quality-rules.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Impact analysis](../metadata/impact-analysis.md), [Paginated reports](../analytics-bi/paginated-reports.md), [Reference data management](../master-data/reference-data-management.md), [Regulatory submission](../serving/regulatory-submission.md) |
| Depends on | [Column-level lineage](../metadata/column-lineage.md), [Data quality rules](../data-quality/data-quality-rules.md) |

# Where it appears

- **Use cases:** [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data steward](../../personas/persona-data-steward.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 1 – Governance; Principle 3 – Accuracy and integrity; Principle 4 – Completeness; Principle 9 – Clarity and usefulness · [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md) |

Narrower capabilities are realised by a further 1 technologies; see their pages.
