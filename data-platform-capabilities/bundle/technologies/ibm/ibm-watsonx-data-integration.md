---
type: Technology
id: ibm-watsonx-data-integration
title: IBM watsonx.data integration
description: Integration product with one control plane for batch ETL and ELT, streaming pipelines, change data replication, unstructured data preparation and pipeline observability, with an agent that builds pipelines from natural language.
formerly: [IBM DataStage]
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- low-code-transformation
- batch-ingestion
- unstructured-ingestion
- data-engineering-agents
- hybrid-data-plane
resource: https://www.ibm.com/products/watsonx-data-integration
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

IBM describes it as formerly IBM DataStage, and DataStage remains the name of its batch engine. Streaming comes from [IBM StreamSets](ibm-streamsets.md), replication from [IBM Data Replication](ibm-data-replication.md) and observability from Databand; streaming on Apache Flink is in preview. Available as SaaS or self-managed, with remote engines that run in the customer's environment. The DataStage parallel engine is widely met in banks and insurers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Data engineering agents](../../capabilities/development-lifecycle/data-engineering-agents.md) (Development and DataOps): Use AI agents that plan, build, test and repair pipelines and models from goals, under platform governance.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx, IBM watsonx.data integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Coalesce Transform](../independent/coalesce-transform.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
