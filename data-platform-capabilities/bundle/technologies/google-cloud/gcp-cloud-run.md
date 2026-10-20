---
type: Technology
id: gcp-cloud-run
title: Cloud Run
description: Serverless platform for running containers, functions and jobs that scale to zero, often used for data APIs, remote functions and data applications.
aliases: [Cloud Run functions]
formerly: [Cloud Functions]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [container-services, serverless-compute, data-applications]
resource: https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cloud Functions is now Cloud Run functions. Cloud Run supports GPUs for inference and is the usual host for BigQuery remote functions, MCP Toolbox and Streamlit-style apps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Container services](../../capabilities/compute/container-services.md) (Query and compute) (primary): Run custom containerised applications and services next to the data, inside the platform's security boundary.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EKS](../aws/aws-emr-on-eks.md) | [Container services](../../capabilities/compute/container-services.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Container Services](../snowflake/snowflake-snowpark-container-services.md) | [Container services](../../capabilities/compute/container-services.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Apps](../databricks/databricks-apps.md) | [Container services](../../capabilities/compute/container-services.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Services on premises](../cloudera/cloudera-data-services-on-premises.md) | [Container services](../../capabilities/compute/container-services.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Container services](../../capabilities/compute/container-services.md) |
