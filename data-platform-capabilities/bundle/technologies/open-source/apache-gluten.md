---
type: Technology
id: apache-gluten
title: Apache Gluten
description: Plug-in that offloads Spark SQL execution to native, vectorised C++ engines such as Velox or ClickHouse while keeping Spark's APIs and scheduling.
aliases: [Gluten]
platform: platform-open-source
kind: open-source
availability: ga
realises: [native-execution-acceleration, distributed-processing]
resource: https://gluten.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Became an ASF top-level project in early 2026. Velox, its main backend, is a Meta-led C++ execution library that also powers Presto's native workers. Check operator coverage, because queries using unsupported functions fall back to the JVM.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) (Query and compute) (primary): Speed up engines by running operators in native, vectorised code without changing user code.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Photon](../databricks/databricks-photon.md) | [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
| [IBM](../../platforms/platform-ibm.md) | [Presto (C++) engine in IBM watsonx.data](../ibm/ibm-watsonx-data-presto.md) | [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
