---
type: Technology
id: informatica-cloud-data-integration
title: Informatica Cloud Data Integration (CDI)
description: 'Visual ETL and ELT service: you design mappings from prebuilt transformations and connectors, run them as tasks, and chain tasks into taskflows.'
aliases: [CDI, Data Integration and Engineering]
platform: platform-informatica
kind: managed-service
availability: ga
realises:
- low-code-transformation
- saas-connectors
- database-extraction
- workflow-orchestration
- hybrid-data-plane
resource: https://www.informatica.com/products/cloud-integration/cloud-data-integration.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Mappings run in one of three modes: standard (Secure Agent engine), advanced (Spark-style cluster) or SQL ELT (pushed into the warehouse). Since Spring 2026 data quality rules can run inside CDI data flows. Informatica now markets CDI as "Data Integration and Engineering".

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md), [Coalesce Transform](../independent/coalesce-transform.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
