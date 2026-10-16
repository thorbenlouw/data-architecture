---
type: Maturity Track
id: track-transformation
title: Transformation engineering
description: How consistently transformation logic is written, tested, reused and run efficiently, from raw data to tables ready for use.
covers:
- processing
- sql-transformation
- transformation-as-code
- low-code-transformation
- data-preparation
- distributed-processing
- single-node-processing
- dataframe-apis
- user-defined-functions
- stream-processing
- streaming-sql
- event-time-windowing
- incremental-processing
- declarative-pipelines
- ai-functions
- document-processing
- data-enrichment
- edge-data-processing
related_tracks: [track-ingestion, track-orchestration, track-path-to-live, track-real-time]
levels:
- level: 1
  name: Initial
  summary: Transformations are written ad hoc in scripts, stored procedures, notebooks or spreadsheets by whoever needs the output.
  criteria:
  - The same business rule, such as what counts as an active customer, is coded differently in several scripts or reports.
  - Transformation code lives in database objects or notebooks that are not under version control.
  - Every run rebuilds its tables in full, however little source data changed.
  - Analysts reshape extracts in spreadsheets or desktop tools outside the platform.
  capabilities: [sql-transformation, single-node-processing, user-defined-functions]
- level: 2
  name: Managed
  summary: A team builds transformations in one framework with version control and some automated tests.
  criteria:
  - Logic for the team's main tables has been moved out of stored procedures and notebooks into a Git repository, and each change is reviewed before it is deployed.
  - The tool resolves run order from references between models instead of hand-ordered scripts.
  - Jobs too large for one machine run on a distributed engine through SQL or DataFrame APIs.
  - Important models have tests for keys, nulls and accepted values that run on every build.
  - Visual integration flows, where used, are stored centrally and exported for review.
  capabilities: [transformation-as-code, distributed-processing, dataframe-apis, low-code-transformation]
- level: 3
  name: Defined
  summary: Transformation follows platform-wide layering, naming and incremental-processing conventions that every team uses.
  criteria:
  - A written layering convention, such as raw, cleaned and business-ready, with naming rules, is applied to every new model and enforced in review.
  - Large tables update incrementally through merge or append logic keyed on change markers, and full rebuilds are a deliberate, scheduled choice.
  - Teams can declare target tables and their logic and let the platform work out run order, retries and refresh.
  - Shared lookups for enrichment are maintained once and joined by key, not copied into each pipeline.
  - Analysts prepare data in a governed self-service tool whose outputs land in the platform with lineage, not as local files.
  capabilities:
  - incremental-processing
  - declarative-pipelines
  - data-enrichment
  - data-preparation
  - stream-processing
  - streaming-sql
  - event-time-windowing
- level: 4
  name: Measured
  summary: Every production transformation has tests, run-time and cost baselines, and alerts when it drifts from them.
  criteria:
  - Each production model has an owner, a run-time and cost baseline, and an alert when a run exceeds the baseline by a set margin.
  - Pull requests are tested against production-like data, comparing row counts and key aggregates before and after the change.
  - The share of models with tests and descriptions is reported against a target.
  - Pipelines that extract fields from documents or call language models from SQL report extraction accuracy on a labelled sample, call volume and cost.
  capabilities: [document-processing, ai-functions]
