---
type: Technology
id: sas-cloud-analytic-services
title: SAS Cloud Analytic Services (CAS)
description: In-memory engine in SAS Viya that loads tables across a cluster of workers and runs data preparation, SQL, statistics and machine learning on them in parallel.
aliases: [CAS, CAS server, Cloud Analytic Services]
platform: platform-sas
kind: feature
availability: ga
realises: [distributed-processing, sql-query-engine, dataframe-apis]
resource: https://go.documentation.sas.com/doc/en/pgmsascdc/default/casfun/titlepage.htm
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

A controller coordinates worker nodes, each of which processes the rows held in its memory. Data sources are reached through caslibs, which point at files, databases or cloud storage. SQL runs through the FedSQL action set, and Python and R programs drive CAS actions through the SWAT packages. CAS can also run as a single-machine server for smaller deployments.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md), [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Apache Gluten](../open-source/apache-gluten.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
