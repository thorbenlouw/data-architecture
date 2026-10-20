---
type: Technology
id: apache-spark
title: Apache Spark
description: Distributed engine for batch, SQL, streaming and machine learning workloads, with DataFrame APIs in Python, Scala, Java, R and SQL.
aliases: [Spark, PySpark, Spark SQL, Spark Connect]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- distributed-processing
- dataframe-apis
- sql-transformation
- user-defined-functions
- semi-structured-data
- approximate-query-processing
resource: https://spark.apache.org/news/index.html
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. Spark 4.2.0 was released in July 2026; the 4.x line made ANSI SQL mode the default, made VARIANT and SQL scripting GA, and made Spark Connect (a thin client protocol) the recommended way to attach clients. Databricks is the main commercial contributor.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
- [Semi-structured data](../../capabilities/storage/semi-structured-data.md) (Storage and table management): Store and query nested data such as JSON without flattening it first.
- [Approximate query processing](../../capabilities/compute/approximate-query-processing.md) (Query and compute): Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark](../snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Approximate query processing](../../capabilities/compute/approximate-query-processing.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Semi-structured data](../../capabilities/storage/semi-structured-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
