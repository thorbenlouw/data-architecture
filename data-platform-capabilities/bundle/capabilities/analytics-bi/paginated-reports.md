---
type: Capability
id: paginated-reports
title: Paginated reports
description: Produce formatted, printable reports with precise layout for operational and regulatory use.
aliases: [pixel-perfect reports]
broader: [analytics-bi]
related: [data-alerting, critical-data-elements, compliance-evidence, row-level-security, data-export]
depends_on: [sql-access]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A paginated report is laid out for pages: fixed headers and footers, page numbers, grouped tables that break cleanly across pages, and exact placement of logos and signature blocks. Typical examples are a monthly statement for each of 50,000 customers, or a regulatory return that must match a prescribed template. Reports take parameters such as account or period and render to PDF, spreadsheet, word-processor formats or print, often in large scheduled batches. Bursting splits one run into a separate copy for each recipient.

They are needed for operational documents and formal submissions where layout and completeness matter more than interactivity: invoices, statements, regulatory filings and audit packs. A dashboard shows the first rows of a table and scrolls; a paginated report prints every row. Requirements to weigh include rendering volume, accurate templates, an archive of what was sent, and evidence that each submitted figure came from a controlled source.

# Key considerations

- Bursting thousands of reports puts sustained load on the platform. Schedule it and size compute so it does not collide with daytime work.
- Archive the rendered output that was actually sent, not only the ability to rerun it, because the underlying data changes.
- Regulatory templates change. Check how easily layouts can be edited, versioned and tested.
- Each external recipient must see only their own data. Apply filtering per recipient at render time and treat distribution as a data-loss risk.

# Questions to ask

- Which reports must match a prescribed layout, or go to regulators, customers or auditors?
- How many reports does each run produce, and in which formats?
- Must you prove later exactly what a recipient received?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Alerts and subscriptions](data-alerting.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Critical data elements](../governance/critical-data-elements.md), [Data export](../serving/data-export.md), [Regulatory submission](../serving/regulatory-submission.md), [Row-level security](../security/row-level-security.md) |
| Depends on | [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 8 – Comprehensiveness; Principle 10 – Frequency · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Quick Sight pixel-perfect reports | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI paginated reports](../../technologies/microsoft/powerbi-paginated-reports.md), [Power BI Report Server](../../technologies/microsoft/powerbi-report-server.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Looker](../../technologies/google-cloud/gcp-looker.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud](../../technologies/oracle/oracle-analytics-cloud.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md) |
