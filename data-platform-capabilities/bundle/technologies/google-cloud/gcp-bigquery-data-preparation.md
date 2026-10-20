---
type: Technology
id: gcp-bigquery-data-preparation
title: BigQuery data preparation
description: Visual, Gemini-assisted editor for cleaning, joining and reshaping BigQuery data that saves its steps as runnable SQLX.
platform: platform-google-cloud
kind: feature
availability: preview
realises: [data-preparation, low-code-transformation, data-cleansing, bad-data-quarantine]
resource: https://docs.cloud.google.com/bigquery/docs/data-prep-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Gemini proposes cleaning and reshaping steps for review. Preparations can be scheduled directly or as tasks inside BigQuery pipelines, and validation steps send failing rows to an error table. It is free of charge while in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation) (primary): Let analysts profile, clean and reshape data interactively without engineering help.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Bad-data quarantine](../../capabilities/data-quality/bad-data-quarantine.md) (Data quality and observability): Route records that fail checks to a holding area for inspection and replay instead of failing or loading them.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** preview  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue DataBrew](../aws/aws-glue-databrew.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Contour and Quiver](../palantir/palantir-contour-quiver.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Engineering](../sas/sas-data-engineering.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [pandas](../open-source/pandas.md) | [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Alteryx One](../independent/alteryx-one.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [Tableau Cloud](../independent/tableau-cloud.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
