---
type: Use Case
id: usecase-customer-facing-analytics
title: Customer-facing analytics
description: Give external customers fast, secure analytics inside a product.
aliases: [embedded analytics, in-product analytics]
requires:
- {capability: embedded-analytics, level: 3, why: 'Charts and tables are rendered inside the product, styled and secured for external users.'}
- {capability: real-time-analytics, level: 3, why: Thousands of concurrent customers expect sub-second queries over fresh data.}
- {capability: row-level-security, level: 4, why: 'Tenant isolation must be automated and tested continuously, because one leak is a breach of contract.'}
- {capability: incremental-processing, level: 2, why: New events are applied continuously without rebuilding every customer's aggregates.}
- {capability: elastic-scaling, level: 3, why: Load follows customer working hours and product launches.}
- {capability: workload-isolation, level: 3, why: Customer queries must not compete with internal analytics or pipelines.}
- {capability: freshness-monitoring, level: 3, why: 'Customers notice stale figures, so delays must be caught before they are.'}
- {capability: query-performance-analysis, level: 3, why: Latency targets are tracked and slow query patterns fixed as the largest customers grow.}
- capability: external-identity
  level: 3
  why: Customers and their tenants come from the product's identity system, and the tenant must be passed securely into every query.
- {capability: read-optimised-views, level: 3, why: 'Per-customer aggregates are built in the shape screens read them, so pages load in about a second at peak.'}
benefits_from:
- {capability: metric-definitions, why: Keeps customer-facing figures consistent with billing and other product screens.}
- {capability: data-apis, why: Lets customers pull the same data into their own systems.}
- {capability: external-data-sharing, why: Gives large customers live access to their data instead of exports.}
- {capability: data-export, why: Lets customers download their data in bulk.}
- {capability: result-caching, why: Serves repeated dashboard loads cheaply.}
- {capability: cost-attribution, why: Shows the cost to serve each customer for pricing decisions.}
- {capability: data-residency, why: Keeps each customer's data in the region their contract requires.}
- {capability: cross-region-failover, why: Supports product availability commitments.}
- {capability: dashboards-as-code, why: Releases analytics screens through the same review and test process as the rest of the product.}
- {capability: materialised-views, why: Lets the engine keep per-customer aggregates current without separate refresh jobs.}
- {capability: data-slas, why: Freshness and availability targets match what the product promises its customers.}
personas:
- persona-software-engineer
- persona-data-product-owner
- persona-platform-engineer
- persona-data-engineer
- persona-analytics-engineer
- persona-security-officer
patterns: [cqrs-read-models, one-big-table, kappa-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Software and service companies increasingly give their customers analytics inside the product: usage dashboards, spend reports, performance benchmarks, delivery tracking. Unlike internal BI, the audience is large and external, expects consumer-grade speed and is paying for the feature. Product events and transactions are loaded continuously, pre-aggregated per customer, and served by an engine built for many fast, concurrent queries, with every query restricted to the requesting customer's data.

Good looks like pages that load in about a second at peak, no possibility of one customer seeing another's data, figures consistent with what the customer sees elsewhere in the product such as invoices, and a cost per customer low enough for the feature to be priced profitably.

# Non-functional requirements

- 95th-percentile query latency under one second at peak concurrency of thousands of users.
- Tenant isolation is covered by automated tests on every release.
- Availability matches the product's own service level, often 99.9 per cent or higher.
- Data is seconds to minutes old, as stated in the product.
- Cost per customer is measured and fits the pricing model.

# Risks

- A filtering or caching bug shows one customer another customer's data.
- Costs grow faster than revenue as usage rises.
- The largest customers outgrow the design and their dashboards slow down.
- Figures disagree with invoices or other screens and generate support tickets.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Charts and tables are rendered inside the product, styled and secured for external users. |
| [Real-time analytical database](../capabilities/compute/real-time-analytics.md) | [Query and compute](../capabilities/compute/compute.md) | 3 (Defined) | Thousands of concurrent customers expect sub-second queries over fresh data. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 4 (Measured) | Tenant isolation must be automated and tested continuously, because one leak is a breach of contract. |
| [Incremental processing](../capabilities/processing/incremental-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | New events are applied continuously without rebuilding every customer's aggregates. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | [Query and compute](../capabilities/compute/compute.md) | 3 (Defined) | Load follows customer working hours and product launches. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | 3 (Defined) | Customer queries must not compete with internal analytics or pipelines. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Customers notice stale figures, so delays must be caught before they are. |
| [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Latency targets are tracked and slow query patterns fixed as the largest customers grow. |
| [External user and tenant identity](../capabilities/security/external-identity.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Customers and their tenants come from the product's identity system, and the tenant must be passed securely into every query. |
| [Read-optimised views](../capabilities/serving/read-optimised-views.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Per-customer aggregates are built in the shape screens read them, so pages load in about a second at peak. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | Keeps customer-facing figures consistent with billing and other product screens. |
| [Data APIs](../capabilities/serving/data-apis.md) | Lets customers pull the same data into their own systems. |
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | Gives large customers live access to their data instead of exports. |
| [Data export](../capabilities/serving/data-export.md) | Lets customers download their data in bulk. |
| [Result caching](../capabilities/compute/result-caching.md) | Serves repeated dashboard loads cheaply. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | Shows the cost to serve each customer for pricing decisions. |
| [Data residency and sovereignty](../capabilities/governance/data-residency.md) | Keeps each customer's data in the region their contract requires. |
| [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) | Supports product availability commitments. |
| [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md) | Releases analytics screens through the same review and test process as the rest of the product. |
| [Materialised views](../capabilities/compute/materialised-views.md) | Lets the engine keep per-customer aggregates current without separate refresh jobs. |
| [Data service levels](../capabilities/data-products/data-slas.md) | Freshness and availability targets match what the product promises its customers. |

# Personas

- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.

# Patterns

- [Separate read models](../patterns/cqrs-read-models.md)
- [One big table](../patterns/one-big-table.md)
- [Kappa architecture](../patterns/kappa-architecture.md)

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 9 of 10 | [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 8 of 10 (+1 in preview) | [Read-optimised views](../capabilities/serving/read-optimised-views.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) (preview only) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 7 of 10 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 8 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [External user and tenant identity](../capabilities/security/external-identity.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 10 (+1 in preview) | [External user and tenant identity](../capabilities/security/external-identity.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md) (preview only) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 6 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Informatica](../platforms/platform-informatica.md) | 3 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 5 of 10 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Oracle](../platforms/platform-oracle.md) | 3 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [SAP](../platforms/platform-sap.md) | 2 of 10 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Teradata](../platforms/platform-teradata.md) | 4 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [IBM](../platforms/platform-ibm.md) | 1 of 10 | [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Row-level security](../capabilities/security/row-level-security.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 10 | [Real-time analytical database](../capabilities/compute/real-time-analytics.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 8 of 10 | [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md) |
| [Independent vendors](../platforms/platform-independent.md) | 6 of 10 | [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Read-optimised views](../capabilities/serving/read-optimised-views.md) |
