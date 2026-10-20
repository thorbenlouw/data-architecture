---
type: Technology
id: gcp-data-fusion
title: Cloud Data Fusion
description: Visual, plugin-based integration service built on open-source CDAP for designing batch and real-time pipelines that run on Managed Service for Apache Spark.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [low-code-transformation, saas-connectors, database-extraction, custom-connectors, data-preparation]
resource: https://docs.cloud.google.com/data-fusion/docs/concepts/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still maintained (6.11.x in 2026), with Wrangler for interactive preparation and a plugin SDK. It is less central to Google's roadmap than Dataform, BigQuery pipelines and Datastream, and is priced per instance-hour by edition.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md), [Dataiku connections](../dataiku/dataiku-connections.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md), [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
