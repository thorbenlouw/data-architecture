---
type: Capability
id: spend-controls
title: Budgets and spend controls
description: Set budgets, quotas and alerts, and stop runaway spend automatically.
aliases: [resource monitors, quotas]
broader: [cost-management]
related:
- workload-management
- cost-attribution
- elastic-scaling
- self-service-provisioning
- ai-spend-controls
depends_on: [system-telemetry]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

These controls act before money is spent rather than reporting it afterwards. Budgets assign an amount per month to a team, project or account, with alerts at thresholds such as 50%, 80% and 100%. Quotas limit what a team can use, such as the largest cluster size or the number of concurrent warehouses. Automatic actions go further: suspend compute when its spending limit is reached, cancel queries that run longer than an hour or scan more than a set volume, and shut down clusters idle for twenty minutes. Policies can block oversized compute from being created at all.

Runaway spend usually has a few causes: an accidental cross join, a job stuck retrying, a cluster left on over a weekend, or a dashboard refreshing every minute. Controls catch these within minutes rather than at month end. Hard stops can halt important work, so production usually gets alerts and soft limits while sandboxes get hard ones. Workload management decides which work runs first; spend controls cap what it can cost.

# Key considerations

- Match the action to the environment. Hard stops suit sandboxes and development; production needs alerts and escalation, not silent suspension.
- Budgets based on billing data react slowly. Use limits enforced by the platform itself for anything that must act within minutes.
- Send alerts to the team that owns the spend, with enough detail to act, not only to a central finance mailbox.
- Review limits regularly. Limits set too low get raised by hand and then forgotten.

# Questions to ask

- What was the most expensive accidental workload in the past year, and how long did it run before anyone noticed?
- Which workloads must never be stopped automatically?
- Who may raise a budget or quota, and how quickly?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Cost management](cost-management.md) |
| Related | [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [AI usage and spend controls](ai-spend-controls.md), [Cost attribution and chargeback](cost-attribution.md), [Data product usage metering](../data-products/data-product-metering.md), [Elastic scaling](../compute/elastic-scaling.md), [Reserved and committed capacity](../compute/reserved-capacity.md), [Resource configuration guardrails](configuration-guardrails.md), [Self-service provisioning](self-service-provisioning.md), [Serverless compute](../compute/serverless-compute.md), [Spend forecasting and anomaly detection](cost-forecasting.md), [Workload management](../compute/workload-management.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md) |
| Needed by | [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Budgets actions | [AWS Budgets](../../technologies/aws/aws-budgets.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Cost Management](../../technologies/microsoft/azure-cost-management.md), [Microsoft Fabric capacities (F SKUs)](../../technologies/microsoft/fabric-capacities.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery workload management](../../technologies/google-cloud/gcp-bigquery-workload-management.md), [Google Cloud Billing](../../technologies/google-cloud/gcp-cloud-billing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | resource monitors, budgets and per-user quotas | [Snowflake budgets](../../technologies/snowflake/snowflake-budgets.md), [Snowflake cost anomaly detection](../../technologies/snowflake/snowflake-cost-anomaly-detection.md), [Snowflake resource monitors](../../technologies/snowflake/snowflake-resource-monitors.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks budgets](../../technologies/databricks/databricks-budgets.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../../technologies/clickhouse/clickhouse-access-control.md), [ClickHouse Cloud usage breakdown and spend alerts](../../technologies/clickhouse/clickhouse-cost-controls.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Resource Management](../../technologies/palantir/palantir-resource-management.md) |
