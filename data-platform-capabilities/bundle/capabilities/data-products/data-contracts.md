---
type: Capability
id: data-contracts
title: Data contracts
description: Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
broader: [data-products]
related: [schema-registry, schema-evolution, data-quality-rules, data-testing, impact-analysis]
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A contract file lists what consumers of a dataset can rely on: column names and types, the meaning of each field, allowed values, quality rules, freshness, and the process for changing any of these. The producer's pipeline checks the contract on every change and every run. If a developer drops a column or changes a type, CI fails before deployment; if a run produces values that break the agreed rules, the output is blocked or flagged.

Contracts matter where data crosses a team boundary, especially from application teams whose database changes would otherwise break analytics without warning. They move detection to the producer, before damage spreads. The Open Data Contract Standard from the Bitol project is a common open format. A contract differs from quality rules, which may be private checks: it is a published promise with an owner and a change process. It also goes beyond a schema registry, which enforces compatibility of event schemas but rarely covers meaning or service levels.

# Key considerations

- Enforcement is what makes a contract more than documentation. Check it in the producer's CI and at run time, not only in the consumer's pipeline.
- Agree a change process: how breaking changes are announced, how long old versions are supported, and who must approve.
- Start at the boundaries that break most often, usually between operational application teams and the data platform.
- Contracts need producer agreement. Imposing them from the consumer side alone rarely holds.

# Questions to ask

- How often do upstream changes break downstream pipelines or reports without warning?
- Do source application teams accept responsibility for the data they emit?
- Which datasets cross team or organisational boundaries?
- Where would contract checks run: in source CI, in pipelines, or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md) |
| Related | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Serving and activation](../serving/serving.md), [Data quality and observability](../data-quality/data-quality.md), [Development and DataOps](../development-lifecycle/development-lifecycle.md), [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Data certification](../metadata/data-certification.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data product lifecycle management](data-product-lifecycle.md), [Data quality rules](../data-quality/data-quality-rules.md), [Data service levels](data-slas.md), [Event and API catalogue](../metadata/event-api-catalogue.md), [Impact analysis](../metadata/impact-analysis.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Reverse ETL](../serving/reverse-etl.md), [Schema change management](../development-lifecycle/schema-change-management.md), [Schema enforcement and evolution](../storage/schema-evolution.md), [Schema registry](../metadata/schema-registry.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 3) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md) · [Shift-left data quality and governance](../../patterns/shift-left.md) · [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data architect](../../personas/persona-data-architect.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 8 Data Consumption Purpose (Accessibility and usage) · [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product; Federated computational governance · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter IV – Unfair contractual terms; Chapter VIII – Interoperability · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-51 – Exchange of data policy statements; ISO 8000-100 and 8000-110 – Master data exchange and conformance to data specification · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Fundamentals; Schema; References; Data Quality · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Product Information (input and output ports)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | data product contract | [Knowledge Catalog data products](../../technologies/google-cloud/gcp-knowledge-catalog-data-products.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md), [IBM Data Product Hub](../../technologies/ibm/ibm-data-product-hub.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Data Contract CLI](../../technologies/open-source/data-contract-cli.md), [Open Data Contract Standard (ODCS)](../../technologies/open-source/open-data-contract-standard.md), [OpenMetadata](../../technologies/open-source/openmetadata.md), [Soda Core](../../technologies/open-source/soda-core.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt platform](../../technologies/independent/dbt-platform.md), [Soda Cloud](../../technologies/independent/soda-cloud.md), [Twilio Segment](../../technologies/independent/twilio-segment.md) |
