---
type: Capability
id: operational-data-store
title: Operational data store
description: Hold a current, integrated view of data from several operational systems for operational reporting and lookups.
aliases: [ODS, operational data hub, operational reporting store]
broader: [serving]
related:
- operational-database
- read-optimised-views
- change-data-capture
- master-data-management
- entity-resolution
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An operational data store (ODS) combines current records from several operational systems, refreshed often or continuously, for day-to-day use. A contact centre might use an ODS that joins a customer's latest orders from the order system, open cases from the service system and payment status from billing, so agents see one current view without querying three systems. Unlike a data warehouse, it holds mostly current values rather than full history and is shaped for lookups and short queries rather than large scans.

It suits operational reporting and cross-system lookups that need data minutes old, where source systems cannot take the query load or lack each other's data. The pattern predates the lakehouse but the need remains: many platforms now build it as frequently refreshed integrated tables, or as a separate database fed by change data capture. Master data management differs in resolving and governing golden records; low-latency serving differs in targeting very high request rates rather than integration.

# Key considerations

- Decide whether the ODS keeps any history. Users often ask what a value was yesterday once the store exists.
- Agree and document the rules for matching records across systems, such as customers, with the source owners.
- Feeding it by change data capture keeps it current but makes it depend on every source's capture working.
- Do not let it become a second system of record. Corrections should go back to the operational sources, not into the ODS.

# Questions to ask

- Which operational decisions need a current view across several systems?
- How current must it be, and how much history do users need?
- Which systems will feed it, and how will records be matched across them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Change data capture](../ingestion-integration/change-data-capture.md), [Entity resolution](../master-data/entity-resolution.md), [Low-latency serving](low-latency-serving.md), [Master data management](../master-data/master-data-management.md), [Operational database integration](operational-database.md), [Read-optimised views](read-optimised-views.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake hybrid tables (Unistore)](../../technologies/snowflake/snowflake-hybrid-tables.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Operational Database](../../technologies/cloudera/cloudera-operational-database.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [PostgreSQL](../../technologies/open-source/postgresql.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [K2view Data Product Platform](../../technologies/independent/k2view-data-product-platform.md), [Materialize](../../technologies/independent/materialize.md) |
