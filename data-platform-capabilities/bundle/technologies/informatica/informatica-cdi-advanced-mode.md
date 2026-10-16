---
type: Technology
id: informatica-cdi-advanced-mode
title: Informatica Cloud Data Integration advanced mode
description: Runs Data Integration mappings on a Kubernetes-based advanced cluster for distributed processing of large and hierarchical data, with Python and Java code steps and machine learning model calls.
formerly: [Cloud Data Integration-Elastic, elastic mappings]
platform: platform-informatica
kind: feature
availability: ga
realises: [distributed-processing, semi-structured-data, elastic-scaling]
resource: https://onlinehelp.informatica.com/IICS/prod/CDI/en/hh-cloud-mappings/Mappings_in_advanced_mode.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

There are four cluster types: local single-node, fully managed by Informatica, self-service on your own Kubernetes (for example Amazon EKS), and one created by a serverless runtime environment. Use it for hierarchical JSON/XML processing (Hierarchy Processor) and volumes too large for the Secure Agent engine.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Spark](../open-source/apache-spark.md), [Dask](../open-source/dask.md), [Apache Gluten](../open-source/apache-gluten.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
