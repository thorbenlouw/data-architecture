---
type: Technology
id: tableau-pulse
title: Tableau Pulse
description: Metric-following experience in Tableau Cloud that defines metrics once and then sends followers automated summaries of trends, drivers and outliers in Slack, Teams, email and mobile.
platform: platform-independent
vendor: Tableau (Salesforce)
kind: feature
availability: ga
realises: [augmented-analytics, metric-definitions, data-alerting]
resource: https://help.tableau.com/current/online/en-us/pulse_intro.htm
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tableau Agent in Pulse (formerly Enhanced Q&A) answers questions across followed metrics, using precomputed statistical insights. Tableau Cloud only.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI) (primary): Use automation and machine learning to surface insights, anomalies and explanations without being asked.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI reports and dashboards](../microsoft/powerbi-reports.md), [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data insights](../google-cloud/gcp-knowledge-catalog-data-insights.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
