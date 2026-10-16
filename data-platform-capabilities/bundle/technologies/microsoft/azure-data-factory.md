---
type: Technology
id: azure-data-factory
title: Azure Data Factory
description: Managed data integration service for copy activities, mapping data flows on Spark and orchestrated pipelines across cloud and on-premises sources.
aliases: [ADF]
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- batch-ingestion
- workflow-orchestration
- low-code-transformation
- saas-connectors
- database-extraction
- hybrid-data-plane
resource: https://learn.microsoft.com/en-us/azure/data-factory/introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still supported, but Microsoft calls Fabric Data Factory its next generation and recommends Fabric for new work; existing factories can be mounted in Fabric. Self-hosted integration runtime reaches private sources.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration) (primary): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
