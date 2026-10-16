---
type: Technology
id: aws-glue-databrew
title: AWS Glue DataBrew
description: No-code visual tool for profiling, cleaning and reshaping datasets with more than 250 reusable transformation steps saved as recipes.
aliases: [DataBrew]
platform: platform-aws
kind: managed-service
availability: ga
realises: [data-preparation, data-profiling, data-cleansing, deidentification]
resource: https://docs.aws.amazon.com/databrew/latest/dg/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Recipes can be run as scheduled jobs writing to S3, and include PII detection and masking steps. Overlaps with SageMaker Canvas data preparation and Glue Studio visual ETL; it is not part of SageMaker Unified Studio.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation) (primary): Let analysts profile, clean and reshape data interactively without engineering help.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** AWS Glue

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pandas](../open-source/pandas.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Alteryx One](../independent/alteryx-one.md), [Dataiku](../independent/dataiku.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
