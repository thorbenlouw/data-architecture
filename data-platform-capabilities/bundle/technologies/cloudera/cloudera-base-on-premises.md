---
type: Technology
id: cloudera-base-on-premises
title: Cloudera Base on premises
description: The on-premises cluster platform with Cloudera Runtime (HDFS, Ozone, Hive, Impala, Spark, Kafka, HBase and others) managed by Cloudera Manager.
formerly: [CDP Private Cloud Base, Cloudera Data Platform Private Cloud Base, CDH, HDP]
platform: platform-cloudera
kind: software
availability: ga
realises: [distributed-processing, deployment-options, provisioned-compute, sql-query-engine]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runtime 7.3.x is the current line, and Cloudera states that it will support version 7.3.2 until 2032. Older CDH and HDP clusters are still common and upgrade or migrate to it. It also provides the storage and SDX base for [Cloudera Data Services on premises](cloudera-data-services-on-premises.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [SQL query engine](../../capabilities/compute/sql-query-engine.md) (Query and compute): Run analytical SQL over large datasets with parallel, optimised execution.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Data Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md), [Snowflake generation 2 standard warehouses](../snowflake/snowflake-gen2-warehouses.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md), [Teradata Factory](../teradata/teradata-factory.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md), [IBM Netezza Performance Server](../ibm/ibm-netezza.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md), [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Enterprise](../independent/starburst-enterprise.md) | [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md), [SQL query engine](../../capabilities/compute/sql-query-engine.md) |
