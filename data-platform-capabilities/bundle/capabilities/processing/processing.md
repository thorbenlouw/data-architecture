---
type: Capability
id: processing
title: Processing and transformation
description: Transform, clean, join and aggregate data into forms ready for use.
aliases: [data transformation, data processing]
broader: []
related: [workflow-orchestration, sql-query-engine, data-testing, data-lineage, data-modelling]
depends_on: [compute, storage]
order: 3
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Processing is the work between raw loaded data and something people and systems can use: fixing values, joining sources, applying business rules and aggregating to the level of detail a report or model needs. The capabilities in this domain differ along three lines: how the logic is written (SQL, DataFrame code, visual tools or interactive preparation), where it runs (one machine, a cluster or a stream processor) and how much is recomputed each time (everything, only what changed, or continuously).

Most platforms now load data first and transform it inside the platform, so SQL transformation and transformation as code are the centre of batch analytics. Distributed processing and DataFrame APIs handle jobs too large or too intricate for plain SQL, while single-node engines run the many datasets that fit on one machine at far lower cost. Stream processing, streaming SQL and event-time windowing handle data that never stops arriving.

Incremental processing and declarative pipelines reduce cost and effort by recomputing only what changed and letting the platform plan execution. AI functions, document processing, data enrichment and edge processing extend what transformation can work on, from free text and scanned files to device data before it leaves the site. Orchestration decides when work runs; processing defines what it does.

# Key considerations

- Limit the number of transformation languages and engines. Each extra one adds skills, test tooling and gaps in lineage.
- Decide where business logic lives: in transformation models, in application code or in a semantic layer. Logic copied across layers drifts apart.
- Batch, micro-batch and streaming have very different running costs. Confirm the latency consumers actually need before building continuous processing.
- Make every transformation deterministic and safe to rerun, so retries and backfills give the same result.
- Lineage, tests and documentation should come out of the transformation tooling itself, not be added later by hand.

# Questions to ask

- What latency does each major dataset need: daily, hourly, minutes or seconds?
- Who writes transformations today: data engineers, analytics engineers, analysts or business users?
- How large are the biggest datasets and joins, and how many datasets would fit on a single machine?
- How are transformations tested, reviewed and released at present?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [AI functions in SQL](ai-functions.md), [Data enrichment](data-enrichment.md), [DataFrame APIs](dataframe-apis.md), [Declarative pipelines](declarative-pipelines.md), [Distributed processing](distributed-processing.md), [Document processing](document-processing.md), [Edge data processing](edge-data-processing.md), [Incremental processing](incremental-processing.md), [Low-code transformation](low-code-transformation.md), [Self-service data preparation](data-preparation.md), [Single-node processing](single-node-processing.md), [SQL transformation](sql-transformation.md), [Stream processing](stream-processing.md), [User-defined functions and procedures](user-defined-functions.md) |
| Related | [Query and compute](../compute/compute.md), [Data lineage](../metadata/data-lineage.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [SQL query engine](../compute/sql-query-engine.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Query and compute](../compute/compute.md), [Storage and table management](../storage/storage.md) |

# Where it appears

- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 157 technologies; see their pages.
