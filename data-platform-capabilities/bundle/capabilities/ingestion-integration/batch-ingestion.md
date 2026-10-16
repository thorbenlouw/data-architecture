---
type: Capability
id: batch-ingestion
title: Batch ingestion
description: Load data from sources on a schedule or on demand, in bulk or incrementally.
broader: [ingestion-integration]
related: [incremental-processing, idempotent-loading, change-data-capture, data-reconciliation]
depends_on: [workflow-orchestration]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A batch job connects to a source at set times or when triggered, reads a bounded set of records and writes them to the platform as one unit. A nightly job might read yesterday's orders from a database, the latest export from an SFTP folder and new contacts from a CRM, landing each in a raw table. Loads are either full, re-reading everything each run, or incremental, reading only records changed since a stored high-water mark such as a last-modified timestamp or sequence number.

Batch remains the default for most analytical data because it is cheap and easy to reason about: a run either succeeded or it did not. Its limits are latency, which is bounded by the schedule, and timestamp-based increments, which miss hard deletes and rows whose timestamps are not updated. Where those limits matter, change data capture or streaming ingestion is the alternative. The child capabilities cover particular source types.

# Key considerations

- Full loads are simple and catch deletes, but their cost grows with table size. Move to incremental loads once a full load no longer fits its window.
- Store the high-water mark with the data it produced, not only in job state, so a failed run resumes from the right point.
- Use overlapping extraction windows and deduplicate on write, because source timestamps are often set late or by servers with skewed clocks.
- Schedule extracts away from source peak hours, or read from replicas, so operational systems are not slowed.

# Questions to ask

- What is the longest acceptable delay between a change in a source and its arrival in the platform?
- Do sources expose reliable change timestamps or sequence numbers, and do they hard-delete records?
- How large are the biggest tables, and how long do full extracts take today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Narrower | [API ingestion](api-ingestion.md), [Bulk and offline transfer](bulk-data-transfer.md), [Database extraction](database-extraction.md), [File ingestion](file-ingestion.md), [SaaS application connectors](saas-connectors.md) |
| Related | [Change data capture](change-data-capture.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Deduplication and idempotent loading](idempotent-loading.md), [Incremental processing](../processing/incremental-processing.md) |
| Depends on | [Workflow orchestration](../orchestration/workflow-orchestration.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3)
- **Patterns:** [Data warehouse](../../patterns/data-warehouse.md) · [ETL](../../patterns/etl.md) · [Lambda architecture](../../patterns/lambda-architecture.md) · [Medallion architecture](../../patterns/medallion-architecture.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Copy job / Copy activity | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Fabric Copy job](../../technologies/microsoft/fabric-copy-job.md), [Pipelines in Fabric Data Factory](../../technologies/microsoft/fabric-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Storage Write API](../../technologies/google-cloud/gcp-bigquery-storage-write-api.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake bulk loading (COPY INTO <table>)](../../technologies/snowflake/snowflake-copy-into.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica PowerCenter](../../technologies/informatica/informatica-powercenter.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Integration](../../technologies/oracle/oracle-oci-data-integration.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data integration](../../technologies/ibm/ibm-watsonx-data-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |

Narrower capabilities are realised by a further 57 technologies; see their pages.
