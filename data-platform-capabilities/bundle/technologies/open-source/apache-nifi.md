---
type: Technology
id: apache-nifi
title: Apache NiFi
description: Visual dataflow tool for routing, transforming and delivering data between systems, with back-pressure and record-level data provenance.
aliases: [NiFi]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- low-code-transformation
- file-ingestion
- api-ingestion
- managed-file-transfer
- unstructured-ingestion
- data-enrichment
- edge-data-processing
resource: https://nifi.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. NiFi 2.x requires Java 21 and supports processors written in Python. Snowflake acquired Datavolo (founded by NiFi's creators) in 2024 and builds Snowflake Openflow on NiFi.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.
- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
- [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) (Ingestion and integration): Bring documents, images, audio and other unstructured content into the platform together with their metadata.
- [Data enrichment](../../capabilities/processing/data-enrichment.md) (Processing and transformation): Add attributes to records from lookup tables or curated third-party reference data.
- [Edge data processing](../../capabilities/processing/edge-data-processing.md) (Processing and transformation): Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md), [Edge data processing](../../capabilities/processing/edge-data-processing.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Unstructured data ingestion](../../capabilities/ingestion-integration/unstructured-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Coalesce Transform](../independent/coalesce-transform.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
