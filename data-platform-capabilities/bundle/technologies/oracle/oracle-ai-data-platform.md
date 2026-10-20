---
type: Technology
id: oracle-ai-data-platform
title: Oracle AI Data Platform
description: OCI lakehouse workbench that combines Spark compute, notebooks, workflow orchestration, a Master Catalog over Delta Lake and Iceberg data, Delta Sharing and agent building.
platform: platform-oracle
kind: managed-service
availability: ga
realises:
- distributed-processing
- notebooks
- workflow-orchestration
- data-catalogue
- table-format-conversion
- open-protocol-sharing
resource: https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/overview-oracle-ai-data-platform.html
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced in October 2025. [Delta Lake](../open-source/delta-lake.md) is the main table format, with UniForm for Iceberg and Hudi readers, and data is shared with [Delta Sharing](../open-source/delta-sharing.md). It reads Autonomous AI Database catalogues without copying data and connects to Fusion applications. Its Spark and pipeline features overlap with OCI Data Flow and OCI Data Integration.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management): Expose one copy of table data in several table formats by generating or translating metadata.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR on EKS](../aws/aws-emr-on-eks.md), [Amazon EMR Serverless](../aws/aws-emr-serverless.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Apache Gluten](../open-source/apache-gluten.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
