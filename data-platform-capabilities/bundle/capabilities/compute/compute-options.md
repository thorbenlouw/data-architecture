---
type: Capability
id: compute-options
title: Compute provisioning options
description: Choose how compute is supplied, from serverless capacity to clusters you size and control.
aliases: [compute types, compute models, job compute, interactive compute]
broader: [compute]
related:
- single-node-processing
- distributed-processing
- workload-isolation
- elastic-scaling
- cost-management
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Two choices decide how a workload gets compute. The first is how capacity is supplied and paid for: serverless capacity allocated per query or job and billed by use, provisioned clusters or warehouses that you size and pay for while they run, capacity reserved in advance at a discount, and spot capacity that is cheap but can be reclaimed. The second is the shape of the capacity: one machine running an in-process engine or a distributed cluster, CPUs or GPUs, and interactive compute shared by people or job compute started for one scheduled run.

Choose per workload, not once for the platform. Spiky ad hoc queries usually suit serverless. Steady hourly transformation is often cheaper on provisioned or reserved capacity. Many pipelines under a few hundred gigabytes run faster and cheaper on one node than on a cluster. Scheduled jobs on interactive compute are a common waste, since it stays on between uses and often costs more per unit. The choice also affects start-up delay, isolation and cost attribution.

# Key considerations

- Compare unit costs at your real utilisation, not list prices. A provisioned cluster running at 20 per cent load is often dearer than serverless.
- Start-up time ranges from seconds to several minutes. Interactive users cannot wait for a cluster to boot.
- Options may differ in networking, security and features. Check private connectivity and governance support on each.
- Let workloads move between options as they mature without rewriting code.

# Questions to ask

- Which workloads run steadily, and which are bursty or unpredictable?
- How sensitive are users to start-up delays?
- Can the organisation commit to a level of spend in advance?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Narrower | [Container services](container-services.md), [GPU and accelerated compute](gpu-compute.md), [Provisioned compute](provisioned-compute.md), [Reserved and committed capacity](reserved-capacity.md), [Serverless compute](serverless-compute.md), [Spot and interruptible compute](interruptible-compute.md) |
| Related | [Cost management](../platform-operations/cost-management.md), [Distributed processing](../processing/distributed-processing.md), [Elastic scaling](elastic-scaling.md), [Single-node processing](../processing/single-node-processing.md), [Workload isolation](workload-isolation.md) |
| Needed by | [Distributed processing](../processing/distributed-processing.md), [Notebooks](../development-lifecycle/notebooks.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 2, Managed)
- **Frameworks:** [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.4 – Resources for AI systems · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 2 – Automated training

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 68 technologies; see their pages.
