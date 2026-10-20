---
type: Technology
id: purview-data-quality
title: Microsoft Purview Data Quality
description: Profiles data and runs out-of-the-box, custom and AI-suggested quality rules on data products, rolling scores up to products and domains.
platform: platform-microsoft
kind: feature
availability: ga
realises:
- data-quality-rules
- data-profiling
- data-quality-scorecards
- freshness-monitoring
- data-issue-management
resource: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs on Purview-managed Spark against sources in the same Azure region, authenticating with managed identity. Up to 200 rules per asset per scan. Alerts go to owners and stewards.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) (Data quality and observability): Track quality results over time and report them by dataset, domain and quality dimension.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.
- [Data issue management](../../capabilities/data-quality/data-issue-management.md) (Data quality and observability): Log, assign, track and resolve data quality incidents with their owners.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md), [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Quality rules](../dataiku/dataiku-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [GX Cloud](../independent/gx-cloud.md), [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
