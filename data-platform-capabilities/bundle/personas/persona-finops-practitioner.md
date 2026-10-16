---
type: Persona
id: persona-finops-practitioner
title: FinOps practitioner
description: Tracks, allocates and optimises what the data platform costs.
cares_about:
- cost-attribution
- system-telemetry
- cost-forecasting
- spend-controls
- cost-optimisation
- reserved-capacity
- ai-spend-controls
- compute-options
- serverless-compute
- provisioned-compute
- interruptible-compute
- workload-management
- workload-isolation
- query-performance-analysis
- elastic-scaling
- data-product-metering
- storage-tiering
- usage-metadata
- configuration-guardrails
- multi-tenancy
- sustainability-reporting
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

FinOps practitioners sit in a cloud FinOps or finance team serving many platforms, or are embedded in the data platform team. They combine billing data with usage telemetry to show who spends what, forecast spend, negotiate commitments and work with engineers on savings. Consumption pricing makes data platforms harder to manage than most: one inefficient query, an always-on cluster or a burst of AI usage can move the monthly bill.

Success is spend that is fully attributed, forecast within an agreed margin and expressed as unit costs the business understands, such as cost per report refresh, per pipeline run or per thousand predictions.

# Goals

- Attribute all platform spend to teams, products or use cases.
- Forecast spend accurately and avoid surprises.
- Remove waste without breaching service levels.
- Express cost as unit economics that business owners understand.

# Jobs

- Build and maintain cost reports from billing and usage telemetry.
- Enforce tagging and allocation rules, and run showback or chargeback.
- Set budgets, quotas and alerts, and investigate anomalies in spend.
- Find idle, oversized or redundant resources and track the savings made.
- Plan and buy reserved capacity and spending commitments.
- Track and cap model and agent consumption.
- Forecast spend per team and for the platform each month, and explain the variance from actuals.
- Review cost estimates in design reviews for new workloads, and check them after launch.
- Combine billing data from clouds, data platforms and model providers into one attributed cost dataset.

# Pain points

- Shared compute and serverless charges are hard to split fairly.
- Tags are missing or applied inconsistently.
- AI token costs are spread across many teams, applications and providers.
- Engineers see costs weeks after the decisions that caused them.
- Billing data from each provider arrives in different formats, units and delays, so combining it takes manual work.

# Questions they ask

- How do we attribute the cost of shared warehouses and clusters fairly?
- When do reserved commitments beat on-demand pricing for our workloads?
- Which controls stop runaway spend automatically, and what do they break when they trigger?
- Which unit cost measures should each data product report?
- Which workloads can run on interruptible capacity, and what do reclaimed nodes cost in reruns?
- How do we detect a spend anomaly within a day rather than at month end?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Attribute spend to teams, products and workloads using tags and usage data. |
| [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Expose platform usage, billing and operational data as queryable tables. |
| [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Set budgets, quotas and alerts, and stop runaway spend automatically. |
| [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Find and act on savings such as idle compute, oversized clusters and unused data. |
| [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md) | [Query and compute](../capabilities/compute/compute.md) | Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Limit, prioritise and attribute model and agent consumption per user, team or application. |
| [Compute provisioning options](../capabilities/compute/compute-options.md) | [Query and compute](../capabilities/compute/compute.md) | Choose how compute is supplied, from serverless capacity to clusters you size and control. |
| [Serverless compute](../capabilities/compute/serverless-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Run workloads without managing servers, with capacity allocated on demand and billed by use. |
| [Provisioned compute](../capabilities/compute/provisioned-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Run workloads on clusters or warehouses you size and control, for predictable performance and cost. |
| [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice. |
| [Workload management](../capabilities/compute/workload-management.md) | [Query and compute](../capabilities/compute/compute.md) | Prioritise, queue and limit queries and jobs so the most important work meets its service levels. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | Run different workloads on separate compute so one cannot slow or starve another. |
| [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Inspect query plans, job stages, run history and bottlenecks to tune performance and cost. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | [Query and compute](../capabilities/compute/compute.md) | Add and remove compute automatically as load changes, including for bursts of concurrent users. |
| [Data product usage metering](../capabilities/data-products/data-product-metering.md) | [Data products](../capabilities/data-products/data-products.md) | Measure how much each consumer uses a data product so it can be billed, charged back or capped. |
| [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) | [Storage and table management](../capabilities/storage/storage.md) | Move data between hot, cool and archive tiers automatically based on age or access patterns. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show who uses which data, how often and how, to guide discovery and clean-up. |
| [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules. |
| [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations. |
| [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Measure and reduce the carbon emissions and energy use of data workloads. |

# Use cases they take part in

- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Platform cost management and chargeback](../use-cases/usecase-platform-cost-management.md): Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
