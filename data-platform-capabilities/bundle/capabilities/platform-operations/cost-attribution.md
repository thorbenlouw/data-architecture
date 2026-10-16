---
type: Capability
id: cost-attribution
title: Cost attribution and chargeback
description: Attribute spend to teams, products and workloads using tags and usage data.
aliases: [showback, chargeback]
broader: [cost-management]
related: [multi-tenancy, usage-metadata, data-products, workload-isolation, spend-controls]
depends_on: [system-telemetry]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some spend is simple to assign: a cluster tagged `team=fraud` belongs to the fraud team. Shared resources need a published rule, such as splitting a shared warehouse by each team's share of query time, allocating storage by the schemas each team owns, or spreading the central team's tooling evenly. Usage records such as query history are joined with billing data and tags to report cost by owner and period, then divided by business volumes to give unit costs, such as cost per pipeline run or per thousand predictions. Showback reports costs to teams; chargeback bills them against internal budgets.

Attribution changes behaviour: teams that see their own spend turn off idle compute and question expensive jobs. Most estates combine bills from several clouds, data platforms and model providers, each with its own units and columns. The FinOps Open Cost and Usage Specification (FOCUS) defines a common schema for billing data, which makes those sources easier to combine. Keep allocation rules simple, because people dispute charges they cannot follow.

# Key considerations

- Enforce tags at creation through policies or templates. Adding tags to running resources afterwards is slow and incomplete.
- Dedicated compute per team is easy to attribute but can cost more in total than shared compute.
- Decide whether producers or consumers pay for shared data products, and how storage and refresh costs are split.
- Reconcile attributed totals with the invoice regularly, so reports stay credible.

# Questions to ask

- Must costs be charged to budgets, or is showing them to teams enough?
- What should costs be reported by: team, domain, data product, project or customer?
- How much current spend runs on shared compute that is hard to attribute?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Cost management](cost-management.md) |
| Related | [Data products](../data-products/data-products.md), [Budgets and spend controls](spend-controls.md), [Cross-region and cross-cloud sharing](../data-sharing/cross-region-sharing.md), [Data domains](../governance/data-domains.md), [Data product usage metering](../data-products/data-product-metering.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Multi-tenancy and workspace isolation](multi-tenancy.md), [Reserved and committed capacity](../compute/reserved-capacity.md), [Serverless compute](../compute/serverless-compute.md), [Sustainability and carbon management](sustainability-reporting.md), [Usage and popularity metadata](../metadata/usage-metadata.md), [Workload isolation](../compute/workload-isolation.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md) |
| Needed by | [Spend forecasting and anomaly detection](cost-forecasting.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 3) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 2)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data platform engineer](../../personas/persona-platform-engineer.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 14 Cost Metrics (Data and technical architecture) · [DCAM v3](../../frameworks/framework-edm-dcam.md): 2 Data Management Program & Funding · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 3 – Benefits and costs · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Pricing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Cost allocation tags and cost categories | [AWS Cost Explorer](../../technologies/aws/aws-cost-explorer.md), [AWS Data Exports](../../technologies/aws/aws-data-exports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Cost Management](../../technologies/microsoft/azure-cost-management.md), [Microsoft Fabric Capacity Metrics app](../../technologies/microsoft/fabric-capacity-metrics-app.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery INFORMATION_SCHEMA views](../../technologies/google-cloud/gcp-bigquery-information-schema.md), [Google Cloud Billing](../../technologies/google-cloud/gcp-cloud-billing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../../technologies/snowflake/snowflake-account-usage.md), [Snowflake budgets](../../technologies/snowflake/snowflake-budgets.md), [Snowflake Cortex AI Gateway](../../technologies/snowflake/snowflake-cortex-ai-gateway.md) (preview), [Snowflake object tagging](../../technologies/snowflake/snowflake-object-tagging.md) |
| [Databricks](../../platforms/platform-databricks.md) | Serverless usage policies and tags | [Databricks budgets](../../technologies/databricks/databricks-budgets.md), [Databricks serverless usage policies](../../technologies/databricks/databricks-serverless-usage-policies.md) (preview), [Databricks system tables](../../technologies/databricks/databricks-system-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud usage breakdown and spend alerts](../../technologies/clickhouse/clickhouse-cost-controls.md) |
| [Informatica](../../platforms/platform-informatica.md) | IPU consumption metering | [Informatica Processing Unit (IPU) consumption pricing](../../technologies/informatica/informatica-ipu-pricing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Observability](../../technologies/cloudera/cloudera-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Resource Management](../../technologies/palantir/palantir-resource-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Dagster+](../../technologies/independent/dagster-plus.md) |
