---
type: Capability
id: data-writeback
title: Data entry and write-back
description: Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.
aliases: [writeback, translytical, input tables, operational actions]
broader: [analytics-bi]
related:
- reference-data-management
- data-applications
- enterprise-planning
- audit-logging
- spreadsheet-integration
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many decisions taken in a report end in an input or a correction: adjusting a sales forecast, explaining a variance, assigning a customer to a segment, or fixing a mis-mapped cost centre. Write-back lets the user do this in the analytics tool instead of emailing a spreadsheet to an engineer. The tool validates the entry and writes it to a governed table with who changed what and when, and downstream models pick it up on their next refresh.

It closes the loop between analysis and action, and replaces side spreadsheets with controlled data. Approaches range from input forms and editable grids in BI tools to small data applications and spreadsheet add-ins. Points to settle are validation rules, approval for sensitive changes, handling two people editing the same row, and history. Larger managed lists overlap with reference data management, which adds versioning and approval workflows.

# Key considerations

- Write user input to separate, append-only tables and apply it in models, rather than editing source data in place. This keeps an audit trail and allows reversal.
- Validate at entry: types, allowed values, ranges and mandatory fields. Bad manual input is a common source of quality incidents.
- Grant write permission explicitly and narrowly. Read access to a dashboard should not imply the right to change its figures.
- Agree how quickly edits appear in reports, since users expect to see their change straight away.

# Questions to ask

- What data is maintained by hand beside the platform today, and by whom?
- Do changes need approval before they take effect?
- Must every change be traceable to a person for audit?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Narrower | [Approved manual adjustments](manual-adjustments.md) |
| Related | [Audit logging](../security/audit-logging.md), [Data application hosting](../development-lifecycle/data-applications.md), [Operational database integration](../serving/operational-database.md), [Planning and forecasting](enterprise-planning.md), [Reference data management](../master-data/reference-data-management.md), [Spreadsheet integration](spreadsheet-integration.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 2)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric user data functions](../../technologies/microsoft/fabric-user-data-functions.md), [Planning in Fabric IQ](../../technologies/microsoft/fabric-iq-planning.md), [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md), [Palantir Workshop](../../technologies/palantir/palantir-workshop.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Metabase](../../technologies/open-source/metabase.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Sigma Computing](../../technologies/independent/sigma.md) |

Narrower capabilities are realised by a further 1 technologies; see their pages.
