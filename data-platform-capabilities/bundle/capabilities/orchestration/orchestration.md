---
type: Capability
id: orchestration
title: Orchestration
description: Schedule, sequence and coordinate the jobs that move and transform data.
broader: []
related: [declarative-pipelines, transformation-as-code, ci-cd, table-lineage]
depends_on: [secrets-management]
order: 4
tags: [orchestration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Orchestration decides when each piece of data work runs, in what order, and what happens when it fails. A pipeline is a set of tasks, such as extract, load, transform, test and publish, with dependencies between them. The orchestrator starts each task when its inputs are ready, passes parameters such as the period being processed, retries failures, records every run and alerts owners when something breaks or runs late. It usually does no data processing itself; it tells engines and tools what to do.

The four capabilities differ in what starts the work. Workflow orchestration runs dependency graphs of tasks on schedules. Event-driven triggering starts work when something happens, such as a file landing or a table changing. Data-aware orchestration turns the view around: it describes the datasets to be produced and how fresh they must be, and works out what must run. Backfill and reprocessing reruns pipelines over past periods to correct or rebuild data, which works only if tasks are parameterised by time and safe to rerun.

Orchestration touches most of the platform. It holds credentials for the systems it calls, produces run history that feeds pipeline monitoring and lineage, and encodes dependencies that cross team boundaries. Many tools now schedule themselves, including declarative pipelines, transformation tools and SaaS connectors, so the design question is often which scheduler owns which dependency and how work in one tool starts work in another.

# Key considerations

- Decide whether one orchestrator coordinates everything or each tool schedules itself. Several unconnected schedulers turn cross-tool dependencies into guesses about timing.
- Keep orchestration code separate from processing logic, so tasks can be tested and rerun without the scheduler.
- Keep pipeline definitions in version control, with review and automated deployment.
- Plan for the orchestrator itself failing. Know what happens to running tasks and missed schedules when it restarts.

# Questions to ask

- How many pipelines exist, and how many dependencies cross team or tool boundaries?
- How are failures noticed today, and how long does recovery usually take?
- Do consumers care about runs finishing at set times, or about specific data being fresh?
- How often is historical data reprocessed, and how is it done now?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Backfill and reprocessing](backfill-replay.md), [Data-aware orchestration](asset-based-orchestration.md), [Event-driven triggering](event-driven-triggering.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Workflow orchestration](workflow-orchestration.md) |
| Related | [CI/CD](../development-lifecycle/ci-cd.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Table-level lineage](../metadata/table-lineage.md), [Transformation as code](../processing/transformation-as-code.md) |
| Depends on | [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Maturity tracks:** [Orchestration](../../maturity/track-orchestration.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 53 technologies; see their pages.
