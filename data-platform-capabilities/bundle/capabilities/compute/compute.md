---
type: Capability
id: compute
title: Query and compute
description: Provide the query engines and processing power that run workloads, sized and isolated appropriately.
broader: []
related: [storage, processing, cost-management, query-performance-analysis, platform-observability]
order: 5
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This domain covers the engines that run queries and jobs and the way processing capacity is supplied to them. At its centre is the SQL query engine, which plans and runs analytical SQL in parallel. Beside it sit engines for other shapes of work: real-time analytical databases that answer in milliseconds, GPUs for training and inference, and container services for custom applications. Query federation and multi-engine interoperability decide whether an engine must hold its own data or can work on data kept elsewhere.

Provisioning options describe how capacity arrives: serverless capacity billed per use, clusters you size, or capacity reserved in advance. Decoupling storage from compute lets several clusters work on one copy of the data, which makes workload isolation and elastic scaling practical: each team or workload gets compute that grows and shrinks with its own demand. Workload management works inside a shared pool, ranking and limiting queries so the most important ones meet their service levels.

Query acceleration cuts the work each query does, through materialised views, result caches, indexes and data skipping, approximation and vectorised native execution. Compute is usually the largest part of a data platform's cost, so these choices drive both performance and the bill. Architects usually settle isolation boundaries first, then the provisioning model for each workload, then where acceleration pays for itself.

# Key considerations

- Tie every cluster, warehouse and serverless budget to an owner and a workload, so the largest cost line can be explained and controlled.
- Separate workloads with different latency and cost profiles, such as dashboards, batch transformation and data science, before tuning any of them.
- Serverless removes capacity planning but makes cost follow query behaviour. Put limits on runaway queries before opening access widely.
- Several engines on the same data add flexibility but multiply security, tuning and support effort. Add an engine for a clear workload reason, not preference.
- Acceleration features cost storage and refresh compute. Weigh what they save on the queries they serve against what they cost to maintain.

# Questions to ask

- What are the main workload types, and what latency and concurrency does each need?
- How predictable is demand across the day, the month and the year?
- Which teams need guaranteed capacity, and which can wait in a queue?
- How is compute cost attributed to teams and controlled today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Compute provisioning options](compute-options.md), [Decoupled storage and compute](decoupled-storage-compute.md), [Elastic scaling](elastic-scaling.md), [Multi-engine interoperability](engine-interoperability.md), [Query acceleration](query-acceleration.md), [Query federation](query-federation.md), [Real-time analytical database](real-time-analytics.md), [Shared compute isolation](../security/compute-user-isolation.md), [SQL query engine](sql-query-engine.md), [Workload isolation](workload-isolation.md), [Workload management](workload-management.md) |
| Related | [Storage and table management](../storage/storage.md), [Processing and transformation](../processing/processing.md), [Platform operations](../platform-operations/platform-operations.md), [Cost management](../platform-operations/cost-management.md), [Platform observability](../platform-operations/platform-observability.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md) |
| Needed by | [Processing and transformation](../processing/processing.md) |

# Where it appears

- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 199 technologies; see their pages.
