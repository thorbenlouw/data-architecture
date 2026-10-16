---
type: Pattern
id: medallion-architecture
title: Medallion architecture
description: Organise data in layers of increasing refinement, typically bronze (raw), silver (cleaned) and gold (business-ready).
aliases:
- multi-hop architecture
- bronze silver gold
- bronze silver gold layers
- bronze, silver and gold
- medallion layers
uses:
- batch-ingestion
- open-table-formats
- incremental-processing
- sql-transformation
- declarative-pipelines
- data-quality-rules
- data-certification
- data-lineage
- backfill-replay
related: [lakehouse, data-lake, elt, write-audit-publish]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The bronze layer keeps source data as received, usually append-only, so anything downstream can be rebuilt from it. Silver holds cleaned, deduplicated and conformed records, typically one table per business entity with consistent types and keys. Gold holds aggregates, dimensional models or feature tables shaped for particular uses. Each hop is a pipeline that reads only from the layer below. The bronze, silver and gold names were popularised by Databricks, but the idea is older: warehouses have long used landing, staging and presentation areas.

The pattern gives teams a shared vocabulary for where data sits and how far it can be trusted, and it makes reprocessing simple because raw data is kept. It says nothing about how to model each layer, so it is often combined with Data Vault in silver or dimensional models in gold. Some teams add a landing zone before bronze or split gold by domain. The number of layers matters less than agreeing what each one guarantees, who owns it and who may read it.

# When to use

- You ingest many sources into a lake or lakehouse and need a consistent way to separate raw, cleaned and consumable data.
- You must be able to rebuild downstream tables from retained raw data after a logic change or incident.
- Several teams share the platform and need a common convention for trust levels and ownership.

# Watch out for

- Layers are a naming convention, not a design; without quality rules and owners per layer, silver and gold drift.
- Copying whole tables at every hop multiplies storage and compute; process incrementally where you can.
- Strict layering can force simple use cases through unnecessary hops and add latency.
- Bronze holds personal data in raw form, so retention, erasure and access controls must reach it too.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Open table formats](../capabilities/storage/open-table-formats.md): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [Incremental processing](../capabilities/processing/incremental-processing.md): Process only new or changed data instead of recomputing everything each run.
- [SQL transformation](../capabilities/processing/sql-transformation.md): Transform data inside the platform using SQL, typically after it has been loaded.
- [Declarative pipelines](../capabilities/processing/declarative-pipelines.md): Declare target tables and their logic, and let the platform work out execution order, incremental refresh and retries.
- [Data quality rules](../capabilities/data-quality/data-quality-rules.md): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data certification](../capabilities/metadata/data-certification.md): Mark assets as trusted, deprecated or under review so consumers know what to rely on.
- [Data lineage](../capabilities/metadata/data-lineage.md): Track where data comes from, how it is transformed and where it goes.
- [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md): Rerun pipelines over historical periods or replay events to correct or rebuild data.

# Related patterns

- [Lakehouse](lakehouse.md)
- [Data lake](data-lake.md)
- [ELT](elt.md)
- [Write-audit-publish](write-audit-publish.md)
- [Data Vault](data-vault.md)
- [Metadata-driven pipelines](metadata-driven-pipelines.md)

# Where it appears

- **Use cases:** [Churn prediction](../use-cases/usecase-churn-prediction.md) · [Customer 360](../use-cases/usecase-customer-360.md) · [Demand forecasting](../use-cases/usecase-demand-forecasting.md) · [Document data extraction](../use-cases/usecase-document-extraction.md) · [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) · [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) · [Marketing audience activation](../use-cases/usecase-marketing-activation.md) · [Operational reporting](../use-cases/usecase-operational-reporting.md) · [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) · [Self-service BI](../use-cases/usecase-self-service-bi.md)
- **Personas:** [Analytics engineer](../personas/persona-analytics-engineer.md) · [Data architect](../personas/persona-data-architect.md) · [Data engineer](../personas/persona-data-engineer.md)
