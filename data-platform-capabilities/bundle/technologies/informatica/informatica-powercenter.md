---
type: Technology
id: informatica-powercenter
title: Informatica PowerCenter
description: On-premises enterprise ETL server with a client designer, repository and workflow engine, and the historical core of Informatica's integration business.
platform: platform-informatica
kind: software
availability: ga
realises: [low-code-transformation, batch-ingestion, workflow-orchestration]
resource: https://www.informatica.com/ca/lp/powercenter-modernization.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still very common in large estates. Standard support for PowerCenter 10.5.x ended on 31 March 2026, and extended support runs to 31 March 2027. Informatica's route forward is [PowerCenter Cloud Edition](informatica-powercenter-cloud-edition.md) and conversion to [Cloud Data Integration](informatica-cloud-data-integration.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** PowerCenter

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
