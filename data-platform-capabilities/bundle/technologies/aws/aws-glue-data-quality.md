---
type: Technology
id: aws-glue-data-quality
title: AWS Glue Data Quality
description: Rule engine built on Deequ that evaluates DQDL rulesets on catalogue tables or inside Glue jobs, recommends rules and flags statistical anomalies.
aliases: [DQDL]
platform: platform-aws
kind: feature
availability: ga
realises:
- data-quality-rules
- data-anomaly-detection
- bad-data-quarantine
- data-profiling
- freshness-monitoring
resource: https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In ETL jobs it can identify the failing records so they can be routed aside; on catalogue tables it runs at rest and can recommend rules (an advanced mode uses Bedrock). Dynamic rules compare with history. Scores surface in SageMaker Catalog.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability): Learn normal patterns in data and alert on unexpected changes without hand-written rules.
- [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md) (Data quality and observability): Route records that fail checks to a holding area for inspection and replay instead of failing or loading them.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** AWS Glue

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Quality rules](../dataiku/dataiku-data-quality.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md), [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md), [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
