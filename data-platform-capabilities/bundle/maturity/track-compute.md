---
type: Maturity Track
id: track-compute
title: Compute and workload management
description: How well compute is provisioned, isolated, scaled and tuned so that workloads meet performance targets at a known cost.
covers:
- compute
- sql-query-engine
- compute-options
- serverless-compute
- provisioned-compute
- gpu-compute
- container-services
- reserved-capacity
- decoupled-storage-compute
- workload-isolation
- elastic-scaling
- workload-management
- query-acceleration
- materialised-views
- result-caching
- data-skipping-indexes
- approximate-query-processing
- native-execution-acceleration
- query-federation
- engine-interoperability
- real-time-analytics
- compute-user-isolation
- interruptible-compute
related_tracks: [track-finops, track-storage, track-platform-migration]
levels:
- level: 1
  name: Initial
  summary: All workloads share whatever compute exists, sized by guesswork and changed through tickets.
  criteria:
  - Batch jobs, ad hoc queries and dashboards run on the same cluster or warehouse, and heavy jobs slow everyone else.
  - Clusters run at a fixed size around the clock whether or not they are in use.
  - Slow queries are investigated only after someone complains.
  capabilities: [sql-query-engine, provisioned-compute]
- level: 2
  name: Managed
  summary: Teams have separate compute for main workload types, with auto-suspend and on-demand options.
  criteria:
  - Separate warehouses, clusters or pools exist at least for batch processing and for interactive use.
  - Compute suspends after a set idle period and resumes on demand.
  - Storage and compute are scaled and paid for separately, so adding data does not mean adding compute.
  - Serverless or on-demand compute is used for spiky or occasional workloads.
  capabilities: [compute-options, serverless-compute, workload-isolation, decoupled-storage-compute]
- level: 3
  name: Defined
  summary: Compute types, sizes and isolation rules are standardised and requested through templates.
  criteria:
  - A written guide says which compute type (serverless, provisioned, GPU or container) suits which workload, and teams request it through templates.
  - Concurrency spikes add clusters or capacity automatically up to a configured ceiling.
  - Queues, priorities and timeouts are configured so interactive and critical work runs before low-priority jobs.
  - Several engines, and queries federated to external databases, work on the same tables through open formats and a shared catalogue instead of private copies.
  - User code on shared compute runs in a sandbox that applies the same access controls as SQL.
  capabilities:
  - elastic-scaling
  - workload-management
  - gpu-compute
  - container-services
  - engine-interoperability
  - query-federation
  - compute-user-isolation
- level: 4
  name: Measured
  summary: Each workload class has a performance target, and acceleration and capacity are managed against it.
  criteria:
  - Each workload class has a performance target, such as dashboard queries under 5 seconds at the 95th percentile, and results are reported.
  - Repeated and selective queries are served by materialised views, result caches or indexes, and hit rates are monitored.
  - Query history with plans, bytes scanned and queue time is kept and used to find the worst regressions each week.
  - Critical workloads that need guaranteed capacity at peak, such as month-end close, run on reserved capacity, and their queue time during those peaks is measured.
  - Application-facing analytics runs on a real-time analytical engine kept separate from batch warehouses and sized from load tests at expected peak concurrency.
  capabilities:
  - query-acceleration
  - materialised-views
  - result-caching
  - data-skipping-indexes
  - reserved-capacity
  - real-time-analytics
