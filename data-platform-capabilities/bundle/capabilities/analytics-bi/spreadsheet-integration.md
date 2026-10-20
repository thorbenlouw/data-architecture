---
type: Capability
id: spreadsheet-integration
title: Spreadsheet integration
description: Work with governed platform data directly from spreadsheet tools.
aliases: [connected sheets, live Excel connection]
broader: [analytics-bi]
related: [semantic-layer, data-writeback, data-loss-prevention, enterprise-planning, column-masking]
depends_on: [sql-access]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of pasting a fresh export each month, a finance analyst inserts a live table or pivot from a certified sales model, filters it in the spreadsheet, and refreshes it next month. Common mechanisms are add-ins that query the platform or semantic layer, connected tables and pivots, spreadsheet-style interfaces that run directly on platform tables, and cell functions that return a governed metric.

Spreadsheets remain the main analysis tool for many finance and operations teams, and unmanaged exports into them create copies that go stale and escape access controls. A live connection keeps one definition and one set of permissions. Variants differ in direction and scale: some only read small results, some push edits back, and some evaluate spreadsheet formulas over billions of rows inside the platform. Sending edits back is covered by data entry and write-back.

# Key considerations

- Queries must run as the spreadsheet user so permissions match other tools. Shared files with embedded credentials break this.
- A refreshed spreadsheet is still a copy once saved. Decide whether sensitive data may be stored in files at all.
- Large pulls into a spreadsheet are slow and hit row limits. Push aggregation down to the platform.
- Connecting through the semantic layer keeps metric definitions consistent with dashboards.

# Questions to ask

- Which teams rely on spreadsheets for recurring reporting, and how do they get data today?
- How much sensitive data sits in exported spreadsheets?
- Do users need to edit data in the sheet and send it back?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Column security and dynamic masking](../security/column-masking.md), [Data entry and write-back](data-writeback.md), [Data loss prevention](../security/data-loss-prevention.md), [Planning and forecasting](enterprise-planning.md), [Self-service data preparation](../processing/data-preparation.md), [Semantic layer](semantic-layer.md), [SQL and programmatic access](../serving/sql-access.md) |
| Depends on | [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Use cases:** [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI Analyze in Excel and connected tables](../../technologies/microsoft/powerbi-excel-integration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Connected Sheets | [Connected Sheets](../../technologies/google-cloud/gcp-connected-sheets.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Excel Add-in](../../technologies/databricks/databricks-excel-add-in.md), [Genie One](../../technologies/databricks/databricks-genie-one.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Visual Analytics](../../technologies/sas/sas-visual-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Sigma Computing](../../technologies/independent/sigma.md) |
