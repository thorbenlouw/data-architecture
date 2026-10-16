---
type: Technology
id: powerbi-paginated-reports
title: Power BI paginated reports
description: Pixel-precise, printable reports built in Power BI Report Builder and rendered to PDF, Excel, Word and other formats.
aliases: [Power BI Report Builder]
platform: platform-microsoft
kind: feature
availability: ga
realises: [paginated-reports, data-export]
resource: https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Successor to SQL Server Reporting Services reports; runs on Pro, PPU or capacity.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) (Analytics and BI) (primary): Produce formatted, printable reports with precise layout for operational and regulatory use.
- [Data export](../../capabilities/serving/data-export.md) (Serving and activation): Unload query results or tables to files and external systems in bulk.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md) | [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data unloading (COPY INTO <location>)](../snowflake/snowflake-unload.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md) | [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Cloud Analytics](../independent/qlik-cloud-analytics.md) | [Paginated reports](../../capabilities/analytics-bi/paginated-reports.md) |
