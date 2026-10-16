---
type: Capability
id: cost-management
title: Cost management
description: Understand, allocate and control what the platform costs.
aliases: [FinOps]
broader: [platform-operations]
related: [workload-management, serverless-compute, sustainability-reporting]
depends_on: [system-telemetry]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data platform bill is made up of compute time or consumption units, storage, data transfer between regions and clouds, and charges for managed features such as model calls, serverless services and replication. The capabilities under cost management turn that bill into action. Attribution links spend to teams and workloads; budgets and spend controls set limits and stop runaway jobs; optimisation finds and removes waste; AI spend controls apply the same ideas to model and agent use. Usage telemetry supplies the raw data for all of them.

Consumption pricing makes platforms cheap to start and easy to overspend, because anyone who can run a query can spend money. A FinOps approach shares responsibility: engineers see the cost of what they build, finance sees forecasts and the platform team sets guard rails. Unit costs, such as cost per pipeline run, per dashboard view or per thousand predictions, are more useful than totals because they show whether growth is efficient.

# Key considerations

- Agree a tagging and naming standard before teams start and enforce it at provisioning. Untagged spend cannot be allocated later.
- Billing data often arrives hours or a day late. Controls that must act quickly need usage metrics from the platform itself, not the invoice.
- Include easily missed costs, such as data transfer, storage of old table versions and background maintenance services.
- Weigh commitments against flexibility. Committed-spend discounts help only if usage forecasts are reliable.

# Questions to ask

- Who is accountable for platform spend today, and do teams see their own costs?
- How much does monthly spend vary, and what caused the last surprise bill?
- Which pricing models apply: consumption, reserved capacity, licences or a mix?
- Which unit cost would show the business that the platform is efficient?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [AI usage and spend controls](ai-spend-controls.md), [Budgets and spend controls](spend-controls.md), [Cost attribution and chargeback](cost-attribution.md), [Cost optimisation](cost-optimisation.md), [Reserved and committed capacity](../compute/reserved-capacity.md), [Spend forecasting and anomaly detection](cost-forecasting.md), [Spot and interruptible compute](../compute/interruptible-compute.md) |
| Related | [Query and compute](../compute/compute.md), [Compute provisioning options](../compute/compute-options.md), [Serverless compute](../compute/serverless-compute.md), [Sustainability and carbon management](sustainability-reporting.md), [Workload management](../compute/workload-management.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md) |

# Where it appears

- **Personas:** [Chief data officer](../../personas/persona-cdo.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Cost Explorer](../../technologies/aws/aws-cost-explorer.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Governance Hub](../../technologies/databricks/databricks-governance-hub.md) (preview) |

Narrower capabilities are realised by a further 58 technologies; see their pages.