- level: 5
  name: Optimising
  summary: Transformation code and engine choices are reworked continuously from run statistics and usage.
  criteria:
  - The slowest and most expensive models are reviewed monthly from run statistics, and refactoring is planned from that list.
  - Business rules that appear in several models are found by code analysis and consolidated into shared models or macros.
  - Each workload's engine (single-node, distributed or streaming) is reviewed against cost and latency, and workloads move when another is cheaper.
  - Logic that runs on devices or at sites is versioned and deployed from the same repositories as central pipelines.
  capabilities: [edge-data-processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up replaces opaque stored procedures, spreadsheet logic and copied SQL with modular, version-controlled transformations that are tested, documented from the code and recompute only what changed. That shortens the time to change a business rule safely and lowers the compute bill. Progress is usually blocked by legacy logic nobody fully understands, analysts and engineers working in separate tools with no shared conventions, and pressure to deliver new tables instead of refactoring old ones.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Transformations are written ad hoc in scripts, stored procedures, notebooks or spreadsheets by whoever needs the output.

- The same business rule, such as what counts as an active customer, is coded differently in several scripts or reports.
- Transformation code lives in database objects or notebooks that are not under version control.
- Every run rebuilds its tables in full, however little source data changed.
- Analysts reshape extracts in spreadsheets or desktop tools outside the platform.

**Capabilities first relied on:** [SQL transformation](../capabilities/processing/sql-transformation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md)

## Level 2: Managed

A team builds transformations in one framework with version control and some automated tests.

- Logic for the team's main tables has been moved out of stored procedures and notebooks into a Git repository, and each change is reviewed before it is deployed.
- The tool resolves run order from references between models instead of hand-ordered scripts.
- Jobs too large for one machine run on a distributed engine through SQL or DataFrame APIs.
- Important models have tests for keys, nulls and accepted values that run on every build.
- Visual integration flows, where used, are stored centrally and exported for review.

**Capabilities first relied on:** [Transformation as code](../capabilities/processing/transformation-as-code.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Low-code transformation](../capabilities/processing/low-code-transformation.md)

## Level 3: Defined

Transformation follows platform-wide layering, naming and incremental-processing conventions that every team uses.

- A written layering convention, such as raw, cleaned and business-ready, with naming rules, is applied to every new model and enforced in review.
- Large tables update incrementally through merge or append logic keyed on change markers, and full rebuilds are a deliberate, scheduled choice.
- Teams can declare target tables and their logic and let the platform work out run order, retries and refresh.
- Shared lookups for enrichment are maintained once and joined by key, not copied into each pipeline.
- Analysts prepare data in a governed self-service tool whose outputs land in the platform with lineage, not as local files.

**Capabilities first relied on:** [Incremental processing](../capabilities/processing/incremental-processing.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Stream processing](../capabilities/processing/stream-processing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md)

## Level 4: Measured

Every production transformation has tests, run-time and cost baselines, and alerts when it drifts from them.

- Each production model has an owner, a run-time and cost baseline, and an alert when a run exceeds the baseline by a set margin.
- Pull requests are tested against production-like data, comparing row counts and key aggregates before and after the change.
- The share of models with tests and descriptions is reported against a target.
- Pipelines that extract fields from documents or call language models from SQL report extraction accuracy on a labelled sample, call volume and cost.

**Capabilities first relied on:** [Document processing](../capabilities/processing/document-processing.md), [AI functions in SQL](../capabilities/processing/ai-functions.md)

## Level 5: Optimising

Transformation code and engine choices are reworked continuously from run statistics and usage.

- The slowest and most expensive models are reviewed monthly from run statistics, and refactoring is planned from that list.
- Business rules that appear in several models are found by code analysis and consolidated into shared models or macros.
- Each workload's engine (single-node, distributed or streaming) is reviewed against cost and latency, and workloads move when another is cheaper.
- Logic that runs on devices or at sites is versioned and deployed from the same repositories as central pipelines.

**Capabilities first relied on:** [Edge data processing](../capabilities/processing/edge-data-processing.md)

# Capabilities in scope

[Processing and transformation](../capabilities/processing/processing.md), [AI functions in SQL](../capabilities/processing/ai-functions.md), [Data enrichment](../capabilities/processing/data-enrichment.md), [DataFrame APIs](../capabilities/processing/dataframe-apis.md), [Declarative pipelines](../capabilities/processing/declarative-pipelines.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [Document processing](../capabilities/processing/document-processing.md), [Edge data processing](../capabilities/processing/edge-data-processing.md), [Event-time windowing](../capabilities/processing/event-time-windowing.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Low-code transformation](../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../capabilities/processing/data-preparation.md), [Single-node processing](../capabilities/processing/single-node-processing.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Stream processing](../capabilities/processing/stream-processing.md), [Streaming SQL](../capabilities/processing/streaming-sql.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [User-defined functions and procedures](../capabilities/processing/user-defined-functions.md)

# Related tracks

- [Ingestion and integration](track-ingestion.md): How reliably, quickly and safely the organisation brings data from source systems into the platform and keeps it in step with them.
- [Orchestration](track-orchestration.md): How dependably the organisation schedules, sequences and recovers the jobs that move and transform data.
- [Path to live](track-path-to-live.md): How safely, quickly and repeatably changes to data and AI workloads move from a developer's first commit to production.
- [Real-time and streaming](track-real-time.md): How well the organisation moves, processes and queries data continuously, with predictable latency and correct results, instead of in scheduled batches.

Levels follow the shared [maturity scale](maturity-scale.md).
