---
type: Technology
id: aws-glue-etl
title: AWS Glue ETL
description: Serverless Apache Spark and Python job service for extracting, transforming and loading data, with a visual editor in Glue Studio and native connectors.
aliases: [AWS Glue Studio, AWS Glue for Apache Spark, Glue jobs]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- distributed-processing
- serverless-compute
- low-code-transformation
- saas-connectors
- incremental-processing
- runtime-management
resource: https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Glue 5.1 is the current Spark runtime. Job bookmarks give incremental loads; streaming ETL jobs read Kinesis and Kafka; native connectors cover JDBC databases and SaaS sources such as Salesforce and SAP. Glue for Ray closed to new customers on 30 April 2026 (AWS suggests KubeRay on EKS).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** AWS Glue

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Incremental processing](../../capabilities/processing/incremental-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark](../snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Apache Gluten](../open-source/apache-gluten.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
