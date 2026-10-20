---
type: Capability
id: data-lineage
title: Data lineage
description: Track where data comes from, how it is transformed and where it goes.
aliases: [lineage, data provenance, traceability]
broader: [metadata]
related:
- data-catalogue
- data-observability
- critical-data-elements
- privacy-management
- metadata-interoperability
depends_on: [metadata-harvesting]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lineage is held as a graph. Nodes are datasets, columns, jobs, reports and models; edges show that one was produced from another by a particular process. The graph is assembled from parsed code, run-time events emitted by engines and tools, and tool APIs, and is shown as an interactive diagram upstream and downstream of any asset. For example, when a regulator asks how a capital ratio in a report was calculated, lineage shows the report's source tables, the transformations applied and the ledger extracts behind them.

Lineage supports impact analysis before changes, root-cause analysis during incidents, regulatory traceability such as the BCBS 239 principles for banks, and privacy work that must show where personal data flows. It varies in granularity, from table to column, and in scope, from one platform to end to end, and now extends to documents and models. Design-time lineage is parsed from code before it runs; run-time lineage records what actually executed. OpenLineage is the main open standard for run-time lineage events.

# Key considerations

- Decide first which questions lineage must answer. Regulatory traceability, impact analysis and incident response need different granularity and scope.
- Only automatic capture keeps lineage current. Hand-drawn data flow diagrams go stale within months.
- Some code is opaque to lineage tools, such as stored procedures, spreadsheets and external scripts. Record where the gaps are rather than hiding them.
- Keep history. Auditors may need lineage as it was when a report was produced, not as it is today.

# Questions to ask

- Which regulations or audits require you to show how data flows?
- How do teams find out today what a change will break?
- Which tools in the chain can emit or expose lineage?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md) |
| Narrower | [Column-level lineage](column-lineage.md), [Document and unstructured lineage](unstructured-lineage.md), [End-to-end lineage](cross-system-lineage.md), [Impact analysis](impact-analysis.md), [Model lineage](model-lineage.md), [Table-level lineage](table-lineage.md) |
| Related | [Processing and transformation](../processing/processing.md), [Governance and compliance](../governance/governance.md), [Critical data elements](../governance/critical-data-elements.md), [Data catalogue](data-catalogue.md), [Data observability](../data-quality/data-observability.md), [Metadata interoperability](metadata-interoperability.md), [Privacy impact assessment](../governance/privacy-impact-assessment.md), [Privacy management](../governance/privacy-management.md), [Records of processing](../governance/records-of-processing.md) |
| Depends on | [Metadata harvesting](metadata-harvesting.md) |
| Needed by | [Data licensing and usage rights](../governance/data-usage-rights.md), [Data subject requests](../governance/data-subject-requests.md), [Privacy impact assessment](../governance/privacy-impact-assessment.md), [Privacy management](../governance/privacy-management.md) |

# Where it appears

- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [Medallion architecture](../../patterns/medallion-architecture.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Architecture; Metadata Management · [DCAM v3](../../frameworks/framework-edm-dcam.md): 3 Architecture – Business, Data & Technology; 7 Data Management Operations, Risk & Control · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 10 – Data and data governance · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(a) – Lawfulness, fairness and transparency; Article 5(2) – Accountability; Article 17 – Right to erasure; Article 19 – Notification to recipients; Article 30 – Records of processing activities · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-120 – Provenance · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 4 – Risks of components · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Product Information (input and output ports)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 44 technologies; see their pages.
