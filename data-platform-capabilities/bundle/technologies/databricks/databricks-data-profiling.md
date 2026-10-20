---
type: Technology
id: databricks-data-profiling
title: Databricks data profiling
description: Computes profile and drift metrics for a table over time as snapshot, time-series or inference profiles, and stores them in Delta tables with a generated dashboard.
formerly: [Lakehouse Monitoring, Databricks Lakehouse Monitoring]
platform: platform-databricks
kind: feature
availability: ga
realises: [data-profiling, drift-detection, model-performance-monitoring]
resource: https://docs.databricks.com/aws/en/data-quality-monitoring
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data profiling is part of data quality monitoring alongside anomaly detection. Inference profiles on inference tables monitor model and endpoint quality. Snapshot profiles are limited to 4 TB.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability) (primary): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks data quality monitoring

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue DataBrew](../aws/aws-glue-databrew.md), [AWS Glue Data Quality](../aws/aws-glue-data-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Quality](../microsoft/purview-data-quality.md), [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data profiling](../google-cloud/gcp-knowledge-catalog-data-profiling.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data Profiling](../informatica/informatica-data-profiling.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [IBM](../../platforms/platform-ibm.md) | [Data quality in IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence-quality.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Engineering](../sas/sas-data-engineering.md), [SAS Data Governance](../sas/sas-data-governance.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku model evaluation stores and Unified Monitoring](../dataiku/dataiku-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md), [GX Core (Great Expectations)](../open-source/great-expectations.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Experian Aperture Data Studio](../independent/experian-aperture-data-studio.md), [GX Cloud](../independent/gx-cloud.md), [Ataccama ONE](../independent/ataccama-one.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md) |
