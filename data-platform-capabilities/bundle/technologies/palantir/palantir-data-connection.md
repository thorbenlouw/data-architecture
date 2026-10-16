---
type: Technology
id: palantir-data-connection
title: Palantir Data Connection
description: Application for configuring sources and running batch, file, streaming and media syncs into Foundry, exports back to external systems, and virtual tables that query external platforms without copying.
aliases: [Foundry Data Connection]
platform: platform-palantir
kind: feature
availability: ga
realises:
- batch-ingestion
- database-extraction
- saas-connectors
- query-federation
- data-export
- hybrid-data-plane
- streaming-ingestion
- change-data-capture
resource: https://www.palantir.com/docs/foundry/data-connection/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

On-premises sources are reached through a Data Connection agent or direct egress. Also supports webhooks, listeners (HTTPS, WebSocket, email), push-based ingestion and change data capture syncs. Virtual tables over platforms such as Databricks, Snowflake and BigQuery let pipelines and the Ontology use external tables in place.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration) (primary): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Data export](../../capabilities/serving/data-export.md) (Serving and activation): Unload query results or tables to files and external systems in bulk.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Fabric Copy job](../microsoft/fabric-copy-job.md), [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Estuary](../independent/estuary.md), [Fivetran](../independent/fivetran.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
