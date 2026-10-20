---
type: Technology
id: databricks-pipeline-expectations
title: Lakeflow pipelines expectations
description: Declarative data quality constraints on pipeline datasets. For each failing record you choose to warn, drop it or fail the update, and the results are recorded in the pipeline event log.
platform: platform-databricks
kind: feature
availability: ga
realises: [data-quality-rules, bad-data-quarantine]
resource: https://docs.databricks.com/aws/en/ldp/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Quarantine needs a pattern, such as writing inverted expectations to a separate table, because there is no built-in holding area. Expectation metrics can be queried from the event log and the pipeline_events system table (Beta).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md) (Data quality and observability): Route records that fail checks to a holding area for inspection and replay instead of failing or loading them.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Quality rules](../dataiku/dataiku-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md), [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
