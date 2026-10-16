---
type: Technology
id: databricks-dqm-anomaly-detection
title: Databricks data quality monitoring anomaly detection
description: Monitors every table in a schema with one setting. It learns each table's update and volume patterns, flags late or incomplete tables, and suggests root causes using lineage.
platform: platform-databricks
kind: feature
availability: preview
realises: [data-anomaly-detection, freshness-monitoring, data-issue-management]
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public Preview since February 2026. Incidents can be claimed or dismissed, and alerts carry root-cause information. Results go to system.data_quality_monitoring.table_results. It bills as serverless usage and scans high-impact tables more often.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability) (primary): Learn normal patterns in data and alert on unexpected changes without hand-written rules.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.
- [Data issue management](../../capabilities/data-quality/data-issue-management.md) (Data quality and observability): Log, assign, track and resolve data quality incidents with their owners.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview  
**Product family:** Databricks data quality monitoring

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica data observability](../informatica/informatica-data-observability.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data observability in IBM watsonx.data integration](../ibm/ibm-data-observability.md), [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Data + AI Observability](../independent/monte-carlo-data-observability.md), [Sifflet](../independent/sifflet.md), [Soda Cloud](../independent/soda-cloud.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data issue management](../../capabilities/data-quality/data-issue-management.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
