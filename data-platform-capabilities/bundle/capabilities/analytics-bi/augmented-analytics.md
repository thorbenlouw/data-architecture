---
type: Capability
id: augmented-analytics
title: Augmented analytics
description: Use automation and machine learning to surface insights, anomalies and explanations without being asked.
aliases: [auto-insights]
broader: [analytics-bi]
related:
- data-anomaly-detection
- data-alerting
- conversational-analytics
- pretrained-predictive-models
- model-explainability
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Augmented analytics applies statistics and machine learning inside analytics tools to do work an analyst would otherwise do by hand. Examples include flagging that weekly returns in one region are far above their normal range, explaining which products and channels contributed most to a change in revenue, suggesting suitable charts for a dataset, and drawing a short forecast on a trend line. Results appear as annotations on dashboards, ranked insight feeds or automatically written summaries.

It helps when there are more metrics and segments than anyone can watch, and changes are noticed too late. The main techniques are anomaly detection on metric time series, key-driver or contribution analysis, automatic segmentation and forecasting; generative models now write many of the narrative summaries. It differs from data anomaly detection in data quality, which looks for broken data. Augmented analytics looks for real business changes, though both often flag the same spike and the cause has to be told apart.

# Key considerations

- Too many automatic insights get ignored. Tune sensitivity and limit feeds to metrics that someone owns.
- Driver analysis shows association, not cause. Present it as a lead for investigation.
- Check data quality status before announcing an insight, so a broken pipeline is not reported as a sales drop.
- Insights are only as good as the metrics behind them. Ungoverned metrics produce confident explanations of the wrong numbers.

# Questions to ask

- Which metrics are watched today, and how quickly are unusual changes noticed?
- Who would act on an automatic insight, and through which channel?
- Can users see how an insight or forecast was calculated?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Alerts and subscriptions](data-alerting.md), [AutoML](../machine-learning/automl.md), [Conversational analytics](conversational-analytics.md), [Data anomaly detection](../data-quality/data-anomaly-detection.md), [Model explainability](../machine-learning/model-explainability.md), [Pretrained predictive models](../machine-learning/pretrained-predictive-models.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Copilot in Power BI](../../technologies/microsoft/powerbi-copilot.md), [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Conversational Analytics in Looker](../../technologies/google-cloud/gcp-looker-conversational-analytics.md), [Knowledge Catalog data insights](../../technologies/google-cloud/gcp-knowledge-catalog-data-insights.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Functions](../../technologies/snowflake/snowflake-ml-functions.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud](../../technologies/oracle/oracle-analytics-cloud.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md), [Tableau Pulse](../../technologies/independent/tableau-pulse.md), [ThoughtSpot Spotter](../../technologies/independent/thoughtspot-spotter.md) |
