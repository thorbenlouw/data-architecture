---
type: Technology
id: gcp-knowledge-catalog-data-quality
title: Knowledge Catalog data quality
description: Runs declarative or recommended data quality rules against BigQuery and Lakehouse tables as scheduled scans and publishes results and scores.
formerly: [Dataplex auto data quality, Dataplex data quality]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-quality-rules, data-quality-scorecards, data-observability, data-trust-indicators]
resource: https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Rules can be managed as code, reused through system templates and debugged with generated queries (preview). Results can be exported to BigQuery and alerted on through Cloud Logging and Monitoring; scorecards integrate with BigQuery pipelines and Dataform (GA October 2026). Older Dataplex data quality tasks are legacy.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) (Data quality and observability): Track quality results over time and report them by dataset, domain and quality dimension.
- [Data observability](../../capabilities/data-quality/data-observability.md) (Data quality and observability): Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
- [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) (Metadata and discovery): Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Knowledge Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md), [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Quality & Observability](../independent/collibra-data-quality-observability.md), [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) |
