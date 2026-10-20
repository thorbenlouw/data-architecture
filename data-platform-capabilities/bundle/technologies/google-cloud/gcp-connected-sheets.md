---
type: Technology
id: gcp-connected-sheets
title: Connected Sheets
description: Lets Google Sheets users analyse BigQuery and Looker data with pivots, formulas and charts that run in the source rather than in the sheet.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [spreadsheet-integration]
resource: https://docs.cloud.google.com/bigquery/docs/connected-sheets
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Google Workspace; queries run under the user's BigQuery permissions and can be refreshed on a schedule. Sheets is outside VPC Service Controls, so perimeters need explicit ingress and egress rules.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) (Analytics and BI) (primary): Work with governed platform data directly from spreadsheet tools.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI Analyze in Excel and connected tables](../microsoft/powerbi-excel-integration.md) | [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Excel Add-in](../databricks/databricks-excel-add-in.md), [Genie One](../databricks/databricks-genie-one.md) | [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Sigma Computing](../independent/sigma.md) | [Spreadsheet integration](../../capabilities/analytics-bi/spreadsheet-integration.md) |
