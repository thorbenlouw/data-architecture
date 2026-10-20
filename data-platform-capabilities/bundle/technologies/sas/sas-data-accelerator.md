---
type: Technology
id: sas-data-accelerator
title: SAS Data Accelerator
description: Capability of SAS Viya that runs SAS model scoring, data quality functions and some analytics inside external databases and cloud data platforms instead of moving the data to SAS.
aliases: [SAS Scoring Accelerator, SAS Code Accelerator, SAS Data Quality Accelerator]
formerly: [SAS In-Database Technologies]
platform: platform-sas
kind: feature
availability: ga
realises: [batch-inference, data-cleansing, entity-resolution]
resource: https://www.sas.com/en_us/software/data-accelerator.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Renamed from SAS In-Database Technologies, whose components included the SAS Scoring Accelerator, SAS Code Accelerator and SAS Data Quality Accelerator. SAS lists it as available for Cloudera Data Platform, Azure Synapse Analytics, Databricks and Teradata. In-database data quality functions include standardisation, matching and entity identification.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations) (primary): Score large datasets with a model on a schedule.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Entity resolution](../../capabilities/master-data/entity-resolution.md) (Master and reference data): Find and link records that refer to the same real-world entity, even when they do not match exactly.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md), [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md), [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow ML](../google-cloud/gcp-dataflow-ml.md), [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md), [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md), [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Bring Your Own Model (BYOM)](../teradata/teradata-byom.md), [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Batch inference](../../capabilities/mlops/batch-inference.md) |
