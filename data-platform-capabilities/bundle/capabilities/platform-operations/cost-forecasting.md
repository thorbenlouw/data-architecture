---
type: Capability
id: cost-forecasting
title: Spend forecasting and anomaly detection
description: Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.
aliases: [cost forecasting, cost anomaly detection, spend anomalies, budget forecasting, cost estimation]
broader: [cost-management]
related: [reserved-capacity, spend-controls, data-anomaly-detection, platform-migration]
depends_on: [system-telemetry, cost-attribution]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Forecasting turns past usage into an expected bill. Daily spend per team, service and workload is projected forward, adjusted for seasonal peaks such as month-end close, for known changes such as a migration wave, and for commitments already bought. Estimates for planned work, such as the bytes a query plan will scan or the cost of a new cluster definition, extend this to workloads that have not yet run. Anomaly detection compares actual spend with the expected pattern and alerts when, for example, one warehouse's daily credits triple on a Tuesday.

Budgets with fixed thresholds catch overspend only after it has happened, often late in the month. Forecasts show weeks ahead that a team will exceed its budget, and anomaly alerts catch a runaway job within a day. Forecasts also size commitments and test business cases. Spend controls act on limits; this capability predicts where spend is heading and spots the unexpected. It needs daily, attributed usage data, because monthly invoices are too coarse.

# Key considerations

- Forecast at the level people manage budgets, such as team or data product, not only for the whole account.
- Anomaly models flag every launch and month-end unless told about expected changes. Feed in planned events and tune sensitivity per scope.
- Send each anomaly to the owning team with the resources and queries behind it, or it is noted and ignored.
- Compare forecasts with actual spend each month and record the error, so people know how far to trust them.

# Questions to ask

- How far ahead must spend be forecast, and how accurately, for budgeting and commitment decisions?
- How long did the last unexpected cost spike run before someone noticed?
- Do design reviews for new workloads include a cost estimate, and is it checked after launch?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Cost management](cost-management.md) |
| Related | [Budgets and spend controls](spend-controls.md), [Data anomaly detection](../data-quality/data-anomaly-detection.md), [Platform migration](platform-migration.md), [Reserved and committed capacity](../compute/reserved-capacity.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md), [Cost attribution and chargeback](cost-attribution.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 5, Optimising)
- **Frameworks:** [DCAM v3](../../frameworks/framework-edm-dcam.md): 2 Data Management Program & Funding

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Cost Explorer](../../technologies/aws/aws-cost-explorer.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Cost Management](../../technologies/microsoft/azure-cost-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Billing](../../technologies/google-cloud/gcp-cloud-billing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake budgets](../../technologies/snowflake/snowflake-budgets.md), [Snowflake cost anomaly detection](../../technologies/snowflake/snowflake-cost-anomaly-detection.md) |
