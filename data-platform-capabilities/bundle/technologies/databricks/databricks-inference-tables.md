---
type: Technology
id: databricks-inference-tables
title: Databricks inference tables
description: Logs requests and responses from serving endpoints, foundation model calls and agents to Unity Catalog Delta tables for monitoring, audit and retraining.
platform: platform-databricks
kind: feature
availability: ga
realises: [inference-logging]
resource: https://docs.databricks.com/aws/en/machine-learning/model-serving/inference-tables
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The legacy inference tables are retired in favour of gateway-enabled inference tables, which use a different schema. Migration is one-way. Data profiling inference profiles run on these tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Inference logging](../../capabilities/mlops/inference-logging.md) (ML operations) (primary): Capture model inputs, outputs and metadata for monitoring, audit and retraining.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Inference logging](../../capabilities/mlops/inference-logging.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Inference logging](../../capabilities/mlops/inference-logging.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Inference logging](../../capabilities/mlops/inference-logging.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview), [KServe](../open-source/kserve.md) | [Inference logging](../../capabilities/mlops/inference-logging.md) |
