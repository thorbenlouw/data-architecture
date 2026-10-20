---
type: Technology
id: gcp-dataflow-templates
title: Dataflow templates
description: Google-provided and custom Flex templates, plus the visual job builder, for running common ingestion and transformation pipelines without writing Beam code.
aliases: [Dataflow job builder]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [low-code-transformation, database-extraction, streaming-ingestion]
resource: https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Common templates cover Pub/Sub to BigQuery, JDBC to BigQuery, Spanner change streams, Kafka and Cloud Storage loads; the job builder builds pipelines in the console and exports them as YAML.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Dataflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Coalesce Transform](../independent/coalesce-transform.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
