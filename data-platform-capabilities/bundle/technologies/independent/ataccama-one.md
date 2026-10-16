---
type: Technology
id: ataccama-one
title: Ataccama ONE
description: Data management platform for profiling, rule-based quality and cleansing, observability, catalogue and lineage, which shares one rule library and metadata model across its modules.
aliases: [Ataccama]
platform: platform-independent
vendor: Ataccama
kind: software
availability: ga
realises: [data-quality-rules, data-profiling, data-cleansing, data-observability, data-catalogue]
resource: https://www.ataccama.com/platform
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Deployed as Ataccama Cloud (SaaS, with processing kept local) or self-managed on premises. The ONE AI Agent helps write rules and set up monitoring. Quality rules can be reused in pipelines, on the platform's own engine or pushed down to Snowflake and similar platforms.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Data observability](../../capabilities/data-quality/data-observability.md) (Data quality and observability): Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md), [CLAIRE Data Quality Agent](../informatica/informatica-claire-data-quality-agent.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data observability](../../capabilities/data-quality/data-observability.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [OpenMetadata](../open-source/openmetadata.md), [Soda Core](../open-source/soda-core.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
