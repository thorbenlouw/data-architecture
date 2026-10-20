---
type: Technology
id: informatica-cloud-data-quality
title: Informatica Cloud Data Quality (CDQ)
description: Defines and runs rule specifications, cleansing, parsing, standardisation, deduplication and verification assets using reference dictionaries, and routes exceptions to people for review.
aliases: [CDQ, Informatica Data Quality and Observability]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [data-quality-rules, data-cleansing, entity-resolution, bad-data-quarantine, data-enrichment]
resource: https://www.informatica.com/products/data-quality.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Informatica now markets it as "Data Quality and Observability". Rules run inside Data Integration mappings, and since Spring 2026 also directly in CDI data flows. Address Verification (formerly AddressDoctor) is available as a quality asset and, since 2026, as a headless service that agents can call.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability) (primary): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md) (Data quality and observability): Route records that fail checks to a holding area for inspection and replay instead of failing or loading them.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Informatica Data Quality and Observability

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data quality](../google-cloud/gcp-knowledge-catalog-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data quality monitoring (data metric functions)](../snowflake/snowflake-data-quality-monitoring.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow pipelines expectations](../databricks/databricks-pipeline-expectations.md) | [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Master Data Governance](../sap/sap-master-data-governance.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Health and data expectations](../palantir/palantir-data-health.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Quality rules](../dataiku/dataiku-data-quality.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [GX Core (Great Expectations)](../open-source/great-expectations.md), [Soda Core](../open-source/soda-core.md), [Dagster](../open-source/dagster.md) | [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Experian Aperture Data Studio](../independent/experian-aperture-data-studio.md), [Precisely Data Integrity Suite](../independent/precisely-data-integrity-suite.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Data enrichment](../../capabilities/processing/data-enrichment.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md), [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
