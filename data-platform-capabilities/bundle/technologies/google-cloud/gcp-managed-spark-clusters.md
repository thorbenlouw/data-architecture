---
type: Technology
id: gcp-managed-spark-clusters
title: Google Cloud Managed Service for Apache Spark on clusters
description: Provisions and manages Spark, Hadoop, Hive, Flink and Trino clusters on Compute Engine that you size, configure and can access directly.
formerly: [Dataproc, Dataproc on Compute Engine]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [distributed-processing, provisioned-compute, native-execution-acceleration, interruptible-compute]
resource: https://docs.cloud.google.com/managed-spark/docs/concepts/compare
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Managed Service for Apache Spark since April 2026; the API is still dataproc. Billed on cluster uptime with Compute Engine discounts, and suited to lift-and-shift Hadoop and long-running shared clusters. The Lightning Engine accelerator is available for Spark SQL and DataFrame workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) (Query and compute): Speed up engines by running operators in native, vectorised code without changing user code.
- [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) (Query and compute): Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Managed Service for Apache Spark

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md), [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Gluten](../open-source/apache-gluten.md), [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md), [Dask](../open-source/dask.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
