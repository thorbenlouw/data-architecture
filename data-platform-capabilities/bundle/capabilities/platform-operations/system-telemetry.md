---
type: Capability
id: system-telemetry
title: Usage and system telemetry
description: Expose platform usage, billing and operational data as queryable tables.
aliases: [system tables, account usage views]
broader: [platform-observability]
related: [usage-metadata, audit-logging, cost-optimisation, metadata-harvesting, query-performance-analysis]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical system tables or views cover query history, job and task runs, compute and billing usage, storage per table, logins, permission grants, lineage and access events. Because they are queryable with SQL, one query can join billing usage to job runs and tags to show last month's cost per team, and another can list every table nobody has read for ninety days. These tables are usually read-only, refreshed with some delay and kept for a fixed period set by the platform.

System telemetry is the raw material for cost attribution and optimisation, usage metadata, audit reports and custom monitoring. Having it as tables rather than only in a console means teams can build their own dashboards, alerts and automated checks, and combine platform data with business data. Coverage, latency and retention vary between services, so many organisations copy the tables into their own storage on a schedule to keep longer history. Audit logging focuses on tamper-evident security records; telemetry covers the wider operational and usage picture.

# Key considerations

- Check the retention period of each table. If it is shorter than you need for trends or audit, copy the data on a schedule.
- Latency ranges from minutes to a day across tables. Do not base time-critical controls on telemetry that arrives late.
- Telemetry reveals who queried what, and sometimes query text. Treat it as sensitive and restrict access.
- System table schemas change between platform releases. Build reports on documented columns and test them after upgrades.

# Questions to ask

- Which operational questions must you answer with SQL: cost, usage, access or performance?
- How long must usage and access history be kept?
- Do you need to combine telemetry across several platforms or accounts?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform observability](platform-observability.md) |
| Related | [Audit logging](../security/audit-logging.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Cost optimisation](cost-optimisation.md), [Governance coverage metrics](../governance/governance-metrics.md), [Metadata harvesting](../metadata/metadata-harvesting.md), [Query and job performance analysis](query-performance-analysis.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |
| Needed by | [Budgets and spend controls](spend-controls.md), [Cost attribution and chargeback](cost-attribution.md), [Cost management](cost-management.md), [Cost optimisation](cost-optimisation.md), [Data product usage metering](../data-products/data-product-metering.md), [Spend forecasting and anomaly detection](cost-forecasting.md), [Sustainability and carbon management](sustainability-reporting.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 14 Cost Metrics (Data and technical architecture)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Data Exports (CUR 2.0, FOCUS) | [Amazon S3 Metadata](../../technologies/aws/aws-s3-metadata.md), [AWS Data Exports](../../technologies/aws/aws-data-exports.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Capacity Metrics app; workspace monitoring | [Azure Monitor](../../technologies/microsoft/azure-monitor.md), [Fabric workspace monitoring](../../technologies/microsoft/fabric-workspace-monitoring.md) (preview), [Microsoft Fabric Capacity Metrics app](../../technologies/microsoft/fabric-capacity-metrics-app.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | INFORMATION_SCHEMA views | [BigQuery INFORMATION_SCHEMA views](../../technologies/google-cloud/gcp-bigquery-information-schema.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | ACCOUNT_USAGE and ORGANIZATION_USAGE schemas | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../../technologies/snowflake/snowflake-account-usage.md) |
| [Databricks](../../platforms/platform-databricks.md) | System tables | [Databricks system tables](../../technologies/databricks/databricks-system-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Query Insights and system tables](../../technologies/clickhouse/clickhouse-cloud-monitoring.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Resource Management](../../technologies/palantir/palantir-resource-management.md) |
