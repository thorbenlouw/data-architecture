---
type: Technology
id: dataiku-data-quality
title: Dataiku Data Quality rules
description: Rules on dataset contents, such as value ranges, uniqueness, record counts, schema and values within their usual range, that can run automatically after each build and roll up into dataset, project and instance views.
aliases: [Metrics and checks, Data Quality Templates]
platform: platform-dataiku
kind: feature
availability: ga
realises: [data-quality-rules, data-quality-scorecards, data-anomaly-detection]
resource: https://doc.dataiku.com/dss/latest/metrics-check-data-quality/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Improves on the older checks mechanism, which remains supported. Rules have hard and soft thresholds, can be written in Python or plugins, and can be reused as templates. A scenario step that verifies rules fails when a rule fails, stopping the pipeline.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) (Data quality and observability): Track quality results over time and report them by dataset, domain and quality dimension.
- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability): Learn normal patterns in data and alert on unexpected changes without hand-written rules.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md), [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md), [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
