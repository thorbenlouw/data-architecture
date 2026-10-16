---
type: Maturity Track
id: track-finops
title: FinOps
description: How well the organisation understands, allocates and controls what the data platform costs, relative to the value it delivers.
covers:
- cost-management
- cost-attribution
- spend-controls
- cost-optimisation
- ai-spend-controls
- sustainability-reporting
- reserved-capacity
- data-product-metering
- cost-forecasting
- interruptible-compute
related_tracks: [track-compute, track-platform-self-service, track-data-products]
levels:
- level: 1
  name: Initial
  summary: Platform cost is a single monthly figure that nobody can break down.
  criteria:
  - Finance sees the platform bill once a month as a single figure.
  - Nobody can say which team or workload caused a cost spike.
  - Idle clusters and forgotten resources are found by accident.
  capabilities: []
- level: 2
  name: Managed
  summary: Resources are tagged, teams have budgets with alerts, and cost reports reach engineers.
  criteria:
  - Resources carry team and environment tags, and untagged spend is reported.
  - Each team or account has a budget with alerts at set thresholds.
  - Engineering teams receive cost reports at least weekly.
  capabilities: [cost-attribution, spend-controls]
- level: 3
  name: Defined
  summary: Spend is attributed to products and workloads by a documented method, with hard limits and a regular savings review.
  criteria:
  - Spend is attributed to teams, data products and workloads, with a documented method for splitting shared compute.
  - Quotas or automatic suspension stop runaway queries and clusters.
  - A monthly review lists idle compute, oversized clusters and unused data, and owners act on it.
  - Model and agent consumption is capped and attributed per user, team or application.
  capabilities: [cost-optimisation, ai-spend-controls]
- level: 4
  name: Measured
  summary: Unit costs are tracked against targets and charged back, commitments are sized from baselines, and carbon is reported alongside cost.
  criteria:
  - Unit costs, such as cost per pipeline run, per query or per thousand predictions, are tracked against targets.
  - Teams are charged or shown their costs monthly from usage data, and each data product's use is metered per consumer so that its cost can be charged back or capped.
  - Reserved and committed capacity is sized from measured baselines, and its coverage and utilisation are reported monthly.
  - Energy use and estimated carbon emissions of workloads are reported alongside cost.
  capabilities: [reserved-capacity, data-product-metering, sustainability-reporting]
- level: 5
  name: Optimising
  summary: Cost is forecast, designed for and linked to the value of the use cases it supports.
  criteria:
  - Spend per team is forecast from usage trends, commitments and planned workloads and compared with actual spend each month, and spend that departs from its expected pattern alerts the owning team within a day.
  - Design reviews for new workloads include cost and carbon estimates, which are checked after launch.
  - Agreed savings actions, such as rightsizing or deleting expired data, are applied automatically within set limits.
  - Spend is linked to the value of the use cases it supports, and low-value workloads are reduced or retired.
  - Fault-tolerant batch and training jobs run on spot or interruptible capacity with checkpointing, and the savings and the share of runs interrupted are reported.
  capabilities: [cost-forecasting, interruptible-compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up lets teams see what their workloads cost within a day, stops runaway spend automatically, and ties spend to the products and use cases it supports. The FinOps Foundation's crawl, walk and run stages correspond roughly to levels 2, 3 to 4 and 5 here, and CDMC key control 14 expects the cost of storing, processing and moving data to be measured and allocated. Sustainability reporting is included because energy and carbon are measured from the same usage data. Typical blockers are untagged resources, shared compute that cannot be split fairly, and cost reports that arrive a month late to people who cannot act on them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Platform cost is a single monthly figure that nobody can break down.

- Finance sees the platform bill once a month as a single figure.
- Nobody can say which team or workload caused a cost spike.
- Idle clusters and forgotten resources are found by accident.

## Level 2: Managed

Resources are tagged, teams have budgets with alerts, and cost reports reach engineers.

- Resources carry team and environment tags, and untagged spend is reported.
- Each team or account has a budget with alerts at set thresholds.
- Engineering teams receive cost reports at least weekly.

**Capabilities first relied on:** [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md)

## Level 3: Defined

Spend is attributed to products and workloads by a documented method, with hard limits and a regular savings review.

- Spend is attributed to teams, data products and workloads, with a documented method for splitting shared compute.
- Quotas or automatic suspension stop runaway queries and clusters.
- A monthly review lists idle compute, oversized clusters and unused data, and owners act on it.
- Model and agent consumption is capped and attributed per user, team or application.

**Capabilities first relied on:** [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md)

## Level 4: Measured

Unit costs are tracked against targets and charged back, commitments are sized from baselines, and carbon is reported alongside cost.

- Unit costs, such as cost per pipeline run, per query or per thousand predictions, are tracked against targets.
- Teams are charged or shown their costs monthly from usage data, and each data product's use is metered per consumer so that its cost can be charged back or capped.
- Reserved and committed capacity is sized from measured baselines, and its coverage and utilisation are reported monthly.
- Energy use and estimated carbon emissions of workloads are reported alongside cost.

**Capabilities first relied on:** [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md)

## Level 5: Optimising

Cost is forecast, designed for and linked to the value of the use cases it supports.

- Spend per team is forecast from usage trends, commitments and planned workloads and compared with actual spend each month, and spend that departs from its expected pattern alerts the owning team within a day.
- Design reviews for new workloads include cost and carbon estimates, which are checked after launch.
- Agreed savings actions, such as rightsizing or deleting expired data, are applied automatically within set limits.
- Spend is linked to the value of the use cases it supports, and low-value workloads are reduced or retired.
- Fault-tolerant batch and training jobs run on spot or interruptible capacity with checkpointing, and the savings and the share of runs interrupted are reported.

**Capabilities first relied on:** [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md)

# Capabilities in scope

[AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Cost management](../capabilities/platform-operations/cost-management.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md), [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md)

# Related tracks

- [Compute and workload management](track-compute.md): How well compute is provisioned, isolated, scaled and tuned so that workloads meet performance targets at a known cost.
- [Platform self-service](track-platform-self-service.md): How far teams can obtain, run and observe what they need on the shared platform without waiting for a central team.
- [Data products](track-data-products.md): How far data is managed as products with accountable owners, known consumers, explicit contracts and service levels.

Levels follow the shared [maturity scale](maturity-scale.md).