- level: 5
  name: Optimising
  summary: Sizing and engine placement are reviewed continuously from benchmarks, trends and forecasts.
  criteria:
  - Warehouse and cluster sizes are adjusted from usage trends, and the effect of each change on cost and latency is recorded.
  - Vectorised native execution is turned on where available, and its effect is measured on representative workloads.
  - Large exploratory aggregates use sampling or sketches where an agreed error margin is acceptable.
  - Workloads are placed on the cheapest engine and capacity type that meets their target, including spot or interruptible capacity for jobs that can restart, using benchmarks rerun when engines change.
  capabilities: [native-execution-acceleration, approximate-query-processing, interruptible-compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means each workload runs on compute sized and isolated for it, scales with demand and has performance targets that are tracked, so a month-end batch no longer slows an operational dashboard and idle clusters no longer run overnight. Common blockers are a single shared cluster for everything, no telemetry linking queries to users and cost, and reluctance to give teams their own compute when nobody can see what it costs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

All workloads share whatever compute exists, sized by guesswork and changed through tickets.

- Batch jobs, ad hoc queries and dashboards run on the same cluster or warehouse, and heavy jobs slow everyone else.
- Clusters run at a fixed size around the clock whether or not they are in use.
- Slow queries are investigated only after someone complains.

**Capabilities first relied on:** [SQL query engine](../capabilities/compute/sql-query-engine.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md)

## Level 2: Managed

Teams have separate compute for main workload types, with auto-suspend and on-demand options.

- Separate warehouses, clusters or pools exist at least for batch processing and for interactive use.
- Compute suspends after a set idle period and resumes on demand.
- Storage and compute are scaled and paid for separately, so adding data does not mean adding compute.
- Serverless or on-demand compute is used for spiky or occasional workloads.

**Capabilities first relied on:** [Compute provisioning options](../capabilities/compute/compute-options.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md)

## Level 3: Defined

Compute types, sizes and isolation rules are standardised and requested through templates.

- A written guide says which compute type (serverless, provisioned, GPU or container) suits which workload, and teams request it through templates.
- Concurrency spikes add clusters or capacity automatically up to a configured ceiling.
- Queues, priorities and timeouts are configured so interactive and critical work runs before low-priority jobs.
- Several engines, and queries federated to external databases, work on the same tables through open formats and a shared catalogue instead of private copies.
- User code on shared compute runs in a sandbox that applies the same access controls as SQL.

**Capabilities first relied on:** [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload management](../capabilities/compute/workload-management.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Container services](../capabilities/compute/container-services.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Query federation](../capabilities/compute/query-federation.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md)

## Level 4: Measured

Each workload class has a performance target, and acceleration and capacity are managed against it.

- Each workload class has a performance target, such as dashboard queries under 5 seconds at the 95th percentile, and results are reported.
- Repeated and selective queries are served by materialised views, result caches or indexes, and hit rates are monitored.
- Query history with plans, bytes scanned and queue time is kept and used to find the worst regressions each week.
- Critical workloads that need guaranteed capacity at peak, such as month-end close, run on reserved capacity, and their queue time during those peaks is measured.
- Application-facing analytics runs on a real-time analytical engine kept separate from batch warehouses and sized from load tests at expected peak concurrency.

**Capabilities first relied on:** [Query acceleration](../capabilities/compute/query-acceleration.md), [Materialised views](../capabilities/compute/materialised-views.md), [Result caching](../capabilities/compute/result-caching.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md)

## Level 5: Optimising

Sizing and engine placement are reviewed continuously from benchmarks, trends and forecasts.

- Warehouse and cluster sizes are adjusted from usage trends, and the effect of each change on cost and latency is recorded.
- Vectorised native execution is turned on where available, and its effect is measured on representative workloads.
- Large exploratory aggregates use sampling or sketches where an agreed error margin is acceptable.
- Workloads are placed on the cheapest engine and capacity type that meets their target, including spot or interruptible capacity for jobs that can restart, using benchmarks rerun when engines change.

**Capabilities first relied on:** [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md)

# Capabilities in scope

[Query and compute](../capabilities/compute/compute.md), [Approximate query processing](../capabilities/compute/approximate-query-processing.md), [Compute provisioning options](../capabilities/compute/compute-options.md), [Container services](../capabilities/compute/container-services.md), [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [GPU and accelerated compute](../capabilities/compute/gpu-compute.md), [Indexes and data skipping](../capabilities/compute/data-skipping-indexes.md), [Materialised views](../capabilities/compute/materialised-views.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Provisioned compute](../capabilities/compute/provisioned-compute.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Query federation](../capabilities/compute/query-federation.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Result caching](../capabilities/compute/result-caching.md), [Serverless compute](../capabilities/compute/serverless-compute.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Vectorised native execution](../capabilities/compute/native-execution-acceleration.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Workload management](../capabilities/compute/workload-management.md)

# Related tracks

- [FinOps](track-finops.md): How well the organisation understands, allocates and controls what the data platform costs, relative to the value it delivers.
- [Storage and table management](track-storage.md): How well data is kept in durable, open, maintained tables that many engines can read, update and trust.
- [Platform migration and portability](track-platform-migration.md): How safely and predictably the organisation moves workloads, code and data to new platforms, and how freely it can choose where the platform runs.

Levels follow the shared [maturity scale](maturity-scale.md).
