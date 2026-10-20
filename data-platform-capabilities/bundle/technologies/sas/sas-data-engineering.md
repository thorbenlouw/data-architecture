---
type: Technology
id: sas-data-engineering
title: SAS Data Engineering
description: Packaged SAS Viya offering for building data pipelines that bundles visual and code-based development, data connectivity, data profiling, data quality, entity resolution and governance.
aliases: [SAS Data Engineering Advanced]
platform: platform-sas
kind: software
availability: ga
realises: [data-cleansing, data-profiling, entity-resolution, data-preparation]
resource: https://www.sas.com/en_us/software/data-engineering.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

It includes [SAS Data and AI Studio](sas-data-and-ai-studio.md), [SAS Data Hub](sas-data-hub.md), [SAS Data Governance](sas-data-governance.md), [SAS Data Accelerator](sas-data-accelerator.md), SAS Workload Management and SAS Visual Analytics; SAS Data Engineering Advanced adds SAS Intelligent Decisioning. Data quality functions such as parsing, standardisation and matchcodes for fuzzy matching come from the SAS Quality Knowledge Base, which holds rules for each locale, and machine learning suggests data preparation steps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability) (primary): Correct and standardise data values such as addresses, names, dates and codes.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue DataBrew](../aws/aws-glue-databrew.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Data profiling](../../capabilities/data-quality/data-profiling.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Quality (CDQ)](../informatica/informatica-cloud-data-quality.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Experian Aperture Data Studio](../independent/experian-aperture-data-studio.md), [Ataccama ONE](../independent/ataccama-one.md), [Tamr](../independent/tamr.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Data profiling](../../capabilities/data-quality/data-profiling.md), [Entity resolution](../../capabilities/master-data/entity-resolution.md) |
