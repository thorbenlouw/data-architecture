---
type: Maturity Track
id: track-orchestration
title: Orchestration
description: How dependably the organisation schedules, sequences and recovers the jobs that move and transform data.
covers:
- orchestration
- workflow-orchestration
- event-driven-triggering
- asset-based-orchestration
- backfill-replay
related_tracks: [track-ingestion, track-transformation, track-platform-self-service]
levels:
- level: 1
  name: Initial
  summary: Jobs run from cron, tool-specific schedulers or by hand, with time gaps standing in for dependencies.
  criteria:
  - A job is scheduled an hour after the one it depends on, with no check that the first has finished.
  - Schedules are spread across server crontabs, database agents and the schedulers built into individual tools.
  - A failure is discovered when a consumer reports missing data.
  - Rerunning a past day means editing dates in scripts by hand.
  capabilities: []
- level: 2
  name: Managed
  summary: Each team defines pipelines as dependency graphs in an orchestrator, with retries and alerts.
  criteria:
  - Pipelines are defined in code as graphs of tasks with explicit upstream dependencies.
  - Tasks retry automatically up to a configured limit, and final failures alert the owning team's channel.
  - Logs, durations and outcomes of every task run are kept and searchable for at least 30 days.
  - Run dates are passed into tasks as parameters, so a single run can be repeated for a chosen date.
  capabilities: [workflow-orchestration]
- level: 3
  name: Defined
  summary: One orchestration standard covers the platform, including event triggers, cross-team dependencies and backfills.
  criteria:
  - All production pipelines run on the shared orchestration service or an approved list, and server crontabs for data jobs have been retired.
  - Pipelines start on file arrival, table updates or messages, configured in the same tool as scheduled runs.
  - A dependency on another team's work is declared against their published dataset or task, not inferred from timing.
  - Backfills for a date range follow a documented, parameterised procedure with no code changes, and pipelines are written to be safe to rerun.
  - Pipeline definitions are deployed from version control through CI, and none are edited directly in production.
  capabilities: [event-driven-triggering, backfill-replay]
- level: 4
  name: Measured
  summary: Scheduling is driven by the freshness of data assets, and delivery is measured against targets.
  criteria:
  - Key datasets declare a freshness target, and the orchestrator runs upstream work to meet it instead of at fixed times.
  - On-time delivery for each critical pipeline is reported weekly against its target.
  - Failure alerts are routed by ownership metadata to the responsible team, and time to recover is tracked.
  - Backfills run in isolated, throttled capacity, and run-time monitoring shows they do not delay daily production runs.
  capabilities: [asset-based-orchestration]
- level: 5
  name: Optimising
  summary: The dependency graph and failure history are analysed regularly to shorten critical paths and prevent repeat failures.
  criteria:
  - The longest chains in the dependency graph are identified regularly and shortened by splitting or parallelising tasks.
  - Run-time trends predict deadline breaches and trigger alerts or extra capacity before the deadline passes.
  - Retry limits and timeouts are tuned per task from failure history, so transient failures recover without paging anyone and persistent ones fail fast.
  - Low-priority pipelines move to off-peak windows automatically, based on measured cluster load and cost.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means jobs start when their inputs are ready rather than at hopeful fixed times, failures are retried and routed to the right owner, and historical periods can be rebuilt safely. That reduces late reports and overnight firefighting. Typical blockers are cron jobs spread across servers and tools, hidden dependencies between teams' pipelines, and pipelines that are not safe to rerun, which turns every backfill into a manual project.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Jobs run from cron, tool-specific schedulers or by hand, with time gaps standing in for dependencies.

- A job is scheduled an hour after the one it depends on, with no check that the first has finished.
- Schedules are spread across server crontabs, database agents and the schedulers built into individual tools.
- A failure is discovered when a consumer reports missing data.
- Rerunning a past day means editing dates in scripts by hand.

## Level 2: Managed

Each team defines pipelines as dependency graphs in an orchestrator, with retries and alerts.

- Pipelines are defined in code as graphs of tasks with explicit upstream dependencies.
- Tasks retry automatically up to a configured limit, and final failures alert the owning team's channel.
- Logs, durations and outcomes of every task run are kept and searchable for at least 30 days.
- Run dates are passed into tasks as parameters, so a single run can be repeated for a chosen date.

**Capabilities first relied on:** [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md)

## Level 3: Defined

One orchestration standard covers the platform, including event triggers, cross-team dependencies and backfills.

- All production pipelines run on the shared orchestration service or an approved list, and server crontabs for data jobs have been retired.
- Pipelines start on file arrival, table updates or messages, configured in the same tool as scheduled runs.
- A dependency on another team's work is declared against their published dataset or task, not inferred from timing.
- Backfills for a date range follow a documented, parameterised procedure with no code changes, and pipelines are written to be safe to rerun.
- Pipeline definitions are deployed from version control through CI, and none are edited directly in production.

**Capabilities first relied on:** [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md), [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md)

## Level 4: Measured

Scheduling is driven by the freshness of data assets, and delivery is measured against targets.

- Key datasets declare a freshness target, and the orchestrator runs upstream work to meet it instead of at fixed times.
- On-time delivery for each critical pipeline is reported weekly against its target.
- Failure alerts are routed by ownership metadata to the responsible team, and time to recover is tracked.
- Backfills run in isolated, throttled capacity, and run-time monitoring shows they do not delay daily production runs.

**Capabilities first relied on:** [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md)

## Level 5: Optimising

The dependency graph and failure history are analysed regularly to shorten critical paths and prevent repeat failures.

- The longest chains in the dependency graph are identified regularly and shortened by splitting or parallelising tasks.
- Run-time trends predict deadline breaches and trigger alerts or extra capacity before the deadline passes.
- Retry limits and timeouts are tuned per task from failure history, so transient failures recover without paging anyone and persistent ones fail fast.
- Low-priority pipelines move to off-peak windows automatically, based on measured cluster load and cost.

# Capabilities in scope

[Orchestration](../capabilities/orchestration/orchestration.md), [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md)

# Related tracks

- [Ingestion and integration](track-ingestion.md): How reliably, quickly and safely the organisation brings data from source systems into the platform and keeps it in step with them.
- [Transformation engineering](track-transformation.md): How consistently transformation logic is written, tested, reused and run efficiently, from raw data to tables ready for use.
- [Platform self-service](track-platform-self-service.md): How far teams can obtain, run and observe what they need on the shared platform without waiting for a central team.

Levels follow the shared [maturity scale](maturity-scale.md).
