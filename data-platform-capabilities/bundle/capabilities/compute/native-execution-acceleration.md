---
type: Capability
id: native-execution-acceleration
title: Vectorised native execution
description: Speed up engines by running operators in native, vectorised code without changing user code.
aliases: [native engines, vectorised execution]
broader: [query-acceleration]
related: [distributed-processing, dataframe-apis, columnar-storage, cost-optimisation, gpu-compute]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many engines run on the Java virtual machine and process data largely one row at a time. Vectorised native execution replaces their operators, such as scans, filters, joins and aggregations, with compiled machine code that processes batches of column values at once, using CPU instructions that apply one operation to many values (SIMD). The planner and user code stay the same; the plan is handed to a native library to run. Velox and Apache DataFusion are open-source examples, used inside Spark through projects such as Apache Gluten and DataFusion Comet.

It can make existing SQL and DataFrame jobs run several times faster on the same compute without rewriting them, which means lower cost or shorter run times. Gains are largest for CPU-heavy scans, aggregations and joins on columnar data, and smaller for jobs limited by reading data or by network transfer. Not every operator or function is supported, so parts of a plan may fall back to the original engine, with a conversion cost at each boundary.

# Key considerations

- Check fallback behaviour. Unsupported functions and user-defined functions can push parts of a plan back to the original engine and erase the gain.
- Verify that results match. Floating-point handling, overflow and string collation can differ at the edges.
- Benchmark on your own jobs. Published speed-ups come from standard benchmarks that may not resemble your workload.
- Native code changes how memory errors and crashes appear. Teams need new skills to debug them.

# Questions to ask

- Is most job time spent on CPU-heavy scans and aggregations, or on reading data and moving it between workers?
- How much code relies on user-defined functions that a native engine may not support?
- Would faster jobs reduce cost, meet a deadline, or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query acceleration](query-acceleration.md) |
| Related | [Columnar storage](../storage/columnar-storage.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [DataFrame APIs](../processing/dataframe-apis.md), [Distributed processing](../processing/distributed-processing.md), [GPU and accelerated compute](gpu-compute.md) |

# Where it appears

- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Managed Service for Apache Spark on clusters](../../technologies/google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Photon](../../technologies/databricks/databricks-photon.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Presto (C++) engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-presto.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache DataFusion](../../technologies/open-source/apache-datafusion.md), [Apache Gluten](../../technologies/open-source/apache-gluten.md), [Presto](../../technologies/open-source/presto.md) |
