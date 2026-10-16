---
type: Use Case
id: usecase-platform-cost-management
title: Platform cost management and chargeback
description: Attribute, forecast and control what the data platform costs, and recover it from the teams and products that use it.
requires:
- {capability: system-telemetry, level: 3, why: 'Usage, billing and query history must be queryable daily for every service, not read from monthly invoices.'}
- {capability: cost-attribution, level: 3, why: 'Every cost needs an owner, with a documented rule for splitting shared warehouses, clusters and storage.'}
- {capability: spend-controls, level: 3, why: 'Budgets, quotas and automatic suspension stop runaway queries and idle clusters within minutes.'}
- {capability: cost-forecasting, level: 2, why: 'Spend per team must be projected ahead of budget cycles, and anomalies flagged within a day.'}
- {capability: cost-optimisation, level: 2, why: 'Idle, oversized and unused resources are found regularly and their owners act on them.'}
- {capability: reserved-capacity, level: 2, why: 'Commitments must be sized from measured base load, and their utilisation tracked.'}
- {capability: configuration-guardrails, level: 2, why: Mandatory cost tags and approved compute sizes are enforced when resources are created.}
- capability: ai-spend-controls
  level: 2
  why: Model and agent calls are attributed and capped per application, because they are often billed outside normal compute.
- capability: workload-isolation
  level: 2
  why: Separate compute for the main workloads keeps attribution simple and stops one team's usage hiding inside another's.
benefits_from:
- {capability: data-product-metering, why: Charges consumers of shared data products by their use rather than by headcount.}
- {capability: query-performance-analysis, why: Finds the few queries and jobs that cause most of the compute spend.}
- {capability: storage-tiering, why: Moves rarely read history to cheaper storage tiers.}
- {capability: interruptible-compute, why: Cuts the cost of fault-tolerant batch and training work.}
- {capability: usage-metadata, why: 'Shows which tables and dashboards nobody uses, so they can be retired.'}
- {capability: self-service-provisioning, why: 'Templates apply tags, budgets and approved sizes to every new workspace.'}
- {capability: workload-management, why: Caps and queues ad hoc work on shared compute.}
- {capability: sustainability-reporting, why: Reports carbon alongside cost from the same usage data.}
personas:
- persona-finops-practitioner
- persona-platform-engineer
- persona-data-engineer
- persona-analytics-engineer
- persona-data-product-owner
- persona-cdo
patterns: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Consumption pricing means every query, pipeline run, cluster hour and model call adds to the bill, and spend grows with adoption whether or not value does. Finance asks what the platform costs per business unit and why the bill moved; engineering leads ask which of their workloads drive it. Cost management combines billing exports and usage telemetry from every cloud, data platform and model provider. It attributes spend to teams, data products and workloads using tags and published rules for shared compute, sets budgets and automatic limits, forecasts spend and commitments, and runs a regular savings routine with the owners of the costliest workloads.

Good looks like nearly all spend attributed to an owner within a day, teams seeing their own costs and unit costs such as cost per pipeline run or per thousand predictions, and overruns forecast weeks ahead rather than found at month end. Commitments are sized from measured use, savings are tracked as realised rather than estimated, and nobody is surprised by the invoice.

# Non-functional requirements

- At least 95 per cent of monthly spend is attributed to a named owner.
- Each team can see the previous day's spend by the start of the next working day.
- Runaway workloads in non-production environments are stopped within minutes of crossing a limit.
- Monthly forecasts per team fall within an agreed margin, such as ten per cent, of actual spend.
- Attributed totals reconcile with provider invoices each month.

# Risks

- Hard limits stop a critical production job during month-end close.
- Allocation rules for shared compute are disputed, and teams stop trusting the reports.
- Model and agent spend through separate provider accounts is missed entirely.
- Savings work targets small items while a few expensive workloads go unreviewed.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Usage, billing and query history must be queryable daily for every service, not read from monthly invoices. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Every cost needs an owner, with a documented rule for splitting shared warehouses, clusters and storage. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Budgets, quotas and automatic suspension stop runaway queries and idle clusters within minutes. |
| [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Spend per team must be projected ahead of budget cycles, and anomalies flagged within a day. |
| [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Idle, oversized and unused resources are found regularly and their owners act on them. |
| [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Commitments must be sized from measured base load, and their utilisation tracked. |
| [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Mandatory cost tags and approved compute sizes are enforced when resources are created. |
| [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Model and agent calls are attributed and capped per application, because they are often billed outside normal compute. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Separate compute for the main workloads keeps attribution simple and stops one team's usage hiding inside another's. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Data product usage metering](../capabilities/data-products/data-product-metering.md) | Charges consumers of shared data products by their use rather than by headcount. |
| [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) | Finds the few queries and jobs that cause most of the compute spend. |
| [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md) | Moves rarely read history to cheaper storage tiers. |
| [Spot and interruptible compute](../capabilities/compute/interruptible-compute.md) | Cuts the cost of fault-tolerant batch and training work. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | Shows which tables and dashboards nobody uses, so they can be retired. |
| [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md) | Templates apply tags, budgets and approved sizes to every new workspace. |
| [Workload management](../capabilities/compute/workload-management.md) | Caps and queues ad hoc work on shared compute. |
| [Sustainability and carbon management](../capabilities/platform-operations/sustainability-reporting.md) | Reports carbon alongside cost from the same usage data. |

# Personas

- [FinOps practitioner](../personas/persona-finops-practitioner.md): Tracks, allocates and optimises what the data platform costs.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.
- [Chief data officer](../personas/persona-cdo.md): Accountable for the organisation's data strategy, value, risk and governance.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 9 of 9 |  |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 9 of 9 |  |
| [Google Cloud](../platforms/platform-google-cloud.md) | 9 of 9 |  |
| [Snowflake](../platforms/platform-snowflake.md) | 6 of 9 | [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 9 | [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 5 of 9 | [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Informatica](../platforms/platform-informatica.md) | 3 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 3 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [Oracle](../platforms/platform-oracle.md) | 1 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [SAP](../platforms/platform-sap.md) | 0 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Teradata](../platforms/platform-teradata.md) | 1 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md) |
| [IBM](../platforms/platform-ibm.md) | 0 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [AI usage and spend controls](../capabilities/platform-operations/ai-spend-controls.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 9 | [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Workload isolation](../capabilities/compute/workload-isolation.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 3 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md) |
| [Independent vendors](../platforms/platform-independent.md) | 3 of 9 | [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Cost optimisation](../capabilities/platform-operations/cost-optimisation.md), [Reserved and committed capacity](../capabilities/compute/reserved-capacity.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) |
