---
type: Technology
id: snowflake-data-quality-monitoring
title: Snowflake data quality monitoring (data metric functions)
description: Schedules system and custom data metric functions on tables and views, compares results with expectations, and detects volume and freshness anomalies, with results in Snowsight.
aliases: [data metric functions, DMFs]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-quality-rules, freshness-monitoring, data-anomaly-detection, data-quality-scorecards]
resource: https://docs.snowflake.com/en/user-guide/data-quality-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition and is billed as serverless credits. Anomaly detection and the account-wide quality dashboard are in preview. DMFs can be applied at schema level and managed through DCM Projects.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.
- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability): Learn normal patterns in data and alert on unexpected changes without hand-written rules.
- [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) (Data quality and observability): Track quality results over time and report them by dataset, domain and quality dimension.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md), [Databricks data quality monitoring anomaly detection](../databricks/databricks-dqm-anomaly-detection.md) (preview) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md), [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md), [Informatica data observability](../informatica/informatica-data-observability.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Quality rules](../dataiku/dataiku-data-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md), [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
